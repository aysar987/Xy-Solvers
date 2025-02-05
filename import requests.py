import requests

url = "http://localhost:8000/jangan_dibuka.zip"
response = requests.get(url)

if response.status_code == 200:
    with open('jangan_dibuka.zip', 'wb') as file:
        file.write(response.content)
    print("File downloaded successfully.")
else:
    print(f"Failed to retrieve the file. HTTP Status code: {response.status_code}")
