# Source: https://docs.iredmail.org/manage.subscribeable.mailing.lists.html

Title: Manage subscribeable mailing lists

URL Source: https://docs.iredmail.org/manage.subscribeable.mailing.lists.html

Published Time: Thu, 26 Feb 2026 14:16:50 GMT

Markdown Content:
Attention

Check out the lightweight on-premises email archiving software developed by iRedMail team: [Spider Email Archiver](https://spiderd.io/).

*   [Manage subscribeable mailing lists](https://docs.iredmail.org/manage.subscribeable.mailing.lists.html#manage-subscribeable-mailing-lists)
    *   [Summary](https://docs.iredmail.org/manage.subscribeable.mailing.lists.html#summary)
    *   [Manage subscribeable mailing lists with iRedAdmin-Pro](https://docs.iredmail.org/manage.subscribeable.mailing.lists.html#manage-subscribeable-mailing-lists-with-iredadmin-pro)
    *   [Manage subscribeable mailing lists with command line tool](https://docs.iredmail.org/manage.subscribeable.mailing.lists.html#manage-subscribeable-mailing-lists-with-command-line-tool)
    *   [References](https://docs.iredmail.org/manage.subscribeable.mailing.lists.html#references)
    *   [See Also](https://docs.iredmail.org/manage.subscribeable.mailing.lists.html#see-also)

Summary
-------

Since iRedMail-0.9.8, iRedMail integrates mlmmj as mailing list manager.

Manage subscribeable mailing lists with iRedAdmin-Pro
-----------------------------------------------------

With [iRedAdmin-Pro](https://www.iredmail.org/admin_panel.html), you can easily manage mailing list accounts with its web UI. Screenshots of mailing list profile pages in iRedAdmin-Pro:

Profile page:

![Image 1](https://docs.iredmail.org/images/iredadmin/mailinglist_profile.png)

Allow users to subscribe from web page:

![Image 2](https://docs.iredmail.org/images/iredadmin/mailinglist_newsletter.png)

Instruction to generate a newsletter sign up form:

![Image 3](https://docs.iredmail.org/images/iredadmin/mailinglist_signup_code.png)

Manage subscribeable mailing lists with command line tool
---------------------------------------------------------

iRedMail integrates [`mlmmjadmin`](https://github.com/iredmail/mlmmjadmin) (a RESTful API server developed by iRedMail team) to help you manage mlmmj mailing lists, it also offers command line script `/opt/mlmmjadmin/tools/maillist_admin.py` for system administrators.

Attention

*   All settings used to create or update mailing list profiles are listed on [mlmmjadmin API document](https://github.com/iredmail/mlmmjadmin/blob/master/docs/API.md).
*   Since mlmmjadmin-3.0, it requires Python 3.

Available commands:

*   `create`: Create a new mailing list account with additional setting:
*   `info`: Show settings of an existing mailing list account
*   `update`: Update an existing mailing list account
*   `delete`: Delete an existing mailing list account
*   `subscribers`: Show all subscribers
*   `has_subscriber`: Check whether mailing list has given subscriber.
*   `subscribed`: Show all subscribed lists of a given subscriber.
*   `add_subscribers`: Add new subscribers to mailing list.
*   `remove_subscribers`: Remove existing subscribers from mailing list.

Examples:

*   Create a new mailing list account with additional setting:

`python3 maillist_admin.py create list@domain.com only_subscriber_can_post=yes disable_archive=no`

*   Get settings of an existing mailing list account

`python3 maillist_admin.py info list@domain.com`

*   Update an existing mailing list account

`python3 maillist_admin.py update list@domain.com only_moderator_can_post=yes disable_subscription=yes`

*   Delete an existing mailing list account

`python3 maillist_admin.py delete list@domain.com archive=yes`

*   Add new subscribers `user1@gmail.com` and `user2@hotmail.com`:

```
python3 maillist_admin.py add_subscribers list@domain.com user1@gmail.com user2@hotmail.com
```

*   List all subscribers:

`python3 maillist_admin.py subscribers list@domain.com`

*   Show subscribed lists of a given subscriber:

`python3 maillist_admin.py subscribed subscriber@domain.com`

*   Check whether mailing list has given subscriber:

`python3 maillist_admin.py has_subscriber list@domain.com subscriber@gmail.com`

References
----------

*   Mlmmj:
    *   [web site](http://mlmmj.org/)
    *   [Tunable parameters](http://mlmmj.org/docs/tunables/)
    *   [Postfix integration](http://mlmmj.org/docs/readme-postfix/)

*   [mlmmjadmin](https://github.com/iredmail/mlmmjadmin): RESTful API server used to manage mlmmj mailing lists. Developed and maintained by iRedMail team.

See Also
--------

*   [Integrate mlmmj mailing list manager in iRedMail (OpenLDAP backend)](https://docs.iredmail.org/integration.mlmmj.ldap.html)
*   [Integrate mlmmj mailing list manager in iRedMail (MySQL/MariaDB backends)](https://docs.iredmail.org/integration.mlmmj.mysql.html)
*   [Integrate mlmmj mailing list manager in iRedMail (PostgreSQL backend)](https://docs.iredmail.org/integration.mlmmj.pgsql.html)
