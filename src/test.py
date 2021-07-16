#!/usr/bin/env python3
 
from potteringabout.awsutils.certs import Certs
from potteringabout.awsutils.network import Network
from potteringabout.awsutils.org import Org
import sys, inspect

def x(**kwargs):
  print(kwargs)

def iterate(**kwargs):
  kwargs.update({"nextToken": "1"})
  x(**kwargs)

def print_classes():
  clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
  for name, obj in clsmembers:
    if inspect.isclass(obj):
      print(obj)
  
if __name__ == "__main__":
  #client = Certs()
  #print(client.list_certificates())
  #print(client.list_client_certificates())
  #client.test()
  #iterate(a="a", b="b")
  #client = Network()
  #print(client.list_vpcs())
  #print(client.list_subnets())
  #all(Network)
  
  o = Org(account="559932348314", role="OrganizationReadOnly")
  #print(o.accounts)
  #r = o.run(cls="Network", role="Infra-Builder", func_name="list_vpcs")
  #r = o.run(cls="Network", role="Infra-Builder", func_name="list_vpcs")
  #print(r)
  #Network.run(accounts=o.accounts(filter={"Name":"Zaptic Dev"}), role="Infra-Builder", func_name="list_vpcs")
  Certs.run(accounts=o.accounts(filter={"Name":"Zaptic Dev"}), role="Infra-Builder", func_name="list_certificates")
  #print_classes()
  
  