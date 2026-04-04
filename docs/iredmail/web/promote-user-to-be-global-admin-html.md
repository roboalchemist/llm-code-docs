# Source: https://docs.iredmail.org/promote.user.to.be.global.admin.html

Title: Promote a mail user to be global admin

URL Source: https://docs.iredmail.org/promote.user.to.be.global.admin.html

Markdown Content:
Attention

Check out the lightweight on-premises email archiving software developed by iRedMail team: [Spider Email Archiver](https://spiderd.io/).

Warning

iRedAdmin open source edition supports only global admin, no per-domain admin. iRedAdmin-Pro supports both.

*   [Promote a mail user to be global admin](https://docs.iredmail.org/promote.user.to.be.global.admin.html#promote-a-mail-user-to-be-global-admin)
    *   [Summary](https://docs.iredmail.org/promote.user.to.be.global.admin.html#summary)
    *   [Promote user to be global admin](https://docs.iredmail.org/promote.user.to.be.global.admin.html#promote-user-to-be-global-admin)
        *   [SQL backends](https://docs.iredmail.org/promote.user.to.be.global.admin.html#sql-backends)
        *   [LDAP backends](https://docs.iredmail.org/promote.user.to.be.global.admin.html#ldap-backends)

    *   [Mark user as global domain admin with iRedAdmin-Pro](https://docs.iredmail.org/promote.user.to.be.global.admin.html#mark-user-as-global-domain-admin-with-iredadmin-pro)
    *   [See also](https://docs.iredmail.org/promote.user.to.be.global.admin.html#see-also)

Summary
-------

If you forgot password of existing global admin account, or mistakenly removed global admin, you can promote an existing mail user to be a global admin by following this tutorial.

### SQL backends

Let's say you want to promote existing mail user `john@example.com` to be **global admin**, here's SQL commands to achieve this goal (note: we use MySQL for example):

```
sql> USE vmail;
sql> UPDATE mailbox SET isadmin=1, isglobaladmin=1 WHERE username='john@example.com';
sql> INSERT INTO domain_admins (username, domain) VALUES ('john@example.com', 'ALL');
```

That's it, you can now login to iRedAdmin as `john@example.com` (with `john@example.com`'s password).

To promote user `smith@test.com` to be admin of domain `test.com` (Note: normal domain admin is only available in iRedAdmin-Pro):

```
sql> USE vmail;
sql> UPDATE mailbox SET isadmin=1, isglobaladmin=0 WHERE username='smith@test.com';
sql> INSERT INTO domain_admins (username, domain) VALUES ('smith@test.com', 'test.com');
```

### LDAP backends

To promote existing mail user `john@example.com` to be **global admin**:

*   Update LDAP object of mail user `john@example.com` (its full dn is: `mail=john@example.com,ou=Users,domainName=example.com,o=domains,dc=xx,dc=xx`), add LDAP attribute `enabledService=domainadmin` and `domainGlobalAdmin=yes`.

To promote existing mail user `smith@test.com` to be admin of domain `test.com`:

1.   Update LDAP object of mail user `smith@test.com` (its full dn is: `mail=smith@test.com,ou=Users,domainName=test.com,o=domains,dc=xx,dc=xx`), add LDAP attribute/value pair: `enabledService=domainadmin`.

2.   Update LDAP object of mail domain `test.com` (its full dn is: `domainName=test.com,o=domains,dc=xx,dc=xx`), add LDAP attribute/value pair: `domainAdmin=smith@test.com`.

Mark user as global domain admin with iRedAdmin-Pro
---------------------------------------------------

With iRedAdmin-Pro, you can mark user as either global domain admin or normal domain admin in user profile page, under tab `General`.

![Image 1](https://docs.iredmail.org/images/iredadmin/user_profile_general.png)

See also
--------

*   [Reset user password](https://docs.iredmail.org/reset.user.password.html)
*   [Password hashes used/supported by iRedMail](https://docs.iredmail.org/password.hashes.html)
