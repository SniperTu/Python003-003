from selenium import webdriver
import time

def crawel():
    browser = webdriver.Chrome()
    browser.get('https://shimo.im/')
    login = browser.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]/button')
    time.sleep(5)
    if (login):
        login.click()
    else:
        print('已登录')
        browser.close()
        
    mobileOrEmail = browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input')
    password = browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input')
    mobileOrEmail.send_keys('snippers@163.com')
    password.send_keys('Gxy221111')
    loginButton = browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button')

    loginButton.click()
    time.sleep(5)
    browser.close()

crawel()


