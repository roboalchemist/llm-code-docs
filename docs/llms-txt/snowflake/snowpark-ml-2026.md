# Source: https://docs.snowflake.com/en/release-notes/clients-drivers/snowpark-ml-2026.md

# Snowflake ML Python release notes

This article contains the release notes for the Snowflake ML Python, including the following when applicable:

* Behavior changes
* New features
* Customer-facing bug fixes

> **Note:**
>
> These notes do not include changes in features that have not been publicly announced.
> Such features might appear in the Snowflake ML Python source code but not in the public documentation.

See [Snowflake ML: End-to-End Machine Learning](../../developer-guide/snowflake-ml/overview.md) for documentation.

## Verifying the `snowflake-ml-python` package

All Snowflake packages are signed, allowing you to verify their origin. To verify the `snowflake.ml.python` package, follow the steps below:

1. Install `cosign`. This example uses the Go installation:
   [Installing cosign with Go](https://edu.chainguard.dev/open-source/sigstore/cosign/how-to-install-cosign/#installing-cosign-with-go).
2. Download the file from a repository such as [PyPi](https://pypi.org/project/snowflake-ml-python/#files).
3. Download a `.sig` file for that release from the GitHub [releases page](https://github.com/snowflakedb/snowflake-ml-python/releases/).
4. Verify the signature using `cosign`. For example:

```bash
cosign verify-blob snowflake_ml_python-1.27.0.tar.gz --key snowflake-ml-python-1.27.0.pub --signature resources.linux.snowflake_ml_python-1.27.0.tar.gz.sig

cosign verify-blob snowflake_ml_python-1.27.0.tar.gz --key snowflake-ml-python-1.27.0.pub --signature resources.linux.snowflake_ml_python-1.27.0.tar.gz.sig
```

> **Note:**
>
> This example uses the library and signature for version 1.27.0 of the package. Use the filenames of the version you are verifying.

## Deprecation notices

* `snowflake.ml.fileset.FileSet` has been deprecated and will be removed in a future release. Use
  [snowflake.ml.dataset.Dataset](../../developer-guide/snowflake-ml/dataset.md) and
  [snowflake.ml.data.DataConnector](/developer-guide/snowpark-ml/reference/latest/api/data/snowflake.ml.data.data_connector.DataConnector) instead.
* The “CamelCase” function names in `snowflake.ml.cortex` have been deprecated and will be removed in a future
  release. Use the “snake_case” names for these functions instead. For example, use `classify_text` instead of
  `ClassifyText`.
* The `partitioned_inference_api` decorator has been deprecated and will be removed in a future release. Use `custom_model.partitioned_api` instead.
* The `additional_payloads` argument of the `MLJob.submit_*` methods has been deprecated and will be removed in a future release.
  Use the `imports` argument instead.
* The `snowflake.ml.model.models.huggingface_pipeline.HuggingfacePipelineModel` class has been deprecated and will be removed in a future release.

## Version 1.27.0 (2026-02-12)

### Bug fixes

Model Registry bug fixes:

* Fixed failure of `model_version.run` caused by requiring READ privilege on the model instead of USAGE when the
  user’s role had only the USAGE privilege.

Feature store bug fixes:

* Fixed failure of `register_feature_view` with `overwrite=True` when the existing feature view is external and the
  new feature view is managed, or vice versa.

## Version 1.26.0 (2026-02-05)

### New features

New Model Registry features:

* Model signatures can now include inference parameters via `ParamSpec`, allowing you to define
  constant parameters to be passed at inference time without including them in the input data.
  Example:

  ```python
  import pandas as pd
  from snowflake.ml.model import custom_model, model_signature
  from snowflake.ml.registry import Registry

  # Define a custom model with inference parameters
  class MyModelWithParams(custom_model.CustomModel):
      @custom_model.inference_api
      def predict(
          self,
          input_df: pd.DataFrame,
          *,
          temperature: float = 1.0,  # keyword-only param with default
      ) -> pd.DataFrame:
          return pd.DataFrame({"output": input_df["feature"] * temperature})

  # Create sample data
  model = MyModelWithParams(custom_model.ModelContext())
  sample_input = pd.DataFrame({"feature": [1.0, 2.0, 3.0]})
  sample_output = model.predict(sample_input, temperature=1.0)

  # Define ParamSpec for the inference parameter
  params = [
      model_signature.ParamSpec(
          name="temperature",
          dtype=model_signature.DataType.FLOAT,
          default_value=1.0,
      ),
  ]

  # Infer signature with params
  sig = model_signature.infer_signature(
      input_data=sample_input,
      output_data=sample_output,
      params=params,
  )

  # Log model with the signature
  registry = Registry(session)
  mv = registry.log_model(
      model=model,
      model_name="my_model_with_params",
      version_name="v1",
      signatures={"predict": sig},
  )

  # Run inference with custom parameter value
  result = mv.run(sample_input, function_name="predict", params={"temperature": 2.0})
  ```

New Feature Store features:

* New `auto_prefix` parameter and `with_name` method to prevent column name collisions when joining multiple feature
  views in dataset generation.
* Dynamic Iceberg tables can now be used as backing storage for Feature Views. Use `StorageConfig` with
  `StorageFormat.ICEBERG` to store data in Apache Iceberg format on external cloud storage. A new
  `default_iceberg_external_volume` parameter is available in `FeatureStore` to set a default external volume for
  Iceberg feature views.

## Version 1.25.1 (2026-02-03)

No public-facing changes. This release includes changes to a preview feature that has not been publicly announced.

## Version 1.25.0 (2026-01-28)

### New features

New Model Serving features:

* The `create_service` method accepts a new `autocapture` argument to indicate whether inference data should be captured
  (see [Autocapture inference logs for realtime inference](../../developer-guide/snowflake-ml/inference/auto-capture-inference-logs.md)).
* The `create_service` and `log_model_and_create_service` methods now accept an optional `min_instances` argument
  to specify the minimum number of instances for the service. The service automatically scales between the specified
  minimum and maximum instances based on traffic and hardware utilization. If `min_instances` is 0, the service
  automatically suspends when no traffic is detected for a period of time. The default value for `min_instances` is 0.

## Version 1.24.0 (2026-01-22)

### New features

New Feature Store features:

* Tile-based aggregation support using a new `Feature` API for efficient and point-in-time correct time-series
  feature computation using pre-computed tiles.

New Model Registry features:

* SentenceTransformer models now support automatic signature inference. When logging a SentenceTransformer model,
  `sample_input_data` is optional. The signature is automatically inferred from the model’s embedding dimension when
  sample input data is not provided.. The `encode`, `encode_query`, `encode_document`, `encode_queries`,
  `encode_documents` methods are supported.

  ```python
  import sentence_transformers
  from snowflake.ml.registry import Registry

  # Create model
  model = sentence_transformers.SentenceTransformer("all-MiniLM-L6-v2")

  # Log model without sample_input_data - signature is auto-inferred
  registry = Registry(session)
  mv = registry.log_model(
      model=model,
      model_name="my_sentence_transformer",
      version_name="v1",
  )

  # Run inference with auto-inferred signature (input: "text", output: "output")
  import pandas as pd
  result = mv.run(pd.DataFrame({"text": ["Hello world"]}))
  ```

## Version 1.23.0 (2026-01-165)

### New features

New ML Jobs features:

* ML Jobs now support Python 3.11 and Python 3.12. Jobs automatically select a runtime environment
  matching the client Python version.

### Bug fixes

Model Registry bug fixes:

* Empty output in HuggingFace’s Token Classification (Named Entity Recognition) models no longer causes failures.

Model Serving bug fixes:

* Container statuses are now correctly reported and should not be blank.

## Version 1.22.0 (2026-01-09)

### New features

New Model Registry features:

* You can now remotely log a transformer pipeline model using a Snowpark Container Services (SPCS) job.

  ```python
  # create reference to the model
  model = huggingface.TransformersPipeline(
      model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
      task="text-generation",
  )

  # Remotely log the model, a SPCS job will run async and log the model
  mv = registry.log_model(
      model=model,
      model_name="tinyllama_remote_log",
      target_platforms=["SNOWPARK_CONTAINER_SERVICES"],
      signatures=openai_signatures.OPENAI_CHAT_SIGNATURE,
  )
  ```

## Version 1.21.0 (2026-01-05)

### Behavior changes

ML Jobs behavior changes:

* The behavior of the `additional_payloads` parameter is changing. Use the `imports` argument to declare additional
  dependencies, such as ZIP files and Python modules. Local directories and Python files are automatically compressed,
  and their internal layout is determined by the specified import path. The import path applies only to local
  directories, Python files, and staged python files; it has no effect on other import types. When referencing files in a
  stage, only individual files are supported, not directories.

Experiment Tracking behavior changes:

* `ExperimentTracking` is now a singleton class.

### Bug fixes

Experiment Tracking bug fixes:

* Reaching the run metadata size limit in `log_metrics` or `log_params` now issues a warning instead of raising an exception.

Model Registry bug fixes:

* `ModelVersion.run` now raises a `ValueError` if the model is a SPCS-only model and `service_name` is not provided.

### New preview features

* The `create_service` method now accepts the Boolean argument `autocapture` to indicate whether inference data is automatically captured.

### New release features

New Model Registry features:

* The new `snowflake.ml.model.models.huggingface.TransformersPipeline` class is intended to replace `snowflake.ml.model.models.huggingface_pipeline.HuggingfacePipelineModel`,
  although the older class is not yet deprecated. The new class knows model signatures for common tasks so that you do not need to specify them manually.
  The supported tasks are currently:

  * `fill-mask`
  * `question-answering`
  * `summarization`
  * `table-question-answering`
  * `text2text-generation`
  * `text-classification` (alias `sentiment-analysis`)
  * `text-generation`
  * `token-classification` (alias `ner`)
  * `translation`
  * `translation_xx_to_yy`
  * `zero-shot-classification` (lets you log models without loading them into memory)
* The `list_services` API now shows an internal endpoint that can be called from another SPCS node or notebook without Enterprise Application Integration.
  It also indicates whether autocapture is enabled for each service.

New DataConnector features:

* New `to_huggingface_dataset` method converts Snowflake data to HuggingFace datasets. Supports both in-memory
  `Dataset` (`streaming=False`) and streaming `IterableDataset` (`streaming=True`) modes.

### Deprecation notices

* The `snowflake.ml.model.models.huggingface_pipeline.HuggingfacePipelineModel` class has been deprecated and will be removed in a future release.
