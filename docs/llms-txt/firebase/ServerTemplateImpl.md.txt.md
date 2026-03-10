# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplateImpl.md.txt

# ServerTemplateImpl

public final class **ServerTemplateImpl** extends Object  
implements [ServerTemplate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate)

### Nested Class Summary

|---|---|---|---|
| class | [ServerTemplateImpl.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplateImpl.Builder) ||   |

### Public Method Summary

|---|---|
| [ServerConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerConfig) | [evaluate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplateImpl#evaluate())() Process the template data without context. |
| [ServerConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerConfig) | [evaluate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplateImpl#evaluate(com.google.firebase.remoteconfig.KeysAndValues))([KeysAndValues](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues) context) Process the template data with a condition evaluator based on the provided context. |
| String | [getCachedTemplate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplateImpl#getCachedTemplate())() |
| [KeysAndValues](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues) | [getDefaultConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplateImpl#getDefaultConfig())() |
| ApiFuture\<Void\> | [load](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplateImpl#load())() Fetches and caches the current active version of the project. |
| String | [toJson](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplateImpl#toJson())() |

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

From interface [com.google.firebase.remoteconfig.ServerTemplate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate)

|---|---|
| abstract [ServerConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerConfig) | [evaluate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate#evaluate())() Process the template data without context. |
| abstract [ServerConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerConfig) | [evaluate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate#evaluate(com.google.firebase.remoteconfig.KeysAndValues))([KeysAndValues](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues) context) Process the template data with a condition evaluator based on the provided context. |
| abstract ApiFuture\<Void\> | [load](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate#load())() Fetches and caches the current active version of the project. |
| abstract String | [toJson](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate#toJson())() |

## Public Methods

#### public [ServerConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerConfig)
**evaluate**
()

Process the template data without context.

##### Throws

| [FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) |   |
|---|---|

#### public [ServerConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerConfig)
**evaluate**
([KeysAndValues](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues) context)

Process the template data with a condition evaluator
based on the provided context.

##### Throws

| [FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) |   |
|---|---|

#### public String
**getCachedTemplate**
()

<br />

#### public [KeysAndValues](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues)
**getDefaultConfig**
()

<br />

#### public ApiFuture\<Void\>
**load**
()

Fetches and caches the current active version of the project.

##### Throws

| [FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) |   |
|---|---|

#### public String
**toJson**
()

<br />