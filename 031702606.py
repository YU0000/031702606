import os
def install_package(package_name):
    package_name = package_name.replace("_", "-")  # 下载pip fake_useragent 包时  包名是:fake-useragent
    p = os.popen("pip list --format=columns")  # 获取所有包名 直接用 pip list 也可获取
    pip_list = p.read()  # 读取所有内容
    # print(pip_list)
    if package_name in pip_list:
        # print("已经安装{}".format(package_name))
        return True
    else:
        # print("没有安装{}!即将自动安装,请稍后".format(package_name))
        p = os.popen("pip install {}".format(package_name))
        if "Success" in p.read():
            # print("安装{}成功!".format(package_name))
            return True if "Success" in p.read() else False
install_package("jieba")
install_package("json")
install_package("re")


import json
import jieba
from jieba import posseg
import re


class Addressbook:
    def __init__(self,name,tele_num,province,city,district,street,road,road_num,building):
        self.name = name
        self.tele_num = tele_num
        self.province = province
        self.city = city
        self.district = district
        self.street = street
        self.road = road
        self.road_num = road_num
        self.building = building
    def print(self):
        print(self.name)
        print(self.tele_num)
        print(self.province)
        print(self.city)
        print(self.district)
        print(self.street)
        print(self.road)
        print(self.road_num)
        print(self.building)

def search_add(addressbook,single_address):
    seg_list = list(jieba.cut(single_address, cut_all=False))
    for eachline in range(len(seg_list)):
        x = seg_list[eachline]
        if (u'省' in seg_list[eachline] or u'自治区' in seg_list[eachline]):
            addressbook.province = seg_list[eachline]
        elif (
                u'浙江' in x or u'安徽' in x or u'福建' in x or u'江西' in x or u'广东' in x or u'湖南' in x or u'海南' in x or u'河南' in x or u'湖北' in x or u'河北' in x or u'山西' in x or u'青海' in x or u'陕西' in x or u'甘肃' in x or u'四川' in x or u'贵州' in x or u'云南' in x or u'辽宁' in x or u'吉林' in x or u'黑龙江' in x):
            addressbook.province = seg_list[eachline] + '省'
        elif (u'广西' in x or u'内蒙古' in x or u'宁夏' in x or u'新疆' in x or u'西藏' in x):
            addressbook.province = seg_list[eachline] + '自治区'
        elif (u'地区' in seg_list[eachline] or u'自治州' in seg_list[eachline] or u'盟' in seg_list[eachline]):
            addressbook.city = seg_list[eachline]
        elif (u'矿区' in seg_list[eachline] or u'自治县' in seg_list[eachline] or u'自治旗' in seg_list[eachline]):
            addressbook.district = seg_list[eachline]
        elif (u'市' in seg_list[eachline]):
            if (u'天津' in seg_list[eachline]):
                addressbook.city = seg_list[eachline]
                addressbook.province = "天津"
            elif (u'北京' in seg_list[eachline]):
                addressbook.city = seg_list[eachline]
                addressbook.province = "北京"
            elif (u'重庆' in seg_list[eachline]):
                addressbook.city = seg_list[eachline]
                addressbook.province = "重庆"
            elif (u'上海' in seg_list[eachline]):
                addressbook.city = seg_list[eachline]
                addressbook.province = "上海"
            else:
                if (addressbook.city != []):
                    addressbook.city = seg_list[eachline]
                else:
                    addressbook.district = seg_list[eachline]
        elif (u'县' in seg_list[eachline] or u'区' in seg_list[eachline]):
            addressbook.district = seg_list[eachline]
        elif (u'街道' in x or u'镇' in x or u'乡' in x or u'路' in x or u'巷' in x or u'街' in x):
            addressbook.street = seg_list[eachline]
        single_address = re.sub(seg_list[eachline], '', single_address)
        if (addressbook.district != ""):
            break
    return addressbook
# def json_output(text):

addressbook = Addressbook('', '', '', '', '', '', '', '', '')
single_address=input()
ret = re.findall(r"1\d{10}",single_address) #(r"1[35678]\d{9}", tel) m=re.findall(r"0\d2,30\d2,3\d{7,8}|0\d{2,3}[ -]?\d{7,8}", single_address)
for  x in ret:
    addressbook.tele_num = x
single_address = re.sub('1\d{10}', '', single_address)
seg_list = list(jieba.cut(single_address,cut_all=False))

for eachline in range(len(seg_list)):
    seg_list[eachline]
    if (seg_list[eachline] == '1' or seg_list[eachline] == '2' or seg_list[eachline] == '3'):
        kind = seg_list[eachline]
        continue
    if(seg_list[eachline] != '!'):
        addressbook.name=addressbook.name+seg_list[eachline]
        if(seg_list[eachline+1] == ','):
            break


single_address = re.sub('^\d+\!+[\u4e00-\u9fa5]+\,','', single_address)
single_address = re.sub('\.','', single_address)


addressbook=search_add(addressbook,single_address)
# for eachline in range(len(seg_list)):
#     x=seg_list[eachline]
#     if(u'省'in seg_list[eachline] or u'自治区' in seg_list[eachline]):
#         addressbook.province=seg_list[eachline]
#     elif(u'浙江' in x or u'安徽' in x or u'福建' in x or u'江西' in x or u'广东' in x or u'湖南' in x or u'海南' in x or u'河南' in x or u'湖北' in x or u'河北' in x or u'山西' in x or u'青海' in x or u'陕西' in x or u'甘肃' in x or u'四川' in x or u'贵州' in x or u'云南' in x or u'辽宁' in x or u'吉林' in x or u'黑龙江' in x):
#         addressbook.province = seg_list[eachline]+'省'
#     elif(u'广西' in x or u'内蒙古' in x or u'宁夏' in x or u'新疆' in x or u'西藏' in x):
#         addressbook.province = seg_list[eachline] + '自治区'
#     elif (u'地区' in seg_list[eachline] or u'自治州' in seg_list[eachline] or u'盟' in seg_list[eachline]):
#         addressbook.city=seg_list[eachline]
#     elif(u'矿区' in seg_list[eachline] or u'自治县' in seg_list[eachline] or u'自治旗' in seg_list[eachline]):
#         addressbook.district=seg_list[eachline]
#     elif(u'市' in seg_list[eachline]):
#         if (u'天津' in seg_list[eachline]):
#             addressbook.city=seg_list[eachline]
#             addressbook.province="天津"
#         elif(u'北京' in seg_list[eachline]):
#             addressbook.city = seg_list[eachline]
#             addressbook.province = "北京"
#         elif(u'重庆' in seg_list[eachline]):
#             addressbook.city = seg_list[eachline]
#             addressbook.province = "重庆"
#         elif(u'上海' in seg_list[eachline]):
#             addressbook.city = seg_list[eachline]
#             addressbook.province = "上海"
#         else:
#             if(addressbook.city != []):
#                 addressbook.city = seg_list[eachline]
#             else:
#                 addressbook.district = seg_list[eachline]
#     elif(u'县' in seg_list[eachline] or u'区' in seg_list[eachline]):
#         addressbook.district = seg_list[eachline]
#     elif(u'街道' in x or u'镇' in x or u'乡' in x or u'路' in x or u'巷' in x or u'街' in x):
#         addressbook.street = seg_list[eachline]
#     single_address = re.sub(seg_list[eachline], '', single_address)
#     if(addressbook.district != ""):
#         break
if(kind == '1'):
    addr=[addressbook.province,
        addressbook.city,
        addressbook.district,
        addressbook.street,
        addressbook.building]
    # data_json = json.dumps(addr.__dict__,ensure_ascii=False)

    data = {
    '姓名':addressbook.name,
    '手机':addressbook.tele_num,
    '地址':addr
    }

    data_json = json.dumps(data,ensure_ascii=False)
    print(data_json)
if(kind == '2'):
    addr = [addressbook.province,
            addressbook.city,
            addressbook.district,
            addressbook.street,
            addressbook.road,
            addressbook.road_num,
            addressbook.building]
    # data_json = json.dumps(addr.__dict__,ensure_ascii=False)

    data = {
        '姓名': addressbook.name,
        '手机': addressbook.tele_num,
        '地址': addr
    }

    data_json = json.dumps(data, ensure_ascii=False)
    print(data_json)
if(kind == '3'):
    addr = [addressbook.province,
            addressbook.city,
            addressbook.district,
            addressbook.street,
            addressbook.road,
            addressbook.road_num,
            addressbook.building]
    # data_json = json.dumps(addr.__dict__,ensure_ascii=False)

    data = {
        '姓名': addressbook.name,
        '手机': addressbook.tele_num,
        '地址': addr
    }

    data_json = json.dumps(data, ensure_ascii=False)
    print(data_json)