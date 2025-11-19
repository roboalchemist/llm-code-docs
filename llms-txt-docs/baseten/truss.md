# Source: https://docs.baseten.co/reference/sdk/truss.md

# Truss SDK Reference

> Python SDK for deploying and managing models with Truss.

# Authentication

## `truss.login(api_key: str) → None`

Authenticates with Baseten using an API key.

**Parameters:**

| Name      | Type  | Description      |
| --------- | ----- | ---------------- |
| `api_key` | *str* | Baseten API Key. |

***

# Deploying a Model

## `truss.push(target_directory: str, **kwargs) → ModelDeployment`

Deploys a **Truss** model to Baseten.

**Parameters:**

| Name                                      | Type             | Description                                                                                                              |
| ----------------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `target_directory`                        | *str*            | Path to the Truss directory to push.                                                                                     |
| `remote`                                  | *Optional\[str]* | Name of the remote in `.trussrc` to push to.                                                                             |
| `model_name`                              | *Optional\[str]* | Override the model name in `config.yaml`.                                                                                |
| `publish`                                 | *bool*           | Deploy as **published**. If no production deployment exists, promote it to production.                                   |
| `promote`                                 | *bool*           | Deploy as **published** and promote to production, even if a production deployment exists.                               |
| `preserve_previous_production_deployment` | *bool*           | Preserve the previous production deployment’s **autoscaling settings** (only with `promote`).                            |
| `trusted`                                 | *bool*           | Grants **access to secrets** on the remote host.                                                                         |
| `deployment_name`                         | *Optional\[str]* | Custom deployment name (must contain only alphanumeric, `.`, `-`, or `_` characters). (Requires `publish` or `promote`.) |

**Returns:** [ModelDeployment](#class-truss-api-definitions-modeldeployment) – An object representing the deployed model.

***

# Model Deployment Object

## *class* `truss.api.definitions.ModelDeployment`

Represents a deployed model (returned by `truss.push()`).

**Attributes**

`model_id` → `str` – Unique ID of the deployed model.
`model_deployment_id` → `str` – Unique ID of the model deployment.

**Methods**

`wait_for_active()` → bool
Waits for the deployment to become **active**.

**Returns**: `True` when deployment is ready.
**Raises**: An error if deployment fails.
