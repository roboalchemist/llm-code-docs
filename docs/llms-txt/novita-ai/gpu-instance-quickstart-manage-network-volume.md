# Source: https://novita.ai/docs/guides/gpu-instance-quickstart-manage-network-volume.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage Network Volume

"Network Volume" can provide multi-instance shared storage space for GPU container instances, with the characteristics of large capacity and multi-instance sharing. Network volumes are billed on a per-second basis. Please note that if your account is in arrears and no instances are running, your Network Volume will be **released 3 days later**. Network Volume is provided in the pursuit of running tasks using its GPUs and is **not meant to be a long-term backup solution**. It is highly advisable to continually back up anything you want to save offsite locally or to a cloud provider.

## Create Network Volume

1. Go to the <a href="https://novita.ai/gpu-instance/console/storage">Console - Storage</a> page and click on "+ New Network Volume".
2. Select the "Data Center" where the Network Volume will reside. The "Data Center" is tightly bound to your instance and currently does not support cross-Data Center mounting of Network Volumes to instances.
3. Enter the "Volume Name" and capacity in GB for the Network Volume partition, and click "Save" after verifying that the details are correct.

## Edit Network Volume

You can edit your Network Volume through the console as follows:

1. Go to the <a href="https://novita.ai/gpu-instance/console/storage">Console - Storage</a> page, locate the Network Volume you plan to expand, and click the "..." button in the upper right corner.
2. Click the "Edit" button to modify the Network Volume configuration.

<Warning>
  Please note that we currently only support the expansion of the Network Volume capacity, and the storage capacity cannot be less than the size before modification.
</Warning>

## Delete Network Volume

You can delete your Network Volume through the console as follows:

1. Go to the <a href="https://novita.ai/gpu-instance/console/storage">Console - Storage</a> page, locate the Network Volume you plan to delete, and click the "..." button in the upper right corner.
2. Click the "Delete" button to delete the Network Volume.

<Warning>
  Please note that deletion of a Network Volume is irreversible. Once deleted, all data stored on it **will be permanently lost**, please proceed with caution.
</Warning>


Built with [Mintlify](https://mintlify.com).