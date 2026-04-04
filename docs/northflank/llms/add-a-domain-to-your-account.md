# Source: https://northflank.com/docs/v1/application/domains/add-a-domain-to-your-account.md

# Add a domain to your account

To add your own domain and subdomains to your Northflank account you must have access to your DNS provider control panel in order to be able to modify the DNS records.

You can manage your domains and subdomains from the domains page in your Northflank account settings.

Domains and subdomains can both be linked to ports on a deployment after adding the required DNS records.

> [!note] 
> [Click here](https://app.northflank.com/s/account/domains) to view your account domains page.

## Add a domain

You can add the same domain to multiple accounts to be able to add subdomains, however only one account will be able to link the [apex domain](#add-an-apex-domain) to a port.

To add a domain you will need to verify it by adding a DNS record on your DNS hosting service.

Click add domain on the domains page and enter your domain name (fully qualified domain name, for example `yourdomain.com`) to view instructions to verify that you control it.

Log in to the control panel on your DNS provider and find the DNS settings for your domain. Add a new text (TXT) record with the name and token shown on Northflank, and set the time to live (TTL) to the recommended or lowest value.

Return to Northflank to verify the domain, once verified you can begin adding subdomains.

Northflank automatically adds an entry for your apex domain, click verify to [add the necessary record](#add-an-apex-domain) to use it with Northflank services.

![A verified domain in the Northflank application](https://assets.northflank.com/documentation/v1/application/domains/add-a-domain-to-your-account/domain-verified.png)

## Add a subdomain

You can add as many subdomains as you require for each domain but each subdomain on Northflank is unique; multiple accounts cannot add the same subdomain.

You can create as many levels of subdomains as required (for example `one.yourdomain.com` or `three.two.one.yourdomain.com`).

To add a subdomain, select the domain namespace to add it to (`yourdomain.com`) and enter the subdomain to add (`one` or `three.two.one`).

After adding a subdomain you will see the name and token to add to your DNS records as a CNAME record, as well as the recommended time to live (TTL).

Log in to the control panel on your [DNS provider](./domains-on-northflank#dns-providers), find the DNS settings for your domain, and add the record with the information specified on Northflank.

![An unverified subdomain in the Northflank application](https://assets.northflank.com/documentation/v1/application/domains/add-a-domain-to-your-account/subdomain-unverified.png)

## Verification

After adding the record for your domain or subdomain, return to your Northflank account's domains page and select verify on the entry for your domain or subdomain.

If it cannot be verified you may need to wait for the DNS to update, this will depend on the TTL set on the DNS host for the record. If it still fails to verify after the TTL has elapsed, check you have entered the record correctly and try again.

You can close the verification information to come back to it later, and view it again by clicking verify on the entry.

When successfully verified you can link the domain or subdomain to a public port on a deployment.

If your domain is proxied by your DNS provider, for example [Cloudflare proxy](domain-registrar-guides/add-a-cloudflare-domain-to-northflank#add-and-verify-your-cloudflare-domains), you may need to disable this during verification and initial certificate generation when adding new domains.

## Add an apex domain

Northflank automatically adds a subdomain entry for your apex domain, unless the apex domain is already associated with another Northflank account. Click verify to see the record content that you must add to your DNS provider to use it with Northflank services. You cannot link an apex domain name to a service if you have configured it using [wildcard redirect routing](wildcard-domains-and-certificates).

Your DNS provider must support CNAME flattening in order to link an apex domain to your Northflank account. If you current provider does not support these records for apex domains, we recommend migrating to a service that does, such as [Cloudflare](https://developers.cloudflare.com/dns/cname-flattening/set-up-cname-flattening/).

## Next steps

- [Link a domain to a port: How to link and unlink domains and subdomains with specific ports on your deployments.](/v1/application/domains/link-a-domain-to-a-port)
- [Use path-based routing: Route incoming traffic to different services and ports for paths on a subdomain.](/v1/application/domains/use-path-based-routing)
- [Add public ports: Configure ports to expose your services on the internet.](/v1/application/network/configure-ports#public-ports)
- [Use wildcard redirect routing: Configure your domains to use wildcard redirect routing to automatically verify subdomains added to Northflank.](/v1/application/domains/wildcard-domains-and-certificates#domain-routing)
