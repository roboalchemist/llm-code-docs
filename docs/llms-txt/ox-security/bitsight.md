# Source: https://docs.ox.security/ox-integrations/3rd-party-integrations/dynamic-app-security/bitsight.md

# Bitsight

> Note: This capability may be in Early Access (EA) in your environment. Coordinate availability with your OX technical contact.

You can connect OX to your BitSight tenant to import BitSight security-ratings data. This lets you view BitSight items alongside other security findings in the OX platform.

## Prerequisites

* BitSight Admin or VRM Admin role to generate the integration token.

## Step 1: Get a BitSight API token \[BitSight]

To start using the BitSight API, create a token from **User Preferences**.

1. In BitSight, go to **Settings > Account > User Preferences**.
2. Choose the token type to generate:
   * **User API Token**: In **User API Token**, select **Generate New Token**.
   * **Company API Token**: In **Company API Token**, enter a **description** in **New Token** (purpose) and select **Generate**.
3. Copy the generated token and store it securely. For security purposes, a **Company API token** is displayed only once.

## Step 2: Connect BitSight to OX \[OX]

1. In the OX platform, go to the **Connectors** page.
2. Select **Add Connector** and search for **BitSight**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-5842f986966540508e702769f86db1aceea9e936%2FBitSight.png?alt=media" alt="" width="502"><figcaption></figcaption></figure>

1. In the connector configuration, provide the following:

| Field                 | Description                                |
| --------------------- | ------------------------------------------ |
| **Bitsight Host URL** | The base server URL Bitsiht provides.      |
| **API token**         | Paste your BitSight **Company API token**. |

1. Select **CONNECT**.
2. When the connection succeeds, OX starts scheduled imports of Bitsight data.
