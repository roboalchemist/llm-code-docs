# Source: https://docs.baseten.co/development/model/custom-health-checks.md

# Custom health checks 🆕

> Customize the health of your deployments.

**Why use custom health checks?**

* **Control traffic and restarts** by configuring failure thresholds to suit your needs.
* **Define replica health with custom logic** (e.g. fail after a certain number of 500s or a specific CUDA error).

By default, health checks run every 10 seconds to verify that each replica of your deployment is running successfully and can receive requests. If a health check fails for an extended period, one or both of the following actions may occur:

* Traffic is immediately stopped from reaching the failing replica.
* The failing replica is restarted.

The thresholds for each of these actions are configurable.

**Understanding readiness vs. liveness**: Baseten uses two types of Kubernetes health probes. The **readiness probe** determines when to stop traffic (controlled by `stop_traffic_threshold_seconds`), while the **liveness probe** determines when to restart the container (controlled by `restart_threshold_seconds`). Both probes check the same health endpoint, but serve different purposes: readiness controls traffic routing, while liveness controls container lifecycle.

Custom health checks can be implemented in two ways:

1. [**Configuring thresholds**](#configuring-health-checks) for when health check failures should stop traffic to or restart a replica.
2. [**Writing custom health check logic**](#writing-custom-health-checks) to define how replica health is determined.

## Configuring health checks

### Parameters

You can customize the behavior of health checks on your deployments by setting the following parameters:

<ParamField body="stop_traffic_threshold_seconds" type="integer" default={1800}>
  The duration that health checks must continuously fail before traffic to the failing replica is stopped.

  `stop_traffic_threshold_seconds` must be between `30` and `1800` seconds, inclusive.
</ParamField>

<ParamField body="restart_check_delay_seconds" type="integer" default={0}>
  How long to wait before running health checks.

  `restart_check_delay_seconds` must be between `0` and `1800` seconds, inclusive.
</ParamField>

<ParamField body="restart_threshold_seconds" type="integer" default={1800}>
  The duration that health checks must continuously fail before triggering a restart of the failing replica.

  `restart_threshold_seconds` must be between `30` and `1800` seconds, inclusive.

  <Note> The combined value of `restart_check_delay_seconds` and `restart_threshold_seconds` must not exceed `1800` seconds. </Note>
</ParamField>

### Model and custom server deployments

Configure health checks in your `config.yaml`.

```yaml config.yaml theme={"system"}
runtime:
  health_checks:
    restart_check_delay_seconds: 60 # Waits 60 seconds after deployment before starting health checks
    restart_threshold_seconds: 300 # Triggers a restart if health checks fail for 5 minutes
    stop_traffic_threshold_seconds: 600 # Stops traffic if health checks fail for 10 minutes
```

You can also specify custom health check endpoints for custom servers. [See here](/development/model/custom-server#1-configuring-a-custom-server-in-config-yaml) for more details.

### Chains

Use `remote_config` to configure health checks for your chainlet classes.

```python chain.py theme={"system"}
class CustomHealthChecks(chains.ChainletBase):
    remote_config = chains.RemoteConfig(
        options=chains.ChainletOptions(
            health_checks=truss_config.HealthChecks(
                restart_check_delay_seconds=30,     # Waits 30 seconds before starting health checks
                restart_threshold_seconds=120,      # Restart replicas after 2 minutes of failure
                stop_traffic_threshold_seconds=300, # Stop traffic after 5 minutes of failure
            )
        )
    )
```

## Writing custom health checks

You can write custom health checks in both **model deployments** and **chain deployments**.

<Info>
  {" "}

  Custom health checks are currently not supported in development deployments.{" "}
</Info>

{" "}

### Custom health checks in models

```python model.py theme={"system"}
class Model:
    def is_healthy(self) -> bool:
        # Add custom health check logic for your model here
		pass
```

### Custom health checks in chains

Health checks can be customized for each chainlet in your chain.

```python chain.py theme={"system"}
@chains.mark_entrypoint
class CustomHealthChecks(chains.ChainletBase):
    def is_healthy(self) -> bool:
        # Add custom health check logic for your chainlet here
        pass
```

## Health checks in action

### Identifying 5xx errors

You might create a custom health check to identify 5xx errors like the following:

```python model.py theme={"system"}
class Model:
    def __init__(self):
        ...
        self._is_healthy = True

    def load(self):
        # Perform load
        # Your custom health check won't run until after load completes
        ...

    def is_healthy(self):
        return self._is_healthy

    def predict(self, input):
        try:
            # Perform inference
            ...
        except Some5xxError:
            self._is_healthy = False
            raise
```

Custom health check failures are indicated by the following log:

```md Example health check failure log line theme={"system"}
Jan 27 10:36:03pm md2pg Health check failed.
```

Deployment restarts due to health check failures are indicated by the following log:

```md Example restart log line theme={"system"}
Jan 27 12:02:47pm zgbmb Model terminated unexpectedly. Exit code: 0, reason: Completed, restart count: 1
```

## FAQs

### Is there a rule of thumb for configuring thresholds for stopping traffic and restarting?

It depends on your health check implementation. If your health check relies on conditions that only change during inference (e.g., `_is_healthy` is set in `predict`), restarting before stopping traffic is generally better, as it allows recovery without disrupting traffic.

Stopping traffic first may be preferable if a failing replica is actively degrading performance or causing inference errors, as it prevents the failing replica from affecting the overall deployment while allowing time for debugging or recovery.

### When should I configure `restart_check_delay_seconds`?

Configure `restart_check_delay_seconds` to allow replicas sufficient time to initialize after deployment or a restart. This delay helps reduce unnecessary restarts, particularly for services with longer startup times.

### Why am I seeing two health check failure logs in my logs?

These refer to two separate health checks we run every 10 seconds:

* One to determine when to stop traffic to a replica.
* The other to determine when to restart a replica.

### Does stopped traffic or replica restarts affect autoscaling?

Yes, both can impact autoscaling. If traffic stops or replicas restart, the remaining replicas handle more load. If the load exceeds the concurrency target during the autoscaling window, additional replicas are spun up. Similarly, when traffic stabilizes, excess replicas are scaled down after the scale down delay. [See here](/deployment/autoscaling#autoscaling-behavior) for more details on autoscaling.

### How does billing get affected?

You are billed for the uptime of your deployment. This includes the time a replica is running, even if it is failing health checks, until it scales down.

### Will failing health checks cause my deployment to stay up forever?

No. If your deployment is configured with a scale down delay and the minimum number of replicas is set to 0, the replicas will scale down once the model is no longer receiving traffic for the duration of the scale down delay. This applies even if the replicas are failing health checks. [See here](/deployment/autoscaling#scale-to-zero) for more details on autoscaling.

### What happens when my deployment is loading?

When your deployment is loading, your custom health check will not be running. Once `load()` is completed, we'll start using your custom `is_healthy()` health check.
