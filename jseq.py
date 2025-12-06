#!/usr/bin/env python
import os
import sys
sys.path.append("sibcommon")
sys.path.append("seqlib")
sys.path.append("Sequences")
import datetime

import random
import json
import argparse
import glob

import time
import signal

from debug import Debug
from specs import Specs

def usage():
  print ("usage:",sys.argv[0]," spec file")
  os._exit(-1)
  
  
class ServiceExit(Exception):
    """
    Custom exception which is used to trigger the clean exit
    of all running threads and the main program.
    """
    pass

def service_shutdown(signum, frame):
    Debug().p('Caught signal %d' % signum)
    raise ServiceExit
    
if __name__ == '__main__':
  pname = sys.argv[0]
  signal.signal(signal.SIGTERM, service_shutdown)
  signal.signal(signal.SIGINT, service_shutdown)
  print("%s at %s"%(pname,datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')))
  random.seed()
 
  os.environ['DISPLAY']=":0.0"
  os.chdir(os.path.dirname(sys.argv[0]))
  print(pname+" at "+datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))  
  parser = argparse.ArgumentParser()
  parser.add_argument('-s', '--spec', nargs=1, help='specify spec file', required=True )
  parser.add_argument('-g', '--goto', nargs=1, help='goto the label')
  
  args = parser.parse_args()
  specFile = args.spec[0]
  print ("using spec:",specFile)
  specs = Specs(specFile)
  
  if args.goto:
    goto = args.goto[0]
    print("goto",goto)
    
  Debug().enable(specs.s['debug'])