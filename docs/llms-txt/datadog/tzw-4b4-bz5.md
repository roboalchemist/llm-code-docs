# Source: https://docs.datadoghq.com/security/default_rules/tzw-4b4-bz5.md

---
title: Blob Containers anonymous access should be restricted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Blob Containers anonymous access should
  be restricted
---

# Blob Containers anonymous access should be restricted
 
## Description{% #description %}

Ensures that Azure Storage Blob Containers are not publicly accessible.

## Rationale{% #rationale %}

Anonymous access to Azure storage blob containers allows unauthenticated users to perform operations against the blob container. Datadog recommends only allowing authenticated users access to storage blobs.

## Remediation{% #remediation %}

Datadog recommends both making the Blob Container private, and blocking public access at the storage account level.

### From the Console{% #from-the-console %}

Follow the [Set the public access level for a container - Azure Console](https://docs.microsoft.com/en-us/azure/storage/blobs/anonymous-read-access-configure?tabs=portal) guide to disable anonymous read access with the Azure Console.

Follow the [Remediate anonymous public access for the storage account](https://learn.microsoft.com/en-us/azure/storage/blobs/anonymous-read-access-prevent?tabs=portal#remediate-anonymous-public-access-for-the-storage-account) guide to block public access at the storage account level with the Azure Console.

### From the Azure CLI{% #from-the-azure-cli %}

Follow the [Set the public access level for a container - Azure CLI](https://docs.microsoft.com/en-us/azure/storage/blobs/anonymous-read-access-configure?tabs=azure-cli) guide to disable anonymous read access with the Azure CLI.

Follow the [Remediate anonymous public access for the storage account](https://learn.microsoft.com/en-us/azure/storage/blobs/anonymous-read-access-prevent?tabs=azure-cli#remediate-anonymous-public-access-for-the-storage-account) guide to block public access at the storage account level with the Azure CLI.
