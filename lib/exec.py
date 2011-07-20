import subprocess
import shlex
import datetime
import os
import time
import signal
import re

'''
__author__="David Busby"
__copyright__="David Busby <d.busby@saiweb.co.uk>, Psycle Interactive Limited <david.busby@psycle.com>"
__license__="GNU v3 + part 5d section 7: Redistribution/Reuse of this code is permitted under the GNU v3 license, as an additional term ALL code must carry the original Author(s) credit in comment form."
'''

def timeout_command(cmd,t):
    s = datetime.datetime.now()
    p = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while p.poll() is None:
        time.sleep(0.1)
        n = datetime.datetime.now()
        if (n - s).seconds > t:
            os.kill(p.pid, signal.SIGKILL)
            os.waitpid(-1, os.WNOHANG)
            return None
    return p.stdout.read()

def background_command(cmd):
    p = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return p
