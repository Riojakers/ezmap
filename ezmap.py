#!/usr/bin/python

import nmap

nm = nmap.PortScannerAsync()
results = nm.scan('127.0.0.1','')
print(results)