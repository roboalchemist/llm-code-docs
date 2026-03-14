# Source: https://docs.envzero.com/guides/integrations/notifications/microsoft-teams.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Microsoft Teams Integration

> Integrate env zero with Microsoft Teams to receive deployment notifications via webhook workflows

## Prerequisites - Microsoft Teams

<Warning>
  Retirement of Office 365 connectors in MS Teams

  Microsoft is retiring Office 365 connectors from MS Teams. Existing connectors may be updated to work until December 2025, but starting August 15th, 2024, all new connectors must be created using the Workflow App in MS Teams. [Read more](https://devblogs.microsoft.com/microsoft365dev/retirement-of-office-365-connectors-within-microsoft-teams/#:~:text=Starting%20August%2015th%2C%202024%20we,%2C%20flexible%2C%20and%20secure%20way.)
</Warning>

To start using Microsoft Teams notifications with env zero, you must first create a ***Post to a channel when a webhook request is received*** flow, as explained in [Microsoft docs](https://support.microsoft.com/en-us/office/post-a-workflow-when-a-webhook-request-is-received-in-microsoft-teams-8ae491c7-0394-4861-ba59-055e33f75498):

1. In Microsoft Teams, choose ***Workflows*** and click on ***+ New flow***
2. Choose ***Post to a channel when a webhook request is received*** .
3. Setup the flow and connect to your desired channel.
4. Copy the webhook to the clipboard and save it. You'll need the webhook URL for sending information to Microsoft Teams.
5. Choose Done.
6. You can see all flows in the ***Workflows*** under the ***Home*** tab:

<img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/notifications/6c215f9-image.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=31b0202e7810b1dfbbfff25a945883aa" alt="" width="2848" height="1225" data-path="images/guides/integrations/notifications/6c215f9-image.png" />

Built with [Mintlify](https://mintlify.com).
