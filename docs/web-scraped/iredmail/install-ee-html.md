# Source: https://docs.iredmail.org/install.ee.html

Title: Install iRedMail Enterprise Edition

URL Source: https://docs.iredmail.org/install.ee.html

Published Time: Thu, 26 Feb 2026 14:16:46 GMT

Markdown Content:
Attention

Check out the lightweight on-premises email archiving software developed by iRedMail team: [Spider Email Archiver](https://spiderd.io/).

*   [Install iRedMail Enterprise Edition](https://docs.iredmail.org/install.ee.html#install-iredmail-enterprise-edition)
    *   [Summary](https://docs.iredmail.org/install.ee.html#summary)
    *   [System Requirements](https://docs.iredmail.org/install.ee.html#system-requirements)
        *   [Supported Linux and BSD distribution releases](https://docs.iredmail.org/install.ee.html#supported-linux-and-bsd-distribution-releases)
        *   [Hardware Requirements](https://docs.iredmail.org/install.ee.html#hardware-requirements)

    *   [Get a License](https://docs.iredmail.org/install.ee.html#get-a-license)
    *   [Download and run the installer](https://docs.iredmail.org/install.ee.html#download-and-run-the-installer)
    *   [Installation](https://docs.iredmail.org/install.ee.html#installation)
        *   [Choose preferred backend](https://docs.iredmail.org/install.ee.html#choose-preferred-backend)
        *   [Choose the components you want to deploy](https://docs.iredmail.org/install.ee.html#choose-the-components-you-want-to-deploy)
        *   [Required settings](https://docs.iredmail.org/install.ee.html#required-settings)
        *   [Review and deploy](https://docs.iredmail.org/install.ee.html#review-and-deploy)
        *   [Setup complete](https://docs.iredmail.org/install.ee.html#setup-complete)
        *   [Login to admin panel](https://docs.iredmail.org/install.ee.html#login-to-admin-panel)

    *   [See Also](https://docs.iredmail.org/install.ee.html#see-also)

Attention

*   All account passwords are generated randomly during deployment, stored in files under `/root/.iredmail/kv/` on your server, also organized in file `/root/iRedMail/iRedMail.tips`.
*   Need to migrate from existing iRedMail server? We have tutorials for you:
    *   [Migrate from iRedMail](https://docs.iredmail.org/iredmail.to.ee.html)
    *   [Migrate from iRedMail Easy](https://docs.iredmail.org/easy.to.ee.html)

Summary
-------

[**iRedMail Enterprise Edition**](https://www.iredmail.org/ee.html) is a web-based, on-premises iRedMail server installer and admin panel.

With iRedMail Enterprise, it's easy to deploy a full-featured email server, and keep the server up to date with just few clicks on the web UI, also manage or tune server settings.

We encourage all users to deploy new iRedMail servers with iRedMail Enterprise Edition and keep the server up to date.

If you prefer classic downloadable shell-based iRedMail installer, you can find the installation guides here: [Install iRedMail](https://docs.iredmail.org/index.html#install).

System Requirements
-------------------

Warning

*   iRedMail Enterprise Edition is designed to be deployed on a fresh / clean server, or installed on an iRedMail server which was deployed with the downloadable iRedMail installer or iRedMail Easy platform. For new installation, it will install and configure required components, so you should not have other network services installed or running on the server **BEFORE** installation.
*   iRedMail Enterprise Edition will install and configure all required software automatically.
*   Many ISPs block network port 25 by default, it's used for communication between mail servers and it must be open, otherwise your server may be not able to receive or / and send emails. Please contact your ISP to make sure it's not blocked, or ask them to unblock.

    *   Amazon AWS EC2. Request to [remove the throttle on port 25](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-port-25-throttle/).
    *   Google Cloud Platform.
    *   Microsoft Azure.
    *   Linode. Explained in the [blog post](https://www.linode.com/blog/linode/a-new-policy-to-help-fight-spam/), you can open a support ticket to request the Linode team to open it. If you [sign up to Linode with our reference](https://www.linode.com/?r=b4d04083428fb99ce452d84b57253d11692a0850), iRedMail Team's Linode account will receive a credit of $15-20.00. Thanks.
    *   DigitalOcean. According to [a post in their community](https://www.digitalocean.com/community/questions/port-25-465-is-blocked-how-can-i-enable-it), **SEEMS** impossible to unblock port 25, that means you can **NOT** run mail server on DigitalOcean VPS.

### Supported Linux and BSD distribution releases

Linux/BSD distribution releases supported by **iRedMail Enterprise Edition**:

| Distribution | Release Versions | Note |
| --- | --- | --- |
| CentOS Stream | 9, 10 | 10 is recommended. |
| Rocky Linux | 9, 10 | 10 is recommended. |
| AlmaLinux | 9, 10 | 10 is recommended. |
| Debian | 11, 12, 13 | 12 is recommended. |
| Ubuntu | 20.04, 22.04, 24.04 | 24.04 is recommended. |
| OpenBSD | 7.7 |  |

If you need to install iRedMail on FreeBSD, please use the [downloadable installer](https://www.iredmail.org/download.html) instead.

Notes:

*   [SOGo Groupware is not available on CentOS/Rocky/AlmaLinux 10 yet](https://bugs.sogo.nu/view.php?id=6118)
*   [SOGo Groupware is not available on Debian 13 (trixie) yet](https://bugs.sogo.nu/view.php?id=6145)
*   Z-Push (open source ActiveSync server) is not available on all CentOS/Rocky/AlmaLinux releases and Debian 13 (trixie) due to missing required `php-imap` package.

### Hardware Requirements

*   iRedMail requires at least `4 GB` memory for a low traffic production server with spam/virus scanning enabled.
*   If you plan to run SOGo Groupware (which offers webmail, calendar (CalDAV), contacts (CardDAV) and ActiveSync), you need a lot more memory. Consider 16 GB memory to support 500 ActiveSync clients.

Get a License
-------------

iRedMail Enterprise Edition requires a license key, you can request a free one-month trial license or purchase one by signing up or login to our [iRedMail Store](https://store.iredmail.org/).

Download and run the installer
------------------------------

Run commands below on the server to download iRedMail Enterprise Edition on Linux or OpenBSD, both x86_64/AMD64 and ARM64 are supported:

Attention

Please download it and save to `/usr/local/bin/iredmail`. This path is hard-coded in systemd service file to start iRedMail Enterprise.

*   For Linux, x86_64 / amd64:

```
cd /usr/local/bin/
wget -O iredmail https://dl.iredmail.org/ee/iredmail-enterprise-latest-linux-amd64
chown root:root iredmail
chmod 0500 iredmail
```

*   For Linux, ARM64 / aarch64:

```
cd /usr/local/bin/
wget -O iredmail https://dl.iredmail.org/ee/iredmail-enterprise-latest-linux-arm64
chown root:root iredmail
chmod 0500 iredmail
```

*   For OpenBSD, x86_64 / amd64 (also install required `bash` shell):

```
cd /usr/local/bin/
wget -O iredmail https://dl.iredmail.org/ee/iredmail-enterprise-latest-openbsd-amd64
chown root:wheel iredmail
chmod 0500 iredmail
pkg_add bash
```

*   For OpenBSD, arm64 aarch64 (also install required `bash` shell too):

```
cd /usr/local/bin/
wget -O iredmail https://dl.iredmail.org/ee/iredmail-enterprise-latest-openbsd-amd64
chown root:wheel iredmail
chmod 0500 iredmail
pkg_add bash
```

Launch the installer:

```
/usr/local/bin/iredmail
```

*   It runs a web server on port `8080` for initial deployment, please visit `http://your-server:8080` with your favourite web browser and go through the wizard to finish the installation.
*   After deployment succeeded, it closes port `8080` and runs on port `127.0.0.1:7793`. Nginx is configured to proxy requests to it through URI `/admin/` (this URI can be customized on web UI during installation), please visit `httpS://your-server/admin/` to access it to manage your iRedMail server.

Below are screenshots of the installation wizard.

Installation
------------

### Choose preferred backend

A backend is a SQL or LDAP database used to store mail domains and accounts. There're not big differences between them, so we suggest you choose the one you're familiar with for easier maintenance.

Since version **v1.6.0**, EE supports [using a remote MySQL or MariaDB server as backend database](https://docs.iredmail.org/ee.remote.mysql.html). This can be done during initial setup, not after.

![Image 1](https://docs.iredmail.org/images/ee/setup-backend.png)

### Choose the components you want to deploy

A component is a software (or software group, service) which implements some network service(s). On this page you can choose the components you want to deploy on your mail server.

![Image 2](https://docs.iredmail.org/images/ee/setup-components.png)

### Required settings

Few settings are required to deploy a mail server.

Note: while typing, it will validate the input value, please fill and wait for 1-3 seconds until it finished the validation.

![Image 3](https://docs.iredmail.org/images/ee/setup-required-settings.png)

### Review and deploy

Attention

All account passwords are generated randomly during deployment, and stored in files under `/root/.iredmail/kv/` on your own server, also organized in file `/root/iRedMail/iRedMail.tips` for your reference.

Review the settings:

![Image 4](https://docs.iredmail.org/images/ee/setup-review-and-deploy.png)

Click `Confirm and Deploy` button to deploy immediately:

![Image 5](https://docs.iredmail.org/images/ee/setup-deploy.png)

### Setup complete

Once setup finished successfully, you should see info for login to admin panel. Please visit the URL and login with given username and password.

Note: This is a global admin which has all privileges.

![Image 6](https://docs.iredmail.org/images/ee/setup-complete.png)

### Login to admin panel

After logged into admin panel, you can manage software components, tune server settings, manage mail accounts, etc.

![Image 7](https://docs.iredmail.org/images/ee/components.png)

![Image 8](https://docs.iredmail.org/images/ee/server-settings.png)

![Image 9](https://docs.iredmail.org/images/ee/domains.png)

See Also
--------

*   [EE: Use a Remote MySQL/MariaDB server as backend database](https://docs.iredmail.org/ee.remote.mysql.html)
*   [Upgrade iRedMail Enterprise Edition](https://docs.iredmail.org/upgrade.ee.html)
*   [Best Practice](https://docs.iredmail.org/ee.best.practice.html)
*   [ChangeLog of iRedMail Enterprise Edition](https://docs.iredmail.org/ee.changelog.html)
*   [Setup DNS records for your iRedMail server](https://docs.iredmail.org/setup.dns.html)
*   [Request a free cert from Let's Encrypt](https://docs.iredmail.org/letsencrypt.html)
*   [Configure mail client applications](https://docs.iredmail.org/index.html#mua)
