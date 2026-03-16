# Source: https://docs.brightdata.com/api-reference/proxy/select_a_specific_ip.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Select a specific IP

Option available only for zones with multiple IPs allocated. To target a specific IP allocated to your zone, use -ip-ip\_address request parameter.

```sh Shell theme={null}
curl "http://target.site" --proxy brd.superproxy.io:33335 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-ip-1.1.1.1.1:<zone_password>
```
