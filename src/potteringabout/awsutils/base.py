import boto3
from potteringabout.awsutils.account import Account

auth = Account()

class Base(object):
  """
  Base class for all our clients to extend
  
  Raises:
      NotImplementedError: All subclasses must define the awstype variable which determines the underlying aws client the class will create.
  """

  @property
  def resources(self):
    raise NotImplementedError
  
  @property
  def clients(self):
    raise NotImplementedError

  @classmethod
  def run(cls, accounts, role, func_name, **kwargs):
    response = []
    for account in accounts:
      o=cls(account=account["Id"], role=role)
      if hasattr(o, func_name) and callable(getattr(o, func_name)):
        f = getattr(o, func_name)
        r = f(**kwargs)
        response.append({"accountId": account["Id"], "response": r})  
    return response

  def __init__(self, account=None, role=None):
    self.c = {}
    self.r = {}
    if account:
      print("Account set to [" + account + "]")
      self.c = {}
      for client in self.clients:
        self.c[client] = self.credentials = auth.client(accountId=account, rtype=client, role=role)
      self.r = {}
      for resource in self.resources:
        self.r[resource] = self.credentials = auth.resource(accountId=account, rtype=resource, role=role)
    else:
      for client in self.clients:
        self.c[client] = boto3.client(client)
      for resource in self.resources:
        self.r[resource] = boto3.resource(resource)

  def client(self, name):
    return self.c[name]
  
  def resource(self, name):
    return self.r[name]

  def iterate(self, cr, func_name, attr, nextToken="NextToken", **kwargs):
    if hasattr(cr, func_name) and callable(getattr(cr, func_name)):
      f = getattr(cr, func_name)
      response = f(**kwargs)
      obs = response[attr]
      while nextToken in response:
        kwargs.update({nextToken: response[nextToken]})
        response = f(**kwargs)
        obs.extend(response[attr]) 
      return obs
    raise Exception("Object does not have callable function [%s]".format(func_name))

