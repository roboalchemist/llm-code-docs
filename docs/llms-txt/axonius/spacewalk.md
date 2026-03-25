# Source: https://docs.axonius.com/docs/spacewalk.md

# Spacewalk

Spacewalk is an open-source systems management solution for system provisioning, patching and configuration.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Software
* SaaS Applications

## Adapter Parameters

1. **Spacewalk Domain** *(required)* - The hostname of the Spacewalk server.
2. **User Name** and **Password** *(required)* - The user name and password for an account with access to RPC API.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![spacewalk.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/spacewalk.png)

## APIs

Axonius uses the [Spacewalk API](https://spacewalkproject.github.io/documentation/api/2.9/).

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                                    | Supported | Notes |
| ------------------------------------------ | --------- | ----- |
| SUSE Manager Server version 4.0 and higher | Yes       |       |
| Spacewalk API version 2.9                  | Yes       |       |