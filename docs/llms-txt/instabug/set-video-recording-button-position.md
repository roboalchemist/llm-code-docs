# Source: https://docs.instabug.com/references/user-interface-design/set-video-recording-button-position.md

# Set Video Recording Button Position

Use this API to set the position of the video recording button when using the screen recording attachment functionality. This API can take an enum of the position.

**Method**

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
BugReporting.videoRecordingFloatingButtonPosition = .topLeft
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
LCQBugReporting.videoRecordingFloatingButtonPosition = LCQPositionTopLeft;
```

{% endtab %}

{% tab title="And - Java" %}

```java
BugReporting.setVideoRecordingFloatingButtonPosition(LuciqVideoRecordingButtonPosition.TOP_LEFT);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
BugReporting.setVideoRecordingFloatingButtonPosition(LuciqVideoRecordingButtonPosition.TOP_LEFT)
```

{% endtab %}

{% tab title="RN" %}

```javascript
BugReporting.setVideoRecordingFloatingButtonPosition(BugReporting.position.topLeft);
```

{% endtab %}

{% tab title="Flutter" %}

```dart
BugReporting.setVideoRecordingFloatingButtonPosition(Position.topLeft);
```

{% endtab %}
{% endtabs %}

#### Position Parameters

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
//Top Left
.topLeft
//Top Right
.topRight
//Bottom Left
.bottomLeft
//Bottom Right
.bottomRight
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
//Top Left
LCQPositionTopLeft
//Top Right
LCQPositionTopRight
//Bottom Left
LCQPositionBottomLeft
//Bottom Right
LCQPositionBottomRight
```

{% endtab %}

{% tab title="And - Java" %}

```java
//Top Left
TOP_LEFT
//Top Right
TOP_RIGHT
//Bottom Left
BOTTOM_LEFT
//Bottom Right
BOTTOM_RIGHT
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
//Top Left
TOP_LEFT
//Top Right
TOP_RIGHT
//Bottom Left
BOTTOM_LEFT
//Bottom Right
BOTTOM_RIGHT
```

{% endtab %}

{% tab title="RN" %}

```javascript
//Top Left
BugReporting.position.topLeft
//Top Right
BugReporting.position.topRight
//Bottom Left
BugReporting.position.bottomLeft
//Bottom Right
BugReporting.position.bottomLeft
```

{% endtab %}

{% tab title="Flutter" %}

```dart
//Top Left
Position.topLeft
//Top Right
Position.topRight
//Bottom Left
Position.bottomLeft
//Bottom Right
Position.bottomLeft
```

{% endtab %}
{% endtabs %}
