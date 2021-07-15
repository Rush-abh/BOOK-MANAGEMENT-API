# BOOK MANAGEMENT API

DJANGO REST FRAMEWORK API

##### Developed By:

[Rushabh Pancholi](https://www.linkedin.com/in/rushabh-pancholi-62235b166/)

## **Title**

- **URL**

  `GET`http://127.0.0.1:8000/books/ : Returns a list of books <br/>
  `GET`http://127.0.0.1:8000/books/book/1 : Returns a detail view of the specified book id <br/>
  `GET`http://127.0.0.1:8000/authors/ : Returns a list of authors <br/>
  `GET`http://127.0.0.1:8000/authors/author/1 : Returns a detail view of the specified author id <br/>
  `POST`http://127.0.0.1:8000/authors/author/ : Creates a new author with the specified details - Expects a JSON body <br/>
  `POST`http://127.0.0.1:8000/books/book/ : Creates a new book with the specified details - Expects a JSON body <br/>
  `PUT` http://127.0.0.1:8000/authors/author/1 : Updates an existing author - Expects a JSON body <br/>
  `PUT` http://127.0.0.1:8000/books/book/1 : Updates an existing book - Expects a JSON body <br/>

- **Success Responses:**

  - **Code:**
  -       201_Created <br />

- **Error Responses:**

  - **Code:** 500 Internal Server Error <br />
  -           404_NOT_FOUND <br />
  -           400_BAD_REQUEST <br />
  -           204_NO_CONTENT <br />

- **Usage Instruction Steps:**

1.  Download the project. <br/>
2.  Install all the dependencies:<br/>
 <p align="center">Dependencies</p>
<p align="center"><img align="centre" width="500" height="300" src="https://user-images.githubusercontent.com/17960965/125812255-44bf2e08-4697-470c-950a-c684edbaecab.png"></p>
3.  Run the project: <br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Migrate database: python manage.py makemigrations <br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; python manage.py migrate <br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Run server : python manage.py runserver <br/>
4.  Open browser or postman: hit the api's, get the JSON response.

Thanks for reading.
