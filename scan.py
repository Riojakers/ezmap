import core

class Scanner:
    """Clase con distintas funciones de escaneo de puertos"""

    def __init__(self):
        self.scanner = core.PortScanner()

    def simpleTCP(self, target, port):
        self.scanner.scan(target, port, '-sT')
        print(self.scanner.csv())

    def simpleUDP(self, target, port):
        self.scanner.scan(target, port, '-sU')
        print(self.scanner.csv())
        print(self.scanner.command_line())

    def medioTCP(self, target, port):
        self.scanner.scan(target, port, '-sV')
        print(self.scanner.csv())
        print(self.scanner.command_line())

    def medioUDP(self, target, port):
        self.scanner.scan(target, port, '-sUT')
        print(self.scanner.csv())
        print(self.scanner.command_line())

    def altoTCP(self, target, port):
        self.scanner.scan(target, port, '-sCV')
        print(self.scanner.csv())
        print(self.scanner.command_line())

    def altoUDP(self, target, port):
        self.scanner.scan(target, port, '-sCU')
        print(self.scanner.csv())
        print(self.scanner.command_line())

