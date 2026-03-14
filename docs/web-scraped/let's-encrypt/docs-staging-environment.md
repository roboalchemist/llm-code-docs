# Source: https://letsencrypt.org/docs/staging-environment/

Title: Staging Environment

URL Source: https://letsencrypt.org/docs/staging-environment/

Markdown Content:
Staging Environment - Let's Encrypt
===============

Languages![Image 1](https://letsencrypt.org/images/language-icon128px-black.png)

[English](https://letsencrypt.org/docs/staging-environment/)[Català](https://letsencrypt.org/ca/docs/staging-environment/)[Čeština](https://letsencrypt.org/cs/docs/staging-environment/)[Dansk](https://letsencrypt.org/da/docs/staging-environment/)[Deutsch](https://letsencrypt.org/de/docs/staging-environment/)[Greek](https://letsencrypt.org/el/docs/staging-environment/)[Español](https://letsencrypt.org/es/docs/staging-environment/)[Suomi](https://letsencrypt.org/fi/docs/staging-environment/)[Français](https://letsencrypt.org/fr/docs/staging-environment/)[עברית](https://letsencrypt.org/he/docs/staging-environment/)[Magyar](https://letsencrypt.org/hu/docs/staging-environment/)[Bahasa Indonesia](https://letsencrypt.org/id/docs/staging-environment/)[Italiano](https://letsencrypt.org/it/docs/staging-environment/)[日本語](https://letsencrypt.org/ja/docs/staging-environment/)[한국어](https://letsencrypt.org/ko/docs/staging-environment/)[Polish](https://letsencrypt.org/pl/docs/staging-environment/)[Português do Brasil](https://letsencrypt.org/pt-br/docs/staging-environment/)[Русский](https://letsencrypt.org/ru/docs/staging-environment/)[සිංහල](https://letsencrypt.org/si/docs/staging-environment/)[Srpski](https://letsencrypt.org/sr/docs/staging-environment/)[Svenska](https://letsencrypt.org/sv/docs/staging-environment/)[Tamil](https://letsencrypt.org/ta/docs/staging-environment/)[Thai](https://letsencrypt.org/th/docs/staging-environment/)[Türkçe](https://letsencrypt.org/tr/docs/staging-environment/)[Українська](https://letsencrypt.org/uk/docs/staging-environment/)[Tiếng Việt](https://letsencrypt.org/vi/docs/staging-environment/)[简体中文](https://letsencrypt.org/zh-cn/docs/staging-environment/)[繁體中文](https://letsencrypt.org/zh-tw/docs/staging-environment/)

[Skip navigation links](https://letsencrypt.org/docs/staging-environment/#main-content)

[![Image 2: Let's Encrypt](https://letsencrypt.org/images/letsencrypt-logo-horizontal.svg)](https://letsencrypt.org/)

*   [Documentation](https://letsencrypt.org/docs/)
*   [Get Help](https://community.letsencrypt.org/)
*   [Blog](https://letsencrypt.org/blog/)
*   
Donate
    *   [Become a Sponsor](https://www.abetterinternet.org/sponsor/)
    *   [Current Sponsors & Funders](https://www.abetterinternet.org/sponsors/)
    *   [Get Involved](https://letsencrypt.org/getinvolved/)
    *   [Donate](https://letsencrypt.org/donate/)

*   
About Us
    *   [Let's Encrypt](https://letsencrypt.org/about/)
    *   [Frequently Asked Questions (FAQ)](https://letsencrypt.org/docs/faq/)
    *   [Policy and Legal Repository](https://letsencrypt.org/repository/)
    *   [Service Status](https://letsencrypt.status.io/)
    *   [Statistics](https://letsencrypt.org/stats/)
    *   [Contact](https://letsencrypt.org/contact/)
    *   [Careers](https://www.abetterinternet.org/careers/)
    *   [Annual reports](https://www.abetterinternet.org/annual-reports/)
    *   [Internet Security Research Group (ISRG)](https://www.abetterinternet.org/about/)

*   [Donate Now](https://letsencrypt.org/donate/)

[Donate Now](https://letsencrypt.org/donate/)

Staging Environment
===================

 Last updated: November 25, 2025 

[See all Documentation](https://letsencrypt.org/docs)

We highly recommend testing against our staging environment before using our production environment. This will allow you to get things right before issuing trusted certificates and reduce the chance of your running up against rate limits.

The ACME URL for our [ACME v2 staging environment](https://community.letsencrypt.org/t/staging-endpoint-for-acme-v2/49605) is:

`https://acme-staging-v02.api.letsencrypt.org/directory`

If you’re using [Certbot](https://certbot.eff.org/), you can use our staging environment with the `--test-cert` or `--dry-run` flag. For other ACME clients, please read their instructions for information on testing with our staging environment.

Note that ACME accounts are scoped to each environment, and thus a separate account for the staging environment is required. Certbot handles this for you.

Rate Limits
===========

The staging environment uses the same rate limits as [described for the production environment](https://letsencrypt.org/docs/rate-limits/) but with different values:

*   The **[New Registrations per IP Address](https://letsencrypt.org/docs/rate-limits/#new-registrations-per-ip-address)** limit is 50 per 3 hours.
*   The **[New Registrations per IPv6 Range](https://letsencrypt.org/docs/rate-limits/#new-registrations-per-ipv6-range)** limit is 500 per 3 hours (the same as production).
*   The **[New Orders per Account](https://letsencrypt.org/docs/rate-limits/#new-orders-per-account)** limit is 1500 per 3 hours.
*   The **[New Certificates per Registered Domain](https://letsencrypt.org/docs/rate-limits/#new-certificates-per-registered-domain)** limit is 30000 per second.
*   The **[New Certificates per Exact Set of Hostnames](https://letsencrypt.org/docs/rate-limits/#new-certificates-per-exact-set-of-hostnames)** limit is 30000 per week.
*   The **[Authorization Failures per Hostname per Account](https://letsencrypt.org/docs/rate-limits/#authorization-failures-per-hostname-per-account)** limit is 200 per hour.
*   The **[Consecutive Authorization Failures per Hostname per Account](https://letsencrypt.org/docs/rate-limits/#consecutive-authorization-failures-per-hostname-per-account)** limit is 3600 per 6 hours.

The [Overall Requests Limits](https://letsencrypt.org/docs/rate-limits/#overall-requests-limit) are:

| Endpoint | Requests per IP (per second) | Burst Capacity |
| --- | --- | --- |
| /acme/new-nonce | 20 | 10 |
| /acme/new-account | 5 | 15 |
| /acme/new-order | 20 | 40 |
| /acme/revoke-cert | 10 | 100 |
| /acme/renewal-info | 1000 | 100 |
| /acme/* | 20 | 20 |
| /directory | 40 | 40 |

Staging Certificate Hierarchy
=============================

The staging environment has a certificate hierarchy that [mimics production](https://letsencrypt.org/certificates/). The names have been modified with a prefix of (STAGING) and unique name to make them clearly distinct from their production counterparts.

Root CAs
--------

The staging environment has four active root certificates which are **not present** in browser/client trust stores: “(STAGING) Pretend Pear X1”, “(STAGING) Bogus Broccoli X2”, “(STAGING) Yearning Yucca Root YE”, and “(STAGING) Yonder Yam Root YR”.

If you wish to modify a test-only client to trust the staging environment for testing purposes you can do so by adding their certificates to your testing trust store. **Important note:** Do not add the staging root or intermediate to a trust store that you use for ordinary browsing or other activities, since they are not audited or held to the same standards as our production roots, and so are not safe to use for anything other than testing.

*   **Pretend Pear X1**
    *   Subject: `O = (STAGING) Internet Security Research Group, CN = (STAGING) Pretend Pear X1`
    *   Key type: `RSA 4096`
    *   Certificate details: [der](https://letsencrypt.org/certs/staging/letsencrypt-stg-root-x1.der), [pem](https://letsencrypt.org/certs/staging/letsencrypt-stg-root-x1.pem), [txt](https://letsencrypt.org/certs/staging/letsencrypt-stg-root-x1.txt)

*   **Bogus Broccoli X2**
    *   Subject: `O = (STAGING) Internet Security Research Group, CN = (STAGING) Bogus Broccoli X2`
    *   Key type: `ECDSA P-384`
    *   Certificate details (self-signed): [der](https://letsencrypt.org/certs/staging/letsencrypt-stg-root-x2.der), [pem](https://letsencrypt.org/certs/staging/letsencrypt-stg-root-x2.pem), [txt](https://letsencrypt.org/certs/staging/letsencrypt-stg-root-x2.txt)
    *   Certificate details (cross-signed by Pretend Pear X1): [der](https://letsencrypt.org/certs/staging/letsencrypt-stg-root-x2-signed-by-x1.der), [pem](https://letsencrypt.org/certs/staging/letsencrypt-stg-root-x2-signed-by-x1.pem), [txt](https://letsencrypt.org/certs/staging/letsencrypt-stg-root-x2-signed-by-x1.txt)

*   **Yearning Yucca Root YE**
    *   Subject: `O = ISRG, CN = (STAGING) Yearning Yucca Root YE`
    *   Key type: `ECDSA P-384`
    *   Certificate details (self-signed): [der](https://letsencrypt.org/certs/staging/gen-y/root-ye.der), [pem](https://letsencrypt.org/certs/staging/gen-y/root-ye.pem), [txt](https://letsencrypt.org/certs/staging/gen-y/root-ye.txt)
    *   Certificate details (cross-signed by Bogus Broccoli X2): [der](https://letsencrypt.org/certs/staging/gen-y/root-ye-by-x2.der), [pem](https://letsencrypt.org/certs/staging/gen-y/root-ye-by-x2.pem), [txt](https://letsencrypt.org/certs/staging/gen-y/root-ye-by-x2.txt)

*   **Yonder Yam Root YR**
    *   Subject: `O = ISRG, CN = (STAGING) Yonder Yam Root YR`
    *   Key type: `RSA 4096`
    *   Certificate details (self-signed): [der](https://letsencrypt.org/certs/staging/gen-y/root-yr.der), [pem](https://letsencrypt.org/certs/staging/gen-y/root-yr.pem), [txt](https://letsencrypt.org/certs/staging/gen-y/root-yr.txt)
    *   Certificate details (cross-signed by Pretend Pear X1): [der](https://letsencrypt.org/certs/staging/gen-y/root-yr-by-x1.der), [pem](https://letsencrypt.org/certs/staging/gen-y/root-yr-by-x1.pem), [txt](https://letsencrypt.org/certs/staging/gen-y/root-yr-by-x1.txt)

Subordinate (Intermediate) CAs
------------------------------

The staging environment has intermediate certificates that mimic production, issued from the untrusted roots detailed above. Like in production, not all are in use at any time. The full list of current intermediates is:

*   (STAGING) Pseudo Plum E5
*   (STAGING) False Fennel E6
*   (STAGING) Puzzling Parsnip E7
*   (STAGING) Mysterious Mulberry E8
*   (STAGING) Fake Fig E9
*   (STAGING) Counterfeit Cashew R10
*   (STAGING) Wannabe Watercress R11
*   (STAGING) Riddling Rhubarb R12
*   (STAGING) Tenuous Tomato R13
*   (STAGING) Not Nectarine R14
*   (STAGING) Artificial Amaranth YE1
*   (STAGING) Baloney Bulgur YE2
*   (STAGING) Cad Corn YE3
*   (STAGING) Dastardly Durum YR1
*   (STAGING) Ersatz Emmer YR2
*   (STAGING) Fake Farro YR3

These intermediates are subject to change at any time, and should not be pinned or trusted by any system. In general, you can expect the staging intermediates to parallel the corresponding production (trusted) intermediates. If strictly necessary, you can get full certificate details [here](https://github.com/letsencrypt/website/blob/main/static/certs/staging).

Certificate Transparency
========================

The staging environment uses several test CT logs. SCTs from these logs are included in staging certificates. However, as staging is a test environment only, CT cannot be used to observe staging issued certificates reliably.

These logs include Let’s Encrypt [Testing Logs](https://letsencrypt.org/docs/ct-logs/#testing), as well as test logs from other Certificate Transparency log operators.

Additionally, some [ct-test-srv](https://pkg.go.dev/github.com/letsencrypt/boulder/test/ct-test-srv) logs may be used, which are not actual logs and do not store issued certificates.

Continuous Integration / Development Testing
============================================

The staging environment has generous rate limits to enable testing but it is not a great fit for integration with development environments or continuous integration (CI). Making network requests to external servers can introduce instability and the staging environment offers no way to “fake” DNS or challenge validation success which makes for more complicated test setups.

In addition to the staging environment Let’s Encrypt offers a small ACME server purpose built for CI and development environments called [Pebble](https://github.com/letsencrypt/pebble). Running Pebble on your development machine or in a CI environment is [quick and easy](https://github.com/letsencrypt/pebble#docker).

![Image 3: Internet Security Research Group (ISRG)](https://letsencrypt.org/images/ISRG-Logo-Blue.svg)
Let's Encrypt is a free, automated, and open Certificate Authority brought to you by the nonprofit [Internet Security Research Group (ISRG)](https://www.abetterinternet.org/). Read all about our nonprofit work this year in our [2025 Annual Report](https://www.abetterinternet.org/annual-reports/).

Legal Address

548 Market St, PMB 77519

San Francisco, CA 94104-5401

USA

Send all mail or inquiries to:

PO Box 18666

Minneapolis, MN 55418-0666

USA

#### Subscribe for email updates about Let's Encrypt and other ISRG projects

 © 2026 [Internet Security Research Group](https://www.abetterinternet.org/)

*   [GitHub](https://github.com/letsencrypt)
*   [LinkedIn](https://www.linkedin.com/company/lets-encrypt/)
*   [Terms](https://www.abetterinternet.org/terms-of-service)
*   [Privacy Policy](https://letsencrypt.org/privacy/)
*   [Trademark Policy](https://www.abetterinternet.org/trademarks)
