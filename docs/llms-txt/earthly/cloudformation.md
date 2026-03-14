# Source: https://docs.earthly.dev/earthly-cloud/satellites/byoc/aws/cloudformation.md

# CloudFormation

This page documents the requirements and steps required to install [BYOC Satellites](https://docs.earthly.dev/earthly-cloud/satellites/byoc) in AWS using Earthly's CloudFormation template.

## Requirements

Before you begin to provision your BYOC configuration, ensure that you meet the [base requirements](https://docs.earthly.dev/earthly-cloud/satellites/byoc/aws/requirements) for installation within AWS.

There are also a few additional requirements you will need to make sure you meet:

* An AWS account or role with permissions to:
  * create a new CloudFormation stack, and
  * describe the newly created CloudFormation stack after it has run.
* An AWS account or role that can create all the resources specified in the template.
* You have [AWS Credentials configured](https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-files.html) on your machine, with permissions to describe the CloudFormation stack you created.

## Installing the CloudFormation Template

You can install our CloudFormation template by opening this link in a new tab and following the prompts:

[![Launch Stack In us-west-2](https://1635908337-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8IWCntycnLCPhIzm97hh%2Fuploads%2Fgit-blob-cf7dd6f689062264466c864f63721c88862e1edf%2Fcloudformation.png?alt=media)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/create/review?templateURL=https://production-byoc-installation.s3.us-west-2.amazonaws.com/cloudformation-byoc-installation.yaml)

If you're curious about what we're provisioning, you can look at our [template](https://production-byoc-installation.s3.us-west-2.amazonaws.com/cloudformation-byoc-installation.yaml) directly.

If you need help, please reference the overview below:

### Template Overview

#### Stack Name

![The AWS Stack Name box in CloudFormation with a single text field for inputting the stack name](https://1635908337-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8IWCntycnLCPhIzm97hh%2Fuploads%2Fgit-blob-c968c00c8700446eb7b8ca52ed0dcef6c07f209a%2Fcloudformation-stack-name.png?alt=media)

A "Stack" is a logical grouping of resources, created by a template using AWS CloudFormation. This name is required by AWS to identify the Stack we will create within CloudFormation.

Earthly will reuse this name as the name of the "installation" within Earthly, so you will always have a direct correlation between items in AWS and Earthly. This is also the string you will provide to the Earthly CLI during step 2.

#### Parameters

![The Parameters box for the CloudFormation template. It contains input fields for a Subnet ID, VPC ID, and an Ingress CIDR Block.](https://1635908337-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8IWCntycnLCPhIzm97hh%2Fuploads%2Fgit-blob-01f1dd12d3b16895d5f895232d57eb2338150c44%2Fcloudformation-stack-params.png?alt=media) \`\`\` There are only a few parameters required to get up and moving with a BYOC setup, and they're mostly related to your networking configuration.

| Parameter          | Description                                                                                                                                                                                                                    |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Subnet             | The location that Earthly will launch your satellites into. It can be as big or small as you would like, just make sure it has enough room to handle the expected number of Satellites.                                        |
| VPC                | The VPC for the subnet you selected earlier. The template should do some validation to ensure these match. While it might feel redundant, this parameter is here to avoid creating a more complicated CloudFormation template. |
| Ingress CIDR Block | This value will be used to create the needed security group rules for the Satellites that Earthly launches on your behalf. For instance, when using Tailscale, this could be the IP address of your Subnet Router.             |

All parameters with "(Required)" in the label subtext are required for a successful installation.

#### Permissions

![The Permissions box for the CloudFormation template. It allows the user to specify an AWS role for the CloudFormation service to use when installing the template.](https://1635908337-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8IWCntycnLCPhIzm97hh%2Fuploads%2Fgit-blob-c6325ea4271b4973d3df5ff9d0b81da7eed6a17c%2Fcloudformation-stack-permissions.png?alt=media)

This box is optional, and depends on your current permissions within AWS. In most cases, you can leave this blank.

If you try to install the template and get permissions errors, you can [contact us](https://earthly.dev/slack) or your AWS administrator for further guidance based on your specific situation.

#### Capabilities

![The Capabilities section for the CloudFormation template. It informs the user that the template requires the AWS::IAM::ManagedPolicy capability, and will install IAM resources with custom names.](https://1635908337-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8IWCntycnLCPhIzm97hh%2Fuploads%2Fgit-blob-feff0e81452749069e8bc27dc3f426ec906c459e%2Fcloudformation-stack-capabilities.png?alt=media)

The CloudFormation template will install two IAM policies within the account. One is to allow Earthly the permissions it needs to access your account and manage your satellite instances, and the other allows Satellites themselves to log to CloudWatch Logs. These have derived names that are associated with the Stack Name specified. Check the box to move on.

If organizational policy prevents you from creating IAM resources with custom names, you can create the needed resources manually, and use the [import functionality within CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import.html) to install this stack.

#### Finalize

If all this looks good, click the "Next" button at the bottom of the page. Your stack will start creating. Click the refresh button in the top right to update the list of events. Proceed with the rest of the BYOC installation once the stack creation is `CREATE_COMPLETE`.

![The events monitoring page for the CloudFormation template you've begun installing. It has successful creation events for items within the stack, and the stack has been created successfully.](https://1635908337-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8IWCntycnLCPhIzm97hh%2Fuploads%2Fgit-blob-019c057bfbc2e801d2aaf4d3a9cc1242f2852296%2Fcloudformation-stack-events.png?alt=media)

### Post-Installation Notes

#### SSH

The template creates an SSH key that can be used to access the Satellites for debugging, or other diagnostic purposes. While the fingerprint and public key are stored in the usual spot within EC2, the private key can take a little bit of digging. Here's how to find it:

* Get the id of the key created by CloudFormation:
  * Open EC2, and click on "Key Pairs", under the "Network & Security" section on the left.
  * Find the key named `<stack-name>-satellite-key`, where `<stack-name>` is the name you used when creating the CloudFormation Stack.
  * Note the id column for this entry, and use it in the next step. ![A list of EC2 SSH Key Pairs. It has several columns, inclding ID.](https://1635908337-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8IWCntycnLCPhIzm97hh%2Fuploads%2Fgit-blob-11bf9cd0f675e818873dc91ad0e309330e5ace11%2Fcloudformation-key-id.png?alt=media)
* Visit the [SSM Parameter Store](https://us-west-2.console.aws.amazon.com/systems-manager/parameters?region=us-west-2)
  * Click on the name of the desired secret, it will be of the format `/ec2/keypair/<key-id>`, where `<key-id>` is the id you got from EC2.
  * On the "Overview" tab, in the "Parameter details" box, there is a toggle labeled "Show decrypted value". Click it to reveal your SSH private key: ![The parameter details box for a given key id. It has a name, ARN, Tier, Type, and Value field. The Show decrypted value toggle is off.](https://1635908337-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F8IWCntycnLCPhIzm97hh%2Fuploads%2Fgit-blob-16f04d530cf315a6ed51848904f49b1d2fb94357%2Fcloudformation-ssm-parameter-store.png?alt=media)

If you prefer the CLI:

* Run this to get the ID of your key:

  ```shell
  aws ec2 describe-key-pairs \
    --filters 'Name=key-name,Values=<stack-name>-satellite-key' \
    --query 'KeyPairs[*].KeyPairId' \
    --output text
  ```

  Where `<stack-name>` is the name you gave the CloudFormation stack at creation time.
* Next, run this to get your key, and save it in a file named `key.pem`:

  ```shell
  aws ssm get-parameter \
  --name /ec2/keypair/<key-id> \
  --with-decryption \
  --query Parameter.Value \
  --output text > key.pem
  ```

  Where `<key-id>` is the value obtained from the prior step.

#### Customization

If you need/want to make changes to your installation, please see AWS' guide for [resolving drift in a CloudFormation stack via import](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-resolve-drift.html).

## Installation Within Earthly

Earthly is able to automatically install BYOC when provisioned via CloudFormation by running:

```shell
earthly cloud install --via terraform --name <stack-name>
```

Where `<stack-name>` is the name used for your stack within AWS. Earthly will also use this name to reference your installation.

Assuming the installation reports the status as `Green`, you should be good to go!
