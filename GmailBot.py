from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import keyboard
from time import sleep


class Driver:
    def __init__(self,website):
        self.website=website
    def access(self):
        Chrome=webdriver.Chrome("C:/Users/Manso/Documents/GitHub/MessagingBot/chromedriver")
        Chrome.get(self.website)
        print("press q to exit")
        sleep(5)
        FirstName=Chrome.find_element_by_css_selector("input[name='firstName']")
        LastName=Chrome.find_element_by_css_selector("input[name='lastName']")
        Email=Chrome.find_element_by_css_selector("input[name='Username']")
        Password=Chrome.find_element_by_css_selector("input[name='Passwd']")
        Confirm=Chrome.find_element_by_css_selector("input[name='ConfirmPasswd']")
        sleep(2)
        FirstName.send_keys("hamid")
        LastName.send_keys("behraoui\t")
        email="hamidbehraoui17"
        Email.send_keys(email)
        Password.send_keys("hliwa123")
        Confirm.send_keys("hliwa123")

        Create=Chrome.find_element_by_xpath("//button[@type='button']")
        Create.click()

        
        sleep(50)



if __name__=="__main__":
    Driver("https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=SignUp").access()

