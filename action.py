import os

import pytest

# 基础路由(方便在部署环境发生变化时切换全局基础路由)
BASE_URL = "https://cnodejs.org/api/v1/"

# 获取脚本的绝对路径(脚本在项目根目录就可以理解为项目路径)
ABS_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(ABS_PATH)

Token = "97463aec-1aef-4561-b054-a980cc1a9a1b"

# 收藏和取消收藏的贴子id
collect_topic_id = "6100f54de3e67140e158fe63"

# 查找用户收藏的所有主题& 查询用户详情
username = "thonatos"

# 要评论的贴子id
view_post_tid = "612494e0fe0c5136ceae6e4c"

# 点赞id
# up_id = "5fdb4a8a0f99cbc8325e341e"

# 命令行启动此脚本时执行测试用例
# pytest.main(["testcase/"])

if __name__ == '__main__':
    print(ABS_PATH)
    print(BASE_URL)