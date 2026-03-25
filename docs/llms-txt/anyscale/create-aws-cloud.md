# Source: https://docs.anyscale.com/admin/cloud/create-aws-cloud.md

# Deploy Anyscale on Amazon EC2

[View Markdown](/admin/cloud/create-aws-cloud.md)

## 1. Install Anyscale's python client package[​](#1-install-anyscales-python-client-package "Direct link to 1. Install Anyscale's python client package")

```
pip install -U anyscale
anyscale login # authenticate
```

## 2. Configure your Cloud Provider account[​](#2-configure-your-cloud-provider-account "Direct link to 2. Configure your Cloud Provider account")

Set up your AWS credentials locally if you haven't done it before (for more details see [the AWS configuration guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html#getting-started-quickstart-new-command)).

```
aws configure
```

note

Before you continue to the next step, make sure your AWS credentials have the following permissions ([learn more](/administration/cloud-deployment/manage-aws-cloud.md)):

* Launch EC2 instances in the AWS region you plan to use
* Manage these resources: VPC, subnets, Security Group, IAM, S3, and EFS

## 3. Create your Anyscale Cloud[​](#3-create-your-anyscale-cloud "Direct link to 3. Create your Anyscale Cloud")

Run the following command to create an Anyscale Cloud with the default configuration.

```
anyscale cloud setup
```

If you wish to use Terraform or customize other settings like VPC, follow [these instructions](/admin/cloud/configure-aws.md) in the documentation.

## 4. Verify your Anyscale Cloud[​](#4-verify-your-anyscale-cloud "Direct link to 4. Verify your Anyscale Cloud")

Run the following command to verify that your newly created Anyscale Cloud is fully functional and ready to use.

Cloud Namemy-aws-cloud

```
anyscale cloud verify --name <your_cloud_name>
```
