# Source: https://docs.iredmail.org/mailbox.sharing.html

Title: Mailbox sharing (Sharing IMAP folder with other users)

URL Source: https://docs.iredmail.org/mailbox.sharing.html

Published Time: Thu, 26 Feb 2026 14:16:50 GMT

Markdown Content:
Mailbox sharing (Sharing IMAP folder with other users)
===============

[![Image 1: iRedMail web site](https://docs.iredmail.org/images/logo-iredmail.png)iRedMail](https://www.iredmail.org/)//[Document Index](https://docs.iredmail.org/index.html)

This tutorial is available in other languages. [Help translate more](https://github.com/iredmail/docs)

[简体中文](https://docs.iredmail.org/mailbox.sharing-zh_CN.html) /

Mailbox sharing (Sharing IMAP folder with other users)
======================================================

Note

*   Since iRedMail-`0.9.0`, mailbox sharing are enabled by default, you don't need to modify any config file.
*   Since iRedMail-`0.7.0`, mailbox sharing related settings are configured in Dovecot but not enabled, what you need to do is enabling `acl` plugin as mentioned below.
*   Do not mistake "shared folders" for "public folders". For shared folders, users must select which folder they want to share and with who, using an interface, like IMAP command line or the ones available with Roundcube webmail or SOGo and SOGo connectors.

Enable mailbox sharing
----------------------

To enable mailbox sharing, please make sure you have plugin `acl` enabled in Dovecot config file `/etc/dovecot/dovecot.conf` like below:

*   For Dovecot-1.2:

```
# Part of file: /etc/dovecot/dovecot.conf

protocol lda {
    mail_plugins = ... acl
}

protocol imap {
    mail_plugins = ... acl imap_acl
}
```

*   For Dovecot-2.x:

```
# Part of file: /etc/dovecot/dovecot.conf

mail_plugins = ... acl

protocol imap {
    mail_plugins = ... imap_acl
}
```

Restarting Dovecot service is required.

Test shared folder
------------------

Example: share `from@domain.ltd`'s `Sent` folder to user `testing@domain.ltd`.

Warning

Do not forget the dot before each IMAP command.

```
# telnet localhost 143                # <- Type this.
* OK [...] Dovecot ready.

. login from@domain.ltd passwd        # <- Type this.
                                      # Login with full email address and password
. OK [... ACL ..] Logged in

. SETACL Sent testing@domain.ltd rli  # <- Type this.
                                      # Share folder `Sent` with user testing@domain.ltd,
                                      # with permissions: read (r), lookup (l) and insert (i).
. OK Setacl complete.

^]                                    # <- Press `Ctrl + ]` to exit telnet.
telnet> quit
```

Log into Roundcube webmail or SOGo as user `testing@domain.ltd`, you should see the shared folder.

Some more details:

*   After you shared folder with `SETACL` command, dovecot will insert a record in MySQL database.

    *   With OpenLDAP backend, it's stored in `iredadmin.share_folder`.
    *   With MySQL/MariaDB/PostgreSQL backends, it's stored in `vmail.share_folder`.

```
# mysql -uroot -p
mysql> USE vmail;
mysql> SELECT * FROM share_folder;
+-----------------+--------------------+-------+
| from_user       | to_user            | dummy |
+-----------------+--------------------+-------+
| from@domain.ltd | testing@domain.ltd | 1     |
+-----------------+--------------------+-------+
```

References
----------

*   [Mailbox sharing between users](https://doc.dovecot.org/configuration_manual/shared_mailboxes/shared_mailboxes/)
*   [Access Control Lists](https://doc.dovecot.org/configuration_manual/acl/)
*   Roundcubemail has official plugin `acl` to manage mailbox sharing.
*   SOGo groupware supports mailbox sharing by default: right-click IMAP folder, choose `Sharing`.
*   [Imap-ACL-Extension for Thunderbird](https://addons.mozilla.org/en-US/thunderbird/addon/imap-acl-extension/), manage acls/permissions for shared mailboxes/folders on imap servers.

See Also
--------

*   [How to create and manage public folder](https://docs.iredmail.org/public.folder.html)

All documents are available in [GitHub repository](https://github.com/iredmail/docs/), and published under [Creative Commons](http://creativecommons.org/licenses/by-nd/3.0/us/) license. You can [download the latest version](https://github.com/iredmail/docs/archive/master.zip) for offline reading. If you found something wrong, please do [contact us](https://www.iredmail.org/contact.html) to fix it.
