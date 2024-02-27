from PIL import Image
import requests
from bs4 import BeautifulSoup

def fetch_blood_status_image(websiteUrl: str) -> Image:
    rawWebsiteContent = requests.get(websiteUrl).text
    parsedWebsiteContent = BeautifulSoup(rawWebsiteContent, 'html.parser')

    matches = parsedWebsiteContent.select('#conteudo img')
    if (len(matches) != 1):
        raise Exception("Something changed on {websiteUrl}, expected html structure must be updated")
    
    imgUrl = matches[0]['src']
    img = Image.open(requests.get(imgUrl, stream=True).raw)

    return img