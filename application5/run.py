import os
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from enum import Enum
from google_drive_examples import (
    list_files_and_folders, 
    upload_file_to_drive,
    upload_csv_file_as_sheet,
    download_files_from_drive,
    create_folder_in_drive
)

class DriveScopes(Enum):

    VIEW_MANAGE = "https://www.googleapis.com/auth/drive"
    METADATA_READONLY = "https://www.googleapis.com/auth/drive.metadata.readonly"


# user = input("enter user id : ")

def create_service(version: str,):
    """
    """

    scope: list = [DriveScopes.VIEW_MANAGE.value,]
    service_account_json_file = os.path.join(os.getcwd(), 'service_account.json')
    credentials = service_account.Credentials.from_service_account_file(
        filename= service_account_json_file,
        scopes= scope,
    )

    try:
        service = build("drive", version, credentials=credentials)
        return service
    except HttpError as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    service = create_service('v3')

    # run examples :
    print("\n OUTPUT :\n","-"*10)
    try:
        # list_files_and_folders(
        #     service
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
