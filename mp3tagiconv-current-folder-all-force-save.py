# -*- coding: utf-8 -*-
import os
import sys
import locale
import mp3tagiconv

def print_help():
	print 'module_name <options>'
	print 'options:'
	print '\t:--force-save: force to save new tags'

def listdir(path, list_name):
	for file in os.listdir(path):
		file_path = os.path.join(path, file)
		if os.path.isdir(file_path):
			listdir(file_path, list_name)
		else:
			list_name.append(file_path)

if __name__ == "__main__":
	list = []
	force_save = '--do-update'
	listdir('.', list)
	"""
	if len(sys.argv) >= 2:
		if sys.argv[1] == '--force-save':
			force_save = '--do-update'
		elif sys.argv[1] is not None:
			print_help()
			exit()
	"""
	for filename in list:
		if filename.split('.')[-1].lower() == 'mp3':
			print filename
			mp3tagiconv.main([sys.argv[0], force_save, filename])
