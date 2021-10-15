# womans-period
Django app to calculate a womans cycle within a given date range and provide the data through an api

### NOTE:
- There can only be one period cycle in the database at a time

- The cycle currently in the database is a test run cycle and can be edited



#### To Run the project: 
- clone Repository. 

- Navigate to project base directory in your terminal

- run the command **python manage.py runserver**


Usage:
##### GET http://localhost:8080/womens-health/api/create-cycles:

This will display a UI form data with the existing period cycle data in the database for the user to edit.


#### POST http://localhost:8080/womens-health/api/create-cycles:

With the following data:
- **Last Period**: as a date string in the format of "yyyy-mm-dd"
- **Cycle Average**: as an integer
- **Period Average**: as an integer
- **Start Date**: as a date string in the format of "yyyy-mm-dd"
- **End Date**:  as a date string in the format of "yyyy-mm-dd"

The response would be a JSON response with the value of the number of created cycles within the given date range.


#### GET http://localhost:8080/womens-health/api/cycle-event?date=a_date:

This will return a JSON response with an array of the event(s) happenning on the given date.

### NOTE: If no event was found, the JSON response returns an empty array.

