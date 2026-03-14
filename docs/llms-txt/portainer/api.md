# Source: https://docs.portainer.io/2.33-lts/admin/environments/add/api.md

# Source: https://docs.portainer.io/2.33-lts/admin/environments/add/swarm/api.md

# Source: https://docs.portainer.io/2.33-lts/admin/environments/add/docker/api.md

# Source: https://docs.portainer.io/sts/admin/environments/add/api.md

# Source: https://docs.portainer.io/sts/admin/environments/add/swarm/api.md

# Source: https://docs.portainer.io/sts/admin/environments/add/docker/api.md

# Source: https://docs.portainer.io/admin/environments/add/api.md

# Source: https://docs.portainer.io/admin/environments/add/swarm/api.md

# Source: https://docs.portainer.io/admin/environments/add/docker/api.md

# Connect to the Docker API

{% hint style="warning" %}
Connecting to the Docker API is a legacy option that does not support edge features or policy management. For most use cases, [the Edge Agent is recommended](https://docs.portainer.io/faqs/getting-started/why-do-we-recommend-using-the-edge-agent-instead-of-the-traditional-agent).
{% endhint %}

Before you begin, you will need to ensure that your Docker instance is configured to admit remote connections. To learn how to do this, refer to Docker's own documentation. Once Docker is configured, you will be able to connect either with or without TLS.

From the menu expand **Environment-related**, click **Environments**, then click **Add environment**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/bWERa8LPxJXdwb33Awvh/Add-env-new.gif" alt=""><figcaption></figcaption></figure>

Next, select **Docker Standalone** as the environment type then click **Start Wizard**. Under **More options**, select the **API** option and your platform, then enter the environment details using the table below as a guide:

<figure><img src="https://2837857291-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxdTQRpMuktD2l0URtOJO%2Fuploads%2FJMAr1ZbJhHQNzmxO915I%2F2.39-API-env-1.png?alt=media&#x26;token=96f989f5-4ead-4d90-b796-34978d44cb1c" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2837857291-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxdTQRpMuktD2l0URtOJO%2Fuploads%2Fjs1rXqlhDUttRY9cVVYU%2F2.39-API-env-2.png?alt=media&#x26;token=a8779a46-99e4-47a5-acf4-cc52de501253" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="280">Field/Option</th><th>Overview</th></tr></thead><tbody><tr><td>Name</td><td>Give the environment a descriptive name.</td></tr><tr><td>Docker API URL</td><td>Enter the DNS name or IP address to connect to the Docker host along with the port. When connecting without TLS, the default port is <code>2375</code>. When connecting with TLS, the default port is <code>2376</code>.</td></tr><tr><td>TLS</td><td>Toggle this option on if you wish to use TLS. Toggle it off if you don't want to use TLS.</td></tr><tr><td>Skip Certification Verification</td><td>Toggle this option on to skip the verification of the TLS certificate used by the Docker API. If this option is off, the below fields will not appear.</td></tr><tr><td>TLS CA certificate</td><td>Select your CA certificate.</td></tr><tr><td>TLS certificate</td><td>Select your certificate.</td></tr><tr><td>TLS key</td><td>Select the key that matches the certificate.</td></tr></tbody></table>

{% hint style="info" %}
Portainer expects TLS certificates and keys to be in PEM format.
{% endhint %}

As an optional step you can expand the **More settings** section to categorize the environment by adding it to a [group](https://docs.portainer.io/admin/environments/groups) or [tagging](https://docs.portainer.io/admin/environments/tags) it for better searchability.

{% hint style="info" %}
GPU configuration has been moved to [Host Setup](https://docs.portainer.io/user/docker/host/setup#other) and can be configured once the environment has been set up.
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/GJXA5epnBPo0wicDh3tU/2.18-environments-add-docker-moresettings.png" alt=""><figcaption></figcaption></figure>

When you're ready, click **Connect**. If you have other environments to configure click **Continue** to proceed, otherwise click **Close** to return to the list of environments.
