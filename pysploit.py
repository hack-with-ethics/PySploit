import os
import time
import pyfiglet
import socket
import re
import sys
import subprocess

class Listers:
	def ssh_lister(self):
		print("\n\t\t[ 1 ] ssh_version ")
		print("\n\t\t[ 2 ] ssh_login ")
		print("\n\t\t[ 3 ] ssh_enumusers ")

	def ftp_lister(self):
		print("\n\t\t[ 1 ] Ftp_version")
		print("\n\t\t[ 2 ] Ftp Login ")


	def list_services(self):
		print("\n\t\t[ 1 ] ssh Enumeration or BruteForce")
		print("\n\t\t[ 2 ] Ftp Enumeration or  BruteForce")
		print("\n\t\t[ 3 ] MySql Service Enumeration")
		print("\n\t\t[ 4 ] telnet Enumeration or BruteForce")
		print("\n\t\t[ 5 ] smb Enumeration")
		print("\n\t\t[ 6 ] Wordpress Enumeration")
		print("\n\t\t[ 7 ] Exit ")
		print("\n\t\t[ 8 ] List Exploits")
		print("\n\t\t[ 9 ] Load Existing script")

	def mysql_service(self):
		print("\n\t[ 1 ] mysql_login")
		print("\n\t[ 2 ] mysql_Version")

	def list_exploits(self):
		return [x for x in os.listdir() if x.endswith(".rb")]
	def telnet_service(self):
		pass

	def smb_enum(self):
		pass

class interact_metasploit(Listers):

	

		


	def write_login_based_exploit(self,serve):
		with open(f"{serve}_version_exploit.rb",'w') as file:
			file.write(f"use auxiliary/scanner/{serve}/{serve}_version")
			file.write(f"\nset rhosts {sys.argv[1]}")
			file.write("\nexploit")
			file.close()
		print("\n\t\t + Written Sucessfull ")
		return os.getcwd() +"/" +f"{serve}_version_exploit.rb"
	def write_version_detection_exploit(self,serve):
		with open(f"{serve}_login_exploit.rb",'w') as file:
			file.write(f"use auxiliary/scanner/{serve}/{serve}_login")
			file.write(f"\nset rhosts {sys.argv[1]}")
			file.write("\nset threads 5")
			file.write("\nset verbose true")
			file.write("\nset STOP_ON_SUCCESS true")
			passopt = input("\n\t\t[1] (passfile | userfile)\n\t\t[ 2 ] userpassfile:")
			if passopt == "1":
				passfile = input("\n\t\t + ( Enter the passfile Path ) > ")
				userfile = input("\n\t\t + ( Enter the userfile Path ) > ")
				file.write(f"\nset PASS_FILE {passfile}")
				file.write(f"\nset USER_FILE {userfile}")
			else:
				passfile = input("\n\t\t( Passfile Path [ Type (Default) :/usr/share/wordlist/metasploit/piata_ssh_userpass.txt ] ) > ").lower().strip()
				if passfile == "default":
					passfile = "/usr/share/wordlists/metasploit/piata_ssh_userpass.txt"
				
				file.write(f"\nset USERPASS_FILE {passfile}")
			file.write(f"\nexploit")
			file.close()
		return os.getcwd() + "/" + f"{serve}_login_exploit.rb"
	def executer(self,loc):
	
		if  input("\n\t\t Do you Want to Run the exploit ? [ y / n ] :").lower() == "y":
			print("\n\t + Executing the Exploit [ ! ] ")
			print("\n\t\t + file ",loc.split('/')[-1])
			os.system(f"msfconsole -r {loc.split('/')[-1]}")
		else:
			print("\n\t + File saved :",loc)
			input("\n\t\t < Press Enter > ")

	def is_postgres_active(self):

		regx = "(?:Active:)(.*)"
		
		if "dead" in re.findall(regx,subprocess.getoutput("service postgresql status"))[0].strip():

			return True
		else:
			return False

	def is_operating_system_eligible(self):

		if os.name !="nt" and os.path.exists("/usr/share/metasploit-framework/"):

			return True
		else:

			return False
	

	def try_get_Banner(self,ip,port):
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		try:
			s.connect((ip,port))

			return s.recv(1024)
		except:
			return "[ ! ] Could Not Grab it Trying to Exploit it"

	def cls(self):
		os.system("clear")

	def write_ruby_exploit(self):
		if self.is_operating_system_eligible() and len(sys.argv) == 2:
			if self.is_postgres_active():
				print("\n\t + starting Postgres service")
				os.system("service postgresql start")
			else:
				print("\n\t + Postgres already started ")
			while True:
				self.cls()
				pyfiglet.print_figlet("                              P y s p l o it")
				print("\n\t\t\t\t[ $ ] The Metasploit Interactor [ ! ] ")
				
				self.list_services()
				inp = input("\n\t\t( Pysploit ) >  ")
				if inp == "1":
					self.cls()
					print("\n\t\t\t< Secure Shell Proto >")
					print("\n\t\t + Version Detected : ",self.try_get_Banner(sys.argv[1],22))
					time.sleep(0.2)

					self.ssh_lister()
					v = input("\n\t\t ( Exploit/ssh ) >  ")
					if v == "1":
						time.sleep(0.5)
						print("\n\t\t [ + ssh_version_Module ]")
						time.sleep(0.5)
						print("\n\t\t  + writing Exploit ")
						loc = self.write_login_based_exploit("ssh")

						self.executer(loc)
					elif v == "2":
						time.sleep(0.5)
						print("\n\t\t [ + ssh_Login_Module ]")
						time.sleep(0.5)
						print("\n\t\t  + writing Exploit ")
						loc = self.write_version_detection_exploit("ssh")
						self.executer(loc)

				elif inp == "2":
					self.cls()
					print("\n\t\t\t< File Transfer Proto >")
					time.sleep(0.5)
					print("\n\t\t + Version Detected : ",self.try_get_Banner(sys.argv[1],21))
					self.ftp_lister()
					v = input("\n\t\t ( Exploit/ftp ) > ")

					if v == "1":
						time.sleep(0.5)
						print("\n\t\t [ + ftp_version_Module ]")
						time.sleep(0.5)
						print("\n\t\t  + writing Exploit ")
						loc = self.write_login_based_exploit("ftp")
						self.executer(loc)
					elif v == "2":
						time.sleep(0.5)
						print("\n\t\t [ + ftp_Login_Module ]")
						time.sleep(0.5)
						print("\n\t\t  + writing Exploit ")
						loc = self.write_version_detection_exploit("ftp")
						self.executer(loc)

				elif inp == "3":
					self.cls()
					print("\n\t\t\t My Sql Server")
					ban = self.try_get_Banner(sys.argv[1],3306)
					if "\\" in str(ban):
						ban = str(ban).split("\\")[4]

					print("\n\t\t + version ",ban)
					self.mysql_service()
					v = input("\n\t\t\t ( Exploits/mySql ) > ")
					if v == "1":
						time.sleep(0.5)
						print("\n\t\t [ + mysql_Login_Module ]")
						time.sleep(0.5)
						print("\n\t\t  + writing Exploit ")
						loc = self.write_version_detection_exploit("mysql")
						self.executer(loc)
					elif v == "2":
						time.sleep(0.5)
						print("\n\t\t [ + mysql_version_Module ]")
						time.sleep(0.5)
						print("\n\t\t  + writing Exploit ")
						loc = self.write_login_based_exploit("mysql")
						self.executer(loc)

				elif inp == "8":
					print("\n\t\t Listing Exploits")
					lst = self.list_exploits()
					if len(lst) == 0:
						print("\n\t\t ! No Exploits Found ")
						
					else:
						for i in range(len(lst)):
							print(f"\n\t\t\t\t{i+1}. {lst[i]}")
						ack =  input("\n\t\t\t Do You Want to Delete the file ? [ Enter the Number ] or [ Press Enter] : ")
						try:
							if int(ack) - 1 <= len(lst) - 1:
								file = lst.pop(int(ack) - 1)
								print("\n\t\tRemoved + ",file)
								os.system(f"rm -rf {file}")

						except:
							pass
					input("\n\n\t\t[ Press Enter ] ")
				elif inp == "9":
					lst = self.list_exploits()
					if len(lst) == 0:
						print("\n\t\t [ + ] No Ruby Scripts Available ")
					else:
						print("\n\t\t [ + ] Loading Modules [ ! ] ")
						for i in range(len(lst)):
							print(f"\n\t\t {i+1}. {lst[i]}")
						l = input(" ( Enter Module Number ) > ")

						try:
							if int(l) - 1 <=len(lst)-1:
								time.sleep(0.3)
								print("\n\t\t + file selected : ",lst[int(l)-1])
								time.sleep(0.2)
								print("\n\t\t + Reading Ruby script")
								time.sleep(0.2)
								
								print("\n\t\t Executing [ ! ]")
								os.system(f"msfconsole -r {lst[int(l)-1]}")
						except:
							pass

					input("\n\t\t< Press Enter >")



				elif inp == "7":
					break
		else:
			print("\n* PLz Run the Code in LInux ENv")
			print(f"\n[ * ] usage : {sys.argv[0]} <ip address> ")
rb = interact_metasploit()
rb.write_ruby_exploit()
