# Source: https://docs.readthedocs.com/platform/latest/custom-domains.html

# Custom domains[](#custom-domains "Link to this heading")

By configuring a *custom domain* for your project, your project can serve documentation from a domain you control, for instance [`docs.example.com`]. This is great for maintaining a consistent brand for your product and its documentation.

Default subdomains

*Without a custom domain configured*, your project's documentation is served from a Read the Docs domain using a unique subdomain for your project:

-   [`<project`]` `[`name>.readthedocs.io`] for Read the Docs Community.

-   [`<organization`]` `[`name>-<project`]` `[`name>.readthedocs-hosted.com`] for Read the Docs for Business. The addition of the organization name allows multiple organizations to have projects with the same name.

See also

[[How to manage custom domains]](guides/custom-domains.html)

:   How to create and manage custom domains for your project.

## Features[](#features "Link to this heading")

Automatic SSL

:   SSL certificates are automatically issued through Cloudflare for every custom domain. No extra set up is required beyond configuring your project's custom domain.

CDN caching

:   Response caching is provided through a [[CDN]](reference/cdn.html) for all documentation projects, including projects using a custom domain. CDN caching improves page response time for your documentation's users, and the CDN edge network provides low latency response times regardless of location.

Multiple domains

:   Projects can be configured to be served from multiple domains, which always includes the [[project's default subdomain]](#default-subdomain). Only one domain can be configured as the canonical domain however, and any requests to non-canonical domains and subdomains will redirect to the canonical domain.

Canonical domains

:   The canonical domain configures the primary domain the documentation will serve from, and also sets the domain search engines use for search results when hosting from multiple domains. Projects can only have one canonical domain, which is the [[project's default subdomain]](#default-subdomain) if no other canonical domain is defined.

See also

[[Canonical URLs]](canonical-urls.html)

:   How canonical domains affect your project's canonical URL, and why canonical URLs are important.

[[Subprojects]](subprojects.html)

:   How to share a custom domain between multiple projects.