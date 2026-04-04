# Source: https://keda.sh/docs/2.19/scalers/dynatrace/

Title: KEDA | Dynatrace

URL Source: https://keda.sh/docs/2.19/scalers/dynatrace/

Markdown Content:
Dynatrace Latest

Scale applications based on Dynatrace metric data points

### Trigger Specification [](https://keda.sh/docs/2.19/scalers/dynatrace/#trigger-specification)

This specification describes the `dynatrace` trigger that scales based on Dynatrace metric data points.

```
triggers:
  - type: dynatrace
    metadata:
      host: https://dummy-instance.live.dynatrace.com/
      threshold: "10"
      # Optional
      activationThreshold: "5"
      # Optional
      metricSelector: 'MyCustomEvent:filter(eq("someProperty","someValue")):count:splitBy("dt.entity.process_group"):fold'
      # Optional
      from: now-2d
      # Optional
      query: 'timeseries { r = max(`my-metric`, scalar: true) }, from:now()-2d'
      # Optional
      queryTimeoutSeconds: "10"
      # Optional
      queryPollingWait: "1s"
      # Optional
      queryPollingTries: "5"
```

**Parameter list:**

*   `host` - The Dynatrace instance to query against. (This value can be different when using `metricSelector` than when using `query`)

*   `metricSelector` - The metric selector query and any transformations that should be applied to it ([transformations docs](https://docs.dynatrace.com/docs/dynatrace-api/environment-api/metric-v2/metric-selector)). (Optional, Mutually exclusive with `query`)

Some relevant aspects:

    *   The selector should focus on a **single metric and dimension**: if multiple are found, a warning is issued and only the first one is considered
    *   The metric data points should be aggregated to produce a single output value (e.g., using the [fold transformation](https://docs.dynatrace.com/docs/shortlink/api-metrics-v2-selector#fold)): if multiple values are found, only the first one is considered
    *   If you need to use the entity selector, do it through the `:filter` transformation in the metric selector

*   `from` - How far back the metric selector should consider when fetching data points. [syntax supported](https://docs.dynatrace.com/docs/dynatrace-api/environment-api/metric-v2/get-data-points#parameters). (Optional, default `now-2h`, i.e., the last 2 hours, This only applies when `metricSelector` is used; with `query`, the time range must be included within the query)

*   `query` - [DQL](https://docs.dynatrace.com/docs/discover-dynatrace/platform/grail/dynatrace-query-language) query to be executed. (Optional, Mutually exclusive with `metricSelector`)

Some relevant aspects:

    *   Query must return a single scalar named `r` that KEDA will use as metric, other fields will be ignored.
    *   KEDA will poll 5 times the value with a second between tries, so the query needs to have a result within that window.

*   `queryTimeoutSeconds` - Timeout in seconds passed to fetch data on Dynatrace side (Default: `10`, Optional, Only applies with `query`)

*   `queryPollingWait` - Time between result polling tries (Default: `1s`, Optional, Only applies with `query`)

*   `queryPollingTries` - Total polling tries (Default: `5`, Optional, Only applies with `query`)

*   `threshold` - A threshold that is used as the `targetValue` or `targetAverageValue` (depending on the trigger metric type) in the HPA configuration. (This value can be a float)

*   `activationThreshold` - Target value for activating the scaler. Learn more about activation [here](https://keda.sh/docs/2.19/concepts/scaling-deployments/#activating-and-scaling-thresholds). (Optional, default `0`, can be a float)

> NOTE: Modifying the values of `queryPollingWait` or `queryPollingTries` can increase the response time and the HPA Controller can register timeouts because of this. If your query requires longer times, you should evaluate options like [caching metrics (`useCachedMetrics`)](https://keda.sh/docs/2.19/reference/scaledobject-spec/#triggers) in addition to these parameters.

### Authentication Parameters [](https://keda.sh/docs/2.19/scalers/dynatrace/#authentication-parameters)

You can use `TriggerAuthentication` CRD to configure authentication for the `host` and `token` parameters.

**Authentication:**

*   `host` - The Dynatrace instance to query against (This value can be different when using `metricSelector` than when using `query`)
*   `token` - The API key that will be leveraged to connect to Dynatrace and make requests. For `metricSelector`, token requires the `metrics.read` scope ([official documentation](https://docs.dynatrace.com/docs/dynatrace-api/basics/dynatrace-api-authentication)). For `query`, token **[has to be a platform token](https://docs.dynatrace.com/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens)** with enough permissions for the table that you want to use (OIDC client isn’t supported).

### Example [](https://keda.sh/docs/2.19/scalers/dynatrace/#example)

```
apiVersion: v1
kind: Secret
metadata:
  name: dynatrace-secret
  namespace: my-project
type: Opaque
data:
  host: aHR0cHM6Ly9kdW1teS1pbnN0YW5jZS5saXZlLmR5bmF0cmFjZS5jb20v # base64 encoding of https://dummy-instance.live.dynatrace.com/
  token: DYNATRACE_TOKEN_REDACTED # base64 encoding of the dynatrace example api key DYNATRACE_TOKEN_REDACTED.G3DFPBEJYMODIDAEX454M7YWBUVEFOWKPRVMWFASS64NFH52PX6BNDVFFM572RZM
---
apiVersion: keda.sh/v1alpha1
kind: TriggerAuthentication
metadata:
  name: keda-trigger-auth-dynatrace
  namespace: my-project
spec:
  secretTargetRef:
  - parameter: token
    name: dynatrace-secret
    key: token
  - parameter: host
    name: dynatrace-secret
    key: host
---
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: dynatrace-scaledobject
  namespace: keda
spec:
  maxReplicaCount: 12
  scaleTargetRef:
    name: dummy
  triggers:
    - type: dynatrace
      metadata:
        metricSelector: 'MyCustomEvent:filter(eq("someProperty","someValue")):count:splitBy("dt.entity.process_group"):fold'
        from: 'now-30m'
        threshold: '1000'
      authenticationRef:
        name: keda-trigger-auth-dynatrace
```

### DQL Example [](https://keda.sh/docs/2.19/scalers/dynatrace/#dql-example)

```
apiVersion: v1
kind: Secret
metadata:
  name: dynatrace-secret
  namespace: my-project
type: Opaque
data:
  host: aHR0cHM6Ly9kdW1teS1pbnN0YW5jZS5hcHBzLmR5bmF0cmFjZS5jb20v # base64 encoding of https://dummy-instance.apps.dynatrace.com/
  token: DYNATRACE_TOKEN_REDACTED # base64 encoding of the dynatrace example api key DYNATRACE_TOKEN_REDACTED.G3DFPBEJYMODIDAEX454M7YWBUVEFOWKPRVMWFASS64NFH52PX6BNDVFFM572RZM
---
apiVersion: keda.sh/v1alpha1
kind: TriggerAuthentication
metadata:
  name: keda-trigger-auth-dynatrace
  namespace: my-project
spec:
  secretTargetRef:
  - parameter: token
    name: dynatrace-secret
    key: token
  - parameter: host
    name: dynatrace-secret
    key: host
---
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: dynatrace-scaledobject
  namespace: keda
spec:
  maxReplicaCount: 12
  scaleTargetRef:
    name: dummy
  triggers:
    - type: dynatrace
      metadata:
        query: 'timeseries { r = max(`my-metric`, scalar: true) }, from:now()-30m'
        threshold: '1000'
      authenticationRef:
        name: keda-trigger-auth-dynatrace
```
