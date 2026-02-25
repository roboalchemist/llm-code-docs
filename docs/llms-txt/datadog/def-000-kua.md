# Source: https://docs.datadoghq.com/security/default_rules/def-000-kua.md

---
title: >-
  Amazon Machine Image (AMI) should not be shared with external accounts or
  organizations
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Amazon Machine Image (AMI) should not
  be shared with external accounts or organizations
---

# Amazon Machine Image (AMI) should not be shared with external accounts or organizations

## Description{% #description %}

This rule evaluates whether Amazon Machine Images (AMIs) are shared with external AWS accounts or organizations that are not onboarded to Datadog. AMIs contain complete system images including operating systems, applications, and potentially sensitive data. Sharing AMIs with unauthorized external accounts or organizations can lead to data exposure and security risks.

The data contained in the `launch_permissions` field is enumerated and the following types of principals are assessed:

- `user_id` - designates an AWS account
- `organization_arn` - designates an organization from AWS Organizations
- `organizational_unit_arn` - designates an organizational unit (OU) from AWS Organizations

The control fails if any AWS account, organization, or OU present in `launch_permissions` is not onboarded to Datadog.

**Note**: If the AMI is shared with a trusted third-party AWS account or organization that you cannot onboard to Datadog, mute the finding and leave a comment documenting the justification.

## Remediation{% #remediation %}

To remove external account or organization sharing permissions from Amazon Machine Images, follow the steps outlined in the [Sharing an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharing-amis.html) section of the Amazon EC2 User Guide. For guidance regarding onboarding AWS accounts to Datadog, follow the [Datadog AWS integration documentation](https://docs.datadoghq.com/integrations/amazon_web_services/) to onboard the account. Ensure that resource collection and Cloud Security are correctly configured.
