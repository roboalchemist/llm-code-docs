# Source: https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig.md.txt

# RemoteConfig

\* A RemoteConfig represents a Remote Config template.

A project's Remote Config template is evaluated during each application instance's fetch.

Note: Server templates currently support percentage conditions. Publishing a server template with unsupported conditional values will return a validation error. See [Remote Config in Server Environments](https://firebase.google.com/docs/remote-config/server) for more information.

The resolved value of a parameter is determined as follows:

Given the `https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#RemoteConfigParameter.FIELDS.conditional_values` that refer to `true` `https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#FIELDS.conditions` for the application instance, the parameter's resolved value is the conditional value whose `https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#RemoteConfigCondition.FIELDS.name` is the earliest in the `https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#FIELDS.conditions`.

Else, if the parameter has a `https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#RemoteConfigParameter.FIELDS.default_value`, the resolved value is set to the default value.

Else, the parameter has no value and is omitted from the result that the application instance fetches.

For example, assume we have parameter key `fruit`, with default value `pear` and conditional value submap `{"is_ios": "apple", "is_in_20_percent":
"banana"}` where `"is_ios"` and `"is_20_percent"` are names of conditions in the ordered condition list. The value of `fruit` would evaluate to `apple` if `is_ios` is true. Otherwise, if `is_in_20_percent` is `true`, `fruit` would evaluate to `banana`, and if `is_ios` and `is_in_20_percent` are both false, `fruit` would evaluate to `pear`. If no default value were specified, and `is_ios` and `is_in_20_percent` were both false, no value for `fruit` would be returned from the Remote Config server to the client.

Once a project's Remote Config template has been published via a successful `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects/updateRemoteConfig#google.firebase.remoteconfig.v1.RemoteConfigService.UpdateRemoteConfig` call, clients can fetch these parameter values and display them to users.

| JSON representation |
|---|
| ``` { "conditions": [ { object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#RemoteConfigCondition`) } ], "parameters": { string: { object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#RemoteConfigParameter`) }, ... }, "version": { object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/Version`) }, "parameterGroups": { string: { object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#RemoteConfigParameterGroup`) }, ... } } ``` |

| Fields ||
|---|---|
| `conditions[]` | ``object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#RemoteConfigCondition`)`` A list of conditions in descending order by priority. The values of the `https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#RemoteConfigCondition.FIELDS.name` entries must be unique. |
| `parameters` | ``map (key: string, value: object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#RemoteConfigParameter`))`` Map of parameter keys to their optional default values and optional conditional values. An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`. |
| `version` | ``object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/Version`)`` Output only, except for the version `https://firebase.google.com/docs/reference/remote-config/rest/v1/Version#FIELDS.description`. Metadata associated with a particular version of a template. A version's description field may be specified in `https://firebase.google.com/docs/reference/remote-config/rest/v1/projects/updateRemoteConfig#google.firebase.remoteconfig.v1.RemoteConfigService.UpdateRemoteConfig` calls. |
| `parameterGroups` | ``map (key: string, value: object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#RemoteConfigParameterGroup`))`` Map of parameter group names to their descriptions and grouped parameters. A group's name is mutable but must be unique among groups in the config. The name is limited to 256 characters and intended to be human-readable. Any Unicode characters are allowed. Groups have a list of parameters which allows users of the API to group parameters that are associated with the same feature or theme together for easy organizational access. For example, a parameter group with the name "Search V2" may have the `description` "New mobile search view" and contain parameters for the new search's layout and font. An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`. |

## RemoteConfigCondition

A condition targeting a specific group of users. A list of these conditions make up part of a RemoteConfig object.

| JSON representation |
|---|
| ``` { "name": string, "expression": string, "tagColor": enum (`https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#ConditionDisplayColor`) } ``` |

| Fields ||
|---|---|
| `name` | `string` Required. A non-empty and unique name of this condition. |
| `expression` | `string` Required. The logic of this condition. See the documentation regarding [Condition Expressions](https://firebase.google.com/docs/remote-config/condition-reference) for the expected syntax of this field. |
| `tagColor` | ``enum (`https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#ConditionDisplayColor`)`` Optional. The color associated with this condition for display purposes in the Firebase Console. Not specifying this value or having "CONDITION_DISPLAY_COLOR_UNSPECIFIED" results in the Console picking an arbitrary color to associate with the condition. |

## ConditionDisplayColor

- List of colors that are associated with Conditions for display purposes.

| Enums ||
|---|---|
| `CONDITION_DISPLAY_COLOR_UNSPECIFIED` | Catch-all for unrecognized enum values. |
| `BLUE` | Blue |
| `BROWN` | Brown |
| `CYAN` | Cyan |
| `DEEP_ORANGE` | aka "Red Orange" |
| `GREEN` | Green |
| `INDIGO` | Indigo |
| `LIME` | Lime |
| `ORANGE` | Orange |
| `PINK` | Pink |
| `PURPLE` | Purple |
| `TEAL` | Teal |

## RemoteConfigParameter

A parameter value associated with a parameter key in `https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#FIELDS.parameters`.

At minimum, a `defaultValue` or a `conditionalValues` entry should be present for the parameter to have any effect.

| JSON representation |
|---|
| ``` { "defaultValue": { object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#RemoteConfigParameterValue`) }, "conditionalValues": { string: { object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#RemoteConfigParameterValue`) }, ... }, "description": string, "valueType": enum (`https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#ParameterValueType`) } ``` |

| Fields ||
|---|---|
| `defaultValue` | ``object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#RemoteConfigParameterValue`)`` Optional - value to set the parameter to, when none of the named conditions evaluate to `true`. |
| `conditionalValues` | ``map (key: string, value: object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#RemoteConfigParameterValue`))`` Optional - a (`https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#RemoteConfigCondition.FIELDS.name`, value) map. The condition_name of the highest priority (the one listed first in the RemoteConfig's conditions list) determines the value of this parameter. An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`. |
| `description` | `string` Optional. A description for this Parameter. Its length must be less than or equal to 256 characters . A description may contain any Unicode characters. |
| `valueType` | ``enum (`https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#ParameterValueType`)`` The data type for all values of this parameter in the current version of the template. Defaults to `ParameterValueType.STRING` if unspecified. |

## RemoteConfigParameterValue

A RemoteConfigParameterValue resource contains the value that a parameter may have.

| JSON representation |
|---|
| ``` { // Union field `value_option` can be only one of the following: "value": string, "useInAppDefault": boolean, "personalizationValue": { object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#PersonalizationValue`) }, "experimentValue": { object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#ExperimentValue`) }, "rolloutValue": { object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#RolloutValue`) } // End of list of possible types for union field `value_option`. } ``` |

| Fields ||
|---|---|
| Union field `value_option`. A RemoteConfigParameterValue consists of either a string (value) or a boolean (use_in_app_default, set to true if applicable). `value_option` can be only one of the following: ||
| `value` | `string` The string value that the parameter is set to. |
| `useInAppDefault` | `boolean` If true, the parameter is omitted from the parameter values returned to a client. |
| `personalizationValue` | ``object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#PersonalizationValue`)`` A dynamic, user-specific value computed when config is fetched. |
| `experimentValue` | ``object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#ExperimentValue`)`` A dynamic value managed by the Firebase ABT Experiment service. |
| `rolloutValue` | ``object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#RolloutValue`)`` A dynamic Rollout value managed by the Firebase ABT Experiment service. |

## PersonalizationValue

Contains the necessary information to fetch a personalized value.

| JSON representation |
|---|
| ``` { "personalizationId": string } ``` |

| Fields ||
|---|---|
| `personalizationId` | `string` Identifier that represents a personalization definition. This definition is used to resolve the value at config fetch time. This system-generated value should not be modified. |

## ExperimentValue

Information related to a parameter value managed by Firebase ABT.

| JSON representation |
|---|
| ``` { "experimentId": string, "variantValue": [ { object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#ExperimentVariantValue`) } ] } ``` |

| Fields ||
|---|---|
| `experimentId` | `string` The identifier that associates a parameter value to an Experiment in Firebase ABT. |
| `variantValue[]` | ``object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#ExperimentVariantValue`)`` A repeated of variants associated with the Experiment. |

## ExperimentVariantValue

Information about the variant for the Experiment.

| JSON representation |
|---|
| ``` { "variantId": string, // Union field `value_option` can be only one of the following: "value": string, "noChange": boolean // End of list of possible types for union field `value_option`. } ``` |

| Fields ||
|---|---|
| `variantId` | `string` The variant identifier for the Experiment. |
| Union field `value_option`. The value to assign. The UI allows developers to toggle between no change and an actual value. `value_option` can be only one of the following: ||
| `value` | `string` The user-specified value for this variant. Can be empty string. |
| `noChange` | `boolean` If this boolean is set, then fallback to the next parameter in the Template condition chain |

## RolloutValue

Information related to a Rollout.

| JSON representation |
|---|
| ``` { "rolloutId": string, "value": string, "percent": number } ``` |

| Fields ||
|---|---|
| `rolloutId` | `string` The identifier that associates a parameter value to a Rollout experiment. |
| `value` | `string` The user-specified value to be rolled out. |
| `percent` | `number` The percentage of users that will receive the rollout value. |

## ParameterValueType

Accepted data types for parameter values.

| Enums ||
|---|---|
| `PARAMETER_VALUE_TYPE_UNSPECIFIED` | Catch-all for unrecognized enum values. |
| `STRING` | Represents String values. |
| `BOOLEAN` | Represents Boolean values ("true" or "false"). |
| `NUMBER` | Represents both positive and negative integer and float values. |
| `JSON` | Represents JSON values. |

## RemoteConfigParameterGroup

A named group of parameters. Grouping parameters is only for management purposes and does not affect client-side fetching of parameter values.

| JSON representation |
|---|
| ``` { "description": string, "parameters": { string: { object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#RemoteConfigParameter`) }, ... } } ``` |

| Fields ||
|---|---|
| `description` | `string` Optional. A description for the group. Its length must be less than or equal to 256 characters. A description may contain any Unicode characters. |
| `parameters` | ``map (key: string, value: object (`https://firebase.google.com/docs/reference/remote-config/rest/v1/RemoteConfig#RemoteConfigParameter`))`` Map of parameter keys to their optional default values and optional conditional values for parameters that belong to this group. A parameter only appears once per RemoteConfig: an ungrouped parameter appears at the top level; a parameter organized within a group appears within its group's map of parameters. An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`. |