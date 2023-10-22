# FSC_py - Free Library REST API

![Logo](https://wepik.com/share/391d57ca-9cc8-49a9-a9df-3e1c30c5b908#rs=link)


The free library is a project allowing users to buy, rent or sell published books simply and quickly without traveling.


## Installation

Install dependecies by install the requirements.txt file

```bash
    cd FSC_py
    python install -r requirements.txt
```


### API Reference & services

There are three type on ressources: _users_, _sheets_ and _comments_

All services are built in the same logic but most of the endpoints can only be accessed through an authentified token


```http
  GET /users/
  POST /users/
  PATCH /users/
  DELETE /users/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Required**. jwt token |


``Get item``

the primary key in the sheets model is the book's ine

```http
  GET /users/${id}
  GET /sheets/${ine} 
  GET /comments/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |


#### Tech Stack

**Client:** Angular

**Server:** Python, django, djangorestframework, djangorestframework-simpleJWT

##### Run Locally

Clone the project

```bash
  git clone https://github.com/TSB04/FSC_py
```

Go to the project directory

```bash
  cd FSC_py
```

Install dependencies

```bash
  python Install -r requirements.txt
```

Start the server

```bash
  python manage.py runserver
```


 [Running Tests]

To run tests, run the following command

```bash
  python manage.py test
```


######  Authors & Related

- [@Thierno Sadou BARRY](https://www.github.com/tsb04)


The project is an REST API project so it is related with a fran app

[front](https://github.com/tsb04/FSC_py)