# Source: https://archivedocs.stackstate.com/saas/user-management.md

# User Management

Users of the SaaS tenants (StackState instances) are managed with [Keycloak](https://www.keycloak.org/). Each customer (tenant) has a dedicated Keycloak realm. A link to the Keycloak console is sent in the welcome message when a user is created.

There are two levels of user management permissions: **Basic** (default) and **Advanced**.

* **Basic** (default): Allows users to add new users and add them to Keycloak groups.
* **Advanced**: Allows users to manage an entire Keycloak realm (configuring Identity Providers, Authentication/Authorization options, etc.). **Available for Enterprise Edition only.**

All SaaS tenants start with **Basic** mode. Paid customers can request an upgrade to **Advanced** mode by filing a support ticket to <help@stackstate.zendesk.com>. Users who are members of the `realm-admin` Keycloak group receive a link to the Keycloak Admin Console in the welcome message.

StackState redirects users to Keycloak for authentication. Users are expected to be members of one or more Keycloak groups.

The predefined Keycloak groups:

* **realm-admin**: Members of this group can log in to the Keycloak realm console and perform operations allowed by their user management mode (Basic or Advanced).
* **stackstate-k8s-troubleshooter**: Users in this group are assigned the `stackstate-k8s-troubleshooter` Keycloak client role, which maps to the StackState role with the same name. The role grants regular StackState permissions.
* **stackstate-k8s-admin**: Users in this group are assigned the `stackstate-k8s-admin` Keycloak client role, which maps to the StackState role with the same name. The role grants privileged StackState permissions.

## Basic user management

* Log in to Keycloak Admin Console.

![Keycloak Admin Console in Basic Mode](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-dc0a670cddc32ab35a567ce2092c0ea5df1f3b65%2Fkeycloak_admin_console.png?alt=media)

### Manage users

* In the left-hand menu, select `Users` under the `Manage` section.

#### Adding a new user

To **add a new user** click the `Add user` button. Enter the necessary user information (Username, Email, First Name, Last Name).

* leave `Required users actions` empty.
* add the user to the required groups.
* click `Save`. The welcome message with the sign-up link and the links to the SaaS tenant, Keycloak Admin and Account consoles are emailed to the user.
* **To activate the account, which includes email confirmation and the password reset, the user must follow the sign-up link.**

![Keycloak Create User](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-4ae868cbc92f393034c8cbef5d37e6853568ab53%2Fkeycloak_create_user.png?alt=media)

#### Updating user details

To **edit user details**, select the user by clicking on Username.

* Change the details as needed.
* Set one or more `Required user actions`, for example, to force users to update password or configure one time passwords.
* Press `Save` button when done.

![Keycloak Update User](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-2ac270bc6941c6825890a62fe584c5c6073bdcb6%2Fkeycloak_update_user.png?alt=media)

#### Deleting a user

To **delete one or more users**, select the required users and press `Delete user` button.

### Group membership

* Log in to the Keycloak Admin Console.
* In the `Groups` section, search for the group you want to manage.
* Click on the group name to open group details and go to the `Members` tab.
* To add a new group member, press the `Add Member` button and select the required users.
* To delete users from the group, select the users from the list, then from the menu that at the same line as the `Add member` button marked as "⋮", select `Leave group`.

## Advanced user management

In Advanced User Management, users have full administrative permissions within their Keycloak realm. They can configure authentication, authorization, external identity providers, and more.

![Keycloak Admin Console in Advanced mode](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-33b81af7eaed88c74f1e14389aec409cee4ef70a%2Fkeycloak_advanced_mode.png?alt=media)

Refer to [the official Keycloak documentation](https://www.keycloak.org/docs/22.0.5/server_admin/index.html) for more details.

A Keycloak realm comes with the initial configuration:

* An OIDC client integrated with a SaaS tenant.
  * A set of Keycloak client roles that map to StackState built-in roles.
    * `stackstate-k8s-troubleshooter`
    * `stackstate-k8s-admin`
* A realm role to manage the Keycloak realm, `realm-admin`.
* A set of Keycloak Groups with corresponding Keycloak client and realm roles assigned:
  * `realm-admin`
  * `stackstate-k8s-troubleshooter`
  * `stackstate-k8s-admin`
* SMTP server configuration to send email notifications generated by Keycloak.
* A custom eventListener, `stackstate-user-creation`, which is responsible for generating a welcome message to new users.

Please avoid modifying the mentioned resources and the default realm's clients, since it might require resetting the Keycloak realm configuration.

### Example: Using Azure Active Directory as an identity provider

⚠️ This guide is applicable for the Advanced User Management only.

#### Prerequisites

* The user must be a member of the `realm-admin` Keycloak group.
* Permissions to create `App registrations` in [the Azure portal](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade).
* An ID of the Active Directory group to grant permissions to StackState. (found in the [Groups section of the Azure portal](https://portal.azure.com/#view/Microsoft_AAD_IAM/GroupsManagementMenuBlade/~/AllGroups)).

#### Creating an app registration in Azure

* Log in to [the Azure portal](https://portal.azure.com) and proceed to [App registrations](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade)
* Press `New registration`, fill in the name of the registration, select `Accounts in this organizational directory only` and leave all other fields as is.

![Azure App Registration](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-3c4943be85c8a5fda49278ed86904bd3eabb2e7e%2Fkeycloak_azure_app_registration.png?alt=media)

* Note the `Application (client) ID` for the created app registration; it will be used later to configure a Keycloak Identity Provider. *The value of the secret is shown only once just after creation.*
* Press `Add a certificate or secret` and create a client secret. Note the value for the created secret; it will be used later to configure a Keycloak Identity Provider.

![Create secret for Azure App Registration](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-f751f971faefde80ac9700ac0848fc8b6d99872b%2Fkeycloak_azure_app_registration-2.png?alt=media)

* From the `App registration` page go to `Endpoints` and note the `OpenID Connect metadata document` link; it will be used later to configure a Keycloak Identity Provider.

![Azure App Discovery Endpoint](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-92803913d71cd723c72e81b9202386376ec8416e%2Fkeylcoak_azure_app_endpoint.png?alt=media)

* Go to the Manifest section and ensure that the `groupMembershipClaims` setting of the App registration is set to `All`. This is required to map Active Directory Groups to the Keycloak Groups/Roles.

![Azure App Manifest](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-507effd9784112677f380bcf4c621dbf92c80408%2Fkeycloak_app_registration_manifest.png?alt=media)

#### Adding an identity provider to Keycloak

* Log in to the Keycloak Admin console.
* In the left-hand menu, select `Identity providers` under the `Configure` section.
* Choose `OpenID Connect v1.0`.
* Fill in the `Display name` as required, and input the `Client ID`, `Client Secret`, and `Discovery endpoint` with the data from the App registration notes.

![Keycloak Identity Provider](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-647b4ef525fc4f4d874926fa97db009cf917093e%2Fkeycloak_identity_provider.png?alt=media)

* Note `Redirect URI`, which is needed to complete the App registration.
* Press `Add`.
* Scroll to the bottom the page and set `Sync mode` to `Force`.
* Click `Save` to finalize the provider configuration.

#### Finalizing app registration

* Return to the `App Registration` section of the Azure portal and click `Add a Redirect URI`

![Configuring Redirect URI for Azure App](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-54ce3cf997906a85701217dcc9d9060c7a8a7633%2Fkeycloak_finalizing_app_registration.png?alt=media)

* Click `Add a platform` and select `Web` from the right-hand frame.
* Enter the Redirect URI from the Keycloak Identity Provider's configuration and click `Configure`.

![Configuring Redirect URI for Azure App](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-c500398710025159fcc93765ec3cc18d2d76d511%2Fkeycloak_finalizing_app_registration-2.png?alt=media)

#### Verifying Keycloak identity provider

* Open your tenant URL in a browser. The Login page should now include an option to sign in with the configured IdentityProvider. *If you have already logged into the tenant you must log out first.*

![Login page](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-00cbe4e9292f7b2bb3b43a9ad3f51feb55855354%2Fkeycloak_login_page.png?alt=media)

* Sign in with `Azure` Identity Provider.
* If everything is configured correctly you should be logged into the tenant with the default StackState role, `stackstate-guest`.

#### Mapping Active Directory role to StackState role

This guide assumes an Azure Identity Provider was added as described earlier.

* Log in to the Keycloak Admin console.
* In the left-hand menu, select `Identity providers` under the `Configure` section and choose the `Azure` Identity Provider.
* Navigate to the `Mappers` tab and press `Add mapper`.
* Fill in the details as shown in the screenshot. For the Claim Value use the ID (⚠️ not a name) of the Active Directory Group.

![Keycloak Identity Mapper](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-6f17d023b1d886ad1d290344748f4819c080a143%2Fkeycloak_idp_group_mapper.png?alt=media)

* Click `Save` to store the mapper settings.
* Log in to the StackState tenant to verify if the stackstate-k8s-troubleshooter StackState role has been granted to your user. You should see additional items in the menu such as Monitors, Stackpacks, etc.

![StackState menu for stackstate-k8s-troubleshooter](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-c0468ca9d5d0fe53044ca914d909ab8a256acc49%2Fkeycloak_stackstate-k8s-troublshooter.png?alt=media)
