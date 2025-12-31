# Source: https://planetscale.com/docs/vitess/scaling/read-only-regions.md

# Read-only regions

## Overview

Replicate your production database across the globe by creating read-only regions in any available [PlanetScale region](/docs/vitess/regions).

This feature supports globally distributed applications by enabling your database to perform low latency reads in the regions closest to your applications and users.

## How to create a read-only region

<Steps>
  <Step>
    In the [PlanetScale dashboard](https://app.planetscale.com), select the database you want to add a read-only region to.
  </Step>

  <Step>
    Navigate to the "**Branches**" page.

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/read-only-regions/landing-to-branches.png?fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=bb6f4651119b4ce2424abb724a860527" alt="landing-to-branches" data-og-width="3606" width="3606" data-og-height="1476" height="1476" data-path="docs/images/assets/docs/concepts/read-only-regions/landing-to-branches.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/read-only-regions/landing-to-branches.png?w=280&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=60848448f979218caf88d21c89f94f97 280w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/read-only-regions/landing-to-branches.png?w=560&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=ba3032ae40fdceb76a1f13ec6816dc32 560w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/read-only-regions/landing-to-branches.png?w=840&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=01b4933edf8ffa7366660436c22b2aff 840w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/read-only-regions/landing-to-branches.png?w=1100&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=d8f394649ca2c88607d471484cdd6347 1100w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/read-only-regions/landing-to-branches.png?w=1650&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=467059d8b85abfc61659caf3894c3bad 1650w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/read-only-regions/landing-to-branches.png?w=2500&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=e8ae806f57ae343d0393c93bd0b8ac28 2500w" />
    </Frame>
  </Step>

  <Step>
    Select the current production branch.

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/read-only-regions/branches-to-production.png?fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=db67ef90e6d7ef3db80f348223fe0a94" alt="branches-to-production" data-og-width="3358" width="3358" data-og-height="1184" height="1184" data-path="docs/images/assets/docs/concepts/read-only-regions/branches-to-production.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/read-only-regions/branches-to-production.png?w=280&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=bfdec70d56386f2da5019cfb7e781d8b 280w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/read-only-regions/branches-to-production.png?w=560&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=a84d42bff9444cd7c2429ce4b7e240d9 560w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/read-only-regions/branches-to-production.png?w=840&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=d534cdd064c1ce0b923c8428a898c82b 840w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/read-only-regions/branches-to-production.png?w=1100&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=ab9d8fe0425aede89632e0d5dabee77d 1100w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/read-only-regions/branches-to-production.png?w=1650&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=614ae78faf1f5005cdd72ef5ef54291c 1650w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/read-only-regions/branches-to-production.png?w=2500&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=162fb0982d31c57debf20dc2602c366c 2500w" />
    </Frame>
  </Step>

  <Step>
    On the right-side menu, click the "**Add region**" button.

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/read-only-regions/add-region.png?fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=a7683c2072c3833c45ecddf4440f0dda" alt="add-region" data-og-width="1296" width="1296" data-og-height="1034" height="1034" data-path="docs/images/assets/docs/concepts/read-only-regions/add-region.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/read-only-regions/add-region.png?w=280&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=7e7eddb10b94582eba1c1f2e6c01d503 280w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/read-only-regions/add-region.png?w=560&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=5669d6d1adbb227c0741ac92262c711a 560w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/read-only-regions/add-region.png?w=840&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=f2ec2e6e9432c741cd4479abe25ed7db 840w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/read-only-regions/add-region.png?w=1100&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=95e6f69f990198668ea6addde3310621 1100w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/read-only-regions/add-region.png?w=1650&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=c55e829cf72366875490ad9c34ad027d 1650w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/read-only-regions/add-region.png?w=2500&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=53b3aa4d2ba369099a8ad508b0611fc9 2500w" />
    </Frame>
  </Step>

  <Step>
    Select the desired AWS region from the dropdown of [available regions](/docs/vitess/regions) in the modal.

    <Frame>
            <img src="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/read-only-regions/modal.png?fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=9680a8cfd4d203d17c2d175f12831389" alt="modal" data-og-width="3099" width="3099" data-og-height="1469" height="1469" data-path="docs/images/assets/docs/concepts/read-only-regions/modal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/read-only-regions/modal.png?w=280&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=1ea6773f61139e7b8f66c81be3b0d182 280w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/read-only-regions/modal.png?w=560&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=9538ebe4143f4f08ba6b8a69ec3099be 560w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/read-only-regions/modal.png?w=840&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=0c8e000c36fab73dc792793af155f11d 840w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/read-only-regions/modal.png?w=1100&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=e870a02d97ca4cf06911f6201ee461a9 1100w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/read-only-regions/modal.png?w=1650&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=e7f32026cf848b179a75eff7e7e94d19 1650w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/read-only-regions/modal.png?w=2500&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=6351359432a80b2983a82618210adf2d 2500w" />
    </Frame>
  </Step>

  <Step>
    Click "**Add region**" and wait for your data to finish initially replicating across regions.
  </Step>
</Steps>

## How to remove a read-only region

<Steps>
  <Step>
    Go to your database's production branch.
  </Step>

  <Step>
    Click on the "**...**" at the top right of the region that you want to delete.
  </Step>

  <Step>
    Click "**Delete region**".
  </Step>
</Steps>

Once you delete a region, you will no longer be charged for the storage or row reads associated with that region. If you were using global replica credentials, you do not need to take any additional action. Read queries will still be sent to the closest replica for any queries that are using global replica credentials.

## How to query a read-only region

Connecting to a read-only region requires using a [replica credential](/docs/vitess/scaling/replicas). You can create a global replica credential by following these steps:

<Steps>
  <Step>
    Go to your database's production branch.
  </Step>

  <Step>
    Click on the "Connect" button in the top right
  </Step>

  <Step>
    On the "Connect" page, select "Replica" as the connection type.
  </Step>

  <Step>
    Click "Create password" to generate a new username and password pair.
  </Step>
</Steps>

Alternatively, you can create a connection string by going to your database settings page > "**Passwords**" > "**New password**".

All queries made using this password will be routed to your branch's replicas or the nearest read-only region. If you want to route queries to a specific read-only region, you can go to the "**Passwords**" page within your database's settings page and select the created password. Under "**Database endpoint**", you can then select "**Direct**" and choose your desired host from the "**Host**" dropdown.

## Concepts

### Replication across regions

PlanetScale replicates your data across regions with an asynchronous strategy, first storing your changes in the primary region and then forwarding them to your read-only region(s). The time that it takes those changes to propagate to your read-only region can be defined as "replication lag" and be measured by issuing the following statement to your read-only regions:

```sql  theme={null}
SELECT max_repl_lag();
```

The `max_repl_lag()` function will return an instantaneous measurement of the maximum amount of seconds it has been since your read-only region has stored changes made to your primary region.

### Read-only connections

Connecting to a read-only region will allow you to query your data, but will not allow you to insert, update, or delete it.

## Availability and pricing

Read-only regions are available on [Scaler Pro and multi-tenant Enterprise plans](/docs/planetscale-plans). Read-only regions are priced differently depending on the selected region. You can find a full list of pricing in the [Scaler Pro cluster pricing documentation](/docs/plans/cluster-sizing).

### Storage costs

Your storage costs will increase linearly with the amount of read-only regions added.
Adding new read-only regions will always be billed as standalone storage and will not count toward your included storage.

As an example, let's say you're on our Scaler Pro plan with 10 GB of included storage and your primary contains 7 GB of data.
If you have two read-only regions, each one will be charged at our additional storage rate, for a total of 14 GB.
The read-only region storage rate is\ $0.75 per GB, and in this case would lead to an additional storage charge of\ $10.50.

For more information on storage billing costs, see our [Billing documentation](/docs/planetscale-plans).

## Pricing

Below we include the costs for read-only regions in each available region up to `400`-level instances.
Larger sizes are available in the app.

### AWS ap-northeast-1 (Tokyo)

| Read-only region | Price   |
| ---------------- | ------- |
| PS-10RR          | \ \$19  |
| PS-20RR          | \ \$28  |
| PS-40RR          | \ \$48  |
| PS-80RR          | \ \$86  |
| PS-160RR         | \ \$168 |
| PS-320RR         | \ \$336 |
| PS-400RR         | \ \$480 |

| Metal read-only region | Storage | Price   |
| ---------------------- | ------- | ------- |
| M-160RR                | 110 GB  | \ \$296 |
| M-160RR                | 460 GB  | \ \$324 |
| M-320RR                | 229 GB  | \ \$588 |
| M-320RR                | 929 GB  | \ \$640 |

### AWS ap-south-1 (Mumbai)

| Read-only region | Price   |
| ---------------- | ------- |
| PS-10RR          | \ \$10  |
| PS-20RR          | \ \$15  |
| PS-40RR          | \ \$26  |
| PS-80RR          | \ \$46  |
| PS-160RR         | \ \$91  |
| PS-320RR         | \ \$182 |
| PS-400RR         | \ \$260 |

| Metal read-only region | Storage | Price   |
| ---------------------- | ------- | ------- |
| M-160RR                | 110 GB  | \ \$256 |
| M-160RR                | 460 GB  | \ \$312 |
| M-320RR                | 229 GB  | \ \$508 |
| M-320RR                | 929 GB  | \ \$620 |

### AWS ap-southeast-1 (Singapore)

| Read-only region | Price   |
| ---------------- | ------- |
| PS-10RR          | \ \$19  |
| PS-20RR          | \ \$28  |
| PS-40RR          | \ \$48  |
| PS-80RR          | \ \$86  |
| PS-160RR         | \ \$168 |
| PS-320RR         | \ \$336 |
| PS-400RR         | \ \$480 |

| Metal read-only region | Storage | Price   |
| ---------------------- | ------- | ------- |
| M-160RR                | 110 GB  | \ \$296 |
| M-160RR                | 460 GB  | \ \$332 |
| M-320RR                | 229 GB  | \ \$588 |
| M-320RR                | 929 GB  | \ \$656 |

### AWS ap-southeast-2 (Sydney)

| Read-only region | Price   |
| ---------------- | ------- |
| PS-10RR          | \ \$19  |
| PS-20RR          | \ \$28  |
| PS-40RR          | \ \$48  |
| PS-80RR          | \ \$86  |
| PS-160RR         | \ \$168 |
| PS-320RR         | \ \$336 |
| PS-400RR         | \ \$480 |

| Metal read-only region | Storage | Price   |
| ---------------------- | ------- | ------- |
| M-160RR                | 110 GB  | \ \$280 |
| M-160RR                | 460 GB  | \ \$332 |
| M-320RR                | 229 GB  | \ \$560 |
| M-320RR                | 929 GB  | \ \$656 |

### AWS eu-central-1 (Frankfurt)

| Read-only region | Price   |
| ---------------- | ------- |
| PS-10RR          | \ \$19  |
| PS-20RR          | \ \$28  |
| PS-40RR          | \ \$48  |
| PS-80RR          | \ \$86  |
| PS-160RR         | \ \$168 |
| PS-320RR         | \ \$336 |
| PS-400RR         | \ \$480 |

| Metal read-only region | Storage | Price   |
| ---------------------- | ------- | ------- |
| M-160RR                | 110 GB  | \ \$292 |
| M-160RR                | 460 GB  | \ \$328 |
| M-320RR                | 229 GB  | \ \$584 |
| M-320RR                | 929 GB  | \ \$652 |

### AWS eu-west-1 (Dublin)

| Read-only region | Price   |
| ---------------- | ------- |
| PS-10RR          | \ \$18  |
| PS-20RR          | \ \$26  |
| PS-40RR          | \ \$44  |
| PS-80RR          | \ \$80  |
| PS-160RR         | \ \$156 |
| PS-320RR         | \ \$313 |
| PS-400RR         | \ \$448 |

| Metal read-only region | Storage | Price   |
| ---------------------- | ------- | ------- |
| M-160RR                | 110 GB  | \ \$272 |
| M-160RR                | 460 GB  | \ \$304 |
| M-320RR                | 229 GB  | \ \$540 |
| M-320RR                | 929 GB  | \ \$604 |

### AWS eu-west-2 (London)

| Read-only region | Price   |
| ---------------- | ------- |
| PS-10RR          | \ \$18  |
| PS-20RR          | \ \$28  |
| PS-40RR          | \ \$46  |
| PS-80RR          | \ \$84  |
| PS-160RR         | \ \$163 |
| PS-320RR         | \ \$327 |
| PS-400RR         | \ \$468 |

| Metal read-only region | Storage | Price   |
| ---------------------- | ------- | ------- |
| M-160RR                | 110 GB  | \ \$288 |
| M-160RR                | 460 GB  | \ \$320 |
| M-320RR                | 229 GB  | \ \$568 |
| M-320RR                | 929 GB  | \ \$632 |

### AWS sa-east-1 (Sao Paulo)

| Read-only region | Price   |
| ---------------- | ------- |
| PS-10RR          | \ \$25  |
| PS-20RR          | \ \$38  |
| PS-40RR          | \ \$63  |
| PS-80RR          | \ \$114 |
| PS-160RR         | \ \$223 |
| PS-320RR         | \ \$447 |
| PS-400RR         | \ \$639 |

### AWS us-east-1 (N. Virginia)

| Read-only region | Price   |
| ---------------- | ------- |
| PS-10RR          | \ \$16  |
| PS-20RR          | \ \$24  |
| PS-40RR          | \ \$40  |
| PS-80RR          | \ \$72  |
| PS-160RR         | \ \$140 |
| PS-320RR         | \ \$280 |
| PS-400RR         | \ \$400 |

| Metal read-only region | Storage  | Price   |
| ---------------------- | -------- | ------- |
| M-160RR                | 110 GB   | \ \$244 |
| M-160RR                | 460 GB   | \ \$276 |
| M-160RR                | 1,241 GB | \ \$404 |
| M-320RR                | 229 GB   | \ \$484 |
| M-320RR                | 929 GB   | \ \$584 |
| M-320RR                | 2,490 GB | \ \$804 |

### AWS us-east-2 (Ohio)

| Read-only region | Price   |
| ---------------- | ------- |
| PS-10RR          | \ \$16  |
| PS-20RR          | \ \$24  |
| PS-40RR          | \ \$40  |
| PS-80RR          | \ \$72  |
| PS-160RR         | \ \$140 |
| PS-320RR         | \ \$280 |
| PS-400RR         | \ \$400 |

| Metal read-only region | Storage  | Price   |
| ---------------------- | -------- | ------- |
| M-160RR                | 110 GB   | \ \$244 |
| M-160RR                | 460 GB   | \ \$276 |
| M-160RR                | 1,241 GB | \ \$404 |
| M-320RR                | 229 GB   | \ \$484 |
| M-320RR                | 929 GB   | \ \$584 |
| M-320RR                | 2,490 GB | \ \$804 |

### AWS us-west-2 (Oregon)

| Read-only region | Price   |
| ---------------- | ------- |
| PS-10RR          | \ \$16  |
| PS-20RR          | \ \$24  |
| PS-40RR          | \ \$40  |
| PS-80RR          | \ \$72  |
| PS-160RR         | \ \$140 |
| PS-320RR         | \ \$280 |
| PS-400RR         | \ \$400 |

| Metal read-only region | Storage  | Price   |
| ---------------------- | -------- | ------- |
| M-160RR                | 110 GB   | \ \$244 |
| M-160RR                | 460 GB   | \ \$276 |
| M-160RR                | 1,241 GB | \ \$404 |
| M-320RR                | 229 GB   | \ \$484 |
| M-320RR                | 929 GB   | \ \$584 |
| M-320RR                | 2,490 GB | \ \$804 |

### GCP asia-northeast3 (Seoul, South Korea)

| Read-only region | Price   |
| ---------------- | ------- |
| PS-10RR          | \ \$19  |
| PS-20RR          | \ \$28  |
| PS-40RR          | \ \$48  |
| PS-80RR          | \ \$86  |
| PS-160RR         | \ \$168 |
| PS-320RR         | \ \$336 |
| PS-400RR         | \ \$480 |

### GCP northamerica-northeast1 (Montréal, Québec)

| Read-only region | Price   |
| ---------------- | ------- |
| PS-10RR          | \ \$16  |
| PS-20RR          | \ \$24  |
| PS-40RR          | \ \$40  |
| PS-80RR          | \ \$72  |
| PS-160RR         | \ \$140 |
| PS-320RR         | \ \$280 |
| PS-400RR         | \ \$400 |

### GCP us-central1 (Council Bluffs, Iowa)

| Read-only region | Price   |
| ---------------- | ------- |
| PS-10RR          | \ \$16  |
| PS-20RR          | \ \$24  |
| PS-40RR          | \ \$40  |
| PS-80RR          | \ \$72  |
| PS-160RR         | \ \$140 |
| PS-320RR         | \ \$280 |
| PS-400RR         | \ \$400 |

### GCP us-east4 (Ashburn, Virginia)

| Read-only region | Price   |
| ---------------- | ------- |
| PS-10RR          | \ \$16  |
| PS-20RR          | \ \$24  |
| PS-40RR          | \ \$40  |
| PS-80RR          | \ \$72  |
| PS-160RR         | \ \$140 |
| PS-320RR         | \ \$280 |
| PS-400RR         | \ \$400 |

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt