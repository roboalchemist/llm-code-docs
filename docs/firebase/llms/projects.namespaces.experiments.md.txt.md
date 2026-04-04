# Source: https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.experiments.md.txt

# REST Resource: projects.namespaces.experiments

## Resource: Experiment

used for returning experiments in the experiments.get call

| JSON representation |
|---|
| ``` { "name": string, "definition": { object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.experiments#ExperimentDefinition`) }, "state": enum (`https://firebase.google.com/docs/reference/remote-config/rest/v1/State`), "startTime": string, "endTime": string, "lastUpdateTime": string, "etag": string } ``` |

| Fields ||
|---|---|
| `name` | `string` Required. Identifier. The name of the experiment to get. Format: projects/{project}/namespaces/{namespace}/experiments/{experimentId} |
| `definition` | ``object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.experiments#ExperimentDefinition`)`` The experiment definition. |
| `state` | ``enum (`https://firebase.google.com/docs/reference/remote-config/rest/v1/State`)`` Output only. The experiment state. |
| `startTime` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#timestamp` format)`` Output only. The time when the experiment was started. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. |
| `endTime` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#timestamp` format)`` Output only. The time when the experiment was ended. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. |
| `lastUpdateTime` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#timestamp` format)`` Output only. The time when the experiment was last updated. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. |
| `etag` | `string` The etag of the experiment. |

## ExperimentDefinition

Defining ExperimentDefinition used in the message ExperimentDefinition

| JSON representation |
|---|
| ``` { "displayName": string, "description": string, "service": enum (`https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.experiments#ExperimentService`), "objectives": { object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.experiments#ExperimentObjectives`) }, "variants": [ { object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/ExperimentVariant`) } ] } ``` |

| Fields ||
|---|---|
| `displayName` | `string` The name of the experiment. |
| `description` | `string` The description of the experiment. |
| `service` | ``enum (`https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.experiments#ExperimentService`)`` The service that the experiment belongs to. |
| `objectives` | ``object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.experiments#ExperimentObjectives`)`` The objectives of the experiment. |
| `variants[]` | ``object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/ExperimentVariant`)`` The variants of the experiment. |

## ExperimentService

Defining ExperimentService used in the message ExperimentService

| Enums ||
|---|---|
| `EXPERIMENT_SERVICE_UNSPECIFIED` | The experiment service is unspecified. |
| `EXPERIMENT_SERVICE_REMOTE_CONFIG` | The Firebase Remote Config Service. |

## ExperimentObjectives

Defining ExperimentObjectives used in the message ExperimentObjectives

| JSON representation |
|---|
| ``` { "activationEvent": { object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.experiments#ActivationEvent`) }, "eventObjectives": [ { object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.experiments#EventObjective`) } ] } ``` |

| Fields ||
|---|---|
| `activationEvent` | ``object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.experiments#ActivationEvent`)`` Optional. The event which triggers the start of the experiment. If not specified, receiving an experiment on the device would count as the activation event. |
| `eventObjectives[]` | ``object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.experiments#EventObjective`)`` Required. The Objectives which are used to determine the winner of an experiment and measure desired outcomes. This must have between \[1-4\] objectives: one primary objective and a maximum of 3 secondary objectives. The order of the objectives does not matter. The server preserves the order. |

## ActivationEvent

An event which triggers the start of the experiment. This can be qualified with zero or more event parameters.

| JSON representation |
|---|
| ``` { "event": string } ``` |

| Fields ||
|---|---|
| `event` | `string` Optional. The Analytics even which indicates that the user has seen an experiment. This is case-sensitive and must be 0-32 characters long. It may only contain alphanumeric characters and underscores, and must start with an alphabetic character. The "firebase_" prefix is reserved and should not be used. |

## EventObjective

The objective used to measure the performance of an experiment. An experiment has a single primary objectives and multiple secondary objectives.

| JSON representation |
|---|
| ``` { "isPrimary": boolean, "abtOptimizationFunction": enum (`https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.experiments#AbtOptimizationFunction`), // Union field `objective_details` can be only one of the following: "customObjectiveDetails": { object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.experiments#CustomObjectiveDetails`) }, "systemObjectiveDetails": { object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.experiments#SystemObjectiveDetails`) } // End of list of possible types for union field `objective_details`. } ``` |

| Fields ||
|---|---|
| `isPrimary` | `boolean` Required. If true, this is the primary objective of the experiment. Exactly one objective should be marked primary. |
| `abtOptimizationFunction` | ``enum (`https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.experiments#AbtOptimizationFunction`)`` Required. How to optimize this metric. NOTE: This field should only be set for custom objectives. Always set to "MAXIMIZE" for "app_crashes" and "app_exception" objectives. |
| Union field `objective_details`. Required. Detailed specification of how to get the data for this objective. `objective_details` can be only one of the following: ||
| `customObjectiveDetails` | ``object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.experiments#CustomObjectiveDetails`)`` Configuration details for user-defined custom objectives. |
| `systemObjectiveDetails` | ``object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.experiments#SystemObjectiveDetails`)`` Configuration details for system objectives. |

## CustomObjectiveDetails

A custom objective for a user generated Scion event.

| JSON representation |
|---|
| ``` { "event": string, "countType": enum (`https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.experiments#CountType`) } ``` |

| Fields ||
|---|---|
| `event` | `string` Required. The name of the user-defined Firebase Analytics event to optimize. The event name is case-sensitive and must be 0-32 characters long. It may only contain alphanumeric characters and underscores, and must start with an alphabetic character. The "firebase_" prefix is reserved and should not be used. |
| `countType` | ``enum (`https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.experiments#CountType`)`` Required. Which countType is used to measure this objective. Always set to "NO_EVENT_USERS" for "app_crashes" and "app_exception" objectives. |

## CountType

The type of count used to measure the objective.

| Enums ||
|---|---|
| `COUNT_TYPE_UNSPECIFIED` | Default value. |
| `UNIQUE` | The objective is capped at 1 per user. |
| `NUM_OCCURRENCES` | Count number of occurrences of this event. |
| `NO_EVENT_USERS` | Count the number of users with zero occurrences of the event. |

## SystemObjectiveDetails

A pre-defined objective.

| JSON representation |
|---|
| ``` { "objective": string } ``` |

| Fields ||
|---|---|
| `objective` | `string` Required. One of the prefined system objective names, such as purchase_revenue. The name determines what to measure and how to count it. For example, app_exception measures the number of app_exception event, while unique_user:app_exception measures the number of unique users who who have had at least one app_exception event. |

## AbtOptimizationFunction

Any optimization function can be applied to the system or custom objectives

| Enums ||
|---|---|
| `ABT_OPTIMIZATION_FUNCTION_UNSPECIFIED` | Catch-all for unrecognized enum values. |
| `MAXIMIZE` | If more is good, maximize; eg. revenue related events |
| `MINIMIZE` | If less is good, minimize; eg. app crashes |

| ## Methods ||
|---|---|
| ### `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.experiments/delete` | Delete an experiment. |
| ### `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.experiments/get` | Get information about an existing experiment. |
| ### `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.experiments/list` | List all experiments for a project. |