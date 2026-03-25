# Source: https://docs.envzero.com/guides/admin-guide/environments/workflow-triggers.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure Workflow Triggers

> Configure chained environment deployments in env zero using workflow triggers for cascading automation

## Workflow Triggers in env zero

env zero allows you to configure chained dependent environments to your current environment. Using workflow triggers, you can define which environments would trigger a deployment downstream in response to a deployment of your current environment. This allows you to configure a cascading series of environment deployments.

Workflow triggers can be configured by Project Deployers and are viewable to all users.

<Info>
  Workflow triggers are operational only upon a **successful deploy** (and not destroy) and can be set only to an active environment. (i.e the *triggered environment* must be active)
</Info>

## How to set Workflow Triggers

Go to your existing **Environment** in env zero, and head over to the **Settings** tab.\
Under the **Workflow Triggers** card you can see a table that consist of all the triggered environments.

* To add a new workflow trigger, simply use the *Add New Trigger* dropdown to select any active environment in your project.

* To remove an existing workflow trigger, use the Trash icon next to the relevant trigger.

Hit *Save* to persist your changes.

<Frame caption="Workflow Triggers Card">
  <img src="https://mintcdn.com/envzero-b61043c8/SMkZGUXJ1AhEm5OR/images/guides/admin-guide/environments/workflow_triggers_configuration_interface.png?fit=max&auto=format&n=SMkZGUXJ1AhEm5OR&q=85&s=1b10520473743bf9c24806276f5c686e" alt="Workflow triggers configuration interface" width="1414" height="435" data-path="images/guides/admin-guide/environments/workflow_triggers_configuration_interface.png" />
</Frame>

Built with [Mintlify](https://mintlify.com).
