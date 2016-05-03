OPERATIONAL GUIDANCE
------------------------------------------

------------------------------------------
TO ADD/REMOVE ADMIN ACCOUNTS:

STEP 1:

During the setup phase, the system admin created a "super user". Please reference the
INSTALL.md file for more information.

Sign into this "super user".

STEP 2:

After logging into the super user, navigate to the User Creation tab on the Admin Page
of the application. Here, you can modify both normal user accounts, as well as accounts
that have staff and "super user" status. 

STEP 3A TO REMOVE:

STEP 3A.1:
On the User Page of the Admin Site, click the gray box next to the account that you wish
to remove. 

STEP 3A.2
After doing so, click on the Action Drop down box and select Delete Selected users and click
Go.

STEP 3B TO ADD:

STEP 3B.1:
On the User PAge of the Admin Site, click the button titled create user.

STEP 3B.2:
Navigate through the following page giving the permissions that you want for that account.
Then simple click create account. 
------------------------------------------

------------------------------------------
TO BACKUP:

STEP 1:

Start PowerShell

STEP 2:

Navigate to the directory in which you created the Web Application from and run the command:
git pull heroku master
This will take what changes were made on the remote location, heroku, and update your local
repository with those changes.

------------------------------------------

------------------------------------------
TO RESTORE:

STEP 1:

Start PowerShell

STEP 2:

To restore your web application, run the following command in the directory of your local
repository for this application.

git push heroku master

This will push your most recently backed up or locally modified version of the web application
to your web application.

------------------------------------------

------------------------------------------
TO CONDUCT MAINTENANCE:

STEP 1:

Start Powershell with a link to the Web Application

STEP 2:

To place your web application in maintenance mode, run the following code:
heroku maintenance:on
This will place your web application in Maintenance mode giving users who visit the page a 
generic maintenance in progress page.

STEP 3:

To take your web application out of maintenance mode, run the following code:
heroku maintenance:off

------------------------------------------

------------------------------------------
TO HARD STOP/START APP:

STEP 1:

Start Powershell with a link to the Web Application

STEP 2:

To completely stop the application and prevent any traffic to the application, run the following code:
heroku ps:scale web=0
Running this code will stop any traffic from reaching the website.

STEP 3:

To restart the application, run the following code:
heroku ps:scale web=1

------------------------------------------