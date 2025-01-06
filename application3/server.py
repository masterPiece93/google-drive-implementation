"""
| Author : Ankit Kumar
| Contact :
    - personal email : ankit8290@gmail.com
    - work email : ankit.kumar05@telusdigital.com

This is an example of a Google Oauth2.0 Authenticated application flow for a
GCP project registered as a web-client.

And using other google services through it .

It uses `Authlib` library for oauth authenication .

"""
import os
import json
import requests
from flask import Flask, url_for, session, redirect, render_template, make_response, send_from_directory, request
from authlib.integrations.flask_client import OAuth
from typing import Union, Final
from environs import Env

# - Setup Environment Variables :
# ! from dotenv import load_dotenv; load_dotenv() # Older approach . Using `environs` in place of it
env = Env()
env.read_env()
env.read_env('.oauth.env')

# - Initializing final config variables :
DEBUG:                  Final[bool] = env.bool('DEBUG', False)
PORT:                   Final[int]  = env.int('PORT')
SECRET_KEY:             Final[str]  = env.str('SECRET_KEY')
SESSION_COOKIE_HTTPONLY:Final[bool] = env.bool('SESSION_COOKIE_HTTPONLY')
SESSION_COOKIE_SECURE:  Final[bool] = env.bool('SESSION_COOKIE_SECURE')
PERMANENT_SESSION_LIFETIME: Final[int]  = env.int('PERMANENT_SESSION_LIFETIME', 86400)
OAUTH_CREDENTIALS_PATH: Final[str] = env.str('OAUTH_CREDENTIALS_PATH')
OAUTH_META_URL:         Final[str] = env.str('OAUTH_META_URL')
OAUTH_SCOPE:            Final[str] = env.str('SCOPE')

with open(os.path.join(os.getcwd(), OAUTH_CREDENTIALS_PATH)) as oauth_credentials_file: # json file (key,value) is added to config
    credentials: dict = json.load(oauth_credentials_file)
    OAUTH_CREDENTIALS_WEB_DICT: Final[dict] = credentials["web"]

# - Initializing flask applictaion :
app = Flask(__name__,)

# - Loading config variables in flask config :
app.config.from_object(__name__)

# - Initializing Oauth object :
oauth = OAuth(app)

# ) : register oauth applictaion
oauth.register("Flask_Gauth"
,   client_id =             OAUTH_CREDENTIALS_WEB_DICT["client_id"]
,   client_secret =         OAUTH_CREDENTIALS_WEB_DICT["client_secret"]
,   server_metadata_url =   OAUTH_META_URL
,   client_kwargs = {
        "scope": OAUTH_SCOPE
    }
)

@app.route('/')
def home():
    
    return render_template('home.html', session=session.get("user"),pretty=json.dumps(session.get("user"), indent=4),authority=json.dumps(session.get("authority"), indent=4))

@app.route('/google-login')
def google_login():
    return oauth.Flask_Gauth.authorize_redirect(redirect_uri=url_for("google_callback",_external=True), access_type="offline",)

@app.route('/signin-google', strict_slashes=False)
def google_callback():
    token = oauth.Flask_Gauth.authorize_access_token()
    session["user"]=token
    return redirect('/')

@app.route('/channel', strict_slashes=False)
def channel():
    return {}

@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))



# - Drive Api's

# ) 1. ( Files )

@app.route('/drive/<string:version>/files')
def drive_list_all_files(version: str):
    
    if version not in {'v1', 'v2', 'v3'}:
        return 204, None
    
    url = f'https://www.googleapis.com/drive/{version}/files'
    token=session['user']
    params = dict(
        access_token=token["access_token"]
    )
    api_response = requests.get(url, params=params)

    if api_response.status_code == 200:
        data = api_response.json()
        del data["nextPageToken"]
        if version == 'v2':
            del data["nextLink"]
        return data
    
    return {}, api_response.status_code

@app.route('/drive/<string:version>/files/<string:file_id>')
def drive_list_contents_of_single_file(version: str, file_id: str):
    
    if version not in {'v1', 'v2', 'v3'}:
        return 204, None
    
    url = f'https://www.googleapis.com/drive/{version}/files/{file_id}'
    token=session['user']
    params = dict(
        access_token=token["access_token"]
    )
    api_response = requests.get(url, params=params)

    if api_response.status_code == 200:
        data = api_response.json()
        if version == 'v2':
            del data['md5Checksum']
        return data
    
    return {}, api_response.status_code

class AccessTokenValidator:

    def is_token_valid(self,):
        token_validation_url= "https://oauth2.googleapis.com/tokeninfo"

        if 'user' not in session:
            return False
        token = session['user']
        params = dict(
            access_token=token["access_token"]
        )
        api_response = requests.get(token_validation_url, params=params)
        if api_response.status_code == 400 :
            data = api_response.json()
            return not data['error'] == 'invalid_token'
        return True
    
        

@app.before_request
def do_something_whenever_a_request_comes_in():
    # request is available
    print('validating token')
    print(request.path)
    if request.path not in (
        '/'
    ,   '/google-login'
    ,   '/signin-google'
    ,   'logout'
    ):
        if not AccessTokenValidator().is_token_valid():
            print('access token invalid')
            return redirect(url_for('google_login'))

if __name__ == '__main__':
    app.run(
        host= '0.0.0.0'
    ,   port= PORT
    ,   debug= DEBUG
    )