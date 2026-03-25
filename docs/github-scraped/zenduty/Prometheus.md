---
id: Prometheus
title: Prometheus
---
Prometheus is an open-source monitoring solution that resides locally on your machine. To integrate Prometheus with Zenduty, complete the following steps:

## In Zenduty

1. To add a new Prometheus integration, go to "Teams" on Zenduty and click on the "Manage" button corresponding to the team you want to add the integration to.

2. Next, go to "Services" and click on the "Manage" button corresponding to the relevant Service.

3. Go to "Integrations" and then "Add New Integration". Give it a name and select the application "Prometheus" from the dropdown menu.

4. Go to "Configure" under your integrations and copy the webhooks URL generated.

## In Prometheus

1. Ensure that both Prometheus and Prometheus Alertmanager are downloaded and accessible locally on your system. To download them, visit [here](https://prometheus.io/download/)

2. Go to Alertmanager Folder and open "alertmanager.yml". Add the webhook url (copied in the earlier steps) under "Webhook Configs".
  Your "alertmanager.yml" file should now look like this:
  
  ```
  global:
    resolve_timeout: 5m
  route:
    group_by: ['alertname', 'cluster', 'service']
    group_wait: 30s
    group_interval: 5m
    repeat_interval: 3h
    receiver: 'web.hook'
  receivers:
  - name: 'web.hook'
    webhook_configs:
    - url: 'https://zenduty.com/api/integration/prometheus/8a02aa3b-4289-4360-9ad4-f31f40aea5ed/'
  inhibit_rules:
    - source_match:
        severity: 'critical'
      target_match:
        severity: 'warning'
      equal: ['alertname', 'dev', 'instance']
  ```

3. Make your "Alert Rules" in a file titled as "first_rules.yml", "second_rules.yml", and so on.

4. In the Prometheus folder, open "prometheus.yml". Add new rules files that you just created and set Target.
 Your "prometheus.yml" file should look like this:
 
  ```
  # my global config
  global:
    scrape_interval:     15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
    evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.
    # scrape_timeout is set to the global default (10s).
  # Alertmanager configuration
  alerting:
    alertmanagers:
    - static_configs:
      - targets: ["localhost:9093"]
  # Load rules once and periodically evaluate them according to the global 'evaluation_interval'.
  rule_files:
    - "first_rules.yml"
    # - "second_rules.yml"
  # A scrape configuration containing exactly one endpoint to scrape:
  # Here it's Prometheus itself.
  scrape_configs:
    # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
    - job_name: 'prometheus'
      # metrics_path defaults to '/metrics'
      # scheme defaults to 'http'.
      static_configs:
      - targets: ['localhost:9090']
  ```

5. Run Prometheus and Alert Manager using commands like:

 `run prometheus: ./prometheus --config.file=prometheus.yml`

 `run alertmanager: ./alertmanager --config.file=alertmanager.yml`

6. Once Prometheus is running, you will be able to see the alerts rules you configured.

![](/img/Integrations/Prometheus/alerts.png)

When an alert is required, Zenduty will automatically create an incident.

![](/img/Integrations/Prometheus/incident.png)

1. Prometheus is now integrated.
