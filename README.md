# PowerToFly

This App aims at developing an API endpoint to get a list of users.

Following is the cURL call for the same end-point. 

curl --location --request GET 'http://127.0.0.1:8000/data/users?search=dav&page=12'

This API support pagination ,filteration and basic caching mechanism. 

The database has around 1.5 MM of data in it. 

Requirements can be installed from the requirements.txt file using the command "pip install -r requirements.txt"
