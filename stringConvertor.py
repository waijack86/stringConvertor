import csv

# build the main menu
menus = {
	1: "Start Simulation",
	0: "Exit Program"}

# build the sub menu
subMenus = {
	1: "Retry Simulation",
	2: "Check CSV",
	0: "Exit Program"}

# define main function
def main():
	print("==========")
	print ("Welcome to String Convertor :)")
	print ()
	# print the menu by row
	for key, value in menus.items():
		print (str(key) + " - " + value)
	print()

	# check if it is a valid input option
	while True:
		data = input("Please choose an option >> ")
		# print error if it is not a digit
		if not data.isdigit():
			print("Invalid selection, please try again.")
			continue
		else:
			# convert the input into integer
			data = int(data)
			# exit the app if input is 0
			if data == 0:
				exitApp()
			# go to convertText function if input is 1
			elif data == 1:
				convertText()
			# return error if it is more than 1
			elif data > 1:
				print("Invalid selection, please try again.")
				continue

# define submenu function
def subMenu():
	print("==========")
	# print the menu by row
	for key, value in subMenus.items():
		print (str(key) + " - " + value)
	print()

	# checking whether the input is valid
	while True:
		data = input("Please choose an option >> ")
		# give error message for invalid input
		if not data.isdigit():
			print("Invalid selection, please try again.")
			continue
		else:
			# convert the input into integer
			data = int(data)
			# exit the app if input is 0
			if data == 0:
				exitApp()
			# go to convertText function if input is 1
			elif data == 1:
				convertText()
			# goto readCSV function if input is 2
			elif data == 2:
				readCSV()
			# return error if input more than 2
			elif data > 2:
				print("Invalid selection, please try again.")
				continue

# define convert text function
def convertText():
	print("==========")
	print("String Convertor")
	print("==========")

	# checking whether the input is valid
	while True:
		data = input("Please input a string to convert >> ")
		# give error message for invalid input
		if not len(data) >= 1:
			print("String cannot be blank.")
			continue
		else:
			print("==========")
			print("Output")
			print("==========")
			# convert the input into upper case
			upper = convertUpper(data)
			print("Upper Case: " + upper)
			# convert the input into alternate upper and lower
			alternate = convertAlternate(data)
			print("Alternate Case: " + alternate)
			# create csv file
			createCSV(data)
			print("CSV created!")
			# return sub menu after stdout
			subMenu()

# define function to convert input into upper case
def convertUpper(data):
	return data.upper()

# define function to convert input into alternate upper and lower case
def convertAlternate(data):
	res = ""
	for x in range(len(data)): 
		if not x % 2: 
			res = res + data[x].lower() 
		else: 
			res = res + data[x].upper() 
	return res

# define function to create csv file with the input
def createCSV(data):
	stringList = []
	# put input into a List
	for i in data:
		stringList.append(i)

	# create a csv file and insert the input with delimiter ,
	with open('csvFile.csv', "w") as csv_file:
		write = csv.writer(csv_file, delimiter=',')
		write.writerow(stringList) 

# define function to read csv file
def readCSV():
	with open('csvFile.csv', 'r') as csv_file:	
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			if any(row):
				print("==========")
				print(f'Content in CSV file: {", ".join(row)}')
	# return sub menu after stdout 
	subMenu()

# exit app function
def exitApp():
	print("==========")
	print ("Thanks for using this app, bye and see you again.")
	exit()

if __name__ == '__main__':
	main()

		
		