# Source: https://docs.axonius.com/docs/managing-timeout.md

# Managing Session Settings

Use Session Settings to manage user authentication and session behavior. These settings allow you to:

* Set [Session Timeout](#setting-timeout-settings) and [Session Lifetime](#session-lifetime-settings) - Require users to reauthenticate after a period of inactivity or after a session reaches the set maximum duration.

* Manage [Concurrent Sessions](#concurrent-sessions-settings) - Control the number of simultaneous active sessions a user can have.

An entry is written to the **Activity Log** whenever any of these settings are enabled or disabled.

**To open the Session Settings page**

1. From the top right corner of any page, click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(269\).png). The **System Settings** page opens.
2. In the Categories/Subcategories pane of the System Settings page, expand **Privacy and Security**, and select **Session**.

## Setting Timeout Settings

Use **Session Timeout Settings** to require a user to reauthenticate when there has been no activity for the configured amount of time.

<Image alt="TimeOutSettings" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TimeOutSettings.png" />

* **Enable session timeout** *(default: disabled)* - Toggle on to enable user session timeout. In this case, session timeout applies for all users based on the **Session idle timeout (minutes)** configuration.
* **Disable 'Remember me'** -
  * Select this option to disable the remember me option on the login page. In this case, the **Remember me** checkbox is not displayed on the login page.
  * Clear this option to enable the remember me option on the login page. In this case, the **Remember me** checkbox is displayed on the login page.
* **Session idle timeout (minutes)** *(default: 1440)* - Set the length of time (in minutes) that a user can remain inactive before the system automatically ends a user session and logs that user off the system.
  * This setting is displayed only if **Enable session timeout** is switched on.
  * This setting is ignored if a specific user has selected the **Remember me** option in the **Axonius Login** dialog.
  * A warning dialog is displayed one minute before the user's session is about to time out.
* **Display browser push notifications to warn about session expiry when session is not in an active tab** - Select this option to have the browser send a push notification *one minute* before an Axonius session is about to expire. This notification is sent when the Axonius session is not in an active tab. Click the notification to continue working with Axonius. In order to receive the browser notification, you have to enable notifications on your browser for the Axonius IP address.

## Session Lifetime Settings

Use **Session Lifetime Settings** to require a user to reauthenticate at the end of the configured session lifetime.

<Image alt="SessionLifetimeSetting.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SessionLifetimeSetting.png" />

* **Enable session lifetime** *(default: disabled)* - Toggle on to enable session lifetime. Session lifetime applies for all users.
* **Session lifespan (hours)** *(default: 8 hours)* - Set the maximum length of a user session. When this limit is reached, the user is required to reauthenticate.
* **Notification before logging off (minutes)** *(default: 10 minutes)* - Set the length of time (in minutes) before the log off to notify the user that they will be logged off for reauthentication. This gives them time to save any unsaved work.
* **Display browser notification for inactive session tab** - Select this option to have the browser send a push notification according to the time configured in **Notification before logging off (minutes)**. This notification is sent only when the Axonius session is not in an active browser tab. Click the notification to switch to the Axonius session tab to save unsaved work. In order to receive the browser notification, you have to enable notifications on your browser for the Axonius IP address.

## Concurrent Session Settings

Use **Concurrent Session Settings** to limit the number of active, simultaneous sessions a single user can have. This prevents a user from being logged in from multiple devices or browsers at the same time.

<Image alt="ConcurrentSessionSettings.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ConcurrentSessionSettings.png" />

* **Activate maximum concurrent sessions** *(default: disabled)* - Toggle on to limit the number of concurrent sessions a user can have.
* **Maximum concurrent sessions per user** *(default:3)* - Set the maximum number of sessions allowed per user (from 1 to 10). When a user reaches this limit, their oldest session is automatically terminated.

<Callout icon="📘" theme="info">
  Note

  * A new tab in the same browser is not considered a new session, as the user isn't required to reauthenticate.

  * Logging in with a different browser is considered a new session, even on the same device, as the user is required to reauthenticate.

  * If you enable this setting when a user already exceeds the limit, all sessions over the limit will be terminated.

  * An entry is written to the **Activity Log** whenever the maximum number of concurrent sessions is updated and when a user's session is terminated.
</Callout>