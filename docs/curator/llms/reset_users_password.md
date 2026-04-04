# Source: https://docs.curator.interworks.com/users_groups/user_management/reset_users_password.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Reset User's Password

> Reset user passwords as an administrator when users cannot access their accounts or have forgotten credentials.

When managing users you may find a need to change a user's password on Curator.  The method used to change user's
passwords will depend on the [authentication type](/setup/authentication/overview)
you are using on Curator: when using *Tableau Server* or *Curator Users* authentication you can reset users passwords
within Curator.  For all other options you will need to use the source-system of your user store (your IdP) to change the
password there.

**To reset a user's password:**

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Tableau** > **Tableau Users** or **Settings** > **Users** > **Frontend Users** section
   from the left-hand menu.
3. Find the user in the list that you're looking for in the list of users, then click on the row to navigate to the
   edit-user page.
4. Type in a new password for the user, then click the save button
5. The end user will **NOT** be notified of this change, so be sure to let them know of the change made.
