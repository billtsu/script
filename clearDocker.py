# -*-coding = utf-8 -*-

import os
res = os.popen('docker image ls')
t = []
for i in res:
    if i.split()[2] == ('IMAGE'):continue
    t.append(i.split()[2])
sorted(t)
# print(' '.join(t))

t_s = 'docker image rm {}'.format(' '.join(t))
os.popen(t_s)
for i in t:
    t_s = 'docker image rm {} --force'.format(i)
    os.popen(t_s)
