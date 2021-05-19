import json
import os
import re

# with open('poppy_sheet.json') as f:
#     data = json.load(f)
# f.close()
#
# names = data['frames'].keys()
# for n in names:
#     print(n)
# print('\n')
# idle = [i for i in names if 'idle' in i]
# for i in idle:
#     print(i)
# print('\n')
# walk = [w for w in names if 'walk' in w]
# for w in walk:
#     print(w)
actions = ('idle', 'hit', 'win', 'lose', 'skill1', 'skill2', 'skill3', 'skill4')

path = 'H:/GitHub/MyDemoGame01/data/images/hero/sprite/Ragna/'
os.chdir(path)
lists = os.listdir()
files = [f for f in lists if f.endswith('json')]
for f in files:
    print(f)
print('\n')

sprite_names = []

for filename in files:
    with open(filename) as f:
        data = json.load(f)
    f.close()
    sprite_names = sprite_names + list(data['frames'].keys())

print(sprite_names)
print(len(sprite_names))

idle = sorted([i for i in sprite_names if 'skill1' in i])
print('skill1:')
for i in idle:
    print(i)
print('\n')
