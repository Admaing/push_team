from selenium import webdriver
import json
from selenium.webdriver.common.action_chains import ActionChains
import os
#填写webdriver的保存目录


#加载cookie
profile_dir=r"C:\Users\高永福\AppData\Local\Google\Chrome\User Data"
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir="+os.path.abspath(profile_dir))
#记得写完整的url 包括http和https

driver = webdriver.Chrome('C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe',chrome_options=chrome_options)
driver.get('http://xgfy.sit.edu.cn/h5/?from=groupmessage#/pages/index/index')
elem = driver.find_element_by_xpath("/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-image")
print(elem)

handles = driver.window_handles
driver.switch_to.window(handles[-1])
actions = ActionChains(driver)
actions.move_to_element(elem)
actions.click(elem)
actions.perform()
handles = driver.window_handles
driver.switch_to.window(handles[-1])
elem1 = driver.find_element_by_xpath("/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-scroll-view[1]/div/div/div/uni-view/uni-view[1]")
actions.click(elem1)
actions.perform()
handles = driver.window_handles
driver.switch_to.window(handles[-1])
elem2 = driver.find_element_by_xpath("/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-scroll-view[2]/div/div/div/uni-view[1]/uni-view/uni-view[11]/uni-view/uni-checkbox-group/uni-label/uni-view[1]")
actions.click(elem2)
actions.perform()
handles = driver.window_handles
driver.switch_to.window(handles[-1])
elem3 = driver.find_element_by_xpath("/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-scroll-view[2]/div/div/div/uni-view[1]/uni-view/uni-view[12]/uni-button")
actions.click(elem3)
actions.perform()
#首先清除由于浏览器打开已有的cookies
# driver.delete_all_cookies()
#
# with open('cookies.txt','r') as cookief:
#     #使用json读取cookies 注意读取的是文件 所以用load而不是loads
#     cookieslist = json.load(cookief)
#
#     # 方法1 将expiry类型变为int
#     for cookie in cookieslist:
#         #并不是所有cookie都含有expiry 所以要用dict的get方法来获取
#         if isinstance(cookie.get('expiry'), float):
#             cookie['expiry'] = int(cookie['expiry'])
#         driver.add_cookie(cookie)

    #方法2删除该字段
    # for cookie in cookieslist:
    #     #该字段有问题所以删除就可以  浏览器打开后记得刷新页面 有的网页注入cookie后仍需要刷新一下
    #     if 'expiry' in cookie:
    #         del cookie['expiry']
    #     driver.add_cookie(cookie)