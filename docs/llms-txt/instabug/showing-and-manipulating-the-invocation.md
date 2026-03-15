# Source: https://docs.instabug.com/references/invocation/showing-and-manipulating-the-invocation.md

# Building Luciq

You can use these methods to build Luciq in your project so that you can invoke it. This method takes a **string token** and **any number of invocation events** as an argument. This method will require that you have Luciq already installed. For more information on how to fully install and integrate **Luciq**, please refer to the relevant documentation sections here:

* [iOS](https://docs.luciq.ai/docs/ios-integration)
* [Android](https://docs.luciq.ai/docs/android-integration)
* [React Native](https://docs.luciq.ai/docs/react-native-integration)
* [Flutter](https://docs.luciq.ai/docs/flutter-integration)

{% tabs fullWidth="false" %}
{% tab title="iOS - Swift" %}

```swift
Luciq.start(withToken: "YOUR-TOKEN-HERE", invocationEvents: [.shake, .screenshot]);
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
[Luciq startWithToken:@"YOUR-TOKEN-HERE" invocationEvents: LCQInvocationEventShake | LCQInvocationEventScreenshot]
```

{% endtab %}

{% tab title="And - Java" %}

```java
new Luciq.Builder(this, "APP_TOKEN")
    .setInvocationEvents(LuciqInvocationEvent.SHAKE, LuciqInvocationEvent.SCREENSHOT)
    .build();
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Luciq.Builder(this, "APP_TOKEN")
            .setInvocationEvents(LuciqInvocationEvent.SHAKE, LuciqInvocationEvent.SCREENSHOT)
            .build()
```

{% endtab %}

{% tab title="RN" %}

```javascript
//iOS
Luciq.startWithToken('IOS_APP_TOKEN', [Luciq.invocationEvent.shake]);

//Android
new RNLuciqReactnativePackage.Builder("TOKEN",MainApplication.this)
							.build();
```

{% endtab %}

{% tab title="Flutter" %}

```dart
//iOS
Luciq.start('APP_TOKEN', [InvocationEvent.shake]);

//Android
ArrayList<String> invocationEvents = new ArrayList<>();
invocationEvents.add(LuciqFlutterPlugin.INVOCATION_EVENT_SHAKE);
new LuciqFlutterPlugin().start(CustomFlutterApplication.this, "APP_TOKEN", invocationEvents);
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
//iOS
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

//Android
"none"
"shake"
"screenshot"
"swipe"
"button"
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
