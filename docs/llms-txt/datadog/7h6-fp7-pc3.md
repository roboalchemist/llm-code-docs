# Source: https://docs.datadoghq.com/security/default_rules/7h6-fp7-pc3.md

---
title: Unused credentials should be deactivated or removed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Unused credentials should be
  deactivated or removed
---

# Unused credentials should be deactivated or removed
 
## Description{% #description %}

AWS IAM users can access AWS resources using various types of credentials, such as passwords and access keys. Datadog recommends that you deactivate or remove all credentials that are unused for 45 or more days to enhance security.

Disabling or removing unnecessary credentials reduces the window of opportunity for compromised or abandoned accounts to be exploited, enhancing the security posture of the AWS environment.

## Remediation{% #remediation %}

For instructions on managing and deactivating unused IAM credentials, refer to [AWS documentation on handling unused credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_finding-unused.html).
