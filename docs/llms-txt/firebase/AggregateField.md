# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/AggregateField.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateField.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateField.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.md.txt

# AggregateField

# AggregateField


```
abstract class AggregateField
```

<br />

Known direct subclasses  
[AggregateField.AverageAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.AverageAggregateField), [AggregateField.CountAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.CountAggregateField), [AggregateField.SumAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.SumAggregateField)  

|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| [AggregateField.AverageAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.AverageAggregateField) | Represents an "average" aggregation that can be performed by Firestore. |
| [AggregateField.CountAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.CountAggregateField)     | Represents a "count" aggregation that can be performed by Firestore.    |
| [AggregateField.SumAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.SumAggregateField)         | Represents a "sum" aggregation that can be performed by Firestore.      |

*** ** * ** ***

Represents an aggregation that can be performed by Firestore.

## Summary

|                                                                                                                                                                         ### Nested types                                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `class `[AggregateField.AverageAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.AverageAggregateField)` : `[AggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField) Represents an "average" aggregation that can be performed by Firestore. |
| `class `[AggregateField.CountAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.CountAggregateField)` : `[AggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField) Represents a "count" aggregation that can be performed by Firestore.        |
| `class `[AggregateField.SumAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.SumAggregateField)` : `[AggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField) Represents a "sum" aggregation that can be performed by Firestore.              |

|                                                                            ### Public functions                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `java-static `[AggregateField.AverageAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.AverageAggregateField) | [average](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField#average(java.lang.String))`(field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Create an [AverageAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.AverageAggregateField) object that can be used to compute the average of a specified field over a range of documents in the result set of a query.                                                  |
| `java-static `[AggregateField.AverageAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.AverageAggregateField) | [average](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField#average(com.google.firebase.firestore.FieldPath))`(fieldPath: `[FieldPath](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)`)` Create an [AverageAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.AverageAggregateField) object that can be used to compute the average of a specified field over a range of documents in the result set of a query. |
| `java-static `[AggregateField.CountAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.CountAggregateField)     | [count](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField#count())`()` Create a [CountAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.CountAggregateField) object that can be used to compute the count of documents in the result set of a query.                                                                                                                                                                                                        |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                                                                         | [equals](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField#equals(java.lang.Object))`(other: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!)` Returns true if the given object is equal to this object.                                                                                                                                                                                                                                                                                   |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                                                                                 | [hashCode](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField#hashCode())`()` Calculates and returns the hash code for this object.                                                                                                                                                                                                                                                                                                                                                                                       |
| `java-static `[AggregateField.SumAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.SumAggregateField)         | [sum](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField#sum(java.lang.String))`(field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`)` Create a [SumAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.SumAggregateField) object that can be used to compute the sum of a specified field over a range of documents in the result set of a query.                                                                       |
| `java-static `[AggregateField.SumAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.SumAggregateField)         | [sum](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField#sum(com.google.firebase.firestore.FieldPath))`(fieldPath: `[FieldPath](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath)`)` Create a [SumAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.SumAggregateField) object that can be used to compute the sum of a specified field over a range of documents in the result set of a query.                      |

|                              ### Public properties                               |
|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | [alias](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField#alias())       |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | [operator](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField#operator()) |

## Public functions

### average

```
java-staticÂ funÂ average(field:Â String):Â AggregateField.AverageAggregateField
```

Create an [AverageAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.AverageAggregateField) object that can be used to compute the average of a specified field over a range of documents in the result set of a query.

The result of an average operation will always be a double or NaN.

- Averaging over zero documents or fields will result in a double value representing NaN.
- Averaging over NaN will result in a double value representing NaN.

|                                        Parameters                                         |
|-------------------------------------------------------------------------------------------|-------------------------------------------------------|
| `field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | Specifies the field to average across the result set. |

|                                                                           Returns                                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AggregateField.AverageAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.AverageAggregateField) | The \`AverageAggregateField\` object that can be used to compute the average of a specified field over a range of documents in the result set of a query. |

### average

```
java-staticÂ funÂ average(fieldPath:Â FieldPath):Â AggregateField.AverageAggregateField
```

Create an [AverageAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.AverageAggregateField) object that can be used to compute the average of a specified field over a range of documents in the result set of a query.

The result of an average operation will always be a double or NaN.

- Averaging over zero documents or fields will result in a double value representing NaN.
- Averaging over NaN will result in a double value representing NaN.

|                                                     Parameters                                                      |
|---------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| `fieldPath: `[FieldPath](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath) | Specifies the field to average across the result set. |

|                                                                           Returns                                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AggregateField.AverageAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.AverageAggregateField) | The \`AverageAggregateField\` object that can be used to compute the average of a specified field over a range of documents in the result set of a query. |

### count

```
java-staticÂ funÂ count():Â AggregateField.CountAggregateField
```

Create a [CountAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.CountAggregateField) object that can be used to compute the count of documents in the result set of a query.

The result of a count operation will always be a 64-bit integer value.  

|                                                                         Returns                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [AggregateField.CountAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.CountAggregateField) | The \`CountAggregateField\` object that can be used to compute the count of documents in the result set of a query. |

### equals

```
funÂ equals(other:Â Any!):Â Boolean
```

Returns true if the given object is equal to this object. Two \`AggregateField\` objects are considered equal if they have the same operator and operate on the same field.  

### hashCode

```
funÂ hashCode():Â Int
```

Calculates and returns the hash code for this object.  

### sum

```
java-staticÂ funÂ sum(field:Â String):Â AggregateField.SumAggregateField
```

Create a [SumAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.SumAggregateField) object that can be used to compute the sum of a specified field over a range of documents in the result set of a query.

The result of a sum operation will always be a 64-bit integer value, a double, or NaN.

- Summing over zero documents or fields will result in 0L.
- Summing over NaN will result in a double value representing NaN.
- A sum that overflows the maximum representable 64-bit integer value will result in a double return value. This may result in lost precision of the result.
- A sum that overflows the maximum representable double value will result in a double return value representing infinity.

|                                        Parameters                                         |
|-------------------------------------------------------------------------------------------|---------------------------------------------------|
| `field: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | Specifies the field to sum across the result set. |

|                                                                       Returns                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| [AggregateField.SumAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.SumAggregateField) | The \`SumAggregateField\` object that can be used to compute the sum of a specified field over a range of documents in the result set of a query. |

### sum

```
java-staticÂ funÂ sum(fieldPath:Â FieldPath):Â AggregateField.SumAggregateField
```

Create a [SumAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.SumAggregateField) object that can be used to compute the sum of a specified field over a range of documents in the result set of a query.

The result of a sum operation will always be a 64-bit integer value, a double, or NaN.

- Summing over zero documents or fields will result in 0L.
- Summing over NaN will result in a double value representing NaN.
- A sum that overflows the maximum representable 64-bit integer value will result in a double return value. This may result in lost precision of the result.
- A sum that overflows the maximum representable double value will result in a double return value representing infinity.

|                                                     Parameters                                                      |
|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| `fieldPath: `[FieldPath](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/FieldPath) | Specifies the field to sum across the result set. |

|                                                                       Returns                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| [AggregateField.SumAggregateField](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/AggregateField.SumAggregateField) | The \`SumAggregateField\` object that can be used to compute the sum of a specified field over a range of documents in the result set of a query. |

## Public properties

### alias

```
valÂ alias:Â String
```  

### operator

```
valÂ operator:Â String
```