# Source: https://docs.firehydrant.com/docs/tutorial-runbooks.md

# Tutorial Runbooks

FireHydrant provides specialized "Tutorial" type Runbooks which will always attach by themselves and only attach to incidents created by executing `tutorial` commands in your chat tool.

These are useful for your organization to quickly onboard and familiarize new responders to using FireHydrant using your processes.

## Creating Tutorial Runbooks

<Image alt="&#x22;Use for tutorial incidents&#x22; setting checked" align="center" width="400px" src="https://files.readme.io/f0b64e3-CleanShot_2024-06-21_at_17.05.49.png">
  "Use for tutorial incidents" setting checked
</Image>

When creating or editing Runbooks, there is an additional checkbox on the right-side details panel labeled "Use for tutorial incidents."

Checking this setting configures this Runbook to be used exclusively for whenever a user executes `/fh tutorial` or `@FireHydrant tutorial`. Only a single Runbook can be marked as a tutorial-type Runbook at any given time, and when executing the `tutorial` commands, the tutorial-type Runbook will attach exclusively without adding additional Runbooks.

If you don't have a Tutorial Runbook, you can start one from a template and then modify according to your organization's needs. Create a new Runbook, and then select **Tutorial** from the list of templates.

<Image alt="Start a Tutorial Runbook from a template" align="center" width="650px" src="https://files.readme.io/57b1e86-CleanShot_2024-06-21_at_17.09.26.png">
  Start a Tutorial Runbook from a template
</Image>

## Using Tutorial Runbooks

<Image alt="The first couple of messages in the tutorial incident's channel" align="center" width="650px" src="https://files.readme.io/701da90-CleanShot_2024-06-21_at_17.16.44.png">
  The first couple of messages in the tutorial incident's channel
</Image>

Tutorial Runbooks make use of FireHydrant's flexible steps and conditions to return differing prompts and buttons to users after they take actions. The template is written so that users can familiarize themselves with several different actions and concepts.

Upon execution of the Tutorial command, a user will receive a message indicating the tutorial has started, and shortly after, they should receive a notification that they've been automatically added to the tutorial incident's channel.

The rest of the experience will highly depend on whether or not an organization's admins and team members decide to make changes to the default tutorial Runbook. The world is your oyster!

## Next Steps

Users onboarding may be interested in the following docs:

* [Slack Responder Guide](https://docs.firehydrant.com/docs/slack-responder-guide)
* [MS Teams Responder Guide](https://docs.firehydrant.com/docs/ms-teams-responder-guide)
* [Declare and Respond](https://docs.firehydrant.com/docs/declare-and-respond)
* [Configuring Incidents](https://docs.firehydrant.com/docs/incident-settings)