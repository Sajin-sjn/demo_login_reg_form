# Sample Project
This is a simple project having two usertypes Admin and User. User can register and the user details are stored in the MySql database. Then, after successfull registration user can navigate to the login page and can enter the username and password that given at time of the registration and if the login criterias are successfull, user will redirect to the userhome page.Admin can simply navigate to the login page as he doesn't have registration, manually inserted username and password in the MySql table. After successfull login admin will redirect to the admin home page.

## Technologies used
- **Language:** Python
- **Framework:** Flask
- **Database:** MySql
- **Front-end:** HTML,CSS,Bootstrap
- **Version control:** Git

## UI
### Home page

<img src="/static/assets/img/home.png" alt="Description" width="400" height="250">

### Login page

<img src="/static/assets/img/login.png" alt="Description" width="400" height="250">

### Registration page

<img src="/static/assets/img/registration.png" alt="Description" width="400" height="250">


## Installation
1. 
    - **Server:** Wamp server
    - **MySql GUI:** Sqlyog

2. Clone the repo
```bash
   git clone "https://github.com/Sajin-sjn/demo_login_reg_form.git"
```

3. Install Flask package if not installed
   -  python -> file location -> file location -> scripts -> navigate to directory - cmd ->
4.
```bash
    pip install flask
```
5.
```bash
      pip install mysql-connector
```

6. Import the demo.sql to SqlYog


4. Run main.py
5. Navigate to the the url.