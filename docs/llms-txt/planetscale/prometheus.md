# Source: https://planetscale.com/docs/vitess/tutorials/prometheus.md

# Source: https://planetscale.com/docs/vitess/integrations/prometheus.md

# Prometheus

> PlanetScale exposes Prometheus-compatible metrics endpoints for scraping metrics about your database branches. This, along with our API-driven service discovery, allow you to automatically get in-depth information about all of the databases in your organization.

In order to collect and store these, you will need to use Prometheus or a Prometheus-compatible metrics engine (such as VictoriaMetrics) that is capable of using the [HTTP SD](https://prometheus.io/docs/prometheus/latest/http_sd/) protocol.

## Prerequisites

This document assumes we'll be configuring a Prometheus 3.x instance via a configuration file running on our local machine.

If you are using managed Prometheus via AWS, GCP or another provider, you will have to deploy Prometheus to scrape and forward metrics via `remote_write`, as these services do not support scraping metrics.

## Getting Started

First, provision a new PlanetScale [Service token](/docs/api/reference/service-tokens) in your Organization settings. Make sure to save the ID and token, as they will not be visible after they've been generated.

When that's created, grant the token `read_metrics_endpoints` permissions and click "Save permissions". Your token should look like the following:

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metrics-service-token-configuration.png?fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=6788de4f7c33b53bae655708c4baff9f" alt="Service Token configuration for Metrics Exporting" data-og-width="1348" width="1348" data-og-height="1136" height="1136" data-path="docs/images/metrics-service-token-configuration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metrics-service-token-configuration.png?w=280&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=64c0aa40bda297dd71fcdc604c7593c8 280w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metrics-service-token-configuration.png?w=560&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=0f82feb485f8046096d6dc4c9fde8cde 560w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metrics-service-token-configuration.png?w=840&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=a507b57eef83b96e43ef16ad9c29afcd 840w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metrics-service-token-configuration.png?w=1100&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=2f04f5ebb7f7f148dc809654a8b192da 1100w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metrics-service-token-configuration.png?w=1650&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=aa009d73fa64ae6d3fd60d37ba0bd94c 1650w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metrics-service-token-configuration.png?w=2500&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=45f8237641306c452d6e3293fec320c1 2500w" />
</Frame>

## Configuring Prometheus

Now that we have a Service Token, we can add a scrape configuration for your PlanetScale organization. A minimal Prometheus configuration should look like the following:

```yaml  theme={null}
scrape_configs:
  - job_name: "${ORG}"
    http_sd_configs:
    - url: https://api.planetscale.com/v1/organizations/${ORG}/metrics
      authorization:
        type: "token"
        credentials: "${TOKEN_ID}:${TOKEN}"
      refresh_interval: 10m
```

Fill in your organization name in the `job_name` and `url`, and place the Service Token and ID that we created in the previous step for the credentials.

Save this file to `prometheus.yml` in your working directory.

## Start Prometheus

Run Prometheus pointed at this configuration file:

```bash  theme={null}
$ prometheus --config.file=prometheus.yml
```

By default, Prometheus will listen at `0.0.0.0:9090`, which means you can access it in your browser at [http://127.0.0.1:9090](http://127.0.0.1:9090).

### Validating Service Discovery

First, let's make sure that Prometheus is properly querying the PlanetScale API for the right branches. If you go to `http://127.0.0.1:9090/service-discovery` you should see the job that we created earlier, with all of your branches listed under `Discovered labels`. In this example, our organization is called `nick`, so it looks like the following:

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metrics-prometheus-targets.png?fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=eb5b15d46086cd686d2e3cdc27a81655" alt="Prometheus Target List" data-og-width="2886" width="2886" data-og-height="1456" height="1456" data-path="docs/images/metrics-prometheus-targets.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metrics-prometheus-targets.png?w=280&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=e6cb52a5d4cfccd6692995ee06e6c17d 280w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metrics-prometheus-targets.png?w=560&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=91f2153cfefce2e2517e04e47459e658 560w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metrics-prometheus-targets.png?w=840&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=4d22ffa22fa8569ff0fae3be6c848ab0 840w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metrics-prometheus-targets.png?w=1100&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=4e43bea221193dd4858ea72417cdd4b0 1100w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metrics-prometheus-targets.png?w=1650&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=3ea68d9b55697ad22d7dd93c4aa58190 1650w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metrics-prometheus-targets.png?w=2500&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=0fa878b0e86c25df0a3b99ea55d34ba4 2500w" />
</Frame>

Here, I have two branches that have been discovered. I can confirm that this matches what's in my organization:

```bash  theme={null}
$ pscale branch list test --org nick
  ID             NAME         PARENT BRANCH   REGION    PRODUCTION   SAFE MIGRATIONS   READY   CREATED AT    UPDATED AT
 -------------- ------------ --------------- --------- ------------ ----------------- ------- ------------- ---------------
  7wxuxewx4l0p   main         n/a             us-east   Yes          Yes               Yes     2 years ago   7 minutes ago
  6o0rr27785fl   partitions   main            us-east   No           No                Yes     1 month ago   9 minutes ago
```

Now, if I go to my list of targets I should see each branch as an Endpoint:

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metrics-prometheus-endpoints.png?fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=e0c332509b19a9bb2ed2b63f14e1020d" alt="Prometheus Endpoint List" data-og-width="2384" width="2384" data-og-height="660" height="660" data-path="docs/images/metrics-prometheus-endpoints.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metrics-prometheus-endpoints.png?w=280&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=ecde7c2e1f790d7eb6730781b3b07224 280w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metrics-prometheus-endpoints.png?w=560&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=c5886bea0a0f432f7ac971d6e1e8de2b 560w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metrics-prometheus-endpoints.png?w=840&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=408a725b71e31d934868b64a2919a8c7 840w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metrics-prometheus-endpoints.png?w=1100&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=88a517da96ac66ad8f2662d9dd1fb502 1100w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metrics-prometheus-endpoints.png?w=1650&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=cd421d5b722f15fa176793ec2f0143b9 1650w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metrics-prometheus-endpoints.png?w=2500&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=a0717a3d71c7bd84bafa55f801912964 2500w" />
</Frame>

This screenshot shows that they're being correctly scraped, and I can start to query my Prometheus instance.

## Querying Prometheus

Now that we're collecting metrics for my branches, our [reference guide](/docs/vitess/integrations/prometheus-metrics) has a list of everything that we export. If I want to see how many `vtgate` pods are running per AZ for my branch, I can query:

```
planetscale_vtgate_total_pods{planetscale_database_branch_id="7wxuxewx4l0p"}
```

Make sure the graph is set to stacked, and it should look like this:

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metrics-prometheus-querying.png?fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=bd02102ef5e2bbc4893da279353807cb" alt="Querying Prometheus for VTGate Count" data-og-width="2710" width="2710" data-og-height="2422" height="2422" data-path="docs/images/metrics-prometheus-querying.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metrics-prometheus-querying.png?w=280&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=150f556daa4de597267520394eadf38e 280w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metrics-prometheus-querying.png?w=560&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=f5e4451baa8d463ad094d56ca63e45bf 560w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metrics-prometheus-querying.png?w=840&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=532753037cda6f5f7dcc62ffe07e456e 840w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metrics-prometheus-querying.png?w=1100&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=e69c7becc71cd28b7403b518ad44df0d 1100w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metrics-prometheus-querying.png?w=1650&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=0be7dd37cb8970f9c3d16cef92f8ae77 1650w, https://mintcdn.com/planetscale-cad1a68a/iWRuaKlb_EL2Lj7R/docs/images/metrics-prometheus-querying.png?w=2500&fit=max&auto=format&n=iWRuaKlb_EL2Lj7R&q=85&s=ec9705a66b171b308f34f32c008836ff 2500w" />
</Frame>

## Next Steps

If you keep this Prometheus instance running, it will collect metrics every 30 seconds, and refresh the list of branches every 10 minutes.

For more information, see:

* [Metrics reference](/docs/vitess/integrations/prometheus-metrics) for a list of metrics we expose
* [Grafana and Prometheus](/docs/vitess/tutorials/prometheus-metrics-grafana) tutorial for using PlanetScale's provided dashboard to visualize these metrics in Grafana.
* [Sending metrics to New Relic](/docs/vitess/tutorials/prometheus-metrics-newrelic) tutorial for using Prometheus to forward metrics to New Relic.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt