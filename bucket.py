from selenium import webdriver
from colorama import Fore, Back, Style
import pyfiglet
import time
import warnings
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import itertools
import threading
import time
import sys
from getpass import getpass

warnings.filterwarnings('ignore')


ascii_banner = pyfiglet.figlet_format("CHICKEN\nTIME\n")
print(ascii_banner)


options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
driver.set_window_size(1124, 850)

try:
    driver.get("https://wolt.com/lt/ltu/vilnius/restaurant/kfc-ozas")
    print('Checking availability')
    time.sleep(6)
    nope = driver.find_element_by_xpath("//span[.='Gerai']")
    if  nope.text == "Gerai":
        print("KFC is " + Fore.RED + "CLOSED\n")
        driver.quit()
except NoSuchElementException:
    login = driver.find_element_by_xpath("//span[.='Prisijungti']").click()
    time.sleep(2)
    withemail = driver.find_element_by_class_name("initial_authentication__continue-email___13Kbr").click()
    time.sleep(3)
    username = driver.find_element_by_class_name("InputField__input___2Ed_-")
    print(Fore.WHITE + "WOLT credentials")
    user = input(Fore.WHITE + "Email: ")
    username.send_keys(user) #USERNAME
    go = driver.find_element_by_xpath("//button[@class='forms__form-button___2W4Ax forms__main___1_W0h']").click()
    time.sleep(3)
    password = driver.find_element_by_class_name("InputField__input___2Ed_-")
    passw = getpass(Fore.WHITE + "Password: ")
    password.send_keys(passw) #PASSWORD
    goTwo = driver.find_element_by_xpath("//button[@class='forms__form-button___2W4Ax forms__main___1_W0h']/span[.='Prisijungti']").click()
    time.sleep(3)
    element = driver.find_element_by_xpath("//p[.='1×Traškių lazdelių kibirėlis keturiems, 15 vnt.']").click()
    time.sleep(3)
    this = driver.find_element_by_class_name("AddToOrderButton__addToOrderButton___295uO").click()
    time.sleep(3)
    checkout = driver.find_element_by_xpath("//button[@class='CheckoutButton__orderButton___lx8tN']/span[@class='CheckoutButton__text___3EL_D']/span[.='Apmokėti']").click()
    time.sleep(3)
    checkfirst = driver.find_element_by_class_name("DeliveryAddressHeader__hideButton___2CypX")
    checkfirst.click()
    time.sleep(3)
    ordernGo = driver.find_element_by_xpath("//span[@class='SendOrderButton__text___3r7zY']/span[.='Spauskite užsisakyti']")
    #Uncomment to make an actual order
    #ordernGo.click()
    print(Fore.GREEN + "\n\nDelivering")
    driver.quit()
