# Source: https://docs.ox.security/ox-integrations/3rd-party-integrations/registry/harbor.md

# Harbor

Integrate Harbor with OX to centralize security findings alongside container, pipeline, cloud, and runtime signals already in OX.

OX scans Harbor on a schedule and on demand, enriches findings with OX context (application mapping, workflows, and compliance), and presents a unified queue for investigation and reporting.

After you connect, Harbor scan results appear in the Active Issues page (use the filter **Source tool > Harbor**).

## What OX adds

* **Context and correlation:** OX maps findings to applications, services, and teams to show impact and ownership.
* **Prioritization with severity factors:** OX may reprioritize scanner severities when exploitability and environment context reduce risk (for example, Critical → High). Severity factors explain why the priority changed.
* **Evidence at a glance:** When available, OX displays scanner evidence, file locations, and remediation guidance alongside OX analytics to speed triage.

## Connection Methods

For general information about connection methods, see[Connection methods](https://docs.ox.security/get-started/onboarding-to-ox/source-control/connection-methods).

Connect to OX with a Harbor username and token.

## Prerequisites

**OX**

* OX permission to configure connectors

**Harbor**

* Admin permissions to the Harbor account you want to connect. The account must be a personal account.

## Connect with username and token

### Step 1: Create personal access token \[Harbor]

This step has several parts.\
\
**Create Robot Account**

1. Verify the [prerequisites](#prerequisites)are in place.
2. Log in to your Harbor account.
3. From the left menu pane, select **Robot Accounts**.<br>

   <figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-1c908fc1c18dc0e7d24f03679e3c551fc5976351%2FHarbor%20%E2%80%93%20select%20robot%20accounts.png?alt=media" alt=""><figcaption></figcaption></figure>
4. Select **New Robot Account**.
5. In **Create System Robot Account**, complete the details.
   * **Name:** Enter a name for the OX account.
   * **Expiration time:** Enter a value (days) or set to Never (recommended).<br>

     <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-933a2e4884a2907dbe63df171ce6834c7b19b3c9%2FHarbor%20%E2%80%93%20create%20system%20robot%20account%20%E2%80%93%20basic.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
6. Select **Next**.

**Add permissions**

1. In **Select System Permissions**, select the following permissions:

   * Project: List
   * Registry: List and Read

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-d4ee898703a7a887a56b992e54ceef816f7021c1%2FHarbor%20%20-%20system%20permissions.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
2. Select **Next**.
3. In **Select Project Permissions**, check the box to cover all projects or select the project and select **PERMISSIONS** to add permission for the selected project.<br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-da241d5ffa6b29a86b83c44f5106d717166a21cf%2FHarbor%20%E2%80%93%20select%20the%20project%20to%20assign%20permissions.png?alt=media" alt=""><figcaption></figcaption></figure></div>
4. On the next screen, scroll and select the following permissions:
   * **Artifact:** List and Read
   * **Repository:** List, Pull and Read
   * **Project:** Read
   * **Tag:** List<br>

     <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-396ffcb2b40749c922b54e65603fee80890eac0e%2FHarbor%20%E2%80%93%20all%20project%20permissions.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
5. Select **Finish**.
6. A success message displays and shows the token name and secret. Save the secret securely. You cannot view it again after this step.\
   **Best practice:** Store credentials in a secrets manager and set a reminder to rotate them according to your policy.<br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-c863839c231ec0fd38ae27e63576fe21a38b4a30%2FHarbor%20%E2%80%93%20success%20message%20name%20and%20token.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

### Step 2: Connect OX to Harbor \[OX]

1. Verify the [prerequisites](#prerequisites)are in place.
2. In OX, go to **Connectors > Registry** and select **Harbor**.<br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-41198d9f39e22e093f13bb024f2e406dce566ea6%2FHarbor%20%E2%80%93%20config%20screen.png?alt=media" alt="" width="362"><figcaption></figcaption></figure></div>
3. Enter the following parameters.

<table><thead><tr><th width="225.20001220703125" valign="top">Parameter</th><th width="265.19989013671875" valign="top">Details</th></tr></thead><tbody><tr><td valign="top">Harbor Host URL</td><td valign="top">The Harbor URL</td></tr><tr><td valign="top">User Name</td><td valign="top">The name of the OX user</td></tr><tr><td valign="top">Password</td><td valign="top">The Harbor secret</td></tr><tr><td valign="top">Connection Name</td><td valign="top">System-generated</td></tr></tbody></table>

1. Select **CONNECT**. OX validates the credentials.
2. In **Configure your Harbor credentials**, select **VERIFY CONNECTIVITY**.\
   A green checkmark indicates a successful connection. If verification fails, check your credentials and permissions.

**Optional configurations**

* To change the images OX scans and monitors, see the section [Change the locations OX scans](#change-the-locations-ox-scans).
* To connect more Harbor accounts to the same organization in the OX platform, repeat the process.
* For information on the OX Broker, see the article [OX Broker](https://docs.ox.security/get-started/onboarding-to-ox/prerequisites-and-access/ox-broker).

## Change the locations OX scans

Once you have a connection, you can change the locations that OX scans and monitors.

1. Use the **Gear** icon at the bottom of the Configuration screen.
2. OX displays the locations or objects that OX scans and monitors.
3. Change the selection as needed.
4. Select **SAVE**.

<div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-5397f500c4f3fdeab972b14d6eb9bf7b1897ad4a%2Fgitlab%20change%20repos%20gear%20icon.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

<br>
