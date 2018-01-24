# Github_Navigator
 Search GitHub repositories by given search term and present them as html page


The app searches GitHub repositories by given search term and present the results - Repository name, Author, Latest commit,  as an html page.

REQUIREMENTS
------------

Python3.3 or higher

DEPENDENCIES
------------

Use the venv module to setup a virtual enviroment by running 

  ```$ python3 -m venv <name-of-env>```

Then activate the virtual environment using
  
  ```$ source <path-to-the-virtualenv>/bin/active```

You should now be using your virtualenv (notice how the prompt of your shell has changed to show the active environment).

Install the dependecies:
  ```$ pip install -r dependencies```

The following depenedencies are installed:
    Flask: a micro webdevelopment framework for Python
    Requests: Used to perform http requests

RUN THE APP
-----------

To run the app activate the venv, and run the script:
  ```$ python application.py```

The application will be runnng on port 9876 and can be accessed on the browser as:

  http://localhost:9876/navigator?search_term=SEARCH_TERM

