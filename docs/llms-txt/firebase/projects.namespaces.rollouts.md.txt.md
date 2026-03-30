# Source: https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.rollouts.md.txt

# REST Resource: projects.namespaces.rollouts

## Resource: Rollout

Representation of a rollout Experiment

| JSON representation |
|---|
| ``` { "name": string, "definition": { object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.rollouts#RolloutDefinition`) }, "state": enum (`https://firebase.google.com/docs/reference/remote-config/rest/v1/State`), "createTime": string, "startTime": string, "endTime": string, "lastUpdateTime": string, "etag": string } ``` |

| Fields ||
|---|---|
| `name` | `string` Identifier. The name of the rollout to get. Format: projects/{project}/namespaces/{namespace}/rollouts/{rolloutId} |
| `definition` | ``object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.rollouts#RolloutDefinition`)`` The rollout definition. |
| `state` | ``enum (`https://firebase.google.com/docs/reference/remote-config/rest/v1/State`)`` Output only. The experiment state of the rollout. Will only be RUNNING or DONE. |
| `createTime` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#timestamp` format)`` Output only. Create time of the rollout experiment. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. |
| `startTime` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#timestamp` format)`` Output only. Start time of the rollout experiment. It is always the same as the createTime. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. |
| `endTime` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#timestamp` format)`` Output only. End time of the rollout experiment. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. |
| `lastUpdateTime` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#timestamp` format)`` Output only. Last update time of the rollout experiment. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. |
| `etag` | `string` Etag for the Experiment which is generated using hash of updateTime. Can be filled during call to UpdateRollout to ensure that the correct version of the experiment is updated. This will ensure that there are no conflicting writes. If no `etag` is provided, then the update will over-write the experiment blindly. |

## RolloutDefinition

Definition to represent a rollout experiment.

| JSON representation |
|---|
| ``` { "displayName": string, "description": string, "controlVariant": { object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/ExperimentVariant`) }, "enabledVariant": { object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/ExperimentVariant`) } } ``` |

| Fields ||
|---|---|
| `displayName` | `string` Required. The display name of the rollout experiment. |
| `description` | `string` Optional. Text description of the rollout experiment. |
| `controlVariant` | ``object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/ExperimentVariant`)`` Required. This is the control variant of the rollout. It will always have weight of 1 and name set as "Control". |
| `enabledVariant` | ``object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/ExperimentVariant`)`` Required. This is the enabled variant of the rollout. It will always have weight of 1 and name set as "Enabled". |

| ## Methods ||
|---|---|
| ### `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.rollouts/delete` | Delete a rollout experiment. |
| ### `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.rollouts/get` | Get details about a rollout experiment. |
| ### `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects.namespaces.rollouts/list` | Get a list of all rollouts for a project. |