import requests
from loguru import logger
class Proxy():
    type:str
    anonymity:int
    country:str
    ip: str

    def __init__(self,type:str,anonymity:int,country:str,ip:str):
        self.type = type
        self.anonymity = anonymity
        self.country = country
        self.ip = ip


class ProxyScrapper():
    
    def __init__(self):
        self.proxies = []
        self.proxies_url = "https://api.proxyscrape.com/proxytable.php?nf=true&country=all"

    def get_proxies(self):
        try:
            proxy_list = requests.get(self.proxies_url).json()
            # for ip, info in proxy_list.json()['http'].items():
            #     anonymity = info.get('anonymity')
            #     country = info.get('country')
            #     self.proxies.append(Proxy(type="http",anonymity=anonymity,country=country,ip=ip))
            with open("proxies.json",'w') as f:
                f.write(str(proxy_list).replace("'",'"'))
        except Exception as e:
            logger.error("Error getting proxies. " + str(e))
            return []
        
if __name__ == "__main__":
    scrapper = ProxyScrapper()
    scrapper.get_proxies()
   

       