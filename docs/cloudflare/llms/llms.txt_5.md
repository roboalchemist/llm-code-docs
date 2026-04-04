# Source: https://developers.cloudflare.com/dns/llms.txt

# DNS

Deliver excellent performance and reliability to your domain

> Links below point directly to Markdown versions of each page. Any page can also be retrieved as Markdown by sending an `Accept: text/markdown` header to the page's URL without the `index.md` suffix (for example, `curl -H "Accept: text/markdown" https://developers.cloudflare.com/dns/`).
>
> For other Cloudflare products, see the [Cloudflare documentation directory](https://developers.cloudflare.com/llms.txt).
>
> Use [DNS llms-full.txt](https://developers.cloudflare.com/dns/llms-full.txt) for the complete DNS documentation in a single file, intended for offline indexing, bulk vectorization, or large-context models.

## Overview

- [Cloudflare DNS](https://developers.cloudflare.com/dns/index.md)

## Get started

- [Get started](https://developers.cloudflare.com/dns/get-started/index.md)

## Concepts

- [Concepts](https://developers.cloudflare.com/dns/concepts/index.md): Understand key DNS concepts with Cloudflare's technical documentation. Learn about nameservers, DNS records, DNSSEC, and more.

## DNS setups

- [DNS setups](https://developers.cloudflare.com/dns/zone-setups/index.md)
- [Convert full setup to partial setup](https://developers.cloudflare.com/dns/zone-setups/conversions/convert-full-to-partial/index.md)
- [Convert full setup to secondary setup](https://developers.cloudflare.com/dns/zone-setups/conversions/convert-full-to-secondary/index.md): If you initially configured a full setup you can later convert your zone to use incoming zone transfers (Cloudflare as secondary).
- [Convert partial setup to full setup](https://developers.cloudflare.com/dns/zone-setups/conversions/convert-partial-to-full/index.md): If you initially set up a partial domain on Cloudflare, you can later migrate it to a full setup.
- [Convert partial setup to secondary setup](https://developers.cloudflare.com/dns/zone-setups/conversions/convert-partial-to-secondary/index.md): If you initially set up a partial zone on Cloudflare, you can later convert it to use a secondary setup.
- [Convert secondary setup to full setup](https://developers.cloudflare.com/dns/zone-setups/conversions/convert-secondary-to-full/index.md): If you initially set up incoming zone transfers (Cloudflare as secondary), you can later convert your zone to use a full setup.
- [Convert secondary setup to partial setup](https://developers.cloudflare.com/dns/zone-setups/conversions/convert-secondary-to-partial/index.md): If you initially set up incoming zone transfers (Cloudflare as secondary), you can later convert your zone to use a partial setup.
- [Primary setup (Full)](https://developers.cloudflare.com/dns/zone-setups/full-setup/index.md)
- [Set up a primary zone (Full setup)](https://developers.cloudflare.com/dns/zone-setups/full-setup/setup/index.md): If you want to use Cloudflare as your primary DNS provider and manage your DNS records, your domain should be using a full setup.
- [Troubleshooting](https://developers.cloudflare.com/dns/zone-setups/full-setup/troubleshooting/index.md): Learn how to troubleshoot issues with a primary setup (full)
- [CNAME setup (Partial)](https://developers.cloudflare.com/dns/zone-setups/partial-setup/index.md)
- [DNS resolution](https://developers.cloudflare.com/dns/zone-setups/partial-setup/dns-resolution/index.md)
- [Setup](https://developers.cloudflare.com/dns/zone-setups/partial-setup/setup/index.md): A CNAME setup (also known as partial) allows you to use Cloudflare's reverse proxy while maintaining your primary and authoritative DNS provider.
- [Records quick scan](https://developers.cloudflare.com/dns/zone-setups/reference/dns-quick-scan/index.md)
- [Zone status](https://developers.cloudflare.com/dns/zone-setups/reference/domain-status/index.md)
- [Zone removal](https://developers.cloudflare.com/dns/zone-setups/removal/index.md)
- [Subdomain setup](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/index.md)
- [Enable DNSSEC](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/dnssec/index.md)
- [Migrate to new account](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/move-to-new-account/index.md)
- [Rollback](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/rollback/index.md)
- [Setup](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/setup/index.md)
- [Parent zone on full setup](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/setup/parent-on-full/index.md)
- [Parent zone on partial setup](https://developers.cloudflare.com/dns/zone-setups/subdomain-setup/setup/parent-on-partial/index.md)
- [Cannot add domain](https://developers.cloudflare.com/dns/zone-setups/troubleshooting/cannot-add-domain/index.md): Troubleshoot issues when adding a domain to Cloudflare, including DNSSEC conflicts, registrar errors, and restriction codes.
- [Delete all DNS records](https://developers.cloudflare.com/dns/zone-setups/troubleshooting/delete-all-records/index.md): Learn how to bulk delete DNS records in Cloudflare with a script so you can start from zero instead of using the quick scan results.
- [Domain deleted from Cloudflare](https://developers.cloudflare.com/dns/zone-setups/troubleshooting/domain-deleted/index.md): Learn why a domain may be removed from Cloudflare and how to recover it using audit logs and registrar verification.
- [DNS Zone transfers](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/index.md)
- [Access Control Lists (ACLs)](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/access-control-lists/index.md)
- [Cloudflare IP addresses](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/access-control-lists/cloudflare-ip-addresses/index.md)
- [Create ACL](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/access-control-lists/create-new-list/index.md)
- [Cloudflare as Primary](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/index.md)
- [Set up DNSSEC with Cloudflare as Primary](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/dnssec-for-primary/index.md): With outgoing zone transfers, you keep Cloudflare as your primary DNS provider and use one or more secondary providers for increased availability and fault tolerance.
- [Setup](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/setup/index.md): With outgoing zone transfers, you can keep Cloudflare as your primary DNS provider and use one or more secondary providers for increased availability.
- [Records transfer](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-primary/transfer-criteria/index.md)
- [Cloudflare as Secondary](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/index.md)
- [Alerts](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/alerts/index.md)
- [DNSSEC options](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/dnssec-for-secondary/index.md)
- [Proxy traffic](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/proxy-traffic/index.md)
- [Setup](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/cloudflare-as-secondary/setup/index.md): With incoming zone transfers, you can keep your primary DNS provider and use Cloudflare as a secondary DNS provider.
- [Troubleshooting](https://developers.cloudflare.com/dns/zone-setups/zone-transfers/troubleshooting/index.md): Learn how to troubleshoot issues with secondary nameservers.

## Foundation DNS

- [Foundation DNS](https://developers.cloudflare.com/dns/foundation-dns/index.md)
- [Advanced nameservers](https://developers.cloudflare.com/dns/foundation-dns/advanced-nameservers/index.md)
- [DNSSEC keys](https://developers.cloudflare.com/dns/foundation-dns/dnssec-keys/index.md)
- [Set up advanced nameservers](https://developers.cloudflare.com/dns/foundation-dns/setup/index.md)

## Nameservers

- [Nameservers](https://developers.cloudflare.com/dns/nameservers/index.md)
- [Advanced nameservers](https://developers.cloudflare.com/dns/nameservers/advanced-nameservers/index.md)
- [Custom nameservers](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/index.md)
- [Set up account custom nameservers](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/account-custom-nameservers/index.md): With account-level custom nameservers, you can use the same custom nameservers for different zones in the account. The domain or domains that provide the nameservers names do not have to exist as zones in Cloudflare.
- [Set up tenant custom nameservers](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/tenant-custom-nameservers/index.md): With tenant-level custom nameservers, you can use the same custom nameservers for different zones and across different accounts, as long as the accounts are part of the [tenant](/tenant/). The domain or domains that provide the nameservers names do not have to exist as zones in Cloudflare.
- [Set up zone custom nameservers](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/zone-custom-nameservers/index.md): With zone-level custom nameservers, each custom nameserver name must be a subdomain of the zone where the custom nameservers are configured. These custom nameservers can only be used within the respective zone.
- [Nameserver options](https://developers.cloudflare.com/dns/nameservers/nameserver-options/index.md)
- [Update nameservers](https://developers.cloudflare.com/dns/nameservers/update-nameservers/index.md)

## DNS records

- [DNS records](https://developers.cloudflare.com/dns/manage-dns-records/index.md)
- [Batch record changes](https://developers.cloudflare.com/dns/manage-dns-records/how-to/batch-record-changes/index.md)
- [Manage DNS records](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/index.md)
- [Create subdomain records](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-subdomain/index.md)
- [Create zone apex record](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-zone-apex/index.md)
- [Set up email records](https://developers.cloudflare.com/dns/manage-dns-records/how-to/email-records/index.md)
- [Import and export records](https://developers.cloudflare.com/dns/manage-dns-records/how-to/import-and-export/index.md)
- [Dynamically update DNS records](https://developers.cloudflare.com/dns/manage-dns-records/how-to/managing-dynamic-ip-addresses/index.md)
- [Round-robin DNS](https://developers.cloudflare.com/dns/manage-dns-records/how-to/round-robin-dns/index.md)
- [Delegate subdomains](https://developers.cloudflare.com/dns/manage-dns-records/how-to/subdomains-outside-cloudflare/index.md)
- [DNS record types](https://developers.cloudflare.com/dns/manage-dns-records/reference/dns-record-types/index.md)
- [Record attributes](https://developers.cloudflare.com/dns/manage-dns-records/reference/record-attributes/index.md)
- [Time to Live (TTL)](https://developers.cloudflare.com/dns/manage-dns-records/reference/ttl/index.md)
- [Vendor-specific DNS records](https://developers.cloudflare.com/dns/manage-dns-records/reference/vendor-specific-records/index.md)
- [Wildcard DNS records](https://developers.cloudflare.com/dns/manage-dns-records/reference/wildcard-dns-records/index.md)
- [Verify a domain with CNAME](https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/cname-domain-verification/index.md): Troubleshoot domain verification failures caused by proxied CNAME records, CNAME flattening, or NS record conflicts.
- [NS records already exist](https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/existing-ns-record/index.md)
- [Exposed IP addresses](https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/exposed-ip-address/index.md): Understand and resolve warnings about DNS records that expose your origin server IP address.
- [Records with the same name](https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/records-with-same-name/index.md)
- [Stale response for upstream DNS resolution](https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/stale-response/index.md)
- [Unexpected DNS records](https://developers.cloudflare.com/dns/manage-dns-records/troubleshooting/unexpected-dns-records/index.md)

## Proxy status

- [Proxy status](https://developers.cloudflare.com/dns/proxy-status/index.md)
- [Proxying limitations](https://developers.cloudflare.com/dns/proxy-status/limitations/index.md)

## DNSSEC

- [DNSSEC](https://developers.cloudflare.com/dns/dnssec/index.md)
- [Migrate an existing zone with DNSSEC enabled](https://developers.cloudflare.com/dns/dnssec/dnssec-active-migration/index.md): Follow this tutorial to migrate an existing DNS zone to Cloudflare without having to disable DNSSEC.
- [DNSSEC states](https://developers.cloudflare.com/dns/dnssec/dnssec-states/index.md)
- [NSEC3 support](https://developers.cloudflare.com/dns/dnssec/enable-nsec3/index.md): Learn how to enable NSEC3 support with Cloudflare to meet compliance requirements.
- [About](https://developers.cloudflare.com/dns/dnssec/multi-signer-dnssec/about/index.md)
- [Set up multi-signer DNSSEC](https://developers.cloudflare.com/dns/dnssec/multi-signer-dnssec/setup/index.md)
- [Troubleshooting](https://developers.cloudflare.com/dns/dnssec/troubleshooting/index.md): Learn how to troubleshoot issues with DNSSEC
- [Validation and keys](https://developers.cloudflare.com/dns/dnssec/validation-and-key-management/index.md)

## CNAME flattening

- [CNAME flattening](https://developers.cloudflare.com/dns/cname-flattening/index.md)
- [Example diagram](https://developers.cloudflare.com/dns/cname-flattening/cname-flattening-diagram/index.md): Consider an example use case and the main steps involved in CNAME flattening.
- [Setup](https://developers.cloudflare.com/dns/cname-flattening/set-up-cname-flattening/index.md)

## Internal DNS (beta)

- [Internal DNS (beta)](https://developers.cloudflare.com/dns/internal-dns/index.md)
- [Analytics and logs](https://developers.cloudflare.com/dns/internal-dns/analytics/index.md)
- [Connect to Gateway resolver](https://developers.cloudflare.com/dns/internal-dns/connectivity/index.md)
- [Manage DNS views](https://developers.cloudflare.com/dns/internal-dns/dns-views/index.md)
- [Get started](https://developers.cloudflare.com/dns/internal-dns/get-started/index.md)
- [Internal zones](https://developers.cloudflare.com/dns/internal-dns/internal-zones/index.md): Explore internal DNS zones in Cloudflare. These zones organize DNS records for resources accessible only within your private network, queried via Cloudflare Gateway.
- [Manage internal DNS records](https://developers.cloudflare.com/dns/internal-dns/internal-zones/internal-dns-records/index.md): Manage internal DNS records in Cloudflare. Learn about supported DNS record types and CNAME flattening.
- [Reference zones](https://developers.cloudflare.com/dns/internal-dns/internal-zones/reference-zones/index.md): Learn about reference zones. Cloudflare Internal DNS allows zones to reference others for query resolution when no direct record is found.
- [Manage internal zones](https://developers.cloudflare.com/dns/internal-dns/internal-zones/setup/index.md): Understand how to set up and manage internal DNS zones with Cloudflare. Explore configuration conditions, zone creation, and available API endpoints.

## DNS Firewall

- [DNS Firewall](https://developers.cloudflare.com/dns/dns-firewall/index.md)
- [Analytics and logs](https://developers.cloudflare.com/dns/dns-firewall/analytics/index.md)
- [DNS Firewall FAQ](https://developers.cloudflare.com/dns/dns-firewall/faq/index.md): Find answers to common questions about Cloudflare's DNS Firewall, including cache behavior, EDNS support, and setting PTR records.
- [Random prefix attack mitigation](https://developers.cloudflare.com/dns/dns-firewall/random-prefix-attacks/index.md)
- [About](https://developers.cloudflare.com/dns/dns-firewall/random-prefix-attacks/about/index.md): Learn about random prefix attacks. As part of DNS Firewall, Cloudflare can protect your upstream authoritative nameservers from these attacks.
- [Setup](https://developers.cloudflare.com/dns/dns-firewall/random-prefix-attacks/setup/index.md)
- [Setup](https://developers.cloudflare.com/dns/dns-firewall/setup/index.md): Set up DNS Firewall to protect upstream nameservers from DDoS attacks and reduce load by caching DNS responses.

## Troubleshooting

- [Troubleshooting](https://developers.cloudflare.com/dns/troubleshooting/index.md)
- [Available debug endpoints](https://developers.cloudflare.com/dns/troubleshooting/dns-debug-endpoints/index.md): Use dig commands against Cloudflare nameservers to find your public IP, connected data center, DNS software version, and more.
- [General DNS issues](https://developers.cloudflare.com/dns/troubleshooting/dns-issues/index.md): Troubleshoot common DNS resolution errors like "This site can't be reached", err_name_not_resolved, and Error 1001 when using Cloudflare.
- [DNS_PROBE_FINISHED_NXDOMAIN](https://developers.cloudflare.com/dns/troubleshooting/dns-probe-finished-nxdomain/index.md): Learn how to fix the DNS_PROBE_FINISHED_NXDOMAIN browser error, which indicates the domain does not exist.
- [DNS_PROBE_POSSIBLE](https://developers.cloudflare.com/dns/troubleshooting/dns-probe-possible/index.md): Learn how to fix the DNS_PROBE_POSSIBLE browser error when using Cloudflare DNS.
- [Email issues](https://developers.cloudflare.com/dns/troubleshooting/email-issues/index.md)

## FAQ

- [FAQ](https://developers.cloudflare.com/dns/faq/index.md): Find answers to common questions about Cloudflare's authoritative DNS.

## Changelog

- [Changelog](https://developers.cloudflare.com/dns/changelog/index.md)

## Glossary

- [Glossary](https://developers.cloudflare.com/dns/glossary/index.md)

## additional-options

- [Analytics and logs](https://developers.cloudflare.com/dns/additional-options/analytics/index.md)
- [Configure DNS zone defaults](https://developers.cloudflare.com/dns/additional-options/dns-zone-defaults/index.md)
- [Reverse zones and PTR records](https://developers.cloudflare.com/dns/additional-options/reverse-zones/index.md)

## reference

- [Features and plans](https://developers.cloudflare.com/dns/reference/all-features/index.md): Review information on all Cloudflare DNS features and their availability.
- [Analytics API properties](https://developers.cloudflare.com/dns/reference/analytics-api-properties/index.md): API properties that you can use in API requests for Cloudflare DNS analytics.
- [Analytics MCP server](https://developers.cloudflare.com/dns/reference/analytics-mcp-server/index.md)
- [Migrate DNS from BIND](https://developers.cloudflare.com/dns/reference/best-practices/index.md)
- [Domain Connect](https://developers.cloudflare.com/dns/reference/domain-connect/index.md): Learn how to onboard your templates to use Domain Connect with Cloudflare as DNS provider.
- [Recommended third-party tools](https://developers.cloudflare.com/dns/reference/recommended-third-party-tools/index.md): List of recommended third-party tools for DNS testing and troubleshooting.