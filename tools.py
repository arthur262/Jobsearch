from lxml import etree
import random


# 用于打印数组中的数据
def printlist(lst):
    for job in lst:
        print(job)


# 能够抓取一页的页面数据
def catchOnePage(html, Jobs,count):
    positionCollection = html.xpath('//div[@class="_2AOmjKmlEtuR_KEoehWYcN"]')
    for position in positionCollection:
        titles = position.xpath(
            ".//div[@class='_1RRlPtjyYmeDGCWt9lrk2P _3vj2eS7k7Mwpko5_6OSRu2']")

        subtitle = position.xpath(
            ".//div[@class='next-col next-col-24 _3xd1nlzzIkGgrscu6LLqv_']")[0]
        lst = []
        # 对于所有的小数据进行遍历并获得数据
        for index,title in enumerate(subtitle,start=1):
            match index:
                case 1:
                    lst.append(title.text)
                case _:
                    lst.append(title.getchildren()[0].text)
        
        Jobs.update({count: 
                {'title': titles[0].text,
                 'updated': lst[0], 
                 'subject':lst[1], 
                 'location':lst[2]}})
        count+=1
    return count
        


# input a int: maxtime
def random_sleep( maxtime):
    sleeptime = random.random() * maxtime
    return sleeptime

# return current page and total page
def process(html):
    pagecount = html.xpath('//span[@class="next-pagination-display"]')[0]
    text = [x.strip() for x in pagecount.xpath('.//text()')]
    text[1] = text[1].lstrip('/')
    text = [int(subject) for subject in text]
    return text
