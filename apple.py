#/usr/bin/env python
# -*- coding: utf-8 -*-  
from subprocess import Popen, PIPE

def run_scpt(scpt,args=[]):
    p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate(scpt)
    #print (stdout, stderr)
    return p.returncode

def keystroke(code):
    """
space 49
enter 52
left 123
up 126
down 125
right 124
    """
    scpt = """
        tell application "System Events" to keystroke (key code %s)
    """ % code
    ret = run_scpt(scpt)
    return ret


def active(app):
    scpt = """
    activate application "%s"
    """ % app
    ret = run_scpt(scpt)
    return ret
