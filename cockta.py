from selenium import webdriver
from time import sleep
import random
import string

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

PATH=""
class CocktaBot:
    def __init__(self, name, surname, email, phone):
        letters = string.ascii_uppercase
        # result_str = ''.join((random.choice(string.ascii_uppercase) for i in range(4)))
        # result_str += ''.join((random.choice(string.digits) for i in range(3)))
        najdlo = True

        options = Options()
        options.headless = True

        # poberi geckodriver-v0.27.0-win64 in spremeni ki je pot
        driver = webdriver.Firefox(options=options, executable_path=PATH+"geckodriver.exe")

        while True:
            result_str = ''.join(random.choice(letters) for _ in range(7))
            driver.get("https://cockta.eu/tvoja_nagrada_tvoja_stvar_vnos_kode/#")
            sleep(1.5)
            try:
                driver.find_element_by_xpath("/html/body/div[6]/div[1]/div/a[2]").click()
            except NoSuchElementException:
                pass
            driver.find_element_by_xpath("//input[@name=\"field_147\"]").send_keys(Keys.CONTROL + 'a')
            driver.find_element_by_xpath("//input[@name=\"field_147\"]").send_keys(result_str)
            if najdlo:
                driver.find_element_by_xpath("//input[@name=\"field_148\"]").send_keys(name)
                driver.find_element_by_xpath("//input[@name=\"field_149\"]").send_keys(surname)
                driver.find_element_by_xpath("//input[@name=\"field_146\"]").send_keys(email)
                driver.find_element_by_xpath("//input[@name=\"field_150\"]").send_keys(phone)
                driver.find_element_by_xpath(".//*[@id=\"generic_form_24_field_151_16\"]").click()
                driver.find_element_by_xpath(".//*[@id=\"generic_form_24_field_152_17\"]").click()
                najdlo = False
            driver.find_element_by_xpath("//*[@id=\"generic_form_24_save\"]").click()

            try:
                sleep(0.4)
                driver.find_element_by_xpath("/html/body/div[3]/div[1]/main/div[2]/div/div/div/p/strong")
            except NoSuchElementException:
                print(result_str)
                # to je ce ces kam ti daje prave resitve
                file = open(PATH+"praveKode.txt", "a")
                file.write(result_str + "\n")
                file.close()
                # to je screenshot od strani pole od useh pravih kod ku najde in ti shrane ku sliku
                S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
                driver.set_window_size(S('Width'), S('Height'))  # May need manual adjustment
                driver.find_element_by_tag_name('body').screenshot(PATH + result_str + ".png")
                driver.set_window_size(1366, 768)
                najdlo = True

            # sleep(5)
            driver.delete_all_cookies()
            if najdlo:
                driver.quit()
                break

while True:
    CocktaBot("Ime", "Priimek", "@gmail.com", "000111222")
