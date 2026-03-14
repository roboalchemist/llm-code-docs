# Source: https://docs.snowflake.com/en/sql-reference/sql/create-compute-pool.md

# CREATE COMPUTE POOL

Creates a new [compute pool](../../developer-guide/snowpark-container-services/working-with-compute-pool.md) in the current account.

See also:
:   [ALTER COMPUTE POOL](alter-compute-pool.md) , [DESCRIBE COMPUTE POOL](desc-compute-pool.md), [DROP COMPUTE POOL](drop-compute-pool.md) , [SHOW COMPUTE POOLS](show-compute-pools.md)

## Syntax

```sqlsyntax
CREATE COMPUTE POOL [ IF NOT EXISTS ] <name>
  [ FOR APPLICATION <app-name> ]
  MIN_NODES = <num>
  MAX_NODES = <num>
  INSTANCE_FAMILY = <instance_family_name>
  [ AUTO_RESUME = { TRUE | FALSE } ]
  [ INITIALLY_SUSPENDED = { TRUE | FALSE } ]
  [ AUTO_SUSPEND_SECS = <num>  ]
  [ [ WITH ] TAG ( <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' , ... ] ) ]
  [ COMMENT = '<string_literal>' ]
  [ PLACEMENT_GROUP = '<placement_group_name>' ]
```

## Required parameters

`name`
:   String that specifies the identifier (that is, the name) for the compute pool; it must be unique for your account. Quoted names for special characters or case-sensitive names are not supported.

`MIN_NODES = num`
:   Specifies the minimum number of nodes for the compute pool. This value must be greater than 0. For more information, see
    [Creating a compute pool](../../developer-guide/snowpark-container-services/working-with-compute-pool.md).

`MAX_NODES = num`
:   Specifies the maximum number of nodes for the compute pool.

`INSTANCE_FAMILY = instance_family_name`
:   Identifies the type of machine you want to provision for the nodes in the compute pool. The machine type determines the amount
    of compute resources in the compute pool and, therefore, the number of credits consumed while the compute pool is running.

    The INSTANCE_FAMILY values in the following table can be grouped into 3 categories:

    * **Generic instance types:** Provide a balance of CPU, memory and disk. This does not include GPU. These instance family names
      start with “CPU”.
    * **High memory instance types:** Similar to generic instance types, but these provide more memory. These instance family
      names start with “HighMemory”.
    * **Instance types with GPU attached:** These instance family names start with “GPU”.

    You can also use the [SHOW COMPUTE POOL INSTANCE FAMILIES](show-compute-pool-instance-families.md) command to get this list of available instance families.

    > | INSTANCE_FAMILY, see [Snowflake Service Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf) | vCPU | Memory (GiB) | Storage (GB) | Bandwidth limit (Gbps) | GPU | GPU Memory per GPU (GB) | Node limit | Description |
    > | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    > | CPU_X64_XS | 1 | 6 | 100 | Up to 12.5 | n/a | n/a | 150 | Smallest instance available for Snowpark Containers. Ideal for cost-savings and getting started. |
    > | CPU_X64_S | 3 | 13 | 100 | Up to 12.5 | n/a | n/a | 150 | Ideal for hosting multiple services/jobs while saving cost. |
    > | CPU_X64_M | 6 | 28 | 100 | Up to 12.5 | n/a | n/a | 150 | Ideal for having a full stack application or multiple services |
    > | CPU_X64_SL (except China) | 14 | 54 | 100 | Up to 12.5 | n/a | n/a | 150 | For applications which need a large number of CPUs, memory and Storage. |
    > | CPU_X64_L | 28 | 116 | 100 | 12.5 | n/a | n/a | 150 | For applications which need an unusually large number of CPUs, memory and Storage. |
    > | HIGHMEM_X64_S | 6 | 58 | 100 | AWS and GCP: Up to 12.5, Azure: 8 | n/a | n/a | 150 | For memory intensive applications. |
    > | HIGHMEM_X64_M | 28 | AWS: 240, Azure and GCP: 244 | 100 | AWS: 12.5, Azure and GCP: 16 | n/a | n/a | 150 | For hosting multiple memory intensive applications on a single machine. |
    > | HIGHMEM_X64_SL (Azure and GCP, except GCP Dammam region) | 92 | 654 | 100 | 32 | n/a | n/a | 20 | Largest Azure or GCP high-memory machine available for processing large in-memory data. |
    > | HIGHMEM_X64_L (AWS only) | 124 | 984 | 100 | 50 | n/a | n/a | 150 | Largest AWS high-memory machine available for processing large in-memory data. |
    > | GPU_NV_S (AWS only, except Singapore, Switzerland North, Paris, and Osaka regions) | 6 | 27 | 300 (NVMe) | Up to 10 | 1 NVIDIA A10G | 24 | 150 | Our smallest NVIDIA GPU size available for Snowpark Containers to get started. |
    > | GPU_NV_M (AWS only, except gov regions, Singapore, Switzerland North, Paris, and Osaka regions) | 44 | 178 | 3.4 TB (NVMe) | 40 | 4 NVIDIA A10G | 24 | 10 | Optimized for intensive GPU usage scenarios like Computer Vision or LLMs/VLMs. |
    > | GPU_NV_L (AWS only, available only in AWS US West and US East non-gov regions by request; limited availability might be possible in other regions upon request) | 92 | 1112 | 6.8 TB (NVMe) | 400 | 8 NVIDIA A100 | 40 | On request | Largest GPU instance for specialized and advanced GPU cases like LLMs and Clustering, etc. |
    > | GPU_NV_XS (Azure only, except Switzerland North, UAE North, Central US, and UK South regions) | 3 | 26 | 100 | 8 | 1 NVIDIA T4 | 16 | 10 | Our smallest Azure NVIDIA GPU size available for Snowpark Containers to get started. |
    > | GPU_NV_SM (Azure only, except Central US region) | 32 | 424 | 100 | 40 | 1 NVIDIA A10 | 24 | 10 | A smaller Azure NVIDIA GPU size available for Snowpark Containers to get started. |
    > | GPU_NV_2M (Azure only, except Central US region) | 68 | 858 | 100 | 80 | 2 NVIDIA A10 | 24 | 5 | Optimized for intensive GPU usage scenarios like Computer Vision or LLMs/VLMs. |
    > | GPU_NV_3M (Azure only, except Central US, North Europe, and UAE North regions) | 44 | 424 | 100 | 40 | 2 NVIDIA A100 | 80 | On request | Optimized for memory-intensive GPU usage scenarios like Computer Vision or LLMs/VLMs. |
    > | GPU_NV_SL (Azure only, except Central US, North Europe, and UAE North regions) | 92 | 858 | 100 | 80 | 4 NVIDIA A100 | 80 | On request | Largest GPU instance for specialized and advanced GPU cases like LLMs and Clustering, etc. |
    > | GPU_GCP_NV_L4_1_24G (Google Cloud only) | 6 | 28 | 300 | Up to 16 | 1 NVIDIA L4 | 24 | 10 | Our smallest NVIDIA GPU size available for Snowpark Containers to get started. |
    > | GPU_GCP_NV_L4_4_24G (Google Cloud only) | 44 | 178 | 1200 | Up to 50 | 4 NVIDIA L4 | 24 | 10 | GPU usage scenarios like Computer Vision or LLMs. |
    > | GPU_GCP_NV_A100_8_40G (Google Cloud only, available only in GCP US Central1 and Europe West4 regions by request) | 92 | 654 | 2500 | Up to 100 | 8 NVIDIA A100 | 40 | On request | Optimized for memory-intensive GPU usage scenarios like Computer Vision or LLMs/VLMs. |

    Note the following:

    * The consumption table link in the first column heading provides information about the credit consumption rate for the specific `INSTANCE_FAMILY`.
    * The Node limit column indicates the maximum number of nodes a Snowflake account can provision for the specific `INSTANCE_FAMILY` type. Contact your account representative to increase the limit.

## Optional parameters

`FOR APPLICATION app_name`
:   Specifies the Snowflake Native App name. If specified, the compute pool can only be used by the native app. The [SHOW COMPUTE POOLS](show-compute-pools.md) command output includes the `is_exclusive` and `application` columns to indicate whether the compute pool is created exclusively for an app and provides the app name.

`AUTO_RESUME = { TRUE | FALSE }`
:   Specifies whether to automatically resume a compute pool when a service or job is submitted to it.

    * If AUTO_RESUME is FALSE, you need to explicitly resume the compute pool (using ALTER COMPUTE POOL RESUME) before you can
      start a service or job on the compute pool.
    * If AUTO_RESUME is TRUE, if you start a new service on a suspended compute pool, Snowflake starts the compute pool. Similarly,
      when you use a service either by invoking a service function or accessing ingress (see
      [Using a service](../../developer-guide/snowpark-container-services/working-with-services.md)), Snowflake starts the previously suspended compute pool and resumes
      the service.

    Default: TRUE

`INITIALLY_SUSPENDED = { TRUE | FALSE }`
:   Specifies whether the compute pool is created initially in the suspended state. If you create a compute pool with
    INITIALLY_SUSPENDED set to TRUE, Snowflake will not provision any nodes requested for the compute pool at the compute pool
    creation time. You can start the suspended compute pool using [ALTER COMPUTE POOL … RESUME](alter-compute-pool.md).

    Default: FALSE

`AUTO_SUSPEND_SECS = num`
:   Number of seconds of inactivity after which you want Snowflake to automatically suspend the compute pool. An inactive compute
    pool is one in which no services or jobs are currently active on any node in the pool. If `auto_suspend_secs` is set to 0,
    Snowflake does not suspend the compute pool automatically.

    Default: 3600 seconds

`TAG tag_name = 'tag_value' [ , tag_name = 'tag_value' , ... ]`
:   Specifies the [tag](../../user-guide/object-tagging/introduction.md) name and the tag string value.

    The tag value is always a string, and the maximum number of characters for the tag value is 256.

    For information about specifying tags in a statement, see [Tag quotas](../../user-guide/object-tagging/introduction.md).

`COMMENT = 'string_literal'`
:   Specifies a comment for the compute pool.

    Default: No value

`PLACEMENT_GROUP = placement_group_name`
:   Identifies the placement group of the compute pool. Use the [SHOW COMPUTE POOLS](show-compute-pools.md)
    and [DESCRIBE COMPUTE POOL](desc-compute-pool.md)
    commands to review the assignment of the compute pool into placement groups.

    You can also set `placement_group` to `DISTRIBUTED`. In this case, Snowflake attempts to distribute compute pool nodes across all available placement groups to maintain an even distribution across multiple placement groups so that the groups are more fault tolerant. For more information, see [Compute pool placement](../../developer-guide/snowpark-container-services/working-with-compute-pool.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE COMPUTE POOL | Account |  |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

Create a 1-node compute pool. This example command specifies the minimum required parameters:

```sqlexample
CREATE COMPUTE POOL tutorial_compute_pool
  MIN_NODES = 1
  MAX_NODES = 1
  INSTANCE_FAMILY = CPU_X64_XS;
```

The following command specifies the optional AUTO_RESUME parameter:

```sqlexample
CREATE COMPUTE POOL tutorial_compute_pool
  MIN_NODES = 1
  MAX_NODES = 1
  INSTANCE_FAMILY = CPU_X64_XS
  AUTO_RESUME = FALSE;
```
