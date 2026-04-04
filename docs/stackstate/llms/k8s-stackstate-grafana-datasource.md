# Source: https://archivedocs.stackstate.com/metrics/advanced-metrics/k8s-stackstate-grafana-datasource.md

# Grafana Datasource

StackState can be used as a datasource for Grafana. This will allow to use Grafana as a visualization tool for your StackState data. This is useful if you already have some dashboards which you want to keep using. Because StackState exposes a Prometheus-compatible API, you can use the [Prometheus datasource](https://grafana.com/docs/grafana/latest/datasources/prometheus) in Grafana to connect to StackState. This also makes StackState usable with other Prometheus-compatible solutions.

## Prerequisites

Before you can add StackState as a datasource in Grafana, you need to setup a ServiceToken to authenticate with StackState. StackState recommends to create a dedicated role with permissions for this purpose.

You can do this via the StackState CLI:

```sh
> sts rbac create-subject --subject grafana
✅ Created subject 'grafana'
> sts rbac grant --subject grafana --permission read-metrics
✅ Granted permission 'read-metrics' on 'system' to subject 'grafana'
PERMISSION   | RESOURCE
read-metrics | system
```

This will create a new role in StackState called `grafana` and grant it the `read-metrics` permission. You can then create a ServiceToken for this role:

```sh
> sts service-token create --name grafana --roles grafana
✅ Service token created: svctok-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

Learn more about [managing ServiceTokens](https://archivedocs.stackstate.com/security/k8s-service-tokens).

The returned ServiceToken can be used to authenticate with StackState. You can now add StackState as a datasource in Grafana.

## Create a new StackState datasource in Grafana

With the created ServiceToken, you can now add StackState as a datasource in Grafana. To do this, go to the Grafana UI and navigate to the datasource configuration page. Click on the `Add data source` button and select `Prometheus` from the list of datasources.

![Grafana new datasource](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-c57861c57cc8b7349f4fe59222ddd54fbc392c46%2Fk8s-grafana-new-datasource.png?alt=media)

On the datasource configuration page, enter the following configuration details:

* **Name**: StackState
* **URL**: `https://<tenant-name>.app.stackstate.io/prometheus`
* **Custom HTTP Headers**
  * **Header**: `X-API-Key`
  * **Value**: `<service-token>`

![Grafana datasource configuration](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-fff332231a7accb534fc950f830159fb4cdc39b2%2Fk8s-grafana-datasource.png?alt=media)

Click on the `Save & Test` button to save the datasource. If the configuration is correct, you should see a green `Data source is working` message.
