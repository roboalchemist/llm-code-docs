# Source: https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/

Title: Keycloak - mailcow: dockerized documentation

URL Source: https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/

Markdown Content:
Keycloak - mailcow: dockerized documentation
===============
- [x] - [x] 

[Skip to content](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#configure)

#### All Commands are available according to the [Docker Compose Plugin](https://docs.docker.com/compose/install/linux/) and the [Standalone Version](https://docs.docker.com/compose/install/other/) syntax

[![Image 1: logo](https://docs.mailcow.email/assets/images/logo.svg)](https://docs.mailcow.email/ "mailcow: dockerized documentation")

 mailcow: dockerized documentation 

 Keycloak 

*   [English](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/)
*   [Deutsch](https://docs.mailcow.email/de/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/)

[](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/?q= "Share")

 Initializing search 

[mailcow/mailcow-dockerized](https://github.com/mailcow/mailcow-dockerized "Go to repository")

[![Image 2: logo](https://docs.mailcow.email/assets/images/logo.svg)](https://docs.mailcow.email/ "mailcow: dockerized documentation") mailcow: dockerized documentation  

[mailcow/mailcow-dockerized](https://github.com/mailcow/mailcow-dockerized "Go to repository")

*   [Information & Support](https://docs.mailcow.email/)
*   - [x]  Get started   Get started  
    *   [Prepare your system](https://docs.mailcow.email/getstarted/prerequisite-system/)
    *   [DNS setup](https://docs.mailcow.email/getstarted/prerequisite-dns/)
    *   [Install mailcow](https://docs.mailcow.email/getstarted/install/)

*   - [x]  Maintaining mailcow   Maintaining mailcow  
    *   [Update](https://docs.mailcow.email/maintenance/update/)
    *   [Migration](https://docs.mailcow.email/maintenance/migration/)
    *   [Deinstallation](https://docs.mailcow.email/maintenance/deinstall/)

*   - [x]  Backup & Restore   Backup & Restore  
    *   - [x]  Component backup & restore   Component backup & restore  
        *   [Backup](https://docs.mailcow.email/backup_restore/b_n_r-backup/)
        *   [Restore](https://docs.mailcow.email/backup_restore/b_n_r-restore/)
        *   [Export](https://docs.mailcow.email/backup_restore/b_n_r-backup-export/)

    *   [Cold-standby (rolling backup)](https://docs.mailcow.email/backup_restore/b_n_r-coldstandby/)
    *   - [x]  Manual backups   Manual backups  
        *   [Maildir](https://docs.mailcow.email/backup_restore/b_n_r-backup_restore-maildir/)
        *   [MySQL (mysqldump)](https://docs.mailcow.email/backup_restore/b_n_r-backup_restore-mysql/)

    *   - [x]  mailcow-internal backups   mailcow-internal backups  
        *   [Recover accidentally deleted data](https://docs.mailcow.email/backup_restore/b_n_r-accidental_deletion/)

*   - [x]  Post Installation Tasks   Post Installation Tasks  
    *   [Advanced SSL](https://docs.mailcow.email/post_installation/firststeps-ssl/)
    *   [SSL with DNS Challenge](https://docs.mailcow.email/post_installation/firststeps-ssl-dns/)
    *   [Authorize Watchdog and Bounce Mails](https://docs.mailcow.email/post_installation/firststeps-authorize_watchdog_and_bounces/)
    *   [Disable IPv6](https://docs.mailcow.email/post_installation/firststeps-disable_ipv6/)
    *   [DMARC Reporting](https://docs.mailcow.email/post_installation/firststeps-dmarc_reporting/)
    *   [IP bindings](https://docs.mailcow.email/post_installation/firststeps-ip_bindings/)
    *   [Local MTA on Docker host](https://docs.mailcow.email/post_installation/firststeps-local_mta/)
    *   [Logging](https://docs.mailcow.email/post_installation/firststeps-logging/)
    *   [Setting up MTA-STS](https://docs.mailcow.email/post_installation/setup-mta-sts/)
    *   - [x]  Reverse Proxy   Reverse Proxy  
        *   [Overview](https://docs.mailcow.email/post_installation/reverse-proxy/r_p/)
        *   [Apache 2.4](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-apache24/)
        *   [Nginx](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-nginx/)
        *   [HAProxy (community supported)](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-haproxy/)
        *   [Traefik v3 (community supported)](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/)
        *   [Caddy v2 (community supported)](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-caddy2/)

    *   [SNAT](https://docs.mailcow.email/post_installation/firststeps-snat/)
    *   [Sync job migration](https://docs.mailcow.email/post_installation/firststeps-sync_jobs_migration/)

*   - [x]  Models   Models  
    *   [ACL](https://docs.mailcow.email/models/model-acl/)
    *   [Password hashing](https://docs.mailcow.email/models/model-passwd/)
    *   [Sender and receiver model](https://docs.mailcow.email/models/model-sender_rcv/)

*   - [x]  General Troubleshooting   General Troubleshooting  
    *   [Introduction](https://docs.mailcow.email/troubleshooting/debug/)
    *   [Admin login to SOGo](https://docs.mailcow.email/troubleshooting/debug-admin_login_sogo/)
    *   [Advanced: Find memory leaks in Rspamd](https://docs.mailcow.email/troubleshooting/debug-rspamd_memory_leaks/)
    *   [Attach to a Container](https://docs.mailcow.email/troubleshooting/debug-attach_service/)
    *   [Common Problems](https://docs.mailcow.email/troubleshooting/debug-common_problems/)
    *   [Google SafeBrowsing issues](https://docs.mailcow.email/troubleshooting/debug-google_safe_browsing/)
    *   [Logs](https://docs.mailcow.email/troubleshooting/debug-logs/)
    *   [Manual MySQL upgrade](https://docs.mailcow.email/troubleshooting/debug-mysql_upgrade/)
    *   [Recover crashed Aria storage engine](https://docs.mailcow.email/troubleshooting/debug-mysql_aria/)
    *   [Remove Persistent Data](https://docs.mailcow.email/troubleshooting/debug-rm_volumes/)
    *   [Resend Quarantine Notifications](https://docs.mailcow.email/troubleshooting/debug-resend-quarantine-notifications/)
    *   [Reset Passwords (incl. SQL)](https://docs.mailcow.email/troubleshooting/debug-reset_pw/)
    *   [Reset TLS certificates](https://docs.mailcow.email/troubleshooting/debug-reset_tls/)
    *   [Use latest SOGo Nightly build](https://docs.mailcow.email/troubleshooting/debug-sogo_nightly/)

*   - [x]  Manual/Guides/Examples   Manual/Guides/Examples  
    *   - [x]  mailcow UI   mailcow UI  
        *   [Blacklist / Whitelist](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-bl_wl/)
        *   [Configuration](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-config/)
        *   [CSS overrides](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-css/)
        *   [Forgot Password Feature](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-forgot_password/)
        *   [Netfilter](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-netfilter/)
        *   [Notification templates](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-notification-templates/)
        *   [Pushover](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-pushover/)
        *   [Spamfilter](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-spamfilter/)
        *   [Sub-addressing](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-sub_addressing/)
        *   [Tags (for Domains and Mailboxes)](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-tags/)
        *   [Temporary email aliases](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-spamalias/)
        *   [Two-Factor Authentication](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-tfa/)
        *   [WebAuthn / FIDO2](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-fido/)
        *   [LDAP](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-ldap/)
        *   - [x]  Keycloak  [Keycloak](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/) Table of contents  
            *   [Configure](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#configure)
            *   [Automatic User Provisioning](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#automatic-user-provisioning)
                *   [How It Works](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#how-it-works)
                *   [Example Configuration](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#example-configuration)
                *   [Updates on Login](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#updates-on-login)
                *   [Import and Updates via Crontask](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#import-and-updates-via-crontask)

            *   [Mailpassword Flow](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#mailpassword-flow)
                *   [How It Works](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#how-it-works_1)
                *   [Generate a BLF-CRYPT Hashed Password](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#generate-a-blf-crypt-hashed-password)

            *   [Change the Authentication Source for Existing Users](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#change-the-authentication-source-for-existing-users)
            *   [Authentication for External Mail Clients (IMAP, SIEVE, POP3, SMTP)](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#authentication-for-external-mail-clients-imap-sieve-pop3-smtp)
            *   [Troubleshooting](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#troubleshooting)

        *   [Generic-OIDC](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-generic-oidc/)

    *   - [x]  Postfix   Postfix  
        *   [Unauthenticated Relaying](https://docs.mailcow.email/manual-guides/Postfix/u_e-postfix-unauthenticated-relaying/)
        *   [Custom transport maps](https://docs.mailcow.email/manual-guides/Postfix/u_e-postfix-custom_transport/)
        *   [Customize/Expand main.cf](https://docs.mailcow.email/manual-guides/Postfix/u_e-postfix-extra_cf/)
        *   [Disable Sender Addresses Verification](https://docs.mailcow.email/manual-guides/Postfix/u_e-postfix-disable_sender_verification/)
        *   [Hardening Ciphers](https://docs.mailcow.email/manual-guides/Postfix/u_e-postfix-harden_ciphers/)
        *   [Max. message size (attachment size)](https://docs.mailcow.email/manual-guides/Postfix/u_e-postfix-attachment_size/)
        *   [Relayhosts](https://docs.mailcow.email/manual-guides/Postfix/u_e-postfix-relayhost/)
        *   [Statistics with pflogsumm](https://docs.mailcow.email/manual-guides/Postfix/u_e-postfix-pflogsumm/)
        *   [TLS-Policy override](https://docs.mailcow.email/manual-guides/Postfix/u_e-postfix-tls_policy_override/)
        *   [Whitelist IP in Postscreen](https://docs.mailcow.email/manual-guides/Postfix/u_e-postfix-postscreen_whitelist/)

    *   - [x]  Unbound   Unbound  
        *   [Using an external DNS service](https://docs.mailcow.email/manual-guides/Unbound/u_e-unbound-fwd/)

    *   - [x]  Dovecot   Dovecot  
        *   [Customize/Expand dovecot.conf](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-extra_conf/)
        *   [Enable "any" ACL settings](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-any_acl/)
        *   [Expunge a Users mails](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-expunge/)
        *   [Full-Text Search](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-fts/)
        *   [Hardening Ciphers](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-harden_ciphers/)
        *   [IMAP IDLE interval](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-idle_interval/)
        *   [Lazy Expunge (Dovecot Plugin)](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-lazy_expunge/)
        *   [Mail crypt](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-mail-crypt/)
        *   [More Examples with DOVEADM](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-more/)
        *   [Move Maildir (vmail)](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-vmail-volume/)
        *   [Performance Optimizations](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-performance/)
        *   [Public folders](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-public_folder/)
        *   [Static master user](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-static_master/)
        *   [Vacation replies for catchall addresses](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-catchall_vacation/)

    *   - [x]  Nginx   Nginx  
        *   [Create subdomain webmail.example.org](https://docs.mailcow.email/manual-guides/Nginx/u_e-nginx_webmail-site/)
        *   [Custom sites](https://docs.mailcow.email/manual-guides/Nginx/u_e-nginx_custom/)

    *   - [x]  Watchdog   Watchdog  
        *   [Thresholds](https://docs.mailcow.email/manual-guides/Watchdog/u_e-watchdog-thresholds/)

    *   [Redis](https://docs.mailcow.email/manual-guides/Redis/u_e-redis/)
    *   - [x]  Rspamd   Rspamd  
        *   [General Settings](https://docs.mailcow.email/manual-guides/Rspamd/u_e-rspamd-general/)
        *   [Tweaks](https://docs.mailcow.email/manual-guides/Rspamd/u-e-rspamd-tweaks/)
        *   [Work with Spam Data](https://docs.mailcow.email/manual-guides/Rspamd/u-e-rspamd-work-with-spamdata/)
        *   [Disable Greylisting](https://docs.mailcow.email/manual-guides/Rspamd/u_e-rspamd-disable-greylisting/)
        *   [Add Additional Modules](https://docs.mailcow.email/manual-guides/Rspamd/u-e-rspamd-add-additional-modules/)

    *   - [x]  ClamAV   ClamAV  
        *   [Whitelist](https://docs.mailcow.email/manual-guides/ClamAV/u_e-clamav-whitelist/)
        *   [Additional Databases](https://docs.mailcow.email/manual-guides/ClamAV/u_e-clamav-additional_dbs/)

    *   [SOGo](https://docs.mailcow.email/manual-guides/SOGo/u_e-sogo/)
    *   - [x]  Docker   Docker  
        *   [Customize Dockerfiles](https://docs.mailcow.email/manual-guides/Docker/u_e-docker-cust_dockerfiles/)

    *   [Why unbound?](https://docs.mailcow.email/manual-guides/u_e-why_unbound/)
    *   [Autodiscover / Autoconfig](https://docs.mailcow.email/manual-guides/u_e-autodiscover_config/)
    *   [Redirect HTTP to HTTPS](https://docs.mailcow.email/manual-guides/u_e-80_to_443/)
    *   [Re-enable TLS 1.0 and TLS 1.1](https://docs.mailcow.email/manual-guides/u_e-reeanble-weak-protocols/)
    *   [Run scripts before and after updates](https://docs.mailcow.email/manual-guides/u_e-update-hooks/)

*   - [x]  Client Configuration   Client Configuration  
    *   [Overview](https://docs.mailcow.email/client/client/)
    *   [Android](https://docs.mailcow.email/client/client-android/)
    *   [Apple macOS / iOS](https://docs.mailcow.email/client/client-apple/)
    *   [eM Client](https://docs.mailcow.email/client/client-emclient/)
    *   [KDE Kontact](https://docs.mailcow.email/client/client-kontact/)
    *   [Microsoft Outlook](https://docs.mailcow.email/client/client-outlook/)
    *   [Mozilla Thunderbird](https://docs.mailcow.email/client/client-thunderbird/)
    *   [Manual configuration](https://docs.mailcow.email/client/client-manual/)

*   - [x]  Third party apps (community managed)   Third party apps (community managed)  
    *   [AbuseIPDB Integration](https://docs.mailcow.email/third_party/abuseipdb/third_party-abuseipdb/)
    *   [Borgmatic Backup](https://docs.mailcow.email/third_party/borgmatic/third_party-borgmatic/)
    *   [CheckMK](https://docs.mailcow.email/third_party/checkmk/u_e-checkmk/)
    *   [Exchange Hybrid Setup](https://docs.mailcow.email/third_party/exchange_onprem/third_party-exchange_onprem/)
    *   [Gitea](https://docs.mailcow.email/third_party/gitea/third_party-gitea/)
    *   [Gogs](https://docs.mailcow.email/third_party/gogs/third_party-gogs/)
    *   [mailcow Logs Viewer](https://docs.mailcow.email/third_party/mailcow-logs-viewer/third_party-mailcow-logs-viewer/)
    *   [Mailman 3](https://docs.mailcow.email/third_party/mailman3/third_party-mailman3/)
    *   [Mailpiler Integration](https://docs.mailcow.email/third_party/mailpiler/third_party-mailpiler_integration/)
    *   [Nextcloud](https://docs.mailcow.email/third_party/nextcloud/third_party-nextcloud/)
    *   [Portainer](https://docs.mailcow.email/third_party/portainer/third_party-portainer/)
    *   [Roundcube](https://docs.mailcow.email/third_party/roundcube/third_party-roundcube/)
    *   [Prometheus Exporter](https://docs.mailcow.email/third_party/prometheus_exporter/third_party-prometheus_exporter/)

 Table of contents  
*   [Configure](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#configure)
*   [Automatic User Provisioning](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#automatic-user-provisioning)
    *   [How It Works](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#how-it-works)
    *   [Example Configuration](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#example-configuration)
    *   [Updates on Login](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#updates-on-login)
    *   [Import and Updates via Crontask](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#import-and-updates-via-crontask)

*   [Mailpassword Flow](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#mailpassword-flow)
    *   [How It Works](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#how-it-works_1)
    *   [Generate a BLF-CRYPT Hashed Password](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#generate-a-blf-crypt-hashed-password)

*   [Change the Authentication Source for Existing Users](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#change-the-authentication-source-for-existing-users)
*   [Authentication for External Mail Clients (IMAP, SIEVE, POP3, SMTP)](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#authentication-for-external-mail-clients-imap-sieve-pop3-smtp)
*   [Troubleshooting](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#troubleshooting)

Keycloak
========

### **Configure**[¶](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#configure "Permanent link")

To add or edit your **Identity Provider** configuration, log in to your _mailcow UI_ as administrator, go to `System > Configuration > Access > Identity Provider` and select **Keycloak** from the Identity Provider dropdown.

*   `Server URL`: The base URL of your Keycloak server.
*   `Realm`: The Keycloak realm where the mailcow client is configured.
*   `Client ID`: The Client ID assigned to mailcow Client in Keycloak.
*   `Client Secret`: The Client Secret assigned to the mailcow client in Keycloak.
*   `Redirect URL`: The redirect URL that Keycloak will use after authentication. This should point to your mailcow UI. Example: `https://mail.mailcow.tld`
*   `Version`: Specifies the Keycloak version.
*   `Attribute Mapping`:
    *   `Attribute`: Defines the attribute value that should be mapped.
    *   `Template`: Specifies which mailbox template should be applied for the defined LDAP attribute value

*   `Mailpassword Flow`: If enabled, mailcow will attempt to validate user credentials using the **Keycloak Admin REST API** instead of relying solely on the Authorization Code Flow.
    *   This requires that the user has a **mailcow_password** attribute set in Keycloak. **mailcow_password** should contain a hashed password
    *   The mailcow client in Keycloak must have a Service Account and permission to view-users.

*   `Ignore SSL Errors`: If enabled, SSL certificate validation is bypassed.
*   `Periodic Full Sync`: If enabled, mailcow periodically performs a full sync of all users from Keycloak.
*   `Import Users`: If enabled, new users are automatically imported from Keycloak into mailcow.
*   `Sync / Import Interval (min)`: Defines the time interval (in minutes) for periodic synchronization and user imports.

* * *

### **Automatic User Provisioning**[¶](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#automatic-user-provisioning "Permanent link")

If a user does not exist in **mailcow** and logs in via the **mailcow UI**, the user will be **automatically created**, provided that a matching **attribute mapping** is configured.

#### **How It Works**[¶](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#how-it-works "Permanent link")

1.   On login, **mailcow** initializes an **Authorization Code Flow** and, if successful, retrieves the user's **OIDC token**. 
2.   **mailcow** then looks for the **`mailcow_template`** value in the user info and retrieves it. 
3.   If the value matches an attribute defined in the **Attribute Mapping**, the corresponding **mailbox template** is applied. 

#### **Example Configuration**[¶](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#example-configuration "Permanent link")

*   The user has an attribute **`mailcow_template`** with the value **`default`**, which can be retrieved from the **User Info Endpoint**. 
*   Under **Attribute Mapping**, set **`Attribute`** to **`default`** and select an appropriate **mailbox template**. 

#### **Updates on Login**[¶](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#updates-on-login "Permanent link")

Each time a user logs in via the **mailcow UI**, **mailcow** checks if the assigned **template** has changed. If so, it updates the mailbox settings accordingly.

#### **Import and Updates via Crontask**[¶](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#import-and-updates-via-crontask "Permanent link")

Prerequisite

This requires **mailcow** to have access to the **Keycloak Admin REST API**.

 Make sure the **mailcow Client** has an Service Account and the Service account role **view-users**.

If **Import Users** is enabled, a scheduled cron job will automatically import users from Keycloak to mailcow at the specified **Sync / Import Interval (min)**.

If **Periodic Full Sync** is enabled, the cron job will also update existing users at the specified **Sync / Import Interval (min)**, ensuring that any changes in LDAP are applied to their corresponding mailboxes in mailcow.

Check the logs for imports and sync updates under `System > Information > Logs > Crontasks`.

* * *

### **Mailpassword Flow**[¶](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#mailpassword-flow "Permanent link")

Prerequisite

This requires **mailcow** to have access to the **Keycloak Admin REST API**.

 Make sure the **mailcow Client** has an Service Account and the Service account role **view-users**.

The **Mailpassword Flow** is a direct authentication method that does **not** use the **OIDC Protocol**. It serves as an alternative to the **Authorization Code Flow**.

With the **Mailpassword Flow**, automatic user provisioning also works for logins via **mail protocols** (IMAP, SIEVE, POP3, SMTP).

#### **How It Works**[¶](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#how-it-works_1 "Permanent link")

1.   On login, **mailcow** uses the **Keycloak Admin REST API** to retrieve the user’s attributes. 
2.   **mailcow** looks for the **`mailcow_password`** attribute. 
3.   The **`mailcow_password`** value should contain a [**compatible hashed password**](https://docs.mailcow.email/models/model-passwd/), which will be used for verification. 

This ensures seamless authentication and mailbox creation for both UI and mail protocol logins.

#### **Generate a BLF-CRYPT Hashed Password**[¶](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#generate-a-blf-crypt-hashed-password "Permanent link")

The following command creates a bcrypt-hashed password and prefixes it with `{BLF-CRYPT}`:

```
mkpasswd -m bcrypt | sed 's/^/{BLF-CRYPT}/'
```

* * *

### **Change the Authentication Source for Existing Users**[¶](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#change-the-authentication-source-for-existing-users "Permanent link")

Once you have configured an **Keycloak Identity Provider**, you can change the authentication source for existing users from **mailcow** to **Keycloak**.

1.   Navigate to **`E-Mail > Configuration > Mailboxes`**. 
2.   Edit the user. 
3.   From the **Identity Provider** dropdown, select **Keycloak**. 
4.   Save the changes. 

Notice

The existing SQL password is **not overwritten**. If you switch the authentication source back to **mailcow**, the user will be able to log in with their previous password.

* * *

### **Authentication for External Mail Clients (IMAP, SIEVE, POP3, SMTP)**[¶](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#authentication-for-external-mail-clients-imap-sieve-pop3-smtp "Permanent link")

Notice

This does not necessarily apply to users utilizing the Mailpassword Flow.

Before users can use external mail clients, they must first log in to the mailcow UI and navigate to the **Mailbox Settings**.

 In the **App Passwords** tab, they can generate a new app password, which must then be used for authentication in the external mail client.

* * *

### **Troubleshooting**[¶](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/#troubleshooting "Permanent link")

If users cannot log in, first check the log details under: `System > Information > Logs > mailcow UI`.

 Then, follow these steps to diagnose and resolve the issue:

1.   **Test Connection**

    *   Navigate to **`System > Configuration > Access > Identity Provider`**. 
    *   Run the **Connection Test** and ensure it completes successfully. 

2.   **Verify the User’s Mail Domain**

    *   Ensure the user’s mail domain exists in mailcow. 
    *   Check if the domain is limited by **"Max. possible mailboxes"** or **"Domain quota"**. 

3.   **Confirm Attribute Mapping**

    *   Make sure a matching **Attribute Mapping** is configured for the users. 

If you’re experiencing issues with **`Periodic Full Sync`** or **`Import Users`**, review the logs under `System > Information > Logs > Crontasks`

2025-03-12 09:26:32

 Back to top 

 Copyright © 2026 mailcow Team & Community 

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

[](https://mailcow.email/ "mailcow.email")[](https://github.com/mailcow "github.com")[](https://x.com/mailcow_email "x.com")[](https://mailcow.social/@doncow "mailcow.social")
