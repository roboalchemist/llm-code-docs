# Source: https://docs.brightdata.com/api-reference/proxy/select_a_specific_gip.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Select a specific gIP

Option available only for Residential or Mobile zones with multiple IPs allocated. To target a specific `gIP` allocated to your zone, use `-gip-gip_name` request parameter.

```sh  theme={null}
curl "http://target.site" --proxy brd.superproxy.io:33335 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-gip-us_7922_fl_hollywood_0:<zone_password>
```
