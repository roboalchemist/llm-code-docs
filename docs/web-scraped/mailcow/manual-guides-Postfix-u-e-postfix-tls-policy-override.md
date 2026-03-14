# Source: https://docs.mailcow.email/manual-guides/Postfix/u_e-postfix-tls_policy_override/

Title: TLS-Policy override - mailcow: dockerized documentation

URL Source: https://docs.mailcow.email/manual-guides/Postfix/u_e-postfix-tls_policy_override/

Markdown Content:
TLS-Policy override - mailcow: dockerized documentation
===============
- [x] - [x] 

[Skip to content](https://docs.mailcow.email/manual-guides/Postfix/u_e-postfix-tls_policy_override/#background)

#### All Commands are available according to the [Docker Compose Plugin](https://docs.docker.com/compose/install/linux/) and the [Standalone Version](https://docs.docker.com/compose/install/other/) syntax

[![Image 1: logo](https://docs.mailcow.email/assets/images/logo.svg)](https://docs.mailcow.email/ "mailcow: dockerized documentation")

 mailcow: dockerized documentation 

 TLS-Policy override 

*   [English](https://docs.mailcow.email/manual-guides/Postfix/u_e-postfix-tls_policy_override/)
*   [Deutsch](https://docs.mailcow.email/de/manual-guides/Postfix/u_e-postfix-tls_policy_override/)

[](https://docs.mailcow.email/manual-guides/Postfix/u_e-postfix-tls_policy_override/?q= "Share")

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
        *   - [x]  TLS-Policy override  [TLS-Policy override](https://docs.mailcow.email/manual-guides/Postfix/u_e-postfix-tls_policy_override/) Table of contents  
            *   [Background](https://docs.mailcow.email/manual-guides/Postfix/u_e-postfix-tls_policy_override/#background)
            *   [Procedure](https://docs.mailcow.email/manual-guides/Postfix/u_e-postfix-tls_policy_override/#procedure)
            *   [Example use cases](https://docs.mailcow.email/manual-guides/Postfix/u_e-postfix-tls_policy_override/#example-use-cases)

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
*   [Background](https://docs.mailcow.email/manual-guides/Postfix/u_e-postfix-tls_policy_override/#background)
*   [Procedure](https://docs.mailcow.email/manual-guides/Postfix/u_e-postfix-tls_policy_override/#procedure)
*   [Example use cases](https://docs.mailcow.email/manual-guides/Postfix/u_e-postfix-tls_policy_override/#example-use-cases)

TLS-Policy override
===================

This guide should only be used by experienced administrators

This guide is intended for experienced administrators who need to adjust TLS policies for specific domains or IP addresses.

 Improper changes to TLS settings can lead to delivery problems or insecure connections.

* * *

Background[¶](https://docs.mailcow.email/manual-guides/Postfix/u_e-postfix-tls_policy_override/#background "Permanent link")
----------------------------------------------------------------------------------------------------------------------------

Since the **mailcow update in September 2025**, mailcow also checks **TLS policies of the recipient for outgoing SMTP connections**.

 Previously, this check applied only to incoming emails or to domains where the feature was explicitly enabled.

In rare cases this can cause emails to no longer be delivered — for example, if a recipient domain publishes faulty or invalid **TLSA records (DANE)**.

 Because Postfix (and thus mailcow) treats these records as authoritative according to [RFC 7672](https://datatracker.ietf.org/doc/html/rfc7672), delivery will be refused in such cases.

If you still want to deliver emails to such affected recipients — for example as a **workaround for faulty TLSA records** — you can set an override policy for the respective domain via the TLS policy management.

 Note that this deliberately bypasses security checks and should only be used **temporarily** or **with proper documentation**.

* * *

Procedure[¶](https://docs.mailcow.email/manual-guides/Postfix/u_e-postfix-tls_policy_override/#procedure "Permanent link")
--------------------------------------------------------------------------------------------------------------------------

1.   **Log in:**

 Sign in to the mailcow web interface as an administrator.

2.   **Navigation:**

 Open **Email > Configuration**.

3.   **Open TLS Policies:**

 Switch to the **TLS Policies** tab.

4.   **Add entry:**

 Click **Add TLS policy entry**.

5.   **Set target:**

 Enter the affected domain or IP address in the **Target** field for which the policy should apply (e.g. `example.com`).

6.   **Select policy:**

 In the **Policy** dropdown choose one of the following options:

    *   `none` – TLS will not be used, even if the target server offers it. 
    *   `may` – TLS will be used if available, but is not required. 
    *   `encrypt` – TLS is required, but certificates are not verified. 
    *   `verify` – TLS is required and the server certificate is verified. 
    *   `secure` – TLS is required; certificate and hostname must be valid. 
    *   `dane` – TLS according to DANE policies, falls back to opportunistic TLS without a TLSA record. 
    *   `dane-only` – TLS only via valid DANE/TLSA records, no fallback. 
    *   `fingerprint` – TLS is required; the certificate must match a stored fingerprint.

_Example:_

 If a domain has faulty TLSA entries, you can temporarily choose `may` or `encrypt` to allow delivery.

7.   **Optional parameters:**

 In the **Parameters** field you can specify additional Postfix options, e.g.: `protocols=!SSLv2,!SSLv3` to disable legacy protocols.

Separate parameters from each other with a blank line.

8.   **Activate policy:**

 Enable the **Active** option so the policy is applied.

9.   **Save:**

 Click **Add** to create and activate the policy.

The policy is now active.

 A **restart of mailcow or Postfix is not required** — the change takes effect immediately.

* * *

Example use cases[¶](https://docs.mailcow.email/manual-guides/Postfix/u_e-postfix-tls_policy_override/#example-use-cases "Permanent link")
------------------------------------------------------------------------------------------------------------------------------------------

| Situation | Recommended policy | Description |
| --- | --- | --- |
| Target domain has invalid TLSA records | `may` | Opportunistic TLS to allow delivery despite faulty DANE entries. |
| Internal test systems without valid certificates | `encrypt` | Enforces encryption without certificate verification. |
| Partner domain with correctly configured DANE | `dane` | Secure delivery via DNSSEC-validated TLSA records. (mailcow default when recipient domain is compatible) |
| High-security environment with known certificates | `fingerprint` | Explicit certificate pinning for maximum control. |

Note

As soon as faulty TLSA records or certificate issues on the recipient side are resolved, you should **remove the temporarily set policy or reset it to the default value** to preserve the integrity of the TLS security model.

2025-10-09 17:06:53

 Back to top 

 Copyright © 2026 mailcow Team & Community 

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

[](https://mailcow.email/ "mailcow.email")[](https://github.com/mailcow "github.com")[](https://x.com/mailcow_email "x.com")[](https://mailcow.social/@doncow "mailcow.social")
