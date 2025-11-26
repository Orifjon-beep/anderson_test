from pages.homepage import HomePage


    
def test_universal_management(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.sumbit()
    homepage.button()
    homepage.check_title_is('Universal management')
    
def test_clien_contracts(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.sumbit()
    homepage.button_2()
    homepage.check_title_is('Client & Contracts')

def test_contracts(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.sumbit()
    homepage.button_3()
    homepage.check_title_is('Contracts')

def test_cases(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.sumbit()
    homepage.button_4()
    homepage.check_title_is('Cases')

def test_tasks(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.sumbit()
    homepage.button_5()
    homepage.check_title_is('Tasks')

def test_calendar(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.sumbit()
    homepage.check_title_is('Calendar')

def test_bills(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.sumbit()
    homepage.button_7()
    homepage.check_title_is('Bills')

def test_payments(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.sumbit()
    homepage.button_8()
    homepage.check_title_is('Payments')

def test_KPI(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.sumbit()
    homepage.button_9()
    homepage.check_title_is('KPI')

# def test_users(browser):
#     homepage = HomePage(browser)
#     homepage.open()
#     homepage.sumbit()
#     homepage.button_10()
#     homepage.check_title_is('Users')

# def test_reviews(browser):
#     homepage = HomePage(browser)
#     homepage.open()
#     homepage.sumbit()
#     homepage.button_11()
#     homepage.check_title_is('Reviews')

# def test_complaints(browser):
#     homepage = HomePage(browser)
#     homepage.open()
#     homepage.sumbit()
#     homepage.button_12()
#     homepage.check_title_is('Complaints')

# def test_reports(browser):
#     homepage = HomePage(browser)
#     homepage.open()
#     homepage.sumbit()
#     homepage.button_13()
#     homepage.check_title_is('Reports')
