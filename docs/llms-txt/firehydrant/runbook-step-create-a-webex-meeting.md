# Source: https://docs.firehydrant.com/docs/runbook-step-create-a-webex-meeting.md

# Create a Webex Meeting

<Image alt="Example incident with a Webex bridge" align="center" width="650px" src="https://files.readme.io/ba06b79-Screenshot_2023-12-20_at_5.07.48_PM.png">
  Example incident with a Webex bridge
</Image>

With this Runbook step, FireHydrant can automatically create a Webex Meetings bridge as part of the incident process. Once the meeting is created, a link will automatically be included on the channel's pinned message in Slack, and anywhere FireHydrant has posted a templated notification.

## Prerequisites

Ensure you have the [Webex](https://docs.firehydrant.com/docs/webex-integration) integration configured.

## Adding the step

To add the step, Edit a Runbook and search for the Webex step. The meeting title and agenda are configurable with [templating](https://docs.firehydrant.com/docs/template-variables), allowing you to use any parameter on the incident to name the meeting.

In addition, you can configure whether users should be able to join before the host and whether the meeting is recorded in the step.

> 🚧 Note:
>
> You can only create one Webex meeting bridge per incident.