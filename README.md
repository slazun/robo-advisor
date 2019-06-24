# Robo Advisor Application Project

The goal of this project is to build a Python based application that uses real-time data from an API to assess stock prices and provide recommendations about whether to buy or sell. 

## Setting up Your Repository

To begin, fork this upstream repository by clicking the green "clone or download" button and selecting "Open in Desktop." This will create a copy of this repo but with your GitHub user name in the URL. From the newly opened GitHub desktop window, you can click "Open in Visual Studio" to have the ability to create and edit files in the text editor and connect seamlessly to your repo. From the navigation bar in GitHub desktop, select "Repository" then "Open in Terminal." In your cloned repo, you should have access to the "robo-advisor.py" application file.

## Environment Set Up

To run the app from the command-line, you need to first execute the following environment set-up steps. This is not necessary if you took the "Open in Terminal" approach from above. First, create and activate a new Anaconda virtual environment:

```
conda create -n stocks-env python=3.7 # (first time only)
conda activate stocks-env
```

When you are in this new environment, install the following required packages specified in the requirements.txt file in the repo:

```
pip install -r requirements.txt
pip install pytest # (only if you'll be writing tests)
```

Now, from within the environment you should be able to execute (from the command-line) the Python script found in the "robo-advisor.py" file: 

```
python robo_advisor.py
```

## Running the App

This application runs off of an API from AlphaVantage. It is necessary for you to obtain your own unique API key in order to run this application. You can obtain your key [here](https://www.alphavantage.co/). Please follow the instructions below to ensure your personal key is secure. 

1. Obtain your AlphaVantage API key and store it somewhere secure. Do not store it anywhere public or visible
2. Create a file called ".env" in your project repository
3. In the .env file, create a variable called ALPHAVANTAGE_API_KEY. 
4. Set this vairable equal to your secure API key in the .env file only. Do not put your key in the .py file directly. Ex: ALPHAVANTAGE_API_KEY="abc123" where "abc123" is replaced by your API key

The ALPHAVANTAGE_API_KEY variable is referenced in the robo-advisor.py file and will pull your key into the application to run it without displaying the key. 


