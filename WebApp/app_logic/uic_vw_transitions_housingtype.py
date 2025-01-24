import pandas as pd
import time
import datetime
from pathlib import Path

current_dir = Path(__file__).parent.parent
upload_relative_path = Path("./uploads")
processed_relative_path = Path("./processed")
UPLOAD_FOLDER = current_dir / upload_relative_path
PROCESSED_FOLDER = current_dir / processed_relative_path

class UicVwTransitionsHousingType():
    def __init__(self,file_path):
        self.file_path = UPLOAD_FOLDER.joinpath(file_path)

    def process(self):
        if self.file_path is None:
            self.df = pd.read_excel(UPLOAD_FOLDER.joinpath('uic_vw_transitions_housingtype.xlsx'))
            print(self.df.info())
            return (self.df.info())

        else:
            self.df = pd.read_excel(self.file_path)
            return (self.df.info())


# # %%
# df.columns

# # %%
# # converting the string to datetime format
# df['Transition_Discharge_Date'] = pd.to_datetime(df['Transition_Discharge_Date'])

# # %%
# # converting the string to datetime format
# df['Activity_Closed_Date'] = pd.to_datetime(df['Activity_Closed_Date'])

# # %%
# # converting the string to datetime format
# df['Activity_Date_Started'] = pd.to_datetime(df['Activity_Date_Started'])

# # %%
# # converting the string to datetime format
# df['Transition_Finished_Date'] = pd.to_datetime(df['Transition_Finished_Date'])

# # %%
# df.dtypes

# # %%
# df['RIN'].sample(10)

# # %%
# # Convert RIN to string
# df['RIN'] = df['RIN'].astype('str') 

# # %%
# df['RIN'] = df['RIN'].str.strip()

# # %%
# df['RIN'].sample(15)

# # %%
# # add leading zeros to Member_RIN
# df['RIN'] = df['RIN'].str.zfill(9)

# # %%
# df['RIN'].sample(10)

# # %%
# #export file without index column
# df.to_excel("UIC_VW_Transitions_Housingtype.xlsx", index=False)

# # %%
# # Create a timestamp object
# timestamp = pd.Timestamp(datetime.datetime.now())

# # Print the timestamp
# print(timestamp)

# # %%
# #the end!

# # %%



