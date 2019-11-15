from __future__ import print_function
import numpy as np
import time
from env import Env        #定义的贪婪函数
from reprint import output


EPSILON = 0.1
ALPHA = 0.1
GAMMA = 0.9
MAX_STEP = 30

np.random.seed(0)    #每次运行代码时设置相同的seed，则每次生成的随机数也相同


def epsilon_greedy(Q, state):     #epsilon 贪婪策略
    #在基于当前的 Q 值估计得出的状态 s 下选择一个动作 a
    #np.random.uniform()返回0-1之间的随机数
    #
    if (np.random.uniform() > 1 - EPSILON) or ((Q[state, :] == 0).all()):#如果这个数大于 epsilon，或者此state每列都有q值的话，那么我们将会进行「利用」
        action = np.random.randint(0, 4)  # 0~3随机整数（探索）
    else:
        action = Q[state, :].argmax() #返回Q值最大的（利用）
    return action


e = Env()
Q = np.zeros((e.state_num, 4))#step 1：初始化Q矩阵

with output(output_type="list", initial_len=len(e.map), interval=0) as output_list:
    for i in range(100):
        e = Env()
        while (e.is_end is False) and (e.step < MAX_STEP):#step 2：小于最大步长时（或者直到训练被中止前），步骤 3 到步骤 5 会一直被重复。
            action = epsilon_greedy(Q, e.present_state)#step 3:选取下一个动作 a
            state = e.present_state#step 4：跟新当前的state与跟新当前的reward
            reward = e.interact(action)
            new_state = e.present_state
            Q[state, action] = (1 - ALPHA) * Q[state, action] + \
                ALPHA * (reward + GAMMA * Q[new_state, :].max()) #step 5：Bellman 方程跟新当前的q值
            e.print_map_with_reprint(output_list)
            time.sleep(0.1)
        for line_num in range(len(e.map)):
            if line_num == 0:
                output_list[0] = 'Episode:{} Total Step:{}, Total Reward:{}'.format(i, e.step, e.total_reward)
            else:
                output_list[line_num] = ''
        time.sleep(2)
