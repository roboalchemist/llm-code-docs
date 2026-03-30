# Source: https://docs.axonius.com/docs/networks-csv.md

# CSV - Networks

**CSV - Networks** adapter imports information about networks from a CSV file. You can use this adapter to fetch a bulk list of network segments.

The adapter parameters are the same as the [CSV Legacy Remote File Configuration](/docs/legacy-remote-file-configuration-csv).  Since the **CSV - Networks** adapter provides data about networks only, unlike the generic CSV adapter, there is no option to configure the adapter to contain information about Users, Devices, or any other type of asset.

The functionality of this adapter is the same as the [CSV adapter](/docs/csv).
Note that the *Accepted CSV field*  names are case sensitive.

## Which fields are imported with a  Networks file?

The following data is imported as part of the Networks file.

| Field         | Accepted CSV Field Name(s) | Notes                                                                                                                                                                                                                | Required? |
| :------------ | :------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------- |
| ID            | id                         | Any type of ID for the row, for example, an ordered number according to the rows index. Axonius will use this value to create a unique asset for each network.                                                       | Yes       |
| Asset Type    | Asset Type                 | The Asset Type must be one of the following types: AWS VPC, Cisco Meraki Network, GCP VPC, Infoblox Network, AD Sites & Subnets, IPv4 Subnet, IPv6 Subnet, Wiz Virtual Network, NetworkSecurityRules, VirtualNetwork | No        |
| Site Name     | Site Name                  |                                                                                                                                                                                                                      | No        |
| State         | State                      |                                                                                                                                                                                                                      | No        |
| Creation Date | Creation Date              |                                                                                                                                                                                                                      | No        |
| CIDR Blocks   | CIDR Blocks                | The format should be comma-separated strings with a space after each comma, for example: *1.1.1.1, 2.2.2.2, 3.3.3.3.*                                                                                                | No        |

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Parse entity fields dynamically** - Enable this to parse all the fields in the file and add a custom prefix.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>