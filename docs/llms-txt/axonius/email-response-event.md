# Source: https://docs.axonius.com/docs/email-response-event.md

# Email Message Response

 

Axonius supports **Email Message Response** as an event in a Workflow, allowing you to trigger or advance a Workflow based on a user's interaction with an interactive email sent by Axonius.

This event is triggered **only** if it follows an interactive <Anchor label="**Axonius - Send Email** " target="_blank" href="https://docs.axonius.com/docs/send-email#/">**Axonius - Send Email** </Anchor> Enforcement Action. An email is considered interactive if it is configured with a list of predefined Responses (in the **Create list of predefined responses** field) that a recipient can click.

When a response is received via a button click in the email:

* The Workflow begins (if a triggering Event).
* The Workflow continues running (if a non-triggering Event).

You can add a **Condition** immediately following this Event to dictate the Workflow's path based on the specific response the user clicked.

## Adding the Email Message Response Event to a Workflow

### Using as the Workflow Trigger

This configuration causes the Workflow to run immediately upon receiving a user's email response.

**To select the Email Message Response event as the Workflow trigger**

1. In the **Trigger Type** pane, under **Message Response**, click the **Email Message Response** tile.

2. In the dropdown, select the type of asset to be retrieved. Subsequent workflow nodes will run on the selected asset type associated with the user who responded.

The Workflow is triggered each time a user submits a response to the interactive email.

### Using as a Non-Triggering Event

This configuration allows an existing running Workflow to pause until a response is received,.

**To select Email Message Response as a non-triggering event**

1. In the **Event** pane, under **Message Response**, click the **Email Message Response** tile.

<Callout icon="📘" theme="info">
  Note

  This non-triggering event must be immediately preceded by the interactive **Axonius - Send Email message** Enforcement Action within the same Workflow path.
</Callout>

When a response is received for the interactive email sent by a previous Workflow node, the event occurs, and the Workflow continues running from that point.

<br />