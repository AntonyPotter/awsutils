#!/usr/bin/env python3
 
from potteringabout.awsutils.certs import Certs
from potteringabout.awsutils.org import Org
import yaml


  
if __name__ == "__main__":
  
  with open("accounts.yml", 'r') as stream:
    config = yaml.safe_load(stream)

  o = Org(account=str(config["org"]["account"]), role=config["org"]["assumed_role"])
  filter = config["account"]["filter"] if "filter" in config["account"] else None 
  Certs.run(accounts=o.accounts(filter=filter), role=config["account"]["assumed_role"], func_name="list_certificates")

  
  