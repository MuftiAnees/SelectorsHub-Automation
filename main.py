import os
# import org.openqa.selenium.By;
# import org.openqa.selenium.WebDriver;
# import org.openqa.selenium.WebElement;
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
PATH = Service("C:\\Users\\mufti\\OneDrive\\Documents\\Github\\Selenium\\chromedriver.exe")
driver = webdriver.Chrome(service=PATH, options=chrome_options)
driver.maximize_window()
driver.get("https://selectorshub.com/xpath-practice-page/")
sleep(2)
search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "userId")))
search.send_keys("muftianees7@gmail.com")
search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
search.send_keys("EnterPasswordHere")
search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#content > div > div.elementor.elementor-1097 > section.elementor-section.elementor-top-section.elementor-element.elementor-element-5dce1dc.practice-link.elementor-section-boxed.elementor-section-height-default.elementor-section-height-default > div > div.elementor-column.elementor-col-50.elementor-top-column.elementor-element.elementor-element-0423319 > div > div.elementor-element.elementor-element-459c920.elementor-widget.elementor-widget-html > div > form > div > div:nth-child(11) > div > div > div > input:nth-child(3)")))
search.send_keys("Care")
search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#content > div > div.elementor.elementor-1097 > section.elementor-section.elementor-top-section.elementor-element.elementor-element-5dce1dc.practice-link.elementor-section-boxed.elementor-section-height-default.elementor-section-height-default > div > div.elementor-column.elementor-col-50.elementor-top-column.elementor-element.elementor-element-0423319 > div > div.elementor-element.elementor-element-459c920.elementor-widget.elementor-widget-html > div > form > div > div:nth-child(11) > div > div > div > input:nth-child(6)")))
search.send_keys("12345678909")
search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'inp_val')))
search.send_keys('Mahnoor')
search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'datepicker')))
search.send_keys(Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE, '2/2/2023')
search=driver.find_element(By.ID, "ohrmList_chkSelectRecord_25")
search.click()
search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="kils"]')))
search.click()


print("\n")
print("TEST COMPLETED")
print("\n")
sleep(2)    