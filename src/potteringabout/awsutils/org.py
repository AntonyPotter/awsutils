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
  accounts = []

  def __init__(self, account=None, role=None, filter=None):
    super().__init__(account=account, role=role)
    accounts = self.iterate(
      cr=self.client("organizations"),
      func_name="list_accounts",
      attr="Accounts"
    )
    if filter:
      for account in accounts:
        for f in filter:
          p = re.compile(filter[f])
          if p.match(account[f]):
            self.accounts.append(account)
    else:
      self.accounts = accounts
  
  def print_classes(self):
    clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)

    for name, obj in clsmembers:
      if inspect.isclass(obj):
        print(obj)
        
  def run(self, cls, role, func_name, pkg=__package__, **kwargs):
    response = []
    '''module = importlib.import_module(pkg)
    clsmembers = inspect.getmembers(sys.modules[__package__], inspect.isclass)
    cls_ = getattr(module, cls)'''
    
    cls_ = getattr(pkg + '.' + cls.lower(), cls)
    for account in self.accounts:
      instance = cls_(account=account["Id"], role=role)
      if hasattr(instance, func_name) and callable(getattr(instance, func_name)):
        f = getattr(instance, func_name)
        r = f(**kwargs)
        response.append({"accountId": account["Id"], "response": r})  
    return response
    
