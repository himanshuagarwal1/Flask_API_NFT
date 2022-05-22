# Flask-RESTful API project template

This project shows one of the possible ways to implement RESTful API server for Eterlast NFT Project.

There are implemented three models: User, Collections and NFT

Main libraries used:
1. Flask - Flask framework
2. Flask-RESTful - restful API library.
3. Flask-SQLAlchemy - adds support for SQLAlchemy ORM.

Project structure:
```



├── README.md
├── app.py
├── endpoints
│   ├── __init__.py
│   ├── collection.py
│   │── NFT.py
│   └── user.py
│
├── data_models
│   ├── __init__.py
│   └── All_models
│
├── data.py
├── database.db
├── requirements.txt
└── test.py
```


* app.py - flask application initialization.
* test.py - unittest for endpoints.
* database.db - database 
* requirements.txt  - requirements to run this projects 
* data_models - contains all data models.
* endpoints - contains all endpoints and resources for API endpoints.

## Running 

1. Clone repository.
2. pip install -r requirements.txt
3. Run command: python app.py

# Running tests
1. this unittests is covered around the endpoints of API
2. before running the tests make sure the flask app is runnig 
3. Open a new terminal and run test.py in that. 

## Usage
### Users endpoint

POST http://127.0.0.1:5000/users

REQUEST
```json
{
         "user_wallet": 3
}
```
RESPONSE
```json
{
   "id": 4,
    "user_wallet": 2
}


REQUEST
GET http://127.0.0.1:5000/users/1

RESPONSE
```json
{
   "id": 1,
    "user_wallet": 3
}

GET http://127.0.0.1:5000/users

RESPONSE
```json
{
    "count": 4,
    "user": [
        {
            "id": 1,
            "user_wallet": 1
        },
        {
            "id": 2,
            "user_wallet": 2
        },
        {
            "id": 3,
            "user_wallet": 3
        },
        {
            "id": 4,
            "user_wallet": 2
        }
    ]
}


### Collections endpoint

POST http://127.0.0.1:5000/collections 

REQUEST
```json
{
    "uuid": 5,
    "name":"himanshu Agarwal",
    "description":"this is himanshu Agarwal description",
    "creator_network":5165165551,    
    "creator":4 
    }



```
RESPONSE
```json
{
    "id": 2,
    "uuid": 5,
    "name": "himanshu Agarwal",
    "description": "this is himanshu Agarwal description",
    "creator": [
        {
            "id": 2,
            "user_wallet": 2
        },
        {
            "id": 4,
            "user_wallet": 2
        }
    ],
    "creator_network": 5165165551
}

REQUEST 

GET http://127.0.0.1:5000/collections

RESPONSE
```json
{
    "count": 2,
    "collections": [
        {
            "id": 1,
            "uuid": 1,
            "name": "himandhu",
            "description": "this is himanshu about mr",
            "creator": [
                {
                    "id": 1,
                    "user_wallet": 1
                }
            ],
            "creator_network": 51651651
        },
        {
            "id": 2,
            "uuid": 5,
            "name": "himanshu Agarwal",
            "description": "this is himanshu Agarwal description",
            "creator": [
                {
                    "id": 2,
                    "user_wallet": 2
                },
                {
                    "id": 4,
                    "user_wallet": 2
                }
            ],
            "creator_network": 5165165551
        }
    ]
}




REQUEST

GET http://127.0.0.1:5000/collections/2


RESPONSE
```json
{
    "id": 2,
    "uuid": 5,
    "name": "himanshu Agarwal",
    "description": "this is himanshu Agarwal description",
    "creator": [
        {
            "id": 2,
            "user_wallet": 2
        },
        {
            "id": 4,
            "user_wallet": 2
        }
    ],
    "creator_network": 5165165551
}


### NFT endpoint

POST http://127.0.0.1:5000/NFT 

REQUEST
```json
{       
    "asset_id": 13,
    "name":"hiamdhu",
    "picture":"picture.html",
    "external_link":"sdhguwsdguwnt",
    "description":"dfghdehdrty",
    "collection":2,
    "supply": 464,
    "royalties": 54156,
    "date_of_creation":"2022-11-31",
    "buyer": 544654, 
}
```
RESPONSE
```json
{
    "id": 6,
    "asset_id": 13,
    "name": "hiamdhu",
    "picture": "picture.html",
    "external_link": "sdhguwsdguwnt",
    "description": "dfghdehdrty",
    "collection": [],
    "supply": 464,
    "royalties": 54156,
    "date_of_creation": "2022-11-31",
    "buyer": "544654"
}


REQUEST
GET http://127.0.0.1:5000/NFT/1


RESPONSE
```json
{
    "id": 1,
    "asset_id": 12,
    "name": "hsidf",
    "picture": "asdfhsuifbu.html",
    "external_link": "sdgsgg",
    "description": "hingwetg",
    "collection": [
        {
            "id": 1,
            "uuid": 1
        }
    ],
    "supply": 5456,
    "royalties": 54156,
    "date_of_creation": "2021-11-25",
    "buyer": "56464"
}

GET http://127.0.0.1:5000/NFT

RESPONSE
```json
{
    "count": 9,
    "user": [
  
        {
            "id": 1,
            "asset_id": 12,
            "name": "hsidf",
            "picture": "asdfhsuifbu.html",
            "external_link": "sdgsgg",
            "description": "hingwetg",
            "collection": [
                {
                    "id": 1,
                    "uuid": 1
                }
            ],
            "supply": 5456,
            "royalties": 54156,
            "date_of_creation": "2021-11-25",
            "buyer": "56464"
        },
   
        {
            "id": 5,
            "asset_id": 12,
            "name": "hsidf",
            "picture": "asdfhsuifbu.html",
            "external_link": "sdgsgg",
            "description": "hingwetg",
            "collection": [
                {
                    "id": 2,
                    "uuid": 5
                }
            ],
            "supply": 5456,
            "royalties": 54156,
            "date_of_creation": "2022-11-30",
            "buyer": "56464"
        },
    
        {
            "id": 9,
            "asset_id": 15,
            "name": "Himanshu Agarwal",
            "picture": "picturedetails.html",
            "external_link": "externalLink_html",
            "description": "description.html",
            "collection": [],
            "supply": 46455,
            "royalties": 54156,
            "date_of_creation": "2022-11-31",
            "buyer": "544654"
        }
    ]
}



## Important ###

* To add a User to creator make sure to pass the valid user_wallet which is already present in collections id meaning collection.id = User.user_wallet Important

* similarly to add a collection to the NFT please pass a Valid uuid which is already present in the NFT  meaning  NFT.id = collections.uuid

Requiremnts wasn't clear to me so I have made certain assumptions 