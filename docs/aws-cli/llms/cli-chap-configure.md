# Configure the AWS CLI

> Configure settings that the AWS CLI uses to interact with AWS.

**Source:** https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html

---

# Configuring settings for the AWS CLI

This section explains how to configure the settings that the AWS Command Line Interface (AWS CLI) uses to
        interact with AWS. These include the following:

- 
            
**Credentials** identify who is calling the API.
                Access credentials are used to encrypt the request to the AWS servers to confirm
                your identity and retrieve associated permissions policies. These permissions
                determine the actions you can perform. For information on setting up your
                credentials, see [Authentication and access credentials for the
      AWS CLI](./cli-chap-authentication.html).

- 
            
**Other configuration details** to tell the AWS CLI how
                to process requests, such as the default output format and the default AWS
                Region.

###### Note

AWS requires that all incoming requests are cryptographically signed. The AWS CLI does
            this for you. The "signature" includes a date/time stamp. Therefore, you must ensure
            that your computer's date and time are set correctly. If you don't, and the date/time in
            the signature is too far off of the date/time recognized by the AWS service, AWS
            rejects the request.

## Configuration and credentials precedence

Credentials and configuration settings are located in multiple places, such as the
            system or user environment variables, local AWS configuration files, or explicitly
            declared on the command line as a parameter. Certain locations take precedence over
            others. The AWS CLI credentials and configuration settings take precedence in the
            following order:

- 
    
**[Command line
        options](./cli-configure-options.html)** â Overrides settings in any other location, such as the
        `--region`, `--output`, and `--profile` parameters.

- 
    
**[Environment
        variables](./cli-configure-envvars.html)** â You can store values in your system's environment
      variables.

- 
    
**[Assume role](./cli-configure-role.html)**
      â Assume the permissions of an IAM role through configuration or the
        [`assume-role`](https://docs.aws.amazon.com/cli/latest/reference/sts/assume-role.html) command.

- 
    
**[Assume role with web
          identity](./cli-configure-role.html)** â Assume the permissions of an IAM role using web
      identity through configuration or the
        [`assume-role-with-web-identity`](https://docs.aws.amazon.com/cli/latest/reference/sts/assume-role-with-web-identity.html) command.

- 
    
**[AWS IAM Identity Center](./cli-configure-files.html)** â The
      IAM Identity Center configuration settings stored in the `config` file are updated when you run
      the `aws configure sso` command. Credentials are then authenticated when you run
      the `aws sso login` command. The `config` file is located at
      `~/.aws/config` on Linux or macOS, or at `C:\Users\USERNAME`\.aws\config on Windows. 

- 
    
**[Credentials
        file](./cli-configure-files.html)** â The `credentials` and `config` file are
      updated when you run the command `aws configure`. The `credentials` file
      is located at `~/.aws/credentials` on Linux or macOS, or at `C:\Users\USERNAME`\.aws\credentials on
      Windows.

- 
    
**[Custom
          process](./cli-configure-sourcing-external.html)** â Get your credentials from an external source.

- 
    
**[Configuration
        file](./cli-configure-files.html)** â The `credentials` and `config` file are
      updated when you run the command `aws configure`. The `config` file is
      located at `~/.aws/config` on Linux or macOS, or at `C:\Users\USERNAME`\.aws\config on
      Windows.

- 
    
**[Container
          credentials](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html)** â You can associate an IAM role with each of your
      Amazon Elastic Container Service (Amazon ECS) task definitions. Temporary credentials for that role are then available to
      that task's containers. For more information, see [IAM Roles for Tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) in the *Amazon Elastic Container Service Developer Guide*.

- 
    
**[Amazon EC2
          instance profile credentials](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html)** â You can associate an IAM role
      with each of your Amazon Elastic Compute Cloud (Amazon EC2) instances. Temporary credentials for that role are then
      available to code running in the instance. The credentials are delivered through the Amazon EC2
      metadata service. For more information, see [IAM Roles for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html) in the
        *Amazon EC2 User Guide* and [Using Instance
        Profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html) in the *IAM User Guide*.

## Additional topics in this section

- 
                
[Configuration and credential file settings in the
            AWS CLI](./cli-configure-files.html)

- 
                
[Configuring environment variables for the
            AWS CLI](./cli-configure-envvars.html)

- 
                
[Command line options in the AWS CLI](./cli-configure-options.html)

- 
                
[Configuring command completion in the AWS CLI](./cli-configure-completion.html)

- 
                
[AWS CLI retries in the AWS CLI](./cli-configure-retries.html)

- 
                
[Using an HTTP proxy for the AWS CLI](./cli-configure-proxy.html)

 **Javascript is disabled or is unavailable in your browser.**

To use the Amazon Web Services Documentation, Javascript must be enabled. Please refer to your browser's Help pages for instructions.

[Document Conventions](/general/latest/gr/docconventions.html)

Setup

Configuration settings