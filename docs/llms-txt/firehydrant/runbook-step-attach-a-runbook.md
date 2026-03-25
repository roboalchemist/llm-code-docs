# Source: https://docs.firehydrant.com/docs/runbook-step-attach-a-runbook.md

# Attach a Runbook

<Image alt="Attach a Runbook step" align="center" src="https://files.readme.io/6aff063-image.png">
  Attach a Runbook step
</Image>

This Runbook step attaches another Runbook to the current incident.

Most use cases can be handled by configuring [Runbook Conditions](https://docs.firehydrant.com/docs/runbook-conditions) at the Runbook level. But sometimes, for organization and clarity, you may limit which Runbooks auto-attach to incidents and configure these to attach other Runbooks explicitly.

## Use Case Comparison

### Setting Runbook-Level Conditions

Let's say you have a generic Runbook that applies to all `SEV1` incidents. However, have a 2nd Runbook that you only want to attach if it's `SEV1` **and** impacted components include `User Portal`.

**This can be set explicitly on the 2nd Runbook, like so:**

<Image alt="Example of tighter conditions on Runbooks" align="center" width="450px" src="https://files.readme.io/40cd855-image.png">
  Example of tighter conditions on Runbooks
</Image>

However, the caveat is that the generic`SEV1` Runbook has no reference to this secondary Runbook, and vice-versa. So users need to know to check both Runbooks for all the steps.

### Attaching a Runbook in a step

Alternatively, you can limit which Runbooks auto-attach at the top level.

As an example, let's say only these three Runbooks will attach to incidents if the Severity matches, and all other Runbooks are set to `when invoked manually`.

<Image alt="Auto-attaching, severity-based Runbooks" align="center" src="https://files.readme.io/9289343-image.png">
  Auto-attaching, severity-based Runbooks
</Image>

From there, we can set an explicit step inside the `SEV1` Runbook to attach the `User Portal` Runbook if that component is involved:

<Image alt="Runbook step to attach User Portal" align="center" src="https://files.readme.io/477a33e-image.png">
  Runbook step to attach User Portal
</Image>

* The net outcome is the same, but there's an explicit step within the `SEV1` Runbook, so it's easier for users to follow the chain of command. This is especially useful if, e.g., a broad adjustment needs to be made to your entire `SEV1` process. You'll enter just a single top-level`SEV1` Runbook, and from there, users will see which downstream Runbooks are called by this one and may also need adjustment.
* We know that the `User Portal` Runbook will never be accidentally attached to any incident unless one of the top-level Runbooks explicitly calls it.

It's a different way to organize and automate Runbook attachments while yielding the same outcome.