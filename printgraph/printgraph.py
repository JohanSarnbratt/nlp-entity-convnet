import sys
sys.path.insert(0, '..')

#import baseWikipediaLinker

class baseEmpty(object):
  a = 0

baseModel = None
disable_convs = []
featureNames = None

#import exp_multi_conv_cosim

def test():
  global baseModel
  baseModel = baseEmpty

def printconv():
  global baseModel
  baseModel = baseEmpty
  import exp_multi_conv_cosim
  queries_exp = exp_multi_conv_cosim.queries_exp

