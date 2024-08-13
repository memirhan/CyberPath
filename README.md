
# Cyber Path

It is a tool developed to perform directory scans for web applications. Users can explore existing directories and files by running various tests on URLs they specify. They can also test paths appended to URLs using a specified word list.


## Installation 

Install Cyber ​​Path

```bash 
  git clone https://github.com/memirhan/CyberPath
  cd CyberPath
  pip install -r requirements.txt
```
    
## Usage

```python
Usage: python cyberpath.py -u URL -w WORDLIST

Example Usage: python cyberpath.py -u https://github.com -w /Users/m.emirhan/Desktop/wordlist.txt
```

  
## Version
```python
1.0
```
  
## Last Update
### 12 August 2024
  
## GUİ




  ```python
  
   _____       _                ______     _   _     
/  __ \     | |               | ___ \   | | | |    
| /  \/_   _| |__   ___ _ __  | |_/ __ _| |_| |__  
| |   | | | | '_ \ / _ | '__| |  __/ _` | __| '_ \ 
| \__/| |_| | |_) |  __| |    | | | (_| | |_| | | |
 \____/\__, |_.__/ \___|_|     \_|  \__,_|\__|_| |_|
         __/ |                                      
        |___/             

---------------------------
https://github.com/memirhan
---------------------------
Version: 1.0
---------------------------
Last Update: 12 August 2024
---------------------------                          

Usage: python cyberpath.py -u URL -w WORDLIST

Example Usage: python cyberpath.py -u https://github.com -w /Users/m.emirhan/Desktop/wordlist.txt

Options:

  -u URL, --url URL ---> URL address [Required]

  -w WORDLIST, --wordlist WORDLIST ---> Wordlist path [Required]

  -o OUTPUT, --output OUTPUT ---> Output path
     Example usage for 'output' argument: -o /Users/m.emirhan/Desktop/output.txt

  -h, --help ---> Shows the user guide of the application

```
## Features

**Cyber Path** is a tool developed for performing directory scans on web applications. Users can explore existing directories and files by running various tests on specified URLs. Additionally, users can test paths appended to URLs using a specified word list. Here are the detailed features of the application:



    1. Directory Scanning:

        - Cyber Path performs directory scans on a specified URL to help discover existing directories and files.
        - It tests appended paths to the URL to find hidden or accessible directories and files.

    2. Word List Usage:

        - Users provide a customizable word list to test paths appended to URLs.
        - The word list can include various directory and file names, allowing for more extensive scanning.

    3. Output File

        - Option to save scan results to a file.
        - Users can specify a file path to save the results, making the scan output more organized and accessible.

    4. Ease of Use:

        - Provides a user-friendly command-line interface.
        - Perform scans using simple and clear commands.

    5. Help and Information:

        - Users can access information on how to use the application with `-h` or `--help` options.
        - Detailed information about various options and how to use them.

    6. Developer Support:

        - The application is open-source and available for anyone to use.
        - Users can provide feedback or report issues and suggestions for improvements.

## Just a little reminder


**Cyber Path** is an open-source tool designed to facilitate directory scanning for web applications. Its purpose is to help users explore and test the structure of web applications by analyzing URLs and directory paths.

As a relatively new project, Cyber Path is continuously evolving. Being in its early stages, it may still have some bugs and limitations. We appreciate your understanding and patience as we work to improve the application.

If you encounter any issues or have suggestions for enhancements, please do not hesitate to reach out. Your feedback is invaluable and will help us make Cyber Path better for everyone.

Thank you for using **Cyber Path**. Happy **hacking**.
### My social media accounts
 - https://instagram.com/memirhansumer
 - https://www.linkedin.com/in/muhammet-emirhan-sümer-2b07a3275/