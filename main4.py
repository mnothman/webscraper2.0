from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def search_query(query):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.google.com/")
    search_query = driver.find_element(By.NAME, "q")
    search_query.send_keys(query)
    search_query.send_keys(Keys.RETURN)
    try:
        # wait for search results to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h3[@class='LC20lb MBeuO DKV0Md']")))
    except TimeoutException:
        print("Timed out waiting for page to load")
        driver.quit()
        return
    return driver

def search_and_print_title(driver):
    try:
        articlesTitle = driver.find_element(By.XPATH, "//h3[@class='LC20lb MBeuO DKV0Md']")
        articlesTitle.click()
        print(driver.title)
    except ElementClickInterceptedException:
        print("Failed to click on article title, trying again...")
        time.sleep(1)
        search_and_print_title(driver)
    except:
        print("An error occurred while searching for the article title")
    finally:
        driver.quit()

# Example usage
driver = search_query("python tutorial")
if driver is not None:
    search_and_print_title(driver)
