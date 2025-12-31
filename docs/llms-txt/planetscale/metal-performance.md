# Source: https://planetscale.com/docs/metal/metal-performance.md

# How to check performance after upgrading to Metal

> PlanetScale [Metal](/docs/metal) databases offer performance benefits for many types of workloads.

## Upgrading to Metal

When upgrading your existing PlanetScale database to Metal, its useful to know where to look to see how the upgrade has improved performance.
Here, we cover the two main places you can inspect: Insights and the database metrics panel.

In this page, we will show the results of upgrading from a `PS-640` to an `M-640`.
These both have 8 vCPUs and 64GB of RAM, but use a different underlying storage system that allows for the `M-640` to have improved performance.
Let's look at the effects of this in PlanetScale.

## Insights

After upgrading to Metal, Insights is a great place to look to see how performance has changed.
When you visit the Insights page, there are several tabs you can use to view graphs for different statistics.
The first and default one is a query latency chart.

### Query latency

After zooming in to the time period when we upgraded to Metal, here is what we see:

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-p50-p95-p99.png?fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=5c0926c621b244ce54a1589e5457b7c5" className="block dark:hidden" alt="Insights query latency" data-og-width="3356" width="3356" data-og-height="2286" height="2286" data-path="docs/images/metal/insights-p50-p95-p99.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-p50-p95-p99.png?w=280&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=873fb00f0a34d4029873620539cd1621 280w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-p50-p95-p99.png?w=560&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=8b37e611c2a267e9783bf220954f2c72 560w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-p50-p95-p99.png?w=840&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=9c24b565e3083a754910eb89cd3568e4 840w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-p50-p95-p99.png?w=1100&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=ef38ddc4b0b6cc387b3aae46342b20be 1100w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-p50-p95-p99.png?w=1650&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=c6168ae24036bfff71b4ef2988e3648a 1650w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-p50-p95-p99.png?w=2500&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=76aad6891c7470983f17d07b02a80843 2500w" />

  <img src="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-p50-p95-p99-darkmode.png?fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=24be79a237990f084d92fe4bf3c1bf82" className="hidden dark:block" alt="Insights query latency" data-og-width="3356" width="3356" data-og-height="2286" height="2286" data-path="docs/images/metal/insights-p50-p95-p99-darkmode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-p50-p95-p99-darkmode.png?w=280&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=53291c1d46bb57ff95f9e96e551bbfbe 280w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-p50-p95-p99-darkmode.png?w=560&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=8ca956d6eb375f2297fc75d505eb5686 560w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-p50-p95-p99-darkmode.png?w=840&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=b2954a9748b4dbf153ddda8b36332b80 840w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-p50-p95-p99-darkmode.png?w=1100&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=b846a0c2772413f0ebbed219fba8b789 1100w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-p50-p95-p99-darkmode.png?w=1650&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=3579d7c4ee78fec24088bbb6b297dcd0 1650w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-p50-p95-p99-darkmode.png?w=2500&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=9adeaa2a58edd77aa3d1d7c58d7693bd 2500w" />
</Frame>

Insights shows indicators on cluster resize and VTGate resize events.
We can see in the graph above the purple vertical line indicates when we upgraded to Metal (plus or minus a few minutes).
This clearly correlates with an order-of-magnitude or more improvement in p95, and p99 query latencies.
You can also click the "p99.9" icon to enable this additional metric, and see yet another significant improvement.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-p50-p95-p99-p99.9.png?fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=3c104c335ece3fa2160dd352dd57fb44" className="block dark:hidden" alt="Insights query latency" data-og-width="3354" width="3354" data-og-height="2286" height="2286" data-path="docs/images/metal/insights-p50-p95-p99-p99.9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-p50-p95-p99-p99.9.png?w=280&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=33b218b0ebc0fde64db10e866a238ea7 280w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-p50-p95-p99-p99.9.png?w=560&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=1284913e1971da6d4ac47588af75f9ff 560w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-p50-p95-p99-p99.9.png?w=840&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=829eb6bf55c4e668c55f37191d417712 840w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-p50-p95-p99-p99.9.png?w=1100&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=4e1aa99675a561492e9fea4bc31b3835 1100w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-p50-p95-p99-p99.9.png?w=1650&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=709773de9ac6eca3cf52d282d1c61901 1650w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-p50-p95-p99-p99.9.png?w=2500&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=b046f54807ba204fac5fbf9d01a55dd3 2500w" />

  <img src="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-p50-p95-p99-p99.9-darkmode.png?fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=87bb2af42bff5022ff3672d801d9dffd" className="hidden dark:block" alt="Insights query latency" data-og-width="3356" width="3356" data-og-height="2286" height="2286" data-path="docs/images/metal/insights-p50-p95-p99-p99.9-darkmode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-p50-p95-p99-p99.9-darkmode.png?w=280&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=e382a812e108376ffe0f2b41e1821088 280w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-p50-p95-p99-p99.9-darkmode.png?w=560&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=a5d81f318d76f5bc8d1c59275470e129 560w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-p50-p95-p99-p99.9-darkmode.png?w=840&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=271637c4dad22aa51e15c6d3b508846a 840w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-p50-p95-p99-p99.9-darkmode.png?w=1100&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=d070f1a4b60337e0685f5382538c44e3 1100w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-p50-p95-p99-p99.9-darkmode.png?w=1650&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=f16ee9d92d523e1413f28ef41c930520 1650w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-p50-p95-p99-p99.9-darkmode.png?w=2500&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=31fd6306431c3bc815e5003fff91b738 2500w" />
</Frame>

### Anomalies

The anomalies graph shows the % of queries that are considered anomalous, or slow-running.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-anomalies.png?fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=cbf4f51fde22c00a47acea28edf77d9d" className="block dark:hidden" alt="Insights anomalies" data-og-width="3356" width="3356" data-og-height="2286" height="2286" data-path="docs/images/metal/insights-anomalies.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-anomalies.png?w=280&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=bf6a63369104d86d3162d22c0888a456 280w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-anomalies.png?w=560&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=b50805e9f9c68c1b932d5035dd65df20 560w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-anomalies.png?w=840&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=62f485af10568d236bf712b7f4de939f 840w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-anomalies.png?w=1100&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=83f9bb03489776c53e0fee581d32ef3b 1100w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-anomalies.png?w=1650&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=65ebd07b3176cd5899fa1c36a321c439 1650w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-anomalies.png?w=2500&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=c6379f92341aeb5280ef15f88a770ccb 2500w" />

  <img src="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-anomalies-darkmode.png?fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=3dab38d383d64b18ea10183419a29ade" className="hidden dark:block" alt="Insights anomalies" data-og-width="3356" width="3356" data-og-height="2286" height="2286" data-path="docs/images/metal/insights-anomalies-darkmode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-anomalies-darkmode.png?w=280&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=dd4b97f921c7c1b8fd27d58292cfbbee 280w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-anomalies-darkmode.png?w=560&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=231da393af64981d29e31062beeaa245 560w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-anomalies-darkmode.png?w=840&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=6f31039560ae24dbbafff096f1f3063c 840w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-anomalies-darkmode.png?w=1100&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=736174d4e8cf12d31dedd63d6ed6dbcb 1100w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-anomalies-darkmode.png?w=1650&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=8c82e6727f1bf5a98e0c3751031200c4 1650w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-anomalies-darkmode.png?w=2500&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=b0de8819b3bb7c3c686dbd4f566e9673 2500w" />
</Frame>

We already had a very small number (less than 0.3%) but even so we see an improvement.

### Queries

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-qps.png?fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=19b002dcdef8801f0366109d6944ef3b" className="block dark:hidden" alt="Insights queries" data-og-width="3356" width="3356" data-og-height="2286" height="2286" data-path="docs/images/metal/insights-qps.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-qps.png?w=280&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=abe1759126df29351a05b7a779ba139c 280w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-qps.png?w=560&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=a7ec93288befd8167aa4dae57095a948 560w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-qps.png?w=840&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=9cb0e8c0cc0d95104f9c982e34178913 840w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-qps.png?w=1100&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=cabdd763f00dce299663f67c9a13a369 1100w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-qps.png?w=1650&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=981cc2f9bf571030c1a0ef1912244ced 1650w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-qps.png?w=2500&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=b380801d68ecaf3680f39998cc1a1e8c 2500w" />

  <img src="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-qps-darkmode.png?fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=820e6dc713cd8684c673c212ec3804ba" className="hidden dark:block" alt="Insights queries" data-og-width="3356" width="3356" data-og-height="2286" height="2286" data-path="docs/images/metal/insights-qps-darkmode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-qps-darkmode.png?w=280&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=75b8053141c73871d893c48c45020034 280w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-qps-darkmode.png?w=560&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=61eb4fe49f986bc9915f5d1d4c3e183e 560w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-qps-darkmode.png?w=840&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=e43582047f76c37af8d533b37104f588 840w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-qps-darkmode.png?w=1100&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=9cefb44a72ace43ce8f0a216638e127d 1100w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-qps-darkmode.png?w=1650&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=36a3c6f14e4e9f9c30eb72f684141808 1650w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-qps-darkmode.png?w=2500&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=a3c8bc1bdb4f8a51b8dbc7bd3a73dcc3 2500w" />
</Frame>

We also see a drastic improvement in average QPS.
Prior to switching over we were averaging around 2k queries per second, and after the average is closer to 14k QPS.

At the moment PlanetScale switched your traffic from the non-Metal database to the new Metal one, queries are buffered for a short span of time (seconds) to allow Vitess to do the failover to the new Metal primary and replicas.
After the failover completed, the buffered queries are quickly pushed to the database to be fulfilled.
This is a zero-downtime operation, but you may see a short spike in QPS or latency when the failover occurs.

In this example, we are using synthetic TPCC load.
In a real production workload you likely would not see such a large QPS jump, as that is dependant on demand from connected application servers.
This similarly applies for row reads and writes below.
However, what you may find is that an instance size with the same compute specs is able to handle more QPS load before needing to upgrade.
The lower IO latency and unlimited IOPS allow you to squeeze more work out of a given node in your database cluster.

### Rows read

This is the rows read graph:

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-rows-read.png?fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=7ec6c2b0f698fd564651130a841eef5e" className="block dark:hidden" alt="Insights rows read" data-og-width="3356" width="3356" data-og-height="2286" height="2286" data-path="docs/images/metal/insights-rows-read.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-rows-read.png?w=280&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=cc8c18a72d001906591c8c1b29a7bb25 280w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-rows-read.png?w=560&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=4f02214adf45e37f30e84d15de730ef6 560w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-rows-read.png?w=840&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=279eddab8e1740ae306fee12afb92479 840w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-rows-read.png?w=1100&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=ebab6037a86297f7e0ebcb7964f21353 1100w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-rows-read.png?w=1650&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=2557053692c05b667e8af3a1bf37f8d4 1650w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-rows-read.png?w=2500&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=cb1a3ac03c197f7d0f7fb49b95f75028 2500w" />

  <img src="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-rows-read-darkmode.png?fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=820e189ed1b5b5bb7e1c42f1824ee1cc" className="hidden dark:block" alt="Insights rows read" data-og-width="3356" width="3356" data-og-height="2286" height="2286" data-path="docs/images/metal/insights-rows-read-darkmode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-rows-read-darkmode.png?w=280&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=92f77cb95c2d7ad6f6bf8b33f288b5f8 280w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-rows-read-darkmode.png?w=560&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=c8210f7ced8c0bbbf8947a0674a8892d 560w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-rows-read-darkmode.png?w=840&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=4c96910125a7be100cc232794a29347c 840w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-rows-read-darkmode.png?w=1100&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=e62b853ba5c423bb1bc4ebe335f169cd 1100w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-rows-read-darkmode.png?w=1650&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=861927b7ad92c41b407672c4f6fea483 1650w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-rows-read-darkmode.png?w=2500&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=0beb8918e82f9a928922fa2487a5b53d 2500w" />
</Frame>

We can definitely see that there was an increase from the pre-Metal rows read.
However, we also see a jump for a short burst before the switch over to Metal.

This increase appears due to the way upgrading to Metal works.
When you upgrade a typical Scaler Pro database to Metal, the (greatly simplified) steps that happen in the background are:

* (A) PlanetScale spins up three new NVMe-backed instances for you (one primary and two replicas)
* (B) Once these are up and running with all the necessary MySQL and Vitess components, we begin copying the data from your existing database onto the three NVMe drives, starting with restoring from the most recent backup.
* (C) Once the backup is restored, we catch the backup up to the current state of your other database.
  This can be as quick as a few minutes or seconds if there isn't much new data, but can take some time, as we see here, if it has a lot of data to catch up.
* (D) Once the state of the old and new databases are identical, the cut over is made and the Metal instances begin serving your database traffic.
* (E) The old instances are torn down.

Depending on your database and growth rate, you may see a similar spike due to step (C).
This could be as short as a minute, or as slow as over an hour, depending on the characteristics of your database workload.

### Rows written

We get a clear jump in rows written after the upgrade:

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-rows-written.png?fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=8a50a94417b6f78e95b653add8605341" className="block dark:hidden" alt="Insights rows written" data-og-width="3356" width="3356" data-og-height="2286" height="2286" data-path="docs/images/metal/insights-rows-written.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-rows-written.png?w=280&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=0917e0bd02b6a1e23b4f4a0a52ef89f9 280w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-rows-written.png?w=560&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=fb32d5a4240b321dbeee50ca88e1dcb7 560w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-rows-written.png?w=840&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=08d39a01b5ae26d6f54b3d3972a56ab4 840w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-rows-written.png?w=1100&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=4db2c812bf56bd24d407e31c40ac3116 1100w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-rows-written.png?w=1650&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=21456ad0da9ef14ca96b77e11524a326 1650w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-rows-written.png?w=2500&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=23f424896b941b49113e5aeb77fe8249 2500w" />

  <img src="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-rows-written-darkmode.png?fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=992542f22a53ab5ba61a0e9ec09e2aa9" className="hidden dark:block" alt="Insights rows written" data-og-width="3356" width="3356" data-og-height="2286" height="2286" data-path="docs/images/metal/insights-rows-written-darkmode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-rows-written-darkmode.png?w=280&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=0f1ecd7fec8bf702c395bf320772cd08 280w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-rows-written-darkmode.png?w=560&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=12cdf44af3190a24908bd7899745b234 560w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-rows-written-darkmode.png?w=840&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=5c45c457b17bedac4432093fb4838998 840w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-rows-written-darkmode.png?w=1100&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=5fed9d2375f21d915f0b3fcc1a6958a3 1100w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-rows-written-darkmode.png?w=1650&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=dc3e83ce82934d4e3782c2f5e9a550a2 1650w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/insights-rows-written-darkmode.png?w=2500&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=94fc1293f83ae296753aae78888acf68 2500w" />
</Frame>

Unlimited IOPS allows for increased write throughput.
We can see that before the switch to Metal, we were only utilizing 20-25% of our CPU capabilities, and much of this was due to being I/O bottlenecked for this particular workload.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/metal/cpu-ram.png?fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=8fd610ae64cfce5be383697781a077de" className="block dark:hidden" alt="Insights rows written" data-og-width="1182" width="1182" data-og-height="414" height="414" data-path="docs/images/metal/cpu-ram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/metal/cpu-ram.png?w=280&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=411ddc584966056894ad7b385e4f82a7 280w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/metal/cpu-ram.png?w=560&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=e2ac6d9574b19c29a12d26bce58435bf 560w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/metal/cpu-ram.png?w=840&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=dd21691d1d902a1b848f3ea4f524da1f 840w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/metal/cpu-ram.png?w=1100&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=9f0e8a10649b9ad6da1e241c2345ab00 1100w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/metal/cpu-ram.png?w=1650&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=269c92cf3a3b97296c2ffcee42b23c45 1650w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/metal/cpu-ram.png?w=2500&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=c9557f62a10ef2c92a2cdc01cbcea59e 2500w" />

  <img src="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/metal/cpu-ram-darkmode.png?fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=8422c1acdd8a8398a6bdc8e277de264a" className="hidden dark:block" alt="Insights rows written" data-og-width="1172" width="1172" data-og-height="416" height="416" data-path="docs/images/metal/cpu-ram-darkmode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/metal/cpu-ram-darkmode.png?w=280&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=14bcbc0f56463ab99a31a6eceec8eaa9 280w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/metal/cpu-ram-darkmode.png?w=560&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=66e02965f12e3a13825ed4ab07b7414e 560w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/metal/cpu-ram-darkmode.png?w=840&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=59d0cce695ccad47f144b3e96c64186b 840w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/metal/cpu-ram-darkmode.png?w=1100&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=68cde1ac32af6a7b8db901e7870a4fcb 1100w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/metal/cpu-ram-darkmode.png?w=1650&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=896104e4de9858296280f081a8004f6f 1650w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/metal/cpu-ram-darkmode.png?w=2500&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=71d3ad66d3c3e7ee43e8b45eeb809dd7 2500w" />
</Frame>

Once we switched to Metal and had faster IO operations and unlimited IOPS, we were suddenly able to increase our CPU utilization to 80%+.

## Primary metrics

Another good place to look after upgrading to Metal is the metrics for your primary database node.
From the database's Dashboard page, click on your primary from the architecture diagram.
A panel should display on the right side of your screen with metrics from this instance.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/primary-metrics.png?fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=f386833d8ba582d2d7d9ffb4604a6895" className="block dark:hidden" alt="Database primary metrics" data-og-width="1334" width="1334" data-og-height="2072" height="2072" data-path="docs/images/metal/primary-metrics.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/primary-metrics.png?w=280&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=7aa325e40ca944da0be3b14aaa234d29 280w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/primary-metrics.png?w=560&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=937e38ec2bd39fdd169bd5292fdd5d7b 560w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/primary-metrics.png?w=840&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=9e3d75ac0efe5b9ca15c7e762cef8c7d 840w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/primary-metrics.png?w=1100&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=513e5e89718b9bb08941f4c914425c61 1100w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/primary-metrics.png?w=1650&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=d2c3610ba123a10fd874ad2cd8719798 1650w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/primary-metrics.png?w=2500&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=068b3f08c8cfed33e059a56d9bc936d8 2500w" />

  <img src="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/primary-metrics-darkmode.png?fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=2876d5e773d36bb24ea1aba76fed8f1d" className="hidden dark:block" alt="Database primary metrics" data-og-width="1334" width="1334" data-og-height="2072" height="2072" data-path="docs/images/metal/primary-metrics-darkmode.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/primary-metrics-darkmode.png?w=280&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=db72fbf8a787992642c345c99ddab6be 280w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/primary-metrics-darkmode.png?w=560&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=6afe907e0ba4f08dce8b4e741ec0dfbd 560w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/primary-metrics-darkmode.png?w=840&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=f0710611b3d11a5ebac648c0f444c608 840w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/primary-metrics-darkmode.png?w=1100&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=038b312f1e7ce27ae9f66de4de254c63 1100w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/primary-metrics-darkmode.png?w=1650&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=ac0a3b2fc5169b3713db7e5cb1677c4a 1650w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metal/primary-metrics-darkmode.png?w=2500&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=fa01712611970a5d1b4799e2a1972fe3 2500w" />
</Frame>

If the change was recently made, you can change the graph to display metrics for only the past hour using the drop down.
This gives you good insight into how the upgrade affected your IOPS capabilities, as well as CPU and RAM.
Note specifically the large jump in IOPS after the switch to Metal.

## Why is Metal so much faster?

PlanetScale databases come in two main flavors: **Metal** and **network-attached storage**.

[**Network-attached storage**](/docs/plans/planetscale-skus#network-attached-storage) (Amazon Elastic Block Storage or Google Persistent Disk) databases store all data on storage volumes that are attached to your database's compute resources over the network.
For databases in AWS we use Elastic Block Storage (EBS) and in GCP we use Persistent Disk.
These network-attached storage solutions are convenient for several reasons.
For one, it is easy to resize such storage volumes.
PlanetScale leverages this to auto-scale your storage as the size of your database grows or shrinks, allowing you to pay a per-GB storage price.

This also means that you can pair a tiny compute instance with a large amount of storage.
This works well for large data sets that are not frequently queried.
The opposite is also true — you can pair a small amount of storage with a large compute instance for workloads that are heavily CPU-bound.

One disadvantage of using **network-attached storage** storage is I/O latency.
Reads from and writes to disk need to make network round-trips to be fulfilled.
The intra-AZ network speeds in AWS and GCP data centers are generally very good, but still slower than accessing a locally-attached solid-state drive.
There is also the issue of IOPS.
The popular `gp3` EBS volume class provides 3000 IOPS included, but using more than this requires paying for additional IO bandwidth, leading to more expensive databases.

These disadvantages do not just apply to PlanetScale.
Many of the popular cloud-hosted database solutions, including those offered by Amazon and Google, use network-attached storage to simplify storage scalability.
This convenience and scalability comes at a performance cost.

**Metal** databases store all data on locally-attached NVMe SSDs.
Using direct-attached storage provides a clear solution to the performance issues described above.
The removal of network round-trips for I/O operations means low-latency IO, and we sidestep the issue of needing to pay for increased IOPS completely.
Your database now has the ability to use modern NVMe SSD technology to it's full potential.

## Data durability

One of the most important aspects of a database is storing data durably, even in the face of unexpected outages or hardware failure.

By default, all databases on PlanetScale have their data replicated three times: once on the primary database node, and then again on each of the two replicas.
More replicas can be added if desired.

When using a network-attached storage database, each of the three database instances stores a copy of the data on three distinct network-attached volumes.
When using network-attached storage, the compute instances and storage volumes are decoupled.
If one of your database compute nodes gets taken down due to an underlying hardware failure, the data is still preserved on the EBS or PD volume and can be quickly re-attached to a new node.
PlanetScale handles the detection, re-attachment, and recovery from such failures automatically.

A Metal cluster also has high durability, but with different characteristics.
Each of the three database instances (1 primary, 2 replicas) stores a copy of the data on the NVMe drives attached to the instance.
However, in this case, if one of the three compute nodes goes down, the data also goes with it.
This is why replication is so critical.
In this scenario, we still have two other copies of the data, and PlanetScale will automatically detect and replace the node that failed, bringing the total back up to three.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt