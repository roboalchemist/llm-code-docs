# Source: https://docs.ox.security/ox-integrations/3rd-party-integrations/cloud-context/wiz.md

# Wiz

{% hint style="info" %}
Wiz connects to OX across four categories. This article covers all four types:

* **Secret/PII Scan:** [Wiz CLI Secrets](#connect-with-wiz-cli-secrets)
* **Open Source Security:** [Wiz CLI SCA](#connect-with-wiz-cli-sca)
* I**nfrastructure as Code Scan:** [Wiz CLI IaC](#connect-with-wiz-cli-iac)
* **Cloud Context:** [Wiz](#connect-with-wiz-cloud-context)
  {% endhint %}

Integrate Wiz with OX to centralize security findings alongside container, pipeline, cloud, and runtime signals already in OX.

OX scans Wiz on a schedule and on demand, enriches findings with OX context (application mapping, workflows, and compliance), and presents a unified queue for investigation and reporting.

After you connect, Wiz scan results appear on the Active Issues page (use the filter **Source tool > Wiz**).

## What OX adds

* **Context and correlation:** OX maps Wiz findings to applications, services, and teams to show impact and ownership.
* **Prioritization with severity factors:** OX may reprioritize scanner severities when exploitability and environment context reduce risk (for example, Critical → High). Severity factors explain why the priority changed.
* **Evidence at a glance:** When available, OX displays scanner evidence, file locations, and remediation guidance alongside OX analytics to speed triage.

## Connection methods

For general information about connection methods, see the article [Connection methods](https://docs.ox.security/get-started/onboarding-to-ox/source-control/connection-methods).

All connection methods use the same Wiz service account credentials: Client ID and Client Secret.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-43558fee0dc67e1f1553eab1fa1efe859b00a6a5%2Fwiz%204%20connectors.jpg?alt=media" alt=""><figcaption></figcaption></figure>

There are four methods to connect Wiz to OX:

* **Wiz CLI Secrets:** Scan for secrets and PII in your codebase through the Wiz CLI.
* **Wiz CLI SCA:** Scan open-source dependencies through the Wiz CLI.
* **Wiz CLI IaC:** Scan Infrastructure as Code configurations for security issues through the Wiz CLI.
* **Wiz Cloud (Cloud Context):** Scan cloud locations and identify critical risks in AWS, Azure, GCP, and Kubernetes. Requires API URL configuration.

## Prerequisites

**OX**

* Permission to configure connectors

**Wiz**

* Access to the Wiz account you want to connect
* Wiz user account with permissions to create accounts and tokens

## Connect with Wiz CLI Secrets

<details>

<summary><mark style="color:purple;">Connect with Wiz CLI Secrets</mark></summary>

The Wiz CLI Secrets connector scans your codebase for secrets and PII through the Wiz command-line interface.

#### Step 1: Create a service account and credentials \[Wiz]

1. Verify that the [prerequisites](#prerequisites)are in place.
2. Log in to your Wiz account.
3. Go to **Settings > Access Management > Service Accounts**.
4. Click **Add Service Account**.
   * **Name:** Enter a name (e.g., OX Security CLI Secrets Integration).
   * **Type:** Select Custom Integration (GraphQL API).
   * (Optional) **Projects:** Select specific projects to limit access, or leave blank to allow access to all projects.
5. Select the required API Scopes (permissions):
   * read:projects
   * read:reports
   * write:reports
   * read:issues
   * read:threat\_issues
6. Click **Add Service Account**.
7. Copy and store the Client ID and Client Secret in a secure location. You cannot view the client secret again after this step.\
   **Best practice:** Store credentials in a secrets manager and set a reminder to rotate the client secret according to your policy.

#### Step 2: Connect to OX \[OX]

1. Verify that the [prerequisites](#prerequisites)are in place.
2. In OX, go to **Connectors > Secret/PII Scan**, and select **Wiz**.<br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-fcf4fedfe1317af3a83ea8c88b14d4cb03a98554%2FWiz%20%E2%80%93Secret%20PII%20scan.png?alt=media" alt=""><figcaption></figcaption></figure></div>
3. In **Configure your Wiz CLI Secrets credentials**, enter the following parameters.

<table><thead><tr><th width="240.13330078125" valign="top">Parameter</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top">Client ID</td><td valign="top">The Client ID from the Wiz Service Account</td></tr><tr><td valign="top">Client Secret</td><td valign="top">The Client Secret from the Wiz Service Account</td></tr></tbody></table>

1. Click **VERIFY CONNECTIVITY**.
2. A green success message at the bottom of the screen indicates a successful connection. If verification fails, check your credentials and permissions.
3. Click **CONNECT**.

**Optional configurations**

To change the resources OX scans and monitors, see the section [Change the locations OX scans](#select-the-resources-ox-scans).

</details>

## Connect with Wiz CLI SCA

<details>

<summary><mark style="color:purple;">Connect with Wiz CLI SCA</mark></summary>

The Wiz CLI SCA connector performs Software Composition Analysis (SCA) to scan open-source dependencies for vulnerabilities through the Wiz command-line interface.

**Step 1: Create a service account and credentials \[Wiz]**

1. Verify that the [prerequisites](#prerequisites)are in place.
2. Log in to your Wiz account.
3. Go to **Settings > Access Management > Service Accounts**.
4. Click **Add Service Account**.
   * **Name:** Enter a name (e.g., OX Security CLI Secrets Integration).
   * **Type:** Select Custom Integration (GraphQL API).
   * (Optional) **Projects:** Select specific projects to limit access, or leave blank to allow access to all projects.
5. Select the required API Scopes (permissions):
   * read:projects
   * read:reports
   * write:reports
   * read:issues
   * read:threat\_issues
6. Click **Add Service Account.**
7. Copy and store the Client ID and Client Secret in a secure location. You cannot view the client secret again after this step.\
   **Best practice:** Store credentials in a secrets manager and set a reminder to rotate the client secret according to your policy.

**Step 2: Connect to OX \[OX]**

1. Verify that the [prerequisites](#prerequisites)are in place.
2. In OX, go to **Connectors > Open Source Security** and select **Wiz**.<br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-8b7a41271fff42c0e3ad9a87c1d71ae2acfee604%2FWiz%20%E2%80%93open%20source%20security%20CLI%20SCA%20config%20screen.png?alt=media" alt=""><figcaption></figcaption></figure></div>
3. In **Configure your Wiz CLI SCA credentials**, enter the following parameters:

<table><thead><tr><th width="256.66668701171875" valign="top">Parameter</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top">Client ID</td><td valign="top">The Client ID from the Wiz Service Account</td></tr><tr><td valign="top">Client Secret</td><td valign="top">The Client Secret from the Wiz Service Account</td></tr></tbody></table>

1. Click **VERIFY CONNECTIVITY**.
2. A green success message at the bottom of the screen indicates a successful connection. If verification fails, check your credentials and permissions.
3. Click **CONNECT**.

**Optional configurations**

To change the resources OX scans and monitors, see the section [Change the locations OX scans.](#change-the-locations-ox-scans)

</details>

## Connect with Wiz CLI IaC

<details>

<summary><mark style="color:purple;">Connect with Wiz CLI IaC</mark></summary>

The Wiz CLI IaC connector scans Infrastructure as Code configurations for security issues through the Wiz command-line interface.

**Step 1: Create a service account and credentials \[Wiz]**

1. Verify that the [prerequisites](#prerequisites)are in place.
2. Log in to your Wiz account.
3. Go to **Settings > Access Management > Service Accounts**.
4. Click **Add Service Account**.
   * **Name:** Enter a name (e.g., OX Security CLI Secrets Integration).
   * **Type:** Select Custom Integration (GraphQL API).
   * (Optional) **Projects:** Select specific projects to limit access, or leave blank to allow access to all projects.
5. Select the required API Scopes (permissions):
   * read:projects
   * read:reports
   * write:reports
   * read:issues
   * read:threat\_issues
6. Click **Add Service Account.**
7. Copy and store the Client ID and Client Secret in a secure location. You cannot view the client secret again after this step.\
   **Best practice:** Store credentials in a secrets manager and set a reminder to rotate the client secret according to your policy.

**Step 2: Connect to OX \[OX]**

1. Verify that the [prerequisites](#prerequisites)are in place.
2. In OX, go to **Connectors > Infrastructure as Code Scan**, and select **Wiz**.\ <br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-3d541323982cc6239937cd5b7d25fbffd9bac57d%2FWiz%20%E2%80%93infrastructure%20as%20code%20scan.png?alt=media" alt=""><figcaption></figcaption></figure></div>
3. In **Configure your Wiz CLI IaC credentials**, enter the following parameters:

<table><thead><tr><th width="248.66668701171875" valign="top">Parameter</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top">Client ID</td><td valign="top">The Client ID from the Wiz Service Account</td></tr><tr><td valign="top">Client Secret</td><td valign="top">The Client Secret from the Wiz Service Account</td></tr></tbody></table>

1. Click **VERIFY CONNECTIVITY**.
2. A green success message at the bottom of the screen indicates a successful connection. If verification fails, check your credentials and permissions.
3. Click **CONNECT**.

**Optional configurations**

To change the resources OX scans and monitors, see the section [Change the locations OX scans.](#change-the-locations-ox-scans)

</details>

## Connect with Wiz (Cloud Context)

<details>

<summary><mark style="color:purple;">Connect with Wiz (Cloud Context)</mark></summary>

The Wiz Cloud Context connector scans cloud resources to identify and remove critical risks in AWS, Azure, GCP, and Kubernetes.

**Step 1: Create a service account and credentials \[Wiz]**

1. Verify that the [prerequisites](#prerequisites)are in place.
2. Log in to your Wiz account.
3. Go to **Settings > Access Management > Service Accounts**.
4. Click **Add Service Account**.
   * **Name:** Enter a name (e.g., OX Security CLI Secrets Integration).
   * **Type:** Select Custom Integration (GraphQL API).
   * (Optional) **Projects:** Select specific projects to limit access, or leave blank to allow access to all projects.
5. Select the required API Scopes (permissions):
   * read:projects
   * read:reports
   * write:reports
   * read:issues
   * read:threat\_issues
6. Click **Add Service Account.**
7. Copy and store the Client ID and Client Secret in a secure location. You cannot view the client secret again after this step.\
   **Best practice:** Store credentials in a secrets manager and set a reminder to rotate the client secret according to your policy.
8. Select your user icon and go to **User Settings > Tenant**.
9. Copy the **API Endpoint URL** and save it.\
   Format: <https://api>.\<region>.app.wiz.io/\
   Where \<region> is your tenant's data center (e.g., us1, us2, eu1, eu2).

**Step 2: Connect to OX \[OX]**

1. Verify that the [prerequisites](#prerequisites)are in place.
2. In OX, go to **Connectors > Cloud Context** and select **Wiz**.\ <br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-07c801860560dbf7c456d48001bc659ff089b3c5%2FWiz%20%E2%80%93cloud%20context%20config%20screen.png?alt=media" alt="" width="362"><figcaption></figcaption></figure></div>
3. In **Configure your Wiz credentials**, select the link **INSTRUCTIONS:WIZ** to open an online summary of the connection process.
4. On the same screen, enter the following parameters.

<table><thead><tr><th width="229.4666748046875" valign="top">Parameter</th><th valign="top">Description</th></tr></thead><tbody><tr><td valign="top">Wiz Host URL</td><td valign="top">Pre-filled: https://auth.app.wiz.io/oauth/token (or https://auth.gov.wiz.io/oauth/token for GovCloud)</td></tr><tr><td valign="top">API URL</td><td valign="top">The API Endpoint URL from Wiz<br>(format: https://api.&#x3C;region>.app.wiz.io/)</td></tr><tr><td valign="top">Client ID</td><td valign="top">The Client ID from the Wiz Service Account</td></tr><tr><td valign="top">Client Secret</td><td valign="top">The Client Secret from the Wiz Service Account</td></tr></tbody></table>

1. Click **VERIFY CONNECTIVITY**.
2. A green success message at the bottom of the screen indicates a successful connection. If verification fails, check your credentials and permissions.
3. Click **CONNECT**.

**Optional configurations**

To change the resources OX scans and monitors, see the section [Change the locations OX scans.](#change-the-locations-ox-scans)

</details>

## Change the locations OX scans

Once you have a connection, you can change the locations that OX scans and monitors.

1. Use the **Gear** icon at the bottom of the Configuration screen.
2. OX displays the locations or objects that OX scans and monitors.
3. Change the selection as needed.
4. Select **SAVE**.

<div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-5397f500c4f3fdeab972b14d6eb9bf7b1897ad4a%2Fgitlab%20change%20repos%20gear%20icon.png?alt=media" alt="" width="375"><figcaption></figcaption></figure></div>
