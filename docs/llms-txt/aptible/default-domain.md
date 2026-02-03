# Source: https://www.aptible.com/docs/core-concepts/apps/connecting-to-apps/app-endpoints/default-domain.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Default Domain

> ❗️ Don't create a CNAME from your domain to an Endpoint using a Default Domain. These Endpoints use an Aptible-provided certificate that's valid for `*.on-aptible.com`, so using your own domain will result in a HTTPS error being shown to your users. If you'd like to use your own domain, set up an Endpoint with a [Custom Domain](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-domain) instead.

When you create an [Endpoint](/core-concepts/apps/connecting-to-apps/app-endpoints/overview) with a Default Domain, Aptible will provide you with a hostname you can directly send traffic to, with the format `app-APP_ID.on-aptible.com`.

# Use Cases

Default Domains are ideal for internal and development apps, but if you need a branded hostname to send customers to, you should use a [Custom Domain](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-domain) instead.

# SSL / TLS Certificate

For Endpoints that require [SSL / TLS Certificates](/core-concepts/apps/connecting-to-apps/app-endpoints/overview#ssl--tls-certificates), Aptible will automatically deploy a valid certificate when you use a Default Endpoint.

# One Default Endpoint per app

At most, one Default Endpoint can be used per app. If you need more than one Endpoint for an app, you'll need to use Endpoints with a [Custom Domain](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-domain).

# Custom Default Domains

If you cannot use the on-aptible.com domain, or have concerns about the fact that external Endpoints using the on-aptible.com domain are discoverable via the App ID, we can replace `*.on-aptible.com` with your own domain. This option is only available for apps hosted on [Dedicated Stacks](/core-concepts/architecture/stacks#dedicated-stacks). Contact [Aptible Support](/how-to-guides/troubleshooting/aptible-support) for more information.
