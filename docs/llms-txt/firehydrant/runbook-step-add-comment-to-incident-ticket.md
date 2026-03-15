# Source: https://docs.firehydrant.com/docs/runbook-step-add-comment-to-incident-ticket.md

# Add Comment to Incident Ticket

This Runbook step will post content to the Jira incident ticket as a comment.

## Prerequisites

* Ensure you have configured [Jira Cloud](https://docs.firehydrant.com/docs/jira-cloud-integration) or [Jira Server (On-Premise)](https://docs.firehydrant.com/docs/jira-server-on-premise-integration) integration(s)
* This step will only work if the incident ticket has already been created (FireHydrant automatically sets this condition on the step)

## Configuration

The step content supports [Template Variables](https://docs.firehydrant.com/docs/template-variables). A common use case is propagating incident updates to Jira tickets, in which case you would need to configure the following:

* The comment can post the latest incident update note with `{{ incident.last_note.body }}`
* You'll need to configure the condition to re-run on every new note
  * **Incident Note is added** condition
  * Check **Rerun on every transition**

<Image alt="Example conditions for re-executing on every new update" align="center" width="650px" src="https://files.readme.io/f25bc3e-CleanShot_2024-08-09_at_15.28.14.png">
  Example conditions for re-executing on every new update
</Image>

Now, whenever responders on an incident post an incident note or update with `update` in the chat app or via the user interface, that note will also be propagated to Jira as a comment.