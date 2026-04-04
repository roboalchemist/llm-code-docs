# Source: https://northflank.com/docs/v1/application/domains/use-a-cdn.md

# Use a CDN

You can enable a CDN for your subdomains to serve static content from your deployments. This can improve the speed at which your content is delivered to users without needing to deploy in multiple regions, and reduce the load on your instances.

You may also choose to deliver stale content, which means your site will still be accessible even if your deployment becomes unavailable.

There is no extra cost to use a CDN with your Northflank deployment.

> [!note] 
> [Click here](https://app.northflank.com/s/account/domains) to view your account domains page.

## Enable CDN for a subdomain

You must configure each subdomain individually to use a CDN.

To enable CDN on a subdomain, navigate to your [team domains page](https://app.northflank.com/s/account/domains). Open the settings  for the subdomain you want to use a CDN with and select the CDN view.

Your subdomain must be [linked to a deployment's port](link-a-domain-to-a-port) to use a CDN.

[Configure the CDN settings](#configure-cdn-settings), or leave as default, and enable CDN. The CDN status will show that the CDN is enabling and the network diagram will update to show the CDN sitting in front of the Northflank load balancer. The CDN will become active usually within a few seconds, and up to a few minutes.

To disable the CDN, click disable CDN. The status and network diagram will update when the CDN has been disabled.

![Configuring CDN settings for a subdomain in the Northflank application](https://assets.northflank.com/documentation/v1/application/domains/use-a-cdn/cdn-settings.png)

## Configure Fastly CDN

#### Logging

If enabled, Fastly logs for your services will be streamed to Northflank. Logs from Fastly can be viewed by [navigating to a container](https://northflank.com/docs/v1/application/observe/view-logs#view-logs) in the deployment service associated with the subdomain, and selecting `all containers` from the observability header.

#### HTTP/3

You can enable connections between end users and Fastly to be upgraded to HTTP/3 (QUIC protocol). Connections between Northflank and Fastly will still use up to HTTP/2. HTTP/3 requires that all connections are secured using TLS. [Learn more.](https://docs.fastly.com/en/guides/enabling-http3-for-fastly-services)

#### Force TLS and enable HSTS

If enabled, all requests must use TLS and will be redirected from `http` to `https`. You must set the HSTS duration, it is recommended to set this to the maximum possible value of `31557600` (1 year) for production applications.

#### Serve stale content on origin failure

When enabled Fastly will serve stale content to your users if your Northflank deployment cannot be reached. The `Stale if Error TTL` defines how long content will be served for if the origin cannot be reached. The default value is `43200` seconds, or 12 hours.

#### Default TTL

Set the default time-to-live (TTL) in seconds. Fastly will serve cached data for the defined TTL, and then fetch from the origin after the TTL has expired. The default value is `3600`, or 1 hour.

#### Compression

If enabled, content sent from Fastly to end users will be compressed using the selected format (`gzip` or `Brotli`). This can potentially improve speeds as well as reduce costs.

## Next steps

- [Add a domain: Add your domain name to your Northflank account.](/v1/application/domains/add-a-domain-to-your-account)
- [Link a domain to a port: How to link and unlink domains and subdomains with specific ports on your deployments.](/v1/application/domains/link-a-domain-to-a-port)
- [Add public ports: Configure ports to expose your services on the internet.](/v1/application/network/configure-ports#public-ports)
- [Domain registrar guides: Follow walkthroughs to add and verify domains on Cloudflare, NS1, OVH, and Namecheap.](/v1/application/domains/domains-on-northflank#custom-domains-and-subdomains)
