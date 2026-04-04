# Source: https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineexecuteoptions.md.txt

# PipelineExecuteOptions interface

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Options defining Pipeline execution.

**Signature:**

    export declare interface PipelineExecuteOptions 

## Properties

| Property | Type | Description |
|---|---|---|
| [indexMode](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineexecuteoptions.md#pipelineexecuteoptionsindexmode) | 'recommended' | ***(Public Preview)*** Specify the index mode. |
| [pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineexecuteoptions.md#pipelineexecuteoptionspipeline) | [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class) | ***(Public Preview)*** Pipeline to be evaluated. |
| [rawOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipelineexecuteoptions.md#pipelineexecuteoptionsrawoptions) | { \[name: string\]: unknown; } | ***(Public Preview)*** An escape hatch to set options not known at SDK build time. These values will be passed directly to the Firestore backend and not used by the SDK.The option name will be used as provided. And must match the name format used by the backend (hint: use a snake_case_name).Custom option values can be any type supported by Firestore (for example: string, boolean, number, map, ...). Value types not known to the SDK will be rejected.Values specified in rawOptions will take precedence over any options with the same name set by the SDK. |

## PipelineExecuteOptions.indexMode

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Specify the index mode.

**Signature:**

    indexMode?: 'recommended';

## PipelineExecuteOptions.pipeline

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Pipeline to be evaluated.

**Signature:**

    pipeline: Pipeline;

## PipelineExecuteOptions.rawOptions

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

An escape hatch to set options not known at SDK build time. These values will be passed directly to the Firestore backend and not used by the SDK.

The option name will be used as provided. And must match the name format used by the backend (hint: use a snake_case_name).

Custom option values can be any type supported by Firestore (for example: string, boolean, number, map, ...). Value types not known to the SDK will be rejected.

Values specified in rawOptions will take precedence over any options with the same name set by the SDK.

**Signature:**

    rawOptions?: {
            [name: string]: unknown;
        };

### Example

Override the `example_option`:

      execute({
        pipeline: myPipeline,
        rawOptions: {
          // Override `example_option`. This will not
          // merge with the existing `example_option` object.
          "example_option": {
            foo: "bar"
          }
        }
      }

`rawOptions` supports dot notation, if you want to override a nested option.

      execute({
        pipeline: myPipeline,
        rawOptions: {
          // Override `example_option.foo` and do not override
          // any other properties of `example_option`.
          "example_option.foo": "bar"
        }
      }