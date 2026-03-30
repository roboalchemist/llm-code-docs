# Source: https://docs.axonius.com/docs/divvycloud.md

# Rapid7 InsightCloudSec

Rapid7 InsightCloudSec (formerly DivvyCloud) manages cloud security posture, secures cloud workloads, and governs identity and access management.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Aggregated Security Findings, Roles, SaaS Applications, Application Services, Containers, Object Storage, Serverless Functions, Secrets

## Parameters

1. **Domain** *(required)* - The hostname or IP address of the DivvyCloud server.
2. **Port** *(optional, default: 8001)* - The port used for the connection (port 443 for the SaaS instance of InsightCloudSec).
3. **Username** and **Password** *(optional)* - The credentials for a user account that has Read-only permissions to fetch assets. To create a user account with Read-only permissions, see [Creating a User in the Rapid7 InsightCloudSec Console](/docs/divvycloud#creating-a-user-in-the-divvycloud-console).

<Callout icon="📘" theme="info">
  Note

  When **API Token** is not supplied, **Username** and **Password** are required.
</Callout>

4. **API Key** *(optional)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **Username** and **Password** are not supplied, **API Key** is required.
</Callout>

5. **Verify SSL**  - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settingss).
6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image align="center" alt="Rapid7%20InsightCloudSec" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Rapid7%20InsightCloudSec.png" className="border" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Containers** *(optional, default: true)* - Select whether to fetch information from container objects.
2. **Do Not Fetch Powered Off Machines** - Select to not fetch machines that have a State field value of 'stopped'.
3. **Fetch Badges as Tags** - Select this option to fetch badges and parse them as asset tags.
4. **List of tags to parse as fields** - Enter a list of tags to parse as additional asset fields.
5. **Fetch Insight Findings** - Select this option to fetch Insight findings.
6. **Categorize Assets Advanced Settings** - Enable the **Categorize Assets by Asset Type** toggle to parse fetched assets as their specific asset type (Container, Secret, Serverless Function, etc.) rather than Instance type, which is the default behavior.
   For example, when **Categorize Assets Advanced Settings** is disabled, Containers and Instances will be both fetched as Instances, and no other asset type will be fetched; when it's enabled, Containers will be fetched as Containers, and any other asset type selected from the **Extra Assets list** (see below) will be fetched and parsed as they respective asset type.
   When you enable this, the following fields become available:
   1. **Extra Assets list** - A multi-select field that enables fetching and parsing assets from an expanded list of asset types.
   2. **Fetch Findings Per Asset Type** - A multi-select field that enables fetching Insight Findings and Aggregated Security Findings (vulnerabilities) from the Extra asset types selected previously. Note that this option might significantly increase the fetch time.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Permissions

The value supplied in [Username](#parameters) must be associated with credentials that have Read-only permissions to fetch assets.

Rapid7 InsightCloudSec has to add IP addresses to a permissions list  in order to accept API requests. If you are working with  an Axonius hosted system and your internal network is already on a permissions list, you can use a gateway to connect. Please contact Axonius Support for the external IP.

## Creating a User in the Rapid7 InsightCloudSec Console

**To create a user in the Rapid7 InsightCloudSec Console**

1. Log in as an administrator to the Rapid7 InsightCloudSec console. Click **Identity Management** and add a user. Axonius only uses the **Username** and **Password** field, so it doesn't matter what you specify in the **Email** field.

<Image align="center" alt="image.png" border={true} width="550px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(66).png" className="border" />

2. In the **Identity Management** page, select **Roles** `>` **Add Role**. Create a role that allows Viewing only and enable **Global Scope**.
3. Select **User Groups** `>` **Add User Group**. Add a new group, then assign the role to the newly created user.

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(67\).png) ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(68\).png) ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(69\).png)

4. Log in with the new user at least once to create it and verify that you can view your cloud accounts.

5. Fill-in all required fields in the adapter configuration and click **Save**. The Rapid7 InsightCloudSec adapter is configured.