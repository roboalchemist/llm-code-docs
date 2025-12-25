# Source: https://docs.readthedocs.com/platform/latest/security-implications.html

# Security considerations for documentation pages[](#security-considerations-for-documentation-pages "Link to this heading")

This article explains the security implications of documentation pages, this doesn't apply to the main dashboard (readthedocs.org/readthedocs.com), only to documentation pages (readthedocs.io, readthedocs-hosted.com, and custom domains).

See also

[[Cross-site requests]](api/cross-site-requests.html)

:   Learn about cross-origin requests in our public APIs.

## Cross-origin requests[](#cross-origin-requests "Link to this heading")

Read the Docs allows [cross-origin requests](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) for documentation resources it serves. However, internal and proxied APIs, typically found under the [`/_/`] path don't allow cross-origin requests.

To facilitate this, the following headers are added to all responses from documentation pages:

-   [`Access-Control-Allow-Origin:`]` `[`*`]

-   [`Access-Control-Allow-Methods:`]` `[`GET,`]` `[`HEAD,`]` `[`OPTIONS`]

These headers allow cross-origin requests from any origin and only allow the GET, HEAD and OPTIONS methods. It's important to note that passing credentials (such as cookies or HTTP authentication) in cross-origin requests is not allowed, ensuring access to public resources only.

Having cross-origin requests enabled allows third-party websites to make use of files from your documentation (as long as they are public), which allows various third-party integrations to work.

If needed, the [`Access-Control`] headers can be changed for your documentation pages by [[contacting support]](support.html). **You are responsible for providing the correct values for these headers, and making sure they don't break your documentation pages.**