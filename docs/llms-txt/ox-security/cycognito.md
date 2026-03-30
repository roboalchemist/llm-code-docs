# Source: https://docs.ox.security/ox-integrations/3rd-party-integrations/dynamic-app-security/cycognito.md

# CyCognito

> Note: This capability may be in Early Access (EA) in your environment. Coordinate availability with your OX technical contact.

You can connect OX to your CyCognito instance to import Dynamic Application Security Testing (DAST) results. This lets you view DAST issues alongside other security findings in OX.

## Prerequisites

* A CyCognito account with Admin role or IT User role, and access to the projects you plan to import.
* Projects or applications in CyCognito that already have at least one completed scan so findings exist.

## Step 1: Generate a Cycognito API token \[CyCognito]

Use a read-only token. If your organization prefers stricter scoping, create a dedicated service account and generate the token from that account.

1. In CyCognito, go to **Settings > API Key Management**.

   * Some tenants label this path **Workflow & Integration > API Key Management**.

   **Note:** If your tenant separates *personal* and *organization* tokens, choose the option your security policy requires.
2. Select **Add API Key**.
3. In the dialog, configure the key:

   | Field              | What to enter                                                                                        |
   | ------------------ | ---------------------------------------------------------------------------------------------------- |
   | **Key name**       | A unique name that explains the purpose, for example, `OX ingestion`.                                |
   | **Access**         | Choose **Read only** for ingestion. Select **Read and write** only if your use case requires writes. |
   | **Set expiration** | (Recommended) Set a validity period to enforce rotation.                                             |

4. Select **Generate** and copy the key value. The API key value is shown only once, store it in a secure location.

## Step 2: Connecting to Cycognito

1. In the OX platform, go to the **Connectors** page.
2. Select **Add Connector** and search for **CyCognito**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-eb3aaa0de31216289fe004cb809f9e76cfeaf038%2FCyCognito.png?alt=media" alt="" width="536"><figcaption></figcaption></figure>

1. In the **Configure your CyCognito credentials** box, provide the following details:

| Field                  | Description                             |
| ---------------------- | --------------------------------------- |
| **CyCognito Host URL** | The base server URL CyCognito provides. |
| **Token**              | The API key you generated in CyCognito. |

1. Select **CONNECT**.
2. To select specific CyCognito projects to import, click the gear icon next to the **DELETE** button.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-b73492c5434033876ccc9834221fd01f31b02b94%2FCyCognito_apps.png?alt=media" alt="" width="249"><figcaption></figcaption></figure>

1. Select the CyCognito projects and select **SAVE**.

When connected, OX starts pulling DAST data from CyCognito.
