import os

os.system("cls && title SteinsFuscator")

intro = """
                                                 \033[4mDiscord : iwa;steins#2808\033[0m
                            GitHub : \033[1;36;40mhttps://github.com/9wi/\033[0m x \033[1;36;40mhttps://github.com/cr0cr0\033[0m
                                 _____ _       _             \033[1;31;40m_____                   _\033[0m
                                /  ___| |     (_)           \033[1;31;40m|  ___|                 | |\033[0m
                                \ `--.| |_ ___ _ _ __  ___  \033[1;31;40m| |_ _   _ ___  ___ __ _| |_ ___  _ __\033[0m
                                 `--. \ __/ _ \ | '_ \/ __| \033[1;31;40m|  _| | | / __|/ __/ _` | __/ _ \| '__|\033[0m
                                /\__/ / ||  __/ | | | \__ \ \033[1;31;40m| | | |_| \__ \ (_| (_| | || (_) | |\033[0m
                                \____/ \__\___|_|_| |_|___/ \033[1;31;40m|_|  \__,_|___/\___\__,_|\__\___/|_|\033[0m
"""

print(intro)

def MakeSC():
    c = input("Encode: ")
    sc = "\\x" + "\\x".join("{0:x}".format(ord(c)) for c in c)
    shellcode =f'"{sc}"'
    return shellcode

x = MakeSC()
print("\n")
print(x)
