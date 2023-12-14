import requests, json
from ip2geotools.databases.noncommercial import DbIpCity as DIP

class _Meta:
    
    @staticmethod
    def data_banner(_type, *strings):
        for string in strings:
            print("\033[01;33m=> \033[37m[ \033[36mGeo -> \033[35m{}\033[37m ]: {}\033[0m".format(_type, string))


class IGLMain:
    
    def __init__(self, target):
        self.host = target
        self.dip_req = DIP.get(ip_address=self.host, api_key="free")
        self.extra_req = requests.get(url="https://internetdb.shodan.io/{}".format(self.host)).json()
        
    def lookup_target(self, opt_type):
        
        match opt_type:
            
            case "city":
                _Meta.data_banner("City", self.dip_req.city); pass
                
            case "region":
                _Meta.data_banner("Region", self.dip_req.region); pass
                
            case "country":
                _Meta.data_banner("Country", self.dip_req.country); pass
                
            case "lat":
                _Meta.data_banner("Latitude", self.dip_req.latitude); pass
                
            case "lon":
                _Meta.data_banner("Longitude", self.dip_req.longitude); pass
                
            case "vuln":
                print("\n\033[37m[ Vulnerabilities ]:\033[0m\n")
                for vuln in self.extra_req["vulns"]:
                    print("\033[33m=>> \033[37m Vulnerability:\t\033[36m{}\033[0m".format(vuln))
                    
            case "ports":
                print("\n\033[37m[ Open Ports ]:\033[0m\n")
                for port in self.extra_req["ports"]:
                    print("\033[34m[*]\033[37m {} : \033[32mOpen\033[0m".format(str(port)))
            
            case _:
                pass