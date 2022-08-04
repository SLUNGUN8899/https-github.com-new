import os,time,sys,shutil

class Main:

	def __init__(self):
		self.detekos()

	def menu(self):
		print("""
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		;        A U T O J P        ;
		;---------------------------;
		;    Author : SLUNGUN8899   ;
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
NOTE: This tool's only work for game hack.
1. SCATTER
2. SUPERWINE
3. MINORJACKPOT
4. MAJORJACKPOT
5. GRANDJACKPOT
""")
		pilih=int(input('slungun8899/> '))
		if pilih == 1:
			import src.scatter
		elif pilih == 2:
			import src.superwine
		elif pilih == 3:
			import src.minorjackpot
		elif pilih == 4:
			import src.majorjackpot
		elif pilih == 5:
			import src.grandjackpot
		else: print("[!] lihat menu dong(o)");self.menu()

	def detekos(self):
		#remove cache
		try:
			shutil.rmtree("src/__pycache__")
		except: pass

		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('clear')
		self.menu()

try:
	Main()
except KeyboardInterrupt:
	exit('[Exit] Key interrupt')
except Exception as F:
	print('Err: %s'%(F))
