# -*- coding:utf-8 -*-

"""
@Author : candy_liu
@Contact :candy_liuhouyu@163.com
@Date : 2021/08/24 18:34
@Desc :接口测试用例
"""

import pytest
import business.cnode_api as api
from common.get_log import GetLog
from common.read_json import load_json


log = GetLog.get_log()


def test_update_topic():
    """
    修改贴子，直接传入贴子id进行修改
    :return:
    """
    test_data = load_json("D:/document/MyProject/data/e_data.json")
    res = api.update_topic(test_data)
    print(res.json())
    log.info("添加功能-状态码为: {}".format(res.status_code))
    log.info("添加功能-是否生成topic_id: {}".format(res.json()["topic_id"]))
    assert res.status_code == 200
    assert res.json()["topic_id"] == test_data["topic_id"]


def test_edit_topic():
    """
    编辑个帖子，调用修改接口前先新增贴子接口，将新增的贴子topic_id获取并拿出来作为修改贴子的变量tid
    :return:
    """
    c_data = load_json("D:/document/MyProject/data/c_topics.json")
    res = api.create_topic(c_data)
    print(res.json())
    log.info("添加功能-状态码为: {}".format(res.status_code))
    log.info("添加功能-success为: {}".format(res.json()["success"]))
    assert res.status_code == 200
    assert res.json()["success"] == True
    # 获取新增的贴子id
    tid = res.json()["topic_id"]
    e_data = {
        "accesstoken": "97463aec-1aef-4561-b054-a980cc1a9a1b",
        "topic_id": tid,
        "title": "test 2110 2021 08 24 edit post",
        "tab": "dev",
        "content": "2021 08 24 edit post height 参rrwghh souoruouehfjfjk 654数weight化"
    }
    e_re = api.update_topic(e_data)
    print(e_re.json())
    log.info("编辑功能-状态码为: {}".format(res.status_code))
    log.info("编辑功能-success为: {}".format(res.json()["success"]))
    assert res.status_code == 200
    assert res.json()["topic_id"] == tid





if __name__ == '__main__':
    pass
    # print(test_data)
    # print(test_data["topic_id"])