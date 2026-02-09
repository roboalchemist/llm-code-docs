# Source: https://docs.datadoghq.com/security/default_rules/def-000-ne9.md

---
title: >-
  VM disks for critical VMs should be encrypted with customer-supplied
  encryption keys
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > VM disks for critical VMs should be
  encrypted with customer-supplied encryption keys
---

# VM disks for critical VMs should be encrypted with customer-supplied encryption keys
 
## Description{% #description %}

Customer-Supplied Encryption Keys (CSEK) are a feature in Google Cloud Storage and Google Compute Engine. If you supply your own encryption keys, Google uses your key to protect the Google-generated keys used to encrypt and decrypt your data. By default, Google Compute Engine encrypts all data at rest. Compute Engine handles and manages this encryption for you without any additional actions on your part. However, if you wanted to control and manage this encryption yourself, you can provide your own encryption keys.

### Default value{% #default-value %}

By default, VM disks are encrypted with Google-managed keys. They are not encrypted with `Customer-Supplied` Encryption Keys.

## Rationale{% #rationale %}

By default, Google Compute Engine encrypts all data at rest. Compute Engine handles and manages this encryption for you without any additional actions on your part. However, if you wanted to control and manage this encryption yourself, you can provide your own encryption keys. If you provide your own encryption keys, Compute Engine uses your key to protect the Google-generated keys used to encrypt and decrypt your data. Only users who can provide the correct key can use resources protected by a customer-supplied encryption key. Google does not store your keys on its servers and cannot access your protected data unless you provide the key. This also means that if you forget or lose your key, there is no way for Google to recover the key or to recover any data encrypted with the lost key. Business critical VMs should have VM disks encrypted with CSEK.

### Impact{% #impact %}

If you lose your encryption key, you will not be able to recover the data.

## Remediation{% #remediation %}

You cannot update the encryption of an existing disk. Therefore, you should create a new disk with encryption set to **Customer supplied**.

### From the console{% #from-the-console %}

1. Go to [Compute Engine Disks](https://console.cloud.google.com/compute/disks) in your Google Cloud console.
1. Click **CREATE DISK**.
1. Set **Encryption type** to `Customer supplied`.
1. Provide the **Key** in the box.
1. Select **Wrapped key**.
1. Click **Create**.

### From the command line{% #from-the-command-line %}

You can use the `gcloud` CLI to encrypt a disk using the `--csek-key-file` flag during instance creation. If you are using an RSA-wrapped key, use the gcloud beta component. See [RSA key wrapping](https://cloud.google.com/compute/docs/disks/customer-supplied-encryption#rsa-encryption) in Google's Compute Engine documentation.

```
gcloud compute instances create <INSTANCE_NAME> --csek-key-file <example-
file.json>
```

To encrypt a standalone persistent disk:

```
gcloud compute disks create <DISK_NAME> --csek-key-file <example-file.json>
```

## References{% #references %}

1. [https://cloud.google.com/compute/docs/disks/customer-supplied-encryption#encrypt_a_new_persistent_disk_with_your_own_keys](https://cloud.google.com/compute/docs/disks/customer-supplied-encryption#encrypt_a_new_persistent_disk_with_your_own_keys)
1. [https://cloud.google.com/compute/docs/reference/rest/v1/disks/get](https://cloud.google.com/compute/docs/reference/rest/v1/disks/get)
1. [https://cloud.google.com/compute/docs/disks/customer-supplied-encryption#key_file](https://cloud.google.com/compute/docs/disks/customer-supplied-encryption#key_file)
