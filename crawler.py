from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import codecs
import os
from bs4 import BeautifulSoup


my_fb_username = "n17dccn187@gmail.com"
my_fb_password = "Daylamatkhaufacebook@123"


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

browser = webdriver.Chrome(executable_path="chromedriver.exe",options=chrome_options)
browser.get("https://www.facebook.com/groups/reactjs.vn/members")


user_input = browser.find_element_by_id("email")
user_input.send_keys(my_fb_username)
pass_input = browser.find_element_by_id("pass")
pass_input.send_keys(my_fb_password)
pass_input.send_keys(Keys.ENTER)
sleep(8)


last_height = browser.execute_script("return document.body.scrollHeight")
page_end = False
last_count = 0

count = 0
while not page_end:
    browser.find_element_by_xpath('//body').send_keys(Keys.END) 
    sleep(4)

    el = browser.find_elements_by_css_selector("div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.pfnyh3mw.d2edcug0.ofv0k9yr.cwj9ozl2")[3]
    member_el_list = el.find_elements_by_css_selector('div div div div div div div div div div span span span a')
    
    # save filter data
    for index in range(last_count,len(member_el_list)):
        member_name =  member_el_list[index].text
        member_id = member_el_list[index].get_attribute('href').split("/")[6]
        group_id = member_el_list[index].get_attribute('href').split("/")[4]
        member_url = "https://www.facebook.com/profile.php?id="+ member_id
        with open('test.txt', 'a', encoding="utf-8") as f:
            output = member_id+","+member_name+","+member_url+","+group_id
            f.write(output)
            f.write('\n')
        
    last_count = len(member_el_list)

    # save html page
    completeName = os.path.join("", "new_source.txt")
    file_object = codecs.open(completeName, "w", "utf-8")
    html = browser.page_source
    file_object.write(html)

    # handle loop
    new_height = browser.execute_script("return document.body.scrollHeight")
    if last_height == new_height:
        if count < 5:
            count += 1
        else:
            page_end = True
    else:
        count = 0
        last_height = new_height


print("END=============")
sleep(1)
browser.close()




