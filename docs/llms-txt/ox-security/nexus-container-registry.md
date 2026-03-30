# Source: https://docs.ox.security/ox-integrations/3rd-party-integrations/registry/nexus-container-registry.md

# Nexus Container Registry

Integrate your Nexus on-premises account with OX to centralize security findings alongside container, pipeline, cloud, and runtime signals already in OX.

OX scans Nexus on a schedule and on demand, enriches findings with OX context (application mapping, workflows, and compliance), and presents a unified queue for investigation and reporting.

After you connect, Nexus scan results appear in the Active issues page (use the filter Source tool > Nexus).

## What OX adds

* **Context and correlation:** OX maps findings to applications, services, and teams to show impact and ownership.
* **Prioritization with severity factors:** OX may reprioritize scanner severities when exploitability and environment context reduce risk (for example, Critical → High). Severity factors explain why the priority changed.
* **Evidence at a glance:** When available, OX displays scanner evidence, file locations, and remediation guidance alongside OX analytics to speed triage.

## Connection Methods

For general information about connection methods, see[Connection methods](https://docs.ox.security/get-started/onboarding-to-ox/source-control/connection-methods).

Connect to OX with a Nexus username and password.

## Prerequisites

* OX permission to configure connectors
* Access to the Nexus on-premises account you want to connect.
* Add the OX Security IP address 108.128.213.11 to Nexus's whitelist or your firewall rules.
* The Docker-hosted repository in Nexus has either an HTTP or HTTPS port enabled.

## Connect with username and password

### **Step 1: Create an OX role and local user \[Nexus]**

The step has several parts.

**Create role and permissions**

1. Verify that the [prerequisites](#prerequisites) are in place.
2. Log in to the Nexus repository.
3. Select the **Gear** icon and select **Roles** from the menu pane.
4. In **Roles**, select **Create Role**.
5. Enter the details:
   * **Role type:** Nexus role
   * **Role ID:** A text identifier of your choice.
   * **Role name:** A descriptive name.
6. Select the **Modify Applied Privileges** button.<br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-01c69416b4aa5e9a35246d3d0ba599d330fa2f6f%2FNexus%20-%20modify%20applied%20privileges%20button%20(1).png?alt=media" alt=""><figcaption></figcaption></figure></div>
7. In **Privileges Selection**, select the privileges:
   * nx-repository-view -\*-\*- browse
   * nx-repository-view -\*-\*- read
   * nx-repository-view-docker -\*- browse
   * nx-repository-view-docker -\*- read
   * nx-search-read
8. Select **Confirm**.
9. To save the new role, scroll to the bottom of the screen and select **Save**.

**Create user**

1. From the menu pane, select **Users**.
2. Select the **Create local user** button.
3. Complete the mandatory fields:
   * Username
   * First name
   * Last name
   * Email address to receive notifications.
   * Password and confirm it
   * Status: Active
4. Scroll down to **Roles** and add the role to the **Granted** box.\ <br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-b8b48c91b2d182bc968eafd6c20749a592769d77%2FNexus%20%20-%20add%20role%20to%20the%20user.png?alt=media" alt="" width="337"><figcaption></figcaption></figure></div>
5. Select **Create local user**.\
   A success message appears. If the verification fails, check the credentials.<br>

**Enable Docker-hosted repository port**

1. Select **Repositories** from the menu pane.
2. Select the **Docker-hosted** repository.
3. Enable either of the HTTP ports.<br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-44d7b3131a1d00289a99e0e7e2456e04b0d2522d%2FNexus%20-%20confirm%20repository%20ports.png?alt=media" alt="" width="543"><figcaption></figcaption></figure></div>

### Step 2: Connect OX to Nexus \[OX]

1. Verify that the [prerequisites](#prerequisites) are in place.
2. In OX, go to **Connectors > Registry > Nexus Container Registry** to open the connector configuration dialog.\ <br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-e3f6d8d1deaf905219dee7db99500ce6bfacdad4%2FNexus%20config%20screen.png?alt=media" alt=""><figcaption></figcaption></figure></div>
3. In **Configure your Nexus Container Registry credentials**, enter the following parameters.

<table><thead><tr><th width="306.2667236328125" valign="top">Parameter</th><th width="282.2666015625" valign="top">Details</th></tr></thead><tbody><tr><td valign="top">Nexus Container Registry Host URL</td><td valign="top">The Nexus URL</td></tr><tr><td valign="top">User Name</td><td valign="top">The Nexus ID for OX</td></tr><tr><td valign="top">Password</td><td valign="top">The password for the OX user</td></tr></tbody></table>

1. Select **CONNECT**. OX validates the credentials.

**Optional configurations**

* To change the images OX scans and monitors, see the section [Change the locations OX scans](#change-the-locations-ox-scans).
* To connect more Nexus accounts to the same organization in the OX platform, repeat the process.

## Change the locations OX scans

Once you have a connection, you can change the locations that OX scans and monitors.

1. Use the **Gear** icon at the bottom of the Configuration screen.
2. OX displays the locations or objects that OX scans and monitors.
3. Change the selection as needed.
4. Select **SAVE**.

<div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-5397f500c4f3fdeab972b14d6eb9bf7b1897ad4a%2Fgitlab%20change%20repos%20gear%20icon.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>

<br>
