<!-- Source: https://namespace.so/docs/architecture/compute/machine-shapes -->

# Machine Shapes

Namespace provides flexible compute resources through a comprehensive selection of machine shapes designed to meet diverse workload requirements.
Machine shapes define the CPU, memory, and storage resources allocated to your compute instances, allowing you to optimize performance and cost for your specific use cases.

## Understanding Machine Shapes

Machine shapes in Namespace follow a simple **AxB** notation format, where **A** represents the number of virtual CPUs (vCPUs) and **B** represents the amount of memory in gigabytes (GB).
For example, a **4x16** machine shape provides 4 vCPUs and 16 GB of RAM.

This standardized format makes it easy to identify and select the appropriate resources for your workload, whether you're running lightweight development tasks or memory-intensive applications.

## Available Configurations

Linux and Windows have a common set of available shapes. MacOS instances use a distinct set of shapes that is explained [below](#macos-configurations).

### Standard shapes

For Linux and Windows, our standard shapes are multiples of 1 vCPU and 2GB RAM.
The list of standard shapes is:
**2x4** (minimum), **4x8** (small), **8x16** (medium), **16x32** (large), **32x64** (maximum).

### Non-Standard shapes

Namespace allows you to freely choose your shape configuration to best match your workflow requirements.
For example, you can grow your memory allocation to 64GB while keeping the vCPU count at 4, forming a 4x64 shape.

Non-standard shapes consume the per-minute cost of the smallest standard shape that contains them.
When billing an instance, Namespace calculates how many 1 vCPU x 2GB RAM units were consumed for that instance:

`unit_count = max(vCPU_count, RAM_GB / 2)`

Contact [support@namespace.so](mailto:support@namespace.so) if you have special shape requirements.

### High-Memory Instances

For workloads requiring exceptional memory capacity like data processing and analytics pipelines, Namespace offers extended memory configurations:

- **80 GB, 96 GB, 112 GB, 128 GB** - Extended memory options
- **256 GB, 384 GB, 512 GB** - High-memory instances for specialized workloads

**Note:** High-memory instances (over 64 GB) require special access and may not be available on all subscription plans. Contact [support@namespace.so](mailto:support@namespace.so) to request access to high-memory configurations.

### Shape Pricing

The following table assembles a list of the most common instance shapes for Linux.
The per-minute price for Linux AMD64 instances and Linux ARM64 instances is identical.

Linux

| vCPU | RAM | Machine shape | Multiplier | Prepaid | Overage |
| --- | --- | --- | --- | --- | --- |
| 1 vCPU | 2 GB | 1 vCPU2 GB | 1 | $0.001 / min | $0.0015 / min |
| 2 vCPU | 4 GB | 2 vCPU4 GB | 2 | $0.002 / min | $0.003 / min |
| 2 vCPU | 8 GB | 2 vCPU8 GB | 4 | $0.004 / min | $0.006 / min |
| 4 vCPU | 8 GB | 4 vCPU8 GB | 4 | $0.004 / min | $0.006 / min |
| 4 vCPU | 16 GB | 4 vCPU16 GB | 8 | $0.008 / min | $0.012 / min |
| 8 vCPU | 16 GB | 8 vCPU16 GB | 8 | $0.008 / min | $0.012 / min |
| 8 vCPU | 32 GB | 8 vCPU32 GB | 16 | $0.016 / min | $0.024 / min |
| 16 vCPU | 32 GB | 16 vCPU32 GB | 16 | $0.016 / min | $0.024 / min |
| 16 vCPU | 64 GB | 16 vCPU64 GB | 32 | $0.032 / min | $0.048 / min |
| 32 vCPU | 64 GB | 32 vCPU64 GB | 32 | $0.032 / min | $0.048 / min |
| 32 vCPU | 128 GB | 32 vCPU128 GB | 64 | $0.064 / min | $0.096 / min |
| 32 vCPU | 256 GB | 32 vCPU256 GB | 128 | $0.128 / min | $0.192 / min |
| 32 vCPU | 512 GB | 32 vCPU512 GB | 256 | $0.256 / min | $0.384 / min |

### Linux on Apple Silicon

Apple M4 Pro support for Linux workloads is available as an early access.

Linux on Apple Silicon

Shapes may differ during early access.

| vCPU | RAM | Machine shape | Multiplier | Prepaid | Overage |
| --- | --- | --- | --- | --- | --- |
| 6 vCPU | 14 GB | 6 vCPU14 GB | 18 | $0.018 / min | $0.027 / min |
| 12 vCPU | 28 GB | 12 vCPU28 GB | 36 | $0.036 / min | $0.054 / min |
| 12 vCPU | 56 GB | 12 vCPU56 GB | 54 | $0.054 / min | $0.081 / min |

During the early access, the shapes may still differ from the target shapes.

## Storage Allocation

Namespace automatically provisions ephemeral storage based on your selected machine shape. The storage allocation scales dynamically to ensure adequate disk space for your workload.

Linux & Windows Ephemeral Storage

| vCPU | RAM | Machine shape | Multiplier | Disk Size |
| --- | --- | --- | --- | --- |
| 1 vCPU | 2 GB | 1 vCPU2 GB | 1 | 40 GB |
| 2 vCPU | 4 GB | 2 vCPU4 GB | 2 | 48 GB |
| 2 vCPU | 8 GB | 2 vCPU8 GB | 4 | 64 GB |
| 4 vCPU | 8 GB | 4 vCPU8 GB | 4 | 64 GB |
| 4 vCPU | 16 GB | 4 vCPU16 GB | 8 | 96 GB |
| 8 vCPU | 16 GB | 8 vCPU16 GB | 8 | 96 GB |
| 8 vCPU | 32 GB | 8 vCPU32 GB | 16 | 160 GB |
| 16 vCPU | 32 GB | 16 vCPU32 GB | 16 | 160 GB |
| 16 vCPU | 64 GB | 16 vCPU64 GB | 32 | 288 GB |
| 32 vCPU | 64 GB | 32 vCPU64 GB | 32 | 288 GB |
| 32 vCPU | 128 GB | 32 vCPU128 GB | 64 | 544 GB |
| 32 vCPU | 256 GB | 32 vCPU256 GB | 128 | 1056 GB |
| 32 vCPU | 512 GB | 32 vCPU512 GB | 256 | 2080 GB |

For non-standard shapes, the provisioned ephemeral disk space for an instance is calculated using the following formula:

`disk_size = 32GB + (max(vCPU_count, RAM_GB / 2)) * 8GB`

## Windows Configurations

Windows instances follow the same set of supported shapes as Linux compute.
Compared to Linux, running a Windows instance incurs twice the associated per-minute cost:

Windows

| vCPU | RAM | Machine shape | Multiplier | Prepaid | Overage |
| --- | --- | --- | --- | --- | --- |
| 1 vCPU | 2 GB | 1 vCPU2 GB | 2 | $0.002 / min | $0.003 / min |
| 2 vCPU | 4 GB | 2 vCPU4 GB | 4 | $0.004 / min | $0.006 / min |
| 2 vCPU | 8 GB | 2 vCPU8 GB | 8 | $0.008 / min | $0.012 / min |
| 4 vCPU | 8 GB | 4 vCPU8 GB | 8 | $0.008 / min | $0.012 / min |
| 4 vCPU | 16 GB | 4 vCPU16 GB | 16 | $0.016 / min | $0.024 / min |
| 8 vCPU | 16 GB | 8 vCPU16 GB | 16 | $0.016 / min | $0.024 / min |
| 8 vCPU | 32 GB | 8 vCPU32 GB | 32 | $0.032 / min | $0.048 / min |
| 16 vCPU | 32 GB | 16 vCPU32 GB | 32 | $0.032 / min | $0.048 / min |
| 16 vCPU | 64 GB | 16 vCPU64 GB | 64 | $0.064 / min | $0.096 / min |
| 32 vCPU | 128 GB | 32 vCPU128 GB | 128 | $0.128 / min | $0.192 / min |
| 32 vCPU | 256 GB | 32 vCPU256 GB | 256 | $0.256 / min | $0.384 / min |
| 32 vCPU | 512 GB | 32 vCPU512 GB | 512 | $0.512 / min | $0.768 / min |

## macOS Configurations

macOS instances have specific vCPU and memory configurations optimized for Apple's architecture.
Below, you can find a table of supported shapes and the associated cost per minute.
For more details on how macOS instances are billed, check out [Billing and Limits →](/docs/workspaces/billing-and-limits).

MacOS

| vCPU | RAM | Machine shape | Multiplier | Prepaid | Overage |
| --- | --- | --- | --- | --- | --- |
| 6 vCPU | 14 GB | 6 vCPU14 GB | 60 | $0.06 / min | $0.09 / min |
| 12 vCPU | 28 GB | 12 vCPU28 GB | 120 | $0.12 / min | $0.18 / min |
| 12 vCPU | 56 GB | 12 vCPU56 GB | 180 | $0.18 / min | $0.27 / min |

Free space available in macOS instances scales with their shapes too. It starts at 48 GB and each 1x2 unit adds 8 GB.

MacOS Ephemeral Storage

| vCPU | RAM | Machine shape | Multiplier | Disk Size |
| --- | --- | --- | --- | --- |
| 6 vCPU | 14 GB | 6 vCPU14 GB | 7 | 104 GB |
| 12 vCPU | 28 GB | 12 vCPU28 GB | 14 | 160 GB |
| 12 vCPU | 56 GB | 12 vCPU56 GB | 28 | 272 GB |

## Billing and Cost Optimization

Machine shapes are billed on a per-minute basis with a one-minute minimum charge.
For more details on the usage and billing calculation, check out [Billing and Limits →](/docs/workspaces/billing-and-limits).

When trying to optimize performance and cost, picking the right shape is an important step:

- Larger shapes may shorten your workflow duration.
- Smaller shapes may be cheaper if your current machine type is oversized.
- Using standard shapes (ratio of 1vCPU : 2GB RAM) leads to better cost efficiency.

For assistance with machine shape selection, high-memory instance access, or performance optimization, reach out to our [support team](mailto:support@namespace.so).

### Unit minute accounting

We account for a minimum of 1 minute for each instance, but round the next 15 seconds down.
For example, 30 seconds of usage is 1 billable minute, 70 seconds is 1 billable minute, and 150 seconds are billed as 3 minutes.
Jobs that run on Windows or macOS consume minutes at a higher rate than jobs on Linux.
Unit minutes usage per shape and platform can be found above.

Last updated March 20, 2026
