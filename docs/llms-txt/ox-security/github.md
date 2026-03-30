# Source: https://docs.ox.security/get-started/onboarding-to-ox/source-control/github.md

# GitHub

GitHub provides cloud-based hosting for software development and version control using Git. It offers distributed version control and source code management capabilities.

By connecting GitHub to OX, you enable the system to map your applications and scan them for security issues.

In addition, when connecting GitHub, GitHub Actions is a CI/CD platform that automates the build, test, and deployment pipeline.

Before deciding on the connection method you are going to use, learn about [the connection methods used in OX](https://docs.ox.security/get-started/onboarding-to-ox/source-control/connection-methods). The following connection methods are available:

* [GitHub App](#github-app)
* [Identity Provider](#identity-provider)
* [Token](#token)
* [OX Broker](https://docs.ox.security/get-started/onboarding-to-ox/prerequisites-and-access/ox-broker)

### GitHub Server Options

* **GitHub.com (Public SaaS)**: If you are using the public GitHub server, you can log in using either the Identity Provider or Token method. The Token method defaults to the public GitHub server address.
* **GitHub Enterprise (Private Server)**: If you are using a private GitHub instance, select the Token login option and provide your GitHub server URL.

## Connecting Multiple Accounts

You can connect multiple source control accounts within the same organization, securing them all under a single organization in the OX platform. For instance, you can connect multiple GitLab accounts under one organization using multiple token connections, multiple identity providers, or multiple apps connections.

Integrating with multiple accounts is especially beneficial for large organizations where different departments may need separate credentials to access different GitLab instances or other services. The integration is flexible and robust because you can combine different connection methods, such as using tokens for more sensitive accounts and apps and identity providers for less sensitive ones.

## Connecting using GitHub App

The GitHub App method offers a streamlined way to connect an OX platform account to GitHub. This method uses an application created by OX Security, which simplifies the connection process.

When using this method, you install the OX GitHub app into your GitHub organization. The app is granted permissions to access your GitHub data, allowing the OX platform to interact with your repositories.

**To connect with GitHub App:**

1. In the **OX** platform, go to **Connectors** and select **GitHub > GITHUB APP**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-d8debfd1eb5b33855b677aef380b9e229693f43e%2FGH_app_connection.png?alt=media" alt="" width="360"><figcaption></figcaption></figure>

1. Select **CONNECT**. You are automatically redirected to the source control system’s authentication dialog.
2. Login to GitHub. The **Install OX Security** dialog appears with the list of organizations that you have defined on GitHub.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-44504b421d58ba7402d27f5041aea355b45fee9d%2FGH_APP_connecting1.png?alt=media" alt="" width="388"><figcaption></figcaption></figure>

1. Select the organization with which you want to set the GitHub-OX integration.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-28edf4f43f0be89cfe4e586c821ecf20a3fc6125%2FGH_APP_connecting2.png?alt=media" alt="" width="259"><figcaption></figcaption></figure>

1. In the **Install & Authorize OX Security** dialog, select as follows:

* **All repositories:** Grants OX GITHUB APP permissions to all the GitHub repositories within the selected GitHub organization.
* **Only select repositories:** Select GitHub repositories to which you want to grants OX GITHUB APP permissions within the selected GitHub organization.

1. Select **Install & Authorize**. The connection is established and you are redirected back to OX Security, where the list of all the repositories that participate in the integration appears.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-1c5aef154f13badd37b9095f85209c5c49a34272%2Fselecting%20repos_no_title%20(1).png?alt=media" alt="" width="266"><figcaption></figcaption></figure>

1. Select the repos you want to scan and click **SAVE**.
2. (optional) [Select branches you want to scan within the selected repos.](https://docs.ox.security/scan-and-analyze-with-ox/scanning/multi-branch-support)
3. To connect more GitHub accounts to the same organization in the OX platform, select **Add another GitHub App +**, add the app and select **CONNECT**.

## Connecting using Identity Provider

The Identity Provider (IDP) method is another way to link GitHub to OX Security. This method relies on authentication services provided by GitHub or a third-party service. The user connects using their GitHub account credentials, allowing the OX platform to use GitHub as the identity provider for authentication.

**To connect with Identity Provider:**

1. In the **OX** platform, go to **Connectors** and select **GitHub > IDENTITY PROVIDER**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-46522ae18ee352447b5bd1af0952a6abe64e3951%2FGH_IDP_connecting1.png?alt=media" alt="" width="449"><figcaption><p><mark style="color:red;">need to replace this screenshot</mark></p></figcaption></figure>

1. Select **CONNECT**. You are automatically redirected to the source control system’s authentication dialog.
2. Log in to GitHub and grant permissions to access the data.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-cadbfe7a5305e4d8b9859efa782c0bc6c3d2b705%2FGH_IDP_connecting2.png?alt=media" alt="" width="348"><figcaption></figcaption></figure>

1. Select **Authorize oxsecurity**. The connection is established and you are redirected back to OX Security, where the list of all the repositories that participate in the integration appears.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-1c5aef154f13badd37b9095f85209c5c49a34272%2Fselecting%20repos_no_title%20(2).png?alt=media" alt="" width="266"><figcaption></figcaption></figure>

1. Select the repos you want to scan and select **SAVE**.
2. (optional) [Select branches you want to scan within the selected repos.](https://docs.ox.security/scan-and-analyze-with-ox/scanning/multi-branch-support)
3. To connect more GitHub accounts to the same organization in the OX platform, select **Add another Identity Provider +**, set the required parameters and select **CONNECT**.

## Connecting using Token

The Token method provides the most flexibility for connecting GitHub to OX Security. In this method, users generate an API token in GitHub, which serves as a security credential to allow OX Security access to specific repositories and actions.

**To connect with Token:**

1. [Get a GitHub token.](https://docs.ox.security/get-started/onboarding-to-ox/source-control/github/getting-github-tokens)
2. In the **OX** platform, go to **Connectors** and select **GitHub > TOKEN**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-b8474369b2f51bce151b9731abe6f5f0cab893e4%2FGH_SC_Token.png?alt=media" alt="" width="359"><figcaption></figcaption></figure>

1. In the **Configure your GitHub credentials** dialog, set the following parameters:

   | Parameter           | Description                                                                                                         |
   | ------------------- | ------------------------------------------------------------------------------------------------------------------- |
   | **GitHub Host URL** | Add your GitHub organization account URL.                                                                           |
   | **Token**           | Paste the GitHub token you have created.                                                                            |
   | **Token Name**      | <p>The token name is automatically generated by OX app.<br>You can change/edit the connection name at any time.</p> |
2. To select specific repositories for scanning by OX platform, select the gear icon next to **DELETE**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-07f73b8b0e9278c5539a519850d40be46afae27e%2Fgear_icon.png?alt=media" alt="" width="321"><figcaption></figcaption></figure>

1. Select the repos you want to protect.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-1c5aef154f13badd37b9095f85209c5c49a34272%2Fselecting%20repos_no_title.png?alt=media" alt="" width="266"><figcaption></figcaption></figure>

1. Select **SAVE**.
2. (optional) [Select branches you want to scan within the selected repos.](https://docs.ox.security/scan-and-analyze-with-ox/scanning/multi-branch-support)
3. To connect more GitHub accounts to the same organization in the OX platform, select **Add another Token +**, set the required parameters and select **CONNECT**.
