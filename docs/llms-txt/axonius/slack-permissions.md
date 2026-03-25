# Source: https://docs.axonius.com/docs/slack-permissions.md

# Slack Permissions

The Slack adapter requires different scopes and tokens for fetching different asset types.

## General

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Asset Type (if available)
      </th>

      <th style={{ textAlign: "left" }}>
        Scope(s)
      </th>

      <th style={{ textAlign: "left" }}>
        API Endpoint(s)
      </th>

      <th style={{ textAlign: "left" }}>
        Token
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        Users
      </td>

      <td style={{ textAlign: "left" }}>
        users:read
      </td>

      <td style={{ textAlign: "left" }}>
        [https://docs.slack.dev/reference/methods/users.list/](https://docs.slack.dev/reference/methods/users.list/)

        [https://docs.slack.dev/reference/methods/users.info/](https://docs.slack.dev/reference/methods/users.info/)

        <br />
      </td>

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        admin.users:read
      </td>

      <td style={{ textAlign: "left" }}>
        [https://docs.slack.dev/reference/methods/admin.users.list/](https://docs.slack.dev/reference/methods/admin.users.list/)
      </td>

      <td style={{ textAlign: "left" }}>
        Admin token is required to fetch Slack users with an Enterprise token
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        admin.teams:read
      </td>

      <td style={{ textAlign: "left" }}>
        [https://docs.slack.dev/reference/methods/admin.teams.admins.list/](https://docs.slack.dev/reference/methods/admin.teams.admins.list/)

        [https://docs.slack.dev/reference/methods/admin.teams.list/](https://docs.slack.dev/reference/methods/admin.teams.list/)

        <br />
      </td>

      <td style={{ textAlign: "left" }}>
        Admin token is required to fetch Slack users with an Enterprise token
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        channels:read, groups:read, im:read, mpim:read
      </td>

      <td style={{ textAlign: "left" }}>
        [https://docs.slack.dev/reference/methods/conversations.list/](https://docs.slack.dev/reference/methods/conversations.list/)

        [https://docs.slack.dev/reference/methods/conversations.members/](https://docs.slack.dev/reference/methods/conversations.members/)

        <br />
      </td>

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        admin
      </td>

      <td style={{ textAlign: "left" }}>
        [https://docs.slack.dev/reference/methods/team.billableinfo](https://docs.slack.dev/reference/methods/team.billableinfo)
      </td>

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        users:read.email
      </td>

      <td style={{ textAlign: "left" }}>
        [https://docs.slack.dev/reference/methods/users.lookupbyemail](https://docs.slack.dev/reference/methods/users.lookupbyemail)
      </td>

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Groups
      </td>

      <td style={{ textAlign: "left" }}>
        usergroups:read
      </td>

      <td style={{ textAlign: "left" }}>
        [https://docs.slack.dev/reference/methods/usergroups.list/](https://docs.slack.dev/reference/methods/usergroups.list/)
      </td>

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Accounts, Roles
      </td>

      <td style={{ textAlign: "left" }}>
        admin.roles:read
      </td>

      <td style={{ textAlign: "left" }}>
        [https://docs.slack.dev/reference/methods/admin.roles.listAssignments/](https://docs.slack.dev/reference/methods/admin.roles.listAssignments/)
      </td>

      <td style={{ textAlign: "left" }}>
        Admin token is required to fetch Slack Roles
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        Application Resources, User Extensions, SaaS Applications
      </td>

      <td style={{ textAlign: "left" }}>
        admin
      </td>

      <td style={{ textAlign: "left" }}>
        [https://docs.slack.dev/reference/methods/team.integrationLogs/](https://docs.slack.dev/reference/methods/team.integrationLogs/)
      </td>

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        admin.invites:read (View a workspace's invites and invite requests)
      </td>

      <td style={{ textAlign: "left" }}>
        [http://docs.slack.dev/reference/methods/admin.inviteRequests.list](http://docs.slack.dev/reference/methods/admin.inviteRequests.list) - List pending workspace invite requests
        [http://docs.slack.dev/reference/methods/admin.inviteRequests.approved.list](http://docs.slack.dev/reference/methods/admin.inviteRequests.approved.list) - List approved invite requests
        [http://docs.slack.dev/reference/methods/admin.inviteRequests.denied.list](http://docs.slack.dev/reference/methods/admin.inviteRequests.denied.list) - List denied invite requests
      </td>

      <td style={{ textAlign: "left" }} />
    </tr>

    <tr>
      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        auditlogs:read (View actions from channels, files, apps, user events, and admin events)
      </td>

      <td style={{ textAlign: "left" }}>
        [http://docs.slack.dev/reference/methods/audit/v1/logs](http://docs.slack.dev/reference/methods/audit/v1/logs)
      </td>

      <td style={{ textAlign: "left" }}>
        Only for Enterprise Grid Organization editions
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }} />

      <td style={{ textAlign: "left" }}>
        team.billing:read (Fetch billing information)
      </td>

      <td style={{ textAlign: "left" }}>
        [https://docs.slack.dev/reference/methods/team.billing.info](https://docs.slack.dev/reference/methods/team.billing.info)
      </td>

      <td style={{ textAlign: "left" }}>
        Only for Enterprise Grid Organization editions
      </td>
    </tr>
  </tbody>
</Table>

## Fetching Application Settings

Based on the API endpoints defined in `SlackSettingsEndpoints`, the following OAuth scopes are required to fetch Application Settings.

<Callout icon="📘" theme="info">
  **Note**

  1. Some high-privilege settings cannot be fetched with an API token. These settings require you to provide an Account Sub Domain, User Name, Password, and MFA Secret when [connecting the adapter in Axonius](https://docs.axonius.com/axonius-help-docs/docs/connecting-the-slack-adapter-in-axonius).
  2. Enterprise Grid accounts cannot use Bot Tokens.
</Callout>

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Scope(s)
      </th>

      <th>
        API Endpoint(s)
      </th>

      <th>
        Token
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        admin.apps:read
      </td>

      <td>
        [https://docs.slack.dev.reference/methods/admin.apps.approved.list](https://docs.slack.dev.reference/methods/admin.apps.approved.list)

        [https://docs.slack.dev.reference/methods/admin.apps.config.lookup](https://docs.slack.dev.reference/methods/admin.apps.config.lookup)

        [https://docs.slack.dev.reference/methods/admin.apps.requests.list](https://docs.slack.dev.reference/methods/admin.apps.requests.list)

        [https://docs.slack.dev.reference/methods/admin.apps.restricted.list](https://docs.slack.dev.reference/methods/admin.apps.restricted.list)
      </td>

      <td>
        Enterprise Grid with an organization-level admin token required
      </td>
    </tr>

    <tr>
      <td>
        admin.barriers:read
      </td>

      <td>
        [https://docs.slack.dev.reference/methods/admin.barriers.list](https://docs.slack.dev.reference/methods/admin.barriers.list)
      </td>

      <td>
        Enterprise Grid with an organization-level admin token required
      </td>
    </tr>

    <tr>
      <td>
        admin.conversations:read
      </td>

      <td>
        [https://docs.slack.dev.reference/methods/admin.conversations.getCustomRetention](https://docs.slack.dev.reference/methods/admin.conversations.getCustomRetention)
      </td>

      <td>
        Enterprise Grid with an organization-level admin token required
      </td>
    </tr>

    <tr>
      <td>
        admin.teams:read
      </td>

      <td>
        [https://docs.slack.dev.reference/methods/admin.teams.list](https://docs.slack.dev.reference/methods/admin.teams.list)
      </td>

      <td>
        Enterprise Grid with an organization-level admin token required
      </td>
    </tr>

    <tr>
      <td>
        admin.users:read
      </td>

      <td>
        [https://docs.slack.dev.reference/methods/admin.users.list](https://docs.slack.dev.reference/methods/admin.users.list)

        [https://docs.slack.dev.reference/methods/admin.users.session.getSettings](https://docs.slack.dev.reference/methods/admin.users.session.getSettings)
      </td>

      <td>
        Enterprise Grid with an organization-level admin token required
      </td>
    </tr>

    <tr>
      <td>
        admin.workflows:read
      </td>

      <td>
        [https://docs.slack.dev.reference/methods/admin.workflows.search](https://docs.slack.dev.reference/methods/admin.workflows.search)
      </td>

      <td>
        Enterprise Grid with an organization-level admin token required
      </td>
    </tr>

    <tr>
      <td>
        calls:read
      </td>

      <td>
        [https://docs.slack.dev.reference/methods/calls.info](https://docs.slack.dev.reference/methods/calls.info)
      </td>

      <td />
    </tr>

    <tr>
      <td>
        channels:read (For public channels data)
      </td>

      <td>
        [https://docs.slack.dev.reference/methods/conversations.info](https://docs.slack.dev.reference/methods/conversations.info) (Public channels)

        [https://docs.slack.dev.reference/methods/conversations.list](https://docs.slack.dev.reference/methods/conversations.list) (Public channels)

        [https://docs.slack.dev.reference/methods/conversations.join](https://docs.slack.dev.reference/methods/conversations.join)
      </td>

      <td />
    </tr>

    <tr>
      <td>
        groups:read (For private channels data)
      </td>

      <td>
        [https://docs.slack.dev.reference/methods/conversations.info](https://docs.slack.dev.reference/methods/conversations.info) (Private channels)

        [https://docs.slack.dev.reference/methods/conversations.list](https://docs.slack.dev.reference/methods/conversations.list) (Private channels)
      </td>

      <td />
    </tr>

    <tr>
      <td>
        im:read - (For direct messages data)
      </td>

      <td>
        [https://docs.slack.dev.reference/methods/conversations.info](https://docs.slack.dev.reference/methods/conversations.info) (DMs)

        [https://docs.slack.dev.reference/methods/conversations.list](https://docs.slack.dev.reference/methods/conversations.list) (DMs)
      </td>

      <td />
    </tr>

    <tr>
      <td>
        mpim:read (For multi-party direct messages data)
      </td>

      <td>
        [https://docs.slack.dev.reference/methods/conversations.info](https://docs.slack.dev.reference/methods/conversations.info) (group DMs)

        [https://docs.slack.dev.reference/methods/conversations.list](https://docs.slack.dev.reference/methods/conversations.list) (group DMs)
      </td>

      <td />
    </tr>

    <tr>
      <td>
        channels:write (For joining public channels)
      </td>

      <td>
        [https://docs.slack.dev.reference/methods/conversations.join](https://docs.slack.dev.reference/methods/conversations.join)
      </td>

      <td />
    </tr>

    <tr>
      <td>
        files:read
      </td>

      <td>
        [https://docs.slack.dev.reference/methods/files.info](https://docs.slack.dev.reference/methods/files.info)

        [https://docs.slack.dev.reference/methods/files.list](https://docs.slack.dev.reference/methods/files.list)

        [https://docs.slack.dev.reference/methods/files.remote.info](https://docs.slack.dev.reference/methods/files.remote.info)
      </td>

      <td />
    </tr>

    <tr>
      <td>
        openid
      </td>

      <td>
        [https://docs.slack.dev.reference/methods/openid.connect.userInfo](https://docs.slack.dev.reference/methods/openid.connect.userInfo)
      </td>

      <td />
    </tr>

    <tr>
      <td>
        profile:read (For user profile access via OpenID)
      </td>

      <td>
        [https://docs.slack.dev.reference/methods/openid.connect.userInfo](https://docs.slack.dev.reference/methods/openid.connect.userInfo)
      </td>

      <td />
    </tr>

    <tr>
      <td>
        email:read (For email address access via OpenID)
      </td>

      <td>
        [https://docs.slack.dev.reference/methods/openid.connect.userInfo](https://docs.slack.dev.reference/methods/openid.connect.userInfo)
      </td>

      <td />
    </tr>

    <tr>
      <td>
        rtm:stream (For RTM API access)
      </td>

      <td>
        [https://docs.slack.dev.reference/methods/rtm.connect](https://docs.slack.dev.reference/methods/rtm.connect)
      </td>

      <td />
    </tr>

    <tr>
      <td>
        search:read (For search functionality)
      </td>

      <td>
        [https://docs.slack.dev.reference/methods/search.all](https://docs.slack.dev.reference/methods/search.all)

        [https://docs.slack.dev.reference/methods/search.files](https://docs.slack.dev.reference/methods/search.files)

        [https://docs.slack.dev.reference/methods/search.messages](https://docs.slack.dev.reference/methods/search.messages)
      </td>

      <td />
    </tr>

    <tr>
      <td>
        team:read
      </td>

      <td>
        [https://docs.slack.dev.reference/methods/team.profile.get](https://docs.slack.dev.reference/methods/team.profile.get)
      </td>

      <td />
    </tr>

    <tr>
      <td>
        users:read
      </td>

      <td>
        [https://docs.slack.dev.reference/methods/users.info](https://docs.slack.dev.reference/methods/users.info)

        [https://docs.slack.dev.reference/methods/users.lookupByEmail](https://docs.slack.dev.reference/methods/users.lookupByEmail)

        [https://docs.slack.dev.reference/methods/users.discoverableContacts.lookup](https://docs.slack.dev.reference/methods/users.discoverableContacts.lookup)
      </td>

      <td />
    </tr>

    <tr>
      <td>
        users:read.email (To access email field)
      </td>

      <td>
        [https://docs.slack.dev.reference/methods/users.lookupByEmail](https://docs.slack.dev.reference/methods/users.lookupByEmail)

        [https://docs.slack.dev.reference/methods/users.info](https://docs.slack.dev.reference/methods/users.info)
      </td>

      <td />
    </tr>
  </tbody>
</Table>

## Enforcement Actions

See [Slack Enforcement Actions](https://docs.axonius.com/axonius-help-docs/docs/slack-enforcement-actions) for the full list or permissions required for Slack Enforcement Actions.