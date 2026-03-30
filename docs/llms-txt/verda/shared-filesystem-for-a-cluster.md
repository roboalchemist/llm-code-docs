# Source: https://docs.verda.com/storage/shared-filesystems-sfs/shared-filesystem-for-a-cluster.md

# Shared filesystem for a cluster

Clusters have a shared filesystem implementation which is better suited for cluster workloads. It is based on the `virtiofs` protocol that allows handling terabytes of data typically needed for clusters.

Cluster filesystems allow any kind of operation compatible with normal block storage, with better speed and compatibility than traditional filesystem workloads.

## Shared Filesystem Compatibility Table

Currently, cluster shared filesystems can only be used in clusters. We are working to make `virtiofs` shared filesystems available for instances as well.

<table data-full-width="false"><thead><tr><th>Compute Type / SFS type</th><th>Mounting to Instances</th><th>Mounting to Clusters</th></tr></thead><tbody><tr><td>Shared filesystem for instances (<code>NFS</code>)</td><td>✓ Supported</td><td>✓ Supported<br><sub>Can be mounted at any time</sub></td></tr><tr><td>Cluster shared filesystem (<code>virtiofs</code>)</td><td><mark style="color:$warning;">✕ Not supported</mark></td><td>✓ Supported<br><sub>Can only be mounted during cluster creation</sub></td></tr></tbody></table>

### Creating an instant cluster

When you create an instant cluster, we automatically create a `/home` shared filesystem which is available on the jumphost and all worker nodes. You can also select existing shared filesystems to be attached when you are creating an instant cluster. Refer to the [deploying-your-cluster](https://docs.verda.com/clusters/instant-clusters/deploying-your-cluster "mention") for more information.

{% hint style="info" %}
You can only mount shared filesystems from the same region as the cluster you are trying to create.
{% endhint %}

### Attaching existing cluster shared filesystem

Currently, it is not possible to attach cluster shared filesystem (`vertiofs`) to a cluster after it was created. You must attach any existing cluster shared filesystems during deployment.

### Mounting and unmounting cluster shared filesystem

{% hint style="info" %}
Replace \<SFS\_NAME> with the generated name of SFS when you created it.
{% endhint %}

1\. Create a directory to which you want to mount the SFS:

```bash
mkdir -p /mnt/<SFS_NAME>
```

2\. Mount the shared filesystem:

```bash
sudo mount -t virtiofs <SFS_NAME> /mnt/<SFS_NAME> 
```

### Using cluster shared filesystem in instances

You cannot attach and mount cluster shared filesystem to the instances. An alternative way is to create an NFS-based shared filesystem, attach it to the cluster, and then copy all files from the cluster shared filesystem to it. See [creating-a-shared-filesystem](https://docs.verda.com/storage/shared-filesystems-sfs/creating-a-shared-filesystem "mention") for more information.
