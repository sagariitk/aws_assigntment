

#lambda function for HR it includes GET, POST, PUT, DELETE methods

import boto3
import json

client = boto3.client('dynamodb')

def lambda_handler(event, context):

#return of the list of items in the table since GET will not take input from the body as event
    response = client.scan(
    TableName='sagarq5',
    )
    item=response['Items']
    return item
    
#if method id POST then Posting in the table given the items
    if event['method'] == 'POST':
        response = client.put_item(
        TableName='sagarq5',
        Item=event['params']
        )
        return response
  
#if method id POST then Posting in the table given the items      
    if event['method'] == 'PUT':
        response = client.put_item(
        TableName='sagarq5',
        Item=event['params']
        )
        return response
        

#if method is DELETE then Deleting the item based on input(which is userid)

    if event['method'] == 'DELETE':
        response = client.delete_item(
        TableName='sagarq5',
        Key=event['params']
        )
        return response


# lambda function for employees which will return only the list of items in the table

import boto3
import json

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    response = client.scan(
        TableName='sagarq5',
        )
    item=response['Items']
    return item

#tried to get seperatly data also 
    # if event['method'] == 'GET':    
    #     response = client.get_item(
    #     TableName='sagarq5',
    #     Key={
    #         'userid': {
    #             'S': event['params']['querystring']["userid"]
    #             }
    #         }
    #     )
    #     return response

        

# couldn't implement authentication part(despite trying a lot)


#additional try to make front end to get and post data to table 

<html>
<head>

<script type="text/javascript" language="javascript">

function loadGet() {

    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("demo").innerHTML =
          this.responseText;
      }
    };
    xhr.open("GET", "https://24zqff8gl1.execute-api.us-east-1.amazonaws.com/prod/sagarq5get", true);
    xhr.send();
}
</script>

</head>
<body id="demo1" >
    
  <h2>Get data from DynamoDB table</h2>

  <button type="button" class="btn" onclick="loadGet()">GETValue</button> 
  <br>
  <p id="demo"></p>

</body>

</html>




<html>
<head>

<script type="text/javascript" language="javascript">

function loadGet() {
    // alert('Get function called')
    var userid=document.getElementById("userid").value;
    console.log(userid);
    var username=document.getElementById("username").value;
    var age=document.getElementById("age").value;
    var TableName=document.getElementById("TableName").value;
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("demo").innerHTML =
            this.responseText;
       }
    };
    xhttp.open("GET", "https://24zqff8gl1.execute-api.us-east-1.amazonaws.com/prod/sagarq5/", true);
    xhttp.send(); 
}


function loadPost() {
    // alert('Post function called')
    var userid = document.getElementById("userid").value;
    var username = document.getElementById("username").value;
    var age = document.getElementById("age").value;
    var TableName = document.getElementById("TableName").value;
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("demo").innerHTML =
            this.responseText;
       }
    };
    xhttp.open("POST", "https://24zqff8gl1.execute-api.us-east-1.amazonaws.com/prod/sagarq5/", true);
    xhttp.send(); 
}
function loadPut() {
    // alert('Put function called')
    var userid=document.getElementById("userid").value;
    var username=document.getElementById("username").value;
    var age=document.getElementById("age").value;
    var TableName=document.getElementById("TableName").value;
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("demo").innerHTML =
            this.responseText;
       }
    };
    xhttp.open("PUT", "https://24zqff8gl1.execute-api.us-east-1.amazonaws.com/prod/sagarq5/", true);
    xhttp.send(); 
}
function loadDel() {
    // alert('Delete function called')
    var userid=document.getElementById("userid").value;
    var username=document.getElementById("username").value;
    var age=document.getElementById("age").value;
    var TableName=document.getElementById("TableName").value;
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("demo").innerHTML =
            this.responseText;
       }
    };
    xhttp.open("DELETE", "https://24zqff8gl1.execute-api.us-east-1.amazonaws.com/prod/sagarq5/", true);
    xhttp.send(); 
}

</script>

</head>
<body>
  <div id="demo"></div>
  <div class="log-form">
  <h2>Play with Dynamodb</h2>
  <form>
    <input type="text" title="userid" id="userid" placeholder="userid" />
    <input type="text" title="TableName" id="TableName" placeholder="TableName" />   
  </form>
    <button type="submit" class="btn" onclick="loadGet()">GET</button>  
    <ul></ul>
  <form>
    <input type="text" title="userid" id="userid" placeholder="userid" />
    <input type="text" title="username" id="username" placeholder="username" />
    <input type="text" title="age" id="age" placeholder="age" />
    <input type="text" title="TableName" id="TableName" placeholder="TableName" />
  </form>
    <button type="submit" onclick="loadPost()" class="btn">POST</button>
    <ul></ul>
  <form>
    <input type="text" title="userid" id="userid" placeholder="userid" />
    <input type="text" title="username" id="username" placeholder="username" />
    <input type="text" title="age" id="age" placeholder="age" />
    <input type="text" title="TableName" id="TableName" placeholder="TableName" />
  </form>
    <button type="submit" onclick="loadPut()" class="btn">PUT</button>
    <ul></ul>
  <form>
    <input type="text" title="userid" id="userid" placeholder="userid" />
    <input type="text" title="TableName" id="TableName" placeholder="TableName" />
  </form>
    <button type="submit" onclick="loadDel()" class="btn">DELETE</button>
    <ul></ul>
</div>
</body>
</html>



