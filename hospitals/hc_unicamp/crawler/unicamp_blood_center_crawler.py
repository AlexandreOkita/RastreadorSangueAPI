import requests
from bs4 import BeautifulSoup
from enum import Enum

UNICAMP_BLOOD_CENTER_URL = 'https://www.hemocentro.unicamp.br/'

class BloodSupplyStatus(Enum):
    CRITIC = "vc_col-sm-3 estoque-sangue-critico"
    ALERT = "vc_col-sm-3 estoque-sangue-alerta"
    STABLE = "vc_col-sm-3 estoque-sangue-estavel"

class UnicampBloodCenterCrawler:

    def __init__(self):
        self.data = requests.get(UNICAMP_BLOOD_CENTER_URL)

    def get_supply_with_status(self, status: BloodSupplyStatus) -> list[str]:
        soup = BeautifulSoup(self.data.text, 'html.parser')
        supply = soup.find_all("div", {"class": status.value})
        blood_types = []
        for i in supply:
            blood_types.append(i.find("h3").string)
        return blood_types

crawler = UnicampBloodCenterCrawler()
print(crawler.get_supply_with_status(BloodSupplyStatus.STABLE))
print(crawler.get_supply_with_status(BloodSupplyStatus.ALERT))
print(crawler.get_supply_with_status(BloodSupplyStatus.CRITIC))