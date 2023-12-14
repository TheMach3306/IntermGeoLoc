from argparse import ArgumentParser as AP
from modules import IGLMain as IGL

class _Main:
    
    def __init__(self):
        pass


def main():
    par = AP(usage="python3 igl.py -i <IP ADDRESS> [OPTIONS]", conflict_handler="resolve")
    par.add_argument('-i', '--ip', dest="host_ip", type=str, metavar="", help="The IP address to target.")
    
    # Argument group 1 -- Basic Geo Data (Non Commercial DB)
    ag1 = par.add_argument_group("Basic Geo Options")
    ag1.add_argument('-c', '--city', dest="geo_city", action="store_true", help="Get geo city.")
    ag1.add_argument('-r', '--region', dest="geo_region", action="store_true", help="Get geo region.")
    ag1.add_argument('-C', '--country', dest="geo_country", action="store_true", help="Get geo country.")
    ag1.add_argument('-l', '--lat', dest="geo_lat", action="store_true", help="Get geo latitude.")
    ag1.add_argument('-L', '--lon', dest="geo_lon", action="store_true", help="Get geo longitude.")
    
    ag2 = par.add_argument_group("Extra Options")
    ag2.add_argument('--vulns', dest="host_vulns", action="store_true", help="List known vulnerabilities of the host.")
    ag2.add_argument('--open', dest="host_open_ports", action="store_true", help="Get open ports on the target.")
    ag2.add_argument('--tags', dest="host_tags", action="store_true", help="Get known tags on the host.")
    ag2.add_argument('--cpes', dest="host_cpes", action="store_true", help="Get Customer Premises Equipment Systems on the host.")
    
    
    args = par.parse_args()
    
    # Module object
    _x = IGL(str(args.host_ip))
    
    if args.host_ip:
        if args.geo_city:
            _x.lookup_target(opt_type="city"); pass
            
        if args.geo_region:
            _x.lookup_target(opt_type="region"); pass
            
        if args.geo_country:
            _x.lookup_target(opt_type="country"); pass
            
        if args.geo_lat:
            _x.lookup_target(opt_type="lat"); pass
            
        if args.geo_lon:
            _x.lookup_target(opt_type="lon"); pass
            
        if args.host_vulns:
            _x.lookup_target(opt_type="vuln"); pass
            
        if args.host_open_ports:
            _x.lookup_target(opt_type="ports"); pass
            
        
    
main()
