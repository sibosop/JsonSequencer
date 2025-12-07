#!/usr/bin/env python
import singleton
from track import Track
from seq import Seq
from tick import Tick

class Tune(Tick):
  __metaclass__ = singleton.Singleton
  seqList = []
  trackList = []
  def __init__(self,specs):
    self.name = "Tune"  
  
  def tick():
    return True
  