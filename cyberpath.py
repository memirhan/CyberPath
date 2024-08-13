import argparse
import sys
import re
import requests
import os
import time

RED = '\033[91m'
GREEN = '\033[92m'
ORANGE = '\033[38;5;208m'
YELLOW = '\033[93m'
PURPLE = '\033[34m'
CYAN = '\033[36m'
RESET = '\033[0m'

CODE403 = "Forbidden Error"
CODE404 = "Not found"
CODE406 = "Not Acceptable"
CODE429 = "Too Many Requests"

output = []
founds = 0
def main(url, wordlist, outputPath, outputName):
    try:
        CyberPath()
        print(f"{PURPLE}URL{RESET}: {url}")
        print(f"{GREEN}Wordlist{RESET}: {wordlist}")
        print(f"{CYAN}Output Path{RESET}: {outputPath}")
        print(f"{RED}Output Name{RESET}: {outputName}\n")
        print(f"{ORANGE}[*] Started...{RESET}\n")

        if not os.path.isfile(wordlist):
            print(f"{RED}[-] The specified file could not be found{RESET}\n")
            sys.exit(1)

        elif not wordlist.lower().endswith('.txt'):
            print(f"{RED}[-] The file extension must be .txt{RESET}\n")
            sys.exit(1)

        else:
            pass

        try:
            with open(wordlist, "r", encoding='utf-8') as wordlistFile:
                wordlist = wordlistFile.readlines()

        except UnicodeDecodeError:
            print(f"{RED}[-] A Unicode error occurred while reading the file{RESET}\n")
            sys.exit(1)

        for word in wordlist:
            word = word.split('#',1)[0].strip()
            if word:
                Buster(normalUrlConvert(url), word)

        if outputPath and outputName:
            try:

                outputFilePath = os.path.join(outputPath, outputName)
                with open(outputFilePath, "w", encoding="utf-8") as file:
                    for out in output:
                        file.write("{}\n".format(out))

            except FileNotFoundError:
                print(f"{RED}[-] The specified file could not be found{RESET}\n")
                sys.exit(1)
        else:
            pass

        print(f"\n{GREEN}[+] {founds} successful directories found{RESET}")
        print(f"\n{YELLOW}[*] Finished...\n")

    except IsADirectoryError:
        print(f"{RED}[-] The specified file could not be found{RESET}\n")
        sys.exit(1)

    except KeyboardInterrupt:
        if outputPath and outputName:
            fileName, fileExtension = os.path.splitext(outputName)
            try:
                if fileExtension == ".txt":

                    outputFilePath = os.path.join(outputPath, outputName)
                    with open(outputFilePath, "w", encoding="utf-8") as file:
                        for out in output:
                            file.write("{}\n".format(out))

                    print(f"\n{GREEN}[+] {founds} successful directories found{RESET}")
                    print(f"\n{YELLOW}[*] Found directories saved to {outputFilePath}{RESET}")
                    print(f"\n{ORANGE}[*] Finished...\n")

                elif fileExtension != ".txt":
                    print(f"{RED}\n[-] The file extension could not be saved because it must be .txt\n")
                    print(f"\n{ORANGE}[*] Finished...\n")

            except FileNotFoundError:
                print(f"{RED}[-] Directory does not exist - {outputFilePath}{RESET}")
                sys.exit(1)

        else:
            pass

def parseArgs():
    parser = argparse.ArgumentParser(add_help=False)  # Standart yardım mesajını kapat
    parser.add_argument('-u', '--url', type=str, help='URL parametresi')
    parser.add_argument('-w', '--wordlist', type=str, help='Wordlist dizini')
    parser.add_argument('-o', '--output', type=str, help='Output dizini')
    parser.add_argument('-h', '--help', action='store_true', help='Show this help message and exit')
    args, unknown = parser.parse_known_args()

    try:
        if args.output:
            outputPath, outputName = os.path.split(args.output)

            if not outputPath:
                try:
                    CyberPath()
                    print(f"{RED}[-] Output path not specified{RESET}\n")
                    outputPath = None
                    outputName = None

                except Exception as e:
                    print(e)

            if not outputName or not os.path.splitext(outputName)[1]:
                try:
                    CyberPath()
                    print(f"{RED}[-] File name or extension is missing\n")
                    outputName = None
                    outputPath = None
                    sys.exit(1)

                except Exception as e:
                    print(e)

            if not os.path.isdir(outputPath):
                try:
                    CyberPath()
                    print(f"{RED}[-] Directory does not exist - {outputPath}{RESET}\n")
                    sys.exit(1)

                except Exception as e:
                    print(e)

        else:
            outputPath = None
            outputName = None

        return args, unknown, outputPath, outputName

    except FileNotFoundError:
        pass

def Buster(domain, word):
    url = f"{domain}/{word}"
    url = normalUrlConvert(url)
    global founds

    try:
        response = requests.get(url, allow_redirects=False, timeout=5)
        statusCode = response.status_code

        if statusCode == 403:
            print(f"{RED} [-] {url} {CODE403} : Code {statusCode}{RESET}")

        elif statusCode == 404:
            print(f"{RED}[-] {url} {CODE404} : Code {statusCode}{RESET}")

        elif statusCode == 406:
            print(f"{RED}[-] {url} {CODE406} : Code {statusCode}{RESET}")

        elif statusCode == 429:
            print(f"{RED}[-] {url} {CODE429} : Code {statusCode}{RESET}")
            waitTime = 15
            while waitTime > 0:
                sys.stdout.write('\r' + ' ' * 80)
                sys.stdout.write(f"\r{YELLOW}[*] Too many requests have been made. Will try again in {waitTime} seconds{RESET}")
                sys.stdout.flush()
                time.sleep(1)
                waitTime -= 1

            responseRepeat = requests.get(url, allow_redirects=False, timeout=5)
            statusCodeRepeat = responseRepeat.status_code

            if statusCodeRepeat == 403:
                print(f"{RED}[-] {url} {CODE403} : Code {statusCodeRepeat}{RESET}")

            elif statusCodeRepeat == 404:
                print(f"\n{RED}[-] {url} {CODE404} : Code {statusCodeRepeat}{RESET}")

            elif statusCodeRepeat == 406:
                print(f"{RED}[-] {url} {CODE406} : Code {statusCodeRepeat}{RESET}")

            elif statusCodeRepeat == 426:
                print(f"{RED}[-] {url} {CODE429} : Code {statusCodeRepeat}{RESET}")

            else:
                print(f"{CODE429}")

        else:
            print(f"{GREEN}[+] {url} Found : Code {statusCode}{RESET}")
            output.append(url)
            founds += 1

    except requests.exceptions.RequestException as e:
        errorMesage = str(e)

        if "NameResolutionError" in errorMesage:
            print(f"{RED}[-] There is no internet connection or the URL address is incorrect{RESET}\n")
            sys.exit(1)
        else:
            print(f"{RED}[-]: {url} - {errorMesage}{RESET}")

def normalUrlConvert(url):
    url = re.sub(r'#.*$', '', url)
    protocolEnd = url.find('://') + 3

    if protocolEnd == 2:
        url = 'http://' + url
        protocolEnd = url.find('://') + 3

    protocol = url[:protocolEnd]
    dizin = url[protocolEnd:]

    dizin = re.sub(r'/{2,}', '/', dizin)

    if dizin.endswith('/'):
        dizin = dizin[:-1]

    return protocol + dizin

def ValidUrlCheck(url):
    regex = re.compile(
        r'^(?:http|https)://',
        re.IGNORECASE
    )
    return re.match(regex, url) is not None

def helpCenter():
    print(f"\n{GREEN}Usage{RESET}: python cyberpath.py -u URL -w WORDLIST")
    print(f"\n{GREEN}Example Usage{RESET}: python cyberpath.py -u https://github.com -w /Users/m.emirhan/Desktop/wordlist.txt")

    print(f"\n{ORANGE}Options{RESET}:\n")
    print(f"  -u URL, --url URL ---> URL address {RED}[Required]{RESET}\n")
    print(f"  -w WORDLIST, --wordlist WORDLIST ---> Wordlist path {RED}[Required]{RESET}\n")
    print("  -o OUTPUT, --output OUTPUT ---> Output path")
    print(f"     {ORANGE}Example usage for 'output' argument{RESET}: -o /Users/m.emirhan/Desktop/output.txt\n")
    print("  -h, --help ---> Shows the user guide of the application\n\n")

def CyberPath():
    print(""" 
 _____       _                ______     _   _     
/  __ \     | |               | ___ \   | | | |    
| /  \/_   _| |__   ___ _ __  | |_/ __ _| |_| |__  
| |   | | | | '_ \ / _ | '__| |  __/ _` | __| '_ \ 
| \__/| |_| | |_) |  __| |    | | | (_| | |_| | | |
\____/ \__, |_.__/ \___|_|    \_|  \__,_|\__|_| |_|
        __/ |                                                      
       |___/                     
            """)

    print("------------------------------------")
    print(f"{ORANGE}Author{RESET}: https://github.com/memirhan")
    print("------------------------------------")
    print(f"{ORANGE}Version{RESET}: 1.0")
    print("------------------------------------")
    print(f"{ORANGE}Last Update{RESET}: 12 August 2024")
    print("------------------------------------\n")

if __name__ == "__main__":
    args, unknown, outputPath, outputName = parseArgs()

    if unknown:
        CyberPath()
        unknownArgs = ', '.join(unknown)
        print(f"{RED}[-] There is no argument named {unknownArgs} available{RESET}\n")
        sys.exit(1)

    if args.help:
        CyberPath()
        helpCenter()
        sys.exit(1)

    if not args.url and not args.wordlist:
        CyberPath()
        print(f"{RED}[-] Use -h or --help for usage information{RESET}\n")
        sys.exit(1)

    if not args.url:
        CyberPath()
        print(f"{RED}[-] The -u [--url] option is missing{RESET}\n")
        sys.exit(1)

    if not args.wordlist:
        CyberPath()
        print(f"{RED}[-] The -w [--wordlist] option is missing{RESET}\n")
        sys.exit(1)

    if not ValidUrlCheck(args.url):
        CyberPath()
        print(f"{RED}[-]: Protocol error, URL must contain https or http{RESET}\n")
        sys.exit(1)

    main(args.url, args.wordlist, outputPath, outputName)