import subprocess
from process import run_bash

CRONTAB = '/home/pi/ascetic/asagao/crontab.txt'

cmd = 'env | grep SSH_AUTH_SOCK'
out, err = run_bash(cmd)
assert err == ''

with open(CRONTAB, 'r') as f:
    lines = f.readlines()

crontab = ''
for i, line in enumerate(lines):
    if not i:
        crontab += out
    else:
        crontab += line

with open(CRONTAB, 'w') as f:
    f.write(crontab)

cmd = 'crontab {}'.format(CRONTAB)
out, err = run_bash(cmd)
assert err == ''

print('rewrite crontab.')
