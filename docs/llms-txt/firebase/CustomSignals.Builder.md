# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/CustomSignals.Builder.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals.Builder.md.txt

# CustomSignals.Builder

# CustomSignals.Builder


```
class CustomSignals.Builder
```

<br />

*** ** * ** ***

Builder for constructing [CustomSignals](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals) instances.

## Summary

|                                                      ### Public constructors                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------|
| [Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals.Builder#Builder())`()` |

|                                                       ### Public functions                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CustomSignals](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals)                 | [build](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals.Builder#build())`()` Creates a [CustomSignals](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals) instance with the added custom signals.                                                                                                                            |
| [CustomSignals.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals.Builder) | [put](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals.Builder#put(java.lang.String,java.lang.String))`(key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, value: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?)` Adds a custom signal with a value that can be a string or null to the builder. |
| [CustomSignals.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals.Builder) | [put](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals.Builder#put(java.lang.String,long))`(key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, value: `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)`)` Adds a custom signal with a long value to the builder.                                          |
| [CustomSignals.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals.Builder) | [put](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals.Builder#put(java.lang.String,double))`(key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`, value: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html)`)` Adds a custom signal with a double value to the builder.                                  |

## Public constructors

### Builder

```
Builder()
```  

## Public functions

### build

```
funÂ build():Â CustomSignals
```

Creates a [CustomSignals](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals) instance with the added custom signals.  

|                                                      Returns                                                      |
|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [CustomSignals](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals) | The constructed [CustomSignals](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals) instance. |

### put

```
funÂ put(key:Â String,Â value:Â String?):Â CustomSignals.Builder
```

Adds a custom signal with a value that can be a string or null to the builder.  

|                                          Parameters                                          |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------|
| `key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)      | The key for the custom signal.                         |
| `value: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | The string value associated with the key. Can be null. |

|                                                              Returns                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| [CustomSignals.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals.Builder) | This Builder instance to allow chaining of method calls. |

### put

```
funÂ put(key:Â String,Â value:Â Long):Â CustomSignals.Builder
```

Adds a custom signal with a long value to the builder.  

|                                       Parameters                                        |
|-----------------------------------------------------------------------------------------|---------------------------------------|
| `key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html) | The key for the custom signal.        |
| `value: `[Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html)   | The long value for the custom signal. |

|                                                              Returns                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| [CustomSignals.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals.Builder) | This Builder instance to allow chaining of method calls. |

### put

```
funÂ put(key:Â String,Â value:Â Double):Â CustomSignals.Builder
```

Adds a custom signal with a double value to the builder.  

|                                        Parameters                                         |
|-------------------------------------------------------------------------------------------|-----------------------------------------|
| `key: `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)   | The key for the custom signal.          |
| `value: `[Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-double/index.html) | The double value for the custom signal. |

|                                                              Returns                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| [CustomSignals.Builder](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/remoteconfig/CustomSignals.Builder) | This Builder instance to allow chaining of method calls. |