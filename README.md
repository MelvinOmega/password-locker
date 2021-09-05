# PASSWORD LOCKER

## By [Melvin Omega] (https://github.com/MelvinOmega/)

## Description
This is a python application that is run in the terminal which allows users to create new accounts and store details such as usernames and passwords.

## User Stories
This are the behaviors that are too be met when the user uses this application.

As a user, I would like to:
* create a new account or login to an existing account.
* store my existing login credentials.
* genetate a new password for a new account.

# Specifications

| Behavior |Input | Output|
| :-------------- | :----------------: | --------------------: |
| Display codes for navigation | **In terminal; $./password_locker.py** | Welcome to password locker, choose an option: ca-Create Account, li-Log In, ex-Exit |

<!-- Welcome to password locker, choose an option: ca-Create Account, li-Log In, ex-Exit | -->
| Display prompt for creating an account | **Enter: ca** | Enter your first name, last name and password |
| Display prompt for login in | **Enter: li** | Enter your account name and password |
<!-- | Display codes for navigation | **Successful login** | Choose an option: cc - Create Credential, dc - Display Credentials, copy - Copy Credential, ex - exit |
| Display prompt for creating a credential | **Enter: cc** | Enter the site name, your username and password |
| Display a list of credentials | **Enter: dc** | Prints a list of saved credentials |
| Display prompt for which credential to copy | **Enter: copy** | Enter the site name of the credential you wish to copy. | -->
| Exit application | **Enter: ex** | Exit the current navigation stage |