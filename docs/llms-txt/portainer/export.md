# Source: https://docs.portainer.io/2.33-lts/user/docker/images/export.md

# Source: https://docs.portainer.io/sts/user/docker/images/export.md

# Source: https://docs.portainer.io/user/docker/images/export.md

# Export an image

You can export any Docker image stored on any node. This is useful when you need to move a container from one host to another, or simply make a backup of the images.

{% hint style="warning" %}
If you export a container to a tar file, the volumes won't get exported with it. You will need to save the data from those volumes using a different method.
{% endhint %}

From the menu select **Images**, select the image you want to export then click **Export this image**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/N2GmJQxzkqBA6OWIGEQS/Export-image-1.gif" alt=""><figcaption></figcaption></figure>

When the warning message appears, click **Continue**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/l2AXaqt7afdRJ2Pkt6d9/2.15-images-export-confirm.png" alt=""><figcaption></figcaption></figure>

When the image has downloaded, a success message will appear, and your browser should automatically download the resulting tar file.<br>
