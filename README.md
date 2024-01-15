![baner](https://github.com/Ghosts6/Local-website/blob/main/img/Baner.png)

# 💻Local-website:
Here is the source code for our web project that i write for a company based on their needs,this project are quite similar to my  other [webproject](https://github.com/Ghosts6/webProject) purpose of this projects are same , i create this project to help tech team of company to manage they time and handleing requests from client This time I've been working on fixing some bugs and enhancing the overall quality of the project. ,also we've introduced a new design, improved the UI/UX, and made adjustments to enhance admin accessibility and the database system, among other improvements

🚨 Hint: For security and privacy reasons, I've made alterations to the code. For instance, certain functions like hashing and login different from the actual project. Additionally, I've replaced the company name, logo, and contact information in this representation to maintain confidentiality.


# ℹ️Directory Structure:
This project is structured into two components: the web part (myTicket_v2) focuses on configuring project settings and assets, while the web application part (Ticket) is dedicated to page creation, path configuration, and associated views
```bash
|____myTicket_v2
| |______pycache__
| |____Template
| |____Static
| | |____js
| | |____LineAwsome
| | | |____scss
| | | |____svg
| | | |____css
| | | |____fonts
| | |____css
| | |____img
| | | |____favicon
|____Ticket
| |______pycache__
| |____migrations
| | |______pycache__
|____staticfiles
| |____js
| |____LineAwsome
| | |____scss
| | |____svg
| | |____css
| | |____fonts
| |____css
| |____admin
| | |____js
| | | |____vendor
| | | | |____jquery
| | | | |____xregexp
| | | | |____select2
| | | | | |____i18n
| | | |____admin
| | |____css
| | | |____vendor
| | | | |____select2
| | |____img
| | | |____gis
| |____img
| | |____favicon
| |____favicon
|____fixture
```

# 👨‍💻Technology:
I created this project using MySQL and PostgreSQL for the database, hosted on a Linux server within a local network, designed the interface with Figma and Canva, implemented the frontend with HTML, CSS, and JS, and developed the backend using Django and Python
![Python](https://img.shields.io/badge/python-3670A0?style=plastic&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=plastic&logo=django&logoColor=white)![Flask](https://img.shields.io/badge/flask-%23000.svg?style=plastic&logo=flask&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=plastic&logo=javascript&logoColor=%23F7DF1E)
 ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=plastic&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=plastic&logo=css3&logoColor=white) ![MySQL](https://img.shields.io/badge/mysql-4479A1?style=plastic&logo=mysql&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/postgresql-336791?style=plastic&logo=postgresql&logoColor=white) ![Linux](https://img.shields.io/badge/linux-FCC624?style=plastic&logo=linux&logoColor=black)
 ![Bash](https://img.shields.io/badge/bash-4EAA25?style=plastic&logo=gnu-bash&logoColor=white)



# Bash:
Here we have bash file i created to manage project inside linux host,with this files IT team can easily made action like start and stop service and etc...
```bash
#! /bin/bash

# This bash file are created to help admin with management of webapplication 
# and it include file like start.sh stop.sh collect.sh and etc for manage service inside linux server host
# Hint! to use this files at first we need make them excuyeable :
# chmod +x file_name.sh

#-----------------------------------------   start.sh   ----------------------------------------------------------
# bash file to start services:   ./start.sh
echo "applying migrations"
python3 manage.py makemigrations
python3 manage.py migrate

echo "starting project....."
python3 manage.py runserver 0.0.0.0:8000
#-----------------------------------------    stop.sh   ----------------------------------------------------------
# bash file to stop services:   ./stop.sh
echo "Stopping project..."
kill $(lsof -t -i:8000)
#-----------------------------------------   collect.sh  ----------------------------------------------------------
# bash file for collecting static file: ./collect.sh
echo "Collecting static files ..."
python3 manage.py  collectstatic --noinput
#-----------------------------------------     log.sh    ----------------------------------------------------------
# bash file to return project logs: ./log.sh
echo "Display logs.... "
tail -n 50 myTicket_v2/logs/error.log
#----------------------------------------- custome_log.sh ----------------------------------------------------------
# bash file to return custome log i create inside setting.py : ./costume_log.sh
echo "setting.py custome log"

tail -n 50 myTicket_v2/mysitelog.txt
```


# Code-sample:
Login Page:

[login.webm](https://github.com/Ghosts6/Local-website/assets/95994481/ae6b7eca-941c-4482-9bd0-376e2fa0d3a9)


```html
{%load static %}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <link rel="icon" type="image/png" sizes="32x32" href="{% static 'img/favicon/favicon-32x32.png'%}">
  <link rel="icon" type="image/png" sizes="16x16" href="{% static 'img/favicon/favicon-16x16.png'%}">
  <link rel="manifest" href="/site.webmanifest">
  <link rel="mask-icon" href="/safari-pinned-tab.svg" color="#5bbad5">
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
  <link href="{% static 'css/login.css' %}" rel="stylesheet"> 
  <meta name="msapplication-TileColor" content="#da532c">
  <meta name="theme-color" content="#ffffff">
<title>Login page</title>
</head>
<body>

<a href="https://kiarashbashokian.com" target="_blank">
  <img src="{% static 'img/Untitled-removebg-preview.png' %}" alt="Your Logo" class="logo">
</a>

<div class="phone-icon" id="phoneIcon">
    <i class="fa-solid fa-phone icon"></i>
    <span class="tooltip" id="tooltip">Telephone: num1 - num2 - num3</span>
</div>

<div class="clock" id="clock">
    <span class="clockMessage" id="clockMessage">Iran Time Zone (GMT +3:30 hours)</span>
</div>

<div id="particles-js"></div>

<form action="{% url 'login' %}" method="post">
  {% csrf_token %}
  
  <div class="login-container">
    <div class="login-form">
      <div class="input-container">
        <input type="text" id="username" name="username" placeholder="Username">
      </div>

      <div class="input-container">
        <input type="password" id="password" name="password" placeholder="Password">
        <i class="far fa-eye" onclick="togglePassword()"></i>
      </div>

      <button id="loginButton" type="submit">Login</button>
      <p id="errorMessage" style="display: none; color: red;">Incorrect password or username</p>
      <span id="errorMessage" style="display: none; color: red;"></span>
              {% if error %}
        <p style="color: red;">{{ error }}</p>
      
      {% endif %}
      
    </div>
  </div>
</form>

<script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
<script src="{% static 'js/login.js' %}"></script>

</body>
</html>
```
```css
body {
  margin: 0;
  padding: 0;
  background-image: url('/static/img/Backgroundpic.png');
  background-size: cover;
  background-repeat: no-repeat;
  background-attachment: fixed;
  font-family: Arial, sans-serif;
}
.phone-icon {
  position: fixed;
  bottom: 20px;
  left: 20px;
  cursor: pointer;
}

.icon {
  font-size: 60px;
}

.logo {
  position: fixed;
  top: 20px;
  left: 20px;
  width: 60px;
  height: auto; 
}
.tooltip {
  display: none;
  position: absolute;
  background-color: rgba(0, 0, 0, 0.8);
  color: white;
  padding: 5px;
  border-radius: 5px;
  top: -70px;
  left: 50%; 
  transform: translateX(-50%);
}

.clock {
  position: fixed;
  top: 20px;
  right: 20px;
  font-size: 24px;
  color: white;
  cursor: pointer;
}

.clockMessage {
  display: none;
  position: absolute;
  background-color: rgba(0, 0, 0, 0.8);
  color: white;
  padding: 5px;
  border-radius: 5px;
  top: 30px;
  right: -150px; 
  width: 200px; 
  text-align: center;
}

.clock:hover .clockMessage {
  display: block;
}

.login-container {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.input-container {
  margin-bottom: 20px;
  display: flex;
  align-items: center;
}

input[type="text"],
input[type="password"] {
  padding: 25px 20px;
  border-radius: 30px; 
  border: 1px solid #ccc;
  font-size: 18px;
  width: 500px;
}

input[type="text"]:focus,
input[type="password"]:focus {
  outline: none;
  border-color: #007bff;
}

.input-container {
  position: relative;
  margin-bottom: 40px;
}

#password {
  padding-right: 35px; 
}

#password:focus + i {
  color: #007bff; 
}

.fa-eye {
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  cursor: pointer;
  color: #999;
}

#loginButton {
  padding: 25px 30px;
  background-image: linear-gradient(90deg, #0097b2, #7ed957);
  color: var(--black-color);
  border: none;
  border-radius: 30px;
  font-size: 20px;
  font-weight: bold; 
  width : 555px;
  cursor: pointer;
  transition: background-image 0.3s ease; 
}

#loginButton:hover {

  background-image: linear-gradient(90deg, #006f84, #5ca742); 
}

#particles-js {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1; 
}

.logo,
.phone-icon,
.clock,
.login-container {
  z-index: 1;
}
```
```js
function updateClock() {
  const clock = document.getElementById('clock');
  const iranTime = new Date().toLocaleString('en-US', { timeZone: 'Asia/Tehran', hour12: false });
  clock.textContent = iranTime.slice(-8);
}

setInterval(updateClock, 1000);

const clockElement = document.getElementById('clock');
const clockMessage = document.getElementById('clockMessage');
let clickCount = 0;

if (clockElement && clockMessage) {
  clockElement.addEventListener('mouseenter', function() {
    clockMessage.style.display = 'block';
  });

  clockElement.addEventListener('mouseleave', function() {
    clockMessage.style.display = 'none';
  });

  clockElement.addEventListener('click', function() {
    clickCount++;
    if (clickCount >= 5) {
      alert(clockMessage.textContent);
      clickCount = 0;
    }
  });
} else {
  console.error("Clock message element not found");
}

document.getElementById('phoneIcon').addEventListener('click', function() {
  const tooltip = document.getElementById('tooltip');
  tooltip.style.display = tooltip.style.display === 'block' ? 'none' : 'block';
});

function togglePassword() {
  const passwordField = document.getElementById('password');

  if (passwordField.type === 'password') {
    passwordField.type = 'text';
  } else {
    passwordField.type = 'password';
  }
}

function togglePassword() {
  const passwordField = document.getElementById('password');

  if (passwordField.type === 'password') {
    passwordField.type = 'text';
  } else {
    passwordField.type = 'password';
  }
}

const errorMessage = document.getElementById('errorMessage');

function displayErrorMessage(message) {
    errorMessage.textContent = message;
    errorMessage.style.display = 'block';
}

document.getElementById('loginButton').addEventListener('click', function(event) {
    event.preventDefault(); 

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (!username || !password) {
        displayErrorMessage('Fill in all the necessary data');
        return;
    }

    event.currentTarget.closest('form').submit();
});

// Add Particle.js initialization
particlesJS("particles-js", {
  particles: {
    number: { value: 80, density: { enable: true, value_area: 800 } },
    color: { value: "#ffffff" },
    shape: { type: "circle", stroke: { width: 0, color: "#000000" }, polygon: { nb_sides: 5 }, image: { src: "img/github.svg", width: 100, height: 100 } },
    opacity: { value: 0.5, random: false, anim: { enable: false, speed: 1, opacity_min: 0.1, sync: false } },
    size: { value: 3, random: true, anim: { enable: false, speed: 40, size_min: 0.1, sync: false } },
    line_linked: { enable: true, distance: 150, color: "#ffffff", opacity: 0.4, width: 1 },
    move: { enable: true, speed: 6, direction: "none", random: false, straight: false, out_mode: "out", bounce: false, attract: { enable: false, rotateX: 600, rotateY: 1200 } },
  },
  interactivity: {
    detect_on: "canvas",
    events: { onhover: { enable: true, mode: "repulse" }, onclick: { enable: true, mode: "push" }, resize: true },
    modes: { grab: { distance: 400, line_linked: { opacity: 1 } }, bubble: { distance: 400, size: 40, duration: 2, opacity: 8, speed: 3 }, repulse: { distance: 200, duration: 0.4 }, push: { particles_nb: 4 }, remove: { particles_nb: 2 } },
  },
  retina_detect: true,
});
```
```python
def user_login(request):
    error_message = None
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            error_message = 'Fill in all the necessary data'
        else:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('admin:index')
                else:
                    return redirect('main')
            else:
                try:
                    failed_login_user = User.objects.get(username=username)
                    failed_login_user.profile.failed_login_attempts += 1
                    failed_login_user.profile.last_login_attempt = timezone.now()
                    failed_login_user.profile.save()

                    if failed_login_user.profile.failed_login_attempts > 10:
                        lock_time = failed_login_user.profile.last_login_attempt + timedelta(minutes=5)
                        if timezone.now() < lock_time:
                            return render(request, 'locked.html')
                        else:
                            failed_login_user.profile.failed_login_attempts = 0
                            failed_login_user.profile.save()
                except User.DoesNotExist:
                    pass  
                
                error_message = 'Incorrect password or username'

    return render(request, 'login.html', {'error': error_message})
```
Main Page:
[main.webm](https://github.com/Ghosts6/Local-website/assets/95994481/e10e6b96-1475-4990-8974-df26c461abe7)

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <link rel="icon" type="image/png" sizes="32x32" href="{% static 'img/favicon/favicon-32x32.png'%}">
  <link rel="icon" type="image/png" sizes="16x16" href="{% static 'img/favicon/favicon-16x16.png'%}">
  <link rel="manifest" href="/site.webmanifest">
  <link rel="mask-icon" href="/safari-pinned-tab.svg" color="#5bbad5">
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
  <link rel= "stylesheet" href= "{% static 'LineAwsome/css/line-awesome.min.css' %}" >
  <link href="{% static 'css/main.css' %}" rel="stylesheet"> 
  <meta name="msapplication-TileColor" content="#da532c">
  <meta name="theme-color" content="#ffffff">
<title>Main page</title>
</head>
<body>

<a href="https://kiarashbashokian.com" target="_blank">
  <img src="{% static 'img/Untitled-removebg-preview.png' %}" alt="Your Logo" class="logo">
</a>

<div class="phone-icon" id="phoneIcon">
    <i class="fa-solid fa-phone icon"></i>
    <span class="tooltip" id="tooltip">Telephone: num1 - num2 - num3</span>
</div>

<div class="clock" id="clock">
    <span class="clockMessage" id="clockMessage">Iran Time Zone (GMT +3:30 hours)</span>
</div>

   <div class="main-container">
    <div class="form-container">
      <form action="{% url 'main' %}" method="post" enctype="multipart/form-data">
        <div class="input-container">
          <label for="name">Name:</label>
          <input type="text" id="name" name="name" placeholder="Enter your name">
        </div>

        <div class="input-container">
              <label for="last_name">Last Name:</label>
              <input type="text" id="last_name" name="last_name" placeholder="Enter your last name">
        </div>

        <div class="input-container">
               <label for="department_name">Department Name:</label>
               <input type="text" id="department_name" name="department_name" placeholder="Enter your department name">
        </div>
        
        <div class="input-container">
          <label for="request_type">Request Type:</label>
          <select id="request_type" name="request_type" class="request-type-select">
          <option value="" selected disabled>Select type of request</option>
          <option value="hardwareissue">Hardware Issue</option>
          <option value="softwareissue">Software Issue</option>
          <option value="update&upgrade">Update & Upgrade</option>
          <option value="boost">Boost</option>
          <option value="repair">Repair</option>
          <option value="installprogram">Install Program</option>
        </select>
      </div>
      <div class="input-container">
    <label for="attachment" id="attachLabel">
      <i class="las la-paperclip" id="attachIcon"></i> Attach file
    </label>
    <input type="file" id="attachment" name="attachment" style="display: none;">
      </div> 
        <div class="input-container">
             <label for="description">Description:</label>
             <textarea id="description" name="description" class="description-textarea" placeholder="Enter description"></textarea>
        </div>

        <!-- CSRF token field (hidden) -->
        <span class="csrf-field">{% csrf_token %}</span>
        <button id="submitButton" type="submit">Submit</button>
        <a href="{% url 'status' %}" class="ticket-history-button">Ticket History</a>
        <span id="errorMessage" style="display: none; color: red;"></span>
      </form>
    </div>
  </div>


<script src="{% static 'js/main.js' %}"></script>

</body>
</html>
```
```css
body {
  margin: 0;
  padding: 0;
  background-image: url('/static/img/Backgroundpic.png'); 
  background-size: cover;
  background-repeat: no-repeat;
  background-attachment: fixed;
  font-family: Arial, sans-serif;
}
.phone-icon {
  position: fixed;
  bottom: 20px;
  left: 20px;
  cursor: pointer;
}

.icon {
  font-size: 60px; 
}

.logo {
  position: fixed;
  top: 20px;
  left: 20px;
  width: 60px;
  height: auto; 
}
.tooltip {
  display: none;
  position: absolute;
  background-color: rgba(0, 0, 0, 0.8);
  color: white;
  padding: 5px;
  border-radius: 5px;
  top: -70px;
  left: 50%; 
  transform: translateX(-50%);
}

.clock {
  position: fixed;
  top: 20px;
  right: 20px;
  font-size: 24px;
  color: white;
  cursor: pointer;
}

.clockMessage {
  display: none;
  position: absolute;
  background-color: rgba(0, 0, 0, 0.8);
  color: white;
  padding: 5px;
  border-radius: 5px;
  top: 30px;
  right: -150px; 
  width: 200px; 
  text-align: center;
}

.clock:hover .clockMessage {
  display: block;
}
.main-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 30px;
}

.form-container form {
  padding: 0;
  border: none; 
  margin: 30px;
}

.input-container {
  margin-bottom: 15px;
  display: flex;
  flex-direction: column;
  position: relative; 
}

.input-container label {
  margin-bottom: 5px;
  font-weight: bold;
  color: black;
}

.input-container input[type="text"],
.input-container select,
.input-container textarea {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 30px; 
  font-size: 18px;
  width: 500px;
}

.description-textarea {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 30px;
  font-size: 18px;
  width: 500px;
  height: 150px; 
}

.csrf-field {
  display: none;
}

#submitButton {
  height: 40px!important;
  line-height: 10px;
  padding: 25px 30px;
  background-image: linear-gradient(90deg, #0097b2, #7ed957);
  color: var(--black-color);
  border: none;
  border-radius: 30px;
  font-size: 20px;
  font-weight: bold;
  width: 555px;
  cursor: pointer;
  transition: background-image 0.3s ease;
}

#submitButton:hover {
  background-image: linear-gradient(90deg, #006f84, #5ca742);
}
#errorMessage {
  display: none;
  text-align: center;
  margin-top: 10px;
  color: red;
  font-weight: bold;
}

#attachLabel {
  cursor: pointer;
  padding: 10px 20px;
  background-color: #fff;
  border-radius: 30px;
  border: 2px solid #ccc;
  height: auto;
  width: 470px; 
  display: flex;
  align-items: center;
}

#attachIcon {
  font-size: 24px;
  margin-right: 1px;
}

#attachIcon,
.attach-text {
  cursor: pointer;
}

#attachLabel:hover {
  border-color: #0097b2;
}

.ticket-history-button {
  margin-top: 10px; 
  padding: 5px;
  height: 40px !important;
  line-height: 40px;
  background-image: linear-gradient(90deg, #0097b2, #7ed957);
  color: var(--black-color);
  border: none;
  border-radius: 30px;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: background-image 0.3s ease;
  text-align: center;
  text-decoration: none;
  margin-top: 10px; 
  display: block;  
}

.ticket-history-button:hover {
  background-image: linear-gradient(90deg, #006f84, #5ca742);

}
```
```js
function updateClock() {
  const clock = document.getElementById('clock');
  const iranTime = new Date().toLocaleString('en-US', { timeZone: 'Asia/Tehran', hour12: false });
  clock.textContent = iranTime.slice(-8);
}

setInterval(updateClock, 1000);

const clockElement = document.getElementById('clock');
const clockMessage = document.getElementById('clockMessage');
let clickCount = 0;

if (clockElement && clockMessage) {
  clockElement.addEventListener('mouseenter', function() {
    clockMessage.style.display = 'block';
  });

  clockElement.addEventListener('mouseleave', function() {
    clockMessage.style.display = 'none';
  });

  clockElement.addEventListener('click', function() {
    clickCount++;
    if (clickCount >= 5) {
      alert(clockMessage.textContent);
      clickCount = 0;
    }
  });
} else {
  console.error("Clock message element not found");
}

document.getElementById('phoneIcon').addEventListener('click', function() {
  const tooltip = document.getElementById('tooltip');
  tooltip.style.display = tooltip.style.display === 'block' ? 'none' : 'block';
});

document.getElementById('submitButton').addEventListener('click', function(event) {
    const inputFields = document.querySelectorAll('input[type="text"], select, textarea');

    let isFormValid = true;

    inputFields.forEach(function(field) {
        if (field.value.trim() === '') {
            isFormValid = false;
            field.style.border = '2px solid red'; 
        } else {
            field.style.border = ''; 
        }
    });

    if (!isFormValid) {
        const errorMessage = document.getElementById('errorMessage');
        errorMessage.textContent = 'Fill all the fields';
        errorMessage.style.display = 'block';
        errorMessage.style.color = 'red';
        event.preventDefault();  
    }
});
```
```python
def main(request):
    if request.method == 'POST':
        # Set the status field
        request.POST = request.POST.copy()
        request.POST['status'] = 'Pending'

        form = TicketForm(request.POST, request.FILES)  

        if form.is_valid():
            name = form.cleaned_data['name']
            lastname = form.cleaned_data['last_name']
            department = form.cleaned_data['department_name']
            request_type = form.cleaned_data['request_type']  
            description = form.cleaned_data['description']
            attachment = request.FILES.get('attachment')

            ticket = Ticket(
                user=request.user,
                name=name,
                last_name=lastname,
                department_name=department,
                request_type=request_type,
                description=description,
                attachment=attachment,
                status='Pending',  
            )
            ticket.save()

            return redirect('status')  
    else:
        form = TicketForm()

    return render(request, 'main.html', {'form': form})

def locked(request):
    return render(request, 'locked.html')
```
