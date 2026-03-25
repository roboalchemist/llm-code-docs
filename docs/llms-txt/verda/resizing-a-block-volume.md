# Source: https://docs.verda.com/storage/block-volumes/resizing-a-block-volume.md

# Resizing a block volume

{% hint style="warning" %}
After resizing the block volume from the console, **you must shutdown and start the instance from the console** (in case it was not already shut down).\
\
**NOTE: Reboot doesn’t count - you must shutdown the instance.**
{% endhint %}

## Resizing the OS volume

The OS volume is resized automatically after the next system start. Please make sure you perform shutdown from the cloud console in order for the change in volume size to be detected during start-up.

### Resizing other block volumes

Run these commands on your instance to resize the non-OS volume.

Replace `<TARGET>` with the volume target e.g. `vdb`.

#### Instructions for EXT4 filesystem (default)

**If partitioned** (e.g. with OS volumes), that are also ext4 by default. The default partition number is 1):

```bash
growpart /dev/<TARGET> <PARTITION_NUMBER>
resize2fs /dev/<TARGET><PARTITION_NUMBER>
```

{% hint style="warning" %}
There's one space character between the parameters of the `growpart` command
{% endhint %}

**If not partitioned:**

```bash
resize2fs /dev/<TARGET>
```

#### Instructions for XFS filesystem

Same process as in [#instructions-for-ext4-filesystem-default](#instructions-for-ext4-filesystem-default "mention"), but replace `resize2fs` with `xfs_growfs`:

```bash
xfs_growfs /dev/<TARGET>
```

### Useful commands

To check if the volume is partitioned use:

```bash
lsblk
```

To check the filesystem type use:

```bash
df -hT
```
