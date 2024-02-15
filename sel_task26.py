from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

url = "https://www.imdb.com/search/name/"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(100)


actions = ActionChains(driver)
actions.send_keys(Keys.ARROW_DOWN).perform()
actions.send_keys(Keys.ARROW_DOWN).perform()
actions.send_keys(Keys.ARROW_DOWN).perform()
actions.send_keys(Keys.ARROW_DOWN).perform()

sleep(4)
wait = WebDriverWait(driver, 10)
name = wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(.,'Name')]")))
name.click()
actions.send_keys(Keys.ARROW_DOWN).perform()
nameVal = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Name']")))
nameVal.send_keys("Leonardo DiCaprio")
name.click()

actions.send_keys(Keys.ARROW_DOWN).perform()
Birth = wait.until(EC.presence_of_element_located((By.XPATH, "//label[.='Birth date']")))
Birth.click()
birthDate1 = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='birth-date-start-input']")))
birthDate2 = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='birthDate-end']")))
birthDate2.send_keys("11/11/1974")
birthDate1.send_keys("11/11/1974")
Birth.click()

actions.send_keys(Keys.ARROW_DOWN).perform()
actions.send_keys(Keys.ARROW_DOWN).perform()
birthDay = wait.until(EC.presence_of_element_located((By.XPATH, "//label[.='Birthday']")))
birthDay.click()
birthDayVal = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Enter birthday']")))
birthDayVal.send_keys("11/11")
birthDay.click()

actions.send_keys(Keys.ARROW_DOWN).perform()
actions.send_keys(Keys.ARROW_DOWN).perform()
actions.send_keys(Keys.ARROW_DOWN).perform()
A_R = wait.until(EC.presence_of_element_located((By.XPATH, "//label[.='Awards & recognition']")))
A_R.click()

best_actor_N = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='test-chip-id"
                                                                    "-oscar_best_actor_nominees']")))
best_actor_N.click()

best_actor_W = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='test-chip-id"
                                                                    "-oscar_best_actor_winners']")))
best_actor_N.click()
A_R.click()

actions.send_keys(Keys.ARROW_DOWN).perform()
actions.send_keys(Keys.ARROW_DOWN).perform()
actions.send_keys(Keys.ARROW_DOWN).perform()
actions.send_keys(Keys.ARROW_DOWN).perform()
PageTopics = wait.until(EC.presence_of_element_located((By.XPATH, "//label[.='Page topics']")))
PageTopics.click()
Bio = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='test-chip-id-BIOGRAPHY']")))
Bio.click()

Bio_val = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='e.g. Arrested']")))
Bio_val.send_keys("Leonardo Wilhelm DiCaprio (/diˈkæprioʊ, dɪ-/; Italian: [diˈkaːprjo]; born November 11, 1974) is an "
                  "American actor and film producer. Known for his work in biographical and period films, "
                  "he is the recipient of numerous accolades, including an Academy Award, a British Academy Film "
                  "Award, and three Golden Globe Awards. As of 2019, his films have grossed over $7.2 billion "
                  "worldwide, and he has been placed eight times in annual rankings of the world's highest-paid "
                  "actors.")
PageTopics.click()

actions.send_keys(Keys.ARROW_DOWN).perform()
actions.send_keys(Keys.ARROW_DOWN).perform()
actions.send_keys(Keys.ARROW_DOWN).perform()
actions.send_keys(Keys.ARROW_DOWN).perform()
sleep(3)
gender = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Gender identity')]")))
gender.click()
gen_Id = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='test-chip-id-MALE']")))
gen_Id.click()
gender.click()

Credits = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Credits')]")))
Credits.click()
Credits_val = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-controls='react-autowhatever-1']")))
Credits_val.send_keys("Titanic")
Credits.click()


Adult_name = wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(.,'Adult names')]")))
Adult_name.click()
ad_val = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Exclude']")))
ad_val.click()
Adult_name.click()

see_result = wait.until(EC.presence_of_element_located((By.XPATH, "//button[.='See results']")))
see_result.click()