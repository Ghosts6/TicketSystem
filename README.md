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
![Python](https://img.shields.io/badge/python-3670A0?style=plastic&logo=python&logoColor=ffdd54)![Django](https://img.shields.io/badge/django-%23092E20.svg?style=plastic&logo=django&logoColor=white)![Flask](https://img.shields.io/badge/flask-%23000.svg?style=plastic&logo=flask&logoColor=white)![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=plastic&logo=javascript&logoColor=%23F7DF1E)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=plastic&logo=html5&logoColor=white)![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=plastic&logo=css3&logoColor=white)


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
