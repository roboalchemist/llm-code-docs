# Source: https://render.com/docs/configure-other-dns.md

# Configuring DNS Providers — Point a custom domain to your Render service.


> This guide assumes you've added a custom domain to your service in the Render Dashboard. If you haven't yet, first complete [this step](custom-domains#1-add-your-domain-in-the-render-dashboard).

This article explains how to configure your DNS provider to point your [custom domain](custom-domains) to Render. Some of these steps might not apply to your provider. We have specific guides for popular DNS providers:

- [Configuring Cloudflare DNS](configure-cloudflare-dns)
- [Configuring Namecheap DNS](configure-namecheap-dns)

We're also happy to help you set things up—just contact us via the Help link in the dashboard.

> *Remove any `AAAA` records from your domain while configuring DNS.*
>
> `AAAA` records map to an IPv6 address, and Render uses IPv4. These records can cause unexpected behavior for your custom domain.

## Configuring root domains

### Using an `ANAME` or `ALIAS` record

When you're pointing a root domain like `example.com` to your Render subdomain, you can use `ANAME` or `ALIAS` records if your DNS provider supports them. These records are not part of the standard DNS protocol but are implemented by some providers to make it easy to point root domains to other domains.

[DNSimple](https://dnsimple.com/), [DNS Made Easy](https://dnsmadeeasy.com/), [Name.com](https://www.name.com/) and [NS1](https://ns1.com/) all support one or both of these record types.

- `ANAME` records let you refer to other domains just like `CNAME` records, but behave like `A` records in that they ultimately resolve to an IP address. This is also often called [CNAME flattening](https://support.cloudflare.com/hc/en-us/articles/200169056-Understand-and-configure-CNAME-Flattening). Read more [here](https://dnsmadeeasy.com/services/anamerecords/).

- `ALIAS` records map a root domain to another domain while coexisting with other record types for the root domain. Read more [here](https://support.dnsimple.com/articles/alias-record/).

To configure your custom root domain for Render, add an `ANAME` or `ALIAS` record for your root domain to point to your app's Render subdomain. For example, if your app subdomain is `example.onrender.com` and your custom domain is `example.com`, you should add an `ANAME` or `ALIAS` record for `example.com` and point it to `example.onrender.com`.

### Using an `A` record

If your DNS provider does not support `ANAME` or `ALIAS` records or `CNAME` flattening, you will need to add an `A` record to point to your Render app. `A` records point to IP addresses, and you can use `216.24.57.1` to point your root domain to Render's load balancer IP.

Once you have made changes to your DNS records, these need to propagate across the internet - this can delay the verification process. Use the `dig` command or an online service like [dnschecker](https://dnschecker.org/) to verify the correct response. If you see additional values in the DNS response other than those provided by Render, your DNS provider may have some defaults or features (e.g., domain forwarding) that need to be removed/disabled.

> If you are using Cloudflare as a DNS provider, you <i>must</i> use a CNAME record instead of an A record. See <a href="/docs/configure-cloudflare-dns">configuring Cloudflare DNS</a> for instructions.

## Configuring `www` and other subdomains

For non-root domains, you should always add a `CNAME` record pointing to your app's Render subdomain. For example, if your Render subdomain is `example.onrender.com` and your custom domain is `www.example.com`, you should add a CNAME record for `www` and point it to `example.onrender.com`.