
##############################################################
# 作成日：2018/05/29
# 作成者：戸田滉洋
#
# 更新日：2018/05/29
# 更新者：戸田滉洋
# Copyright © 2018 Flugell System Studio. All rights reserved.
##############################################################


#!/user/bin/python
# -*- coding: utf-8 -*-

import sys
import insert_main

def opts_read(cfg):
    opts = {}

    # セクション内の指定項目だけを取り込む。
    sect = "path"
    opts= dict(cfg.items(sect))
    return opts

def account_read(cfg):
    account = {}

    # セクション内の指定項目だけを取り込む。
    sect = "account"

    account = dict(cfg.items(sect))
    return account
