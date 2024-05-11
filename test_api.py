import requests

# Specify the URL of the API endpoint
url = "http://127.0.0.1:5000/predict"
# Open the image file in binary mode
with open("1.jpeg", "rb") as image_file:
    # Create a dictionary with the file data
    files = {"file": image_file}

    # Send the POST request with the image file
    response = requests.post(url, files=files)

# Check the response status code
if response.status_code == 200:
    print("Image sent successfully!")
    print(response.text)
else:

    print(response.text)
    print("Failed to send image.")