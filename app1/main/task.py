# encoding: utf-8
# 业务函数与路由

import json
from addict import Dict
from . import main
from ..ansible_runner import runner
from ..my_websocket.websockets import *  # 从自定义的websockets文件中导入websocket函数，必须


@main.route('/listen_consul', methods=['GET', 'POST'])
def run_task():
    # 传入inventory路径
    ansible = MyRunner('./host', passwords='111111')  # 指定host文件
    # 获取服务器系统信息
    module_name = 'shell'
    module_args = 'cat /etc/redhat-release'
    # ansible.run('all', 'setup', "filter='ansible_mounts'") # 获取磁盘数据
    ansible.run('all', module_name, module_args)
    # 结果
    result = ansible.get_result()
    # 成功
    succ = result['success']
    # 失败
    failed = result['failed']
    # 不可达
    unreachable = result['unreachable']

    # 序列化为可访问的字典
    sdict = Dict(succ)
    print(sdict.keys())
    for ip in sdict.keys():
        print(sdict[ip].invocation.module_args._raw_params)

