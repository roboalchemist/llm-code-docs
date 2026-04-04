# Source: https://docs.instabug.com/references/invocation/change-invocation-event.md

# Change Invocation Event

You can change the way Luciq is invoked at runtime using this method. This method takes any number of **Invocation Events** as an argument.

Below are all the possible invocation event triggers:

**Method**

{% tabs fullWidth="false" %}
{% tab title="iOS - Swift" %}

```swift
BugReporting.invocationEvents = [.shake, .screenshot]
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
LCQBugReporting.invocationEvents = LCQInvocationEventShake | LCQInvocationEventScreenshot;
```

{% endtab %}

{% tab title="And - Java" %}

```java
BugReporting.setInvocationEvents(LuciqInvocationEvent.SHAKE, LuciqInvocationEvent.SCREENSHOT);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
BugReporting.setInvocationEvents(LuciqInvocationEvent.SHAKE, LuciqInvocationEvent.SCREENSHOT)
```

{% endtab %}

{% tab title="RN" %}

```javascript
BugReporting.setInvocationEvents([Luciq.invocationEvent.shake])
```

{% endtab %}

{% tab title="Flutter" %}

```dart
BugReporting.setInvocationEvents(List<InvocationEvent> invocationEvents)
```

{% endtab %}
{% endtabs %}

**Invocation Event Parameters:**

{% tabs fullWidth="false" %}
{% tab title="iOS - Swift" %}

```swift
//No Trigger
.none
//Shake
.shake
//Screenshot
.screenshot
//Two Finger Swipe Left
.twoFingersSwipeLeft
//Right Edge Pan
.rightEdgePan
//Floating Button
.floatingButton
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
//No Trigger
LCQInvocationEventNone
//Shake
LCQInvocationEventShake
//Screenshot
LCQInvocationEventScreenshot
//Two Finger Swipe Left
LCQInvocationEventTwoFingersSwipeLeft
//Right Edge Pan
LCQInvocationEventRightEdgePan
//Floating Button
LCQInvocationEventFloatingButton
```

{% endtab %}

{% tab title="And - Java" %}

```java
//No Trigger
NONE
//Shake
SHAKE
//Screenshot
SCREENSHOT
//Two Finger Swipe Left
TWO_FINGER_SWIPE_LEFT
//Floating Button
FLOATING_BUTTON
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
//No Trigger
NONE
//Shake
SHAKE
//Screenshot
SCREENSHOT
//Two Finger Swipe Left
TWO_FINGER_SWIPE_LEFT
//Floating Button
FLOATING_BUTTON
```

{% endtab %}

{% tab title="RN" %}

```javascript
//No Trigger
Luciq.invocationEvent.none
//Shake
Luciq.invocationEvent.shake
//Screenshot
Luciq.invocationEvent.screenshot
//Two Finger Swipe Left
Luciq.invocationEvent.twoFingersSwipe
//Floating Button
Luciq.invocationEvent.floatingButton
```

{% endtab %}

{% tab title="Flutter" %}

```dart
//iOS
InvocationEvent.none
InvocationEvent.shake
InvocationEvent.screenshot
InvocationEvent.twoFingersSwipe
InvocationEvent.floatingButton

//Android
LuciqFlutterPlugin.INVOCATION_EVENT_NONE
LuciqFlutterPlugin.INVOCATION_EVENT_SHAKE
LuciqFlutterPlugin.INVOCATION_EVENT_SCREENSHOT
LuciqFlutterPlugin.INVOCATION_EVENT_SWIPE
LuciqFlutterPlugin.INVOCATION_EVENT_BUTTON
```

{% endtab %}
{% endtabs %}
