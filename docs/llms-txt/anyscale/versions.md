# Source: https://docs.anyscale.com/services/versions.md

# Deploy multiple versions of an Anyscale service

[View Markdown](/services/versions.md)

# Deploy multiple versions of an Anyscale service

Deploy and manage multiple versions of an Anyscale service behind a single endpoint to run A/B experiments or control the rollout of new models and configurations.

important

This feature is in beta release for Anyscale clouds backed by virtual machines (VMs) on AWS. See [Beta limitations and considerations](#beta-limitations) for current limitations.

## What are multi-version services?[​](#what-are-multi-version-services "Direct link to What are multi-version services?")

Multi-version services allow you to deploy up to 10 versions of a service behind a single endpoint. Each version runs on its own cluster with independent autoscaling, and you control how traffic distributes across versions using percentage weights.

The following are examples of patterns supported by multi-version services:

* A/B testing between different models or application configurations.
* Gradual rollouts with more than two versions active simultaneously.
* Shadowing traffic to new versions for validation.
* Canary testing at scale with fine-grained traffic control.

## How multi-version services work[​](#how-multi-version-services-work "Direct link to How multi-version services work")

When you deploy a multi-version service, Anyscale does the following:

* Creates a shared endpoint that distributes traffic across all active versions.
* Deploys each version to its own Ray cluster.
* Scales each version independently based on its service configuration.
* Tags logs and metrics with version names for easy filtering and comparison.

You specify traffic percentages for each version, and these percentages must sum to 100. Anyscale automatically distributes incoming requests according to these weights.

## Version management concepts[​](#version-management-concepts "Direct link to Version management concepts")

You can deploy up to 10 versions to a service. You specify version names in your service configuration and use these version names to specify traffic allocation and interact with individual versions.

### Version names[​](#version-names "Direct link to Version names")

Each version requires a unique name within the service. Anyscale recommends specifying version names in your service configuration for easier management and tracking.

If you don't specify a version name, Anyscale generates one using the format `v-{10 random alphanumeric characters}`.

note

You can't edit the version name for a deployed version. To use custom version names, you must specify a name using the `version_name` field in your service config while deploying your service.

### Traffic allocation[​](#traffic-allocation "Direct link to Traffic allocation")

Traffic allocation controls what percentage of requests each version receives. You specify traffic percentages using the `--versions` parameter when deploying or updating a service.

The following rules apply to traffic allocation:

* All traffic percentages must sum to exactly 100.
* Each version must have a traffic percentage greater than 0.
* You can adjust traffic percentages without redeploying service configurations.

When you adjust traffic allocation, the service state shows `UPDATING` while Anyscale reallocates traffic and scales clusters.

## Create a new service with multiple versions[​](#create-multi-version "Direct link to Create a new service with multiple versions")

To create a new service with multiple versions, provide a service configuration file for each version and specify traffic percentages using the `--versions` parameter.

Each service configuration must include the following:

* A `version_name` field with a unique name for the version.
* The same `name` value across all configurations, which specifies the service name.
* The same `cloud` and `project` values across all configurations.

The following example creates a service with three versions:

* CLI
* SDK

```
anyscale service deploy \
  --versions '[{"name":"v1","traffic_percent":30}, {"name":"v2","traffic_percent":30}, {"name":"v3","traffic_percent":40}]' \
  -f config_v1.yaml \
  -f config_v2.yaml \
  -f config_v3.yaml
```

```
import anyscale
from anyscale.service.models import ServiceConfig

configs = [
    ServiceConfig.from_yaml("config_v1.yaml"),
    ServiceConfig.from_yaml("config_v2.yaml"),
    ServiceConfig.from_yaml("config_v3.yaml")
]

anyscale.service.deploy(
    configs,
    versions='[{"name":"v1","traffic_percent":30}, {"name":"v2","traffic_percent":30}, {"name":"v3","traffic_percent":40}]'
)
```

The following shows an example service configuration file for version `v1`:

```
name: test_service
version_name: v1
working_dir: .
applications:
  - import_path: main:my_app
    deployments:
      - name: Model
        autoscaling_config:
          target_ongoing_requests: 2
          min_replicas: 1
          max_replicas: 1
          downscale_delay_s: 10
          metrics_interval_s: 10
          look_back_period_s: 10
```

Each version can have different autoscaling configurations or application settings. The `version_name` field identifies the version in the `--versions` parameter.

## Add a new version to an existing service[​](#add-version "Direct link to Add a new version to an existing service")

To add a new version to an existing service, provide a configuration file only for the new version. Existing versions maintain their current configurations.

The following example adds version `v3` to a service with two existing versions and adjusts traffic across all three versions:

* CLI
* SDK

```
anyscale service deploy \
  --versions '[{"name":"v1","traffic_percent":10}, {"name":"v2","traffic_percent":60}, {"name":"v3","traffic_percent":30}]' \
  -f config_v3.yaml
```

```
import anyscale
from anyscale.service.models import ServiceConfig

config_v3 = ServiceConfig.from_yaml("config_v3.yaml")

anyscale.service.deploy(
    [config_v3],
    versions='[{"name":"v1","traffic_percent":10}, {"name":"v2","traffic_percent":60}, {"name":"v3","traffic_percent":30}]'
)
```

Anyscale deploys the new version and reallocates traffic according to the specified percentages.

### Adjust traffic between versions[​](#adjust-traffic "Direct link to Adjust traffic between versions")

To adjust traffic percentages between existing versions without changing service configurations, use the `--versions` parameter without providing configuration files.

The following example adjusts traffic across three existing versions:

* CLI
* SDK

```
anyscale service deploy \
  --versions '[{"name":"v1","traffic_percent":30}, {"name":"v2","traffic_percent":20}, {"name":"v3","traffic_percent":50}]'
```

```
import anyscale

anyscale.service.deploy(
    [],
    versions='[{"name":"v1","traffic_percent":30}, {"name":"v2","traffic_percent":20}, {"name":"v3","traffic_percent":50}]',
    name="test_service"
)
```

The service state shows `UPDATING` while Anyscale reallocates traffic and scales clusters to match the new percentages.

## Remove a version[​](#remove-version "Direct link to Remove a version")

To remove versions from a service, omit them from the `--versions` parameter. Anyscale terminates any versions not included in the parameter.

The following example removes versions `v2` by specifying only `v1` and `v3`:

* CLI
* SDK

```
anyscale service deploy \
  --versions '[{"name":"v1","traffic_percent":50},{"name":"v3","traffic_percent":50}]'
```

```
import anyscale

anyscale.service.deploy(
    [],
    versions='[{"name":"v1","traffic_percent":50},{"name":"v3","traffic_percent":50}]',
    name="test_service"
)
```

Anyscale terminates the omitted versions after reallocating traffic to the remaining versions.

## Query a multi-version service[​](#query "Direct link to Query a multi-version service")

By default, the service endpoint distributes traffic across all versions according to their traffic percentages. You can also send requests to a specific version for testing or debugging.

To query a specific version, add the `X-ANYSCALE-VERSION` header to your request. The following example queries version `v1` of the target service:

```
curl -H "Authorization: Bearer <auth-token>" \
  -H "X-ANYSCALE-VERSION: v1" \
  "https://your-service.anyscale.com/"
```

To allow the service to distribute traffic normally, omit the query parameter:

```
curl -H "Authorization: Bearer <auth-token>" \
  "https://your-service.anyscale.com/"
```

## View service status[​](#service-status "Direct link to View service status")

Use the `anyscale service status` command to view the state of a multi-version service and its versions.

* CLI
* SDK

```
anyscale service status -n test_service
```

```
import anyscale

status = anyscale.service.status(name="test_service")
print(status.to_dict())
```

The status output includes the following information for each version:

* Version ID, which shows the version name you specified.
* Current state, such as `RUNNING` or `UPDATING`.
* Traffic weight percentage.
* Creation timestamp.

The following shows example output:

```
name: test_service
id: service2_uztqb281sq7kx2tg5v6pxw9ktz
state: RUNNING
query_url: https://test-service.cld-kvedzwag2qa8i5bj.s.anyscale.com
creator: user@example.com
query_auth_token: <auth-token>
versions:
  - id: m71fqjx4
    name: v1
    state: RUNNING
    weight: 30
    created_at: 2025-10-27 18:57:47.953895+00:00
  - id: c5nbqwlq
    name: v2
    state: RUNNING
    weight: 30
    created_at: 2025-10-27 18:57:47.953895+00:00
  - id: cm4muq7g
    name: v3
    state: RUNNING
    weight: 20
    created_at: 2025-10-27 18:57:47.953895+00:00
  - id: addcp9dv
    name: v4
    state: RUNNING
    weight: 20
    created_at: 2025-10-27 18:57:47.953895+00:00
```

## Metrics and observability[​](#metrics "Direct link to Metrics and observability")

The Serve dashboard automatically tags metrics with version names, allowing you to filter and compare metrics across versions. You can view per-version metrics for QPS, latency, and error rates.

To view metrics by version, access the Serve dashboard for your service and use the version filter to select specific versions for comparison.

## Update autoscaling configuration[​](#update-autoscaling "Direct link to Update autoscaling configuration")

You can update the autoscaling configuration for deployed service versions without redeploying them. See [Enable worker group autoscaling in the compute config](/services/scale.md#worker-scaling).

## Beta limitations and considerations[​](#beta-limitations "Direct link to Beta limitations and considerations")

The following limitations apply to multi-version services in beta:

* This feature is only available for Anyscale clouds deployed on the VM stack on AWS. You can't use this feature with Google Cloud, Azure, or Kubernetes.
* **Configuration updates**: You can't update the Ray Serve configuration for deployed versions, including applications and HTTP options. To change these settings, deploy a new version. The exception is the autoscaling configuration, which you can update through the Anyscale console.

- **Rollback**: The `anyscale service rollback` command doesn't work with multi-version services. To fix issues, deploy a new version with the corrected configuration.
- **Version limit**: You can deploy up to 10 versions per service.

important

Multi-version services provide manual control over multiple service versions behind a single endpoint. This behavior is similar to using the `--canary-percent` parameter to manage how Anyscale routes traffic to two versions during rollouts. See [Manually-controlled rollouts](/services/update.md#manual)

You can't use the `--canary-percent` parameter with multi-version services. If you specify both `--canary-percent` and `--versions`, Anyscale ignores the `--canary-percent` parameter.
