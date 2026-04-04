# Source: https://developers.cloudflare.com/waf/llms.txt

# WAF

Filter incoming traffic and protect against web app vulnerabilities

> Links below point directly to Markdown versions of each page. Any page can also be retrieved as Markdown by sending an `Accept: text/markdown` header to the page's URL without the `index.md` suffix (for example, `curl -H "Accept: text/markdown" https://developers.cloudflare.com/waf/`).
>
> For other Cloudflare products, see the [Cloudflare documentation directory](https://developers.cloudflare.com/llms.txt).
>
> Use [WAF llms-full.txt](https://developers.cloudflare.com/waf/llms-full.txt) for the complete WAF documentation in a single file, intended for offline indexing, bulk vectorization, or large-context models.

## Overview

- [Cloudflare Web Application Firewall](https://developers.cloudflare.com/waf/index.md): The Cloudflare Web Application Firewall (WAF) provides automatic protection from vulnerabilities and the flexibility to create custom rules.

## Get started

- [Get started](https://developers.cloudflare.com/waf/get-started/index.md)

## Concepts

- [Concepts](https://developers.cloudflare.com/waf/concepts/index.md)

## Traffic detections

- [Traffic detections](https://developers.cloudflare.com/waf/detections/index.md)
- [AI Security for Apps](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/index.md)
- [Example mitigation rules](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/example-rules/index.md)
- [AI Security for Apps fields](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/fields/index.md)
- [Get started with AI Security for Apps](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/get-started/index.md)
- [Log mode versus production mode](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/log-mode-vs-production-mode/index.md)
- [PII detection](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/pii-detection/index.md)
- [Prompt injection detection](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/prompt-injection/index.md)
- [Token counting](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/token-counting/index.md)
- [Unsafe and custom topic detection](https://developers.cloudflare.com/waf/detections/ai-security-for-apps/unsafe-topics/index.md)
- [WAF attack score](https://developers.cloudflare.com/waf/detections/attack-score/index.md)
- [Leaked credentials detection](https://developers.cloudflare.com/waf/detections/leaked-credentials/index.md)
- [Common API calls](https://developers.cloudflare.com/waf/detections/leaked-credentials/api-calls/index.md)
- [Example mitigation rules](https://developers.cloudflare.com/waf/detections/leaked-credentials/examples/index.md): Examples of rules for mitigating requests containing leaked credentials.
- [Get started](https://developers.cloudflare.com/waf/detections/leaked-credentials/get-started/index.md)
- [Terraform configuration examples](https://developers.cloudflare.com/waf/detections/leaked-credentials/terraform-examples/index.md)
- [Bot score](https://developers.cloudflare.com/waf/detections/link-bots/index.md)
- [Malicious uploads detection](https://developers.cloudflare.com/waf/detections/malicious-uploads/index.md)
- [Common API calls](https://developers.cloudflare.com/waf/detections/malicious-uploads/api-calls/index.md)
- [Example rules](https://developers.cloudflare.com/waf/detections/malicious-uploads/example-rules/index.md)
- [Get started](https://developers.cloudflare.com/waf/detections/malicious-uploads/get-started/index.md)
- [Terraform configuration examples](https://developers.cloudflare.com/waf/detections/malicious-uploads/terraform-examples/index.md)

## Custom rules

- [Custom rules](https://developers.cloudflare.com/waf/custom-rules/index.md)
- [Create a custom rule via API](https://developers.cloudflare.com/waf/custom-rules/create-api/index.md)
- [Create a custom rule in the dashboard](https://developers.cloudflare.com/waf/custom-rules/create-dashboard/index.md)
- [Custom rulesets (zone level)](https://developers.cloudflare.com/waf/custom-rules/custom-rulesets/index.md)
- [Create using Terraform](https://developers.cloudflare.com/waf/custom-rules/link-create-terraform/index.md)
- [Configure a rule with the Skip action](https://developers.cloudflare.com/waf/custom-rules/skip/index.md)
- [API examples](https://developers.cloudflare.com/waf/custom-rules/skip/api-examples/index.md)
- [Available skip options](https://developers.cloudflare.com/waf/custom-rules/skip/options/index.md)
- [Allow traffic from IP addresses in allowlist only](https://developers.cloudflare.com/waf/custom-rules/use-cases/allow-traffic-from-ips-in-allowlist/index.md)
- [Allow traffic from specific countries only](https://developers.cloudflare.com/waf/custom-rules/use-cases/allow-traffic-from-specific-countries/index.md)
- [Allow traffic from search engine bots](https://developers.cloudflare.com/waf/custom-rules/use-cases/allow-traffic-from-verified-bots/index.md)
- [Block requests by attack score](https://developers.cloudflare.com/waf/custom-rules/use-cases/block-attack-score/index.md)
- [Block traffic by geographical location](https://developers.cloudflare.com/waf/custom-rules/use-cases/block-by-geographical-location/index.md)
- [Block Microsoft Exchange Autodiscover requests](https://developers.cloudflare.com/waf/custom-rules/use-cases/block-ms-exchange-autodiscover/index.md)
- [Block traffic from specific countries](https://developers.cloudflare.com/waf/custom-rules/use-cases/block-traffic-from-specific-countries/index.md)
- [Challenge bad bots](https://developers.cloudflare.com/waf/custom-rules/use-cases/challenge-bad-bots/index.md)
- [Issue challenge for admin user in JWT claim based on attack score](https://developers.cloudflare.com/waf/custom-rules/use-cases/check-jwt-claim-to-protect-admin-user/index.md)
- [Configure token authentication](https://developers.cloudflare.com/waf/custom-rules/use-cases/configure-token-authentication/index.md)
- [Exempt partners from Hotlink Protection](https://developers.cloudflare.com/waf/custom-rules/use-cases/exempt-partners-hotlink-protection/index.md)
- [Require a specific cookie](https://developers.cloudflare.com/waf/custom-rules/use-cases/require-specific-cookie/index.md)
- [Require specific HTTP headers](https://developers.cloudflare.com/waf/custom-rules/use-cases/require-specific-headers/index.md)
- [Require specific HTTP ports](https://developers.cloudflare.com/waf/custom-rules/use-cases/require-specific-http-ports/index.md)
- [Build a sequence rule within custom rules](https://developers.cloudflare.com/waf/custom-rules/use-cases/sequence-custom-rules/index.md)
- [Require known IP addresses in site admin area](https://developers.cloudflare.com/waf/custom-rules/use-cases/site-admin-only-known-ips/index.md)
- [Stop R-U-Dead-Yet? (R.U.D.Y.) attacks](https://developers.cloudflare.com/waf/custom-rules/use-cases/stop-rudy-attacks/index.md)
- [Update custom rules for customers or partners](https://developers.cloudflare.com/waf/custom-rules/use-cases/update-rules-customers-partners/index.md)

## Rate limiting rules

- [Rate limiting rules](https://developers.cloudflare.com/waf/rate-limiting-rules/index.md)
- [Rate limiting best practices](https://developers.cloudflare.com/waf/rate-limiting-rules/best-practices/index.md)
- [Create a rate limiting rule via API](https://developers.cloudflare.com/waf/rate-limiting-rules/create-api/index.md)
- [Create a rate limiting rule in the dashboard](https://developers.cloudflare.com/waf/rate-limiting-rules/create-zone-dashboard/index.md)
- [Find appropriate rate limit](https://developers.cloudflare.com/waf/rate-limiting-rules/find-rate-limit/index.md)
- [Create using Terraform](https://developers.cloudflare.com/waf/rate-limiting-rules/link-create-terraform/index.md)
- [Rate limiting parameters](https://developers.cloudflare.com/waf/rate-limiting-rules/parameters/index.md)
- [Request rate calculation](https://developers.cloudflare.com/waf/rate-limiting-rules/request-rate/index.md)
- [Troubleshoot rate limiting rules](https://developers.cloudflare.com/waf/rate-limiting-rules/troubleshooting/index.md)
- [Rate limiting rule examples](https://developers.cloudflare.com/waf/rate-limiting-rules/use-cases/index.md)

## Managed Rules

- [Managed Rules](https://developers.cloudflare.com/waf/managed-rules/index.md)
- [Check for exposed credentials](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/index.md)
- [Configure exposed credentials checks via API](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/configure-api/index.md)
- [Configure exposed credentials checks using Terraform](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/configure-terraform/index.md)
- [How exposed credentials checks work](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/how-checks-work/index.md)
- [Monitor exposed credentials events](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/monitor-events/index.md)
- [Test your exposed credentials checks configuration](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/test-configuration/index.md)
- [Upgrade to leaked credentials detection](https://developers.cloudflare.com/waf/managed-rules/check-for-exposed-credentials/upgrade-to-leaked-credentials-detection/index.md)
- [Deploy a WAF managed ruleset via API (zone)](https://developers.cloudflare.com/waf/managed-rules/deploy-api/index.md)
- [Deploy a WAF managed ruleset in the dashboard](https://developers.cloudflare.com/waf/managed-rules/deploy-zone-dashboard/index.md)
- [Deploy using Terraform](https://developers.cloudflare.com/waf/managed-rules/link-deploy-terraform/index.md)
- [Log the payload of matched rules](https://developers.cloudflare.com/waf/managed-rules/payload-logging/index.md)
- [Command-line operations](https://developers.cloudflare.com/waf/managed-rules/payload-logging/command-line/index.md)
- [Decrypt the payload content](https://developers.cloudflare.com/waf/managed-rules/payload-logging/command-line/decrypt-payload/index.md)
- [Generate a key pair](https://developers.cloudflare.com/waf/managed-rules/payload-logging/command-line/generate-key-pair/index.md)
- [Configure payload logging in the dashboard](https://developers.cloudflare.com/waf/managed-rules/payload-logging/configure/index.md)
- [Configure payload logging via API](https://developers.cloudflare.com/waf/managed-rules/payload-logging/configure-api/index.md)
- [Store decrypted matched payloads in logs](https://developers.cloudflare.com/waf/managed-rules/payload-logging/decrypt-in-logs/index.md)
- [View the payload content in the dashboard](https://developers.cloudflare.com/waf/managed-rules/payload-logging/view/index.md)
- [Cloudflare Managed Ruleset](https://developers.cloudflare.com/waf/managed-rules/reference/cloudflare-managed-ruleset/index.md)
- [Cloudflare Exposed Credentials Check Managed Ruleset](https://developers.cloudflare.com/waf/managed-rules/reference/exposed-credentials-check/index.md)
- [Cloudflare OWASP Core Ruleset](https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/index.md)
- [Concepts](https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/concepts/index.md)
- [Configure via API](https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/configure-api/index.md)
- [Configure in the dashboard](https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/configure-dashboard/index.md)
- [OWASP evaluation example](https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/example/index.md)
- [Configure in Terraform](https://developers.cloudflare.com/waf/managed-rules/reference/owasp-core-ruleset/link-configure-terraform/index.md)
- [Cloudflare Sensitive Data Detection](https://developers.cloudflare.com/waf/managed-rules/reference/sensitive-data-detection/index.md)
- [Troubleshoot managed rules](https://developers.cloudflare.com/waf/managed-rules/troubleshooting/index.md)
- [Create exceptions](https://developers.cloudflare.com/waf/managed-rules/waf-exceptions/index.md)
- [Add an exception via API](https://developers.cloudflare.com/waf/managed-rules/waf-exceptions/define-api/index.md)
- [Add an exception in the dashboard](https://developers.cloudflare.com/waf/managed-rules/waf-exceptions/define-dashboard/index.md): Use the Cloudflare dashboard to create exceptions that skip the execution of WAF managed rulesets or specific ruleset rules.

## Account-level WAF configuration

- [Account-level WAF configuration](https://developers.cloudflare.com/waf/account/index.md)
- [Custom rulesets (account level)](https://developers.cloudflare.com/waf/account/custom-rulesets/index.md)
- [Create a custom ruleset using the API](https://developers.cloudflare.com/waf/account/custom-rulesets/create-api/index.md)
- [Work with custom rulesets in the dashboard](https://developers.cloudflare.com/waf/account/custom-rulesets/create-dashboard/index.md)
- [Use Terraform](https://developers.cloudflare.com/waf/account/custom-rulesets/link-create-terraform/index.md)
- [Managed rulesets](https://developers.cloudflare.com/waf/account/managed-rulesets/index.md)
- [Deploy a WAF managed ruleset via API (account)](https://developers.cloudflare.com/waf/account/managed-rulesets/deploy-api/index.md)
- [Deploy a WAF managed ruleset in the dashboard (account)](https://developers.cloudflare.com/waf/account/managed-rulesets/deploy-dashboard/index.md)
- [Create exceptions](https://developers.cloudflare.com/waf/account/managed-rulesets/link-create-exceptions/index.md)
- [Deploy using Terraform](https://developers.cloudflare.com/waf/account/managed-rulesets/link-create-terraform/index.md)
- [Rate limiting rulesets](https://developers.cloudflare.com/waf/account/rate-limiting-rulesets/index.md)
- [Create a rate limiting ruleset via API](https://developers.cloudflare.com/waf/account/rate-limiting-rulesets/create-api/index.md)
- [Create a rate limiting ruleset in the dashboard](https://developers.cloudflare.com/waf/account/rate-limiting-rulesets/create-dashboard/index.md)
- [Create using Terraform](https://developers.cloudflare.com/waf/account/rate-limiting-rulesets/link-create-terraform/index.md)

## Security features interoperability

- [Security features interoperability](https://developers.cloudflare.com/waf/feature-interoperability/index.md): How Cloudflare security features interact and execute in order.

## Glossary

- [Glossary](https://developers.cloudflare.com/waf/glossary/index.md)

## WAF changelog overview

- [WAF changelog overview](https://developers.cloudflare.com/waf/change-log/index.md)
- [Changelog](https://developers.cloudflare.com/waf/change-log/changelog/index.md)
- [Historical (2022)](https://developers.cloudflare.com/waf/change-log/historical-2022/index.md): Changes to WAF managed rulesets done in 2022.
- [Historical (2023)](https://developers.cloudflare.com/waf/change-log/historical-2023/index.md): Changes to WAF managed rulesets done in 2023.
- [Historical (2024)](https://developers.cloudflare.com/waf/change-log/historical-2024/index.md): Changes to WAF managed rulesets done in 2024.
- [Scheduled changes](https://developers.cloudflare.com/waf/change-log/scheduled-changes/index.md)

## analytics

- [Security Analytics](https://developers.cloudflare.com/waf/analytics/security-analytics/index.md)
- [Security Events](https://developers.cloudflare.com/waf/analytics/security-events/index.md)

## reference

- [Alerts for security events](https://developers.cloudflare.com/waf/reference/alerts/index.md)
- [Firewall rules upgrade](https://developers.cloudflare.com/waf/reference/legacy/firewall-rules-upgrade/index.md)
- [Firewall rules](https://developers.cloudflare.com/waf/reference/legacy/link-firewall-rules/index.md)
- [Rate Limiting (previous version)](https://developers.cloudflare.com/waf/reference/legacy/old-rate-limiting/index.md)
- [Troubleshoot Rate Limiting (previous version)](https://developers.cloudflare.com/waf/reference/legacy/old-rate-limiting/troubleshooting/index.md)
- [Rate limiting (previous version) upgrade](https://developers.cloudflare.com/waf/reference/legacy/old-rate-limiting/upgrade/index.md): Guide on upgrading rate limiting rules from the previous version to the new version.
- [WAF managed rules (previous version)](https://developers.cloudflare.com/waf/reference/legacy/old-waf-managed-rules/index.md)
- [Troubleshoot WAF managed rules (previous version)](https://developers.cloudflare.com/waf/reference/legacy/old-waf-managed-rules/troubleshooting/index.md)
- [WAF managed rules upgrade](https://developers.cloudflare.com/waf/reference/legacy/old-waf-managed-rules/upgrade/index.md)
- [WAF phases](https://developers.cloudflare.com/waf/reference/phases/index.md)

## tools

- [Browser Integrity Check](https://developers.cloudflare.com/waf/tools/browser-integrity-check/index.md)
- [IP Access rules](https://developers.cloudflare.com/waf/tools/ip-access-rules/index.md)
- [IP Access rules actions](https://developers.cloudflare.com/waf/tools/ip-access-rules/actions/index.md)
- [Create an IP access rule](https://developers.cloudflare.com/waf/tools/ip-access-rules/create/index.md)
- [IP Access rules parameters](https://developers.cloudflare.com/waf/tools/ip-access-rules/parameters/index.md)
- [Enable security.txt](https://developers.cloudflare.com/waf/tools/link-security-txt/index.md)
- [Lists](https://developers.cloudflare.com/waf/tools/lists/index.md)
- [Create a list in the dashboard](https://developers.cloudflare.com/waf/tools/lists/create-dashboard/index.md)
- [Custom lists](https://developers.cloudflare.com/waf/tools/lists/custom-lists/index.md)
- [Bulk Redirect Lists](https://developers.cloudflare.com/waf/tools/lists/link-bulk-redirect-lists/index.md)
- [Lists API](https://developers.cloudflare.com/waf/tools/lists/lists-api/index.md)
- [Lists API endpoints](https://developers.cloudflare.com/waf/tools/lists/lists-api/endpoints/index.md)
- [List JSON object](https://developers.cloudflare.com/waf/tools/lists/lists-api/json-object/index.md): Reference information on the JSON object used in Lists API calls.
- [Managed Lists](https://developers.cloudflare.com/waf/tools/lists/managed-lists/index.md)
- [Use lists in expressions](https://developers.cloudflare.com/waf/tools/lists/use-in-expressions/index.md): Learn how to use lists in rule expressions.
- [Privacy Pass](https://developers.cloudflare.com/waf/tools/privacy-pass/index.md)
- [Replace insecure JS libraries](https://developers.cloudflare.com/waf/tools/replace-insecure-js-libraries/index.md)
- [Email Address Obfuscation](https://developers.cloudflare.com/waf/tools/scrape-shield/email-address-obfuscation/index.md)
- [Hotlink Protection](https://developers.cloudflare.com/waf/tools/scrape-shield/hotlink-protection/index.md)
- [Security Level](https://developers.cloudflare.com/waf/tools/security-level/index.md)
- [User Agent Blocking](https://developers.cloudflare.com/waf/tools/user-agent-blocking/index.md)
- [Validation checks](https://developers.cloudflare.com/waf/tools/validation-checks/index.md)
- [Zone Lockdown](https://developers.cloudflare.com/waf/tools/zone-lockdown/index.md)

## troubleshooting

- [Bing's Site Scan blocked by a managed rule](https://developers.cloudflare.com/waf/troubleshooting/blocked-bing-site-scans/index.md): A WAF managed rule may block site scans performed by Bing Webmaster Tools.
- [Issues sharing to Facebook](https://developers.cloudflare.com/waf/troubleshooting/facebook-sharing/index.md)
- [FAQ](https://developers.cloudflare.com/waf/troubleshooting/faq/index.md)
- [SameSite cookie interaction with Cloudflare](https://developers.cloudflare.com/waf/troubleshooting/samesite-cookie-interaction/index.md)