# Source: https://docs.axonius.com/docs/mimecast.md

# Mimecast - V1

Mimecast provides a mail management system designed to protect email, ensure access and simplify the tasks of managing email.

<Callout icon="📘" theme="info">
  Note

  This adapter supports Mimecast API 1.0. If you are using Mimecast API 2.0 use the [Mimecast - V2](/docs/mimecast-v2) adapter.
</Callout>

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Mimecast server. Select the Base URL that corresponds to your region.
   For more information, see [Global Base URLs](https://integrations.mimecast.com/documentation/api-overview/global-base-urls/).

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **Application ID** and **Application Key** *(required)* -  The Mimecast Application ID and Application Key. Refer to [Mimecaster Managing API Applications](https://community.mimecast.com/s/article/Managing-API-Applications-505230018) for information about generating the Application ID and Application Key.

4. **Internal Domain** *(optional)* - The name of the domain the client wants to get the internal users from.  Set this parameter if you enable the advanced *Fetch internal domain users* setting. You can enter more than one internal domain separated by  commas (without any spaces).

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="MimecastN" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MimecastN.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch user groups** *(required, default false)* - Select this option to fetch user groups.
2. **Fetch user\`s performance data**  *(required, default false)* - Select this option to fetch user\`s performance data.
3. **Fetch user\`s watchlist data** *(required, default false)* -  Select this option to fetch user\`s watchlist data.
4. **Fetch Phishing Campaign user data** *(required, default false)* -  Select this option to fetch  Phishing Campaign user data.
5. **Fetch user\`s on-hold sent messages data**  *(required, default false)* -   Select this option to fetch  user\`s on-hold sent messages data.
6. **Fetch internal domain users** - Select this option to get internal users.
7. **Usernames exclude list** - Enter a comma-separated list of usernames to exclude from the fetch. Any user that contains a string from the exclude list, will be excluded from the fetch.
8. **User mails exclude list** - Enter a comma-separated list of users' emails to exclude from the fetch. Any user that contains a string from the exclude list, will be excluded from the fetch.
9. **Exclude alias users** - Select this option to not fetch a user if it is an alias.
10. **Fetch email activity in the last X days** - Specify the number of days to fetch email activity per each user.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses [Mimecast API 1.0](https://integrations.mimecast.com/documentation/api-overview/api-concepts/).
Axonius uses [Get Internal Users](https://integrations.mimecast.com/documentation/endpoint-reference/user/get-internal-users/) to fetch internal users.

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* 80, 443 or the port configured.

## Required Permissions

The value supplied in [User Name](#parameters) must have the following permissions in order to fetch assets:

* Awareness Training | Dashboard | Read

* Account | Dashboard | Read

* Directories | Groups | Edit

* Directories | Groups | Read.

* Must be a Mimecast administrator with at least the Directories | Internal | Read permission in order to fetch Internal Users.

## Supported From Version

Supported from Axonius version 4.7