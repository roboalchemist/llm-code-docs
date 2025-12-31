# Source: https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/deep-learning-platform/deployments.md

# Deployments

Deploy your models to production with auto-scaling and load balancing.

![Deployments View](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-8e280f6ec2b925174213e1212b6779e11ed5caaf%2Fsection_deployments_1764148292871.png?alt=media)

## Creating a Deployment

Navigate to **Deployments** → Click **Create**

![Create Deployment Form](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-7b6971746661e0581696a0215d6a1e95e8bb0e05%2Fcreate_deployment_form.png?alt=media)

### Basic Information

**Deployment Name**\* (Required)

* Enter a descriptive name for the deployment
* Example: `resnet-prod`, `bert-api-v1`

**Description** (Optional)

* Deployment purpose and details

**Model ID**\* (Required)

* ID of the model to deploy
* Helper text: "ID of the model to deploy"

**Model Version**\* (Required)

* Version of the model to deploy
* Helper text: "Version of the model to deploy"

**Environment**\* (Required)

* Select deployment environment:
  * Development
  * Staging
  * Production
* Default: `development`

### Resource Configuration

**CPU Cores**\* (Required)

* Number of CPU cores per instance
* Example: `4`, `8`, `16`

**Memory (GB)**\* (Required)

* Memory allocation per instance in GB
* Example: `8`, `16`, `32`

**GPU Count** (Optional)

* Number of GPUs (0 or GPU Count)
* Default: `0`

**GPU Type** (Optional)

* Select GPU type if GPU Count > 0:
  * NVIDIA T4
  * NVIDIA V100
  * NVIDIA A100

**Min Replicas**\* (Required)

* Minimum number of instances
* Example: `1`, `2`

**Max Replicas**\* (Required)

* Maximum number of instances
* Example: `10`, `20`

**Target CPU Utilization (%)**\* (Required)

* CPU threshold for scaling
* Example: `70`, `80`

**Target Memory Utilization (%)**\* (Required)

* Memory threshold for scaling
* Example: `80`, `90`

### Scaling Configuration

**Enable Auto-Scaling** (Checkbox)

* Enable automatic scaling based on metrics

When enabled:

* **Min Instances**\*: Minimum instances to maintain
* **Max Instances**\*: Maximum instances allowed
* **Target GPU Utilization (%)**: GPU threshold
* **Target Memory Utilization (%)**: Memory threshold

### Load Balancer

**Enable Load Balancer** (Checkbox)

* Enable load balancing across instances

When enabled:

* **Service Type**\*: Round Robin, Least Connections, IP Hash
* **Health Check URL**\*: Endpoint for health checks (e.g., `/health`)
* **Health Check Interval (seconds)**\*: Frequency of health checks
* **Sticky Sessions**: Enable session affinity

### Actions

* **Cancel**: Discard and close
* **Create Deployment**: Submit and create the deployment

## Example Configuration

```yaml
Deployment Name: resnet-production-v1
Model ID: model_abc123
Model Version: 1.0.0
Environment: Development

Resource Configuration:
  CPU Cores: 4
  Memory (GB): 16
  GPU Count: 0
  Min Replicas: 2
  Max Replicas: 10

Scaling:
  Enable Auto-Scaling: ✓
  Min Instances: 2
  Max Instances: 10
  Target CPU: 70%

Load Balancer:
  Enable: ✓
  Service Type: Round Robin
  Health Check URL: /health
  Health Check Interval: 30s
  Sticky Sessions: ✓
```

## Viewing Deployment Details

To view detailed information about a deployment:

1. Navigate to **Deployments**
2. Click on a deployment from the list
3. View comprehensive details in the modal dialog

![View Deployment Details](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-36449470f401360fe63f3c58af0a7abd813c62d7%2Fdeployment_details_view.png?alt=media)

**Details Panel Sections**:

**Basic Information**:

* **Deployment Name**: e.g., "BERT Sentiment API"
* **Description**: Full description of the deployment
* **Model ID**: ID of the deployed model (e.g., "model-001")
* **Model Version**: Version being deployed (e.g., "v2.1.0")
* **Environment**: Production, Staging, or Development
* **Deployment Strategy**: Blue-Green, Rolling Update, Canary

**Resource Configuration**:

* **CPU Cores**: Number of CPU cores per instance (e.g., 4)
* **Memory (GB)**: Memory allocation (e.g., 16 GB)
* **GPU Count**: Number of GPUs (e.g., 2)
* **GPU Type**: GPU model (e.g., A100, V100)
* **Storage (GB)**: Storage allocation (e.g., 200 GB)
* **Network Bandwidth (Mbps)**: Network bandwidth (e.g., 1000 Mbps)

**Scaling Configuration**:

* **Current Instances**: Number of running instances (e.g., 2)
* **Enable Auto-Scaling**: Checkbox status
* **Min Instances**: Minimum replicas (e.g., 2)
* **Max Instances**: Maximum replicas (e.g., 10)
* **Target CPU Utilization (%)**: CPU scaling threshold (e.g., 70%)
* **Target GPU usage for trigger scaling**: GPU threshold
* **Target Memory Utilization (%)**: Memory threshold (e.g., 80%)
* **Target memory usage for trigger scaling**: Memory threshold

**Load Balancer**:

* **Enable Load Balancer**: Checkbox status
* **Load Balancing Algorithm**: Round Robin, Least Connections, IP Hash
* **Health Check Path**: Endpoint for health checks (e.g., "/health")
* **Health Check Interval (seconds)**: Check frequency (e.g., 30)
* **Sticky Sessions**: Checkbox for session affinity

## Editing a Deployment

To update deployment configuration:

1. Open deployment details page
2. Click **Edit** button (or three-dot menu → Edit)
3. Modify editable fields in the Edit Deployment modal

![Edit Deployment Form](https://3962875474-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F01Fyr0ujWr1ipjmUOTbr%2Fuploads%2Fgit-blob-bedcb9c10701fad02bdf47c6649a6609669a872c%2Fdeployment_edit_form.png?alt=media)

4. Click **Update Deployment** to save changes

> \[!NOTE] The Edit form is identical to the View form, but with editable fields and an "Update Deployment" button. Some changes may require a deployment restart.

> \[!NOTE] Some changes may require a deployment restart to take effect.

**Editable Fields**:

* ✅ Description
* ✅ Environment variables
* ✅ Min/Max replicas
* ✅ Auto-scaling thresholds
* ✅ Health check settings
* ✅ Load balancer configuration
* ⚠️ CPU/Memory (requires restart)
* ❌ Model ID (use Update Model instead)
* ❌ Deployment name (cannot edit)

## Updating Model Version

To deploy a new model version:

1. Open deployment details
2. Click **Update Model** button
3. Select new model version
4. Choose update strategy:
   * **Rolling Update**: Gradual replacement (zero downtime)
   * **Blue-Green**: Switch all at once
   * **Canary**: Test with small percentage first
5. Click **Update**

**Update Strategies**:

**Rolling Update** (Recommended):

* Gradually replaces old instances
* Zero downtime
* Automatic rollback on failure

**Blue-Green**:

* Deploys new version alongside old
* Switches traffic all at once
* Quick rollback possible

**Canary**:

* Routes small % of traffic to new version
* Monitor performance
* Gradually increase if successful

## Scaling a Deployment

**Manual Scaling**:

1. Open deployment details
2. Click **Scale** button
3. Adjust number of replicas
4. Click **Apply**

**Auto-scaling**:

1. Open deployment details
2. Click **Edit**
3. Enable auto-scaling
4. Set min/max replicas
5. Configure scaling triggers
6. Save changes

## Stopping a Deployment

To temporarily stop a deployment:

1. Open deployment details
2. Click **Stop** button
3. Confirm action
4. All instances will shut down
5. Endpoint will become unavailable

**Use Cases**:

* Maintenance window
* Cost optimization
* Testing in isolation

## Restarting a Deployment

To restart a stopped deployment:

1. Open deployment details
2. Click **Start** button
3. Deployment will resume with previous configuration

## Deleting a Deployment

To permanently remove a deployment:

1. Navigate to deployment details
2. Click **Delete** button
3. Confirm deletion

> \[!WARNING] Deleting a deployment will:
>
> * Shut down all instances
> * Remove the endpoint
> * Delete deployment configuration
> * This action cannot be undone!

**Before Deleting**:

* Stop sending traffic to the endpoint
* Update client applications
* Export logs if needed
* Verify you have the correct deployment

## Monitoring Deployments

**Real-time Metrics**:

* Request rate
* Latency (p50, p95, p99)
* Error rate
* Resource usage

**Actions**:

* Scale up/down
* Update model version
* View logs
* Rollback

## Best Practices

* Set appropriate min/max replicas
* Configure auto-scaling thresholds
* Enable health checks
* Use load balancing for high traffic
* Monitor performance continuously

## Next Steps

* Monitor in [Analytics](https://docs.kaisar.io/kaisar-network/kaisar-ai-ops/deep-learning-platform/analytics)
* View logs and metrics
* Set up alerts
