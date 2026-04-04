# Source: https://firebase.google.com/docs/reference/ai-logic/rest/v1beta/projects.locations.templates/templatePredict.md.txt

# Method: projects.locations.templates.templatePredict

Perform an online prediction using a server-side prompt template.

### HTTP request

`POST https://firebasevertexai.googleapis.com/v1beta/{name=projects/*/locations/*/templates/*}:templatePredict`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

| Parameters ||
|---|---|
| `name` | `string` Required. Name of the template to use in the request. projects/project-id/location/location-name/template/template-id |

### Request body

The request body contains data with the following structure:

| JSON representation |
|---|
| ``` { "inputs": { object } } ``` |

| Fields ||
|---|---|
| `inputs` | ``object (`https://protobuf.dev/reference/protobuf/google.protobuf#struct` format)`` Optional. Client provided data that can be used when rendering the template. When calling via JSON/http surfaces this should be wire compatible with an arbitrary JSON object. |

### Response body

Response message for `PredictionService.Predict`.

If successful, the response body contains data with the following structure:

| JSON representation |
|---|
| ``` { "predictions": [ value ], "deployedModelId": string, "model": string, "modelVersionId": string, "modelDisplayName": string, "metadata": value } ``` |

| Fields ||
|---|---|
| `predictions[]` | ``value (`https://protobuf.dev/reference/protobuf/google.protobuf#value` format)`` The predictions that are the output of the predictions call. The schema of any single prediction may be specified via Endpoint's DeployedModels' \[Model's \]\[DeployedModel.model\] \[PredictSchemata's\]\[Model.predict_schemata\] \[prediction_schema_uri\]\[PredictSchemata.prediction_schema_uri\]. |
| `deployedModelId` | `string` ID of the Endpoint's DeployedModel that served this prediction. |
| `model` | `string` Output only. The resource name of the Model which is deployed as the DeployedModel that this prediction hits. |
| `modelVersionId` | `string` Output only. The version ID of the Model which is deployed as the DeployedModel that this prediction hits. |
| `modelDisplayName` | `string` Output only. The \[display name\]\[Model.display_name\] of the Model which is deployed as the DeployedModel that this prediction hits. |
| `metadata` | ``value (`https://protobuf.dev/reference/protobuf/google.protobuf#value` format)`` Output only. Request-level metadata returned by the model. The metadata type will be dependent upon the model implementation. |

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [OAuth 2.0 Overview](https://developers.google.com/identity/protocols/OAuth2).