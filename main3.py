from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
import time #for sleep
from selenium.webdriver.common.keys import Keys #allows us to use enter and esc keys in search bar etc
from selenium.webdriver.common.by import By #need to search
from selenium.webdriver.support.wait import WebDriverWait #need to wait before pages are loaded to search
from selenium.webdriver.support import expected_conditions as EC #need to wait before pages are loaded to search
from tkinter import * #need tkinter to get user input and store into a variable to pass thru the google search bar
from selenium.common.exceptions import StaleElementReferenceException #FOR THE STALEELEMENTREFERENCEEXCEPTION

#what code is doing: the search query asks for user input and then sends that into google, then in the search and print, we get the total list of article titles, and then we TRY to loop through them, and we make sure we are not revisiting the same
#url by adding it into a list and then checking if our url we are on is in that list. BUT, getting the url returns something like <selenium.webdriver.remote.webelement.WebElement (session="a60e40bd6d127cdc2cc71f0190a5f2ab", element="8103ec07-ab2b-4a28-a698-8f62409b9025")>
#and not the actual http url


#WHAT I CAN DO IS, I CAN JUST OPEN A NEW TAB AND THEN IN THAT TAB I CAN PRINT WHAT I NEED AND THEN CLOSE IT, AND THEN NAVIGATE BACK TO THE FIRST TAB AND LOOP THROUGH THAT WAY 









#get user input for what to google search -> get article titles, article urls, article info and store them in a csv file -> to make sure we not revisiting the same site we can store the url into a set and only continue if its not in there


#uses tkinter to get user input during runtime to search, gets input and stores it into search box variable, and then we search for said variable.
#this in turn would cause us to loop thru each of the articles and then scrape the data from them 

#keep a set to keep track of sites we visited so we don't revisit the same site
driver = webdriver.Chrome() # Open a new Chrome window


def searchQuery(): 
    query = entry.get() # Get the user's query from the text box
 #   driver = webdriver.Chrome() # Open a new Chrome window
    driver.get('https://www.google.com/') # Navigate to the Google home page
    search_box = driver.find_element(By.CLASS_NAME, 'gLFyf') #get the google search bar
    search_box.send_keys(query) # Type the user's query into the search box
    search_box.submit() # Submit the search
    articlesTitle = driver.find_elements(By.CLASS_NAME, 'LC20lb.MBeuO.DKV0Md') #need to have . instead of space with css

    return articlesTitle


#time.sleep(5)  # add a delayso page doesnt instantly shut off 

#articlesTitle = driver.find_elements(By.CLASS_NAME, "LC20lb MBeuO DKV0Md") #LC20lb MBeuO DKV0Md is the class name of the articles that are returned in google chrome
#articlesTitle = WebDriverWait(driver, 5).until(
        #EC.presence_of_all_elements_located((By.CLASS_NAME, "LC20lb MBeuO DKV0Md"))) #wait 10 seconds until all articles with the specified class name are present 

def scrapeSite():
#     # Scrape data from the current page
#     # This function can be modified to extract the data that you need
    print("article url:", driver.current_url)
    print("ARTICLE TITLE:", driver.title) #gets the article title while we are inside the article, don't need to get it while we are outside anymore
    #print(driver.page_source)

# def openSiteNewTab():
#     action = ActionChains(driver)
#     action.context_click(article).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.RETURN).perform()


#get all the articles in a list and loop thru it using for i in range(len(listofarticles))

def search_and_print_title(): #PRINTING THE TITLES WORK BUT WHEN I TRY AND LOOP THRU THE SITES IT GIVES ME PROBLEMS
    visited_urls = set()
    articlesTitle = searchQuery()
    wait = WebDriverWait(driver, 10)  # wait up to 10 seconds for the articles to be present NEW
    articlesTitle = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'LC20lb.MBeuO.DKV0Md'))) #NEW
    num_articles = len(articlesTitle) #can do here or in the loop
    print("NUMBER OF ARTICLES ON PAGE:", num_articles)

    print("error 1 stopped before loop")
    for i in range(len(articlesTitle)): #ITERATE THRU THE LENGTH OF ARTICLES
        try:         
            article = articlesTitle[i] #GET ONE ARTICLE i
            time.sleep(10) 
            article.click() #CLICK ON THE ARTICLE AND GET THE URL, IF THE URL IS IN OUR VISITED URLS THEN CONTINUE i++, IF IT IS NOT THEN GET THE DATA FROM THE ELSE STATEMENT
            time.sleep(10) 
            url = driver.current_url
            print("error 2")
            if url in visited_urls:
                print("error 3 driver already in visited url")
                continue
            else: #I WANT TO OPEN THE PAGE IN ANOTHER PAGE 
                url = driver.current_url
                scrapeSite()
                #wait.until(EC.url_changes(driver.current_url))  # wait for the page to load NEW
                print("error 7")
                
                driver.back()
                print("page did not fully load yet")
                print(visited_urls)
                print("error 8") #this doesn't load until the web page is done loading
                time.sleep(3) #sleep to wait for the articles to load again
        except StaleElementReferenceException:
                # The element is no longer attached to the page, retry the action
            continue
              




root = Tk() # Create the main window
root.title('Google Search')

label = Label(root, text='Enter your search query:')
label.pack()

entry = Entry(root, width=50)
entry.pack()

button = Button(root, text='Search', command=search_and_print_title) #needs to be search and print to print the article titles
button.pack()

root.mainloop() # Start the main loop BE CAREFUL PUTTING SLEEPS OUTSIDE OF A DEF BECAUSE THE LOOP WILL NOT WORK THEN

