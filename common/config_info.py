# -*- coding:utf-8 -*-

"""
@File : get_header
@Author : candy_liu
@Contact :candy_liuhouyu@163.com
@Date : 2021/08/19 18:34
@Desc :获取请求头信息
"""

import json
import action
from common.get_log import GetLog

# 获取日志器
log = GetLog.get_log()


# 获取config.json配置文件中的请求头信息 原主待废弃
def get_header():
    try:
        with open(action.BASE_DIR + "/data/config.json", "r", encoding="utf-8") as f:
            result = json.load(f)  # 解析json数据
            return result["headers"]
    except Exception as ex:
        log.error(ex)


# 设置cookie为token，并写配置文件中   原主待废弃
def set_token(token):
    try:
        with open(action.BASE_DIR + "/data/config.json", "r", encoding="utf-8") as f:
            result = json.load(f)
            result['headers']['Cookie'] = token

        with open(action.BASE_DIR + "/data/config.json", "w", encoding="utf-8") as f:
            json.dump(result, f)
    except Exception as ex:
        log.error(ex)


# 新  设置配置文件
def set_config(key, value):
    try:
        with open(action.BASE_DIR + "/data/config.json", "r", encoding="utf-8") as f:
            result = json.load(f)
            result[key] = value

        with open(action.BASE_DIR + "/data/config.json", "w", encoding="utf-8") as f:
            json.dump(result, f)
    except Exception as ex:
        log.error(ex)


# 新 获取配置文件数据
def get_config(key):
    try:
        with open(action.BASE_DIR + "/data/config.json", "r", encoding="utf-8") as f:
            result = json.load(f)
            return result[key]
    except Exception as ex:
        log.error(ex)


def get_submenu(key_1, key_2):
    obj = get_config(key_1)
    if key_2 in key_1:
        return obj[key_2]
    else:
        return None


def set_submenu(key_1, key_2, value):
    obj = get_config(key_1)
    obj[key_2] = value
    set_config(key_1, obj)


if __name__ == '__main__':
    # header_data = get_header()
    # print(header_data)
    token = "Cookie"
    key_cookie = get_config(token)
    print(key_cookie)  # 变量传入函数之后被设置为了None
