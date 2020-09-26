import platform    # For getting the operating system name
import subprocess  # For executing a shell command
from multiprocessing import Pool

#
# Few hosts on UFRJ
#
hosts = [
  'if.ufrj.br',
  'im.ufrj.br',
  'cos.ufrj.br',
  'poli.ufrj.br',
  'nce.ufrj.br',
]

#
# `ping` extracted from https://stackoverflow.com/questions/2953462/pinging-servers-in-python
# * Added stdout suppress
#
def ping(host):
  """
  Returns True if host (str) responds to a ping request.
  Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
  """

  # Option for the number of packets as a function of
  param = '-n' if platform.system().lower()=='windows' else '-c'

  # Building the command. Ex: "ping -c 1 google.com"
  command = ['ping', param, '1', host]

  return subprocess.call(command, stdout=subprocess.DEVNULL) == 0

#
# Ping multiple hosts
#
def ping_multiple (hosts):
  """
  Returns True if one of the hosts (list of str) reponds to ping requests.
  Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
  """

  with Pool(len(hosts)) as p:
    results = p.map(ping, hosts)

  return any(results)

#
# Main
#
if __name__ == '__main__':
  print ("UFRJ is {}".format("UP" if ping_multiple(hosts) else "DOWN"))