# Source: https://docs.axonius.com/docs/twistlock.md

# Twistlock

Twistlock provides container and cloud native cybersecurity for teams using Docker, Kubernetes, serverless, and other cloud native technologies.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Users, Aggregated Security Findings, Software, SaaS Applications, Containers

## Parameters

1. **Twistlock Domain** *(required)* - The hostname or IP address of the Twistlock server.
2. **Tenant Name** *(optional)* - A specific tenant.
   * If supplied, data will be fetched from a specific tenant, i.e. *https\://\<Twistlock\_Domain>/\<Tenant\_Name>:8083/api/v1/*
   * If not supplied, data will be fetched from the value supplied in **Twistlock Domain**, i.e. *https\://\<Twistlock\_Domain>:8083/api/v1/*
3. **Tenant Project Name** - If you use Projects in Prisma Cloud (Twistlock), enter the project name of a tenant you wish to fetch from **instead** of in the **Tenant Name** field (this will cause the project name to be added as a parameter: `?project=PROJECT_NAME` instead of appending it to the API’s prefix).
4. **User Name** and **Password** *(optional)* - The credentials for a user account that has the permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **API Token** is not supplied, **User Name** and **Password** are required.
</Callout>

5. **Authenticate with Prisma Cloud**- Select this option to authenticate using Prisma Cloud. When you select this option the API Version drop-down is available.
6. **API Version** *(required, default: 32.07)* - Select the CWPP version that you're running.
   To find your version, see [How to Find Your Version](https://prisma.pan.dev/api/cloud/cwpp/#how-to-find-your-version).
7. **API Token** *(optional)*  - An API Token  associated with a user account that has permissions to fetch assets. Refer to the API documentation for information about obtaining the API Token.

<Callout icon="📘" theme="info">
  Note

  When **User Name** and **Password** are not supplied, **API Token** is required.
</Callout>

8. **Verify SSL** - Select to verify the SSL certificate offered by the value supplied in **Twistlock Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
9. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Twistlock Domain**.
10. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Twistlock](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Twistlock.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Descriptions**  - Select whether to fetch full details of descriptions and vulnerabilities.
2. **Fetch Container as Container Asset** - Select this option to parse container data as the Container Axonius asset type.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Prisma Cloud Compute API](https://cdn.twistlock.com/docs/api/twistlock_api.html#).