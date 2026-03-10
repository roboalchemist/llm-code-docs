# Source: https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics.md.txt

# firebase::analytics Namespace

# firebase::analytics

Firebase Analytics API.

## Summary

See [the developer guides](https://firebase.google.com/docs/analytics) for general information on using Firebase Analytics in your apps.

| ### Enumerations ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a2114d33effb1667d452c3a5da2cdedfd` | enumThe state of an app in its lifecycle. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a506d02f0829e762922caf374c8d1fd2f` | enumThe status value of the consent type. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1ab36250435cd94106989a32f1b654e166` | enumThe type of consent to set. |

| ### Typedefs ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a6c81f9ca01bf861467b83770a1e137e6` | using `std::function< void(https://firebase.google.com/docs/reference/cpp/namespace/firebase#namespacefirebase_1a52d8f08cc8edeccdb334bf5c121aa698, const char *)>` The callback type for logging messages from the SDK. |

| ### Functions ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a8e239d353f50f6e4bc3397847ae36ed0()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< std::string >` Get the instance ID from the analytics service. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1abafce2e71d83a834319a7341f10e6144()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< std::string >` Get the result of the most recent [GetAnalyticsInstanceId()](https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a8e239d353f50f6e4bc3397847ae36ed0) call. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1acb5e391f7d8ee65993480117fda89e48()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< int64_t >` Asynchronously retrieves the identifier of the current app session. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a1cf61d682de53c12896bca7dc83072c3()` | `https://firebase.google.com/docs/reference/cpp/class/firebase/future#classfirebase_1_1_future< int64_t >` Get the result of the most recent [GetSessionId()](https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1acb5e391f7d8ee65993480117fda89e48) call. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1ab15684936a9f93921f0fa31deb508a4d(const https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app & app)` | `void` Initialize the Analytics API. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a3b2895a358908e8352f479422ec48dc0(const char *email_address)` | `void` Initiates on-device conversion measurement given a user email address on iOS and tvOS (no-op on Android). |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a7bc21c3b9892b99c73496e0959f6d692(std::vector< unsigned char > hashed_email_address)` | `void` Initiates on-device conversion measurement given a SHA256-hashed user email address. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a02e45fc29925592550e7ebedb259fef0(std::vector< unsigned char > hashed_phone_number)` | `void` Initiates on-device conversion measurement given a SHA256-hashed phone number in E.164 format. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1afdd62efe3ae1461d6fcc40e5ee4c5c00(const char *phone_number)` | `void` Initiates on-device conversion measurement given a phone number in E.164 format on iOS (no-op on Android). |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a96b56268fdead856095f0d9bccb74bda()` | `bool` Returns whether the desktop Analytics SDK is initialized. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a93b61cf7740883d81eeaa442d951ac82(const char *name, const char *parameter_name, const char *parameter_value)` | `void` Log an event with one string parameter. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1aef2252a6cae8a45704aec3af60c8df21(const char *name, const char *parameter_name, const double parameter_value)` | `void` Log an event with one float parameter. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a339e179eaee0abd26a6e3db20d07bab0(const char *name, const char *parameter_name, const int64_t parameter_value)` | `void` Log an event with one 64-bit integer parameter. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a59844903c84bb1711bb7397a31c8d461(const char *name, const char *parameter_name, const int parameter_value)` | `void` Log an event with one integer parameter (stored as a 64-bit integer). |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1ad4aff1c74480a5a13d5e6e58170bc75d(const char *name)` | `void` Log an event with no parameters. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a638c62aa918c2cb5d23740c19fb911df(const char *name, const https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter#structfirebase_1_1analytics_1_1_parameter *parameters, size_t number_of_parameters)` | `void` Log an event with associated parameters. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a62bc9eddd52e49ced413f74c3fcdca2f(const char *name, const std::vector< https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter#structfirebase_1_1analytics_1_1_parameter > & parameters)` | `void` Log an event with associated parameters. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a894bb12936a26480555dd78a68d33a84(https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a2114d33effb1667d452c3a5da2cdedfd state)` | `void` Notifies the current state of the app's lifecycle. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1aa011e496efbc85e1e740d8caadd8e37b()` | `void` Clears all analytics data for this app from the device and resets the app instance id. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a5615fefec127488911e140d180ee7479(bool enabled)` | `void` Sets whether analytics collection is enabled for this app on this device. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a2942e4f437ff60079bc786c5ea8bb474(const std::map< https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1ab36250435cd94106989a32f1b654e166, https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a506d02f0829e762922caf374c8d1fd2f > & consent_settings)` | `void` Sets the applicable end user consent state (e.g., for device identifiers) for this app on this device. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a407f4f775c4c5cc91c50ff3dbb3bd899(const https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter#structfirebase_1_1analytics_1_1_parameter *parameters, size_t number_of_parameters)` | `void` Adds parameters that will be set on every event logged from the SDK. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1aa206c0bac53f93be2d585dd1749b905b(const std::vector< https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter#structfirebase_1_1analytics_1_1_parameter > & parameters)` | `void` Adds parameters that will be set on every event logged from the SDK. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1ac041941bc76c745d9a374e3fd4bebdcf(bool enabled)` | `void` Sets whether desktop debug mode is enabled. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a4b7ce0a279f4f7740461eed735764ff2(const https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a6c81f9ca01bf861467b83770a1e137e6 & callback)` | `void` Allows the passing of a callback to be used when the SDK logs any messages regarding its behaviour. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1affa3d0db3d8803d15b1d0d951adf6fb7(int64_t milliseconds)` | `void` Sets the duration of inactivity that terminates the current session. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a45bf93e57c474e4ab36f92433e62cfbd(const char *user_id)` | `void` Sets the user ID property. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1aaf483fcf6eeaf78db243635783b4f6b1(const char *name, const char *property)` | `void` Set a user property to the given value. |
| `https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a4ffbdf8db17725dd3c2e1732fb6a8009()` | `void` Terminate the Analytics API. |

| ### Structs ||
|---|---|
| [firebase::analytics::Parameter](https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter) | Event parameter. |

## Enumerations

### AppLifecycleState

```c++
 AppLifecycleState
```
The state of an app in its lifecycle.

kUnknown is an invalid state that is used to capture uninitialized values. kTermination is used to indicate that the app is about to be terminated.

### ConsentStatus

```c++
 ConsentStatus
```
The status value of the consent type.

Supported statuses are kConsentStatusGranted and kConsentStatusDenied.

### ConsentType

```c++
 ConsentType
```
The type of consent to set.

Supported consent types are mapped to corresponding constants in the Android and iOS SDKs. Omitting a type retains its previous status.

## Typedefs

### LogCallback

```c++
std::function< void(LogLevel, const char *)> LogCallback
```
The callback type for logging messages from the SDK.

The callback is invoked whenever the SDK logs a message. Currently only works for Windows Desktop.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `log_level` | The log level of the message. | | `message` | The message logged by the SDK. | |

## Functions

### GetAnalyticsInstanceId

```c++
Future< std::string > GetAnalyticsInstanceId()
```
Get the instance ID from the analytics service.


> [!NOTE]
> **Note:** This is *not* the same ID as the ID returned by firebase::instance_id::InstanceId.

<br />

| Details ||
|---|---|
| **Returns** | Object which can be used to retrieve the analytics instance ID. |

### GetAnalyticsInstanceIdLastResult

```c++
Future< std::string > GetAnalyticsInstanceIdLastResult()
```
Get the result of the most recent [GetAnalyticsInstanceId()](https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a8e239d353f50f6e4bc3397847ae36ed0) call.

<br />

| Details ||
|---|---|
| **Returns** | Object which can be used to retrieve the analytics instance ID. |

### GetSessionId

```c++
Future< int64_t > GetSessionId()
```
Asynchronously retrieves the identifier of the current app session.

The session ID retrieval could fail due to Analytics collection disabled, or if the app session was expired.

<br />

| Details ||
|---|---|
| **Returns** | Object which can be used to retrieve the identifier of the current app session. |

### GetSessionIdLastResult

```c++
Future< int64_t > GetSessionIdLastResult()
```
Get the result of the most recent [GetSessionId()](https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1acb5e391f7d8ee65993480117fda89e48) call.

<br />

| Details ||
|---|---|
| **Returns** | Object which can be used to retrieve the identifier of the current app session. |

### Initialize

```c++
void Initialize(
  const App & app
)
```
Initialize the Analytics API.

This must be called prior to calling any other methods in the [firebase::analytics](https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics) namespace.

**See also:** [firebase::App::GetInstance()](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app_1a52b5b2208b7bd41a0f9a2940d194409f).

| Details ||
|---|---|
| Parameters | |---|---| | `app` | Default [firebase::App](https://firebase.google.com/docs/reference/cpp/class/firebase/app#classfirebase_1_1_app) instance. | |

### InitiateOnDeviceConversionMeasurementWithEmailAddress

```c++
void InitiateOnDeviceConversionMeasurementWithEmailAddress(
  const char *email_address
)
```
Initiates on-device conversion measurement given a user email address on iOS and tvOS (no-op on Android).

On iOS and tvOS, this method requires the dependency GoogleAppMeasurementOnDeviceConversion to be linked in, otherwise the invocation results in a no-op.

| Details ||
|---|---|
| Parameters | |---|---| | `email_address` | User email address. Include a domain name for all email addresses (e.g. gmail.com or hotmail.co.jp). | |

### InitiateOnDeviceConversionMeasurementWithHashedEmailAddress

```c++
void InitiateOnDeviceConversionMeasurementWithHashedEmailAddress(
  std::vector< unsigned char > hashed_email_address
)
```
Initiates on-device conversion measurement given a SHA256-hashed user email address.

Requires dependency GoogleAppMeasurementOnDeviceConversion to be linked in, otherwise it is a no-op.

| Details ||
|---|---|
| Parameters | |---|---| | `hashed_email_address` | User email address as a UTF8-encoded string normalized and hashed according to the instructions at <https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-3>. | |

### InitiateOnDeviceConversionMeasurementWithHashedPhoneNumber

```c++
void InitiateOnDeviceConversionMeasurementWithHashedPhoneNumber(
  std::vector< unsigned char > hashed_phone_number
)
```
Initiates on-device conversion measurement given a SHA256-hashed phone number in E.164 format.

Requires dependency GoogleAppMeasurementOnDeviceConversion to be linked in, otherwise it is a no-op.

| Details ||
|---|---|
| Parameters | |---|---| | `hashed_phone_number` | UTF8-encoded user phone number in E.164 format and then hashed according to the instructions at <https://firebase.google.com/docs/tutorials/ads-ios-on-device-measurement/step-3>. | |

### InitiateOnDeviceConversionMeasurementWithPhoneNumber

```c++
void InitiateOnDeviceConversionMeasurementWithPhoneNumber(
  const char *phone_number
)
```
Initiates on-device conversion measurement given a phone number in E.164 format on iOS (no-op on Android).

On iOS, requires dependency GoogleAppMeasurementOnDeviceConversion to be linked in, otherwise it is a no-op.

| Details ||
|---|---|
| Parameters | |---|---| | `phone_number` | User phone number. Must be in E.164 format, which means it must be limited to a maximum of 15 digits and must include a plus sign (+) prefix and country code with no dashes, parentheses, or spaces. | |

### IsDesktopInitialized

```c++
bool IsDesktopInitialized()
```
Returns whether the desktop Analytics SDK is initialized.

Returns true if the Analytics SDK is initialized, false otherwise. The method only works on windows and is a NO-OP on iOS and Android.

### LogEvent

```c++
void LogEvent(
  const char *name,
  const char *parameter_name,
  const char *parameter_value
)
```
Log an event with one string parameter.


**See also:**
[LogEvent(const char\*, const Parameter\*, size_t)](https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a638c62aa918c2cb5d23740c19fb911df)

| Details ||
|---|---|
| Parameters | |---|---| | `name` | Name of the event to log. Should contain 1 to 40 alphanumeric characters or underscores. The name must start with an alphabetic character. Some event names are reserved. See [Analytics Events](https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names) (event_names.h) for the list of reserved event names. The "firebase_" prefix is reserved and should not be used. Note that event names are case-sensitive and that logging two events whose names differ only in case will result in two distinct events. | | `parameter_name` | Name of the parameter to log. For more information, see [Parameter](https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter#structfirebase_1_1analytics_1_1_parameter). | | `parameter_value` | Value of the parameter to log. | |

### LogEvent

```c++
void LogEvent(
  const char *name,
  const char *parameter_name,
  const double parameter_value
)
```
Log an event with one float parameter.


**See also:**
[LogEvent(const char\*, const Parameter\*, size_t)](https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a638c62aa918c2cb5d23740c19fb911df)

| Details ||
|---|---|
| Parameters | |---|---| | `name` | Name of the event to log. Should contain 1 to 40 alphanumeric characters or underscores. The name must start with an alphabetic character. Some event names are reserved. See [Analytics Events](https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names) (event_names.h) for the list of reserved event names. The "firebase_" prefix is reserved and should not be used. Note that event names are case-sensitive and that logging two events whose names differ only in case will result in two distinct events. | | `parameter_name` | Name of the parameter to log. For more information, see [Parameter](https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter#structfirebase_1_1analytics_1_1_parameter). | | `parameter_value` | Value of the parameter to log. | |

### LogEvent

```c++
void LogEvent(
  const char *name,
  const char *parameter_name,
  const int64_t parameter_value
)
```
Log an event with one 64-bit integer parameter.


**See also:**
[LogEvent(const char\*, const Parameter\*, size_t)](https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a638c62aa918c2cb5d23740c19fb911df)

| Details ||
|---|---|
| Parameters | |---|---| | `name` | Name of the event to log. Should contain 1 to 40 alphanumeric characters or underscores. The name must start with an alphabetic character. Some event names are reserved. See [Analytics Events](https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names) (event_names.h) for the list of reserved event names. The "firebase_" prefix is reserved and should not be used. Note that event names are case-sensitive and that logging two events whose names differ only in case will result in two distinct events. | | `parameter_name` | Name of the parameter to log. For more information, see [Parameter](https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter#structfirebase_1_1analytics_1_1_parameter). | | `parameter_value` | Value of the parameter to log. | |

### LogEvent

```c++
void LogEvent(
  const char *name,
  const char *parameter_name,
  const int parameter_value
)
```
Log an event with one integer parameter (stored as a 64-bit integer).


**See also:**
[LogEvent(const char\*, const Parameter\*, size_t)](https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a638c62aa918c2cb5d23740c19fb911df)

| Details ||
|---|---|
| Parameters | |---|---| | `name` | Name of the event to log. Should contain 1 to 40 alphanumeric characters or underscores. The name must start with an alphabetic character. Some event names are reserved. See [Analytics Events](https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names) (event_names.h) for the list of reserved event names. The "firebase_" prefix is reserved and should not be used. Note that event names are case-sensitive and that logging two events whose names differ only in case will result in two distinct events. | | `parameter_name` | Name of the parameter to log. For more information, see [Parameter](https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter#structfirebase_1_1analytics_1_1_parameter). | | `parameter_value` | Value of the parameter to log. | |

### LogEvent

```c++
void LogEvent(
  const char *name
)
```
Log an event with no parameters.


**See also:**
[LogEvent(const char\*, const Parameter\*, size_t)](https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a638c62aa918c2cb5d23740c19fb911df)

| Details ||
|---|---|
| Parameters | |---|---| | `name` | Name of the event to log. Should contain 1 to 40 alphanumeric characters or underscores. The name must start with an alphabetic character. Some event names are reserved. See [Analytics Events](https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names) (event_names.h) for the list of reserved event names. The "firebase_" prefix is reserved and should not be used. Note that event names are case-sensitive and that logging two events whose names differ only in case will result in two distinct events. | |

### LogEvent

```c++
void LogEvent(
  const char *name,
  const Parameter *parameters,
  size_t number_of_parameters
)
```
Log an event with associated parameters.

An Event is an important occurrence in your app that you want to measure. You can report up to 500 different types of events per app and you can associate up to 25 unique parameters with each Event type.

Some common events are documented in [Analytics Events](https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names) (event_names.h), but you may also choose to specify custom event types that are associated with your specific app.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `name` | Name of the event to log. Should contain 1 to 40 alphanumeric characters or underscores. The name must start with an alphabetic character. Some event names are reserved. See [Analytics Events](https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names) (event_names.h) for the list of reserved event names. The "firebase_" prefix is reserved and should not be used. Note that event names are case-sensitive and that logging two events whose names differ only in case will result in two distinct events. | | `parameters` | Array of [Parameter](https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter#structfirebase_1_1analytics_1_1_parameter) structures. | | `number_of_parameters` | Number of elements in the parameters array. | |

### LogEvent

```c++
void LogEvent(
  const char *name,
  const std::vector< Parameter > & parameters
)
```
Log an event with associated parameters.

An Event is an important occurrence in your app that you want to measure. You can report up to 500 different types of events per app and you can associate up to 25 unique parameters with each Event type.

Some common events are documented in [Analytics Events](https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names) (event_names.h), but you may also choose to specify custom event types that are associated with your specific app.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `name` | Name of the event to log. Should contain 1 to 40 alphanumeric characters or underscores. The name must start with an alphabetic character. Some event names are reserved. See [Analytics Events](https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names) (event_names.h) for the list of reserved event names. The "firebase_" prefix is reserved and should not be used. Note that event names are case-sensitive and that logging two events whose names differ only in case will result in two distinct events. | | `parameters` | Vector of [Parameter](https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter#structfirebase_1_1analytics_1_1_parameter) structures. | |

### NotifyAppLifecycleChange

```c++
void NotifyAppLifecycleChange(
  AppLifecycleState state
)
```
Notifies the current state of the app's lifecycle.

This method is used to notify the Analytics SDK about the current state of the app's lifecycle. The Analytics SDK will use this information to log events, update user properties, upload data, etc. The method only works on windows and is a NO-OP on iOS and Android.

kTermination is used to indicate that the app is about to be terminated. The caller will be blocked until all pending data is uploaded or an error occurs. The caller must ensure the OS does not terminate background threads before the call returns. Currently only works for Windows Desktop.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `state` | The current state of the app's lifecycle. | |

### ResetAnalyticsData

```c++
void ResetAnalyticsData()
```
Clears all analytics data for this app from the device and resets the app instance id.

### SetAnalyticsCollectionEnabled

```c++
void SetAnalyticsCollectionEnabled(
  bool enabled
)
```
Sets whether analytics collection is enabled for this app on this device.

This setting is persisted across app sessions. By default it is enabled.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `enabled` | true to enable analytics collection, false to disable. | |

### SetConsent

```c++
void SetConsent(
  const std::map< ConsentType, ConsentStatus > & consent_settings
)
```
Sets the applicable end user consent state (e.g., for device identifiers) for this app on this device.

Use the consent map to specify individual consent type values. Settings are persisted across app sessions. By default consent types are set to "granted".

### SetDefaultEventParameters

```c++
void SetDefaultEventParameters(
  const Parameter *parameters,
  size_t number_of_parameters
)
```
Adds parameters that will be set on every event logged from the SDK.

Adds parameters that will be set on every event logged from the SDK, including automatic ones. The values passed in the parameters bundle will be added to the map of default event parameters. These parameters persist across app runs. They are of lower precedence than event parameters, so if an event parameter and a parameter set using this API have the same name, the value of the event parameter will be used. The same limitations on event parameters apply to default event parameters.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `parameters` | Array of [Parameter](https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter#structfirebase_1_1analytics_1_1_parameter) structures. | | `number_of_parameters` | Number of elements in the parameters array. | |

### SetDefaultEventParameters

```c++
void SetDefaultEventParameters(
  const std::vector< Parameter > & parameters
)
```
Adds parameters that will be set on every event logged from the SDK.

Adds parameters that will be set on every event logged from the SDK, including automatic ones. The values passed in the parameters bundle will be added to the map of default event parameters. These parameters persist across app runs. They are of lower precedence than event parameters, so if an event parameter and a parameter set using this API have the same name, the value of the event parameter will be used. The same limitations on event parameters apply to default event parameters.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `parameters` | reference to vector of [Parameter](https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter#structfirebase_1_1analytics_1_1_parameter) structures. | |

### SetDesktopDebugMode

```c++
void SetDesktopDebugMode(
  bool enabled
)
```
Sets whether desktop debug mode is enabled.

This methods enables desktop debug mode for the analytics SDK. The method only works on windows and is a NO-OP on iOS and Android.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `enabled` | A flag that enables or disables debug mode. | |

### SetLogCallback

```c++
void SetLogCallback(
  const LogCallback & callback
)
```
Allows the passing of a callback to be used when the SDK logs any messages regarding its behaviour.

The callback must be thread-safe.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `callback` | The callback to use. Must be thread-safe. | |

### SetSessionTimeoutDuration

```c++
void SetSessionTimeoutDuration(
  int64_t milliseconds
)
```
Sets the duration of inactivity that terminates the current session.


> [!NOTE]
> **Note:** The default value is 1800000 (30 minutes).

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `milliseconds` | The duration of inactivity that terminates the current session. | |

### SetUserId

```c++
void SetUserId(
  const char *user_id
)
```
Sets the user ID property.

This feature must be used in accordance with [Google's Privacy Policy](https://www.google.com/policies/privacy)

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `user_id` | The user ID associated with the user of this app on this device. The user ID must be non-empty and no more than 256 characters long. Setting user_id to NULL or nullptr removes the user ID. | |

### SetUserProperty

```c++
void SetUserProperty(
  const char *name,
  const char *property
)
```
Set a user property to the given value.

Properties associated with a user allow a developer to segment users into groups that are useful to their application. Up to 25 properties can be associated with a user.

Suggested property names are listed [Analytics User Properties](https://firebase.google.com/docs/reference/cpp/group/user-property-names#group__user__property__names) (user_property_names.h) but you're not limited to this set. For example, the "gamertype" property could be used to store the type of player where a range of values could be "casual", "mid_core", or "core".

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `name` | Name of the user property to set. This must be a combination of letters and digits (matching the regular expression \[a-zA-Z0-9\] between 1 and 40 characters long starting with a letter \[a-zA-Z\] character. | | `property` | Value to set the user property to. Set this argument to NULL or nullptr to remove the user property. The value can be between 1 to 100 characters long. | |

### Terminate

```c++
void Terminate()
```
Terminate the Analytics API.

Cleans up resources associated with the API.