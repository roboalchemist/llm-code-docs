# Source: https://docs.firehydrant.com/docs/intro-to-runbooks.md

# Intro to Runbooks

<Image align="center" alt="Example of a Runbook and steps within" border={false} caption="Example of a Runbook and steps within" src="https://files.readme.io/5bbf9f6-CleanShot_2024-08-13_at_17.15.34.png" width="650px" />

## What is a Runbook?

Runbooks are FireHydrant's automation engine. They define and automate a workflow of steps and actions according to specified conditions.

Runbooks consist of steps, which are individual actions or units of automation. Some examples of actions include creating a Slack channel, starting a Zoom meeting, or creating a Jira ticket, among many more.

The automation Runbooks provide reduces toil and allows responders to focus immediately on resolving the incident.

## Default Runbook

When you first sign up for an account, FireHydrant builds a **Default Runbook** for you that always attaches to every incident. It comes with a couple default steps and dynamically inserts more based on the integrations you install.

* The default Runbook will always have two default steps:
  * **[Assign a Role](https://docs.firehydrant.com/docs/runbook-step-assign-a-role)**: Assigns whoever opened the incident to the [Commander role](https://docs.firehydrant.com/docs/incident-roles).
  * **[Add Task List](https://docs.firehydrant.com/docs/runbook-step-add-task-list)**: Assigns a [default Task List](https://docs.firehydrant.com/docs/managing-tasks) to whoever is the Commander.
* If you install the [Slack integration](https://docs.firehydrant.com/docs/slack-integration), FireHydrant automatically inserts the following steps:
  * **[Create or Rename Incident Channel](https://docs.firehydrant.com/docs/runbook-step-create-incident-channel)**: Creates an incident channel linked to the incident.
  * **[Archive Incident Channel](https://docs.firehydrant.com/docs/runbook-step-archive-incident-channel)**: Automatically archives the incident channel. The default condition is "When milestone = Retrospective Completed".
* If you install either [Google Meet](https://docs.firehydrant.com/docs/google-meet-integration) or [Zoom](https://docs.firehydrant.com/docs/zoom-integration), FireHydrant will insert one of the following steps:
  * **[Create a Google Meet](https://docs.firehydrant.com/docs/runbook-step-create-a-google-meet)**
  * **[Create a Zoom Meeting](https://docs.firehydrant.com/docs/runbook-step-create-a-zoom-meeting)**

The default Runbook is an introduction to and basic example of Runbooks. Organizations are able and encouraged to make any modifications and build additional Runbooks beyond the Default.

## Managing Runbooks

### Creating a Runbook

To create a new Incident Runbook:

1. Go to the [Runbooks](https://app.firehydrant.io/runbooks) page and click "+ Add runbook."
2. Fill out a name and description to make this Runbook discoverable in the future. If you want this Runbook to only attach to certain incidents, you can specify [Runbook conditions](#runbook-conditions).
3. In the steps section, click "+ Add Step." In this modal, you can search for all available Runbook steps to add to the incident. More steps become available as more integrations are added. See [Integrations Overview](https://docs.firehydrant.com/docs/integrations-overview) for an overview of all the available integrations.
4. Once you click on a step, you are presented with configuration options that will be different depending on the step. The **Details** tab shows specific details you can configure for this step, and the **Conditions & scheduling** tab allows you to specify [execution conditions for the step](#step-conditions). When you are finished, click "Add step" button.
5. In addition to adding steps, you can perform actions on existing steps in the Runbook, including editing the step, moving it up and down on the list\*\*, duplicating, and deleting it.

   <Image align="center" border={false} width="650px" src="https://files.readme.io/37e3393-CleanShot_2024-08-13_at_17.17.47.png" />
6. Repeat steps #3 - #5 above until you've configured the Runbook to your liking. Then click "Save Runbook" on the top right.

> 📘 \*\*Note:
>
> Runbooks are designed for each step to execute immediately and concurrently; this means Runbook steps won't always execute in order (as they appear in the FireHydrant UI).
>
> To add Runbook steps that won't be executed until after another specific step, you can add that limitation by using Runbook [conditions](#step-conditions).

### Editing a Runbook

To edit a Runbook, navigate to your [Runbooks](https://app.firehydrant.io/runbooks) page and then click on the Runbook you want to edit. In this page, click on "Edit Runbook". This screen will be the same screen you saw in [Creating a Runbook](#creating-a-runbook) you saw above.

### Duplicating a Runbook

<Image align="center" alt="Action buttons in a Runbook, just below Execution Rules in the Details panel" border={false} caption="Action buttons in a Runbook, just below Execution Rules in the Details panel" src="https://files.readme.io/ef5a496-CleanShot_2024-08-13_at_17.19.14.png" width="400px" />

You can create copies of any existing Runbook by entering the Runbook's details and clicking **Copy** on the bottom right in the details panel. This clones the Runbook's steps to a **New Runbook** screen, allowing you to begin editing from what's existing and creating a new Runbook.

### Deleting a Runbook

Similar to duplicating a Runbook, you can delete a Runbook by going into the Runbook's details and clicking **Delete** at the bottom right in the details panel.

### Runbook Ownership

You can lock down Runbooks so that only users from a specific team can edit them. By default, Runbooks do not have Owners, and subsequently, Runbooks are editable by anyone in your organization who has <Glossary>Owner</Glossary> or <Glossary>Member</Glossary> permissions.

> 🚧 Note:
>
> Once you set the Owning Team on a Runbook and save, permissions changes immediately take effect. So if you are not a member of the Owning Team that is set, you will immediately lose Edit access to that Runbook.

## Runbook Execution

<Image align="center" alt="Visual overview of Runbook execution lifecycle" border={false} caption="Visual overview of Runbook execution lifecycle" src="https://files.readme.io/1ffde5f-CleanShot_2024-08-14_at_17.36.41.png" width="650px" />

At any time, all of your incidents are constantly evaluating your Runbooks' conditions. This means Runbooks can attach at any time throughout an incident's lifecycle as soon as conditions match or when manually attached.

When attaching a Runbook, FireHydrant uses the snapshot of the defined Runbook and its steps at that given moment, so any changes to Runbook steps and definitions after a Runbook has been attached to incidents will not be reflected on said incidents, only future attachments.

### Automatic Attachment

<Image align="center" alt="Example Runbook conditions" border={false} caption="Example Runbook conditions" src="https://files.readme.io/e810d83-CleanShot_2024-08-07_at_10.29.04.png" width="400px" />

You can configure Runbooks to automatically attach based on your defined conditions and triggers. To learn more, visit [Runbook Conditions](https://docs.firehydrant.com/docs/runbook-conditions).

### Manual Attachment

<Image align="center" alt="Attaching Runbook via Command Center and Microsoft Teams Tab" border={false} caption="Attaching Runbook via Command Center and Microsoft Teams Tab" src="https://files.readme.io/2e15828-CleanShot_2024-08-07_at_10.20.22.png" width="650px" />

<Image align="center" alt="Attach from Slack with `/fh runbooks`" border={false} caption="Attach from Slack with `/fh runbooks`" src="https://files.readme.io/a05280a-CleanShot_2024-08-07_at_10.24.43.png" width="400px" />

You can manually attach Runbooks to execute them by visiting the **Runbooks** tab and clicking **+ Attach a Runbook** when using the web UI and Microsoft Teams Tab in the incident channel. In Slack, you can run `/fh runbooks` to pull up the Runbooks modal.

Manually attaching a new Runbook will immediately process the steps within and their conditions.

### Stopping and Rerunning

<Image align="center" alt="Stop and Run again buttons when viewing a Runbook on an incident" border={false} caption="Stop and Run again buttons when viewing a Runbook on an incident" src="https://files.readme.io/52e2364-CleanShot_2024-08-07_at_10.36.32.png" width="650px" />

After a Runbook has been attached, you can view it directly in the Command Center by visiting the **Runbooks** tab and clicking on the specific Runbook. Within, you'll also see buttons to **Stop runbook** and **Run again**, which will halt all steps in the Runbook and then re-execute and re-evaluate them, respectively.

> 📘 Note:
>
> When stopping and re-running a Runbook, it will re-execute the steps as-attached and will not include any changes made to the Runbook post-attachment.

## Step Execution

<Image align="center" alt="Visual overview of Runbook Step execution lifecycle" border={false} caption="Visual overview of Runbook Step execution lifecycle" src="https://files.readme.io/143d46e-CleanShot_2024-08-14_at_18.04.16.png" width="650px" />

A Runbook's steps will begin evaluation and execution when the Runbook itself has attached. Just like Runbooks, individual Runbook steps can automatically execute, execute based on conditions, or be manually triggered.

Some steps are repeatable, while other steps can only be executed once. Repeatable steps can be rerun so long as the Runbook has not completed its lifecycle. 30 days after a step is scheduled, if it still has not completed, it will terminate automatically.

<Image align="center" alt="Example of taking manual actions on a Runbook step" border={false} caption="Example of taking manual actions on a Runbook step" src="https://files.readme.io/40de89aa47ca478abad9d285d253c0d60d586a7ad38f1783c710871be48a3c4e-CleanShot_2025-01-03_at_13.46.342x.png" width="650px" />

Just like with Runbooks, individual steps can be triggered, retried, or stopped within the Command Center's Runbooks page.

## Visual Explorer

<Image align="center" alt="Runbook Visual Explorer" border={false} caption="Runbook Visual Explorer" src="https://files.readme.io/4661a5f-CleanShot_2024-08-14_at_18.21.45.png" width="650px" />

Within each Runbook and when browsing a Runbook's execution status in [The Command Center](https://docs.firehydrant.com/docs/the-command-center), there is a **Visual Runbook Explorer**. This can help you visually see which steps depend on which other steps, and what has already executed vs. not.

To view the explorer, toggle the switch at the top next to **Explorer**.

## Next Steps

* Learn how to use Runbooks further by understanding [conditions](https://docs.firehydrant.com/docs/runbook-conditions).
* Read about [Runbook Best Practices](https://docs.firehydrant.com/docs/runbook-best-practices) and see some suggested Runbook recipes.
* Set up some basic conditions in your Runbooks and test them out. Then, tailor the Runbooks for different situations (e.g., `SEV1` vs. `SEV2`) or for different teams and impacted components.
* Browse the [Runbook Steps](https://docs.firehydrant.com/docs/runbook-steps) that are available, or check out our [Integrations Overview](https://docs.firehydrant.com/docs/integrations-overview) to learn more about all of our integrations. Configuring more integrations will unlock more Runbook steps.