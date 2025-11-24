# Source: https://docs.baseten.co/deployment/deployments.md

# Deployments

> Deploy, manage, and scale machine learning models with Baseten

A **deployment** in Baseten is a **containerized instance of a model** that serves inference requests via an API endpoint. Deployments exist independently but can be **promoted to an environment** for structured access and scaling.

Every deployment is **automatically wrapped in a REST API**. Once deployed, models can be queried with a simple HTTP request:

```python  theme={"system"}
import requests

resp = requests.post(
    "https://model-{modelID}.api.baseten.co/deployment/[{deploymentID}]/predict",
    headers={"Authorization": "Api-Key YOUR_API_KEY"},
    json={'text': 'Hello my name is {MASK}'},
)

print(resp.json())
```

[Learn more about running inference on your deployment](/inference/calling-your-model)

***

# Development deployment

A **development deployment** is a mutable instance designed for rapid iteration. It is always in the **development state** and cannot be renamed or detached from it.

Key characteristics:

* **Live reload** enables direct updates without redeployment.
* **Single replica, scales to zero** when idle to conserve compute resources.
* **No autoscaling or zero-downtime updates.**
* **Can be promoted** to create a persistent deployment.

Once promoted, the development deployment transitions to a **deployment** and can optionally be promoted to an environment.

***

# Environments & Promotion

Environments provide **logical isolation** for managing deployments but are **not required** for a deployment to function. A deployment can be executed independently or promoted to an environment for controlled traffic allocation and scaling.

* The **production environment** exists by default.
* **Custom environments** (e.g., staging) can be created for specific workflows.
* **Promoting a deployment does not modify its behavior**, only its routing and lifecycle management.

## Canary deployments

Canary deployments support **incremental traffic shifting** to a new deployment, mitigating risk during rollouts.

* Traffic is routed in **10 evenly distributed stages** over a configurable time window.
* Traffic only begins to shift once the new deployment reaches the min replica count of the current production model.
* Autoscaling dynamically adjusts to real-time demand.
* Canary rollouts can be enabled or canceled via the UI or [REST API](/reference/management-api/environments/update-an-environments-settings).

***

# Managing Deployments

## Naming deployments

By default, deployments of a model are named `deployment-1`, `deployment-2`, and so forth sequentially. You can instead give deployments custom names via two methods:

1. While creating the deployment, using a [command line argument in truss push](/reference/sdk/truss#deploying-a-model).
2. After creating the deployment, in the model management page within your Baseten dashboard.

Renaming deployments is purely aesthetic and does not affect model management API paths, which work via model and deployment IDs.

## Deactivating a deployment

A deployment can be deactivated to suspend inference execution while preserving configuration.

* **Remains visible in the dashboard.**
* **Consumes no compute resources** but can be reactivated anytime.
* **API requests return a 404 error while deactivated.**

For demand-driven deployments, consider [autoscaling with scale to zero](/reference/management-api/deployments/autoscaling/updates-a-deployments-autoscaling-settings).

## Deleting deployments

Deployments can be **permanently deleted**, but production deployments must be replaced before deletion.

* **Deleted deployments are purged from the dashboard** but retained in usage logs.
* **All associated compute resources are released.**
* **API requests return a 404 error post-deletion.**

<Warning>
  Deletion is irreversible — use deactivation if retention is required.
</Warning>
