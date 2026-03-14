# Source: https://docs.ox.security/get-started/onboarding-to-ox/source-control/github/getting-github-tokens.md

# Getting GitHub Tokens

When integrating with [GitHub](https://docs.ox.security/get-started/onboarding-to-ox/source-control/github) source control and [GitHub Issues](https://docs.ox.security/ticketing-and-messaging/ticket-management/github-issues), you need to get GitHub tokens.

**To get GitHub tokens:**

1. Log in to your GitHub account.
2. From your profile picture in the top-right corner select **Settings**, then scroll down and select **Developer settings**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-a807fe88c9396bae32f9688dff0c800992c90859%2FGH_dev_settings.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

1. In the **Developer settings** page, select **Personal access tokens > Tokens (classic)** and define the parameters as follows.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-14ad9f0d3e269543a30f500f31bb24d7c7f50e96%2FGH_dev_settings_access_token.png?alt=media" alt=""><figcaption></figcaption></figure>

| Parameter         | Description                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**          | A significant name that makes it easy to identify the purpose of the token.                                                                                                                                                                                                                                                                                                                  |
| **Expiration**    | Set the expiration date as far as possible.                                                                                                                                                                                                                                                                                                                                                  |
| **Select scopes** | <p>By selecting scopes you define the access permissions.<br></p><p>For GitHub source control - OX integration, select the following scopes:</p><ul><li>read:packages</li><li>write:org</li><li>read:org</li><li>read:repo\_hook</li><li>user:email</li></ul><p>For GitHub Issues - OX integration, select the following scopes:</p><ul><li>repo</li><li>read:user</li><li>project</li></ul> |

1. Select **Create token**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-17853548cd91ca96cdc3b4e7ce70536b004a36c1%2FGH_taken.png?alt=media" alt=""><figcaption></figcaption></figure>

1. Copy the token and store it in a different location.\
   After closing this dialog you cannot see it again.
