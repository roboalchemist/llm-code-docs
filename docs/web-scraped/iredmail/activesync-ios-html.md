# Source: https://docs.iredmail.org/activesync.ios.html

Title: Exchange ActiveSync: Setup iOS devices

URL Source: https://docs.iredmail.org/activesync.ios.html

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

1: Open application `Settings` on home screen:

![Image 1](https://docs.iredmail.org/images/sogo/ios.settings.png)

2: Click `Mails , Contacts, Calendars`:

![Image 2](https://docs.iredmail.org/images/sogo/ios.settings.accounts.png)

3: Click `Add Account`:

![Image 3](https://docs.iredmail.org/images/sogo/ios.settings.accounts.add.png)

4: Choose `Exchange`.

![Image 4](https://docs.iredmail.org/images/sogo/ios.settings.accounts.add.exchange.png)

5: Fill up the form with your server address and email account credential

*   Email: `your full email address`
*   Password: `password of your email account`
*   Description: `you can type anything here`

![Image 5](https://docs.iredmail.org/images/sogo/ios.exchange.1.png)

6: If it cannot auto discover server settings, you should fill up the form with server address and username.

*   Server: `your server name or IP address`
*   Username: `your full email address`

![Image 6](https://docs.iredmail.org/images/sogo/ios.exchange.2.png)

7: Choose items you want to sync to this mobile device:

![Image 7](https://docs.iredmail.org/images/sogo/ios.exchange.sync.items.png)

That's all.
