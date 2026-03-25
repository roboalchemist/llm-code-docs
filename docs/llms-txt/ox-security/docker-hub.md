# Source: https://docs.ox.security/ox-integrations/3rd-party-integrations/registry/docker-hub.md

# Docker Hub

Integrate Docker Hub with OX to centralize security findings alongside container, pipeline, cloud, and runtime signals already in OX.

OX scans Docker Hub on a schedule and on demand, enriches findings with OX context (application mapping, workflows, and compliance), and presents a unified queue for investigation and reporting.

After you connect, Docker Hub scan results appear in the Active issues page (use the filter **Source tool > Docker Hub**).

## What OX adds

* **Context and correlation:** OX maps Docker Hub findings to applications, services, and teams to show impact and ownership.
* **Prioritization with severity factors:** OX may reprioritize scanner severities when exploitability and environment context reduce risk (for example, Critical → High). Severity factors explain why the priority changed.
* **Evidence at a glance:** When available, OX displays scanner evidence, file locations, and remediation guidance alongside OX analytics to speed triage.

## Connection Methods

For general information about connection methods, see[Connection methods](https://docs.ox.security/get-started/onboarding-to-ox/source-control/connection-methods).

Connect to OX with a Docker Hub username and token.

## Prerequisites

**OX**

* Permission to configure connectors

**Docker Hub**

* Create a personal access token (PAT).
* **IP Whitelisting:** Add the OX Security IP address 108.128.213.11 to Docker Hub's whitelist or your firewall rules.

## Connect with username and token

### **Step 1: Create personal access token \[Docker]**

1. Verify that the [prerequisites](https://app.gitbook.com/s/DoksSYnSCvYSMGAaU9SQ/ox-integrations/3rd-party-integrations/registry/docker-hub#prerequisites)are in place.
2. Log in to the Docker Hub workspace.
3. Go to **Account Settings > Personal access token** and select **Generate access token**.
4. In **Create access token**, enter:
   * **Token name**: A name of the token
   * **Expiry:** Set to None
   * **Access permissions:** Read-only<br>

     <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-6570178cbf228a119c7aff4cadcdccdadfaa7b48%2FDocker%20-%20create%20access%20token.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
5. Select **Generate**. Docker generates a token.
6. Copy and save the user name and token. Save them securely. You cannot view the token again. **Best practice:** Store the token in a secrets manager and set a reminder to rotate it according to your policy.

### **Step 2: Connect OX to Docker \[OX]**

1. Verify that the [prerequisites](https://app.gitbook.com/s/DoksSYnSCvYSMGAaU9SQ/ox-integrations/3rd-party-integrations/registry/docker-hub#prerequisites)are in place.
2. In OX, go to **Connectors > Registry** and select **Docker Hub**.<br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-686c7c0836b0d8a28ba19d274fec14dbb1078c7a%2FDocker%20hub%20OX%20configure%20credentials.png?alt=media" alt="" width="434"><figcaption></figcaption></figure></div>
3. In **Configure your Docker Hub credentials,** select the link **HELP CONNECTING DOCKER HUB** to open an online summary of the connection process.
4. Enter the following parameters:

<table><thead><tr><th width="155.3333740234375" valign="top">Parameter</th><th width="431.5999755859375" valign="top">Details</th></tr></thead><tbody><tr><td valign="top">User Name</td><td valign="top">The Docker token user name</td></tr><tr><td valign="top">Password</td><td valign="top">The Docker token</td></tr></tbody></table>

1. Select **CONNECT**. OX validates the credentials.
2. In **Configure your Docker Hub connector**, select the images you want OX to scan.\
   \
   ![](https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-3b44e1d0dbcfc6e801ddc7fda2c955d5e68120d0%2FDocker%20hub%20%E2%80%93%20select%20image%20folders.png?alt=media)<br>
3. Select **SAVE**.
4. In **Configure your Docker Hub credentials**, select **VERIFY CONNECTIVITY**.\
   A green checkmark indicates a successful connection. If verification fails, check your credentials and permissions.

**Optional configurations**

* To change the images OX scans and monitors, see the section [Change the locations OX scans](#change-the-locations-ox-scans).
* For information on the OX Broker, see the article [OX Broker](https://docs.ox.security/get-started/onboarding-to-ox/prerequisites-and-access/ox-broker).

## Change the locations OX scans

Once you have a connection, you can change the locations that OX scans and monitors.

1. Use the **Gear** icon at the bottom of the Configuration screen.
2. OX displays the locations or objects that OX scans and monitors.
3. Change the selection as needed.
4. Select **SAVE**.

<div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-1258743af4005adcc8366578f78e9576a3952305%2Funknown%20(3)%20(1)%20(1)%20(1).png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>

<br>
