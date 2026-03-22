# Source: https://docs.brightdata.com/api-reference/proxy/request_error_handling.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Request Error Handling

| value      | description                                                                       |
| ---------- | --------------------------------------------------------------------------------- |
| `pass_dyn` | if a request can't pass via proxy peer, automatically pass it via the Super Proxy |
| `block`    | if a request can't pass via proxy peer, block it and don't send via Super Proxy   |

<CodeGroup>
  ```sh pass_dyn theme={null}
  curl "http://target.site" --proxy brd.superproxy.io:33335 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-route_err-pass_dyn:<zone_password>
  ```

  ```sh block theme={null}
  curl "http://target.site" --proxy brd.superproxy.io:33335 --proxy-user brd-customer-<customer_id>-zone-<zone_name>-route_err-block:<zone_password>
  ```
</CodeGroup>
