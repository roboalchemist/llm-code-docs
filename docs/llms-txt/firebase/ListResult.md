# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult.md.txt

# ListResult

# ListResult


```
class ListResult
```

<br />

*** ** * ** ***

Contains the prefixes and items returned by a [list](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference#list(int)) call.

## Summary

|                                                                                                                                                    ### Public properties                                                                                                                                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| `(`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)`)`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference)`!>!` | [items](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult#items())         |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`                                                                                                                                                                                                                                         | [pageToken](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult#pageToken()) |
| `(`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/index.html)`)`[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference)`!>!` | [prefixes](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult#prefixes())   |

|                                                                                                   ### Extension functions                                                                                                   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `operator `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference)`>` | [ListResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult)`.`[component1](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult#(com.google.firebase.storage.ListResult).component1())`()` Destructuring declaration for [ListResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult) to provide its items.     |
| `operator `[List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference)`>` | [ListResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult)`.`[component2](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult#(com.google.firebase.storage.ListResult).component2())`()` Destructuring declaration for [ListResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult) to provide its prefixes.  |
| `operator `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?`                                                                                                                              | [ListResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult)`.`[component3](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult#(com.google.firebase.storage.ListResult).component3())`()` Destructuring declaration for [ListResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult) to provide its pageToken. |

## Public properties

### items

```
valÂ items:Â (Mutable)List<StorageReference!>!
```  

### pageToken

```
valÂ pageToken:Â String?
```  

### prefixes

```
valÂ prefixes:Â (Mutable)List<StorageReference!>!
```  

## Extension functions

### component1

```
operatorÂ funÂ ListResult.component1():Â List<StorageReference>
```

Destructuring declaration for [ListResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult) to provide its items.  

|                                                                                                     Returns                                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference)`>` | the items of the [ListResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult) |

### component2

```
operatorÂ funÂ ListResult.component2():Â List<StorageReference>
```

Destructuring declaration for [ListResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult) to provide its prefixes.  

|                                                                                                     Returns                                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-list/index.html)`<`[StorageReference](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/StorageReference)`>` | the prefixes of the [ListResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult) |

### component3

```
operatorÂ funÂ ListResult.component3():Â String?
```

Destructuring declaration for [ListResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult) to provide its pageToken.  

|                                       Returns                                       |
|-------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`?` | the pageToken of the [ListResult](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/storage/ListResult) |