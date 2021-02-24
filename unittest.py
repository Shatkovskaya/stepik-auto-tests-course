import unittest
from selenium import webdriver
import time

class test_Site(unittest.TestCase):
   def test_site_1(self):
     link = "http://suninjuly.github.io/registration1.html"
     browser = webdriver.Chrome()
     browser.get(link)

    # Ваш код, который заполняет обязательные поля
     input1 = browser.find_element_by_tag_name("input")
     input1.send_keys("Ivan")
     input3 = browser.find_element_by_css_selector("[placeholder = 'Input your last name']")
     input3.send_keys("Ivanov")
     input4 = browser.find_element_by_css_selector("[placeholder = 'Input your email']")
     input4.send_keys("a@a.com")

    # Отправляем заполненную форму
     button = browser.find_element_by_css_selector("button.btn")
     button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
     time.sleep(1)

    # находим элемент, содержащий текст
     welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
     welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
     self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "The registration failed")
    
   def test_site_2(self):
       link = "http://suninjuly.github.io/registration2.html"
       browser = webdriver.Chrome()
       browser.get(link)

    # Ваш код, который заполняет обязательные поля
       input1 = browser.find_element_by_tag_name("input")
       input1.send_keys("Ivan")
       input3 = browser.find_element_by_css_selector("[placeholder = 'Input your last name']")
       input3.send_keys("Ivanov")
       input4 = browser.find_element_by_css_selector("[placeholder = 'Input your email']")
       input4.send_keys("a@a.com")

    # Отправляем заполненную форму
       button = browser.find_element_by_css_selector("button.btn")
       button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
       time.sleep(1)

    # находим элемент, содержащий текст
       welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
       welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
       self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "The registration failed")
       
       
       
if __name__ == "__main__":
    unittest.main()      