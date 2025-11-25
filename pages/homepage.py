from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, browser):
        self.browser = browser

    
    def open(self):
        self.browser.get('https://andersenrelease.netlify.app/partner/tasks')

    def sumbit(self):
        open_1 = self.browser.find_element(By.ID, 'number')
        open_1.send_keys('909090909')
        open_2 = self.browser.find_element(By.ID, 'password')
        open_2.send_keys('1212qwqw')
        open_2.submit()

    
    def check_title_is(self, title):
        page_title = self.browser.find_element(By.CSS_SELECTOR, 'h1')
        assert page_title.text == title

    
    def button(self):
        button = self.browser.find_element(By.CLASS_NAME, 'lucide-layout-dashboard')
        button.click()
        self.browser.implicitly_wait(5)


    def button_2(self):
        button_2 = self.browser.find_element(By.CLASS_NAME, 'lucide-contact-round')
        button_2.click()
        self.browser.implicitly_wait(5)

    
    def button_3(self):
        button_3 = self.browser.find_element(By.CSS_SELECTOR, 'svg[class="lucide lucide-paperclip w-5 h-5"]')
        button_3.click()
        self.browser.implicitly_wait(5)

    def button_4(self):
        button_4 = self.browser.find_element(By.CSS_SELECTOR, 'svg[class="lucide lucide-briefcase w-5 h-5"]')
        button_4.click()
        self.browser.implicitly_wait(5)


    def button_5(self):
        button_5 = self.browser.find_element(By.CSS_SELECTOR, 'svg[class="lucide lucide-list w-5 h-5"]')
        button_5.click()
        self.browser.implicitly_wait(5)


    def button_7(self):
        button_7 = self.browser.find_element(By.CSS_SELECTOR, 'svg[class="lucide lucide-receipt w-5 h-5"]')
        button_7.click()
        self.browser.implicitly_wait(5)


    def button_8(self):
        button_8 = self.browser.find_element(By.CSS_SELECTOR, 'svg[class="lucide lucide-dollar-sign w-5 h-5"]')
        button_8.click()
        self.browser.implicitly_wait(5)

    def button_9(self):
        button_9 = self.browser.find_element(By.CSS_SELECTOR, 'svg[class="lucide lucide-chart-line w-5 h-5"]')
        button_9.click()
        self.browser.implicitly_wait(5)


    def button_10(self):
        button_10 = self.browser.find_element(By.CSS_SELECTOR, 'svg[class="lucide lucide-users w-5 h-5"]')
        button_10.click()
        self.browser.implicitly_wait(5)


    def button_11(self):
        button_11 = self.browser.find_element(By.CSS_SELECTOR, 'svg[class="lucide lucide-user-round-x w-5 h-5"]')
        button_11.click()
        self.browser.implicitly_wait(5)


    def button_12(self):
        button_12 = self.browser.find_element(By.CSS_SELECTOR, 'svg[class="lucide lucide-message-circle w-5 h-5"]')
        button_12.click()
        self.browser.implicitly_wait(5)

    
    def button_13(self):
        button_13 = self.browser.find_element(By.CSS_SELECTOR, 'svg[class="lucide lucide-chart-no-axes-column-increasing w-5 h-5"]')
        button_13.click()
        self.browser.implicitly_wait(5)
   