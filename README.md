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


## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
