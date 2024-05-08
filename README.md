# Part 1
I use PostgreSQL as my database. When running my create.sql file, I use the commmand: psql -U postgres -h localhost -d api. I use postgres as my username, the host as localhost since I ran locally on my machine, and then saved the database to the name api which I later used to connect (important). The create.sql file creates a table called api_data that stores information about the timestamp and the JSON data received from the API calls.
In the Python file, process.py, this is where I actually call the API and connect to my table that I previously created. It runs for an hour, fetching data every minute for a total of 60 entries in api_data. I saved the api_data table into a csv file that is uploaded.  

# Part 1 - Analysis
Looking at the JSON data from in the csv file api_calls.csv, we can see that the factor follows a cubic progression where it takes the minute from the timestamp and cubes this value approximately. For instance, at time 01:29:50, the factor was calculated as 29^3 which is equal to 24389. When a new hour is reached like 02:00:13, the factor is calculated as 0^3 which is 1. This trend continues and it seems that the larger the factor is, the more precise the pi value is. At a factor of 1, pi is 4.0 while at a factor of 205379, pi is 3.141597522636734 which suggests some correlation between the two data variables fetched.

# Part 2
I utilized API calls to generate the weather given a city name, a random fact, and a random inspirational quote. The user can ask the Discord for these information using commands like !weather (city name), !fact, and !quote. 
