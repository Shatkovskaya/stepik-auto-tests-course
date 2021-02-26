import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    
    
@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1" , "https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"] )

def test_guest_should_see_login_link(browser, link):
    link1 = f"{link}"
    browser.get(link1)
    browser.implicitly_wait(5)
    form = browser.find_element_by_css_selector('[placeholder = "Type your answer here..."]')
    answer = str(math.log(int(time.time())))
    form.send_keys(answer)
    browser.find_element_by_css_selector(".attempt__actions .submit-submission").click()
    WebDriverWait(browser,5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".attempt__message .smart-hints__feedback")))
    text = browser.find_element_by_css_selector(".attempt__message .smart-hints__feedback > pre").text
    assert text == "Correct!", text