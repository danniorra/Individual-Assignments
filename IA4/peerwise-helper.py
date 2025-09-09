# The package 'random' is used in this code
# import argparse
# import configparser
# import random
# #Page ranges
# # 113 - 155
# # 208 - 216
# # 1 - 2

# min_page = int(input('Lower page range: '))
# max_page = int(input('Upper page range: '))

# # Defining the page numbers
# pages = list(range(min_page, max_page))

# # Asking for no. of questions
# qs = int(input('How many pages? '))

# # Generating the specified amount of random pages
# for i in range(0,qs):
#     ind = random.randint(0,len(pages)-1)
#     print(pages[ind])
#     pages.pop(ind)

# Above is my old code

# To be honest I have no idea how I should get started with using the argparse and configparser modules 
# even after spending an hour reading up on these modules and viewing example codes. So I took a code that 
# was generated with DeepSeek with the following input:

# I have a simple python program that takes in lower/upper boundaries for pages and also takes an input for number of questions. 
# This code then creates a list of numbers within the range and chooses at random number of questions amount of numbers. 
# Now i need to change this code so that it will use the modules argparse and configparse. 
# The arguments should include the ability to set the minimum page, maximum page, and how many pages to choose. 
# Number of pages to choose is the same as number of questions. I also need to create a configuration file in my home directory called peerwise.ini. 
# There must be something in the peerwise.ini file. How would i implement these functionalities into my existing code ?

# I will do my best to explain this code in order to better understand it.


import argparse
import configparser
import random
import os

# Here i had to set the path to the configuration file 'peerwise.ini'
config_path = '/Users/daniel/Mech1/Individual-Assignments/peerwise.ini'

# This creates a config parser object
config = configparser.ConfigParser()

# This section chaecks if there exists a file at the specified path 'config_path' and reads it if the file exists.
# If the file does not exist then it will create that file at the specified path directory. 
if not os.path.exists(config_path):
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(config_path), exist_ok=True)
    
    # Set default values
    config['DEFAULT'] = {
        'min_page': '1',
        'max_page': '10',
        'num_questions': '5'
    }
    
    # Opens the directory as a write and writes the default values to the file.
    with open(config_path, 'w') as f:
        config.write(f)
else:
    # Read existing config file
    config.read(config_path)

# Set up argument parser with config defaults
parser = argparse.ArgumentParser(description='Random page selector')

# This adds the command line arguments I will be using to select the page range and number of pages to select
parser.add_argument('--min-page', type=int,
                    default=config['DEFAULT'].getint('min_page'),
                    help='Minimum page number (default: %(default)s)')
parser.add_argument('--max-page', type=int,
                    default=config['DEFAULT'].getint('max_page'),
                    help='Maximum page number (default: %(default)s)')
parser.add_argument('--num-questions', type=int,
                    default=config['DEFAULT'].getint('num_questions'),
                    help='Number of pages to select (default: %(default)s)')

# This line examines the arguments passed in and transforms them to 'namespace' instance wich is the args object caught by the program as the return value
args = parser.parse_args()

# This sections checks if the values pssed intu the program can be used, fx. the lower boundary should not be larger then the higher boundary
if args.min_page > args.max_page:
    parser.error("min_page cannot be greater than max_page")
    
if args.num_questions > (args.max_page - args.min_page + 1):
    parser.error("num_questions cannot exceed available pages in range")

# This creates a list with the specified values from the 'peerwise.ini' file
pages = list(range(args.min_page, args.max_page + 1))

# Selects at random the specified amount of pages
selected = []
for i in range(args.num_questions):
    if not pages:  # If no pages left, break
        break
    ind = random.randint(0, len(pages) - 1)
    selected.append(pages[ind])
    pages.pop(ind)

print(f"Selected pages: {selected}")