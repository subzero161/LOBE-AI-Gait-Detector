import os
import requests
from bs4 import BeautifulSoup

# Create a folder to store the images
if not os.path.exists('gaits'):
    os.makedirs('gaits')

# Define the search terms for normal and abnormal gait
normal_term = 'normal gait'
abnormal_term = 'abnormal gait'

# Loop through the search terms
for term in [normal_term, abnormal_term]:
    # Create a Google search URL for the term
    search_url = f"https://www.google.com/search?q={term}&tbm=isch"

    # Send a request to the search URL
    response = requests.get(search_url)

    # Parse the HTML response using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the image URLs from the HTML
    image_urls = [img['src'] for img in soup.find_all('img')]

    # Loop through the first 500 image URLs
    for i, url in enumerate(image_urls[:500]):
        # Download the image from the URL
        response = requests.get(url)
        image_data = response.content

        # Save the image to the gait folder
        with open(f"gaits/{term}_{i}.jpg", 'wb') as f:
            f.write(image_data)
