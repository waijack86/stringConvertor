# stringConvertor
 
Python project created for Setel System Reliability Assignment: Problem 1. 

Using object-oriented concepts, create a CLI tool that accepts a string and does the following to it:
- converts the string to uppercase and outputs it to stdout.
- converts the string to alternate upper and lower case and outputs it to stdout.
- creates a CSV file from the string by making each character a column in the CSV and then output "CSV created!" to stdout.

## Getting Started

### Prerequisites

You need Python 3.5 or later to run this file. You can have multiple Python versions (2.x and 3.x) installed on the same system without problems.

### Installing

See below link on how to install Python. 
```
https://realpython.com/installing-python/
```

## How to use this

Clone this to your working environment and run the below script in the directory. 
```
$ python stringConvertor.py
```

The app should show you the menu as below once the file has been executed successfully. 
```
1 - Start Simulation
0 - Exit Program
```

Select the menu 1 will start the String convertor or 0 to exit the program. 

The program will ask you to input string if menu 1 is selected. 

The String Convertor should do the below once received a valid input:
- converts the string to uppercase and outputs it to stdout.
- converts the string to alternate upper and lower case and outputs it to stdout.
- creates a CSV file from the string by making each character a column in the CSV and then output "CSV created!" to stdout.

Sample Input
```
hello world
```
 
Sample Output
```
HELLO WORLD
hElLo wOrLd
CSV created!
```

The program will show the submenu as below after the stdout is printed. 
```
1 - Retry Simulation
2 - Check CSV
0 - Exit Program
```

You may input menu 2 to check the content in CSV file. The CSV file is created on the root directory which containing the following: 
```
h,e,l,l,o, ,w,o,r,l,d
```

## Testing

There is a unittest python script created under the same directory and it can be run as below:
```
$ python unittestScript.py 
```

The unittest script is checking the below functions of the scriptConvertor:
1) test_upper
- To test whether the input being converted to upper case as expected. 
2) test)alternate
- To test whether the input being converted to have alternate upper and lower case as expected
3) test_csvExist
- To check whether the csv file being created and content matching with input
