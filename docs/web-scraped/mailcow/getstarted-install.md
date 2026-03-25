# Source: https://docs.mailcow.email/getstarted/install/

Title: Install mailcow - mailcow: dockerized documentation

URL Source: https://docs.mailcow.email/getstarted/install/

Markdown Content:
Install mailcow - mailcow: dockerized documentation
===============
- [x] - [x] 

[Skip to content](https://docs.mailcow.email/getstarted/install/#installation-of-mailcow)

#### All Commands are available according to the [Docker Compose Plugin](https://docs.docker.com/compose/install/linux/) and the [Standalone Version](https://docs.docker.com/compose/install/other/) syntax

[![Image 1: logo](https://docs.mailcow.email/assets/images/logo.svg)](https://docs.mailcow.email/ "mailcow: dockerized documentation")

 mailcow: dockerized documentation 

 Install mailcow 

*   [English](https://docs.mailcow.email/getstarted/install/)
*   [Deutsch](https://docs.mailcow.email/de/getstarted/install/)

[](https://docs.mailcow.email/getstarted/install/?q= "Share")

 Initializing search 

[mailcow/mailcow-dockerized](https://github.com/mailcow/mailcow-dockerized "Go to repository")

[![Image 2: logo](https://docs.mailcow.email/assets/images/logo.svg)](https://docs.mailcow.email/ "mailcow: dockerized documentation") mailcow: dockerized documentation  

[mailcow/mailcow-dockerized](https://github.com/mailcow/mailcow-dockerized "Go to repository")

*   [Information & Support](https://docs.mailcow.email/)
*   - [x]  Get started   Get started  
    *   [Prepare your system](https://docs.mailcow.email/getstarted/prerequisite-system/)
    *   [DNS setup](https://docs.mailcow.email/getstarted/prerequisite-dns/)
    *   - [x]  Install mailcow  [Install mailcow](https://docs.mailcow.email/getstarted/install/) Table of contents  
        *   [Prerequisites](https://docs.mailcow.email/getstarted/install/#prerequisites)
            *   [System Packages](https://docs.mailcow.email/getstarted/install/#system-packages)
            *   [Docker and Docker Compose](https://docs.mailcow.email/getstarted/install/#docker-and-docker-compose)
            *   [Quick Installation](https://docs.mailcow.email/getstarted/install/#quick-installation)
                *   [System Packages](https://docs.mailcow.email/getstarted/install/#system-packages_1)
                    *   [Debian/Ubuntu:](https://docs.mailcow.email/getstarted/install/#debianubuntu)
                    *   [RHEL-based systems (e.g., Rocky Linux 9):](https://docs.mailcow.email/getstarted/install/#rhel-based-systems-eg-rocky-linux-9)
                    *   [Alpine Linux (e.g., 3.22):](https://docs.mailcow.email/getstarted/install/#alpine-linux-eg-322)

                *   [Docker](https://docs.mailcow.email/getstarted/install/#docker)
                    *   [Debian/Ubuntu:](https://docs.mailcow.email/getstarted/install/#debianubuntu_1)
                    *   [RHEL-based systems (e.g., Rocky Linux 9):](https://docs.mailcow.email/getstarted/install/#rhel-based-systems-eg-rocky-linux-9_1)
                    *   [Alpine Linux (e.g., 3.22):](https://docs.mailcow.email/getstarted/install/#alpine-linux-eg-322_1)

                *   [Docker Compose](https://docs.mailcow.email/getstarted/install/#docker-compose)
                    *   [Installation via Package Manager (Plugin)](https://docs.mailcow.email/getstarted/install/#installation-via-package-manager-plugin)
                        *   [Debian/Ubuntu:](https://docs.mailcow.email/getstarted/install/#debianubuntu_2)
                        *   [RHEL-based systems:](https://docs.mailcow.email/getstarted/install/#rhel-based-systems)
                        *   [Alpine Linux (e.g., 3.22):](https://docs.mailcow.email/getstarted/install/#alpine-linux-eg-322_2)

                    *   [Installation as a Standalone Version](https://docs.mailcow.email/getstarted/install/#installation-as-a-standalone-version)

        *   [SELinux Configuration (Optional)](https://docs.mailcow.email/getstarted/install/#selinux-configuration-optional)
        *   [Installing mailcow](https://docs.mailcow.email/getstarted/install/#installing-mailcow)
        *   [Starting mailcow](https://docs.mailcow.email/getstarted/install/#starting-mailcow)
        *   [Troubleshooting](https://docs.mailcow.email/getstarted/install/#troubleshooting)
            *   [MTU not equal to 1500 (e.g., OpenStack)](https://docs.mailcow.email/getstarted/install/#mtu-not-equal-to-1500-eg-openstack)
            *   [No IPv6 on the Host System](https://docs.mailcow.email/getstarted/install/#no-ipv6-on-the-host-system)

        *   [Important Notes](https://docs.mailcow.email/getstarted/install/#important-notes)

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
*   [Prerequisites](https://docs.mailcow.email/getstarted/install/#prerequisites)
    *   [System Packages](https://docs.mailcow.email/getstarted/install/#system-packages)
    *   [Docker and Docker Compose](https://docs.mailcow.email/getstarted/install/#docker-and-docker-compose)
    *   [Quick Installation](https://docs.mailcow.email/getstarted/install/#quick-installation)
        *   [System Packages](https://docs.mailcow.email/getstarted/install/#system-packages_1)
            *   [Debian/Ubuntu:](https://docs.mailcow.email/getstarted/install/#debianubuntu)
            *   [RHEL-based systems (e.g., Rocky Linux 9):](https://docs.mailcow.email/getstarted/install/#rhel-based-systems-eg-rocky-linux-9)
            *   [Alpine Linux (e.g., 3.22):](https://docs.mailcow.email/getstarted/install/#alpine-linux-eg-322)

        *   [Docker](https://docs.mailcow.email/getstarted/install/#docker)
            *   [Debian/Ubuntu:](https://docs.mailcow.email/getstarted/install/#debianubuntu_1)
            *   [RHEL-based systems (e.g., Rocky Linux 9):](https://docs.mailcow.email/getstarted/install/#rhel-based-systems-eg-rocky-linux-9_1)
            *   [Alpine Linux (e.g., 3.22):](https://docs.mailcow.email/getstarted/install/#alpine-linux-eg-322_1)

        *   [Docker Compose](https://docs.mailcow.email/getstarted/install/#docker-compose)
            *   [Installation via Package Manager (Plugin)](https://docs.mailcow.email/getstarted/install/#installation-via-package-manager-plugin)
                *   [Debian/Ubuntu:](https://docs.mailcow.email/getstarted/install/#debianubuntu_2)
                *   [RHEL-based systems:](https://docs.mailcow.email/getstarted/install/#rhel-based-systems)
                *   [Alpine Linux (e.g., 3.22):](https://docs.mailcow.email/getstarted/install/#alpine-linux-eg-322_2)

            *   [Installation as a Standalone Version](https://docs.mailcow.email/getstarted/install/#installation-as-a-standalone-version)

*   [SELinux Configuration (Optional)](https://docs.mailcow.email/getstarted/install/#selinux-configuration-optional)
*   [Installing mailcow](https://docs.mailcow.email/getstarted/install/#installing-mailcow)
*   [Starting mailcow](https://docs.mailcow.email/getstarted/install/#starting-mailcow)
*   [Troubleshooting](https://docs.mailcow.email/getstarted/install/#troubleshooting)
    *   [MTU not equal to 1500 (e.g., OpenStack)](https://docs.mailcow.email/getstarted/install/#mtu-not-equal-to-1500-eg-openstack)
    *   [No IPv6 on the Host System](https://docs.mailcow.email/getstarted/install/#no-ipv6-on-the-host-system)

*   [Important Notes](https://docs.mailcow.email/getstarted/install/#important-notes)

Installation of mailcow[¶](https://docs.mailcow.email/getstarted/install/#installation-of-mailcow "Permanent link")
===================================================================================================================

Prerequisites[¶](https://docs.mailcow.email/getstarted/install/#prerequisites "Permanent link")
-----------------------------------------------------------------------------------------------

### System Packages[¶](https://docs.mailcow.email/getstarted/install/#system-packages "Permanent link")

The following Linux packages are required for using mailcow and may need to be installed depending on your distribution:

*   git
*   openssl
*   curl
*   awk
*   sha1sum
*   grep
*   cut
*   jq (**new as of [2025-09](https://mailcow.email/posts/2025/release-2025-09/#2025-09-release-10th-september-2025)**)

### Docker and Docker Compose[¶](https://docs.mailcow.email/getstarted/install/#docker-and-docker-compose "Permanent link")

For the installation, you will need:

*   **Docker**: Version `>= 24.0.0`
*   **Docker Compose**: Version `>= 2.0`

Installation guides can be found here:

*   [Install Docker](https://docs.docker.com/install/)
*   [Install Docker Compose](https://docs.docker.com/compose/install/)

### Quick Installation[¶](https://docs.mailcow.email/getstarted/install/#quick-installation "Permanent link")

#### System Packages[¶](https://docs.mailcow.email/getstarted/install/#system-packages_1 "Permanent link")

##### Debian/Ubuntu:[¶](https://docs.mailcow.email/getstarted/install/#debianubuntu "Permanent link")

```
apt update
apt install -y git openssl curl gawk coreutils grep jq
```

##### RHEL-based systems (e.g., Rocky Linux 9):[¶](https://docs.mailcow.email/getstarted/install/#rhel-based-systems-eg-rocky-linux-9 "Permanent link")

```
dnf install -y git openssl curl gawk coreutils grep jq
```

##### Alpine Linux (e.g., 3.22):[¶](https://docs.mailcow.email/getstarted/install/#alpine-linux-eg-322 "Permanent link")

```
apk add --no-cache --upgrade sed findutils bash git openssl curl gawk coreutils grep jq
```

Note

All programs not explicitly listed in the installation process are already included as subprograms in `coreutils`.

#### Docker[¶](https://docs.mailcow.email/getstarted/install/#docker "Permanent link")

Important

Use the **latest available Docker Engine** and not the version from your Linux distribution's package sources.

##### Debian/Ubuntu:[¶](https://docs.mailcow.email/getstarted/install/#debianubuntu_1 "Permanent link")

```
curl -sSL https://get.docker.com/ | CHANNEL=stable sh
systemctl enable --now docker
```

##### RHEL-based systems (e.g., Rocky Linux 9):[¶](https://docs.mailcow.email/getstarted/install/#rhel-based-systems-eg-rocky-linux-9_1 "Permanent link")

```
dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo
dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
systemctl enable --now docker
```

##### Alpine Linux (e.g., 3.22):[¶](https://docs.mailcow.email/getstarted/install/#alpine-linux-eg-322_1 "Permanent link")

```
apk --no-cache --upgrade add docker
rc-update add docker default
rc-service docker start
```

Note

The `get.docker.com` script does not work reliably or at all on RHEL and Alpine Linux systems. Use the manual method instead.

#### Docker Compose[¶](https://docs.mailcow.email/getstarted/install/#docker-compose "Permanent link")

Warning

**mailcow requires Docker Compose version `>= 2.0`.**

##### Installation via Package Manager (Plugin)[¶](https://docs.mailcow.email/getstarted/install/#installation-via-package-manager-plugin "Permanent link")

Note

This method requires that the Docker repository has been added (see [Docker](https://docs.mailcow.email/getstarted/install/#docker)).

###### Debian/Ubuntu:[¶](https://docs.mailcow.email/getstarted/install/#debianubuntu_2 "Permanent link")

```
apt update
apt install docker-compose-plugin
```

###### RHEL-based systems:[¶](https://docs.mailcow.email/getstarted/install/#rhel-based-systems "Permanent link")

```
dnf update
dnf install docker-compose-plugin
```

###### Alpine Linux (e.g., 3.22):[¶](https://docs.mailcow.email/getstarted/install/#alpine-linux-eg-322_2 "Permanent link")

```
apk add --no-cache --upgrade docker-cli-compose
```

Warning

For the plugin version, the command is **`docker compose`** (without a hyphen).

##### Installation as a Standalone Version[¶](https://docs.mailcow.email/getstarted/install/#installation-as-a-standalone-version "Permanent link")

```
LATEST=$(curl -Ls -w %{url_effective} -o /dev/null https://github.com/docker/compose/releases/latest) && \
LATEST=${LATEST##*/} && \
curl -L https://github.com/docker/compose/releases/download/$LATEST/docker-compose-$(uname -s)-$(uname -m) > /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```

Warning

For the standalone version, the command is **`docker-compose`** (with a hyphen).

* * *

SELinux Configuration (Optional)[¶](https://docs.mailcow.email/getstarted/install/#selinux-configuration-optional "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------------

On SELinux-enabled systems (e.g., CentOS 7):

1.   Check if the `container-selinux` package is installed:

```
rpm -qa | grep container-selinux
``` 
2.   Enable SELinux support in Docker:

    *   Edit `/etc/docker/daemon.json` and add `"selinux-enabled": true`:

```
{
  "selinux-enabled": true
}
```

    *   Restart the Docker daemon.

For more information, see the [container-selinux Readme](https://github.com/containers/container-selinux).

* * *

Installing mailcow[¶](https://docs.mailcow.email/getstarted/install/#installing-mailcow "Permanent link")
---------------------------------------------------------------------------------------------------------

1.   Clone the repository:

```
su
umask 0022
cd /opt
git clone https://github.com/mailcow/mailcow-dockerized
cd mailcow-dockerized
``` 
2.   Generate the configuration file:

```
./generate_config.sh
``` 
3.   Adjust the configuration if necessary:

```
nano mailcow.conf
``` 

* * *

Starting mailcow[¶](https://docs.mailcow.email/getstarted/install/#starting-mailcow "Permanent link")
-----------------------------------------------------------------------------------------------------

Download the images and start the containers:

Docker Compose (Plugin) Docker Compose (Standalone) 

```
docker compose pull
docker compose up -d
```

```
docker-compose pull
docker-compose up -d
```

Done!

You can now access **`https://${MAILCOW_HOSTNAME}/admin`** using the default credentials `admin` and the password `moohoo`.

* * *

Troubleshooting[¶](https://docs.mailcow.email/getstarted/install/#troubleshooting "Permanent link")
---------------------------------------------------------------------------------------------------

### MTU not equal to 1500 (e.g., OpenStack)[¶](https://docs.mailcow.email/getstarted/install/#mtu-not-equal-to-1500-eg-openstack "Permanent link")

Adjust the network settings in `docker-compose.yml`:

```
networks:
  mailcow-network:
    driver_opts:
      com.docker.network.driver.mtu: 1450
```

### No IPv6 on the Host System[¶](https://docs.mailcow.email/getstarted/install/#no-ipv6-on-the-host-system "Permanent link")

Disable IPv6 for the mailcow network if your host system does not support IPv6. More information can be found [here](https://docs.mailcow.email/post_installation/firststeps-disable_ipv6/).

* * *

Important Notes[¶](https://docs.mailcow.email/getstarted/install/#important-notes "Permanent link")
---------------------------------------------------------------------------------------------------

*   **Data Persistence**: Your data is stored in Docker volumes and remains intact even if you recreate or delete containers.
*   **Reverse Proxy**: If you are not using a reverse proxy, you should [redirect HTTP to HTTPS](https://docs.mailcow.email/manual-guides/u_e-80_to_443/).

2025-12-22 16:54:33

 Back to top 

 Copyright © 2026 mailcow Team & Community 

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

[](https://mailcow.email/ "mailcow.email")[](https://github.com/mailcow "github.com")[](https://x.com/mailcow_email "x.com")[](https://mailcow.social/@doncow "mailcow.social")
