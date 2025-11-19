# Source: https://www.aptible.com/docs/core-concepts/scaling/cpu-isolation.md

# CPU Allocation

Learn how Aptible effectively manages CPU allocations to maximize performance and reliability

# Overview

Scaling up resources in Aptible directly increases the guaranteed CPU Allocation for a container. However, containers can sometimes burst above their CPU allocation if the underlying infrastructure host has available capacity. For example, if a container is scaled to a 4GB general-purpose container, it would have a 1 vCPU allocation or 100% CPU utilization in our metrics. You may see in your metrics graph that the CPU utilization bursts to higher values, like 150% or higher. This burst capability was allowed because the infrastructure host had excess capacity, which is not guaranteed. At other times, if your CPU metrics are flattening out at a usage of 100%, it likely signifies that the container(s) are being prevented from using more than their allocation because excess capacity is unavailable.

It's important to note that users cannot view the full CPU capacity of the host, so users must consider metric drains to monitor and alert on CPU usage to ensure that app services have adequate CPU allocation. To ensure a higher guaranteed CPU allocation, you must scale your resources.

# Modifying CPU Allocation

The guaranteed CPU Allocation can be increased or decreased by vertical scaling. See: [App Scaling](/core-concepts/scaling/app-scaling) or [Database Scaling](/core-concepts/scaling/database-scaling) for more information on vertical scaling.
