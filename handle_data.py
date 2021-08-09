import codecs
from bs4 import BeautifulSoup
from lxml import etree
import os
import json

file = open("new_source.txt", encoding="utf8")

soup = file.read()
bs =  BeautifulSoup(soup,"html.parser")

el = bs.select('div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.pfnyh3mw.d2edcug0.ofv0k9yr.cwj9ozl2')[3]
member_el_list = el.select('div div div div div div div div div div span span span a')
print(len(member_el_list))

# member_list= []
# for member_el in member_el_list:
#     member_dic = {}
#     member_dic['name'] = member_el.get_text().strip()
#     member_dic['user_id'] = member_el['href'].split("/")[4]
#     member_dic['group_id'] = member_el['href'].split("/")[2]
#     member_dic['url'] = "https://www.facebook.com/profile.php?id="+member_dic['user_id']
#     member_list.append(member_dic)

    # print(member_el.get_text().strip())
    # print(member_el['href'])

# with open('jsonfile.json', 'w') as fout:
#     json.dump(your_list_of_dict, fout)