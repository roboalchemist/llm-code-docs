# Source: https://novita.ai/docs/guides/gpu-instance-choose-a-gpu.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Choose a GPU?

## Introduction

Novita AI offers a variety of GPU container cloud computing specifications to meet different virtualization capability needs, supporting a wide range of business applications and service scenarios.

Each computing specification is divided into several families based on hardware capability differences. Each family utilizes different Intel processors, CPU/memory ratios, GPU cards, cloud disk types, and network card virtualization methods to achieve differentiated computing, storage, and network performance. Each family is further subdivided into various instance specifications, with higher specifications offering stronger performance.

## How to Choose a GPU

| Model     | Memory   | Single Precision (FP32) | Half Precision (FP16) | Description                                                                                                                                                                                                                                             |
| --------- | -------- | ----------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tesla P40 | 24 GB    | 11.76 T                 | 11.76 T               | Based on the earlier Pascal architecture, suitable for tasks requiring large memory and using versions of cuda before 11.x.                                                                                                                             |
| TITAN XP  | 12 GB    | 12.15 T                 | 12.15 T               | An older model under the Pascal architecture, a suitable entry-level choice for beginners.                                                                                                                                                              |
| 1080 Ti   | 11 GB    | 11.34 T                 | 11.34 T               | A product of the same generation as TITAN XP, suitable for entry-level users, though its 11 GB memory may be limiting in some cases.                                                                                                                    |
| 2080Ti    | 11 GB    | 13.45 T                 | 53.8 T                | Turing architecture GPU, offers good performance, especially suitable for mixed precision computing scenarios, with a high cost-performance ratio.                                                                                                      |
| V100      | 16/32 GB | 15.7 T                  | 125 T                 | A high-end product designed for professional computing scenarios, especially suitable for high half-precision computing tasks, leading the previous generation of compute cards.                                                                        |
| 3060      | 12 GB    | 12.74 T                 | About 24 T            | If the memory of 1080 Ti does not meet the requirements, 3060 provides a good alternative, especially suitable for beginners and requires the use of cuda 11.x.                                                                                         |
| A4000     | 16 GB    | 19.17 T                 | About 76 T            | Balanced memory and computing power, suitable for intermediate users. Requires the use of cuda 11.x environment.                                                                                                                                        |
| 3080Ti    | 12 GB    | 34.10 T                 | About 70 T            | Excellent performance output makes it an ideal choice for scenarios not requiring extreme memory. Requires the use of cuda 11.x.                                                                                                                        |
| A5000     | 24 GB    | 27.77 T                 | About 117 T           | High-performance GPU, suitable for scenarios requiring large memory and high half-precision computing power. Requires the use of cuda 11.x.                                                                                                             |
| 3090      | 24 GB    | 35.58 T                 | About 71 T            | Provides excellent performance and memory quota, suitable for a wide range of application scenarios, the first choice for cost-effectiveness. Requires the use of cuda 11.x.                                                                            |
| A40       | 48 GB    | 37.42 T                 | 149.7 T               | Huge memory capacity, computing power close to 3090, suitable for computing tasks with extremely high memory requirements. Requires the use of cuda 11.x.                                                                                               |
| A100 SXM4 | 40/80 GB | 19.5 T                  | 312 T                 | Top professional computing GPU, with huge memory and half-precision computing capability, suitable for the most complex computing tasks. Supports NVLink, optimized for multi-card parallel computing. Requires the use of cuda 11.x.                   |
| 4090      | 24 GB    | 82.58 T                 | 165.2 T               | A new generation high-performance GPU, provides excellent single precision and half precision computing capability, suitable for scenarios with high cost-performance ratio. Apart from relatively small memory, it has almost no obvious shortcomings. |

## Notes

* GPU instance prices and configuration options (system disk, data disk, public IP, etc.) can be viewed on the console page. These prices are for reference only, and the actual order on the Novita AI console shall prevail.
* Instance specifications vary by region and availability zone; please refer to the actual display on the console.
* GPU instances can only be changed within the same specification family. For detailed information, please refer to the document on modifying instance specifications.
* For purchasing instances, please refer to the sections on purchasing GPU container cloud computing instances and purchasing high-performance computing GPU instances.

**Actual supply is subject to the [GPU Market](https://novita.ai/gpu-instance/console/explore).**


Built with [Mintlify](https://mintlify.com).