# Source: https://docs.iredmail.org/

Title: iRedMail Documentations

URL Source: https://docs.iredmail.org/

Published Time: Mon, 09 Mar 2026 09:11:13 GMT

Markdown Content:
iRedMail Documentations
===============

[![Image 1: iRedMail web site](https://docs.iredmail.org/images/logo-iredmail.png)iRedMail](https://www.iredmail.org/)

Some tutorials have been translated to different languages. [Help translate more](https://github.com/iredmail/docs)

[Italiano](https://docs.iredmail.org/index-it_IT.html) / [Nederlands](https://docs.iredmail.org/index-nl_DU.html) / [简体中文](https://docs.iredmail.org/index-zh_CN.html) /

Attention

Check out the lightweight on-premises email archiving software developed by iRedMail team: [Spider Email Archiver](https://spiderd.io/).

### Overview

*   [Why build your own mail server instead of outsourcing to external entities](https://docs.iredmail.org/why.build.your.own.mail.server.html)
*   [Major open source software used in iRedMail, and big picture of mail flow](https://docs.iredmail.org/used.components.html)
*   [Which network ports are open by iRedMail](https://docs.iredmail.org/network.ports.html)

### iRedMail (Open Source Edition)

Attention

We recommend [iRedMail Enterprise Edition](https://docs.iredmail.org/#ee) instead of iRedMail open source edition.

*   Install iRedMail (with downloadable installer) on:
    *   [Red Hat Enterprise Linux, CentOS](https://docs.iredmail.org/install.iredmail.on.rhel.html)
    *   [Debian, Ubuntu](https://docs.iredmail.org/install.iredmail.on.debian.ubuntu.html)
    *   [FreeBSD (without Jail)](https://docs.iredmail.org/install.iredmail.on.freebsd.html), [FreeBSD with Jail (ezjail)](https://docs.iredmail.org/install.iredmail.on.freebsd.with.jail.html)
    *   [OpenBSD](https://docs.iredmail.org/install.iredmail.on.openbsd.html)

*   After installation:
    *   [Setup DNS records for your iRedMail server (A, PTR, MX, SPF, DKIM, DMARC)](https://docs.iredmail.org/setup.dns.html)

*   Additional installation tips
    *   [Install iRedMail with a remote MySQL server](https://docs.iredmail.org/install.iredmail.with.remote.mysql.server.html)
    *   [Perform silent/unattended iRedMail installation](https://docs.iredmail.org/unattended.iredmail.installation.html)

*   [Performance tuning for a busy server](https://docs.iredmail.org/performance.tuning.html)

### **iRedMail Enterprise Edition (EE)**

Attention

[Features and comparison](https://www.iredmail.org/ee.html)

*   [Install EE](https://docs.iredmail.org/install.ee.html)
    *   [Use a Remote MySQL/MariaDB server as backend database](https://docs.iredmail.org/ee.remote.mysql.html)

*   [Upgrade EE](https://docs.iredmail.org/upgrade.ee.html)
*   [Best Practice](https://docs.iredmail.org/ee.best.practice.html)
*   [ChangeLog](https://docs.iredmail.org/ee.changelog.html)
*   [Translate EE to your local language](https://docs.iredmail.org/ee.translation.html)
*   [SSL certificate management](https://docs.iredmail.org/ee.cert.html)
*   [Replicate mail accounts from Microsoft Active Directory](https://docs.iredmail.org/ee.ad.html)
*   [Disable 2FA (TOTP) for account](https://docs.iredmail.org/ee.disable.2fa.html)
*   Migration:
    *   [Migrate from iRedMail Easy](https://docs.iredmail.org/easy.to.ee.html)
    *   [Migrate from iRedMail](https://docs.iredmail.org/iredmail.to.ee.html)

### Configure mail client applications

Quick MUA Settings

*   Login username of SMTP/POP3/IMAP services must be full email address.
*   POP3 service: port 110 over STARTTLS, or port 995 with SSL.
*   IMAP service: port 143 over STARTTLS, or port 993 with SSL.
*   SMTP service: port 587 over STARTTLS, or port 465 with SSL.
*   CalDAV and CardDAV server addresses: `https://<server>/SOGo/dav/<full email address>`

*   [Exchange ActiveSync: Setup Android devices](https://docs.iredmail.org/activesync.android.html)
*   [Exchange ActiveSync: Setup BlackBerry 10 devices](https://docs.iredmail.org/activesync.bb10.html)
*   [Exchange ActiveSync: Setup iOS devices](https://docs.iredmail.org/activesync.ios.html)
*   [Exchange ActiveSync: Setup Outlook 2013 for Windows](https://docs.iredmail.org/activesync.outlook.html)
*   [Setup Thunderbird: POP3/IMAP, SMTP and global ldap address book](https://docs.iredmail.org/configure.thunderbird.html)
*   [Setup Thunderbird: SOGo Address Book and Calendar synchronization with CardDAV and CalDAV](https://docs.iredmail.org/thunderbird.sogo.html)
*   [Mac OS X: Add contact service (CardDAV) in Contacts.app](https://docs.iredmail.org/sogo.macosx.contacts.html)
*   [Mac OS X: Add calendar (CalDAV) and task (Reminders) service in iCalendar.app](https://docs.iredmail.org/sogo.macosx.icalendar.html)

### Release notes and upgrade tutorials

*   [iRedMail release notes and upgrade tutorials](https://docs.iredmail.org/iredmail.releases.html)
*   [iRedAdmin-Pro (web-based admin panel) release notes and upgrade tutorials](https://docs.iredmail.org/iredadmin-pro.releases.html)
*   [iRedAPD (Postfix Access Policy Daemon) release notes and upgrade tutorials](https://docs.iredmail.org/iredapd.releases.html)
*   [mlmmjadmin upgrade tutorial (RESTful API server used to manage mlmmj mailing list)](https://docs.iredmail.org/upgrade.mlmmjadmin.html)
*   [Upgrade milter manually](https://docs.iredmail.org/upgrade.milter.html)

### **iRedMail Easy** - Web-based Deployment, Upgrade and Tech Support Platform

Warning

iRedMail Easy platform will be discontinued on Jan 25, 2026. [Get a FREE iRedMail Enterprise Edition license and migrate.](https://forum.iredmail.org/topic20762.html)

*   [iRedMail Easy: Getting started](https://docs.iredmail.org/iredmail-easy.getting.start.html)
*   [iRedMail Easy: Best Practice](https://docs.iredmail.org/iredmail-easy.best.practice.html)
*   [iRedMail Easy: FAQ](https://docs.iredmail.org/iredmail-easy.faq.html)
*   [iRedMail Easy: Release Notes](https://docs.iredmail.org/iredmail-easy.release.notes.html)
*   [iRedMail Easy: Request a free cert from Let's Encrypt](https://docs.iredmail.org/letsencrypt-easy.html)
*   [iRedMail Easy: How to cancel your subscription](https://docs.iredmail.org/iredmail-easy.unsubscribe.html)
*   [iRedMail Easy: Setup DNS records for autoconfig and autodiscover](https://docs.iredmail.org/iredmail-easy.autoconfig.autodiscover.html)
*   [iRedMail Easy: Setup sudo for deployment](https://docs.iredmail.org/iredmail-easy.setup.sudo.html)
*   [iRedMail Easy: What is SSH jump server](https://docs.iredmail.org/iredmail-easy.what.is.ssh.jump.server.html)

### Migrations

*   [Migrate old iRedMail server to the latest stable release](https://docs.iredmail.org/migrate.to.new.iredmail.server.html)
*   [Password hashes](https://docs.iredmail.org/password.hashes.html)

### How to

*   [Allow certain users to send email as another user](https://docs.iredmail.org/allow.certain.users.to.send.email.as.different.user.html)
*   [Change mail attachment size](https://docs.iredmail.org/change.mail.attachment.size.html)
*   [Completely disable Amavisd + ClamAV + SpamAssassin](https://docs.iredmail.org/completely.disable.amavisd.clamav.spamassassin.html)
*   [Enable SMTP SASL AUTH on port 25](https://docs.iredmail.org/enable.smtp.auth.on.port.25.html)
*   [Enable SMTPS service (SMTP over SSL, port 465)](https://docs.iredmail.org/enable.smtps.html)
*   [Disable spam virus scanning for outgoing mails](https://docs.iredmail.org/disable.spam.virus.scanning.for.outgoing.mails.html)
*   [Amavisd + SpamAssassin not working? no mail header (X-Spam-*) inserted](https://docs.iredmail.org/no.x-spam.headers.html)
*   [Quarantining](https://docs.iredmail.org/quarantining.html)
*   [Sign DKIM signature on outgoing emails for new mail domain](https://docs.iredmail.org/sign.dkim.signature.for.new.domain.html)
*   [Allow insecure POP3/IMAP/SMTP connections without STARTTLS](https://docs.iredmail.org/allow.insecure.pop3.imap.smtp.connections.html)
*   [Allow internal network devices to send email with insecure connection](https://docs.iredmail.org/additional.smtp.port.html)
*   [Allow member to send email as mailing list or mail alias](https://docs.iredmail.org/allow.member.to.send.email.as.mail.list.html)
*   [Allow some user to send email without smtp authentication](https://docs.iredmail.org/allow.send.without.smtp.auth.html)
*   [Amavisd: Enable per-recipient policy lookup](https://docs.iredmail.org/amavisd.per-recipient.policy.lookup.html)
*   [Authenticate without domain part in email address](https://docs.iredmail.org/authenticate.without.domain.name.html)
*   [How to mark a mail domain as backup MX](https://docs.iredmail.org/backupmx.html)
*   [Change per-user mailbox format (e.g. maildir, mdbox)](https://docs.iredmail.org/change.mailbox.format.html)
*   [Change server hostname](https://docs.iredmail.org/change.server.hostname.html)
*   [Process more (or less) emails concurrently](https://docs.iredmail.org/concurrent.processing.html)
*   [Auto learn spam/ham with Dovecot `imap_sieve` plugin](https://docs.iredmail.org/dovecot.imapsieve.html)
*   [Dovecot Master User: Access user's mailbox without owner's password.](https://docs.iredmail.org/dovecot.master.user.html)
*   [Enable DNSBL service in Postfix to reduce spam](https://docs.iredmail.org/enable.dnsbl.html)
*   [Enable postscreen service](https://docs.iredmail.org/enable.postscreen.html)
*   [Fail2ban: Store banned IP addresses in SQL database](https://docs.iredmail.org/fail2ban.sql.html)
*   [Force mail user to change password in 90 days](https://docs.iredmail.org/force.user.to.change.password.html)
*   [Ignore Trash folder in mailbox quota](https://docs.iredmail.org/ignore.trash.folder.in.quota.html)
*   [LDAP: Add an alias domain](https://docs.iredmail.org/ldap.add.alias.domain.html)
*   [LDAP: Add per-domain catch-all account](https://docs.iredmail.org/ldap.add.catch-all.html)
*   [LDAP: Add a mail alias account](https://docs.iredmail.org/ldap.add.mail.alias.html)
*   [LDAP: Add a (unsubscribeable) mailing list](https://docs.iredmail.org/ldap.add.mail.list.html)
*   [LDAP: Bulk create mail users](https://docs.iredmail.org/ldap.bulk.create.mail.users.html)
*   [How to allow external access to OpenLDAP service](https://docs.iredmail.org/ldap.external.access.html)
*   [LDAP: User mail forwarding](https://docs.iredmail.org/ldap.user.mail.forwarding.html)
*   [Request a free cert from Let's Encrypt (for servers deployed with downloadable iRedMail installer)](https://docs.iredmail.org/letsencrypt.html)
*   [Mailbox sharing (Sharing IMAP folder with other users)](https://docs.iredmail.org/mailbox.sharing.html)
*   [Manage iRedAPD (white/blacklists, greylisting, throttling and more)](https://docs.iredmail.org/manage.iredapd.html)
*   [Manage subscribeable mailing lists](https://docs.iredmail.org/manage.subscribeable.mailing.lists.html)
*   [Monitor incoming and outgoing mails with BCC](https://docs.iredmail.org/monitor.incoming.and.outgoing.mails.with.bcc.html)
*   [Move detected spam to Junk folder](https://docs.iredmail.org/move.detected.spam.to.junk.folder.html)
*   [Per-domain or per-user transport (relay)](https://docs.iredmail.org/per-account.transport.html)
*   [Pipe incoming email for certain user to external script](https://docs.iredmail.org/pipe.incoming.email.for.certain.user.to.external.script.html)
*   [Promote a mail user to be global admin](https://docs.iredmail.org/promote.user.to.be.global.admin.html)
*   [How to create and manage public folder](https://docs.iredmail.org/public.folder.html)
*   [Force Dovecot to recalculate mailbox quota](https://docs.iredmail.org/recalculate.mailbox.quota.html)
*   [Setup relayhost](https://docs.iredmail.org/relayhost.html)
*   [Reset user password](https://docs.iredmail.org/reset.user.password.html)
*   [Restrict mail user to login from specified IP addresses or networks](https://docs.iredmail.org/restrict.mail.user.to.login.from.specified.ip.or.networks.html)
*   [Send out email from specified IP address](https://docs.iredmail.org/send.out.email.from.specified.ip.addresses.html)
*   [Sign disclaimer on outgoing mails](https://docs.iredmail.org/sign.disclaimer.html)
*   [SOGo: per-user free/busy availability](https://docs.iredmail.org/sogo.free.busy.html)
*   [SOGo: Manage resources](https://docs.iredmail.org/sogo.manage.resources.html)
*   [SQL: Add an alias domain](https://docs.iredmail.org/sql.add.alias.domain.html)
*   [SQL: Add per-domain catch-all account](https://docs.iredmail.org/sql.create.catch-all.html)
*   [SQL: Add a mail alias account](https://docs.iredmail.org/sql.create.mail.alias.html)
*   [SQL: Create new mail user](https://docs.iredmail.org/sql.create.mail.user.html)
*   [SQL: User mail forwarding](https://docs.iredmail.org/sql.user.mail.forwarding.html)
*   [Enable SRS (Sender Rewriting Scheme) support](https://docs.iredmail.org/srs.html)
*   [Store SpamAssassin bayes in SQL](https://docs.iredmail.org/store.spamassassin.bayes.in.sql.html)
*   [Run web applications under subdomain with Nginx](https://docs.iredmail.org/subdomain.web.apps.html)
*   [Track user last login time](https://docs.iredmail.org/track.user.last.login.html)
*   [Fixes you need after upgrading Debian from 10 to 11](https://docs.iredmail.org/upgrade.debian.10-11.html)
*   [Fixes you need after upgrading Debian from 11 to 12](https://docs.iredmail.org/upgrade.debian.11-12.html)
*   [Upgrade Debian from 12 (bookworm) to 13 (trixie), for iRedMail Enterprise Edition.](https://docs.iredmail.org/upgrade.debian.12-13.ee.html)
*   [Fixes you need after upgrading Debian from 12 to 13 (trixie)](https://docs.iredmail.org/upgrade.debian.12-13.html)
*   [Fixes you need after upgrading Debian from 8 to 9](https://docs.iredmail.org/upgrade.debian.8-9.html)
*   [Fixes you need after upgrading Debian from 9 to 10](https://docs.iredmail.org/upgrade.debian.9-10.html)
*   [Upgrade Dovecot from 2.2.x to 2.3.x](https://docs.iredmail.org/upgrade.dovecot.2.2-2.3.html)
*   [How to upgrade netdata](https://docs.iredmail.org/upgrade.netdata.html)
*   [Upgrade php to v8.0 on CentOS Stream / Rocky / AlmaLinux 8](https://docs.iredmail.org/upgrade.php.v8.0.on.centos.8.html)
*   [Upgrade SOGo from v4 to v5](https://docs.iredmail.org/upgrade.sogo.4.to.5.html)
*   [Fixes you need after upgrading Ubuntu from 14.04 to 16.04](https://docs.iredmail.org/upgrade.ubuntu.14.04-16.04.html)
*   [Upgrade Ubuntu from 18.04 to 20.04](https://docs.iredmail.org/upgrade.ubuntu.18.04-20.04.html)
*   [Upgrade Ubuntu from 22.04 to 24.04](https://docs.iredmail.org/upgrade.ubuntu.22.04-24.04.html)
*   [Use a bought SSL certificate](https://docs.iredmail.org/use.a.bought.ssl.certificate.html)
*   [Use OpenLDAP as address book in Microsoft Outlook](https://docs.iredmail.org/use.openldap.as.address.book.in.outlook.html)
*   [Per-user alias address](https://docs.iredmail.org/user.alias.address.html)
*   [Webmail customization](https://docs.iredmail.org/webmail.customization.html)

Documents contributed by iRedMail users:

*   [Anti-spam with Dovecot antispam plugin and SpamAssassin](https://forum.iredmail.org/topic8169-iredmail-support-antispam-via-dovecot-and-spamassassin.html), contributed by Dexus.

### Third-party integrations

Below tutorials are maintained by iRedMail project.

*   [Integrate Microsoft Active Directory for user authentication and address book](https://docs.iredmail.org/active.directory.html)

*   [](https://docs.iredmail.org/)Integrate mlmmj mailing list manager (mlmmj is a required core component since iRedMail-0.9.8):

    *   [For LDAP backends](https://docs.iredmail.org/integration.mlmmj.ldap.html)
    *   [For MySQL/MariaDB backend](https://docs.iredmail.org/integration.mlmmj.mysql.html)
    *   [For PostgreSQL backend](https://docs.iredmail.org/integration.mlmmj.pgsql.html)

*   [](https://docs.iredmail.org/)Integrate netdata monitor (netdata is an optional component since iRedMail-0.9.8):

    *   [For Linux](https://docs.iredmail.org/integration.netdata.linux.html)
    *   [For FreeBSD](https://docs.iredmail.org/integration.netdata.freebsd.html)
    *   netdata doesn't work on OpenBSD (yet).

*   Install SOGo groupware on:

    *   CentOS 6: [MySQL](https://docs.iredmail.org/sogo-centos-6-mysql.html), [OpenLDAP](https://docs.iredmail.org/sogo-centos-6-openldap.html).

Documents contributed by iRedMail users:

*   [Integreate OpenFire in iRedMail (MySQL backend)](http://www.murat.ws/openfire-iredmail-yapilandirmasi/) (Turkish)
*   [Enabling Apache Solr 4.10 (using jetty) with Dovecot 2.2 for fulltext search results on Centos 6 (iRedMail compatible)](https://extremeshok.com/6622/enabling-apache-solr-4-10-using-jetty-with-dovecot-2-2-for-fulltext-search-results-on-centos-6-iredmail-compatible/)
*   [Install iRedMail and Mailman on Debian Squeeze](http://www.howtoforge.com/installing-iredmail-and-mailman-on-debian-squeeze). Howtoforge tutorial, contributed by Jason Norwood-Young.
*   [Integrate DBMail in iRedMail (MySQL backend), CentOS](https://docs.iredmail.org/dbmail.mysql.centos.html)
*   [High-Availability Maildir Storage With GlusterFS + CentOS 5.x](https://forum.iredmail.org/topic2147-highavailability-maildir-storage-with-glusterfs-centos-5x.html), contributed by Basem Hegazy. 2011-06-26
*   [Integrate OpenVPN in iRedMail with OpenLDAP](https://www.howtoforge.com/using-iredmail-and-openvpn-for-virtual-email-hosting-and-vpn-services-centos-5.4), Howtoforge tutorial.
*   [Integrate Ejabberd in iRedMail with OpenLDAP](https://docs.iredmail.org/ejabberd.openldap.ubuntu.html)

### Cluster

Documents contributed by iRedMail users:

*   [Build an iRedMail fail-over Cluster with KeepAlived, HAProxy, GlusterFS, OpenLDAP, Mariadb](https://docs.iredmail.org/haproxy.keepalived.glusterfs.html), contributed by Setyo Prayitno
*   [An Ultra-HA, full Mult-Master E-mail cluster with iRedMail, MariaDB, and IPVS](http://pastebin.com/JcYeQBrX), contributed by Joshua Boniface.

### iRedAdmin-Pro

*   [iRedAdmin-Pro: Custom (Amavisd) ban rules](https://docs.iredmail.org/iredadmin-pro.custom.ban.rules.html)
*   [iRedAdmin-Pro: Custom base url (/iredadmin)](https://docs.iredmail.org/iredadmin-pro.custom.base.url.html)
*   [iRedAdmin-Pro: Custom logo image, brand name, short product description](https://docs.iredmail.org/iredadmin-pro.custom.logo.html)
*   [iRedAdmin-Pro (LDAP backend): Add and manage custom services for mail user](https://docs.iredmail.org/iredadmin-pro.custom.user.services.html)
*   [iRedAdmin-Pro: Customize maildir path](https://docs.iredmail.org/iredadmin-pro.customize.maildir.path.html)
*   [iRedAdmin-Pro: Default password restrictions](https://docs.iredmail.org/iredadmin-pro.default.password.policy.html)
*   [iRedAdmin-Pro: Domain ownership verification](https://docs.iredmail.org/iredadmin-pro.domain.ownership.verification.html)
*   [iRedAdmin-Pro: RESTful API](https://docs.iredmail.org/iredadmin-pro.restful.api.html)
*   [iRedAdmin-Pro: Enable self-service to allow users to manage their own preferences and more](https://docs.iredmail.org/iredadmin-pro.self-service.html)
*   [iRedAdmin-Pro: Set a proper time zone](https://docs.iredmail.org/iredadmin-pro.set.a.proper.timezone.html)
*   [iRedAdmin-Pro: Priority of spam policy used in iRedMail & iRedAdmin-Pro](https://docs.iredmail.org/iredadmin-pro.spam.policy.priority.html)
*   [iRedAdmin-Pro: Subscribable mailing list](https://docs.iredmail.org/iredadmin-pro.subscribable.mailing.list.html)
*   [iRedAdmin: Translate iRedAdmin to your local language](https://docs.iredmail.org/translate.iredadmin.html)

### Troubleshooting and Debug

*   [Turn on debug mode in Amavisd and SpamAssassin](https://docs.iredmail.org/debug.amavisd.html)
*   [Turn on debug mode in Dovecot](https://docs.iredmail.org/debug.dovecot.html)
*   [Turn on debug logging in Fail2ban](https://docs.iredmail.org/debug.fail2ban.html)
*   [Turn on debug mode in iRedAPD](https://docs.iredmail.org/debug.iredapd.html)
*   [Log executed SQL commands in MySQL/MariaDB](https://docs.iredmail.org/debug.mysql.html)
*   [Turn on debug mode in Nginx](https://docs.iredmail.org/debug.nginx.html)
*   [Turn on debug mode in OpenLDAP](https://docs.iredmail.org/debug.openldap.html)
*   [Turn on debug mode in Postfix](https://docs.iredmail.org/debug.postfix.html)
*   [Turn on debug mode in Roundcube webmail](https://docs.iredmail.org/debug.roundcubemail.html)
*   [Turn on debug mode in SOGo](https://docs.iredmail.org/debug.sogo.html)

### Frequently Asked Questions

*   [Errors you may see while maintaining iRedMail server](https://docs.iredmail.org/errors.html)
*   [Why append timestamp in maildir path](https://docs.iredmail.org/why.append.timestamp.in.maildir.path.html)
*   [Explanation of Amavisd SQL database](https://docs.iredmail.org/amavisd.sql.db.html)
*   [Backup and restore](https://docs.iredmail.org/backup.restore.html)
*   [Locations of configuration and log files of major components](https://docs.iredmail.org/file.locations.html)
*   [Introduce the OpenLDAP server configured by iRedMail](https://docs.iredmail.org/openldap.intro.html)
*   [Why no sieve support (Vacation, Forwarding) in SOGo Groupware](https://docs.iredmail.org/why.no.sieve.support.in.sogo.html)

All documents are available in [GitHub repository](https://github.com/iredmail/docs/), and published under [Creative Commons](http://creativecommons.org/licenses/by-nd/3.0/us/) license. You can [download the latest version](https://github.com/iredmail/docs/archive/master.zip) for offline reading. If you found something wrong, please do [contact us](https://www.iredmail.org/contact.html) to fix it.
