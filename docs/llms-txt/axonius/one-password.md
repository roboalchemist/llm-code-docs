# Source: https://docs.axonius.com/docs/one-password.md

# 1Password

1Password is a password manager providing a place for users to store various passwords, software licenses, and other sensitive information in a virtual vault.

<Callout icon="❗️" theme="error">
  Caution

  The credentials used to configure the adapter provide access to all passwords in all the vaults accessible by that user account.

  The adapter **does not** use these credentials to fetch data, and the password information is not displayed.
</Callout>

**Related Enforcement Actions:**

* [1Password - Suspend User](/docs/one-password-suspend-user)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* Application Resources
* Permissions

## Parameters

1. **OnePasswordAddress** *(required)* - The address of OnePassword that Axonius can communicate with via the [Required Ports](#required-ports). This should not contain a prefix of http\:// or https\://. Do not add any specific endpoints after the domain For example agilebits.1password.com
2. **Auth Method** - Select an Authentication method, either **Secret Key Authentication** (default) or **Service Account Token Authentication**.
   * **Secret Key Authentication**:
     * **Email** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.
     * **Secret Key** *(required)* - A secret key that can be retrieved from the profile page of the relevant user. For example: `A3-CFER76-3V6WK9-83MJS-CVRYQ-ZXLXM-GXS28` (dummy sequence)
     * **MFA Secret** *(optional)* - The secret generated in 1Password for setting up multi-factor authentication for the 1Password user. To use this setting you need to set up connection to applications on 1Password. Follow the instructions [here](https://support.1password.com/two-factor-authentication/#set-up-two-factor-authentication) to set up MFA authentication. At the end of the procedure you get a six-digit authentication code. This is the code that you need to paste into this field.
       Example for an MFA secret: `J7NGB45ZMB2V6JUE` (dummy sequence)
   * **Service Account Token Authentication**:
     * **Service Account Token** *(required)* - A unique token associated with a service account (a non-human account) to use for authentication without human intervention.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="OnePAssword" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/OnePAssword.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch Vault Items** - Select this option to fetch vault items.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [1Password CLI](https://developer.1password.com/docs/cli/).

## Required Ports

Axonius must be able to communicate with the value supplied in [OnePasswordAddress](#parameters) via the following ports:

* **80/443**

## Required Permissions

The value supplied in [Email](#parameters) must have Read permission and access to each vault the customer wants to see in Axonius  in order to fetch assets.

If the following error is received:

*Unsupported six-digit authentication*

This means you did not enable two-factor authentication. If you do not wish to use two-factor authentication, then disable the  two factor authentication for the  account used. To do this enter the profile of the user, select more actions, and then select *turn off two-factor authentication*

## Supported From Version

Supported from Axonius version 6.0