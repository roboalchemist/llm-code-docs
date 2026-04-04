# Source: https://docs.iredmail.org/ee.remote.mysql.html

Title: EE: Use a Remote MySQL/MariaDB server as backend database

URL Source: https://docs.iredmail.org/ee.remote.mysql.html

Published Time: Thu, 26 Feb 2026 14:16:47 GMT

Markdown Content:
*   [EE: Use a Remote MySQL/MariaDB server as backend database](https://docs.iredmail.org/ee.remote.mysql.html#ee-use-a-remote-mysqlmariadb-server-as-backend-database)
    *   [Requirements](https://docs.iredmail.org/ee.remote.mysql.html#requirements)
    *   [Initial Setup](https://docs.iredmail.org/ee.remote.mysql.html#initial-setup)
    *   [Post-install management](https://docs.iredmail.org/ee.remote.mysql.html#post-install-management)
    *   [See Also](https://docs.iredmail.org/ee.remote.mysql.html#see-also)

Since iRedMail Enterprise Edition **v1.6.0** ("EE" for short), EE supports using a remote MySQL or MariaDB server as backend database.

**This can be done during initial setup, not after.**

Requirements
------------

*   A working remote MySQL or MariaDB server.
    *   A valid ssl cert for secure connection on server side is highly recommended for security concern.

*   iRedMail server must be running one of below Linux/BSD distributions and releases:
    *   CentOS Stream 10 or later
    *   Rocky 10 or later
    *   AlmaLinux 10 or later
    *   Debian 13 or later
    *   Ubuntu 24.04 or later
    *   OpenBSD 7.8 or later

*   **Network latency** of SQL connection between iRedMail server and remote SQL server **should NOT be longer than 20 ms**. Long latency causes bad performance and user experience.

Initial Setup
-------------

During initial setup, you can choose to use a remote MySQL or MariaDB server as backend database to store mail accounts and application data.

![Image 1](https://docs.iredmail.org/images/ee/remote-mysql/setup-1.png)![Image 2](https://docs.iredmail.org/images/ee/remote-mysql/setup-2.png)

Post-install management
-----------------------

After initial setup, you can manage parameters of remote MySQL/MariaDB server.

*   Login to EE as global admin
*   Click `Server Settings` ->`Remote MySQL Server`

Notes:

*   SQL root password is hidden and not transferred on network due to security concern.
*   You can still click button `Test Connection` to test connection to remote SQL server.
*   If you need to update SQL root password, please click the `Update` button, it will show you an input box, input the new password and click `Save Changes` to update it.

![Image 3](https://docs.iredmail.org/images/ee/remote-mysql/server-settings.png)

See Also
--------

*   [Install iRedMail Enterprise Edition](https://docs.iredmail.org/install.ee.html)
*   [Best Practice](https://docs.iredmail.org/ee.best.practice.html)
*   [ChangeLog of iRedMail Enterprise Edition](https://docs.iredmail.org/ee.changelog.html)
