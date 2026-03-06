# Source: https://docs.vast.ai/documentation/instances/choosing/reserved-instances.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Reserved Instances

> Save up to 50% on GPU costs by pre-paying for reserved instances. Learn how to convert on-demand instances to reserved pricing.

<script
  type="application/ld+json"
  dangerouslySetInnerHTML={{
__html: JSON.stringify({
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Create and Manage Reserved Instances on Vast.ai",
  "description": "A comprehensive guide to saving up to 50% on GPU costs by converting on-demand instances to reserved instances with pre-payment, including creating, extending, and managing reservations.",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Rent an On-Demand Instance",
      "text": "Go to the Search page at cloud.vast.ai/create, find a GPU that meets your requirements, and click the Rent button. This creates an on-demand instance which can later be converted to reserved pricing."
    },
    {
      "@type": "HowToStep",
      "name": "Convert to Reserved Instance",
      "text": "Navigate to the Instances page at cloud.vast.ai/instances. On your instance card, find and click the green discount badge. A window will open showing available pre-paid periods (e.g., 1 month, 3 months, 6 months). Select your preferred period and confirm - the system calculates deposit and discount automatically."
    },
    {
      "@type": "HowToStep",
      "name": "Verify Reserved Status",
      "text": "After conversion, your instance card will display a 'Saved %' badge indicating the reserved discount is active. The discounted rate is now applied to your instance billing."
    },
    {
      "@type": "HowToStep",
      "name": "Extend Reservation (Optional)",
      "text": "You can extend your reservation at any time by clicking the Save badge again on the instance card (Web UI) or using the 'vastai prepay instance ID AMOUNT' command (CLI). Every time you add credits, your discount is recalculated, so avoid adding small amounts mid-term."
    },
    {
      "@type": "HowToStep",
      "name": "Cancel and Get Refund (Optional)",
      "text": "If you cancel (destroy) a reserved instance, you'll receive a partial refund of your unused pre-paid balance minus the total discount received. The refund amount is displayed in the delete instance modal and appears on the Billing page after deletion."
    }
  ]
})
}}
/>

Reserved instances allow you to get significant discounts (up to 50%) by pre-paying for GPU time. You can convert any on-demand instance to a reserved instance at any time.

## How Reserved Instances Work

You can **convert an on-demand instance into a reserved instance** with a lower hourly rate by pre-paying.

**Key points:**

* Convert any on-demand instance to reserved pricing
* Discounts up to 50% based on commitment length
* Pre-paid credits are locked to that specific instance
* Cannot migrate between hosts

## Creating a Reserved Instance

<Tabs>
  <Tab title="Web UI">
    **Step 1 — Rent the Instance**

    1. Go to [Search](https://cloud.vast.ai/create/) page.
    2. Find a GPU that meets your requirements, click the **Rent** button.
    3. This creates an **on-demand instance**.

    **Step 2 — Convert to a Reserved Instance**

    1. Go to the [**Instances**](https://cloud.vast.ai/instances/) page.
    2. On your instance card, find the **green** **discount badge**.

       <Frame caption="Save badge">
           <img src="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved.webp?fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=7f6fa18f75bee7b5af6c3a951a44b475" alt="Save badge" data-og-width="1009" width="1009" data-og-height="253" height="253" data-path="images/instances-reserved.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved.webp?w=280&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=7813f60a47134e77ef2621a494a71d1a 280w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved.webp?w=560&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=af308796688a137616b2f888cf2ef539 560w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved.webp?w=840&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=bd5e0a0c84c2f5741d782e30411e0743 840w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved.webp?w=1100&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=300871637bb6b6fa0f2fa647dd4eb025 1100w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved.webp?w=1650&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=4add022a9fedf1b247da8306ba570902 1650w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved.webp?w=2500&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=e9e9074e3515f6ce98b580ca4aad3968 2500w" />
       </Frame>
    3. Click the badge — a new window will open with the **available pre-paid periods** (e.g., 1 month, 3 months, 6 months).

       <Frame caption="Add Reserved Discount">
           <img src="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved-2.webp?fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=0d1c6936dcff580d464cfa2c774609f0" alt="Reserved Discount" data-og-width="800" width="800" data-og-height="703" height="703" data-path="images/instances-reserved-2.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved-2.webp?w=280&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=cf59f5a95054890d5711a1aebdc5e21c 280w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved-2.webp?w=560&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=0ebb1858f50acd48c6c8706550fd8305 560w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved-2.webp?w=840&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=896c2936d60389a866696b1a7b3fc42d 840w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved-2.webp?w=1100&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=7f892282b86a727759f95f53dd737cbc 1100w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved-2.webp?w=1650&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=442f3777e8c0a07e76f098ad6969d571 1650w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved-2.webp?w=2500&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=24ae0e1596fe64cef438dc012cf884f1 2500w" />
       </Frame>
    4. Select your preferred period and confirm. The system calculates deposit and discount automatically.

    Your instance is now reserved at the discounted rate. When an instance is converted to a reserved instance, you will see **Saved %** badge on the instance card to indicate the reserved discount is active.

        <img src="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved-3.webp?fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=f8b6fff9111a6f239d05782764737dc1" alt="" data-og-width="800" width="800" data-og-height="354" height="354" data-path="images/instances-reserved-3.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved-3.webp?w=280&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=f1a2305481103432769a3eedfd71a7ba 280w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved-3.webp?w=560&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=b933077653d549cf8d902d92dba5aed2 560w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved-3.webp?w=840&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=69e52657e1a30dff64d6d40eeaf21bfc 840w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved-3.webp?w=1100&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=02ee5c28a6f14452a03ad8b32d891c5f 1100w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved-3.webp?w=1650&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=c21ad0d829dc0883a0b5295b7f8cf27d 1650w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved-3.webp?w=2500&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=c7518417a97a8a9a6a5ef625ae1ebb60 2500w" />
  </Tab>

  <Tab title="CLI">
    1. **Add credits** to your account (if needed).
    2. Create an instance, get the instance id. CLI:`vastai show instances`
    3. Run the following command, where: **ID** is the id of instance to prepay for **AMOUNT** is amount of instance credit prepayment (default discount func of 0.2 for 1 month, 0.3 for 3 months)

    ```cli CLI theme={null}
    vastai prepay instance ID AMOUNT
    ```

    An example:

    ```cli CLI theme={null}
    vastai prepay instance 24973511 50
    prepaid for 0.546 months of instance 24973511 applying $50.0 credits for a discount of 3.5000000000000004%
    ```
  </Tab>
</Tabs>

## Important Considerations

* If you later change your mind, you can withdrawal only any fraction of the funds that remain after paying the difference between the on demand and discounted price over the current duration.
* If the machine fails the implicit or explicit Service Level Agreement and is deverified the full balance can be withdrawn without penalty.
* Reserved instances cannot migrate between different hosts.

<Warning>
  **Important:** Every time you add credits, your discount is recalculated. Avoid adding small amounts mid-term — you could end up with a worse rate. For example: If you have a 3-month reservation and add 2 weeks of credit with only 2 weeks left, your discount could drop.
</Warning>

## Extending a Reserved Instance

You can extend your reservation at any time:

<Tabs>
  <Tab title="Web UI">
    Same flow as above - via **Save** badge on instance card.
  </Tab>

  <Tab title="CLI">
    More flexibility — deposit any amount you choose. For example:

    ```bash Bash theme={null}
    vastai prepay instance 24973511 50
    prepaid for 0.546 months of instance 24973511 applying $50.0 credits for a discount of 3.5000000000000004%
    ```
  </Tab>
</Tabs>

## Refunds

You can cancel (destroy) a reserved / prepaid instance to get part of your deposit back. Refund = Remaining deposit **minus** total discount already received.

**Example:**

* On-demand: $1/hr → $720/month
* Reserved (1 month): \$576/month
* Cancel immediately → Refund = \$576
* Cancel after 15 days → Remaining = $288 → Refund = $216 (after discount penalty)
* Cancel at the end → Refund = \$0

You will see the refund on the Billing page -> Invoices table.

## Preview Reserved Pricing Before Renting

You can check the reserved price before committing:

1. Go to the **Search** page.
2. Switch the **On-demand** filter to the **Reserved** filter.

   <Frame caption="Reserved Filter">
       <img src="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved-5.webp?fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=71bab55e7a0904c2f26b94bbda5c1e6b" alt="Reserved Filter" data-og-width="1032" width="1032" data-og-height="658" height="658" data-path="images/instances-reserved-5.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved-5.webp?w=280&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=e70d16316831a5c23152372b20e8429d 280w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved-5.webp?w=560&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=4de8d1b6936e39d6ff553b5852234d44 560w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved-5.webp?w=840&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=082f1c496d0cb3b518a671bd769884c9 840w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved-5.webp?w=1100&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=7e24d0444cff330e45ddb0bdd7b25f5f 1100w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved-5.webp?w=1650&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=d823ceda86efb47e9c8672c2eeeb5758 1650w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved-5.webp?w=2500&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=aed8b83ac53fbe79e8e45bbd06eca487 2500w" />
   </Frame>
3. Set the **duration filter** (e.g., 1 month), if needed.
4. Hover over the **Rent** button — you'll see a breakdown, including a **Reserved cost** section.

   <Frame caption="Price Breakdown">
       <img src="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved-6.webp?fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=37bf837abbfab76a8d864d2923323827" alt="Price" data-og-width="830" width="830" data-og-height="451" height="451" data-path="images/instances-reserved-6.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved-6.webp?w=280&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=699bdf7e69f66cc44bc1131d39dc08b3 280w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved-6.webp?w=560&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=e7d299ae128902ddb6ce5fa0e884e408 560w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved-6.webp?w=840&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=99a34a439cd5baec2d97b7277b45d8ce 840w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved-6.webp?w=1100&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=7c0faa451f9df48912796b2569694f21 1100w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved-6.webp?w=1650&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=6dfcb0b28fa2236a84fa653717a6704f 1650w, https://mintcdn.com/vastai-80aa3a82/rJSuh7NkZ00k8fzX/images/instances-reserved-6.webp?w=2500&fit=max&auto=format&n=rJSuh7NkZ00k8fzX&q=85&s=fa4c222d761053b62dfc63939c066d25 2500w" />
   </Frame>
5. If you like the price, click **Rent** and follow the steps to convert it to a reserved instance.

## Common Questions

### Can I switch an existing on-demand instance to reserved?

Yes, if there is an available discount. Go to the **Instances** page, click the **discount badge** on your instance card, choose a period, and confirm.

### Can I extend a reserved instance?

Yes — you can extend it anytime via the same discount badge in the Instances page, as long as the instance still has an active discount period. You can use the CLI for custom amounts.

### What happens if I cancel / delete a reserved instance early?

You'll receive a partial refund of your unused pre-paid balance, minus the total discount received so far. The refund amount will be displayed in the delete instance modal and will also appear on the Billing page after you delete the instance.

<img src="https://mintcdn.com/vastai-80aa3a82/S-Qxq5X5egtYDcmf/images/image.png?fit=max&auto=format&n=S-Qxq5X5egtYDcmf&q=85&s=093b0f562ed809c88aa30f1c04b5920f" alt="image.png" data-og-width="700" width="700" data-og-height="400" height="400" data-path="images/image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/S-Qxq5X5egtYDcmf/images/image.png?w=280&fit=max&auto=format&n=S-Qxq5X5egtYDcmf&q=85&s=05f736bb7ce4e2b653b783a857568938 280w, https://mintcdn.com/vastai-80aa3a82/S-Qxq5X5egtYDcmf/images/image.png?w=560&fit=max&auto=format&n=S-Qxq5X5egtYDcmf&q=85&s=b3f6cdbb0d406c20763c99c3cce05df7 560w, https://mintcdn.com/vastai-80aa3a82/S-Qxq5X5egtYDcmf/images/image.png?w=840&fit=max&auto=format&n=S-Qxq5X5egtYDcmf&q=85&s=ce300e3bb3ef6db7b43ea5af676ed47f 840w, https://mintcdn.com/vastai-80aa3a82/S-Qxq5X5egtYDcmf/images/image.png?w=1100&fit=max&auto=format&n=S-Qxq5X5egtYDcmf&q=85&s=10db613cb26d730940956e94fc70c4ce 1100w, https://mintcdn.com/vastai-80aa3a82/S-Qxq5X5egtYDcmf/images/image.png?w=1650&fit=max&auto=format&n=S-Qxq5X5egtYDcmf&q=85&s=e1b273c57e521c8848fb9bceac5b6da5 1650w, https://mintcdn.com/vastai-80aa3a82/S-Qxq5X5egtYDcmf/images/image.png?w=2500&fit=max&auto=format&n=S-Qxq5X5egtYDcmf&q=85&s=402c4d425842f3bc4ee9e21a5d9fbc0a 2500w" />

### What happens if I stop a reserved instance?

If you stop the instance, the GPU will be released like any other instance and may be rented by another user.

## Next Steps

* Learn about other [rental types](/documentation/instances/pricing#rental-types)
* Understand [billing basics](/documentation/reference/billing)
* View your [current instances](https://cloud.vast.ai/instances/)
