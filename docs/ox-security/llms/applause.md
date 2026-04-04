# Source: https://docs.ox.security/ox-integrations/3rd-party-integrations/dynamic-app-security/applause.md

# Applause

> Note: This capability may be in Early Access (EA) in your environment. Coordinate availability with your OX technical contact.

You can connect OX to your Applause instance to import Dynamic Application Security Testing (DAST) results without interfering with live cycles.

If your Applause deployment is self-hosted or uses a custom domain, you may need a custom API host URL.

## Prerequisites

* **Applause role**: You must have **Primary Manager** account in Applause to manage API keys.
* **Access to the customer tenant** where products and test cycles are defined.

## Step 1: Generate an Applause API key \[Applause]

For validation, Applause users can issue a restricted API key, which is limited to 1–2 test cycles and certain issue types.

After testing, they can issue an unrestricted API key that works for all products in the customer’s Applause tenant.

**To generate a restricted Applause API key:**

1. Sign in to Applause with a **Primary Manager** account.
2. Go to **Configurations > API keys**.
3. Select **Generate New API key**.
4. **In the Generate New API Key dialog**, set the following:

| Field                                    | Description                                                                                                                                                                                                                                                               |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Key Name**                             | Provide a key name.                                                                                                                                                                                                                                                       |
| **Restricted Key by Product (Optional)** | <ul><li><strong>Unrestricted (recommended for OX)</strong>: Do not select any products. The key will work for all products in the tenant.</li><li><strong>Product-restricted</strong>: Select one or more products to limit the key strictly to those products.</li></ul> |

1. Select **Generate Key**. The information box with the key appears.
2. Select **Copy Key & Close**, and store the copied key securely, it is shown only once.

## Step 2: Connect Applause to OX \[OX]

1. In the OX platform, go to the **Connectors** page.
2. Select **Add Connector** and search for **Applause**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-a95d2c02d544396ba99c62a801c1932a625be180%2FApplause.png?alt=media" alt="" width="538"><figcaption></figcaption></figure>

1. In the **Configure your Applause credentials** box, provide the following details:

| Field                 | Description                                                               |
| --------------------- | ------------------------------------------------------------------------- |
| **Applause Host URL** | The base server URL Applause provides.                                    |
| **Token**             | The unrestricted API key (no products selected) you generated in Appause. |

1. Select **CONNECT**.
2. To select specific Applause projects to import, click the gear icon next to the **DELETE** button.
3. Select the Applause projects and select **SAVE**.

   When connected, OX starts pulling DAST data from Applause.
