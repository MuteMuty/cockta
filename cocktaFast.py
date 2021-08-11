from selenium import webdriver
from time import sleep
import random
import string

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys


class CocktaBot:
    def __init__(self, name, surname, email, phone):
        letters = string.ascii_uppercase

        options = Options()
        options.headless = True
        options.set_preference('javascript.enabled', False)

        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.cache.disk.enable', False)
        profile.set_preference('browser.cache.memory.enable', False)
        profile.set_preference('browser.cache.offline.enable', False)
        profile.set_preference("network.cookie.cookieBehaviour", 2)
        profile.update_preferences()

        # poberi geckodriver-v0.27.0-win64 in spremeni ki je pot
        driver = webdriver.Firefox(firefox_profile=profile, options=options, executable_path=r'C:\Users\Erik\Downloads\geckodriver-v0.27.0-win64\geckodriver.exe')

        driver.get("https://cockta.eu/tvoja_nagrada_tvoja_stvar_vnos_kode/#")

        while True:
            result_str = ''.join(random.choice(letters) for _ in range(7))
            try:
                driver.find_element_by_xpath("//input[@name=\"field_147\"]").send_keys(Keys.CONTROL + 'a')
                driver.find_element_by_xpath("//input[@name=\"field_147\"]").send_keys(result_str)
                driver.find_element_by_xpath("//input[@name=\"field_148\"]").send_keys(Keys.CONTROL + 'a')
                driver.find_element_by_xpath("//input[@name=\"field_148\"]").send_keys(name)
                driver.find_element_by_xpath("//input[@name=\"field_149\"]").send_keys(Keys.CONTROL + 'a')
                driver.find_element_by_xpath("//input[@name=\"field_149\"]").send_keys(surname)
                driver.find_element_by_xpath("//input[@name=\"field_146\"]").send_keys(Keys.CONTROL + 'a')
                driver.find_element_by_xpath("//input[@name=\"field_146\"]").send_keys(email)
                driver.find_element_by_xpath("//input[@name=\"field_150\"]").send_keys(Keys.CONTROL + 'a')
                driver.find_element_by_xpath("//input[@name=\"field_150\"]").send_keys(phone)

                if not driver.find_element_by_xpath(".//*[@id=\"generic_form_24_field_151_16\"]").is_selected():
                    driver.find_element_by_xpath(".//*[@id=\"generic_form_24_field_151_16\"]").click()
                    driver.find_element_by_xpath(".//*[@id=\"generic_form_24_field_152_17\"]").click()

                driver.find_element_by_xpath("//*[@id=\"generic_form_24_save\"]").click()
            except Exception as e:
                print(e)
                break
            driver.delete_all_cookies()
            driver.get("https://cockta.eu/tvoja_nagrada_tvoja_stvar_vnos_kode/#")
            # sleep(3)
        driver.close()


while True:
    CocktaBot("x", "x", "x", "x")
