# Source: https://docs.datadoghq.com/security/default_rules/def-000-zzm.md

---
title: Instances should use instance-specific SSH keys instead of project-wide keys
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Instances should use instance-specific
  SSH keys instead of project-wide keys
---

# Instances should use instance-specific SSH keys instead of project-wide keys

## Description{% #description %}

Datadog recommends using instance-specific SSH key(s) instead of common or shared project-wide SSH key(s) to access instances.

## Rationale{% #rationale %}

Project-wide SSH keys are stored in compute or project-meta-data. Project-wide SSH keys can be used to log into all instances within a project. Using project-wide SSH keys facilitates SSH key management, but if compromised, poses a security risk which can impact all instances within a project. Datadog recommmends using instance-specific SSH keys, which can limit the attack surface if SSH keys are compromised.

## Impact{% #impact %}

Users already having project-wide SSH key pairs and are using third-party SSH clients will lose access to the impacted instances. For project users using Google Cloud or GCP Console-based SSH options, no manual key creation and distribution is required, this is all handled by Google Compute Engine (GCE) itself. To access an instance using third-party SSH clients, the instance-specific SSH key pairs need to be created and distributed to the required users.

## Remediation{% #remediation %}

### From Console{% #from-console %}

1. In the Google Cloud Console, navigate to [VM Instances page](https://console.cloud.google.com/compute/instances), which lists all instances in your project.
1. Click on the impacted instance name.
1. Click **Edit** in the toolbar.
1. To block users with project-wide SSH keys from connecting to this instance, select **Block project-wide SSH keys** under **SSH Keys**.
1. Click **Save** at the bottom of the page.
1. Repeat these steps for every impacted instance.

### From Command Line{% #from-command-line %}

To block project-wide public SSH keys, set the metadata value to true using `gcloud compute instances add-metadata <INSTANCE_NAME> --metadata block-project-ssh-keys=TRUE`.

## Default Value{% #default-value %}

By default, Block Project-wide SSH keys is not enabled.

## References{% #references %}

[https://cloud.google.com/compute/docs/instances/adding-removing-ssh-keys](https://cloud.google.com/compute/docs/instances/adding-removing-ssh-keys) [https://cloud.google.com/sdk/gcloud/reference/topic/formats](https://cloud.google.com/sdk/gcloud/reference/topic/formats)

## Additional Information{% #additional-information %}

If OS Login is enabled, SSH keys in the instance metadata are ignored, which means you do not need to block project-wide SSH keys.
