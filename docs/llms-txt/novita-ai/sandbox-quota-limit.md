# Source: https://novita.ai/docs/guides/sandbox-quota-limit.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Quota Limit

Currently, each user allows to create a maximum of **<u>100</u>** concurrent sandboxes by default. The quota can be adjusted based on your requirements after our evaluation.

If you need a higher quota, please <Link href="https://meet.brevo.com/novita-ai/contact-sales" taget="_blank">contact our support team</Link>.

## Agent Sandbox CPU and Memory Ratio Restrictions

When creating an Agent sandbox template, the system enforces constraints on the ratio between **CPU** and **memory**. These restrictions are designed to ensure the stability and resource efficiency of Agent sandboxes, and to avoid operational issues caused by unreasonable resource allocation.

### CPU Restrictions

* Supported CPU specification range: **1‒8 vCPU**
* Only integer values for CPU count are supported, such as: `1`, `2`, `4`, `8 vCPU`

### Memory Restrictions

* Maximum memory limit: **8192 MiB (8 GiB)**
* Memory must be an integer multiple of **512 MiB**, e.g.: `512 MiB`, `1024 MiB`, `2048 MiB`, etc.

### Ratio Rules

| Item          | Restriction Requirement | Description                                                                   |
| :------------ | :---------------------- | :---------------------------------------------------------------------------- |
| Minimum Ratio | 1:0.5 (CPU:Memory)      | Each 1 vCPU requires at least: 0.5 × 1024 = **512 MiB** memory                |
| Maximum Ratio | 1:4 (CPU:Memory)        | Each 1 vCPU can allocate up to: 4 × 1024 = **4096 MiB** memory                |
| Memory Step   | 512 MiB increments      | Memory must be a multiple of 512 MiB, e.g.: 512 MiB, 1024 MiB, 1536 MiB, etc. |

### Example Overview

| CPU Spec | Minimum Memory   | Maximum Value by Ratio | Actual Maximum Selectable |
| :------- | :--------------- | :--------------------- | :------------------------ |
| 1 vCPU   | 512 MiB          | 4096 MiB (4 GiB)       | 4096 MiB (4 GiB)          |
| 2 vCPU   | 1024 MiB (1 GiB) | 8192 MiB (8 GiB)       | 8192 MiB (8 GiB)          |
| 4 vCPU   | 2048 MiB (2 GiB) | 16384 MiB (16 GiB)     | 8192 MiB (8 GiB)          |
| 8 vCPU   | 4096 MiB (4 GiB) | 32768 MiB (32 GiB)     | 8192 MiB (8 GiB)          |

### Notes

* The above rules are only effective **when creating the <Link href="/guides/sandbox-template">sandbox template</Link>**. Sandboxes launched from this template will inherit its specifications.
* The memory upper limit is **8192 MiB (8 GiB)** by default; even if the calculated ratio exceeds this value, the actual selectable memory cannot surpass this limit.
* If the configuration is out of range, the system will prompt an error and the user needs to select again.
* It is recommended to reasonably choose the CPU to memory ratio according to your workload, to avoid OOM (out-of-memory) errors due to insufficient resources or wasting resources due to overallocation.


Built with [Mintlify](https://mintlify.com).