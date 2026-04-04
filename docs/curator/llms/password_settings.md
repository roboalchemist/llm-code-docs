# Source: https://docs.curator.interworks.com/best_practices/security/password_settings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Password Settings

> Configure password complexity requirements and security policies for enhanced site security

It’s always a good idea to keep your site as secure as possible. Beyond settings like https, multi-factor authentication
and firewalls, you can now set better password policies. Password complexity options allow you to set stricter rules for
passwords to prevent users from creating weak passwords. Password expiration allows you to require users to change their
passwords on a frequent basis. Let’s take a deeper look into these two settings.

## Password Complexity Options

Password complexity allows you to set rules to require stronger passwords. To enable and configure password complexity
options, go to Backend > Settings > Curator > Portal Settings. Under the general tab, you will find a section called
Security. Expand that, and you can now find the Password Complexity Options toggle. Please note that in order to view
and configure this setting, you must have Password Change or Password Reset settings (or both) enabled, which require
you to use Tableau or Curator as your authentication:

Once you toggle on Password Complexity Options, you will see three different options you can set to require stronger passwords:

It’s a good idea to set a long length requirement, the longer the better, but don’t go too overboard or your users may
want to write their passwords down on a Post-it note attached to their display. The first time you enable this setting,
it will default to 10.

Once enabled, you will now see these requirements on pages that allow you to set a password:

## Password Expiration

Password expiration can be found on the same Portal Settings page and tab, right next to the Password Complexity
Options. Like the prior option we looked at, you must have Password Change or Password Reset enabled to be able to view
password expiration. Click the toggle to enable it, and you will now see you can set the number of days until user
passwords will expire:

If enabled, the login page will check to see if the user’s password is expired and, if so, redirect them to a page to
set a new password. Once this is done, they will be able to log in with the new password.

Setting a prudent expiration date, such as 90 days, and turning on password complexity options are easy, effective ways
to make your Curator portal even more secure.
