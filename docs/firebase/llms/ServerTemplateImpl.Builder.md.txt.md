# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplateImpl.Builder.md.txt

# ServerTemplateImpl.Builder

public static class **ServerTemplateImpl.Builder** extends Object  
implements [ServerTemplate.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate.Builder)

### Public Method Summary

|---|---|
| [ServerTemplate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate) | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplateImpl.Builder#build())() |
| [ServerTemplateImpl.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplateImpl.Builder) | [cachedTemplate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplateImpl.Builder#cachedTemplate(java.lang.String))(String templateJson) |
| [ServerTemplateImpl.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplateImpl.Builder) | [defaultConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplateImpl.Builder#defaultConfig(com.google.firebase.remoteconfig.KeysAndValues))([KeysAndValues](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues) config) |

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

From interface [com.google.firebase.remoteconfig.ServerTemplate.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate.Builder)

|---|---|
| abstract [ServerTemplate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate) | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate.Builder#build())() |
| abstract [ServerTemplate.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate.Builder) | [cachedTemplate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate.Builder#cachedTemplate(java.lang.String))(String templateJson) |
| abstract [ServerTemplate.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate.Builder) | [defaultConfig](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate.Builder#defaultConfig(com.google.firebase.remoteconfig.KeysAndValues))([KeysAndValues](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues) config) |

## Public Methods

#### public [ServerTemplate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplate)
**build**
()

<br />

#### public [ServerTemplateImpl.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplateImpl.Builder)
**cachedTemplate**
(String templateJson)

<br />

#### public [ServerTemplateImpl.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/ServerTemplateImpl.Builder)
**defaultConfig**
([KeysAndValues](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/remoteconfig/KeysAndValues) config)

<br />