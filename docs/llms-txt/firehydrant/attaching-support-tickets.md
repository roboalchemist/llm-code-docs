# Source: https://docs.firehydrant.com/docs/attaching-support-tickets.md

# Attaching Support Tickets

Support tickets are one of the key indicators of how an incident might impact customers. FireHydrant currently offers a [Zendesk](https://docs.firehydrant.com/docs/zendesk-integration) integration (with more planned) to help streamline incident communications with customers, specifically:

* Associating support tickets to an active incident from within FireHydrant
* Creating a new FireHydrant incident or associating a support ticket with an existing FireHydrant incident via the [FireHydrant Zendesk Marketplace app](https://www.zendesk.com/marketplace/apps/support/854375/firehydrant/)
* Automating incident status updates back to linked Zendesk tickets as internal notes

## Prerequisites

* You'll need to install the [Zendesk](https://docs.firehydrant.com/docs/zendesk-integration) integration
* You must be one of <Glossary>Collaborator</Glossary>, <Glossary>Member</Glossary>, or <Glossary>Owner</Glossary> roles to interact with an incident and modify its details
* If performing actions from Zendesk, you must have a Zendesk account and have access to support tickets

## Creating an Incident with a Zendesk Ticket Attached

You can declare an incident in FireHydrant and include the link to your Zendesk ticket in either the **Description** or the **Customer Impact Summary** fields.

If FireHydrant detects Zendesk ticket link(s) in either of those fields (and your Zendesk integration is configured), it will also automatically associate the ticket(s) with the incident.

<Image alt="Inserting the ZD link into either **Description** or **Customer Impact** fields" align="center" width="400px" src="https://files.readme.io/107d0c1-Screenshot_2024-01-22_at_7.45.10_PM.png">
  Inserting the ZD link into either **Description** or **Customer Impact** fields
</Image>

<Image alt="FireHydrant auto-attaches that ticket to the incident" align="center" width="650px" src="https://files.readme.io/10cc66e-Screenshot_2024-01-22_at_7.49.39_PM.png">
  FireHydrant auto-attaches that ticket to the incident
</Image>

## Linking Zendesk Tickets to an Incident from within FireHydrant

<Image alt="Customer Support Issues section" align="center" width="650px" src="https://files.readme.io/8ef6c11-Screenshot_2024-01-08_at_6.25.51_PM.png">
  Customer Support Issues section
</Image>

1. In the **Details** panel on an existing incident, click the edit pencil next to **Customer Support Issues**.
2. This will open a modal where you'll see a list of all the Zendesk tickets in reverse chronological order.
3. Select any support ticket(s) you want to attach to the incident, then click **Link issues**.

<Image alt="Issue linking selection modal" align="center" width="650px" src="https://files.readme.io/a85f29c-image.png">
  Issue linking selection modal
</Image>

4. Once linked, the tickets will be linked to this particular FireHydrant incident, and information about the impacted customer(s) for the ticket(s), along with a link to the original ticket, will be present on the incident.

<Image alt="Ticket link and customer name after linking support issues" align="center" width="400px" src="https://files.readme.io/70c990d-image.png">
  Ticket link and customer name after linking support issues
</Image>

## Creating a FireHydrant incident from within Zendesk

1. While looking at a support ticket, find the FireHydrant app and click on the **New Incident** tab. At a minimum, you must complete any required fields which are [configurable by your organization's Owner(s)](https://docs.firehydrant.com/docs/incident-fields).
2. Click **Declare Incident**.

<Image alt="Screen_Shot_2022-09-05_at_12.13.32_PM.png" align="center" width="400px" src="https://support.firehydrant.com/hc/article_attachments/9101374866708/Screen_Shot_2022-09-05_at_12.13.32_PM.png">
  Example of declaring an incident from Zendesk app
</Image>

## Linking a ticket to existing FireHydrant incidents within Zendesk

1. From the **Existing Incidents** tab of the FireHydrant app in Zendesk, you can search for and attach your Zendesk ticket to existing FireHydrant incidents instead of opening a new one.
2. Expanding the incident row will display additional incident summary information, and you can click "+ Attach Ticket to Incident" to attach the current ticket.

<Image alt="Screen_Shot_2022-09-05_at_12.16.56_PM.png" align="center" width="400px" src="https://support.firehydrant.com/hc/article_attachments/9101427200148/Screen_Shot_2022-09-05_at_12.16.56_PM.png">
  Attaching a ticket to an existing incident
</Image>

## Viewing FireHydrant incidents linked to a Zendesk ticket & unlinking

Any linked incidents will appear on the **Relevant Incidents** tab. From here, you also have the option to unlink the ticket from said incident(s).

<Image alt="Screen_Shot_2022-09-05_at_12.18.43_PM.png" align="center" width="400px" src="https://support.firehydrant.com/hc/article_attachments/9101468532372/Screen_Shot_2022-09-05_at_12.18.43_PM.png">
  Showing linked incidents and a button to unlink
</Image>

## Posting status updates to linked Zendesk tickets

1. When you [post any incident updates](https://docs.firehydrant.com/docs/posting-updates) on FireHydrant, the update will also be published as an internal note to any linked Zendesk tickets, along with a link back to the FireHydrant incident. 

<Image alt="Screen_Shot_2022-07-27_at_2.12.34_PM.png" align="center" width="650px" src="https://support.firehydrant.com/hc/article_attachments/8122899974036/Screen_Shot_2022-07-27_at_2.12.34_PM.png">
  Example incident update posted as an internal note on a linked Zendesk ticket
</Image>

These updates are helpful for your Support/Success personnel to understand what the latest updates are on an incident and to craft external update notes to customer(s) accordingly.

## Next Steps

* If you haven't read the docs yet, learn more about [Posting Updates](https://docs.firehydrant.com/docs/posting-updates)
* Browse the rest of [FireHydrant's integrations](https://docs.firehydrant.com/docs/integrations-overview) to see how you can optimize your incident management processes