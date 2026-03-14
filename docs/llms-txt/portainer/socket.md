# Source: https://docs.portainer.io/2.33-lts/admin/environments/add/podman/socket.md

# Source: https://docs.portainer.io/2.33-lts/admin/environments/add/swarm/socket.md

# Source: https://docs.portainer.io/2.33-lts/admin/environments/add/docker/socket.md

# Source: https://docs.portainer.io/sts/admin/environments/add/podman/socket.md

# Source: https://docs.portainer.io/sts/admin/environments/add/swarm/socket.md

# Source: https://docs.portainer.io/sts/admin/environments/add/docker/socket.md

# Source: https://docs.portainer.io/admin/environments/add/podman/socket.md

# Source: https://docs.portainer.io/admin/environments/add/swarm/socket.md

# Source: https://docs.portainer.io/admin/environments/add/docker/socket.md

# Connect to the Docker Socket

{% hint style="warning" %}
Connecting to the Docker Socket is a legacy option that does not support edge features or policy management. For most use cases, [the Edge Agent is recommended](https://docs.portainer.io/faqs/getting-started/why-do-we-recommend-using-the-edge-agent-instead-of-the-traditional-agent).
{% endhint %}

Connecting to the Docker socket directly can only be done from the local environment. Before you begin, ensure the user running the Portainer Server container has permissions to access the Docker socket.

From the menu expand **Environment-related**, click **Environments**, then click **Add environment**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/bWERa8LPxJXdwb33Awvh/Add-env-new.gif" alt=""><figcaption></figcaption></figure>

Next, select **Docker Standalone** as the environment type then click **Start Wizard**. Under **More options**, select the **Socket** option and your platform. You will be shown the required parameter to pass to the Portainer container as part of your `docker run` command.

Fill out the fields based on the table below.

<figure><img src="https://2837857291-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxdTQRpMuktD2l0URtOJO%2Fuploads%2FIFTRQjLNr8yPFAt1zovF%2F2.39-socket-env-1.png?alt=media&#x26;token=f2a5fb58-e730-4a26-a44d-79c8a78674b4" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2837857291-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxdTQRpMuktD2l0URtOJO%2Fuploads%2FSDOieV6sYnUqPtg1Rgbt%2F2.39-socket-env-2.png?alt=media&#x26;token=3dac19f2-a020-463d-a127-dfd244a5e2f4" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="280">Field/Option</th><th>Overview</th></tr></thead><tbody><tr><td>Name</td><td>Give the environment a descriptive name.</td></tr><tr><td>Override default socket path</td><td>Toggle this option on to override the default <code>/var/run/docker.sock</code> socket path.</td></tr><tr><td>Socket Path</td><td>If <strong>Override default socket path</strong> is enabled, enter the path to the Docker socket.</td></tr></tbody></table>

{% hint style="info" %}
Ensure that if you change the Socket Path, that you update the required bind mount parameter above to suit.
{% endhint %}

As an optional step you can expand the **More settings** section to categorize the environment by adding it to a [group](https://docs.portainer.io/admin/environments/groups) or [tagging](https://docs.portainer.io/admin/environments/tags) it for better searchability.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/GJXA5epnBPo0wicDh3tU/2.18-environments-add-docker-moresettings.png" alt=""><figcaption></figcaption></figure>

When you're ready, click **Connect**. If you have other environments to configure click **Continue** to proceed, otherwise click **Close** to return to the list of environments.
