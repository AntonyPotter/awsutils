import boto3
from potteringabout.awsutils.base import Base
from datetime import datetime

class Network(Base):

  clients = ["ec2"]
  resources = []

  def list_subnets(self):
    return self.iterate(
      cr=self.client("ec2"), 
      func_name="describe_subnets",
      attr="Subnets"
    )

  def list_vpcs(self):
    return self.iterate(
      cr=self.client("ec2"),
      func_name="describe_vpcs", 
      attr="Vpcs"
    )