import requests

# a simple get request to github
response = requests.get("https://api.github.com")

# let's see what information it contains
print(response.status_code)



# sample error handling
if response:
    print("Success!")
else:
    raise Exception(f"Non-success status code: {response.status_code}")