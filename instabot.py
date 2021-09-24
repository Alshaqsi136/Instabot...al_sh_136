from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait 
browser =  webdriver.Chrome()
# al_sh_136///:
browser.get("https://www.instagram.com")  

time.sleep (2)

username_input = browser.find_element_by_css_selector("input[name='username']").send_keys("هنا كتب حسابك")

password_input = browser.find_element_by_css_selector("input[name='password']").send_keys("هنا كتب الرمز")

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

time.sleep(3)
notNowButton = WebDriverWait(browser, 15).until(
    lambda d: d.find_element_by_xpath('//button[text()="Not Now"]'))
notNowButton.click()

time.sleep(3)
notNowButton = WebDriverWait(browser, 15).until(
    lambda d: d.find_element_by_xpath('//button[text()="Not Now"]'))
notNowButton.click()

time.sleep(1)

for i in range (10):
    browser.find_element_by_xpath('//*[@id="react-root"]/div/div/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[1]/div[3]/button/div').click()
    browser.find_element_by_xpath('//*[@id="react-root"]/div/div/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[2]/div[3]/button/div').click()
    browser.find_element_by_xpath('//*[@id="react-root"]/div/div/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[3]/div[3]/button/div').click()
    browser.find_element_by_xpath('//*[@id="react-root"]/div/div/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[4]/div[3]/button/div').click()
    browser.find_element_by_xpath('//*[@id="react-root"]/div/div/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[5]/div[3]/button/div').click()
    browser.refresh()
    time.sleep(3)