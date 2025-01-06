# https://developers.google.com/identity/protocols/oauth2/web-server#example

# -*- coding: utf-8 -*-

import os, secrets
import flask
import requests

import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from enum import Enum
import logging
from google_drive_examples import (
    list_files_and_folders, 
    upload_file_to_drive,
    upload_csv_file_as_sheet,
    download_files_from_drive,
    create_folder_in_drive
)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
logger.debug("Line 16 debuger is working")

CREDENTIALS_FILE_NAME = 'credentials.json' # OAuth Client secret file provided by GCP
__base_dir__ = os.path.join(os.getcwd(), '')
__credentials_file__ = os.path.join(__base_dir__, CREDENTIALS_FILE_NAME)

class GenericScopes(Enum):
    OPENID = 'openid'


class UserInfoScopes(Enum):
    PROFILE = "https://www.googleapis.com/auth/userinfo.profile"
    EMAIL = "https://www.googleapis.com/auth/userinfo.email"


class CalendarScopes(Enum):
    READONLY = "https://www.googleapis.com/auth/calendar.readonly"


class TaskScopes(Enum):
    READONLY = "https://www.googleapis.com/auth/tasks.readonly"


class DriveScopes(Enum):

    VIEW_MANAGE = "https://www.googleapis.com/auth/drive"
    METADATA_READONLY = "https://www.googleapis.com/auth/drive.metadata.readonly"


SCOPES = [
    GenericScopes.OPENID.value,
    UserInfoScopes.EMAIL.value,
    UserInfoScopes.PROFILE.value,
    CalendarScopes.READONLY.value,
    TaskScopes.READONLY.value,
    DriveScopes.VIEW_MANAGE.value,
]

app = flask.Flask(__name__)

app.secret_key= os.environ.get("SECRET_KEY") or secrets.token_hex()

@app.route('/')
def index():
  return print_index_table()

@app.route('/authorize')
def authorize():
    
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        __credentials_file__, scopes=SCOPES)

    # The URI created here must exactly match one of the authorized redirect URIs
    # for the OAuth 2.0 client, which you configured in the API Console. If this
    # value doesn't match an authorized URI, you will get a 'redirect_uri_mismatch'
    # error.
    flow.redirect_uri = flask.url_for('oauth2callback', _external=True)

    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true')

    # Store the state so the callback can verify the auth server response.
    flask.session['state'] = state

    return flask.redirect(authorization_url)


@app.route('/oauth2callback')
def oauth2callback():
  
    state = flask.session['state']

    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        __credentials_file__, scopes=SCOPES, state=state)
    flow.redirect_uri = flask.url_for('oauth2callback', _external=True)

    # Use the authorization server's response to fetch the OAuth 2.0 tokens.
    authorization_response = flask.request.url
    flow.fetch_token(authorization_response=authorization_response)
    
    credentials = flow.credentials
    flask.session['credentials'] = credentials_to_dict(credentials)

    return flask.redirect(flask.url_for('index'))


@app.route('/revoke')
def revoke():
    if 'credentials' not in flask.session:
        return ('You need to <a href="/authorize">authorize</a> before ' +
                'testing the code to revoke credentials.')

    credentials = google.oauth2.credentials.Credentials(
        **flask.session['credentials'])

    revoke = requests.post('https://oauth2.googleapis.com/revoke',
        params={'token': credentials.token},
        headers = {'content-type': 'application/x-www-form-urlencoded'})

    status_code = getattr(revoke, 'status_code')
    if status_code == 200:
        return('Credentials successfully revoked.' + print_index_table())
    else:
        return('An error occurred.' + print_index_table())


@app.route('/clear')
def clear_credentials():
    if 'credentials' in flask.session:
        del flask.session['credentials']
    return ('Credentials have been cleared.<br><br>' +
            print_index_table())

@app.route('/test')
def test_api_request():
    """
    a sample test
    """

    if 'credentials' not in flask.session:
        return flask.redirect('authorize')

    # Load credentials from the session.
    credentials = google.oauth2.credentials.Credentials(
        **flask.session['credentials'])

    if not credentials.valid:
        return flask.redirect('authorize')
    
    service = build("drive", "v3", credentials=credentials)

    files = service.files().list().execute()

    flask.session['credentials'] = credentials_to_dict(credentials)

    return flask.jsonify(**files)

@app.route('/run-example/<string:example_id>')
def access_drive_api(example_id: str):

    if 'credentials' not in flask.session:
        return flask.redirect(flask.url_for('authorize'))

    # Load credentials from the session.
    credentials = google.oauth2.credentials.Credentials(
        **flask.session['credentials'])

    if not credentials.valid:
        return flask.redirect(flask.url_for('authorize'))
    
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


def credentials_to_dict(credentials):
    return {'token': credentials.token,
            'refresh_token': credentials.refresh_token,
            'token_uri': credentials.token_uri,
            'client_id': credentials.client_id,
            'client_secret': credentials.client_secret,
            'scopes': credentials.scopes}

def print_index_table():
    return ('<table>' +
            '<tr><td><a href="/test">Test an API request</a></td>' +
            '<td>Submit an API request and see a formatted JSON response. ' +
            '    Go through the authorization flow if there are no stored ' +
            '    credentials for the user.</td></tr>' +
            '<tr><td><a href="/authorize">Test the auth flow directly</a></td>' +
            '<td>Go directly to the authorization flow. If there are stored ' +
            '    credentials, you still might not be prompted to reauthorize ' +
            '    the application.</td></tr>' +
            '<tr><td><a href="/revoke">Revoke current credentials</a></td>' +
            '<td>Revoke the access token associated with the current user ' +
            '    session. After revoking credentials, if you go to the test ' +
            '    page, you should see an <code>invalid_grant</code> error.' +
            '</td></tr>' +
            '<tr><td><a href="/clear">Clear Flask session credentials</a></td>' +
            '<td>Clear the access token currently stored in the user session. ' +
            '    After clearing the token, if you <a href="/test">test the ' +
            '    API request</a> again, you should go back to the auth flow.' +
            '</td></tr>' +
            '<tr><td><a href="/run-example/1" target="_blank">Run Example - 1</a></td>' +
            '<td>This example lists all files and folders in the provided folder-id' +
            '</td></tr>' +
            '<tr><td><a href="/run-example/2" target="_blank">Run Example - 2</a></td>' +
            '<td>This example upload file to drive in the provided folder-id' +
            '</td></tr>' +
            '<tr><td><a href="/run-example/3" target="_blank">Run Example - 3</a></td>' +
            '<td>This example uploads csv file as sheet in the provided folder-id' +
            '</td></tr>' +
            '<tr><td><a href="/run-example/4" target="_blank">Run Example - 4</a></td>' +
            '<td>This example download files from drive in the downloads folder of system' +
            '</td></tr>' +
            '<tr><td><a href="/run-example/5" target="_blank">Run Example - 5</a></td>' +
            '<td>This example creates folder in drive ' +
            '</td></tr>' +
            
            '</table>'
            )


if __name__ == '__main__':
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    app.run('0.0.0.0', 5000, debug=True)
