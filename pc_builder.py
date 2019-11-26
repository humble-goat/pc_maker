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


def menu(ls, text):
		for pick, i in enumerate(ls):
			print(f'{pick}) {i}')
		choice = input(f'{text}')

		return choice


def menu_picker(func_to_call, ls):
	temp = func_to_call
	try:
		if int(temp) in list(range(0, len(ls))):
			return temp
		else:
			raise Exception
	except Exception as err:
		os.system('cls')



def mode_menu(check, color, ls, text):
	banner()
	print('Give me more details about your:', f'{color}{check}{CmdColor.end_sequence}', 'PC!')
	mode = menu_picker(menu(ls, text), ls)
	if not mode:
		print(f'{CmdColor.fail}Wrong choice! You entered "{mode}" which is invalid. Please input an option number of the above{CmdColor.end_sequence}')
		mode_menu(check, color, ls, text)
	return mode


def main_menu():
	start = time.perf_counter()
	# driver = init_browser()

	banner()

	style = menu_picker(menu(style_list, 'Pick your Poison (e.g. 1): '), style_list)
	if not style:
		print(f'{CmdColor.fail}Wrong choice! You entered "{style}" which is invalid. Please input an option number of the above{CmdColor.end_sequence}')
		main_menu()
	else:
		os.system('cls')

	if style_list[int(style)] == 'Browsing':
		color = CmdColor.browsing
	elif style_list[int(style)] == 'Gaming':
		color = CmdColor.gaming
	elif style_list[int(style)] == 'Programming':
		color = CmdColor.programming
	elif style_list[int(style)] == 'Digital Editing':
		color = CmdColor.digital_editing
	elif style_list[int(style)] == 'Game Developing':
		color = CmdColor.game_dev
	elif style_list[int(style)] == 'Architecting':
		color = CmdColor.architecht
	elif style_list[int(style)] == 'Hacking':
		color = CmdColor.hacking
	else:
		raise IndexError

	mode_menu(style_list[int(style)], color, mode_list, 'Enter your Mode (e.g. 0):')



if __name__ == '__main__':
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

	style_list = ['Browsing', 'Gaming', 'Programming', 'Digital Editing', 'Game Developing', 'Architecting', 'Hacking']
	mode_list = ['Simple', 'Advanced']
	main_menu()
