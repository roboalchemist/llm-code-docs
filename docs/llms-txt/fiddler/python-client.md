# Source: https://docs.fiddler.ai/api/fiddler-python-client-sdk/python-client.md

# Introduction

**Version:** 3.10.0

## Overview

Complete API reference documentation for the fiddler package.

## Components

### Connection

Connection management and initialization

* [Connection](https://docs.fiddler.ai/api/fiddler-python-client-sdk/connection/connection)
* [ConnectionMixin](https://docs.fiddler.ai/api/fiddler-python-client-sdk/connection/connection-mixin)

### Constants

Constants module documentation

* [AlertCondition](https://docs.fiddler.ai/api/fiddler-python-client-sdk/constants/alert-condition)
* [AlertThresholdAlgo](https://docs.fiddler.ai/api/fiddler-python-client-sdk/constants/alert-threshold-algo)
* [BinSize](https://docs.fiddler.ai/api/fiddler-python-client-sdk/constants/bin-size)
* [CompareTo](https://docs.fiddler.ai/api/fiddler-python-client-sdk/constants/compare-to)
* [Priority](https://docs.fiddler.ai/api/fiddler-python-client-sdk/constants/priority)
* [BaselineType](https://docs.fiddler.ai/api/fiddler-python-client-sdk/constants/baseline-type)
* [WindowBinSize](https://docs.fiddler.ai/api/fiddler-python-client-sdk/constants/window-bin-size)
* [EnvType](https://docs.fiddler.ai/api/fiddler-python-client-sdk/constants/env-type)
* [JobStatus](https://docs.fiddler.ai/api/fiddler-python-client-sdk/constants/job-status)
* [ArtifactStatus](https://docs.fiddler.ai/api/fiddler-python-client-sdk/constants/artifact-status)
* [CustomFeatureType](https://docs.fiddler.ai/api/fiddler-python-client-sdk/constants/custom-feature-type)
* [DataType](https://docs.fiddler.ai/api/fiddler-python-client-sdk/constants/data-type)
* [ModelInputType](https://docs.fiddler.ai/api/fiddler-python-client-sdk/constants/model-input-type)
* [ModelTask](https://docs.fiddler.ai/api/fiddler-python-client-sdk/constants/model-task)
* [ArtifactType](https://docs.fiddler.ai/api/fiddler-python-client-sdk/constants/artifact-type)
* [DeploymentType](https://docs.fiddler.ai/api/fiddler-python-client-sdk/constants/deployment-type)
* [DownloadFormat](https://docs.fiddler.ai/api/fiddler-python-client-sdk/constants/download-format)
* [ExplainMethod](https://docs.fiddler.ai/api/fiddler-python-client-sdk/constants/explain-method)

### Entities

Core entity classes for interacting with the platform

* [AlertRecord](https://docs.fiddler.ai/api/fiddler-python-client-sdk/entities/alert-record)
* [AlertRule](https://docs.fiddler.ai/api/fiddler-python-client-sdk/entities/alert-rule)
* [Baseline](https://docs.fiddler.ai/api/fiddler-python-client-sdk/entities/baseline)
* [BaselineCompact](https://docs.fiddler.ai/api/fiddler-python-client-sdk/entities/baseline-compact)
* [CustomMetric](https://docs.fiddler.ai/api/fiddler-python-client-sdk/entities/custom-metric)
* [Segment](https://docs.fiddler.ai/api/fiddler-python-client-sdk/entities/segment)
* [Dataset](https://docs.fiddler.ai/api/fiddler-python-client-sdk/entities/dataset)
* [DatasetCompact](https://docs.fiddler.ai/api/fiddler-python-client-sdk/entities/dataset-compact)
* [File](https://docs.fiddler.ai/api/fiddler-python-client-sdk/entities/file)
* [Job](https://docs.fiddler.ai/api/fiddler-python-client-sdk/entities/job)
* [Model](https://docs.fiddler.ai/api/fiddler-python-client-sdk/entities/model)
* [ModelCompact](https://docs.fiddler.ai/api/fiddler-python-client-sdk/entities/model-compact)
* [ModelDeployment](https://docs.fiddler.ai/api/fiddler-python-client-sdk/entities/model-deployment)
* [Project](https://docs.fiddler.ai/api/fiddler-python-client-sdk/entities/project)
* [ProjectCompact](https://docs.fiddler.ai/api/fiddler-python-client-sdk/entities/project-compact)
* [Webhook](https://docs.fiddler.ai/api/fiddler-python-client-sdk/entities/webhook)

### Exceptions

Exceptions module documentation

* [ApiError](https://docs.fiddler.ai/api/fiddler-python-client-sdk/exceptions/api-error)
* [AsyncJobFailed](https://docs.fiddler.ai/api/fiddler-python-client-sdk/exceptions/async-job-failed)
* [Conflict](https://docs.fiddler.ai/api/fiddler-python-client-sdk/exceptions/conflict)
* [ConnError](https://docs.fiddler.ai/api/fiddler-python-client-sdk/exceptions/conn-error)
* [ConnTimeout](https://docs.fiddler.ai/api/fiddler-python-client-sdk/exceptions/conn-timeout)
* [HttpError](https://docs.fiddler.ai/api/fiddler-python-client-sdk/exceptions/http-error)
* [IncompatibleClient](https://docs.fiddler.ai/api/fiddler-python-client-sdk/exceptions/incompatible-client)
* [NotFound](https://docs.fiddler.ai/api/fiddler-python-client-sdk/exceptions/not-found)
* [Unsupported](https://docs.fiddler.ai/api/fiddler-python-client-sdk/exceptions/unsupported)

### Schemas

Schemas module documentation

* [CustomFeature](https://docs.fiddler.ai/api/fiddler-python-client-sdk/schemas/custom-feature)
* [Enrichment](https://docs.fiddler.ai/api/fiddler-python-client-sdk/schemas/enrichment)
* [ImageEmbedding](https://docs.fiddler.ai/api/fiddler-python-client-sdk/schemas/image-embedding)
* [Multivariate](https://docs.fiddler.ai/api/fiddler-python-client-sdk/schemas/multivariate)
* [TextEmbedding](https://docs.fiddler.ai/api/fiddler-python-client-sdk/schemas/text-embedding)
* [VectorFeature](https://docs.fiddler.ai/api/fiddler-python-client-sdk/schemas/vector-feature)
* [DeploymentParams](https://docs.fiddler.ai/api/fiddler-python-client-sdk/schemas/deployment-params)
* [Column](https://docs.fiddler.ai/api/fiddler-python-client-sdk/schemas/column)
* [ModelSchema](https://docs.fiddler.ai/api/fiddler-python-client-sdk/schemas/model-schema)
* [ModelSpec](https://docs.fiddler.ai/api/fiddler-python-client-sdk/schemas/model-spec)
* [ModelTaskParams](https://docs.fiddler.ai/api/fiddler-python-client-sdk/schemas/model-task-params)
* [DatasetDataSource](https://docs.fiddler.ai/api/fiddler-python-client-sdk/schemas/dataset-data-source)
* [EventIdDataSource](https://docs.fiddler.ai/api/fiddler-python-client-sdk/schemas/event-id-data-source)
* [RowDataSource](https://docs.fiddler.ai/api/fiddler-python-client-sdk/schemas/row-data-source)
* [XaiParams](https://docs.fiddler.ai/api/fiddler-python-client-sdk/schemas/xai-params)

### Utils

Utils module documentation

* [create\_columns\_from\_df](https://docs.fiddler.ai/api/fiddler-python-client-sdk/utils/create-columns-from-df)
* [group\_by](https://docs.fiddler.ai/api/fiddler-python-client-sdk/utils/group-by)
