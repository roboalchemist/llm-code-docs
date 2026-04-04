# Source: https://firebase.google.com/docs/reference/cpp/struct/firebase/analytics/parameter.md.txt

# Source: https://firebase.google.com/docs/reference/unity/class/firebase/analytics/parameter.md.txt

# Firebase.Analytics.Parameter Class Reference

# Firebase.Analytics.Parameter

Event parameter.

## Summary

Parameters supply information that contextualize events (see LogEvent). You can associate up to 25 unique Parameters with each event type (name).

Common event types are provided as static properties of the [FirebaseAnalytics](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#class_firebase_1_1_analytics_1_1_firebase_analytics) class (e.g [FirebaseAnalytics.EventPostScore](https://firebase.google.com/docs/reference/unity/group/event-names#group__event__names_1gae6c7bae26bf168725550d92fde85686b)) where parameters of these events are also provided in this [FirebaseAnalytics](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#class_firebase_1_1_analytics_1_1_firebase_analytics) class (e.g [FirebaseAnalytics.ParameterScore](https://firebase.google.com/docs/reference/unity/group/parameter-names#group__parameter__names_1gac69aa0a217496876f0e5a9aedf98b853)).

You are not limited to the set of event types and parameter names suggested in [FirebaseAnalytics](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/firebase-analytics#class_firebase_1_1_analytics_1_1_firebase_analytics) class properties. Additional Parameters can be supplied for suggested event types or custom Parameters for custom event types.

[Parameter](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/parameter#class_firebase_1_1_analytics_1_1_parameter) names must be a combination of letters and digits (matching the regular expression \[a-zA-Z0-9\]) between 1 and 40 characters long starting with a letter \[a-zA-Z\] character. The "firebase_", "google_" and "ga_" prefixes are reserved and should not be used.

[Parameter](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/parameter#class_firebase_1_1_analytics_1_1_parameter) string values can be up to 100 characters long.

An array of [Parameter](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/parameter#class_firebase_1_1_analytics_1_1_parameter) class instances can be passed to LogEvent in order to associate parameters's of an event with values where each value can be a double, 64-bit integer or string.

For example, a game may log an achievement event along with the character the player is using and the level they're currently on:


```c#
using Firebase.Analytics;

int currentLevel = GetCurrentLevel();
Parameter[] AchievementParameters = {
  new Parameter(FirebaseAnalytics.ParameterAchievementID,
                "ultimate_wizard"),
  new Parameter(FirebaseAnalytics.ParameterCharacter, "mysterion"),
  new Parameter(FirebaseAnalytics.ParameterLevel, currentLevel),
};
FirebaseAnalytics.LogEvent(FirebaseAnalytics.EventLevelUp,
                           AchievementParameters);
```

<br />

| ### Constructors and Destructors ||
|---|---|
| [Parameter](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/parameter#class_firebase_1_1_analytics_1_1_parameter_1a49b506a973b11fcb697cd6e88d8820d6)`(string parameterName, string parameterValue)` ||
| [Parameter](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/parameter#class_firebase_1_1_analytics_1_1_parameter_1a858ca9f11994cd3bcc4269e85d8c1719)`(string parameterName, long parameterValue)` ||
| [Parameter](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/parameter#class_firebase_1_1_analytics_1_1_parameter_1aeeee33485121a1ae6db869f3f2d65bc1)`(string parameterName, double parameterValue)` ||
| [Parameter](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/parameter#class_firebase_1_1_analytics_1_1_parameter_1ab8ff3659e207a8de19f5b3b3241cf831)`(string parameterName, IDictionary< string, object > parameterValue)` ||
| [Parameter](https://firebase.google.com/docs/reference/unity/class/firebase/analytics/parameter#class_firebase_1_1_analytics_1_1_parameter_1ab281d29182ca20b7b12b8a643242e696)`(string parameterName, IEnumerable< IDictionary< string, object >> parameterValue)` ||

## Public functions

### Parameter

```c#
 Parameter(
  string parameterName,
  string parameterValue
)
```  

### Parameter

```c#
 Parameter(
  string parameterName,
  long parameterValue
)
```  

### Parameter

```c#
 Parameter(
  string parameterName,
  double parameterValue
)
```  

### Parameter

```c#
 Parameter(
  string parameterName,
  IDictionary< string, object > parameterValue
)
```  

### Parameter

```c#
 Parameter(
  string parameterName,
  IEnumerable< IDictionary< string, object >> parameterValue
)
```