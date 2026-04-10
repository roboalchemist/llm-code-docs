# Source: https://docs.deepconverse.com/product-docs/ticket-automation/setup-zendesk-email-and-ticket-automation.md

# Setup Zendesk email and ticket automation

DeepConverse for Zendesk email and ticket automation allows you to build an AI and Automation layer to respond and handle tickets efficiently. The automation engine does the work of understanding the tickets and responding accordingly with macros, email templates and responses from knowledge articles.&#x20;

### Pre-requisties&#x20;

Before configuring Zendesk we need to ensure that there are some steps completed in the DeepConverse dashboard.

1. Establish **OAuth connection** with your Zendesk instance
2. Create **bot** and **workflows** (these are the actions you want the bot to handle)
3. Configure **connection** to use for the bot&#x20;

### Execution Flow

At a high level this is the flow that gets executed

1. Customer **creates a ticket** in Zendesk
2. When the ticket is created a Zendesk **trigger** will get fired and **notify** DeepConverse with the relevant ticket information.
3. DeepConverse will make **predictions** and choose the **workflow to execute**
4. Workflow will **update the ticket** and if needed **add a reply** in the ticket as a comment.

### Zendesk Setup and Configuration

#### Create a Webhook in Zendesk

You will need to add a webhook to inform DeepConverse of changes to tickets in Zendesk. The steps to do this in Zendesk are here -

[Creating webhooks to interact with third-party systems](https://support.zendesk.com/hc/en-us/articles/4408839108378-Creating-webhooks-to-interact-with-third-party-systems)

You can find the webhook url from the DeepConverse channels page.&#x20;

![Screenshot 2023-08-17 at 9.41.53 AM.png](https://help.deepconverse.com/hc/article_attachments/18372773802260) ![Screenshot 2023-08-17 at 9.42.20 AM.png](https://help.deepconverse.com/hc/article_attachments/18372773808916)

&#x20;

#### Create a trigger in Zendesk

For DeepConverse to handle tickets we will need to add a trigger which will inform DeepConverse when tickets are created.&#x20;

1. Navigate to **Zendesk Admin Center** > **Objects and Rules** > **Triggers**
2. Click **Add Trigger**
3. Fill out the trigger with the information below.

**Name**: DeepConverse Automation

**Conditions**

Meet ALL of the following conditions

* `Tags` contains none of `dc-automation-triggered`
* `Ticket` is `Updated`

Meet ANY of the following conditions

* `Channel` is `Email` (Add any other channels that you would like the trigger to run for)

Actions

* Notify active webhook: DeepConverse Automation\
  JSON Body:

  ```
  {
    "agent": {
      "name": "{{ticket.assignee.name}}",
      "email": "{{ticket.assignee.email}}"
    },
    "requester": {
      "name": "{{ticket.requester.name}}",
      "email": "{{ticket.requester.email}}"
    },
    "payload": {
      "id": "{{ticket.id}}",
      "source": "{{ticket.via}}",
      "title": "{{ticket.title}}",
      "description": "{{ticket.description}}",
      "status": "{{ticket.status}}",
      "message": "{{ticket.latest_comment}}",
      "tags": "{{ticket.tags}}",
      "updated_stamp": "{{ticket.updated_at_with_timestamp}}",
      "brand": "{{ticket.brand.name}}",
      ... custom fields
      "marketplace": "{{ticket.ticket_field_8792255150861}}"
    }
  }
  ```
* Add tags: `dc-automation-triggered`

Once the trigger has been Saved go back to the triggers screen.&#x20;

#### Ordering of Triggers

To ensure that DeepConverse gets all the information needed for executing the Automation we will need to have the DeepConverse Automation trigger placed after some of the business rule triggers have been applied.&#x20;

Follow the instructions here to reorder the trigger: [Reordering and sorting triggers](https://support.zendesk.com/hc/en-us/articles/4408894209562-Reordering-and-sorting-triggers)

&#x20;

### Tags that are used by DeepConverse

| **Tag**                      | **Description**                                                         |
| ---------------------------- | ----------------------------------------------------------------------- |
| dc-automation-triggered      | Marks that the ticket went through the DeepConverse automation webhook. |
| dc-auto-reply                | Marks that the ticket has an auto reply comment to the customer.        |
| dc-automation-ticket-updated | Marks that certain fields in the ticket were updated by the automation  |
| dc-email-positive-feedback   | Marks positive feedback given by the customer to the auto reply email   |
| dc-email-negative-feedback   | Marks negative feedback given by the customer to the auto reply email   |

<br>
