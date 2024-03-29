<img src='./readme_images/logo.png' width="300" height="150"/> 

# F1 statistic dashboard (seasons 2000-2021)

Interactive dashboard created with Python, Dash-Plotly, Pandas and Numpy.


## Table of Contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
Dashboad created in educational purposes. It's main goal is to count down time to the next race, visualize results, speed, teams structures in seasons 2000 - 2021. <br>
Dataset used in project came from [Kaggle](htts://www.kaggle.com) service and was shared by user [Vopani](https://www.kaggle.com/rohanrao) based on CC0: Public Domain.<br>
[F1-World-Championship ](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020)
<br><br>
<img src='./readme_images/countdown.jpg' width="300" height="150"/><br>
<img src='./readme_images/constructors_and_teams.jpg' width="1200" height="350"/> <br>
<img src='./readme_images/track_speed.jpg' width="1200" height="350"/> 
<br><br>
## Technologies
    * Python 3.10.8
    * Dash 2.6.1
    * Flask 2.2.2
    * Plotly 5.10.0
## Setup
Dashboard has been deployed on DigitalOcean service and you can find it <a href="http://64.227.120.12:8484/" target="_blank">here</a>

Or if you want to run code locally:
* download code and unzip it,
* install requirements using `pip install -r requirements.txt`,
* run app with command `python f1_app.py`


