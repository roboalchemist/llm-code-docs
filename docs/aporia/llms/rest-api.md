# Source: https://docs.aporia.com/v1/api-reference/rest-api.md

# REST API

Aporia provides a REST API, which is currently in beta.

### Using the REST API

The API is accessible thorough `https://app.aporia.com/v1beta`.

To use the API, you must pass your token in the authorization header of each request:

```
Authorization: Bearer <token>
```

### Endpoints

#### Create Model

Creates a new [model](https://docs.aporia.com/v1/core-concepts/model-versions#model).

```
POST https://app.aporia.com/v1beta/models
{
    "id": "my-model",
    "name": "My Model",
    "description": "My awesome model",
    "color": "turquoise",
    "icon": "fraud-detection",
    "owner": "owner@example.com",
    "tags": {
        "foo": "bar"
    }
}
```

```
{
    "id": "my-model"
}
```

**Request Parameters**

| Parameter   | Type            | Required | Description                                                                                                                                                            |
| ----------- | --------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id          | str             | False    | A unique identifier for the new model, which will be used in all future operations. If this parameter is not passed, an id will be generated from the `name` parameter |
| name        | str             | True     | A name for the new model, which will be displayed in Aporia's dashboard                                                                                                |
| description | str             | False    | A description of the model                                                                                                                                             |
| color       | ModelColor      | False    | A color to distinguish the model in Aporia's dashboard. Defaults to `blue`                                                                                             |
| icon        | ModelIcon       | False    | An icon that indicates the model's designation. Defaults to `general`                                                                                                  |
| owner       | str             | False    | The email of the model owner (must be a registered aporia user)                                                                                                        |
| tags        | Dict\[str, str] | False    | A mapping of tag keys to tag values                                                                                                                                    |

**ModelColor options:** `blue`,`arctic_blue`, `green`, `turquoise`, `pink`, `purple`, `yellow`, `red`

**ModelIcon options**: `general`, `churn-and-retention`, `conversion-predict`, `anomaly`, `dynamic-pricing`, `email-filtering`, `demand-forecasting`, `ltv`, `personalization`, `fraud-detection`, `credit-risk`, `recommendations`

**Response**

| Value | Type | Description                       |
| ----- | ---- | --------------------------------- |
| id    | str  | The id of the newly created model |

#### Delete Model

Deletes a model.

```
DELETE https://app.aporia.com/v1beta/models/<model_id>/
```

**Path Parameters**

| Parameter | Description                    |
| --------- | ------------------------------ |
| model\_id | The ID of the model to delete. |

#### Get Model Versions

Returns all model versions and their creation date.

```
GET https://app.aporia.com/v1beta/models/<model_id>/versions
```

```
[
    {
        "id": "4dc246a2-0fd4-4342-8e30-95c2b43e8b63",
        "name": "v1",
        "model_type": "regression",
        "created_at": "2021-10-03T10:23:00.913784+00:00"
    },
    {
        "id": "21a6ee3f-8102-4e54-90bd-5809cff409cd",
        "name": "v2",
        "model_type": "regression",
        "created_at": "2021-10-03T10:33:54.073001+00:00"
    }
]
```

**Path Parameters**

| Parameter | Description                                           |
| --------- | ----------------------------------------------------- |
| model\_id | The ID of the model whose versions you wish to fetch. |

**Response**

A List of VersionDetails objects, each with the following format:

| Value       | Type | Description                                                             |
| ----------- | ---- | ----------------------------------------------------------------------- |
| id          | str  | Version id.                                                             |
| name        | str  | Version name.                                                           |
| model\_type | str  | The type of the model created by the version (regression, binary, etc). |
| created\_at | str  | The creation date of the version.                                       |

#### Create Model Version

Defines a new version for an existing model.

```
POST https://app.aporia.com/v1beta/models/<model_id>/versions
{
    "name": "v1",
    "model_type": "binary",
    "version_schema": {
        "features": {
            "amount": "numeric",
            "owner": "string",
            "is_new": "boolean",
            "created_at": "datetime"
        },
        "predictions": {
            "approved": "boolean",
            "another_output_field": "numeric"
        }
    },
    "feature_importance" : {
        "amount": 100,
        "owner": 20,
        "is_new": 50,
        "created_at": 10
    }
}
```

```
{
    "id": "d84a497b-6a13-49e3-91f0-b01117f49ac7"
}
```

**Path Parameters**

| Parameter | Description                                                    |
| --------- | -------------------------------------------------------------- |
| model\_id | The ID of the model for which the new version is being defined |

**Request Parameters**

| Parameter           | Type              | Required                                                              | Description                                      |
| ------------------- | ----------------- | --------------------------------------------------------------------- | ------------------------------------------------ |
| name                | str               | True                                                                  | A unique name for the new model version          |
| model\_type         | ModelType         | True                                                                  | Model type                                       |
| version\_schema     | object            | The schema for the new version, mapping various fields to their types |                                                  |
| feature\_importance | Dict\[str, float] | False                                                                 | Mapping between feature name to it's importance. |

**Notes**

* **ModelType options:** `binary`, `multiclass`, `multi-label`, `regression`
* **Feature positions:** When reporting a model schema, there is an optional argument called feature\_positions. This argument provides mapping of feature names to feature positions in the dataframe which the model receives. Feature Positions are required for Explainability capabilities. In the console, to explain a data point, go to Model Overview -> Investigation Toolbox -> Data points and click Explain on a specific data point. For example:

```
"feature_positions":{
    "Age":1,
    "Gender:2
}
```

**Response**

| Value | Type | Description                     |
| ----- | ---- | ------------------------------- |
| id    | UUID | The id of the new model version |

#### Create Monitor

Creates a new monitor.

The documentation for each monitor contains an example of creating that monitor using the REST API.

```
POST https://app.aporia.com/v1beta/monitors
{
    "name": "Hourly Predictions > 100",
    "type": "model_activity",
    "scheduling": "*/5 * * * *",
    "configuration":  {
        "configuration": {
            "focal": {
                "source": "SERVING",
                "timePeriod": "1h"
            },
            "metric": {
                "type": "count",
                "field": "_id"
            },
            "actions": [
                {
                    "type": "ALERT",
                    "schema": "v1",
                    "severity": "MEDIUM",
                    "alertType": "model_activity_threshold",
                    "description": "An anomaly in the number of total predictions within the defined limits was detected.<br />The anomaly was observed in the <b>{model}</b> model, in version <b>{model_version}</b> for the <b>last {focal_time_period} ({focal_times})</b> <b>{focal_segment}</b>.<br /><br />Based on defined limits, the count was expected to be above <b>{min_threshold}</b>, but <b>{focal_value}</b> was received.<br />",
                    "notification": [
                        {
                            "type": "EMAIL",
                            "emails": [
                                "dev@aporia.com"
                            ]
                        }
                    ],
                    "visualization": "value_over_time"
                }
            ],
            "logicEvaluations": [
                {
                    "max": null,
                    "min": 100,
                    "name": "RANGE"
                }
            ]
        },
        "identification": {
            "models": {
                "id": "seed-0000-5wfh"
            },
            "segment": {
                "group": null
            },
            "environment": null
        }
    }
}
```

```
{
    "id": "a5d11808-0a42-4d25-84fa-0cc71173044c"
}
```

**Request Parameters**

| Parameter                  | Type        | Required | Description                                                                                    |
| -------------------------- | ----------- | -------- | ---------------------------------------------------------------------------------------------- |
| name                       | str         | True     | A name for the new monitor, which will be displayed in Aporia's dashboard                      |
| type                       | MonitorType | True     | The type of monitor to create                                                                  |
| scheduling                 | str         | True     | A cron expression that indicates how often the monitor will run                                |
| configuration              | object      | True     | The monitor's configuration                                                                    |
| is\_active                 | bool        | False    | True if the new monitor should be created as active, False if it should be created as inactive |
| custom\_alert\_description | str         | False    | A custom description for the alerts generated by this monitor                                  |

**MonitorType options:** `model_activity`, `missing_values`, `data_drift`, `prediction_drift`, `values_range`, `new_values`, `model_staleness`, `performance_degradation`, `metric_change`, `custom_metric`

**Response**

| Value | Type | Description                         |
| ----- | ---- | ----------------------------------- |
| id    | UUID | The id of the newly created monitor |

#### Delete Monitor

Deletes a monitor.

```
DELETE https://app.aporia.com/v1beta/monitors/<monitor_id>/
```

**Path Parameters**

| Parameter   | Description                      |
| ----------- | -------------------------------- |
| monitor\_id | The ID of the monitor to delete. |

#### Get Existing Environments

Return the defined environments.

```
GET https://app.aporia.com/v1beta/environments
```

```
{
    "environments": [
        {
            "id": "12345678-1234-1234-1234-1234567890abc",
            "name": "local-dev"
        }
    ]
}
```

**Request Parameters**

No parameters required for the request.

**Response**

Return "environments" list of objects with the following fields:

| Value | Type | Description                 |
| ----- | ---- | --------------------------- |
| id    | UUID | The id of the environment   |
| name  | str  | The name of the environment |

#### Get Model Tags

Returns all of the tags that were defined for a model.

```
GET https://app.aporia.com/v1beta/models/<model_id>/tags
```

```
{
    "tags": {
        "foo": "bar",
        "tag_key": "tag_value"
    }
}
```

**Path Parameters**

| Parameter | Description                                       |
| --------- | ------------------------------------------------- |
| model\_id | The ID of the model whose tags you wish to fetch. |

**Response**

| Value | Type            | Description                         |
| ----- | --------------- | ----------------------------------- |
| tags  | Dict\[str, str] | A mapping of tag keys to tag values |

#### Delete Model Tag

Deletes a single model tag.

```
DELETE https://app.aporia.com/v1beta/models/<model_id>/tags/<tag_key>
```

**Path Parameters**

| Parameter | Description                                       |
| --------- | ------------------------------------------------- |
| model\_id | The ID of the model whose tags you wish to fetch. |
| tag\_key  | The key of the tag to delete.                     |

#### Create Model Tags

Creates or updates model tags.

```
POST https://app.aporia.com/v1beta/models/<model_id>/tags
{
    "tags": {
        "tag_1": "value_1",
        "foo": "bar",
        "my tag key": "my-tag-value!"
    }
}
```

**Path Parameters**

| Parameter | Description                                       |
| --------- | ------------------------------------------------- |
| model\_id | The ID of the model whose tags you wish to fetch. |

**Request Parameters**

| Parameter | Type            | Required | Description                         |
| --------- | --------------- | -------- | ----------------------------------- |
| tags      | Dict\[str, str] | True     | A mapping of tag keys to tag values |

**Notes**

* Each model is restricted to 10 tags
* Tag keys are restricted to 15 characters, and may only contain letters, numbers, spaces, '-' and '\_'.
* Tag values are restricted to 100 characters, and may only contain letters, numbers and special characters
* If a tag key already exists, you can use this enpoint to update its value

#### Update Model Owner

Update the owner of an existing model.

```
POST https://app.aporia.com/v1beta/models/<model_id>/owner
{
    "owner": "owner@example.com"
}
```

**Path Parameters**

| Parameter | Description                                                      |
| --------- | ---------------------------------------------------------------- |
| model\_id | The ID of the model for which you would like to update an owner. |

**Request Parameters**

| Parameter | Type | Required | Description                                                      |
| --------- | ---- | -------- | ---------------------------------------------------------------- |
| owner     | str  | True     | The email of the model owner (must be a registered aporia user). |

**Response**

| Value     | Type | Description                           |
| --------- | ---- | ------------------------------------- |
| model\_id | str  | The ID of the model that was updated. |
| owner     | str  | The email of new model's owner.       |

#### Update Feature Positions

Update feature positions for an existing model version. Feature Positions are required for Explainability capabilities. In the console, to explain a datapoint, go to Model Overview -> Investigation Toolbox -> Datapoints and click Explain on a specific datapoint.

```
POST https://app.aporia.com/v1beta/models/{model_id}/versions/{model_version}/feature_positions
{
    "feature_positions":{
            "Age": 1,
            "Gender: 2
        }
}
```

**Path Parameters**

| Parameter      | Description                                                                 |
| -------------- | --------------------------------------------------------------------------- |
| model\_id      | The ID of the model for which you would like to update features' positions. |
| model\_version | The version for which you would like to update an features' positions.      |

**Request Parameters**

| Parameter          | Type | Required | Description                                                                              |
| ------------------ | ---- | -------- | ---------------------------------------------------------------------------------------- |
| feature\_positions | dict | True     | Mapping of feature names to feature positions in the dataframe which the model receives. |

**Notes**

* Features should be identical to the model schema.

#### Update Feature Importance

Update feature importance for an existing model version.

```
POST https://app.aporia.com/v1beta/models/{model_id}/versions/{model_version}/feature_importance
{
    "feature_importance":{
            "Age": 100,
            "Gender: 50
        }
}
```

**Path Parameters**

| Parameter      | Description                                                                  |
| -------------- | ---------------------------------------------------------------------------- |
| model\_id      | The ID of the model for which you would like to update features' importance. |
| model\_version | The version for which you would like to update an features' importance.      |

**Request Parameters**

| Parameter           | Type | Required | Description                                     |
| ------------------- | ---- | -------- | ----------------------------------------------- |
| feature\_importance | dict | True     | Mapping of feature names to feature importance. |

**Notes**

* Mapping of features from the scema and their importance is expected. Partial mappings are also supported.
* When using the API call, all previous reported feature importance values will be overridden.
