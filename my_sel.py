#Importing Necessary Libraries
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
import time
import logging 

#logging.basicConfig(level=logging.DEBUG)

def buy_stock(driver: uc.Chrome,order):
    search_div = driver.find_element(By.CSS_SELECTOR,'.search-field-container.ng-tns-c309-0')
    search = search_div.find_element(By.CSS_SELECTOR,'input')
    search.send_keys(order['symbol'])
    time.sleep(2)
    search.send_keys(Keys.ENTER)
    

    invest = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'.trade-button.button-green'))
        )
    invest.click()
    
    # SETTING THE PARAMETERS 
    
    amount_input_div = driver.find_element(By.CSS_SELECTOR,'.stepper')
    input = amount_input_div.find_element(By.CSS_SELECTOR,'input')
    
    input.clear()
    
    for i in range(10):
        input.send_keys(Keys.SHIFT,Keys.ARROW_LEFT)
        
        input.send_keys(Keys.DELETE)
        
    input.clear()
        
    input.send_keys(order['amount'])
    
    # HIT BUY 

    ex_button = driver.find_element(By.CSS_SELECTOR,'.execution-button.button-standard.button-blue')
    
    time.sleep(1)
    
    my_i = 1
    
    while my_i == 1:
        try:
            ex_button.click()
        except Exception as e:
            print('The exception is ', e, " Continuing the program now ")
            my_i = 0
            break
            
        
    

    

    return True
    


def get_value(elem):
    total_value = []
    sign = 1
    
    for i in reversed(elem):
        if i == '>':
            break
        else:
            total_value.append(i)
    
    print(total_value, ' . - is my return value')
    
    
    number = 0
    power = -2
    while ' ' in total_value:
        total_value.remove(' ')
    while '.' in total_value:    
        total_value.remove('.')
    while ',' in total_value:
        total_value.remove(',')       
    if '-' in total_value:
        total_value.remove('-')
        sign = -1
        
    for i in total_value:
        number += 10**(power) * int(i)
        power += 1
    

    return number * sign

def get_stock_stats(elem : uc.Chrome,driver: uc.Chrome ):
    
    ticker = elem.find_element(By.CSS_SELECTOR,'.group-name.top-line.table-name')
    ticker_name = ticker.get_attribute('innerHTML')
    
    print(ticker_name)
    
    driver.implicitly_wait(0.2)
    
    try: 
        buying = elem.find_element(By.CSS_SELECTOR,'span.pending')
        the_text = buying.get_attribute('innerHTML')
        print("Printing here ", the_text)
        return 
    except:
        pass
    
    
    
    
    the_values = elem.find_elements(By.CSS_SELECTOR,'span.table-cell-body')

    count = 0 
    
    final_dict = {'symbol':ticker_name}
    
    for j in the_values:
        if count == 0:
            final_dict['units'] = j.get_attribute('innerHTML')
        elif count == 1:
            final_dict['is_buy'] = j.get_attribute('innerHTML')
        elif count == 2:
            final_dict['avg_open'] = j.get_attribute('innerHTML')
        elif count == 3:
            final_dict['invested'] = j.get_attribute('innerHTML')
        elif count == 4:
            final_dict['pnl'] = j.get_attribute('innerHTML')
        elif count == 5: 
            final_dict['pnl_percent'] = j.get_attribute('innerHTML')
        elif count == 6:
            final_dict['current_value'] = j.get_attribute('innerHTML')
        count += 1
       
    
    
    print(final_dict)
    
    return final_dict
        
    


    
    


#bypass function
def seleniumUndetected():
    driver = uc.Chrome(version_main = 107) #creating a webdriver object
    driver.maximize_window() #maximize window size

    driver.get("https://www.etoro.com/login") #opening the url
    driver.implicitly_wait(25)
    
    

    mail = driver.find_element(By.ID,'username')
    mail.send_keys('videlik@gmail.com')
    
    
    my_pass = driver.find_element(By.ID,'password')
    my_pass.send_keys('Basilaras02')
    my_pass.send_keys(Keys.ENTER)
    
    try:
        virtual = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'.to-virtual'))
        )
        virtual.click()
    except Exception as e:
        logging.exception(e)
        
    
    #virtual = driver.find_element(By.CSS_SELECTOR,'.to-virtual')
    
    
    virtual_activate = driver.find_element(By.CSS_SELECTOR,'.toggle-account-button')
    virtual_activate.click()
    
    portfolio = driver.find_element(By.CSS_SELECTOR,'a[href*="/app/portfolio-page"]')
    
    
    
    portfolio.click()
    
    unit_values = driver.find_elements(By.CSS_SELECTOR,'.footer-unit-value')
    
    print(unit_values)
    

    counter = 0
    for i in unit_values:
        print(counter , i.get_attribute('innerHTML'))
        if counter == 0:
            cash_available = i
        elif counter == 1:
            cash_invested = i
        elif counter == 2:
            cash_pnl = i
        else:
            cash_value = i
        counter += 1
    
    cash_available_value = get_value(cash_available.get_attribute('innerHTML'))
    cash_invested_value = get_value(cash_invested.get_attribute('innerHTML'))
    cash_pnl_value = get_value(cash_pnl.get_attribute('innerHTML'))
    cash_value_value = get_value(cash_value.get_attribute('innerHTML'))
    
    print(cash_available_value)
    print(cash_invested_value)
    print(cash_pnl_value)
    print(cash_value_value)
    
    
    stocks_div = driver.find_element(By.CSS_SELECTOR,'.et-table-body')
    print('=========')
    
    
    stocks = stocks_div.find_elements(By.CSS_SELECTOR,'.et-table-row-main')
    
    
    for i in stocks:
        get_stock_stats(i,driver)

    driver.implicitly_wait(20)

    
    test_order = {
        'symbol': 'BTC',
        'amount' : '1999'
    }
    
    buy_stock(driver,test_order)
    
        
    
    
    
    
    time.sleep(300)

#driver
if __name__ == "__main__":
    seleniumUndetected() #call the function
    
    
    
    
time.sleep(10)


