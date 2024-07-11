Metricool Service
----------------------------------------------------------------------------------------
Steps:
1) virtualenv venv1
2) source venv1/bin/activate
3) pip install -r requirements.txt
4) modify config.py with correct credentials values
4) python app.py

----------------------------------------------------------------------------------------
Architecture:

MetricoolService class has 2 objects:
    base_url: str
    request: Request

base_url: is the main url
request: is a Request object that will have a login and headers.


Request class has 2 objects:
    - login: Login 
    - headers: dict

Login class has 3 objets:
    - user_id
    - user_token
    - blog_id

----------------------------------------------------------------------------------------
So:

The service has a main URL and a Request. The Request you build will have auth and headers. The auth is the Login class.

