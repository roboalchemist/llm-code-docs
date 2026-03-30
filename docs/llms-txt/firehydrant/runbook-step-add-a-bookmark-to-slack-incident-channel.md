# Source: https://docs.firehydrant.com/docs/runbook-step-add-a-bookmark-to-slack-incident-channel.md

# Add a Bookmark to Slack Incident Channel

> 📘 Note:
>
> This Runbook step is available for Slack only.

You can add custom bookmarks to your incident channels using the same conditional execution rules as other runbook steps. This allows you to include links to useful resources and attach links or playbooks based on assigned teams, impacted services, and more.

<Image alt="Add a bookmark Runbook step" align="center" width="650px" src="https://files.readme.io/91dad0d-image.png">
  Add a bookmark Runbook step
</Image>

## Prerequisites

* You'll need to have [Slack](https://docs.firehydrant.com/docs/slack-integration) configured
* Before this step executes, you'll need to ensure the channel exists on the incident first. See [Conditions](#conditions) below.

## Configuration

There are two available fields:

* **Bookmark Title** - The display name of the bookmark in the channel. For example, `UI Portal Playbook`.
* **Bookmark Link** - Where that bookmark should direct to. For example, `https://path-to-a-google-doc`.

Both fields support [Template Variables](https://docs.firehydrant.com/docs/template-variables).

### Conditions

<Image alt="Ensuring the channel exists before this step runs" align="center" width="650px" src="https://files.readme.io/1e48352-image.png">
  Ensuring the channel exists before this step runs
</Image>

By default, we include this condition on the step, but just in case, you will also want to ensure the channel creation step is completed before this bookmark step executes; otherwise, it could fail if it tries to run before the channel exists.

The above example should lead to the custom bookmark attaching to your incident channel next to your internal status page and Command Center links, like so:

<Image alt="Example of a bookmark added to an incident channel" align="center" width="650px" src="https://files.readme.io/bbd3682-slack-bookmark-2.png">
  Example of a bookmark added to an incident channel
</Image>