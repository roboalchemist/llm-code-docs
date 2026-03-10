# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentVariantValue.md.txt

# ParameterValue.ExperimentVariantValue

public static final class **ParameterValue.ExperimentVariantValue** extends Object  
Represents a specific variant within an Experiment.

### Public Method Summary

|---|---|
| boolean | [equals](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentVariantValue#equals(java.lang.Object))(Object o) |
| String | [getValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentVariantValue#getValue())() Gets the value of the experiment variant. |
| String | [getVariantId](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentVariantValue#getVariantId())() Gets the ID of the experiment variant. |
| int | [hashCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentVariantValue#hashCode())() |
| boolean | [isNoChange](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentVariantValue#isNoChange())() Returns whether the experiment variant is a no-change variant. |
| static [ParameterValue.ExperimentVariantValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentVariantValue) | [of](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentVariantValue#of(java.lang.String, java.lang.String))(String variantId, String value) Creates a new `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentVariantValue` instance. |
| static [ParameterValue.ExperimentVariantValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentVariantValue) | [ofNoChange](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentVariantValue#ofNoChange(java.lang.String))(String variantId) Creates a new `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentVariantValue` instance. |

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

## Public Methods

#### public boolean
**equals**
(Object o)

<br />

#### public String
**getValue**
()

Gets the value of the experiment variant.

##### Returns

- The variant value

#### public String
**getVariantId**
()

Gets the ID of the experiment variant.

##### Returns

- The variant ID

#### public int
**hashCode**
()

<br />

#### public boolean
**isNoChange**
()

Returns whether the experiment variant is a no-change variant.

##### Returns

- true if the experiment variant is a no-change variant, and false otherwise.

#### public static [ParameterValue.ExperimentVariantValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentVariantValue)
**of**
(String variantId, String value)

Creates a new `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentVariantValue` instance.

##### Parameters

| variantId | The variant ID. |
| value | The value of the variant. |
|---|---|

##### Returns

- A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentVariantValue` instance.

#### public static [ParameterValue.ExperimentVariantValue](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentVariantValue)
**ofNoChange**
(String variantId)

Creates a new `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentVariantValue` instance.

##### Parameters

| variantId | The variant ID. |
|---|---|

##### Returns

- A `https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ParameterValue.ExperimentVariantValue` instance.