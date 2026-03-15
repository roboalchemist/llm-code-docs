# Source: https://docs.jit.io/docs/integrating-with-shortcut.md

# Shortcut Integration

Integrating with Shortcut

Integrating **Shortcut** with **Jit** allows you to create security-related stories directly from findings and track remediation progress. Stories are automatically created with the `[Jit]` prefix and the `Opened-by-jit` label for easy identification. Learn more [here](https://docs.jit.io/docs/integrating-with-tms).

## Web App Integration

### Quickstart

1. In the Jit web app, go to the **Integrations** page.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/9de2ecf0e63ee943a32d31759c122678d8d772d0df1f33a98a986d32e7430e0c-Screenshot_2025-11-17_at_15.50.33.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "500px"
    }
  ]
}
[/block]

2. Find the **Shortcut** card and click **Connect**.
3. A connection window will appear. Click **Connect** in the top-right corner.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/db230ceb69b22443423c29bd3af401bba63d2711a3e49ca8ce3ce1ed7fb95d25-Screenshot_2025-11-17_at_15.51.41.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "500px"
    }
  ]
}
[/block]

4. Generate and provide a **Shortcut API Token**. Learn more [here](https://help.shortcut.com/hc/en-us/articles/205701199-Shortcut-API-Tokens).

* Log into your Shortcut account.
* Go to **Settings** → **API Tokens**.
* Create a new token with appropriate permissions.
* Copy the token and paste it in the **API Token** field.

❗️ **Note your token expiration** Make note of the expiration date - You will need to reconnect when expiration is reached, we advise to set `Never` as expiration.

5. **Connect the integration**\
   Use created API token to connect to **Shortcut**.

[block:image]{"images":[{"image":["https://files.readme.io/9045c01ce9ce42f721727185fba1f6dd5900a004aef8faa02e2e7657cbf1909b-Screenshot_2025-11-17_at_16.15.43.png",null,""],"align":"center","sizing":"500px"}]}[/block]

6. **Configure the integration:**

   * **Default Workflow Name** – Enter the name of the workflow to use for new stories (required).
   * **Default Project Name (Optional)** – Optionally enter a project name to associate stories with.
   * **Default Epic Name (Optional)** – Optionally enter an epic name to use as default for new stories.

   ![](https://files.readme.io/689e41554df2b91d8a8f9c611d24a0488624666068c7aa12b121fd5d790b24eb-Screenshot_2025-11-17_at_15.53.12.png)

   <br />

### Configuration Fields

#### Default Workflow Name (Required)

The workflow name determines which workflow state will be used when creating new stories. The system will automatically find the workflow by name and use its default state ID. This field is required because Shortcut's API requires a `workflow_state_id` when creating stories.

**Example:** `Engineering`, `Product`, `Backend`

#### Default Project Name (Optional)

If provided, stories will be associated with the specified project. The system will automatically find the project by name and add the `project_id` to the story. Projects are optional and can be used in addition to workflows for better organization.

**Example:** `Backend`, `Frontend`, `Infrastructure`

#### Default Epic Name (Optional)

If provided, new stories will be automatically associated with the specified epic. The system will search for the epic by name and add the `epic_id` to the story. This is useful for grouping related security findings.

**Example:** `Security Q1 2024`, `Vulnerability Remediation`

#### Completed Workflow State Name (Required for Auto-Close)

When enabling the "Close Shortcut Stories From Fixed Findings" workflow, you must specify the workflow state name that represents a completed/closed state. The system will automatically find this state by name across workflows and use it when closing stories.

**Example:** `Done`, `Completed`, `Closed`

### Features

#### Create Stories from Findings

From the **Findings** page, create stories directly from security findings.

Stories are automatically:

* Created with the `[Jit]` prefix in the name for easy identification
* Tagged with the `Opened-by-jit` label
* Set as `bug` story type
* Associated with your configured workflow (required)
* Optionally associated with your configured project and epic

The story description includes:

* Finding title, severity, and type
* Location information
* Detection details (security tool and date)
* Full finding description
* Links to learn more about the issue

#### Auto-Close Stories

Enable the **Close Shortcut Stories From Fixed Findings** workflow to automatically move stories to your specified completed state when findings are fixed in Jit.

**Configuration:**

* Enable the workflow toggle
* Enter the **Completed Workflow State Name** (e.g., "Done", "Completed")
* The system will automatically find the state by name across all workflows

❗️ **Important** The completed state name must match exactly (case-insensitive) with a workflow state in your Shortcut workspace.

#### Sync Story Status

Enable the **Listen to Shortcut Story Updates** workflow to automatically sync story status changes from Shortcut back to Jit. This enables bidirectional synchronization:

* When a story's workflow state changes in Shortcut, the status is updated in Jit
* When a story is archived in Shortcut, the status is set to "Archived" in Jit
* Only stories with the `[Jit]` prefix are processed

**Automatic Webhook Creation:** When you enable this workflow, Jit automatically creates a webhook in your Shortcut account. You don't need to manually configure webhooks - the integration handles this for you.

❗️ **Important**

* The webhook is automatically created when the workflow is enabled
* The webhook is user-specific and tied to your Shortcut connection
* Only workflow state changes and archive actions are synced back to Jit
* Stories without workflow state changes (e.g., title-only updates) are ignored

### Workflows

Integrate Shortcut into your workflows to automate story creation and status synchronization.

**After connecting:**

1. Configure your default workflow (required) and optionally set default project and epic
2. Enable the workflows you want to use:
   * **Create Stories from Findings** - Automatically creates stories when findings are created
   * **Close Shortcut Stories From Fixed Findings** - Automatically closes stories when findings are fixed
   * **Listen to Shortcut Story Updates** - Syncs status changes from Shortcut back to Jit
3. Go to **Settings** → **Workflows** to create automation rules

![](https://files.readme.io/fe218db1b09f1ad0754376ce0255bd62c7dd35eb5284906b9977cf4b1ad7da94-Screenshot_2025-11-17_at_15.57.01.png)

### Sample Story

When a story is created from a finding, it will look like this:

![](https://files.readme.io/b89d6921e6870ab4cde6880d8c5095f10e924664a217bc7ac9a027ab6e670c39-Screenshot_2025-11-17_at_16.03.04.png)

### Notes

* A label `Opened-by-jit` will be added to every created story to help Jit track tickets in your workspace.
* All stories created by Jit are prefixed with `[Jit]` in the name for easy identification.
* Stories are created as `bug` type by default.
* The workflow name matching is case-insensitive - you can enter "Engineering" or "engineering" and it will work.
* Project and Epic names are also matched case-insensitively.
* If a workflow, project, or epic name is not found, you'll receive an error message
* The webhook for status syncing is automatically managed - no manual configuration required.
* Only stories with workflow state changes are synced back to Jit to avoid unnecessary API calls.