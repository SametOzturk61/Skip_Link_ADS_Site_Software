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
options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0")

clear = lambda: os.system('cls')
clear()

def ButtonFix():

    print("Geçme butonuna basılamadı, tarayıcı yeniden başlatılıyor...")

    LinkGec()

def Cloudflare():

    print("Cloudflare çıktı, browser yeniden başlatılıyor...")

    LinkGec()

def LinkGec():

    tiklama = 0

    while True:

        driver = webdriver.Firefox(executable_path="geckodriver.exe", options=options)

        driver.get("https://google.com")

        driver.get(link)

        sleep(1)

        driver.refresh()

        if "Cloudflare" in driver.title:

            sleep(8)

            driver.refresh

            if "Cloudflare" in driver.title:
                
                driver.quit()

                Cloudflare()

        driver.find_element_by_id("robot_button").click()

        sleep(14)
        
        SkipButton = driver.find_element_by_id("skip_button")

        if(SkipButton.is_displayed()):

            driver.find_element_by_id("skip_button").click()

            sleep(1)

            driver.switch_to.window(driver.window_handles[0])

            sleep(1)

            driver.find_element_by_id("skip_button").click()
   
            sleep(1)

            driver.switch_to.window(driver.window_handles[0])
   
            sleep(2)

            tiklama += 1

            print(Fore.CYAN)
            print("----------------------------------")
            print("1 tıklama elde edildi !")
            print(f"Toplam tıklama: {tiklama}")
            print("----------------------------------")

            driver.quit()

        else:

            driver.quit()

            ButtonFix()

LinkGec()