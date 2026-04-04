# Source: https://docs.mailcow.email/backup_restore/b_n_r-restore/

Title: Restore - mailcow: dockerized documentation

URL Source: https://docs.mailcow.email/backup_restore/b_n_r-restore/

Markdown Content:
Restore - mailcow: dockerized documentation
===============
- [x] - [x] 

[Skip to content](https://docs.mailcow.email/backup_restore/b_n_r-restore/#restore)

#### All Commands are available according to the [Docker Compose Plugin](https://docs.docker.com/compose/install/linux/) and the [Standalone Version](https://docs.docker.com/compose/install/other/) syntax

[![Image 1: logo](https://docs.mailcow.email/assets/images/logo.svg)](https://docs.mailcow.email/ "mailcow: dockerized documentation")

 mailcow: dockerized documentation 

 Restore 

*   [English](https://docs.mailcow.email/backup_restore/b_n_r-restore/)
*   [Deutsch](https://docs.mailcow.email/de/backup_restore/b_n_r-restore/)

[](https://docs.mailcow.email/backup_restore/b_n_r-restore/?q= "Share")

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
        *   - [x]  Restore  [Restore](https://docs.mailcow.email/backup_restore/b_n_r-restore/) Table of contents  
            *   [Restore](https://docs.mailcow.email/backup_restore/b_n_r-restore/#restore)
                *   [Variables for backup/restore script](https://docs.mailcow.email/backup_restore/b_n_r-restore/#variables-for-backuprestore-script)
                    *   [Multithreading](https://docs.mailcow.email/backup_restore/b_n_r-restore/#multithreading)
                    *   [Backup path](https://docs.mailcow.email/backup_restore/b_n_r-restore/#backup-path)

                *   [Restoring Data](https://docs.mailcow.email/backup_restore/b_n_r-restore/#restoring-data)

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
*   [Restore](https://docs.mailcow.email/backup_restore/b_n_r-restore/#restore)
    *   [Variables for backup/restore script](https://docs.mailcow.email/backup_restore/b_n_r-restore/#variables-for-backuprestore-script)
        *   [Multithreading](https://docs.mailcow.email/backup_restore/b_n_r-restore/#multithreading)
        *   [Backup path](https://docs.mailcow.email/backup_restore/b_n_r-restore/#backup-path)

    *   [Restoring Data](https://docs.mailcow.email/backup_restore/b_n_r-restore/#restoring-data)

Restore
=======

### Restore[¶](https://docs.mailcow.email/backup_restore/b_n_r-restore/#restore "Permanent link")

#### Variables for backup/restore script[¶](https://docs.mailcow.email/backup_restore/b_n_r-restore/#variables-for-backuprestore-script "Permanent link")

##### Multithreading[¶](https://docs.mailcow.email/backup_restore/b_n_r-restore/#multithreading "Permanent link")

With the 2022-10 update it is possible to run the script with multithreading support. This can be used for backups as well as for restores.

To start the backup/restore with multithreading you have to add `THREADS` as an environment variable in front of the command to execute the script.

```
THREADS=14 /opt/mailcow-dockerized/helper-scripts/backup_and_restore.sh restore
```

 The number after the `=` character indicates the number of threads. Please keep your core count -2 to leave enough CPU power for mailcow itself.
##### Backup path[¶](https://docs.mailcow.email/backup_restore/b_n_r-restore/#backup-path "Permanent link")

The script will ask you for a backup location. Inside of this location it will create folders in the format "mailcow_DATE". You should not rename those folders to not break the restore process.

To run a backup unattended, define MAILCOW_BACKUP_LOCATION as environment variable before starting the script:

```
MAILCOW_BACKUP_LOCATION=/opt/backup /opt/mailcow-dockerized/helper-scripts/backup_and_restore.sh restore
```

Tip

Both variables mentioned above can also be combined! Ex:

```
MAILCOW_BACKUP_LOCATION=/opt/backup THREADS=14 /opt/mailcow-dockerized/helper-scripts/backup_and_restore.sh restore
```

#### Restoring Data[¶](https://docs.mailcow.email/backup_restore/b_n_r-restore/#restoring-data "Permanent link")

Danger

**Please do not copy this script to another location.**

Warning

To restore a backup on a new system, **mailcow must be initialized and running!** Therefore, reinstall mailcow according to the instructions and wait to proceed with the restoration until mailcow is up and running in an empty state.

Danger for older installations

Before restoring your mailcow system on a new server and a clean mailcow-dockerized folder, please check if the value `MAILDIR_SUB` is set in your mailcow.conf. If this value is not set, do not set it in your new mailcow or remove it, otherwise **NO** emails will be displayed. Dovecot loads emails from the mentioned subfolder of the Maildir volume under `$DOCKER_VOLUME_PATH/mailcowdockerized_vmail-vol-1` and if there is any change compared to the original state, no emails will be available there.

To run a restore, **start mailcow**, use the script with "restore" as first parameter.

```
# Syntax:
# ./helper-scripts/backup_and_restore.sh restore
```

The script will ask you for a backup location containing the mailcow_DATE folders:

```
Backup location (absolute path, starting with /): /opt/backup
```

All available backups in the specified folder (in our example `/opt/backup`) are then displayed:

```
Found project name mailcowdockerized
[ 1 ] - /opt/backup/mailcow-2023-12-11-13-27-14/
[ 2 ] - /opt/backup/mailcow-2023-12-11-14-02-06/
```

Now you can enter the number of your backup that you want to restore, in this example the 2nd backup:

```
Select a restore point: 2
```

The script will now display all the backed up components that you can restore, in our case we have selected `all` for the backup process, so this will now appear here:

```
[ 0 ] - all
[ 1 ] - Crypt data
[ 2 ] - Rspamd data
[ 3 ] - Mail directory (/var/vmail)
[ 4 ] - Redis DB
[ 5 ] - Postfix data
[ 6 ] - SQL DB
```

Again, we select the component that we want to restore. Option 0 restores **EVERYTHING**.

If you want to restore to a different architecture...
If you have made the backup on a different architecture, e.g. x86, and now want to restore this backup to ARM64, the backup of Rspamd is displayed as incompatible and cannot be selected individually. When restoring with the 0 key, the restoration of Rspamd is also skipped.

Example of incompatible Rspamd backup in the selection menu:

```
[...]
[ NaN ] - Rspamd data (incompatible Arch, cannot restore it)
[...]
```

Now mailcow will restore the backups you have selected. Please note that the restoration may take some time, depending on the size of the backups.

2024-10-16 15:53:14

 Back to top 

 Copyright © 2026 mailcow Team & Community 

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

[](https://mailcow.email/ "mailcow.email")[](https://github.com/mailcow "github.com")[](https://x.com/mailcow_email "x.com")[](https://mailcow.social/@doncow "mailcow.social")
