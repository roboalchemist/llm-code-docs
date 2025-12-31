# Source: https://www.activepieces.com/docs/handbook/customer-support/pylon.md

# How to use Pylon

> Guide for using Pylon to manage customer support tickets

At Activepieces, we use Pylon to manage Slack-based customer support requests through a Kanban board.

Learn more about Pylon's features: [https://docs.usepylon.com/pylon-docs](https://docs.usepylon.com/pylon-docs)

<img src="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/pylon-board.png?fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=5e653ec9a78ead22b3edc7f3cbac1a31" alt="Pylon board showing different columns for ticket management" data-og-width="1693" width="1693" data-og-height="1022" height="1022" data-path="resources/pylon-board.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/pylon-board.png?w=280&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=5afae234a251cddb52fbc2e98fd6f9df 280w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/pylon-board.png?w=560&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=edc15a6de060b8d731356098bf781b8b 560w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/pylon-board.png?w=840&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=ab9422f6444c07fe2739dd07f2b2059d 840w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/pylon-board.png?w=1100&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=990ffc64f2da10c0c8bdb6659826ddbb 1100w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/pylon-board.png?w=1650&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=096a95126fe07af16cb9735913d688ab 1650w, https://mintcdn.com/activepieces/j3GVg3kKyC3IS6YV/resources/pylon-board.png?w=2500&fit=max&auto=format&n=j3GVg3kKyC3IS6YV&q=85&s=8e737a78dc7abb9402b62abd98e1265f 2500w" />

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
