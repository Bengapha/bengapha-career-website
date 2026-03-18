import socket
from datetime import datetime


class Target:
    def __init__(self, hostname):
        self.hostname = hostname
        self.ip = "unknown"
        self.status = "pendind"
        self.timestamp = None

    def resolve_ip(self):
          
            try:
                self.ip = socket.gethostbyname(self.hostname)
                return self.ip
              
            except socket.gaierror:
                return "unknown"

    def check_connectivity(self):
          self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
          
          try:
            sock = socket.create_connection((self.hostname, 80), timeout=4)
            sock.close()
            self.status = "alive"

          except OSError:
            self.status = "down"

    def get_report_line(self):
      print(f"hostname: {self.hostname}")
      print(f"ip: {self.ip}")
      print(f"status: {self.status}")
      print(f"timestamp: {self.timestamp}")
      print("-" * 20)

t1 = Target("google.com")
t2 = Target("github.com")
t3 = Target("cloudflare.com")

for target in[t1, t2, t3]:
  target.resolve_ip()
  target.check_connectivity()
  target.get_report_line()                 
                
   


            
                

                    

        
                