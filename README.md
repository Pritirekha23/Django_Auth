## Django Full Authentication Project

## Features :
- User Registration
- User Login
- Password Reset with Email Verification
- Session Management
- Secured Pages for Logged-in Users Only
- Custom User Feedback with Django Messages

##  Features in Detail
### User Registration

![alt text](<Screenshot 2024-12-05 231641.png>)
### User Login
- Registered users can log in using their username and password. Invalid credentials will prompt a feedback message.
![alt text](image.png)
###  Forgot Password
- Users can request a password reset by entering a valid registered email.
- A reset link will be sent to the provided email address.

![alt text](img/image-1.png)

![alt text](image-2.png)
### email sent msg
- Users can set a new password by following the link in the email.
- Once submitted, the password is updated, and the user can log in with the new credentials.
![alt text](image-3.png)

### Password Reset
![alt text](image-4.png)
![alt text](image-5.png)
- here we can reset our password

### admin panel
- Accessible only to admin users, the Django admin panel allows management of users, permissions, and other database models.
![alt text](image-6.png)
![alt text](image-11.png)
###  Secure Pages - login sucess
- After a successful login, users can access restricted pages available only to authenticated users.
![alt text](image-9.png)

## smith is user so smith can't access django admin panel
- Non-admin users, like Smith, cannot access the Django admin panel. A permission error will be displayed.
![alt text](image-10.png)