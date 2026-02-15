# Source: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/delegated-dcv/index.md

---

title: Delegated domain control validation (DCV) · Cloudflare for Platforms docs
description: Delegated DCV allows SaaS providers to delegate the DCV process to Cloudflare.
lastUpdated: 2025-10-30T10:25:20.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/delegated-dcv/
  md: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/delegated-dcv/index.md
---

Delegated DCV allows SaaS providers to delegate the DCV process to Cloudflare.

DCV Delegation requires your customers to place a one-time record at their authoritative DNS that allows Cloudflare to auto-renew all future certificate orders, so that there is no manual intervention from you or your customers at the time of the renewal.

***

## Setup

To set up Delegated DCV:

1. Add a [custom hostname](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/create-custom-hostnames/) for your zone, choosing `TXT` as the **Certificate validation method**.

2. On the [**Custom Hostnames**](https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/custom-hostnames) page, go to **DCV Delegation for Custom Hostnames**.

3. Copy the hostname value.

4. For each hostname, the domain owner needs to place a `CNAME` record at their authoritative DNS. In this example, the SaaS zone is `example.com`.

   ```txt
   _acme-challenge.example.com CNAME example.com.<COPIED_HOSTNAME>.
   ```

Once this is complete, Cloudflare will place two TXT DCV records - one for `example.com` and one for `*.example.com` - at the `example.com.<COPIED_HOSTNAME>` hostname. The CNAME record will need to stay in place in order to allow Cloudflare to continue placing the records for the renewals.

If desired, you could also manually fetch the DCV tokens and share them with your customers.

Remove previous TXT records

Existing TXT records for `_acme-challenge` will conflict with the delegated DCV CNAME record. Make sure to check and remove records such as the following:

```txt
_acme-challenge.example.com TXT <CERTIFICATE_VALIDATION_VALUE>
```

## Moved domains

If you [move your SaaS zone to another account](https://developers.cloudflare.com/fundamentals/manage-domains/move-domain/), you will need to update the `CNAME` record with a new hostname value.
