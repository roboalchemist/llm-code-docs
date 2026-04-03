# Source: https://developers.cloudflare.com/terraform/llms.txt

# Terraform

Define and store Cloudflare configurations in source code repositories like GitHub

> Links below point directly to Markdown versions of each page. Any page can also be retrieved as Markdown by sending an `Accept: text/markdown` header to the page's URL without the `index.md` suffix (for example, `curl -H "Accept: text/markdown" https://developers.cloudflare.com/terraform/`).
>
> For other Cloudflare products, see the [Cloudflare documentation directory](https://developers.cloudflare.com/llms.txt).
>
> Use [Terraform llms-full.txt](https://developers.cloudflare.com/terraform/llms-full.txt) for the complete Terraform documentation in a single file, intended for offline indexing, bulk vectorization, or large-context models.

## Overview

- [Cloudflare Terraform provider](https://developers.cloudflare.com/terraform/index.md)

## Get started

- [Get started](https://developers.cloudflare.com/terraform/installing/index.md)

## Tutorials

- [Tutorials](https://developers.cloudflare.com/terraform/tutorial/index.md)
- [5 â Add exceptions with Page Rules](https://developers.cloudflare.com/terraform/tutorial/add-page-rules/index.md): Page Rules let you override zone settings for specific URL patterns. Redirects old URLs with a 301 permanent redirect.
- [3 â Configure HTTPS settings](https://developers.cloudflare.com/terraform/tutorial/configure-https-settings/index.md): This tutorial shows how to enable TLS 1.3, Automatic HTTPS Rewrites, and Strict SSL mode using the updated v5 provider.
- [1 â  Initialize Terraform](https://developers.cloudflare.com/terraform/tutorial/initialize-terraform/index.md): This tutorial shows you how to get started with Terraform. You will create a DNS record pointing www.example.com to a web server at 203.0.113.10.
- [6 â Revert configuration](https://developers.cloudflare.com/terraform/tutorial/revert-configuration/index.md): Sometimes, you may have to roll back configuration changes. To revert your configuration, check out the desired branch and ask Terraform to move your Cloudflare settings back in time.
- [2 â Track your history](https://developers.cloudflare.com/terraform/tutorial/track-history/index.md): Learn how to track history with Cloudflare Terraform.
- [4 â Improve performance](https://developers.cloudflare.com/terraform/tutorial/use-load-balancing/index.md): Learn how to use Terraform with Cloudflare Load Balancing product to fail traffic over as needed.

## additional-configurations

- [DDoS managed rulesets configuration using Terraform](https://developers.cloudflare.com/terraform/additional-configurations/ddos-managed-rulesets/index.md)
- [Bulk Redirects](https://developers.cloudflare.com/terraform/additional-configurations/link-bulk-redirects/index.md)
- [Cache Rules](https://developers.cloudflare.com/terraform/additional-configurations/link-cache-rules/index.md)
- [Configuration Rules](https://developers.cloudflare.com/terraform/additional-configurations/link-configuration-rules/index.md)
- [Origin Rules](https://developers.cloudflare.com/terraform/additional-configurations/link-origin-rules/index.md)
- [Single Redirects](https://developers.cloudflare.com/terraform/additional-configurations/link-single-redirects/index.md)
- [Snippets](https://developers.cloudflare.com/terraform/additional-configurations/link-snippets/index.md)
- [Workers](https://developers.cloudflare.com/terraform/additional-configurations/link-workers/index.md)
- [Rate limiting rules configuration using Terraform](https://developers.cloudflare.com/terraform/additional-configurations/rate-limiting-rules/index.md)
- [Transform Rules configuration using Terraform](https://developers.cloudflare.com/terraform/additional-configurations/transform-rules/index.md)
- [WAF custom rules configuration using Terraform](https://developers.cloudflare.com/terraform/additional-configurations/waf-custom-rules/index.md)
- [WAF Managed Rules configuration using Terraform](https://developers.cloudflare.com/terraform/additional-configurations/waf-managed-rulesets/index.md)

## advanced-topics

- [Best practices](https://developers.cloudflare.com/terraform/advanced-topics/best-practices/index.md)
- [Import Cloudflare resources](https://developers.cloudflare.com/terraform/advanced-topics/import-cloudflare-resources/index.md): The Cloudflare Terraform tool is available in the Terraform ME repository. To use it, you must first install the Terraform app on your Mac or Linux system. You must then import Cloudflare resources individually by providing their IDs and names.
- [Provider customization](https://developers.cloudflare.com/terraform/advanced-topics/provider-customization/index.md)
- [Remote R2 backend](https://developers.cloudflare.com/terraform/advanced-topics/remote-backend/index.md)

## how-to

- [Create a partial zone using Terraform](https://developers.cloudflare.com/terraform/how-to/create-partial-zone/index.md)
- [Create a subdomain zone using Terraform](https://developers.cloudflare.com/terraform/how-to/create-secondary-zone/index.md)

## troubleshooting

- [403 Authentication error when creating DNS records](https://developers.cloudflare.com/terraform/troubleshooting/authentication-error-dns-records/index.md)
- [Rule IDs change when I modify a ruleset](https://developers.cloudflare.com/terraform/troubleshooting/rule-id-changes/index.md)