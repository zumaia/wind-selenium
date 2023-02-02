from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

options = Options()
options.add_argument("--incognito")

DRIVER_PATH = './chromedriver'
browser = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

browser.get("https://github.com/zumaia")

# Wait 20 seconds for page to load
timeout = 20
try:
	# Wait until the final element [Avatar link] is loaded.
   	# Assumption: If Avatar link is loaded, the whole page would be relatively loaded because it is among
	# the last things to be loaded.
    WebDriverWait(browser, 
                  timeout).until(EC.visibility_of_element_located((By.XPATH, '//img[@class="rounded-1 avatar-user"]')))
                                                                   
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()
    
 # Get all of the titles for the pinned repositories
# We are not just getting pure titles but we are getting a selenium object
# with selenium elements of the titles.

# find_elements_by_xpath - Returns an array of selenium objects.
titles_element = browser.find_elements_by_xpath("//a[@class='text-bold flex-auto min-width-0]")

# List Comprehension to get the actual repo titles and not the selenium objects.
titles = [x.text for x in titles_element]

# print response in terminal
print('TITLES:')
print(titles, '\n')


