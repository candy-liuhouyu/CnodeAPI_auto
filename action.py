import os

import pytest

# 基础路由(方便在部署环境发生变化时切换全局基础路由)
BASE_URL = "https://cnodejs.org/api/v1/"

# 获取脚本的绝对路径(脚本在项目根目录就可以理解为项目路径)
ABS_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(ABS_PATH)

# 命令行启动此脚本时执行测试用例
# pytest.main(["testcase/"])

if __name__ == '__main__':
    print(ABS_PATH)
    print(BASE_URL)