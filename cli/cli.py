import os 
import getpass
import time
import random
import string
from wonderwords import RandomWord
from supabase import create_client, Client
import hashlib
from cryptography.fernet import Fernet
import base64
import json
supabase: Client = create_client("https://gkkpwnqytanjsdjojqur.supabase.co", "sb_publishable_Sdn9s5v2IvPSjYlbjDDp_g_YnXbK_N8")
global key
KeyExists = False
OneStorePath = os.path.join(os.path.expanduser("~"), ".onestore")
KeyPath = os.path.join(OneStorePath, "keyphrases.txt")
SessionPath = os.path.join(OneStorePath, "session.json")


# Terminal colors (this is better than importing ig?) 
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

# Encryption and Decryption functions (lgm -- don't touch Istg)
def get_fernet_key() -> bytes:
    keyphrases = ""
    with open(KeyPath, "r") as file:
        keyphrases = file.read().strip()
    key_bytes = hashlib.sha256(keyphrases.encode()).digest()
    return base64.urlsafe_b64encode(key_bytes)
def encrypt_data(data: dict) -> str:
    keyen = get_fernet_key()
    fernet = Fernet(keyen)
    json_str = json.dumps(data)
    encrypted = fernet.encrypt(json_str.encode())
    return encrypted.decode()
def decrypt_data(encrypted_str: str) -> dict:
    keyen = get_fernet_key()
    fernet = Fernet(keyen)
    decrypted = fernet.decrypt(encrypted_str.encode())
    return json.loads(decrypted.decode())

## BASE CODE (for the UI and UX :P)
def clrso():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')    
def onestorelogo():
    clrso()
    check = ""
    if authcheck() == True:
        check = "Authenticated"
    else:
        check = "Not Authenticated"
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
|_____________________________________________________________________|"""
    print(colors.GREEN + onestorelogo + colors.RESET)
    print(f"{colors.GREEN}  You are {check} into OneStore.{colors.RESET}")
def helpmenu():
    print(f"{colors.BOLD}{colors.CYAN}OneStore Help Menu{colors.RESET}")
    print(f"{colors.YELLOW}help{colors.RESET}           : Show this help menu")
    print(f"{colors.YELLOW}auth{colors.RESET}           : OneStore account Login/Signup")
    print(f"{colors.YELLOW}password-gen{colors.RESET}   : Generate a secure password")
    print(f"{colors.YELLOW}passstore{colors.RESET}      : Store a password in OneStore")
    print(f"{colors.YELLOW}clear-passstore{colors.RESET} : Clear all stored passwords in OneStore")
    print(f"{colors.YELLOW}passretrieve{colors.RESET}   : Retrieve stored passwords from OneStore")
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
    elif inputstr == "clear-passstore":
        clearpassstore()
    elif inputstr == "password-gen":
        passgen()
    elif inputstr == "passretrieve":
        passretrieve()
    elif inputstr == "support":
        support()
    elif inputstr == "passstore":
        passstore()
    elif inputstr == "exit":
        print("Exiting OneStore...")
        clrso()
        onestorelogo()
        print("Thank you for using OneStore")
        time.sleep(1)
        exit()
    else:
        print(f"{colors.BOLD}{colors.RED}Unknown command: {inputstr}{colors.RESET}")
        print(f"{colors.CYAN}Returning to OneStore CLI...{colors.RESET}")
        time.sleep(2)
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
    print(f"{colors.YELLOW} 4. Logout of OneStore{colors.RESET}")
    print(f"{colors.YELLOW} 5. Quit Auth{colors.RESET}")
    print(f"{colors.YELLOW}-------------------------------------{colors.RESET}")
    choice = input("Select an option : ")
    if choice == "1":
        login()
    elif choice == "2":
        signup()
    elif choice == "3":
        resetpass()
    elif choice == "4":
        logout()
    elif choice == "5":
        onestoreinput()
    else:
        print(f"{colors.RED} Invalid choice. Please try Again")
        time.sleep(1)
        auth()
        

# AUTHENTICATION TAB ---{
# Session mgmt
def save_session(access_token: str, refresh_token: str):
    session_data = {
        "access_token": access_token,
        "refresh_token": refresh_token
    }
    encrypted_session = encrypt_data(session_data)
    with open(SessionPath, 'w') as f:
        f.write(encrypted_session)
def load_session() -> dict | None:
    if not os.path.exists(SessionPath) or not key:
        return None
    try:
        with open(SessionPath, 'r') as f:
            encrypted_session = f.read().strip()
        if not encrypted_session:
            return None
        return decrypt_data(encrypted_session)
    except Exception:
        clear_session()
        return None
def clear_session():
    if os.path.exists(SessionPath):
        os.remove(SessionPath)
# Auto Authentication on boot
def auto_login() -> bool:
    session = load_session()
    if session:
        try:
            response = supabase.auth.set_session(
                access_token=session['access_token'],
                refresh_token=session['refresh_token']
            )
            if response.user:
                return True
        except Exception:
            clear_session()
    return False
# Login Logout
def logout():      
    supabase.auth.sign_out()
    clear_session()
    open(KeyPath, 'w').close() 
    print(f"{colors.GREEN} Thank you for using OneStore.\n You have now been logged out successfully.{colors.RESET}")
    time.sleep(2)
    onestoreinput()
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
    if response.user:
        enter= False
        ybc = supabase.table("Databayse").select("Yubiconnect").eq("useruid", response.user.id).execute()
        if ybc.data[0]['Yubiconnect'] == True:
            yubilogin(response)
            return
        while enter == False:
            
            clrso()
            onestorelogo()
            key1 = input (f"{colors.BOLD}{colors.CYAN}Enter Keyphrase 1: {colors.RESET}").lower()
            key2 = input (f"{colors.BOLD}{colors.CYAN}Enter Keyphrase 2: {colors.RESET}").lower()
            key3 = input (f"{colors.BOLD}{colors.CYAN}Enter Keyphrase 3: {colors.RESET}").lower()
            key4 = input (f"{colors.BOLD}{colors.CYAN}Enter Keyphrase 4: {colors.RESET}").lower()
            key5 = input (f"{colors.BOLD}{colors.CYAN}Enter Keyphrase 5: {colors.RESET}").lower()
            finalkey = key1 + key2 + key3 + key4 + key5
            uid = response.user.id
            respondevu = (
                supabase.table("Databayse")
                .select("salt", "hash")
                .eq("useruid", uid)
                .execute()
            )
            salt = respondevu.data[0]['salt']
            dbhash = respondevu.data[0]['hash']
            checkMaHash = hashlib.sha256((finalkey + salt).encode()).hexdigest()
            if checkMaHash == dbhash:
                enter = True
                global key
                key = finalkey
                open(KeyPath, 'w').write(finalkey)
                save_session(
                    response.session.access_token,
                    response.session.refresh_token
                )
            else:
                print(f"{colors.RED} Incorrect keyphrases. Please try again.{colors.RESET}")
                print(f"{colors.CYAN} Passwords cannot be decrypted without correct keyphrases.{colors.RESET}")
        print(f"{colors.GREEN}Login Successful! Welcome back to OneStore.{colors.RESET}")
        time.sleep(1)
        onestoreinput()
    else:
        print(f"{colors.RED}Login FAILED! Please check your email and password and try again.{colors.RESET}")
def authcheck():
    try:
        if supabase.auth.get_user():        
            return True
        else:
            return False
    except Exception:
        clear_session()
        return False
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
    elif len(password) < 6:
        print(f"{colors.RED}Password must be at least 6 characters long. Please try again.{colors.RESET}")
        time.sleep(1)
        signup()
    else:
        try:  
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
                global key
                key = finalkey
                passwordjson = encrypt_data({})
                response = (
                    supabase.table("Databayse")
                    .insert({"useruid": uid, "salt": salt, "hash": hashlib.sha256((finalkey + salt).encode()).hexdigest(), "passwords": passwordjson})
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
                            print(f"{colors.RED}Defaulting to KEYPHRASES @ OneStore{colors.RESET}")
                            print(f"{colors.RED}Please save these keyphrases in a safeplace{colors.RESET}")
                            time.sleep(0.5)
        except Exception as e:
            print(f"{colors.RED}Signup FAILED! An error occurred: {e}{colors.RESET}")
            print(f"{colors.RED}Please try again{colors.RESET}")
            signup()
# BEFORE PRODUCTION ADD THE RESET FUNCTIONALITY HERE  - next version, i aint doing ts now
# Dont be lazy smh
# REMINDER TO DO IT (hence the 3 line comments)
def resetpass():
    onestorelogo()
    print(f"{colors.BOLD}{colors.PURPLE}OneStore Authentication Master {colors.RESET}")
    print(f"{colors.BOLD}{colors.CYAN}OneStore password reset{colors.RESET}")
    email = input(f"{colors.BOLD}{colors.CYAN}Enter your OneStore email: {colors.RESET}")
#}

# Password storage tab ---{
# Pass retreival once pass storage actually works 😔
def passretrieve():
    if authcheck() == False:
        print(f"{colors.RED}You must be logged in to retrieve passwords from OneStore.{colors.RESET}")
        time.sleep(2)
        onestoreinput()
        return
    try:
        uid = supabase.auth.get_user().user.id
        response = supabase.table("Databayse").select("passwords").eq("useruid", uid).execute()
        encrypted_passwords = response.data[0]['passwords']
        if not encrypted_passwords:
            print(f"{colors.YELLOW}No passwords stored yet.{colors.RESET}")
            input("Press enter/return to return to OneStore CLI:")
            onestoreinput()
            return
        passwordsjson = decrypt_data(encrypted_passwords)
        print(passwordsjson)
        input("Press enter/return to return to OneStore CLI:")
        onestoreinput()
    except Exception as e:
        print(f"{colors.RED}ERROR: Cannot decrypt stored passwords.{colors.RESET}")
        print(f"{colors.YELLOW}Your keyphrases may not match the ones used to encrypt your passwords.{colors.RESET}")
        print(f"{colors.YELLOW}This can happen if password data was corrupted or stored incorrectly.{colors.RESET}")
        print(f"{colors.CYAN}You can use 'clear-passstore' to reset your password store if needed.{colors.RESET}")
        input("Press enter/return to return to OneStore CLI:")
        onestoreinput()  
def passstorefx(service, username, password):
    if authcheck() == True:
        uid = supabase.auth.get_user().user.id
        dbdata = supabase.table("Databayse").select("passwords").eq("useruid", uid).execute()
        encrypted_passwords = dbdata.data[0]['passwords']
        print(encrypted_passwords)
        passwordsjson = ''
        if encrypted_passwords:
            try:
                passwordsjson = decrypt_data(encrypted_passwords)
                passwordsjson = json.dumps(passwordsjson)
                print(passwordsjson)
                time.sleep(5)
            except Exception:
                print(f"{colors.RED}ERROR: Cannot decrypt stored passwords.{colors.RESET}")
                print(f"{colors.YELLOW}Your keyphrases don't match the ones used to encrypt your passwords.{colors.RESET}")
                print(f"{colors.YELLOW}Please logout and login again with the correct keyphrases.{colors.RESET}")
                input("Press enter/return to return to OneStore CLI:")
                onestoreinput()
                return
        passnum = 1
        for k in json.loads(passwordsjson).keys():
            if k.startswith("pass"):
                num = int(k[4:])
                if num >= passnum:
                    passnum = num + 1
        appendar = json.loads(passwordsjson)
        appendi = {f"pass{passnum}" : {"service": service, "username": username, "password": password}}
        appendar.update(appendi)
        encrypted_data = encrypt_data(appendar)
        uid = supabase.auth.get_user().user.id
        response =( supabase.table("Databayse").update({"passwords": encrypted_data}).eq("useruid", uid).execute())
        print(f"{colors.GREEN}Password saved successfully to OneStore!{colors.RESET}")
        input("Press enter/return to return to OneStore CLI:")
        onestoreinput()
    else:
        print(f"{colors.RED}You must be logged in to store passwords in OneStore.{colors.RESET}")
        time.sleep(2)
        onestoreinput()
def passstore():
    onestorelogo()
    print(f"{colors.CYAN}OneStore Password Services{colors.RESET}")
    service = input("Enter the URL/Service name: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    onestorelogo()
    print(f"{colors.CYAN}OneStore Password Services{colors.RESET}")
    print(f"{colors.YELLOW}{colors.BOLD}Password entry received. Processing...{colors.RESET}")
    passstorefx(service, username, password)
    time.sleep(1)
    onestorelogo()
    print(f"{colors.CYAN}OneStore Password Services{colors.RESET}")
    print(f"{colors.GREEN}Password saved successfully to OneStore!{colors.RESET}")
    input("Press enter/return to return to OneStore CLI:")
    onestoreinput()
def clearpassstore():
    onestorelogo()
    print(f"{colors.CYAN}OneStore Password Services{colors.RESET}")
    confirm = input(f"{colors.RED}Are you sure you want to clear all stored passwords? This action cannot be undone. (y/n): {colors.RESET}")
    if confirm.lower() == 'y':
        if authcheck() == True:
            uid = supabase.auth.get_user().user.id
            empty = encrypt_data({})
            supabase.table("Databayse").update({"passwords": empty}).eq("useruid", uid).execute()
            print(f"{colors.GREEN}All stored passwords have been cleared from OneStore.{colors.RESET}")
            input("Press enter/return to return to OneStore CLI:")
            onestoreinput()
        else:
            print(f"{colors.RED}You must be logged in to clear stored passwords in OneStore.{colors.RESET}")
            time.sleep(2)
            onestoreinput()
    else:
        print(f"{colors.YELLOW}Password clearing cancelled. Returning to OneStore CLI.{colors.RESET}")
        time.sleep(1)
        onestoreinput()
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
        passstorefx(url, username, password)
    else:
        print("Password not saved.")
        input("Press enter/return to return to OneStore CLI:")
        onestoreinput()
#}

# YubiConnect - a passwordless remote system ---{

def yubilogin(response):
    clrso()
    onestorelogo()
    print(f"{colors.BOLD}{colors.CYAN}OneStore Yubi Authenticate{colors.RESET}")
    print("Please touch your YubiKey to authenticate...")
    yubipass = getpass.getpass(f"{colors.BOLD}{colors.CYAN}Please touch your yubikey to authenticate... {colors.RESET}")
    uid = response.user.id
    respondevu = (
        supabase.table("Databayse")
        .select("salt", "hash")
        .eq("useruid", uid)
        .execute()
    )
    salt = respondevu.data[0]['salt']
    dbhash = respondevu.data[0]['hash']
    checkMaHash = hashlib.sha256((yubipass + salt).encode()).hexdigest()
    if checkMaHash == dbhash:
        global key
        key = yubipass
        open(KeyPath, 'w').write(yubipass)
        save_session(
            response.session.access_token,
            response.session.refresh_token
        )
        print(f"{colors.GREEN}YubiKey Authentication Successful! Welcome back to OneStore.{colors.RESET}")
        time.sleep(1)
        onestoreinput()
    else:
        print(f"{colors.RED}YubiKey Authentication FAILED! Please try again.{colors.RESET}")
        time.sleep(2)
        onestoreinput()
        

def yubisign():
    if authcheck() == False:
        print(f"{colors.RED}You must be logged in to use YubiConnect in OneStore.{colors.RESET}")
        time.sleep(2)
        onestoreinput()
        return
    elif authcheck() == True:
        clrso()
        onestorelogo()
        print(f"{colors.BOLD}{colors.CYAN}OneStore YubiConnect{colors.RESET}")
        print("Connect your yubikey to securely access your OneStore passwords.")
        input("Press enter/return once your YubiKey is connected:")
        clrso()
        onestorelogo()
        print(f"{colors.BOLD}{colors.CYAN}OneStore YubiConnect{colors.RESET}")
        print(f"{colors.RED}WARNING! Switching to yubiconnect will overwrite your keyphrases{colors.RESET}")
        print(f"{colors.RED}and you will no longer be able to login or retrieve passwords using them.{colors.RESET}")
        print(f"{colors.YELLOW}This action is irreversible, your passwords however will be retained.{colors.RESET}")
        confirm = input(f"{colors.YELLOW}Type 'confirm' to proceed with YubiConnect setup: {colors.RESET}")
        if confirm == "confirm":
            clrso()
            onestorelogo()
            print(f"{colors.BOLD}{colors.CYAN}OneStore YubiConnect{colors.RESET}")
            yubipass = getpass.getpass(f"{colors.BOLD}{colors.CYAN}Please touch your yubikey to authenticate... {colors.RESET}")
            uid = supabase.auth.get_user().user.id
            respondevu = (
                supabase.table("Databayse")
                .select("salt")
                .eq("useruid", uid)
                .execute()
            )
            # Decrypt them passwords 🙂‍↕
            if authcheck() == False:
                print(f"{colors.RED}You must be logged in to retrieve passwords from OneStore.{colors.RESET}")
                time.sleep(2)
                onestoreinput()
                return
            try:
                    uid = supabase.auth.get_user().user.id
                    response = supabase.table("Databayse").select("passwords").eq("useruid", uid).execute()
                    encrypted_passwords = response.data[0]['passwords']
                    if not encrypted_passwords:
                        print(f"{colors.YELLOW}No passwords stored yet.{colors.RESET}")
                        input("Press enter/return to return to OneStore CLI:")
                        onestoreinput()
                        return
                    passwordsjson = decrypt_data(encrypted_passwords)
                    # Recrypt em 
                    open(KeyPath, 'w').write(yubipass)
                    recrypt = encrypt_data(passwordsjson)
                    supabase.table("Databayse").update({"passwords": recrypt}).eq("useruid", uid).execute()
                    salt = respondevu.data[0]['salt']
                    supabase.table("Databayse").update({"salt": salt, "hash": hashlib.sha256((yubipass + salt).encode()).hexdigest(),"Yubiconnect":"true"}).eq("useruid", uid).execute()
                    print(f"{colors.GREEN}YubiConnect setup complete! You can now login using your YubiKey.{colors.RESET}")
                    input("Press enter/return to return to OneStore CLI:")
                    onestoreinput()  
                    return


            except Exception as e:
                    print(f"{colors.RED}ERROR: Cannot decrypt stored passwords.{colors.RESET}")
                    print(f"{colors.YELLOW}Your keyphrases may not match the ones used to encrypt your passwords.{colors.RESET}")
                    print(f"{colors.CYAN}You can use 'clear-passstore' to reset your password store if needed.{colors.RESET}")
                    input("Press enter/return to return to OneStore CLI:")
                    onestoreinput()  
                    return


#}
## ON LOAD
# Check for keyphrases file and path/ or jst create
if not os.path.exists(OneStorePath):
    KeyExists = False
    os.makedirs(OneStorePath)
    open(KeyPath, 'w').close()
else:
    KeyExists = True
    with open(KeyPath, "r") as file:
        key = file.read().strip()
if KeyExists and key:
    if auto_login():
        onestorelogo()
        print(f"{colors.GREEN}Welcome back! Auto-logged in using saved session.{colors.RESET}")
        time.sleep(1)

yubisign()