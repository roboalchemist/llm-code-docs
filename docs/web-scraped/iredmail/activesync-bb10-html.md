# Source: https://docs.iredmail.org/activesync.bb10.html

Title: Exchange ActiveSync: Setup BlackBerry 10 devices

URL Source: https://docs.iredmail.org/activesync.bb10.html

Markdown Content:
Important Notes

*   SOGo provides **EAS (Exchange ActiveSync)** support, but not **EWS (Exchange Web Service)**.
*   **Outlook** 2013, 2016 for Windows works well with EAS.
*   Mainstream **mobile devices** (iOS, Android, BlackBerry 10) work well with EAS, they can sync mails, calendars, contacts, tasks.
*   Apple Mail.app, and Outlook for Mac support EWS. But not EAS.
*   Outlook 2010 for Windows supports MAPI.

Requirements
------------

*   iRedMail-0.9.0 or later releases is required.
*   You must choose to install SOGo groupware during iRedMail installation.

Step-by-step configuration
--------------------------

1: Open application `Settings`:

![Image 1](https://docs.iredmail.org/images/sogo/bb10.settings.png)

2: Click `Accounts`:

![Image 2](https://docs.iredmail.org/images/sogo/bb10.settings.accounts.png)

3: Click `Add Account` at the bottom:

![Image 3](https://docs.iredmail.org/images/sogo/bb10.settings.accounts.list.png)

4: Click `Advanced` at the bottom:

![Image 4](https://docs.iredmail.org/images/sogo/bb10.settings.add.account.png)

5: Choose `Microsoft Exchange ActiveSync`.

![Image 5](https://docs.iredmail.org/images/sogo/bb10.add.exchange.png)

6: Fill up the form with your server address and email account credential

*   Description: `you can type anything here`
*   Domain: `you can type anything here`
*   Username: `your full email address`
*   Email Address: `your full email address`
*   Password: `password of your email account`
*   Server Address: `your server name or IP address`
*   Port: `443`
*   Use SSL: checked

![Image 6](https://docs.iredmail.org/images/sogo/bb10.exchange.1.png)![Image 7](https://docs.iredmail.org/images/sogo/bb10.exchange.2.png)

That's all.
