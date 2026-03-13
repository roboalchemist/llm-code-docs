# Source: https://docs.iredmail.org/upgrade.ee.html

Title: Upgrade iRedMail Enterprise Edition

URL Source: https://docs.iredmail.org/upgrade.ee.html

Markdown Content:
iRedMail Enterprise Edition is a single binary program, upgrading is simple:

*   Download the latest version from our [website](https://www.iredmail.org/ee.html).
*   Stop the service.
*   Replace the program file and set correct owner / group / permission.
*   Start the service.
*   Login as global admin and click the `Upgrade` button. It handles all required changes like updating config files, applying SQL structure changes, etc.

That's all.

Let's take Linux and amd64 architecture for example, run commands below as `root` user:

```
wget -O /tmp/iredmail https://dl.iredmail.org/ee/iredmail-enterprise-latest-linux-amd64
chown root /tmp/iredmail
chmod 0500 /tmp/iredmail
service iredmail stop
mv /tmp/iredmail /usr/local/bin/iredmail
service iredmail start
```

After upgraded binary, please **empty the web browser cache first**, then login to the web UI as global admin. If there's some update for deployed software like Postfix, Dovecot, Nginx, etc, it will show a banner with `Upgrade` button, click it to finish the upgrade.

![Image 1](https://docs.iredmail.org/images/ee/dashboard-upgrade.png)

See Also
--------

*   [Install iRedMail Enterprise Edition](https://docs.iredmail.org/install.ee.html)
*   [ChangeLog of iRedMail Enterprise Edition](https://docs.iredmail.org/ee.changelog.html)
