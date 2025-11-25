# Source: https://getlago.com/docs/guide/subscriptions/terminate-subscription.md

# Terminate a subscription

> You can terminate a subscription at any time, whether it's active or pending.

## Terminate an active subscription

<Tabs>
  <Tab title="Dashboard">
    To terminate an active subscription through the user interface:

    1. Access the **"Customers"** section via the side menu;
    2. Select a customer from the list;
    3. In the **"Overview"** tab, select an active subscription; and
    4. Click **"Terminate subscription"**; and to terminate an active subscription.
  </Tab>

  <Tab title="API">
    <CodeGroup>
      ```bash Terminate an active subscription theme={"dark"}
        LAGO_URL="https://api.getlago.com"
        API_KEY="__YOUR_API_KEY__"
        EXTERNAL_ID="__YOUR_SUBSCRIPTION_ID__"

        curl --location --request DELETE "$LAGO_URL/api/v1/subscriptions/$EXTERNAL_ID" \
          --header "Authorization: Bearer $API_KEY"

      ```
    </CodeGroup>
  </Tab>
</Tabs>

### Generate a closing invoice at subscription termination

By default, Lago automatically generates a closing invoice for any **outstanding usage-based charges** or **pay-in-arrears subscription fees** that haven’t yet been invoiced.
If you don’t want to generate an invoice at termination:

<Tabs>
  <Tab title="Dashboard">
    In the Termination dialog, simply switch off the **Generate final invoice** option.
  </Tab>

  <Tab title="API">
    <CodeGroup>
      ```bash Terminate a subscription without closing invoice theme={"dark"}
        LAGO_URL="https://api.getlago.com"
        API_KEY="__YOUR_API_KEY__"
        EXTERNAL_ID="__YOUR_SUBSCRIPTION_ID__"

        curl --location --request DELETE "$LAGO_URL/api/v1/subscriptions/$EXTERNAL_ID?on_termination_invoice=skip" \
          --header "Authorization: Bearer $API_KEY"
      ```
    </CodeGroup>
  </Tab>
</Tabs>

### Generate a closing credit note at subscription termination

If the subscription fee has been **paid in advance**, Lago automatically issues a credit note for the **unused days**.
At termination, you can :

<Tabs>
  <Tab title="Dashboard">
    In the Termination dialog, you can choose how to handle unused amounts:

    * **Skip** – Don’t generate a credit note.
    * **Refund** – If the invoice is paid or partially paid, the unused paid amount is refunded; any unpaid unused amount is credited back to the customer.
    * **Credit** (default) – The unused amount is credited back to the customer.

    <Frame caption="Termination options">
            <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/subscriptions/images/terminate-subscription-options.png?fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=82cab54066906288f43fb1c967d12ae4" alt="" data-og-width="3456" width="3456" data-og-height="2161" height="2161" data-path="guide/subscriptions/images/terminate-subscription-options.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/subscriptions/images/terminate-subscription-options.png?w=280&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=0c0f96094f1e0ee775898b6ba4a475a6 280w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/subscriptions/images/terminate-subscription-options.png?w=560&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=a966b3418525f8c580c216446af60d07 560w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/subscriptions/images/terminate-subscription-options.png?w=840&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=ac64e9d9cf781b7fd8e2331ca9d465e1 840w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/subscriptions/images/terminate-subscription-options.png?w=1100&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=405a6df075af6fcdf92b40093fc856f2 1100w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/subscriptions/images/terminate-subscription-options.png?w=1650&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=7af1d301742b5b5fe8471eacfc682094 1650w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/subscriptions/images/terminate-subscription-options.png?w=2500&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=883d81f577cb09d18dd5f6f1fd330f86 2500w" />
    </Frame>
  </Tab>

  <Tab title="API">
    <CodeGroup>
      ```bash Terminate a subscription without closing credit note theme={"dark"}
        LAGO_URL="https://api.getlago.com"
        API_KEY="__YOUR_API_KEY__"
        EXTERNAL_ID="__YOUR_SUBSCRIPTION_ID__"

        curl --location --request DELETE "$LAGO_URL/api/v1/subscriptions/$EXTERNAL_ID?on_termination_credit_note=skip" \
          --header "Authorization: Bearer $API_KEY"
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Terminate a pending subscription

<Tabs>
  <Tab title="Dashboard">
    To terminate a pending subscription through the user interface:

    1. Access the **"Customers"** section via the side menu;
    2. Select a customer from the list;
    3. In the **"Overview"** tab, select a pending subscription (subscription set in the future or pending downgrade); and
    4. Click **"Terminate subscription"**; and to cancel a pending subscription subscription.
  </Tab>

  <Tab title="API">
    <CodeGroup>
      ```bash Terminate a pending subscription theme={"dark"}
          LAGO_URL="https://api.getlago.com"
          API_KEY="__YOUR_API_KEY__"
          EXTERNAL_ID="__YOUR_SUBSCRIPTION_ID__"

          curl --location --request DELETE "$LAGO_URL/api/v1/subscriptions/$EXTERNAL_ID?status=pending" \
            --header "Authorization: Bearer $API_KEY"
      ```
    </CodeGroup>
  </Tab>
</Tabs>

<Warning>
  To ensure the termination of a pending subscription, it is crucial to include the `?status=pending` filter in your endpoint.
  Neglecting to do so will render any termination attempts ineffective.
</Warning>
