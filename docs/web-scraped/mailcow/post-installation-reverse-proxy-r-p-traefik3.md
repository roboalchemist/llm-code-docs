# Source: https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/

Title: Traefik v3 (community supported) - mailcow: dockerized documentation

URL Source: https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/

Markdown Content:
Traefik v3 (community supported) - mailcow: dockerized documentation
===============
- [x] - [x] 

[Skip to content](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/#prerequisites)

#### All Commands are available according to the [Docker Compose Plugin](https://docs.docker.com/compose/install/linux/) and the [Standalone Version](https://docs.docker.com/compose/install/other/) syntax

[![Image 1: logo](https://docs.mailcow.email/assets/images/logo.svg)](https://docs.mailcow.email/ "mailcow: dockerized documentation")

 mailcow: dockerized documentation 

 Traefik v3 (community supported) 

*   [English](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/)
*   [Deutsch](https://docs.mailcow.email/de/post_installation/reverse-proxy/r_p-traefik3/)

[](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/?q= "Share")

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
        *   - [x]  Traefik v3 (community supported)  [Traefik v3 (community supported)](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/) Table of contents  
            *   [Prerequisites](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/#prerequisites)
            *   [Overview](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/#overview)
            *   [Update mailcow Configuration](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/#update-mailcow-configuration)
            *   [Configure Traefik](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/#configure-traefik)
            *   [Step 3: Restart Services](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/#step-3-restart-services)
            *   [Testing Your Configuration](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/#testing-your-configuration)
            *   [Troubleshooting](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/#troubleshooting)
                *   [Certificate Issues](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/#certificate-issues)
                *   [Routing Problems](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/#routing-problems)

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
*   [Prerequisites](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/#prerequisites)
*   [Overview](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/#overview)
*   [Update mailcow Configuration](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/#update-mailcow-configuration)
*   [Configure Traefik](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/#configure-traefik)
*   [Step 3: Restart Services](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/#step-3-restart-services)
*   [Testing Your Configuration](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/#testing-your-configuration)
*   [Troubleshooting](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/#troubleshooting)
    *   [Certificate Issues](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/#certificate-issues)
    *   [Routing Problems](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/#routing-problems)

Traefik v3 (community supported)
================================

Important

First read [the overview](https://docs.mailcow.email/post_installation/reverse-proxy/r_p/).

Danger

This is an community supported contribution. Feel free to provide fixes.

This tutorial explains how to set up mailcow with Traefik as a reverse proxy to handle HTTPS connections, domain routing, and certificate management.

Prerequisites[¶](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/#prerequisites "Permanent link")
-------------------------------------------------------------------------------------------------------------------------

*   Traefik v3.x installed and running
*   Domain names configured to point to your server according to [this guide](https://docs.mailcow.email/getstarted/prerequisite-dns/)

Overview[¶](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/#overview "Permanent link")
---------------------------------------------------------------------------------------------------------------

Traefik will handle all incoming web traffic and route appropriate requests to mailcow. This setup allows Traefik to:

*   Manage SSL certificates
*   Handle autodiscover and autoconfig services
*   Handle frontend UI
*   Pass ACME challenge responses for certificate validation of the mail server

Update mailcow Configuration[¶](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/#update-mailcow-configuration "Permanent link")
-------------------------------------------------------------------------------------------------------------------------------------------------------

First, modify your `mailcow.conf` or `.env` file to disable mailcow's built-in SSL handling:

```
# Disable mailcow autodiscover SAN
AUTODISCOVER_SAN=n

# Skip running ACME (acme-mailcow, Let's Encrypt certs) - y/n
SKIP_LETS_ENCRYPT=y
```

Configure Traefik[¶](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/#configure-traefik "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------

Traefik Dynamic Configuration Traefik Label Configuration 

Create or update your Traefik dynamic configuration file with the following content:

```
http:
  routers:
    mailcow:
      entryPoints: "websecure"
      rule: "Host(`mail.domain.com`)"
      service: mailcow-svc
      tls:
        certResolver: cloudflare

    mailcow-autoconfig:
      entryPoints: "websecure"
      rule: "(Host(`autoconfig.domain.com`) && Path(`/mail/config-v1.1.xml`))"
      service: mailcow-svc
      tls:
        certResolver: cloudflare

    mailcow-autodiscover:
      entryPoints: "websecure"
      rule: "(Host(`autodiscover.domain.com`) && Path(`/autodiscover/autodiscover.xml`))"
      service: mailcow-svc
      tls:
        certResolver: cloudflare

  services:
    mailcow-svc:
      loadBalancer:
        servers:
          - url: "http://mailcow-nginx-mailcow-1:8080"
```

Add / Update your `docker-compose.yaml` file:

```
services:
  certdumper:
    image: ghcr.io/kereis/traefik-certs-dumper:latest
    container_name: traefik_certdumper
    restart: unless-stopped
    network_mode: none
    command: --restart-containers mailcow_postfix-mailcow_1,mailcow_dovecot-mailcow_1
    volumes:
      - traefik_certs:/traefik:ro # mount your traefik certificate file
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - ./data/assets/ssl:/output:rw
    environment:
      - DOMAIN=domain.com
      - ACME_FILE_PATH=/traefik/cloudflare-acme.json # your traefik acme file

  # ...

  nginx:
    # ...
    expose:
      - 8080
    labels:
      - traefik.enable=true
      - traefik.http.routers.mailcow-autodiscover.entrypoints=websecure
      - traefik.http.routers.mailcow-autodiscover.rule=Host(`autodiscover.domain.com`) && Path(`/autodiscover/autodiscover.xml`)
      - traefik.http.routers.mailcow-autodiscover.tls.certresolver=cloudflare
      - traefik.http.routers.mailcow-autodiscover.service=mailcow-svc

      - traefik.http.routers.mailcow-autoconfig.entrypoints=websecure
      - traefik.http.routers.mailcow-autoconfig.rule=Host(`autoconfig.domain.com`)&& Path(`/mail/config-v1.1.xml`)
      - traefik.http.routers.mailcow-autoconfig.tls.certresolver=cloudflare
      - traefik.http.routers.mailcow-autoconfig.service=mailcow-svc

      - traefik.http.routers.mailcow.entrypoints=websecure
      - traefik.http.routers.mailcow.rule=Host(`mail.domain.com`)
      - traefik.http.routers.mailcow.tls=true
      - traefik.http.routers.mailcow.tls.certresolver=cloudflare
      - traefik.http.routers.mailcow.service=mailcow-svc

      - traefik.http.services.mailcow-svc.loadbalancer.server.port=8080
      - traefik.docker.network=proxy
    restart: always
    networks:
      mailcow-network:
        aliases:
          - nginx
      proxy:
```

**Important notes about this configuration:**

*   Replace `mail.domain.com`, `autoconfig.domain.com`, and `autodiscover.domain.com` with your actual domain names
*   `entryPoints: "websecure"` - replace it with your actual Traefik https entrypoint
*   `certResolver: cloudflare` - replace it with your actual certificate resolver

Step 3: Restart Services[¶](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/#step-3-restart-services "Permanent link")
----------------------------------------------------------------------------------------------------------------------------------------------

Restart both Traefik and mailcow to apply the changes:

docker compose (Plugin) docker-compose (Standalone) 

```
# Restart mailcow
cd /path/to/mailcow-dockerized
docker compose up -d
```

```
# Restart mailcow
cd /path/to/mailcow-dockerized
docker-compose up -d
```

Testing Your Configuration[¶](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/#testing-your-configuration "Permanent link")
---------------------------------------------------------------------------------------------------------------------------------------------------

1.   Visit `https://mail.domain.com` to check if the mailcow web interface loads properly
2.   Configure an email client to test autodiscover functionality
3.   Monitor Traefik logs for any routing or certificate errors

Troubleshooting[¶](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/#troubleshooting "Permanent link")
-----------------------------------------------------------------------------------------------------------------------------

### Certificate Issues[¶](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/#certificate-issues "Permanent link")

*   Check `traefik_certsdumper` for any errors / missing acme file
*   Ensure the Certificate file is correctly mounted

### Routing Problems[¶](https://docs.mailcow.email/post_installation/reverse-proxy/r_p-traefik3/#routing-problems "Permanent link")

*   Verify network connectivity between Traefik and mailcow
*   Check that the mailcow IP address is correct in Traefik configuration
*   Make sure all required ports are open in firewalls

2025-09-28 14:30:43

 Back to top 

 Copyright © 2026 mailcow Team & Community 

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

[](https://mailcow.email/ "mailcow.email")[](https://github.com/mailcow "github.com")[](https://x.com/mailcow_email "x.com")[](https://mailcow.social/@doncow "mailcow.social")
