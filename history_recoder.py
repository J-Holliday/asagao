import glob
import os
import subprocess


TMP_DIR = '/var/www/html/tmp/'
DEST_DIR = 'iida@alpha.c.dendai.ac.jp:asagao/history'


files = glob.glob(TMP_DIR + '*')

if len(files) > 0:
    print('start scp...')
    for f in files:
        # call wait own subprocess, then don't use Popen
        subprocess.call(['scp', '{}'.format(f), DEST_DIR])
    print('removing tmp directory...')
    # In using wildcard, use string command and shell=True
    subprocess.call('sudo rm ' + TMP_DIR + '*', shell=True)
    print('finish all process.')
else:
    print('no img file.')
