# Source: https://docs.axonius.com/docs/brex.md

# Brex

Brex is a financial technology platform that offers corporate credit cards and expense management solutions.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Expenses
* SaaS Applications

## Parameters

1. **API Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets. For information on authorization, see the Security section under [List expenses](https://developer.brex.com/openapi/expenses_api/#operation/listExpenses).

2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

3. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

4. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

5. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Brex.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Brex.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Expense Status Filter** - From the dropdown, select one or more expense status filters.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Brex Expenses API](https://developer.brex.com/openapi/expenses_api/).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have admin permissions in order to fetch assets. For more information, see [Roles, permissions, and scopes](http://developer.brex.com/docs/roles_permissions_scopes/).

## Supported From Version

Supported from Axonius version 6.1.58.0