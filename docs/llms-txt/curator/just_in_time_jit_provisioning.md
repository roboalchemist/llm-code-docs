# Source: https://docs.curator.interworks.com/users_groups/user_management/just_in_time_jit_provisioning.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Just-in-time (JIT) Provisioning 

> Configure just-in-time user provisioning to automatically create user accounts during first-time authentication.

## JIT Provisioning on Curator

When paired with externally managed authentication providers (SAML, Tableau Server, Active Directory, etc.), Curator will
automatically create a user record in its own database when they first log in.

If you need to disable this, the setting can be found under **Settings** > **Security** > **Authentication Settings** >
**Customization** section > *Disable Just-in-time Provisioning of Curator Users* setting.  Be sure to click the save button.

## JIT Provisioning on Tableau

Curator can also serve as an intermediary to that process and automatically create the users on Tableau Server after a
successful authentication with Okta or other SAML identity providers.  You will still be required to manually assign any
groups, or license levels (Explorer by default), in Tableau Server.  But this allows simple authentication into Curator if
the user does not yet exist on Tableau.
(/setup/authentication/okta\_saml)
To enable this, complete the steps for SAML setup ([instructions here](/setup/authentication/okta_saml))

Then on the backend under **Settings** > **Security** > **Authentication Settings**, open up the **SAML Advanced** section
and enable *Just-in-time (JIT) Provisioning* then Save your SAML settings.
