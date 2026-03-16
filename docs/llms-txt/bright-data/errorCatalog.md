# Source: https://docs.brightdata.com/proxy-networks/errorCatalog.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.brightdata.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Proxy errors troubleshooting

> Explore the catalog of Bright Data HTTP errors, including error codes, descriptions, and actions to resolve common proxy issues.

This article provides information on how to identify proxy errors from other errors, how to analyze errors, troubleshoot and resolve issues with Bright Data proxy services.

## How can I get indication on Bright Data proxy services health status?

Bright Data publishes its products and services status in this page: [https://brightdata.com/network-status](https://brightdata.com/network-status) . In this page you can see if there are current issues or incidents in the products you use or our global availability. You can also register for email alerts which are sent upon changes in our availability of reporting on wide incidents.

## What to do if I see that there is current incident in the proxy network I am using?

First, you need to check if your operations are impacted. Two main indications are degredation in response time (slowness) or increased error rates. If one of those occur, reduce your processing rate and follow the next steps to identify the issue.

## How can I tell if the error I got is originates from a Bright Data proxy?

While using our proxies, you may encounter errors that do not originate from Bright Data. To identify the source of the error, check if the response headers include BrightData error fields listed below, we cover most errors by proxy layer in those codes.

If you are still not able to get to your target website, or receive a response `HTTP` status `200` without the data you are expecting, you were probably blocked. In this article: [Overcoming website blocking](https://docs.brightdata.com/proxy-networks/website-blocking) we provide some best practices.

## How to resolve "Proxy Error" when testing Bright Data proxies thru another software?

Many software tools and utilities use Bright Data proxies, and have a function to "Test proxy" in them. When you hit "Test proxy" and get a generic "Proxy Error" message in that software, it can originate from various reasons.

### Common issues and resolutions

* Targeting a search engine like [google.com](http://google.com) or [bing.com](http://bing.com): Bright Data lmits search engine access via its proxy networks. To resolve go to your software settings and change the test website to be: [https://geo.brdtest.com/welcome.txt](https://geo.brdtest.com/welcome.txt)
* Using Bright Data residential network without installing a certificate: Bright Data does not allow using its Residential netowork without passing a KYC verification or installing a certificate. Read on different access modes [Residential Network Access Policy. ](https://docs.brightdata.com/proxy-networks/residential/network-access)

# Bright Data Proxy Errors Troubleshooting

## Bright Data's proxy error format and standard now supports RFC9209

Starting October 2025, Bright Data supports two sets of headers to relay proxy error in response payload:

1. Propietary `x-brd-*` fields: `x-brd-err-code` and `x-brd-err-msg`
2. Standard RFC9209`Proxy-Status` response header supporting RFC9209 standard proxy error format.

The `Proxy-Status` header standard field will eventually replace the `x-brd-*` fields, during 2026.

## What is RFC9209?

RFC9209 is the standard on how to relay proxy errors in response headers over proxy. Bright Data is adopting this standard and applied it to all its error catalog. This will allow customers' code as well as 3rd party tools using proxy as infrastructure to refer to error from proxy interaction and resolve issues faster.

You can read more about it here: [The Proxy-Status HTTP Response Header](https://www.rfc-editor.org/rfc/rfc9209.html)

## How to implelement RFC9209?

### Example Proxy-Status HTTP header

```
Proxy-Status: brd.brighdata.io; 
received-status=400; 
error=destination_ip_unroutable; 
details="client-10060: Requested IP ##.##.##.## is not allocated to this zone. Select an IP that is allocated to this zone or skip the -ip parameter in proxy username."
```

### Implementation Instructions

1. Parse the response header: Ensure that your systems are configured to interpret the Proxy-Status header in HTTP responses.
2. Extract relevant fields:
   * `received-status`: Provides the HTTP status code received.
   * `error`: Describes the general error encountered.
   * `details`: Contains specific error codes and further information from our error catalog.
   * The first field in the details will be bright data error code (like: client\_10060) followed by ':' (colon) delimiter. 
   * You can browse directly to the error document using this prefix, and replacing the '\_' (underscore) with '-' (dash) in the error code: `https://docs.brightdata.com/proxy-networks/errorCatalog#[Bright data error code]`. Example for client\_10060: [https://docs.brightdata.com/proxy-networks/errorCatalog#client-10060](https://docs.brightdata.com/proxy-networks/errorCatalog#client-10060)
3. Adapt your error handling processes according to these structured codes to improve debugging and ensure a seamless proxy operation.

## Bright Data HTTP proxy header fields

The following fields are returned upon and `HTTP` or `HTTPS` requests:

| Field            | Description                                                                                                                                                        | Examples                                                                                                                                                                                                                                  | REST API Field Name |
| :--------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| `HTTP Error`     | The protocol error numbers                                                                                                                                         | `404` or `502`                                                                                                                                                                                                                            | `status_code`       |
| `x-brd-err-code` | Bright data module and error code number                                                                                                                           | `client_10001`                                                                                                                                                                                                                            | `error_code`        |
| `x-brd-error`    | Bright data main error message                                                                                                                                     | Authentication failed                                                                                                                                                                                                                     | `error`             |
| `x-brd-err-msg`  | Bright data elaborated message and actions                                                                                                                         | Authentication failed. Please check your credentials or review your [account status and billing settings](https://brightdata.com/cp/settings/billing).                                                                                    | `error_message`     |
| `Proxy-Status`   | RFC9209 compliant response header. It will include Bright Data proxy server, the HTTP status and details string which has a reference to Bright Data's error code. | `Proxy-Status: brd.superproxy.io; received-status=407; error="http_request_denied"; details="client_10000: Invalid authentication: check credentials and retry. Bright Data credentials include your account ID, zone name and password"` | Not supported       |

### Getting HTTP header fields

#### Testing from command line

To view and test your settings, or restoring an issue, you can run a `curl` command from your shell prompt and add the option flag `-v` or `i`. These flags will run curl in verbose mode and print out the header fields, including the custom error code and message.

```sh  theme={null}
curl -v [rest of curl command options]
```

To see a more compact view with the header fields response only use the `-i` option for curl:

```sh  theme={null}
curl -i [rest of curl command options]
```

Alternatively, you can use the `nc` command to get the fields printed to screen:

```sh  theme={null}
echo "[tcp nc inputs]" | nc -C -v brd.superproxy.io 33335
```

<Note>
  `nc` inputs may include "empty" lines, those are essential for correct testing using `nc` command
</Note>

#### `curl` Command snippet

`curl` command snippet, with all required zone parameters is available in the **Overview** tab in Bright Data control panel for the zone you are working on.

#### Accessing via programming language

Bright Data HTTP header fields can be accessed thru your programming language, as any other HTTP header field.

#### Accessing via Bright Data's Proxy REST API

Bright data offers a REST API to access its proxy networks as well as the Unlocker API and our SERP for targeting search engines. The error field names are slightly different , yet the content is identical.

Example response:

```JSON  theme={null}
"status_code": 407,
"status_message": "Proxy Authentication Required",
"error": "Proxy Authentication Required",
"error_message": "No proxy credentials provided. Please add credentials and try again.",
"error_code": "client_10010"
```

## Error Catalog

### HTTP Error 400

When Using the Data center/ISP or gIPs products with the `-ip-x.x.x.x` targeting flag, the error code `400` can appear in case the IPs under your zone has been refreshed, removed, or simply changed due to system updates

<Note>
  This error typically arises after your BrightData account has been recently suspended. An automatic suspension occurs if your account balance becomes negative. If the suspension extends beyond 24 hours, the static allocated IPs will be released from your account. Upon reactivation, the reallocated IPs may differ from the original ones, thus if the previously allocated IPs are still being targeted - this error is thrown.
</Note>

Whenever this error appears, you should go to your Bright Data Zones page, and view the updated list of IPs relevant to this zone.

| Error Code     | `x-brd-error`                            | `x-brd-err-msg`                                                                                                                                                                                                                                                                                                                      | RFC9209 Error Code          |
| :------------- | :--------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| `client_10060` | `ip_requested_not_allocated_by_customer` | Requested IP `##.##.##.##` is not allocated to this zone. Select an IP that is allocated to this zone or skip the `-ip` parameter in proxy username.                                                                                                                                                                                 | `destination_ip_unroutable` |
| `client_10061` | Peer not found                           | No proxy found in selected default countries: `%Countries_list%`. Please revise your default country selection or use `-country` flag to another country and override default settings. [Read more](https://docs.brightdata.com/api-reference/proxy/geolocation-targeting)                                                           | —                           |
| `client_10062` | Peer not found                           | Your `[proxy type] [DC\|ISP]` zone does not have IPs in selected countries. Either IPs location has changed, or zone is not configured with proxies in selected countries. Check zone configuration and try again with the relevant country code. [Read more](https://docs.brightdata.com/api-reference/proxy/geolocation-targeting) | —                           |
| `client_10063` | Bad IP format                            | The IP address provided is either empty or does not comply with IPv6/IPv4 protocol. Please check your inputs and try again.                                                                                                                                                                                                          | —                           |

### HTTP Error 401

These are the `x-brd-err-code` values for HTTP error 401:

| Error Code     | `x-brd-error`                     | `x-brd-err-msg`                                                                                                                                                                                   |
| :------------- | :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `client_10050` | Auth failed: IP denylisted `[IP]` | Auth Failed IP denylisted: `[IP]`. [Check FAQ: how to denylist/allowlist IPs and domains?](https://docs.brightdata.com/proxy-networks/faqs#how-to-allowlist-denylist-ips-and-domains) to resolve. |

### HTTP Error 402

These are the `x-brd-err-code` values for HTTP error 402:

| Error Code     | `x-brd-error`                     | `x-brd-err-msg`                                                                                                                                                                                                                                                                                                                        |
| :------------- | :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `policy_20130` | Residential Failed `bad_endpoint` | Residential Failed (`bad_endpoint`) — Requested site is not available for immediate residential (no KYC) access mode because `%HTTP_METHOD%` requests are not allowed. To get full residential access for targeting this site, fill in the KYC form: [https://brightdata.com/cp/kyc](https://brightdata.com/cp/kyc)                    |
| `policy_20140` | Residential Failed `bad_endpoint` | Requested site is not available in Immediate Access mode for Bright Data residential network due to violation of target's `robots.txt`. To gain full access follow the instructions in: [https://docs.brightdata.com/proxy-networks/residential/network-access](https://docs.brightdata.com/proxy-networks/residential/network-access) |

### HTTP Error 403

HTTP 403 response code means you are forbidden from accessing a **valid** URL. The server processed the request, but it can't fulfill the request either due to the way the request was sent by the client or due to Bright Data policy, blocking target access.

These are the `x-brd-err-code` values for HTTP error 403:

| Error Code     | `x-brd-error`                                                                          | `x-brd-err-msg`                                                                                                                                                                                                                                                                                                                                         |
| :------------- | :------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `client_10070` | No Protocol                                                                            | Protocol was missing from original request. Please add either HTTP or HTTPS and retry.                                                                                                                                                                                                                                                                  |
| `client_10080` | No Destination Host                                                                    | No destination host. Destination host is missing or incorrect. Check your request parameters and try again.                                                                                                                                                                                                                                             |
| `client_10090` | You are trying to use Browser API zone as regular proxy                                | You are trying to use Browser API zone as regular proxy. A browser should be used to access this zone. See [Browser API](https://docs.brightdata.com/scraping-automation/scraping-browser/introduction) for information on how to access your Browser API zone.                                                                                         |
| `client_10130` | Forbidden: this super proxy is allowed only for China domains via China peers          | Forbidden: this super proxy is allowed to be used only for China domains via China peers. Otherwise use `brd.superproxy.io`. For more details review: [Mobile FAQs — Chinese sites](https://docs.brightdata.com/proxy-networks/mobile/faqs#how-to-browse-chinese-sites-by-using-chinese-residentials-ips)                                               |
| `client_10250` | Forbidden: You tried to target `%HOST%` but got blocked                                | Forbidden: You tried to target `%HOST%` but got blocked since this host is not an allowed target in your zone's allowlist security setting. Please add this host to your allowlist or delete all content from the allowlist to allow all targets.                                                                                                       |
| `client_10260` | Forbidden: You tried to target `%HOST%` but got blocked                                | Forbidden: You tried to target `%HOST%` but got blocked since this host is an explicitly blocked target in your zone's denylist security setting. Please remove this host from your denylist or delete all content from the denylist to allow all targets.                                                                                              |
| `policy_20010` | Bad protocol                                                                           | The protocol you are using to access our proxy is not supported. Bright Data supports HTTP, HTTPS & SOCKS5 upon special approval. Please fix your protocol and try again.                                                                                                                                                                               |
| `policy_20020` | Bad port                                                                               | Bad port used. See supported ports: [https://docs.brightdata.com/proxy-networks/faqs#how-to-see-supported-ports-and-protocols](https://docs.brightdata.com/proxy-networks/faqs#how-to-see-supported-ports-and-protocols)                                                                                                                                |
| `policy_20021` | Forbidden: Target is blocked by Bright Data for superproxy requests                    | Request was rerouted through a superproxy due to compliance policy, but was then blocked because the destination port is forbidden for requests from the superproxy.                                                                                                                                                                                    |
| `policy_20030` | Forbidden: target blocked                                                              | Forbidden: You tried to target `www.somehost.com` but got blocked. It can be related to your denylist or allowlist settings or the target site is not allowed by Bright Data policy. [Read more](https://docs.brightdata.com/proxy-networks/faqs#what-is-error-code-403)                                                                                |
| `policy_20031` | Forbidden: Target `%HOST%` is blocked                                                  | Forbidden: target `%HOST%` is blocked by Bright Data. Target host provides web service or information of Bright Data and our proxies cannot be used to target it. For further assistance please contact [support@brightdata.com](mailto:support@brightdata.com)                                                                                         |
| `policy_20040` | Forbidden host                                                                         | Destination host is blocked either by Bright Data in accordance with our compliance policy or by your account rules' configuration. Please check if this domain is allowed for targeting by this zone in zone settings: [https://brightdata.com/cp/zones/](https://brightdata.com/cp/zones/)                                                            |
| `policy_20050` | Forbidden: target site requires special permission. Contact Bright Data for assistance | Forbidden: target site requires special permission. You are trying to access a target site which is not permitted by our compliance policy. You may need to undergo a KYC process: [https://brightdata.com/cp/kyc](https://brightdata.com/cp/kyc). If you have already completed KYC approval, please contact your account manager for further details. |
| `policy_20051` | Forbidden: target site requires special permission. Contact Bright Data for assistance | Forbidden: target site is a government site and requires special permissions to access. You may need to undergo a KYC process: [https://brightdata.com/cp/kyc](https://brightdata.com/cp/kyc). If you have already completed KYC approval, please contact your account manager for further details.                                                     |
| `policy_20080` | Forbidden: request needs to be made using residential network                          | Forbidden: You are accessing a domain which is not permitted to access by Bright Data Datacenter or ISP networks. Please retry your request using a Residential network zone.                                                                                                                                                                           |
| `policy_20090` | Forbidden: requests to this domain are blocked using the proxy networks                | Forbidden: requests to this domain are blocked using the Datacenter, ISP and Residential proxy networks. Please get access via an Unlocker API zone or IDE tools, or contact your account manager for further assistance.                                                                                                                               |
| `policy_20091` | Forbidden: Target `$host` is blocked by Bright Data on IPv6 protocol                   | Forbidden: Target `$host` is blocked by Bright Data on IPv6 protocol. Please try IPv4 proxies or our Unlocker API to access this target.                                                                                                                                                                                                                |
| `policy_20110` | Forbidden SERP domain                                                                  | Destination host is blocked either by Bright Data in accordance with our compliance policy or by your account rules' configuration. Please check if this domain is allowed for targeting by this zone in zone settings: [https://brightdata.com/cp/zones/](https://brightdata.com/cp/zones/)                                                            |
| `policy_20230` | Country `%COUNTRY%` is not permitted for targeting                                     | Country `%COUNTRY%` is not permitted for targeting, please modify to a different country.                                                                                                                                                                                                                                                               |
| `policy_20240` | Proxy port `%PORT%` is restricted                                                      | Proxy port `%PORT%` is restricted. Contact [Bright Data support](mailto:support@brightdata.com).                                                                                                                                                                                                                                                        |
| `policy_20250` | Forbidden: You tried to target `%HOST%` but got blocked                                | Forbidden: You tried to target `%HOST%` but got blocked by Bright Data policy settings. Either this website is forbidden by Bright Data policy or your account doesn't have the right permission to access it.                                                                                                                                          |
| `policy_20251` | Forbidden: You tried to target `%HOST%` but got blocked                                | Forbidden: You tried to target `%HOST%` but got blocked by Bright Data policy settings. Either this website is forbidden by Bright Data policy or your account doesn't have the right permission to access it.                                                                                                                                          |
| `policy_20260` | Forbidden: You tried to target `%HOST%` but got blocked                                | Forbidden: You tried to target `%HOST%` but got blocked by Bright Data policy settings. Either this website is forbidden by Bright Data policy or your account doesn't have the right permission to access it.                                                                                                                                          |
| `policy_20261` | Forbidden: You tried to target `%HOST%` but got blocked                                | Forbidden: You tried to target `%HOST%` but got blocked by Bright Data policy settings. Either this website is forbidden by Bright Data policy or your account doesn't have the right permission to access it.                                                                                                                                          |
| `policy_20000` | Access denied: `<URL>` is classified as `<category>` and blocked by Bright Data        | Access denied: `%URL%` is classified as `%CATEGORY%` and blocked by Bright Data as it might breach Bright Data usage policy. [Read more](https://docs.brightdata.com/proxy-networks/residential/network-access#residential-proxy-network-policy)                                                                                                        |

### HTTP Error 407

If you get HTTP error 407, this implies there is an error in authentication. This can be due to incorrect credentials or due to your account being suspended.

| Error Code     | `x-brd-error`                                                                                                       | `x-brd-err-msg`                                                                                                                                                                                                                                                                                                                             |
| :------------- | :------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `client_10000` | Authentication failed                                                                                               | Invalid authentication: check credentials and retry. Bright Data credentials include your account ID, zone name and password.                                                                                                                                                                                                               |
| `client_10001` | Invalid Auth                                                                                                        | Invalid authentication: check credentials and retry.                                                                                                                                                                                                                                                                                        |
| `client_10002` | Auth failed: Zone not found                                                                                         | Authentication failed: zone not found. Zone name used is either misspelled, or zone is disabled or deleted. Check your inputs, and validate zone is "Active" in Bright Data control panel, or use our API to get current zone status: [Get Active Zones](https://docs.brightdata.com/api-reference/account-management-api/Get_active_Zones) |
| `client_10010` | Proxy Authentication Required                                                                                       | No proxy credentials provided. Please add credentials and try again.                                                                                                                                                                                                                                                                        |
| `client_10020` | Account is suspended. [Login](https://brightdata.com/cp/setting/billing) to activate your account                   | Account is suspended. [Login](https://brightdata.com/cp/setting/billing) to activate your account.                                                                                                                                                                                                                                          |
| `client_10030` | Authentication failed                                                                                               | You are not allowed to access our API via this IP. Please verify your settings or allowlist this IP.                                                                                                                                                                                                                                        |
| `client_10040` | KYC Required. Please visit [http://brightdata.com/cp/kyc](http://brightdata.com/cp/kyc) and ensure you are verified | KYC Required. Please visit [http://brightdata.com/cp/kyc](http://brightdata.com/cp/kyc) and ensure you are verified.                                                                                                                                                                                                                        |
| `policy_20120` | IP parameter `<IP>` is incorrect, use correct format in the IP parameter                                            | IP parameter `<IP>` is incorrect, use `x-luminati-ip` header format in the IP parameter.                                                                                                                                                                                                                                                    |

### HTTP Error 429

These are the `x-brd-err-code` values for HTTP error 429:

| Error Code     | `x-brd-error`                            | `x-brd-err-msg`                                                                                                                                                                                                                                                                                  |
| :------------- | :--------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `client_10110` | Account exceeded the allowed rate limits | Your account exceeded the allowed rate limits. Reduce requests rate and try again or complete the [verification process](https://brightdata.com/cp/account_verification) to relieve rate limits. You will not be charged for this request.                                                       |
| `policy_20220` | Requests rate to `%URL%` is too high     | Rate limit for domain `%DOMAIN%` has been reached. Bright Data's health monitor is throttling down these requests to prevent overloading of the target website. Reduce requests rate and try again or contact [brightdata.com](http://brightdata.com/) for support.                              |
| `policy_20221` | Requests rate to `%URL%` is too high     | Rate limit for domain `%DOMAIN%` has been reached. Bright Data's health monitor is throttling down these requests to prevent overloading of the target website. Reduce requests rate and try again or contact [brightdata.com](http://brightdata.com/) for support.                              |
| `policy_20222` | Requests rate per IP is too high         | Rate limit per IP `%IP%` on zone `%ZONE%` has been reached. Requests are throttled down to avoid overload. Either increase the number of IPs or reduce rate, and review your rotation logic or your response size to assure even distribution of requests and bandwidth across IPs of this zone. |

### HTTP Error 499

These are the `x-brd-err-code` values for HTTP error 401:

| Error Code     | `x-brd-error`     | `x-brd-err-msg`                                                                                                                                                                                                                                                                                    |
| :------------- | :---------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `client_10140` | Client disconnect | The client closed the connection to the proxy before the response was fully returned. This is usually caused by client-side timeouts, cancelled requests, or local network interruptions. Review your client timeout configuration and ensure the client waits long enough for the proxy response. |

### HTTP Error 502

These are the `x-brd-err-code` values for HTTP error 502:

| Error Code     | `x-brd-error`                                                 | `x-brd-err-msg`                                                                                                                                                                                                                                                           |
| :------------- | :------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `client_10120` | Block direct route                                            | Request reroute blocked. You chose the option not to reroute requests through our superproxy on failure, so the reroute was blocked. To see more about this setting see: [Request Error Handling](https://docs.brightdata.com/api-reference/proxy/request_error_handling) |
| `client_10100` | Zone has reached usage limit                                  | Zone has reached usage limit. Go to [https://brightdata.com/cp/zones](https://brightdata.com/cp/zones) to remove/modify the limitation.                                                                                                                                   |
| `peer_30030`   | Proxy Error: We do not have proxies in the city you requested | Proxy Error: We do not have proxies in the city you requested. Please check the spelling or try again later. Check [Target a specific city](https://docs.brightdata.com/proxy-networks/faqs#how-to-target-a-specific-city) for proper use of city targeting.              |
| `policy_20070` | Host is blocked in requested country                          | Host you are trying to access is blocked in requested country. Please change country and retry.                                                                                                                                                                           |
| `target_40001` | Could not resolve host `%HOST%`                               | Could not resolve host `%HOST%`. Check host name is correctly spelled and retry. If host is properly spelled or can only be resolved from a specific region, contact Bright Data support for DNS support.                                                                 |
| `target_40011` | No IPv6 address (AAAA record) found for `%HOST%`              | Attempting to resolve `%HOST%` to IPv6 failed. This is probably because the host you are targeting does not publish an IPv6 IP address. Retry the request on an IPv4 proxy.                                                                                               |

***
