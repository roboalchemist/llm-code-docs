# Source: https://www.apollographql.com/docs/apollo-operator/resources/supergraph/rollouts.md

# Safe Deployments

*Safe deployments* enable progressive, canary‑based rollouts with controlled traffic shifting, metrics‑driven analysis, and automatic promotion or rollback to reduce risk during router, schema, and configuration changes. You declaratively define rollout steps, weights, timing, and pause points in your `Supergraph` configuration and the Apollo GraphOS Operator creates and manages the necessary [Argo Rollouts](https://argoproj.github.io/argo-rollouts/) resources to execute these transitions and resume safely after failures.

## Prerequisites

You need:

* A Kubernetes cluster with permissions to install resources
* [kubectl](https://kubernetes.io/docs/reference/kubectl/) configured to access your cluster
* The Apollo GraphOS Operator v1.1.0 or greater installed in your cluster (see [Install Operator](https://www.apollographql.com/docs/apollo-operator/get-started/install-operator))

For Helm installation, you also need [Helm](https://helm.sh/) installed.

## Install Argo Rollouts

Before you can use safe deployments, you need to install Argo Rollouts in your cluster. You can [install Argo Rollouts using different methods](https://argoproj.github.io/argo-rollouts/installation/). The most common methods are `kubectl` or Helm.

### Install with `kubectl`

#### Create the Argo Rollouts namespace

```sh
kubectl create namespace argo-rollouts --dry-run=client -o yaml | kubectl apply -f -
```

#### Install Argo Rollouts

Install Argo Rollouts v1.7.2:

```sh
kubectl apply -n argo-rollouts -f https://github.com/argoproj/argo-rollouts/releases/download/v1.7.2/install.yaml
```

### Install with Helm

#### Add the Argo Helm repository

```sh
helm repo add argo https://argoproj.github.io/argo-helm
helm repo update
```

#### Install Argo Rollouts

Install Argo Rollouts using Helm:

```sh
helm install argo-rollouts argo/argo-rollouts --namespace argo-rollouts --create-namespace --version 1.7.2
```

### Verify installation

After installing using either method, verify the installation by waiting for the Argo Rollouts deployment to be ready:

```sh
kubectl rollout -n argo-rollouts status deployment argo-rollouts --timeout=90s
```

You should now have Argo Rollouts installed and ready to use.

## Configure safe deployments

To enable safe deployments for a Supergraph, configure the `deploymentStrategy` field in your Supergraph spec. The operator supports canary deployments with Argo Rollouts.

If you have an existing `Supergraph` using a standard Kubernetes `Deployment`, you can migrate to a `Rollout` strategy with zero downtime. See the [migration guide](https://www.apollographql.com/docs/apollo-operator/resources/supergraph/rollouts/advanced#migrate-from-deployment-to-rollout) for details.

### Basic configuration

Here's a complete example that configures a canary deployment with steps:

```yaml
apiVersion: apollographql.com/v1alpha3
kind: Supergraph
metadata:
  name: my-supergraph
spec:
  replicas: 2  # Number of replicas for the Supergraph
  podTemplate:
    routerVersion: 2.7.0  # GraphOS Router version
  deploymentStrategy:
    rollout:  # Use Argo Rollouts for safe deployments
      steps:
        - setWeight: 30  # Shift 30% of traffic to new version
        - pause:
            duration: 2m  # Wait 2 minutes before next step
        - setWeight: 50  # Shift 50% of traffic to new version
        - pause:
            duration: 2m  # Wait 2 minutes before next step
        - setWeight: 80  # Shift 80% of traffic to new version
        - pause:
            duration: 2m  # Wait 2 minutes before final step
        - setWeight: 100  # Shift all traffic to new version
  routerConfig:
    homepage:
      enabled: false
    sandbox:
      enabled: true
    supergraph:
      introspection: true
  schema:
    studio:
      graphRef: my-graph@my-variant  # GraphOS graph variant reference
```

### Understand Rollout Steps

Steps define the canary deployment progression. Use the following patterns as starting points for common use cases. For additional options and advanced configurations, see the [Argo Rollouts canary documentation](https://argoproj.github.io/argo-rollouts/features/canary/).

Common step types include:

* **`setWeight`**: Sets the percentage of traffic to send to the new version (`0`-`100`)
* **`pause`**: Pauses the rollout for a specified duration or until manually resumed
* **`pause: {}`**: Pauses indefinitely until manually resumed

### Recommended canary step patterns

#### Gradual traffic increase

Gradually increase traffic over time:

```yaml
deploymentStrategy:
  rollout:
    steps:
      - setWeight: 10
      - pause:
          duration: 5m
      - setWeight: 25
      - pause:
          duration: 5m
      - setWeight: 50
      - pause:
          duration: 5m
      - setWeight: 100
```

#### Manual approval points

Add manual approval steps for critical deployments:

```yaml
deploymentStrategy:
  rollout:
    steps:
      - setWeight: 20
      - pause: {}  # Wait for manual approval
      - setWeight: 50
      - pause: {}  # Wait for manual approval
      - setWeight: 100
```

To resume a paused rollout, use the [Argo Rollouts `kubectl` plugin](https://argo-rollouts.readthedocs.io/en/stable/installation/#kubectl-plugin-installation):

```sh
kubectl argo rollouts promote <rollout-name>
```

## Understand `Rollout` states

When using safe deployments, the Supergraph status includes detailed rollout information. Understanding the states helps you monitor your deployments.

### Rollout phases

The rollout goes through several phases, which map to Supergraph conditions:

| Rollout Phase   | Description                     | Supergraph Condition                 | Reason                 | Message                                    |
| --------------- | ------------------------------- | ------------------------------------ | ---------------------- | ------------------------------------------ |
| `Initializing`  | Rollout is starting             | `Progressing: True`                  | `HasChanges`           | `Supergraph` had recent changes            |
| `Progressing`   | Rollout is moving through steps | `Progressing: True`                  | `DeploymentInProgress` | Supergraph deployment is in progress       |
| `PausedForStep` | Rollout paused at a step        | `Progressing: True`                  | `DeploymentInProgress` | Supergraph deployment is in progress       |
| `Completed`     | Rollout finished successfully   | `Progressing: True`, `Ready: True`   | `DeploymentCompleted`  | Supergraph deployment is in a stable state |
| `Failed`        | Rollout has failed              | `Progressing: False`, `Ready: False` | `DeploymentFailed`     | Supergraph deployment failed               |
| `RollingBack`   | Rollout is rolling back         | `Progressing: False`, `Ready: False` | `DeploymentFailed`     | Supergraph deployment failed               |

### Check the Rollout status

The Supergraph status includes rollout details:

```yaml
status:
  rollout:
    currentStep: 2
    totalSteps: 5
    trafficPercentage: 50
    phase: Progressing
```

* **`currentStep`**: Current step index (`0`-based) in the rollout
* **`totalSteps`**: Total number of steps configured
* **`trafficPercentage`**: Current traffic percentage for the canary (0-100)
* **`phase`**: Current rollout phase

### Monitor Rollouts

When you check the `Supergraph` status, you see `Rollout` information in the `status.rollout` section. Here's an example of what to look for:

```yaml
status:
  rollout:
    currentStep: 2        # Current step in the rollout (0-based)
    totalSteps: 5         # Total number of steps configured
    trafficPercentage: 50 # Percentage of traffic on the canary
    phase: Progressing    # Current rollout phase
```

Key fields to monitor:

* **`rollout.phase`**: Shows the current phase (e.g., `Progressing`, `PausedForStep`, `Completed`, `Failed`)
* **`rollout.currentStep`** and **`rollout.totalSteps`**: Indicates progress through the rollout steps
* **`rollout.trafficPercentage`**: Shows how much traffic is currently on the canary version

Check the rollout status:

```sh
kubectl get supergraph my-supergraph -o yaml
```

View rollout details:

```sh
kubectl get rollout my-supergraph -o yaml
```

## Explore next steps

Now that you have safe deployments configured, you can:

* Learn about [advanced topics](https://www.apollographql.com/docs/apollo-operator/resources/supergraph/rollouts/advanced) including custom analysis, networking integration, and migration
* Monitor your rollouts using the status information
* Configure automated analysis for your deployments
