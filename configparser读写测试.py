'''
读取配置文件

read(filename) 直接读取ini文件内容
sections() 得到所有的section，并以列表的形式返回
options(section) 得到该section的所有option
items(section) 得到该section的所有键值对
get(section,option) 得到section中option的值，返回为string类型
getint(section,option) 得到section中option的值，返回为int类型
getfloat(section,option)得到section中option的值，返回为float类型
getboolean(section, option)得到section中option的值，返回为boolean类型


写入配置文件

add_section(section) 添加一个新的section
has_section(section) 判断是否有section
set( section, option, value) 对section中的option进行设置
remove_setion(section)删除一个section
remove_option(section, option)删除section中的option
write(fileobject)将内容写入配置文件。

配置文件：config.ini
[user]
username = tom
password = ***
email = test@host.com

[book]
bookname = python
bookprice = 25
'''

import configparser

# 生成 Config 对象
conf = configparser.ConfigParser()

# 使用Config对象读取配置文件
conf.read("config.ini", encoding="utf-8")

# 读配置件文件信息
'''
options = conf.options("user"): 得到指定section的所有option（key）   # ['username', 'password', 'email']

useritem = conf.items("user"): 得到所有指定section的所有键值对（列表形式），键值对是以元组的形式返回的  
# [('username', 'tom'), ('password', '***'), ('email', 'test@host.com')]

str_val = conf.get("book", "bookname")  # 获取 str 类型的值
int_val = conf.getint("book", "bookprice")  # 获取 int 类型的值

# conf.getboolean() # 获取 bool 类型
# conf.getfloat()   # 获取 float 类型
'''


# 以列表的形式返回所有的section
sections = conf.sections()
print(sections)  # ['user', 'book']

# 得到指定section的所有option（key）
options = conf.options("user")
print(options)  # ['username', 'password', 'email']

# 得到所有指定section的所有键值对（列表形式），键值对是以元组的形式返回的
useritem = conf.items("user")
print(useritem)  # [('username', 'tom'), ('password', '***'), ('email', 'test@host.com')]

str_val = conf.get("book", "bookname")  # 获取 str 类型的值
int_val = conf.getint("book", "bookprice")  # 获取 int 类型的值
# conf.getboolean() # 获取 bool 类型
# conf.getfloat()   # 获取 float 类型
print(str_val)  # python    （str 类型）
print(int_val)  # 25        （int 类型）


# 写配置文件
'''
conf.add_section("book"): 如果文件内有这个就不能再添加了，否则会报错
conf.set("book", "bookprice", "25"): 设置必须设置 str 类型的值，如果存在 option 就更新值，不存在就创建
conf.write(open("config.ini", "w", encoding="utf-8")): 最后写入的时候打开一个文件，并且最好指定编码
conf.remove_option("book", "bookpress"): 不存在不会报错
conf.remove_section("purchasecar"): 移除指定section
'''

# 增加新的section
# conf.add_section("book")

# # 增加指定 section 的 option 和值
# conf.set("book", "bookname", "python learning")
# # 增加指定 section 的 option 和值
# conf.set("book", "bookprice", "25")
# # 增加指定 section 的 option 和值
# conf.set("book", "bookpress", "人民邮电出版社")

# 移除指定 section 的 option
conf.remove_option("book", "bookpress")

# 移除指定 section，会将之对应的所有数据也移除了
conf.remove_section("purchasecar")

# 将配置写入配置文件
conf.write(open("config.ini", "w", encoding="utf-8"))
