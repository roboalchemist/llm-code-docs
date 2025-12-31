# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseOptions.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasecore/api/reference/Classes/FirebaseOptions.md.txt

# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/FirebaseOptions.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.md.txt

# FirebaseOptions

# FirebaseOptions


```
class FirebaseOptions
```

<br />

*** ** * ** ***

Configurable Firebase options.

## Summary

|                                                                              ### Nested types                                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `class `[FirebaseOptions.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions.Builder) Builder for constructing FirebaseOptions. |

|                                                   ### Public functions                                                    |
|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)                                        | [equals](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions#equals(java.lang.Object))`(o: `[Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)`!)`                                                                                                                                                                                                              |
| `java-static `[FirebaseOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions)`?` | [fromResource](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions#fromResource(android.content.Context))`(context: `[Context](https://developer.android.com/reference/kotlin/android/content/Context.html)`)` Creates a new [FirebaseOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions) instance that is populated from string resources. |
| [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-int/index.html)                                                | [hashCode](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions#hashCode())`()`                                                                                                                                                                                                                                                                                                          |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!`                                       | [toString](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions#toString())`()`                                                                                                                                                                                                                                                                                                          |

|                                ### Public properties                                |
|-------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [apiKey](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions#apiKey())               |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [applicationId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions#applicationId()) |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [databaseUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions#databaseUrl())     |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [gaTrackingId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions#gaTrackingId())   |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [gcmSenderId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions#gcmSenderId())     |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [projectId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions#projectId())         |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!` | [storageBucket](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions#storageBucket()) |

## Public functions

### equals

```
funÂ equals(o:Â Any!):Â Boolean
```  

### fromResource

```
java-staticÂ funÂ fromResource(context:Â Context):Â FirebaseOptions?
```

Creates a new [FirebaseOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions) instance that is populated from string resources.  

|                                                   Returns                                                   |
|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| [FirebaseOptions](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/FirebaseOptions)`?` | The populated options or null if applicationId is missing from resources. |

### hashCode

```
funÂ hashCode():Â Int
```  

### toString

```
funÂ toString():Â String!
```  

## Public properties

### apiKey

```
valÂ apiKey:Â String!
```  

### applicationId

```
valÂ applicationId:Â String!
```  

### databaseUrl

```
valÂ databaseUrl:Â String!
```  

### gaTrackingId

```
valÂ gaTrackingId:Â String!
```  

### gcmSenderId

```
valÂ gcmSenderId:Â String!
```  

### projectId

```
valÂ projectId:Â String!
```  

### storageBucket

```
valÂ storageBucket:Â String!
```