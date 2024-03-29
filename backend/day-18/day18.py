import requests

headers = {
    "User-Agent": "MyApp/1.0"
}

api_url = "https://jsonplaceholder.typicode.com/posts"

response_get = requests.get(api_url, headers=headers)

print("GET Request Status Code:", response_get.status_code)
print("GET Response Headers:")
for key, value in response_get.headers.items():
    print(f"{key}: {value}")
print("GET Response Content:", response_get.json())

post_data = {
    "title": "New Post",
    "body": "This is the content of the new post."
}

response_post = requests.post(api_url, json=post_data, headers=headers)
print("\nPOST Response:")
print("POST Request Status Code:", response_post.status_code)
print("POST Response Content:", response_post.json())
