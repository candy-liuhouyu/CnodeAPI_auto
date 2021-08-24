# -*- coding:utf-8 -*-

"""
@Author : candy_liu
@Contact :candy_liuhouyu@163.com
@Date : 2021/08/19 18:34
@Desc :接口模板，将测试的接口全都封装在此文件内，并定义请求参数等内容
"""

import json
import requests
import action

api_create_topic = action.BASE_URL + "topics"
api_edit_topic = action.BASE_URL + "topics/update"
api_query_home = action.BASE_URL + "topics"
api_query_topic = action.BASE_URL + "topic/"
api_collect_topic = action.BASE_URL + "topic_collect/collect"
api_de_collect_topic = action.BASE_URL + "topic_collect/de_collect"
api_collect_all = action.BASE_URL + "topic_collect/"
api_create_view = action.BASE_URL + "topic/:topic_id/replies"
api_query_user = action.BASE_URL + "user/"
api_query_message = action.BASE_URL + "messages"
api_no_msg_count = action.BASE_URL + "message/count"


# 接口实现
def create_topic(test_data):
    """
    创建主题接口
    :param test_data:
    :return:
    """
    r = requests.post(api_create_topic, json=test_data)
    return r


def query_tid_detail(tid):
    """
    查询贴子详情信息
    :param tid:
    :return:
    """
    r = requests.get(api_query_topic + tid)
    return r


def query_home_index(para_data):
    """
    查询主题首页数据
    :param para_data: 请求参数
    :return:
    """
    r = requests.get(api_query_home, params=para_data)
    return r


def update_topic(e_data):
    """
    修改主题信息
    :param e_data:
    :return:
    """
    r = requests.post(api_edit_topic, e_data)
    return r


def collect_topic(param_data):
    """
    收藏贴子
    :param param_data:
    :return:
    """
    r = requests.post(api_collect_topic, param_data)
    return r


def de_collect(param_data):
    """
    取消收藏贴子
    :param param_data:
    :return:
    """
    r = requests.post(api_de_collect_topic, param_data)
    return r


def collect_all(user_name):
    """
    查询用户收藏的所有贴子
    :param user_name:
    :return:
    """
    r = requests.get(api_collect_all + user_name)
    return r


def add_review(tid, param_data):
    """
    创建评论和回复
    :param tid:
    :param param_data:
    :return:
    """
    r = requests.post(action.BASE_URL + "topic/" + tid + "/replies", param_data)
    return r


def raise_reply(view_id, param_data):
    """
    点赞评论
    :param view_id:
    :param param_data:
    :return:
    """
    r = requests.post(action.BASE_URL + "reply/" + view_id + "/ups", param_data)
    return r


def query_user(username):
    """
    查询用户
    :param username:
    :return:
    """
    r = requests.get(api_query_user, username)
    return r


def query_no_read_message(param):
    """
    查询未读消息数
    :return:
    """
    r = requests.get(api_no_msg_count, param)
    return r


def query_message(param_data):
    """
    查询所有已读和未读消息
    :param param_data:
    :return:
    """
    r = requests.get(api_query_message, param_data)
    return r
