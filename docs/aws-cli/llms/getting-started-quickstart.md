# Setup

> Learn how to quickly configure basic settings that the AWS Command Line Interface uses to interact with your resources on AWS services.

**Source:** https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html

---

# Setting up the AWS CLI

This topic explains how to quickly configure basic settings that the AWS Command Line Interface (AWS CLI)
        uses to interact with AWS. These include your security credentials, the default output
        format, and the default AWS Region.

###### Topics

- 
[Gather your credential information for
                programmatic access](#getting-started-prereqs-keys)

- 
[Setting up new configuration and
                credentials](#getting-started-quickstart-new)

- 
[Using existing configuration and
                credentials files](#getting-started-quickstart-existing)

## Gather your credential information for
                programmatic access

You'll need programmatic access if you want to interact with AWS outside of the
            AWS Management Console. For authentication and credential instructions, choose one of the following
            options:

        Authentication type
        Purpose
        Instructions

AWS Management Console credentials

**(Recommended)**Use short-term credentials by logging into the
            AWS CLI with your console credentials. Recommended if you use root, IAM users, or
            federation with IAM for AWS account access

        [Login for AWS local development using console credentials](./cli-configure-sign-in.html)

IAM Identity Center
            workforce users short-term credentials

        Use short-term credentials for an
          IAM Identity Center workforce user.
Security best practice is to use AWS Organizations with IAM Identity Center. It
            combines short-term credentials with a user directory, such as the built-in IAM Identity Center
            directory or Active Directory.

        [Configuring IAM Identity Center authentication with the AWS CLI](./cli-configure-sso.html)

        IAM user short-term credentials
        Use IAM user short-term credentials, which are more secure than long-term
          credentials. If your credentials are compromised, there is a limited time they can be used
          before they expire.
        [Authenticating with short-term credentials
            for the AWS CLI](./cli-authentication-short-term.html)

        IAM or
            IAM Identity Center users on an Amazon EC2 instance. 
        Use Amazon EC2 instance metadata to query for temporary credentials using the role
          assigned to the Amazon EC2 instance.
        [Using Amazon EC2 instance metadata as credentials in the
            AWS CLI](./cli-configure-metadata.html)

        Assume roles for permissions
        Pair another credential method and assume a role for temporary access to
          AWS services your user might not have access to.
        [Using an IAM role in the AWS CLI](./cli-configure-role.html)

        IAM user long-term credentials
        **(Not recommended)** Use long-term credentials, which
          have no expiration.
        [Authenticating using IAM user credentials for
            the AWS CLI](./cli-authentication-user.html)

        External storage of IAM or
            IAM Identity Center workforce users 
        
        **(Not recommended)** Pair another credential method but
          store credential values in a location outside of the AWS CLI. This method is only as secure
          as the external location the credentials are stored.
        [Sourcing credentials with an external
            process in the AWS CLI](./cli-configure-sourcing-external.html)

## Setting up new configuration and
                credentials

The AWS CLI stores your configuration and credential information in a *profile* (a collection of settings) in the
                `credentials` and `config` files. 

###### There are primarily two methods to quickly get setup:

- 
[Configuring using AWS CLI
                    commands](#getting-started-quickstart-new-command)

- 
[Manually editing the
                    credentials and config files](#getting-started-quickstart-new-file)

The following examples use sample values for each of the authentication methods.
            Replace sample values with your own.

### Configuring using AWS CLI
                    commands

For general use, the `aws configure` or `aws configure sso`
                commands in your preferred terminal are the fastest way to set up your AWS CLI
                installation. Based on the credential method you prefer, the AWS CLI prompts you for
                the relevant information. By default, the information in this profile is used when
                you run an AWS CLI command that doesn't explicitly specify a profile to use.

For more information on the `credentials` and
                    `config` files, see [Configuration and credential file settings in the
            AWS CLI](./cli-configure-files.html).

For more detailed information on authentication and credential methods see [Authentication and access credentials for the
      AWS CLI](./cli-chap-authentication.html).

### Manually editing the
                    credentials and config files

When copy and pasting information, we suggest manually editing the
                    `config` and `credentials` file. Based on
                the credential method you prefer, the files are setup in a different way.  

The files are stored in your home directory under the `.aws`
                folder. Where you find your home directory location varies based on the operating
                system, but is referred to using the environment variables
                    `%UserProfile%` in Windows and `$HOME` or `~`
                (tilde) in Unix-based systems. For more information on where these settings are
                stored, see [Where are configuration settings
                stored?](./cli-configure-files.html#cli-configure-files-where).

The following examples show a `default` profile and a profile named
                    `user1` and use sample values. Replace sample values with your own.
                For more information on the `credentials` and
                    `config` files, see [Configuration and credential file settings in the
            AWS CLI](./cli-configure-files.html).

For more detailed information on authentication and credential methods see [Authentication and access credentials for the
      AWS CLI](./cli-chap-authentication.html).

## Using existing configuration and
                credentials files

If you have existing configuration and credentials files, these can be used for the
            AWS CLI. 

To use the `config` and `credentials` files,
            move them to the folder named `.aws` in your home directory. Where you find
            your home directory location varies based on the operating system, but is referred to
            using the environment variables `%UserProfile%` in Windows and
                `$HOME` or `~` (tilde) in Unix-based systems. 

You can specify a non-default location for the `config` and
                `credentials` files by setting the `AWS_CONFIG_FILE`
            and `AWS_SHARED_CREDENTIALS_FILE` environment variables to another local
            path. See [Configuring environment variables for the
            AWS CLI](./cli-configure-envvars.html)
            for details. 

For more detailed information on configuration and credentials files, see [Configuration and credential file settings in the
            AWS CLI](./cli-configure-files.html).

 **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Amazon ECR Public/Docker

Configure the AWS CLI