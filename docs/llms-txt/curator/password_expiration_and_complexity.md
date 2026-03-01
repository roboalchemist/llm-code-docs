# Source: https://docs.curator.interworks.com/users_groups/user_security/password_expiration_and_complexity.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Password Expiration and Complexity 

> Configure password complexity requirements and expiration policies to enhance user account security.

For sites that use password change or password reset options you can now enable password expiration to force
frontend users to change their passwords on a frequent basis. To further bolster security, you can also
require users to have more complex passwords, requiring a specific length, numbers, and special characters.

***Please note that for these options to be able to be turned on, password reset or password change must be
enabled, and the site must be using Curator or Tableau for authentication.***

## Password Complexity Options

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.
3. Click on the ‘General’ tab and expand the 'Security’ section.
4. Enable the toggle for **Password Complexity Options**.
5. Enter a minimum password length, and enable toggles for special character and require a number as desired.
6. Save your settings.

The new requirements will now appear on pages where you can change your password.

## Password Expiration

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.
3. Click on the ‘General’ tab and expand the 'Security’ section.
4. Enable the toggle for **Enable Password Expiration**.
5. Enter the number of days until user passwords will expire
6. Save your settings.

Note, upon updating a Curator site to have these new settings password changed date will be set for all users
of the current day and time. This will prevent a flood of users having to change their passwords. Password
expiration is checked upon login.
