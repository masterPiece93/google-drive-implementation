import os
from pathlib import Path
from flask import Flask, redirect, url_for, abort, request
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
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


app = Flask(__name__)

# COMMON DATA FOR BOTH UI & API
SCOPES = [DriveScopes.VIEW_MANAGE,]

@app.route('/')
def home():
    return '''
    HOME

    <!-- <a href="/ui"> go to drive examples ui </a> -->
    '''
@app.route('/ui', )
@app.route('/ui/<route>', )
def index(route: str = ''):

    view = '''
    <div>
        <b>{flash_message}</b>
    </div>
    
    <h1>Drive Examples UI</h1>

    <section>
    {html}
    </section>
    '''
    
    _index_ = '''
    <input >
    <a href="/ui/access-drive/"> Access Drive </a>
    '''

    if route == 'scopes-denied':    
        message = request.args.get('message', type=str,)
        return view.format(flash_message='', html=message)
    
    return view.format(flash_message='', html=_index_)

@app.route('/ui/grant-drive-access/<string:username>')
def grant_drive_access(username: str):
    
    username = username.replace('.', '_')
    
    credentials = None

    # initializations :
    scopes = [DriveScopes.VIEW_MANAGE.value,]
    token = TOKEN_FILE_FORMAT.format(username)
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
                return redirect(f'/ui/scopes-denied/?message=permission denied by user {username} for the following scopes\n{scopes}')
            
    # Save the credentials for the next run :
    with open(token_file, "w") as token:
        _credentials_as_json_obj = credentials.to_json()
        token.write(_credentials_as_json_obj)

    return redirect(f'/ui/access-drive/{username}')

@app.route('/ui/access-drive/<string:username>')
def access_drive(username: str,):
    
    username = username.replace('.', '_')
    
    # initializations :
    scopes = [DriveScopes.VIEW_MANAGE.value,]
    token = TOKEN_FILE_FORMAT.format(username)
    token_file = os.path.join(__storage_dir__, token)

    credentials = None
    if token_exists(token_file):
        credentials = Credentials.from_authorized_user_file(token_file, scopes)
    else:
        if not credentials or not credentials.valid:
            return redirect(url_for('grant_drive_access', username=username))
    view = '''
    <div>
        <b>{flash_message}</b>
    </div>
    
    <h1>Drive Examples List</h1>

    <section>
    {html}
    </section>
    '''
    
    _index_ = f'''
    
    List of drive examples :
    
    <ul>
        <li>
            <a href="/api/access-drive/{username}/run-example/1">
                list_files_and_folders
            </a>
        </li>
        <li>
            <a href="/api/access-drive/{username}/run-example/2">
                upload_file_to_drive
            </a>
        </li>
        <li>
            <a href="/api/access-drive/{username}/run-example/3">
                upload_csv_file_as_sheet
            </a>
        </li>
        <li>
            <a href="/api/access-drive/{username}/run-example/4">
                download_files_from_drive
            </a>
        </li>
        <li>
            <a href="/api/access-drive/{username}/run-example/5">
                create_folder_in_drive
            </a>
        </li>
        
    </ul>
    '''

    return view.format(flash_message='', html=_index_)



# API :

@app.route('/api/access-drive/<string:username>/run-example/<string:example_id>')
def access_drive_api(username: str, example_id: str):

    username = username.replace('.', '_')
    
    # initializations :
    scopes = [DriveScopes.VIEW_MANAGE.value,]
    token = TOKEN_FILE_FORMAT.format(username)
    token_file = os.path.join(__storage_dir__, token)

    if token_exists(token_file):
        credentials = Credentials.from_authorized_user_file(token_file, scopes)
    else:
        return abort(400, 'user grant for drive needed')
    
    # build drive service :
    service = build("drive", "v3", credentials=credentials)

    # run examples :
    print("\n OUTPUT :\n","-"*10)
    data = None
    try:

        if example_id == 1:
            list_files_and_folders(
                service,
                folder_id="1-tpctrXMKpB1oVm6a4V2nQD34QzsLGZx"
            )
        elif example_id == 2:
            upload_file_to_drive(
                service,
                sample_data_dir='',
                folder_id="1YttjORydGKHnP5mjBr3-gRaPhw1XkX5v"
            )
        elif example_id == 3:
            upload_csv_file_as_sheet(
                service,
                sample_data_dir='',
                folder_id="1YttjORydGKHnP5mjBr3-gRaPhw1XkX5v"
            )
        elif example_id == 4:
            download_files_from_drive(
                service,
                download_files_map={
                # 'my_downloaded_file_1.xlsx'   :   '1PZrvx_0e09ecglzSPf92JbZzxyNTOrV6aQAp1hA2dLs',
                'my_downloaded_file_2.png'      :   '1Jbnsjjax93nVsHPdsOY5as1fBKRJ_4wj',
                'my_donloaded_file_3.txt'       :    '1bytph26Uxxthfi3wETJlW-1_D4GHYvZ1'
            }
            )
        elif example_id == 5: 

            create_folder_in_drive(
                service
            )

    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f"An error occurred: {error}")
        raise error
    
    return data or {"message": f"example <{example_id}> ran sucessfully. Check server console."}

if __name__ == '__main__':
    app.run(
        host='0.0.0.0'
    ,   port=101010
    ,   debug=True
    )