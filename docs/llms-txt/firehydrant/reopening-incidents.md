# Source: https://docs.firehydrant.com/docs/reopening-incidents.md

# Reopening Incidents

Occasionally, you may need to reopen an incident.

As a best practice, FireHydrant recommends not resolving an incident until you're sure of any residual impact the mitigation may have. We typically recommend moving the Milestone to **Mitigated** and observing the situation for a while before officially resolving.

But in situations where you must reopen the incident, FireHydrant provides this capability.

## Reopening an incident via Slack

When you reopen an incident, it reverts back to the most recent milestone that was reached before it was resolved.

> 🚧 Note:
>
> Reopening an incident doesn't re-trigger any automations. You will need to attach new Runbooks.

You can reopen an incident from Slack by running `/fh reopen`, which aliases to `/fh update` with the Milestone automatically set back to the last Milestone it was in before the incident was resolved. In most cases, this will be **Mitigated**.

<Image alt="Running `/fh reopen` or `/fh update` and modifying the Milestone to something other than **Resolved** will reopen the incident." align="center" width="400px" src="https://files.readme.io/2a062a0-image.png">
  Running `/fh reopen` or `/fh update` and modifying the Milestone to something other than **Resolved** will reopen the incident.
</Image>

> 📘 Note:
>
> This must be executed from within the incident channel belonging to the incident. If the channel has been archived, you will need to unarchive it to do this.

## via Command Center

<Image alt="Reopening an incident from Command Center" align="center" src="https://files.readme.io/6e0574a-Screenshot_2023-12-07_at_5.48.58_PM.png">
  Reopening an incident from Command Center
</Image>

1. Navigate to **Incidents** in the top navigation and go to the incident you want to reopen.
2. On the right side, click the ellipses and click on "Reopen incident"
3. This opens a confirmation modal. Click "Confirm" to reopen the incident.

Alternatively, clicking the dropdown selector for Milestones and selecting a milestone prior to **Resolved** will also achieve the same thing.

## Next Steps

* Learn about [creating historical, resolved incidents](https://docs.firehydrant.com/docs/retroactive-incidents)
* Look at [Conducting Retrospectives](https://docs.firehydrant.com/docs/conducting-retrospectives) and see how FireHydrant keeps your responders focused when reviewing incidents