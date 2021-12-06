# Anyfin-Pythondev

### Built With

* [Python](https://python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Docker](https://https://www.docker.com/)

## Design



 
## Installation 
> 1: clone the project in to your device or server


> 2: go into project directory


> 3: run command 
` sudo docker-compose up`


> 4: send your requests to http://localhost/credit-policies or http://localhost:5000/credit-policies


## Request and Response examples

request 1:
 ```sh
 {
    "data":{
                "customer_income": 1000,
                "customer_debt": 500,
                "payment_remarks_12m": 0,
                "payment_remarks": 1,
                "customer_age": 20
            }
}
   ```

response 1:
 ```sh
 {
    "category": "ACCEPT",
    "message": "credit check passed",
    "status": 200
}
   ```


request 2:
 ```sh
{
    "data":{
                "customer_income": 1000,
                "customer_debt": 5000,
                "payment_remarks_12m": 3,
                "payment_remarks": 1,
                "customer_age": 20
            }
}
   ```

response 2:
 ```sh
{
    "category": "REJECT",
    "message": [
        "HIGH_DEBT_FOR_INCOME",
        "PAYMENT_REMARKS_12M"
    ],
    "status": 200
}
   ```

request 3:
 ```sh
{
    "data":{
                "customer_income": 100,
                "customer_debt": 5000,
                "payment_remarks_12m": 13,
                "payment_remarks": 4,
                "customer_age": 17
            }
}}
   ```

response 3:
 ```sh
{
    "category": "REJECT",
    "message": [
        "LOW_INCOME",
        "HIGH_DEBT_FOR_INCOME",
        "PAYMENT_REMARKS_12M",
        "PAYMENT_REMARKS",
        "UNDERAGE"
    ],
    "status": 200
}
   ```

request 4:
 ```sh
{
    "data":{
                "customer_income": 100,
                "customer_debt": 50,
                "payment_remarks_12m": 0,
                "payment_remarks": 1,
                "customer_age": 22
            }
}
   ```

response 4:
 ```sh
{
    "category": "REJECT",
    "message": [
        "LOW_INCOME"
    ],
    "status": 200
}
   ```

request 5:
 ```sh
{
    "data":{
                "customer_income": 10000,
                "customer_debt": 505,
                "payment_remarks_12m": 0,
                "customer_age": 34
            }
}
   ```

response 5:
 ```sh
{
    "message": [
        "payment_remarks"
    ],
    "status": 500
}
   ```




<!-- CONTACT -->
## Contact

Parastoo Maleki - parastoomaleki100@gmail.com
