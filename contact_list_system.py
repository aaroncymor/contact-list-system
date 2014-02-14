"""
=========================START OF CONTACT LIST FUNCTIONS==================
"""
#This will read the file and generate the list and append it to another list
def generate_contact_list(filename):
	txt = open(filename).read()
	sub_list = txt.split('\n')
	main_list = []
	
	for list in range(len(sub_list)):
		main_list.append(sub_list[list].split(";"))
	
	while main_list[-1] == '':
		main_list.pop(-1)
	
	return main_list

def save_file(filename, contact_list):
	new_txt = open(filename,'w')
	
	for contact in contact_list:
		if contact != contact_list[-1]:
			new_txt.write(";".join(contact) + "\n")
		else:
			new_txt.write(";".join(contact))
	
#Finds the indexes of the sub-list through given name, address, or phone number
def find_sub_list_index(contact_list,name='',address='',phone_num=''):
	index_list = [] #This list will be populated by the indexes found
	for contact in range(len(contact_list)):
		if name in contact_list[contact] or address in contact_list[contact] or phone_num in contact_list[contact]:
			index_list.append(contact)
	return index_list

#This will be the number of items in the sub-list
def count_sub_list_index(sub_list):
	return len(sub_list)
	
#Display sub_lists that were searched
def display_sub_lists(contact_list,sub_list_index):
	display_text = ''
	
	if count_sub_list_index(sub_list_index) > 0:
		for index in range(len(sub_list_index)):
			display_text += "\n[" + str(index + 1) + "]" 
			for item in range(len(contact_list[index])):
				if item == 0:
					display_text += "\nName: " + contact_list[sub_list_index[index]][item]
				if item == 1:
					display_text += "\nAddress: " + contact_list[sub_list_index[index]][item]
				if item == 2:
					display_text += "\nPhone Number: " + contact_list[sub_list_index[index]][item] + "\n"
	else:
		display_text += 'There are no contacts to display!\n NOTE: Please type 3 or more characters when searching.'
				
	return display_text

#Displays all contacts
def display_all_contacts(contact_list):
	display_text = ''
	for contact in range(len(contact_list)):
		for item in range(len(contact_list[contact])):
			if item == 0:
				display_text += "\nName: " + contact_list[contact][item]
			if item == 1:
				display_text += "\nAddress: " + contact_list[contact][item]
			if item == 2:
				display_text += "\nPhone Number: " + contact_list[contact][item] + "\n"
	return display_text

#Search contact by name - similary to contains in SQL
def search_contact(contact_list,contact,type):
	option = {'name':0, 'address':1, 'phone':2}
	item_list = []
	sub_list_index = []
	begin_counter = 0
	end_counter = len(contact)
	
	if len(contact) >= 3:
		for i in range(len(contact_list)):
			if len(contact_list[i][option[type]]) >= len(contact):
				while len(contact_list[i][option[type]]) >= end_counter:
					item_list.append(contact_list[i][option[type]][begin_counter:end_counter].lower())
					
					if contact in item_list:
						if i not in sub_list_index:
							sub_list_index.append(i)
							del item_list[:]
							break
							
					begin_counter = begin_counter + 1
					end_counter = end_counter + 1	
							
			begin_counter = 0
			end_counter = len(contact)
	return sub_list_index

#Inserts contact to the contact_list
def add_contact(contact_list,name,address,phone_num=''):
	#This sub_contact_list will be populated by the given name, address, and phone number
	message = ''
	sub_contact_list = []
	
	#If there is no existing
	if count_sub_list_index(find_sub_list_index(contact_list,name,address,phone_num)) == 0:
		if not name or not address:
			message += "Please fill in name and address!"
		else:
			sub_contact_list.append(name)
			sub_contact_list.append(address)
			sub_contact_list.append(phone_num)
				
			message += 'Contact successfully added!'
			#Add the item to the main list
			
			contact_list.append(sub_contact_list)
	else:
		message += 'The contact that you\'re trying to add, already exists!'
		
	return message
				
def update_contact(contact_list,sub_list_index,name='',address='',phone_num=''):
	#This will display status of the update.
	message = ''
	
	#These variables will store the values from the contact_list[index]
	#before they get updated/edited.
	old_name = ''
	old_address = ''
	old_phone_num = ''
	
	#If user provided the name, it will update the name of the sub-list
	if name != '':
		old_name = contact_list[sub_list_index][0]
		contact_list[sub_list_index][0] = name
		message += old_name + ' was successfully changed to ' + name + '.\n'
	
	#If user provided the add, it will update the add of the sub-list
	if address != '':
		old_address = contact_list[sub_list_index][1]
		contact_list[sub_list_index][1] = address
		message += old_address + ' was successfully changed to ' + address + '.\n'
	
	#If user provided the phone, it will update the phone of the sub-list
	if phone_num != '':
		curr_phone_num = contact_list[sub_list_index][2]
		contact_list[sub_list_index][2] = phone_num
		message += old_phone_num + ' was successfully changed to ' + phone_num + '.\n'
	
	return message

def delete_contact(contact_list,sub_list_index):
	message = 'Contact successfully deleted!'
	del contact_list[sub_list_index]
	return message

"""
==================END OF CONTACT LIST SYSTEM FUNCTIONS=================
"""

from sys import argv

script, filename = argv
prompt = "Display [D] | Search [S] | Add [A] | Save [V] | Exit [X] "
sub_prompt = "Please choose what you wanted to do with the searched contacts:\nUpdate [U] | Delete [E] | Exit [X] "
save_prompt = "Please coose if you want to overwrite or save in a new file:\nOverwrite[O] | New [N] | Exit [X] "
exit = 0
sub_exit = 0

#This will open the file and generate a list which will contain the sub-lists of contacts
cont_list = generate_contact_list(filename)

while exit == 0:
	option_list = ['D','d','S','s','A','a','U','u','E','e','X','x','V','v','N','n','O','o']
	#Ask user for input
	option = raw_input(prompt)
	
	if option in option_list:
		if option == option_list[0] or option == option_list[1]: #Display
			#Contact Lists will be displayed in command prompt
			print display_all_contacts(cont_list)
			continue
		if option == option_list[2] or option == option_list[3]: #Search:
			type_list = {1:'Name', 2:'Address', 3:'Phone'}
			prompt_type = "Choose what you need to search: \nName [1] | Address [2] | Phone [3] "
			
			try:
				key = int(raw_input(prompt_type))

				if key in type_list.keys():
					input = raw_input(type_list[key] + ": ")
					sub_list_index = search_contact(cont_list,input.lower(),type_list[key].lower())
					print display_sub_lists(cont_list,sub_list_index)
					
					if sub_list_index:
						sub_option = raw_input(sub_prompt)
							
						if sub_option in option_list:
							if sub_option == option_list[6] or sub_option == option_list[7]: #Update
						
								cont_id = int(raw_input("Please choose the number you need to update: "))
								cont_name = raw_input("Name: ")
								cont_address = raw_input("Address: ")
								cont_phone = raw_input("Phone Number: ")
								
								print update_contact(cont_list,sub_list_index[cont_id - 1],cont_name,cont_address,cont_phone)
								print display_all_contacts(cont_list)
								continue
							elif sub_option == option_list[8] or sub_option == option_list[9]: #Delete
								cont_id = int(raw_input("Please choose the number you need to delete: "))
								try:
									print delete_contact(cont_list,sub_list_index[cont_id - 1])
									print display_all_contacts(cont_list)
								except IndexError:
									print "Number does not exist!"
								continue
							elif sub_option == option_list[10] or sub_option == option_list[11]: #Exit
								continue
					else:
						continue
				else:
					print "Please choose the following: Name [1] | Address [2] | Phone [3] "
			except ValueError:
				print "Please type numbers only!"
			continue
		elif option == option_list[4] or option == option_list[5]: #Add
			print "Please type in your name, address, and phone number."
			print "**Please take note that name and address is required.\n"
			
			cont_name = raw_input("Name: ")
			cont_address = raw_input("Address: ")
			cont_phone = raw_input("Phone Number: ")
			
			#Checks if there are existing contacts
			if count_sub_list_index(find_sub_list_index(cont_list,cont_name,cont_address,cont_phone)) >= 1:
				print "The contact you\'re trying to register already exists!"
			else:
				print add_contact(cont_list,cont_name,cont_address,cont_phone)
				print display_all_contacts(cont_list)
			continue
		elif option == option_list[12] or option == option_list[13]: #Save
			save_option = raw_input(save_prompt)
			if save_option in option_list:
				if save_option == option_list[14] or save_option == option_list[15]: #New
					new_filename = raw_input("Please type in a new filename")
					save_file(new_filename + ".txt",cont_list)
					print new_filename + ".txt was successfully saved!"
					continue
				elif save_option == option_list[16] or save_option == option_list[17]: #Overwrite
					save_file(filename,cont_list)
					print filename + "was successfully overwrited!"
					continue
				elif save_option == option_list[10] or save_option == option_list[11]:
					continue
		elif option == option_list[10] or option == option_list[11]: #Exit
			sure = raw_input("Are you sure? Y/N ")
			if not sure:
				continue
			elif sure:
				if sure == 'Y' or sure == 'y':
					exit = 1
				elif sure == 'N' or sure == 'n':
					exit = 0
					continue
	else:
		print "\nYou can only choose from the following: \n"
		print "Display [D] | Search [S] | Add [A] | Save [V] | Exit [X] "
		print "===========================================================\n"
		continue 