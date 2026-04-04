# Source: https://firebase.google.com/docs/reference/js/firestore_pipelines.stageoptions.md.txt

# StageOptions interface

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Options defining how a Stage is evaluated.

**Signature:**

    export declare interface StageOptions 

## Properties

| Property | Type | Description |
|---|---|---|
| [rawOptions](https://firebase.google.com/docs/reference/js/firestore_pipelines.stageoptions.md#stageoptionsrawoptions) | { \[name: string\]: unknown; } | ***(Public Preview)*** An escape hatch to set options not known at SDK build time. These values will be passed directly to the Firestore backend and not used by the SDK.The option name will be used as provided. And must match the name format used by the backend (hint: use a snake_case_name).Raw option values can be any type supported by Firestore (for example: string, boolean, number, map, ...). Value types not known to the SDK will be rejected.Values specified in rawOptions will take precedence over any options with the same name set by the SDK.`rawOptions` supports dot notation, if you want to override a nested option. |

## StageOptions.rawOptions

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

An escape hatch to set options not known at SDK build time. These values will be passed directly to the Firestore backend and not used by the SDK.

The option name will be used as provided. And must match the name format used by the backend (hint: use a snake_case_name).

Raw option values can be any type supported by Firestore (for example: string, boolean, number, map, ...). Value types not known to the SDK will be rejected.

Values specified in rawOptions will take precedence over any options with the same name set by the SDK.

`rawOptions` supports dot notation, if you want to override a nested option.

**Signature:**

    rawOptions?: {
            [name: string]: unknown;
        };