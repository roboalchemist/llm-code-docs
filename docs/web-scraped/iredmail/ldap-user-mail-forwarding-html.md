# Source: https://docs.iredmail.org/ldap.user.mail.forwarding.html

Title: LDAP: User mail forwarding

URL Source: https://docs.iredmail.org/ldap.user.mail.forwarding.html

Markdown Content:
Attention

Check out the lightweight on-premises email archiving software developed by iRedMail team: [Spider Email Archiver](https://spiderd.io/).

*   [LDAP: User mail forwarding](https://docs.iredmail.org/ldap.user.mail.forwarding.html#ldap-user-mail-forwarding)
    *   [Set mail forwarding with iRedAdmin-Pro](https://docs.iredmail.org/ldap.user.mail.forwarding.html#set-mail-forwarding-with-iredadmin-pro)
    *   [Set mail forwarding with phpLDAPadmin](https://docs.iredmail.org/ldap.user.mail.forwarding.html#set-mail-forwarding-with-phpldapadmin)
    *   [Related tutorial](https://docs.iredmail.org/ldap.user.mail.forwarding.html#related-tutorial)

Set mail forwarding with iRedAdmin-Pro
--------------------------------------

With iRedAdmin-Pro, you can simply add mail forwarding addresses in user profile page, under tab `Forwarding`.

Screenshot:

![Image 1](https://docs.iredmail.org/images/iredadmin/user_profile_mail_forwarding.png)

Set mail forwarding with phpLDAPadmin
-------------------------------------

To forward emails to other email addresses, you can add value in LDAP attribute `mailForwardingAddress` of user object.

For example, if you want to forward all emails sent to `user@domain.ltd` to two addresses: `forward@domain.ltd`, `user@gmail.com`. Steps:

1.   Login to phpLDAPadmin (https://[your_server]/phpldapadmin ) as LDAP root dn `cn=Manager,dc=xx,dc=xx` or 'cn=vmailadmin,dc=xx,dc=xx'.

2.   Find the LDAP object of email account which you want to forward emails in left panel of phpLDAPadmin, click the ldap object, phpLDAPadmin will show you detailed LDAP attributes/values in right panel.

3.   Add a new LDAP attribute `mailForwardingAddress` to this mail account, set value to first forwarding address `forward@domain.ltd`.

4.   Repeat step #3, add another email address: `user@gmail.com`.

5.   Save your changes.

Now all emails sent to `user@domain.ltd` will be forwarded to both `forward@domain.ltd` and `user@gmail.com`.

If you want to save a copy of forwarded email, please add `user@domain.ltd` as additional value of LDAP attribute `mailForwardingAddress`.

*   [SQL: user mail forwarding](https://docs.iredmail.org/sql.user.mail.forwarding.html)
