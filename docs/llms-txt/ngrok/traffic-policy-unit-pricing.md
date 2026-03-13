# Source: https://ngrok.com/docs/pricing-limits/traffic-policy-unit-pricing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Traffic Policy Unit (TPU) Pricing

> Learn about how ngrok uses Traffic Processing Units (TPUs) to measure and charge for Traffic Policy usage.

## Traffic Policy Units (TPUs)

Traffic Processing Units (TPUs) are ngrok's usage-based metric for measuring the work your Traffic Policies perform. Because requests can include any mix of expressions, macros, and actions—often applied only to a subset of traffic—charging a flat rate per request or connection would usually result in overcharging. Instead, ngrok calculates TPUs dynamically for each request, based only on the parts of the Traffic Policy that were actually executed.

TPUs are sold in bundles of 100,000 for \$1 and are charged as your policies execute.

## TPU pricing breakdown

* [**Actions**](/traffic-policy/concepts/actions/): Define what happens when a Traffic Policy rule matches (such as adding headers, denying a request, or forwarding traffic).
* [**Macros**](/traffic-policy/macros/): Macros can be used within the Traffic Policy engine to simplify traffic management and dynamic configuration.
* [**Variables**](/traffic-policy/variables/): Metadata about connections or requests that you can use in expressions or actions (such as the client IP or headers).

### Actions

| Name                                                              | TPU Cost |
| ----------------------------------------------------------------- | -------- |
| [add-headers](/traffic-policy/actions/add-headers/)               | Free     |
| [basic-auth](/traffic-policy/actions/basic-auth/)                 | Free     |
| [circuit-breaker](/traffic-policy/actions/circuit-breaker/)       | 10 TPUs  |
| [close-connection](/traffic-policy/actions/close-connection/)     | Free     |
| [compress-response](/traffic-policy/actions/compress-response/)   | 10 TPUs  |
| [custom-response](/traffic-policy/actions/custom-response/)       | Free     |
| [deny](/traffic-policy/actions/deny/)                             | Free     |
| [forward-internal](/traffic-policy/actions/forward-internal/)     | Free     |
| [http-request](/traffic-policy/actions/http-request/)             | 1 TPU    |
| [jwt-validation](/traffic-policy/actions/jwt-validation/)         | 10 TPUs  |
| [log](/traffic-policy/actions/log/)                               | Free     |
| [oauth](/traffic-policy/actions/oauth/)                           | Free     |
| [oidc](/traffic-policy/actions/oidc/)                             | Free     |
| [owasp-crs-request](/traffic-policy/actions/owasp-crs-request/)   | 10 TPUs  |
| [owasp-crs-response](/traffic-policy/actions/owasp-crs-response/) | 10 TPUs  |
| [rate-limit](/traffic-policy/actions/rate-limit/)                 | 1 TPU    |
| [redirect](/traffic-policy/actions/redirect/)                     | 10 TPUs  |
| [remove-headers](/traffic-policy/actions/remove-headers/)         | 1 TPU    |
| [restrict-ips](/traffic-policy/actions/restrict-ips/)             | 10 TPUs  |
| [set-vars](/traffic-policy/actions/set-vars/)                     | Free     |
| [terminate-tls](/traffic-policy/actions/terminate-tls/)           | 100 TPUs |
| [url-rewrite](/traffic-policy/actions/url-rewrite/)               | 10 TPUs  |
| [verify-webhook](/traffic-policy/actions/verify-webhook/)         | 1 TPU    |

### Macros

| Name                                                                                  | TPU Cost                 |
| ------------------------------------------------------------------------------------- | ------------------------ |
| [b64.decode(string)](/traffic-policy/macros/#base64)                                  | 3 TPUs per GB after 1 GB |
| [b64.encode(string)](/traffic-policy/macros/#base64)                                  | 3 TPUs per GB after 1 GB |
| [basic\_auth.encode(username, password)](/traffic-policy/macros/#basic-auth)          | Free                     |
| [http.header(name)](/traffic-policy/macros/#http-requests)                            | Free                     |
| [http.header(name, default)](/traffic-policy/macros/#http-requests)                   | Free                     |
| [http.param(name)](/traffic-policy/macros/#http-requests)                             | Free                     |
| [http.param(name, default)](/traffic-policy/macros/#http-requests)                    | Free                     |
| [http.path()](/traffic-policy/macros/#http-requests)                                  | Free                     |
| [http.path\_segment(index)](/traffic-policy/macros/#http-requests)                    | Free                     |
| [http.path\_segment(index, default)](/traffic-policy/macros/#http-requests)           | Free                     |
| [http.query()](/traffic-policy/macros/#http-requests)                                 | Free                     |
| [http.query\_param(name)](/traffic-policy/macros/#http-requests)                      | Free                     |
| [http.query\_param(name, default)](/traffic-policy/macros/#http-requests)             | Free                     |
| [http.remote\_addr()](/traffic-policy/macros/#http-requests)                          | Free                     |
| [http.request\_body()](/traffic-policy/macros/#http-requests)                         | Free                     |
| [http.request\_body\_json()](/traffic-policy/macros/#http-requests)                   | Free                     |
| [http.request\_body\_query()](/traffic-policy/macros/#http-requests)                  | Free                     |
| [http.request\_method()](/traffic-policy/macros/#http-requests)                       | Free                     |
| [http.request\_uri()](/traffic-policy/macros/#http-requests)                          | Free                     |
| [http.response\_body()](/traffic-policy/macros/#http-responses)                       | Free                     |
| [http.response\_body\_json()](/traffic-policy/macros/#http-responses)                 | Free                     |
| [http.response\_body\_query()](/traffic-policy/macros/#http-responses)                | Free                     |
| [http.scheme()](/traffic-policy/macros/#http-requests)                                | Free                     |
| [http.status()](/traffic-policy/macros/#http-responses)                               | Free                     |
| [http.status\_text()](/traffic-policy/macros/#http-responses)                         | Free                     |
| [http.user\_agent()](/traffic-policy/macros/#http-requests)                           | Free                     |
| [inCidrRange(ip, cidr)](/traffic-policy/macros/#utility)                              | Free                     |
| [inCidrRanges(ip, cidrs)](/traffic-policy/macros/#utility)                            | Free                     |
| [json.decode(string)](/traffic-policy/macros/#json)                                   | 3 TPUs per GB after 1 GB |
| [json.encode(list\| map)](/traffic-policy/macros/#json)                               | 3 TPUs per GB after 1 GB |
| [list.encodeJson()](/traffic-policy/macros/#lists)                                    | Free                     |
| [object.encodeJson()](/traffic-policy/macros/#maps)                                   | Free                     |
| [object.encodeQueryString()](/traffic-policy/macros/#maps)                            | Free                     |
| [queryString.decode(string)](/traffic-policy/macros/#query-string)                    | Free                     |
| [queryString.encode(map)](/traffic-policy/macros/#query-string)                       | Free                     |
| [rand.double()](/traffic-policy/macros/#random)                                       | Free                     |
| [rand.int(min, max)](/traffic-policy/macros/#random)                                  | Free                     |
| [security.secret(string, string)](/traffic-policy/macros/#secrets)                    | Free                     |
| [string.decodeBase64()](/traffic-policy/macros/#string)                               | Free                     |
| [string.decodeJson()](/traffic-policy/macros/#string)                                 | Free                     |
| [string.decodeQueryString()](/traffic-policy/macros/#string)                          | Free                     |
| [string.encodeBase64()](/traffic-policy/macros/#string)                               | Free                     |
| [string.escapeUrl()](/traffic-policy/macros/#string)                                  | Free                     |
| [string.isJson()](/traffic-policy/macros/#string)                                     | Free                     |
| [string.isQueryString()](/traffic-policy/macros/#string)                              | Free                     |
| [string.isURL()](/traffic-policy/macros/#string)                                      | Free                     |
| [string.parseUrl()](/traffic-policy/macros/#string)                                   | Free                     |
| [string.unescapeUrl()](/traffic-policy/macros/#string)                                | Free                     |
| [url.escape(string)](/traffic-policy/macros/#url)                                     | Free                     |
| [url.parse(string)](/traffic-policy/macros/#url)                                      | Free                     |
| [url.unescape(string)](/traffic-policy/macros/#url)                                   | Free                     |
| [utility.base64\_decode(string)](/traffic-policy/macros/#base64)                      | Free                     |
| [utility.base64\_encode(string)](/traffic-policy/macros/#base64)                      | Free                     |
| [utility.basic\_auth\_encode(username, password)](/traffic-policy/macros/#basic-auth) | Free                     |
| [utility.in\_cidr\_range(ip, cidr)](/traffic-policy/macros/#utility)                  | Free                     |
| [utility.in\_cidr\_ranges(ip, cidrs)](/traffic-policy/macros/#utility)                | Free                     |
| [utility.json\_decode(string)](/traffic-policy/macros/#json)                          | Free                     |
| [utility.json\_encode(list \| map)](/traffic-policy/macros/#json)                     | Free                     |
| [utility.list\_encode\_json()](/traffic-policy/macros/#lists)                         | Free                     |
| [utility.object\_encode\_json()](/traffic-policy/macros/#maps)                        | Free                     |
| [utility.object\_encode\_query\_string()](/traffic-policy/macros/#maps)               | Free                     |
| [utility.query\_string\_decode(string)](/traffic-policy/macros/#query-string)         | Free                     |
| [utility.query\_string\_encode(map)](/traffic-policy/macros/#query-string)            | Free                     |
| [utility.rand\_double()](/traffic-policy/macros/#random)                              | Free                     |
| [utility.rand\_int(min, max)](/traffic-policy/macros/#random)                         | Free                     |
| [utility.string\_decode\_base64()](/traffic-policy/macros/#string)                    | Free                     |
| [utility.string\_decode\_json()](/traffic-policy/macros/#string)                      | Free                     |
| [utility.string\_decode\_query\_string()](/traffic-policy/macros/#string)             | Free                     |
| [utility.string\_encode\_base64()](/traffic-policy/macros/#string)                    | Free                     |
| [utility.string\_escape\_url()](/traffic-policy/macros/#string)                       | Free                     |
| [utility.string\_is\_json()](/traffic-policy/macros/#string)                          | Free                     |
| [utility.string\_is\_query\_string()](/traffic-policy/macros/#string)                 | Free                     |
| [utility.string\_is\_url()](/traffic-policy/macros/#string)                           | Free                     |
| [utility.string\_parse\_url()](/traffic-policy/macros/#string)                        | Free                     |
| [utility.string\_unescape\_url()](/traffic-policy/macros/#string)                     | Free                     |
| [utility.url\_escape(string)](/traffic-policy/macros/#url)                            | Free                     |
| [utility.url\_parse(string)](/traffic-policy/macros/#url)                             | Free                     |
| [utility.url\_unescape(string)](/traffic-policy/macros/#url)                          | Free                     |

### Variables

| Name                                                                                                        | TPU Cost |
| ----------------------------------------------------------------------------------------------------------- | -------- |
| [actions.ngrok.add\_headers.headers\_added](/traffic-policy/variables/action/#add-headers)                  | Free     |
| [actions.ngrok.basic\_auth.credentials.presented](/traffic-policy/variables/action/#basic-auth)             | Free     |
| [actions.ngrok.basic\_auth.credentials.username](/traffic-policy/variables/action/#basic-auth)              | Free     |
| [actions.ngrok.basic\_auth.credentials.authorized](/traffic-policy/variables/action/#basic-auth)            | Free     |
| [actions.ngrok.compress.already\_compressed](/traffic-policy/variables/action/#compress-response)           | Free     |
| [actions.ngrok.compress.negotiated\_algorithm](/traffic-policy/variables/action/#compress-response)         | Free     |
| [actions.ngrok.http\_request.error.code](/traffic-policy/variables/action/#http-request)                    | Free     |
| [actions.ngrok.http\_request.error.message](/traffic-policy/variables/action/#http-request)                 | Free     |
| [actions.ngrok.http\_request.attempts](/traffic-policy/variables/action/#http-request)                      | Free     |
| [actions.ngrok.http\_request.req](/traffic-policy/variables/action/#http-request)                           | Free     |
| [actions.ngrok.http\_request.res](/traffic-policy/variables/action/#http-request)                           | Free     |
| [actions.ngrok.jwt\_validation.tokens](/traffic-policy/variables/action/#jwt-validation)                    | Free     |
| [actions.ngrok.jwt\_validation.error.code](/traffic-policy/variables/action/#jwt-validation)                | Free     |
| [actions.ngrok.jwt\_validation.error.message](/traffic-policy/variables/action/#jwt-validation)             | Free     |
| [actions.ngrok.log.metadata](/traffic-policy/variables/action/#log)                                         | Free     |
| [actions.ngrok.oauth.error.code](/traffic-policy/variables/action/#oauth)                                   | Free     |
| [actions.ngrok.oauth.error.message](/traffic-policy/variables/action/#oauth)                                | Free     |
| [actions.ngrok.oauth.identity.id](/traffic-policy/variables/action/#oauth)                                  | Free     |
| [actions.ngrok.oauth.identity.email](/traffic-policy/variables/action/#oauth)                               | Free     |
| [actions.ngrok.oauth.identity.name](/traffic-policy/variables/action/#oauth)                                | Free     |
| [actions.ngrok.oauth.identity.provider\_user\_id](/traffic-policy/variables/action/#oauth)                  | Free     |
| [actions.ngrok.oauth.identity.current\_provider\_session\_id](/traffic-policy/variables/action/#oauth)      | Free     |
| [actions.ngrok.oauth.access\_token](/traffic-policy/variables/action/#oauth)                                | Free     |
| [actions.ngrok.oauth.refresh\_token](/traffic-policy/variables/action/#oauth)                               | Free     |
| [actions.ngrok.oauth.expires\_at](/traffic-policy/variables/action/#oauth)                                  | Free     |
| [actions.ngrok.oauth.session\_timed\_out](/traffic-policy/variables/action/#oauth)                          | Free     |
| [actions.ngrok.oauth.session\_max\_duration\_reached](/traffic-policy/variables/action/#oauth)              | Free     |
| [actions.ngrok.oidc.error.code](/traffic-policy/variables/action/#openid-connect-oidc)                      | Free     |
| [actions.ngrok.oidc.error.message](/traffic-policy/variables/action/#openid-connect-oidc)                   | Free     |
| [actions.ngrok.oidc.identity.id](/traffic-policy/variables/action/#openid-connect-oidc)                     | Free     |
| [actions.ngrok.oidc.identity.email](/traffic-policy/variables/action/#openid-connect-oidc)                  | Free     |
| [actions.ngrok.oidc.identity.name](/traffic-policy/variables/action/#openid-connect-oidc)                   | Free     |
| [actions.ngrok.oidc.identity.provider\_user\_id](/traffic-policy/variables/action/#openid-connect-oidc)     | Free     |
| [actions.ngrok.oidc.identity.current\_session\_id](/traffic-policy/variables/action/#openid-connect-oidc)   | Free     |
| [actions.ngrok.oidc.identity\_token](/traffic-policy/variables/action/#openid-connect-oidc)                 | Free     |
| [actions.ngrok.oidc.access\_token](/traffic-policy/variables/action/#openid-connect-oidc)                   | Free     |
| [actions.ngrok.oidc.refresh\_token](/traffic-policy/variables/action/#openid-connect-oidc)                  | Free     |
| [actions.ngrok.oidc.expires\_at](/traffic-policy/variables/action/#openid-connect-oidc)                     | Free     |
| [actions.ngrok.oidc.session\_timed\_out](/traffic-policy/variables/action/#openid-connect-oidc)             | Free     |
| [actions.ngrok.oidc.session\_max\_duration\_reached](/traffic-policy/variables/action/#openid-connect-oidc) | Free     |
| [actions.ngrok.oidc.userinfo\_refreshed](/traffic-policy/variables/action/#openid-connect-oidc)             | Free     |
| [actions.ngrok.rate\_limit.bucket\_key](/traffic-policy/variables/action/#rate-limit)                       | Free     |
| [actions.ngrok.rate\_limit.limited](/traffic-policy/variables/action/#rate-limit)                           | Free     |
| [actions.ngrok.rate\_limit.error.code](/traffic-policy/variables/action/#rate-limit)                        | Free     |
| [actions.ngrok.rate\_limit.error.message](/traffic-policy/variables/action/#rate-limit)                     | Free     |
| [actions.ngrok.redirect.matches](/traffic-policy/variables/action/#redirect)                                | Free     |
| [actions.ngrok.redirect.url](/traffic-policy/variables/action/#redirect)                                    | Free     |
| [actions.ngrok.redirect.error.code](/traffic-policy/variables/action/#redirect)                             | Free     |
| [actions.ngrok.redirect.error.message](/traffic-policy/variables/action/#redirect)                          | Free     |
| [actions.ngrok.remove\_headers.headers\_removed](/traffic-policy/variables/action/#remove-headers)          | Free     |
| [actions.ngrok.restrict\_ips.action](/traffic-policy/variables/action/#restrict-ips)                        | Free     |
| [actions.ngrok.restrict\_ips.matched\_cidr](/traffic-policy/variables/action/#restrict-ips)                 | Free     |
| [actions.ngrok.restrict\_ips.error.code](/traffic-policy/variables/action/#restrict-ips)                    | Free     |
| [actions.ngrok.restrict\_ips.error.message](/traffic-policy/variables/action/#restrict-ips)                 | Free     |
| [actions.ngrok.url\_rewrite.matches](/traffic-policy/variables/action/#url-rewrite)                         | Free     |
| [actions.ngrok.url\_rewrite.url](/traffic-policy/variables/action/#url-rewrite)                             | Free     |
| [actions.ngrok.url\_rewrite.error.code](/traffic-policy/variables/action/#url-rewrite)                      | Free     |
| [actions.ngrok.url\_rewrite.error.message](/traffic-policy/variables/action/#url-rewrite)                   | Free     |
| [actions.ngrok.verify\_webhook.verified](/traffic-policy/variables/action/#verify-webhook)                  | Free     |
| [conn.bytes\_in](/traffic-policy/variables/connection/#connbytes-in)                                        | Free     |
| [conn.bytes\_out](/traffic-policy/variables/connection/#connbytes-out)                                      | Free     |
| [conn.client\_ip](/traffic-policy/variables/connection/#connclient-ip)                                      | Free     |
| [conn.client\_port](/traffic-policy/variables/connection/#connclient-port)                                  | Free     |
| [conn.server\_ip](/traffic-policy/variables/connection/#connserver-ip)                                      | Free     |
| [conn.server\_port](/traffic-policy/variables/connection/#connserver-port)                                  | Free     |
| [conn.server\_region](/traffic-policy/variables/connection/#connserver-region)                              | Free     |
| [conn.ts.start](/traffic-policy/variables/connection/#conntsstart)                                          | Free     |

## Traffic Policy Unit (TPU) discounts at scale

The Pay-as-you-go plan provides discounts on TPUs for large scale deployments so you always get the best price as you grow. Discounted pricing is as follows:

| Count | TPU Cost    |
| ----- | ----------- |
| 0+    | \$1/100k    |
| 1M+   | \$.75/100k  |
| 10M+  | \$.55/100k  |
| 100M+ | \$0.35/100k |
| 1B+   | \$0.25/100k |


Built with [Mintlify](https://mintlify.com).