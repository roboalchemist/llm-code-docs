# Source: https://docs.luciq.ai/references/bug-reporting/extended-bug-report-mode.md

# Extended Bug Report Mode

This method can be used to show additional details in your bug reports. You can find more details on what it does here:

* [iOS](https://docs.luciq.ai/docs/ios-extended-bug-report)
* [Android](https://docs.luciq.ai/docs/android-extended-bug-report)
* [React Native](https://docs.luciq.ai/docs/react-native-extended-bug-report)
* [Cordova](https://docs.luciq.ai/docs/cordova-extended-bug-report)
* [Xamarin](https://docs.luciq.ai/docs/xamarin-extended-bug-report)

There is a single argument for this method that determines if the mode is enabled or not. The possible options are:

* Disable extended bug report mode
* Enable extended bug report mode and set fields to required
* Enable extended bug report mode and set fields to optional

**Method**

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
BugReporting.extendedBugReportMode = .enabledWithRequiredFields
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
LCQBugReporting.extendedBugReportMode = LCQExtendedBugReportModeEnabledWithRequiredFields;
```

{% endtab %}

{% tab title="And - Java" %}

```java
BugReporting.setExtendedBugReportState(ExtendedBugReport.State.ENABLED_WITH_REQUIRED_FIELDS);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
BugReporting.setExtendedBugReportState(ExtendedBugReport.State.ENABLED_WITH_REQUIRED_FIELDS)
```

{% endtab %}

{% tab title="RN" %}

```javascript
import { ExtendedBugReportMode } from '@luciq/react-native';

BugReporting.setExtendedBugReportMode(ExtendedBugReportMode.enabledWithRequiredFields;);
```

{% endtab %}

{% tab title="Flutter" %}

```csharp
BugReporting.setExtendedBugReportMode(ExtendedBugReportMode.enabledWithRequiredFields;);
```

{% endtab %}
{% endtabs %}

**Report Mode Options Parameters:**

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
//Disabled
.disabled
//Enabled and Required
.enabledWithRequiredFields
//Enabled and Optional
.enabledWithOptionalFields
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
//Disabled
LCQExtendedBugReportModeDisabled
//Enabled and Required
LCQExtendedBugReportModeEnabledWithRequiredFields
//Enabled and Optional
LCQExtendedBugReportModeEnabledWithOptionalFields
```

{% endtab %}

{% tab title="Android" %}

```java
//Disabled
ExtendedBugReport.State.DISABLED
//Enabled and Required
ExtendedBugReport.State.ENABLED_WITH_REQUIRED_FIELDS
//Enabled and Optional
ExtendedBugReport.State.ENABLED_WITH_OPTIONAL_FIELDS
```

{% endtab %}

{% tab title="RN" %}

```javascript
//Disabled
ExtendedBugReportMode.disabled
//Enabled and Required
ExtendedBugReportMode.enabledWithRequiredFields;
//Enabled and Optional
ExtendedBugReportMode.enabledWithOptionalFields
```

{% endtab %}

{% tab title="Flutter" %}

```dart
//Disabled
ExtendedBugReportMode.disabled
//Enabled and Required
ExtendedBugReportMode.enabledWithRequiredFields;
//Enabled and Optional
ExtendedBugReportMode.enabledWithOptionalFields
```

{% endtab %}
{% endtabs %}
