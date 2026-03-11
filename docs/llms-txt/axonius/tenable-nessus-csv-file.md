# Source: https://docs.axonius.com/docs/tenable-nessus-csv-file.md

# Tenable Nessus CSV File

Tenable Nessus CSV File Adapter imports device information from vulnerability scan data.

The adapter parameters are as same as the [CSV Legacy Remote File Configuration](/docs/legacy-remote-file-configuration-csv), except for the **File contains users information** and the **File contains installed software information** parameters. These fields are not part of the Tenable Nessus CSV File adapter configuration, as the adapter provides devices data only, without any information on the installed software.

When uploading the CSV file, you will need to ensure that the field with IP address information is labeled "Host".

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **Only get devices with MAC, Hostname or correlatable IP address** *(required, default: False)* - Choose whether to exclude fetching devices without MAC address, without hostname and without an IP address that can be correlated to other existing IP address.
   * If enabled, all connections for this adapter will only fetch devices having at least one of the following:
     * MAC address
     * Hostname
     * IP address that can be correlated with an existing IP address in Axonius.
   * If disabled, all connections for this adapter will fetch devices even if those do not have MAC address, no hostname and no IP address that can be correlated to other existing IP address.
2. **Parse Plugin Output field** - Select this option to fetch the plugin output field.

<Callout icon="📘" theme="info">
  NOTE

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>