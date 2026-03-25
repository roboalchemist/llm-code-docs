# Source: https://docs.axonius.com/docs/one-pwd.md

# 1Password Account Management

1Password Account Management provides information about audit activities, including actions performed by team members in a 1Password account, such as changes made to the account, vaults, groups, users, and more.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Activities

## Parameters

1. **Host URL** *(required, default: `https://events.1password.com`)* - The hostname or IP address of the 1Password server. The base URL you use to make API calls is determined by the server that hosts your 1Password account. For more details, see [1Password Events API reference](https://developer.1password.com/docs/events-api/reference/#servers).

<Table>
  <thead>
    <tr>
      <th>
        If your account is on:
      </th>

      <th>
        Your base URL is:
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        1Password.com
      </td>

      <td>
        `https://events.1password.com` (1Password Business)
        `https://events.net.1password.com` (1Password Enterprise)
      </td>
    </tr>

    <tr>
      <td>
        1Password.ca
      </td>

      <td>
        `https://events.1password.ca`
      </td>
    </tr>

    <tr>
      <td>
        1Password.eu
      </td>

      <td>
        `https://events.1password.eu`
      </td>
    </tr>
  </tbody>
</Table>

4. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets. For more information, see [Get started with 1Password Events Reporting](https://support.1password.com/events-reporting/#appendix-issue-or-revoke-bearer-tokens).

<Callout icon="📘" theme="info">
  Note

  This adapter works with an API that doesn’t provide user information (except for user activities).
</Callout>

9. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

10. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

11. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

12. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="1Password REST" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/1Password%20REST.png" />

## APIs

Axonius uses the [1Password Events Reporting API](https://developer.1password.com/docs/events-api).

## Supported From Version

Supported from Axonius version 6.1