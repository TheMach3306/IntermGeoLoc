# IntermGeoLoc
A small program written in python. The purpose of this script is to probe the IP address of a valid hostname service and return Geographical data relating to the supplied host.

# Basic Usage
```bash
python3 igl.py -h
```
```bash
sage: python3 igl.py -i <IP ADDRESS> [OPTIONS]

options:
  -h, --help     show this help message and exit
  -i , --ip      The IP address to target.

Basic Geo Options:
  -c, --city     Get geo city.
  -r, --region   Get geo region.
  -C, --country  Get geo country.
  -l, --lat      Get geo latitude.
  -L, --lon      Get geo longitude.

Extra Options:
  --vulns        List known vulnerabilities of the host.
  --open         Get open ports on the target.
  --tags         Get known tags on the host.
  --cpes         Get Customer Premises Equipment Systems on the host.
```

# Example Run
```bash
python3 igl.py -i 1.1.1.1 -c -r -C -l -L --vuln
```
