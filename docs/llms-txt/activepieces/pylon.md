# Source: https://www.activepieces.com/docs/handbook/customer-support/pylon.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.activepieces.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to use Pylon

> Guide for using Pylon to manage customer support tickets

At Activepieces, we use Pylon to manage Slack-based customer support requests through a Kanban board.

Learn more about Pylon's features: [https://docs.usepylon.com/pylon-docs](https://docs.usepylon.com/pylon-docs)

<img src="https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/pylon-board.png?fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=4c286a0ac7893dd6c11f1cf931dd8a42" alt="Pylon board showing different columns for ticket management" data-og-width="1693" width="1693" data-og-height="1022" height="1022" data-path="resources/pylon-board.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/pylon-board.png?w=280&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=aed1a4c386c560b84316c67c862dd9b4 280w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/pylon-board.png?w=560&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=c15468d855923650fdd7b0b7acc8b558 560w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/pylon-board.png?w=840&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=72d41d0109b83197b9387af825220d25 840w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/pylon-board.png?w=1100&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=d972699d3d6b29f881b8688498f14903 1100w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/pylon-board.png?w=1650&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=dbb1483923d46d27d2c0e5f248cb939c 1650w, https://mintcdn.com/activepieces/ki8mFooo8mAmhMdP/resources/pylon-board.png?w=2500&fit=max&auto=format&n=ki8mFooo8mAmhMdP&q=85&s=6ba2e0d7c7f40f94bac7ac5ab050ed2e 2500w" />

### New Column

Contains new support requests that haven't been reviewed yet

* Action Items:
  * Respond fast even if you don't have an answer, the important thing here is to reply that you will take a look into it, the key to winning the customer's heart.

### On You Column

Contains active tickets that require your attention and response. These tickets need immediate review and action.

* Action items:
  * Set ticket fields (status and priority) according to the guide below
  * Check the [handle request page](./handle-requests) on how to handle tickets

<Tip>
  The goal as a support engineer is to keep the "New" and "On You" columns empty.
</Tip>

### On Hold

Contains only tickets that have a linked Linear issue.

* Place tickets here after:
  * You have identified the customer's issue
  * You have created a Linear issue (if one doesn't exist - avoid duplicates!)
  * You have linked the issue in Pylon
  * You have assigned it to a team member (for urgent cases only)

<Warning>
  Please do not place tickets on hold without a ticket.
</Warning>

<Note>
  Tickets will automatically move back to the "On You" column when the linked GitHub issue is closed.
</Note>

### Closed Column

This means you did awesome job and the ticket reached it's Final destination for resolved tickets and no further attention required.
