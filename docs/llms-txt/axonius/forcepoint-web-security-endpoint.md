# Source: https://docs.axonius.com/docs/forcepoint-web-security-endpoint.md

# Forcepoint Web Security Endpoint CSV File

Forcepoint Web Security Endpoint enables end-users to authenticate and receive policy enforcement via the Forcepoint Web Security Cloud infrastructure.

The Forcepoint Web Security Endpoint adapter is able to import Forcepoint Web Security Endpoint CSV files with information about devices.

<Callout icon="📘" theme="info">
  NOTE

  This page describes how to retrieve information from Forcepoint Web Security Endpoint using a CSV File. To connect to the Forcepoint Web Security Endpoint database, see [Forcepoint Web Security Endpoint](/docs/forcepoint-web-security-endpoint-sql).
</Callout>

The adapter parameters are as same as the [CSV Legacy Remote File Configuration](/docs/legacy-remote-file-configuration-csv), except that the **File contains users information** and the **File contains installed software information** parameters. These fields are not part of the Forcepoint Web Security Endpoint adapter configuration, as the adapter provides devices data only, without any information on installed software.

The functionality of this adapter is as same as the [CSV Legacy Remote File Configuration](/docs/legacy-remote-file-configuration-csv).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Parse "Version" as Agent Version (Instead of "Client Installation Version")** - Select this option to parse "Version" as Agent Version.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>