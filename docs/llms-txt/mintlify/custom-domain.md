# Source: https://www.mintlify.com/docs/customize/custom-domain.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom domain

> Host your documentation on a custom domain.

To host your documentation on a custom domain:

1. Add your domain in your dashboard.
2. Configure DNS settings on your domain provider.
3. Allow time for DNS to propagate and TLS certificates to be automatically provisioned.

<Info>
  Looking to set up a subpath like `example.com/docs`? See [/docs subpath](/deploy/docs-subpath).
</Info>

## Add your custom domain

1. Navigate to the [Custom domain setup](https://dashboard.mintlify.com/settings/deployment/custom-domain) page in your dashboard.
2. Enter your domain name. For example, `docs.example.com` or `www.example.com`.
3. Click **Add domain**.

<Frame>
  <img alt="The Custom domain setup page showing the field to enter your custom domain URL." className="block dark:hidden" src="https://mintcdn.com/mintlify/Br3zUjMmXXI3_HaI/images/domain/add-custom-domain-light.png?fit=max&auto=format&n=Br3zUjMmXXI3_HaI&q=85&s=d8c8e3f4b035a6714614e52b173bf3f6" data-og-width="2236" width="2236" data-og-height="608" height="608" data-path="images/domain/add-custom-domain-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Br3zUjMmXXI3_HaI/images/domain/add-custom-domain-light.png?w=280&fit=max&auto=format&n=Br3zUjMmXXI3_HaI&q=85&s=8a358764b781030282efd06c666e8b66 280w, https://mintcdn.com/mintlify/Br3zUjMmXXI3_HaI/images/domain/add-custom-domain-light.png?w=560&fit=max&auto=format&n=Br3zUjMmXXI3_HaI&q=85&s=b57f050bf5ba4232b6433261b08e8314 560w, https://mintcdn.com/mintlify/Br3zUjMmXXI3_HaI/images/domain/add-custom-domain-light.png?w=840&fit=max&auto=format&n=Br3zUjMmXXI3_HaI&q=85&s=af9f18817720073ead81503eae8dc413 840w, https://mintcdn.com/mintlify/Br3zUjMmXXI3_HaI/images/domain/add-custom-domain-light.png?w=1100&fit=max&auto=format&n=Br3zUjMmXXI3_HaI&q=85&s=d60da8f2866c7169a5033af11ddc62e7 1100w, https://mintcdn.com/mintlify/Br3zUjMmXXI3_HaI/images/domain/add-custom-domain-light.png?w=1650&fit=max&auto=format&n=Br3zUjMmXXI3_HaI&q=85&s=24ddd10a48e57680f5a70c499f477272 1650w, https://mintcdn.com/mintlify/Br3zUjMmXXI3_HaI/images/domain/add-custom-domain-light.png?w=2500&fit=max&auto=format&n=Br3zUjMmXXI3_HaI&q=85&s=dbe6d16e2a3e01d4d725059e466121ae 2500w" />

  <img alt="The Custom domain setup page showing the field to enter your custom domain URL." className="hidden dark:block" src="https://mintcdn.com/mintlify/Br3zUjMmXXI3_HaI/images/domain/add-custom-domain-dark.png?fit=max&auto=format&n=Br3zUjMmXXI3_HaI&q=85&s=d6b5b7f57c57ff72142613135e77cc98" data-og-width="2236" width="2236" data-og-height="608" height="608" data-path="images/domain/add-custom-domain-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Br3zUjMmXXI3_HaI/images/domain/add-custom-domain-dark.png?w=280&fit=max&auto=format&n=Br3zUjMmXXI3_HaI&q=85&s=b287d9b27e043c331e70755deb24c7ee 280w, https://mintcdn.com/mintlify/Br3zUjMmXXI3_HaI/images/domain/add-custom-domain-dark.png?w=560&fit=max&auto=format&n=Br3zUjMmXXI3_HaI&q=85&s=1776d0139e6f5b2dc1e4b9e7c5b6e1db 560w, https://mintcdn.com/mintlify/Br3zUjMmXXI3_HaI/images/domain/add-custom-domain-dark.png?w=840&fit=max&auto=format&n=Br3zUjMmXXI3_HaI&q=85&s=68c9e83b5e98d5e7b652513c42d04142 840w, https://mintcdn.com/mintlify/Br3zUjMmXXI3_HaI/images/domain/add-custom-domain-dark.png?w=1100&fit=max&auto=format&n=Br3zUjMmXXI3_HaI&q=85&s=b8c48cb9b4bd586f794663b3a9936735 1100w, https://mintcdn.com/mintlify/Br3zUjMmXXI3_HaI/images/domain/add-custom-domain-dark.png?w=1650&fit=max&auto=format&n=Br3zUjMmXXI3_HaI&q=85&s=11c3173d0becd05b6fceb19faa52940d 1650w, https://mintcdn.com/mintlify/Br3zUjMmXXI3_HaI/images/domain/add-custom-domain-dark.png?w=2500&fit=max&auto=format&n=Br3zUjMmXXI3_HaI&q=85&s=6e41be617f081100da740499dd7083b9 2500w" />
</Frame>

## Configure your DNS

1. On your domain provider's website, navigate to your domain's DNS settings.
2. Create a new DNS record with the following values:

```text  theme={null}
CNAME | docs | cname.mintlify-dns.com.
```

<Tip>
  Each domain provider has different ways to add DNS records. Refer to your domain provider's documentation for specific instructions.
</Tip>

### DNS propagation

DNS changes typically take 1-24 hours to propagate globally, though it can take up to 48 hours in some cases. You can verify your DNS is configured correctly using [DNSChecker](https://dnschecker.org).

Once your DNS records are active, your documentation is first accessible via HTTP. HTTPS is available after Vercel provisions your TLS certificate.

### Automatic TLS provisioning

Once your DNS records propagate and resolve correctly, Vercel automatically provisions a free SSL/TLS certificate for your domain using Let's Encrypt.

This typically completes within a few hours of DNS propagation, though it can take up to 24 hours in rare cases. Certificates are automatically renewed before expiration.

### CAA records

If your domain uses CAA (Certification Authority Authorization) records, you must authorize Let's Encrypt to issue certificates for your domain. Add the following CAA record to your DNS settings:

```text  theme={null}
0 issue "letsencrypt.org"
```

### Reserved paths

The `/.well-known/acme-challenge` path is reserved for certificate validation and cannot be redirected or rewritten. If you have configured redirects or rewrites for this path, certificate provisioning will fail.

### Provider-specific settings

<AccordionGroup>
  <Accordion title="Vercel verification">
    If Vercel is your domain provider, you must add a verification `TXT` record. This information appears on your dashboard after submitting your custom domain, and is emailed to you.
  </Accordion>

  <Accordion title="Cloudflare encryption mode">
    If Cloudflare is your DNS provider, you must enable the "Full (strict)" mode for the SSL/TLS encryption setting. Additionally, disable "Always Use HTTPS" in your Edge Certificates settings. Cloudflare's HTTPS redirect will block Let's Encrypt from validating your domain during certificate provisioning.
  </Accordion>
</AccordionGroup>

## Set a canonical URL

After configuring your DNS, set a canonical URL to ensure search engines index your preferred domain. A canonical URL tells search engines which version of your documentation is the primary one. This improves SEO when your documentation is accessible from multiple URLs and prevents issues with duplicate content.

Add the `canonical` meta tag to your `docs.json`:

```json  theme={null}
"seo": {
    "metatags": {
        "canonical": "https://www.your-custom-domain-here.com"
    }
}
```

Replace `https://www.your-custom-domain-here.com` with your actual custom domain. For example, if your custom domain is `docs.mintlify.com`, you would use:

```json  theme={null}
"seo": {
    "metatags": {
        "canonical": "https://docs.mintlify.com"
    }
}
```
