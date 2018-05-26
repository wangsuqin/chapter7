'''

'''
import os

def run(**args):
	print("[*] in dirlist module")
	files = os.listdir(".")
	
	return str(files)

