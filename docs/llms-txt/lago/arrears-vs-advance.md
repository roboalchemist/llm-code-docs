# Source: https://getlago.com/docs/guide/plans/charges/arrears-vs-advance.md

# Arrears vs Advance

> Usage-based charges can be either charged in advance or in arrears

You have the flexibility to define the nature of charges associated with your products or services. Specifically, you can
**determine whether a charge has to be paid in arrears (at the end of the period), or in advance (immediately on event ingestion)**.

## Charges paid in arrears[](#charges-arrears "Direct link to heading")

If you opt for charges to be settled in arrears, they will be invoiced at the end of the billing period based on
the actual usage during that period. This payment option is ideal for usage types like storage, API calls, or compute,
where it is more practical to wait until the end of the period before billing. By default, all charges are configured to be
billed in arrears.

<Tabs>
  <Tab title="Dashboard">
    You can easily manage this billing settings through the user interface. Within the UI, you will find options to customize
    the invoice cadence by setting a charge as invoiced in arrears.

    <Frame caption="Define a charge paid in arrears">
      <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/charge-in-arrears-1d16763a9e4212018386d79e400eea2a.png?fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=fbedaa93617058529d9a24565e9c1f60" data-og-width="1638" width="1638" data-og-height="1200" height="1200" data-path="guide/plans/images/charge-in-arrears-1d16763a9e4212018386d79e400eea2a.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/charge-in-arrears-1d16763a9e4212018386d79e400eea2a.png?w=280&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=e6c12b9ba4894ad4b8b8ca5973b38624 280w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/charge-in-arrears-1d16763a9e4212018386d79e400eea2a.png?w=560&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=c05b42b1337026da4012263d867c3640 560w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/charge-in-arrears-1d16763a9e4212018386d79e400eea2a.png?w=840&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=a39ca9ff2c19285454bd11b4abf15d6f 840w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/charge-in-arrears-1d16763a9e4212018386d79e400eea2a.png?w=1100&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=865fbd2ceeea4b3821ca978c9ff20684 1100w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/charge-in-arrears-1d16763a9e4212018386d79e400eea2a.png?w=1650&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=ca6bbac67eb7b237a7e6c1dbc56f656d 1650w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/charge-in-arrears-1d16763a9e4212018386d79e400eea2a.png?w=2500&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=63f119945540e59539b705ef6455620e 2500w" />
    </Frame>
  </Tab>

  <Tab title="API">
    Define `pay_in_advance : false` on a charge to bill it in arrears:

    <CodeGroup>
      ```bash Define a charge as paid in arrears {16, 22} theme={"dark"}
          LAGO_URL="https://api.getlago.com"
          API_KEY="__YOUR_API_KEY__"

          curl --location --request POST "$LAGO_URL/api/v1/plans" \
          --header "Authorization: Bearer $API_KEY" \
          --header 'Content-Type: application/json' \
          --data-raw '{
            "plan": {
              "name": "Premium",
              "code": "premium",
              "interval": "monthly",
              "description": "Premium plan for SMB companies",
              "amount_cents": 50000,
              "amount_currency": "USD",
              "trial_period": 0.0,
              "pay_in_advance": true,
              "bill_charges_monthly": true,
              "charges": [
                {
                  "billable_metric_id": "1111_2222_3333_4444",
                  "charge_model": "percentage",
                  "pay_in_advance": false,
                  "invoiceable": true,
                  "min_amount_cents": 100,
                  "properties": {
                    "rate": "0.5",
                    "fixed_amount": "1",
                    "free_units_per_events": 3,
                    "free_units_per_total_aggregation": null
                  }
                }
              ]
            }
          }'
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Charges paid in advance[](#charges-advance "Direct link to heading")

With this payment option, charges are invoiced immediately upon any changes in usage. It is particularly useful for scenarios
where you need to bill customers instantly for usage-based actions, such as new user seat or integrations.

<Tabs>
  <Tab title="Dashboard">
    You can easily manage this billing settings through the user interface. Within the UI, you will find options to customize
    the invoice cadence by setting a charge as invoiced in arrears.

    <Frame caption="Define a charge paid in arrears">
      <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/charge-in-advance-5a13fc011d78a058f7767519c5817961.png?fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=98670066a3fbbc6ae69a0cbc82d72ef4" data-og-width="1638" width="1638" data-og-height="1194" height="1194" data-path="guide/plans/images/charge-in-advance-5a13fc011d78a058f7767519c5817961.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/charge-in-advance-5a13fc011d78a058f7767519c5817961.png?w=280&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=7f1d5a2048e7e01096205f2c36ea0edd 280w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/charge-in-advance-5a13fc011d78a058f7767519c5817961.png?w=560&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=ca7499beb0102f82577793774e3ddb2b 560w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/charge-in-advance-5a13fc011d78a058f7767519c5817961.png?w=840&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=0c35480e7c43fe989c3c81cd9f981b02 840w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/charge-in-advance-5a13fc011d78a058f7767519c5817961.png?w=1100&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=681ac1a8e1ddd752b8b0f5fa0e196a4a 1100w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/charge-in-advance-5a13fc011d78a058f7767519c5817961.png?w=1650&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=49354a70b8d942e1c0de8a63dd9d6dec 1650w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/charge-in-advance-5a13fc011d78a058f7767519c5817961.png?w=2500&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=cacd77fdc1d2e8123db1285a4c17b9cf 2500w" />
    </Frame>
  </Tab>

  <Tab title="API">
    Define `pay_in_advance : true` on a charge to bill it in advance:

    <CodeGroup>
      ```bash Define a charge as paid in advance {16, 22} theme={"dark"}
      LAGO_URL="https://api.getlago.com"
      API_KEY="__YOUR_API_KEY__"

      curl --location --request POST "$LAGO_URL/api/v1/plans" \
      --header "Authorization: Bearer $API_KEY" \
      --header 'Content-Type: application/json' \
      --data-raw '{
        "plan": {
          "name": "Premium",
          "code": "premium",
          "interval": "monthly",
          "description": "Premium plan for SMB companies",
          "amount_cents": 50000,
          "amount_currency": "USD",
          "trial_period": 0.0,
          "pay_in_advance": true,
          "bill_charges_monthly": true,
          "charges": [
            {
              "billable_metric_id": "1111_2222_3333_4444",
              "charge_model": "percentage",
              "pay_in_advance": true,
              "invoiceable": true,
              "min_amount_cents": 100,
              "properties": {
                "rate": "0.5",
                "fixed_amount": "1",
                "free_units_per_events": 3,
                "free_units_per_total_aggregation": null
              }
            }
          ]
        }
      }'
      ```
    </CodeGroup>
  </Tab>
</Tabs>
