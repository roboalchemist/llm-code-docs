# Source: https://letsencrypt.org/docs/allow-port-80/

Title: Best Practice - Keep Port 80 Open

URL Source: https://letsencrypt.org/docs/allow-port-80/

Markdown Content:
Best Practice - Keep Port 80 Open - Let's Encrypt
===============

Languages![Image 1](https://letsencrypt.org/images/language-icon128px-black.png)

[English](https://letsencrypt.org/docs/allow-port-80/)[Català](https://letsencrypt.org/ca/docs/allow-port-80/)[Čeština](https://letsencrypt.org/cs/docs/allow-port-80/)[Dansk](https://letsencrypt.org/da/docs/allow-port-80/)[Deutsch](https://letsencrypt.org/de/docs/allow-port-80/)[Greek](https://letsencrypt.org/el/docs/allow-port-80/)[Español](https://letsencrypt.org/es/docs/allow-port-80/)[Suomi](https://letsencrypt.org/fi/docs/allow-port-80/)[Français](https://letsencrypt.org/fr/docs/1/)[עברית](https://letsencrypt.org/he/docs/allow-port-80/)[Magyar](https://letsencrypt.org/hu/docs/allow-port-80/)[Bahasa Indonesia](https://letsencrypt.org/id/docs/allow-port-80/)[Italiano](https://letsencrypt.org/it/docs/allow-port-80/)[日本語](https://letsencrypt.org/ja/docs/allow-port-80/)[한국어](https://letsencrypt.org/ko/docs/allow-port-80/)[Polish](https://letsencrypt.org/pl/docs/allow-port-80/)[Português do Brasil](https://letsencrypt.org/pt-br/docs/allow-port-80/)[Русский](https://letsencrypt.org/ru/docs/allow-port-80/)[සිංහල](https://letsencrypt.org/si/docs/allow-port-80/)[Srpski](https://letsencrypt.org/sr/docs/allow-port-80/)[Svenska](https://letsencrypt.org/sv/docs/allow-port-80/)[Tamil](https://letsencrypt.org/ta/docs/allow-port-80/)[Thai](https://letsencrypt.org/th/docs/allow-port-80/)[Türkçe](https://letsencrypt.org/tr/docs/allow-port-80/)[Українська](https://letsencrypt.org/uk/docs/allow-port-80/)[Tiếng Việt](https://letsencrypt.org/vi/docs/allow-port-80/)[简体中文](https://letsencrypt.org/zh-cn/docs/allow-port-80/)[繁體中文](https://letsencrypt.org/zh-tw/docs/allow-port-80/)

[Skip navigation links](https://letsencrypt.org/docs/allow-port-80/#main-content)

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

Best Practice - Keep Port 80 Open
=================================

 Last updated: January 24, 2019 

[See all Documentation](https://letsencrypt.org/docs)

We occasionally get reports from people who have trouble using the HTTP-01 challenge type because they’ve firewalled off port 80 to their web server. Our recommendation is that all servers meant for general web use should offer both HTTP on port 80 and HTTPS on port 443. They should also send redirects for all port 80 requests, and possibly an HSTS header (on port 443 requests).

Allowing port 80 doesn’t introduce a larger attack surface on your server, because requests on port 80 are generally served by the same software that runs on port 443.

Closing port 80 doesn’t reduce the risk to a person who accidentally visits your website via HTTP. In normal circumstances, that person would receive a redirect to HTTPS, and their subsequent traffic will be protected. If that person was subject to an active MITM, the MITM would answer on port 80, so your site would never have a chance to answer “connection refused.”

Lastly, keeping port 80 open in order to serve a redirect helps get people to the right version of your site (the HTTPS version). There are various situations beyond your control that might briefly land someone on the HTTP version of your site - for instance, automatic linkification in emails, or manually typing a domain name. It’s better for them to get a redirect than an error.

Unfortunately, you might not have control over whether port 80 is blocked for your site. Some (mostly residential) ISPs block port 80 for various reasons. If your ISP does this but you’d still like to get certificates from Let’s Encrypt, you have two options: You can use DNS-01 challenges or you can use [one of the clients that supports TLS-ALPN-01 challenges](https://community.letsencrypt.org/t/which-client-support-tls-alpn-challenge/75859/2) (on port 443).

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
