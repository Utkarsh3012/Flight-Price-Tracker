from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import time, threading
from re import sub
from decimal import Decimal
import smtplib 

global lowest_flight
lowest_flight=100000

driver = webdriver.Chrome(ChromeDriverManager().install())
#getting the website
def find_cheapest_flight():

    driver.get("https://www.makemytrip.com/flight/search?tripType=O&itinerary=RPR-MAA-01/01/2021&paxType=A-1_C-0_I-0&cabinClass=E&sTime=1605865231358&forwardFlowRequired=true&mpo=&intl=false")
    sleep(5)
    #The name of the class airways-name
    flight_name=driver.find_elements_by_class_name("airways-name")[0].text
    
    #print(flight_name)
    
    flight_price1= driver.find_elements_by_class_name("actual-price")[0].text
    #print(flight_price)
    flight_price= Decimal(sub(r'[^\d.]', '', flight_price1))

    return flight_name, flight_price

def notification():
    
  
    # Connecting to gmail
    s = smtplib.SMTP('smtp.gmail.com', 587) 
  
    # to start TLS 
    s.starttls() 
  
    #  FOR Authentication 
    s.login("utkarshutest@gmail.com", "password") 
  
    # email body  
    message = "Check the website the prices just went down!!"
  
    # sender and receiver
    s.sendmail("utkarshutest@gmail.com", "upendrautkarsh02@gmail.com", message) 
  
    s.quit()    
    

def caller_function(lowest_flight):
    
    
    
    
    flight_name, flight_price= find_cheapest_flight()
    #print(flight_name)
    #print(flight_price)

    #Check Statement
    if(flight_price<lowest_flight):
        lowest_flight= flight_price
        lowest_flight_name= flight_name
        
        print(lowest_flight_name)
        print(lowest_flight)  
        notification()  


    threading.Timer(10, caller_function(lowest_flight)).start()

caller_function(lowest_flight)