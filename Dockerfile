FROM python:3.8
# CREATE A WORKING DIRECTORY FOR APP
WORKDIR /character
# CREATE A ENVIRONMENTAL VARIABLE TO COVER THE DATABASE
ENV DATABASE_URI = mysql+pymysql://root:password123@mysql_container:3306/racedb
# ANOTHER ONE FOR THE SECRET KEY
ENV SECRET=12345
# COPY THE APPLICATION FOLDER
COPY application /character/application
# COPY OVER THE PARTICULAR FILE EXCEPT THE TEST FOLDER
COPY app.py create.py requirements.txt /character/
# RUN THE REQUIREMENTS INSTALL FIRST
RUN pip install -r requirements.txt
# RUN THE DATABASE FIRST

#RUN python3 create.py

# NOW START THE APP

ENTRYPOINT ["python3", "app.py"]