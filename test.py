from lxml import etree
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
import tools

# initalizes
url = "https://talent-holding.alibaba.com/off-campus/position-list?lang=zh"
Jobs = []

# 使用浏览器进行抓取
driver = webdriver.Firefox()
driver.get(url)


while True:
    driver.implicitly_wait(3)
    try:
        driver.find_element(By.CSS_SELECTOR,
                            "div#_1RRlPtjyYmeDGCWt9lrk2P _3vj2eS7k7Mwpko5_6OSRu2")
    except Exception as e:
        doNothing = e

    pageSource = driver.page_source
    html = etree.HTML(pageSource, etree.HTMLParser())

# 抓取一次页面的数据
    tools.catchOnePage(html, Jobs)
# 获得总page数

# tools.random_sleep(driver, 10)
# 滑动到底
    js_code = 'window.scrollBy(0, document.body.scrollHeight)'
    driver.execute_script(script=js_code)
    tools.random_sleep(driver, 10)

    driver.implicitly_wait(2)
    next = driver.find_element(By.XPATH,
                               ".//button[@class='next-btn next-medium next-btn-normal next-pagination-item next-next'] ")
    next.click()
    text = tools.process(html)
    if text[0] >= text[1]:
        break


tools.random_sleep(driver, 5)
driver.quit()
print(Jobs)
