# Source: https://northflank.com/docs/v1/application/domains/domain-registrar-guides/add-a-cloudflare-domain-to-northflank.md

# Add a Cloudflare domain to Northflank

Configure your domain by following these instructions or read [Cloudflare's documentation](https://developers.cloudflare.com/dns/manage-dns-records/how-to/) for more platform specific information.

Cloudflare features such as SSL/TLS encryption, caching, bot protection, and always online are only active while Cloudflare proxy is enabled for a domain. You can add a [custom security rule](#configure-cloudflare-security-rules) to avoid issues with certificate regeneration while Cloudflare security features are active. Domains configured with [wildcard certificate generation](wildcard-domains-and-certificates#wildcard-certificate-generation) do not require custom security rules for certificate regeneration.

> [!important] 
> You cannot enable Cloudflare proxy while Northflank is verifying your subdomains. You can temporarily disable the proxy to verify the subdomain, generate an initial certificate, and re-enable the proxy afterwards.

## Add and verify a Cloudflare domain

To add and verify Cloudflare domains and subdomains on Northflank:

1. [Add your domain to Northflank](https://northflank.com/docs/v1/application/domains/add-a-domain-to-your-account)

2. Open Cloudflare in a new browser tab or window and log in to your Cloudflare dashboard

3. Select the domain you are adding to Northflank

4. Select the DNS tab and add record

5. Open the type dropdown and scroll down to choose TXT to verify a domain namespace, or CNAME to add a subdomain

6. Copy the record name from Northflank into the name field

7. Set the TTL (time to live) to 2 minutes (you can select a higher value, but it might take longer to register changes) and disable the proxy

8. Copy the record content from Northflank into the target field and save the record

![Adding a TXT record to verify a domain on Cloudflare](https://assets.northflank.com/documentation/v1/application/domains/domain-registrar-guides/cloudflare/cloudflare-domain.png)

1. Return to the domains page on Northflank and select verify on the entry for your domain

2. Your domain should verify shortly. If not, check you have entered the record correctly and try again.

3. Enable the proxy option for the record in Cloudflare, if desired

4. You can now [link your domain to a port](https://northflank.com/docs/v1/application/domains/link-a-domain-to-a-port)

> [!note] 
> If subdomain records are created using the proxied setting the connection will use a Cloudflare certificate. Use DNS only to use a Northflank-generated certificate and to manually set the TTL.

### Add an apex domain

You can add an apex domain on Cloudflare by adding a CNAME record with `@` as the name and the Northflank generated content as the target.

![Adding a CNAME record to link an apex domain on Cloudflare](https://assets.northflank.com/documentation/v1/application/domains/domain-registrar-guides/cloudflare/cloudflare-apex-cname.png)

## Use the Cloudflare proxy

You can use the Cloudflare proxy with subdomains on Northflank, but you must disable the Cloudflare proxy for any DNS records you are using to verify with Northflank. If you have created a proxied record to verify your Northflank subdomain, disable the proxy and manually verify the domain on Northflank again.

You can configure the Cloudflare proxy for subdomains by selecting your domain on Cloudflare and navigating to the records page under DNS in the menu. Click edit to configure the proxy an individual record.

You will need to a [add custom security rule](#configure-cloudflare-security-rules) or disable the Cloudflare proxy in order to generate the initial certificate for a subdomain. To generate a certificate for a subdomain you must first link it to a service in Northflank, which automatically triggers certificate generation. If certificate generation has been triggered while the Cloudflare proxy is enabled you can [add a custom security rule](#configure-cloudflare-security-rules) or disable the proxy and re-trigger certificate generation from the subdomain settings in Northflank before re-enabling the Cloudflare proxy.

## Configure Cloudflare SSL/TLS

You can configure Cloudflare's SSL/TLS encryption mode via the SSL/TLS overview in your Cloudflare dashboard. You are recommended to use the `Full (Strict)` mode for to serve all requests securely and ensure Cloudflare recognises the Northflank-generated certificates for your subdomains.

The `flexible` SSL/TLS configuration may cause issues if Cloudflare does not enable SSL/TLS between Cloudflare and Northflank.

To use Cloudflare proxy with domains other than your root domain (`example.com`) and immediate subdomains (`*.example.com`) you will need to use Cloudflare's Advanced Certificate Manager feature.

## Use Cloudflare cache

You can [configure how Cloudflare caches your content](https://developers.cloudflare.com/cache/concepts/default-cache-behavior/) when the Cloudflare proxy is enabled for a domain on the configuration page of the caching section in your Cloudflare dashboard.

Cloudflare will cache static assets such as images and archives, but not HTML and JSON content. You may need to purge the cache or configure your cache settings if you do not see the expected changes from your Northflank service.

## Configure Cloudflare security rules

Northflank may be unable to generate certificates for your subdomains while Cloudflare security features such as bot protection are enabled.

To avoid issues with certificate regeneration you can add a custom security rule in the security section of your Cloudflare dashboard. You can also add these security rules to enable initial certificate generation with proxied subdomains.

| Field | Operator | Value | Action |
| - | - | - |
| URI Path  | ends with  | `/.well-known/dns-challenge/:token` | Skip |
| URI Path  | ends with  | ` /.well-known/acme-challenge/:token` | Skip |

#### Rule expression

```text
(ends_with(http.request.uri.path, " /.well-known/dns-challenge/:token")) or
(ends_with(http.request.uri.path, " /.well-known/acme-challenge/:token"))
```

You can then skip Cloudflare Web Application Firewall (WAF) components for these paths to allow challenges to succeed.

![Adding a custom security rule in the Cloudflare dashboard](https://assets.northflank.com/documentation/v1/application/domains/domain-registrar-guides/cloudflare/cloudflare-domain.png)

## Next steps

- [Link a domain to a port: How to link and unlink domains and subdomains with specific ports on your deployments.](/v1/application/domains/link-a-domain-to-a-port)
- [Add public ports: Configure ports to expose your services on the internet.](/v1/application/network/configure-ports#public-ports)
