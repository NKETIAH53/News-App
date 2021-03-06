# News-App

## About
A simple app that enables visitors view current news uploaded daily by users on the app’s homepage. Each day, the homepage is set to display the news items available for the current day with the most recent upload as the topmost view.

Registered users can upvote or downvote news items as well as comment on them. Similarly, only registered users on this app can create news items.


## App Features
Currently, 
 1. visitors can:
    - View all items uploaded to the page
    - View details of a particular/ preferred news item
    - Create an account
  
 2. registered users can:
    - Create news items

### To run program:
1. Clone the repository:
```
  git clone <repository url>
```
2. Create a virtual environment with the directory name 'venv', run the command;
  ```
  python -m venv venv
  ```
3. Install app requirements
 ```
  pip install -r requirements.txt
```
4. Create a .env file with your SECRET_KEY

5. Run server as localhost on port 8000(default) or a preferred port
```
  python manage.py runserver <preferred port:optional>
```

### Tests
To run tests:
```
  python manage.py tests
```
