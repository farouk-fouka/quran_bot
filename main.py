import requests

# Page number variable
page_number = "002"  # You can change this to any other page number
url = f"https://alquran.vip/APIs/quran-pages/{page_number}.png"

# Sending a GET request to the endpoint
response = requests.get(url)

# Save the image with a dynamic filename
if response.status_code == 200:
    file_name = f"{page_number}.png"
    with open(file_name, "wb") as file:
        file.write(response.content)
    print(f"Image {file_name} downloaded successfully!")
else:
    print(f"Failed to download image. Status code: {response.status_code}")
