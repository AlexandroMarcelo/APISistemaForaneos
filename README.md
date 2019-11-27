# APISistemaForaneos

To launch the api to Azure, log in in your account and create a resource group, the in the terminal (at the top of your dashboard) clone this github repository in the user root (/home/<user_name>/), and cd to the APISistemaForaneos folder created by git clone, then run the following command:

    az webapp up --sku F1 -n apistudentexchange -l centralus
 
Wait for the status of the page (json). Copy the URL given by the previous command, and save it

Finally change the Startup Command of the appservice in App Services -> apistudentexchange -> Configuration (left panel) -> General Settings -> Startup Command, by typing the following:

    gunicorn --bind=0.0.0.0 --timeout 600 app:app

Wait some minutes and finally go to the URL given and thats all.