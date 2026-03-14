# Source: https://letsencrypt.org/docs/revoking/

Title: Revoking Certificates

URL Source: https://letsencrypt.org/docs/revoking/

Markdown Content:
Revoking Certificates - Let's Encrypt
===============

Languages![Image 1](https://letsencrypt.org/images/language-icon128px-black.png)

[English](https://letsencrypt.org/docs/revoking/)[Català](https://letsencrypt.org/ca/docs/revoking/)[Čeština](https://letsencrypt.org/cs/docs/revoking/)[Dansk](https://letsencrypt.org/da/docs/revoking/)[Deutsch](https://letsencrypt.org/de/docs/revoking/)[Greek](https://letsencrypt.org/el/docs/revoking/)[Español](https://letsencrypt.org/es/docs/revoking/)[Suomi](https://letsencrypt.org/fi/docs/revoking/)[Français](https://letsencrypt.org/fr/docs/revoking/)[עברית](https://letsencrypt.org/he/docs/revoking/)[Magyar](https://letsencrypt.org/hu/docs/revoking/)[Bahasa Indonesia](https://letsencrypt.org/id/docs/revoking/)[Italiano](https://letsencrypt.org/it/docs/revoking/)[日本語](https://letsencrypt.org/ja/docs/revoking/)[한국어](https://letsencrypt.org/ko/docs/revoking/)[Polish](https://letsencrypt.org/pl/docs/revoking/)[Português do Brasil](https://letsencrypt.org/pt-br/docs/revoking/)[Русский](https://letsencrypt.org/ru/docs/revoking/)[සිංහල](https://letsencrypt.org/si/docs/revoking/)[Srpski](https://letsencrypt.org/sr/docs/revoking/)[Svenska](https://letsencrypt.org/sv/docs/revoking/)[Tamil](https://letsencrypt.org/ta/docs/revoking/)[Thai](https://letsencrypt.org/th/docs/revoking/)[Türkçe](https://letsencrypt.org/tr/docs/revoking/)[Українська](https://letsencrypt.org/uk/docs/revoking/)[Tiếng Việt](https://letsencrypt.org/vi/docs/revoking/)[简体中文](https://letsencrypt.org/zh-cn/docs/revoking/)[繁體中文](https://letsencrypt.org/zh-tw/docs/revoking/)

[Skip navigation links](https://letsencrypt.org/docs/revoking/#main-content)

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

Revoking Certificates
=====================

 Last updated: July 31, 2025 

[See all Documentation](https://letsencrypt.org/docs)

When a certificate is no longer safe to use, you should revoke it. This can happen for a few different reasons. For instance, you might accidentally share the private key on a public website; hackers might copy the private key off of your servers; or hackers might take temporary control over your servers or your DNS configuration, and use that to validate and issue a certificate for which they hold the private key.

When you revoke a Let’s Encrypt certificate, Let’s Encrypt may publish revocation information in [Certificate Revocation Lists (CRLs)](https://en.wikipedia.org/wiki/Certificate_revocation_list), and some browsers will check CRLs to see whether they should trust a certificate. Revoking certificates that correspond to compromised private keys is an important practice, and is required by Let’s Encrypt’s [Subscriber Agreement](https://letsencrypt.org/repository/).

To revoke a certificate with Let’s Encrypt, you will use the [ACME API](https://github.com/letsencrypt/boulder/blob/main/docs/acme-divergences.md), most likely through an ACME client like [Certbot](https://certbot.eff.org/). You will need to prove to Let’s Encrypt that you are authorized to revoke the certificate. There are three ways to do this: from the account that issued the certificate, using a different authorized account, or using the certificate private key.

Specifying a reason code
========================

When revoking a certificate, Let’s Encrypt subscribers should select a reason code as follows:

*   No reason provided or `unspecified` (RFC 5280 CRLReason #0) 
    *   When the reason codes below do not apply to the revocation request, the subscriber must not provide a reason code other than “unspecified”.

*   `keyCompromise` (RFC 5280 CRLReason #1) 
    *   The certificate subscriber must choose the “keyCompromise” revocation reason when they have reason to believe that the private key of their certificate has been compromised, e.g. an unauthorized person has had access to the private key of their certificate.
    *   If the revocation request is signed using the Certificate private key, rather than a Subscriber account private key, Let’s Encrypt may ignore the revocation reason in the request and set the reason to “keyCompromise”.

*   `superseded` (RFC 5280 CRLReason #4) 
    *   The certificate subscriber should choose the “superseded” revocation reason when they request a new certificate to replace their existing certificate.

*   `cessationOfOperation` (RFC 5280 CRLReason #5) 
    *   The certificate subscriber should choose the “cessationOfOperation” revocation reason when they no longer own all of the domain names in the certificate or when they will no longer be using the certificate because they are discontinuing their website.
    *   If the revocation request is from a Subscriber account which did not order the certificate in question, but has demonstrated control over all identifiers in the certificate, Let’s Encrypt may ignore the revocation reason in the request and set the reason to “cessationOfOperation”.

Revocation requests that specify any reason code other than those detailed above will be rejected.

From the account that issued the certificate
============================================

If you originally issued the certificate, and you still have control of the account you used to issue it, you can revoke it using your account credentials. Certbot will attempt this by default. Example:

```bash
certbot revoke --cert-path /etc/letsencrypt/archive/${YOUR_DOMAIN}/cert1.pem
```

Using a different authorized account
====================================

If someone issued a certificate after compromising your host or your DNS, you’ll want to revoke that certificate once you regain control. In order to revoke the certificate, Let’s Encrypt will need to ensure that you control the domain names in that certificate (otherwise people could revoke each other’s certificates without permission)!

To validate this control, Let’s Encrypt uses the same methods it uses to validate control for issuance: you can put a [value in a DNS TXT record](https://tools.ietf.org/html/rfc8555#section-8.4) or put a [file on an HTTP server](https://tools.ietf.org/html/rfc8555#section-8.3). Generally, an ACME client will handle these for you. Note that most ACME clients combine validation and issuance, so the only way to ask for validations is to attempt issuance. You can then revoke the resulting certificate if you don’t want it, or simply destroy the private key.

If you want to avoid issuing a certificate at all, you can include a non-existent domain name in your command line, which will cause issuance to fail while still validating the other, existing domain names. Example:

```bash
certbot certonly --manual --preferred-challenges=dns -d ${YOUR_DOMAIN} -d nonexistent.${YOUR_DOMAIN}
```

And follow the instructions, skipping the validation step for `nonexistent.${YOUR_DOMAIN}`. If you’d prefer to validate using HTTP rather than DNS, replace the `--preferred-challenges` flag with `--preferred-challenges=http`. Note that in many cases, the DNS version of these steps will not work if you replace `--manual` with a certbot plugin to fulfill DNS-01 challenges automatically, since certbot will happily place a TXT record at `_acme-challenge.nonexistent.${YOUR_DOMAIN}` if it has the ability to do so.

Once you’ve validated control of all the domain names in the certificate you want to revoke, you can download the certificate from [crt.sh](https://crt.sh/), then proceed to revoke the certificate as if you had issued it:

```bash
certbot revoke --cert-path /PATH/TO/downloaded-cert.pem
```

Using the certificate private key
=================================

If you did not originally issue the certificate, but you have a copy of the corresponding private key, you can revoke by using that private key to sign the revocation request. For instance, if you see that a private key has accidentally been made public, you can use this method to revoke certificates that used that private key, even if you are not the person who originally issued those certificates.

To use this method, you will first need a copy of the private key in PEM format.

Then, if you don’t already have it, download the certificate to be revoked. Let’s Encrypt logs all certificates to [Certificate Transparency](https://www.certificate-transparency.org/) logs, so you can find and download certificates from a log monitor like [crt.sh](https://crt.sh/). Searching for a matching `SubjectPublicKeyInfo` (SPKI) field will find all certificates that use the private key. To extract the SPKI hash from a private key:

```bash
openssl pkey -outform DER -in /PATH/TO/privkey.pem -pubout | openssl sha256
```

Once you have the private key and certificate, you can revoke the certificate like so:

```bash
certbot revoke --cert-path /PATH/TO/cert.pem --key-path /PATH/TO/privkey.pem --reason keyCompromise
```

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
