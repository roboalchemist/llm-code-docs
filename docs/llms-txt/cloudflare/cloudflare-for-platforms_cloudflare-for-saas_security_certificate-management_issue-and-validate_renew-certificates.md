# Source: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/renew-certificates/index.md

---

title: Renew certificates · Cloudflare for Platforms docs
description: The exact method for certificate renewal depends on whether that
  hostname is active1 and whether it is a wildcard certificate.
lastUpdated: 2026-01-30T10:18:21.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/renew-certificates/
  md: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/renew-certificates/index.md
---

The exact method for certificate renewal depends on whether that hostname is active[1](#user-content-fn-1) and whether it is a wildcard certificate.

Custom hostname certificates have a 90-day validity period and are available for renewal 30 days before their expiration.

## Non-wildcard hostnames

If all of the following are true, Cloudflare will try to perform DCV automatically on the hostname's behalf by serving the [HTTP token](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/http/).

* You are using a non-wildcard hostname.
* The hostname is active.
* You are not using [Delegated DCV](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/delegated-dcv/).

If the custom hostname is not active, then the custom hostname domain owner will need to add the TXT or HTTP DCV token for the new certificate to validate and issue. As the SaaS provider, you will be responsible for sharing this token with the custom hostname domain owner.

If you are using Delegated DCV, Cloudflare will continue to add TXT DCV tokens on your behalf as explained in [Issue and validate certificates](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/delegated-dcv/).

## Wildcard hostnames

With wildcard hostnames, you cannot use HTTP. In this case, you will have to use TXT DCV tokens.

These tokens can be fetched through the API or the dashboard when the certificates are in a [pending validation](https://developers.cloudflare.com/ssl/reference/certificate-statuses/#new-certificates) state during custom hostname creation or during certificate renewals.

If your hostname is using another validation method, you will need to [update](https://developers.cloudflare.com/api/resources/custom_hostnames/methods/edit/) the `"method"` field in the SSL object to be `"txt"`.

After this step, follow the normal steps for [TXT validation](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/txt/).

Note

To allow Cloudflare to auto-renew all future certificate orders, consider [DCV delegation](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/delegated-dcv/).

## Footnotes

1. Meaning Cloudflare could verify your customer's ownership of the hostname and the [hostname status](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/validation-status/) is active. [↩](#user-content-fnref-1)
