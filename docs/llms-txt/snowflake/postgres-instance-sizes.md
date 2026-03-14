# Source: https://docs.snowflake.com/en/user-guide/snowflake-postgres/postgres-instance-sizes.md

# Snowflake Postgres Instance Sizes

Snowflake Postgres offers three tiers of instances — Burstable, Standard, and Memory — to cover a variety of use cases.

For credit costs for each instance size, see the [Snowflake Service Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf).

In general:

* **Burstable** instances have a baseline CPU level but can temporarily burst above this baseline.
* **Standard** instances have a good balance of CPU and memory.
* **Memory-optimized** instances have a higher ratio of memory to CPU, which may improve performance for workloads with greater
  memory needs.

## Burstable

*Important notes*

* Burstable instances can be provisioned with a maximum of 100GB storage.
* Burstable instances have burstable vCPUs. Utilization in excess of the CPU baseline shown below will deplete available vCPU
  credits, leading to CPU rate limiting. This may appear as a sudden downgrade in performance with no other cause.
* Burstable instances do not support High Availability standbys.

| Name | Cores | Memory | IOPS | HA supported |
| --- | --- | --- | --- | --- |
| BURST_XS | 2 | 1GB | 11,800 | No |
| BURST_S | 2 | 2GB | 11,800 | No |
| BURST_M | 2 | 4GB | 11,800 | No |

## General purpose

| Name | Cores | Memory | IOPS | HA supported |
| --- | --- | --- | --- | --- |
| STANDARD_M | 1 | 4GB | 20,000 | Yes |
| STANDARD_L | 2 | 8GB | 40,000 | Yes |
| STANDARD_XL | 4 | 16GB | 40,000 | Yes |
| STANDARD_2XL | 8 | 32GB | 40,000 | Yes |
| STANDARD_4XL | 16 | 64GB | 40,000 | Yes |
| STANDARD_8XL | 32 | 128GB | 40,000 | Yes |
| STANDARD_12XL | 48 | 192GB | 60,000 | Yes |
| STANDARD_24XL | 96 | 384GB | 78,000 | Yes |

> **Note:**
>
> The STANDARD_M instance size is not available on Microsoft Azure.

## Memory optimized

| Name | Cores | Memory | IOPS | HA supported |
| --- | --- | --- | --- | --- |
| HIGHMEM_L | 2 | 16GB | 40,000 | Yes |
| HIGHMEM_XL | 4 | 32GB | 40,000 | Yes |
| HIGHMEM_2XL | 8 | 64GB | 40,000 | Yes |
| HIGHMEM_4XL | 16 | 128GB | 40,000 | Yes |
| HIGHMEM_8XL | 32 | 256GB | 40,000 | Yes |
| HIGHMEM_12XL | 48 | 384GB | 78,000 | Yes |
| HIGHMEM_16XL | 64 | 512GB | 78,000 | Yes |
| HIGHMEM_24XL | 96 | 768GB | 78,000 | Yes |
| HIGHMEM_32XL | 128 | 1TB | 78,000 | Yes |
| HIGHMEM_48XL | 192 | 1.5TB | 78,000 | Yes |
