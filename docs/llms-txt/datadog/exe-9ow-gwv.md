# Source: https://docs.datadoghq.com/security/default_rules/exe-9ow-gwv.md

---
title: Amazon Machine Image (AMI) should not be publicly shared
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Amazon Machine Image (AMI) should not
  be publicly shared
---

# Amazon Machine Image (AMI) should not be publicly shared
 
## Description{% #description %}

Identify publicly accessible Amazon Machine Images (AMIs).

## Rationale{% #rationale %}

When an AMI is shared publicly, anyone outside your organization can see it in the [list of public AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/usingsharedamis-finding.html) and create an EC2 instance from it, accessing all the files it contains.

AMIs typically contain source code, configuration files and credentials and should not be shared publicly. AMIs should only be shared with [specific AWS accounts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharingamis-explicit.html) or [your AWS Organization](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/share-amis-with-organizations-and-OUs.html).

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

Follow the instructions outlined in the [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharingamis-explicit.html).

### From the command line{% #from-the-command-line %}

Use the following command to stop sharing the AMI:

```bash
aws ec2 modify-image-attribute \
--image-id ami-xxxx \
--launch-permission "Remove=[{Group=all}]"
```

.
