import requests
from bs4 import BeautifulSoup
from enum import Enum

UNICAMP_BLOOD_CENTER_URL = 'https://www.hemocentro.unicamp.br/'

class BloodSupplyStatus(Enum):
    CRITIC = "lista-estoque__item estado-critico"
    ALERT = "lista-estoque__item estado-alerta"
    STABLE = "lista-estoque__item estado-estavel"

class UnicampBloodCenterCrawler:

    def __init__(self):
        self.data = requests.get(UNICAMP_BLOOD_CENTER_URL)

    def get_blood_suplies(self) -> list[str]:
        soup = BeautifulSoup(self.data.text, 'html.parser')
        suplies = {}
        for statusName, bloodSupplyStatus in BloodSupplyStatus.__members__.items():
            bloodTypes = []
            supply = soup.find_all("div", {"class": bloodSupplyStatus.value})
            for i in supply:
                bloodTypes.append(i.find("h3").string)
            for bloodType in bloodTypes:
                suplies[bloodType] = statusName
        return suplies

if __name__ == '__main__':
    crawler = UnicampBloodCenterCrawler()
    print(crawler.get_blood_suplies())
