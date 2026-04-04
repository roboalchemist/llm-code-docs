# Source: https://archivedocs.stackstate.com/5.1/stackpacks/integrations/aws/aws-sts-ec2.md

# StackState/Agent IAM role: EC2

## Overview

If StackState or StackState Agent are running within an AWS environment on an EC2 instance, an IAM role can be attached to the EC2 instance for authentication. When this role is available it can be used for authentication by StackState or StackState Agent running on the same EC2 instance.

{% hint style="info" %}
Note: If the AWS Data Collection Account and the Monitor Account aren't a part of the same AWS organization, it isn't possible to authenticate using the attached IAM role in this way. For details see the AWS documentation on [AWS organizations (docs.aws.amazon.com)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html).
{% endhint %}

## Set up IAM role for StackState/StackState Agent on EC2

To set up an IAM role for StackState or StackState Agent to use, follow the instructions below.

1. If you did not do so already, [create a policy](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/aws#aws-policy) that allows the `AssumeRole` action for the resource `arn:aws:iam::*:role/StackStateAwsIntegrationRole`. Take note of the policy name.
2. Create an EC2 instance role and attach the policy from the previous step.

   ![Policy for AssumeRole](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-a5987e9d80ce94f254cd4f3253a35ee3dda092d5%2Fsts_on_ec2_aws_stp_02.png?alt=media)
3. Attach the newly created EC2 instance role to the EC2 instance where StackState or StackState Agent V3 is running.

   ![Attach role to EC2 instance](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-24535d9fc7d4881b4f2fe3858f81238f721684cd%2Fsts_on_ec2_aws_stp_03.png?alt=media)
4. Configure the StackPack instance or Agent AWS check to [authenticate using the attached IAM role](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/aws#iam-role-on-ec2-or-eks).

## See also

* [AWS StackPack](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/aws/aws)
