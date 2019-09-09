# REST API using FLASK

REST, or REpresentational State Transfer, is an architectural style for providing standards between computer systems on the web, making it easier for systems to communicate with each other. REST-compliant systems, often called RESTful systems, are characterized by how they are stateless and separate the concerns of client and server. We will go into what these terms mean and why they are beneficial characteristics for services on the Web.

**Statelessness**

Systems that follow the REST paradigm are stateless, meaning that the server does not need to know anything about what state the client is in and vice versa. In this way, both the server and the client can understand any message received, even without seeing previous messages.

**How is data sent?**

REST APIs can use different data formats to  transfer data between the client and the server. In this particular application, we are using the ```JSON``` syntax to transfer the data between client and the server.

**JavaScript Object Notation** is an open-standard file format that uses human-readable text to transmit data objects consisting of attribute–value pairs and array data types. An example can be seen as follows:
```
{
     "firstName": "John",
     "lastName": "Smith",
     "address": {
         "streetAddress": "21 2nd Street",
         "city": "New York",
         "state": "NY",
         "postalCode": 10021
     },
     "phoneNumbers": [
         "212 555-1234",
         "646 555-4567"
     ]
 }
```

**Flask**

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.

We will be using ```flask``` to create a ```REST``` API so that we can send and receive data in the JSON syntax.


## Installation and Startup

Download or clone the repository in a directory and ```cd``` into folder containing the file ```app.py```. 
* Set the FLASK environment variable ```FLASK_APP``` to the name of the python file as follows in the terminal (for Windows):

  ```bash
  set FLASK_APP=app.py
  ```

* Run the flask app using the following command:
  ```bash
  flask run
  ```



## Usage

1. Once the application is running, you can send/receive JSON objects to/from the server. The route/path that returns the ```JSON``` object is:

    ```python
    @app.route('/requestjson', methods=['POST','GET'])
    def receiveSendJSON():
    ```

2. The route accepts only POST requests as some JSON object must be sent to the server so that it can interpret the data from it. If the request type is GET, the server responds with an error:

   ![Get_Response_Error](get_response.png)

3. In this application, the JSON object that is being sent from the server to the client as a response to the client request, is some sample data that is of the type ```dict``` in python. The code snippet is as follows:

    ```python
    sample_data = {
        'Name': "JSONResponse",
        'Message': "Received by Client"
    }
    ```

   In order to test this application, you can use a website that can post HTTP requests online. An example is https://reqbin.com/. Enter the url where you want to post the request and add a JSON object in the the content section. The server will receive the JSON object and then return another JSON object to the client.

   ![Response_To_Client](response_to_client.png)

   The python console displays the data received from the client:

   ![Received_From_Server](json_received_server.png)

## Information about REST APIs

https://www.codecademy.com/articles/what-is-rest

https://www.javatpoint.com/json-example

https://reqbin.com/ (to send requests to web-server)