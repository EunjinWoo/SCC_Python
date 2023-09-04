import requests
from pprint import pprint

# 통신 할 base url 지정
url = "https://jsonplaceholder.typicode.com/"

# 1번 사용자 정보를 받아오기 위해 users/1 경로에 get 요청
r = requests.get(f"{url}users/1")

pprint({
    "contents": r.text,
    "status_code": r.status_code,
})

# result output
"""
{'contents': '{\n'
             '  "id": 1,\n'
             '  "name": "Leanne Graham",\n'
             '  "username": "Bret",\n'
             '  "email": "Sincere@april.biz",\n'
             '  "address": {\n'
             '    "street": "Kulas Light",\n'
             '    "suite": "Apt. 556",\n'
             '    "city": "Gwenborough",\n'
             '    "zipcode": "92998-3874",\n'
             '    "geo": {\n'
             '      "lat": "-37.3159",\n'
             '      "lng": "81.1496"\n'
             '    }\n'
             '  },\n'
             '  "phone": "1-770-736-8031 x56442",\n'
             '  "website": "hildegard.org",\n'
             '  "company": {\n'
             '    "name": "Romaguera-Crona",\n'
             '    "catchPhrase": "Multi-layered client-server neural-net",\n'
             '    "bs": "harness real-time e-markets"\n'
             '  }\n'
             '}',
 'status_code': 200}
"""