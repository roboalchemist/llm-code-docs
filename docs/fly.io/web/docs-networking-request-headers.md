# Source: https://fly.io/docs/networking/request-headers/

Title: Request headers

URL Source: https://fly.io/docs/networking/request-headers/

Markdown Content:
Request headers · Fly Docs
===============

[Skip to content](https://fly.io/docs/networking/request-headers/#main-content-start)

[](https://fly.io/)[](https://fly.io/docs/)

[**Need a Logo?** View Our Brand Assets](https://fly.io/docs/about/brand/)

Search

Open main menu[](https://fly.io/)[](https://fly.io/docs/)

[Pricing](https://fly.io/pricing/)[Support](https://fly.io/docs/about/support/)

[Sign In](https://fly.io/app/sign-in/)[Sign Up](https://fly.io/app/sign-up/)

[Getting Started](https://fly.io/docs/getting-started/launch)Toggle Getting Started section
*   [Quickstart: Launch your app](https://fly.io/docs/getting-started/launch/)
*   [Launch HelloFly Demo App](https://fly.io/docs/getting-started/launch-demo)
*   [Deep Dive Demo App](https://fly.io/docs/deep-dive/)
*   [Choose a Language or Framework](https://fly.io/docs/getting-started/get-started-by-framework/)
*   [Fly.io Essentials](https://fly.io/docs/getting-started/essentials/)
*   [Migrate from Heroku](https://fly.io/docs/getting-started/migrate-from-heroku/)
*   [Troubleshoot Deployments](https://fly.io/docs/getting-started/troubleshooting/)

[Guides (Blueprints)](https://fly.io/docs/blueprints/)Toggle Guides (Blueprints) section
*   [Guides Overview](https://fly.io/docs/blueprints/)

[Apps on Fly.io](https://fly.io/docs/apps/overview)Toggle Apps on Fly.io section
*   [Fly Apps Overview](https://fly.io/docs/apps/overview/)
*   [Fly Launch](https://fly.io/docs/launch/)
*   [Secrets](https://fly.io/docs/apps/secrets/)
*   [Production Checklist](https://fly.io/docs/apps/going-to-production/)

[Languages & Frameworks](https://fly.io/docs/languages-and-frameworks/)Toggle Languages & Frameworks section
*   [Elixir](https://fly.io/docs/elixir/)
*   [Rails](https://fly.io/docs/rails/getting-started/)
*   [Laravel](https://fly.io/docs/laravel/)
*   [Django](https://fly.io/docs/django/getting-started/)
*   [JavaScript](https://fly.io/docs/js/)
*   [Rust](https://fly.io/docs/rust/)
*   [Python](https://fly.io/docs/python/)
*   [More...](https://fly.io/docs/languages-and-frameworks/)

[Fly Machines](https://fly.io/docs/machines/overview)Toggle Fly Machines section
*   [Introduction to Fly Machines](https://fly.io/docs/machines/overview/)
*   [Machines API](https://fly.io/docs/machines/api/)
*   [Run a New Machine](https://fly.io/docs/machines/flyctl/fly-machine-run/)
*   [Update a Machine](https://fly.io/docs/machines/flyctl/fly-machine-update/)
*   [Machine Sizing](https://fly.io/docs/machines/guides-examples/machine-sizing/)
*   [Machine Restart Policy](https://fly.io/docs/machines/guides-examples/machine-restart-policy/)
*   [Machine States](https://fly.io/docs/machines/machine-states/)
*   [Run User Code on Fly Machines](https://fly.io/docs/machines/guides-examples/functions-with-machines/)
*   [One App Per Customer - Why?](https://fly.io/docs/machines/guides-examples/one-app-per-user-why/)
*   [The Machine Runtime Environment](https://fly.io/docs/machines/runtime-environment/)

[Managed Postgres](https://fly.io/docs/mpg)Toggle Managed Postgres section
*   [Create and Connect to a Managed Postgres Cluster](https://fly.io/docs/mpg/create-and-connect/)
*   [Cluster Configuration Options](https://fly.io/docs/mpg/configuration/)
*   [Phoenix with Managed Postgres](https://fly.io/docs/mpg/guides-examples/phoenix-guide/)
*   [Monitoring and Metrics](https://fly.io/docs/mpg/metrics/)
*   [Import data from another postgres cluster](https://fly.io/docs/mpg/import/)
*   [Supported Postgres Extensions](https://fly.io/docs/mpg/extensions/)

[Fly GPUs](https://fly.io/docs/gpus/gpu-quickstart)Toggle Fly GPUs section
*   [GPU Quickstart](https://fly.io/docs/gpus/gpu-quickstart/)
*   [Getting Started with GPU Machines](https://fly.io/docs/gpus/getting-started-gpus/)
*   [Python GPU Dev Machine](https://fly.io/docs/gpus/python-gpu-example/)

[Databases & Storage](https://fly.io/docs/database-storage-guides/)Toggle Databases & Storage section
*   [Fly Managed Postgres](https://fly.io/docs/mpg/)
*   [Tigris Object Storage](https://fly.io/docs/tigris/)
*   [Upstash for Redis®](https://fly.io/docs/upstash/redis/)

[Fly Volumes](https://fly.io/docs/volumes/overview)Toggle Fly Volumes section
*   [Fly Volumes Overview](https://fly.io/docs/volumes/overview/)
*   [Create and Manage Volumes](https://fly.io/docs/volumes/volume-manage/)
*   [Manage Volume Snapshots](https://fly.io/docs/volumes/snapshots/)
*   [Volume States](https://fly.io/docs/volumes/volume-states/)

[Fly Kubernetes](https://fly.io/docs/kubernetes/fks-quickstart)Toggle Fly Kubernetes section
*   [Fly Kubernetes Quickstart](https://fly.io/docs/kubernetes/fks-quickstart/)
*   [Fly Kubernetes Features](https://fly.io/docs/kubernetes/fks-features/)
*   [Create an FKS Cluster](https://fly.io/docs/kubernetes/clusters/)
*   [Connect to an FKS Cluster](https://fly.io/docs/kubernetes/connect-clusters/)
*   [Configure FKS Services](https://fly.io/docs/kubernetes/services/)
*   [Use GPUs with FKS](https://fly.io/docs/kubernetes/using-gpus/)
*   [Use Volumes with FKS](https://fly.io/docs/kubernetes/using-volumes/)

[Networking](https://fly.io/docs/networking/)Toggle Networking section
*   [Connect to an App Service](https://fly.io/docs/networking/app-services/)
*   [Public Networking](https://fly.io/docs/networking/services/)
*   [Private Networking](https://fly.io/docs/networking/private-networking/)
*   [Custom Private Networks](https://fly.io/docs/networking/custom-private-networks/)
*   [Flycast - Private Proxy Services](https://fly.io/docs/networking/flycast/)
*   [Egress IP Addresses](https://fly.io/docs/networking/egress-ips/)
*   [Dynamic Request Routing](https://fly.io/docs/networking/dynamic-request-routing/)
*   [Custom Domains](https://fly.io/docs/networking/custom-domain/)
*   [Understanding Cloudflare](https://fly.io/docs/networking/understanding-cloudflare/)
*   [Request Headers](https://fly.io/docs/networking/request-headers/)
*   [Run UDP Services](https://fly.io/docs/networking/udp-and-tcp/)
*   [TLS Support](https://fly.io/docs/networking/tls/)

[Monitoring](https://fly.io/docs/monitoring/)Toggle Monitoring section
*   [Metrics](https://fly.io/docs/monitoring/metrics/)
*   [Sentry Error Tracking](https://fly.io/docs/monitoring/sentry/)
*   [Logging](https://fly.io/docs/monitoring/logging-overview/)Toggle Logging section
    *   [Live Tail Logs](https://fly.io/docs/monitoring/live-tail-logs/)
    *   [Logs API Options](https://fly.io/docs/monitoring/logs-api-options/)
    *   [Search Logs](https://fly.io/docs/monitoring/search-logs/)
    *   [Export Logs](https://fly.io/docs/monitoring/exporting-logs/)
    *   [Error Codes](https://fly.io/docs/monitoring/error-codes/)

[Security](https://fly.io/docs/security/)Toggle Security section
*   [Organization Roles and Permissions](https://fly.io/docs/security/org-roles-permissions/)
*   [SSO for Organizations](https://fly.io/docs/security/sso/)
*   [Remove a Member from an Org](https://fly.io/docs/security/remove-org-member/)
*   [TLS Termination](https://fly.io/docs/security/tls-termination/)
*   [App Security by Arcjet](https://fly.io/docs/security/arcjet/)
*   [Access Tokens](https://fly.io/docs/security/tokens/)
*   [OpenID Connect](https://fly.io/docs/reference/openid-connect/)
*   [Shared Responsibility Model](https://fly.io/docs/security/shared-responsibility/)
*   [Security Practices and Compliance](https://fly.io/docs/security/security-at-fly-io/)

[Reference](https://fly.io/docs/reference/)Toggle Reference section
*   [flyctl](https://fly.io/docs/flyctl/)
*   [App Config Reference (fly.toml)](https://fly.io/docs/reference/configuration/)
*   [Architecture](https://fly.io/docs/reference/architecture/)
*   [Autoscaling](https://fly.io/docs/reference/autoscaling/)
*   [AWS to Fly Overview](https://fly.io/docs/reference/aws-to-fly-guide/)
*   [Builders](https://fly.io/docs/reference/builders/)
*   [Content Encoding](https://fly.io/docs/reference/content-encoding/)
*   [Fly Launch](https://fly.io/docs/reference/fly-launch/)
*   [Health Checks](https://fly.io/docs/reference/health-checks/)
*   [Load Balancing](https://fly.io/docs/reference/load-balancing/)
*   [Machine Migration](https://fly.io/docs/reference/machine-migration/)
*   [Multiple Processes in Apps](https://fly.io/docs/app-guides/multiple-processes/)
*   [Fly Proxy](https://fly.io/docs/reference/fly-proxy/)
*   [Fly Proxy Autostop/Autostart](https://fly.io/docs/reference/fly-proxy-autostop-autostart/)
*   [Regions](https://fly.io/docs/reference/regions/)
*   [Suspend/Resume](https://fly.io/docs/reference/suspend-resume/)

[About](https://fly.io/docs/about/)Toggle About section
*   [Pricing](https://fly.io/docs/about/pricing/)
*   [Billing](https://fly.io/docs/about/billing/)
*   [Cost Management](https://fly.io/docs/about/cost-management/)
*   [Free Trial](https://fly.io/docs/about/free-trial/)
*   [Support](https://fly.io/docs/about/support/)
*   [Engineering Jobs](https://fly.io/docs/hiring/)
*   [Healthcare on Fly.io](https://fly.io/docs/about/healthcare/)
*   [Extensions Program](https://fly.io/docs/about/extensions/)
*   [Extensions API](https://fly.io/docs/reference/extensions_api/)
*   [Merch](https://fly.io/docs/about/merch/)
*   [Open Source](https://fly.io/docs/about/open-source/)
*   [Using Our Brand](https://fly.io/docs/about/brand/)
*   [Privacy Policy](https://fly.io/legal/privacy-policy/)
*   [Terms of Service](https://fly.io/legal/terms-of-service/)

--- title: Request headers layout: docs nav: firecracker --- <figure><img src="/static/images/request-headers.png" alt="Illustration by Annie Ruygt of flying ghosts carrying lanterns" class="w-full max-w-lg mx-auto"></figure> Request headers carry information that is specific to the incoming request and its path taken to the application. Request headers are added by the HTTP handler service. ## Request Headers ### `Fly-Client-IP` **Client IP Address**: The IP address of the client from the perspective of Fly Proxy. If you are using another reverse proxy service in front of the Fly.io platform, this header will be set to proxy service's IP addresses, rather than the client making the request. In that case, you'll need to parse the IP addresses in the [`X-Forwarded-For` header](#x-forwarded-for) to find the client IP address. ### `Fly-Forwarded-Port` **Original connection port**: This header is always set by the Fly Proxy and denotes the actual port that the client connected to the Fly edge node which is then forwarded to the application instance. ### `Fly-Region` **Edge Node Region**: This header is a three letter region code which represents the region that the connection was accepted in and routed from. Not to be confused with the [environment variable](/docs/machines/runtime-environment/#fly_region) `FLY_REGION`, which is where the application is running. ### `X-Forwarded-For` **Client and Proxy List**: A comma separated list of IP addresses including the address of the client that originated the request and the addresses of the proxy servers the request passed through. For example, "77.97.0.98, 77.83.142.33" contains the client and the one proxy it passed through. On the Fly.io platform, the last address (rightmost) in this list will be a shared or dedicated IP address assigned to your app. This header must be treated with caution to avoid spoofing attempts. Follow the directives in the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For+external) for `X-Forwarded-For` to learn how parse the header safely. If you aren't using another reverse proxy in front of the Fly.io platform, the [`Fly-Client-IP` header](#fly-client-ip) might be a better choice to get client IP addresses. ### `X-Forwarded-Proto` **Original client protocol**: The protocol which the client used to make the request. Either `http` or `https`. ### `X-Forwarded-Port` **Original connection port**: This header may be set by the client and should denote the port that the client set out to connect to. ### `X-Forwarded-SSL` **SSL Status**: This indicates if the client connected over SSL. Its value can be either `on` or `off`. ## Request and Response Headers ### `Via` **Proxy Route**: This header, added by proxies, shows the path taken, and protocols used, by the connection. MDN has [full documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Via) for this header. For example, a connection through the Fly edge may show `2 fly.io` in the field, denoting that version 2 of HTTP was used by the connection as it passed through the Fly Proxy. 

[Docs](https://fly.io/docs/)[Networking](https://fly.io/docs/networking)Request headers
Request headers
===============

![Image 2: Illustration by Annie Ruygt of flying ghosts carrying lanterns](https://fly.io/static/images/request-headers.png)
Request headers carry information that is specific to the incoming request and its path taken to the application. Request headers are added by the HTTP handler service.

[](https://fly.io/docs/networking/request-headers/#request-headers)Request Headers
----------------------------------------------------------------------------------

### [](https://fly.io/docs/networking/request-headers/#fly-client-ip)`Fly-Client-IP`

**Client IP Address**: The IP address of the client from the perspective of Fly Proxy. If you are using another reverse proxy service in front of the Fly.io platform, this header will be set to proxy service’s IP addresses, rather than the client making the request. In that case, you’ll need to parse the IP addresses in the [`X-Forwarded-For` header](https://fly.io/docs/networking/request-headers/#x-forwarded-for) to find the client IP address.

### [](https://fly.io/docs/networking/request-headers/#fly-forwarded-port)`Fly-Forwarded-Port`

**Original connection port**: This header is always set by the Fly Proxy and denotes the actual port that the client connected to the Fly edge node which is then forwarded to the application instance.

### [](https://fly.io/docs/networking/request-headers/#fly-region)`Fly-Region`

**Edge Node Region**: This header is a three letter region code which represents the region that the connection was accepted in and routed from.

Not to be confused with the [environment variable](https://fly.io/docs/machines/runtime-environment/#fly_region)`FLY_REGION`, which is where the application is running.

### [](https://fly.io/docs/networking/request-headers/#x-forwarded-for)`X-Forwarded-For`

**Client and Proxy List**: A comma separated list of IP addresses including the address of the client that originated the request and the addresses of the proxy servers the request passed through. For example, “77.97.0.98, 77.83.142.33” contains the client and the one proxy it passed through. On the Fly.io platform, the last address (rightmost) in this list will be a shared or dedicated IP address assigned to your app.

This header must be treated with caution to avoid spoofing attempts. Follow the directives in the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For) for `X-Forwarded-For` to learn how parse the header safely. If you aren’t using another reverse proxy in front of the Fly.io platform, the [`Fly-Client-IP` header](https://fly.io/docs/networking/request-headers/#fly-client-ip) might be a better choice to get client IP addresses.

### [](https://fly.io/docs/networking/request-headers/#x-forwarded-proto)`X-Forwarded-Proto`

**Original client protocol**: The protocol which the client used to make the request. Either `http` or `https`.

### [](https://fly.io/docs/networking/request-headers/#x-forwarded-port)`X-Forwarded-Port`

**Original connection port**: This header may be set by the client and should denote the port that the client set out to connect to.

### [](https://fly.io/docs/networking/request-headers/#x-forwarded-ssl)`X-Forwarded-SSL`

**SSL Status**: This indicates if the client connected over SSL. Its value can be either `on` or `off`.

[](https://fly.io/docs/networking/request-headers/#request-and-response-headers)Request and Response Headers
------------------------------------------------------------------------------------------------------------

### [](https://fly.io/docs/networking/request-headers/#via)`Via`

**Proxy Route**: This header, added by proxies, shows the path taken, and protocols used, by the connection. MDN has [full documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Via) for this header. For example, a connection through the Fly edge may show `2 fly.io` in the field, denoting that version 2 of HTTP was used by the connection as it passed through the Fly Proxy.

Copy page as markdown or[Open in ChatGPT](https://chatgpt.com/?hints=search&q=Read+https%3A%2F%2Fraw.githubusercontent.com%2Fsuperfly%2Fdocs%2Fmain%2Fnetworking%2Frequest-headers.html.md)

[Report an issue](https://github.com/superfly/docs/issues/new?body=I+found+an+issue+with+this+document.%0A%0ATitle%3A+Request+headers%0ALocation%3A+https%3A%2F%2Ffly.io%2Fdocs%2Fnetworking%2Frequest-headers%2F%0ASource%3A+https%3A%2F%2Fgithub.com%2Fsuperfly%2Fdocs%2Fblob%2Fmain%2Fnetworking%2Frequest-headers.html.md%0A%0A%23%23%23+Describe+the+issue%0A%0A%3C%21--+Describe+the+issue+and+include+the+section+you%27re+referring+to%2C+if+applicable.+Provide+lots+of+detail+about+the+issue+that+you+found.++--%3E%0A%0A%23%23%23+Additional+info%0A%0A%3C%21--+Add+any+other+context+about+the+issue+here.+If+applicable%2C+add+screenshots+to+help+explain+the+issue.+--%3E%0A&title=Issue+with+the+%22Request+headers%22+doc) or [edit this page on GitHub](https://github.com/superfly/docs/edit/main/networking/request-headers.html.md)

[On this page](https://fly.io/docs/networking/request-headers/#)
*   [Request Headers](https://fly.io/docs/networking/request-headers/#request-headers)
    *   [Fly-Client-IP](https://fly.io/docs/networking/request-headers/#fly-client-ip)
    *   [Fly-Forwarded-Port](https://fly.io/docs/networking/request-headers/#fly-forwarded-port)
    *   [Fly-Region](https://fly.io/docs/networking/request-headers/#fly-region)
    *   [X-Forwarded-For](https://fly.io/docs/networking/request-headers/#x-forwarded-for)
    *   [X-Forwarded-Proto](https://fly.io/docs/networking/request-headers/#x-forwarded-proto)
    *   [X-Forwarded-Port](https://fly.io/docs/networking/request-headers/#x-forwarded-port)
    *   [X-Forwarded-SSL](https://fly.io/docs/networking/request-headers/#x-forwarded-ssl)

*   [Request and Response Headers](https://fly.io/docs/networking/request-headers/#request-and-response-headers)
    *   [Via](https://fly.io/docs/networking/request-headers/#via)

Copy page as markdown[Open in ChatGPT](https://chatgpt.com/?hints=search&q=Read+https%3A%2F%2Fraw.githubusercontent.com%2Fsuperfly%2Fdocs%2Fmain%2Fnetworking%2Frequest-headers.html.md)
