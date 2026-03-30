# Source: https://render.com/docs/configure-cloudflare-dns.md

# Configuring Cloudflare DNS


> This guide assumes you've already added a custom domain from Cloudflare to your service in the [Render Dashboard](https://dashboard.render.com). If you haven't done this yet, first read [Custom Domains](custom-domains).

## Common setup

Most commonly when setting up a Cloudflare custom domain, you add a CNAME record for the root domain, along with another for the `www` subdomain.

> *Remove all `AAAA` records for your domain if it has any.* `AAAA` records map a domain to a corresponding IPv6 record, but Render does not yet support IPv6 addresses. As a result, `AAAA` records can interfere with your custom domain's behavior on Render.

1. Log in to your Cloudflare dashboard and select your domain from the Home page to open its settings.

2. Navigate to *SSL/TLS > Overview*. Set your encryption mode to *Full*:

   [image: Cloudflare SSL/TLS settings]

3. Navigate to *DNS > Records* and click *Add record*.

4. Create a new CNAME record that points to your Render service's `onrender.com` subdomain (obtain this value in the [Render Dashboard](https://dashboard.render.com)):

   [image: Cloudflare Root CNAME Addition]

   - Set *Name* to `@` to specify your root domain (next you'll add a separate record for `www`).
   - Set *Target* to your Render service's subdomain (e.g., `example.onrender.com`).
   - Set *Proxy status* to *DNS only*. This ensures that requests go to Render instead of Cloudflare, so that we can verify the domain and issue a certificate.

   Click *Save*.

5. Repeat the previous step to create a _second_ CNAME record.

   - This time, set *Name* to `www` and provide the same values as before for *Target* and *Proxy status*.

   Click *Save*.

6. Your completed configuration should resemble this:

   [image: Cloudflare DNS records with two CNAME records]

That's it! DNS changes might take a few minutes to propagate, after which your domain points to your Render service. You can check the status of your service's certificates and manually request verification in the [Render Dashboard](https://dashboard.render.com) under *Custom Domains*:

[image: Verified certificates in the Render Dashboard]

After the Render Dashboard indicates that your certificates are issued and valid, you can optionally set *Proxy status* to *Proxied* for your CNAME records.

## Adding a wildcard custom domain without the base domain

Your Cloudflare domain requires some additional configuration if _all_ of the following are true:

- You're adding a wildcard custom domain (e.g., `*.example.com`) to your Render service.
- You are _not_ adding the corresponding _base_ domain (e.g., `example.com`) to your service.
- You've [enabled proxying](https://community.cloudflare.com/t/what-is-the-proxied-feature-in-cloudflare/32887) for your base domain (i.e., *Proxy status* is set to *Proxied*).

### Origin override with a Cloudflare Worker

To direct wildcard traffic to Render while directing base domain traffic elsewhere, you can use a Cloudflare Worker to perform an [origin override](https://developers.cloudflare.com/workers/examples/bulk-origin-proxy).

*The instructions below assume the following:*

- You have the custom Cloudflare domain `example.com`.
- You want your Render web service `example.onrender.com` to serve traffic for `*.example.com`
- You want `base-domain-origin.com` to serve traffic for `example.com`.

#### 1. Add a DNS record pointing to base-domain-origin.com

[image: Cloudflare Base Domain DNS Record]

#### 2. Create a Worker

1. Navigate to *Workers* -> *Overview* -> *Create Service*
2. Name your service `base-domain-override`, select *HTTP Handler*, and click *Create service*

   [image: Cloudflare Create a Service]

3. Scroll down and click *Quick Edit*.
4. Add the following configuration. Replace `example.com` with your custom domain and make sure the `base-domain-origin` subdomain matches the DNS record you created in the first step.

   ```javascript
   addEventListener('fetch', (event) => {
     event.respondWith(handleRequest(event.request))
   })

   async function handleRequest(request) {
     return fetch(request, {
       cf: { resolveOverride: 'base-domain-origin.example.com' },
     })
   }
   ```

   [image: Cloudflare Worker Configuration]

5. Click *Save and Deploy* -> Navigate back to the Worker overview page -> Click *Triggers* -> *Add Route*
6. Add a route matching your base domain and click *Add Route*:

   [image: Cloudflare Triggers]

7. Finally, add CNAME records for both your base domain and wildcard domain pointing to your onrender subdomain. Pointing your base domain to Render is required for an [orange to orange setup](https://community.cloudflare.com/t/the-orange-to-orange-problem/91864). With this configuration, Cloudflare will send traffic to your zone first. The Worker that you just set up will match the route and trigger an origin override, so traffic for the base domain will not get sent to Render. If you do not do this, Cloudflare will send the traffic directly to Render's zone and the Worker you set up wil have no effect.

[image: Cloudflare DNS Records]

Your wildcard traffic should now be directed to Render and your base domain traffic directed to the origin you specified. If you have any questions, you can get in touch with us at support@render.com.