from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def send_json(json_string, api_key, wait_time):

    options = Options()
    options.add_argument("--no-sandbox")
    
    driver = webdriver.Chrome(options=options)

    driver.get("https://qa.mina.com.br/integration/swagger/index.html")
    driver.implicitly_wait(2)

    section = driver.find_element(by=By.ID, value="operations-ProductionCount-post_v1_ProductionCount")
    section.click()

    try_button_div = driver.find_element(by=By.CLASS_NAME, value="try-out")
    try_button_div.click()

    api_key_input = driver.find_element(by=By.CSS_SELECTOR, value=".parameters .parameters-col_description input")
    api_key_input.clear()
    api_key_input.send_keys(api_key)

    param_text_area = driver.find_element(by=By.CSS_SELECTOR, value=".body-param__text")
    param_text_area.clear()
    param_text_area.send_keys(json_string)

    execute_button_div = driver.find_element(by=By.CLASS_NAME, value="execute-wrapper")
    execute_button_div.click()

    # response_html = driver.find_element(by=By.CSS_SELECTOR, value="table .responses-table .live-responses-table")
    # response_text = response_html.text
    response_text = ""

    time.sleep(wait_time)
    driver.quit()

    return response_text