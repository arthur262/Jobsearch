from lxml import etree
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
import tools
from file_R_W_tool import write_file, readfile
import json



# initalizes    
url = "https://talent-holding.alibaba.com/off-campus/position-list?lang=zh"
Jobs = dict()
# 使用浏览器进行抓取
driver = webdriver.Firefox()
driver.get(url)
count=0
while True:
    time=tools.random_sleep(10)
    if time<3:time+=3
    driver.implicitly_wait(time )
    try:
        driver.find_element(By.CSS_SELECTOR,
                            "div#_1RRlPtjyYmeDGCWt9lrk2P _3vj2eS7k7Mwpko5_6OSRu2")
    except Exception as e:
        doNothing = e

    pageSource = driver.page_source
    html = etree.HTML(pageSource, etree.HTMLParser())
    
    # 抓取一次页面的数据
    count=tools.catchOnePage(html, Jobs,count)
    # 获得比较当前页面数和总page数
    text = tools.process(html)
    
    if text[0] >= text[1]:
        break
    
    # 滑动到底
    js_code = 'window.scrollBy(0, document.body.scrollHeight)'
    driver.execute_script(script=js_code)
    
    driver.implicitly_wait(tools.random_sleep(10))
    next = driver.find_element(By.XPATH,
                               ".//button[@class='next-btn next-medium next-btn-normal next-pagination-item next-next'] ")
    next.click()
    
driver.implicitly_wait(tools.random_sleep(10))
driver.quit()
json_dict_2 = json.dumps(Jobs, indent=2, sort_keys=True, ensure_ascii=False)
write_file(json_dict_2,'data.json')
