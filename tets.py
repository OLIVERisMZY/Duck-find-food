from __future__ import print_function
import copy


MAP = \
    '''
.........
.       .
.     o .
.       .
.........
'''

# MAP = \
#     '''
# .........
# .  x    .
# .   x o .
# .       .
# .........
# '''
MAP = MAP.strip().split('\n')
print(MAP)
MAP = [[c for c in line] for line in MAP]
print(MAP)
print(len(MAP))
print(len(MAP[0]))