# Source: https://docs.curator.interworks.com/users_groups/user_management/automatic_license_provisioning.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Automatic License Provisioning 

> Automatically provision Tableau Server licenses for users when they access Curator for streamlined license management.

Tableau allows Administrators to manage their licenses in a way that all users can be added as unlicensed and only
[grant them a license][1] once they are logging into Tableau Server. You can now use this feature through your Curator.
All users that are currently unlicensed will receive a license when trying to log into Curator if you have this feature enabled.

## Note This feature is only available when you either use SAML or OAuth/OpenID for authentication

***To grant license on sign-in with SAML***

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Tableau** > **Tableau Server Settings** section from the left-hand menu.
3. In the Authentication tab, expand the **SAML Advanced** section and enable the "License Users if Unlicensed" toggle.

***To grant license on sign-in with OAuth/OpenID***

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Tableau** > **Tableau Server Settings** section from the left-hand menu.
3. In the Authentication tab, expand the **Customization** section and enable the "License Users if Unlicensed" toggle.

[1]: https://help.tableau.com/current/server/en-us/grant_role.htm
