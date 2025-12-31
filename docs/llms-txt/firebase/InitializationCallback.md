# Source: https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/InitializationCallback.md.txt

# InitializationCallback

public interface **InitializationCallback**  

|---|---|---|
| Known Indirect Subclasses [InitializationCallback.Empty](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/InitializationCallback.Empty) |----------------------------------------------------------------------------------------------------------------------------------------------|---| | [InitializationCallback.Empty](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/InitializationCallback.Empty) |   | |||

Callback to use when monitoring [Fabric](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric) initialization.
Use by calling [initializationCallback(InitializationCallback)](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder#initializationCallback(io.fabric.sdk.android.InitializationCallback<io.fabric.sdk.android.Fabric>))  

### Nested Class Summary

|-------|---|---|---|
| class | [InitializationCallback.Empty](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/InitializationCallback.Empty) ||   |

### Field Summary

|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|---|
| public static final [InitializationCallback](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/InitializationCallback) | [EMPTY](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/InitializationCallback#EMPTY) |   |

### Public Method Summary

|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| abstract void | [failure](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/InitializationCallback#failure(java.lang.Exception))(Exception exception) Failed initialization with exception |
| abstract void | [success](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/InitializationCallback#success(T))(T t) Successful initialization.                                             |

## Fields

#### public static final InitializationCallback
**EMPTY**

<br />

## Public Methods

#### public abstract void
**failure**
(Exception exception)

Failed initialization with exception  

##### Parameters

|-----------|---|
| exception |   |

#### public abstract void
**success**
(T t)

Successful initialization.  

##### Parameters

|---|---|
| t |   |