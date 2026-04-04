# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.md.txt

# firebase-admin.remote-config package

Firebase Remote Config.

## Functions

|                                                               Function                                                                |                                                                                                                                                                                            Description                                                                                                                                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [getRemoteConfig(app)](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.md#getremoteconfig_8a40afc) | Gets the [RemoteConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfig.md#remoteconfig_class) service for the default app or a given app.`getRemoteConfig()` can be called with no arguments to access the default app's `RemoteConfig` service or as `getRemoteConfig(app)` to access the `RemoteConfig` service associated with a specific app. |

## Classes

|                                                                                    Class                                                                                     |                                  Description                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [RemoteConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfig.md#remoteconfig_class)                                        | The Firebase `RemoteConfig` service interface.                                 |
| [RemoteConfigFetchResponse](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigfetchresponse.md#remoteconfigfetchresponse_class) | Represents a fetch response that can be used to interact with RC's client SDK. |

## Enumerations

|                                                                Enumeration                                                                 |                        Description                        |
|--------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| [CustomSignalOperator](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.md#customsignaloperator)         | Defines supported operators for custom signal conditions. |
| [PercentConditionOperator](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.md#percentconditionoperator) | Defines supported operators for percent conditions.       |

## Interfaces

|                                                                                      Interface                                                                                      |                                                                                                                                                                    Description                                                                                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AndCondition](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.andcondition.md#andcondition_interface)                                           | Represents a collection of conditions that evaluate to true if all are true.                                                                                                                                                                                                                                                                       |
| [CustomSignalCondition](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.customsignalcondition.md#customsignalcondition_interface)                | Represents a condition that compares provided signals against a target value.                                                                                                                                                                                                                                                                      |
| [ExplicitParameterValue](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.explicitparametervalue.md#explicitparametervalue_interface)             | Interface representing an explicit parameter value.                                                                                                                                                                                                                                                                                                |
| [FetchResponseData](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.fetchresponsedata.md#fetchresponsedata_interface)                            | JSON-serializable representation of evaluated config values. This can be consumed by Remote Config web client SDKs.                                                                                                                                                                                                                                |
| [GetServerTemplateOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.getservertemplateoptions.md#getservertemplateoptions_interface)       | Represents optional arguments that can be used when instantiating [ServerTemplate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplate.md#servertemplate_interface).                                                                                                                                 |
| [InAppDefaultValue](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.inappdefaultvalue.md#inappdefaultvalue_interface)                            | Interface representing an in-app-default value.                                                                                                                                                                                                                                                                                                    |
| [InitServerTemplateOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.initservertemplateoptions.md#initservertemplateoptions_interface)    | Represents optional arguments that can be used when instantiating [ServerTemplate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplate.md#servertemplate_interface) synchronously.                                                                                                                   |
| [ListVersionsOptions](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.listversionsoptions.md#listversionsoptions_interface)                      | Interface representing options for Remote Config list versions operation.                                                                                                                                                                                                                                                                          |
| [ListVersionsResult](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.listversionsresult.md#listversionsresult_interface)                         | Interface representing a list of Remote Config template versions.                                                                                                                                                                                                                                                                                  |
| [MicroPercentRange](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.micropercentrange.md#micropercentrange_interface)                            | Represents the limit of percentiles to target in micro-percents. The value must be in the range \[0 and 100000000\]                                                                                                                                                                                                                                |
| [NamedCondition](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.namedcondition.md#namedcondition_interface)                                     | Represents a Remote Config condition in the dataplane. A condition targets a specific group of users. A list of these conditions comprise part of a Remote Config template.                                                                                                                                                                        |
| [OneOfCondition](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.oneofcondition.md#oneofcondition_interface)                                     | Represents a condition that may be one of several types. Only the first defined field will be processed.                                                                                                                                                                                                                                           |
| [OrCondition](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.orcondition.md#orcondition_interface)                                              | Represents a collection of conditions that evaluate to true if any are true.                                                                                                                                                                                                                                                                       |
| [PercentCondition](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.percentcondition.md#percentcondition_interface)                               | Represents a condition that compares the instance pseudo-random percentile to a given limit.                                                                                                                                                                                                                                                       |
| [RemoteConfigCondition](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigcondition.md#remoteconfigcondition_interface)                | Interface representing a Remote Config condition. A condition targets a specific group of users. A list of these conditions make up part of a Remote Config template.                                                                                                                                                                              |
| [RemoteConfigParameter](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigparameter.md#remoteconfigparameter_interface)                | Interface representing a Remote Config parameter. At minimum, a `defaultValue` or a `conditionalValues` entry must be present for the parameter to have any effect.                                                                                                                                                                                |
| [RemoteConfigParameterGroup](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigparametergroup.md#remoteconfigparametergroup_interface) | Interface representing a Remote Config parameter group. Grouping parameters is only for management purposes and does not affect client-side fetching of parameter values.                                                                                                                                                                          |
| [RemoteConfigTemplate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfigtemplate.md#remoteconfigtemplate_interface)                   | Represents a Remote Config client template.                                                                                                                                                                                                                                                                                                        |
| [RemoteConfigUser](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfiguser.md#remoteconfiguser_interface)                               | Interface representing a Remote Config user.                                                                                                                                                                                                                                                                                                       |
| [ServerConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.serverconfig.md#serverconfig_interface)                                           | Represents the configuration produced by evaluating a server template.                                                                                                                                                                                                                                                                             |
| [ServerTemplate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplate.md#servertemplate_interface)                                     | Represents a stateful abstraction for a Remote Config server template.                                                                                                                                                                                                                                                                             |
| [ServerTemplateData](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplatedata.md#servertemplatedata_interface)                         | Represents the data in a Remote Config server template.                                                                                                                                                                                                                                                                                            |
| [Value](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.value.md#value_interface)                                                                | Wraps a parameter value with metadata and type-safe getters.Type-safe getters insulate application logic from remote changes to parameter names and types.                                                                                                                                                                                         |
| [Version](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.version.md#version_interface)                                                          | Interface representing a Remote Config template version. Output only, except for the version description. Contains metadata about a particular version of the Remote Config template. All fields are set at the time the specified Remote Config template is published. A version's description field may be specified in `publishTemplate` calls. |

## Type Aliases

|                                                                   Type Alias                                                                   |                                                                                                                                                                                                                  Description                                                                                                                                                                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [DefaultConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.md#defaultconfig)                           | Defines the format for in-app default parameter values.                                                                                                                                                                                                                                                                                                                                                                                       |
| [EvaluationContext](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.md#evaluationcontext)                   | Represents template evaluation input signals.                                                                                                                                                                                                                                                                                                                                                                                                 |
| [ParameterValueType](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.md#parametervaluetype)                 | Type representing a Remote Config parameter value data type. Defaults to `STRING` if unspecified.                                                                                                                                                                                                                                                                                                                                             |
| [PredefinedSignals](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.md#predefinedsignals)                   | Predefined template evaluation input signals.                                                                                                                                                                                                                                                                                                                                                                                                 |
| [RemoteConfigParameterValue](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.md#remoteconfigparametervalue) | Type representing a Remote Config parameter value. A `RemoteConfigParameterValue` could be either an `ExplicitParameterValue` or an `InAppDefaultValue`.                                                                                                                                                                                                                                                                                      |
| [ServerTemplateDataType](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.md#servertemplatedatatype)         | Represents the type of a Remote Config server template that can be set on [ServerTemplate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplate.md#servertemplate_interface). This can either be a [ServerTemplateData](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplatedata.md#servertemplatedata_interface) object or a template JSON string. |
| [TagColor](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.md#tagcolor)                                     | Colors that are associated with conditions for display purposes.                                                                                                                                                                                                                                                                                                                                                                              |
| [UserProvidedSignals](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.md#userprovidedsignals)               | Generic map of developer-defined signals used as evaluation input signals.                                                                                                                                                                                                                                                                                                                                                                    |
| [ValueSource](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.md#valuesource)                               | Indicates the source of a value. - "static" indicates the value was defined by a static constant. - "default" indicates the value was defined by default config. - "remote" indicates the value was defined by config produced by evaluating a template.                                                                                                                                                                                      |

## getRemoteConfig(app)

Gets the [RemoteConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfig.md#remoteconfig_class) service for the default app or a given app.

`getRemoteConfig()` can be called with no arguments to access the default app's `RemoteConfig` service or as `getRemoteConfig(app)` to access the `RemoteConfig` service associated with a specific app.

**Signature:**  

    export declare function getRemoteConfig(app?: App): RemoteConfig;

### Parameters

| Parameter | Type |                                                          Description                                                          |
|-----------|------|-------------------------------------------------------------------------------------------------------------------------------|
| app       | App  | Optional app for which to return the `RemoteConfig` service. If not provided, the default `RemoteConfig` service is returned. |

**Returns:**

[RemoteConfig](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.remoteconfig.md#remoteconfig_class)

The default `RemoteConfig` service if no app is provided, or the `RemoteConfig` service associated with the provided app.

### Example 1

    // Get the `RemoteConfig` service for the default app
    const defaultRemoteConfig = getRemoteConfig();

### Example 2

    // Get the `RemoteConfig` service for a given app
    const otherRemoteConfig = getRemoteConfig(otherApp);

## DefaultConfig

Defines the format for in-app default parameter values.

**Signature:**  

    export type DefaultConfig = {
        [key: string]: string | number | boolean;
    };

## EvaluationContext

Represents template evaluation input signals.

**Signature:**  

    export type EvaluationContext = UserProvidedSignals & PredefinedSignals;

## ParameterValueType

Type representing a Remote Config parameter value data type. Defaults to `STRING` if unspecified.

**Signature:**  

    export type ParameterValueType = 'STRING' | 'BOOLEAN' | 'NUMBER' | 'JSON';

## PredefinedSignals

Predefined template evaluation input signals.

**Signature:**  

    export type PredefinedSignals = {
        randomizationId?: string;
    };

## RemoteConfigParameterValue

Type representing a Remote Config parameter value. A `RemoteConfigParameterValue` could be either an `ExplicitParameterValue` or an `InAppDefaultValue`.

**Signature:**  

    export type RemoteConfigParameterValue = ExplicitParameterValue | InAppDefaultValue;

## ServerTemplateDataType

Represents the type of a Remote Config server template that can be set on [ServerTemplate](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplate.md#servertemplate_interface). This can either be a [ServerTemplateData](https://firebase.google.com/docs/reference/admin/node/firebase-admin.remote-config.servertemplatedata.md#servertemplatedata_interface) object or a template JSON string.

**Signature:**  

    export type ServerTemplateDataType = ServerTemplateData | string;

## TagColor

Colors that are associated with conditions for display purposes.

**Signature:**  

    export type TagColor = 'BLUE' | 'BROWN' | 'CYAN' | 'DEEP_ORANGE' | 'GREEN' | 'INDIGO' | 'LIME' | 'ORANGE' | 'PINK' | 'PURPLE' | 'TEAL';

## UserProvidedSignals

Generic map of developer-defined signals used as evaluation input signals.

**Signature:**  

    export type UserProvidedSignals = {
        [key: string]: string | number;
    };

## ValueSource

Indicates the source of a value.

- "static" indicates the value was defined by a static constant.
- "default" indicates the value was defined by default config.
- "remote" indicates the value was defined by config produced by evaluating a template.

**Signature:**  

    export type ValueSource = 'static' | 'default' | 'remote';

## CustomSignalOperator

Defines supported operators for custom signal conditions.

**Signature:**  

    export declare enum CustomSignalOperator 

## Enumeration Members

|             Member             |               Value                |                                                                       Description                                                                        |
|--------------------------------|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| NUMERIC_EQUAL                  | `"NUMERIC_EQUAL"`                  | Matches a numeric value equal to the target value.                                                                                                       |
| NUMERIC_GREATER_EQUAL          | `"NUMERIC_GREATER_EQUAL"`          | Matches a numeric value greater than or equal to the target value.                                                                                       |
| NUMERIC_GREATER_THAN           | `"NUMERIC_GREATER_THAN"`           | Matches a numeric value greater than the target value.                                                                                                   |
| NUMERIC_LESS_EQUAL             | `"NUMERIC_LESS_EQUAL"`             | Matches a numeric value less than or equal to the target value.                                                                                          |
| NUMERIC_LESS_THAN              | `"NUMERIC_LESS_THAN"`              | Matches a numeric value less than the target value.                                                                                                      |
| NUMERIC_NOT_EQUAL              | `"NUMERIC_NOT_EQUAL"`              | Matches a numeric value not equal to the target value.                                                                                                   |
| SEMANTIC_VERSION_EQUAL         | `"SEMANTIC_VERSION_EQUAL"`         | Matches if the actual version value is equal to the target value.                                                                                        |
| SEMANTIC_VERSION_GREATER_EQUAL | `"SEMANTIC_VERSION_GREATER_EQUAL"` | Matches if the actual version value is greater than or equal to the target value.                                                                        |
| SEMANTIC_VERSION_GREATER_THAN  | `"SEMANTIC_VERSION_GREATER_THAN"`  | Matches if the actual version value is greater than the target value.                                                                                    |
| SEMANTIC_VERSION_LESS_EQUAL    | `"SEMANTIC_VERSION_LESS_EQUAL"`    | Matches if the actual version value is less than or equal to the target value.                                                                           |
| SEMANTIC_VERSION_LESS_THAN     | `"SEMANTIC_VERSION_LESS_THAN"`     | Matches if the actual version value is less than the target value.                                                                                       |
| SEMANTIC_VERSION_NOT_EQUAL     | `"SEMANTIC_VERSION_NOT_EQUAL"`     | Matches if the actual version value is not equal to the target value.                                                                                    |
| STRING_CONTAINS                | `"STRING_CONTAINS"`                | Matches if at least one of the target values is a substring of the actual custom signal value (e.g. "abc" contains the string "a", "bc").                |
| STRING_CONTAINS_REGEX          | `"STRING_CONTAINS_REGEX"`          | The target regular expression matches at least one of the actual values. The regex conforms to RE2 format. See https://github.com/google/re2/wiki/Syntax |
| STRING_DOES_NOT_CONTAIN        | `"STRING_DOES_NOT_CONTAIN"`        | Matches if none of the target values is a substring of the actual custom signal value.                                                                   |
| STRING_EXACTLY_MATCHES         | `"STRING_EXACTLY_MATCHES"`         | Matches if the actual value exactly matches at least one of the target values.                                                                           |
| UNKNOWN                        | `"UNKNOWN"`                        | A catchall error case.                                                                                                                                   |

## PercentConditionOperator

Defines supported operators for percent conditions.

**Signature:**  

    export declare enum PercentConditionOperator 

## Enumeration Members

|    Member     |       Value       |                                                                                                                               Description                                                                                                                               |
|---------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BETWEEN       | `"BETWEEN"`       | Target percentiles within an interval defined by a lower bound and an upper bound. The lower bound is an exclusive (open) bound and the micro_percent_range_upper_bound is an inclusive (closed) bound. A condition using this operator must specify microPercentRange. |
| GREATER_THAN  | `"GREATER_THAN"`  | Target percentiles greater than the target percent. A condition using this operator must specify microPercent.                                                                                                                                                          |
| LESS_OR_EQUAL | `"LESS_OR_EQUAL"` | Target percentiles less than or equal to the target percent. A condition using this operator must specify microPercent.                                                                                                                                                 |
| UNKNOWN       | `"UNKNOWN"`       | A catchall error case.                                                                                                                                                                                                                                                  |