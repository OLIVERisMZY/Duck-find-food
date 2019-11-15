from __future__ import print_function
import copy


MAP = \
    '''
............
.          .
.       x  .
.          .
.          .
.   x      .
.x        o.
............
'''

# MAP = \
#............
#.          .
#.       x  .
#.          .
#.          .
#.   x      .
#.x        o.
#............
MAP = MAP.strip().split('\n')#map通过换行符进行划分['.........', '.       .', '.     o .', '.       .', '.........']
MAP = [[c for c in line] for line in MAP]
#map变成['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', ' '全是字符

DX = [-1, 1, 0, 0] #action有四种
DY = [0, 0, -1, 1]


class Env(object):
    def __init__(self):
        self.map = copy.deepcopy(MAP)#deepcopy 无论怎样改变map都不会影响
        self.x = 1
        self.y = 1
        self.step = 0
        self.total_reward = 0
        self.is_end = False

    def interact(self, action):#定义行动后的下一个位置
        assert self.is_end is False
        new_x = self.x + DX[action]#x轴方向移动
        new_y = self.y + DY[action]#y轴方向移动
        new_pos_char = self.map[new_x][new_y]#新的位置跟新
        self.step += 1#step+1
        if new_pos_char == '.':#到达边界处，reward定义为0
            reward = 0  # do not change position
        elif new_pos_char == ' ':#到达无宝藏处处，reward定义为0
            self.x = new_x
            self.y = new_y
            reward = 0
        elif new_pos_char == 'o':#到达宝藏处，结束学习，reward定义为100
            self.x = new_x
            self.y = new_y
            self.map[new_x][new_y] = ' '  # update map
            self.is_end = True  # end
            reward = 100
        elif new_pos_char == 'x':#到达危险处，reward定义为-5
            self.x = new_x
            self.y = new_y
            self.map[new_x][new_y] = ' '  # update map
            reward = -5
        self.total_reward += reward
        return reward

    @property
    def state_num(self):
        rows = len(self.map)#map的行数
        cols = len(self.map[0])#map的列数
        return rows * cols#map的全部元素值

    @property#返回当前位置
    def present_state(self):
        cols = len(self.map[0])
        return self.x * cols + self.y

    def print_map(self):#打印当前位置
        printed_map = copy.deepcopy(self.map)
        printed_map[self.x][self.y] = 'A'
        print('\n'.join([''.join([c for c in line]) for line in printed_map]))

    def print_map_with_reprint(self, output_list):
        printed_map = copy.deepcopy(self.map)
        printed_map[self.x][self.y] = 'A'
        printed_list = [''.join([c for c in line]) for line in printed_map]
        for i, line in enumerate(printed_list):
            output_list[i] = line
