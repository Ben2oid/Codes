import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def download_images(url, output_dir):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Find all image tags
    img_tags = soup.find_all('img')
    
    for img_tag in img_tags:
        img_url = urljoin(url, img_tag['src'])
        
        # Remove query parameters from the URL
        parsed_url = urlparse(img_url)
        img_path = parsed_url.path
        
        # Generate the image file name
        img_filename = os.path.join(output_dir, os.path.basename(img_path))
        
        # Send a request to download the image
        img_response = requests.get(img_url)
        
        # Save the image to the output directory
        with open(img_filename, 'wb') as img_file:
            img_file.write(img_response.content)
        
        print(f"Downloaded: {img_filename}")

# Usage example
url = 'https://blancajano.com'
output_dir = r'C:/Users/Administrator/Pictures/'  # Replace with your desired output directory
download_images(url, output_dir)
