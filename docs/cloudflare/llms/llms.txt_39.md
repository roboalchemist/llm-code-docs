# Source: https://developers.cloudflare.com/fundamentals/llms.txt

# Cloudflare Fundamentals

Learn about using Cloudflare and features that span across Cloudflare products

> Links below point directly to Markdown versions of each page. Any page can also be retrieved as Markdown by sending an `Accept: text/markdown` header to the page's URL without the `index.md` suffix (for example, `curl -H "Accept: text/markdown" https://developers.cloudflare.com/fundamentals/`).
>
> For other Cloudflare products, see the [Cloudflare documentation directory](https://developers.cloudflare.com/llms.txt).
>
> Use [Cloudflare Fundamentals llms-full.txt](https://developers.cloudflare.com/fundamentals/llms-full.txt) for the complete Cloudflare Fundamentals documentation in a single file, intended for offline indexing, bulk vectorization, or large-context models.

## Overview

- [Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/index.md)

## Get started

- [Get started](https://developers.cloudflare.com/fundamentals/get-started/index.md)

## Organizations

- [Organizations](https://developers.cloudflare.com/fundamentals/organizations/index.md)
- [Limitations](https://developers.cloudflare.com/fundamentals/organizations/limitations/index.md)
- [Set up](https://developers.cloudflare.com/fundamentals/organizations/setup/index.md)

## Members and permissions

- [Members and permissions](https://developers.cloudflare.com/fundamentals/manage-members/index.md)
- [Set up dashboard SSO](https://developers.cloudflare.com/fundamentals/manage-members/dashboard-sso/index.md)
- [Manage](https://developers.cloudflare.com/fundamentals/manage-members/manage/index.md)
- [Policies](https://developers.cloudflare.com/fundamentals/manage-members/policies/index.md)
- [Roles](https://developers.cloudflare.com/fundamentals/manage-members/roles/index.md)
- [Role scopes](https://developers.cloudflare.com/fundamentals/manage-members/scope/index.md)
- [User Groups](https://developers.cloudflare.com/fundamentals/manage-members/user-groups/index.md)

## User profiles

- [User profiles](https://developers.cloudflare.com/fundamentals/user-profiles/index.md)
- [Two-factor authentication](https://developers.cloudflare.com/fundamentals/user-profiles/2fa/index.md)
- [Account recovery](https://developers.cloudflare.com/fundamentals/user-profiles/account-recovery/index.md)
- [Email address and password](https://developers.cloudflare.com/fundamentals/user-profiles/change-password-or-email/index.md): Learn how to change your email address or password associated with your account.
- [Profile settings](https://developers.cloudflare.com/fundamentals/user-profiles/customize-account/index.md)
- [Delete your Cloudflare account](https://developers.cloudflare.com/fundamentals/user-profiles/delete-account/index.md)
- [Log in to Cloudflare](https://developers.cloudflare.com/fundamentals/user-profiles/login/index.md)
- [Multi-Factor Email Authentication](https://developers.cloudflare.com/fundamentals/user-profiles/multi-factor-email-authentication/index.md): Cloudflare's Multi-Factor Email Authentication prevents unauthorized access by sending one-time codes to your email.
- [Verify email address](https://developers.cloudflare.com/fundamentals/user-profiles/verify-email-address/index.md)

## Domains

- [Domains](https://developers.cloudflare.com/fundamentals/manage-domains/index.md)
- [Add multiple sites via automation](https://developers.cloudflare.com/fundamentals/manage-domains/add-multiple-sites-automation/index.md): To add multiple sites to Cloudflare at once and more efficiently, you can do so via the Cloudflare API.
- [Onboard a domain](https://developers.cloudflare.com/fundamentals/manage-domains/add-site/index.md): Learn how to onboard your domain to Cloudflare, to speed up and protect your website or application.
- [Change your domain version](https://developers.cloudflare.com/fundamentals/manage-domains/domain-version/index.md): Version Management allows you to safely test, deploy, and roll back changes to your zone configurations. By default, Version Management is not enabled on a zone.
- [Manage subdomains](https://developers.cloudflare.com/fundamentals/manage-domains/manage-subdomains/index.md)
- [Move a domain between Cloudflare accounts](https://developers.cloudflare.com/fundamentals/manage-domains/move-domain/index.md): Learn how to transfer a domain between Cloudflare accounts, including requirements, DNS settings, and SSL/TLS certificate management for seamless migration.
- [Pause Cloudflare](https://developers.cloudflare.com/fundamentals/manage-domains/pause-cloudflare/index.md)
- [Redirect one domain to another](https://developers.cloudflare.com/fundamentals/manage-domains/redirect-domain/index.md)
- [Remove a domain](https://developers.cloudflare.com/fundamentals/manage-domains/remove-domain/index.md)
- [Star domains](https://developers.cloudflare.com/fundamentals/manage-domains/star-zones/index.md)

## account

- [Add abuse contact](https://developers.cloudflare.com/fundamentals/account/account-security/abuse-contact/index.md)
- [Audit Logs - version 2](https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/index.md)
- [Allow Cloudflare access](https://developers.cloudflare.com/fundamentals/account/account-security/cloudflare-access/index.md)
- [Set up SSO](https://developers.cloudflare.com/fundamentals/account/account-security/dashboard-sso/index.md)
- [Leaked Password Notifications](https://developers.cloudflare.com/fundamentals/account/account-security/leaked-password-notifications/index.md)
- [Manage active sessions](https://developers.cloudflare.com/fundamentals/account/account-security/manage-active-sessions/index.md)
- [Review audit logs - v1](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/index.md)
- [SCIM provisioning](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/index.md)
- [Provision with Authentik](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/authentik/index.md)
- [Provision with Microsoft Entra](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/entra/index.md)
- [Provision with Okta](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/okta/index.md)
- [SCIM troubleshooting](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/troubleshooting/index.md)
- [Secure compromised account](https://developers.cloudflare.com/fundamentals/account/account-security/secure-a-compromised-account/index.md): If you observe suspicious activity within your Cloudflare account, secure your account with these steps.
- [Zone holds](https://developers.cloudflare.com/fundamentals/account/account-security/zone-holds/index.md)
- [Change Super Administrator](https://developers.cloudflare.com/fundamentals/account/change-super-admin/index.md)
- [Create account](https://developers.cloudflare.com/fundamentals/account/create-account/index.md): Learn how to create a new Cloudflare account.
- [Find account and zone IDs](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/index.md)

## api

- [Account API tokens](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/index.md): Learn what account API tokens are, when to use them, and what they currently work with
- [Get Origin CA keys](https://developers.cloudflare.com/fundamentals/api/get-started/ca-keys/index.md)
- [Create API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/index.md): Learn how to create a token to perform actions using the Cloudflare API.
- [Get Global API key (legacy)](https://developers.cloudflare.com/fundamentals/api/get-started/keys/index.md)
- [API token template URLs](https://developers.cloudflare.com/fundamentals/api/how-to/account-owned-token-template/index.md): Generate Cloudflare API tokens with pre-configured permissions using template URLs. Learn how to create and customize template URLs for any use case.
- [Control API Access](https://developers.cloudflare.com/fundamentals/api/how-to/control-api-access/index.md)
- [Create tokens via API](https://developers.cloudflare.com/fundamentals/api/how-to/create-via-api/index.md): Learn how to create API tokens via Cloudflare's API. Follow steps to define access policies, set restrictions, and generate tokens securely.
- [Make API calls](https://developers.cloudflare.com/fundamentals/api/how-to/make-api-calls/index.md): Learn how to make API calls using Cloudflare's API with step-by-step instructions for Windows, including using curl and PowerShell, and handling JSON.
- [Restrict tokens](https://developers.cloudflare.com/fundamentals/api/how-to/restrict-tokens/index.md)
- [Roll tokens](https://developers.cloudflare.com/fundamentals/api/how-to/roll-token/index.md)
- [API deprecations](https://developers.cloudflare.com/fundamentals/api/reference/deprecations/index.md)
- [GraphQL API](https://developers.cloudflare.com/fundamentals/api/reference/graphql-api/index.md)
- [Rate limits](https://developers.cloudflare.com/fundamentals/api/reference/limits/index.md)
- [API token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/index.md)
- [REST API](https://developers.cloudflare.com/fundamentals/api/reference/rest-api/index.md)
- [SDKs](https://developers.cloudflare.com/fundamentals/api/reference/sdks/index.md)
- [API token templates](https://developers.cloudflare.com/fundamentals/api/reference/template/index.md): Explore Cloudflare's API token templates to efficiently manage permissions. Start with a template and customize token permissions and resources as needed.
- [Wrangler API](https://developers.cloudflare.com/fundamentals/api/reference/wrangler-api/index.md)
- [Troubleshooting](https://developers.cloudflare.com/fundamentals/api/troubleshooting/index.md)

## concepts

- [Accounts, zones, and profiles](https://developers.cloudflare.com/fundamentals/concepts/accounts-and-zones/index.md)
- [Cloudflare IP addresses](https://developers.cloudflare.com/fundamentals/concepts/cloudflare-ip-addresses/index.md)
- [How Cloudflare DNS works](https://developers.cloudflare.com/fundamentals/concepts/how-cloudflare-works/index.md)
- [Traffic flow through Cloudflare](https://developers.cloudflare.com/fundamentals/concepts/traffic-flow-cloudflare/index.md)

## new-features

- [Available RSS Feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/index.md): Read about the various RSS feeds available for Cloudflare's changelogs.
- [Consuming RSS Feeds](https://developers.cloudflare.com/fundamentals/new-features/consuming-rss-feeds/index.md): Learn how to consume our changelog RSS feeds.

## performance

- [Improve SEO](https://developers.cloudflare.com/fundamentals/performance/improve-seo/index.md)
- [Maintenance mode](https://developers.cloudflare.com/fundamentals/performance/maintenance-mode/index.md)
- [Minimize downtime](https://developers.cloudflare.com/fundamentals/performance/minimize-downtime/index.md): Learn how to minimize downtime while onboarding your domain onto Cloudflare.
- [Optimize site speed](https://developers.cloudflare.com/fundamentals/performance/optimize-speed-external-link/index.md)
- [Prepare for surges or spikes in web traffic](https://developers.cloudflare.com/fundamentals/performance/preparing-for-surges-or-spikes-in-web-traffic/index.md)
- [Test speed](https://developers.cloudflare.com/fundamentals/performance/test-speed/index.md)

## reference

- [Account and domain management best practices](https://developers.cloudflare.com/fundamentals/reference/best-practices/index.md)
- [/cdn-cgi/ endpoint](https://developers.cloudflare.com/fundamentals/reference/cdn-cgi-endpoint/index.md)
- [Cloudflare Ray ID](https://developers.cloudflare.com/fundamentals/reference/cloudflare-ray-id/index.md)
- [Cloudflare crawlers](https://developers.cloudflare.com/fundamentals/reference/cloudflare-site-crawling/index.md)
- [Cloudy AI agent (beta)](https://developers.cloudflare.com/fundamentals/reference/cloudy-ai-agent/index.md)
- [Connection limits](https://developers.cloudflare.com/fundamentals/reference/connection-limits/index.md)
- [Cryptographic Attestation of Personhood](https://developers.cloudflare.com/fundamentals/reference/cryptographic-personhood/index.md)
- [Glossary](https://developers.cloudflare.com/fundamentals/reference/glossary/index.md)
- [Cloudflare and Google Analytics](https://developers.cloudflare.com/fundamentals/reference/google-analytics/index.md)
- [Cloudflare HTTP headers](https://developers.cloudflare.com/fundamentals/reference/http-headers/index.md)
- [Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/index.md)
- [SCIM v1 to v2 Migration](https://developers.cloudflare.com/fundamentals/reference/migration-guides/scim-virtual-groups-migration/index.md): Migrate from SCIM v1 Virtual Groups to Cloudflareâs GA SCIM User Groups
- [Network Layers](https://developers.cloudflare.com/fundamentals/reference/network-layers/index.md)
- [Network ports](https://developers.cloudflare.com/fundamentals/reference/network-ports/index.md)
- [Partners](https://developers.cloudflare.com/fundamentals/reference/partners/index.md)
- [Cloudflare Cookies](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cloudflare-cookies/index.md)
- [Compliance documentation](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/compliance-docs/index.md)
- [Content Security Policies (CSPs)](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/content-security-policies/index.md)
- [Project Cybersafe Schools](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cybersafe/index.md)
- [Delivering Videos with Cloudflare](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/delivering-videos-with-cloudflare/index.md)
- [Licenses](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/licenses/index.md)
- [Redirects](https://developers.cloudflare.com/fundamentals/reference/redirects/index.md)
- [Abuse](https://developers.cloudflare.com/fundamentals/reference/report-abuse/index.md): Learn how to report DMCA issues, phishing, trademark infringement, malware sites, child exploitation material, and more to Cloudflareâs Trust and Safety team.
- [Customer abuse report obligations](https://developers.cloudflare.com/fundamentals/reference/report-abuse/abuse-report-obligations/index.md)
- [Complaint types](https://developers.cloudflare.com/fundamentals/reference/report-abuse/complaint-types/index.md)
- [Providing specific URLs](https://developers.cloudflare.com/fundamentals/reference/report-abuse/provide-specific-urls/index.md): Learn how to provide specific asset URLs when submitting an abuse report.
- [Review abuse policies](https://developers.cloudflare.com/fundamentals/reference/report-abuse/review-policies/index.md)
- [View and submit reports](https://developers.cloudflare.com/fundamentals/reference/report-abuse/submit-report/index.md)
- [Scans and penetration testing policy](https://developers.cloudflare.com/fundamentals/reference/scans-penetration/index.md)
- [SDK ecosystem support policy](https://developers.cloudflare.com/fundamentals/reference/sdk-ecosystem-support-policy/index.md)
- [TCP connections](https://developers.cloudflare.com/fundamentals/reference/tcp-connections/index.md)
- [Troubleshooting](https://developers.cloudflare.com/fundamentals/reference/troubleshooting/index.md)
- [Under Attack mode](https://developers.cloudflare.com/fundamentals/reference/under-attack-mode/index.md)

## security

- [Scan for PCI compliance](https://developers.cloudflare.com/fundamentals/security/pci-scans/index.md)
- [Prevent DDoS attacks](https://developers.cloudflare.com/fundamentals/security/prevent-ddos-attacks-external/index.md)
- [Protect your origin server](https://developers.cloudflare.com/fundamentals/security/protect-your-origin-server/index.md)
- [Recovering from a hacked site](https://developers.cloudflare.com/fundamentals/security/recovering-from-hacked-site/index.md)
- [Secure your website](https://developers.cloudflare.com/fundamentals/security/secure-your-website/index.md)
- [Under a DDoS attack?](https://developers.cloudflare.com/fundamentals/security/under-ddos-attack/index.md): Learn a few ways to tell if your application is under a DDoS attack.