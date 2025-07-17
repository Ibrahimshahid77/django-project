from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")
print(driver.title)

input("Press Enter to quit...") 
driver.quit()

