# Source: https://docs.luciq.ai/references/report-data/attachments/set-attachment-types.md

# Set Attachment Types

You can set the types of attachments your users can add to reports using this API.

The available attachment types are:

* Initial Screenshot
* Extra Screenshot
* Gallery Image
* Screen Recording

**Method:**

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
BugReporting.enabledAttachmentTypes = [.screenShot, .extraScreenShot]
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
LCQBugReporting.enabledAttachmentTypes = LCQAttachmentTypeScreenShot | LCQAttachmentTypeExtraScreenshot;
```

{% endtab %}

{% tab title="And - Java" %}

```java
// Arguments: initialScreenshot, extraScreenshot, galleryImage & ScreenRecording
BugReporting.setAttachmentTypesEnabled(true, true, true, true);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
// Arguments:initialScreenshot, extraScreenshot, galleryImage & ScreenRecording
BugReporting.setAttachmentTypesEnabled(true, true, true, true);
```

{% endtab %}

{% tab title="RN" %}

```javascript
BugReporting.setEnabledAttachmentTypes(screenshot, extraScreenshot, galleryImage, screenRecording);

//All properties are boolean values
```

{% endtab %}

{% tab title="Flutter" %}

```csharp
//Boolean Arguments
BugReporting.setEnabledAttachmentTypes(screenshot, extraScreenshot, galleryImage, screenRecording);
```

{% endtab %}
{% endtabs %}

**Attachment Types Enums:**

{% tabs %}
{% tab title="iOS - Swift" %}

```swift
//Inital Screenshot
.screenShot
//Extra Screenshot
.extraScreenShot
//Gallery Image
.galleryImage
//Screen Recording
.screenRecording
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objective-c
//Inital Screenshot
LCQAttachmentTypeScreenshot;
//Extra Screenshot
LCQAttachmentTypeExtraScreenshot;
//Gallery Image
LCQAttachmentTypeGalleryImage;
//Screen Recording
LCQAttachmentTypeScreenRecording;
```

{% endtab %}
{% endtabs %}

**Screen Recording Encoder:**\
For the Screen Recording, you can define a custom configuration using the API below:

{% tabs %}
{% tab title="And - Java" %}

```java
Luciq.setVideoEncoderConfig(VideoEncoderConfig config);
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Luciq.setVideoEncoderConfig(config: VideoEncoderConfig)
```

{% endtab %}
{% endtabs %}
