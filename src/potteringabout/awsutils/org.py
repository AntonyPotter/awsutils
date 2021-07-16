import boto3
from potteringabout.awsutils.base import Base
from datetime import datetime
import re
import sys
import inspect
import importlib

class Org(Base):

  clients = ["organizations"]
  resources = []
  __accounts = []

  def __init__(self, account=None, role=None):
    super().__init__(account=account, role=role)
    self.__accounts = self.iterate(
      cr=self.client("organizations"),
      func_name="list_accounts",
      attr="Accounts"
    )
  
  def accounts(self, filter=None):
    accounts = []
    if filter:
      for account in self.__accounts:
        for f in filter:
          p = re.compile(filter[f])
          if p.match(account[f]):
            accounts.append(account)
    else:
      accounts = self.__accounts
    return accounts
