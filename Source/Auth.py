try:
    import subprocess
    import requests
    import hashlib
    import time
    from os import system

    system("title " + "Soud Was Here - @_agf - Soud#0737")

except Exception as m:
    print(m)
    input("Press Any Key To Exit...\n")
    exit()
print("""
    ░██████╗░█████╗░██╗░░░██╗██████╗░░█████╗░░█████╗░  ██╗░░██╗███████╗██████╗░███████╗
    ██╔════╝██╔══██╗██║░░░██║██╔══██╗██╔═══╝░██╔══██╗  ██║░░██║██╔════╝██╔══██╗██╔════╝
    ╚█████╗░██║░░██║██║░░░██║██║░░██║██████╗░╚██████║  ███████║█████╗░░██████╔╝█████╗░░
    ░╚═══██╗██║░░██║██║░░░██║██║░░██║██╔══██╗░╚═══██║  ██╔══██║██╔══╝░░██╔══██╗██╔══╝░░
    ██████╔╝╚█████╔╝╚██████╔╝██████╔╝╚█████╔╝░█████╔╝  ██║░░██║███████╗██║░░██║███████╗
    ╚═════╝░░╚════╝░░╚═════╝░╚═════╝░░╚════╝░░╚════╝░  ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝
                            Credit @_agf - Soud#0737
                            """)

print("This is simple Auth tool by Soud\n")
# HWID Here
qw = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
hwidd = hashlib.md5(qw.encode()).hexdigest()
hwid = hwidd.upper()
print(f"This is Your ID {qw}\nPlease give it Dev to Register")
# User Here
us = str(input("Please Enter Your User: "))
uss = hashlib.md5(us.encode()).hexdigest()
user = uss.upper()

# Pass Here
ps = str(input("Please Enter Your Password: "))
pss = hashlib.md5(ps.encode()).hexdigest()
password = pss.upper()

# HWID|USER|PASS in Pastebin/Database
try:
    req = requests.get("https://pastebin.com/raw/n2BH820j")
    if f"{hwid}|{user}|{password}" in req:
        print("[+] Logged in Successfully\nWelcome", us)
        pass
    else:
        print("[!] Login Failed\nPlease Contact The Dev For More Info")
        time.sleep(4)
        exit()
except Exception as m:
    print("[Error] Failed To Connect To Database\n")
    print(m)
    time.sleep(4)
    exit()
