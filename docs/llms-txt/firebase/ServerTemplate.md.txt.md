# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate.md.txt

# ServerTemplate

public interface **ServerTemplate**

|---|---|---|
| Known Indirect Subclasses [ServerTemplateImpl](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplateImpl) |---|---| | [ServerTemplateImpl](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplateImpl) |   | |||

### Nested Class Summary

|---|---|---|---|
| interface | [ServerTemplate.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate.Builder) ||   |

### Public Method Summary

|---|---|
| abstract [ServerConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerConfig) | [evaluate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate#evaluate())() Process the template data without context. |
| abstract [ServerConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerConfig) | [evaluate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate#evaluate(com.google.firebase.remoteconfig.KeysAndValues))([KeysAndValues](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues) context) Process the template data with a condition evaluator based on the provided context. |
| abstract ApiFuture\<Void\> | [load](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate#load())() Fetches and caches the current active version of the project. |
| abstract String | [toJson](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate#toJson())() |

## Public Methods

#### public abstract [ServerConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerConfig)
**evaluate**
()

Process the template data without context.

##### Throws

| [FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) |   |
|---|---|

#### public abstract [ServerConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerConfig)
**evaluate**
([KeysAndValues](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues) context)

Process the template data with a condition evaluator
based on the provided context.

##### Throws

| [FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) |   |
|---|---|

#### public abstract ApiFuture\<Void\>
**load**
()

Fetches and caches the current active version of the project.

##### Throws

| [FirebaseRemoteConfigException](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/FirebaseRemoteConfigException) |   |
|---|---|

#### public abstract String
**toJson**
()

<br />