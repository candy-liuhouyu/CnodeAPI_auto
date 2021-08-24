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

test_data = load_json("D:/document/MyProject/data/topics.json")
log = GetLog.get_log()


def test_add_topic():
    data = {
        "accesstoken": "97463aec-1aef-4561-b054-a980cc1a9a1b",
        "title": " hjasfhjkafhakjh afddgt ",
        "tab": "dev",
        "content": "hejgtes 参gsfgsg数fgfdgdfgh化"
    }
    r = api.create_topic(data)
    print(r.json())
    log.info("添加功能-状态码为: {}".format(r.status_code))
    log.info("添加功能-是否生成topic_id: {}".format(r.json()["topic_id"]))

    # 断言状态码
    assert r.status_code == 200, "状态码断言"
    assert r.json()["success"] == True


@pytest.mark.parametrize("topic_data,code,msg", test_data)
def test_create_topic(topic_data, code, msg):
    print(topic_data, code, msg)
    r = api.create_topic(topic_data)
    # print(r.json())
    # 打印状态码日志信息
    log.info("添加功能-状态码为: {}".format(r.status_code))
    log.info("添加功能-是否生成topic_id: {}".format(r.json()["error_msg"]))
    # 断言状态码和error_msg
    assert r.status_code == code, "状态码断言"
    assert r.json()["error_msg"] == msg
