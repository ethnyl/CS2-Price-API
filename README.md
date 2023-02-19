# csmb
CS:GO Market Bot

This is a Flask web app that provides two API endpoints to get item data for both weapons and a cases in CS:GO. The item data is fetched by calling functions from another module called marketdata, which retrieves the highest buy order and lowest sell order price for an item, as well as its nameid.

## Installation

To run the Flask app, you need to install Python 3 and the required Python packages listed in the requirements.txt file. You can install the packages using the following command:

```
pip install -r requirements.txt
```

## Usage

To start the Flask app, run the following command:

```
python main.py
```

This will start the app in debug mode. The API endpoints are:

    POST /api/weapon: retrieves item data for a weapon based on its name, skin, wear, and stat.
    POST /api/case: retrieves item data for a case based on its name.

Both endpoints require a JSON object in the request body with the appropriate keys and values. If the item data is not available, the response will contain an error message.

## TO-DO
- Add proxy support
