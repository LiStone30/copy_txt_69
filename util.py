import time
import random

def run_element(in_driver, xpath_str, description, in_str=None, log_save_path=None, sleep_time=5):
    """
    获取xpath_str指向的元素，如果in_str非空则输入字符串，否则点击元素
    """
    time.sleep(sleep_time + random.randint(0,sleep_time))
    try:
        element = in_driver.find_element_by_xpath(xpath_str)
        if in_str == None:
            element.click()
        else:
            element.send_keys(in_str)
    except Exception as e:
        print(description + "元素未能获取 \n")
        with open(log_save_path, "a+") as fa:
            fa.write(time.asctime(time.localtime(time.time()))  + description + "元素未能获取 \n")

def is_get_element(in_driver, xpath_str, description, log_save_path, sleep_time=5):
    try:
        return in_driver.find_element_by_xpath(xpath_str)
    except Exception as e:
        print(description + "元素未能获取 \n")
        with open(log_save_path, "a+") as fa:
            fa.write(time.asctime(time.localtime(time.time())) + description + "元素未能获取 \n")
        return None
    
def is_True_page():
    """
    判断两页是否正确
    eg：
    第1章
    第12章
    return False
    """
    
    pass