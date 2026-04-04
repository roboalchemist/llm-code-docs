<!-- Source: https://docs.verda.com/storage/block-volumes/attaching-a-block-volume.md -->

# Attaching a block volume

## Attaching a block volume to an instance

### Attaching volume with existing data

First `Attach` the volume to the instance either during the instance creation, either via UI or the API.

After you have attached the volume, it should become available as a block device such as `/dev/vdb`.\
\
Next you will need to run these commands on your instance to start using a volume:

Replace `<TARGET>`with the volume target, e.g. `vdb` and `<DIR_NAME>` with the name of the directory you want to mount it to.

Create directory:

```bash
mkdir /mnt/<DIR_NAME>
```

Mount volume:

```bash
mount /dev/<TARGET> /mnt/<DIR_NAME>
```

Recommended: add volume to `fstab` (this will automatically mount the volume on every system startup):

```bash
echo "/dev/<TARGET> /mnt/<DIR_NAME> ext4 defaults,nofail 0 0" >> /etc/fstab
```

### Attaching new block device (with no data on it)

If you attach an empty block device, you will first need to format the device. The rest of the steps in the section [#attaching-volume-with-existing-data](#attaching-volume-with-existing-data "mention") are the same. Format volume (only needed once, e.g, if it's a new volume):

```bash
mkfs.ext4 /dev/<TARGET>
```

***

## Attaching a block volume to an instant cluster <a href="#attaching-a-block-volume-to-an-instance" id="attaching-a-block-volume-to-an-instance"></a>

{% hint style="info" %}
Currently instant clusters have fixed storage by default. Contact us via chat in the console or email us at <support@verda.com> if you need to adjust your cluster's storage.
{% endhint %}
