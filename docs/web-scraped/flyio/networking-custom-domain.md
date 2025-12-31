# Source: https://fly.io/docs/networking/custom-domain/

\*)\]:mx-auto \[body\_:where(&\>\*)\]:max-w-2xl \[body:not(.toc)\_:where(&\>\*)\]:lg:mx-\[calc(50%-min(50%,35rem))\] \[body\_:where(&\>\*)\]:lg:max-w-3xl min-w-0 relative\"\>

# Custom domains 

![image](/static/images/docs-ui.webp)

When you create a Fly App, it is automatically given a `fly.dev` subdomain, based on the app's name. This is great for testing, but when you want to go to full production you'll want your application to appear on your own domain and have HTTPS set up for you as it is with your `.fly.dev` domain. You can do this by adding your domain to your Fly App, then configuring DNS records through your DNS provider.

## [](#add-a-custom-domain-for-your-app)[Add a custom domain for your app] 

To add a custom domain, first attach your domain to your Fly App to get DNS configuration instructions, then configure your DNS records with your DNS provider.

### [](#add-your-domain-to-your-app)[Add your domain to your app] 

Attach your domain to your Fly App. This prepares your app to generate TLS certificates and handle traffic for your custom domain, and shows you the DNS configuration options for your setup.

You can add your domain with flyctl or in your app [dashboard](https://fly.io/dashboard/) under **Certificates**.

For example, using the CLI:

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PGcgYnVmZmVyZWQtcmVuZGVyaW5nPSJzdGF0aWMiPjxwYXRoIGQ9Ik05LjkxMiA4LjAzN2gyLjczMmMxLjI3NyAwIDIuMzE1LS45NjIgMi4zMTUtMi4yMzdhMi4zMjUgMi4zMjUgMCAwMC0yLjMxNS0yLjMxSDIuOTU5bTEwLjIyOCA5LjAxSDIuOTU5TTYuODAyIDhIMi45NTkiPjwvcGF0aD48cGF0aCBkPSJNMTEuMDgxIDYuNDY2TDkuNTMzIDguMDM3bDEuNTQ4IDEuNTcxIj48L3BhdGg+PC9nPjwvc3ZnPg==) [ Wrap text ]

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiPjxnIGJ1ZmZlcmVkLXJlbmRlcmluZz0ic3RhdGljIj48cGF0aCBkPSJNMTAuNTc2IDcuMjM5YzAtLjk5NS0uODItMS44MTUtMS44MTUtMS44MTVIMy4zMTVjLS45OTUgMC0xLjgxNS44Mi0xLjgxNSAxLjgxNXY1LjQ0NmMwIC45OTUuODIgMS44MTUgMS44MTUgMS44MTVoNS40NDZjLjk5NSAwIDEuODE1LS44MiAxLjgxNS0xLjgxNVY3LjIzOXoiPjwvcGF0aD48cGF0aCBkPSJNMTAuNTc2IDEwLjU3N2gyLjEwOUExLjgyNSAxLjgyNSAwIDAwMTQuNSA4Ljc2MVYzLjMxNUExLjgyNiAxLjgyNiAwIDAwMTIuNjg1IDEuNUg3LjIzOWMtLjk5NiAwLTEuODE1LjgxOS0xLjgxNiAxLjgxNXYxLjYxNyI+PC9wYXRoPjwvZz48L3N2Zz4=) [ Copy to clipboard ]

``` 
fly certs add example.com
```

This command will show you the applicable DNS configuration options for your setup, including:

-   A and AAAA records
-   CNAME records
-   Proxy setup (if using a CDN)
-   DNS-01 challenge (required for wildcards, optional for pre-traffic certificate generation)

If you are adding a wildcard domain with the CLI, put quotes around the hostname to avoid shell expansion:

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PGcgYnVmZmVyZWQtcmVuZGVyaW5nPSJzdGF0aWMiPjxwYXRoIGQ9Ik05LjkxMiA4LjAzN2gyLjczMmMxLjI3NyAwIDIuMzE1LS45NjIgMi4zMTUtMi4yMzdhMi4zMjUgMi4zMjUgMCAwMC0yLjMxNS0yLjMxSDIuOTU5bTEwLjIyOCA5LjAxSDIuOTU5TTYuODAyIDhIMi45NTkiPjwvcGF0aD48cGF0aCBkPSJNMTEuMDgxIDYuNDY2TDkuNTMzIDguMDM3bDEuNTQ4IDEuNTcxIj48L3BhdGg+PC9nPjwvc3ZnPg==) [ Wrap text ]

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiPjxnIGJ1ZmZlcmVkLXJlbmRlcmluZz0ic3RhdGljIj48cGF0aCBkPSJNMTAuNTc2IDcuMjM5YzAtLjk5NS0uODItMS44MTUtMS44MTUtMS44MTVIMy4zMTVjLS45OTUgMC0xLjgxNS44Mi0xLjgxNSAxLjgxNXY1LjQ0NmMwIC45OTUuODIgMS44MTUgMS44MTUgMS44MTVoNS40NDZjLjk5NSAwIDEuODE1LS44MiAxLjgxNS0xLjgxNVY3LjIzOXoiPjwvcGF0aD48cGF0aCBkPSJNMTAuNTc2IDEwLjU3N2gyLjEwOUExLjgyNSAxLjgyNSAwIDAwMTQuNSA4Ljc2MVYzLjMxNUExLjgyNiAxLjgyNiAwIDAwMTIuNjg1IDEuNUg3LjIzOWMtLjk5NiAwLTEuODE1LjgxOS0xLjgxNiAxLjgxNXYxLjYxNyI+PC9wYXRoPjwvZz48L3N2Zz4=) [ Copy to clipboard ]

``` 
fly certs add "*.example.com"
```

Use `fly certs check <hostname>` to check the certificate status and validation progress, or `fly certs setup <hostname>` to view the setup instructions again.

### [](#configure-dns-records)[Configure DNS records] 

Now that you've added your domain to your app, configure DNS records with your DNS provider to direct traffic to your Fly App. The setup instructions in the dashboard, or from `fly certs add`, show the recommended DNS configuration for your situation.

Choose the DNS setup that matches your needs:

#### [](#a-and-aaaa-records-recommended)[A and AAAA records (recommended)] 

Use A and AAAA records for most direct connections to your app. These records point your domain directly to your app's IP addresses.

The A and AAAA records you need to set will be shown in your dashboard, and in the output from `fly certs add`. If your app doesn't have an IPv6 address, allocate one with `fly ips allocate-v6`.

**Important:** Hostname validation will fail without an IPv6 addressâ€"and we wonâ€™t attempt to issue or renew a certificateâ€"unless youâ€™re using a [CNAME `_acme-challenge` for domain verification](#dns-challenge). However, we still recommend having both an IPv4 and an IPv6 address allocated if your app is serving traffic.

#### [](#cname-records)[CNAME records] 

CNAME records work well for subdomains (like `www.example.com` or `app.example.com`). A CNAME points your custom domain at a unique `.fly.dev` hostname for your app. CNAME records are also a good option if you have many IP addresses assigned to your app, or expect to change them in the future.

Set the CNAME record with your DNS provider. Each app has a unique CNAME target that will be shown in the dashboard for your certificate, or in the output from `fly certs add`.

Setting CNAME records for the apex domain can be problematic, and should be avoided unless your DNS provider supports CNAME flattening. Some providers use a special name for these records, such as ANAME or ALIAS, and some will flatten a CNAME at the apex automatically. In general, we recommend setting A/AAAA records on the apex domain.

#### [](#proxy-cdn-setup)[Proxy/CDN setup] 

If you're using a proxy or CDN (like Cloudflare) in front of your Fly application, configure only an AAAA record pointing to your app's IPv6 address, as certificate generation requires IPv6 traffic.

#### [](#dns-challenge)[DNS Challenge] 

Use the DNS-01 challenge when:

-   You need a wildcard certificate
-   You want to generate the certificate before directing traffic to your app
-   Automatic validation methods don't work for your setup

This will require setting an `_acme-challenge` CNAME record on your domain. The required record will be shown in your dashboard, or in the output from `fly certs add`.

### [](#certificate-validation)[Certificate validation] 

After you have configured your DNS, Fly.io automatically validates your domain ownership and issues certificates. This happens through one of these methods:

-   **TLS-ALPN challenge**: Validates through a TLS handshake with Fly Proxy. This is the preferred method and works automatically for direct connections.

-   **HTTP-01 challenge**: Validates by requesting a specific file from your domain. Used automatically when TLS-ALPN isn't available, such as with proxy/CDN configurations.

-   **DNS-01 challenge**: You manually add a DNS record to validate domain ownership. Required for wildcard certificates, or to generate certificates before directing traffic to your app.

## [](#other-fly-cert-commands)[Other `fly cert` commands] 

-   `fly certs list` - List the certificates associated with an app.
-   `fly certs check <hostname>` - Trigger a check on the domain validation and DNS configuration for the given hostname and return results in the same format as `fly certs show`.
-   `fly certs setup <hostname>` - Shows setup instructions for configuring DNS records for an existing certificate.
-   `fly certs remove <hostname>` - Remove a certificate from an app for the given hostname.

## [](#teaching-your-app-about-custom-domains)[Teaching your app about custom domains] 

Your application code needs to know how to accept custom domains and adjust the responses accordingly. If you're hosting content on behalf of your users, this typically means mapping the incoming hostname to a particular ID in your application database.

When users make requests, their browser sends a `Host` header you can use to alter the behavior of your application. When you run your app server on Fly.io directly, just get the contents of the `Host` header to identify a request.

If you're running your application on another provider, you will need to create a proxy application, like nginx to route traffic through Fly.io. Your application can then use the `X-Forwarded-Host` header to determine how to handle requests.

## [](#supported-top-level-domains)[Supported top-level domains] 

We support the top-level domains on the [IANA list![](data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIHdpZHRoPSIxNCIgaGVpZ2h0PSIxNCIgY2xhc3M9ImlubGluZS1mbGV4IG1sLTIgc2VsZi1jZW50ZXIgcG9pbnRlci1ldmVudHMtbm9uZSIgdmlld2JveD0iMCAwIDE0IDE0Ij48ZyBidWZmZXJlZC1yZW5kZXJpbmc9InN0YXRpYyIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS4zIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjxwYXRoIGQ9Ik0xMi42MjUgNC44MjVjMC0yLjMxOC0xLjg4Mi00LjItNC4yLTQuMmgtMy42YTQuMjAyIDQuMjAyIDAgMDAtNC4yIDQuMnYzLjZjMCAyLjMxOCAxLjg4MiA0LjIgNC4yIDQuMmgzLjZjMi4zMTggMCA0LjItMS44ODIgNC4yLTQuMnYtMy42ek00LjQ4MiA4LjYyNWw0LTQiPjwvcGF0aD48cGF0aCBkPSJNOC40ODIgNy4yOTdWNC42MjVINS44MSI+PC9wYXRoPjwvZz48L3N2Zz4=)](https://data.iana.org/TLD/tlds-alpha-by-domain.txt). Note that we only periodically update top-level domain support and there might be a delay before we add support for new top-level domains.

## [](#troubleshoot-certificate-creation)[Troubleshoot certificate creation] 

### [](#certificate-creation-or-validation-seems-to-hang-stall-or-fail)[Certificate creation or validation seems to hang, stall, or fail] 

*Let's Encryptâ„¢* is a free, automated, and open certificate authority that Fly.io uses to issue TLS certificates for custom domains. However, Let's Encrypt imposes certain rate limits to ensure fair usage. If you encounter issues when creating or validating a certificate for a custom domain on Fly.io, it's possible that you've hit these rate limits.

The following [rate limits](https://letsencrypt.org/docs/rate-limits/) from Let's Encrypt apply:

-   Certificates per Registered Domain: 50 per week
-   Duplicate Certificate limit: 5 per week
-   Failed Validation limit: 5 failures per hostname, per hour

Note that certificate renewals donâ€™t count against your Certificates per Registered Domain limit.

If you encounter issues when adding or validating a certificate for a custom domain on Fly.io, you can use the following methods to troubleshoot:

-   Use [Let's Debug](https://letsdebug.net/): A diagnostic tool/website to help figure out why you might not be able to issue a certificate for Let's Encrypt. Using a set of tests, it can identify a variety of issues, including: problems with basic DNS setup, problems with nameservers, rate limiting, networking issues, CA policy issues, and common website misconfigurations.
-   Wait and retry: If you've hit a rate limit, you'll need to wait until the rate limit window passes before you can successfully create or validate a certificate again. We donâ€™t have a way to reset it.

The best way to avoid hitting rate limits is to use staging environments and domains for testing and development, and to carefully plan your certificate issuance to stay within the limits. Avoid failed validation by ensuring that your DNS records are correctly configured, with no conflicting records.

If you're building a platform on top of Fly.io, and you expect that your users will frequently delete and then recreate the same resources within a short window, consider implementing "soft delete" logic into your platform that retains the Fly.io resources for a period of time, negating the need to recreate certs frequently.

### [](#i-use-cloudflare-and-there-seems-to-be-a-problem-issuing-or-validating-my-fly-io-tls-certificate)[I use Cloudflare, and there seems to be a problem issuing or validating my Fly.io TLS certificate] 

If you're using Cloudflare's proxying feature (orange cloud), Fly.io can generate a certificate using the HTTP-01 challenge.

For this to work:

1.  **Configure DNS records properly**: Create only an AAAA record pointing to your app's IPv6 address. Do not create an A record or CNAME when using Cloudflare's proxy.
2.  **Set SSL mode**: Use "Full" or "Full (Strict)" SSL mode in Cloudflare. "Flexible" mode can cause redirect loops.

Alternatively, you can use the [DNS-01 challenge method](#dns-challenge) instead of the automatic validation method, though this may conflict with Cloudflare's own certificate issuance.

## [](#related-reading)[Related reading] 

-   [Networking overview](/docs/networking/) Broader look at how Fly.io handles routing, DNS, IPs, and certificates.
-   [Automate the certificate process for custom domains](/docs/networking/custom-domain-api/) Use Fly.io's GraphQL API to automate cert provisioning and domain verification.
-   [TLS termination by Fly Proxy](/docs/security/tls-termination/) â€" How Fly.io handles HTTPS for your apps and manages TLS certificates automatically behind the scenes.
-   [Understanding Cloudflare](/docs/networking/understanding-cloudflare/) What happens when you put Fly.io behind Cloudflare, and how to avoid common pitfalls.

![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSIgc3R5bGU9IndpZHRoOiAxNnB4OyBoZWlnaHQ6IDE2cHg7IHBvaW50ZXItZXZlbnRzOiBub25lOyIgdmlld2JveD0iMCAwIDIwOCAxMjgiIGZpbGw9ImN1cnJlbnRDb2xvciI+CiAgPHJlY3Qgd2lkdGg9IjE5OCIgaGVpZ2h0PSIxMTgiIHg9IjUiIHk9IjUiIHJ5PSIxMCIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMTAiIGZpbGw9Im5vbmUiPjwvcmVjdD4KICA8cGF0aCBkPSJNMzAgOThWMzBoMjBsMjAgMjUgMjAtMjVoMjB2NjhIOTBWNTlMNzAgODQgNTAgNTl2Mzl6bTEyNSAwbC0zMC0zM2gyMFYzMGgyMHYzNWgyMHoiPjwvcGF0aD4KPC9zdmc+) [Copy page as markdown]

[or] [![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE2cHg7IGhlaWdodDogMTZweDsiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8cGF0aCBkPSJNMjIuMjgyIDkuODIxYTUuOTg1IDUuOTg1IDAgMCAwLS41MTYtNC45MSA2LjA0NiA2LjA0NiAwIDAgMC02LjUxLTIuOUE2LjA2NSA2LjA2NSAwIDAgMCA0Ljk4MSA0LjE4YTUuOTg1IDUuOTg1IDAgMCAwLTMuOTk4IDIuOSA2LjA0NiA2LjA0NiAwIDAgMCAuNzQzIDcuMDk3IDUuOTggNS45OCAwIDAgMCAuNTEgNC45MTEgNi4wNTEgNi4wNTEgMCAwIDAgNi41MTUgMi45QTUuOTg1IDUuOTg1IDAgMCAwIDEzLjI2IDI0YTYuMDU2IDYuMDU2IDAgMCAwIDUuNzcyLTQuMjA2IDUuOTkgNS45OSAwIDAgMCAzLjk5Ny0yLjkgNi4wNTYgNi4wNTYgMCAwIDAtLjc0Ny03LjA3M3pNMTMuMjYgMjIuNDNhNC40NzYgNC40NzYgMCAwIDEtMi44NzYtMS4wNGwuMTQxLS4wODEgNC43NzktMi43NThhLjc5NS43OTUgMCAwIDAgLjM5Mi0uNjgxdi02LjczN2wyLjAyIDEuMTY4YS4wNzEuMDcxIDAgMCAxIC4wMzguMDUydjUuNTgzYTQuNTA0IDQuNTA0IDAgMCAxLTQuNDk0IDQuNDk0ek0zLjYgMTguMzA0YTQuNDcgNC40NyAwIDAgMS0uNTM1LTMuMDE0bC4xNDIuMDg1IDQuNzgzIDIuNzU5YS43NzEuNzcxIDAgMCAwIC43OCAwbDUuODQzLTMuMzY5djIuMzMyYS4wOC4wOCAwIDAgMS0uMDMzLjA2Mkw5Ljc0IDE5Ljk1YTQuNSA0LjUgMCAwIDEtNi4xNC0xLjY0NnpNMi4zNCA3Ljg5NmE0LjQ4NSA0LjQ4NSAwIDAgMSAyLjM2Ni0xLjk3M1YxMS42YS43NjYuNzY2IDAgMCAwIC4zODguNjc2bDUuODE1IDMuMzU1LTIuMDIgMS4xNjhhLjA3Ni4wNzYgMCAwIDEtLjA3MSAwbC00LjgzLTIuNzg2QTQuNTA0IDQuNTA0IDAgMCAxIDIuMzQgNy44NzJ6bTE2LjU5NyAzLjg1NWwtNS44MzMtMy4zODdMMTUuMTE5IDcuMmEuMDc2LjA3NiAwIDAgMSAuMDcxIDBsNC44MyAyLjc5MWE0LjQ5NCA0LjQ5NCAwIDAgMS0uNjc2IDguMTA1di01LjY3OGEuNzkuNzkgMCAwIDAtLjQwNy0uNjY3em0yLjAxLTMuMDIzbC0uMTQxLS4wODUtNC43NzQtMi43ODJhLjc3Ni43NzYgMCAwIDAtLjc4NSAwTDkuNDA5IDkuMjNWNi44OTdhLjA2Ni4wNjYgMCAwIDEgLjAyOC0uMDYxbDQuODMtMi43ODdhNC41IDQuNSAwIDAgMSA2LjY4IDQuNjZ6bS0xMi42NCA0LjEzNWwtMi4wMi0xLjE2NGEuMDguMDggMCAwIDEtLjAzOC0uMDU3VjYuMDc1YTQuNSA0LjUgMCAwIDEgNy4zNzUtMy40NTNsLS4xNDIuMDhMOC43MDQgNS40NmEuNzk1Ljc5NSAwIDAgMC0uMzkzLjY4MXptMS4wOTctMi4zNjVsMi42MDItMS41IDIuNjA3IDEuNXYyLjk5OWwtMi41OTcgMS41LTIuNjA3LTEuNXoiPjwvcGF0aD4KPC9zdmc+) Open in ChatGPT ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1sLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE0cHg7IGhlaWdodDogMTRweDsiIHZpZXdib3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSI+CiAgPHJlY3Qgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiByeD0iMyIgZmlsbD0iY3VycmVudENvbG9yIiBvcGFjaXR5PSIwLjEiPjwvcmVjdD4KICA8cGF0aCBkPSJNNiA1aDV2NU0xMSA1bC01IDUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48L3BhdGg+Cjwvc3ZnPg==)](https://chatgpt.com/?hints=search&q=Read+https%3A%2F%2Fraw.githubusercontent.com%2Fsuperfly%2Fdocs%2Fmain%2Fnetworking%2Fcustom-domain.html.markerb)

[![](data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIGNsYXNzPSJtci0xLjUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3R5bGU9InBvaW50ZXItZXZlbnRzOiBub25lOyB3aWR0aDogMjBweDsgaGVpZ2h0OiAyMHB4OyIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8ZyBidWZmZXJlZC1yZW5kZXJpbmc9InN0YXRpYyI+CiAgICA8cGF0aCBkPSJNMTEuOTk5IDEuMjcxQzUuOTI1IDEuMjcxIDEgNi4xOTYgMSAxMi4yNzNjMCA0Ljg1OSAzLjE1MiA4Ljk4MiA3LjUyMyAxMC40MzcuNTUuMS43NTEtLjIzOS43NTEtLjUzbC0uMDE1LTEuODcyYy0zLjA2LjY2Ni0zLjcwNi0xLjQ3NC0zLjcwNi0xLjQ3NC0uNS0xLjI3MS0xLjIyMS0xLjYwOS0xLjIyMS0xLjYwOS0uOTk5LS42ODMuMDc1LS42NjguMDc1LS42NjggMS4xMDUuMDc3IDEuNjg1IDEuMTMzIDEuNjg1IDEuMTMzLjk4MSAxLjY4MSAyLjU3NSAxLjE5NiAzLjIwMi45MTQuMS0uNzExLjM4NC0xLjE5Ni42OTgtMS40NzEtMi40NDItLjI3Ny01LjAxMS0xLjIyMS01LjAxMS01LjQzNiAwLTEuMjAxLjQyOS0yLjE4MyAxLjEzMy0yLjk1Mi0uMTE0LS4yNzgtLjQ5MS0xLjM5Ny4xMDgtMi45MTEgMCAwIC45MjMtLjI5NiAzLjAyNSAxLjEyN0ExMC41NiAxMC41NiAwIDAgMSAxMiA2LjU5MWMuOTM1LjAwNCAxLjg3Ni4xMjcgMi43NTQuMzcgMi4xLTEuNDIzIDMuMDIyLTEuMTI3IDMuMDIyLTEuMTI3LjYgMS41MTQuMjIzIDIuNjMzLjExIDIuOTExLjcwNS43NjkgMS4xMzEgMS43NTEgMS4xMzEgMi45NTIgMCA0LjIyNS0yLjU3MyA1LjE1NS01LjAyMyA1LjQyNy4zOTUuMzQuNzQ3IDEuMDExLjc0NyAyLjAzOCAwIDEuNDcxLS4wMTQgMi42NTctLjAxNCAzLjAxOCAwIC4yOTMuMTk5LjYzNi43NTYuNTI4QzE5Ljg1MSAyMS4yNTEgMjMgMTcuMTMgMjMgMTIuMjczYzAtNi4wNzctNC45MjYtMTEuMDAyLTExLjAwMS0xMS4wMDJ6Ij48L3BhdGg+CiAgPC9nPgo8L3N2Zz4=) Report an issue](https://github.com/superfly/docs/issues/new?body=I+found+an+issue+with+this+document.%0A%0ATitle%3A+Custom+domains%0ALocation%3A+https%3A%2F%2Ffly.io%2Fdocs%2Fnetworking%2Fcustom-domain%2F%0ASource%3A+https%3A%2F%2Fgithub.com%2Fsuperfly%2Fdocs%2Fblob%2Fmain%2Fnetworking%2Fcustom-domain.html.markerb%0A%0A%23%23%23+Describe+the+issue%0A%0A%3C%21--+Describe+the+issue+and+include+the+section+you%27re+referring+to%2C+if+applicable.+Provide+lots+of+detail+about+the+issue+that+you+found.++--%3E%0A%0A%23%23%23+Additional+info%0A%0A%3C%21--+Add+any+other+context+about+the+issue+here.+If+applicable%2C+add+screenshots+to+help+explain+the+issue.+--%3E%0A&title=Issue+with+the+%22Custom+domains%22+doc) or [edit this page on GitHub](https://github.com/superfly/docs/edit/main/networking/custom-domain.html.markerb)