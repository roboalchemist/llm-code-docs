# Source: https://northflank.com/docs/v1/application/domains/wildcard-domains-and-certificates.md

# Wildcard domains and certificates

You can configure your domains on Northflank to use wildcard redirect routing, which allows you to add subdomains without the need to add an individual DNS record for each new subdomain, and to use wildcard certificate generation, which allows you to add subdomains without requiring an individual certificate to be generated for each one, or to import and use your own certificate for your subdomains on Northflank.

You can use wildcard redirect routing in combination with wildcard certificate generation to allow the dynamic provisioning of subdomains in [templates](https://northflank.com/docs/v1/application/infrastructure-as-code/infrastructure-as-code) and [preview environments](https://northflank.com/docs/v1/application/release/set-up-a-preview-environment).

> [!note] 
> [Click here](https://app.northflank.com/s/account/domains) to view your account domains page.

## Domain routing

You can enable wildcard domain routing when you [add a domain to Northflank](add-a-domain-to-your-account) to automatically verify subdomains added to Northflank. Wildcard redirect routing must be configured when adding a domain to Northflank, and cannot be changed except by removing and re-adding the domain.

> [!note] 
> Wildcard routing will restrict the use of your domain to a single region, and you will be unable to use the top-level domain (also called the apex or root domain) for services. You may find [path-based routing](use-path-based-routing) more suitable depending on your requirements.

To add a domain with wildcard routing, [begin by adding a domain normally](add-a-domain-to-your-account#add-a-domain) and expand advanced options. Select `wildcard redirect` from the domain routing drop-down menu, and choose the region you want to use the domain in. Click add domain and create the record on your DNS provider. In this case a `CNAME` record with an asterisk subdomain for the name (for example `*.wildcard` for the domain `*.wildcard.example.com`), and the record content from Northflank for the value.

Return to Northflank and verify your domain to begin using it in your selected region. You can now add subdomains for this domain on Northflank without adding new DNS records to your DNS provider.

![Adding a wildcard domain in the Northflank application](https://assets.northflank.com/documentation/v1/application/domains/wildcard-domains-and-certificates/wildcard-domain-and-certificate.png)

## Wildcard certificate generation

You can choose to enable wildcard certificate generation when adding a domain to Northflank which allows you to avoid hitting rate limits for [certificate generation](https://northflank.com/docs/v1/application/domains/domains-on-northflank#certificate-generation), as certificates are not generated for individual subdomains. Certificate generation must be configured when adding a domain to Northflank, and cannot be changed except by removing and re-adding the domain.

Wildcard certificates generate a certificate for the entire subdomain level. For example, enabling wildcard generation for `*.example.com` would provide the same certificate for any subdomains added to `example.com`, such as `a.example.com` and `b.example.com`.

You must configure wildcard certificate generation and domain redirect routing for a domain to dynamically generate subdomains in Northflank [templates](https://northflank.com/docs/v1/application/infrastructure-as-code/infrastructure-as-code) and [preview environments](https://northflank.com/docs/v1/application/release/set-up-a-preview-environment).

> [!note] 
> Chromium-based browsers may return a 404 error if a user tries to access multiple subdomains that share the same certificate, at the same time, on a service.

### DCV

Domain Control Validation (DCV) allows you to use wildcard certificate generation by adding a CNAME record to your DNS provider.

To add a domain with wildcard certificate generation using DCV, [begin by adding a domain normally](add-a-domain-to-your-account#add-a-domain) and expand advanced options. Select `wildcard via DCV` from the certificate generation drop-down menu, and click add domain. Create a CNAME record in your DNS provider with the content provided on Northflank under `wildcard certificate DCV verification`, as well as the record required to confirm you own the domain, and verify the domain on Northflank.

After your DNS record has been verified any new subdomains you create under the domain will use the same wildcard certificate.

### Imported certificate

You can enable the use of wildcard certificates by importing a wildcard certificate from your DNS provider or certificate authority.

To add a domain with an imported certificate, [begin by adding a domain normally](add-a-domain-to-your-account#add-a-domain) and expand advanced options. Select `wildcard via imported certificate` from the certificate generation drop-down menu, and click add domain. Copy the certificate content and private key into Northflank, create the record required to confirm you own the domain on your DNS provider, and verify the domain.

Any new subdomains you create under the domain will use your own imported wildcard certificate, rather than a [Northflank-generated Let's Encrypt certificate](https://northflank.com/docs/v1/application/domains/domains-on-northflank#certificate-generation).

You can update the certificate for a domain by opening the settings  for the domain. Expand the certificate import view, paste the new certificate and private key, and click update to begin using the new certificate.

![Importing a wildcard certificate in the Northflank application](https://assets.northflank.com/documentation/v1/application/domains/wildcard-domains-and-certificates/import-wildcard-certificate.png)

## Redirect all subdomains

You can create a wildcard subdomain, which will accept requests to any subdomain and route them to the assigned port of a service.

To add a wildcard subdomain you must add your domain with [wildcard redirect](#domain-routing) and [wildcard certificate generation](#certificate-generation).

Once the domain has been verified, add a subdomain with `*` as the value and [assign it to a service's port](link-a-domain-to-a-port).

Requests to any subdomain at the level of the wildcard subdomain will now be forwarded to the assigned port.

For example, a wildcard subdomain added as `*.preview.example.com` for the domain `preview.example.com` will accept all requests to any subdomain `<string>.preview.example.com`, and route them to the specified service.

## Next steps

- [Add a domain: Add your domain name to your Northflank account.](/v1/application/domains/add-a-domain-to-your-account)
- [Link a domain to a port: How to link and unlink domains and subdomains with specific ports on your deployments.](/v1/application/domains/link-a-domain-to-a-port)
- [Add public ports: Configure ports to expose your services on the internet.](/v1/application/network/configure-ports#public-ports)
- [Domain registrar guides: Follow walkthroughs to add and verify domains on Cloudflare, NS1, OVH, and Namecheap.](/v1/application/domains/domains-on-northflank#custom-domains-and-subdomains)
