# Source: https://developer.1password.com/docs/sdks/concepts

On this page

# 1Password SDK concepts

## Authentication[â€‹](#authentication "Direct link to Authentication") 

1Password SDKs support authentication with [1Password Service Accounts](/docs/service-accounts/), which are designed to authenticate automated processes to 1Password.

You can choose which vaults a service account can access and its permissions in each vault, allowing you to follow the [principle of least privilege](https://csrc.nist.gov/glossary/term/least_privilege) in your project.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)]Beta feature

The option to authenticate 1Password SDKs with the 1Password desktop app is now in beta. Learn how to [build desktop integrations](/docs/sdks/desktop-app-integrations/).

## Autofill behavior[â€‹](#autofill-behavior "Direct link to Autofill behavior") 

### Which credentials 1Password suggests[â€‹](#which-credentials-1password-suggests "Direct link to Which credentials 1Password suggests") 

When you create a Login or Password item, use the following IDs and field types for the credentials you want 1Password to suggest and fill:

  ID           fieldType     Description
  ------------ ------------- -----------------------------------------
  `username`   `Text`        The username associated with the login.
  `password`   `Concealed`   The password associated with the login.

See [an example of how to create a Login item](/docs/sdks/manage-items#create-an-item).

### Where a login is suggested and filled[â€‹](#where-a-login-is-suggested-and-filled "Direct link to Where a login is suggested and filled") 

The `Item` struct for Login and Password items contains an optional list of websites, so you can manage where 1Password autofills your credentials. Autofill behavior options include:

  Autofill behavior     Description
  --------------------- ----------------------------------------------------------------------------------------------------------
  `AnywhereOnWebsite`   Default. 1Password autofills credentials on any page thatâ€™s part of the website, including subdomains.
  `ExactDomain`         1Password autofills credentials only if the domain (hostname and port) is an exact match.
  `Never`               1Password never autofills credentials on this website.

## Document file[â€‹](#document-file "Direct link to Document file") 

A document file is a file stored in 1Password as a [Document item](https://support.1password.com/item-categories#document). You can [read, save, and replace](/docs/sdks/files/) document files saved in 1Password using the SDKs.

## Item categories[â€‹](#item-categories "Direct link to Item categories") 

Items in 1Password have a category that determines some characteristics about the item, like the fields available by default and whether 1Password suggests the item when you sign in to a website. Learn more about [the different types of items you can save in 1Password](https://support.1password.com/item-categories/). See [supported item categories](/docs/sdks/manage-items#item-parameters).

## Item states[â€‹](#item-states "Direct link to Item states") 

`ItemOverview` exposes one of two states: `Active` or `Archived`.

  Item state   Description
  ------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Active       An item located inside a vault. (Default)
  Archived     An item that has been moved to the Archive. 1Password doesnâ€™t include archived items in search results or suggest them when you fill in apps and browsers. You can keep archived items as long as youâ€™d like.

## Field file[â€‹](#field-file "Direct link to Field file") 

A field file is a file attachment saved in a 1Password item. You can [read, save, and remove](/docs/sdks/files/) file attachments saved in 1Password using the SDKs.

## Field types[â€‹](#field-types "Direct link to Field types") 

1Password SDKs currently support operations on the following field types. You can only retrieve and make changes to supported field types.

  Field type           Description
  -------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `Address`            An address. Specify each part of the address [in the field\'s details](/docs/sdks/manage-items#address). Don\'t set or edit the address field\'s value directly.
  `Concealed`          A secret value that 1Password conceals by default, like a password, API key, or credit card PIN.
  `CreditCardNumber`   A credit card number.
  `CreditCardType`     Type of credit card. For example Visa, Mastercard, or American Express.
  `Date`               A date, formatted as `YYYY-MM-DD`.
  `Email`              An email address.
  `Menu`               A menu of predefined options included in certain item types, like Database, Server, Email Account, and Wireless Router items.
  `MonthYear`          A month-year combination, formatted as `MM/YYYY`.
  `Notes`              A note about an item.
  `Phone`              A phone number.
  `Text`               A text string.
  `Totp`               A one-time password field. Must be [either a valid TOTP URL or a one-time password seed](/docs/sdks/manage-items#totp).
  `Url`                A web address to copy or open in your default web browser, not used for autofill behavior. You can [add autofill websites](#where-a-login-is-suggested-and-filled) to set where 1Password suggests and fills a Login or Password item.
  `Reference`          The [valid ID](/docs/sdks/concepts#unique-identifiers) of another item in the same vault.
  `SSHKey`             Must be a valid SSH private key â€" [a decrypted, PEM-encoded string](/docs/sdks/manage-items#ssh-key). SSH key fields can only be added to items with the [SSH Key](https://support.1password.com/item-categories#ssh-key) category. You can add one SSH key field per item. 1Password will generate a public key, fingerprint, and key type which are stored in the SSH key field details.

If an item contains information saved in unsupported field types, you won\'t be able to update or delete the item.

See [supported functionality](/docs/sdks/functionality/) for more information.

## Query parameters[â€‹](#query-parameters "Direct link to Query parameters") 

### `otp`[â€‹](#otp "Direct link to otp") 

You can use the `otp` (or `totp`) [attribute query parameter](/docs/cli/secret-reference-syntax#attribute-parameter) to retrieve one-time passwords with the [`Resolve` function](/docs/sdks/load-secrets/).

Append the `?attribute=otp` query parameter to a secret reference that points to the field where your one-time password is stored. For example:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

### `ssh-format`[â€‹](#ssh-format "Direct link to ssh-format") 

You can use the `ssh-format` [attribute query parameter](/docs/cli/secret-reference-syntax#attribute-parameter) to fetch a private SSH key in OpenSSH format using the [`Resolve` function](/docs/sdks/load-secrets/).

Append the `?ssh-format=openssh` query parameter to a secret reference that points to the field where your SSH private key is stored. For example:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

## Rate limits[â€‹](#rate-limits "Direct link to Rate limits") 

1Password Service Accounts have hourly and daily rate limits. These also apply while using a service account with an SDK. Learn more about [service account rate limits](/docs/service-accounts/rate-limits).

## SDK client[â€‹](#sdk-client "Direct link to SDK client") 

When you initialize an SDK, you create a 1Password SDK client instance and pass your configuration parameters to the SDK core. You can instantiate multiple SDK clients sequentially or in parallel using the same or different service account tokens.

## Secret references[â€‹](#secret-references "Direct link to Secret references") 

1Password SDKs allow you to use [secret reference URIs](/docs/cli/secret-reference-syntax/) to avoid the risk of exposing plaintext secrets in your code. Secret references reflect changes you make in 1Password, so when you use the SDK to load a secret you get the latest value.

Secret references use the following syntax:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

[Learn more about secret references](/docs/cli/secret-reference-syntax/).

## State management[â€‹](#state-management "Direct link to State management") 

The 1Password SDK client sets up an authenticated session with the 1Password servers and automatically refreshes it whenever it expires. As a result, you don\'t need to worry about managing your authentication and session keys.

## Unique identifiers[â€‹](#unique-identifiers "Direct link to Unique identifiers") 

A unique identifier (ID) is a string of 26 numbers and letters that can be used to identify a 1Password object, like a vault, item, section, or field. IDs only change if you move an item to a different vault.

1Password SDKs require you to use IDs rather than names to refer to 1Password objects while performing item management operations.

You can get IDs by [listing vaults and items](/docs/sdks/list-vaults-items/).