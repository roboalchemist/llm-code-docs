<!-- Source: https://docs.verda.com/cpu-and-gpu-instances/tips-and-tricks/best-ways-to-copy-files-between-two-block-devices.md -->

# Best ways to copy files between two block devices

There are several options on how to transfer data from one volume to another. In this article we will cover two that should cover most use cases.

## Option 1: dd to create a 'carbon copy' of volume

{% hint style="danger" %}
CARELESS USAGE OF `dd` CAN RESULT IN DATA LOSS\
\
`dd` overwrites the contents of the output file/device, please always double check that the if= points to input file/device, of= points to output file/device and those files/devices are not confused with other files/devices.
{% endhint %}

You can see the device path for each volume attached to instance in storage tab of selected instance

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-fe19ac69719a25cdcf41795a0f31314a45b08952%2Ftarget%20devices.png?alt=media" alt=""><figcaption></figcaption></figure>

To create a carbon copy of input device and write it to other device/file simply run:

```bash
dd if=/path/to/input of=/path/to/output bs=96M status=progress
```

If we were intending to clone OS-viJ5Hd2x to Volume-2th9Aa6j (see the above picture), the command would be:

```bash
dd if=/dev/vda of=/dev/vdb bs=96M status=progress
```

## Option 2: rsync to copy folders and files between two mounted volumes

{% hint style="info" %}
See [attaching-a-block-volume](https://docs.verda.com/storage/block-volumes/attaching-a-block-volume "mention") to know how to mount volume to system
{% endhint %}

{% hint style="info" %}
In this guide we will focus on copying to volumes that are mounted to system, therefore it will be considered local from rclone's point of view. You can also use

```bash
rclone config
```

to configure remote storage device to use with rclone. See [rclone docs](https://rclone.org/docs/) for more information.
{% endhint %}

First, install rclone, a powerful utility for copying files locally and from/to remote disks.

```bash
apt install rclone
```

Then the command to copy the files would be:

{% code overflow="wrap" fullWidth="false" %}

```bash
rclone copy --links --progress --metadata --ignore-checksum --log-file=/tmp/rclone-$( date -I ) --exclude="/excluded_dir/" SRC DST
```

{% endcode %}

Change SRC folder you want to copy, change DST to destination folder where files from SRC should go to and adapt the --exclude flags to what you want to exclude.\
\
In case you need maximum performance you can add some flags to the above command and adapt their values to your setup:

{% code overflow="wrap" %}

```bash
--transfers=8 --checkers=1 --multi-thread-streams=8 --multi-thread-cutoff 256Mi
```

{% endcode %}

Read more about these options at [rclone flags](https://rclone.org/flags/).
