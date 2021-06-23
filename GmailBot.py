from selenium import webdriver
import keyboard
from time import sleep


class Driver:
    def __init__(self,website):
        self.website=website
    def access(self):
        Chrome=webdriver.Chrome("C:/Users/Manso/Documents/GitHub/GmailAccCreator/chromedriver.exe")
        Chrome.get(self.website)
        print("press q to exit")
        FirstName=Chrome.find_elements_by_xpath("input[@name='firstName']")
        LastName=Chrome.find_elements_by_xpath("input[@name='lastName']")
        
        sleep(5)
        while True:
            if keyboard.is_pressed('q'):
                Chrome.close()



if __name__=="__main__":
    Driver("https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=SignUp").access()

