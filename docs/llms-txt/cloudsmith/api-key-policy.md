# Source: https://help.cloudsmith.io/docs/api-key-policy.md

# API Key Policy

## API Key Policy Overview

The API key policy allows workspaces to customize the maximum age of API keys across all workspace accounts, by specifying the duration after which keys should be rotated. Frequent API Key rotation ensures that API keys older than the designated age are invalidated for authentication, with the added flexibility to enforce a refresh for keys that exceed the specified duration.

## View API Key Policy

To view your workspace's API Key Policy, go to your Workspace settings > Manage policies and select Authentication Policies from the left-hand menu.

> 📘 Note
>
> The API Key Policy is disabled by default.

<Image
  alt="API Key Policy

"
  align="center"
  src="https://files.readme.io/968354c3784e9cf543591c4d432d35902ca80caa4617a4840204e69cea5df8a1-api-key-policies.png"
>
  API Key Policy
</Image>

## Enable API Key Policy

To enable the API Key Policy, set the "Maximum permitted age (hours)" field and click "Update policy".

<Image
  alt="Enable API Key Policy

"
  align="center"
  src="https://files.readme.io/458fb4315f9da55ac80d898f0f41a5910256f6bd550718dd3b5783247a32919b-api-key-policies-2.png"
>
  Enable API Key Policy
</Image>

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th />

      <th />
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **Maximum permitted age (hours)**
      </td>

      <td>
        The maximum permitted age of an account's API key.

        Note: the minimum value this can be set to is “24”.
      </td>
    </tr>

    <tr>
      <td>
        **Days**
      </td>

      <td>
        Read-only field, displaying the value of "Maximum permitted age (hours)" field in days.

        For example, if the "Maximum permitted age (hours)" field is set to “720” hours, this field will display “30” days.
      </td>
    </tr>

    <tr>
      <td>
        **Enforce automatic API key refresh**
      </td>

      <td>
        Enable to automatically refresh API keys that violate the policy. Take extreme caution when enabling this option, as this cannot be undone.

        See section [ Enforce Automatic API Key Refresh](https://help.cloudsmith.io/docs/api-key-policy#enforce-automatic-api-key-refresh) for further details.
      </td>
    </tr>
  </tbody>
</Table>

Once the policy is enabled, permission will be revoked for any API key older than the specified maximum age. This applies to all accounts associated with the workspace, including members, managers, owners, service accounts, and collaborators.

If a user attempts to utilize an API key that violates the policy, they will receive a "permission denied" error message

To regain access, the user should update their [API Key](https://help.cloudsmith.io/docs/api-key) by clicking "Refresh" within the API settings page.

<Image alt="Refresh API Key" align="center" src="https://files.readme.io/1aff04357788e8383754d7e927c208b63650165ba77cea164b2793058177bc4d-api-key-refreshv2.png">
  Refresh API Key
</Image>

### Enforce Automatic API key Refresh

> 🚧
>
> Exercise extreme care when utilizing this option, as refreshing an API key is an irreversible action.

To automatically force refresh an API key that violates the policy, enable "Enforce automatic API key refresh".

> 📘
>
> This force refreshes API keys of all users (member, manager, owners and service accounts) that violate the policy, except for collaborators.

<Image align="center" src="https://files.readme.io/8bd8870f1c66a205315c5937a98403d8fc6cb58c6778968115cf669fb7707991-automatically-refresh.png" />

> 📘
>
> The process of force refreshing all API keys may take up to 60 minutes to complete.

To enforce an immediate refresh of API keys that violate the policy, enable both the "Enforce automatic API key refresh" and "Refresh immediately" options.

<Image align="center" src="https://files.readme.io/eeebfd89e143f3cda6be80517d2aad357454e93c039cb48d380b16b256e5a14f-refresh-immediately.png" />

## Disable API Key Policy

To disable the API key policy, clear the value within the "Maximum permitted age (hours)" field and click "Update policy".

<Image align="center" src="https://files.readme.io/ff914822a6436fde7f9b860a1857ab40d53d3ebcb01d5e1a65f1357b76402801-disable-api-key-policy.png" />

The UI will then update to confirm the Policy has been disabled.

<Image align="center" src="https://files.readme.io/e6c8ed318a1507a5f21eabddbe6f3e2f7a956be5b5f8e902fee477b0c5147705-confirmed-disabled.png" />

Once disabled, restrictions to API keys that previously violated the policy are lifted and these API keys will become operational again.

## Members of Multiple Workspaces

If a user is a member of multiple workspaces the user's permissions will only be revoked for the workspace where the API key policy is enforced and their API key violates the policy. Their permissions in all other workspaces are unaffected.

However, if the user is a member of a workspace which also has "Enforce automatic API key refresh" enabled, the user's API key will be refreshed across all their workspaces.

## Notifications

When an API key is approaching its expiration age, users will receive a notification at least 24 hours in advance. This notification will be sent via email and will also appear as a notification when they log into the application.

Additionally, users will receive an email and UI notification when their API key has expired.

If the API policy is enabled and "Enforce automatic API key refresh" is set, users will also receive an email notification when their API key has been refreshed. This email will include details about the user who initiated the refresh process.

For service accounts, the creator of the service account will receive an email notification informing them of the upcoming expiration of the service's API key. The email also provides a URL that the user can use to reset the API key. Additionally, when the creator logs into the application's user interface, they receive a warning message.

If a service account has been created by another service account, no email notification will be sent for an upcoming API key expiration. In this scenario, with the API Key Policy enabled, you can use the [Get a list of all services within a workspace](https://help.cloudsmith.io/reference/orgs_services_list) REST API call to retrieve your services, and find each respective key expiry in the `key_expires_at` field.

## Audit Logs

All actions and notifications related to the API Key Policy are also logged within the Audit logs.

In scenarios where a user is a member of multiple workspaces, it is important to note that the user who enforces the API key refresh will only be visible as the initiator within the workspace where they hold the ownership role. In other workspaces where the user is a member, the API key refresh action will still be recorded in the audit logs. However, the user who enforced the refresh will be obscured, and the action will be listed as a "refreshed API key" rather than an "enforced API key refresh."