import requests

url = "http://localhost:5000/process_intent"
data = {
    "intent": "create_file",
    "params": {
        "file_path": "C:/Users/sidha/Desktop/test.txt",
        "content": "Hello, World!"
    }
}

response = requests.post(url, json=data)
print(response.json())