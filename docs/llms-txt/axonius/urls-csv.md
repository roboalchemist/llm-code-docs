# Source: https://docs.axonius.com/docs/urls-csv.md

# CSV - URLs

**CSV - URLs** adapter imports information about URLs from a CSV file.

The adapter parameters are the same as the [CSV Legacy Remote File Configuration](/docs/legacy-remote-file-configuration-csv).  Since the **CSV - URLs** adapter provides data about URLs only, unlike the generic CSV adapter, there is no option to configure the adapter to contain information about Users, Devices, or any other type of asset.

The functionality of this adapter is the same as the [CSV adapter](/docs/csv).
Note that the *Accepted CSV field*  names are case insensitive.

## Which fields are imported with a  URLs file?

The following data is imported as part of the URLs file.

| Field              | Accepted CSV Field Name(s) | Notes | Required? |
| :----------------- | :------------------------- | :---- | :-------- |
| Brand              | Brand                      |       | No        |
| Report Name        | Report Name                |       | No        |
| Finding Name       | Finding Name               |       | Yes       |
| URL                | URL                        |       | Yes       |
| Parameter          | Parameter                  |       | No        |
| Attack Value       | Attack Value               |       | No        |
| Reproduction Steps | Reproduction Steps         |       | No        |
| Summary            | Summary                    |       | No        |
| Open Date          | Open Date                  |       | No        |
| Comment            | Comment                    |       | No        |
| BU                 | BU                         |       | No        |
| Overdue by days    | Overdue by days            |       | No        |

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Parse entity fields dynamically** - This setting is enabled by default so that the adapter dynamically parses all of the fields of the entity fetched. Unselect to disable this setting.
2. **Custom Parsing** - see [Adapter Custom Parsing](/docs/adapter-custom-parsing) for more information.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

<br />