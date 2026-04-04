# Prerequisites

> Before you install the AWS Command Line Interface version 2 on your system you need an AWS account and IAM credentials.

**Source:** https://docs.aws.amazon.com/cli/latest/userguide/getting-started-prereqs.html

---

# Prerequisites to use the AWS CLI version 2

To access AWS services with the AWS CLI, you need an AWS account with IAM or IAM Identity Center credentials.
        When running AWS CLI commands, the AWS CLI needs to have access to those AWS credentials.  To
        increase the security of your AWS account, we recommend that you only use short-lived credentials 
        when using root or IAM users. You should create a user with least privilege to provide access
        credentials to the tasks you'll be running in AWS. For information about best practices, see 
        [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-users-federation-idp) 
        in the IAM User Guide. 

###### Topics

- 
[Create an IAM or IAM Identity Center administrative account](#getting-started-prereqs-iam)

- 
[Next steps](#getting-started-prereqs-next)

## Create an IAM or IAM Identity Center administrative account

Before you can configure the AWS CLI, you need to create an IAM or IAM Identity Center
            account.

Account creation options
                    
                        Choose a way to manage your credentials
                        To
                        How to create an account
                        How to configure programmatic access to the account

                        AWS Management Console credentials
                        Use short-term credentials corresponding to the root user created during initial account set up, an IAM user, or a federated identity from your identity provider.
                        Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup) and follow the online instructions.
                        No additional steps are necessary. To sign in to the AWS CLI with your AWS account, see [Login for AWS local development using console credentials](./cli-configure-sign-in.html)

                        IAM Identity Center
                        Use short-term credentials to access AWS services.
                        Following the instructions in Getting started in the AWS IAM Identity Center User Guide.
                        Configure programmatic access by Configuring the to use in the AWS IAM Identity Center User Guide.

                        AWS Identity and Access Management
(Not recommended)

                        Use long-term credentials to access AWS services.
                        Following the instructions in Create an for emergency access in the IAM User Guide.
                        Configure programmatic access by Manage access keys for users in the IAM User Guide.

## Next steps

After creating an AWS account and IAM credentials, to use the AWS CLI you can do one
            of the following: 

- 
                
[Install the latest release](./getting-started-install.html) of
                    the AWS CLI version 2 on your computer.

- 
        
[Install a past release](./getting-started-version.html) of the AWS CLI version 2 on your
          computer.

- 
                
Access the AWS CLI version 2 from your computer [using a Docker image.](./getting-started-docker.html)

- 
                
Access the AWS CLI version 2 in the AWS console from your browser using AWS CloudShell. For
                    more information see the [AWS CloudShell User Guide](https://docs.aws.amazon.com/cloudshell/latest/userguide/).

 **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Get started

Install/Update