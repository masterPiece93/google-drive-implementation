# Running Google Drive Api's in Web Applictaion 

- Using : google-api-python-client library 

- category : Using a Web flow IN webserver

#### How to Run

- Please get Google Credentials File ( Web Application )
- generate credentials file : [link](https://developers.google.com/workspace/guides/create-credentials)
    - you can connect with your devops for generating one for you .
- credential file name must be : `credentials.json` and it must be placed at the root level 
    - take the hint from below directory structure to understand the location of credentials.json file :
    ```
    /application-4 (root)
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
    (venv) .../application4$ pip install -r requirements.txt
    ```

4. run server 

    ```sh
    (venv) .../application4$ python3 server.py
    ```

- When you'll successfully run the poc application , you will see a server logs like this below :

![application4_server_log_1](https://github.com/masterPiece93/google-drive-implementation/blob/957f6c47e30ea5d0e10ea3ed7bd308a48e767ffc/__static_resources/application4_server_logs_1.png)


- click on the web link 

![application4_server_log_2](https://github.com/masterPiece93/google-drive-implementation/blob/957f6c47e30ea5d0e10ea3ed7bd308a48e767ffc/__static_resources/application4_server_logs_2.png)

- browser will be opened on home page

![application4_home_screen](https://github.com/masterPiece93/google-drive-implementation/blob/957f6c47e30ea5d0e10ea3ed7bd308a48e767ffc/__static_resources/application4_home_screen.png)

Post this just follow the instructions on the home page to run all the examples .
