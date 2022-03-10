# Fantasy Character Creation Application

## Summary:

The objective of this project is to demonstrate all current knowledge learned throughout the course and most importantly CRUD functionality of a web app with a relationship of two entities, using flask. The topic that I chose was for the ability of the user to create the name of a race and create a character based on the race submitted.
An image is built based on commands written on the Docker file.
Create a character option:

•	Name

•	Age

•	Gender

•	‘Class’ (Playstyle)

•	Description 

•	Date of creation

•	Race (From ‘create a race’)

### Additional requirements include to:
•	Document progress using Jira with Epics and story points

•	Full CRUD functionality of the website.

•	At least 75% coverage for the “routes.py”

•	Comments on the flask application (‘#’) to aid the user in explaining the functionality of some code.

•	Jenkins CI/CD pipeline to automate pytest, creating a docker image then pushing to docker hub and connecting to another Virtual Machine via SSH to deploy the application in a Docker Swarm

Entity Relationship Diagram:
![image](https://user-images.githubusercontent.com/97620482/157718248-89664b89-a54b-404e-baf7-dcf53725f1be.png)

This entity diagram shows the relationship between race and character. A single race can have many characters and a single character can only have one race. So, therefore, this is a one-to-many relationship.

## Planning:
### Initial stage
![image](https://user-images.githubusercontent.com/97620482/157718471-3f46eef3-5ebe-4e4d-a80d-4ea4e610b5f9.png)

### Final Stage 

![image](https://user-images.githubusercontent.com/97620482/157718600-5e2e108a-10a3-42ce-928e-6af276bdb1a3.png)


The resource used for my planning of this project is Jira- Kanban board.

•	To-do:  Any tasks/issues that need to be completed

•	User stories: Detailing what the user would want to be able to do and have.

•	In progress: Any tasks/issues that are currently being assessed and dealt with

•	Done: Tasks/issues that are completed 

## Application: 

![image](https://user-images.githubusercontent.com/97620482/157719143-2a8606eb-b4e4-4fc5-9a4e-788daca7708d.png)

The first step is to create a race and submit your selection

![image](https://user-images.githubusercontent.com/97620482/157719320-471c5d09-da53-4d57-9fc5-65ab7be114b3.png)

This allows your race to be present in the drop-down bar when building your character

![image](https://user-images.githubusercontent.com/97620482/157720922-52941204-7f7f-4474-a078-817435bdeb5c.png)

![image](https://user-images.githubusercontent.com/97620482/157721593-2c1ea717-cae4-4702-8907-1a253980ece5.png)

![image](https://user-images.githubusercontent.com/97620482/157721616-8abef7b2-b325-4ed9-97fe-c061c8afe8e7.png)

I created another race and character to demonstrate that ability to add new races.
Notice how I update the name of the race, the race that is bound to the character is also updated. The same happens when that race is deleted.

## CI/CD Pipeline: 

![image](https://user-images.githubusercontent.com/97620482/157735964-a74acafd-2203-420e-9b5c-12f8a4bc3e0d.png)

This diagram shows the workflow of each stage. It all begins with the planning stage, in this case, a Jira Kanban board is used. After a task is received, navigate to the version control system, Github. The code is pulled down to the local machine, changes are made on the code development environment (VS Code), and then pushed back up to the repository. Branching can be utilized to work on different features of the code, then merge them. Once the code has been pushed, a Jenkins pipeline is automatically triggered via a webhook. The Jenkins Pipeline initiates the testing. If there’s a problem with the code, the developers look back on the code for any debugging. The Docker images are built and if there are any issues with the pipeline itself, evaluate the execute shell as well as any parameters and credentials. Once the Build the successful, the flask application is deployed in a Docker swarm, on another Virtual Machine.

## Testing:

![image](https://user-images.githubusercontent.com/97620482/157736356-637d868c-10ee-421c-ba57-163c23354ea4.png)

![image](https://user-images.githubusercontent.com/97620482/157736681-bf551988-c48c-4d63-a1a2-0c537a99043e.png)


This tests the CRUD functionality of my application. The Coverage means how much of the lines of code are being run and tested. The main reason why the coverage is quite high is because of testing both the create, read and delete functions of the race and character The test results can be generated via an HTML, as so above to view. This process can be automated using Jenkins in a CI/CD pipeline, provided the correct commands are on the execute shell.

## Risk Assessment:

![image](https://user-images.githubusercontent.com/97620482/157744869-e5469d02-4966-415f-88a0-d607c61f7c6a.png)

## Known Issues with the application:

•	When submitting the same race name, the name will still be accepted and appended onto the race choices list.

•	Only the race of the corresponding character will be deleted rather than warning the user that the character will have to be deleted entirely. 

## Possible Improvements to Flask App: 

•	Implement a validator system on the Age, so certain Age ranges are acceptable

•	A login system where each user can save their character creations on their accounts.

•	Descriptive details of each feature such example, information about different classes and attributes

•	Randomization option to randomize selections.

•	More customization options for the character such as Height, Background story, hair color, etc.

•	Ability to save data when exiting out the page when filling out the boxes, rather than having to fill it out again.

•	Better overall design and navigation.

