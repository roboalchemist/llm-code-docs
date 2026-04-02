Source: https://docs.slack.dev/changelog/2024-05-security-updates-coded-workflows

# Release: version 2.25.0 of the Slack CLI

May 30, 2024

Version 2.25.0 of the developer tools for the Slack automations platform is kicking off the summer fun!

* You can now update your local project's `apps.json` file with app IDs for your existing apps using the `slack app link` command. Refer to [app commands](/tools/slack-cli/reference/commands/slack_app) for more details.
* We've updated the formatting for section text and trace prints for the `slack collaborator add`, `slack collaborator list`, and `slack collaborator remove` commands.
* We've updated the debug log output when installing dependencies using the `slack create` command. We also now suggest installing project dependencies if an error occurs when running this command.
* We fixed a bug to avoid formatting printed strings if the string to be printed has no arguments.
* We now set authentication configurations such as custom API hosts for selected tokens with the `slack manifest validate` command.
* Starting **June 11, 2024**, we are enforcing admin restrictions on built-in steps and webhook triggers in coded workflows. This update aims to align the security settings of coded workflows with those of connector steps and triggers. Read on to learn more.

## Enforcing admin restrictions on built-in steps and triggers in coded workflows {#enforcing-admin-restrictions-on-built-in-steps-and-triggers-in-coded-workflows}

### What is changing {#what-is-changing}

Starting June 11, 2024, we are enforcing admin restrictions on built-in steps and triggers in coded workflows. This update aims to align the security settings of coded workflows with those built in Workflow Builder.

Specifically, the changes include:

* **Restricted Steps**: Coded workflows using restricted steps will continue to function but **cannot** be updated or republished unless permissions are granted by an admin.
* **Restricted Triggers**: Creation of **new** triggers will be subject to your team's trigger restrictions; this cannot be bypassed via the CLI. This also includes updates to workflows using previously created webhook triggers on teams that had denied access to webhook triggers in workflow builder prior to the addition of dedicated admin trigger restrictions.

### Why this change is happening {#why-this-change-is-happening}

We understand that breaking changes are never easy, and we appreciate your patience and understanding. We are implementing this update to enhance the consistency and reliability of our platform. By applying the same admin-set restrictions to coded workflows as we do to Workflow Builder-built workflows with connector steps or webhook triggers, we are ensuring that settings are uniformly applied across all workflows. This will provide a higher level of control and predictability for admins and developers going forward.

### What are restricted steps and triggers? {#what-are-restricted-steps-and-triggers}

Admins can restrict steps and triggers in Workflow Builder. When a step or trigger is restricted by an admin, users are prevented from using them in their workflows.

Restricted steps may include third-party connectors, custom steps, and steps for creating or modifying channels and user groups. For more details, refer to the [Slack administration guide on restricting custom steps for Workflow Builder](https://slack.com/help/articles/13621100461203-Slack-administration--Restrict-custom-steps-for-Workflow-Builder).

### Developer options {#developer-options}

When attempting to update or republish a coded workflow using restricted steps or triggers, developers will receive a clear error message from the Slack CLI indicating the restriction (`user_cannot_use_function` or `user_cannot_use_trigger_type`).

To address these restrictions, developers have two options:

1. **Request Permission**: Admins can grant the necessary permissions via the **Workflow Steps & Triggers** page in the org dashboard.
2. **Modify Workflows**: Developers can update their workflows to use non-restricted steps or triggers that comply with the admin settings.

### Timeline {#timeline}

* **June 11, 2024**: The enforcement of these admin restrictions will go into effect on this date. Any updates or new webhook triggers created after this date must comply with the updated settings.

### Impact {#impact}

* Existing coded workflows will continue to execute without interruption.
* Updates to coded workflows and the creation of new triggers will be subject to the enforced admin restrictions.

Please ensure that your workflows are compliant with these security enhancements by June 11, 2024.

**Tags:**

* [Release](/changelog/tags/release)
* [Slack CLI](/changelog/tags/slack-cli)
