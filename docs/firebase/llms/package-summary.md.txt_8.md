# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/package-summary.md.txt

# com.google.firebase.remoteconfig

### Interfaces

|---|---|
| [ServerTemplate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate) |   |
| [ServerTemplate.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate.Builder) |   |

### Classes

|---|---|
| [Condition](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Condition) | Represents a Remote Config condition that can be included in a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template`. |
| [FirebaseRemoteConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfig) | This class is the entry point for all server-side Firebase Remote Config actions. |
| [KeysAndValues](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues) | Represents data stored in context passed to server-side Remote Config. |
| [KeysAndValues.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues.Builder) | Builder class for KeysAndValues using which values will be assigned to private variables. |
| [ListVersionsOptions](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions) | A class representing options for Remote Config list versions operation. |
| [ListVersionsOptions.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsOptions.Builder) |   |
| [ListVersionsPage](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ListVersionsPage) | Represents a page of `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version` instances. |
| [Parameter](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Parameter) | Represents a Remote Config parameter that can be included in a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template`. |
| [ParameterGroup](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterGroup) | Represents a Remote Config parameter group that can be included in a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template`. |
| [ParameterValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue) | Represents a Remote Config parameter value that can be used in a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template`. |
| [ParameterValue.ExperimentValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentValue) | Represents an Experiment value. |
| [ParameterValue.ExperimentVariantValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentVariantValue) | Represents a specific variant within an Experiment. |
| [ParameterValue.Explicit](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit) | Represents an explicit Remote Config parameter value with a value that the parameter is set to. |
| [ParameterValue.InAppDefault](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.InAppDefault) | Represents an in app default parameter value. |
| [ParameterValue.PersonalizationValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.PersonalizationValue) | Represents a Personalization value. |
| [ParameterValue.RolloutValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.RolloutValue) | Represents a Rollout value. |
| [PercentCondition](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/PercentCondition) | Represents a condition that compares the instance pseudo-random percentile to a given limit. |
| [ServerConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerConfig) | Represents the configuration produced by evaluating a server template. |
| [ServerTemplateImpl](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplateImpl) |   |
| [ServerTemplateImpl.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplateImpl.Builder) |   |
| [Template](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template) | Represents a Remote Config template. |
| [User](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/User) | Represents a Remote Config user. |
| [Version](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Version) | Represents a Remote Config template version. |

### Enums

|---|---|
| [ParameterValueType](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValueType) | Data types that are associated with parameter values. |
| [PercentConditionOperator](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/PercentConditionOperator) | Defines supported operators for percent conditions. |
| [RemoteConfigErrorCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/RemoteConfigErrorCode) | Error codes that can be raised by the Remote Config APIs. |
| [TagColor](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/TagColor) | Colors that are associated with conditions for display purposes in the Firebase Console. |
| [ValueSource](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ValueSource) | Indicates the source of a value. |

### Exceptions

|---|---|
| [FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) | Generic exception related to Firebase Remote Config. |