import os
import sys
from pathlib import Path
from enum import Enum
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_drive_examples import (
    list_files_and_folders, 
    upload_file_to_drive,
    upload_csv_file_as_sheet,
    download_files_from_drive,
    create_folder_in_drive
)
STORAGE_DIR_NAME = 'storage' # used to store tokens
CREDENTIALS_FILE_NAME = 'credentials.json' # OAuth Client secret file provided by GCP
TOKEN_FILE_FORMAT = "token_{0}.json" # token files will be in this format

# dir paths
__base_dir__ = os.path.join(os.getcwd(), '')
__storage_dir__ = os.path.join(__base_dir__, STORAGE_DIR_NAME)
__credentials_file__ = os.path.join(__base_dir__, CREDENTIALS_FILE_NAME)

# auto create storage dir
Path(__storage_dir__).mkdir(parents=True, exist_ok=True)

class DriveScopes(Enum):

    VIEW_MANAGE = "https://www.googleapis.com/auth/drive"
    METADATA_READONLY = "https://www.googleapis.com/auth/drive.metadata.readonly"


def token_exists(token_file: str):
    """
    -- checks in storage dir if token_{userid}.json file exists or not
    """
    return os.path.exists(token_file)

def credentials_expired(credentials: Credentials):
    """
    -- checks if credentials expired or not
    """
    return credentials.expired and credentials.refresh_token

if __name__ == '__main__':

    credentials = None

    userid = input("Enter a User ID for Identifying your Account : ")
    
    # initializations :
    scopes = [DriveScopes.VIEW_MANAGE.value,]
    token = TOKEN_FILE_FORMAT.format(userid)
    token_file = os.path.join(__storage_dir__, token)
    
    # fetching / creating credentials :

    if token_exists(token_file):
        credentials = Credentials.from_authorized_user_file(token_file, scopes)

    if not credentials or not credentials.valid:
        if credentials and credentials_expired(credentials):
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow\
                .from_client_secrets_file(
                __credentials_file__,
                scopes
            )
            try:
                credentials = flow.run_local_server(port=0) # Initiating Browser for consent
            except Exception as e:
                print(e)
                exit(f"Permissions not Granted by user for scope : {scopes}")
    # Save the credentials for the next run :
    with open(token_file, "w") as token:
        _credentials_as_json_obj = credentials.to_json()
        token.write(_credentials_as_json_obj)

    # build drive service :
    service = build("drive", "v3", credentials=credentials)

    # run examples :
    print("\n OUTPUT :\n","-"*10)
    try:
        # list_files_and_folders(
        #     service,
        #     folder_id="1-tpctrXMKpB1oVm6a4V2nQD34QzsLGZx"
        # )

        # upload_file_to_drive(
        #     service,
        #     sample_data_dir='',
        #     folder_id="1YttjORydGKHnP5mjBr3-gRaPhw1XkX5v"
        # )

        # upload_csv_file_as_sheet(
        #     service,
        #     sample_data_dir='',
        #     folder_id="1YttjORydGKHnP5mjBr3-gRaPhw1XkX5v"
        # )

        # download_files_from_drive(
        #     service,
        #     download_files_map={
        #     # 'my_downloaded_file_1.xlsx'   :   '1PZrvx_0e09ecglzSPf92JbZzxyNTOrV6aQAp1hA2dLs',
        #     'my_downloaded_file_2.png'      :   '1Jbnsjjax93nVsHPdsOY5as1fBKRJ_4wj',
        #     'my_donloaded_file_3.txt'       :    '1bytph26Uxxthfi3wETJlW-1_D4GHYvZ1'
        # }
        # )

        # create_folder_in_drive(
        #     service
        # )
        
        ...

    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f"An error occurred: {error}")
    print('\n',"-"*10)

    # NOTE :
    # if you want to see docmentation of example :
    if False: # set `True` to run
        print(help(list_files_and_folders))

    # if you want to see the documentation of all examples :
    if False: # set `True` to run
        print(help(google_drive_examples))

    # if you want to get a markdown documentation file of all examples :
    if False: # set `True` to run
        with open('examples_doc.md', 'w+') as f:
            print(google_drive_examples.__doc__, file=f)

    # if you want to see the complete source code of any example :
    if False: # set `True` to run
        import inspect
        print(inspect.getsource(list_files_and_folders))
