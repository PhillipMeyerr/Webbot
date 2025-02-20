from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
# Define the remote URL and desired capabilities
remote_url = "http://localhost:4444/wd/hub"
capabilities = DesiredCapabilities.CHROME.copy()

# Create a new instance of the Chrome driver
driver = webdriver.Remote(command_executor=remote_url, desired_capabilities=capabilities)

# Example usage: open a webpage
driver.get("google.com")

time.sleep(100)
# Close the browser
driver.quit()