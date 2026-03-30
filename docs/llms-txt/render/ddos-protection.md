# Source: https://render.com/docs/ddos-protection.md

# DDoS Protection

Render provides free distributed denial-of-service protection to every application and website hosted on our platform. We're using Cloudflare’s industry-leading DDoS protection infrastructure behind the scenes, and you don't have to do anything to benefit. When your web service is deployed to Render, it is automatically protected.

<div style="max-width: 500px; margin-left: auto; margin-right: auto;">

[image: Diagram of an example DDoS attack]

</div>

Please see our [announcement blog post](/blog/free-ddos-protection) to learn more about DDoS attacks and why we built this feature.

## Limitations

If you use wildcard custom subdomains and your own Cloudflare account, please see our [Custom Domains documentation](configure-cloudflare-dns#adding-a-wildcard-custom-domain-without-the-base-domain) for a specific configuration that may cause traffic to be incorrectly routed. If you have any questions, you can get in touch with us at support@render.com.