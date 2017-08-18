import subprocess


def run_bash(command):
    p = subprocess.Popen(command, shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    out = ''.join([so.decode('utf-8') for so in p.stdout.readlines()])
    err = ''.join([se.decode('utf-8') for se in p.stderr.readlines()])
    return (out, err)
