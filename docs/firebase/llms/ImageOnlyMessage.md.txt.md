# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageOnlyMessage.md.txt

# ImageOnlyMessage

# ImageOnlyMessage


```
public class ImageOnlyMessage extends InAppMessage
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [com.google.firebase.inappmessaging.model.InAppMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage) ||
|   | ↳ | [com.google.firebase.inappmessaging.model.ImageOnlyMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageOnlyMessage) |

*** ** * ** ***

Encapsulates a Firebase In App ImageOnly Message.

## Summary

| ### Public fields |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Action` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageOnlyMessage#action()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageData` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageOnlyMessage#imageData()` !!!!!WARNING!!!!! We are overriding equality in this class. |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Action` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageOnlyMessage#getAction()()` Gets the `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Action` associated with this message |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageData` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageOnlyMessage#getImageData()()` Gets the `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageData` associated with this message |

| ### Inherited fields |
|---|
| From [com.google.firebase.inappmessaging.model.InAppMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage) |---|---| | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Button` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#actionButton()` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#backgroundHexColor()` | | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Text` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#body()` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#campaignId()` | | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CampaignMetadata` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#campaignMetadata()` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#campaignName()` | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/String.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#data()` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#imageUrl()` | | `https://developer.android.com/reference/kotlin/java/lang/Boolean.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#isTestMessage()` | | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/MessageType` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#messageType()` | | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Text` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#title()` | |

| ### Inherited methods |
|---|
| From [com.google.firebase.inappmessaging.model.InAppMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage) |---|---| | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Button` | `[getActionButton](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getActionButton())()` **This method is deprecated.** Use the message specific methods (see `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ModalMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/BannerMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageOnlyMessage`) instead. <br /> | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `[getBackgroundHexColor](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getBackgroundHexColor())()` **This method is deprecated.** Use the message specific methods (see `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ModalMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/BannerMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageOnlyMessage`) instead. <br /> | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Text` | `[getBody](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getBody())()` **This method is deprecated.** Use the message specific methods (see `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ModalMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/BannerMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageOnlyMessage`) instead. <br /> | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `[getCampaignId](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getCampaignId())()` **This method is deprecated.** Use `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getCampaignMetadata()` instead. <br /> | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CampaignMetadata` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getCampaignMetadata()()` Gets the `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CampaignMetadata` of the message | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `[getCampaignName](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getCampaignName())()` **This method is deprecated.** Use `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getCampaignMetadata()` instead. <br /> | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/String.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getData()()` Gets the extra data map of the message. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `[getImageUrl](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getImageUrl())()` **This method is deprecated.** Use the message specific methods (see `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ModalMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/BannerMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageOnlyMessage`) instead. <br /> | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Boolean.html` | `[getIsTestMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getIsTestMessage())()` **This method is deprecated.** Use `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getCampaignMetadata()` instead. <br /> | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/MessageType` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getMessageType()()` Gets the `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/MessageType` of the message | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Text` | `[getTitle](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getTitle())()` **This method is deprecated.** Use the message specific methods (see `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ModalMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/BannerMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageOnlyMessage`) instead. <br /> | |

## Public fields

### action

```
public @Nullable Action action
```

### imageData

```
public @NonNull ImageData imageData
```

!!!!!WARNING!!!!! We are overriding equality in this class. Please add equality checks for all new private class members.

## Public methods

### getAction

```
public @Nullable Action getAction()
```

Gets the `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Action` associated with this message

### getImageData

```
public @NonNull ImageData getImageData()
```

Gets the `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageData` associated with this message