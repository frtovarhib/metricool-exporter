from pydantic import BaseModel, Field
import requests
from urllib.parse import urlencode
from config import BASE_URL, auth, headers
from modules.errors import InvokeApiExeption

class Login(BaseModel):
    user_id: str = Field(alias='userId')
    user_token: str = Field(alias='userToken')
    blog_id: str = Field(alias='blogId')

class Request(BaseModel):
    login: Login
    headers: dict

class MetricoolService(BaseModel):
    base_url: str
    request: Request

    def get(self, endpoint, params={}):
        login = self.request.login.dict(by_alias = True)
        params.update(login)
        encoded_params = urlencode(params)
        url = self.base_url+endpoint+f'?{encoded_params}'

        print(f"Request URL: {self.base_url+endpoint}")

        result = requests.get(url=url, params=encoded_params, headers=self.request.headers)

        if result.status_code == 200:
            return result.json()
        else:
            error = {
                "status_code": result.status_code,
                "error": result.text
            }
            raise InvokeApiExeption(error)




creds = {Login.__fields__[k].alias: v for k, v in auth.items()}
login = Login(**creds)
headers = {'Accept': 'application/json'}

request = Request(login=login, 
                  headers = headers)

client = MetricoolService(base_url=BASE_URL, 
                          request=request)