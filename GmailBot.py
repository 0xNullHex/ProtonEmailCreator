from selenium import webdriver
from time import sleep
import random
import pathlib
import json
import platform

class Driver:
    def __init__(self,website):
        self.website=website
    def access(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--log-level=3") # Make selenium silent
        # Detach chrome instance from chrome driver
        options.add_experimental_option("detach", True)
        # Detect OS for correct path syntax
        if platform.system() == "Windows":
            driver_filename = "\\chromedriver"
        else:
            driver_filename = "/chromedriver"
        Chrome=webdriver.Chrome(str(pathlib.Path(__file__).parent.resolve()) + driver_filename, options=options)
        Chrome.get(self.website)
        sleep(5)
        # Generating credentials
        credentials = Driver.generate_credentials()
        # Fill isolated username field in iframe
        form_frame = Chrome.find_element_by_css_selector("iframe")
        Chrome.switch_to.frame(form_frame)
        Username=Chrome.find_element_by_css_selector("input#username")
        Username.send_keys(credentials["Email"])
        Chrome.switch_to.default_content()
        # Setup other fields
        Password=Chrome.find_element_by_css_selector("input#password")
        Confirm=Chrome.find_element_by_css_selector("input#repeat-password")
        sleep(2)
        # Filling fields with credentials
        Password.send_keys(credentials["Password"])
        Confirm.send_keys(credentials["Password"])
        # Add generated data to database
        credentials["Email"] += "@protonmail.com"
        Driver.database_edit(credentials)
        # Print Email and Password on terminal
        print("Email: {}\nPassword: {}".format(credentials["Email"], credentials["Password"]))
        # Confirm operation to next page
        Create=Chrome.find_element_by_xpath("//button[@type='submit']")
        Create.click()

        # Skip recovery options
        sleep(3)
        Skip=Chrome.find_element_by_css_selector("form[name='recoveryForm'] > button[type='button']")
        Skip.click()

        # Confirm skip from modal
        sleep(3)
        ConfirmSkip=Chrome.find_element_by_css_selector("form.modal-content > footer > button[type='button']")
        ConfirmSkip.click()

        # Select free plan (ofc)
        sleep(3)
        select_free_plan = Chrome.find_element_by_css_selector("button[aria-describedby='desc_Free'][type='button']")
        select_free_plan.click()
        
        # Ask the user to enter the Captcha manually
        print("Am stuck stepbro ! Can you pass the capcha for me UwU ?")


    def database_edit(new_creds):
        try:
            db = open("DataBase.json", "r")
            db_json = json.loads(db.read())
            db.close()
        except FileNotFoundError or FileExistsError:
            db_json = []
        db = open("DataBase.json", "w")
        db_json.append(new_creds)
        db.write(json.dumps(db_json))
        db.close()

    def generate_credentials():
        creds = {
            "Email": Driver.generator(),
            "Password": Driver.generator()
        }
        return creds

    def generator():
        Characters ="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        holder=""
        while len(holder) < 10:
            holder+=random.choice(Characters)
        return holder

    def generator_bis():
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        data = [letters, letters.lower(), "0123456789"]
        holder = ""
        while len(holder) < 10:
            index = random.randint(0,2)
            holder += data[index][random.randint(0, len(data[index]) - 1)]
        return holder

if __name__=="__main__":
    Driver("https://account.protonmail.com/signup?language=en").access()
    

