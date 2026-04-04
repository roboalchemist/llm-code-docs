# Source: https://docs.gitguardian.com/platform/enterprise-administration/workspace-settings.md

# Workspace settings

> Configure workspace-level settings for collaboration, sharing, incident permissions, and default behaviors.

## Collaboration and sharing options

### Team leaders can invite workspace users

:::info
This feature is only available for workspaces with a Business plan.
:::

These settings are designed to give non-manager users the ability to onboard new users onto the platform, reducing the administrative burden on workspace managers.

Enabling this setting allows users with the `Member` access level to invite people to the teams they lead. Team leaders can only invite new users by adding them to their teams and cannot invite new users to the workspace via the Settings > Members page.
Newly added users will be assigned the `Member` access level. Upon signing up, they will automatically be added to the team from which they were invited.

This setting is `ON` by default. Deactivate it [in your workspace settings](https://dashboard.gitguardian.com/settings/workspace/general) if you want the privilege of adding new users to your workspace to remain exclusive to `Managers`.

### âFull accessâ incident permissions allow to invite users

:::info
This feature is only available for workspaces with a Business plan.
:::

Similarly, this setting allows non-manager users who belong to a team and have [`Full access`](../collaboration-and-sharing/incident-permissions-and-sharing) incident permission to invite new users to the workspace. The goal is to enable trusted team members to take an active role in onboarding new users, without requiring manager-level access. Users with `Full access` incident permission can only invite new users by granting them access to the incident where they have `Full access` permission, and cannot invite new users to the workspace via the Settings > Members page.

Upon signup:

- the newly added user will only have access to the incident they have been invited from
- to prevent privilege escalation, the access level of the new user will be the same as the person who granted them access to the incident:
  - If granted access by a `Restricted` user, the new user will have the `Restricted` access level.
  - If granted access by a `Member` user, the new user will have the `Member` access level.
  - If granted access by a `Manager` user, the new user will have the `Member` access level since we consider the highly privileged `Manager` access level can only be given specifically on the Settings > Members page.

This setting is `ON` by default. Deactivate it [in your workspace settings](https://dashboard.gitguardian.com/settings/workspace/general) if you want the privilege of adding new users to your workspace to remain exclusive to `Managers`.

### Public sharing

In the [workspace settings](https://dashboard.gitguardian.com/settings/workspace/general), Managers can activate or deactivate public sharing across the entire workspace. Enabling public sharing allows users to access an incident without needing to be registered.
For more details about public sharing, please refer to our [Collaboration and sharing section](../collaboration-and-sharing/incident-permissions-and-sharing).

Public sharing is available in all plans:

- in the `Free` plan, both Managers and Members can perform public sharing.
- in the `Business` plan, only users with `Full_access` incident permission can perform public sharing.

Public sharing is `OFF` by default.

### By default, users are notified by email when a new incident is detected

:::info
This feature is only available for workspaces with a Business plan.
:::

When this setting is enabled, users will automatically receive email notifications whenever a new incident is detected within a member's team perimeter. This notification can be modified by users in their personal settings under [Secrets detection > Incident alerting](https://dashboard.gitguardian.com/settings/personal/notifications), overriding the workspace setting if needed.

Workspace Managers can adjust the default notification setting for all users via the workspace settings. If email notifications for new incidents are disabled, users should rely on the notifier configured at the team level. For further details on configuring alerting and notifications, please refer to the [Alerting and Notifications](../configure-alerting/alerting-and-notifications) page.

This setting is `ON` by default. To disable email notifications for new incidents by default for both new and existing users, deactivate it in your [workspace settings](https://dashboard.gitguardian.com/settings/workspace/general).

### Enable comments and feedback for "Can view" permission

Managers can allow team members with the `Can view` incident permission to provide comments and feedback on incidents. Enable or disable this option in your [workspace settings](https://dashboard.gitguardian.com/settings/workspace/general) to broaden collaboration without granting edit rights.

This setting is `OFF` by default.

## Security options

### Maximum lifetime of API personal access tokens

:::info
This feature is only available for workspaces with a Business plan.
:::

In [the workspace settings](https://dashboard.gitguardian.com/settings/workspace/security), Managers can enforce a maximum lifetime for API personal access tokens created within their workspace. This applies whether the creation happens via [the API > Personal access tokens page](https://dashboard.gitguardian.com/api/personal-access-tokens) or via ggshield using the `ggshield auth login` command.

If existing personal access tokens exceed the new maximum lifetime at the time of the setting modification, GitGuardian will force their lifetime to fit the new setting, starting from the time of the setting modification.

By default, there is no enforced maximum lifetime for API personal access tokens.

### Restrict git patch visibility

:::info
This feature is only available for workspaces with a Business plan.
:::

In [the workspace settings](https://dashboard.gitguardian.com/settings/workspace/security), Managers can activate the restriction for git patch visibility.

When the restriction is activated, the git patch of an occurrence will be visible to a user if either of the following conditions are met:
- **The user is a member of a team that includes the repository where the occurrence took place**. It's worth noting that since workspace Managers are automatically part of the "All-incidents" team, they will always have access to all the git patches.
- **The user is directly involved in the occurrence**, meaning their email matches the committer email of the occurrence.

It is important to note that while the restriction on git patch visibility is in effect, the metadata of an occurrence will still be visible to users. Only the git patch of the occurrence will be impacted by the restriction. 
This means that there may be instances where a user has access to a secret incident that contains multiple occurrences. The user will be able to view the metadata of all occurrences, but only a subset of them will have visible git patches.

This distinction is critical to ensure an effective remediation when multiple teams are involved and collaboration is necessary. By restricting access to the code (git patch) of each other's occurrences, teams can maintain the necessary level of confidentiality while still working together to resolve the incident.

When the restriction on git patch visibility is enabled, the git patches of occurrences are hidden on the public share page of an incident.

### Enable API endpoint to retrieve detected secrets in clear text for each incident

:::info
This feature is only available for workspaces with a Business plan.
:::

In [the workspace settings](https://dashboard.gitguardian.com/settings/workspace/security), Managers can control access to secret values through the API endpoint `/v1/secrets/{secret_id}`. This endpoint allows users to securely retrieve secret values directly via the API, enabling enhanced security automation and integration with existing security workflows.

The secret access API provides several layers of security controls that must be properly configured:

- **Personal Access Token (PAT) permissions**: Users must have appropriate PAT permissions (`secret:read`) to access secret values. SAT are not allowed.
- **Workspace settings**: Managers must first activate the setting to enable API access to secrets at the workspace level.
- **IP allowlisting**: Workspace owners need to configure [IP-based access controls to allow access from authorized sources](./ip-allowlist).
- **Complete secret context**: Once properly configured, the API returns both the secret value and detector information for comprehensive remediation.

For more information about using this API endpoint, please refer to the [API documentation](https://api.gitguardian.com/docs#tag/Secret-Incidents/operation/get-secret-detail).

### Session duration

In [the workspace settings](https://dashboard.gitguardian.com/settings/workspace/security), Managers can customize how long a dashboard session lasts before users are automatically logged out.

Choose from one of the preset durations or select **Custom** to specify a session duration in minutes. Leave the custom duration field empty to reset to GitGuardian defaults.

:::warning
Changing the session duration requires all users to log in again once the change is applied.
:::

### Restrict Personal Access Token scopes

:::info
This feature is only available for workspaces with a Business plan.
:::

In [the workspace settings](https://dashboard.gitguardian.com/settings/workspace/security), Managers can restrict the scopes available to Members when creating Personal Access Tokens (PATs). This allows Managers to enforce the principle of least privilege by limiting what Members can do with their tokens.

This restriction does not apply to Managers.

By default, there is no restriction on PAT scopes for Members.
