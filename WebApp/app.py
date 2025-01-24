from flask import Flask,flash, render_template, request, redirect, url_for, send_file
from flask_bootstrap import Bootstrap5
import os
from werkzeug.utils import secure_filename
import pandas as pd
from pathlib import Path
import app_logic.uic_vw_transitions_housingtype as applogic
import pandas as pd
import importlib.util
import re
import nbformat
from nbconvert import PythonExporter
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Set up directory paths using environment variables or default values
current_dir = Path(__file__).parent
upload_relative_path = Path(os.getenv("UPLOAD_FOLDER", "./uploads"))
processed_relative_path = Path(os.getenv("PROCESSED_FOLDER", "./processed"))
script_relative_path = Path(os.getenv("SCRIPT_FOLDER", "../GoodScript_Lower_Case"))
app_logic_relative_path = Path(os.getenv("APP_LOGIC_FOLDER", "./app_logic"))

UPLOAD_FOLDER = current_dir / upload_relative_path
PROCESSED_FOLDER = current_dir / processed_relative_path
SCRIPT_FOLDER = current_dir / script_relative_path
APP_LOGIC = current_dir / app_logic_relative_path

# Load other environment variables
SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret-key")
ALLOWED_EXTENSIONS = set(os.getenv("ALLOWED_EXTENSIONS", "txt,xlsx,xls,csv").split(','))

# Ensure the required folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

app = Flask(__name__)

# Configure the Flask app
app.config['SECRET_KEY'] = SECRET_KEY
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

bootstrap = Bootstrap5(app)

# Global variables to store selected process and uploaded file
UPLOADED_FILE_NAME = None
SELECTED_PROCESS_NAME = None


# Convert all existing .ipynb to .py 
def convert_notebooks_to_scripts(source_folder):
    """
    Converts all .ipynb files in the given folder to .py files,
    renames them to lowercase, and saves them in the same location.

    Args:
        source_folder (str): Path to the folder containing .ipynb files.
    """
    source_path = Path(source_folder)
    if not source_path.exists():
        print(f"Error: The folder '{source_folder}' does not exist.")
        return

    for notebook_file in source_path.glob("*.ipynb"):
        try:
            # Read the notebook
            with open(notebook_file, 'r', encoding='utf-8') as f:
                notebook_content = nbformat.read(f, as_version=4)

            # Convert notebook to Python script
            python_exporter = PythonExporter()
            script_content, _ = python_exporter.from_notebook_node(notebook_content)

            # Create new file name in lowercase with .py extension
            new_filename = notebook_file.stem.lower() + ".py"
            new_script_path = source_path / new_filename

            # Save the converted Python script
            with open(new_script_path, 'w', encoding='utf-8') as f:
                f.write(script_content)
            
            print(f"Converted: {notebook_file.name} -> {new_filename}")

            # Optionally, remove the original .ipynb file (uncomment if needed)
            # notebook_file.unlink()

        except Exception as e:
            print(f"Failed to convert {notebook_file.name}: {e}")

    print("Conversion process completed.")

convert_notebooks_to_scripts(SCRIPT_FOLDER)

# Function to dynamically load and execute the corresponding Pandas processing script
def process_file(filename, file_path):
    script_name = filename.lower().replace(" ", "_").replace(".csv", "").replace(".xlsx", "") + ".py"
    script_path = os.path.join(SCRIPT_FOLDER, script_name)

    if os.path.exists(script_path):
        spec = importlib.util.spec_from_file_location(script_name, script_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, 'process'):
            df = module.process(file_path)

            return df
        else:
            return f"Error: No 'process' function found in {script_name}"
    else:
        return f"Error: No matching script found for {filename}"


@app.route('/')
def index():
    return render_template('index.html')


def allowed_file(filename):
    return "." in filename and filename.rsplit('.')[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET','POST'])
def upload_file():
    if request.method == "POST":
        pass
        if 'file' not in request.files:
            flash('No file path')
            return redirect(url_for(request.url))
    
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(url_for(request.url))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename).lower()
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        global UPLOADED_FILE_NAME
        UPLOADED_FILE_NAME = filename

        SELECTED_PROCESS_NAME = re.sub(r"\..+", ".ipynb", filename)
        flash(f"File {filename} uploaded successfully.")
        return redirect(url_for('process', process_name=SELECTED_PROCESS_NAME))
    
    return render_template('index.html')

@app.route('/process/<process_name>', methods = ["GET", "POST"])
def process(process_name):   
    if request.method == "POST":

        global UPLOADED_FILE_NAME

        if not UPLOADED_FILE_NAME:
            flash("No file uploaded yet.")
            return redirect(url_for('index'))
        
        # Determine the correct script filename by replacing extensions
        script_name = re.sub(r"\..+", ".py", UPLOADED_FILE_NAME)  # Convert to .py for execution
        script_path = SCRIPT_FOLDER / script_name

        if not script_path.exists():
            flash(f"No matching script found for {UPLOADED_FILE_NAME}")
            return redirect(url_for('index'))

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], UPLOADED_FILE_NAME)


        
        # Execute the corresponding processing script
        result = process_file(UPLOADED_FILE_NAME, file_path)


        
        return redirect(url_for('download_file'))
    
   
    elif request.method == "GET":

           return render_template('process.html', uploaded_file=UPLOADED_FILE_NAME, script_name=process_name)
    



@app.route('/download')
def download_file():
    """
    Allows the user to download the processed file and then redirects to index.html.
    """
    global UPLOADED_FILE_NAME

    if not UPLOADED_FILE_NAME:
        flash("No processed file available for download.")
        return redirect(url_for('index'))


    processed_file_path = os.path.join(app.config['PROCESSED_FOLDER'], UPLOADED_FILE_NAME)

    if not os.path.exists(processed_file_path):
        flash("Processed file not found.")
        return redirect(url_for('index'))

    # Serve the processed file for download
    return send_file(processed_file_path, as_attachment=True, download_name=UPLOADED_FILE_NAME)

if __name__ == '__main__':
    app.run(debug=True)
