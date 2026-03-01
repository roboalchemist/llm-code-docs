# Source: https://docs.curator.interworks.com/users_groups/user_management/username_mapping.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Username Mapping 

> Map external user identifiers to local usernames for proper authentication and user synchronization across systems.

If your analytic infrastructure was built by several independent groups within your organization, it's possible that the
username formats don't match across the platforms. Authenticating to each platform can usually be solved with a single
sign-on solution, but the issue still exists for embedding these platforms. API's that are used to verify user
information, permission to analytic content, group membership, etc. rely on local platform users and can't leverage SSO
credentials. Curator solves this with a built-in platform username formatting.

<Note>
  Username mapping can only change the **format** of a username, not the username itself. For example, it can convert
  `first.last@example.com` to `example\first.last`, but it cannot convert `first.last@example.com` to
  `flast@example.com`.
</Note>

## How it Works

Curator's username formatting feature will take the username received from your authentication source (SAML IdP, Tableau
Server local auth, ThoughtSpot local auth, etc.) and map it to another format based on the API call being made. For
instance, if Okta is returning the username as an email address but Tableau Server users use the prefixed domain format
the following will happen (assuming the username is InterWorks\Curator in Tableau Server):

1. User logs into Curator via Okta using their Okta credentials.
2. Okta returns the username as `curator@interworks.com`.
3. Curator automatically re-formats the username to InterWorks\Curator in order to sync the Tableau Server user details.

## How to Configure

1. Navigate to the Curator Backend > Settings > Users > Username Formatting
2. Turn on the "Enable Username Mapping" switch
3. Specify the username format your authentication source is returning back to Curator using the "Curator Frontend
   Username Format" field.
4. Specify the username format for each Connection you've configured in Curator. You can use a different format per Connection.

## Supported Formats

The following are the supported username formats assuming the username is "Curator" and the domain is "InterWorks":

* Username Only > Curator
* Username with Prefixed Domain > InterWorks\Curator
* User Email > `curator@interworks.com`

## Domain Formatting

In addition to mapping username formats for multiple platforms, you may also need to map the domains. For instance,
*iw\Curator* doesn't match `curator@interworks.com` in format or domain. To handle this situation, you can configure
domain mapping:

1. Navigate to the Curator Backend > Settings > Users > Username Formatting
2. Turn on the "Enable Domain Mapping" switch
3. Use the "Domain Map" area to specify as many mappings as you need, specifically the following:
   * **Connection**: The connection being mapped to from your Frontend User
   * **Frontend User Domain**: The domain to find in the Frontend User name
   * **\[Platform] User Domain**: The replacement domain for the platform user name

## Example

My SSO system is returning *iw\Curator* but my Tableau user is `curator@interworks.com`. The following settings would
resolve this mismatch:

For the mismatch format

1. Turn on "Enable Username Mapping" switch
2. Choose "Username with Prefixed Domain" for the "Frontend User Username Format" field
3. Choose "User Email" for the "Tableau Username Format"

For the mismatch domain

1. Turn on "Enable Domain Mapping" switch
2. Add a new item under "Domain Map"
3. Choose "Tableau" for the "Connection" field
4. Type "iw" for the "Frontend User Domain"
5. Type "InterWorks" for the "Tableau User Domain"
6. Save all the settings
