# Source: https://docs.baseten.co/development/model/environments.md

# Source: https://docs.baseten.co/deployment/environments.md

# Environments

> Manage your model’s release cycles with environments.

Environments provide structured management for deployments, ensuring controlled rollouts, stable endpoints, and autoscaling. They help teams stage, test, and release models without affecting production traffic.

<img noZoom src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-environments.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=e922f3e12c24577d6594ca58f80431ee" data-og-width="964" width="964" data-og-height="552" height="552" data-path="images/deployment-environments.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-environments.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=210053dfe7b0d3398f261f1105ac6bf9 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-environments.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=3a7e2675275ae1f78ac5fe83330e926c 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-environments.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=874b4335f21d8939c58dcd2c2b978c8c 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-environments.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=09f864b743a3921b713612d54ed9708b 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-environments.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=a6397fff11d9c0edfd8103f44b8b501e 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-environments.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=23a5dd05c6ee1ab42cecb3698098cbb3 2500w" />

Deployments can be promoted to an environment (e.g., "staging") to validate outputs before moving to production, allowing for safer model iteration and evaluation.

***

## Using Environments to manage deployments

Environments support **structured validation** before promoting a deployment, including:

* **Automated tests & evaluations**
* **Manual testing in pre-production**
* **Gradual traffic shifts with canary deployments**
* **Shadow serving for real-world analysis**

Promoting a deployment ensures it inherits **environment-specific scaling and monitoring settings**, such as:

* **Dedicated API endpoint** → [Predict API Reference](/reference/inference-api/overview#predict-endpoints)
* **Autoscaling controls** → Scale behavior is managed per environment.
* **Traffic ramp-up** → Enable [canary rollouts](/deployment/deployments#canary-deployments).
* **Monitoring & Metrics** → [Export environment metrics](/observability/export-metrics/overview).

A **production environment** operates like any other environment but has restrictions:

* **It cannot be deleted** unless the entire model is removed.
* **You cannot create additional environments named "production."**

***

## Creating custom environments

In addition to the standard **production** environment, you can create as many custom environments as needed. There are two ways to create a custom environment:

1. In the model management page on the Baseten dashboard.
2. Via the [create environment endpoint](/reference/management-api/environments/create-an-environment) in the model management API.

***

## Promoting deployments to environments

When a deployment is promoted, Baseten follows a **three-step process**:

1. A **new deployment** is created with a unique deployment ID.
2. The deployment **initializes resources** and becomes active.
3. The new deployment **replaces the existing deployment** in that environment.

* If there was **no previous deployment, default autoscaling settings** are applied.
* If a **previous deployment existed**, the new one **inherits autoscaling settings**, and the old deployment is **demoted and scales to zero**.

### Promoting a Published Deployment

If a **published deployment** (not a development deployment) is promoted:

* Its **autoscaling settings are updated** to match the environment.
* If **inactive**, it must be **activated** before promotion.

Previous deployments are **demoted but remain in the system**, retaining their **deployment ID and scaling behavior**.

***

## Deploying directly to an environment

You can **skip development stage** and deploy directly to an environment by specifying `--environment` in `truss push`:

```sh  theme={"system"}
cd my_model/
truss push --environment {environment_name}
```

<Note>Only one active promotion per environment is allowed at a time.</Note>

***

## Accessing environments in your code

The **environment name** is available in `model.py` via the `environment` keyword argument:

```python  theme={"system"}
def __init__(self, **kwargs):
    self._environment = kwargs["environment"]
```

To ensure the **environment variable remains updated**, enable\*\* "Re-deploy when promoting" \*\*in the UI or via the [REST API](/reference/management-api/environments/update-an-environments-settings). This guarantees the environment is fully initialized after a promotion.

***

## Deleting environments

Environments can be deleted, **except for production**. To remove a **production deployment**, first **promote another deployment to production** or delete the entire model.

* **Deleted environments are removed from the overview** but remain in billing history.
* **They do not consume resources** after deletion.
* **API requests to a deleted environment return a 404 error.**

<Warning>Deletion is permanent - consider deactivation instead.</Warning>
