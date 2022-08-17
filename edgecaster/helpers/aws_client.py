from botocore.config import Config
import boto3
import os
import json, boto3, sys, uuid
import logging

# from urllib.parse import unquote_plus

retryConfig = Config(retries={"max_attempts": 2, "mode": "standard"})

log = logging.getLogger()


def new_aws_client(service, customer_key, region, arn):
    log.info(f"AWS CONFIG IN AWS CLIENT {service} ")
    credentials = sts_client(customer_key, arn)
    client = boto3.client(
        service_name=service,
        aws_access_key_id=credentials["AccessKeyId"],
        aws_secret_access_key=credentials["SecretAccessKey"],
        aws_session_token=credentials["SessionToken"],
        region_name=region,
        config=retryConfig,
    )
    return client


def sts_client(customer_key, arn):  # External ID is the Customer key in Django
    # create an STS client object that represents a live connection to the
    # STS service
    log.info(f"Calling STS Client : \n {customer_key}")
    sts_client = boto3.client("sts")

    # Call the assume_role method of the STSConnection object and pass the role
    # ARN and a role session name.
    # customer = Customer.objects.get(key=external_id)

    assumed_role_object = sts_client.assume_role(
        RoleArn=arn,
        RoleSessionName="AssumeRoleSession1",
        ExternalId=customer_key,
    )

    # From the response that contains the assumed role, get the temporary
    # credentials that can be used to make subsequent API calls

    credentials = assumed_role_object["Credentials"]
    log.info(credentials)
    return credentials
