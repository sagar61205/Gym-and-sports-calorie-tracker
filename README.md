# Gym and sports calorie tracker
A simple ML based website which calculates calculates calories burnt by weighing in various parameters such as TotalSteps, TotalDistance, VeryActiveDistance etc.

## Application interface screenshot:
![Screenshot 2021-07-05 020940](https://user-images.githubusercontent.com/5305547/126999828-44299d61-5398-4fb7-860f-6d6dd7af8db6.png)


## Application screenshot showing what the application does:
![Screenshot 2021-07-05 021054](https://user-images.githubusercontent.com/5305547/127000193-452f106b-849c-445a-af4b-001815aca210.png)

# Features:
1.	Id: The customer ID
2.	ActivityDate: The date for which the activity is getting tracked.
3.	TotalSteps:  Total Steps taken on that day.
4.	TotalDistance: Total distance covered.
5.	TrackerDistance: Distance as per the tracker
6.	LoggedActivitiesDistance: Logged 
7.	VeryActiveDistance: The distance for which the user was the most active. 
8.	ModeratelyActiveDistance: The distance for which the user was moderately active.
9.	LightActiveDistance: The distance for which the user was the least active.
10.	SedentaryActiveDistance: The distance for which the user was almost inactive.
11.	VeryActiveMinutes: The number of minutes for the most activity.
12.	FairlyActiveMinutes: The number of minutes for moderately activity.
13.	LightlyActiveMinutes: The number of minutes for the least activity
14.	SedentaryMinutes: The number of minutes for almost no activity
15.	Calories(Target): The calories burnt. 


This is a POC(Proof of concept) kind-of project. The data used here comes up with no guarantee from the creator. So, don't use it for making calorie tracking decisions. If you do so, the creator is not responsible for anything. However, this project presents the idea that how we can use ML into practice.

## MOTIVATION 💪
Fitness is one of the fastest growing areas. Everybu is moving towards fitness especially after the Covid-19 pandemic. This app is just one small and humble effort to help fitness enthusiasts for their short and long term fitness goals. 

In this project, I present a website in which the predictions are implemented as; Batch File PRediction(which predicts and generates a new file with predicted values based in the pre-trained model. 
For the calories tracking application, the user can input the data and the application will predict the number of calories burnt.


## Built with 🛠️
<p align="left"> <a href="https://www.arduino.cc/" target="_blank"> <img src="https://cdn.worldvectorlogo.com/logos/arduino-1.svg" alt="arduino" width="40" height="40"/> </a> <a href="https://www.gnu.org/software/bash/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/gnu_bash/gnu_bash-icon.svg" alt="bash" width="40" height="40"/> </a> <a href="https://getbootstrap.com" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a><a href="https://flask.palletsprojects.com/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://heroku.com" target="_blank"> <img src="https://www.vectorlogo.zone/logos/heroku/heroku-icon.svg" alt="heroku" width="40" height="40"/> </a> <a href="https://www.mysql.com/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a><a href="https://postman.com" target="_blank"> <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" alt="postman" width="40" height="40"/> </a><a href="https://scikit-learn.org/" target="_blank"> <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikit_learn" width="40" height="40"/> </a></p>       

    

## DEPLOYMENT 🚀
Deployment is done using deploy branch.<br/>
This website is deployed at Heroku.<br/>
You can access it here: https://gym-and-sports-calorie-tracker.herokuapp.com/ <br/>
Note: The website may take a minute to load sometimes, as the server may be in hibernate state.<br/>
How to use? <br/>
Value-based-prediction ==> enter the corresponding values and it will fetch the number of calories burnt.<br/>
File-based-prediction  ==> Click in 'default file prediction' to see the prediction on the already trained model OR Enter an absolute file path and clixk on 'Custom file predict'.



## Application screenshot for the 'About' section.
![Screenshot 2021-07-05 021125](https://user-images.githubusercontent.com/5305547/127006780-e9db9aab-a120-4e03-914c-0b6c4e60117e.png)
## Application screenshot for the health benefits of calorie tracking:
![Screenshot 2021-07-05 021147](https://user-images.githubusercontent.com/5305547/127006914-98cb98d5-9f91-44cf-ab01-7890a3e3cc9d.png)

## Application screenshot for batch file prediction. Here deafult prediction takes place on pre-trained dataset. A custom file file prediction can also be done.
![Screenshot 2021-07-05 021215](https://user-images.githubusercontent.com/5305547/127007072-be80bb04-646c-49b2-8eea-94059ad1bcfe.png)

## Application screenshot for the important information section:
![Screenshot 2021-07-05 021229](https://user-images.githubusercontent.com/5305547/127007130-bef97d9b-bb39-47e1-8c31-cbfbdc27869d.png)

## Prediction:
![fitbit gif](https://user-images.githubusercontent.com/5305547/127011833-bf847429-45ca-4909-9020-4403d4e4a3bc.gif)


