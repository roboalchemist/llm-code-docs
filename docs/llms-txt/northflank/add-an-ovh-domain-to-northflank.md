# Source: https://northflank.com/docs/v1/application/domains/domain-registrar-guides/add-an-ovh-domain-to-northflank.md

# Add an OVH domain to Northflank

If you manage your domain through OVH, you can configure it by following these instructions. You can also read [OVH's documentation](https://docs.ovh.com/gb/en/domains/web_hosting_how_to_edit_my_dns_zone/) for more platform specific information.

It is not possible to link an apex domain through OVH. If you want to link your apex domain you must manage your DNS through another provider's DNS service that supports CNAME flattening or ALIAS/ANAME records.

## Add and verify an OVH domain

1. [Add your domain to Northflank](https://northflank.com/docs/v1/application/domains/add-a-domain-to-your-account)

2. Open OVH in a new browser tab or window and log in to your OVHcloud Control Panel

3. Navigate to Web Cloud - Domains and select the domain you are adding to Northflank

4. Select DNS zone and add an entry

5. Select TXT under extended records, or CNAME to add a subdomain

6. Copy the record name from Northflank into the sub-domain field

7. Set the TTL (time to live) to custom and 60 seconds (you can select a higher or default value, but it might take longer to register changes)

8. Copy the record content from Northflank into the value/target field (when adding a CNAME you must add a period to the end of the target)

9. Click next and confirm to save the record

![Adding a TXT record to verify a domain on OVH](https://assets.northflank.com/documentation/v1/application/domains/domain-registrar-guides/ovh/ovh-domain.png)

1. Return to the domains page on Northflank and select verify on the entry for your domain

2. Your domain should verify shortly. If not, check you have entered the record correctly and try again.

3. You can now [link your domain to a service](https://northflank.com/docs/v1/application/domains/link-a-domain-to-a-port)

![Adding a CNAME record to link a subdomain on OVH](https://assets.northflank.com/documentation/v1/application/domains/domain-registrar-guides/ovh/ovh-subdomain.png)

## Next steps

- [Link a domain to a port: How to link and unlink domains and subdomains with specific ports on your deployments.](/v1/application/domains/link-a-domain-to-a-port)
- [Add public ports: Configure ports to expose your services on the internet.](/v1/application/network/configure-ports#public-ports)
