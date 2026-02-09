# Using Lambda's Managed Slurm -

Source: https://docs.lambda.ai/public-cloud/1-click-clusters/managed-slurm/

---

[1-click clusters](../../../tags/#tag:1-click-clusters)[slurm](../../../tags/#tag:slurm)

# Using Lambda's Managed Slurm

[See our video guide on using Lambda's Managed Slurm.](https://youtu.be/G2yFiZroW3g)

## Introduction to Slurm

Slurm is a widely used open-source workload manager optimized for high-performance computing (HPC) and machine learning (ML) workloads. When deployed on a Lambda 1-Click Cluster (1CC), Slurm allows administrators to create user accounts with controlled access, enabling individual users to submit, monitor, and manage distributed ML training jobs.

Slurm automatically schedules workloads across the 1CC, maximizing cluster utilization while preventing resource contention.

## Lambda's Slurm

The table below summarizes the key differences between Lambda's Managed and Unmanaged Slurm deployments on a 1CC:
Feature Managed Slurm ✓ Unmanaged Slurm ✗ Access only through login node ✓ ✗ (all nodes accessible) User `sudo`/ `root`privileges ✗ ✓ Lambda monitors Slurm daemons ✓ ✗ (customer is responsible) Lambda applies patches and upgrades ✓ (on request) ✗ (customer is responsible) Slurm support with SLAs ✓ ✗ Lambda Slurm configuration ✓ ✓ Slurm configured for high availability ✓ ✓ Shared `/home`across all nodes ✓ ✓ Shared `/data`across all nodes ✓ ✓

### Managed Slurm

When Lambda's Managed Slurm (MSlurm) is deployed on a 1CC:

-
All interaction with the cluster happens through the login node. Access to other nodes is restricted to help ensure cluster integrity and reliability.

-
Lambda monitors and maintains the health of Slurm daemons such as `slurmctld`and `slurmdbd`.

-
Lambda coordinates with the customer to apply security patches and upgrade to new Slurm releases, if requested.

-
Lambda provides support according to the service level agreements (SLAs) in place with the customer.

### Unmanaged Slurm

In contrast, on a 1CC with Unmanaged Slurm:

-
All nodes are directly accessible, and users have system administrator privileges ( `sudo`or `root`) across the cluster.

Warning

Workloads that run outside of Slurm might interfere with the resources managed by Slurm. Additionally, users with administrator access can make changes that render the 1CC unrecoverable. In such cases, Lambda might need to "repave" the 1CC, fully wiping and reinstalling the system.
