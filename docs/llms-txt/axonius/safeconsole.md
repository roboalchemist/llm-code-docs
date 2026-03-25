# Source: https://docs.axonius.com/docs/safeconsole.md

# SafeConsole

SafeConsole by DataLocker allows administrators to provision, secure, manage, and audit encrypted USB drives, USB ports, and virtual folders.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the SafeConsole server.
2. **Token** *(required)* - An API token associated with a user account that has permissions to fetch assets.
   To obtain an API token, see [How to Obtain an API Token to Access SafeConsole's REST API](https://support.datalocker.com/support/solutions/articles/4000162693-how-to-obtain-api-key-to-access-safeconsole-s-rest-api).
3. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="SafeConsole" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SafeConsole.png" />

## APIs

Axonius uses the [SafeConsole REST API (v1.0 Beta)](https://api.safeconsole.com/).

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes                                         |
| ------- | --------- | --------------------------------------------- |
| v5.7    | Yes       | At least v5.7 is required for API integration |

## Supported From Version

Supported from Axonius version 4.5