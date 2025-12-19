# Source: https://gokapi.readthedocs.io/en/stable/examples.html

[]

# Examples[](#examples "Link to this heading")

[]

## Nginx Configuration[](#nginx-configuration "Link to this heading")

    server 

            # Always redirect to https
            if ( $scheme = http ) 
    }

## OpenID Connect Configuration[](#openid-connect-configuration "Link to this heading")

[]

### Authelia[](#authelia "Link to this heading")

#### Server Configuration[](#server-configuration "Link to this heading")

Note

This guide has been written for version 4.37.5

See the [Authelia documentation](https://www.authelia.com/configuration/identity-providers/open-id-connect/) on how to setup an OIDC server. An example file would be as followed:

    identity_providers:
      oidc:
        hmac_secret: noz1Aow6Soo9lieyus2E_EXAMPLE_KEY
        issuer_private_key: |
          -----BEGIN PRIVATE KEY-----
          ohf2shae1bahph7ahSh1
          EXAMPLE_KEY
          EP3EihoPhei9iingai0v==
          -----END PRIVATE KEY-----
        access_token_lifespan: 1h
        authorize_code_lifespan: 1m
        id_token_lifespan: 1h
        refresh_token_lifespan: 90m
        enable_client_debug_messages: false
        enforce_pkce: public_clients_only
        cors:
          endpoints:
            - authorization
            - token
            - revocation
            - introspection
          allowed_origins:
            - "https://*.your.domain"
          allowed_origins_from_client_redirect_uris: false
        clients:
          - id: gokapi-dev
            description: Gokapi Example
            secret: 'AhXeV7_EXAMPLE_KEY'
            sector_identifier: ''
            public: false
            authorization_policy: one_factor
            consent_mode: pre-configured
            pre_configured_consent_duration: 1w
            audience: []
            scopes:
              - openid
              - email
              - profile
              - groups
            redirect_uris:
              - https://gokapi.website.com/oauth-callback
            userinfo_signing_algorithm: none

-   Set [`authorization_policy`] to [`two_factor`] to use OTP or a hardware key.

-   If [`consent_mode`] is [`pre-configured`], the user has the option to remember consent. That way you can use a lower [`Recheck`]` `[`identity`] interval in Gokapi. Logout through the Gokapi interface will not be possible anymore, unless the user logs out their Authelia account. If the option is set to [`explicit`], the user always has to grant the permission after the [`Recheck`]` `[`identity`] interval has passed

-   [`scopes`] may exclude [`groups`] if these are not required for authentication, e.g. if all users registered with Authelia may access Gokapi.

-   Make sure [`redirect_uris`] is set to the correct value

#### Gokapi Configuration[](#gokapi-configuration "Link to this heading")

+---------------------------+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| Gokapi Configuration      | Input                                                                                    | Example                                                                 |
+===========================+==========================================================================================+=========================================================================+
| Provider URL              | URL to Authelia Server                                                                   | https://auth.autheliaserver.com                                         |
+---------------------------+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| Client ID                 | Client ID provided in config                                                             | gokapi-dev                                                              |
+---------------------------+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| Client Secret             | Client secret provided in config                                                         | AhXeV7_EXAMPLE_KEY                                                      |
+---------------------------+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| Admin email address       | The email address for the super-admin                                                    | [gokapi@example.com](mailto:gokapi%40example.com) |
+---------------------------+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| Recheck identity          | If mode is [`pre-configured`], use a low interval | 12 hours                                                                |
+---------------------------+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| Restrict to group         | Check this, if only users from certain groups shall be                                   | checked                                                                 |
|                           |                                                                                          |                                                                         |
|                           | allowed to access Gokapi admin menu                                                      |                                                                         |
+---------------------------+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| Scope identifier (group)  | Use a scope that lists the user's groups                                                 | groups                                                                  |
+---------------------------+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| Authorised groups         | Enter all groups, separated by semicolon                                                 | dev;admins;gokapi-\*                                                    |
|                           |                                                                                          |                                                                         |
|                           | [`*`] can be used as a wildcard                   |                                                                         |
+---------------------------+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| Only allow existing users | Check this, if you do not want authenticated users to                                    | unchecked                                                               |
|                           |                                                                                          |                                                                         |
|                           | automatically create a new account or restore a deleted one                              |                                                                         |
+---------------------------+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+

[]

### Keycloak[](#keycloak "Link to this heading")

Note

This guide has been written for version 24.0.3

Warning

In a previous version of this guide, the client mapping was for the predefined mapper "Group memberships", which in some cases always returned the value "admin". Please make sure that you are using a custom mapper, as described in [[Addding a scope for exposing groups (optional)]](#oidcconfig-keycloak-opt)

#### Server Configuration[](#id2 "Link to this heading")

##### Creating the client[](#creating-the-client "Link to this heading")

1.  In your realm (default: master) click on [`[Manage]`]` `[`Clients`] and then [`Create`]` `[`Client`]

    > <div>
    >
    > -   Client Type: OpenID Connect
    >
    > -   Client ID: a unique ID, [`gokapi-dev`] is used in this example
    >
    > </div>

2.  Click [`Next`]

    > <div>
    >
    > -   Set [`Client`]` `[`authentication`] to on
    >
    > -   Only select [`Standard`]` `[`flow`] in [`Authentication`]` `[`flow`]
    >
    > </div>

3.  Click [`Next`], add your redirect URL, e.g. [`https://gokapi.website.com/oauth-callback`] and click [`Save`]

4.  Click [`Credentials`] and note the [`Client`]` `[`Secret`]

[]

##### Addding a scope for exposing groups (optional)[](#addding-a-scope-for-exposing-groups-optional "Link to this heading")

1.  In the realm click on [`[Manage]`]` `[`Client`]` `[`Scopes`] and then [`Create`]` `[`Client`]` `[`Scope`]

    > <div>
    >
    > -   Name: groups
    >
    > -   Type: Default
    >
    > -   Protocol: OpenID Connect
    >
    > -   Click [`Save`]
    >
    > </div>

2.  Click [`Mappers`]

    > <div>
    >
    > -   Click [`Add`]` `[`mapper`]
    >
    > -   Select [`Configure`]` `[`a`]` `[`new`]` `[`mapper`]
    >
    > -   Select [`Group`]` `[`Membership`]
    >
    > -   Enter a name and set [`Token`]` `[`Claim`]` `[`Name`] to a claim name, e.g. [`groups`]
    >
    > -   Deselect [`Full`]` `[`group`]` `[`path`] if you are only using a single realm. Otherwise use the full name for your groups in the Gokapi configuration, e.g. [`/admins`] instead of [`admins`]
    >
    > -   Click [`Save`]
    >
    > </div>

3.  In the realm click on [`[Manage]`]` `[`Clients`] and then [`gokapi-dev`]

    > <div>
    >
    > -   Click [`Client`]` `[`Scopes`]
    >
    > -   Click [`Add`]` `[`Client`]` `[`Scope`]
    >
    > -   Select the new scope and click [`Add`]` `[`/`]` `[`Default`]
    >
    > </div>

#### Gokapi Configuration[](#id3 "Link to this heading")

+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| Gokapi Configuration      | Input                                                                                                                                                                             | Example                                                                 |
+===========================+===================================================================================================================================================================================+=========================================================================+
| Provider URL              | URL to Keycloak realm                                                                                                                                                             | http://keycloak.server.com/realms/master                                |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| Client ID                 | Client ID provided                                                                                                                                                                | gokapi-dev                                                              |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| Client Secret             | Client secret provided                                                                                                                                                            | AhXeV7_EXAMPLE_KEY                                                      |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| Recheck identity          | If open [`Consent`]` `[`required`] is disabled, use a low interval | 12 hours                                                                |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| Admin email address       | The email address for the super-admin                                                                                                                                             | [gokapi@example.com](mailto:gokapi%40example.com) |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| Restrict to group         | Check this, if only users from certain groups shall be                                                                                                                            | checked                                                                 |
|                           |                                                                                                                                                                                   |                                                                         |
|                           | allowed to access Gokapi admin menu                                                                                                                                               |                                                                         |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| Scope identifier (group)  | Use a scope that lists the user's groups                                                                                                                                          | groups                                                                  |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| Authorised groups         | Enter all groups, separated by semicolon                                                                                                                                          | dev;admins;gokapi-\*                                                    |
|                           |                                                                                                                                                                                   |                                                                         |
|                           | [`*`] can be used as a wildcard                                                                                                            |                                                                         |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| Only allow existing users | Check this, if you do not want authenticated users to                                                                                                                             | unchecked                                                               |
|                           |                                                                                                                                                                                   |                                                                         |
|                           | automatically create a new account or restore a deleted one                                                                                                                       |                                                                         |
+---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+

Note

Logout through the Gokapi interface will not be possible anymore, unless the user logs out their Keycload account.

[]

### Google[](#google "Link to this heading")

#### Server Configuration[](#id4 "Link to this heading")

Note

This guide has been last updated in January 2024 and is based on [this documentation](https://support.google.com/cloud/answer/6158849)

1.  Go to the [Google Cloud Platform Console](https://console.cloud.google.com/).

2.  From the projects list, select a project or create a new one.

3.  If the APIs & services page isn't already open, open the console left side menu and select APIs & services.

4.  On the left, click Credentials.

5.  Click New Credentials, then select OAuth client ID.

6.  Select Application Type [`Webapplication`]

7.  Add the correct Gokapi redirect URL and click Create

#### Gokapi Configuration[](#id5 "Link to this heading")

+---------------------------+-------------------------------------------------------------+-------------------------------------------------------------------------+
| Gokapi Configuration      | Input                                                       | Example                                                                 |
+===========================+=============================================================+=========================================================================+
| Provider URL              | https://accounts.google.com                                 | https://accounts.google.com                                             |
+---------------------------+-------------------------------------------------------------+-------------------------------------------------------------------------+
| Client ID                 | Client ID provided                                          | XXX.apps.googleusercontent.com                                          |
+---------------------------+-------------------------------------------------------------+-------------------------------------------------------------------------+
| Client Secret             | Client secret provided                                      | AhXeV7_EXAMPLE_KEY                                                      |
+---------------------------+-------------------------------------------------------------+-------------------------------------------------------------------------+
| Recheck identity          | Use a low interval                                          | 12 hours                                                                |
+---------------------------+-------------------------------------------------------------+-------------------------------------------------------------------------+
| Admin email address       | The email address for the super-admin                       | [gokapi@example.com](mailto:gokapi%40example.com) |
+---------------------------+-------------------------------------------------------------+-------------------------------------------------------------------------+
| Restrict to group         | Unsupported                                                 | unchecked                                                               |
+---------------------------+-------------------------------------------------------------+-------------------------------------------------------------------------+
| Only allow existing users | Check this, if you do not want authenticated users to       | unchecked                                                               |
|                           |                                                             |                                                                         |
|                           | automatically create a new account or restore a deleted one |                                                                         |
+---------------------------+-------------------------------------------------------------+-------------------------------------------------------------------------+

[]

### Microsoft Entra / Azure[](#microsoft-entra-azure "Link to this heading")

#### Server Configuration[](#id6 "Link to this heading")

Note

This guide has been last updated in February 2024

##### Creating the client[](#id7 "Link to this heading")

1.  Open [https://entra.microsoft.com/](https://entra.microsoft.com/)

2.  Go to Applications / App registration / New registration

3.  Enter name and for redirect values [`Web`] and the Gokapi redirect URL shown in the setup

4.  In Manage / Authentication / Implicit grant and hybrid flows check [`ID`]` `[`Tokens`]

5.  In Certificate & secrets / Client secrets click New client secret, enter the value of the secret in Gokapi setup

6.  In Application / API permissions / click Grant admin consent.

7.  The client ID shown in Application Overview / Application (client) ID

8.  The provider URL is [`https://login.microsoftonline.com/REALM/v2.0/`], replace [`REALM`] with the tenant id shown in Application Overview / Directory (tenant) ID (see also [https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols-oidc](https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols-oidc) for other options)

##### Optional: Restricting Gokapi to specific users or groups:[](#optional-restricting-gokapi-to-specific-users-or-groups "Link to this heading")

1.  Open [https://entra.microsoft.com/](https://entra.microsoft.com/)

2.  Go to Applications / Enterprise Applications and select Gokapi

3.  Go to Manage / Properties and check [`Assignment`]` `[`required?`]

4.  Go to Manage / Users & Groups and add the allowed users / groups

#### Gokapi Configuration[](#id8 "Link to this heading")

+---------------------------+---------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| Gokapi Configuration      | Input                                                                                                   | Example                                                                    |
+===========================+=========================================================================================================+============================================================================+
| Provider URL              | https://login.microsoftonline.com/REALM/v2.0/, replace [`REALM`] | https://login.microsoftonline.com/abcdef-1234-4678-9540-abcdefabcdef/v2.0/ |
+---------------------------+---------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| Client ID                 | Client ID provided                                                                                      | 11111122222-4444-55555-66666-abcdefabcdef                                  |
+---------------------------+---------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| Client Secret             | Client secret provided                                                                                  | ach5sho3Ru-Heop7aMaez-example                                              |
+---------------------------+---------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| Admin email address       | The email address for the super-admin                                                                   | [gokapi@example.com](mailto:gokapi%40example.com)    |
+---------------------------+---------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| Recheck identity          | Use a low interval                                                                                      | 12 hours                                                                   |
+---------------------------+---------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| Restrict to group         | Unsupported                                                                                             | unchecked                                                                  |
+---------------------------+---------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| Only allow existing users | Check this, if you do not want authenticated users to                                                   | checked                                                                    |
|                           |                                                                                                         |                                                                            |
|                           | automatically create a new account or restore a deleted one                                             |                                                                            |
+---------------------------+---------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+