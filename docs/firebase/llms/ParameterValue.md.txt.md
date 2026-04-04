# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.md.txt

# ParameterValue

public abstract class **ParameterValue** extends Object  

|---|---|---|
| Known Direct Subclasses [ParameterValue.ExperimentValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentValue), [ParameterValue.Explicit](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit), [ParameterValue.InAppDefault](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.InAppDefault), [ParameterValue.PersonalizationValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.PersonalizationValue), [ParameterValue.RolloutValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.RolloutValue) |---|---| | [ParameterValue.ExperimentValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentValue) | Represents an Experiment value. | | [ParameterValue.Explicit](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit) | Represents an explicit Remote Config parameter value with a value that the parameter is set to. | | [ParameterValue.InAppDefault](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.InAppDefault) | Represents an in app default parameter value. | | [ParameterValue.PersonalizationValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.PersonalizationValue) | Represents a Personalization value. | | [ParameterValue.RolloutValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.RolloutValue) | Represents a Rollout value. | |||

Represents a Remote Config parameter value that can be used in a `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/Template`.

### Nested Class Summary

|---|---|---|---|
| class | [ParameterValue.ExperimentValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentValue) || Represents an Experiment value. |
| class | [ParameterValue.ExperimentVariantValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentVariantValue) || Represents a specific variant within an Experiment. |
| class | [ParameterValue.Explicit](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit) || Represents an explicit Remote Config parameter value with a value that the parameter is set to. |
| class | [ParameterValue.InAppDefault](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.InAppDefault) || Represents an in app default parameter value. |
| class | [ParameterValue.PersonalizationValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.PersonalizationValue) || Represents a Personalization value. |
| class | [ParameterValue.RolloutValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.RolloutValue) || Represents a Rollout value. |

### Public Constructor Summary

|---|---|
|   | [ParameterValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue#ParameterValue())() |

### Public Method Summary

|---|---|
| static [ParameterValue.InAppDefault](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.InAppDefault) | [inAppDefault](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue#inAppDefault())() Creates a new `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.InAppDefault` instance. |
| static [ParameterValue.Explicit](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit) | [of](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue#of(java.lang.String))(String value) Creates a new `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit` instance with the given value. |
| static [ParameterValue.ExperimentValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentValue) | [ofExperiment](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue#ofExperiment(java.lang.String, java.util.List<com.google.firebase.remoteconfig.ParameterValue.ExperimentVariantValue>))(String experimentId, List\<[ParameterValue.ExperimentVariantValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentVariantValue)\> variantValues) Creates a new `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentValue` instance. |
| static [ParameterValue.PersonalizationValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.PersonalizationValue) | [ofPersonalization](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue#ofPersonalization(java.lang.String))(String personalizationId) Creates a new `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.PersonalizationValue` instance. |
| static [ParameterValue.RolloutValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.RolloutValue) | [ofRollout](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue#ofRollout(java.lang.String, java.lang.String, double))(String rolloutId, String value, double percent) Creates a new `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.RolloutValue` instance. |

### Inherited Method Summary

From class java.lang.Object

|---|---|
| Object | clone() |
| boolean | equals(Object arg0) |
| void | finalize() |
| final Class\<?\> | getClass() |
| int | hashCode() |
| final void | notify() |
| final void | notifyAll() |
| String | toString() |
| final void | wait(long arg0, int arg1) |
| final void | wait(long arg0) |
| final void | wait() |

## Public Constructors

#### public
**ParameterValue**
()

<br />

## Public Methods

#### public static [ParameterValue.InAppDefault](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.InAppDefault)
**inAppDefault**
()

Creates a new `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.InAppDefault` instance.

##### Returns

- A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.InAppDefault` instance.

#### public static [ParameterValue.Explicit](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit)
**of**
(String value)

Creates a new `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit` instance with the given value.

##### Parameters

| value | The value of the `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit`. |
|---|---|

##### Returns

- A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit` instance.

#### public static [ParameterValue.ExperimentValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentValue)
**ofExperiment**
(String experimentId, List\<[ParameterValue.ExperimentVariantValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentVariantValue)\> variantValues)

Creates a new `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentValue` instance.

##### Parameters

| experimentId | The experiment ID. |
| variantValues | The list of experiment variant values. |
|---|---|

##### Returns

- A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentValue` instance.

#### public static [ParameterValue.PersonalizationValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.PersonalizationValue)
**ofPersonalization**
(String personalizationId)

Creates a new `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.PersonalizationValue` instance.

##### Parameters

| personalizationId | The personalization ID. |
|---|---|

##### Returns

- A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.PersonalizationValue` instance.

#### public static [ParameterValue.RolloutValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.RolloutValue)
**ofRollout**
(String rolloutId, String value, double percent)

Creates a new `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.RolloutValue` instance.

##### Parameters

| rolloutId | The rollout ID. |
| value | The value of the rollout. |
| percent | The percentage of the rollout. |
|---|---|

##### Returns

- A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.RolloutValue` instance.