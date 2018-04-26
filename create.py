'''
Author: Evan Arends
File: create.py
to-run: python create.py
python v. 2.7
FUNCTIONALITY:
	- Takes in json file that contains an Array of json objects
	- will create a folder , which contains a json file for each object contained in the json file which contains the array of obejects
file array of stuff.json 
	[{"name":"evan","school":"Gonzga"},{"name":"Dave","school":"Bishop"}] 
	-> is converted to two files one for each array item named after name field
	evan.json containing {"name":"evan","school":"Gonzga"}
	and 
	Dave.json containing {"name":"Dave","school":"Bishop"}
'''
#depencies
import json
import re
import os

'''
Function - write
input - str - string to be wrtitten to a file
	  - fn - folder name of file location 
	  - file_out_id - id to help you find file name by calling findId
'''
def write(str,fn,file_out_id):
	id = findID(str,file_out_id)
	file = open(fn + id + ".json",'w') 
	str.replace("^","'")
	file.write(str) 

'''
Function findID
- Will turn a string into a list with each index being a string found inbetween a set of quotes
- used to find id within object
'''	
def findID(str,id):
	str_list = re.findall('"([^"]*)"', str)
	new_id = ""
	for i in range(len(str_list)):
		if "id" == str_list[i]:
			return str_list[i + 1]
	return "null"

	
def read(folder,file_in_name,file_out_id):
	file = open(file_in_name, 'r') 
	c = file.read() #string
	clist = list(c) #list of chars
	lbc = 0 # "{"
	rbc = 0 # "}"
	temp = "" # json file contents
	'''
	Loop through each character
	look for left and right brackets to indicate begin/end objects
	replace ' with ^ so does not mess with object format
	replace back when in string
	'''
	for char in clist:
		if char == "'":
			temp = temp + "^"
			continue
		if char == "{":
			temp = temp + char
			lbc+=1
		if lbc != 0 and char != "}" and char != "{":
			temp = temp + char
		else:
			if char == "}":
				temp = temp + char
				rbc += 1
				if (lbc == rbc):
					write(temp,folder,file_out_id)
					lbc = 0
					rbc = 0
					temp = ""
					

	
			
			
		
		
def main():
	new_folder = "C:/Users/Evan/Documents/code/Hearthstone Pack Tracker/cards/" #Set your own location for new folder
	if not os.path.exists(new_folder):
		os.makedirs(new_folder) #Create folder
	
	'''
	Call main read function with ...
		- name of file to be read from 
		- what object variable would you like to name each file 
		- refer to top of page for file_in name and file_out_id
	'''
	file_in = "cards.json"
	file_out_id= "id"
	read(new_folder,file_in,file_out_id)
	

main()
		
			
			
			

