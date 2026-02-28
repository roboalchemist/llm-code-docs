# Source: https://docs.datadoghq.com/security/default_rules/def-000-6vi.md

---
title: Cloud KMS cryptokeys should restrict anonymous and/or public access
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Cloud KMS cryptokeys should restrict
  anonymous and/or public access
---

# Cloud KMS cryptokeys should restrict anonymous and/or public access

## Description{% #description %}

It is recommended that the IAM policy on Cloud KMS `cryptokeys` should restrict anonymous and/or public access.

## Rationale{% #rationale %}

Granting permissions to `allUsers` or `allAuthenticatedUsers` allows anyone to access the dataset. Such access might not be desirable if sensitive data is stored at the location. In this case, ensure that anonymous and/or public access to a Cloud KMS `cryptokey` is not allowed.

### Default Value{% #default-value %}

By default Cloud KMS does not allow access to `allUsers` or `allAuthenticatedUsers`.

### Impact{% #impact %}

Removing the binding for `allUsers` and `allAuthenticatedUsers` members denies anonymous and public users access to `cryptokeys`.

### Additional Information{% #additional-information %}

`key_ring_name` is the resource ID of the key ring, which is the fully-qualified key ring name. This value is case-sensitive and in the format: `projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING` You can retrieve the key ring resource ID using the Cloud Console:

1. Open the **Cryptographic Keys** page in the Cloud Console.
1. For the key ring whose resource ID you are retrieving, click the kebab menu (3 vertical dots).
1. Click **Copy Resource ID**. The resource ID for the key ring is copied to your clipboard.

`key_name` is the resource ID of the key, which is the fully-qualified CryptoKey name. This value is case-sensitive and in the format: `projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY` You can retrieve the key resource ID using the Cloud Console:

1. Open the **Cryptographic Keys** page in the Cloud Console.
1. Click the name of the key ring that contains the key.
1. For the key ring whose resource ID you are retrieving, click the kebab menu (3 vertical dots).
1. Click **Copy Resource ID**. The resource ID for the key ring is copied to your clipboard.

`role` is the role to remove the member from.

## Finding Notes{% #finding-notes %}

Findings may be inconsistent while `gcloud kms keyrings get-iam-policy` is implemented.

### Manual audits may be performed using{% #manual-audits-may-be-performed-using %}

1. List all Cloud KMS Cryptokeys.

   ```
   gcloud kms keys list --keyring=[key_ring_name] --location=global --format=json | jq '.[].name'
   ```

1. Ensure the below command's output does not contain `allUsers` or `allAuthenticatedUsers`.

   ```
   gcloud kms keys get-iam-policy [key_name] --keyring=[key_ring_name] --location=global --format=json | jq '.bindings[].members[]'
   ```

## Remediation{% #remediation %}

### From the command line{% #from-the-command-line %}

1. List all Cloud KMS `Cryptokeys`.
   ```
   gcloud kms keys list --keyring=[key_ring_name] --location=global --format=json | jq '.[].name'
   ```
1. To remove access to `allUsers` and `allAuthenticatedUsers`, remove the IAM policy binding for a KMS key using the below command.

```
gcloud kms keys remove-iam-policy-binding [key_name] --keyring=[key_ring_name] --location=global --member='allAuthenticatedUsers' --role='[role]'

gcloud kms keys remove-iam-policy-binding [key_name] --keyring=[key_ring_name] --location=global --member='allUsers' --role='[role]'
```

## References{% #references %}

1. [https://cloud.google.com/sdk/gcloud/reference/kms/keys/remove-iam-policy-binding](https://cloud.google.com/sdk/gcloud/reference/kms/keys/remove-iam-policy-binding)
1. [https://cloud.google.com/sdk/gcloud/reference/kms/keys/set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/kms/keys/set-iam-policy)
1. [https://cloud.google.com/sdk/gcloud/reference/kms/keys/get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/kms/keys/get-iam-policy)
1. [https://cloud.google.com/kms/docs/object-hierarchy#key_resource_id](https://cloud.google.com/kms/docs/object-hierarchy#key_resource_id)
