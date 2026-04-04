# Source: https://northflank.com/docs/v1/application/domains/remove-a-domain.md

# Remove a domain

You can unlink subdomains from ports and re-assign them to other ports without having to update your DNS records or re-verify, as long as the subdomain is already verified on Northflank.

You can also remove domains and subdomains entirely from your account, but you will need to re-verify them if you want to use them with your Northflank services again.

## Unlink a domain from a port

You can unlink a subdomain from a port via a service's ports & DNS page, or from your account's domains page.

### Unlink a subdomain via a service

Navigate to the service that contains the port linked to your subdomain and open the ports & DNS page. Open the custom domains & security rules dropdown on the port your subdomain is linked to, and click remove from port . If you previously disabled the default `code.run` endpoint, it will now be active again.

If you no longer require the port, you can simply remove the port .

### Unlink a subdomain via the domains page

Find the subdomain in the list, or search for it. Select the x in the drop-down menu containing the service to unlink the subdomain from the service and port, or select another service and port to link the subdomain to.

## Remove a domain from your account

To remove a domain or subdomain from your account, simply delete the entry from the [domains page in your account settings](https://app.northflank.com/s/account/domains). Removing an apex domain will also remove any subdomains associated with it.

You will be notified if the domain or subdomain is currently linked to any deployments, review this carefully before confirming.

It is recommended that you also remove any Northflank records from your DNS host to avoid confusion, as you will need to re-verify if you re-add the domain or subdomain.

## Next steps

- [Add a domain: Add your domain name to your Northflank account.](/v1/application/domains/add-a-domain-to-your-account)
- [Domain registrar guides: Follow walkthroughs to add and verify domains on Cloudflare, NS1, OVH, and Namecheap.](/v1/application/domains/domains-on-northflank#custom-domains-and-subdomains)
