# Source: https://docs.datadoghq.com/security/default_rules/def-000-9fh.md

---
title: KMS encryption keys should be rotated every 90 days or less
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > KMS encryption keys should be rotated
  every 90 days or less
---

# KMS encryption keys should be rotated every 90 days or less

## Description{% #description %}

Google Cloud Key Management Service stores cryptographic keys in a hierarchical structure designed for useful and elegant access control management. The format for the rotation schedule depends on the client library that is used. For the gcloud CLI, the flag `--next-rotation-time` must be in ISO or RFC3339 format; the flag `--rotation-period` must be in the format `INTEGER[UNIT]`, where units can be one of: seconds (s), minutes (m), hours (h), or days (d). For example, `30d` for a rotation period of 30 days.

## Rationale{% #rationale %}

Set a key rotation period and starting time. A key can be created with a specified *rotation period*, which is the time between when new key versions are generated automatically. A key can also be created with a specified *next rotation time*.

A key is a named object that represents a cryptographic key and is used for a specific purpose. The key material (the actual bits used for encryption) can change over time as new key versions are created. A key is used to protect a *corpus of data*. A collection of files could be encrypted with the same key, and people with `decrypt` permissions on that key would be able to decrypt those files. Therefore, it's necessary to make sure the rotation period is set to a specific time.

## Impact{% #impact %}

After a successful key rotation, the older key version is required to decrypt the data encrypted by the previous key version.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. See your cryptographic keys by visiting: [https://console.cloud.google.com/security/kms](https://console.cloud.google.com/security/kms).
1. Click on the specific key ring.
1. From the list of keys, locate the key you wish to edit. Click on the three vertical dots under the **Actions** column.
1. Click on **Edit rotation period**.
1. In the pop-up window, select a new rotation period. Choose value less than 90 days. Then, choose the date from which the rotation period begins.

### From the command line{% #from-the-command-line %}

1. Update and schedule rotation by `ROTATION_PERIOD` and `NEXT_ROTATION_TIME` for each key: For example, you can use the iam.json file shown below as follows:
   ```
    gcloud kms keys update new --keyring=KEY_RING --location=LOCATION --next- rotation-time=NEXT_ROTATION_TIME --rotation-period=ROTATION_PERIOD
   ```

## Default value{% #default-value %}

By default, KMS encryption keys are rotated every 90 days.

## References{% #references %}

1. [https://cloud.google.com/kms/docs/key-rotation#frequency_of_key_rotation](https://cloud.google.com/kms/docs/key-rotation#frequency_of_key_rotation)
1. [https://cloud.google.com/kms/docs/re-encrypt-data](https://cloud.google.com/kms/docs/re-encrypt-data)

## Additional Information{% #additional-information %}

A user-managed key cannot be created on GCP-Managed Service Accounts.
