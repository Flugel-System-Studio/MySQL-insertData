###############################################################
# 作成日：2018/05/29
# 作成者：戸田滉洋
#
# 更新日：2018/08/14
# 更新者：戸田滉洋
# Copyright © 2018 Flugell System Studio. All rights reserved.
###############################################################

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ドライバをimport
import mysql.connector
import csv
import pandas as pd
import sys
import os
import glob
import configparser
import insert_config
import shutil
from datetime import datetime as dt

def main():
    # 設定ファイルをロード
    cfg = configparser.ConfigParser()
    conf = "db.cfg"
    config_path = os.path.join("../config",conf)
    # print(config_path)
    # print(os.path.isdir(config_path))
    cfg.read(config_path,encoding="utf-8")
    # print(cfg)
    cfg_opts = insert_config.opts_read(cfg)
    opts = cfg_opts
    # print(opts)
    cfg_account = insert_config.account_read(cfg)
    account = cfg_account
    # print(account)


# データベースに接続
connect = mysql.connector.connect(user=account['user'], password=account['pass'], host=account['host'], database='mietaro', charset='utf8')
cursor = connect.cursor()

# ファイル読み込み
SrcPath = os.path.join(opts['srcpath'],'*')
print(SrcPath)

# CSVデータから値を取得し、DBに値を挿入
for file in glob.glob(SrcPath):
    print(file)
    csv_file = open(file,"r",encoding='utf-8')
    for data in csv_file:
        data = data.replace('\n','')
        print(data.split(",")[0])
        print(data.split(",")[1])
        print(data.split(",")[2])
        if (issset(data.split(",")[3])){
            sql = "INSERT INTO electric (electric_at,str_id,electric_kw,damad_kw,electric_m) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (data.split(",")[0],data.split(",")[1],data.split(",")[2]),data.split(",")[3]),0)
        }else if (issset(data.split(",")[4])){
            sql = "INSERT INTO electric (electric_at,str_id,electric_kw,damad_kw,electric_m) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (data.split(",")[0],data.split(",")[1],data.split(",")[2]),data.split(",")[3],data.split(",")[4])
        }else{
            sql = "INSERT INTO electric (electric_at,str_id,electric_kw,damad_kw,electric_m) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (data.split(",")[0],data.split(",")[1],data.split(",")[2]),0,0)
        }
        print(data.split(",")[3])
        #sql = "INSERT INTO electric (electric_at,str_id,electric_kw,damad_kw) VALUES (%s, %s, %s,%s)"
        cursor.execute(sql, (data.split(",")[0],data.split(",")[1],data.split(",")[2]))

    csv_file.close()
    shutil.move(file,opts['workpath'])
# データベースから切断
connect.commit()
cursor.close()
connect.close()

if __name__ == '__main__':
main()
