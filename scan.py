import core
import csv
import threading
class Scanner:
	"""Clase con distintas funciones de escaneo de puertos"""
	def __init__(self):
		self.scanner = core.PortScanner()

################### SERVICIO EN SEGUNDO PLANO ########################

	def servicioHilo(self, target, port):
		print("Se ha ejecutado el intermedio para: "+target+":"+port)

######################################################################
	def simpleTCP(self, target, port):
		self.scanner.scan(target, port, '-sT')
		estadoPuerto = self.scanner[target]['tcp'][int(port)]['state']
		print(port+" "+estadoPuerto)
		if estadoPuerto == 'open':
			servicio = threading.Thread(target=self.servicioHilo, args=(target,port))
			servicio.start()
		# fichero = open("datos.csv","w")
		# cadena = self.scanner.csv()
		# fichero.write(cadena);
		# fichero.close()
		# fichero = open("datos.csv")
		# csv_controlador = csv.reader(fichero, delimiter=';')
		# header = csv_controlador.next()
		# for fila in  csv_controlador:
			# estadoPuerto = fila[6]
			# numeroPuerto = fila[4]
			# servicioPuerto = fila[5]
			# print("Puerto: "+numeroPuerto+" Servicio: "+servicioPuerto+" Estado: "+("ABIERTO" if estadoPuerto == "open" else "CERRADO"))
	def simpleUDP(self, target, port):
		self.scanner.scan(target, port, '-sU')
		print(self.scanner.csv())
		print(self.scanner.command_line())
		
###############################################################################################
	def medioTCP(self, target, port):
		self.scanner.scan(target, port, '-sV')
		print(self.scanner.csv())
		print(self.scanner.command_line())
	def medioUDP(self, target, port):
		self.scanner.scan(target, port, '-sUT')
		print(self.scanner.csv())
		print(self.scanner.command_line())

###############################################################################################
	def altoTCP(self, target, port):
		self.scanner.scan(target, port, '-sCV')
		print(self.scanner.csv())
		print(self.scanner.command_line())
	def altoUDP(self, target, port):
		self.scanner.scan(target, port, '-sCU')
		print(self.scanner.csv())
		print(self.scanner.command_line())