# Source: https://render.com/docs/custom-domains.md

# Custom Domains on Render


> *Hobby workspaces support a maximum of two custom domains across all services.*
>
> Professional workspaces and higher support unlimited custom domains.

You can apply your own custom domains to Render [web services](web-services) and [static sites](static-sites). Services with a custom domain also keep their `onrender.com` subdomain.

Render automatically creates and renews TLS certificates for all custom domains, including [wildcard domains](#wildcard-domains). All HTTP traffic to a custom domain is automatically redirected to HTTPS.

Apply a custom domain in three steps:

1. [Add your domain in the Render Dashboard](#1-add-your-domain-in-the-render-dashboard).
2. [Configure DNS](#2-configure-dns-with-your-provider) with your domain's provider.
3. [Verify your domain](#3-verify-your-domain) in the Render Dashboard.

These steps are detailed below.

## 1. Add your domain in the Render Dashboard

1. In the [Render Dashboard](https://dashboard.render.com), select the service that will use your custom domain.

   - Only web services and static sites support custom domains.

2. Open the service's *Settings* page and scroll down to the *Custom Domains* section:

   [image: Adding a custom domain in the Render Dashboard]

3. Click *+ Add Custom Domain* and provide your custom domain name.

> *If your domain includes Unicode characters,* first convert it to Punycode with a tool like [Punycoder](https://www.punycoder.com/).
>
>    For example, you would provide `ëxample.com` as `xn--xample-ova.com`.

4. Click *Save*. Your custom domain now appears in the list:

   [image: Added custom domain with DNS update needed]

   - *If you add a `www` subdomain* (e.g., `www.example.org`), Render automatically adds the corresponding root domain and redirects it to the `www` subdomain. This is shown in the screenshot above.

   - *If you add a root domain* (e.g., `example.org`), Render automatically adds the corresponding `www` subdomain and redirects it to the root domain.

*Your domain does not yet point to your service!* Next, you'll [configure DNS](#2-configure-dns-with-your-provider).

## 2. Configure DNS with your provider

> *Remove any `AAAA` records from your domain while configuring DNS.*
>
> `AAAA` records map to an IPv6 address, and Render uses IPv4. These records can cause unexpected behavior for your custom domain.

1. Log in to your custom domain's DNS provider (such as Cloudflare, Namecheap, or GoDaddy).
2. Navigate to the DNS settings for your domain.
3. Add DNS records for your domain based on your provider, then return here:

   - [Cloudflare](configure-cloudflare-dns)
   - [Namecheap](configure-namecheap-dns)
   - [All other providers](configure-other-dns)

> *If you're adding a wildcard domain,* see [additional instructions](#wildcard-domains).

4. Return to the Render Dashboard and [verify your domain](#3-verify-your-domain).

## 3. Verify your domain

1. Return to your service's *Custom Domains* settings in the [Render Dashboard](https://dashboard.render.com):

   [image: Added custom domain with DNS update needed]

2. Click the *Verify* button next to your custom domain.

   - If verification fails, your DNS settings might not have propagated yet. Wait a few minutes and try again. See also [Speeding up domain verification](#speeding-up-domain-verification).

3. If verification succeeds, Render issues a TLS certificate for your domain and updates the verification status:

   [image: Verified domains in the Render Dashboard]

4. Try visiting your custom domain in a browser.

   - If you see a *502 Bad Gateway* error, Render might still be updating routing rules for your service. Wait a few minutes and try again.

5. When your custom domain loads successfully, you're good to go!

### Speeding up domain verification

We recommend removing cached entries in public DNS servers after updating your DNS records. This is especially important if you're updating nameservers for your domains. Clearing the cache will speed up DNS verification and TLS certificate issuance for your domains.

Use the links below to clear cached records in popular public DNS servers:

- [Flush Google Public DNS Cache](https://developers.google.com/speed/public-dns/cache)
- [Purge Cloudflare Public DNS Cache](https://1.1.1.1/purge-cache/)
- [Refresh OpenDNS Cache](https://cachecheck.opendns.com/)

## Disabling your `onrender.com` subdomain

If your service has at least one custom domain, you can disable the service's default `onrender.com` subdomain. After you do, your service is reachable exclusively at its custom domain(s).

1. In the [Render Dashboard](https://dashboard.render.com), select the service that you want to disable the `onrender.com` subdomain for.
2. Open the service's *Settings* page and scroll down to the *Custom Domains* section:

   [image: Disabling the `onrender.com` subdomain]

3. Toggle the *Render Subdomain* setting to *Disabled* and confirm.

After you disable your `onrender.com` subdomain, all requests to it receive a 404 response. These requests do _not_ reach your service. You can re-enable the subdomain at any time.

## Advanced DNS configuration

### Wildcard domains

You can apply a wildcard domain (e.g., `*.example.org`) to a Render service to point all matching subdomains (`docs.example.org`, `blog.example.org`, etc.) to it:

[image: Wildcard Custom Domain with DNS update needed]

This configuration requires setting _three_ `CNAME` DNS records with your provider:

| Name | Value |
| --- | --- |
| `*` | Your service's `onrender.com` subdomain, available in the [Render Dashboard](https://dashboard.render.com). *Example:* `svelte.onrender.com` |
| `_acme-challenge` | Has the format `[your-service-id].verify.renderdns.com` Enables Render to manage certificate issuance and renewal for your wildcard domain via Let's Encrypt. *Example:* `svelte.verify.renderdns.com` |
| `_cf-custom-hostname` | Has the format `[your-service-id].hostname.renderdns.com` Enables Cloudflare (Render's DDoS protection provider) to validate ownership of your wildcard domain. *Example:* `svelte.hostname.renderdns.com` |

#### Using Cloudflare DNS with wildcard domains

If you manage your custom domain with Cloudflare DNS, note the following:

If you add a wildcard domain (e.g., `*.example.com`) to Render but _not_ the corresponding root domain (e.g., `example.com`), using Cloudflare with [proxying enabled](https://community.cloudflare.com/t/what-is-the-proxied-feature-in-cloudflare/32887) (orange cloud) will cause traffic for the root domain to be sent to the _same Render destination_ as your wildcard domain.

To prevent service disruptions, make sure to _disable_ proxying for your root domain (gray cloud). If you have any questions, please get in touch at support@render.com.

### CAA records

> If your custom domain doesn't define any `CAA` records, you can ignore this section.

If your custom domain defines [`CAA` records](https://en.wikipedia.org/wiki/DNS_Certification_Authority_Authorization), make sure to define records for Render's certificate authorities:

- Let's Encrypt (`letsencrypt.org`)
- Google Trust Services (`pki.goog; cansignhttpexchanges=yes`)

Additionally, if you add a [wildcard domain](#wildcard-domains), make sure to define corresponding `issuewild` records for each authority.

```
example.com IN CAA 0 issue "letsencrypt.org"
example.com IN CAA 0 issuewild "letsencrypt.org"
example.com IN CAA 0 issue "pki.goog; cansignhttpexchanges=yes"
example.com IN CAA 0 issuewild "pki.goog; cansignhttpexchanges=yes"
```