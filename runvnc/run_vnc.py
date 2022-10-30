# -*- coding: utf-8 -*-

import subprocess
x0 = r'C:\Program Files\TightVNC\tvnviewer.exe -optionsfile=d:\\' 


def runvnc(addr):
    x1 = addr+r
    proc = subprocess.Popen(x0+x1)
    #proc = subprocess.Popen("ping -c2 %s" % ip, shell=True, stdout=subprocess.PIPE)