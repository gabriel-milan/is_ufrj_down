from check_ufrj import *

def loop_check ():
  while True:
    res = ping_multiple(hosts)
    if (res):
      print ("We're back!")
    else:
      print ("Still down...")

if __name__ == '__main__':
  loop_check()
