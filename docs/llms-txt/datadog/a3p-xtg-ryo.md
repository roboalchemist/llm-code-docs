# Source: https://docs.datadoghq.com/security/default_rules/a3p-xtg-ryo.md

---
title: Potential administrative port open to the world via AWS security group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Potential administrative port open to
  the world via AWS security group
---

# Potential administrative port open to the world via AWS security group
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detect when an AWS security group is opened to the world on a port commonly associated with an administrative service.

## Strategy{% #strategy %}

Monitor CloudTrail and detect when an AWS security group has been created or modified with one of the following API calls:

- [`AuthorizeSecurityGroupIngress`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupIngress.html)

This rule inspects the `@requestParameters.ipPermissions.items.ipRanges.items.cidrIp` or `@requestParameters.cidrIp` array to determine if either of the strings are contained - `0.0.0.0/0` or `::/0` for the following ports:

- 21 (FTP)
- 22 (SSH)
- 23 (Telnet)
- 445 (SMB)
- 2375 (Docker daemon)
- 3389 (RDP)
- 5900 (VNC)
- 5985 (WinRM HTTP)
- 5986 (WinRM HTTPS)

Administrative ports that are open to the world are a common target for attackers to gain unauthorized access to resources or data.

**Note:** There is a separate rule to detect AWS [Security Group Open to the World](https://docs.datadoghq.com/security/default_rules/aws-security-group-open-to-world/).

## Triage and response{% #triage-and-response %}

1. Determine if `{{@userIdentity.session_name}}` should have made a `{{@evt.name}}` API call.

1. If the API call was not made by the user:

   - Rotate the user credentials.
   - Determine what other API calls were made by the user.
   - Investigate VPC flow logs and OS system logs to determine if unauthorized access occurred.

1. If the API call was made legitimately by the user:

   - Advise the user to modify the IP range to the company private network or bastion host.

1. Revert security group configuration back to known good state if required:

   - Use the `aws-cli` command [`revoke-security-group-ingress`](https://docs.aws.amazon.com/cli/latest/reference/ec2/revoke-security-group-ingress.html) or the [AWS console](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#deleting-security-group-rules) to remove the rule.
   - Use the `aws-cli` command [`modify-security-group-rules`](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-security-group-rules.html) or [AWS console](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#updating-security-group-rules) to modify the existing rule.

## Changelog{% #changelog %}

- 26 August 2022 - Updated rule query.
- 1 November 2022 - Updated rule query and severity.
- 23 July 2025 - Updated rule queries to remove failed attempts.
