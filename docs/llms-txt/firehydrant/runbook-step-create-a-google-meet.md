# Source: https://docs.firehydrant.com/docs/runbook-step-create-a-google-meet.md

# Create a Google Meet

<Image alt="Google Meet Runbook step executing and link available in Command Center" align="center" width="650px" src="https://files.readme.io/1b7ddb1-Screenshot_2023-12-20_at_3.04.21_PM.png">
  Google Meet Runbook step executing and link available in Command Center
</Image>

FireHydrant makes it easy to automatically spin up a meeting bridge as part of the incident process. Once the meeting is created, a link to it will automatically be included on the channel's pinned message and anywhere FireHydrant has posted a [templated notification](https://docs.firehydrant.com/docs/runbook-step-notify-channel).

<Image alt="Google Meet link available on a [Notify message](https://docs.firehydrant.com/docs/runbook-step-notify-channel)" align="center" width="650px" src="https://files.readme.io/f98a5fa-Screenshot_2023-12-20_at_3.05.30_PM.png">
  Google Meet link available on a [Notify message](https://docs.firehydrant.com/docs/runbook-step-notify-channel)
</Image>

## Prerequisites

To use this step, you must have configured your [Google Meet integration](https://docs.firehydrant.com/docs/google-meet-integration).

## Add Runbook step

<Image alt="Google Meet step" align="center" width="650px" src="https://files.readme.io/ccd3f1d-image.png">
  Google Meet step
</Image>

To add the step, Edit a Runbook and search for the Google Meet step. The meeting topic or name is configurable with [templating](https://docs.firehydrant.com/docs/template-variables), allowing you to use any parameter on the incident to name the meeting.

> 📘 Note:
>
> You can create as many Google Meetings per incident as you like; they will all be captured and available to join.