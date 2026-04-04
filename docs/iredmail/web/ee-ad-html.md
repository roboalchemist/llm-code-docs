# Source: https://docs.iredmail.org/ee.ad.html

Title: EE: Replicate mail accounts from Microsoft Active Directory

URL Source: https://docs.iredmail.org/ee.ad.html

Published Time: Thu, 26 Feb 2026 14:16:47 GMT

Markdown Content:
*   [EE: Replicate mail accounts from Microsoft Active Directory](https://docs.iredmail.org/ee.ad.html#ee-replicate-mail-accounts-from-microsoft-active-directory)
    *   [Requirements](https://docs.iredmail.org/ee.ad.html#requirements)
    *   [Replicate mail accounts from Microsoft Active Directory](https://docs.iredmail.org/ee.ad.html#replicate-mail-accounts-from-microsoft-active-directory)
        *   [Add Active Directory as an account resource](https://docs.iredmail.org/ee.ad.html#add-active-directory-as-an-account-resource)

    *   [See Also](https://docs.iredmail.org/ee.ad.html#see-also)

Since iRedMail Enterprise Edition **v1.6.0** ("EE" for short), EE supports replicating mail accounts from a Microsoft Active Directory ("AD" for short) server.

You can setup such replication anytime after iRedMail initial setup, with any backend database (MariaDB, PostgreSQL or OpenLDAP).

Requirements
------------

*   A working iRedMail server which runs iRedMail Enterprise Edition version v1.6.0 or later.
*   A working Active Directory server which allows connection from iRedMail server.
    *   iRedMail server connects to the AD server via port 389 or 636 (secure connection) using the LDAP protocol. Please make sure those ports are open to iRedMail server in your network firewall.
    *   Port 636 (a.k.a. LDAP over SSL) is recommended for security concern, otherwise the network between iRedMail and AD servers must be trustable.

*   You must specify a hosted email domain as target for such replication, accounts replicated from AD will be hosted under this target domain.

EE retrieves the full email addresses of accounts from specified LDAP attributes on AD server, the domain part of email address must be same as the target domain, otherwise these accounts will be ignored and not replicated.

For example, you choose to replicate mail accounts from AD to email domain `example.com` which is hosted on iRedMail server, and retrieve full email addresses of AD user accounts from LDAP attribute `userPrincipalName`, then the value of `userPrincipalName` must be a valid email address ends with `@example.com`.

Replicate mail accounts from Microsoft Active Directory
-------------------------------------------------------

### Add Active Directory as an account resource

Please login to EE as global admin, then click `Account Resource` on left sidebar. It shows you supported server types for account replication.

> Currently only AD is supported, [contact us](https://www.iredmail.org/contact.html) if you need to support other servers.

![Image 1](https://docs.iredmail.org/images/ee/account-resource/account-resource.png)

Click the **`Active Directory`** icon to add AD for account replication, it will redirect to replication management page.

*   It saves default values under **`Replication`**, **`Users`** and **`Groups`** tabs, but you may want to tune it to work with your AD server.

Fill AD server related settings under **`Connection`** tab.

*   **`Replicate accounts for domain`**: The email domain name you'd like to replicate for. It will search existing domains when you start typing, click the domain name you want to replicate.
*   **`Server address and port`**: The hostname of IP address of the AD server.
    *   Port 389 is plain/insecure connection by default. A valid ssl cert is required on server side to enable TLS secure connection support on this port.
    *   Port 636 is SSL secure connection. A valid ssl cert is required on server side.

*   **`Secure connection (TLS/SSL) is required`**: Toggle on this option if AD server has valid ssl cert and requires secure TLS/SSL connection.
*   **`Connection timeout`**: Timeout (in seconds) for connection to AD server.
*   **`Base DN`**: The container which contains all user / group accounts. For example, `cn=Users,dc=xx,dc=xx`.
*   **`Bind DN`**: The full LDAP dn used to login to AD. This bind dn is used to search all user / group accounts under base dn.
*   **`Bind Password`**: Password of the bind dn.

![Image 2](https://docs.iredmail.org/images/ee/account-resource/ad-connection.png)

After inputed all values, please click the **`Test connection`** link to verify those parameters. If all values are correct, it will show you message **`Connection succeeded`**, and retrieve up to 10 users and groups under the message. You can verify the retrieved attributes.

Click `Save Changes` after test succeeded.

![Image 3](https://docs.iredmail.org/images/ee/account-resource/ad-test-connection.png)

Click **`Replication`** tab:

*   **`Replication Interval`**: Set how often to replicate incrementally.
    *   Changes made on AD server will be replicated during next replication.

*   **`Replicate AD groups as mail alias accounts`**: Replicate AD group accounts, and create them as mail alias accounts locally.
    *   Group members will be replicated too. You can manage members on AD, and view the members on mail alias profile page on iRedMail server.
    *   If this option is not toggled on, the tab `Groups` will be hidden and invisible.

*   **`Delete accounts locally when they were removed from Active Directory`**: delete mail accounts and their application data (e.g. webmail preferences, calendar, contacts, per-user whitelists / blacklists, etc) on iRedMail server when they were removed from Active Directory.

Click `Save Changes` if you made some changes.

![Image 4](https://docs.iredmail.org/images/ee/account-resource/ad-replication.png)

Click **`Users`** tab:

*   **`LDAP Filter`**: The LDAP filter used to query against AD to find mail users. Default is `(|(objectClass=user)(objectClass=person))`.
*   **`Get full email address from attribute`**: Set the LDAP attribute name which stores account's full email address on AD.
    *   You can select from pre-defined attributes, or input your own one if the name is not listed on drop-down menu.

*   **`Replicate additional user profile`**: Besides email address, EE supports replicating additional user profiles from AD.
    *   Again, you can select from pre-defined attributes, or input your own one if the name is not listed on drop-down menu.
    *   Leave it empty to not replicate certain profiles.

Click `Save Changes` if you made some changes.

You may want to go back to `Connection` tab and click `Test connection` to check the replicated user profiles.

![Image 5](https://docs.iredmail.org/images/ee/account-resource/ad-users.png)

If you enables option **`Replicate AD groups as mail alias accounts`** under **`Replication`** tab, the `Groups` tab becomes visible. Click it to manage group replication related settings.

AD group will be replicated and created as mail alias account locally, you can set default access policy.

Click `Save Changes` if you made some changes.

Again, you may want to go back to `Connection` tab and click `Test connection` to check the replicated group profiles.

![Image 6](https://docs.iredmail.org/images/ee/account-resource/ad-groups.png)

You can now click **`Account Resources`** on left sidebar, it will show you all created account resources.

*   It displays brief info of the account resource, including server address and port, target domain, replication interval, and time of last replication.
*   Click `Edit` button to manage account resource.
*   Click `Replicate Now` to replicate immediately.
*   Click `Log` to check replication history.
*   Click `Delete` to delete this account resource.
*   Click the small status icon to enable or disable this account resource.

![Image 7](https://docs.iredmail.org/images/ee/account-resource/ad-list.png)

See Also
--------

*   [Install iRedMail Enterprise Edition](https://docs.iredmail.org/install.ee.html)
*   [Use a remote MySQL or MariaDB server as backend database](https://docs.iredmail.org/ee.remote.mysql.html)
*   [Best Practice](https://docs.iredmail.org/ee.best.practice.html)
*   [ChangeLog of iRedMail Enterprise Edition](https://docs.iredmail.org/ee.changelog.html)
