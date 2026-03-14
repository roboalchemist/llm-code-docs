# Source: https://docs.mailcow.email/post_installation/firststeps-sync_jobs_migration/

Title: Sync job migration - mailcow: dockerized documentation

URL Source: https://docs.mailcow.email/post_installation/firststeps-sync_jobs_migration/

Markdown Content:
Sync job migration - mailcow: dockerized documentation
===============
- [x] - [x] 

[Skip to content](https://docs.mailcow.email/post_installation/firststeps-sync_jobs_migration/#creating-a-sync-job)

#### All Commands are available according to the [Docker Compose Plugin](https://docs.docker.com/compose/install/linux/) and the [Standalone Version](https://docs.docker.com/compose/install/other/) syntax

[![Image 1: logo](https://docs.mailcow.email/assets/images/logo.svg)](https://docs.mailcow.email/ "mailcow: dockerized documentation")

 mailcow: dockerized documentation 

 Sync job migration 

*   [English](https://docs.mailcow.email/post_installation/firststeps-sync_jobs_migration/)
*   [Deutsch](https://docs.mailcow.email/de/post_installation/firststeps-sync_jobs_migration/)

[](https://docs.mailcow.email/post_installation/firststeps-sync_jobs_migration/?q= "Share")

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
    *   - [x]  Sync job migration  [Sync job migration](https://docs.mailcow.email/post_installation/firststeps-sync_jobs_migration/) Table of contents  
        *   [Creating a Sync Job](https://docs.mailcow.email/post_installation/firststeps-sync_jobs_migration/#creating-a-sync-job)

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
        *   [Keycloak](https://docs.mailcow.email/manual-guides/mailcow-UI/u_e-mailcow_ui-keycloak/)
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
*   [Creating a Sync Job](https://docs.mailcow.email/post_installation/firststeps-sync_jobs_migration/#creating-a-sync-job)

Sync job migration
==================

Sync jobs are used to copy or move existing emails either from an external IMAP server or between existing mailboxes within mailcow.

Notice

Depending on your mailbox’s access control list (ACL), you may not have permission to create a sync job. In this case, please contact your domain administrator.

Creating a Sync Job[¶](https://docs.mailcow.email/post_installation/firststeps-sync_jobs_migration/#creating-a-sync-job "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------------

1.   Navigate to “E-Mail  Configuration  Synchronizations” (if logged in as an admin or domain admin) or “User Settings  Sync Jobs” (as a regular mailbox user) to create a new sync job.

2.   If you are an administrator, select the mailbox username from the “Username” dropdown menu where the emails should be copied to (target mailbox).

3.   Fill in the “Host” and “Port” fields with the correct connection details of the source IMAP server (the server from which the emails will be fetched).

4.   Enter the correct login credentials for the source IMAP server in the “Username” and “Password” fields.

5.   Select the appropriate encryption method. If the source IMAP server uses port 143, TLS is likely the correct choice, while SSL is typically used with port 993. PLAIN authentication is also possible, but strongly discouraged.

6.   All other fields can be left at their default values or adjusted as needed.

7.   Make sure to check the “Active” box and click “Add” to finalize the sync job.

Please remember...

Once you’re done, log in to the target mailbox and verify that all emails were imported correctly. If everything worked as expected, all your emails will appear in the new inbox. Don’t forget to disable or delete the sync job once it’s no longer needed.

2025-05-07 10:33:59

 Back to top 

 Copyright © 2026 mailcow Team & Community 

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

[](https://mailcow.email/ "mailcow.email")[](https://github.com/mailcow "github.com")[](https://x.com/mailcow_email "x.com")[](https://mailcow.social/@doncow "mailcow.social")
