# Source: https://docs.portainer.io/2.33-lts/user/account-settings.md

# Source: https://docs.portainer.io/sts/user/account-settings.md

# Source: https://docs.portainer.io/user/account-settings.md

# Account settings

To get access to and update your user settings, click your username in the top-right of the Portainer UI and select **My account**.

<figure><img src="https://2837857291-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxdTQRpMuktD2l0URtOJO%2Fuploads%2FenlJjfzMdqKbATEGUDRG%2F2.39-account-settings.gif?alt=media&#x26;token=f5050c63-6611-4bce-bfa8-f64e5587a67c" alt=""><figcaption></figcaption></figure>

## Changing the theme

Portainer lets you choose between light, dark and high-contrast themes, or to auto-select the theme based on your system theme. The chosen theme applies only to this user.

Select a theme from the options. The change will be automatically applied.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/XxRQxWYLqxDp0mTF0oAw/2.32-myaccount-theme.png" alt=""><figcaption></figcaption></figure>

## Changing your password

Enter the following details, using the table below as a guide. When you're finished, click **Update password**.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/eGpz78ARNknemA5M0KhE/2.15-accountsettings-changepw.png" alt=""><figcaption></figcaption></figure>

| Field/Option     | Overview                                                    |
| ---------------- | ----------------------------------------------------------- |
| Current password | Enter the password you currently use to log into Portainer. |
| New password     | Enter a new password for your account.                      |
| Confirm password | Enter the new password again.                               |

[Minimum password length requirements](https://docs.portainer.io/admin/settings/authentication) are set by the administrator.

## Application settings

In this section you can enable or disable front-end data caching for your Kubernetes environments. When this this option is enabled, Portainer will cache data provided about your Kubernetes cluster in the front-end in order to improve load times when viewing the cluster. This caching can however mean that you may not see fully up-to-date information, and changes made by other users or outside of Portainer may take up to five minutes to update in your session.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/GcLUg5T2loWPcUpyueeo/2.20-account-application.png" alt=""><figcaption></figcaption></figure>

## Access tokens

This section allows you to manage your API access tokens. You can see a list of the access tokens that exist for your user as well as add and remove tokens as required.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/9w0XZjIRT0ElKgJLSAB4/2.15-accountsettings-apitokens.png" alt=""><figcaption></figcaption></figure>

For more information on access tokens, refer to our [API access documentation](https://docs.portainer.io/api/access#creating-an-access-token).

## Git credentials

This section lets you manage your saved Git credentials for use in deployments. These credentials are available only to your user.

{% hint style="info" %}
This feature is only available in Portainer Business Edition.
{% endhint %}

{% hint style="info" %}
Adding shared Git credentials can be done from the [Shared credentials](https://docs.portainer.io/admin/settings/credentials) view.
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/v4bwsNEaioHgJ9of14nC/2.16-account-gitcreds.png" alt=""><figcaption></figcaption></figure>

To add a new credential, click the **Add git credential** button and fill out the fields using the table below as a guide:

| Field                 | Overview                                                                                                                                                                                |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                  | Enter a name for this credential entry. This is how it will appear when selecting it for use when deploying.                                                                            |
| Authorization type    | Select either **Basic** or **Token** authorization depending on what your Git repository requires. For example, GitHub uses Basic authorization and Bitbucket uses Token authorization. |
| Username              | Enter the username, if relevant.                                                                                                                                                        |
| Personal Access Token | Enter the personal access token.                                                                                                                                                        |

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/7pW3XT9lKfRd020mlWtf/2.33-account-git-creds-new.png" alt=""><figcaption></figcaption></figure>

Once you've entered the relevant details, click **Save git credential** to save the entry.

## Helm repositories

By default, Portainer ships with the [Bitnami Helm chart repository](https://bitnami.com/stacks/helm) already pre-configured. In this section you can add additional Helm repositories to reference when deploying Helm charts.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/HvJh3QcqnZIFfoZvujZl/2.20-account-helmrepos.png" alt=""><figcaption></figcaption></figure>

If you would like to add an additional third-party repo, click on **Add Helm repository**, enter the repository URL and click **Save Helm repository**.

{% hint style="info" %}
Repositories added here are only available to your user. You can configure a Helm repository that will be available to all users in [Settings](https://docs.portainer.io/admin/settings/general#helm-repository).
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/9QTtnSoYu85hp3PUz6XF/2.20-account-helmrepos-add.png" alt=""><figcaption></figcaption></figure>
