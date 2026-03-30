# Source: https://docs.ox.security/ox-integrations/3rd-party-integrations/registry/gitlab-container-registry.md

# GitLab Container Registry

Integrate GitLab with OX to centralize security findings alongside container, pipeline, cloud, and runtime signals already in OX.

OX scans GitLab on a schedule and on demand, enriches findings with OX context (application mapping, workflows, and compliance), and presents a unified queue for investigation and reporting.

After you connect, GitLab scan results appear in the Active issues page (use the filter **Source tool > GitLab**).

## What OX adds

* **Context and correlation:** OX maps findings to applications, services, and teams to show impact and ownership.
* **Prioritization with severity factors:** OX may reprioritize scanner severities when exploitability and environment context reduce risk (for example, Critical → High). Severity factors explain why the priority changed.
* **Evidence at a glance:** When available, OX displays scanner evidence, file locations, and remediation guidance alongside OX analytics to speed triage.

## Connection Methods

For general information about connection methods, see[Connection methods](https://docs.ox.security/get-started/onboarding-to-ox/source-control/connection-methods).

Connect to OX with a GitLab token.

## Prerequisites

**OX**

OX permission to configure connectors

**GitLab**

* Admin permissions to the GitLab account you want to connect.

## Connect with username and token

### Step 1: Create personal access token \[GitLab]

1. Verify that the [prerequisites](#prerequisites)are in place.
2. Log in to your GitLab account.
3. From the **Profile** icon, select **Edit Profile**.
4. From the left menu pane, select **Personal access tokens**.
5. In **Personal access tokens**, select **Add new token**.
6. On the next screen enter:
   * Token name
   * Expiration date
7. In **Scopes**, select:
   * read\_user
   * Read\_registry
   * Read\_api<br>

     <figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-a54ed9ba30915e3ecbf3f44edb1830e395d89dcc%2FGitlab%20%E2%80%93%20personal%20access%20token%20and%20scopes%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>
8. Scroll down and select **Generate token**.
9. From the next screen, copy the token and save it securely. You won’t see it again after this step.\
   **Best practice:** Store credentials in a secrets manager and set a reminder to rotate them according to your policy.

### Step 2: Connect OX to GitLab \[OX]

1. Verify that the [prerequisites](#prerequisites)are in place.
2. In OX, go to **Connectors > Registry** and select **GitLab Container Registry**.<br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-55b48a7a2ab37efbfc619b5f36ab14832d556203%2FGitlab%20%E2%80%93%20configure%20screen.png?alt=media" alt="" width="434"><figcaption></figcaption></figure></div>
3. Enter the following parameters.

<table><thead><tr><th valign="top">Parameter</th><th valign="top">Details</th></tr></thead><tbody><tr><td valign="top">GitLab Container Registry Host URL</td><td valign="top">URL for GitLab cloud or on-premise</td></tr><tr><td valign="top">Token</td><td valign="top">GitLab token</td></tr></tbody></table>

1. Select **CONNECT**. OX validates the credentials.
2. In **Configure your GitLab credentials**, select **VERIFY CONNECTIVITY**.\
   A green checkmark indicates a successful connection. If verification fails, check your credentials and permissions.

**Optional configurations**

* To change the images OX scans and monitors, see the section [Change the locations OX scans](#change-the-locations-ox-scans).
* To connect more GitLab accounts to the same organization in the OX platform, repeat the process.
* For information on the OX Broker, see the article [OX Broker](https://docs.ox.security/get-started/onboarding-to-ox/prerequisites-and-access/ox-broker).

## Change the locations OX scans

Once you have a connection, you can change the locations that OX scans and monitors.

1. Use the **Gear** icon at the bottom of the Configuration screen.
2. The locations or objects OX scans and monitors display.
3. Change the selection as needed.
4. Select **SAVE**.

<div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-5397f500c4f3fdeab972b14d6eb9bf7b1897ad4a%2Fgitlab%20change%20repos%20gear%20icon.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>
