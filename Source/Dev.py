try:
    import subprocess
    import hashlib
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
qw = str(input("Please Customer ID: "))
hwidd = hashlib.md5(qw.encode()).hexdigest()
hwid = hwidd.upper()

# User Here
us = str(input("Please Customer User: "))
uss = hashlib.md5(us.encode()).hexdigest()
user = uss.upper()

# Pass Here
ps = str(input("Please Customer Password: "))
pss = hashlib.md5(ps.encode()).hexdigest()
password = pss.upper()

print(f"Add This to your Pastebin\n{hwid}|{user}|{password}\n Bye <3")
