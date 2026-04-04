# Source: https://docs.iredmail.org/activesync.android.html

Title: Exchange ActiveSync: Setup Android devices

URL Source: https://docs.iredmail.org/activesync.android.html

Markdown Content:
Important Notes

*   SOGo provides **EAS (Exchange ActiveSync)** support, but not **EWS (Exchange Web Service)**.
*   **Outlook** 2013, 2016 for Windows works well with EAS.
*   Mainstream **mobile devices** (iOS, Android, BlackBerry 10) work well with EAS, they can sync mails, calendars, contacts, tasks.
*   Apple Mail.app, and Outlook for Mac support EWS. But not EAS.
*   Outlook 2010 for Windows supports MAPI.

iRedMail doesn't integrate [OpenChange](http://www.openchange.org/) and [Samba4](http://www.samba.org/) for native MAPI support.

Requirements
------------

*   iRedMail-0.9.0 or later releases is required.
*   You must choose to install SOGo groupware during iRedMail installation.

Step-by-step configuration
--------------------------

1: Open application `Mail` on home screen:

![Image 1](https://docs.iredmail.org/images/sogo/android.mail.png)

2: Fill your full email address and password in `Account Setup` page:

![Image 2](https://docs.iredmail.org/images/sogo/android.account.setup.png)

3: If it asks you to choose `Account Type`, please choose `Exchange`:

![Image 3](https://docs.iredmail.org/images/sogo/android.account.type.png)

4: In detailed account setup page, fill up the form with your server address and email account credential

*   Domain\Username: `your full email address`
*   Password: `password of your email account`
*   Server: `your server name or IP address`
*   Port: `443`

Please also check `Use secure connection (SSL)` and `Accept all SSL certificates`:

![Image 4](https://docs.iredmail.org/images/sogo/android.account.details.png)

5: In `Account Settings` page, you can choose Push. it's all up to you.

![Image 5](https://docs.iredmail.org/images/sogo/android.account.settings.png)

6: Choose a name for your Exchange account.

![Image 6](https://docs.iredmail.org/images/sogo/android.account.name.png)

Click `Next` to finish account setup. That's all.
