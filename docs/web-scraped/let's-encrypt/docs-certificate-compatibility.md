# Source: https://letsencrypt.org/docs/certificate-compatibility/

Title: Certificate Compatibility

URL Source: https://letsencrypt.org/docs/certificate-compatibility/

Markdown Content:
Certificate Compatibility - Let's Encrypt
===============

Languages![Image 1](https://letsencrypt.org/images/language-icon128px-black.png)

[English](https://letsencrypt.org/docs/certificate-compatibility/)[Català](https://letsencrypt.org/ca/docs/certificate-compatibility/)[Čeština](https://letsencrypt.org/cs/docs/certificate-compatibility/)[Dansk](https://letsencrypt.org/da/docs/certificate-compatibility/)[Deutsch](https://letsencrypt.org/de/docs/certificate-compatibility/)[Greek](https://letsencrypt.org/el/docs/certificate-compatibility/)[Español](https://letsencrypt.org/es/docs/certificate-compatibility/)[Suomi](https://letsencrypt.org/fi/docs/certificate-compatibility/)[Français](https://letsencrypt.org/fr/docs/certificate-compatibility/)[עברית](https://letsencrypt.org/he/docs/certificate-compatibility/)[Magyar](https://letsencrypt.org/hu/docs/certificate-compatibility/)[Bahasa Indonesia](https://letsencrypt.org/id/docs/certificate-compatibility/)[Italiano](https://letsencrypt.org/it/docs/certificate-compatibility/)[日本語](https://letsencrypt.org/ja/docs/certificate-compatibility/)[한국어](https://letsencrypt.org/ko/docs/certificate-compatibility/)[Polish](https://letsencrypt.org/pl/docs/certificate-compatibility/)[Português do Brasil](https://letsencrypt.org/pt-br/docs/certificate-compatibility/)[Русский](https://letsencrypt.org/ru/docs/certificate-compatibility/)[සිංහල](https://letsencrypt.org/si/docs/certificate-compatibility/)[Srpski](https://letsencrypt.org/sr/docs/certificate-compatibility/)[Svenska](https://letsencrypt.org/sv/docs/certificate-compatibility/)[Tamil](https://letsencrypt.org/ta/docs/certificate-compatibility/)[Thai](https://letsencrypt.org/th/docs/certificate-compatibility/)[Türkçe](https://letsencrypt.org/tr/docs/certificate-compatibility/)[Українська](https://letsencrypt.org/uk/docs/certificate-compatibility/)[Tiếng Việt](https://letsencrypt.org/vi/docs/certificate-compatibility/)[简体中文](https://letsencrypt.org/zh-cn/docs/certificate-compatibility/)[繁體中文](https://letsencrypt.org/zh-tw/docs/certificate-compatibility/)

[Skip navigation links](https://letsencrypt.org/docs/certificate-compatibility/#main-content)

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

Certificate Compatibility
=========================

 Last updated: January 19, 2025 

[See all Documentation](https://letsencrypt.org/docs)

The determining factor for whether a platform can validate Let’s Encrypt certificates is whether that platform trusts ISRG’s “ISRG Root X1” or “ISRG Root X2” certificates. Both of these roots have been included in platform trust stores for several years now (ISRG Root X1 since late 2016, ISRG Root X2 since mid 2022), but it can take much longer for platform updates to be widely installed. Today, trust in ISRG Root X1 is nearly ubiquitous, while trust in ISRG Root X2 is still propagating.

If your certificate validates on some of the “Known Compatible” platforms but not others, the problem may be a web server misconfiguration. If you’re having an issue with modern platforms, the most common cause is failure to provide the correct certificate chain. Test your site with [SSL Labs’ Server Test](https://www.ssllabs.com/ssltest/). If that doesn’t identify the problem, ask for help in our [Community Forums](https://community.letsencrypt.org/).

If your platform is not listed here, we appreciate [pull requests](https://github.com/letsencrypt/website/blob/main/content/en/docs/cert-compat.md) that include documentation of when each root was added to that platform’s trust store.

Platforms that trust ISRG Root X1
=================================

*   Windows >= [XP SP3, Server 2008](https://learn.microsoft.com/en-us/security/trusted-root/participants-list) (unless [Automatic Root Certificate Updates](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc733922%28v=ws.10%29) have been disabled)
*   macOS >= [10.12.1 Sierra](https://support.apple.com/en-us/103425)
*   iOS >= [10](https://support.apple.com/en-us/HT207177)
*   Android >= [7.1.1](https://android.googlesource.com/platform/system/ca-certificates/+/android-7.1.1_r15)
*   Firefox >= [50.0](https://bugzilla.mozilla.org/show_bug.cgi?id=1204656)
*   Ubuntu >= [12.04 Precise Pangolin](https://launchpad.net/ubuntu/+source/ca-certificates/20161102) (with updates applied)
*   Debian >= [8 / Jessie](https://tracker.debian.org/news/812114/accepted-ca-certificates-20161102-source-all-into-unstable/) (with updates applied)
*   RHEL >= 6.10, 7.4 ([with updates applied](https://src.fedoraproject.org/rpms/ca-certificates/c/02204a071d2effe7cdb840c1a2763bcdc396c4be)), 8+
*   Java >= [7u151](https://www.oracle.com/java/technologies/javase/7u151-relnotes.html), [8u141](https://www.oracle.com/java/technologies/javase/8u141-relnotes.html), [9+](https://www.oracle.com/java/technologies/javase/9-all-relnotes.html#JDK-8177539)
*   NSS >= [3.26](https://nss-crypto.org/reference/security/nss/legacy/nss_releases/nss_3.26_release_notes/index.html)
*   Chrome >= [105](https://chromium.googlesource.com/chromium/src/+/main/net/data/ssl/chrome_root_store/faq.md#when-are-these-changes-taking-place) (earlier versions use the operating system trust store)
*   PlayStation >= [PS4 v8.0.0](https://web.archive.org/web/20210306180757/https://www.sie.com/content/dam/corporate/jp/guideline/PS4_Web_Content-Guidelines_e.pdf)

Platforms that trust ISRG Root X2
=================================

*   Windows >= [XP SP3, Server 2008](https://learn.microsoft.com/en-us/security/trusted-root/2021/may2021) (unless [Automatic Root Certificate Updates](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc733922%28v=ws.10%29) have been disabled)
*   macOS >= [13](https://support.apple.com/en-us/103100)
*   iOS >= [16](https://support.apple.com/en-us/103100)
*   Android >= [14](https://android.googlesource.com/platform/system/ca-certificates/+/c8d7f51bbb3de2c40a0d868972be008070eb25d8)
*   Firefox >= [97](https://bugzilla.mozilla.org/show_bug.cgi?id=1701317)
*   Ubuntu >= [18.04 Bionic Beaver](https://launchpad.net/ubuntu/+source/ca-certificates/20230311) (with updates applied)
*   Debian >= [12 / Bookworm](https://tracker.debian.org/news/1426477/accepted-ca-certificates-20230311-source-into-unstable/)
*   RHEL >= 7.9, 8.6, 9.1 ([with updates applied](https://src.fedoraproject.org/rpms/ca-certificates/c/f6b8f45e836dfc9c69585bf7ef0250ad734b086a))
*   Java >= [8u401](https://www.oracle.com/java/technologies/javase/8u401-relnotes.html#JDK-8317374), [11.0.22](https://www.oracle.com/java/technologies/javase/11-0-22-relnotes.html#JDK-8317374), [17.0.10](https://www.oracle.com/java/technologies/javase/17-0-10-relnotes.html#JDK-8317374), [21.0.2](https://www.oracle.com/java/technologies/javase/21-0-2-relnotes.html#JDK-8317374), [22+](https://www.oracle.com/java/technologies/javase/22-relnote-issues.html#JDK-8317374)
*   NSS >= [3.74](https://firefox-source-docs.mozilla.org/security/nss/releases/nss_3_74.html)
*   Chrome >= [105](https://chromium.googlesource.com/chromium/src/+/main/net/data/ssl/chrome_root_store/faq.md#when-are-these-changes-taking-place) (earlier versions use the operating system trust store)

In addition, all platforms which trust ISRG Root X1 also trust the [cross-signed version of ISRG Root X2](https://letsencrypt.org/certificates/#root-cas).

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
