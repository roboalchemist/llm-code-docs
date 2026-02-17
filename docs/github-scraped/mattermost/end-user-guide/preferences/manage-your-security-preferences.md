# Manage your security preferences

.. raw:: html

> \<div class=\"mm-badge mm-badge\--note\"\>

[\|plans-img-yellow\|](##SUBST##|plans-img-yellow|) Available on [Entry,
Professional, Enterprise, and Enterprise Advanced
plans](https://mattermost.com/pricing/)

</div>

Select your profile picture, select **Profile**, and then select
**Security** to configure your password, view access history, and to
view or logout of active sessions.

+----------------+------------------------------------------------------------------------------------------------------------------------------+
| **Security     | **Description**                                                                                                              |
| setting**      |                                                                                                                              |
+================+==============================================================================================================================+
| Password       | You may change your password if you\'ve logged in by email using Mattermost in a web browser or using the desktop app.       |
|                |                                                                                                                              |
|                | :::: important                                                                                                               |
|                | ::: title                                                                                                                    |
|                | Important                                                                                                                    |
|                | :::                                                                                                                          |
|                |                                                                                                                              |
|                | - If you sign in to Mattermost using a single sign-on service, you must update your password through your SSO service        |
|                |   account.                                                                                                                   |
|                | - **Password Security Enhancement**: From v11.0, Mattermost uses PBKDF2 password hashing for improved security. When you log |
|                |   in after your server upgrades to v11.0+, your password will be automatically migrated to the more secure format. If your   |
|                |   server is later downgraded to a version prior to v11.0, you may be unable to log in and will need to contact your system   |
|                |   administrator for a password reset.                                                                                        |
|                | ::::                                                                                                                         |
+----------------+------------------------------------------------------------------------------------------------------------------------------+
| Multi-factor   | If your system admin has enabled `multi-factor authentication                                                                |
| authentication | <administration-guide/configure/authentication-configuration-settings:enable multi-factor authentication>`{.interpreted-text |
| (MFA)          | role="ref"} (MFA), you can require a passcode in addition to your password to log-in to your Mattermost account.             |
|                |                                                                                                                              |
|                | You\'ll need to download a MFA passcode generation app, such as Google Authenticator or a similar app, and then set-up MFA   |
|                | in your Mattermost account.                                                                                                  |
|                |                                                                                                                              |
|                | **Download a passcode generation app**                                                                                       |
|                |                                                                                                                              |
|                | - Download Google Authenticator for an Apple device from                                                                     |
|                |   [iTunes](https://apps.apple.com/us/app/google-authenticator/id388497605)                                                   |
|                | - Download Google Authenticator for an Android device from [Google                                                           |
|                |   Play](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=en)                          |
|                |                                                                                                                              |
|                | **Enable MFA in Mattermost**                                                                                                 |
|                |                                                                                                                              |
|                | 1.  Open Mattermost in a web browser or the desktop app.                                                                     |
|                | 2.  In Mattermost, from your profile picture, select **Profile \> Security**.                                                |
|                | 3.  Under **Multi-factor Authentication**, select **Edit**.                                                                  |
|                |                                                                                                                              |
|                | ![Enable multi-factor authentication through your Mattermost user profile.](../../images/multi-factor-authentication.png)    |
|                |                                                                                                                              |
|                | 4.  Select **Add MFA to Account**.                                                                                           |
|                |                                                                                                                              |
|                | ![Add multi-factor authentication to your Mattermost user profile.](../../images/add-mfa-to-account.png)                     |
|                |                                                                                                                              |
|                | 5.  Scan the QR code or enter the **Secret** provided by Mattermost into the authenticator app.                              |
|                | 6.  In Mattermost, enter the **MFA Code** generated by the authenticator app.                                                |
|                | 7.  Select **Save**.                                                                                                         |
+----------------+------------------------------------------------------------------------------------------------------------------------------+
| Sign-in method | This option allows you to switch your login method between using email/username and password and                             |
|                | `single sign-on credentials <end-user-guide/access/access-your-workspace:single sign-on (sso)>`{.interpreted-text            |
|                | role="ref"}.                                                                                                                 |
|                |                                                                                                                              |
|                | You can configure this setting using Mattermost in a web browser or using the desktop app.                                   |
|                |                                                                                                                              |
|                | :::: note                                                                                                                    |
|                | ::: title                                                                                                                    |
|                | Note                                                                                                                         |
|                | :::                                                                                                                          |
|                |                                                                                                                              |
|                | While you can choose to log in with either set of credentials, you can only enable one login method at a time. For example,  |
|                | if AD/LDAP single sign-on is enabled, you can select **Switch to using AD/LDAP**, and enter your AD/LDAP credentials to      |
|                | switch login over to AD/LDAP. You\'ll need to enter the password for your email account to verify your existing credentials. |
|                | Following the change, you\'ll receive an email to confirm the action.                                                        |
|                | ::::                                                                                                                         |
+----------------+------------------------------------------------------------------------------------------------------------------------------+
| View access    | Using Mattermost in a browser or using the desktop app, you can access a chronological list of the last 20 login and logout  |
| history        | attempts, channel creations and deletions, account settings changes, or channel setting modifications made with your         |
|                | account.                                                                                                                     |
|                |                                                                                                                              |
|                | The details of the Session ID, which is a unique identifier for each Mattermost browser session, and IP Address of the       |
|                | action is recorded for audit log purposes.                                                                                   |
+----------------+------------------------------------------------------------------------------------------------------------------------------+
| View and log   | Sessions are created when you log in with your credentials a new browser on a device. Sessions let you use Mattermost for up |
| out of active  | to 30 days without having to log in again.                                                                                   |
| sessions       |                                                                                                                              |
|                | Using Mattermost in a browser or using the desktop app:                                                                      |
|                |                                                                                                                              |
|                | - Select **Logout** during an active session if you want to revoke automatic login privileges for a specific browser or      |
|                |   device.                                                                                                                    |
|                | - Select **More Info** to view browser and system details.                                                                   |
+----------------+------------------------------------------------------------------------------------------------------------------------------+
