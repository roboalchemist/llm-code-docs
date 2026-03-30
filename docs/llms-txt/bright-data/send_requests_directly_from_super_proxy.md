# Source: https://docs.brightdata.com/api-reference/proxy/send_requests_directly_from_super_proxy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Send requests directly from Super Proxy

You can choose to perform the request from the super proxy directly instead of the IP of the peer. In that case, the IP of the request will be the one of the Super Proxy by adding `-direct` to your request authorization string.

```sh Shell theme={null}
curl "http://target.site" --proxy brd.superproxy.io:33335 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-direct:<zone_password>
```
