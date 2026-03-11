# Source: https://docs.axonius.com/docs/default-field-mapping.md

# Default Field Mapping

When an Enforcement Action creates an asset in some third party software, the asset is created with a set of default attributes populated based on the following field mapping:

| Axonius Device Field                     | Asset Attribute |
| ---------------------------------------- | --------------- |
| Asset Name / Host Name                   | name            |
| Device Manufacturer                      | manufacturer    |
| Device Manufacturer Serial / BIOS Serial | serial\_number  |
| Network Interfaces: IPs                  | ip\_address     |
| Network Interfaces: MAC                  | mac\_address    |
| OS Type                                  | os              |

Some Enforcement Actions allow you to disable this default field mapping.