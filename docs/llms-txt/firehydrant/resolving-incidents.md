# Source: https://docs.firehydrant.com/docs/resolving-incidents.md

# Resolving Incidents

Once you've fully fixed issues and feel comfortable closing out the incident, it's time to **Resolve** the incident.

## From Slack

In Slack, you can run the `/fh resolve` command. This aliases to the `/fh update` modal, but it sets the Milestone to Resolved for you. Alternatively, you can run `/fh update` and change the Milestone to **Resolved** yourself and click "Update."

<Image alt="`/fh resolve` aliases to `/fh update` but sets the Milestone to **Resolved** for you" align="center" width="400px" src="https://files.readme.io/fe5f1dc-image.png">
  `/fh resolve` aliases to `/fh update` but sets the Milestone to **Resolved** for you
</Image>

## From Command Center

<Image alt="Resolve button location in the Command Center" align="center" src="https://files.readme.io/26a4091-Screenshot_2023-12-07_at_4.56.26_PM.png">
  Resolve button and milestone dropdown in the Command Center
</Image>

In the Command Center, you can click the "Resolve incident" button as well as transition the Milestone to **Resolved** by clicking on the dropdown. Both will close out the incident and log the appropriate timeline events.

## Conditions and Runbooks

Resolving the incident will halt most Runbook steps. The exception to this is if any of your steps have been configured for Resolution and post-resolution conditions (e.g., *When Incident Milestone is Retrospective Completed*, for example).

So, for example, if you have a Runbook step that automatically runs every 30 minutes to remind your Incident channel to post updates, that step will automatically cease repeating when you resolve the incident. If you don't want this, then ensure you have explicit conditions in there, such as "If current milestone is one of... t all of them, including *Retrospective Started* and *Retrospective Completed*]".

".

See [Incident Milestones](https://docs.firehydrant.com/docs/incident-milestones) and [Runbooks Basics](https://docs.firehydrant.com/docs/runbooks-basics) for more information.

## Post-Resolution Status Updates

Status update notes and messages now continue to be posted to Slack, Microsoft Teams, and Status Pages **even after an incident is resolved**. This allows teams to receive ongoing updates throughout the entire incident lifecycle, including post-resolution communications.

This is particularly useful for:

* Notifying stakeholders about final resolution details
* Sharing retrospective findings or follow-up actions
* Providing closure updates to customers via status pages
* Maintaining complete communication transparency from start to finish

To post updates after resolution, use the same update commands (`/fh update` in Slack) or the Command Center interface as you would during an active incident.

## Next Steps

* Look at [Conducting Retrospectives](https://docs.firehydrant.com/docs/conducting-retrospectives) and see how FireHydrant keeps your responders focused when reviewing incidents
* Read more about [Runbooks Basics](https://docs.firehydrant.com/docs/runbooks-basics) and how automation and conditions work in FireHydrant
* Learn about [Archiving Incidents](https://docs.firehydrant.com/docs/archiving-incidents), [Reopening Incidents](https://docs.firehydrant.com/docs/reopening-incidents), or retroactively logging [past incidents](https://docs.firehydrant.com/docs/retroactive-incidents)