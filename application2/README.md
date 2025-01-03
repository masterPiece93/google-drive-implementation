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

When you'll successfully run the poc application , you will see a prompt like this below :


> Now you be prompted on you browser automatically & will be redirected to google permissions Consent Screen .


