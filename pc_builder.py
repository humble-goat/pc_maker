class CmdColor:
	header = '\033[95m'
	warning = '\033[93m'
	fail = '\033[31m'
	bold = '\033[1m'
	underline = '\033[4m'
	end_sequence = '\033[0m'
	browsing = '\033[36m'
	gaming = '\033[91m'
	programming = '\033[96m'
	digital_editing = '\033[95m'
	game_dev = '\033[93m'
	architecht = '\033[33m'
	hacking = '\033[32m'
	
	blue='\033[34m'
	lightgrey='\033[37m'
	darkgrey='\033[90m'
	lightgreen='\033[92m'


def init_browser():
	dirname = os.path.abspath(__file__)
	chrome_options = Options()
    # chrome_options.add_argument("--headless")
	cromium_path = os.path.split(dirname)[0] + '\\chromedriver.exe'
	driver = webdriver.Chrome(cromium_path, options=chrome_options) 
	return driver


def banner():
	banner_2 = \
		'''
			 _______  _______    _______  _______  _        _______  _______ 
			(  ____ )(  ____ \  (       )(  ___  )| \    /\(  ____ \(  ____ )
			| (    )|| (    \/  | () () || (   ) ||  \  / /| (    \/| (    )|
			| (____)|| |        | || || || (___) ||  (_/ / | (__    | (____)|
			|  _____)| |        | |(_)| ||  ___  ||   _ (  |  __)   |     __)
			| (      | |        | |   | || (   ) ||  ( \ \ | (      | (\ (   
			| )      | (____/\  | )   ( || )   ( ||  /  \ \| (____/\| ) \ \__
			|/       (_______/  |/     \||/     \||_/    \/(_______/|/   \__/
		'''
	banner_3 = \
		'''
		██████╗  ██████╗    ███╗   ███╗ █████╗ ██╗  ██╗███████╗██████╗ 
		██╔══██╗██╔════╝    ████╗ ████║██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
		██████╔╝██║         ██╔████╔██║███████║█████╔╝ █████╗  ██████╔╝
		██╔═══╝ ██║         ██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗
		██║     ╚██████╗    ██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗██║  ██║
		╚═╝      ╚═════╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
		'''
	banner_4 = \
		'''
		
		 ██▓███   ▄████▄      ███▄ ▄███▓ ▄▄▄       ██ ▄█▀▓█████  ██▀███  
		▓██░  ██▒▒██▀ ▀█     ▓██▒▀█▀ ██▒▒████▄     ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
		▓██░ ██▓▒▒▓█    ▄    ▓██    ▓██░▒██  ▀█▄  ▓███▄░ ▒███   ▓██ ░▄█ ▒
		▒██▄█▓▒ ▒▒▓▓▄ ▄██▒   ▒██    ▒██ ░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
		▒██▒ ░  ░▒ ▓███▀ ░   ▒██▒   ░██▒ ▓█   ▓██▒▒██▒ █▄░▒████▒░██▓ ▒██▒
		▒▓▒░ ░  ░░ ░▒ ▒  ░   ░ ▒░   ░  ░ ▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
		░▒ ░       ░  ▒      ░  ░      ░  ▒   ▒▒ ░░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
		░░       ░           ░      ░     ░   ▒   ░ ░░ ░    ░     ░░   ░ 
				 ░ ░                ░         ░  ░░  ░      ░  ░   ░     
				 ░                                                       
		'''
	banner_5 = \
		'''
		╔═╗╔═╗  ╔╦╗╔═╗╦╔═╔═╗╦═╗
		╠═╝║    ║║║╠═╣╠╩╗║╣ ╠╦╝
		╩  ╚═╝  ╩ ╩╩ ╩╩ ╩╚═╝╩╚═
		'''
	banner_6 = \
		'''
		   ▄███████▄  ▄████████         ▄▄▄▄███▄▄▄▄      ▄████████    ▄█   ▄█▄    ▄████████    ▄████████ 
		  ███    ███ ███    ███       ▄██▀▀▀███▀▀▀██▄   ███    ███   ███ ▄███▀   ███    ███   ███    ███ 
		  ███    ███ ███    █▀        ███   ███   ███   ███    ███   ███▐██▀     ███    █▀    ███    ███ 
		  ███    ███ ███              ███   ███   ███   ███    ███  ▄█████▀     ▄███▄▄▄      ▄███▄▄▄▄██▀ 
		▀█████████▀  ███              ███   ███   ███ ▀███████████ ▀▀█████▄    ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
		  ███        ███    █▄        ███   ███   ███   ███    ███   ███▐██▄     ███    █▄  ▀███████████ 
		  ███        ███    ███       ███   ███   ███   ███    ███   ███ ▀███▄   ███    ███   ███    ███ 
		 ▄████▀      ████████▀         ▀█   ███   █▀    ███    █▀    ███   ▀█▀   ██████████   ███    ███ 
																	 ▀                        ███    ███ 
		'''
	banner_7 = \
		'''
		 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄    ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
		▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
		▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀      ▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌ ▐░▌ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
		▐░▌       ▐░▌▐░▌               ▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌▐░▌▐░▌  ▐░▌          ▐░▌       ▐░▌
		▐░█▄▄▄▄▄▄▄█░▌▐░▌               ▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌░▌   ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
		▐░░░░░░░░░░░▌▐░▌               ▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░░▌    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
		▐░█▀▀▀▀▀▀▀▀▀ ▐░▌               ▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌   ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ 
		▐░▌          ▐░▌               ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌  ▐░▌          ▐░▌     ▐░▌  
		▐░▌          ▐░█▄▄▄▄▄▄▄▄▄      ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌ ▐░▌ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ 
		▐░▌          ▐░░░░░░░░░░░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
		 ▀            ▀▀▀▀▀▀▀▀▀▀▀       ▀         ▀  ▀         ▀  ▀    ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀                        
		'''
	banner_8 = \
		'''
		 ▄▄▄· ▄▄·     • ▌ ▄ ·.  ▄▄▄· ▄ •▄ ▄▄▄ .▄▄▄  
		▐█ ▄█▐█ ▌▪    ·██ ▐███▪▐█ ▀█ █▌▄▌▪▀▄.▀·▀▄ █·
		 ██▀·██ ▄▄    ▐█ ▌▐▌▐█·▄█▀▀█ ▐▀▀▄·▐▀▀▪▄▐▀▀▄ 
		▐█▪·•▐███▌    ██ ██▌▐█▌▐█ ▪▐▌▐█.█▌▐█▄▄▌▐█•█▌
		.▀   ·▀▀▀     ▀▀  █▪▀▀▀ ▀  ▀ ·▀  ▀ ▀▀▀ .▀  ▀
		'''
	banner_list = [banner_2,
				   banner_3, banner_4,
				   banner_5, banner_6,
				   banner_7, banner_8]
	print(random.choice(banner_list))


def menu():
		for pick, i in enumerate(modes):
			print(f'{pick}) {i}')
		choice = input('Pick your Poison (e.g. 1): ')

		return choice


if __name__ == "__main__":
	import os
	import time
	import itertools
	import random
	from io import BytesIO

	import pandas as pd
	
	from bs4 import BeautifulSoup

	from PIL import Image

	from selenium import webdriver
	from selenium.webdriver.chrome.options import Options
	from selenium.webdriver.support.ui import WebDriverWait
	from selenium.webdriver.support import expected_conditions as EC
	from selenium.common.exceptions import TimeoutException
	
	start = time.perf_counter()
	# driver = init_browser()
	modes = ['Browsing', 'Gaming', 'Programming', 'Digital Editing', 'Game Developing', 'Architecting', 'Hacking']
	trigger = True
	
	while trigger is True:
		banner()
		temp = menu()
		try:
			if int(temp) in list(range(0, len(modes))):
				trigger = False
			else:
				raise Exception
		except Exception as err:
			trigger = True
			os.system('cls')
			print(f'{CmdColor.fail}Wrong choice! You entered "{temp}" which is invalid. Please input an option number of the above{CmdColor.end_sequence}')
	
	os.system('cls')
	if modes[int(temp)] == 'Browsing':
		color = CmdColor.browsing
	elif modes[int(temp)] == 'Gaming':
		color = CmdColor.gaming
	
	elif modes[int(temp)] == 'Programming':
		color = CmdColor.programming
	elif modes[int(temp)] == 'Digital Editing':
		color = CmdColor.digital_editing
	elif modes[int(temp)] == 'Game Developing':
		color = CmdColor.game_dev
	elif modes[int(temp)] == 'Architecting':
		color = CmdColor.architecht
	elif modes[int(temp)] == 'Hacking':
		color = CmdColor.hacking
	else:
		raise IndexError


	print('Give me more details about your:', f'{color}{modes[int(temp)]}{CmdColor.end_sequence}', 'PC!')
	
	