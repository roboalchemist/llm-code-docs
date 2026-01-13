# Source: https://docs.datadoghq.com/containers/datadog_operator/crd_monitor.md

---
title: DatadogMonitor CRD
description: >-
  Deploy and manage Datadog monitors using the DatadogMonitor custom resource
  definition with the Datadog Operator
breadcrumbs: Docs > Container Monitoring > Datadog Operator > DatadogMonitor CRD
source_url: https://docs.datadoghq.com/datadog_operator/crd_monitor/index.html
---

# DatadogMonitor CRD

To deploy a Datadog monitor, you can use the Datadog Operator and `DatadogMonitor` custom resource definition (CRD).

## Prerequisites{% #prerequisites %}

- [Helm](https://helm.sh/)
- [`kubectl` CLI](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [Datadog Operator](https://docs.datadoghq.com/containers/kubernetes/installation?tab=datadogoperator#installation) v0.6+

## Setup{% #setup %}

1. Create a file with the spec of your `DatadogMonitor` deployment configuration.

**Example**:

The following spec creates a [metric monitor](https://docs.datadoghq.com/monitors/types/metric/?tab=threshold) that alerts on the query `avg(last_10m):avg:system.disk.in_use{*} by {host} > 0.5`.

In the `datadog-metric-monitor.yaml` file:

   ```yaml
      apiVersion: datadoghq.com/v1alpha1
      kind: DatadogMonitor
      metadata:
        name: datadog-monitor-test
        namespace: datadog
      spec:
        query: "avg(last_10m):avg:system.disk.in_use{*} by {host} > 0.5"
        type: "metric alert"
        name: "Test monitor made from DatadogMonitor"
        message: "1-2-3 testing"
        tags:
          - "test:datadog"
        priority: 5
        controllerOptions:
          disableRequiredTags: false
        options:
          evaluationDelay: 300
          includeTags: true
          locked: false
          newGroupDelay: 300
          notifyNoData: true
          noDataTimeframe: 30
          renotifyInterval: 1440
          thresholds:
            critical: "0.5"
            warning: "0.28"
      
```

See the complete list of configuration fields.

1. Deploy your `DatadogMonitor`:

   ```shell
   kubectl apply -f /path/to/your/datadog-metric-monitor.yaml
   ```

## Additional examples{% #additional-examples %}

### Metric monitors{% #metric-monitors %}

- [A pod is in CrashLoopBackOff](https://github.com/DataDog/datadog-operator/blob/main/examples/datadogmonitor/metric-monitor-crashloopbackoff.yaml)
- [A pod is in ImagePullBackOff](https://github.com/DataDog/datadog-operator/blob/main/examples/datadogmonitor/metric-monitor-imagepullbackoff.yaml)
- [More than one deployment replica's pods are down](https://github.com/DataDog/datadog-operator/blob/main/examples/datadogmonitor/metric-monitor-deployment-replicas.yaml)
- [More than one StatefulSet replica's pods are down](https://github.com/DataDog/datadog-operator/blob/main/examples/datadogmonitor/metric-monitor-statefulset-replicas.yaml)
- [More than 20% of nodes on a cluster are unschedulable](https://github.com/DataDog/datadog-operator/blob/main/examples/datadogmonitor/metric-monitor-nodes-unavailable.yaml)
- [More than 10 pods are failing in a cluster](https://github.com/DataDog/datadog-operator/blob/main/examples/datadogmonitor/metric-monitor-pods-failed-state.yaml)
- [Pods are restarting multiple times in the last five minutes](https://github.com/DataDog/datadog-operator/blob/main/examples/datadogmonitor/metric-monitor-pods-restarting.yaml)

### Other monitors{% #other-monitors %}

- [Audit monitor](https://github.com/DataDog/datadog-operator/blob/main/examples/datadogmonitor/audit-alert-monitor-test.yaml)
- [Event monitor](https://github.com/DataDog/datadog-operator/blob/main/examples/datadogmonitor/event-alert-monitor-test.yaml)
- [Event V2 monitor](https://github.com/DataDog/datadog-operator/blob/main/examples/datadogmonitor/event-v2-alert-monitor-test.yaml)
- [Log monitor](https://github.com/DataDog/datadog-operator/blob/main/examples/datadogmonitor/log-alert-monitor-test.yaml)
- [Process monitor](https://github.com/DataDog/datadog-operator/blob/main/examples/datadogmonitor/process-alert-monitor-test.yaml)
- [RUM monitor](https://github.com/DataDog/datadog-operator/blob/main/examples/datadogmonitor/rum-alert-monitor-test.yaml)
- [Service check monitor](https://github.com/DataDog/datadog-operator/blob/main/examples/datadogmonitor/service-check-monitor-test.yaml)
- [SLO monitor](https://github.com/DataDog/datadog-operator/blob/main/examples/datadogmonitor/slo-alert-monitor-test.yaml)
- [Trace analytics monitor](https://github.com/DataDog/datadog-operator/blob/main/examples/datadogmonitor/trace-analytics-alert-monitor-test.yaml)

## All available configuration fields{% #all-available-configuration-fields %}

The following table lists all available configuration fields for the `DatadogMonitor` custom resource.

{% dl %}

{% dt %}
`message`
{% /dt %}

{% dd %}
**required** - *string*A message to include with notifications for this monitor.
{% /dd %}

{% dt %}
`name`
{% /dt %}

{% dd %}
**required** - *string*The monitor name.
{% /dd %}

{% dt %}
`query`
{% /dt %}

{% dd %}
**required** - *string*The monitor query.
{% /dd %}

{% dt %}
`type`
{% /dt %}

{% dd %}
**required** - *enum*The type of the monitor.Allowed enum values: `metric alert`, `query alert`, `service check`, `event alert`, `log alert`, `process alert`, `rum alert`, `trace-analytics alert`, `slo alert`, `event-v2 alert`, `audit alert`, `composite`
{% /dd %}

{% dt %}
`controllerOptions.disableRequiredTags`
{% /dt %}

{% dd %}
*boolean*Disables the automatic addition of required tags to monitors.
{% /dd %}

{% dt %}
`priority`
{% /dt %}

{% dd %}
*int64*An integer from 1 (high) to 5 (low) indicating alert severity.
{% /dd %}

{% dt %}
`restrictedRoles`
{% /dt %}

{% dd %}
*[string]*A list of unique role identifiers to define which roles are allowed to edit the monitor. The unique identifiers for all roles can be pulled from the [Roles API](https://docs.datadoghq.com/api/latest/roles/#list-roles) and are located in the `data.id` field.
{% /dd %}

{% dt %}
`tags`
{% /dt %}

{% dd %}
*[string]*Tags associated to your monitor.
{% /dd %}

{% dt %}
`options`
{% /dt %}

{% dd %}
*object*List of options associated with your monitor. See Options.
{% /dd %}

{% /dl %}

### Options{% #options %}

The following fields are set in the `options` property.

For example:

```yaml
apiVersion: datadoghq.com/v1alpha1
kind: DatadogMonitor
metadata:
  name: datadog-monitor-test
  namespace: datadog
spec:
  query: "avg(last_10m):avg:system.disk.in_use{*} by {host} > 0.5"
  type: "metric alert"
  name: "Test monitor made from DatadogMonitor"
  message: "1-2-3 testing"
  options:
    enableLogsSample: true
    thresholds:
      critical: "0.5"
      warning: "0.28"
```

{% dl %}

{% dt %}
`enableLogsSample`
{% /dt %}

{% dd %}
*boolean*Whether or not to send a log sample when the log monitor triggers.
{% /dd %}

{% dt %}
`escalationMessage`
{% /dt %}

{% dd %}
*string*A message to include with a re-notification.
{% /dd %}

{% dt %}
`evaluationDelay`
{% /dt %}

{% dd %}
*int64*Time (in seconds) to delay evaluation, as a non-negative integer. For example: if the value is set to 300 (5min), the timeframe is set to `last_5m`, and the time is 7:00, then the monitor evaluates data from 6:50 to 6:55. This is useful for AWS CloudWatch and other backfilled metrics to ensure the monitor always has data during evaluation.
{% /dd %}

{% dt %}
`groupRetentionDuration`
{% /dt %}

{% dd %}
*string*The time span after which groups with missing data are dropped from the monitor state. The minimum value is one hour, and the maximum value is 72 hours. Example values are: `60m`, `1h`, and `2d`. This option is only available for APM Trace Analytics, Audit Trail, CI, Error Tracking, Event, Logs, and RUM monitors.
{% /dd %}

{% dt %}
`groupbySimpleMonitor`
{% /dt %}

{% dd %}
*boolean*DEPRECATED: Whether the log alert monitor triggers a single alert or multiple alerts when any group breaches a threshold. Use `notifyBy` instead.
{% /dd %}

{% dt %}
`includeTags`
{% /dt %}

{% dd %}
*boolean*A Boolean indicating whether notifications from this monitor automatically inserts its triggering tags into the title.
{% /dd %}

{% dt %}
`locked`
{% /dt %}

{% dd %}
*boolean*DEPRECATED: Whether or not the monitor is locked (only editable by creator and admins). Use `restrictedRoles` instead.
{% /dd %}

{% dt %}
`newGroupDelay`
{% /dt %}

{% dd %}
*int64*Time (in seconds) to allow a host to boot and applications to fully start before starting the evaluation of monitor results. Should be a non-negative integer.
{% /dd %}

{% dt %}
`noDataTimeframe`
{% /dt %}

{% dd %}
*int64*The number of minutes before a monitor notifies after data stops reporting. Datadog recommends at least 2x the monitor timeframe for metric alerts or 2 minutes for service checks. If omitted, 2x the evaluation timeframe is used for metric alerts, and 24 hours is used for service checks.
{% /dd %}

{% dt %}
`notificationPresetName`
{% /dt %}

{% dd %}
*enum*Toggles the display of additional content sent in the monitor notification.Allowed enum values: `show_all`, `hide_query`, `hide_handles`, `hide_all`Default: `show_all`
{% /dd %}

{% dt %}
`notifyAudit`
{% /dt %}

{% dd %}
*boolean*A Boolean indicating whether tagged users are notified on changes to this monitor.
{% /dd %}

{% dt %}
`notifyBy`
{% /dt %}

{% dd %}
*[string]*A string indicating the granularity a monitor alerts on. Only available for monitors with groupings. For example, if you have a monitor grouped by cluster, namespace, and pod, and you set `notifyBy` to `["cluster"]`, then your monitor only notifies on each new cluster violating the alert conditions.Tags mentioned in `notifyBy` must be a subset of the grouping tags in the query. For example, a query grouped by cluster and namespace cannot notify on region.Setting `notifyBy` to `[*]` configures the monitor to notify as a simple-alert.
{% /dd %}

{% dt %}
`notifyNoData`
{% /dt %}

{% dd %}
*boolean*A Boolean indicating whether this monitor notifies when data stops reporting.Default: `false`.
{% /dd %}

{% dt %}
`onMissingData`
{% /dt %}

{% dd %}
*enum*Controls how groups or monitors are treated if an evaluation does not return any data points. The default option results in different behavior depending on the monitor query type. For monitors using Count queries, an empty monitor evaluation is treated as 0 and is compared to the threshold conditions. For monitors using any query type other than Count, for example Gauge, Measure, or Rate, the monitor shows the last known status. This option is only available for APM Trace Analytics, Audit Trail, CI, Error Tracking, Event, Logs, and RUM monitors.Allowed enum values: `default`, `show_no_data`, `show_and_notify_no_data`, `resolve`
{% /dd %}

{% dt %}
`renotifyInterval`
{% /dt %}

{% dd %}
*int64*The number of minutes after the last notification before a monitor re-notifies on the current status. It only re-notifies if it's not resolved.
{% /dd %}

{% dt %}
`renotifyOccurrences`
{% /dt %}

{% dd %}
*int64*The number of times re-notification messages should be sent on the current status at the provided re-notification interval.
{% /dd %}

{% dt %}
`renotifyStatuses`
{% /dt %}

{% dd %}
*[string]*The types of monitor statuses for which re-notification messages are sent.If `renotifyInterval` is null, defaults to null.If `renotifyInterval` is not null, defaults to `["Alert", "No Data"]`Values for monitor status: `Alert`, `No Data`, `Warn`
{% /dd %}

{% dt %}
`requireFullWindow`
{% /dt %}

{% dd %}
*boolean*A Boolean indicating whether this monitor needs a full window of data before it's evaluated. Datadog highly recommends you set this to `false` for sparse metrics, otherwise some evaluations are skipped.Default: `false`.
{% /dd %}

{% dt %}
`schedulingOptions`
{% /dt %}

{% dd %}
*object*Configuration options for scheduling:
{% dl %}

{% dt %}
`customSchedule`
{% /dt %}

{% dd %}
*object*Configuration options for the custom schedule:
{% dl %}

{% dt %}
`recurrence`
{% /dt %}

{% dd %}
*[object]*Array of custom schedule recurrences.
{% dl %}

{% dt %}
`rrule`
{% /dt %}

{% dd %}
*string*The recurrence rule in iCalendar format. For example, `FREQ=MONTHLY;BYMONTHDAY=28,29,30,31;BYSETPOS=-1`.
{% /dd %}

{% dt %}
`start`
{% /dt %}

{% dd %}
*string*The start date of the recurrence rule defined in `YYYY-MM-DDThh:mm:ss` format. If omitted, the monitor creation time is used.
{% /dd %}

{% dt %}
`timezone`
{% /dt %}

{% dd %}
*string*The timezone in `tz database` format, in which the recurrence rule is defined. For example, `America/New_York` or `UTC`.
{% /dd %}

{% /dl %}

{% /dd %}

{% /dl %}

{% /dd %}

{% dt %}
`evaluationWindow`
{% /dt %}

{% dd %}
*object*Configuration options for the evaluation window. If `hour_starts` is set, no other fields may be set. Otherwise, `day_starts` and `month_starts` must be set together.
{% dl %}

{% dt %}
`dayStarts`
{% /dt %}

{% dd %}
*string*The time of the day at which a one day cumulative evaluation window starts. Must be defined in UTC time in `HH:mm`format.
{% /dd %}

{% dt %}
`hourStarts`
{% /dt %}

{% dd %}
*integer*The minute of the hour at which a one hour cumulative evaluation window starts.
{% /dd %}

{% dt %}
`monthStarts`
{% /dt %}

{% dd %}
*integer*The day of the month at which a one month cumulative evaluation window starts.
{% /dd %}

{% /dl %}

{% /dd %}

{% /dl %}

{% /dd %}

{% dt %}
`thresholdWindows`
{% /dt %}

{% dd %}
*object*Alerting time window options:
{% dl %}

{% dt %}
`recoveryWindow`
{% /dt %}

{% dd %}
*string*Describes how long an anomalous metric must be normal before the alert recovers.
{% /dd %}

{% dt %}
`triggerWindow`
{% /dt %}

{% dd %}
*string*Describes how long a metric must be anomalous before an alert triggers.
{% /dd %}

{% /dl %}

{% /dd %}

{% dt %}
`thresholds`
{% /dt %}

{% dd %}
*object*List of the different monitor thresholds available:
{% dl %}

{% dt %}
`critical`
{% /dt %}

{% dd %}
*string*The monitor CRITICAL threshold.
{% /dd %}

{% dt %}
`criticalRecovery`
{% /dt %}

{% dd %}
*string*The monitor CRITICAL recovery threshold.
{% /dd %}

{% dt %}
`ok`
{% /dt %}

{% dd %}
*string*The monitor OK threshold.
{% /dd %}

{% dt %}
`unknown`
{% /dt %}

{% dd %}
*string*The monitor UNKNOWN threshold.
{% /dd %}

{% dt %}
`warning`
{% /dt %}

{% dd %}
*string*The monitor WARNING threshold.
{% /dd %}

{% dt %}
`warningRecovery`
{% /dt %}

{% dd %}
*string*The monitor WARNING recovery threshold.
{% /dd %}

{% /dl %}

{% /dd %}

{% dt %}
`timeoutH`
{% /dt %}

{% dd %}
*int64*The number of hours of the monitor not reporting data before it automatically resolves from a triggered state.
{% /dd %}

{% /dl %}

## Further reading{% #further-reading %}

- [API Reference: Create a Datadog monitor](https://docs.datadoghq.com/api/latest/monitors/#create-a-monitor)
- [DatadogMonitor CRD](https://github.com/DataDog/helm-charts/blob/main/crds/datadoghq.com_datadogmonitors.yaml)
