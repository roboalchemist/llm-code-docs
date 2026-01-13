# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_instance_type.dataset.md

---
title: EC2 Instance Types
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EC2 Instance Types
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.ec2_instance_type.dataset/index.html
---

# EC2 Instance Types

EC2 Instance Types in AWS define the virtual server configurations you can run in the cloud. They specify combinations of CPU, memory, storage, and networking capacity to suit different workloads. Instance families are optimized for general purpose, compute, memory, storage, or accelerated computing needs. This allows you to choose the right balance of performance and cost for applications such as web hosting, databases, analytics, or machine learning.

```
aws.ec2_instance_type
```

## Fields

| Title                           | ID   | Type          | Data Type                                                                                                                                  | Description |
| ------------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                            | core | string        |
| auto_recovery_supported         | core | bool          | Indicates whether Amazon CloudWatch action based recovery is supported.                                                                    |
| bare_metal                      | core | bool          | Indicates whether the instance is a bare metal instance type.                                                                              |
| burstable_performance_supported | core | bool          | Indicates whether the instance type is a burstable performance T instance type. For more information, see Burstable performance instances. |
| current_generation              | core | bool          | Indicates whether the instance type is current generation.                                                                                 |
| dedicated_hosts_supported       | core | bool          | Indicates whether Dedicated Hosts are supported on the instance type.                                                                      |
| ebs_info                        | core | json          | Describes the Amazon EBS settings for the instance type.                                                                                   |
| fpga_info                       | core | json          | Describes the FPGA accelerator settings for the instance type.                                                                             |
| free_tier_eligible              | core | bool          | Indicates whether the instance type is eligible for the free tier.                                                                         |
| gpu_info                        | core | json          | Describes the GPU accelerator settings for the instance type.                                                                              |
| hibernation_supported           | core | bool          | Indicates whether On-Demand hibernation is supported.                                                                                      |
| hypervisor                      | core | string        | The hypervisor for the instance type.                                                                                                      |
| inference_accelerator_info      | core | json          | Describes the Inference accelerator settings for the instance type.                                                                        |
| instance_storage_info           | core | json          | Describes the instance storage for the instance type.                                                                                      |
| instance_storage_supported      | core | bool          | Indicates whether instance storage is supported.                                                                                           |
| instance_type                   | core | string        | The instance type. For more information, see Instance types in the Amazon EC2 User Guide.                                                  |
| media_accelerator_info          | core | json          | Describes the media accelerator settings for the instance type.                                                                            |
| memory_info                     | core | json          | Describes the memory for the instance type.                                                                                                |
| network_info                    | core | json          | Describes the network settings for the instance type.                                                                                      |
| neuron_info                     | core | json          | Describes the Neuron accelerator settings for the instance type.                                                                           |
| nitro_enclaves_support          | core | string        | Indicates whether Nitro Enclaves is supported.                                                                                             |
| nitro_tpm_info                  | core | json          | Describes the supported NitroTPM versions for the instance type.                                                                           |
| nitro_tpm_support               | core | string        | Indicates whether NitroTPM is supported.                                                                                                   |
| phc_support                     | core | string        | Indicates whether a local Precision Time Protocol (PTP) hardware clock (PHC) is supported.                                                 |
| placement_group_info            | core | json          | Describes the placement group settings for the instance type.                                                                              |
| processor_info                  | core | json          | Describes the processor.                                                                                                                   |
| supported_boot_modes            | core | array<string> | The supported boot modes. For more information, see Boot modes in the Amazon EC2 User Guide.                                               |
| supported_root_device_types     | core | array<string> | The supported root device types.                                                                                                           |
| supported_usage_classes         | core | array<string> | Indicates whether the instance type is offered for spot, On-Demand, or Capacity Blocks.                                                    |
| supported_virtualization_types  | core | array<string> | The supported virtualization types.                                                                                                        |
| v_cpu_info                      | core | json          | Describes the vCPU configurations for the instance type.                                                                                   |
