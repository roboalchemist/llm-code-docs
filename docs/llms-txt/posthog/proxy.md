# Source: https://posthog.com/docs/advanced/proxy.md

# Deploy a reverse proxy - Docs

A reverse proxy helps you capture more complete usage data. Ad blockers maintain lists of known analytics domains and block requests to them. A reverse proxy bypasses this by routing events through your own domain, which ad blockers haven't cataloged. This typically increases event capture by 10-30% depending on your user base.

A reverse proxy sends events to PostHog through your own subdomain (like `e.yourdomain.com`) instead of directly to PostHog's domain.

You don't need a reverse proxy to start using PostHog. We recommend setting one up before going to production for more reliable data capture.

## Set up managed reverse proxy

PostHog's managed reverse proxy routes traffic through our infrastructure. We handle SSL certificates, routing, and maintenance automatically.

This option is free for all PostHog Cloud users. You just need access to your domain's DNS settings.

**Setting up during onboarding?**

If you're onboarding a web-based product like Web Analytics, Surveys, or LLM Analytics, you'll be guided through managed proxy setup as part of the onboarding flow. The steps below are for setting it up manually from the organization settings.

1.  1

    ## Create your proxy

    1.  Go to [organization proxy settings](https://app.posthog.com/settings/organization-proxy)
    2.  Click **new managed proxy**
    3.  Enter a subdomain you control. For example, if your app runs on `myapp.com`, use `yoursubdomain.myapp.com`

    **Before you start**

    Choose a neutral subdomain that doesn't include words like `analytics`, `tracking`, `telemetry`, `posthog`, or `ph`. Ad blockers target these terms. If ad blockers block your domain, the proxy won't achieve its intended effect.

2.  2

    ## Create a DNS record

    Go to your DNS provider and create a new **CNAME record**:

    1.  Set the **Name** to your chosen subdomain (just the subdomain part, like `yoursubdomain`)
    2.  Set the **Target** to the proxy domain PostHog generated in the previous step. You'll see it in your proxy settings, it looks like `4854cf84789d8596ad01.proxy-us.posthog.com`
    3.  Save the record

    **Disable DNS provider proxy features**

    If you're using a DNS provider like Cloudflare that offers proxy options (orange cloud), make sure the proxy is **disabled** (gray cloud) for this CNAME record. Enabling the proxy at your DNS provider may interfere with PostHog's managed reverse proxy functionality and SSL certificate provisioning.

3.  3

    ## Wait for propagation and provisioning

    Your proxy status will change from **waiting** → **issuing** → **live**. This typically takes 2-5 minutes for a new record, but can take up to 30 minutes if DNS propagation is slow. (Propagation can take a few hours if you're making changes to an existing CNAME.)

    PostHog will automatically detect your DNS record and provision an SSL certificate. No further action needed.

    > **Note:** If your proxy stays in **issuing** for more than 30 minutes, see [troubleshooting](/docs/advanced/proxy/proxy-reference.md#troubleshooting).

4.  4

    ## Update your PostHog SDK

    Update your PostHog initialization to use your new subdomain:

    PostHog AI

    ### US

    ```javascript
    posthog.init('<ph_project_token>', {
      api_host: 'https://yoursubdomain.myapp.com',
      ui_host: 'https://us.posthog.com'
    })
    ```

    ### EU

    ```javascript
    posthog.init('<ph_project_token>', {
      api_host: 'https://yoursubdomain.myapp.com',
      ui_host: 'https://eu.posthog.com'
    })
    ```

    Replace `yoursubdomain.myapp.com` with your actual subdomain, and provide your **project token**.

    Always set both `api_host` (your proxy) and `ui_host` (PostHog's actual domain) so features like the toolbar work correctly.

5.  ## Verify your setup

    Checkpoint

    Confirm events are flowing through your proxy:

    1.  Open your browser's developer tools and go to the **Network** tab
    2.  Trigger an event in your app, like a page view
    3.  Look for a request to your proxy subdomain (e.g., `yoursubdomain.myapp.com`)
    4.  Verify the response is `200 OK`
    5.  Check the [PostHog app](https://app.posthog.com) to confirm events appear

    If you see errors or events aren't appearing, see [troubleshooting](/docs/advanced/proxy/proxy-reference.md#troubleshooting).

## Deploy your own proxy

If the managed proxy doesn't work for your use case, you can deploy your own reverse proxy.

**Self-hosted proxies**

If you use a self-hosted proxy, PostHog can't help troubleshoot configuration issues.

Choose your platform and follow the setup guide:

-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/cloudflare_icon_ef34353f85.svg)Cloudflare](/docs/advanced/proxy/cloudflare.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/Cloud_Front_76c0f62ab5.svg)AWS CloudFront](/docs/advanced/proxy/cloudfront.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/caddy_c78a5a013f.svg)Caddy](/docs/advanced/proxy/caddy.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/kubernetes_svgrepo_com_b9716be409.svg)Kubernetes](/docs/advanced/proxy/kubernetes-ingress-controller.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/frameworks/nextjs.svg)Next.js proxy file](/docs/advanced/proxy/nextjs-middleware.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/netlify_original_cdea69c2b5.svg)Netlify](/docs/advanced/proxy/netlify.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/frameworks/nextjs.svg)Next.js rewrites](/docs/advanced/proxy/nextjs.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/nginx_icon_872690f0fe.svg)nginx](/docs/advanced/proxy/nginx.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/nodejs.svg)Node](/docs/advanced/proxy/node.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/frameworks/nuxt.svg)Nuxt](/docs/advanced/proxy/nuxt.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/Cloud_Front_76c0f62ab5.svg)Pomerium](/docs/advanced/proxy/pomerium.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/logo_dark_f8e870867f.svg)Railway](/docs/advanced/proxy/railway.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/remix_letter_glowing_49183adce2.svg)Remix](/docs/advanced/proxy/remix.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/docs/integrate/frameworks/svelte.svg)SvelteKit](/docs/advanced/proxy/sveltekit.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/vercel_icon_svgrepo_com_b7e78b41f9.svg)Vercel](/docs/advanced/proxy/vercel.md)

### Find the right self-hosted option

#### Where are you deploying?

Select your hosting platform or deployment target.

VercelNetlifyAWSCloudflareRailwaySelf-hosted serverOther / Framework-specific

For technical requirements, routing configuration, and best practices when running your own proxy, see the [self-hosted proxy reference](/docs/advanced/proxy/proxy-reference.md).

## FAQ

### Why doesn't PostHog use its own proxy?

We do use our own infrastructure. But ad blockers specifically target well-known analytics domains. When they visit `posthog.com`, they catalog our tracking scripts and add them to block lists.

Your proxy works because ad blockers haven't visited your domain to catalog your setup. They don't know what to block.

### What about DNS uncloaking?

DNS uncloaking (also called CNAME uncloaking) is a technique where a DNS resolver follows the CNAME chain of a subdomain to check whether it ultimately points to a known analytics provider. If it does, the resolver blocks the request before it ever reaches the browser.

This is **only possible at the DNS level** — it requires a custom DNS resolver or network-level tool like NextDNS or Pi-hole. Browser ad blocker extensions (like uBlock Origin) cannot perform DNS lookups. They only see HTTP requests after DNS resolution has already happened, so they rely on static blocklists of known domains and URL patterns.

DNS resolvers with uncloaking support maintain their own lists of known analytics domains. When your subdomain's CNAME chain resolves to one of these domains, the resolver can detect and block it. For the small percentage of users running these DNS configurations, a reverse proxy may not fully bypass blocking.

### Does PostHog provide static IP addresses?

No. Our domains use AWS infrastructure with load balancing, which rotates IPs for performance and reliability.

If your firewall requires IP allowlisting, you have two options:

**Option 1: Use domain-based filtering**

Allow outbound HTTPS traffic on port 443 to `*.posthog.com`, or allow specific domains: `us.i.posthog.com` and `us-assets.i.posthog.com`. Replace `us` with `eu` for EU region.

**Option 2: Deploy a reverse proxy with a static IP**

This is the recommended approach for enterprise environments with strict firewall policies.

1.  Deploy a reverse proxy in your infrastructure
2.  Assign your proxy a static IP address
3.  Allowlist only your proxy's IP in your firewall

This gives you full control over network routing without depending on PostHog's infrastructure.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better