import requests
from pprint import pprint

# 통신 할 base url 지정
url = "https://jsonplaceholder.typicode.com/"

# 데이터 생성에 사용될 값 지정
data = {
    "name": "sparta",
    "email": "sparta@test.com",
    "phone": "010-0000-0000",
}


# 사용자를 생성하기 위해 users 경로에 data를 담아 post 요청
r = requests.post(f"{url}users", data=data)

pprint({
    "contents": r.text,
    "status_code": r.status_code,
})

# result output
"""
{'contents': '{\n'
             '  "name": "sparta",\n'
             '  "email": "sparta@test.com",\n'
             '  "phone": "010-0000-0000",\n'
             '  "id": 11\n'
             '}',
 'status_code': 201}
"""