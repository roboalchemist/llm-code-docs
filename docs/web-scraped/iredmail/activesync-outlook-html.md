# Source: https://docs.iredmail.org/activesync.outlook.html

Title: Exchange ActiveSync: Setup Outlook 2013 for Windows

URL Source: https://docs.iredmail.org/activesync.outlook.html

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
*   You must choose to install SOGo groupware during iRedMail installation. If you install SOGo after iRedMail installation, don't forget to install `sogo-activesync` package for ActiveSync support.
*   Outlook 2013 for Windows. Earlier releases of Outlook for Windows doesn't work.

Step-by-step configuration
--------------------------

1: Open application `Outlook 2013`:

![Image 1](https://docs.iredmail.org/images/sogo/outlook.2013.app.png)

2: Add a new account in Outlook, in `Auto Account Setup` page, please choose 
```
Manual setup
   or additional server types
```
, then click `Next`:

![Image 2](https://docs.iredmail.org/images/sogo/outlook.add.account.png)

3: In `Choose Service` page, please choose 
```
Outlook.com or Exchange ActiveSync
   compatible service
```
, then click `Next`:

![Image 3](https://docs.iredmail.org/images/sogo/outlook.choose.service.png)

4: In `Server Settings` page, fill up the form with your server address and email account credential, then click `Next`:

*   Your Name: `your full name`
*   E-mail Address: `your full email address`
*   Mail server: `your server name or IP address`
*   User Name: `your full email address`
*   Password: `password of your email account`

![Image 4](https://docs.iredmail.org/images/sogo/outlook.server.settings.png)

After you click `Next`, Outlook will start verifying your email account, please wait and you will see below screen after verified:

![Image 5](https://docs.iredmail.org/images/sogo/outlook.test.account.settings.png)

That's all.

References
----------

*   [SOGo web site](http://sogo.nu/)
*   Outlook plugins:

    *   [Outlook CalDav Synchronizer](https://github.com/aluxnimm/outlookcaldavsynchronizer)

> Outlook Plugin, which synchronizes events, tasks and contacts(beta) between Outlook and Google, SOGo, Horde or any other CalDAV or CardDAV server. Supported Outlook versions are 2016, 2013, 2010 and 2007.

*   [How to disable Simplified Account Creation in Outlook 2016](https://support.microsoft.com/en-us/help/3189194/how-to-disable-simplified-account-creation-in-outlook-2016)
