# Source: https://getlago.com/docs/guide/events/events-list.md

# Events list

> By ingesting events, you can see them flowing in the Lago application by using the events list. It allows you to take a deeper look at ingested events and detect possible warnings.

## Accessing the events list[](#accessing-the-events-list "Direct link to heading")

You can access the events list from the UI by following this path:

1. Go to the **Developers** section in the sidebar;
2. Click the **events** tab;
3. See a list of ingested events; and
4. Reload this list when you ingest new events.

By default, the UI shows you a list of the latest 20 events, but you can load
much more by scrolling down the page.

<Tip>If an event is not shown in the UI, it has **not** been ingested.</Tip>

<Frame caption="Accessing the events list">
  <img src="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/events/images/events-debugger-6bcbcf7e46f1bd4bb8a9b6e6964bba69.png?fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=b8ce3364517f3abca106e86515e098db" data-og-width="2402" width="2402" data-og-height="1296" height="1296" data-path="guide/events/images/events-debugger-6bcbcf7e46f1bd4bb8a9b6e6964bba69.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/events/images/events-debugger-6bcbcf7e46f1bd4bb8a9b6e6964bba69.png?w=280&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=2f9a5c28c78aa24302eb854dd6749926 280w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/events/images/events-debugger-6bcbcf7e46f1bd4bb8a9b6e6964bba69.png?w=560&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=6199c096230abde12d6eac4fa85141ff 560w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/events/images/events-debugger-6bcbcf7e46f1bd4bb8a9b6e6964bba69.png?w=840&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=ae5728665c3fa95e1f95bea259c2a6d3 840w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/events/images/events-debugger-6bcbcf7e46f1bd4bb8a9b6e6964bba69.png?w=1100&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=8ab83c47bb9f3032cdbf717a1b71382a 1100w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/events/images/events-debugger-6bcbcf7e46f1bd4bb8a9b6e6964bba69.png?w=1650&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=4b40bd99f0e2b563d5af9ec16c2556e4 1650w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/events/images/events-debugger-6bcbcf7e46f1bd4bb8a9b6e6964bba69.png?w=2500&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=78c2ab559626c4ad669ae1b9d1adc793 2500w" />
</Frame>

## Accessing a specific event[](#accessing-a-specific-event "Direct link to heading")

In the events list view, by clicking on a specific event, you will have access to 2 main
blocks:

1. **A list of useful properties returned**
   * **Time:** timestamp of the received events;
   * **Customer ID:** the ID of your customer;
   * **Billable metric code:** code of the billable metric linked to the event;
   * **Billable metric name:** name of the billable metric linked to the event;
   * **Transaction ID:** unique `transaction_id` of the event used as
     idempotency key;
   * **IP Address:** IP address of the event sender; and
   * **Client API:** Lago Client API used to send the event.
2. **A JSON with event's arguments sent in the payload**

## Possible warnings[](#possible-warnings "Direct link to heading")

Some events can be ingested but triggering a bad or unexpected behavior. This is
why Lago displays in the UI two possible warnings:

1. The event `code` is **not related to an existing billable metric**; and
2. The billable metric's **property used for the aggregation is not sent**
   through this event.
