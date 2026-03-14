# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/api/learn_api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.api.learn_api

## Classes

### LearnApi

```python  theme={"system"}
edgeimpulse_api.api.learn_api.LearnApi(
	api_client=None
)
```

| Parameters        |     |
| ----------------- | --- |
| `api_client=None` | ` ` |

***

**METHODS**

#### anomaly\_trained\_features

```python  theme={"system"}
edgeimpulse_api.api.learn_api.LearnApi.anomaly_trained_features(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	learn_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')],
	feature_ax1: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Feature axis 1')],
	feature_ax2: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Feature axis 2')],
	**kwargs
) ‑> edgeimpulse_api.models.anomaly_trained_features_response.AnomalyTrainedFeaturesResponse
```

Trained features

Get a sample of trained features, this extracts a number of samples and their features.

| Parameters    |                                                                                                                                                                  |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`        | ` `                                                                                                                                                              |
| `project_id`  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                   |
| `learn_id`    | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')]` |
| `feature_ax1` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Feature axis 1')]`                                               |
| `feature_ax2` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Feature axis 2')]`                                               |
| `**kwargs`    | ` `                                                                                                                                                              |

| Returns                                                                                   |
| ----------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.anomaly_trained_features_response.AnomalyTrainedFeaturesResponse` |

#### anomaly\_trained\_features\_per\_sample

```python  theme={"system"}
edgeimpulse_api.api.learn_api.LearnApi.anomaly_trained_features_per_sample(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	learn_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')],
	sample_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')],
	**kwargs
) ‑> edgeimpulse_api.models.anomaly_trained_features_response.AnomalyTrainedFeaturesResponse
```

Trained features for sample

Get trained features for a single sample. This runs both the DSP prerequisites and the anomaly classifier.

| Parameters   |                                                                                                                                                                  |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                              |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                   |
| `learn_id`   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')]` |
| `sample_id`  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Sample ID')]`                                                    |
| `**kwargs`   | ` `                                                                                                                                                              |

| Returns                                                                                   |
| ----------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.anomaly_trained_features_response.AnomalyTrainedFeaturesResponse` |

#### download\_keras\_data

```python  theme={"system"}
edgeimpulse_api.api.learn_api.LearnApi.download_keras_data(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	learn_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')],
	**kwargs
) ‑> str
```

Download Keras data export

Download the data of an exported Keras block - needs to be exported via 'exportKerasBlockData' first

| Parameters   |                                                                                                                                                                  |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                              |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                   |
| `learn_id`   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')]` |
| `**kwargs`   | ` `                                                                                                                                                              |

| Returns |
| ------- |
| `str`   |

#### download\_keras\_export

```python  theme={"system"}
edgeimpulse_api.api.learn_api.LearnApi.download_keras_export(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	learn_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')],
	**kwargs
) ‑> str
```

Download Keras export

Download an exported Keras block - needs to be exported via 'exportKerasBlock' first

| Parameters   |                                                                                                                                                                  |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                              |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                   |
| `learn_id`   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')]` |
| `**kwargs`   | ` `                                                                                                                                                              |

| Returns |
| ------- |
| `str`   |

#### download\_learn\_model

```python  theme={"system"}
edgeimpulse_api.api.learn_api.LearnApi.download_learn_model(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	learn_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')],
	model_download_id: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Model download ID, which can be obtained from the project information')],
	**kwargs
) ‑> str
```

Download trained model

Download a trained model for a learning block. Depending on the block this can be a TensorFlow model, or the cluster centroids.

| Parameters          |                                                                                                                                                                           |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`              | ` `                                                                                                                                                                       |
| `project_id`        | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                            |
| `learn_id`          | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')]`          |
| `model_download_id` | `Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Model download ID, which can be obtained from the project information')]` |
| `**kwargs`          | ` `                                                                                                                                                                       |

| Returns |
| ------- |
| `str`   |

#### download\_pretrained\_model

```python  theme={"system"}
edgeimpulse_api.api.learn_api.LearnApi.download_pretrained_model(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	pretrained_model_download_type: Annotated[str, Strict(strict=True)],
	impulse_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None,
	**kwargs
) ‑> str
```

Download pretrained model

Download a pretrained model file

| Parameters                       |                                                                                                                                                                                              |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                           | ` `                                                                                                                                                                                          |
| `project_id`                     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                               |
| `pretrained_model_download_type` | `Annotated[str, Strict(strict=True)]`                                                                                                                                                        |
| `impulse_id`                     | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None` |
| `**kwargs`                       | ` `                                                                                                                                                                                          |

| Returns |
| ------- |
| `str`   |

#### get\_anomaly

```python  theme={"system"}
edgeimpulse_api.api.learn_api.LearnApi.get_anomaly(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	learn_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')],
	**kwargs
) ‑> edgeimpulse_api.models.anomaly_config_response.AnomalyConfigResponse
```

Anomaly information

Get information about an anomaly block, such as its dependencies. Use the impulse blocks to find the learnId.

| Parameters   |                                                                                                                                                                  |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                              |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                   |
| `learn_id`   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')]` |
| `**kwargs`   | ` `                                                                                                                                                              |

| Returns                                                                |
| ---------------------------------------------------------------------- |
| `edgeimpulse_api.models.anomaly_config_response.AnomalyConfigResponse` |

#### get\_anomaly\_metadata

```python  theme={"system"}
edgeimpulse_api.api.learn_api.LearnApi.get_anomaly_metadata(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	learn_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')],
	**kwargs
) ‑> edgeimpulse_api.models.anomaly_model_metadata_response.AnomalyModelMetadataResponse
```

Anomaly metadata

Get metadata about a trained anomaly block. Use the impulse blocks to find the learnId.

| Parameters   |                                                                                                                                                                  |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                              |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                   |
| `learn_id`   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')]` |
| `**kwargs`   | ` `                                                                                                                                                              |

| Returns                                                                               |
| ------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.anomaly_model_metadata_response.AnomalyModelMetadataResponse` |

#### get\_gmm\_metadata

```python  theme={"system"}
edgeimpulse_api.api.learn_api.LearnApi.get_gmm_metadata(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	learn_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')],
	**kwargs
) ‑> edgeimpulse_api.models.anomaly_gmm_metadata_response.AnomalyGmmMetadataResponse
```

Anomaly GMM metadata

Get raw model metadata of the Gaussian mixture model (GMM) for a trained anomaly block. Use the impulse blocks to find the learnId.

| Parameters   |                                                                                                                                                                  |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                              |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                   |
| `learn_id`   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')]` |
| `**kwargs`   | ` `                                                                                                                                                              |

| Returns                                                                           |
| --------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.anomaly_gmm_metadata_response.AnomalyGmmMetadataResponse` |

#### get\_keras

```python  theme={"system"}
edgeimpulse_api.api.learn_api.LearnApi.get_keras(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	learn_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')],
	**kwargs
) ‑> edgeimpulse_api.models.keras_response.KerasResponse
```

Keras information

Get information about a Keras block, such as its dependencies. Use the impulse blocks to find the learnId.

| Parameters   |                                                                                                                                                                  |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                              |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                   |
| `learn_id`   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')]` |
| `**kwargs`   | ` `                                                                                                                                                              |

| Returns                                               |
| ----------------------------------------------------- |
| `edgeimpulse_api.models.keras_response.KerasResponse` |

#### get\_keras\_data\_explorer\_features

```python  theme={"system"}
edgeimpulse_api.api.learn_api.LearnApi.get_keras_data_explorer_features(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	learn_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')],
	**kwargs
) ‑> edgeimpulse_api.models.get_data_explorer_features_response.GetDataExplorerFeaturesResponse
```

Get data explorer features

t-SNE2 output of the raw dataset using embeddings from this Keras block

| Parameters   |                                                                                                                                                                  |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                              |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                   |
| `learn_id`   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')]` |
| `**kwargs`   | ` `                                                                                                                                                              |

| Returns                                                                                      |
| -------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_data_explorer_features_response.GetDataExplorerFeaturesResponse` |

#### get\_keras\_metadata

```python  theme={"system"}
edgeimpulse_api.api.learn_api.LearnApi.get_keras_metadata(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	learn_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')],
	exclude_labels: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='If set to "true", the "labels" field is left empty (which can be big on e.g. regression projects).')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.keras_model_metadata_response.KerasModelMetadataResponse
```

Keras metadata

Get metadata about a trained Keras block. Use the impulse blocks to find the learnId.

| Parameters       |                                                                                                                                                                                                                                   |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`           | ` `                                                                                                                                                                                                                               |
| `project_id`     | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                                    |
| `learn_id`       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')]`                                                                  |
| `exclude_labels` | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='If set to "true", the "labels" field is left empty (which can be big on e.g. regression projects).')] = None` |
| `**kwargs`       | ` `                                                                                                                                                                                                                               |

| Returns                                                                           |
| --------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.keras_model_metadata_response.KerasModelMetadataResponse` |

#### get\_learn\_x\_data

```python  theme={"system"}
edgeimpulse_api.api.learn_api.LearnApi.get_learn_x_data(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	learn_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')],
	**kwargs
) ‑> str
```

Download data

Download the processed data for this learning block. This is data already processed by the signal processing blocks.

| Parameters   |                                                                                                                                                                  |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                              |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                   |
| `learn_id`   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')]` |
| `**kwargs`   | ` `                                                                                                                                                              |

| Returns |
| ------- |
| `str`   |

#### get\_learn\_y\_data

```python  theme={"system"}
edgeimpulse_api.api.learn_api.LearnApi.get_learn_y_data(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	learn_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')],
	**kwargs
) ‑> str
```

Download labels

Download the labels for this learning block. This is data already processed by the signal processing blocks. Not all blocks support this function. If so, a GenericApiResponse is returned with an error message.

| Parameters   |                                                                                                                                                                  |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                              |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                   |
| `learn_id`   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')]` |
| `**kwargs`   | ` `                                                                                                                                                              |

| Returns |
| ------- |
| `str`   |

#### get\_pretrained\_model\_info

```python  theme={"system"}
edgeimpulse_api.api.learn_api.LearnApi.get_pretrained_model_info(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	impulse_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.get_pretrained_model_response.GetPretrainedModelResponse
```

Get pretrained model

Receive info back about the earlier uploaded pretrained model (via `uploadPretrainedModel`) input/output tensors. If you want to deploy a pretrained model from the API, see `startDeployPretrainedModelJob`.

| Parameters   |                                                                                                                                                                                              |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                          |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                               |
| `impulse_id` | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                          |

| Returns                                                                           |
| --------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_pretrained_model_response.GetPretrainedModelResponse` |

#### profile\_pretrained\_model

```python  theme={"system"}
edgeimpulse_api.api.learn_api.LearnApi.profile_pretrained_model(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	impulse_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Profile pretrained model

Returns the latency, RAM and ROM used for the pretrained model - upload first via  `uploadPretrainedModel`. This is using the project's selected latency device. Updates are streamed over the websocket API (or can be retrieved through the /stdout endpoint). Use getProfileTfliteJobResult to get the results when the job is completed.

| Parameters   |                                                                                                                                                                                              |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                                                          |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                               |
| `impulse_id` | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None` |
| `**kwargs`   | ` `                                                                                                                                                                                          |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |

#### save\_pretrained\_model\_parameters

```python  theme={"system"}
edgeimpulse_api.api.learn_api.LearnApi.save_pretrained_model_parameters(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	save_pretrained_model_request: edgeimpulse_api.models.save_pretrained_model_request.SavePretrainedModelRequest,
	impulse_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Save parameters for pretrained model

Save input / model configuration for a pretrained model. This overrides the current impulse. If you want to deploy a pretrained model from the API, see `startDeployPretrainedModelJob`.

| Parameters                      |                                                                                                                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                          | ` `                                                                                                                                                                                          |
| `project_id`                    | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                               |
| `save_pretrained_model_request` | `edgeimpulse_api.models.save_pretrained_model_request.SavePretrainedModelRequest`                                                                                                            |
| `impulse_id`                    | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None` |
| `**kwargs`                      | ` `                                                                                                                                                                                          |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### set\_anomaly

```python  theme={"system"}
edgeimpulse_api.api.learn_api.LearnApi.set_anomaly(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	learn_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')],
	set_anomaly_parameter_request: edgeimpulse_api.models.set_anomaly_parameter_request.SetAnomalyParameterRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Anomaly settings

Configure the anomaly block, such as its minimum confidence score. Use the impulse blocks to find the learnId.

| Parameters                      |                                                                                                                                                                  |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                          | ` `                                                                                                                                                              |
| `project_id`                    | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                   |
| `learn_id`                      | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')]` |
| `set_anomaly_parameter_request` | `edgeimpulse_api.models.set_anomaly_parameter_request.SetAnomalyParameterRequest`                                                                                |
| `**kwargs`                      | ` `                                                                                                                                                              |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### set\_keras

```python  theme={"system"}
edgeimpulse_api.api.learn_api.LearnApi.set_keras(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	learn_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')],
	set_keras_parameter_request: edgeimpulse_api.models.set_keras_parameter_request.SetKerasParameterRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Keras settings

Configure the Keras block, such as its minimum confidence score. Use the impulse blocks to find the learnId.

| Parameters                    |                                                                                                                                                                  |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                        | ` `                                                                                                                                                              |
| `project_id`                  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                   |
| `learn_id`                    | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')]` |
| `set_keras_parameter_request` | `edgeimpulse_api.models.set_keras_parameter_request.SetKerasParameterRequest`                                                                                    |
| `**kwargs`                    | ` `                                                                                                                                                              |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### start\_anomaly\_profile\_job

```python  theme={"system"}
edgeimpulse_api.api.learn_api.LearnApi.start_anomaly_profile_job(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	learn_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Start a profile job for an anomaly learn block

Starts an asynchronous profiling job, if there's no profiling information for the currently selected latency device. Afterwards, re-fetch model metadata to get the profiling job IDs.

| Parameters   |                                                                                                                                                                  |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                              |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                   |
| `learn_id`   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')]` |
| `**kwargs`   | ` `                                                                                                                                                              |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### start\_keras\_profile\_job

```python  theme={"system"}
edgeimpulse_api.api.learn_api.LearnApi.start_keras_profile_job(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	learn_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Start a profile job for a Keras learn block

Starts an asynchronous profiling job, if there's no profiling information for the currently selected latency device. Afterwards, re-fetch model metadata to get the profiling job IDs.

| Parameters   |                                                                                                                                                                  |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`       | ` `                                                                                                                                                              |
| `project_id` | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                   |
| `learn_id`   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Learn Block ID, use the impulse functions to retrieve the ID')]` |
| `**kwargs`   | ` `                                                                                                                                                              |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### test\_pretrained\_model

```python  theme={"system"}
edgeimpulse_api.api.learn_api.LearnApi.test_pretrained_model(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	test_pretrained_model_request: edgeimpulse_api.models.test_pretrained_model_request.TestPretrainedModelRequest,
	impulse_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.test_pretrained_model_response.TestPretrainedModelResponse
```

Test pretrained model

Test out a pretrained model (using raw features) - upload first via  `uploadPretrainedModel`. If you want to deploy a pretrained model from the API, see `startDeployPretrainedModelJob`.

| Parameters                      |                                                                                                                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                          | ` `                                                                                                                                                                                          |
| `project_id`                    | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                               |
| `test_pretrained_model_request` | `edgeimpulse_api.models.test_pretrained_model_request.TestPretrainedModelRequest`                                                                                                            |
| `impulse_id`                    | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None` |
| `**kwargs`                      | ` `                                                                                                                                                                                          |

| Returns                                                                             |
| ----------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.test_pretrained_model_response.TestPretrainedModelResponse` |

#### test\_pretrained\_model\_images

```python  theme={"system"}
edgeimpulse_api.api.learn_api.LearnApi.test_pretrained_model_images(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	test_pretrained_model_images_request: edgeimpulse_api.models.test_pretrained_model_images_request.TestPretrainedModelImagesRequest,
	impulse_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.test_pretrained_model_response.TestPretrainedModelResponse
```

Test pretrained model using image data

Test out a pretrained model (using image data) - upload first via  `uploadPretrainedModel`. If you want to deploy a pretrained model from the API, see `startDeployPretrainedModelJob`. This will transform raw image data (e.g. RGB to grayscale, resize) before classifying. To classify raw features, see `testPretrainedModel`.

| Parameters                             |                                                                                                                                                                                              |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                                 | ` `                                                                                                                                                                                          |
| `project_id`                           | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                               |
| `test_pretrained_model_images_request` | `edgeimpulse_api.models.test_pretrained_model_images_request.TestPretrainedModelImagesRequest`                                                                                               |
| `impulse_id`                           | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None` |
| `**kwargs`                             | ` `                                                                                                                                                                                          |

| Returns                                                                             |
| ----------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.test_pretrained_model_response.TestPretrainedModelResponse` |

#### upload\_pretrained\_model

```python  theme={"system"}
edgeimpulse_api.api.learn_api.LearnApi.upload_pretrained_model(
	self,
	project_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')],
	model_file: Annotated[str, Strict(strict=True)],
	model_file_name: Annotated[str, Strict(strict=True)],
	model_file_type: Annotated[str, Strict(strict=True)],
	impulse_id: Annotated[Annotated[int, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None,
	representative_features: Annotated[str, Strict(strict=True)] | None = None,
	device: Annotated[Annotated[str, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='MCU used for calculating latency, query `latencyDevices` in `listProject` for a list of supported devices (and use the \\"mcu\\" property here). If this is kept empty then we\'ll show an overview of multiple devices.')] = None,
	override_input_shape: Annotated[List[Annotated[int, Strict(strict=True)]] | None, FieldInfo(annotation=NoneType, required=True, description="Optional for ONNX files: overrides the input shape of the model. This is highly suggested if the model has dynamic dimensions. If this field is not set, then all dynamic dimensions will be set to '1'.")] = None,
	**kwargs
) ‑> edgeimpulse_api.models.start_job_response.StartJobResponse
```

Upload a pretrained model

Upload a pretrained model and receive info back about the input/output tensors. If you want to deploy a pretrained model from the API, see `startDeployPretrainedModelJob`.

| Parameters                |                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `self`                    | ` `                                                                                                                                                                                                                                                                                                                                                    |
| `project_id`              | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Project ID')]`                                                                                                                                                                                                                                         |
| `model_file`              | `Annotated[str, Strict(strict=True)]`                                                                                                                                                                                                                                                                                                                  |
| `model_file_name`         | `Annotated[str, Strict(strict=True)]`                                                                                                                                                                                                                                                                                                                  |
| `model_file_type`         | `Annotated[str, Strict(strict=True)]`                                                                                                                                                                                                                                                                                                                  |
| `impulse_id`              | `Annotated[Annotated[int, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='Impulse ID. If this is unset then the default impulse is used.')] = None`                                                                                                                                                           |
| `representative_features` | `Annotated[str, Strict(strict=True)] \| None = None`                                                                                                                                                                                                                                                                                                   |
| `device`                  | `Annotated[Annotated[str, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='MCU used for calculating latency, query `latencyDevices` in `listProject` for a list of supported devices (and use the \\"mcu\\" property here). If this is kept empty then we\'ll show an overview of multiple devices.')] = None` |
| `override_input_shape`    | `Annotated[List[Annotated[int, Strict(strict=True)]] \| None, FieldInfo(annotation=NoneType, required=True, description="Optional for ONNX files`                                                                                                                                                                                                      |
| `**kwargs`                | ` `                                                                                                                                                                                                                                                                                                                                                    |

| Returns                                                      |
| ------------------------------------------------------------ |
| `edgeimpulse_api.models.start_job_response.StartJobResponse` |


Built with [Mintlify](https://mintlify.com).