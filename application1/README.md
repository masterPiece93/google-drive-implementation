### Running Google Drive API's in a Python Script

- Using : google-api-python-client library 

- category : Using a Device flow IN webserver

here we use `InstalledAppFlow` class of `google-api-python-client` library .

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
    (venv) .../application1$ pip install -r requirements.txt
    ```

4. execute script 

    ```sh
    (venv) .../application1$ python3 run.py
    ```

When you'll successfully run the poc application , you will see a prompt like this below :
```sh
(venv) .../application1$ run.py 
Enter a User ID for Identifying your Account : 
```

you'll have to enter any string value as an identification of your login , for example :
```sh
(venv) .../application1$ run.py 
Enter a User ID for Identifying your Account : ankit8290
```

> Now you be prompted on you browser automatically & will be redirected to google permissions Consent Screen .

And then the script will exit with no example execution .
The screen will look something like this :
```sh
(venv) .../application1$ run.py 
Enter a User ID for Identifying your Account : ankit8290

 OUTPUT :
 ----------

 ----------
```

#### Running examples 

1. open `run.py` file in editor .
2. in this file , goto comment with name `# run examples :`. you can search for it in this script .
3. now you'll see the code ( try-catch block ) like this :
    ```py
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

    ```
4. there are commented example-function calls .
5. uncomment the example-function call to get it executed .
6. Then run the script : `run.py` every time .