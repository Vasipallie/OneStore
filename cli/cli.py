import os 
import getpass
import time
import random
import string
from wonderwords import RandomWord
from supabase import create_client, Client
import hashlib
supabase: Client = create_client("https://gkkpwnqytanjsdjojqur.supabase.co", "sb_publishable_Sdn9s5v2IvPSjYlbjDDp_g_YnXbK_N8")

class colors:
    RESET = "\033[0m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    INVERTED = "\033[7m"
    PURPLE = "\033[95m"
def clrso():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')    
def onestorelogo():
    clrso()
    onestorelogo= """
     _____________________________________________________________________
    |                                                                     |
    |  ▄▄█▀▀▀█▄▄                    ▄█▀▀▀▄█   ▄                           |
    | ▄█▀     ██  ▄▄▄▄▄     ▄▄▄▄   ██▄▄  ▀  ▄██▄    ▄▄▄   ▄▄▄ ▄▄    ▄▄▄▄  |
    | ██      ██  ██  ██  ▄█▄▄▄██   ▀▀███▄   ██   ▄█  ▀█▄  ██▀ ▀▀ ▄█▄▄▄██ |
    | ▀█▄     ██  ██  ██  ██      ▄     ▀██  ██   ██   ██  ██     ██      |
    |  ▀▀█▄▄▄█▀  ▄██▄ ██▄  ▀█▄▄▄▀ █▀▄▄▄▄█▀   ▀█▄▀  ▀█▄▄█▀ ▄██▄     ▀█▄▄▄▀ |
    |_____________________________________________________________________|
    |                  Your Ultimate CLI Password Manager                 |
    |_____________________________________________________________________|
    """
    print(colors.GREEN + onestorelogo + colors.RESET)

def helpmenu():
    print(f"{colors.BOLD}{colors.CYAN}OneStore Help Menu{colors.RESET}")
    print(f"{colors.YELLOW}help{colors.RESET}           : Show this help menu")
    print(f"{colors.YELLOW}auth{colors.RESET}           : OneStore account Login/Signup")
    print(f"{colors.YELLOW}password-gen{colors.RESET}   : Generate a secure password")
    #NEED TO ADD MORE COMMANDS HERE LATER
    print(f"{colors.YELLOW}support{colors.RESET}        : Get OneStore support information")
    print(f"{colors.YELLOW}exit{colors.RESET}           : Exit OneStore")
    print("")
    input("Press enter/return to return to OneStore CLI:")
    onestoreinput()

def onestoreinput() -> None:
    onestorelogo()
    print(f"{colors.YELLOW}Type 'help' to see all the available OneStore commands {colors.RESET}")
    inputstr = input(f"{colors.BOLD}{colors.CYAN}OneStore >> {colors.RESET}")
    
    onestorelogo()
    if inputstr == "help":
        helpmenu()
    elif inputstr == "auth":
        auth()
    elif inputstr == "password-gen":
        passgen()
    elif inputstr == "exit":
        print("Exiting OneStore...")
        clrso()
        onestorelogo()
        print("Thank you for using OneStore")
        time.sleep(1)

        exit()
    else:
        print(f"{colors.RED}Unknown command: {inputstr}{colors.RESET}")
        onestoreinput()



def support():
    onestorelogo()
    print(f"{colors.BOLD}{colors.CYAN}OneStore Support Information{colors.RESET}")
    print("For support, please visit our github repo @ https://github.com/vasipallie/OneStore")
def auth():
    clrso()
    onestorelogo()
    print(f"{colors.BOLD}{colors.PURPLE}OneStore Authentication{colors.RESET}")
    print(f"{colors.YELLOW} 1. Login to your OneStore account{colors.RESET}")
    print(f"{colors.YELLOW} 2. Signup for a OneStore account{colors.RESET}")
    print(f"{colors.YELLOW} 3. Reset OneStore password{colors.RESET}")
    print(f"{colors.YELLOW} 4. Quit Auth{colors.RESET}")
    print(f"{colors.YELLOW}-------------------------------------{colors.RESET}")
    choice = input("Select an option : ")
    if choice == "1":
        login()
    elif choice == "2":
        signup()
    elif choice == "3":
        resetpass()
    elif choice == "4":
        onestoreinput()
    else:
        print(f"{colors.RED} Invalid choice. Please try Again")
        time.sleep(1)
        auth()
        
# BEFORE PRODUCTION ADD THE RESET FUNCTIONALITY HERE
# Dont be lazy smh
def resetpass():
    onestorelogo()
    print(f"{colors.BOLD}{colors.PURPLE}OneStore Authentication Master {colors.RESET}")
    print(f"{colors.BOLD}{colors.CYAN}OneStore password reset{colors.RESET}")
    email = input(f"{colors.BOLD}{colors.CYAN}Enter your OneStore email: {colors.RESET}")
    response = supabase.auth.reset_password_for_email(email)
    print(response)
    if response:
        print(f"{colors.GREEN}Password reset email sent! Please check your email to reset your OneStore password.{colors.RESET}")
        time.sleep(2)
        onestoreinput()
    else:
        print(f"{colors.RED}FAILED TO SEND PASSWORD RESET EMAIL! Please check your email and try again.{colors.RESET}")
        print(f"{colors.CYAN}If this issue persists, please contact OneStore support.{colors.RESET}")
        print(f"{colors.CYAN}Redirecting to OneStore{colors.RESET}")
        time.sleep(5)
        onestoreinput()
def signup():
    onestorelogo()
    print(f"{colors.BOLD}{colors.PURPLE}OneStore Authenticate {colors.RESET}")
    print(f"{colors.YELLOW}Signup for a OneStore account{colors.RESET}")
    email = input(f"{colors.BOLD}{colors.CYAN}Enter your OneStore email: {colors.RESET}")
    password = getpass.getpass(f"{colors.BOLD}{colors.CYAN}Create a OneStore password: {colors.RESET}")
    confirm_password = getpass.getpass(f"{colors.BOLD}{colors.CYAN}Confirm your OneStore password: {colors.RESET}")

    if password != confirm_password:
        print(f"{colors.RED}Passwords do not match. Please try again.{colors.RESET}")
        time.sleep(1)
        signup()
    else:
        response = supabase.auth.sign_up({
            "email": email,
            "password": password,
        })
        if response.user: 
            rword = RandomWord()
            uid = response.user.id
            key1 = rword.word(word_min_length=3, word_max_length=8).lower()
            key2 = rword.word(word_min_length=3, word_max_length=8).lower()
            key3 = rword.word(word_min_length=3, word_max_length=8).lower()
            key4 = rword.word(word_min_length=3, word_max_length=8).lower()
            key5 = rword.word(word_min_length=3, word_max_length=8).lower()
            finalkey = key1 + key2 + key3 + key4 + key5

            usualchar = "!@#$%&*"
            characters = string.ascii_letters + string.digits + usualchar
            salt = ''.join(random.choice(characters) for i in range(7))
            response = (
                supabase.table("Databayse")
                .insert({"useruid": uid, "salt": salt, "hash": hashlib.sha256((finalkey + salt).encode()).hexdigest()})
                .execute()
            )
            checkpass = False
            while checkpass == False:
                onestorelogo()
                print(f"{colors.BOLD}{colors.PURPLE}OneStore Authenticate {colors.RESET}")
                print(f"{colors.BOLD}{colors.PURPLE}-------------------------------------{colors.RESET}")
                print(f"{colors.RED} PLEASE NOTE DOWN YOUR ONESTORE KEYPHRASES!{colors.RESET}")
                print(f"{colors.YELLOW} These keyphrases are required to recover your OneStore account. {colors.RESET}")
                print(f"{colors.YELLOW} If you lose these keyphrases, you will lose access to your OneStore account permanently. {colors.RESET}")
                print(f"{colors.BOLD}{colors.CYAN}-------------------------------------{colors.RESET}")
                print(f"{colors.BOLD}{colors.GREEN} 1. {key1}{colors.RESET}")
                print(f"{colors.BOLD}{colors.GREEN} 2. {key2}{colors.RESET}")
                print(f"{colors.BOLD}{colors.GREEN} 3. {key3}{colors.RESET}")
                print(f"{colors.BOLD}{colors.GREEN} 4. {key4}{colors.RESET}")
                print(f"{colors.BOLD}{colors.GREEN} 5. {key5}{colors.RESET}")
                print(f"{colors.BOLD}{colors.CYAN}-------------------------------------{colors.RESET}")
                confirm = input(f"{colors.BOLD}{colors.CYAN}Type 'confirm' to confirm you have noted down your keyphrases: {colors.RESET}")
                if confirm == "confirm":
                    clrso()
                    onestorelogo()
                    print(f"{colors.BOLD}{colors.PURPLE}OneStore Authenticate {colors.RESET}")
                    key1i= input(f"{colors.BOLD}{colors.CYAN}Enter keyphrase 1: {colors.RESET}").lower()
                    key2i= input(f"{colors.BOLD}{colors.CYAN}Enter keyphrase 2: {colors.RESET}").lower()
                    key3i= input(f"{colors.BOLD}{colors.CYAN}Enter keyphrase 3: {colors.RESET}").lower()
                    key4i= input(f"{colors.BOLD}{colors.CYAN}Enter keyphrase 4: {colors.RESET}").lower()
                    key5i= input(f"{colors.BOLD}{colors.CYAN}Enter keyphrase 5: {colors.RESET}").lower()
                    if key1 == key1i and key2 == key2i and key3 == key3i and key4 == key4i and key5 == key5i:
                        clrso()
                        onestorelogo()
                        print(f"{colors.BOLD}{colors.PURPLE}OneStore Authenticate {colors.RESET}")
                        print(f"{colors.GREEN}Keyphrases confirmed! Your OneStore account has been created successfully.{colors.RESET}")
                        print(f"{colors.GREEN}You can now login to your OneStore account using your email and password.{colors.RESET}")
                        time.sleep(2)
                        checkpass = True
                        clrso()
                        login()
                    else:
                        print(f"{colors.RED}Keyphrases do not match. Please try again.{colors.RESET}")
                        print(f"{colors.RED}Defaulting to KEYPHRASES@OneStore{colors.RESET}")
                        print(f"{colors.RED}Please save these keyphrases in a safeplace{colors.RESET}")
                        time.sleep(0.5)
            
def login():
    onestorelogo()
    print(f"{colors.BOLD}{colors.PURPLE}OneStore Authenticate {colors.RESET}")
    print(f"{colors.YELLOW}Login to your OneStore account{colors.RESET}")
    email = input(f"{colors.BOLD}{colors.CYAN}Enter your OneStore email: {colors.RESET}")
    password = getpass.getpass(f"{colors.BOLD}{colors.CYAN}Enter your OneStore password: {colors.RESET}")
    response = supabase.auth.sign_in_with_password({
        "email": email,
        "password": password,
    })
    print(response)
    if response.user:
        clrso()
        onestorelogo()
        print(f"{colors.GREEN}Login Successful! Welcome back to OneStore.{colors.RESET}")
        time.sleep(1)
        onestoreinput()
    else:
        print(f"{colors.RED}Login FAILED! Please check your email and password and try again.{colors.RESET}")


def passstore(url="", username="", password=""):
    print('UNDER DEVELOPEMENT')
    
def passgen():
    length = 12
    length = int(input("Enter desired password length (default 12): ") or 12)
    usualchar = "!@#$%&*"
    characters = string.ascii_letters + string.digits + usualchar
    password = ''.join(random.choice(characters) for i in range(length))
    print(f"Generated password: {password}")

    if input("Do you want to save this password? (y/n): ").lower() == 'y':
        url = input("Enter the URL/Service name: ")
        username = input("Enter the username: ")
        passstore(url, username, password)
    else:
        print("Password not saved.")
        input("Press enter/return to return to OneStore CLI:")
        onestoreinput()
    
onestoreinput()
