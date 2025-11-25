# Source: https://docs.upsun.com/domains/cdn/cloudflare.md

# Set up your Cloudflare CDN

You can [use a CDN](https://docs.upsun.com/domains/cdn.md) to deliver your site's content to users more quickly.

## Before you begin

You need:

- An up-and-running Upsun project
- A [Cloudflare](https://www.cloudflare.com/) CDN subscription

## 1. Avoid double-caching

To avoid stale content that can't be cleared,
avoid using Cloudflare with [HTTP caching](https://docs.upsun.com/define-routes/cache.md).

For routes where Cloudflare is used,
disable HTTP caching using the following configuration:

```yaml  {location=".upsun/config.yaml"}
https://{default}/:
    type: upstream
    ...
    cache:
        enabled: false
```

## 2. Set up your Cloudflare CDN

To properly configure your Cloudflare CDN,
see the Cloudflare official documentation on [how to get started](https://developers.cloudflare.com/cache/get-started/).
Then set up a [custom domain](https://docs.upsun.com../steps.md).
To get the [DNS challenge to succeed](https://docs.upsun.com../troubleshoot.md#ownership-verification),
have your CDN point to your [project's target URL](https://docs.upsun.com../../domains/steps.md#1-get-the-target-for-your-project).

## 3. Handle apex domains

To start routing client traffic through Cloudflare,
you need to [create `CNAME` records for your domain names](https://docs.upsun.com../../domains/steps/dns.md)
through your DNS provider.

But `CNAME` records can't point to apex domains.
As a workaround, Cloudflare offers [`HTTPS` records](https://developers.cloudflare.com/dns/manage-dns-records/reference/dns-record-types/#svcb-and-https) and [`CNAME` flattening](https://developers.cloudflare.com/dns/additional-options/cname-flattening/).

## 4. Mitigate security risks

Like all networks exposed to the internet, your origin server may become the target of security attacks.
The best way to protect your site from threats like on-path attacks, spoofing attacks, or credential stuffing,
is to configure mutual TLS (mTLS).

[mTLS](https://www.cloudflare.com/en-gb/learning/access-management/what-is-mutual-tls/) not only has both parties in a connection authenticate each other
through the TLS protocol.
It also ensures that requests can't be sent directly to the origin server (Upsun).
Instead, requests must transit through Cloudflare first.

**Note**: 

mTLS is only compatible with environments where you have attached domains you own, meaning:

 - Your production environment
 - Each preview environment where you have [attached a custom domain](https://docs.upsun.com/domains/steps/custom-domains-preview-environments.md)

Therefore, mTLS is **not** compatible with preview environments created by a [source code integration](https://docs.upsun.com/integrations/source.md).

If you can't use mTLS, you can still take the following measures to protect your site from on-path attacks:

1. [Enable full strict SSL/TLS encryption](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full-strict/). 
   Any communication between a client and Cloudflare or between Cloudflare and your Upsun server is then encrypted through HTTPS.
   In addition, Cloudflare checks that your Upsun server's [TLS certificate](https://docs.upsun.com/glossary.md#transport-layer-security-tls)
   was issued by a trusted certificate authority.
   This confirms the client is truly communicating with your Upsun server.

2. [Enable HTTP strict transport security (HSTS)](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/http-strict-transport-security/). 
   This ensures that your HTTPS connections can't be downgraded to HTTP.

