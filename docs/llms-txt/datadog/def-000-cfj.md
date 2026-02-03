# Source: https://docs.datadoghq.com/security/default_rules/def-000-cfj.md

---
title: EMR block public access setting should be enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > EMR block public access setting should
  be enabled
---

# EMR block public access setting should be enabled
 
## Description{% #description %}

Amazon EMR provides the 'Block public access' (BPA) setting to help restrict unintended public access to data stored in EMR. By default, accounts that have created Amazon EMR clusters after July 2019 have this setting enabled automatically. Additionally, an exemption for SSH traffic on port 22 is present by default. Exemptions can be added or removed as necessary depending on your requirements.

## Remediation{% #remediation %}

For guidance on configuring EMR BPA settings, refer to the [Using Amazon EMR block public access](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-block-public-access.html) section of the Amazon EMR Management Guide.
