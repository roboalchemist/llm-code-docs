# Source: https://docs.firehydrant.com/docs/ip-and-domain-based-restrictions.md

# IP and Domain-Based Restrictions

## IP Addresses

FireHydrant's infrastructure makes all requests from the following two IP addresses:

* `34.150.247.118`
* `35.185.58.206`

Make sure you authorize incoming requests from these addresses in your firewall.

All of our integrations use authenticated API calls. But if you are using the Webhook Runbook step or a [Webhook](https://docs.firehydrant.com/docs/webhooks) in conjunction with a [Command Extension](https://docs.firehydrant.com/docs/command-extensions) to make a call to a separate system/service, you should make sure to [verify the signature](/docs/runbook-step-send-a-webhook#signature-verification) to ensure the call is being made from FireHydrant.

## Domains

FireHydrant's domains are `firehydrant.io` and `firehydrant.com`. If you need to implement any domain or subdomain-based allowance, then we recommend allowing the following values:

* `*.firehydrant.com`
* `*.firehydrant.io`