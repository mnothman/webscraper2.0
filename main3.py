from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
import time #for sleep
from selenium.webdriver.common.keys import Keys #allows us to use enter and esc keys in search bar etc
from selenium.webdriver.common.by import By #need to search
from selenium.webdriver.support.wait import WebDriverWait #need to wait before pages are loaded to search
from selenium.webdriver.support import expected_conditions as EC #need to wait before pages are loaded to search
from tkinter import * #need tkinter to get user input and store into a variable to pass thru the google search bar


#uses tkinter to get user input during runtime to search, gets input and stores it into search box variable, and then we search for said variable.
#this in turn would cause us to loop thru each of the articles and then scrape the data from them 

driver = webdriver.Chrome() # Open a new Chrome window


def searchQuery(): 
    query = entry.get() # Get the user's query from the text box
 #   driver = webdriver.Chrome() # Open a new Chrome window
    driver.get('https://www.google.com/') # Navigate to the Google home page
    search_box = driver.find_element(By.CLASS_NAME, 'gLFyf') #get the google search bar
    search_box.send_keys(query) # Type the user's query into the search box
    search_box.submit() # Submit the search
    articlesTitle = driver.find_elements(By.CLASS_NAME, 'LC20lb.MBeuO.DKV0Md')
    #articles = WebDriverWait(driver, 5).until(
    #    EC.presence_of_all_elements_located((By.CLASS_NAME, "LC20lb MBeuO DKV0Md"))) #wait 10 seconds until all articles with the specified class name are present 
    return articlesTitle


#time.sleep(5)  # add a delayso page doesnt instantly shut off 

#articlesTitle = driver.find_elements(By.CLASS_NAME, "LC20lb MBeuO DKV0Md") #LC20lb MBeuO DKV0Md is the class name of the articles that are returned in google chrome
#articlesTitle = WebDriverWait(driver, 5).until(
        #EC.presence_of_all_elements_located((By.CLASS_NAME, "LC20lb MBeuO DKV0Md"))) #wait 10 seconds until all articles with the specified class name are present 

def search_and_print():
   # time.sleep(5)  # add a delayso page doesnt instantly shut off 
    articlesTitle = searchQuery()
    for article in articlesTitle:
        print("ARTICLE TITLE:", article.text)




#def scrapeSite(): #make a variable that scrapes each site, and loop thru each article and then call this scrape method 



root = Tk() # Create the main window
root.title('Google Search')

label = Label(root, text='Enter your search query:')
label.pack()

entry = Entry(root, width=50)
entry.pack()

button = Button(root, text='Search', command=search_and_print) #needs to be search and print to print the article titles
button.pack()

root.mainloop() # Start the main loop BE CAREFUL PUTTING SLEEPS BECAUSE THE LOOP WILL NOT WORK THEN

