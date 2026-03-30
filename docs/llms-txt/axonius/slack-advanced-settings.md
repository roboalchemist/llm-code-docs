# Source: https://docs.axonius.com/docs/slack-advanced-settings.md

# Slack Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

### Fetch Settings

Configurations that define how data is fetched from the data source:

* **Fetch deleted users** *(required, default: true)* - Select this option to fetch deleted users. When cleared, only active users are fetched.
* **Fetch user conversations** - Select this option to fetch Slack conversations. This requires the `admin.conversations:read` permission.
* **Fetch groups** - Select this option to fetch Slack groups as assets. This requires the `admin.usergroups:read` permission.
* **Fetch Roles** - Select this option to fetch roles in Slack.
* **Fetch Application Add-Ons** - Select this option to installed, third-party application add-ons.
* **Fetch Approved Apps** - Select this option to fetch approved apps in Slack. This required the admin scope.
* **Fetch Application Settings** - Select this option to fetch Application Settings from Slack API. Ensure you have the [required permissions](https://docs.axonius.com/update/docs/slack-permissions) for that.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>