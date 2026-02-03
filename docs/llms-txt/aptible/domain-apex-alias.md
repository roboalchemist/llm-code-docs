# Source: https://www.aptible.com/docs/how-to-guides/app-guides/use-domain-apex-with-endpoints/domain-apex-alias.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Domain Apex ALIAS

Setting up an ALIAS record lets you serve your App from your [domain apex](/how-to-guides/app-guides/use-domain-apex-with-endpoints/overview) directly, but there are significant tradeoffs involved in this approach:

First, this will break some Aptible functionality. Specifically, if you use an ALIAS record, Aptible will no longer be able to serve your [Maintenance Page](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/maintenance-page) from its backup error page server, [Brickwall](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/maintenance-page#brickwall). In fact, what happens exactly will depend on your DNS provider:

* Amazon Route 53: no error page will be served. Customers will most likely be presented with an error page from their browser indicating that the site is not working.

* Cloudflare, DNSimple: a generic Aptible error page will be served.

Second, depending on the provider, the ALIAS record may break in the future if Aptible needs to replace the underlying load balancer for your Endpoint. Specifically, this will be the case if your DNS provider is Amazon Route 53. We'll do our best to notify you if such a replacement needs to happen, but we cannot guarantee that you won't experience disruption during said replacement.

If, given these tradeoffs, you still want to set up an ALIAS record directly to your Aptible Endpoint, please contact [Aptible Support](/how-to-guides/troubleshooting/aptible-support) for instructions.

If not, use this alternate approach: [Redirecting from your domain apex to a subdomain](/how-to-guides/app-guides/use-domain-apex-with-endpoints/domain-apex-redirect).
