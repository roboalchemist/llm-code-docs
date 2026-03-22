<!-- Source: https://docs.verda.com/storage/block-volumes/cloning-a-block-volume.md -->

# Cloning a block volume

Cloning a volume will duplicate all of its data onto a new volume. A volume can be cloned from the settings menu on the right side of the card.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-2c5deddfd7c41c2509a9acfbdc40943b5901babe%2Fclone.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Volumes must either be **detached** or the instance to which it is attached must be **shutdown**.
{% endhint %}

Volumes can be cloned across datacenter locations. For example, a volume in **FIN-01** can be cloned to **FIN-03**. Volumes can also be cloned from NVMe to HDD and vice versa. This allows you to move data to more cost-effective HDD storage when it isn't actively needed.

<div align="center"><figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2FJ0mG492w7CfkdBDC9Zfp%2Fimage.png?alt=media&#x26;token=29811326-f2de-4d27-b295-9bdca1f4ef22" alt="" width="314"><figcaption></figcaption></figure></div>

{% hint style="info" %}
If you clone an OS volume and convert it to HDD, it can no longer be used as a boot volume.
{% endhint %}
