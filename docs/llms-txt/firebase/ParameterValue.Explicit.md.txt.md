# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit.md.txt

# ParameterValue.Explicit

public static final class **ParameterValue.Explicit** extends [ParameterValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue)  
Represents an explicit Remote Config parameter value with a value that the
parameter is set to.

### Public Method Summary

|---|---|
| boolean | [equals](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit#equals(java.lang.Object))(Object o) |
| String | [getValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit#getValue())() Gets the value of `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit`. |
| int | [hashCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit#hashCode())() |

### Inherited Method Summary

From class [com.google.firebase.remoteconfig.ParameterValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue)

|---|---|
| static [ParameterValue.InAppDefault](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.InAppDefault) | [inAppDefault](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue#inAppDefault())() Creates a new `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.InAppDefault` instance. |
| static [ParameterValue.Explicit](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit) | [of](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue#of(java.lang.String))(String value) Creates a new `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit` instance with the given value. |
| static [ParameterValue.ExperimentValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentValue) | [ofExperiment](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue#ofExperiment(java.lang.String, java.util.List<com.google.firebase.remoteconfig.ParameterValue.ExperimentVariantValue>))(String experimentId, List\<[ParameterValue.ExperimentVariantValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentVariantValue)\> variantValues) Creates a new `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentValue` instance. |
| static [ParameterValue.PersonalizationValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.PersonalizationValue) | [ofPersonalization](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue#ofPersonalization(java.lang.String))(String personalizationId) Creates a new `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.PersonalizationValue` instance. |
| static [ParameterValue.RolloutValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.RolloutValue) | [ofRollout](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue#ofRollout(java.lang.String, java.lang.String, double))(String rolloutId, String value, double percent) Creates a new `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.RolloutValue` instance. |

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

## Public Methods

#### public boolean
**equals**
(Object o)

<br />

#### public String
**getValue**
()

Gets the value of `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.Explicit`.

##### Returns

- The value.

#### public int
**hashCode**
()

<br />