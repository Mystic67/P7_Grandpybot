P7 GrandpyBot

############################### Installation ##################################

- Install pipenv on your system
- copy or clone this repository in your folder

- Open shell and go to the root directory
    ex: cd /YOUR_FOLDER/P7_Grandpybot-master

- Install and run the python 3.7 virtualenv with command:
    pipenv shell

- Install the requirements with command:
    pipenv install -r requirements.txt

- Create environment variables:
    1) create a new file ".env" in root directory (ex: /YOUR_FOLDER/P7_Grandpybot-master)

    2) Copy the following line in new .env file with your personal keys
        SECRET_KEY = YOUR_APP_KEY
        GOOGLE_API_KEY = YOUR_GOOGLE_API_KEY

    3) Save the .env file.

    PS: To generate YOUR_APP_KEY secret key you can type following command in Python shell: <br/>
        >>> import random, string <br/>
        >>> "".join([random.choice(string.printable) for _ in range(24)]) <br/>

- Start the local server with command:
    python3 run.py

The app is started on server, you can yet open webpage with your favorite web browser (Firefox, Chrome, Safari etc..) and copy the address indicate from server in your shell.
ex:  127.0.0.1:5000 or localhost:5000

################################################################################

<div align="center">
    <img src="/grandpybotapp/static/img/Screen_GrandpyBot1.png" width="750px"</img> </br></br>
    <img src="/grandpybotapp/static/img/Screen_GrandpyBot2.png" width="750px"</img>
</div>
