# Source: https://docs.brightdata.com/api-reference/proxy/os_targeting.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# OS Targeting

Bright Data allows targeting the following **Operating Systems**:

<CodeGroup>
  ```sh Windows theme={null}
  curl "https://target.site" --proxy brd.superproxy.io:33335 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-os-windows:<password>
  ```

  ```sh macOS theme={null}
  curl "https://target.site" --proxy brd.superproxy.io:33335 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-os-osx:<password>
  ```

  ```sh Android theme={null}
  curl "https://target.site" --proxy brd.superproxy.io:33335 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-os-android:<password>
  ```
</CodeGroup>
