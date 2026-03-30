# Source: https://docs.datadoghq.com/security/default_rules/def-000-dj0.md

---
title: Customer-Managed Encryption Keys (CMEK) should be used for boot disks
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Customer-Managed Encryption Keys (CMEK)
  should be used for boot disks
---

# Customer-Managed Encryption Keys (CMEK) should be used for boot disks

## Description{% #description %}

Use Customer-Managed Encryption Keys (CMEK) to encrypt node boot disks using keys managed within Cloud Key Management Service (Cloud KMS). GCE persistent disks are encrypted at rest by default using envelope encryption with keys managed by Google. For additional protection, users can manage the Key Encryption Keys using Cloud KMS.

## Remediation{% #remediation %}

**Note:** This cannot be remediated by updating an existing cluster. The node pool must either be recreated or a new cluster created.

### From the console{% #from-the-console %}

To create a new node pool:

1. Go to the [Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)
1. Select Kubernetes clusters for which node boot disk CMEK is `disabled`
1. Click `ADD NODE POOL`
1. In the Nodes section, under machine configuration, ensure Boot disk type is `Standard persistent disk` or `SSD persistent disk`
1. Select `Enable customer-managed encryption for Boot Disk` and select the Cloud KMS encryption key to be used.
1. Click `CREATE`

To create a new cluster:

1. Go to the [Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)
1. Click `CREATE` and click `CONFIGURE` for the required cluster mode
1. Under `NODE POOLS`, expand the default-pool list and click `Nodes`
1. In the Configure node settings pane, select `Standard persistent disk` or `SSD Persistent Disk` as the Boot disk type
1. Select `Enable customer-managed encryption for Boot Disk` check box and choose the `Cloud KMS encryption key` to be used
1. Configure the rest of the cluster settings as required
1. Click `CREATE`

### From the commandline{% #from-the-commandline %}

1. Create a new node pool using customer-managed encryption keys for the node boot disk, of disk_type either `pd-standard` or `pd-ssd`:
   ```
   gcloud container node-pools create <cluster_name> --disk-type <disk_type> --boot-disk-kms-keyprojects/<key_project_id>/locations/<location>/keyRings/<ring_name>/cryptoKeys/<key_name>
   ```
1. Create a cluster using customer-managed encryption keys for the node boot disk, of disk_type either `pd-standard` or `pd-ssd`:
   ```
   gcloud container clusters create <cluster_name> --disk-type <disk_type> --boot-disk-kms-key projects/<key_project_id>/locations/<location>/keyRings/<ring_name>/cryptoKeys/<key_name>
   ```

## References{% #references %}
