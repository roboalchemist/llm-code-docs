# Source: https://docs.ox.security/get-started/onboarding-to-ox/source-control/bitbucket.md

# Bitbucket

Integrate Bitbucket Cloud with OX to centralize repository security findings alongside container, pipeline, cloud, and runtime signals already in OX.

OX scans Bitbucket repositories on a schedule and on demand, enriches findings with OX context (application mapping, workflows, and compliance), and presents a unified queue for investigation and reporting.

After you connect, Bitbucket scan results appear in the Active issues page (use the filter\
**Source tool > Bitbucket Cloud**).

## What OX adds

* **Context and correlation:** OX maps Bitbucket findings to applications, services, and teams to show impact and ownership.
* **Prioritization with severity factors:** OX may reprioritize scanner severities when exploitability and environment context reduce risk (for example, Critical → High). Severity factors explain why the priority changed.
* **Evidence at a glance:** When available, OX displays scanner evidence, file locations, and remediation guidance alongside OX analytics to speed triage.

## Terminology mapping

Bitbucket and OX use different labels for similar concepts. Use this quick map while you work.

<table><thead><tr><th width="255.2222900390625">Bitbucket Cloud</th><th>OX Security</th></tr></thead><tbody><tr><td>Pipelines</td><td>CI/CD Pipelines</td></tr><tr><td>Repositories</td><td>Applications</td></tr></tbody></table>

## Connection methods

For general information about connection methods, see the article [Connection methods](https://docs.ox.security/get-started/onboarding-to-ox/source-control/connection-methods).

There are three options to connect Bitbucket Cloud to OX.

<table><thead><tr><th width="247.0740966796875" valign="top">Connection Method</th><th valign="top">Details</th></tr></thead><tbody><tr><td valign="top"><a href="#connect-with-the-ox-bitbucket-app">Bitbucket App </a>(recommended)</td><td valign="top">Use the OX-created application for streamlined connection with app-level permissions. Simplifies installation and authorization.</td></tr><tr><td valign="top"><a href="#connect-with-identity-provider">Identity Provider</a></td><td valign="top">Use your existing connection for centralized authentication.</td></tr><tr><td valign="top"><a href="#connect-with-username-and-password">User name and password</a></td><td valign="top">Use Bitbucket app passwords for basic authentication with granular permission control.</td></tr></tbody></table>

## Prerequisites

#### Prerequisites for all connection methods

| Prerequisite           | Description                                                    |
| ---------------------- | -------------------------------------------------------------- |
| OX permissions         | Permission to configure connectors                             |
| Bitbucket Cloud access | Access to the Bitbucket Cloud workspace(s) you want to connect |

#### Additional prerequisites by connection method

<table><thead><tr><th width="244.851806640625" valign="top">Connection Method</th><th valign="top">Prerequisites</th></tr></thead><tbody><tr><td valign="top">Bitbucket app</td><td valign="top">Permission to install apps in the workspace</td></tr><tr><td valign="top">Identity provider (IdP)</td><td valign="top">Access to Bitbucket Cloud using an OAuth connection and Bitbucket Cloud administrator access</td></tr><tr><td valign="top">User name and password</td><td valign="top">Bitbucket account with permission to generate app passwords</td></tr></tbody></table>

## Connect with the OX Bitbucket app

The Bitbucket App method uses an OX-created application to simplify connection. The app requests read access to repositories and branches, pull requests, and pipeline configuration results.

1. Verify that the [prerequisites](#prerequisites) are in place.
2. In OX, go to **Connectors** and select **Bitbucket Cloud > BITBUCKET APP**.<br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-c43d5468e1b9ed0e0d2945a28fbc1c39c9bd21c2%2Fbitbucket%20cloud%20app%20configure%20screen.png?alt=media" alt=""><figcaption></figcaption></figure></div>
3. Select **CONNECT**. OX validates the credentials.
4. The **Grant access** dialog opens.<br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-5353a8a38432e3bc6fc0ef69255b6e7606f8d873%2FBitbucket%20cloud%20app%20grant%20access.png?alt=media" alt="" width="377"><figcaption></figcaption></figure></div>
5. In **Configure your Bitbucket Cloud connector**, select the repos you want OX to scan.<br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-1ae5d9a27f31a5417c4d84263f016ab755dabdd6%2FBitbucket%20cloud%20app%20choose%20repos.png?alt=media" alt="" width="327"><figcaption></figcaption></figure></div>
6. Select **SAVE**.
7. In **Configure your Bitbucket Cloud credentials**, select **VERIFY CONNECTIVITY.**<br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-2aa8fa8529a4db1de2a11fd1a2206301aaf4973b%2FBitbucket%20cloud%20app%20verify%20connectivity.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

A green success message at the bottom of the screen indicates a successful connection. If verification fails, check your credentials and permissions.

#### Optional configurations

* To change the repositories OX scans and monitors, see the section [Change the repositories OX scans](#change-the-repositories-ox-scans).
* To connect more Bitbucket accounts to the same organization in the OX platform, see the section [Connect multiple Bitbucket accounts](#connect-multiple-bitbucket-accounts).

## Connect with Identity Provider

1. Verify that the [prerequisites](#prerequisites) are in place.
2. In OX, go to **Connectors** and select **Bitbucket Cloud > IDENTITY PROVIDER**.<br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-4b73a89930f4251d973dbb1d316d8697c20d4bc1%2FBitbucket%20cloud%20%E2%80%93%20identity%20provider%20configure.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
3. Select **CONNECT**. OX validates the credentials.
4. In **Confirm access to your account**, select **Grant access**.<br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-ebccb0a347479e99f6b77cfccad372f954fd3a81%2FBitbucket%20cloud%20grant%20access.png?alt=media" alt="" width="447"><figcaption></figcaption></figure></div>
5. In **Configure your Bitbucket connector**, select the repos you want OX to scan.<br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-a0e69c2ee438c04364ac41ae3e17d19c48dce48b%2Fbitbucket%20cloud%20select%20repos.png?alt=media" alt="" width="327"><figcaption></figcaption></figure></div>
6. Select **SAVE**.
7. In **Configure your Bitbucket credentials**, select **VERIFY CONNECTIVITY**.\
   A green checkmark indicates a successful connection. If verification fails, check your credentials and permissions.

#### Optional configurations

* To change the repositories OX scans and monitors, see the section [Change the repositories OX scans](#change-the-repositories-ox-scans).
* To connect more Bitbucket accounts to the same organization in the OX platform, see the section [Connect multiple Bitbucket accounts](#connect-multiple-bitbucket-accounts).

## Connect with user name and password

**Step 1: Create password and permissions \[Bitbucket]**

For information on creating a password, see the Bitbucket article[Create an app password](https://support.atlassian.com/bitbucket-cloud/docs/create-an-app-password/).\
You can also get the link from the OX UI. Click the link **HELP CONNECTING A PASSWORD**.

<div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-6f641a6719499fcb5a68b3033886ccbb39ad0c39%2FBitbucket%20cloud%20create%20password%20help%20link.png?alt=media" alt=""><figcaption></figcaption></figure></div>

1. Verify that the [prerequisites](#prerequisites) are in place.
2. Log in to your Bitbucket Cloud workspace.
3. Go to **Settings > Personal settings > App passwords**.
4. Select **Create app password**.
5. Enter a meaningful label (for example, OX Security Integration).
6. Select the required permissions:
   * Account: Read and Write
   * Workspace memberships: Read and Write
   * Projects: Write and Admin
   * Repositories: Write and Admin
   * Pull requests: Read and Write
   * Issues: Read and Write
   * Snippets: Read
   * Webhooks: Read and Write
   * Pipelines: Read
   * Runners: Read
7. Select **Create**.
8. Copy and store the app password in a secure location. You cannot view it again.

> **Best practice:** Store credentials in a secrets manager and set a reminder to rotate it according to your policy.

**Step 2: Connect to OX \[OX]**

1. Go to **Connectors** and select **Bitbucket Cloud > USER NAME AND PASSWORD**.<br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-76f00e4e8ca4a9d78ebe19be20adcde709ad37c4%2FBitbucket%20cloud%20username%20and%20password%20(1).png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
2. Enter the following parameters.

<table><thead><tr><th width="260.407470703125" valign="top">Parameter</th><th valign="top">Details</th></tr></thead><tbody><tr><td valign="top">Bitbucket Cloud Host URL</td><td valign="top">https://api.bitbucket.org/2.0 (system-generated</td></tr><tr><td valign="top">User Name</td><td valign="top">Your Bitbucket name</td></tr><tr><td valign="top">Password</td><td valign="top">Your Bitbucket password</td></tr><tr><td valign="top">Connection Name</td><td valign="top">Enter a meaningful name</td></tr></tbody></table>

1. Select **CONNECT**. OX validates the credentials.
2. In **Configure your Bitbucket connector**, select the repos you want OX to scan.<br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-a0e69c2ee438c04364ac41ae3e17d19c48dce48b%2Fbitbucket%20cloud%20select%20repos.png?alt=media" alt="" width="327"><figcaption></figcaption></figure></div>
3. Select **SAVE**.
4. In **Configure your Bitbucket credentials**, select **VERIFY CONNECTIVITY**.\
   A green checkmark indicates a successful connection. If verification fails, check your credentials and permissions.

#### Optional configurations

* To change the repositories OX scans and monitors, see the section [Change the repositories OX scans](#change-the-repositories-ox-scans).
* To connect more Bitbucket accounts to the same organization in the OX platform, see the section [Connect multiple Bitbucket accounts](#connect-multiple-bitbucket-accounts).

## Change the repositories OX scans

Once you have a connection, you can change the repositories that OX scans and monitors.

1. Use the **Gear** icon at the bottom of the Configuration screen.
2. OX displays the locations or objects that OX scans and monitors.
3. Change the selection as needed.
4. Select **SAVE**.

<div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-1258743af4005adcc8366578f78e9576a3952305%2Funknown%20(24).png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>

## Connect multiple Bitbucket accounts

You can connect multiple Bitbucket Cloud accounts within the same OX organization. OX secures all accounts under a single organization, and each account can use a different connection method.

This setup is useful for large organizations where different teams manage separate Bitbucket Cloud workspaces or require different authentication models. You can combine connection methods—for example:

* Use the Bitbucket app for streamlined setup and app-level access.
* Use username and password/token for accounts that do not support app installation.
* Use an identity provider for centrally managed user access.

To add another Bitbucket account, select the connection method and follow the steps in this article.

<br>
