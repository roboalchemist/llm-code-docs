# Source: https://firebase.google.com/docs/reference/cpp/namespace/google-play-services.md.txt

# google_play_services Namespace

# google_play_services

Google Play services APIs included with the Firebase C++ SDK.

## Summary

These APIs are Android-specific.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ### Enumerations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ||
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| [Availability](https://firebase.google.com/docs/reference/cpp/namespace/google-play-services#namespacegoogle__play__services_1ab190babadb1852efc71630ddc4b82f45)`{` ` `[kAvailabilityAvailable](https://firebase.google.com/docs/reference/cpp/namespace/google-play-services#namespacegoogle__play__services_1ab190babadb1852efc71630ddc4b82f45a73bfb38551be2a1ff427078d791fd155)`,` ` `[kAvailabilityUnavailableDisabled](https://firebase.google.com/docs/reference/cpp/namespace/google-play-services#namespacegoogle__play__services_1ab190babadb1852efc71630ddc4b82f45a599f59588c2187bdb2b3d6cfc57e6f10)`,` ` `[kAvailabilityUnavailableInvalid](https://firebase.google.com/docs/reference/cpp/namespace/google-play-services#namespacegoogle__play__services_1ab190babadb1852efc71630ddc4b82f45a6bdcd50d809b8547d878437b286efd1c)`,` ` `[kAvailabilityUnavailableMissing](https://firebase.google.com/docs/reference/cpp/namespace/google-play-services#namespacegoogle__play__services_1ab190babadb1852efc71630ddc4b82f45a988d5c63f0ef559c9274f38972f59e6b)`,` ` `[kAvailabilityUnavailablePermissions](https://firebase.google.com/docs/reference/cpp/namespace/google-play-services#namespacegoogle__play__services_1ab190babadb1852efc71630ddc4b82f45a65ed0920128a5c4fd67920d0f8c85621)`,` ` `[kAvailabilityUnavailableUpdateRequired](https://firebase.google.com/docs/reference/cpp/namespace/google-play-services#namespacegoogle__play__services_1ab190babadb1852efc71630ddc4b82f45a1d9f3240807fb358e25a003859105fe3)`,` ` `[kAvailabilityUnavailableUpdating](https://firebase.google.com/docs/reference/cpp/namespace/google-play-services#namespacegoogle__play__services_1ab190babadb1852efc71630ddc4b82f45aca4c2b12c85661890e22acdaa0d0351e)`,` ` `[kAvailabilityUnavailableOther](https://firebase.google.com/docs/reference/cpp/namespace/google-play-services#namespacegoogle__play__services_1ab190babadb1852efc71630ddc4b82f45a723cad0c45257fb512f36f05083b42b4) `}` | enum Possible availability states for Google Play services. |

|                                                                                                                                                                                                                                                                          ### Functions                                                                                                                                                                                                                                                                          ||
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CheckAvailability](https://firebase.google.com/docs/reference/cpp/namespace/google-play-services#namespacegoogle__play__services_1a03ea6a3db30e6ef80a816d7605423a3a)`(JNIEnv *env, jobject activity)` | [Availability](https://firebase.google.com/docs/reference/cpp/namespace/google-play-services#namespacegoogle__play__services_1ab190babadb1852efc71630ddc4b82f45) Check whether Google Play services is available on this device.                                                                                                                        |
| [MakeAvailable](https://firebase.google.com/docs/reference/cpp/namespace/google-play-services#namespacegoogle__play__services_1a9b9a9a553ee7476d697260c685074520)`(JNIEnv *env, jobject activity)`     | `::`[firebase::Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Attempt to make Google Play services available, by installing, updating, activating, or whatever else needs to be done.                                                                                                 |
| [MakeAvailableLastResult](https://firebase.google.com/docs/reference/cpp/namespace/google-play-services#namespacegoogle__play__services_1aa3600ded2dcb469a466b9ace2839a382)`()`                        | `::`[firebase::Future](https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future)`< void >` Get the future result from the most recent call to [MakeAvailable()](https://firebase.google.com/docs/reference/cpp/namespace/google-play-services#namespacegoogle__play__services_1a9b9a9a553ee7476d697260c685074520). |

## Enumerations

### Availability

```c++
 Availability
```  
Possible availability states for Google Play services.

|                                              Properties                                               ||
|------------------------------------------|-------------------------------------------------------------|
| `kAvailabilityAvailable`                 | Google Play services are available.                         |
| `kAvailabilityUnavailableDisabled`       | Google Play services is disabled in Settings.               |
| `kAvailabilityUnavailableInvalid`        | Google Play services is invalid.                            |
| `kAvailabilityUnavailableMissing`        | Google Play services is not installed.                      |
| `kAvailabilityUnavailableOther`          | Some other error occurred.                                  |
| `kAvailabilityUnavailablePermissions`    | Google Play services does not have the correct permissions. |
| `kAvailabilityUnavailableUpdateRequired` | Google Play services need to be updated.                    |
| `kAvailabilityUnavailableUpdating`       | Google Play services is currently updating.                 |

## Functions

### CheckAvailability

```c++
Availability CheckAvailability(
  JNIEnv *env,
  jobject activity
)
```  
Check whether Google Play services is available on this device.


**See also:**
[MakeAvailable()](https://firebase.google.com/docs/reference/cpp/namespace/google-play-services#namespacegoogle__play__services_1a9b9a9a553ee7476d697260c685074520)
| **Note:** This function is Android-specific.

<br />

|                                                                                                                                                            Details                                                                                                                                                            ||
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | True if Google Play services is available and up-to-date, false if not. If false was returned, you can call [MakeAvailable()](https://firebase.google.com/docs/reference/cpp/namespace/google-play-services#namespacegoogle__play__services_1a9b9a9a553ee7476d697260c685074520) to attempt to resolve the issue. |

### MakeAvailable

```c++
::firebase::Future< void > MakeAvailable(
  JNIEnv *env,
  jobject activity
)
```  
Attempt to make Google Play services available, by installing, updating, activating, or whatever else needs to be done.


| **Note:** This function is Android-specific.

<br />

|                                                                    Details                                                                    ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | A future result. When completed, the Error will be 0 if Google Play services are now available, or nonzero if still unavailable. |

### MakeAvailableLastResult

```c++
::firebase::Future< void > MakeAvailableLastResult()
```  
Get the future result from the most recent call to [MakeAvailable()](https://firebase.google.com/docs/reference/cpp/namespace/google-play-services#namespacegoogle__play__services_1a9b9a9a553ee7476d697260c685074520).


**See also:**
[MakeAvailable()](https://firebase.google.com/docs/reference/cpp/namespace/google-play-services#namespacegoogle__play__services_1a9b9a9a553ee7476d697260c685074520)
| **Note:** This function is Android-specific.

<br />

|                                                                                                                                                                     Details                                                                                                                                                                      ||
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Returns** | The future result from the most recent call to [MakeAvailable()](https://firebase.google.com/docs/reference/cpp/namespace/google-play-services#namespacegoogle__play__services_1a9b9a9a553ee7476d697260c685074520). When completed, the Error will be 0 if Google Play services are now available, or nonzero if still unavailable. |