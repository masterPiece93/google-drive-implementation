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

![application2_server_op_2](https://github.com/masterPiece93/google-drive-implementation/blob/c42bb0ab3d0d7ca64b89a139596d08dcbbad431f/__static_resources/application2_server_op_2.png)

- browser will be opened on home page

![application2_home_screen](https://github.com/masterPiece93/google-drive-implementation/blob/c42bb0ab3d0d7ca64b89a139596d08dcbbad431f/__static_resources/application2_home_screen.png)

- enter the url :

    > /ui/access-drive/<string:username>

![application2_drive_api_sc_2](https://github.com/masterPiece93/google-drive-implementation/blob/c42bb0ab3d0d7ca64b89a139596d08dcbbad431f/__static_resources/application2_drive_api_sc_2.png)

- for example :

    > /ui/access-drive/ankit8290

![application2_drive_api_sc_1](https://github.com/masterPiece93/google-drive-implementation/blob/c42bb0ab3d0d7ca64b89a139596d08dcbbad431f/__static_resources/application2_drive_api_sc_1.png)

- if not already logged in , you'll be redirected to google 


    ![google account screen](https://github.com/masterPiece93/google-drive-implementation/blob/c42bb0ab3d0d7ca64b89a139596d08dcbbad431f/__static_resources/google_account_screen.png)

    Here choose the account whose drive you want to acess .

- You'll land on security page , because in GCP console we haven't verified our sample app account as this is for testing purpose .

    - just click on `advanced` option 

    ![applictaion2_redirection_sc_2](https://github.com/masterPiece93/google-drive-implementation/blob/c42bb0ab3d0d7ca64b89a139596d08dcbbad431f/__static_resources/applictaion2_redirection_sc_2.png)

    - then you'll land on following screen 

    ![application2_redirection_sc_2](https://github.com/masterPiece93/google-drive-implementation/blob/c42bb0ab3d0d7ca64b89a139596d08dcbbad431f/__static_resources/application2_redirection_sc_2.png)

    click on `Go to <YOUR-APP-NAME> (unsafe)`

- Now You see the google consent screen as below :

    ![google_consent_screen](https://github.com/masterPiece93/google-drive-implementation/blob/c42bb0ab3d0d7ca64b89a139596d08dcbbad431f/__static_resources/google_consent_screen.png)

    click continue 

- Now Your flow is complete . you'll get a screen as shown below :

    ![application2_redirection_sc_complete](https://github.com/masterPiece93/google-drive-implementation/blob/c42bb0ab3d0d7ca64b89a139596d08dcbbad431f/__static_resources/application2_redirection_sc_complete.png)

- Now you can go back to to browser screen from where you redirected and it will look something like this now :

    ![application2_final_screen](https://github.com/masterPiece93/google-drive-implementation/blob/c42bb0ab3d0d7ca64b89a139596d08dcbbad431f/__static_resources/application2_final_screen.png)


Now You may click on any of the example , to run it .

`NOTE` : you must go to the code base , modify the examples 

#### Running examples 

1. open `server.py` file in editor .
2. in this file , goto comment with name `# run examples :`. you can search for it in this script .
3. now you'll see the code ( try-catch block ) like this :
    ```py
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

    ```
4. there are example-function calls in If-Else blocks.
5. you must provide the folder id's of your own drive
6. Then you may re-run the server and test the examples .
