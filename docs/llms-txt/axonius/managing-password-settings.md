# Source: https://docs.axonius.com/docs/managing-password-settings.md

# Managing Authentication Settings

Use **Password** settings to manage password settings.

<Image alt="MngAuthSettings.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MngAuthSettings.png" />

**To open Authentication settings:**

1. From the top right corner of any page, click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(269\).png). The **System Settings** page opens.
2. In the Categories/Subcategories pane of the System Settings page, expand **Privacy and Security**, and select **Authentication**.

## Password Policy Settings

<Callout icon="📘" theme="info">
  Note

  Password Policy Settings are configured by default for Axonius-hosted (SaaS) customers and cannot be changed.
</Callout>

* **Enforce password complexity** - Toggle on to configure and enforce password complexity for new/changed Axonius user accounts' defined passwords.

  If switched on, specify the following parameters:

  * **Minimum password length** *(default: 12)* - Specify the minimum length for a defined password. The specified value must be equal to or greater than the sum of the remaining fields.
  * **Minimum lowercase letters required** *(default: 1)* - Specify the minimum lowercase letters required for an Axonius user account's (new/changed) defined password.
  * **Minimum uppercase letters required** *(default: 1)* - Specify the minimum uppercase letters required for an Axonius user account's (new/changed) defined password.
  * **Minimum numbers required** *(default: 1)* - Specify the minimum numbers required for an Axonius user account's (new/changed) defined password.
  * **Minimum special characters required** *(default: 0)* - Specify the minimum special characters required for an Axonius user account's (new/changed) defined password.

    * Special characters refer to the following list: \~!@#$%^&\*\_-+=\`|(){}\[]:;"'\< >,.?/

If switched on, when a user wants or needs to change their password, the password complexity requirements are displayed. For example,  [changing user password from the Manage Users page](/docs/manage-users#reset-a-user-password).

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1136).png" />

## Password Reset Settings

<Image alt="PasswordResetSettings" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PasswordResetSettings.png" />

* **Reset password link expiration (hours)** *(default: 48)* - The number of hours that the reset password link remains valid.

## Password Brute Force Settings

<Image alt="PasswordBruteForceSettings" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PasswordBruteForceSettings.png" />

<Callout icon="📘" theme="info">
  Note

  Password Brute Force Settings are configured by default for Axonius-hosted (SaaS) customers and cannot be changed.
</Callout>

* **Enable Brute force protection** - Toggle on to enforce a rate limit on user login and on [Changing user account password](/docs/account-settings).

  Axonius uses a fixed window with an elastic expiry strategy for rate limiting. This strategy helps circumvent bursts.
  **Example** - 10/minute rate limit is configured:

  * If the user login is attacked at the rate of **10 hits per minute**, the attacker is locked out of the resource for **1 minute after the last hit**.

  * If the user login is attacked at the rate of **1 hit per second for 1 minute (total of 60 hits)** - after passing the first 10 hits (after 10 seconds), the attacker is locked out of the resource for **1 minute**. As the attacker continues with additional attempts, each attempt after the rate limit is exceeded increases the lockout by the relative impact of a single hit on the defined window size. In the example, each hit increases the lockout by an additional 6 seconds (60 seconds / 10 hits = 6 seconds per hit).

  If switched on, specify the following parameters:

  * **Maximum attempts** *(default: 20, minimum: 5)* - Specify the maximum number of attempts allowed before the brute force protections are started.

<Callout icon="📘" theme="info">
  Note

  Both GET and POST requests are considered attempts.
</Callout>

* **Window size in minutes** *(default: 5)* - Specify the number of minutes to define a window size for the attempts allowed.
  * **Lock Type** *(default: IP address)* - Select **IP address** or **User name**.
    * User login rate limit is always per IP address.
    * [Changing user account password](/docs/account-settings) rate limiting can be done by either IP address or user name.

<Callout icon="📘" theme="info">
  Note

  When a specific user name is locked, Axonius  also locks the IP address associated with the session of that user name.
</Callout>

## Password Expiration Settings

<Image alt="PasswordExpirationSettings" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PasswordExpirationSettings.png" />

* **Enable password expiration** *(default: switched off)* - Toggle on to enforce password expiration for all users in the system.
* **Password expiration (days)** (default: 90) - The number of days that a password is valid. Users with expired passwords are required to change their password when logging in.

## Two-Factor Authentication Settings

Use two-factor authentication for Axonius platform users to add a second layer of protection in addition to the standard user password. Users will be send a verification code to the email address associated with their account. The code is valid for 10 minutes.

<Callout icon="📘" theme="info">
  Note

  User email addresses must be valid when using two-factor authentication. Invalid email addresses will result in users not being able to log in.
</Callout>

<Image align="center" alt="TwoFactorAuthentication.png" border={false} width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TwoFactorAuthentication.png" />

<Callout icon="📘" theme="info">
  Notes

  * After 3 failed attempts, the user will be locked out for 10 minutes.

  * Users **must** register their email to login with two-factor authentication.
</Callout>

**To enable two-factor authentication:**

* Under Two-Factor Authentication, toggle on **Require use of email verification code**.

When enabled, the user will receive an email at their registered email address with an authentication code to be entered into the Axonius login page. The code is valid for 10 minutes.

<Image align="center" alt="2FALoginScreen.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/2FALoginScreen.png" />