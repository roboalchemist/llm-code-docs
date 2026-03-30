# Source: https://northflank.com/docs/v1/application/domains/domain-registrar-guides/add-an-ns1-domain-to-northflank.md

# Add an NS1 domain to Northflank

If you manage your domain through NS1, you can configure it by following these instructions, or read [IBM NS1 Connect's documentation](https://www.ibm.com/docs/en/ns1-connect?topic=dns-resource-management) for more platform specific information.

## Add and verify an NS1 domain

To add and verify NS1 domains and subdomains on Northflank:

1. [Add your domain to Northflank](https://northflank.com/docs/v1/application/domains/add-a-domain-to-your-account)

2. Open NS1 in a new browser tab or window and sign in

3. Navigate to DNS and select the domain you are adding to Northflank from Zones

4. Select add record

5. Select TXT under record type, or CNAME to add a subdomain

6. Set the TTL (time to live) to 60 seconds (you can select a higher or default value, but it might take longer to register changes)

7. Copy the record name from Northflank into the answers field, click save all changes to save the record

![Adding a TXT record to verify a domain on NS1](https://assets.northflank.com/documentation/v1/application/domains/domain-registrar-guides/ns1/ns1-domain.png)

1. Return to the domains page on Northflank and select verify on the entry for your domain

2. Your domain should verify shortly. If not, check you have entered the record correctly and try again.

3. You can now [link your domain to a service](https://northflank.com/docs/v1/application/domains/link-a-domain-to-a-port)

### Add an apex domain

You can add an apex domain on NS1 by adding an ALIAS record with an empty name field and the Northflank generated content as the answer.

![Adding a CNAME record to link an apex domain on NS1](https://assets.northflank.com/documentation/v1/application/domains/domain-registrar-guides/ns1/ns1-apex.png)

## Next steps

- [Link a domain to a port: How to link and unlink domains and subdomains with specific ports on your deployments.](/v1/application/domains/link-a-domain-to-a-port)
- [Add public ports: Configure ports to expose your services on the internet.](/v1/application/network/configure-ports#public-ports)
