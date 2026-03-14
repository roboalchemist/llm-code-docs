# Source: https://docs.enate.net/enate-help/integrations/enate-integrations/webhooks/webhook-troubleshooting.md

# Webhook Troubleshooting

**Q: In the event of the external system being down, or a failure response, does the Enate system retry?**\
A: YES. The Enate system will retry failed messages 3 times.

**Q: Is there a possibility of duplicate events?**\
A: YES. Duplicate events can occur, for instance multiple updates to a work item occurring in quick succession, or when an email is received (which triggers a 'new email received' webhook and may very likely then trigger the packet update API too, if incoming email will change the work item's current state.

**Q: Is there a standard response structure for Enate Webhooks?**\
A: NO. Response structures can be different between Webhooks. Please see the list of [Enate's Webhooks](https://docs.enate.net/enate-help/integrations/enate-integrations/webhooks/enates-webhooks) for the specifics of each response structure.

**Q: If I've unsubscribed from a Webhook, what is the procedure for re-subscribing. Is there some kind of 'reactivation' approach?**\
A: NO, this is a simple case of adding a subscription again, as you did when first subscribing to it.

**Q: Is it mandatory to supply an Entity for a Webhook?** \
A: No. This is dependent upon the Webhook. In some situations it is mandatory, in some optional, and in others there isn't such a filter option.

**Q: Can the same subscriber URL be used in multiple subscriptions?** \
A: Yes, it is possible for the same subscriber URL to be used in multiple subscriptions. However, it may be preferable to create different URLs for each subscription to prevent bottlenecks and to create more logical routes for messages into downstream systems.

**Q: How can I identify whether the Webhook update is for a Case or Ticket or Action?**\
A: The ProcessType field will indicate the type of packet i.e. 1= Case, 2=Ticket, 3=Action but a more informative approach would be to add some identifying information to the custom header when creating the webhook subscription, this header information will then be included with every message sent out i.e.:

* "CustomHeader": " Update-ticket-200243-T-subscription"
* "CustomHeaderValue": "Ticket 200243-T has been updated "

**Q: Can Webhook Subscriptions be seen by other users?**\
A: Webhook Subscriptions are per user and the permissions of that user are applied to the messages that are sent so, depending on permission configurations, not all users will be able to see all Webhook Subscriptions.

**Q:  In which scenarios will a New Communication event be triggered for a packet ?**\
A: A New Communication event is triggered whenever a new Packet Communication is written to the database. A Packet Communication may be:&#x20;

* A note written by Agent
* A note written in Self Service
* An email coming in
* An email going out
* An existing email being “duplicated” onto another Work Item (for instance a Ticket merge into a Ticket/Case/Action causes a “new” email in the target work item)
