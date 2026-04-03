# Filesystems -

Source: https://docs.lambda.ai/public-cloud/filesystems/

---

[storage ](../../tags/#tag:storage)
# Filesystems [# ](#filesystems)

A *filesystem *is a high-capacity regional file store you can attach to your instance to store datasets and back up system state. In most regions, each filesystem has a capacity of 8 EB (8,000,000 TB), and you can create up to 24 total filesystems. In the Texas, USA (us-south-1) region, filesystems are currently limited to 10 TB of capacity. 

For information on how filesystems are billed, see the [Billing overview ](../billing/#filesystems). 

## Accessing your filesystem [# ](#accessing-your-filesystem)

### Accessing from another instance or a 1-Click Cluster [# ](#accessing-from-another-instance-or-a-1-click-cluster)

To access a filesystem from within Lambda Cloud: 

- The filesystem must reside in the same region as the instance or cluster. 
- You must attach the filesystem to your instance or cluster at the time that the instance or cluster is launched. 
Note 

Filesystems cannot currently be transferred between regions.
