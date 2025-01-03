# Running Google Drive Api's in Web Applictaion 

- Using : google-api-python-client library 

- category : Using a Device flow IN webserver

here tweak the use of `InstalledAppFlow` class of `google-api-python-client` library, so as to fir it for working with werserver .

#### How to Run

- Please get Google Credentials File ( Installed device ) \
> NOTE : Please goto this [wiki]() page for understanding on how to get a creadentials file
- credential file name must be : `credentials.json` and it must be placed at the root level 
    - take the hint from below directory structure to understand the location of credentials.json file :
    ```
    /application-1 (root)
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

4. run server 

    ```sh
    (venv) .../application2$ python3 server.py
    ```



> Now you be prompted on you browser automatically & will be redirected to google permissions Consent Screen .


- When you'll successfully run the poc application , you will see a server logs like this below :


![application2_server_op](https://github.com/masterPiece93/google-drive-implementation/blob/55603089669268bc7f8928bfa02ae59d05148211/__static_resources/application2_server_op.png)


- click on the web link 

![application2_server_op_2]()

- browser will be opened on home page

![application2_home_screen]()

- enter the url :

    > /ui/access-drive/<string:username>

![application2_drive_api_sc_2]()

- for example :

    > /ui/access-drive/ankit8290

![application2_drive_api_sc_1]()

- if not already logged in , you'll be redirected to google 


    ![google account screen]()

    Here choose the account whose drive you want to acess .

- You'll land on security page , because in GCP console we haven't verified our sample app account as this is for testing purpose .

    - just click on `advanced` option 

    ![applictaion2_redirection_sc_2]()

    - then you'll land on following screen 

    ![application2_redirection_sc_2]()

    click on `Go to <YOUR-APP-NAME> (unsafe)`

- Now You see the google consent screen as below :

    ![google_consent_screen]()

    click continue 

- Now Your flow is complete . you'll get a screen as shown below :

    ![application2_redirection_sc_complete]()

- Now you can go back to to browser screen from where you redirected and it will look something like this now :

    ![application2_final_screen]()


