import requests, json

email_list = []
email_dict = {}

response = requests.get("https://gorest.co.in/public/v1/comments")
if response.status_code == 200:
    response = response.json()
for item in response['data']:
    email_dict[item['id']]=item['email']
    email_list.append(item['email'])

print("email are {}".format(email_list))
print("emails and id are {}".format(email_dict))

