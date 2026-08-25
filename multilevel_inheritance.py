class machine:
    def start(self):
        print("starting")

class computer(machine):
    def run_App(self):
        print("App running")

class smartphone(computer):
    def call(self):
        print("calling")

sp = smartphone()
sp.start()
sp.run_App()
sp.call()