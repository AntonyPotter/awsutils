#!/usr/bin/env python3
 
from potteringabout.awsutils.certs import Certs
from potteringabout.awsutils.org import Org
import yaml


  
if __name__ == "__main__":
  
  with open("accounts.yml", 'r') as stream:
    config = yaml.safe_load(stream)

  org = Org(account=str(config["org"]["account"]), role=config["org"]["assumed_role"])
  filter = config["account"]["filter"] if "filter" in config["account"] else None 
  exclude_filter = config["account"]["exclude_filter"] if "exclude_filter" in config["account"] else None 

  accounts = org.accounts(include_filter=filter, exclude_filter=exclude_filter)

  response = Certs.run(accounts=accounts, role=config["account"]["assumed_role"], func_name="list_certificates")
  
  print(response)


  
  