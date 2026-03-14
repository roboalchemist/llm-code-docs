# Source: https://letsencrypt.org/docs/acme-protocol-updates/

Title: ACME Protocol Updates

URL Source: https://letsencrypt.org/docs/acme-protocol-updates/

Markdown Content:
ACME Protocol Updates - Let's Encrypt
===============

Languages![Image 1](https://letsencrypt.org/images/language-icon128px-black.png)

[English](https://letsencrypt.org/docs/acme-protocol-updates/)[Català](https://letsencrypt.org/ca/docs/acme-protocol-updates/)[Čeština](https://letsencrypt.org/cs/docs/acme-protocol-updates/)[Dansk](https://letsencrypt.org/da/docs/acme-protocol-updates/)[Deutsch](https://letsencrypt.org/de/docs/acme-protocol-updates/)[Greek](https://letsencrypt.org/el/docs/acme-protocol-updates/)[Español](https://letsencrypt.org/es/docs/acme-protocol-updates/)[Suomi](https://letsencrypt.org/fi/docs/acme-protocol-updates/)[Français](https://letsencrypt.org/fr/docs/acme-protocol-updates/)[עברית](https://letsencrypt.org/he/docs/acme-protocol-updates/)[Magyar](https://letsencrypt.org/hu/docs/acme-protocol-updates/)[Bahasa Indonesia](https://letsencrypt.org/id/docs/acme-protocol-updates/)[Italiano](https://letsencrypt.org/it/docs/acme-protocol-updates/)[日本語](https://letsencrypt.org/ja/docs/acme-protocol-updates/)[한국어](https://letsencrypt.org/ko/docs/acme-protocol-updates/)[Polish](https://letsencrypt.org/pl/docs/acme-protocol-updates/)[Português do Brasil](https://letsencrypt.org/pt-br/docs/acme-protocol-updates/)[Русский](https://letsencrypt.org/ru/docs/acme-protocol-updates/)[සිංහල](https://letsencrypt.org/si/docs/acme-protocol-updates/)[Srpski](https://letsencrypt.org/sr/docs/acme-protocol-updates/)[Svenska](https://letsencrypt.org/sv/docs/acme-protocol-updates/)[Tamil](https://letsencrypt.org/ta/docs/acme-protocol-updates/)[Thai](https://letsencrypt.org/th/docs/acme-protocol-updates/)[Türkçe](https://letsencrypt.org/tr/docs/acme-protocol-updates/)[Українська](https://letsencrypt.org/uk/docs/acme-protocol-updates/)[Tiếng Việt](https://letsencrypt.org/vi/docs/acme-protocol-updates/)[简体中文](https://letsencrypt.org/zh-cn/docs/acme-protocol-updates/)[繁體中文](https://letsencrypt.org/zh-tw/docs/acme-protocol-updates/)

[Skip navigation links](https://letsencrypt.org/docs/acme-protocol-updates/#main-content)

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

ACME Protocol Updates
=====================

 Last updated: October 7, 2019 

[See all Documentation](https://letsencrypt.org/docs)

The [IETF-standardized](https://letsencrypt.org/2019/03/11/acme-protocol-ietf-standard) ACME protocol, [RFC 8555](https://datatracker.ietf.org/doc/rfc8555/), is the cornerstone of how Let’s Encrypt works.

API Endpoints
=============

We currently have the following API endpoints. Please see [our divergences documentation](https://github.com/letsencrypt/boulder/blob/main/docs/acme-divergences.md) to compare their implementation to the ACME specification.

ACME v2 (RFC 8555)
------------------

*   [Production] `https://acme-v02.api.letsencrypt.org/directory`
*   [Staging] `https://acme-staging-v02.api.letsencrypt.org/directory`

ACME v1 (Deprecated)
--------------------

*   [Production] `https://acme-v01.api.letsencrypt.org/directory`
*   [Staging] `https://acme-staging.api.letsencrypt.org/directory`

New Backwards-Compatible ACME Features
======================================

From time to time Let’s Encrypt may implement new backwards-compatible features for existing API endpoints. Typically new backwards-compatible features are introduced because we’ve decided to implement a part of the ACME spec that we hadn’t implemented before.

When new features are introduced to existing API endpoints, the features will always be clearly specified in a public ACME specification and will not break properly implemented clients.

New Versions of ACME with Breaking Changes
==========================================

We do not plan to make breaking changes to our ACME support, but if we feel it’s important to do so we’ll work to allow for a smooth transition over sufficient time and communicate as far in advance as possible. Systems administrators should maintain the ability to deploy timely updates to their ACME clients in the event that a breaking change is necessary.

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
