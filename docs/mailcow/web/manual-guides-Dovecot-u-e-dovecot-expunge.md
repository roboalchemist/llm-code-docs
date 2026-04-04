# Source: https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-expunge/

Title: Expunge a Users mails - mailcow: dockerized documentation

URL Source: https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-expunge/

Markdown Content:
Expunge a Users mails - mailcow: dockerized documentation
===============
- [x] - [x] 

[Skip to content](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-expunge/#the-manual-way)

#### All Commands are available according to the [Docker Compose Plugin](https://docs.docker.com/compose/install/linux/) and the [Standalone Version](https://docs.docker.com/compose/install/other/) syntax

[![Image 1: logo](https://docs.mailcow.email/assets/images/logo.svg)](https://docs.mailcow.email/ "mailcow: dockerized documentation")

 mailcow: dockerized documentation 

 Expunge a Users mails 

*   [English](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-expunge/)
*   [Deutsch](https://docs.mailcow.email/de/manual-guides/Dovecot/u_e-dovecot-expunge/)

[](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-expunge/?q= "Share")

 Initializing search 

[mailcow/mailcow-dockerized * 2026-03 * 12.3k * 1.6k](https://github.com/mailcow/mailcow-dockerized "Go to repository")

[![Image 2: logo](https://docs.mailcow.email/assets/images/logo.svg)](https://docs.mailcow.email/ "mailcow: dockerized documentation") mailcow: dockerized documentation  

[mailcow/mailcow-dockerized * 2026-03 * 12.3k * 1.6k](https://github.com/mailcow/mailcow-dockerized "Go to repository")

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
        *   - [x]  Expunge a Users mails  [Expunge a Users mails](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-expunge/) Table of contents  
            *   [The manual way](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-expunge/#the-manual-way)
            *   [Job scheduler](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-expunge/#job-scheduler)
                *   [via the host system cron](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-expunge/#via-the-host-system-cron)
                *   [via Docker job scheduler](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-expunge/#via-docker-job-scheduler)

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
*   [The manual way](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-expunge/#the-manual-way)
*   [Job scheduler](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-expunge/#job-scheduler)
    *   [via the host system cron](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-expunge/#via-the-host-system-cron)
    *   [via Docker job scheduler](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-expunge/#via-docker-job-scheduler)

Expunge a Users mails
=====================

If you want to delete old mails out of the `.Junk` or `.Trash` folders or maybe delete all read mails that are older than a certain amount of time you may use dovecot's tool doveadm [man doveadm-expunge](https://wiki.dovecot.org/Tools/Doveadm/Expunge).

The manual way[¶](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-expunge/#the-manual-way "Permanent link")
------------------------------------------------------------------------------------------------------------------------

That said, let's dive in:

Delete a user's mails inside the junk folder that **are read** and **older** than 4 hours

[docker compose (Plugin)](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-expunge/#__tabbed_1_1) [docker-compose (Standalone)](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-expunge/#__tabbed_1_2) 

```
docker compose exec dovecot-mailcow doveadm expunge -u 'mailbox@example.com' mailbox 'Junk' SEEN not SINCE 4h
```

```
docker-compose exec dovecot-mailcow doveadm expunge -u 'mailbox@example.com' mailbox 'Junk' SEEN not SINCE 4h
```

Delete **all** user's mails in the junk folder that are **older** than 7 days

[docker compose (Plugin)](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-expunge/#__tabbed_2_1) [docker-compose (Standalone)](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-expunge/#__tabbed_2_2) 

```
docker compose exec dovecot-mailcow doveadm expunge -A mailbox 'Junk' savedbefore 7d
```

```
docker-compose exec dovecot-mailcow doveadm expunge -A mailbox 'Junk' savedbefore 7d
```

Delete **all** mails (of all users) in **all** folders that are **older** than 52 weeks (internal date of the mail, not the date it was saved on the system =>`before` instead of `savedbefore`). Useful for deleting very old mails on all users and folders (thus especially useful for GDPR-compliance).

[docker compose (Plugin)](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-expunge/#__tabbed_3_1) [docker-compose (Standalone)](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-expunge/#__tabbed_3_2) 

```
docker compose exec dovecot-mailcow doveadm expunge -A mailbox % before 52w
```

```
docker-compose exec dovecot-mailcow doveadm expunge -A mailbox % before 52w
```

Delete mails inside a custom folder **inside** a user's inbox that are **not** flagged and **older** than 2 weeks

[docker compose (Plugin)](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-expunge/#__tabbed_4_1) [docker-compose (Standalone)](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-expunge/#__tabbed_4_2) 

```
docker compose exec dovecot-mailcow doveadm expunge -u 'mailbox@example.com' mailbox 'INBOX/custom-folder' not FLAGGED not SINCE 2w
```

```
docker-compose exec dovecot-mailcow doveadm expunge -u 'mailbox@example.com' mailbox 'INBOX/custom-folder' not FLAGGED not SINCE 2w
```

Info

For possible [time spans](https://wiki.dovecot.org/Tools/Doveadm/SearchQuery#section_date_specification) or [search keys](https://wiki.dovecot.org/Tools/Doveadm/SearchQuery#section_search_keys) have a look at [man doveadm-search-query](https://wiki.dovecot.org/Tools/Doveadm/SearchQuery)

Job scheduler[¶](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-expunge/#job-scheduler "Permanent link")
----------------------------------------------------------------------------------------------------------------------

### via the host system cron[¶](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-expunge/#via-the-host-system-cron "Permanent link")

If you want to automate such a task you can create a cron job on your host that calls a script like the one below:

[docker compose (Plugin)](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-expunge/#__tabbed_5_1) [docker-compose (Standalone)](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-expunge/#__tabbed_5_2) 

```
#!/bin/bash
# Path to mailcow-dockerized, for example: /opt/mailcow-dockerized
cd /path/to/your/mailcow-dockerized

docker compose exec -T dovecot-mailcow doveadm expunge -A mailbox 'Junk' savedbefore 2w
docker compose exec -T dovecot-mailcow doveadm expunge -A mailbox 'Junk' SEEN not SINCE 12h
[...]
```

```
#!/bin/bash
# Path to mailcow-dockerized, for example: /opt/mailcow-dockerized
cd /path/to/your/mailcow-dockerized

docker-compose exec -T dovecot-mailcow doveadm expunge -A mailbox 'Junk' savedbefore 2w
docker-compose exec -T dovecot-mailcow doveadm expunge -A mailbox 'Junk' SEEN not SINCE 12h
[...]
```

To create a cron job you may execute `crontab -e` and insert something like the following to execute a script:

```
# Execute everyday at 04:00 A.M.
0 4 * * * /path/to/your/expunge_mailboxes.sh
```

### via Docker job scheduler[¶](https://docs.mailcow.email/manual-guides/Dovecot/u_e-dovecot-expunge/#via-docker-job-scheduler "Permanent link")

To achieve this with a docker job scheduler use this docker-compose.override.yml with your mailcow:

```
services:

  dovecot-mailcow:
    labels:
      ofelia.enabled: "true"
      ofelia.job-exec.dovecot-expunge-junk.schedule: "0 0 4 * * *"
      ofelia.job-exec.dovecot-expunge-junk.command: "doveadm expunge -A mailbox 'Junk' savedbefore 2w"
      ofelia.job-exec.dovecot-expunge-junk.tty: "false"
```

We add a few label to our dovecot-container to activate the job scheduler and tell him in a cron compatible scheduling format when to run. Note: Ofelia uses the [scheduling format](https://pkg.go.dev/github.com/robfig/cron?utm_source=godoc) of the Go cron implementation which starts with a field for seconds instead of minutes.

This docker-compose.override.yml deletes all mails older then 2 weeks from the "Junk" folder every day at 4 am. To see if things ran proper, you can not only see in your mailbox but also check Ofelia's docker log if it looks something like this:

```
common.go:124 ▶ NOTICE [Job "dovecot-expunge-junk" (8759567efa66)] Started - doveadm expunge -A mailbox 'Junk' savedbefore 2w,
common.go:124 ▶ NOTICE [Job "dovecot-expunge-junk" (8759567efa66)] Finished in "285.032291ms", failed: false, skipped: false, error: none,
```

If it failed it will say so and give you the output of the doveadm in the log to make it easy on you to debug.

In case you want to add more jobs, ensure you change the "dovecot-expunge-junk" part after "ofelia.job-exec." to something else, it defines the name of the job. Syntax of the labels you find at [mcuadros/ofelia](https://github.com/mcuadros/ofelia).

2025-08-05 06:37:39

 Back to top 

 Copyright © 2026 mailcow Team & Community 

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

[](https://mailcow.email/ "mailcow.email")[](https://github.com/mailcow "github.com")[](https://x.com/mailcow_email "x.com")[](https://mailcow.social/@doncow "mailcow.social")
