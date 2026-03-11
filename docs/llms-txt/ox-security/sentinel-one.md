# Source: https://docs.ox.security/ox-integrations/3rd-party-integrations/cloud-context/sentinel-one.md

# Sentinel One

Sentinel One (Singularity) is an endpoint security platform that detects, prevents, and responds to threats across laptops, servers, and cloud workloads.

By integrating Sentinel One's Singularity™ Vulnerability Management with OX, you centralize endpoint findings alongside code, container, pipeline, and cloud signals already in OX. OX ingests Sentinel One data on a schedule and on demand, enriches it with OX context (application mapping, workflows, compliance), and presents a unified queue for investigation and reporting.

After connecting, you will see Sentinel One results in **Issues > Active issues** (filter **Source tool = SentinelOne**) and on relevant **Application** pages. The connector imports data only; it does not run scans in Sentinel One.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-b8340c8e5732657acf2bd58699d3eec656046109%2FSentinelOne_Active_Issues.png?alt=media" alt=""><figcaption></figcaption></figure>

### What OX adds

* **Context and correlation:** OX maps Sentinel One vulnerability data to affected applications and services to show impact and ownership.
* **Prioritization with severity factors:** OX may reprioritize vendor severities when exploitability and environment context reduce risk. For example, the following screencapture shows that in the Sentinel One the issue was evaluated as High severity, and due to OX severity factors, the issue was reprioritized and now it is a Low priority issue.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-89e2a9812e5b2cbc511793cb46fc6c7c4fefee50%2FSentinelOne_Active_Issues_severity_reprioritization.png?alt=media" alt=""><figcaption></figcaption></figure>

* **Evidence at a glance:** When available, OX displays vendor evidence and links alongside OX analytics to speed triage.

### Terminology mapping

| SentinelOne term    | What it includes (examples)                           | OX equivalent                         |
| ------------------- | ----------------------------------------------------- | ------------------------------------- |
| **Vulnerabilities** | OS/package CVEs on endpoints and workloads            | **Issues** (Vulnerabilities category) |
| **Management URL**  | Base URL of your Singularity Operations Center tenant | **Connector field: Management URL**   |
| **API Token**       | Token generated in **My Profile**                     | **Connector field: API token**        |

## Prerequisites

* Sentinel One **Singularity Operations Center** account with access to **My Profile**.

## Step 1: Generate a SentinelOne API token \[Sentinel One]

1. Log in to **Singularity Operations Center**.
2. In the top right, select **Your username > My Profile**.
3. Select **Actions > API Token Operations > Generate API token**.
4. When prompted, enter your **Two-Factor Authentication** code and select **Confirm**.
5. In the **API Token** window, select **Copy API Token**, then **Close**.
6. Paste and **save the token** in a secure location.

> **Note**\
> After generation, your **Actions > API Token Operations** menu includes **Revoke API Token** and **Regenerate API Token**.

> **Best practice**\
> Save the token in a secrets manager and set a reminder to **regenerate** it before it expires.

## Step 2: Connect SentinelOne to OX \[OX]

1. In OX, go to **Connectors**.
2. Search for **Sentinel One**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-05a1b855d8493041da6d8a43ecf7bdcc690974dd%2FSentinel_One_connect.png?alt=media" alt=""><figcaption></figcaption></figure>

Enter the following:

<table><thead><tr><th width="268.166748046875">Field</th><th>What to use</th></tr></thead><tbody><tr><td><strong>Sentinel One Host URL</strong></td><td>The host URL of your SentinelOne Management account (<code>your_management_url</code>).<br><br>To find your Management URL, view the URL in your browser while signed into the Singularity Operations Center.<br>For example: If your dashboard URL is <a href="https://usea1-partners.sentinelone.net/dashboard">https://usea1-partners.sentinelone.net/dashboard</a> , then Management URL will be <a href="https://usea1-partners.sentinelone.net/">https://usea1-partners.sentinelone.net</a></td></tr><tr><td><strong>API token</strong></td><td>The token you generated in <strong>Step 1</strong>.</td></tr></tbody></table>

1. Select **Connect**. OX validates the credentials. When connected, OX begins scheduled imports. You can also trigger a **manual sync** from the connector card.
2. To select specific resources for scanning by OX platform, select the gear icon next to **DELETE**.
3. Select the resources you want to protect.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-4015fbfdf86512121805e42a71ce70b34aded994%2FSentinel_One_connect_recources_selection.png?alt=media" alt="" width="326"><figcaption></figcaption></figure>

1. Select **SAVE**.
