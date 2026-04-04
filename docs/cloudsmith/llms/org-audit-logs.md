# Source: https://help.cloudsmith.io/docs/org-audit-logs.md

# Audit Logs

Organization Audit Logs provide a log of events across your organization, such as [creating](https://help.cloudsmith.io/docs/create-a-repository)/[deleting](https://help.cloudsmith.io/reference/repos_delete) a repository or modifications to repository settings/configuration.

<Image title="org-audit-logs.png" alt={1322} align="center" border={true} src="https://files.readme.io/994c519bd88edbe5071aaad9001e81f2626ecfa673691f5c78e04b699643a5e1-app.cloudsmith.com_demo_logsiPad_Pro.png">
  Organization Audit Logs
</Image>

## Key Concepts

Clicking on a row in your audit log will expand to show more details.

<Image alt="Expanded log entry" align="center" src="https://files.readme.io/4e9356d46f85b38b0939a0b3a5a19fbe4f3b2fe65e6850633f172f1a482b503c-app.cloudsmith.com_demo_logsiPad_Pro_1.png">
  Expanded log entry
</Image>

Each entry in the log represents an event or a state change and consists of four main components.

* **Actor**: The object that performed the Action, such as a User, Service Account or System
* **Verb**: The verb (phrase) identifying "what\_happened", such as `login`, `retention_settings_changed` or `token_created`
* **Action Object**:  The object which was created, deleted or updated by the action.
* **Target**: (Optional) The object within which the Action was performed, such as a repository or account

## Searching / Filtering

You can Search and Filter the Audit Log using the search box at the top. You can also use boolean logic (e.g. AND/OR/NOT) for complex search queries.

### Search Terms

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Search By
      </th>

      <th>
        Search Terms Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Actor
      </td>

      <td>
        `actor:some-user`
      </td>
    </tr>

    <tr>
      <td>
        Actor Kind
      </td>

      <td>
        `actor_kind:user` (user)\
        `actor_kind:service_account` (service account)\
        `actor_kind:system`
      </td>
    </tr>

    <tr>
      <td>
        Event Time
      </td>

      <td>
        `event_at:>"1 day ago"`\
        `event_at:<"June 21, 2022 EST"`
      </td>
    </tr>

    <tr>
      <td>
        Event Kind
      </td>

      <td>
        `event_kind:action` (action)\
        `event_kind:create` (create)\
        `event_kind:read` (read)\
        `event_kind:update` (update)\
        `event_kind:delete` (delete)
      </td>
    </tr>

    <tr>
      <td>
        Event (Fuzzy)
      </td>

      <td>
        `event:api_key` (api key events)\
        `event:entitlement` (entitlement events)\
        `event:login` (login events)\
        `event:package` (package events)\
        `event:retention` (retention events)\
        `event:service_account` (service account events)
      </td>
    </tr>
  </tbody>
</Table>

#### Field type modifiers (depending on the type, you can influence behaviour)

* For all queries, you can use:\
  `~foo` for negation

* For string queries, you can use:\
  `^foo` to anchor to start of term\
  `foo$` to anchor to end of term\
  `foo*bar` for fuzzy matching

* For number/date queries, you can use:\
  `>foo` for values greater than\
  `>=foo` for values greater / equal\
  `<foo` for values less than\
  `<=foo` for values less / equal

## 🔐 Audit Log Event Types (User and Organization)

Cloudsmith tracks a wide range of user and organization-level activities. The following audit events help you monitor security, access control, policy enforcement, and team collaboration across your organization.

| **Event**                           | **Identifier**                            | **Description**                                     | **Content Type** |
| ----------------------------------- | ----------------------------------------- | --------------------------------------------------- | ---------------- |
| API Token Refreshed                 | `user.api_token.refreshed`                | A user refreshed their API token.                   | User             |
| API Token Refresh Enforced          | `user.api_token.enforced_refresh`         | An API token refresh was enforced.                  | User             |
| API Token Expiry Notified           | `user.api_token.expiring_soon`            | User notified of upcoming API token expiration.     | User             |
| API Token Expired Notified          | `user.api_token.expired`                  | User notified that their API token has expired.     | User             |
| Password Updated                    | `user.password.updated`                   | User password was updated.                          | User             |
| User Login                          | `user.login`                              | User successfully logged in.                        | User             |
| Service Created                     | `user.service.created`                    | Created a new service user.                         | User             |
| Service Deleted                     | `user.service.deleted`                    | Deleted a service user.                             | User             |
| Service Key Refreshed               | `user.service.key_refreshed`              | Refreshed the key for a service user.               | User             |
| User Deactivated                    | `user.deleted`                            | A user account was deactivated.                     | User             |
| User Restored                       | `user.restored`                           | A previously deactivated user account was restored. | User             |
| Member Invited                      | `org.invite.invited`                      | Invited a new member to the organization.           | Org              |
| Invitation Canceled                 | `org.invite.canceled`                     | Canceled an organization invitation.                | Org              |
| Invitation Extended                 | `org.invite.extended`                     | Extended an existing invitation.                    | Org              |
| Invitation Accepted                 | `org.invite.accepted`                     | A user accepted an organization invitation.         | Org              |
| Member Added                        | `org.member.added`                        | A user was added to the organization.               | Org              |
| Member Removed                      | `org.member.removed`                      | A user was removed from the organization.           | Org              |
| OIDC Settings Created               | `org.oidc.created`                        | Created OpenID Connect (OIDC) settings.             | Org              |
| OIDC Settings Updated               | `org.oidc.updated`                        | Updated OIDC settings.                              | Org              |
| OIDC Settings Deleted               | `org.oidc.deleted`                        | Deleted OIDC settings.                              | Org              |
| Organization Deleted                | `org.deleted`                             | Deleted an organization.                            | Org              |
| Organization Renamed                | `org.renamed`                             | Renamed an organization.                            | Org              |
| Repo Creation Enabled               | `org.create_repos_enabled`                | Enabled repository creation in the organization.    | Org              |
| Repo Creation Disabled              | `org.create_repos_disabled`               | Disabled repository creation.                       | Org              |
| Team Creation Enabled               | `org.create_teams_enabled`                | Enabled creation of new teams.                      | Org              |
| Team Creation Disabled              | `org.create_teams_disabled`               | Disabled creation of new teams.                     | Org              |
| Invite Collaborators Enabled        | `org.invite_collaborators_enabled`        | Enabled collaborator invites.                       | Org              |
| Invite Collaborators Disabled       | `org.invite_collaborators_disabled`       | Disabled collaborator invites.                      | Org              |
| Invite Users Enabled                | `org.invite_users_enabled`                | Enabled user invites.                               | Org              |
| Invite Users Disabled               | `org.invite_users_disabled`               | Disabled user invites.                              | Org              |
| Unredacted Email View Enabled       | `org.view_unredacted_members_enabled`     | Enabled viewing member emails without redaction.    | Org              |
| Unredacted Email View Disabled      | `org.view_unredacted_members_disabled`    | Disabled viewing member emails without redaction.   | Org              |
| SCIM Provisioning Allowed           | `org.scim_allowed`                        | Allowed SCIM provisioning.                          | Org              |
| SCIM Provisioning Blocked           | `org.scim_blocked`                        | Blocked SCIM provisioning.                          | Org              |
| SAML Login Enabled                  | `org.saml_enabled`                        | Enabled SAML-based login.                           | Org              |
| SAML Login Disabled                 | `org.saml_disabled`                       | Disabled SAML-based login.                          | Org              |
| SAML Enforce Enabled                | `org.saml_enforce_enabled`                | Enforced SAML login for all users.                  | Org              |
| SAML Enforce Disabled               | `org.saml_enforce_disabled`               | Disabled SAML enforcement.                          | Org              |
| SAML Group Sync Enabled             | `org.saml_group_sync_enabled`             | Enabled SAML group synchronization.                 | Org              |
| SAML Group Sync Disabled            | `org.saml_group_sync_disabled`            | Disabled SAML group synchronization.                | Org              |
| Enforce 2FA Enabled                 | `org.enforce_2fa_enabled`                 | Enforced Two-Factor Authentication.                 | Org              |
| Enforce 2FA Disabled                | `org.enforce_2fa_disabled`                | Disabled 2FA enforcement.                           | Org              |
| License Policy Created              | `org.policy.license.created`              | Created a package license policy.                   | Org              |
| License Policy Updated              | `org.policy.license.updated`              | Updated a package license policy.                   | Org              |
| License Policy Deleted              | `org.policy.license.deleted`              | Deleted a package license policy.                   | Org              |
| Vulnerability Policy Created        | `org.policy.vulnerability.created`        | Created a vulnerability policy.                     | Org              |
| Vulnerability Policy Updated        | `org.policy.vulnerability.updated`        | Updated a vulnerability policy.                     | Org              |
| Vulnerability Policy Deleted        | `org.policy.vulnerability.deleted`        | Deleted a vulnerability policy.                     | Org              |
| API Key Policy Created              | `org.policy.api.policy_created`           | Created an API key policy.                          | Org              |
| API Key Policy Deleted              | `org.policy.api.policy_deleted`           | Deleted an API key policy.                          | Org              |
| API Key Auto-Refresh Enabled        | `org.policy.api.enforce_refresh_enabled`  | Enabled automatic API key refresh.                  | Org              |
| API Key Auto-Refresh Disabled       | `org.policy.api.enforce_refresh_disabled` | Disabled automatic API key refresh.                 | Org              |
| API Key Max Age Updated             | `org.policy.api.max_age_changed`          | Changed maximum allowed API key age.                | Org              |
| Package Deny Policy Created         | `org.policy.deny.created`                 | Created a package deny policy.                      | Org              |
| Package Deny Policy Updated (Name)  | `org.policy.deny.name_updated`            | Updated deny policy name.                           | Org              |
| Package Deny Policy Updated (Desc)  | `org.policy.deny.description_updated`     | Updated deny policy description.                    | Org              |
| Package Deny Policy Updated (Query) | `org.policy.deny.query_updated`           | Updated deny policy query.                          | Org              |
| Package Deny Policy Enabled         | `org.policy.deny.enabled`                 | Enabled a deny policy.                              | Org              |
| Package Deny Policy Disabled        | `org.policy.deny.disabled`                | Disabled a deny policy.                             | Org              |
| Package Deny Policy Deleted         | `org.policy.deny.deleted`                 | Deleted a deny policy.                              | Org              |
| Team Created                        | `org.team.created`                        | Created a team.                                     | Org              |
| Team Deleted                        | `org.team.deleted`                        | Deleted a team.                                     | Org              |
| Team Renamed                        | `org.team.renamed`                        | Renamed a team.                                     | Org              |
| Team Slug Renamed                   | `org.team.renamed_slug`                   | Changed the team’s slug.                            | Org              |
| Added to Team                       | `org.team.member_added`                   | Added a user to a team.                             | Org              |
| Removed from Team                   | `org.team.member_removed`                 | Removed a user from a team.                         | Org              |
| Team Role Changed                   | `org.team.role_changed`                   | Updated a team member’s role.                       | Org              |