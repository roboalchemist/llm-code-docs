# Source: https://docs.portainer.io/2.33-lts/api/access.md

# Source: https://docs.portainer.io/2.33-lts/admin/environments/access.md

# Source: https://docs.portainer.io/2.33-lts/user/kubernetes/namespaces/access.md

# Source: https://docs.portainer.io/sts/api/access.md

# Source: https://docs.portainer.io/sts/user/kubernetes/namespaces/access.md

# Source: https://docs.portainer.io/api/access.md

# Source: https://docs.portainer.io/user/kubernetes/namespaces/access.md

# Manage access to a namespace

{% hint style="info" %}
Kubernetes role-based access control (RBAC) must be enabled and working before access control will work in Portainer.
{% endhint %}

From the menu select **Namespaces** then select **Manage access** on the same row as the namespace you want to manage.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/FFd3RJIpMnGvVdO3Evvx/manage-access-namespace.gif" alt=""><figcaption></figcaption></figure>

Select the users/teams who will have access then click **Create access**.

{% hint style="info" %}
Users or groups with cluster-wide roles (such as the Operator role) cannot be assigned to individual namespaces, as their cluster-wide nature applies to all namespaces in the environment.
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/nB3drRf6UOQBLe1VDQfA/2.20-namespaces-access-create.png" alt=""><figcaption></figcaption></figure>
