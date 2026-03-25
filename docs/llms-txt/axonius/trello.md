# Source: https://docs.axonius.com/docs/trello.md

# Trello

Trello is a collaboration and project management tool that helps teams organize and manage their work tasks and projects.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required, default: `https://api.trello.com`)* - The hostname or IP address of the Trello server.

2. **Organization ID** *(required)* - Specify your Trello Organization ID. You can obtain it from the address bar on the workspace page.

3. **API Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets. For information about how to generate the API Key, see: [https://trello.com/power-ups/admin](https://trello.com/power-ups/admin)

4. **API Token** *(required)* - Specify the API Token you have created in Trello. To generate the token, you must:

   1. Open `https://trello.com/1/authorize?expiration=never&scope=read,account&response_type=token&key=YOUR_API_KEY` and replace `YOUR_API_KEY` with the API Key that you created.
   2. Give access to your account by clicking **Allow**.

   <Image align="center" alt="Trello API Token Access" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Trello%20API%20Token%20Access.png" />

   3. Copy the token and paste it into the Axonius connection.

   <Image align="center" alt="Trello API Token Copy" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Trello%20API%20Token%20Copy.png" />

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Trello" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Trello.png" />

## APIs

Axonius uses the following APIs:

* [Authorization](https://developer.atlassian.com/cloud/trello/guides/rest-api/authorization/#using-basic-oauth)
* [Trello REST API](https://developer.atlassian.com/cloud/trello/rest/api-group-organizations/#api-organizations-id-members-get)

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have read,account permissions in order to fetch assets.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| 1       | Yes       | --    |

## Supported From Version

Supported from Axonius version 6.1