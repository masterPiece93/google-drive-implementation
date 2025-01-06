# Running Google Drive Api's in Web Applictaion 

- Using : Authlib library 

- category : Webserver Oauth

#### How to Run

- Please get Google Credentials File ( Web Application )
- generate credentials file : [link](https://developers.google.com/workspace/guides/create-credentials)
    - you can connect with your devops for generating one for you .
- credential file name must be : `credentials.json` and it must be placed at the root level 
    - take the hint from below directory structure to understand the location of credentials.json file :
    ```
    /application-2 (root)
    ----/data
    ----/local_dist
    ----credentials.json
    ----   .
    ----   .
    ----   .
    ```

##### on local python

0. pre-requisites
    - Install python ( version : `3`.`*`.`*` )
    - Install python-virtualenv

1. create a virtualenv 
    ```sh
    python3 -m venv <venv>
    ```
    > NOTE : `<venv>` represents the name of your virtual env you want to keep.
    Replace it with any name like my-venv, virtual-env etc ...

2. activate virtualenv

    | Platform | Shell | Command to activate virtual environment |
    | -------- | ----- | --------------------------------------- |
    |   POSIX  | bash/zsh | `$ source <venv>/bin/activate` |
    |   POSIX  | fish | `$ source <venv>/bin/activate.fish` |
    |   POSIX  | csh/tcsh | `$ source <venv>/bin/activate.csh` |
    |   POSIX  | pwsh | `$ <venv>/bin/Activate.ps1` |
    |   WINDOWS  | cmd.exe | `C:\> <venv>\Scripts\activate.bat` |
    |   WINDOWS  | PowerShell | `PS C:\> <venv>\Scripts\Activate.ps1` |
    
    
3. install requirements

    ```sh
    (venv) .../application2$ pip install -r requirements.txt
    ```

4. add .env file at root dir , with following contents :

    ```sh
    # application3/.env
    
    DEBUG=True
    PORT=4000
    SECRET_KEY = "super-secret-value"
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = False
    PERMANENT_SESSION_LIFETIME = 86400
    ```

5. run server 

    ```sh
    (venv) .../application2$ python3 server.py
    ```

- When you'll successfully run the poc application , you will see a server logs like this below :

![application3_server_log_1](https://github.com/xavient/gdrive-sync-poc-impl/blob/42b2175e4e35c03f1c673d18e0fa16bd6b8e7c52/__static_resources/application3_server_log_1.png)


- click on the web link 

![application3_server_log_2](https://github.com/xavient/gdrive-sync-poc-impl/blob/42b2175e4e35c03f1c673d18e0fa16bd6b8e7c52/__static_resources/application3_server_log_2.png)

- browser will be opened on home page

![application3_landing_page](https://github.com/xavient/gdrive-sync-poc-impl/blob/42b2175e4e35c03f1c673d18e0fa16bd6b8e7c52/__static_resources/application3_landing_page.png)

- click on login and you'll be redirected to account selection screen 

![application3_account_selection](https://github.com/xavient/gdrive-sync-poc-impl/blob/42b2175e4e35c03f1c673d18e0fa16bd6b8e7c52/__static_resources/application3_account_selection.png)

- post this , you'll be redirected back on home screen with information

![application3_post_login](https://github.com/xavient/gdrive-sync-poc-impl/blob/42b2175e4e35c03f1c673d18e0fa16bd6b8e7c52/__static_resources/application3_post_login.png)

- enter the api urls :

    > drive_list_all_files : /drive/<string:version>/files
    > drive_list_contents_of_single_file : /drive/<string:version>/files/<string:file_id>

- for example :

    > /drive/v3/files

![application3_drive_api_call](https://github.com/xavient/gdrive-sync-poc-impl/blob/42b2175e4e35c03f1c673d18e0fa16bd6b8e7c52/__static_resources/application3_drive_api_call.png)
