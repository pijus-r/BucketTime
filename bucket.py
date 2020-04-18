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

done = False
warnings.filterwarnings('ignore')


ascii_banner = pyfiglet.figlet_format("CHICKEN\nTIME")
print(ascii_banner)


options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
driver.set_window_size(1124, 650)
driver.get("https://wolt.com/lt/ltu/vilnius/restaurant/kfc-ozas")
print('Checking availability')
try:
    time.sleep(6)
    nope = driver.find_element_by_xpath("//span[.='Gerai']")
    if nope.text == "Gerai":
       print("KFC is " + Fore.RED + "CLOSED\n")
    else:
        def animate():
            for c in itertools.cycle(['|', '/', '-']):
                if done:
                    break
                sys.stdout.write(Fore.WHITE + '\rPreparing the bucket ' + c)
                sys.stdout.flush()
                time.sleep(0.1)

        t = threading.Thread(target=animate)
        t.start()
        login = driver.find_element_by_xpath("//span[.='Prisijungti']").click()
        time.sleep(5)
        withemail = driver.find_element_by_class_name("initial_authentication__continue-email___13Kbr").click()
        time.sleep(5)
        username = driver.find_element_by_class_name("InputField__input___2Ed_-")
        print(Fore.WHITE + "WOLT credentials")
        user = input(Fore.WHITE + "Email: ")
        username.send_keys(user) #USERNAME
        go = driver.find_element_by_xpath("//button[@class='forms__form-button___2W4Ax forms__main___1_W0h']").click()
        time.sleep(5)
        password = driver.find_element_by_class_name("InputField__input___2Ed_-")
        passw = getpass(Fore.WHITE + "Password: ")
        password.send_keys(passw) #PASSWORD
        goTwo = driver.find_element_by_xpath("//button[@class='forms__form-button___2W4Ax forms__main___1_W0h']/span[.='Prisijungti']").click()
        time.sleep(5)
        element = driver.find_element_by_xpath("//p[.='1×Traškių lazdelių kibirėlis keturiems, 15 vnt.']").click()
        time.sleep(5)
        this = driver.find_element_by_class_name("MenuItem__plusIcon___344Vh MenuItem__show___2i0Ae").click()
        time.sleep(5)
        checkout = driver.find_element_by_xpath("//button[@class='CheckoutButton__orderButton___lx8tN']/span[@class='CheckoutButton__text___3EL_D']/span[.='Apmokėti']").click()
        time.sleep(5)
        checkfirst = driver.find_element_by_class_name("DeliveryAddressHeader__hideButton___2CypX")
        checkfirst.click()
        time.sleep(3)
        ordernGo = driver.find_element_by_xpath("//span[@class='SendOrderButton__text___3r7zY']/span[.='Spauskite užsisakyti']")
        #Uncomment to make an actual order
        #orderGo.click()
        done = True
        print(Fore.WHITE + "\n\nDelivering")
        driver.quit()
except NoSuchElementException:
     pass
