from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def scrapehrs():
    for i in range(1,6):
        try:
            course = driver.find_element(f'xpath','//*[@class ="heading"]')
            course.click()
            time.sleep(3)
            name = driver.find_element(f'xpath','//*[@id="udemy"]/div[1]/div[2]/div/div/div[1]/div[3]/div/div/div[3]/div/h1').text
            rating = driver.find_element('xpath','//*[@id="udemy"]/div[1]/div[2]/div/div/div[1]/div[3]/div/div/div[3]/div/div[2]/div/a/span[1]/span[2]').text
            total_stu = driver.find_element('xpath','//*[@id="udemy"]/div[1]/div[2]/div/div/div[1]/div[3]/div/div/div[3]/div/div[2]/div/div').text
            hours = driver.find_element('xpath','//*[@id="udemy"]/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div/div/div[5]/div/div/ul/li[1]/div/div/span').text

            print(name,rating, total_stu, hours)
        except Exception as e:
            print(e)





def startpy():
    driver.get("https://999coursesale.com/freebie-courses-list.php?pd12=free-v5-ret-orig-2-udemy-ans-yes-yes&orig_utm_content=&orig_utm_medium=&orig_utm_campaign=&utm_source=nonzu&_redir=")
    driver.maximize_window()
    time.sleep(3)
    scrapehrs()

startpy()