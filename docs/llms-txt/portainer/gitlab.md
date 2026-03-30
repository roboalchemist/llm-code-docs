# Source: https://docs.portainer.io/2.33-lts/admin/registries/add/gitlab.md

# Source: https://docs.portainer.io/sts/admin/registries/add/gitlab.md

# Source: https://docs.portainer.io/admin/registries/add/gitlab.md

# Add a GitLab registry

From the menu select **Registries** then click **Add registry** and select **GitLab** as the registry provider.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/SVNqQ00aB8jMaGV9sUPE/Add-registry-GitLab-new.gif" alt=""><figcaption></figcaption></figure>

Complete the form, using the table below as a guide.

| Field/Option                   | Overview                                                                                                                                                         |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Username                       | Enter the username you use to log into your GitLab registry.                                                                                                     |
| Personal Access Token          | Enter the personal access token that corresponds to the username above. Your personal access token will need the `read_api` and `read_registry` scopes assigned. |
| Override default configuration | If you need to make changes to the Portainer defaults for GitLab, you can do so here.                                                                            |

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/mnn0xRt9qdxn3ZvQahmo/GitLab-registry.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
For more information about creating a personal access token, see [Gitlab's own documentation](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html).
{% endhint %}

When the form is complete, click **Add registry**.
