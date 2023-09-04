# json 모듈을 사용하기 위해 import 합니다.
import json
import requests
# from pprint import pprint

# 해당 사이트는 요청에 대한 응답을 json 형태의 문자열로 내려줍니다.
url = "https://jsonplaceholder.typicode.com/"

r = requests.get(f"{url}users/1")
# pprint(r.text)
print(type(r.text))  # <class 'str'>

# 문자열 형태의 json을 dictionary 자료형으로 변경합니다.
response_content = json.loads(r.text)
print(type(response_content))  # <class 'dict'>

# dictionary 자료형이기 때문에 key를 사용해 value를 확인할 수 있습니다.
print(f"사용자 이름은 {response_content['name']} 입니다.")

# result output
"""
사용자 이름은 Leanne Graham 입니다.
"""