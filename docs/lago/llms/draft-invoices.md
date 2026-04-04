# Source: https://getlago.com/docs/guide/invoicing/draft-invoices.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Draft invoices

> A draft invoice is an editable invoice by several ways.

While an invoice is in draft status, you can:

* **Add usage records** by sending event with a valid timestamp within the billing period
* **Edit specific fees** (adjusting total amount or unit count)
* **Apply coupons** to the customer’s account
* **Add credits** to the customer’s wallet or credit note wallet

### Add fees to draft invoice

Since Lago does not generate fees for charges with 0 units, some may not appear in the draft invoice by default.
You can add them either by [sending usage records](../invoicing/draft-invoices#add-usage-records) or manually through the Dashboard:

1. Open the draft invoice details;
2. Click Add a fee (if applicable);
3. Select the charge and filters;
4. Adjust the display name (optional);
5. Choose between `Total amount` or `Total unit`;
6. Input your values — note that `Total amount` overwrites the original fee;
7. If using `Total unit`, Lago recalculates the fee automatically.

Manual fee editing is only available via the Dashboard.

### Edit a specific fee

If a fee has already been added to the draft invoice, you can edit it from the Dashboard:

1. Open the draft invoice details;
2. Click the `three-dot` icon next to the fee;
3. Adjust the display name (optional);
4. Choose `Total amount` or `Total unit`;
5. Input new values — same recalculation logic applies as above.

Manual fee editing is only available via the Dashboard.

### Add usage records

In order to add usage to an invoice that is in `draft` status, the `timestamp`
of the [events](/guide/events/ingesting-usage) must be
within the billing period. Consider the following example:

> Billing period: January 1 – January 31
> Grace period: 3 days
> Today: February 2
>
> A draft invoice was generated on February 1.
>
> To send additional usage for this invoice, the event timestamps must fall between January 1st and 31st.
>
> ✅ Usage event on January 11 (timestamp: `1673457300`) → included
> ❌ Usage event on February 2 (timestamp: `1675354500`) → excluded (will be part of next invoice)

After sending new events, refresh the relevant draft invoice to see the events taken into account.

When the grace period ends, invoices in draft status are automatically finalized.
Alternatively, you can **finalize them manually** via the UI or API.

Once `finalized`, invoices are locked and trigger the `invoice.created` webhook.

<Frame caption="Draft invoice in the Lago app">
  <img src="https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/grace-period-draft-invoice-0a9ccbd1d7dc1b87faeb5a44abf484e1.png?fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=c4ff1d6ecde4bf1acb615663920052a9" data-og-width="2880" width="2880" data-og-height="1570" height="1570" data-path="guide/invoicing/images/grace-period-draft-invoice-0a9ccbd1d7dc1b87faeb5a44abf484e1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/grace-period-draft-invoice-0a9ccbd1d7dc1b87faeb5a44abf484e1.png?w=280&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=0360101661ac307410007c9f1f165401 280w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/grace-period-draft-invoice-0a9ccbd1d7dc1b87faeb5a44abf484e1.png?w=560&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=54e0dcf003b5bcc55adbbbd51b6db02a 560w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/grace-period-draft-invoice-0a9ccbd1d7dc1b87faeb5a44abf484e1.png?w=840&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=d986c3cfbd8a34e16e2038b58f62eca2 840w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/grace-period-draft-invoice-0a9ccbd1d7dc1b87faeb5a44abf484e1.png?w=1100&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=9a6b3975bf8427766d901557b15851f9 1100w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/grace-period-draft-invoice-0a9ccbd1d7dc1b87faeb5a44abf484e1.png?w=1650&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=f39645e0f5b5ba18bd8e888616b0cbfa 1650w, https://mintcdn.com/lago-docs/x0ux42rCkjpwz1jk/guide/invoicing/images/grace-period-draft-invoice-0a9ccbd1d7dc1b87faeb5a44abf484e1.png?w=2500&fit=max&auto=format&n=x0ux42rCkjpwz1jk&q=85&s=8ce5b862c47ba74194ea7fbf61599086 2500w" />
</Frame>

<Info>
  Coupons and credits added during the grace period won’t appear on `draft` invoices, but they **will be automatically applied** to the next `finalized` invoice.
</Info>
