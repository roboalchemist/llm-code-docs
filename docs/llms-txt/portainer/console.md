# Source: https://docs.portainer.io/2.33-lts/user/docker/containers/console.md

# Source: https://docs.portainer.io/sts/user/docker/containers/console.md

# Source: https://docs.portainer.io/user/docker/containers/console.md

# Access a container's console

From the menu select **Containers**, select the container then select **Console**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/ydk0cLR2M3CnFR0zxTAr/Container-console-new.gif" alt=""><figcaption></figcaption></figure>

Select the command and the user you want to give access to, then click **Connect**.

{% hint style="info" %}
For Alpine Linux containers, you must select the`/bin/ash` command.
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/Wu9tG73ZOXe10tfuNov7/2.15-docker_containers_container_console_execute.png" alt=""><figcaption></figcaption></figure>

If you need to define a command other than those provided, toggle the **Use custom command** option on. Once connected, you can run commands in the console the same as any other Linux system.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/ZisBQ0gnHCvfgASZzqNG/2.20-containers-console-connected.png" alt=""><figcaption></figcaption></figure>

To disconnect from the console session, click the **Disconnect** button.
