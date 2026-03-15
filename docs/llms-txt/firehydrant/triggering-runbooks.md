# Source: https://docs.firehydrant.com/docs/triggering-runbooks.md

# Triggering Runbooks

Runbooks are the core automation engine underneath the hood of FireHydrant. Unlike normal Runbooks, which list instructions for responders, FireHydrant's Runbooks bring true automation to your incident response by executing actions on your behalf.

Any time an incident is declared, Runbooks evaluate their conditions to decide whether or not they should trigger. Once they do, the steps within the Runbook also assess their conditional rules and execute accordingly.

To learn more, visit the documentation on [Runbooks](https://docs.firehydrant.com/docs/runbook-basics) and [Runbook Conditions](https://docs.firehydrant.com/docs/runbook-conditions). The rest of this documentation page describes how to trigger Runbooks in an incident **manually**.

## Triggering via Slack

<Image alt="The modal for Runbooks with `/fh runbooks`" align="center" width="400px" src="https://files.readme.io/a303270-image.png">
  The modal for Runbooks with `/fh runbooks`
</Image>

From Slack, inside an incident channel, you can browse the list of triggered Runbooks for this by executing `/fh`. This will show you not only all triggered Runbooks, but also the status of each step within the Runbook.

At the bottom, you can then select additional Runbooks to trigger. You can also execute an explicit command to do this, `/fh add runbook`.

<Image alt="Adding a new Runbook via the previous modal or via `/fh add runbook`" align="center" width="400px" src="https://files.readme.io/fc00bef-image.png">
  Adding a new Runbook via the previous modal or via `/fh add runbook`
</Image>

Once you've triggered a Runbook, it will also show up on the list of Runbooks shown at `/fh runbooks`.

## Triggering via UI

In the incident's Command Center, you can navigate to the **Runbooks** tab to see the list of Runbooks that have been triggered by this incident. Like Slack above, you can also browse the statuses of individual steps within each Runbook by drilling down into the Runbooks.

To trigger a new one, you can click "+ Attach a runbook" and then search for the one you'd like to trigger.

<Image alt="Attaching a Runbook via Command Center" align="center" width="650px" src="https://files.readme.io/c018f7e-Screenshot_2024-01-25_at_5.12.22_PM.png">
  Attaching a Runbook via Command Center
</Image>

## Next Steps

* Learn more about [Runbooks](https://docs.firehydrant.com/docs/runbook-basics) and [Runbook Conditions](https://docs.firehydrant.com/docs/runbook-conditions) to understand how they work
* Then check out [Runbook Testing](https://docs.firehydrant.com/docs/runbook-testing) and [Runbook Best Practices](https://docs.firehydrant.com/docs/runbook-best-practices) to hone in on configuring Runbooks in a way that works best for your team
* Browse the [available Runbook steps](https://docs.firehydrant.com/docs/runbook-steps)