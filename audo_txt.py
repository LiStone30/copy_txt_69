from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from pathlib import Path
from util import run_element, is_get_element

import time
import random
import os
import logging
import requests

# 从69小说中爬取一本小说的txt

def copy_txt(in_driver_link, dirs, page_id, text_xpath='/html/body/div[2]/div[1]/div[3]'):
    # in_driver 打开网页
    # 读取str 保存在txt中
    
    edge_options = Options()
    edge_options.add_argument('--headless')  
    in_driver = webdriver.Edge(options=edge_options)
    in_driver.maximize_window()
    in_driver.get(in_driver_link)
    try:
        texts_page = in_driver.find_element(By.XPATH, text_xpath).text
    except Exception as e:
        logging.basicConfig(level=logging.ERROR,#控制台打印的日志级别
            filename='new.log',
            filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
            #a是追加模式，默认如果不写的话，就是追加模式
            format=
            '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
            #日志格式
            )
        return 0
    file_name = str(page_id) + ".txt"
    path = os.path.join(dirs, file_name)
    with open(path, "w") as fw:
        fw.write(texts_page)

def copy_catalogue(link, dirs, book_name, user_agent, id=0, \
    in_catalogue_xpath='//*[@id="catalog"]/ul/li/a', \
    in_text_xpath='/html/body/div[2]/div[1]/div[3]', \
    in_proxy=None):
    dirs = os.path.join(dirs, book_name)
    if not os.path.exists(dirs):
        os.makedirs(dirs)

    edge_options = Options()
    edge_options.add_argument('--headless')  
    edge_options.add_argument('--user-agent=%s' % user_agent)
    if in_proxy != None:
        edge_options.add_argument('--proxy-server=' + in_proxy)
    driver = webdriver.Edge(options=edge_options)
    driver.maximize_window()
    driver.get(link)

    catalogue = driver.find_elements(By.XPATH, in_catalogue_xpath)
    links = [(link.get_attribute('href'), link.get_attribute('text')) for link in catalogue]
    driver.quit()
    out_id = 0
    for t_i in range(id, len(links)):
        t_link = links[t_i]
        copy_txt(t_link[0], dirs, str(t_i)+t_link[1], text_xpath=in_text_xpath) # 16 239
        out_id = t_i
    return out_id


URL = "https://www.69shu.pro/book/46913/" # 目录页
# https://www.69shu.pro/txt/54780/35201209
# https://www.sumingxs.com/xiaoshuo/42/
dirs = "./page_text"
# in_catalogue_xpath = '//*[@id="list"]/ul/li/a' 
# in_text_xpath = '//*[@id="c"]'
in_catalogue_xpath = '//*[@id="catalog"]/ul/li/a'
in_text_xpath = '/html/body/div[2]/div[1]/div[3]'

in_user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
# in_proxy = '58.58.213.55:8888' # 自己设置一个ip代理的池子  防止封IP
# https://httpbin.org/headers
# https://httpbin.org/ip

out_id = copy_catalogue(URL, dirs, "北宋穿越指南", in_user_agent, 0, in_catalogue_xpath, in_text_xpath)
print(out_id)
