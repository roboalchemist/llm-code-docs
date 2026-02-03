# Source: https://docs.datadoghq.com/security/default_rules/def-000-8zc.md

---
title: KMS keys should not be unintentionally deleted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > KMS keys should not be unintentionally
  deleted
---

# KMS keys should not be unintentionally deleted
 
## Description{% #description %}

This control verifies if KMS keys are set for deletion. The control will not pass if a KMS key is set for deletion and replicas do not exist.

Once a KMS key is deleted, it cannot be recovered. Data encrypted with a KMS key becomes permanently unrecoverable if the key is deleted. If important data is encrypted under a KMS key that is scheduled for deletion, it is recommended to decrypt or re-encrypt the data using a new KMS key unless a cryptographic erasure is intentional.

If a KMS key is scheduled for deletion, there is a required waiting period to allow for the possibility of reversing the deletion if it was set in error. The default waiting period is 30 days, but it can be shortened to a minimum of 7 days when scheduling the deletion of a KMS key. During this waiting period, the deletion can be canceled, and the KMS key will not be deleted.

For more details on deleting KMS keys, refer to the Deleting [KMS keys section in the AWS Key Management Service Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html).

## Remediation{% #remediation %}

To revoke a planned deletion of a KMS key, please refer to the [Scheduling and canceling key deletion (console)](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-scheduling-key-deletion.html#deleting-keys-scheduling-key-deletion-console) of the AWS Key Management Service Developer Guide.
