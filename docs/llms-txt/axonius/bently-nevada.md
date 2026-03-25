# Source: https://docs.axonius.com/docs/bently-nevada.md

# Bently Nevada

Bently Nevada is a condition monitoring system that provides asset protection and predictive maintenance solutions.

This adapter uploads XML and TXT files.

### Asset Types Fetched

* Devices

The adapter parameters are the same as the [CSV adapter parameters](/docs/csv), except for the **File contains users information**, **File contains installed software information**, and the **File contains database information** parameters. These fields are not part of the adapter configuration, as the adapter provides devices data only, without any information on the installed software.

#### Supported From Version

Supported from Axonius version 6.1.65

![Bently Nevada.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Bently%20Nevada.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Devices of sub type xml\_device from Devices from XML** - Select this option to fetch devices of the subtype 'xml\_device' from the Devices endpoint from XML.
2. **Fetch Devices of sub type txt\_device from Devices from TXT** - Select this option to fetch devices of the subtype 'txt\_device' from the Devices endpoint from TXT.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>