# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/models/get_model_monitoring_deployments_response_all_of_deployments.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.models.get_model_monitoring_deployments_response_all_of_deployments

## Classes

### GetModelMonitoringDeploymentsResponseAllOfDeployments

```python  theme={"system"}
edgeimpulse_api.models.get_model_monitoring_deployments_response_all_of_deployments.GetModelMonitoringDeploymentsResponseAllOfDeployments(
	**data: Any
)
```

Create a new model by parsing and validating input data from keyword arguments.

Raises ValidationError if the input data cannot be parsed to form a valid model.

| Parameters |       |
| ---------- | ----- |
| `**data`   | `Any` |

| Bases                              |
| ---------------------------------- |
| `pydantic.v1.main.BaseModel`       |
| `pydantic.v1.utils.Representation` |

| Class variables   |                                                                                  |
| ----------------- | -------------------------------------------------------------------------------- |
| `Config`          | ` `                                                                              |
| `created`         | `datetime.datetime`                                                              |
| `deployment_type` | `pydantic.v1.types.StrictStr`                                                    |
| `engine`          | `edgeimpulse_api.models.deployment_target_engine.DeploymentTargetEngine \| None` |
| `id`              | `float`                                                                          |
| `impulse_id`      | `float \| None`                                                                  |
| `impulse_name`    | `pydantic.v1.types.StrictStr \| None`                                            |
| `model_type`      | `edgeimpulse_api.models.keras_model_type_enum.KerasModelTypeEnum \| None`        |
| `version`         | `float \| None`                                                                  |

***

**STATIC METHODS**

#### from\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_model_monitoring_deployments_response_all_of_deployments.GetModelMonitoringDeploymentsResponseAllOfDeployments.from_dict(
	obj: dict
) ‑> edgeimpulse_api.models.get_model_monitoring_deployments_response_all_of_deployments.GetModelMonitoringDeploymentsResponseAllOfDeployments
```

Create an instance of GetModelMonitoringDeploymentsResponseAllOfDeployments from a dict

| Parameters |        |
| ---------- | ------ |
| `obj`      | `dict` |

| Returns                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_model_monitoring_deployments_response_all_of_deployments.GetModelMonitoringDeploymentsResponseAllOfDeployments` |

#### from\_json

```python  theme={"system"}
edgeimpulse_api.models.get_model_monitoring_deployments_response_all_of_deployments.GetModelMonitoringDeploymentsResponseAllOfDeployments.from_json(
	json_str: str
) ‑> edgeimpulse_api.models.get_model_monitoring_deployments_response_all_of_deployments.GetModelMonitoringDeploymentsResponseAllOfDeployments
```

Create an instance of GetModelMonitoringDeploymentsResponseAllOfDeployments from a JSON string

| Parameters |       |
| ---------- | ----- |
| `json_str` | `str` |

| Returns                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_model_monitoring_deployments_response_all_of_deployments.GetModelMonitoringDeploymentsResponseAllOfDeployments` |

***

**METHODS**

#### to\_dict

```python  theme={"system"}
edgeimpulse_api.models.get_model_monitoring_deployments_response_all_of_deployments.GetModelMonitoringDeploymentsResponseAllOfDeployments.to_dict(
	self
)
```

Returns the dictionary representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

#### to\_json

```python  theme={"system"}
edgeimpulse_api.models.get_model_monitoring_deployments_response_all_of_deployments.GetModelMonitoringDeploymentsResponseAllOfDeployments.to_json(
	self,
	indent=None
) ‑> str
```

Returns the JSON representation of the model using alias

| Parameters    |     |
| ------------- | --- |
| `self`        | ` ` |
| `indent=None` | ` ` |

| Returns |
| ------- |
| `str`   |

#### to\_str

```python  theme={"system"}
edgeimpulse_api.models.get_model_monitoring_deployments_response_all_of_deployments.GetModelMonitoringDeploymentsResponseAllOfDeployments.to_str(
	self
) ‑> str
```

Returns the string representation of the model using alias

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

| Returns |
| ------- |
| `str`   |


Built with [Mintlify](https://mintlify.com).