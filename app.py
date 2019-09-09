from flask import Flask, request
from flask import jsonify

#Initializing our application
app = Flask(__name__)


#Creating some dummy data to be sent as a JSON response
sample_data = {
        'Name': "JSONResponse",
        'Message': "Received by Client"
    }


#Route that sends the JSON response to the client
@app.route('/requestjson', methods=['POST','GET'])
def receiveSendJSON():
    if request.method == 'GET': #We want some data to be received by the server, hence we return an error if the method was GET
        return "<h1 style='color:red'> GET requests are not allowed, send some JSON data to this URL. </h1>"
    else:
        data = request.json # JSON received from the client

        # Do something with the data received

        print(f"The received JSON data is:{data}")

        return jsonify(sample_data) #JSON response

if __name__ == '__main__':
    app.run(debug=False,threaded=False)
