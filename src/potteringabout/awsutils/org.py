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
  
  def accounts(self, include_filter=None, exclude_filter=None):
    accounts = []
    if not include_filter and not exclude_filter:
      return self.__accounts

    if include_filter:
      for account in self.__accounts:
        for fs in include_filter:
          for f in include_filter[fs]:
            p = re.compile(f)
            if p.match(account[fs]):
              accounts.append(account)
    if exclude_filter:
      for fs in exclude_filter:
        for f in exclude_filter[fs]:
          p = re.compile(f)
          accounts = [i for i in accounts if not p.match(i[fs])]

    return accounts
