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

    SrcPath = os.path.join(opts['srcpath'],'*')
    # print(SrcPath)

    for file in glob.glob(SrcPath):
        print(file)
        csv_file = open(file,"r",encoding='utf-8')
    # df = pd.read_csv(csv_file)

        # csv_file = pd.read_csv(file,header=None)
        for data in csv_file:
            print(data)
            data = data.replace('\n','')
            data0 = data.split(",")[0]

            if data0 != "\"electric_at\"":
                re_data0 = data0.replace("/","-")
                re_data0 = re_data0.replace("\"","")
                print(re_data0)
                # t_date = dt.strptime(re_data0, '%Y-%m-%d %H:%M:%S')
                # print(t_data)
                # print(data.split(",")[0])
                # print(data.split(",")[1])
                # print(data.split(",")[2])
                sql = "INSERT INTO electric (electric_at,str_id,electric_kw) VALUES (%s, %s, %s)"
                cursor.execute(sql, (re_data0,data.split(",")[1],data.split(",")[2]))

        csv_file.close()
        mv_file = file.split("/")
        work_file = dt.now().strftime('%Y%m%d%H%M%S')+"-"+mv_file[2]
        print(work_file)
        work_path_file = os.path.join(opts['workpath'],work_file)
        print(work_path_file)
        shutil.move(file,work_path_file)
    # データベースから切断
    connect.commit()
    cursor.close()
    connect.close()

if __name__ == '__main__':
    main()
