import core
import csv
import threading
from io import StringIO
class Scanner:
	"""Clase con distintas funciones de escaneo de puertos"""
	def __init__(self):
		self.scanner = core.PortScanner()

########################### SIMPLE SCANNER ###########################


	def simple(self, target, port, protocol):
		#Choose parameter according to the protocol
		parameter = ' '
		if protocol == 'tcp':
			parameter = '-sT'
		else:
			parameter = '-sU'

		#Launches the scanner
		self.scanner.scan(target, port, parameter)
		
		#Recover the state of the port
		portState = self.scanner[target][protocol][int(port)]['state']

		#Returns a boolean according to the state of the port
		if portState == 'open' or portState == 'open|filtered':
			return True

		return False

########################### ADVANCE SCANNER ##########################

	def start(self, target, port, protocol):
		#Choose parameter according to the protocol
		parameter = ' '
		if protocol == 'tcp':
			parameter = '-sV'
		elif protocol == 'udp':
			parameter = '-sUT'
		elif protocol == 'tcpH':
			parameter = '-sCV'
		else:
			parameter = '-sCU'

		#Launches the scanner
		self.scanner.scan(target, port, parameter)

		#Format information to a String
		cad_string = self.scanner.csv()
		csv_controlador = csv.reader(cad_string.split('\n'), delimiter=';')
		header = csv_controlador.next()
		cad = ' '

		#Return data
		if protocol == 'tcp' or protocol == 'udp':
			for row in csv_controlador:
				if len(row) >= 12:
					cad += 'Servicio: '+row[5]+' Version: '+row[10]+"\n "
		else:
			for row in csv_controlador:
				if len(row) >= 12:
					cad += ";".join(row)+"\n"
		return cad
