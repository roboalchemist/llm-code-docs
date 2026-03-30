# Source: https://fly.io/docs/networking/understanding-cloudflare/

Title: Understanding Cloudflare

URL Source: https://fly.io/docs/networking/understanding-cloudflare/

Markdown Content:
[Docs](https://fly.io/docs/)[Networking](https://fly.io/docs/networking)Understanding Cloudflare![Image 1: Illustration by Annie Ruygt of a big cloud with Fly balloons exiting from inside it](https://fly.io/static/images/understanding-cloudfare.png)
Many Fly.io apps use Cloudflare—sometimes just for DNS, sometimes with proxying enabled, and sometimes for both. This guide covers the supported configurations, how to set them up, and what to watch out for when using Cloudflare with Fly.io.

[](https://fly.io/docs/networking/understanding-cloudflare/#dns-only-setup)DNS-only setup
-----------------------------------------------------------------------------------------

This is the simplest and most reliable way to use Cloudflare with Fly.io. To configure a DNS-only setup:

1.   Point your domain to your Fly.io app using an `AAAA` record for the IPv6 address and an `A` record for the IPv4 address. 
2.   Alternatively, use a `CNAME` record pointing to your app’s unique target, shown in your certificate setup instructions. 
3.   Disable the Cloudflare proxy (select “grey cloud”) for these records. 
4.   SSL certificates will be handled by Fly.io automatically using Let’s Encrypt. 

[](https://fly.io/docs/networking/understanding-cloudflare/#cdn-proxy-setup-quot-orange-cloud-quot)CDN proxy setup (“orange cloud”)
-----------------------------------------------------------------------------------------------------------------------------------

Enabling Cloudflare’s proxy gives you caching and DDoS protection, but it also changes how SSL certificates work. Cloudflare terminates TLS traffic, which means Fly.io can’t use its default TLS-ALPN-01 certificate issuance process. The key to a smooth setup is a `_fly-ownership` TXT record that proves domain ownership to Fly.io and allows certificate validation to work through Cloudflare’s proxy.

**Important:** Wildcard certificates (e.g. `*.example.com`) cannot be issued automatically through Cloudflare’s proxy, because Let’s Encrypt requires a DNS-01 challenge for wildcards and Cloudflare’s Universal SSL can interfere with it. To use a wildcard certificate behind Cloudflare’s proxy, import a [Cloudflare Origin Certificate](https://fly.io/docs/networking/understanding-cloudflare/#using-a-cloudflare-origin-certificate) instead.

### [](https://fly.io/docs/networking/understanding-cloudflare/#recommended-setup)Recommended setup

1.   Add your domain to your Fly app: 

```
fly certs add example.com
```

1.   Add a `_fly-ownership` TXT record in Cloudflare DNS. Run `fly certs setup` to see the required record: 

```
fly certs setup example.com
```

Add the TXT record shown in the output. This record proves domain ownership to Fly.io.

1.   Configure your DNS records in Cloudflare:

    *   Add an `A` record pointing to your Fly app’s IPv4 address. 
    *   Add an `AAAA` record pointing to your Fly app’s IPv6 address. 
    *   Alternatively, use a `CNAME` record pointing to your app’s `.fly.dev` target. 
    *   Enable the Cloudflare proxy (orange cloud) for these records. 

2.   Set SSL mode in Cloudflare to **Full (strict)**.

3.   Enable **Always Use HTTPS** in Cloudflare (recommended).

Fly.io will automatically issue a Let’s Encrypt certificate via the HTTP-01 challenge, which works through Cloudflare’s proxy when the ownership TXT record is in place. Run `fly certs check example.com` to monitor validation progress.

Some Cloudflare configurations will block HTTP-01 challenges altogether. If certificate issuance is not progressing, import a [Cloudflare Origin Certificate](https://fly.io/docs/networking/understanding-cloudflare/#using-a-cloudflare-origin-certificate) instead.

### [](https://fly.io/docs/networking/understanding-cloudflare/#using-a-cloudflare-origin-certificate)Using a Cloudflare Origin Certificate

If automatic certificate issuance doesn’t work for your setup, or if you need a wildcard certificate (like `*.example.com`), you can import a Cloudflare Origin Certificate instead.

1.   Generate a Cloudflare Origin Certificate in the Cloudflare dashboard:

    *   Go to SSL/TLS > Origin Server > Create Certificate. 
    *   Choose the hostnames to cover (for example, `example.com` and `*.example.com`). 
    *   Choose a validity period (Cloudflare offers up to 15 years). 
    *   Keep the page open — Cloudflare only shows the private key once. 

2.   Import the certificate to Fly.io in your app dashboard under **Certificates**. You can paste the certificate and private key directly from Cloudflare. Alternatively, save them as files and use the CLI:

```
fly certs import example.com --fullchain cert.pem --private-key key.pem
fly certs import "*.example.com" --fullchain cert.pem --private-key key.pem
```

1.   Add the `_fly-ownership` TXT record shown in the certificate setup details, if you haven’t already set one up.

2.   Configure your DNS records and Cloudflare SSL mode as described in the [recommended setup](https://fly.io/docs/networking/understanding-cloudflare/#recommended-setup) above.

Custom and ACME certificates can coexist for the same hostname. The custom certificate is served as primary, and any ACME certificate acts as an automatic fallback.

[](https://fly.io/docs/networking/understanding-cloudflare/#common-issues-to-watch-for)Common issues to watch for
-----------------------------------------------------------------------------------------------------------------

### [](https://fly.io/docs/networking/understanding-cloudflare/#general-issues)General issues

*   Always use “Full (strict)” in Cloudflare when connecting to Fly.io. Using “Flexible” mode may cause redirect loops. 
*   Only one application should manage certificates for a subdomain or apex domain. Using more than one can cause conflicts. 

### [](https://fly.io/docs/networking/understanding-cloudflare/#acme-specific-issues)ACME-specific issues

These issues apply when using Let’s Encrypt (ACME) certificates behind Cloudflare’s proxy. They do not apply if you are using a [Cloudflare Origin Certificate](https://fly.io/docs/networking/understanding-cloudflare/#using-a-cloudflare-origin-certificate).

*   Check that your domain allows Let’s Encrypt with a CAA record like: 

```
example.com.  CAA  0 issue "letsencrypt.org"
```

*   Let’s Encrypt has rate limits. Check the certificate status tab in the Fly.io dashboard if issuance fails. 
*   DNS-01 certificates will conflict with Cloudflare Universal SSL. This happens when Cloudflare’s Universal SSL automatically inserts hidden ACME challenge TXT records that don’t appear in your DNS dashboard. These ghost records interfere with Let’s Encrypt’s validation process. The best choice in this situation is to import a [Cloudflare Origin Certificate](https://fly.io/docs/networking/understanding-cloudflare/#using-a-cloudflare-origin-certificate) instead. 

### [](https://fly.io/docs/networking/understanding-cloudflare/#custom-certificate-issues)Custom certificate issues

*   Unlike Let’s Encrypt certificates, which renew automatically, custom certificates must be manually renewed and re-imported before they expire. Cloudflare Origin Certificates can be issued with long validity periods (up to 15 years), but you should still track expiry. 

[](https://fly.io/docs/networking/understanding-cloudflare/#tools-for-debugging)Tools for debugging
---------------------------------------------------------------------------------------------------

These tools can help when diagnosing certificate or DNS issues:

*   `fly certs check <hostname>`: Check ownership TXT status, custom certificate status, and ACME certificate status all in one place. This is the best starting point for debugging. 
*   [crt.sh](https://crt.sh/): Check issued certificates. 
*   [DNSChecker](https://dnschecker.org/): Confirm DNS propagation. 
*   [Let’s Debug](https://letsdebug.net/): Analyze Let’s Encrypt certificate validation issues. 
*   dig: Inspect DNS records from the command line. 

For example:

```
fly certs check your-app.example.com

dig AAAA your-app.example.com

dig TXT _fly-ownership.your-app.example.com
```

*   [Custom domain guide](https://fly.io/docs/networking/custom-domain/)
*   [Certificates API reference](https://fly.io/docs/machines/api/certificates-resource/)
*   [flyctl certs commands](https://fly.io/docs/flyctl/certs/)
*   [fly certs import reference](https://fly.io/docs/flyctl/certs-import/)
