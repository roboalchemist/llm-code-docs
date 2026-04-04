# Source: https://getlago.com/docs/guide/revenue-share.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Revenue share

> Model your revenue-sharing structure within Lago.

<Info>
  **PREMIUM ADD-ON** ✨

  This revenue-share feature is available upon request only. Please **[contact us](mailto:hello@getlago.com)** to get access to this premium feature.
</Info>

If you’re selling your product or service through a partner, model this revenue-share in Lago.
Mark your customer as a partner, and Lago will generate all invoices as self-billed invoices.

Self-billing is a billing arrangement where the customer creates and issues the invoice on behalf of the supplier for goods or services received.
That said, **please own and ensure** an agreement is in place with your partner to allow Lago to issue these invoices on their behalf.

## Create a partner

To generate self-billed invoices, create your first partner by following these steps:

<Tabs>
  <Tab title="Dashboard">
    1. Go to the **Customers** navigation tab.
    2. Click on **Create a Customer**.
    3. Enable the **Partner** option by toggling it on.
    4. Fill in the customer’s billing information—this will be used to generate invoices.

    <Frame caption="Mart a customer as partner in creation form">
      <img src="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-partner.png?fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=dc8110822436a4b6cfd7affa40d4b9c1" data-og-width="3456" width="3456" data-og-height="2159" height="2159" data-path="guide/images/customer-partner.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-partner.png?w=280&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=3c7ce41b6a160a696cf68cb3ab9394eb 280w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-partner.png?w=560&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=88f28fff0aa4a4b47a686a6fdbe8215e 560w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-partner.png?w=840&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=3bc22828d6f09dcc05fb8a25229e3bb7 840w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-partner.png?w=1100&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=f678a35a2f89584d39c56b2b32cbbe33 1100w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-partner.png?w=1650&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=a14f25198a694cc305664e3a1b0a4488 1650w, https://mintcdn.com/lago-docs/L57i4PY_iDpAEuWL/guide/images/customer-partner.png?w=2500&fit=max&auto=format&n=L57i4PY_iDpAEuWL&q=85&s=768d80ad37d111399e1d9627990012ef 2500w" />
    </Frame>
  </Tab>

  <Tab title="API">
    ```bash Create a customer theme={"dark"}
    LAGO_URL="https://api.getlago.com"
    API_KEY="__YOUR_API_KEY__"

      curl --location --request POST "$LAGO_URL/api/v1/customers" \
      --header "Authorization: Bearer $API_KEY" \
      --header 'Content-Type: application/json' \
      --data-raw '{
        "customer": {
          …
          "account_type: "partner",
          …
        }
      }'
    ```
  </Tab>
</Tabs>

## Generate invoices

To simplify your payment process, Lago will generate invoices on behalf of partners.

All invoices generated for a partner will be marked as **self-billed**. As a result, they won’t appear in revenue analytics in Lago.

The PDF invoice will explicitly mention **Self-billing Invoice** and will not be affected by the custom footer.
A specific notice will be displayed to indicate that the invoice was generated on behalf of the partner with their consent.

These invoices follow a specific numbering system tied to the customer.
Regardless of whether your organization’s invoice numbering is scoped per **organization** or **customer**, all partner invoices will adhere to the **partner invoice numbering**.
