# Source: https://render.com/docs/static-sites.md

# Static Sites — Host your website's frontend (React, Next.js, etc.) over a global CDN.

You can deploy static websites (React, Next.js, etc.) to Render in just a few clicks. Serve your application frontends, blogs, and documentation sets over a global CDN, minimizing load times for your users around the world.

*Static sites are fast and free to deploy.* After you link your site's Git repo, Render automatically updates your site with every push to your specified branch. Each site receives a unique `onrender.com` URL, and you can add your own [custom domains](custom-domains).

> *Deploying a _dynamic_ site, such as a Rails app?*
>
> Create a web service instead of a static site.

Static sites count against your workspace's monthly included amounts of outbound bandwidth and pipeline minutes. You can track your usage in the [Render Dashboard](https://dashboard.render.com/billing#included-usage).

## Get started

In the [Render Dashboard](https://dashboard.render.com/), click *New > Static Site*:

[image: Selecting Static Site from the New menu]

Connect your repo, specify your build details (including which Git branch to deploy), and click *Create Static Site*. You're all set! Render kicks off your site's initial deploy.

For extra help with popular static site generators, we have quickstarts for:

- [Next.js](/deploy-nextjs-app#deploy-as-a-static-site)
- [Vue.js](/deploy-vue-js)
- [Hugo](/deploy-hugo)
- [Docusaurus](/deploy-docusaurus)
- [Svelte](/deploy-svelte)
- [Jekyll](/deploy-jekyll)
- [Gatsby](/deploy-gatsby)
- [Create React App](/deploy-create-react-app)

## Features

### Global CDN

Render serves your site over a blazing-fast, reliable, and secure global CDN. We cache your content on network edges around the world, ensuring the fastest possible load times for your users.

### Pull request previews

With each pull request to your site's deployed branch, Render can automatically generate a preview instance of the site with its own URL. This helps you quickly test out updates before merging.

[Learn more about PR previews.](service-previews)

### Redirects and rewrites

Define [redirect and rewrite rules](redirects-rewrites) for your site's paths directly from the Render Dashboard—no code required.

Additionally, Render automatically redirects HTTP traffic to HTTPS.

### Custom response headers

Add [custom HTTP headers](static-site-headers) to your site's responses for security and performance.

### Immediate cache invalidation

Render insulates your site against failure with [zero-downtime deploys](/deploys#zero-downtime-deploys). We build your site with every push to your deployed branch, and each build is fully atomic. As soon as a build succeeds, we deploy it and _immediately_ invalidate our CDN caches so your users always see the latest working version of your site.

### DDoS protection

Render provides free denial-of-service protection to all static sites and web services. [Learn more.](ddos-protection)

### Brotli compression

Render serves your content with [Brotli compression](https://en.wikipedia.org/wiki/brotli), which is [better than gzip](https://blogs.akamai.com/2016/02/understanding-brotlis-potential.html) and makes your sites faster by reducing page sizes.

### HTTP/2

All Render sites and web services support [HTTP/2](https://http2.github.io/) by default, which means fewer client connections to your site and faster page loads.

### Managed TLS certificates

Render uses Let's Encrypt and Google Trust Services to automatically issue and renew TLS certificates for every site and service. There is no additional setup, and TLS certificates are always included for free.

### Custom domains

> *Hobby workspaces support a maximum of two custom domains across all services.*
>
> Professional workspaces and higher support unlimited custom domains.

Add [custom domains](custom-domains) to your static site for free. Specify the domain on your site's Settings page in the [Render Dashboard](https://dashboard.render.com), then follow the instructions to update DNS with your provider:

- [Cloudflare](configure-cloudflare-dns)
- [Namecheap](configure-namecheap-dns)
- [Other](configure-other-dns)

### Dependency installation

By default, Render automatically attempts to detect and install your static site's dependencies. If you prefer to install dependencies manually, add a `SKIP_INSTALL_DEPS` [environment variable](configure-environment-variables) to your site and set it to `true`. You can then include your own dependency installation as part of your site's build command.

---

##### Appendix: Glossary definitions

###### web service

Deploy this *service type* to host a dynamic application at a public URL.

Ideal for full-stack web apps and API servers.

Related article: https://render.com/docs/web-services.md

###### outbound bandwidth

The amount of network traffic you send to destinations outside of Render (HTTP responses, third-party API calls, and so on).

Your workspace receives a monthly included amount of outbound bandwidth. If you exceed this amount, Render bills you for a supplementary amount.

Related article: https://render.com/docs/outbound-bandwidth.md

###### pipeline minutes

The amount of time Render spends running *build commands* and *pre-deploy commands* for your services.

Your workspace receives a monthly included amount of pipeline minutes. If you exceed this amount, Render bills you for a supplementary amount.

Related article: https://render.com/docs/build-pipeline.md