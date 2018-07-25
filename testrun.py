#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import logging
import os
import getopt
import sys
import coverage



from utx import *
rootdir = os.path.join(os.path.dirname(os.path.realpath(__file__)),'test')
# rootdir = 'E:/unittest/backend'
print("rootdir=",rootdir)
os.chdir(rootdir)
if __name__ == '__main__':
    cov = coverage.Coverage()
    cov.start()
    kargs =  {'testName':'qdy@xkool.xyz','rootdir':rootdir}
    try:
        options,args = getopt.getopt(sys.argv[1:],"h:",["user=",'rootdir='])
    except getopt.GetoptError:
        print('error')
        sys.exit()
    for name,value in options:
        if name in ("--user"):
            kargs['testName'] = value
        elif name in ("--rootdir"):
            kargs['rootdir'] = value
    log.set_level(logging.DEBUG)
    print(kargs)
    runner = TestRunner(testName=kargs['testName'])
    runner.add_case_dir(kargs['rootdir'])
    runner.run_test()
    cov.stop()
    cov.save()
    cov.html_report(directory='report')
    #对文件进行打包