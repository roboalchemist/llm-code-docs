# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.drs_replication_configuration_template.dataset.md

---
title: Elastic Disaster Recovery Replication Configuration Template
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Elastic Disaster Recovery
  Replication Configuration Template
---

# Elastic Disaster Recovery Replication Configuration Template

Elastic Disaster Recovery Replication Configuration Template in AWS defines the default settings used when creating replication configurations for source servers. It specifies parameters such as replication frequency, data routing, staging area subnet, encryption, and other options that control how data is replicated from on-premises or cloud-based servers to AWS for disaster recovery.

```
aws.drs_replication_configuration_template
```

## Fields

| Title                                    | ID   | Type          | Data Type                                                                                                                                           | Description |
| ---------------------------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                     | core | string        |
| account_id                               | core | string        |
| arn                                      | core | string        | The Replication Configuration Template ARN.                                                                                                         |
| associate_default_security_group         | core | bool          | Whether to associate the default Elastic Disaster Recovery Security group with the Replication Configuration Template.                              |
| auto_replicate_new_disks                 | core | bool          | Whether to allow the AWS replication agent to automatically replicate newly added disks.                                                            |
| bandwidth_throttling                     | core | int64         | Configure bandwidth throttling for the outbound data transfer rate of the Source Server in Mbps.                                                    |
| create_public_ip                         | core | bool          | Whether to create a Public IP for the Recovery Instance by default.                                                                                 |
| data_plane_routing                       | core | string        | The data plane routing mechanism that will be used for replication.                                                                                 |
| default_large_staging_disk_type          | core | string        | The Staging Disk EBS volume type to be used during replication.                                                                                     |
| ebs_encryption                           | core | string        | The type of EBS encryption to be used during replication.                                                                                           |
| ebs_encryption_key_arn                   | core | string        | The ARN of the EBS encryption key to be used during replication.                                                                                    |
| pit_policy                               | core | json          | The Point in time (PIT) policy to manage snapshots taken during replication.                                                                        |
| replication_configuration_template_id    | core | string        | The Replication Configuration Template ID.                                                                                                          |
| replication_server_instance_type         | core | string        | The instance type to be used for the replication server.                                                                                            |
| replication_servers_security_groups_i_ds | core | array<string> | The security group IDs that will be used by the replication server.                                                                                 |
| staging_area_subnet_id                   | core | string        | The subnet to be used by the replication staging area.                                                                                              |
| staging_area_tags                        | core | hstore        | A set of tags to be associated with all resources created in the replication staging area: EC2 replication server, EBS volumes, EBS snapshots, etc. |
| tags                                     | core | hstore_csv    |
| use_dedicated_replication_server         | core | bool          | Whether to use a dedicated Replication Server in the replication staging area.                                                                      |
