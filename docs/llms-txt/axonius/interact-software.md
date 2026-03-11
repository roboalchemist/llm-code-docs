# Source: https://docs.axonius.com/docs/interact-software.md

# Interact Software

## Overview

Interact Software is an intranet and employee engagement platform used for internal communication, content publishing, and collaboration.

## Types of Assets Fetched

* ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Users.svg) Users

## Before you begin

### Version

* Supported from Axonius v8.0.9.

### Required Ports

* 443 (HTTPS)

### APIs

* Axonius uses the [Interact Software REST API](https://developer.interactsoftware.com/reference/introduction).

### Required Permissions

* No special permissions are required, except for a username and password for authentication.

## Configuring the Interact Software Adapter Credentials

You must log in to Interact as an Application Administrator or a Power User with access to the Control Panel to perform these steps.

1. Log in to your Interact account.
2. Navigate to the Control Panel (usually found in the top-right menu under your profile or a cog icon).
3. Under the System or Security section, look for Manage Security or API Keys.

   <Callout icon="📘" theme="info">
     Note

     In some versions, this is located under Integrations > Developer Resources.
   </Callout>
4. Click **New API Key** (or **Add Key**).
5. Enter a name for the key (e.g., "Internal HR Integration") to help you identify it later.
6. Assign the necessary User or Permissions to this key.

   Interact API keys often act on behalf of a specific user context. You may need to associate the key with a "Service User" account rather than your own personal account to ensure the integration keeps working if you leave the company.
7. Click **Save/Generate**. The system will display an API Key and a Secret.

   IMMEDIATELY COPY THE SECRET.

<Callout icon="🚧" theme="warn">
  Important

  The Secret is displayed only once. If you close the window without saving it, you will have to generate a new key.
</Callout>

## Deploying the Interact Software Adapter

**To deploy the adapter:**

1. Navigate to the Adapters page, search for `Interact Software`, and click on the adapter tile.
2. Click **Add Connection**.
3. Configure the parameters.

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Interact server.
2. **Tenant ID** and **Password** - The credentials for a user account that has the permissions to fetch assets.

### Optional Fields

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.
5. **Connection Label** - A friendly name for this connection in Axonius.

* **Select Gateway** – Select the [Axonius Gateway](https://docs.axonius.com/docs/installing-axonius-gateway) to use when connecting adapters whose sources are only accessible by an internal network and not from the primary Axonius instance, which may be an Axonius-hosted (SaaS) instance or Customer-hosted (on-premises / private cloud). To use this option, you need to set up an Axonius Gateway.

<Image align="center" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/InteractSoftware.png" />