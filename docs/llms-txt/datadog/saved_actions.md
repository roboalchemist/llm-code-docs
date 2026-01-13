# Source: https://docs.datadoghq.com/actions/app_builder/saved_actions.md

---
title: Save and Reuse Actions
description: Save and reuse an action and its parameters
breadcrumbs: Docs > App Builder > Save and Reuse Actions
source_url: https://docs.datadoghq.com/app_builder/saved_actions/index.html
---

# Save and Reuse Actions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

Use the *Saved Actions* feature to save a copy of an action for reuse. You can insert a saved action into your app as a new step, or use a saved action to populate an existing step's parameters.

{% alert level="info" %}
You can only save actions if you have [Editor access.](https://docs.datadoghq.com/actions/app_builder/access_and_auth/#app-permissions) for that app.
{% /alert %}

## Save an action{% #save-an-action %}

1. In Datadog, navigate to [**Actions** > **App Builder**](https://app.datadoghq.com/app-builder/apps/list) and hover over an app. Action icons for that app will appear under the **Last Saved** column. Click the **Edit**  icon.
1. Click the **Actions**  menu, then **Save Action**.
1. Enter a name and description for the action.
1. If you want others in your organization to have access to the action, turn on the **Usable by others in the organization** toggle.
1. Verify the configuration details for the action and click **Save Action Configuration**.

## Use a saved action in your app{% #use-a-saved-action-in-your-app %}

1. In Datadog, navigate to [**Actions** > **App Builder**](https://app.datadoghq.com/app-builder/apps/list), hover over an app, and click the **Edit**  icon.
1. Click the **Actions**  menu and select **Use Saved Actions**.
1. Browse through the list to find the saved action you're looking for.
1. Select the saved action to add it as a configured step in your app.

## Manage a saved action{% #manage-a-saved-action %}

You can edit, clone, or delete your saved actions from the Action Catalog.

{% alert level="info" %}
If you did not create an action, you cannot delete it or edit it directly. Instead, select the Clone  icon to copy the action and make your configuration changes.
{% /alert %}

To find a saved action:

1. In Datadog, navigate to the [**Action Catalog**](https://app.datadoghq.com/actions/action-catalog).
1. Click **Saved Actions**.
1. Browse through the list of saved actions or use the search bar to search for actions by name. Hover over the saved action you'd like to edit, clone, or delete.
1. Click **Manage Saved Actions**.
1. Select the icon to edit , clone , or delete  the saved action.

## Further Reading{% #further-reading %}

- [Learn about actions in workflows](https://docs.datadoghq.com/actions/workflows/actions/)
- [Learn about integrations](https://docs.datadoghq.com/integrations/)

Do you have questions or feedback? Join the **#app-builder** channel on the [Datadog Community Slack](https://chat.datadoghq.com/).
