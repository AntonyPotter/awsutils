import boto3
from potteringabout.awsutils.base import Base
from datetime import datetime

class Certs(Base):

  clients = ["acm", "apigateway"]
  resources = []

  def list_certificates(self):
    cert_summaries = self.iterate(
      cr=self.client("acm"),
      func_name="list_certificates",
      attr="CertificateSummaryList"
    )
    certs = []
    for cert_summary in cert_summaries:
      cert = self.client("acm").describe_certificate(
        CertificateArn=cert_summary["CertificateArn"]
      )["Certificate"]
      certs.append(cert)
    return certs

  def list_client_certificates(self):
    return self.iterate(
      cr=self.client("apigateway"),
      func_name="get_client_certificates", 
      attr="items", 
      nextToken="position"
    )

    

