# Source: https://docs.curator.interworks.com/server_management/system_administration/disk_speed_metrics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Disk Speed Metrics

> Performance optimization guide covering disk speed benchmarking, cloud platform recommendations, and hardware upgrades to improve Curator system performance.

## Introduction

In the modern era of cloud computing, understanding disk speed is complex, yet paramount.

Without adequate disk read/write speeds, Curator can seem sluggish or even outright slow.

Improving disk speed benchmarks can be a complex combination of software configurations, hardware upgrades,
and understanding the underlying systems' operations.

## Benchmarking Basics

1. **The Dilemma**: Many users consider upgrading their machine CPU/RAM specifications as the primary
   solution to improve speed. However, increasing this hardware is only a part of the puzzle. Disk speed can be
   a huge factor in the performance of your Curator system.

2. **Windows vs. Linux**: It's essential to note that inherent differences exist between Windows and Linux
   regarding OS efficiencies. Typically, Windows systems have substantially slower disk speed test results
   compared to Linux counterparts because of operating system intricacies.

## Actionable Steps to Improve Disk Speed

1. **Cloud Platforms**: For those using cloud systems, such as AWS or Azure, different disk types and
   instance types offer varying speeds. It's imperative to choose configurations that align with your
   performance requirements. Increasing disk speed may be as easy as changing a few toggles!

2. **Instance Recommendations for AWS Users**:

   * **gp3 Volumes**: If you haven't already, switch your EBS volume to a gp3 EBS volume. AWS defaults to
     "gp2" type volumes,
     [but gp3 is more cost efficient AND faster.](https://aws.amazon.com/blogs/storage/migrate-your-amazon-ebs-volumes-from-gp2-to-gp3-and-save-up-to-20-on-costs/)
     It's literally a "win-win". EBS volumes using gp3 also allow you to configure both IOPS (Input/Output
     Operations Per Second) and Throughput, enabling better control over disk performance. Consider increasing
     these metrics to improve disk speed.

   * **IOPS (Input/Output Operations Per Second)**: This metric defines the number of read and write
     operations that the volume can perform per second. In simple terms, it's the "speed" of data
     transactions. A higher IOPS value usually leads to faster disk performance. When you increase the IOPS
     configuration, it can be beneficial for applications that require high random access, like Curator's
     database. If your individual read/write speeds are passing benchmarks, but the batch operations are not,
     increasing IOPS could be a good solution.

   * **Throughput**: This measures the volume's capacity to read and write data in megabytes per second
     (MB/s). It's essentially the "bandwidth" of data transactions. Throughput is especially important for
     applications that move large amounts of data.

   * **Instance Types**: Not all CPU types are created equal. Although it may seem unrelated, CPU resources
     are a large part of disk speed metrics. Utilizing newer, faster instance types can yield drastically
     better results than AWS's older instance types, usually for equivalent or better pricing. If possible,
     you may wish to investigate utilizing the newer ARM infrastructure, which will yield drastically faster
     performance.

3. **Instance Recommendations for Azure Users**:
   * **Disk Types**: Azure offers two types of SSD drives. Instead of "Standard SSD", use "Premium SSD" for production workloads.

   * **Instance Types**: Ensure that the instance type used for Curator is using modern CPU technology.
     Older CPU types are available, however, these are significantly slower than Azure's newer generation CPUs.
     Consider using Azure's 5-Series instance types, or better. A good starter instance is the "Standard\_D8ls\_v5".

4. **Instance Recommendations for Users of On-Prem Virtual Machines**:
   * **Dedicated Hardware**: Systems using shared resources can see wild swings in performance depending on
     the load of other systems in the virtual machine cluster. Curator recommends requesting dedicated CPU
     affinity when possible.

   * **vCPUs vs CPUs**: vCPUs can often be underpowered compared to physical CPU resources. A good rule of
     thumb is to consider 2 vCPUs to be roughly equivalent to 1 physical CPU resource. For example, to achieve
     the performance of a "4 core" environment, consider acquiring "8 vCPUs".

5. **Other Hardware Upgrades**:

   * **CPU/RAM**: Although it might seem unrelated, increasing CPU and RAM can significantly improve your
     read/write benchmarks, especially for Curator installations on Windows Server.

6. **Network Speed**:

   * **Importance in Cloud-Based Systems**: In cloud environments, network speed plays a large role in disk
     speed metrics. A capped disk speed due to low network speeds can hinder performance substantially.

   * **Cloud Vendor Specifications**: Depending on your cloud service provider, you might need to shift to a
     different instance type or family to achieve the desired network speed.

7. **Notes on Antivirus Software**:

   * One potential cause of filesystem speed issues is antivirus software. While this software is vitally
     important, it does introduce extra overhead, especially in regards to disk speed. To counter this effect,
     you may need to increase hardware requirements more than you'd expect to cover the hardware requirements
     of your antivirus software. (RAM/CPU/Disk Speed).

   * To add exclusions, you can either whitelist the entire Curator installation directory, or specific
     processes (particularly **libs\PHP\php.exe**, **libs\MariaDB\bin\mariadbd.exe**, and **libs\Apache24\bin\httpd.exe**)

8. **Windows Security Exclusions**:

   * Windows Security is particularly slow. Adding exclusions can make a huge difference on Windows systems,
     in particular. In some tests, disk speed benchmarks have dropped by as much as 75% by adding exclusions
     in the Windows Security software.

   * To add Windows Security exclusions, go to **Start**, then open **Settings** . Under
     **Privacy & security** , select **Virus & threat protection**. Under
     **Virus & threat protection settings**, select **Manage settings**, and then under **Exclusions**,
     select **Add or remove exclusions**.
     Ideally, whitelist the entire Curator install folder, or use the individual exclusions in the Antivirus section above.
