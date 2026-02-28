# Source: https://docs.datadoghq.com/security/default_rules/def-000-njb.md

---
title: EC2 instance created using risky AMI search pattern
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EC2 instance created using risky AMI
  search pattern
---

# EC2 instance created using risky AMI search pattern
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1195-supply-chain-compromise](https://attack.mitre.org/techniques/T1195)
## Goal{% #goal %}

Detect when an EC2 instance is instantiated using a vulnerable AMI search pattern.

## Strategy{% #strategy %}

This rule allows you to monitor CloudTrail and detect when EC2 instances are created in a way that is vulnerable to a type of supply chain attack known as a *name confusion attack*. When this rule triggers, it does not mean an attack was successfully executed. Rather, it means that the way AMI IDs are being searched for is vulnerable to a name confusion attack. Unless the software is updated, an attacker who publishes an AMI that matches the search pattern used could gain remote code execution in the affected AWS account.

The rule triggers when both of the following conditions are met:

1. `ec2:DescribeImages` is called without specifying the `owner` parameter
1. Subsequently, the same IAM principal executes a call to `ec2:RunInstances`

The two CloudTrail events covered by this rule are:

- [ec2:DescribeImages](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImages.html)
- [ec2:RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html)

This rule inspects all `ec2:DescribeImages` events and specifically the `@requestParameters.filterSet.items` array to determine if the `name` key is used, which indicates the user is looking for an AMI by name. The rule then filters out all of the cases where the user included protections that would prevent exploitation, for instance, by using the `@requestParameters.ownersSet.items.owner` attribute or by requesting a specific AMI by ID. The rule also filters out all instances where the user has set `-@requestParameters.executableBySet.items.user:self` which would limit the results to self hosted AMIs.

The rule also includes a subsequent check to see if the same ARN that made the insecure query above also creates an EC2 instance shortly thereafter. This prevents false positives for when people manually use `ec2:DescribeImages` without ever using that data to create an EC2 instance.

The likelihood of exploitation for this vulnerability depends on the search filter used for the AMI. If the query string is a common AMI name pattern like `ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*` or `amzn2-ami-hvm-2.0.*-x86_64-gp2`, the likelihood of exploitation is greater. If the query string is unique to your organization, like `orgname-devops-xyz-image-*`, it typically limits exploitation to actors with knowledge of the image name pattern, such as developers.

**An example of behavior that would trigger this rule**:

Find the AMI ID using `ec2:DescribeImages` with a filter and without specifying the `owner` parameter:

```
AMIID="$(aws ec2 describe-images --filters "Name=name,Values=ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*" --query "Images[0].ImageId" --output text)"
```

Create the EC2 instance using the retrieved AMI ID:

```
aws ec2 run-instances --image-id "$AMIID" --instance-type t3.micro --subnet-id "$SUBNETID"
```

## Triage and response{% #triage-and-response %}

1. Investigate the ARN (`{{@userIdentity.arn}}`) that made the these calls.
1. Contact the user and attempt to identify the code that triggered this rule.
1. Work with the code owner to ensure they add one of the attributes in the `ec2:DescribeImages` call that limits the returned AMIs to those that are trusted. These include:
   - Owner attribute: `Owner=[AccountID, self, amazon, aws-backup-vault, and aws-marketplace]`
   - Filter: `owner-alias=[amazon, aws-marketplace, aws-backup-vault]`
   - Filter: `owner-id=[AccountID]`
1. Consider using AWS's [Allowed AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-allowed-amis.html) guardrail to limit which accounts are trusted to serve AMIs within your environment. This control can be enforced at an account/region level, or at an organization level.

## Known false positives and limitations{% #known-false-positives-and-limitations %}

- This detection relies on two separate CloudTrail events, executed by the same ARN, occurring in succession. However, CloudTrail does not contain all of the information needed to tie the two events together conclusively. It is possible that the ARN making the insecure `ec2:DescribeImages` call happens to subsequently call `ec2:DescribeImages` in a way that is unrelated to the insecure `ec2:DescribeImages` call. The best course of action is to find the user or code that made the `ec2:DescribeImages` call and determine if they used the result of the `ec2:DescribeImages` to create an EC2 instance.

- The `ec2:DescribeImages` CloudTrail event does not contain any information to indicate how the principal handled the data that came back. For example, from the CloudTrail event alone, there is no way to determine if the caller sorted the results by most recent creation date, simply used the first returned results, etc.

## Changelog{% #changelog %}

- 3 February 2025 - Added suppression for Packer by HashiCorp. The observed Packer behavior that matches this detection is a false positive.
