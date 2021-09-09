
from typing import List
import requests
res=requests.get('https://dummy.restapiexample.com/api/v1/employees')
content=res.content
res1=List(content)
for i in res1['data']:
    print(i['employee_name'])
    print(i['employee_id'])
