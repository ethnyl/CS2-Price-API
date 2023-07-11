# CS:GO Market API
Implementation for CS:GO Market Bot

This is a Flask web app that provides two API endpoints to get item data for weapons, cases, and items in CS:GO. The item data is fetched by calling functions from another module called marketdata, which retrieves the highest buy order and lowest sell order price for an item, as well as its nameid.

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

# API Documentation

## /api/weapon

Returns data about a weapon skin in the game.

### Method

POST

### Request Body

| Parameter | Type    | Description                                                                                       | Example        |
| --------- | ------- | ------------------------------------------------------------------------------------------------- | -------------- |
| gun       | string  | The name of the weapon.                                                                           | "AK-47"        |
| skin      | string  | The name of the skin for the weapon.                                                              | "Asiimov"      |
| wear      | integer | The wear of the skin, represented by a number between 1 (Factory New) and 5 (Battle-Scarred).     | 3              |
| stat      | integer | Whether the skin has StatTrak&trade; or not. 1 represents that the skin has StatTrak&trade;, and 0 represents that it does not. | 1 |

### Example Request

```http
POST /api/weapon HTTP/1.1
Content-Type: application/json

{
 "gun": "AK-47",
 "skin": "Redline",
 "wear": 3,
 "stat": 1
}
```

Would return data for a StatTrak AK-47 | Redline (Field-Tested), such as
```
{
    "buy_req": 54.25,
    "nameid": "7180207",
    "sell_req": 60.79,
    "volume": 29
}
```

## /api/case

Returns data about a case or item. The item functionality is limited and not reccommended to use. 

### Method

POST

### Request Body

| Parameter | Type   | Description       | Example          |
| --------- | ------ | ----------------- | ---------------- |
| case      | string | The name of the case. | "Snakebite Case" |

### Example Request

```http
POST /api/case HTTP/1.1
Content-Type: application/json

{
 "case": "Snakebite Case"
}
```

Would return data for the Snakebite Case, such as
```
{
    "buy_req": 0.37,
    "nameid": "176240926",
    "sell_req": 0.38
}
```
Note: volume data not avaliable for cases.

## TO-DO
- Add proxy support (steam market ratelimit)
    - volume function might affect ratelimits?
- Add other buy/sell orders
- Make /api/case have better item functionality.
