# Source: https://docs.axonius.com/docs/hubspot.md

# HubSpot

HubSpot provides software products for inbound marketing, sales, and customer service.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* SaaS Data

## Parameters

1. **Host Name or IP Address** *(required, default: `https://api.hubapi.com`)* - The hostname or IP address of the HubSpot server.

2. **API Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Web URL**  - *(Required to fetch SaaS data)* - the URL of the HubSpot portal that the customer uses (e.g. [https://app.hubspot.com](https://app.hubspot.com)")

4. **Hub ID**  - *(Required to fetch SaaS data)* - The Hub ID number from your Hubspot profile.

5. **Username and Password** - *(Required to fetch SaaS data)* - A username and password for a Hubspot user with user.table access permissions.

6. **2FA Secret Key** - *(Required to fetch SaaS data)* - The secret generated in the adapter for setting up 2-factor authentication for the adapter  user created to collect SaaS data.

7. **Use SSO** - *(Required to fetch SaaS data)* -  Select this option if your organization uses  SSO to log in to hubspot. For more information, see [Connecting your SSO Solution Provider](/docs/adding-a-new-adapter-connection#connecting-your-sso-solution-provider).

8. **Verify SSL** *(required, default: false)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

9. **HTTPS Proxy** *(optional, default: empty)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

10. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

11. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

![HubspotSM](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HubspotSM.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced Settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **Fetch archived owners** *(required, default: false)* - Select to fetch archived owners in addition to unarchived owners. When cleared, only unarchived owners are fetched.
2. **Fetch login activity** - Select this option to enrich users with login activity data. Accessing this data requires an additional permission: 'account-info.security.read.'

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [HubSpot CRM API | Owners](https://developers.hubspot.com/docs/api/crm/owners).

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have Super Admin permissions to fetch assets.
To make a user a super admin, from HubSpot, click the **Actions** dropdown and select **Make super admin**.

In addition, you need the following read-only scopes to view CRM data:

* **crm.objects.owners**
* **crm.objects.owners.read**

To fetch SaaS data
You need the following read-only scopes:

* **settings.users**
* **settings.users.teams**
* **permission.sets**
* **user.table access**.
* **account-info.security.read** (to fetch login activity)

## Supported From Version

Supported from Axonius version 4.5