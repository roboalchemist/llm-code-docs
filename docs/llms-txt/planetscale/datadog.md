# Source: https://planetscale.com/docs/vitess/monitoring/datadog.md

# Source: https://planetscale.com/docs/vitess/integrations/datadog.md

# Datadog integration

> PlanetScale can push metrics to Datadog to assist your team with understanding your database usage and performance.

<Warning>
  This Datadog integration is no longer receiving updates or new metric additions. You should instead use our [Datadog Agent Integration](/docs/vitess/tutorials/prometheus-metrics-datadog), which provides more metrics than this native integration.

  If you have any questions about migrating to the Datadog Agent Integration, [reach out to support](https://planetscale.com/contact?initial=support).
</Warning>

## Prerequisites

* A [Datadog](https://www.datadoghq.com/) account

## Configuring the Datadog integration

<Steps>
  <Step>
    In Datadog, install the [PlanetScale integration](https://app.datadoghq.com/account/settings#integrations/planetscale).
  </Step>

  <Step>
    Create a Datadog API key in your [Datadog Organization Settings](https://app.datadoghq.com/organization-settings/api-keys) and copy the key.
  </Step>

  <Step>
    In PlanetScale, go to your organization's [Integrations settings](https://app.planetscale.com/settings/integrations), and select **Configure** for the Datadog integration. Paste your Datadog API key into the field.
  </Step>
</Steps>

Once complete, a "PlanetScale" dashboard will be available with incoming metrics from PlanetScale.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/datadog/dashboard.png?fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=82eface6b002bf541dfbdfd3872fcb5f" alt="PlanetScale Default Dashboard in Datadog" data-og-width="2728" width="2728" data-og-height="1988" height="1988" data-path="docs/images/assets/docs/integrations/datadog/dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/datadog/dashboard.png?w=280&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=854a1bf1a8734829cbef18fb81e9d792 280w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/datadog/dashboard.png?w=560&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=168cdb12f985df9a270efb4f30f37bb6 560w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/datadog/dashboard.png?w=840&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=c0ddbfa415ac9c1e0171056e83d7cb7a 840w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/datadog/dashboard.png?w=1100&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=893cd14f67d8e83c73532e8626137a0b 1100w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/datadog/dashboard.png?w=1650&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=c56a588d6fbf265d0ba56b864e1f6b61 1650w, https://mintcdn.com/planetscale-cad1a68a/52I47nER2-XBxbHF/docs/images/assets/docs/integrations/datadog/dashboard.png?w=2500&fit=max&auto=format&n=52I47nER2-XBxbHF&q=85&s=e7352e48985d34ec6cad22cfb7a6f507 2500w" />
</Frame>

## Metrics We Collect

Once configured, PlanetScale collects the following metrics from every branch in your organization.

| **Metric name**                            | **Metric type** | **Description**                                                                                     |
| :----------------------------------------- | :-------------- | :-------------------------------------------------------------------------------------------------- |
| planetscale.connections                    | gauge           | Number of active connections to a database branch. *Shown as connection.*                           |
| planetscale.primary.cpu\_usage             | gauge           | Percentage of CPU utilized on a database branch's primary. *Shown as percent.*                      |
| planetscale.primary.memory\_usage          | gauge           | Percentage of memory utilized on a database branch's primary. *Shown as percent.*                   |
| planetscale.queries.latency                | gauge           | Query times in the p50, p95, p99 and p999 percentiles. *Shown as millisecond.*                      |
| planetscale.replication\_lag               | gauge           | Replication lag in seconds between a database branch's primary and each replica. *Shown as second.* |
| planetscale.rows\_read                     | count           | Number of rows read from a database branch. *Shown as row.*                                         |
| planetscale.rows\_written                  | count           | Number of rows written to a database branch. *Shown as row.*                                        |
| planetscale.tables.cumulative\_query\_time | count           | Cumulative active query time in a database branch, by table and statement. *Shown as nanosecond.*   |
| planetscale.tables.queries                 | count           | Number of queries issued to a database branch, by table and statement. *Shown as query.*            |
| planetscale.tables.rows\_deleted           | count           | Number of rows deleted from a database branch, by table. *Shown as row.*                            |
| planetscale.tables.rows\_inserted          | count           | Number of rows inserted into a database branch, by table. *Shown as row.*                           |
| planetscale.tables.rows\_selected          | count           | Number of rows selected in a database branch, by table. *Shown as row.*                             |
| planetscale.tables.rows\_updated           | count           | Number of rows updated in a database branch, by table. *Shown as row.*                              |
| planetscale.tables.storage                 | gauge           | Total bytes stored in a database branch, by table. *Shown as byte.*                                 |
| planetscale.vtgate.errors                  | count           | Number of errors encountered by a database branch's vtgate. *Shown as error.*                       |
| planetscale.vttablet.mem\_util.max         | gauge           | Maximum memory utilization of a database branch's vttablet. *Shown as percent.*                     |
| planetscale.vttablet.mem\_util.avg         | gauge           | Average memory utilization of a database branch's vttablet. *Shown as percent.*                     |
| planetscale.vttablet.iops                  | gauge           | Number of IOPS performed by a database branch's vttablet. *Shown as operation.*                     |

## Billing

The Datadog integration is available on all of our [paid plans](https://planetscale.com/pricing).

## Frequently asked questions

### How do I track replication lag in Datadog?

You can use the following formula to set alerts for replication lag:

```bash  theme={null}
(max:planetscale.replication_lag{ps_database:<DATABASE_NAME> ps_tablet_type:replica, ps_branch:<MAIN>})
```

Make sure you replace `<DATABASE_NAME>` with your PlanetScale database name and `<MAIN>` with the name of the branch for which you'd like to track replication lag.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt