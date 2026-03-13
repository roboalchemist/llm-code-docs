# Source: https://docs.iredmail.org/ee.disable.2fa.html

Title: Disabling TOTP (2FA) for an Account

URL Source: https://docs.iredmail.org/ee.disable.2fa.html

Markdown Content:
iRedMail Enterprise Edition (EE) stores all configurations, including 2FA settings, in the SQLite database located at:

```
/opt/iredmail/conf/settings.db
```

To disable TOTP-based two-factor authentication (2FA) for a specific account, follow these steps:

*   Install the SQLite3 Command-Line Tool:

⚠️ Version Requirement

Ensure SQLite version 3.37.0 or later is installed. 
    *   RHEL-based (CentOS/Rocky/AlmaLinux): `yum install -y sqlite`

    *   Debian/Ubuntu: `apt -y install sqlite3`

    *   OpenBSD: `pkg_add sqlite3`

*   Connect to the database by run the following command:

`sqlite3 /opt/iredmail/conf/settings.db`

You should now see the `sqlite>` prompt.

*   Remove the TOTP entry by executing the following SQL command (replace `your-email@example.com` with the actual email address):

`DELETE FROM totp WHERE mail="your-email@example.com";`

*   Disconnect the database:

`.quit`

Note: The `.quit` command has a leading dot and no semicolon (`;`).

After completing these steps, the user will no longer be prompted for a TOTP code upon login.
