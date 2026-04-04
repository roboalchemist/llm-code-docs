# Source: https://docs.unifygtm.com/reference/deliverability/domain-configuration.md

# Domain Configuration

> Set up domain names for Unify-managed mailboxes.

## Overview

In order to send emails through Unify Managed Email Deliverability, you need to add one or more sending domain to
the platform. We recommend adding multiple sending domains in order to distribute volume and create redundancy.

## What domains can I use?

* **YES** — Secondary domains: The reputation of these secondary domains are isolated from your primary domain. You want to follow best practices when naming these secondary domains to ensure they don't get flagged as spam.
* **NO** — Domains installed on other ESPs: The product cannot be used with domains that are used on e.g. Google Workspace because MX records can only be installed for one ESP at a time. You would need to remove certain existing DNS records to ensure we can register the domain succesfully on Unify.
* **NO** — Primary domains: We do not recommend using your primary domain for high-volume sending. The reason for this is to ensure your primary domain reputation is always kept pristine.

## How should I name my domain?

We generally recommend aiming for a .com or .io name and avoiding hyphens if possible. Common naming conventions include mybusiness.io, trymybusiness.com, getmybusiness.com.

We do not recommend using misspelt variations of your domain like mybuziness.com, even if these domain names are only a few letters off from your primary domain or company name. Your email provder will potentially show spam warnings on these emails because they look like phishing attempts.

## Best practices

* `SPF`, `DKIM`, `DMARC` - Unify enforces and monitors email authentication to ensure that your emails pass the tests conducted by the ESPs.
* `Branded links` - Unify will automatically generate branded links with your domain. E.g. links.mybusiness.io. These are used for unsubscribe links and open tracking.
* `Primary Domain Forwarding` - Secondary domains and subdomains should forward the user to the primary domain. This improves deliverability as users can investigate the secondary domain and as it creates a link between your primary domain and secondary domain.
* `WHOIS` - WHOIS information should be provided on the domain.
  Privacy Policy - The primary domain should have an easily accessible privacy policy.
* `Domain monitoring` - Unify will continuously monitor your domain health. For example by monitoring domain blocklists. If there is a problem you will be notified and sending can be paused.

## Purchasing a domain

The first step is to purchase a domain. This can be done through domain providers like CloudFlare, Google Domains, Squarespace, GoDaddy or Namecheap.

## Registering the domain in Unify

Navigate to the [domain settings page](https://app.unifygtm.com/dashboard/settings/deliverability/domains) and press "Add domain". Type in your domain name in the text box and press register. This process can take a few seconds, please wait for the registration to finish.

## DNS record overview

The screen will refresh showing you 7 DNS records to add. Below is an explanation of why we require each record:

<Frame><img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/domain-details-unverified.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=4989c087393aa6818b7c6675285d2bef" alt="domain-details-unverified" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/domain-details-unverified.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/domain-details-unverified.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=34980848b979a33ec5a85f7f192d205c 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/domain-details-unverified.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=a88c3656339a57689706b3d561b60ead 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/domain-details-unverified.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=b3d91e25237b2c9123f2feb1d3576c9f 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/domain-details-unverified.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=c1e892d47ddf1139cd168b79aa86f47c 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/domain-details-unverified.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=e9937a504c54597d9d8679e295184bd0 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/domain-details-unverified.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=c45dc8b0dc7858d693a1b0359cf6b02a 2500w" /></Frame>

* `SPF` - The SPF record authorizes Unify to send emails on your behalf. The SPF record must be exclusive to Unify as no other email providers can be used in conjunction.,
* `DKIM` - The DKIM record allows Unify to digitally sign your emails, enabling recipients to verify their authenticity and integrity.,
* `DMARC` - The DMARC record instructs recipient mail servers on how to handle emails from your domain that fail SPF or DKIM checks, enhancing your email security.,
* `MX` - Use priority 10. The MX record allows Unify to receive email messages on your behalf. The MX records must be exclusive to Unify as no other email providers can be used in conjunction. There are two MX records to create redundancy.
* `CNAME` - There are two CNAME records. The first CNAME record is an alias to Unify servers which allows branded links to be used for unsubscribes and open tracking. The second CNAME record is a validation record which authorizes Unify to accept HTTPS requests for the branded links.

## Adding the DNS records

1. Go to your domain provider (e.g. Squarespace or GoDaddy).
2. Navigate to the DNS settings.
3. Copy paste the DNS records. In order for the DNS records to propagate quickly you can use a TTL of 600 seconds.
4. Certain providers will ask you not to include the domain in the host name field. For example, `mybusiness.io` becomes `@` or sometimes just an empty string and `links.mybusiness.io` becomes just `links`.
5. It can take multiple minutes if not hours for the DNS records to propagate. You can use the refresh button in Unify to refresh the status.
6. Once the records are verified they will light up green with the text "Verified".

## Domain activation

Once the domain is verified we will automatically activate the domain which will enable you to register mailboxes under it. This process can take up to an hour.

<Frame><img src="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/domain-details-active.png?fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=d4b1aadcbeff4859a5f61826d3a34526" alt="domain-details-active" data-og-width="2880" width="2880" data-og-height="2048" height="2048" data-path="images/domain-details-active.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/domain-details-active.png?w=280&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=19c32650243d68b7c8baabd7068950c4 280w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/domain-details-active.png?w=560&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=755a286ce78ef244f61cc931d6d83812 560w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/domain-details-active.png?w=840&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=40359bebcd813fe923f21ae39d8d97a9 840w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/domain-details-active.png?w=1100&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=ac9245f3796460084b98c00f118463d9 1100w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/domain-details-active.png?w=1650&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=c49a0b3d7ebc52a6f3ba1a976a5c254e 1650w, https://mintcdn.com/unify-19/hCdysogYM6qFbUs-/images/domain-details-active.png?w=2500&fit=max&auto=format&n=hCdysogYM6qFbUs-&q=85&s=5105d08723ae39a0fc7a878d31babbed 2500w" /></Frame>

#
