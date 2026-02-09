# Source: https://docs.datadoghq.com/security/default_rules/def-000-nxe.md

---
title: RDS clusters should have encryption at rest enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > RDS clusters should have encryption at
  rest enabled
---

# RDS clusters should have encryption at rest enabled
 
## Description{% #description %}

This check verifies RDS database clusters encrypt data at rest. Data at rest encompasses any information stored in persistent, non-volatile storage. Encryption is crucial for safeguarding the confidentiality of this data, mitigating the risk of unauthorized access. Ensuring your RDS database clusters are encrypted protects both your data and metadata from unauthorized access, as well as assists with adherence to compliance standards for encrypting data at rest in production file systems.

## Remediation{% #remediation %}

To enable encryption at rest, configure it during the creation of an RDS database cluster, as encryption settings cannot be modified post-creation. For further guidance, refer to the [Encrypting an Amazon Aurora DB cluster section in the Amazon Aurora User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.Encryption.html#Overview.Encryption.Enabling).
