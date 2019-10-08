#!/usr/bin/python3
# -*- coding: utf-8 -*-

import string
import os,time
import hashlib

def file_time(path):
     
    file_name=path
 
    file_times_access=time.localtime(os.path.getatime(file_name)) #总时间戳
    year_access=file_times_access.tm_year  #年
    month_access=file_times_access.tm_mon  #月
    day_access=file_times_access.tm_mday   #日
 
    hour_access=file_times_access.tm_hour  #小时
    minute_access=file_times_access.tm_min #分
    second_access=file_times_access.tm_sec  #秒

    filetime = ("%s/%s/%s %s:%s:%s"%(year_access,month_access,day_access,hour_access,minute_access,second_access))
    return filetime
   

drive_list = []  # 存放磁盘分区列表

for c in string.ascii_uppercase:
    drive = c + ":\\"
    if os.path.isdir(drive):
        drive_list.append(drive)

print(drive_list)
md5_list = []
path_list = []
for root, dirs, files in os.walk("D:\\"):
    for f in files:
        if f[-4:].lower() in (".txt",".exe",".mp3",".mp4",".jpg",".gif","png",".doc",".xsl"):
        #if f[-4:].lower() == ".txt":
            dest_file_path = os.path.join(root, f)

            m = hashlib.md5()

            with open(dest_file_path, "rb") as f:
                data = f.read()

            m.update(data)

            md5_value = m.hexdigest()  # 消息散列
            
            path_list.append(dest_file_path)
            
            md5_list.append(md5_value)
           

          
            #print(dest_file_path, md5_value)
            # os.remove(dest_file_path)


b = []
for i in md5_list:
    if i not in b:
        b.append(i)
            
CF_list = []
for i in range(len(b)):
    CF_list.append([])

a = 0
for s in b:
    for item in enumerate(md5_list):
        if item[1] == s:
            CF_list[a].append(item[0])
    if len(CF_list[a]) > 1:
        print("检测到以下重复文件，请问是否删除\n")
        for i in range(len(CF_list[a])):
           # print(path_list[CF_list[a][i]],file_time(path_list[CF_list[a][i]]),CF_list[a])
            print(path_list[CF_list[a][i]],file_time(path_list[CF_list[a][i]]))
        
        t = input("\n输入Y确认删除,N取消\n")
        if t == "Y":
            for i in range(1,len(CF_list[a])):
                os.remove(path_list[CF_list[a][i]])
        elif t == "N":
            pass
        
    a += 1

    
    
