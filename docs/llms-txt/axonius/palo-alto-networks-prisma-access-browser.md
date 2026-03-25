# Source: https://docs.axonius.com/docs/palo-alto-networks-prisma-access-browser.md

# Palo Alto Networks Prisma Access Browser

## Overview

Palo Alto Networks Prisma Access Browser is a secure enterprise browser that offers integrated threat prevention, data-loss protection, and zero-trust access for web and SaaS applications on managed or unmanaged devices.

## Types of Assets Fetched

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg) Devices | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Users.svg) Users

## Before you Begin

### Supported from Version

* Supported from Axonius v8.0.8

### Required Ports

* TCP 443

### APIs

* Aoxnius uses the Prisma Access Browser SEB API v1

### Required Permissions

* `View Only Administrator` role

## Configuring the Palo Alto Networks Prisma Access Browser credentials

Use Palo Alto Networks Common Services UI to add a Service Account in the desired Tenant Service Group (TSG). Reference: [Add Service Accounts (Common Services)](https://docs.paloaltonetworks.com/common-services/identity-and-access-access-management/manage-identity-and-access/add-service-accounts).

1. Sign in to the Palo Alto Networks cloud management portal.

2. Navigate to **Common Services → Identity & Access**.

3. Select the Tenant Service Group (TSG) where you want to create the service account.
   1. If needed, create a new TSG first

4. Click **Add**.

5. For Identity Type, select **Service Account**.

6. Enter a unique Service Account Name and Description.

7. Proceed to the **Client Credentials** step.

8. On the Client Credentials screen:
   1. Copy the Client ID and Client Secret. *(the Client Secret is displayed only once)*

9. Assign a predefined least-privileged role suitable for data retrieval: `View Admin Only`.

10. **Save** to complete creation.

11. In Identity & Access, open the TSG details and record the **TSG ID**.

## Deploying the Palo Alto Networks Prisma Access Browser Adapter

* Navigate to the Adapters page, search for `Palo Alto Networks Prisma Access Browser`, and click on the adapter tile.
* Click  **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Domain** - Base domain URL for SEB API requests. Must include protocol (`http://` or `https://`).  Example: `https://<seb-api-host>` *(Do not append path segments)*
2. **Client ID**  - Client identifier from the Prisma SASE Service Account.
3. **Client Secret** - Client secret from the Prisma SASE Service Account.
4. **Tenant Service Group ID** - TSG identifier used to scope the access token.
5. **Authentication Domain** - Base domain URL for the Authentication Service token endpoint. Use `https://auth.apps.paloaltonetworks.com`.
6. **Connection Label** - Friendly name for your new adapter connection.

<Image align="center" alt="Palo Alto Prisma Access Broswer Add Connection screen" border={false} width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/main/img/adapters/pan_prisma_access_browser.png" />

### Optional Fields

* **Verify SSL** - Enable/disable SSL certificate verification for API calls.
* **HTTPS Proxy** - Proxy URL used for outbound API communication.
* **HTTPS Proxy User Name** - Username for proxy authentication.
* **HTTPS Proxy Password** - Password for proxy authentication.
* **Select Gateway** – Select the [Axonius Gateway](https://docs.axonius.com/docs/installing-axonius-gateway) to use when connecting adapters whose sources are only accessible by an internal network. To use this option, you need to set up an Axonius Gateway.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<br />