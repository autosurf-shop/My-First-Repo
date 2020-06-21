from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--allow-popups-during-page-unload")
chrome_options.add_argument("--enable-auto-reload")
driver = webdriver.Chrome('./chromedriver', options=chrome_options)


driver.maximize_window()


driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://t.co/HlVUCorAUc?amp=1")
time.sleep(5)
driver.find_element_by_xpath('//*[@id="navbar-main"]/div/ul/li[4]/a').click()
time.sleep(5)
driver.find_element_by_id("email").send_keys("minamandal100@gmail.com")
driver.find_element_by_id("password").send_keys("mina38985")
driver.find_element_by_id("btn-submit").click()
time.sleep(5)
driver.get("https://www.netvisiteurs.com/member/surf-auto.php")
time.sleep(2)
driver.find_element_by_id("surf").click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[2])
time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
driver.get("https://ultraviews.net/Client/")
time.sleep(2)
driver.find_element_by_id("Username").send_keys("rock6064")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="6NeGUw"]/div[1]/button').click()

time.sleep(3600)

driver.quit()
