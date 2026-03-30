# Source: https://docs.verda.com/storage/shared-filesystems-sfs/mounting-a-shared-filesystem.md

# Mounting a shared filesystem

## Mounting to an instance

{% hint style="warning" %}
Only SFS that have been shared with instance can be mounted to this instance, see\
[Editing share settings](https://docs.verda.com/storage/shared-filesystems-sfs/editing-share-settings)
{% endhint %}

{% hint style="info" %}
Shared filesystem can obly be attached to the instance in the same region
{% endhint %}

{% hint style="info" %}
Replace \<SFS\_NAME> with the name of the directory you want to mount it to.\
Replace \<PSEUDO> with the filesystem's pseudopath. [Where to find pseudopath](#where-to-find-the-pseudopath)\
Replace \<DC> with the datacenter location (ex: `fin-01`)
{% endhint %}

1. Create a directory to which you want to mount the SFS:

```bash
mkdir -p /mnt/<SFS_NAME>
```

2. Mount the shared filesystem:

```bash
mount -t nfs -o nconnect=16 nfs.<DC>.datacrunch.io:<PSEUDO> /mnt/<SFS_NAME>
```

3. Add filesystem to the `/etc/fstab`, to have it mount on instance startup:

{% code overflow="wrap" %}

```bash
grep -qxF 'nfs.<DC>.datacrunch.io:/<PSEUDO> /mnt/<SFS_NAME> nfs defaults,nconnect=16 0 0' /etc/fstab || echo 'nfs.<DC>.datacrunch.io:/<PSEUDO> /mnt/<SFS_NAME> nfs defaults,nconnect=16 0 0' | sudo tee -a /etc/fstab
```

{% endcode %}

***

## Mounting to every node in a cluster

{% hint style="info" %}
Replace \<SFS\_NAME> with the name of the directory you want to mount it to.\
Replace \<PSEUDO> with the filesystem's pseudopath. [Where to find pseudopath](#where-to-find-the-pseudopath)\
Replace \<DC> with the datacenter location (ex: `fin-01`)
{% endhint %}

{% code overflow="wrap" %}

```bash
pdsh -a "sudo mkdir -vp /mnt/<SFS_NAME> && grep -qxF 'nfs.<DC>.datacrunch.io:/<PSEUDO> /mnt/<SFS_NAME> nfs defaults,nconnect=16 0 0' /etc/fstab || echo 'nfs.<DC>.datacrunch.io:/<PSEUDO> /mnt/<SFS_NAME> nfs defaults,nconnect=16 0 0' | sudo tee -a /etc/fstab && sudo mount /mnt/<SFS_NAME>"
```

{% endcode %}
