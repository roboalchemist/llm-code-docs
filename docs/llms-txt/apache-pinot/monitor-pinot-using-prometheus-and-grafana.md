# Source: https://docs.pinot.apache.org/release-0.9.0/operators/tutorials/monitor-pinot-using-prometheus-and-grafana.md

# Source: https://docs.pinot.apache.org/release-0.10.0/operators/tutorials/monitor-pinot-using-prometheus-and-grafana.md

# Source: https://docs.pinot.apache.org/release-0.11.0/operators/tutorials/monitor-pinot-using-prometheus-and-grafana.md

# Source: https://docs.pinot.apache.org/release-0.12.0/operators/tutorials/monitor-pinot-using-prometheus-and-grafana.md

# Source: https://docs.pinot.apache.org/release-0.12.1/operators/tutorials/monitor-pinot-using-prometheus-and-grafana.md

# Source: https://docs.pinot.apache.org/release-1.0.0/for-operators/tutorials/monitor-pinot-using-prometheus-and-grafana.md

# Source: https://docs.pinot.apache.org/release-1.1.0/for-operators/tutorials/monitor-pinot-using-prometheus-and-grafana.md

# Source: https://docs.pinot.apache.org/release-1.2.0/for-operators/tutorials/monitor-pinot-using-prometheus-and-grafana.md

# Source: https://docs.pinot.apache.org/release-1.3.0/for-operators/tutorials/monitor-pinot-using-prometheus-and-grafana.md

# Source: https://docs.pinot.apache.org/release-1.4.0/for-operators/tutorials/monitor-pinot-using-prometheus-and-grafana.md

# Source: https://docs.pinot.apache.org/operators/tutorials/monitor-pinot-using-prometheus-and-grafana.md

# Monitor Pinot using Prometheus and Grafana

Here we will introduce how to monitor Pinot with Prometheus and Grafana in Kubernetes environment.

## Prerequisite

* Kubernetes v1.16.5
* HelmCharts v3.1.2

## Deploy Pinot

### Install Pinot helm repo

```
## Adding Pinot helm repo
helm repo add pinot https://raw.githubusercontent.com/apache/pinot/master/helm
## Extract all the configurable values of Pinot Helm into a config.
helm inspect values pinot/pinot > /tmp/pinot-values.yaml
```

### Configure Pinot Helm to enable Prometheus JMX Exporter

1. Configure jvmOpts:

Add [JMX Prometheus Java Agent](https://github.com/prometheus/jmx_exporter) to `controller.jvmOpts` / `broker.jvmOpts`/ `server.jvmOpts` . Note that Pinot Docker image already packages `jmx_prometheus_javaagent.jar`.

Below config will expose pinot metrics to port 8008 for Prometheus to scrape.

```
controller:
  ...
  jvmOpts: "-javaagent:/opt/pinot/etc/jmx_prometheus_javaagent/jmx_prometheus_javaagent.jar=8008:/opt/pinot/etc/jmx_prometheus_javaagent/configs/pinot.yml -Xms256M -Xmx1G"
```

You can port forward port 8008 to local and access metrics though: <http://localhost:8008/metrics>

1. Configure service annotations:

Add Prometheus related annotations to enable Prometheus to scrape metrics.

* `controller.service.annotations`
* `broker.service.annotations`
* `server.service.annotations`
* `controller.podAnnotations`
* `broker.podAnnotations`
* `server.podAnnotations`

```
controller:
  ...
  service:
    annotations:
      "prometheus.io/scrape": "true"
      "prometheus.io/port": "8008"
  ...
  podAnnotations:
    "prometheus.io/scrape": "true"
    "prometheus.io/port": "8008"
```

### Deploy Pinot Helm

```
kubectl create ns pinot
helm install pinot pinot/pinot -n pinot --values /tmp/pinot-values.yaml
```

## Deploy Prometheus

Once Pinot is deployed and running, we can start deploy Prometheus.

Similar to Pinot Helm, we will have Prometheus Helm and its config yaml file:

```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm inspect values prometheus-community/prometheus > /tmp/prometheus-values.yaml
```

Configure Prometheus

Remember to check the configs:

* server.persistentVolume: data storage location/size limit/storage class
* server.retention: how long to keep the data (default is 15d)

Deploy Prometheus

```
kubectl create ns prometheus
helm install prometheus prometheus-community/prometheus -n prometheus --values /tmp/prometheus-values.yaml
```

Access Prometheus

Port forward Prometheus service to local and open the page on `localhost:30080`

```
kubectl port-forward service/prometheus-server 30080:80 -n prometheus
```

Then we can query metrics Prometheus scrapped:

![](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LtH6nl58DdnZnelPdTc%2F-MGp25S25RI4ZpgNTQi3%2F-MGp33o3rbsSe8lwVekc%2Fimage.png?alt=media\&token=188d1824-784d-47c2-b667-637825387f8a)

## Deploy Grafana

Similar to Pinot Helm, we will have Grafana Helm and it's config yaml file:

```
helm repo add grafana https://grafana.github.io/helm-charts
helm inspect values grafana/grafana > /tmp/grafana-values.yaml
```

* Configure Grafana
* Deploy Grafana

```
kubectl create ns grafana
helm install grafana grafana/grafana -n grafana --values /tmp/grafana-values.yaml
```

### Get password to access Grafana

```
kubectl get secret --namespace grafana grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
```

### Access Grafana dashboard

You can access it locally through port forwarding:

```
kubectl port-forward service/grafana 20080:80 -n grafana
```

Log in with your credentials.

`admin`/`[ PASSWORD GET FROM PREVIOUS STEP]`

### Add data source

Click on Prometheus and set HTTP URL to `http://prometheus-server.prometheus.svc.cluster.local`

![Prometheus data source config](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LtH6nl58DdnZnelPdTc%2F-MGoq_KwsY_BcKxZoUa-%2F-MGovrJvB9hS9cw1Ms87%2Fimage.png?alt=media\&token=08e63f5e-8a1b-47d8-9eca-a9f9c2041c14)

### Configure Pinot dashboard

Once data source is added, we can import a Pinot dashboard:

![Grafana Import Button](https://github.com/pinot-contrib/pinot-docs/blob/latest/.gitbook/assets/grafana-import-pinot-dashboard\).png)

A sample Pinot dashboard JSON is:

{% file src="<https://459170765-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LtH6nl58DdnZnelPdTc%2F-MINK2aYFvs1L8KHr2B-%2F-MINKFOVVHZxfP6_91WU%2FPinot-1601334866100.json?alt=media&token=39eb1419-3f29-43a7-a5c9-23b07538e4b6>" %}
sample-pinot-dashboard
{% endfile %}

Upload this file and select Prometheus as data source to finish the import:

![Grafana Import Page](https://github.com/pinot-contrib/pinot-docs/blob/latest/.gitbook/assets/grafana-import\).png)

Then you can explore and make your own Pinot dashboard.

![](https://459170765-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LtH6nl58DdnZnelPdTc%2F-MISwb3NVEPL4XdpjWxO%2F-MISwqdy1ofNMvbXp-wQ%2Fimage.png?alt=media\&token=25d80860-a0ce-407d-8061-627a37b7132e)
