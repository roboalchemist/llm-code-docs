# Source: https://www.iredmail.org/ee.html

Title: iRedMail Enterprise Edition

URL Source: https://www.iredmail.org/ee.html

Markdown Content:
iRedMail Enterprise Edition
===============

[](https://www.iredmail.org/ee.html#)

*   [Products](https://www.iredmail.org/ee.html#)
    *   [**iRedMail Enterprise Edition (Recommend)** One Single Binary. One-Click Upgrade. On-Premises.](https://www.iredmail.org/ee.html)
    *   [**iRedMail** Downloadable Installer, Open Source.](https://www.iredmail.org/index.html)
    *   [**iRedAdmin-Pro** Full-featured Web Admin Panel](https://www.iredmail.org/admin_panel.html)
    *   [**Spider Email Archiver** Lightweight, Performant Email Archiving Software, developed by iRedMail team.](https://spiderd.io/)

*   [Download](https://www.iredmail.org/download.html)
*   [Support](https://www.iredmail.org/support.html)
*   [Contact](https://www.iredmail.org/contact.html)
*   [Document](https://docs.iredmail.org/index.html)

[![Image 1](https://www.iredmail.org/assets/images/logo-iredmail.png)](https://www.iredmail.org/index.html)

*   [Products](https://www.iredmail.org/ee.html#)
    *   [**iRedMail Enterprise Edition (Recommend)** One Single Binary. One-Click Upgrade. On-Premises.](https://www.iredmail.org/ee.html)
    *   [**iRedMail** Downloadable Installer, Open Source.](https://www.iredmail.org/index.html)
    *   [**iRedAdmin-Pro** Full-featured Web Admin Panel](https://www.iredmail.org/admin_panel.html)
    *   [**Spider Email Archiver** Lightweight, Performant Email Archiving Software, developed by iRedMail team.](https://spiderd.io/)

*   [Download](https://www.iredmail.org/download.html)
*   [Support](https://www.iredmail.org/support.html)
*   [Contact](https://www.iredmail.org/contact.html)
*   [Document](https://docs.iredmail.org/index.html)

iRedMail Enterprise Edition (EE)
================================

### _It replaces and beyonds the iRedMail + iRedAdmin-Pro + iRedMail Easy.

[Comparison](https://www.iredmail.org/ee.html#comparison)_

[Pricing Per mailbox, or per server](https://www.iredmail.org/ee.html#pricing)[Getting Started**v1.6.1 (Jan 16, 2026)**](https://docs.iredmail.org/install.ee.html)
### _One Single Binary._

_One-Click Upgrade._

_On-Premises._

_All data on your own server._

[**Linux (amd64)**](https://dl.iredmail.org/ee/iredmail-enterprise-latest-linux-amd64)[**Linux (arm64)**](https://dl.iredmail.org/ee/iredmail-enterprise-latest-linux-arm64)[**OpenBSD (amd64)**](https://dl.iredmail.org/ee/iredmail-enterprise-latest-openbsd-amd64)[**OpenBSD (arm64)**](https://dl.iredmail.org/ee/iredmail-enterprise-latest-openbsd-arm64)[**Docker**](https://hub.docker.com/r/iredmail/ee)

### Fearless One-Click Upgrade

Easily keep the email server up to date. [Tutorial](https://docs.iredmail.org/upgrade.ee.html)

### Microsoft Active Directory

Replicate user / group accounts from Microsoft Active Directory as mail accounts. [Tutorial](https://docs.iredmail.org/ee.ad.html)

### Domain-Level Admins

Either promote a mail user to domain admin role, or create a separated domain admin account to manage his/her own mail domains.

### Self-Service

Allow users to login to manage their own preferences like password, mail forwarding, white/blacklists, quarantined mails, basic spam policy.

### HTTP Push Notification

When new email arrives, send the basic info of new message to your http endpoint.

### Throttling

Global, per-domain and per-user throttling based on: max size of single message, number of max inbound/outbound messages per time unit.

### Two-Factor Authentication

Based on TOTP (Time-based One-Time Password).

### Firewall Rules Management

Simple web UI to manage firewall rules.

### Antispam

Manage greylisting, whitelists, blacklists, spam policy, quarantined emails. You can even whitelist or blacklist sender/recipient in quarantined mails with one click.

### DKIM Key Management

Manage per-domain and catch-all DKIM keys on web UI. Keys are stored in SQL database.

### Searching

Search accounts with domain name, email address, display name. You can also manage searched accounts in search result page, such as enable/disable/delete account.

### Log Admin Activities

Logs normal admin activities, such as account creation, activation, removal, password change, and more.

### Multi-language Support

English, Español, German, Thai and Chinese are available for now.

### Testimonials

#### What People Said

EE delivers a robust, enterprise-grade self-hosted email solution with seamless one-click deployment and upgrades. The upgrade path from earlier versions is well documented and straightforward, ensuring minimal downtime. It offers strong security features like two-factor authentication, fail2ban integration, automated Let's Encrypt SSL, and per-user spam controls, along with efficient management of multiple domains and dedicated domain admins. The centralized web interface simplify operations.

**Robert S. (Kuakawa Solutions)**, Dec 26, 2025 

Comparison: iRedMail (shell-based installer) vs iRedMail Enterprise Edition
---------------------------------------------------------------------------

| Feature | iRedMail | iRedMail Enterprise Edition |
| --- | --- | --- |
| Web-based installer with i18n support | Shell and terminal based installer |  |
| Initial Deployment |  |  |
| Re-perform full deployment after initial installation Useful for re-generating config files to match new software versions after OS upgrade. |  |  |
| Fearless one-click upgrade to keep server up to date | Follow [upgrade tutorials](https://docs.iredmail.org/iredmail.releases.html) and apply the changes manually |  |
| Install components after initial installation |  |  |
| Remove installed components after initial installation |  |  |
| Reinstall, redeploy / re-config installed components after initial installation |  |  |
| Remote MySQL or MariaDB backend Use a remote MySQL or MariaDB server as backend database for storing mail accounts and application data. [Tutorial](https://docs.iredmail.org/ee.remote.mysql.html) |  |  |
| MariaDB and PostgreSQL backends Install MariaDB or PostgreSQL server locally for storing mail accounts and application data. |  |  |
| OpenLDAP backend |  |  |
| Supports CentOS, Rocky Linux, AlmaLinux |  |  |
| Supports Debian, Ubuntu |  |  |
| Supports OpenBSD |  |  |
| Supports FreeBSD |  |  |
| License | GPL v3 | Commercial |

Comparison: iRedAdmin-Pro vs iRedMail Enterprise Edition
--------------------------------------------------------

| Feature | iRedAdmin-Pro | iRedMail Enterprise Edition |
| --- | --- | --- |
| Unlimited Mailboxes With per-domain and per-user mailbox quota control |  | Priced per-mailbox, or per-server. [Pricing](https://www.iredmail.org/ee.html#pricing) |
| Unlimited Mail Domains Host as many mail domains as you want |  |  |
| Unlimited Mailing List/Aliases Manage members, access policies, etc |  |  |
| Unlimited Domain-Level Admins Either promote a mail user to domain admin role, or create a separated domain admin account |  |  |
| Advanced Domain Management Domain-level mailbox quota, limit numbers of user/list/alias accounts, Relay, BCC, Alias Domain, Catch-all, Backup MX, user password length and complexity control |  |  |
| Advanced User Management Per-user BCC, Relay, Mail Forwarding, Alias Addresses, Rename email address, restrict login IP/network |  |  |
| Per-Domain and Per-User Anti-Spam Settings Throttling, Greylisting, Spam Policy |  |  |
| Self-Service Allow end user to manage their own preferences: Password, Mail Forwarding, Whitelists, Blacklists, Quarantined Mails, Spam Policy |  |  |
| Service Control One click to enable/disable mail services for mail user: POP3, IMAP, SMTP, Sieve filter, Mail Forwarding, BCC, and more. |  |  |
| Spam/Virus Quarantining Quarantine detected SPAM/Virus into SQL database for later management (delete, release, whitelist, blacklist) |  |  |
| View basic info of all sent and received emails Sender, Recipient, Subject, Spam Score, Size, Date |  |  |
| RESTful API Interface | [API Document](https://docs.iredmail.org/iredadmin-pro.restful.api.html) | [API Document](https://www.iredmail.org/ee/api/index.html)Also embedded in the executable program. |
| Greylisting |  |  |
| Throttling Based on: max size of single email, number of max inbound/outbound emails, cumulative size of all inbound/outbound emails |  |  |
| Whitelisting, Blacklisting Based on: IP addresses/networks, Sender address, Sender domain name |  |  |
| Searching Account Searching with display name or email address, domain name |  |  |
| Log Admin Activities Account creation, activation, removal, password change, and more. |  |  |
| Fail2ban Integration View info of banned IP address (Country/City, reverse DNS name), log lines which triggerred the ban (easy to troubleshoot why the ban happened), and unban it with one click |  |  |
| Track user last login date View the time of user last login via IMAP and POP3 services, also the time of last (locally) delivered email |  |  |
| Set isolation level of spam/ham auto-learning bayes data Per-user, per-domain or server wide. |  |  |
| HTTP Push Notification When new email arrives, send the basic info of new message to your http endpoint. |  |  |
| Firewall rules management |  |  |
| Two-Factor Authentication (2FA) |  |  |
| Recover Password Allow end users to reset password with a secondary email. |  |  |
| Builtin Autoconfig and AutoDiscover support Helps end user to setup the mail account when configure mail client. |  |  |
| SSL certificate management Request free SSL cert from Let's Encrypt with one click, up to 100 domain names. Renew automatically. |  |  |
| DKIM Key Management Manage per-domain and catch-all DKIM keys on web UI. Keys are stored in SQL databse. |  |  |
| New milter program Filter spam/virus and modify mails on the fly. |  |  |
| View mail related DNS records with one click A, MX, DKIM, SPF, DMARC, autoconfig, autodiscover, XMPP. Also, server hostname, PTR. |  |  |
| License | Commercial | Commercial |

Comparison: iRedMail Easy platform vs iRedMail Enterprise Edition
-----------------------------------------------------------------

| Feature | iRedMail Easy Platform | iRedMail Enterprise Edition |
| --- | --- | --- |
| On-Premises | Runs on cloud server, connects to your server via ssh |  |
| Deployment speed | Slow (Ansible with remote ssh) | At least 10 times faster. Deploy locally with Ansible-like tool (written in Golang). |
| Web-based installation wizard |  |  |
| Deploy with few clicks on web UI |  |  |
| Fearless one-click upgrade |  |  |
| Rich configurations |  |  |

Pricing (Perpetual License)
---------------------------

Your purchase or use of our products implies that you have read and accepted [License Agreements](https://www.iredmail.org/ee.html#LA) below.

### $15 / mailbox / year

*   Buy specific number of mailboxes

Minimal 10 mailboxes, buy more anytime.

Upgrade to per-server license anytime by just paying the rest instead of full price.
*   Unlimited mail domains, mailing lists
*   Deploy on ONE server
*   Annual renew fee: 40% of initial purchase
*    Purchase or request free trial license

[Sign up / login](https://store.iredmail.org/)

### $3000 / server / year

*   Unlimited mailboxes
*   Unlimited mail domains, mailing lists
*   Deploy on ONE server
*   Annual renew fee: $1200
*    Purchase or request free trial license

[Sign up / login](https://store.iredmail.org/)

*   Need bank wire transfer? [Contact us](https://www.iredmail.org/contact.html) to get pro forma invoice and/or final invoice.
*   iRedMail Enterprise Edition works with MySQL, MariaDB, PostgreSQL and OpenLDAP. NOT Microsoft Active Directory or other LDAP servers.
*   Tech support included.

### License Agreement

*   One license per server.
*   It's perpetual license. After license expired, customer can continue running purchased license and all features remain the same, but no more technical support and software updates.
*   After license expired, customer has to purchase a new license to get the latest release.
*   iRedMail team reserves the right to change the terms of iRedMail Enterprise Edition at any time without notifying customers.

© 2025 **iRedMail**
