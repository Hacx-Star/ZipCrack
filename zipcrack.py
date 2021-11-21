try:
	#This Tool create by Hacx-Star
	import zipfile
	from tqdm import tqdm
	import pyfiglet
	import os
	from colorama import Fore
	
	os.system("clear")
	print(Fore.LIGHTYELLOW_EX)
	###################
	a=pyfiglet.figlet_format("Zip-Crack")
	print(a)
	print("                             Hacx-Star")
	print()
	print("You Tube : https://youtube.com/channel/UCJn2-qHoPUSgWe2focJVeUQ")
	print()
	print("github   : https://github.com/Hacx-Star")
	print()
	print(Fore.LIGHTGREEN_EX)
	a=input("ZIPFILE> ")
	print()
	b=input("WORD LIST> ")
	print()
	zip_file = zipfile.ZipFile(a)
	t_words = len(list(open(b, "rb")))
	print(Fore.LIGHTYELLOW_EX,"=============================================")
	print("Total Passwords To Test:", t_words)
	print()
	with open(b, "rb") as wordlist:
	    for word in tqdm(wordlist, total=t_words, unit="word"):
	        try:
	            zip_file.extractall(pwd=word.strip())
	        except:
	            continue
	        else:
	            print(Fore.GREEN,"[+] Password found:", word.decode().strip())
	            exit(0)
	print()
	print(Fore.RED,"[!] Password not found, try other wordlist")
except:
	print("Sorry")