from lxml import etree

import random
# 定义了储存结构


class Job:
    def __init__(self, title, updated, label, location):
        self.title = title
        self.updated = updated
        self.label = label
        self.location = location

# 用于打印数组中的数据


def printlist(lst):
    for job in lst:
        print(job)


# 能够抓取一页的页面数据
def catchOnePage(html, Jobs):
    positionCollection = html.xpath('//div[@class="_2AOmjKmlEtuR_KEoehWYcN"]')

    for position in positionCollection:
        titles = position.xpath(
            ".//div[@class='_1RRlPtjyYmeDGCWt9lrk2P _3vj2eS7k7Mwpko5_6OSRu2']")

        subtitle = position.xpath(
            ".//div[@class='next-col next-col-24 _3xd1nlzzIkGgrscu6LLqv_']")[0]
        lst = []
        # 对于所有的小数据进行遍历并获得数据
        for e in subtitle:
            lst.append(e.xpath('string(.)'))
        Jobs.append(Job(titles[0].text, lst[0], lst[1], lst[2]))


# input a int: maxtime
def random_sleep(driver, maxtime):
    sleeptime = random.random() * maxtime*5
    driver.implicitly_wait(sleeptime)


# return current page and total page
def process(html):
    pagecount = html.xpath('//span[@class="next-pagination-display"]')[0]
    text = [x.strip() for x in pagecount.xpath('.//text()')]
    text[1] = text[1].lstrip('/')
    text = [int(subject) for subject in text]
    return text
