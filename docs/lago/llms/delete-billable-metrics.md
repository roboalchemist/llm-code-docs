# Source: https://getlago.com/docs/guide/billable-metrics/delete-billable-metrics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete billable metrics

You may delete a billable metric linked to [charges](/guide/plans/charges) associated
with existing [subscriptions](/guide/subscriptions/assign-plan).

If you do so:

* The events associated with this billable metric, which are assigned to the
  current billing period or linked to `draft` invoices, will be immediately
  deleted;
* The charges associated with this billable metric will be immediately removed
  from all plans and existing subscriptions;
* The charges associated with this billable metric will no longer be included in
  the [current usage](/api-reference/customer-usage/customer-usage-object) of the customers
  concerned; and
* The charges associated with this billable metric will be immediately removed
  from all `draft` invoices linked to these subscriptions.

However, the charges associated with this billable metric will still be included
in all `finalized` invoices linked to these subscriptions.

<Info>
  After deleting a billable metric, you can create a new one using the same
  code. However, past events will not be linked to this new billable metric.
</Info>

<Tabs>
  <Tab title="Dashboard">
        <img src="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/billable-metrics-delete-68cd9763df888a65237c8f0f5c85358a.png?fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=97e5a6846e326e36d253d56e358f224f" alt="How to delete a billable metric" data-og-width="2880" width="2880" data-og-height="1562" height="1562" data-path="guide/images/billable-metrics-delete-68cd9763df888a65237c8f0f5c85358a.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/billable-metrics-delete-68cd9763df888a65237c8f0f5c85358a.png?w=280&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=3077a9023437c49b0cb532915bc9c615 280w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/billable-metrics-delete-68cd9763df888a65237c8f0f5c85358a.png?w=560&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=0be4549b1b0605f944549bc91a3f4a24 560w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/billable-metrics-delete-68cd9763df888a65237c8f0f5c85358a.png?w=840&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=078fc4953ee301b53cc0d10ca2bcc091 840w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/billable-metrics-delete-68cd9763df888a65237c8f0f5c85358a.png?w=1100&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=e95d4d27e92f3b57b04083d00db779ec 1100w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/billable-metrics-delete-68cd9763df888a65237c8f0f5c85358a.png?w=1650&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=b3beaa52e3d53f77a66cc3090bbbb6c2 1650w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/billable-metrics-delete-68cd9763df888a65237c8f0f5c85358a.png?w=2500&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=026d805ad609ecf4892d22132180bbed 2500w" />
  </Tab>

  <Tab title="API">
    <CodeGroup>
      ```bash Delete "Storage" metric theme={"dark"}
      LAGO_URL="https://api.getlago.com"
      API_KEY="__YOUR_API_KEY__"

      curl --location --request DELETE "$LAGO_URL/api/v1/billable_metrics/storage" \
        --header "Authorization: Bearer $API_KEY"
      ```
    </CodeGroup>
  </Tab>
</Tabs>
