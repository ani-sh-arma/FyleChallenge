Install all the required libraries in your environment using this command
    pip install -r requirements.txt

Create your github authorization token and then create a .env file in the directory with manage.py file
and add the token in that file as specified
    GITHUB_TOKEN = "your_github_token"

Now the app is set to run you can use this command to run the app
    python manage.py runserver