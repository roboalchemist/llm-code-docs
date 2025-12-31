# Source: https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/KitGroup.md.txt

# KitGroup

public interface **KitGroup**  

|---|---|---|
| Known Indirect Subclasses [Crashlytics](https://firebase.google.com/docs/reference/android/com/crashlytics/sdk/android/crashlytics/Crashlytics) |-----------------------------------------------------------------------------------------------------------------------|---| | [Crashlytics](https://firebase.google.com/docs/reference/android/com/crashlytics/sdk/android/crashlytics/Crashlytics) |   | |||

Wrapper for a set of logically grouped [Kit](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit)'s.  

### Public Method Summary

|-----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| abstract Collection\<? extends [Kit](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit)\> | [getKits](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/KitGroup#getKits())() |

## Public Methods

#### public abstract Collection\<? extends [Kit](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit)\>
**getKits**
()

<br />

##### Returns

- Collection of Kits to be initialized by [with(android.content.Context, Kit[])](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric#with(android.content.Context, io.fabric.sdk.android.Kit...))