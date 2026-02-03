# Source: https://getlago.com/docs/guide/plans/charges/grouping.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Group keys

## Pricing group keys

AI and infrastructure platforms often tailor pricing based on variables such as geography, hosting provider, or service tier. Lago's Pricing Group Keys offer a streamlined way to support this kind of dynamic pricing without duplicating product definitions.

With pricing group keys, you can group usage events to a single product based on configurable dimensions—like cloud provider, model type, deployment region, or instance class. This allows you to reflect real-world cost variations while keeping your product catalog clean and manageable.

When setting up a charge, you define the relevant keys. You don't need to predefine every possible value. Instead, Lago intelligently routes each usage event to the correct pricing group based on the attributes provided at runtime.

### Define pricing group keys

To define a pricing group key, you need to:

1. Go to the plan where you want to configure dynamic pricing;
2. Select the charge you want to apply the pricing group key to;
3. In the charge settings, enter a key in the Pricing Group Key field (e.g., region, cloud, instance\_type);
4. Send usage events that include this key in the properties object, using any value without predefining them; and
5. Lago will automatically group usage into the correct pricing bucket based on the key's value.

<Note>
  Pricing group keys are available for all charge models. You can define multiple pricing group keys for a single charge.
</Note>

### Example of pricing group keys

Let's define a pricing group key called `regions` for a charge used to calculate Storage costs for your customers.

<Frame caption="Define a pricing group key">
  <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/pricing-group-key.png?fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=b0573b6610633157243b8e56cbe9cea8" data-og-width="692" width="692" data-og-height="613" height="613" data-path="guide/plans/images/pricing-group-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/pricing-group-key.png?w=280&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=e7937975c5d443a96d76393304385989 280w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/pricing-group-key.png?w=560&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=34ee3c52d7aac0b84d67682bd5365208 560w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/pricing-group-key.png?w=840&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=f168d44f4dfe80cb3d5ae2342ea2b2d7 840w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/pricing-group-key.png?w=1100&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=0321f0ba58c2308b509803366afdf184 1100w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/pricing-group-key.png?w=1650&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=b3a5635a17d06f9a70fe3b29b14a51b3 1650w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/pricing-group-key.png?w=2500&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=36599b9620a019525db7ab843d48262d 2500w" />
</Frame>

By sending usage events with a `regions` property, you can include any number of region values. Lago will automatically group and aggregate usage based on the values provided in your events.

```json  theme={"dark"}
{
  "event": {
    "transaction_id": "{{$randomUUID}}",
    "external_subscription_id": "8546dce0-d9e6-4544-ac8a-fbc77340cd9f",
    "code": "storage",
    "properties": {
      "gb": 20,
      "regions": "us-east-1"
    }
  }
}
```

<Frame caption="Calculate usage with pricing group values">
  <img src="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/pricing-group-usage.png?fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=26c60d1276bd5a80e8e5bc95fb25eef4" data-og-width="786" width="786" data-og-height="566" height="566" data-path="guide/plans/images/pricing-group-usage.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/pricing-group-usage.png?w=280&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=abe26c08c32b182ef49a62d061c21bdd 280w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/pricing-group-usage.png?w=560&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=809fd1dda1f58ea6bfe0b856a6474f9c 560w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/pricing-group-usage.png?w=840&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=2b6085591b5e03c1fb69788c4a99f56a 840w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/pricing-group-usage.png?w=1100&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=40a4a052647e9931f2153afe9325d88b 1100w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/pricing-group-usage.png?w=1650&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=65552da825392aee7c266217e810a6c5 1650w, https://mintcdn.com/lago-docs/ugh-mbZn6BFsC-Za/guide/plans/images/pricing-group-usage.png?w=2500&fit=max&auto=format&n=ugh-mbZn6BFsC-Za&q=85&s=08e6626196280fcc0d2b39ac0272f9ef 2500w" />
</Frame>
