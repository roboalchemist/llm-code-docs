# Source: https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter.md.txt

# firebase::analytics::Parameter Struct Reference

# firebase::analytics::Parameter


`#include <analytics.h>`

Event parameter.

## Summary

Parameters supply information that contextualize events (see [LogEvent](https://firebase.google.com/docs/reference/cpp/namespace/firebase/analytics#namespacefirebase_1_1analytics_1a93b61cf7740883d81eeaa442d951ac82)). You can associate up to 25 unique Parameters with each event type (name).

Common event types (names) are suggested in [Analytics Events](https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names) (event_names.h) with parameters of common event types defined in [Analytics Parameters](https://firebase.google.com/docs/reference/cpp/group/parameter-names#group__parameter__names) (parameter_names.h).

You are not limited to the set of event types and parameter names suggested in [Analytics Events](https://firebase.google.com/docs/reference/cpp/group/event-names#group__event__names) (event_names.h) and parameter_names.h respectively. Additional Parameters can be supplied for suggested event types or custom Parameters for custom event types.

[Parameter](https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter#structfirebase_1_1analytics_1_1_parameter) names must be a combination of letters and digits (matching the regular expression \[a-zA-Z0-9\]) between 1 and 40 characters long starting with a letter \[a-zA-Z\] character. The "firebase_", "google_" and "ga_" prefixes are reserved and should not be used.

[Parameter](https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter#structfirebase_1_1analytics_1_1_parameter) string values can be up to 100 characters long.

An array of this structure is passed to LogEvent in order to associate parameter's of an event ([Parameter::name](https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter#structfirebase_1_1analytics_1_1_parameter_1aba705f47b129352dfef5d9481cf907d7)) with values ([Parameter::value](https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter#structfirebase_1_1analytics_1_1_parameter_1aa894317308ad4208f3a195c301005ed6)) where each value can be a double, 64-bit integer or string.

For example, a game may log an achievement event along with the character the player is using and the level they're currently on:


```c++
using namespace firebase::analytics;
int64_t current_level = GetCurrentLevel();
const Parameter achievement_parameters[] = {
  Parameter(kParameterAchievementID,  "ultimate_wizard"),
  Parameter(kParameterCharacter, "mysterion"),
  Parameter(kParameterLevel, current_level),
};
LogEvent(kEventUnlockAchievement, achievement_parameters,
         sizeof(achievement_parameters) /
         sizeof(achievement_parameters[0]));
```

<br />

| ### Constructors and Destructors ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter#structfirebase_1_1analytics_1_1_parameter_1aada5505c002bf36f1e35d484f6261087()` Construct an empty parameter. ||
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter#structfirebase_1_1analytics_1_1_parameter_1a88757052ac9bed32235a505e52e8cf7a(const char *parameter_name, https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant parameter_value)` Construct a parameter. ||
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter#structfirebase_1_1analytics_1_1_parameter_1a80d12a6d4e25636270c574561468e515(const char *parameter_name, int parameter_value)` Construct a 64-bit integer parameter. ||
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter#structfirebase_1_1analytics_1_1_parameter_1a0e3da2af18d007e67eb540efa9ed344c(const char *parameter_name, int64_t parameter_value)` Construct a 64-bit integer parameter. ||
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter#structfirebase_1_1analytics_1_1_parameter_1a79042aa646c0fec8b77981c5ce6e9157(const char *parameter_name, double parameter_value)` Construct a floating point parameter. ||
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter#structfirebase_1_1analytics_1_1_parameter_1abfb180cbd208825145e45f0e0576c4bc(const char *parameter_name, const char *parameter_value)` Construct a string parameter. ||

| ### Public attributes ||
|---|---|
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter#structfirebase_1_1analytics_1_1_parameter_1aba705f47b129352dfef5d9481cf907d7` | `const char *` Name of the parameter. |
| `https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter#structfirebase_1_1analytics_1_1_parameter_1aa894317308ad4208f3a195c301005ed6` | `https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant` Value of the parameter. |

## Public attributes

### name

```c++
const char * firebase::analytics::Parameter::name
```
Name of the parameter.

[Parameter](https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter#structfirebase_1_1analytics_1_1_parameter) names must be a combination of letters and digits (matching the regular expression \[a-zA-Z0-9\]) between 1 and 40 characters long starting with a letter \[a-zA-Z\] character. The "firebase_", "google_" and "ga_" prefixes are reserved and should not be used.

### value

```c++
Variant firebase::analytics::Parameter::value
```
Value of the parameter.

See [firebase::Variant](https://firebase.google.com/docs/reference/cpp/class/firebase/variant#classfirebase_1_1_variant) for usage information.

> [!NOTE]
> **Note:** String values can be up to 100 characters long.

<br />

## Public functions

### Parameter

```c++
 firebase::analytics::Parameter::Parameter()
```
Construct an empty parameter.

This is provided to allow initialization after construction.

### Parameter

```c++
 firebase::analytics::Parameter::Parameter(
  const char *parameter_name,
  Variant parameter_value
)
```
Construct a parameter.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `parameter_name` | Name of the parameter (see [Parameter::name](https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter#structfirebase_1_1analytics_1_1_parameter_1aba705f47b129352dfef5d9481cf907d7)). | | `parameter_value` | Value for the parameter. Variants can hold numbers and strings. | |

### Parameter

```c++
 firebase::analytics::Parameter::Parameter(
  const char *parameter_name,
  int parameter_value
)
```
Construct a 64-bit integer parameter.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `parameter_name` | Name of the parameter. (see [Parameter::name](https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter#structfirebase_1_1analytics_1_1_parameter_1aba705f47b129352dfef5d9481cf907d7)). | | `parameter_value` | Integer value for the parameter. | |

### Parameter

```c++
 firebase::analytics::Parameter::Parameter(
  const char *parameter_name,
  int64_t parameter_value
)
```
Construct a 64-bit integer parameter.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `parameter_name` | Name of the parameter. (see [Parameter::name](https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter#structfirebase_1_1analytics_1_1_parameter_1aba705f47b129352dfef5d9481cf907d7)). | | `parameter_value` | Integer value for the parameter. | |

### Parameter

```c++
 firebase::analytics::Parameter::Parameter(
  const char *parameter_name,
  double parameter_value
)
```
Construct a floating point parameter.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `parameter_name` | Name of the parameter. (see [Parameter::name](https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter#structfirebase_1_1analytics_1_1_parameter_1aba705f47b129352dfef5d9481cf907d7)). | | `parameter_value` | Floating point value for the parameter. | |

### Parameter

```c++
 firebase::analytics::Parameter::Parameter(
  const char *parameter_name,
  const char *parameter_value
)
```
Construct a string parameter.

<br />

| Details ||
|---|---|
| Parameters | |---|---| | `parameter_name` | Name of the parameter. (see [Parameter::name](https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter#structfirebase_1_1analytics_1_1_parameter_1aba705f47b129352dfef5d9481cf907d7)). | | `parameter_value` | String value for the parameter, can be up to 100 characters long. | |