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
