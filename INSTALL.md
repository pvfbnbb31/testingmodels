INSTALLATION FILE FOR MEMORAID APPLICATION
------------------------------------------
STEP 1:

Start PowerShell and change into the directory you wish to work in.

STEP 2:

Create a new Django project from the GitHub repository.
django-admin startproject --template=https://github.com/usma-it394/ay16-2-project-team-c-1.git 

STEP 3:

Install the required packages for this application.
pip install -r requirements.txt

STEP 4:

In using this type of application template, we need to unistall gunicorn or the application 
will stop in the deployment phase.
pip unistall gunicorn

STEP 5:

Initialize the datebase structure and create the initial security principal.
python .\manage.py syncdb

STEP 6:

Initialize a local git repository.
git init

STEP 7:

Add the local files to this repository.
git add .

STEP 8:

Login to Heroku and create a new application.
heroku login
heroku create

STEP 9:

Deploy local git repository to Heroku.
git push heroku master

STEP 10:

Initialize the datebase structure on Heroku, while also creating an initial security principal.
heroku run:detached python manage.py migrate
heroku run:detached bash ./create_admin.sh admin admin@example.com password

STEP 11:

Open the application.
heroku open
------------------------------------------
