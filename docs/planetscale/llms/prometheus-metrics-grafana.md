# Source: https://planetscale.com/docs/vitess/tutorials/prometheus-metrics-grafana.md

# Source: https://planetscale.com/docs/vitess/monitoring/prometheus-metrics-grafana.md

# Source: https://planetscale.com/docs/vitess/guides/prometheus-metrics-grafana.md

# Grafana Dashboard for PlanetScale Branches

> In this tutorial, you'll learn how to set up Grafana and connect it to a Prometheus instance to see metrics about your PlanetScale database.

## Introduction

This guide requires that you've set up a Prometheus instance from our documentation.

If you're already running Grafana in production and you're just looking for our standard dashboard template, you can find it [on GitHub](https://github.com/planetscale/grafana-dashboard).

## Install Grafana

Grafana's [installation documentation](https://grafana.com/docs/grafana/latest/setup-grafana/installation/) contains information for their supported platforms. For this guide, we'll be setting this up locally on a macOS machine.

If you're using a hosted Grafana option such as [Grafana Cloud](https://grafana.com/products/cloud/) or [AWS Managed Grafana](https://aws.amazon.com/grafana/) you can skip this step.

On macOS, Grafana is availabile via [homebrew](https://brew.sh/), and I can install it with:

```bash  theme={null}
$ brew install grafana
```

This will download and install Grafana, and I can start it with:

```bash  theme={null}
$ brew services start grafana
```

When that succeeds, I can go to `http://localhost:3000/` and I should see the Grafana welcome page:

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/metrics-grafana-welcome.png?fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=569ab1148e332bf9c8817988ff8ebea9" alt="Grafana Welcome Page" data-og-width="3008" width="3008" data-og-height="2326" height="2326" data-path="docs/vitess/tutorials/metrics-grafana-welcome.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/metrics-grafana-welcome.png?w=280&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=e0d475c9afa651fdf3ccc9f26422ce4b 280w, https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/metrics-grafana-welcome.png?w=560&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=a61e8cebd18725e1b7b3d9d8cbe8622c 560w, https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/metrics-grafana-welcome.png?w=840&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=1fb013d5340d8023da5389c25ce7096c 840w, https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/metrics-grafana-welcome.png?w=1100&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=8af773900d52f7d8d8ce88abde83e50d 1100w, https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/metrics-grafana-welcome.png?w=1650&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=ff9ac6e12979c3d37286c50f707ad258 1650w, https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/metrics-grafana-welcome.png?w=2500&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=2af627b979fe0f362c793eed6f9d61d5 2500w" />
</Frame>

The default username and password for a new install is `admin` and `admin`. Grafana will ask you to change the password the first time you log in, please pick something more secure than `admin`.

### Adding a Prometheus Endpoint

You can skip this step as well if you're already running a managed Prometheus or have added your datasource to Grafana already.

If you're running Prometheus locally, you'll need to add that as a datasource. To do this:

<Steps>
  <Step>
    Open the menu in the top left and click "Connections"
  </Step>

  <Step>
    Search for "Prometheus" and pick the plain "Prometheus" option
  </Step>

  <Step>
    Click "Add new data source" in the top right of the page
  </Step>
</Steps>

Now, you should look see a page that looks like this:

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/metrics-add-prometheus-connection.png?fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=5c6624bb11d3b92dcd327686426ebb0d" alt="Grafana Add Datasource" data-og-width="3024" width="3024" data-og-height="3010" height="3010" data-path="docs/vitess/tutorials/metrics-add-prometheus-connection.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/metrics-add-prometheus-connection.png?w=280&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=45864b735b894467268eecba79c38aac 280w, https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/metrics-add-prometheus-connection.png?w=560&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=4fd1bb03b34fba84acbef64779ff564e 560w, https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/metrics-add-prometheus-connection.png?w=840&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=ee754e8a82184144b5df8439522cf404 840w, https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/metrics-add-prometheus-connection.png?w=1100&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=cb50a1ba2da6ce96cbea57bd32fe066d 1100w, https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/metrics-add-prometheus-connection.png?w=1650&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=72f59be560278c017ffda052ad3f12a0 1650w, https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/metrics-add-prometheus-connection.png?w=2500&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=27fadd371e63ddf51c10b29ec9fa1b5a 2500w" />
</Frame>

You can call this whatever you want, we'll use the following:

* Name: "PlanetScale"
* Prometheus server URL: `http://localhost:9090/`

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/metrics-prometheus-configuration.png?fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=2d4dd7f8dbef421801fcebcbbb03055b" alt="Grafana Prometheus Configuration" data-og-width="2936" width="2936" data-og-height="2922" height="2922" data-path="docs/vitess/tutorials/metrics-prometheus-configuration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/metrics-prometheus-configuration.png?w=280&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=82ce937c41081ec21e76c79774373054 280w, https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/metrics-prometheus-configuration.png?w=560&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=d782a494cfea2b0973e5c678f9df2b0d 560w, https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/metrics-prometheus-configuration.png?w=840&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=335befdb3d314dcd710d5d8d0197ead6 840w, https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/metrics-prometheus-configuration.png?w=1100&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=d40ea531005719f722d5a7163f98ec54 1100w, https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/metrics-prometheus-configuration.png?w=1650&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=ba8bd36ea388996be473fc20257a7f89 1650w, https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/metrics-prometheus-configuration.png?w=2500&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=0b6c7d8940c745fe3b4537bef8af8a1a 2500w" />
</Frame>

Because this is running on your local machine, we do not need to use any Authentication or TLS

Scroll down to the "Interval behaviour" section and set the "Scrape interval" to `1m`.

Finally, scroll to the bottom and click "Save & test".

## Import the PlanetScale Dashboard

Now that we have our datasource added, let's import the PlanetScale Dashboard. This is a starter dashboard that PlanetScale has produced which shows an overview of your branch with the metrics that we expose.

From the Grafana homepage, go to the top left menu and pick "Dashboards".

In the top right, click "New" and then Import":

PlanetScale maintains the latest version of the dashboard located here:

[https://github.com/planetscale/grafana-dashboard/blob/main/overview.json](https://github.com/planetscale/grafana-dashboard/blob/main/overview.json)

Download this file to your computer, and then click "Upload dashboard JSON file".

Find the JSON file you downloaded in the previous step, and configure it with the Prometheus datasource that we added in an earlier:

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/metrics-prometheus-configuration.png?fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=2d4dd7f8dbef421801fcebcbbb03055b" alt="Grafana Prometheus Configuration" data-og-width="2936" width="2936" data-og-height="2922" height="2922" data-path="docs/vitess/tutorials/metrics-prometheus-configuration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/metrics-prometheus-configuration.png?w=280&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=82ce937c41081ec21e76c79774373054 280w, https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/metrics-prometheus-configuration.png?w=560&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=d782a494cfea2b0973e5c678f9df2b0d 560w, https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/metrics-prometheus-configuration.png?w=840&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=335befdb3d314dcd710d5d8d0197ead6 840w, https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/metrics-prometheus-configuration.png?w=1100&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=d40ea531005719f722d5a7163f98ec54 1100w, https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/metrics-prometheus-configuration.png?w=1650&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=ba8bd36ea388996be473fc20257a7f89 1650w, https://mintcdn.com/planetscale-cad1a68a/PORMOvRUq48-lind/docs/vitess/tutorials/metrics-prometheus-configuration.png?w=2500&fit=max&auto=format&n=PORMOvRUq48-lind&q=85&s=0b6c7d8940c745fe3b4537bef8af8a1a 2500w" />
</Frame>

Click 'Import' and you should be directed to the dashboard, configured to query your local Prometheus with the data it's been scraping!

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt