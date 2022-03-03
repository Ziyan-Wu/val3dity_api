import json
import requests

print("=============================== /cityjson ====================================================")
cityjson_path = '../../../data/cityjson/cube.json'  # path of data
# # cityjson_path = 'option1.json' # invalid input

# with open(cityjson_path, 'r') as f:
#     cityjson = json.load(f)


d = requests.post('http://127.0.0.1:5000/validate', json=cityjson_path)
print(d.url)
print(d.text)
# print(d)
print(d.status_code)

print("============================= end ======================================================")