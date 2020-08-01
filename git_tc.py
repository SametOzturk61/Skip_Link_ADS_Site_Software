import random
import os
import string

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import colorama
from colorama import Fore, Back, Style
colorama.init()

print(Fore.GREEN)
print("Özel Link Geçme Botu")
print("by SametOzturk :)")
print(Fore.WHITE)
input("Devam etmek için ENTER")
clear = lambda: os.system('cls')
clear()
print(Fore.YELLOW)
link = input("Link (Https/http etiketiyle birlikte): ")

options = webdriver.FirefoxOptions()
options.set_preference("dom.push.enabled", False)
options.set_preference("browser.privatebrowsing.autostart", True)
options.set_preference("network.proxy.type", 1)
options.set_preference("network.proxy.socks", "127.0.0.1")
options.set_preference("network.proxy.socks_port", 9150)
options.set_preference("network.proxy.socks_remote_dns", True)
options.set_preference("network.dns.disablePrefetch", True)
options.set_preference("network.cookie.cookieBehavior", 1)
options.set_preference("network.cookie.lifetimePolicy", 2)
options.set_preference("network.disable.ipc.security", True)
options.set_preference("media.peerconnection.enabled", False)

clear = lambda: os.system('cls')
clear()

useragent = ""

def RandomUserAgent():
    no = random.randint(0,20)

    if no == 1:
        useragent = "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36"
    if no == 2:
        useragent = "Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36"
    if no == 3:
        useragent = "Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"
    if no == 4:
        useragent = "Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36"
    if no == 5:
        useragent = "Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36"
    if no == 6:
        useragent = "Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36"
    if no == 7:
        useragent = "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36"
    if no == 8:
        useragent = "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1"
    if no == 9:
        useragent = "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1"
    if no == 10:
        useragent = "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/13.2b11866 Mobile/16A366 Safari/605.1.15"
    if no == 11:
        useragent = "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
    if no == 12:
        useragent = "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
    if no == 13:
        useragent = "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A5370a Safari/604.1"
    if no == 14:
        useragent = "Mozilla/5.0 (iPhone9,3; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1"
    if no == 15:
        useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
    if no == 16:
        useragent = "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36"
    if no == 17:
        useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"
    if no == 18:
        useragent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36"
    if no == 19:
        useragent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"
    if no == 20:
        useragent = "Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36"

def LinkGec():

    tiklama = 0

    while True:

        RandomUserAgent() 

        options.set_preference("general.useragent.override", f"{useragent}")

        driver = webdriver.Firefox(executable_path="geckodriver.exe", options=options)
        
        driver.minimize_window()

        driver.get(link)

        sleep(9)

        driver.find_element_by_id("sayac").click()

        sleep(1)

        driver.switch_to.window(driver.window_handles[0])

        sleep(1)

        driver.find_element_by_id("sayac").click()

        sleep(1)
        
        tiklama += 1

        print(Fore.CYAN)
        print("----------------------------------")
        print("1 tıklama elde edildi !")
        print(f"Toplam tıklama: {tiklama}")
        print("----------------------------------")

        driver.quit()

LinkGec()