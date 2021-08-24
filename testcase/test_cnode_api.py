# -*- coding:utf-8 -*-

"""
@Author : candy_liu
@Contact :candy_liuhouyu@163.com
@Date : 2021/08/24 18:34
@Desc :接口测试用例
"""

import pytest

import action
import business.cnode_api as api
from common.get_log import GetLog
from common.read_json import load_json


log = GetLog.get_log()
token = action.Token

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
        "accesstoken": token,
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


def test_collect_de_topic():
    """
    收藏主题/取消收藏
    :return:
    """
    tid = action.collect_topic_id
    para_data = {
        "accesstoken": token,
        "topic_id": tid
    }
    # 收藏贴子
    res = api.collect_topic(para_data)
    print(res.json())
    log.info("收藏贴子-状态码为: {}".format(res.status_code))
    log.info("收藏贴子-success为: {}".format(res.json()["success"]))
    assert res.json()["success"] == True
    assert res.status_code == 200

    # 取消收藏
    de_re = api.de_collect(para_data)
    print(de_re.json())
    log.info("取消收藏贴子-状态码为: {}".format(de_re.status_code))
    log.info("取消收藏贴子-success为: {}".format(de_re.json()["success"]))
    assert de_re.json()["success"] == True
    assert de_re.status_code == 200


def test_query_collect_all():
    """
    查询用户收藏的所有贴子
    :return:
    """
    # 要查的用户收藏的所有主题
    user = action.username
    res = api.collect_all(user)
    print(res.status_code)
    log.info("收藏的所有贴子-状态码为: {}".format(res.status_code))
    assert res.status_code == 200


def test_view_reply():
    """
    新建贴子评论，以及评论回复
    :return:
    """
    tid = action.view_post_tid
    view_para = {
        "accesstoken": token,
        "content": "hello hello test",
        "reply_id": ""
    }
    # 评论贴子接口调用
    res = api.add_review(tid, view_para)
    print(res.json())
    log.info("评论贴子-状态码为: {}".format(res.status_code))
    log.info("评论贴子-评论id为: {}".format(res.json()["reply_id"]))
    assert res.status_code == 200
    assert res.json()["success"] == True

    # 获取评论的id
    view_id = res.json()["reply_id"]

    # 回复评论参数
    reply_para = {
        "accesstoken": token,
        "content": "hello hello view",
        "reply_id": view_id
    }
    # 回复评论接口调用
    re_r = api.add_review(tid, reply_para)
    print(re_r.json())
    log.info("回复评论-状态码为: {}".format(re_r.status_code))
    log.info("回复评论-回复的id为: {}".format(re_r.json()["reply_id"]))
    assert re_r.status_code == 200
    assert re_r.json()["success"] == True


def test_raise_reply():
    """
    点赞评论，不能为自己点赞
    :return:
    """
    reply_id = "5fdb4a8a0f99cbc8325e341e"
    up_para = {
        "accesstoken": token
    }
    up_r = api.raise_reply(reply_id, up_para)
    print(up_r.json())
    log.info("点赞-状态码为: {}".format(up_r.status_code))
    log.info("点赞-状态为(up--赞 or down--取消赞): {}".format(up_r.json()["action"]))
    # 取消赞
    up_r = api.raise_reply(reply_id, up_para)
    log.info("点赞-状态为(up--赞 or down--取消赞): {}".format(up_r.json()["action"]))
    assert up_r.status_code == 200
    assert up_r.json()["success"] == True


def test_query_no_msg_count():
    """
    查询未读消息数
    :return:
    """
    para = {
        "accesstoken": token
    }
    res = api.query_no_read_message(para)
    print(res.json())
    log.info("未读消息-状态码为: {}".format(res.status_code))
    log.info("未读消息-未读消息数量为: {}".format(res.json()["data"]))
    assert res.status_code == 200
    assert res.json()["success"] == True


def test_query_message():
    """
    查询所有已读和未读消息
    :return:
    """
    para = {
        "accesstoken": token,
        "mdrender": "false"
    }
    res = api.query_message(para)
    print(res.json())
    log.info("系统消息-状态码为: {}".format(res.status_code))
    log.info("系统消息-消息类型为: {}".format(res.json()["data"]))
    assert res.status_code == 200
    assert res.json()["success"] == True


if __name__ == '__main__':
    pass
    # print(test_data)
    # print(test_data["topic_id"])