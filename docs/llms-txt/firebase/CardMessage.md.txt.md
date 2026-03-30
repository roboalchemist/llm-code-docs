# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage.md.txt

# CardMessage

# CardMessage


```
public class CardMessage extends InAppMessage
```

<br />

|---|---|---|
| [java.lang.Object](https://developer.android.com/reference/kotlin/java/lang/Object.html) |||
| ↳ | [com.google.firebase.inappmessaging.model.InAppMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage) ||
|   | ↳ | [com.google.firebase.inappmessaging.model.CardMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage) |

*** ** * ** ***

Encapsulates a Firebase In App Card Message.

## Summary

| ### Public fields |
|---|---|
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage#backgroundHexColor()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Text` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage#body()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageData` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage#landscapeImageData()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageData` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage#portraitImageData()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Action` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage#primaryAction()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Action` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage#secondaryAction()` |
| `final @https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Text` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage#title()` !!!!!WARNING!!!!! We are overriding equality in this class. |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Action` | `[getAction](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage#getAction())()` **This method is deprecated.** Use `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage#getPrimaryAction()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage#getSecondaryAction()` instead. <br /> |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage#getBackgroundHexColor()()` Gets the background hex color associated with this message |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Text` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage#getBody()()` Gets the body `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Text` associated with this message |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageData` | `[getImageData](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage#getImageData())()` **This method is deprecated.** Use `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage#getPortraitImageData()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage#getLandscapeImageData()` instead. <br /> |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageData` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage#getLandscapeImageData()()` Gets the `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageData` displayed when the phone is in a landscape orientation |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageData` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage#getPortraitImageData()()` Gets the `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageData` displayed when the phone is in a portrait orientation |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Action` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage#getPrimaryAction()()` Gets the primary `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Action` associated with this message. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Action` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage#getSecondaryAction()()` Gets the secondary `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Action` associated with this message |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Text` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage#getTitle()()` Gets the title `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Text` associated with this message |

| ### Inherited fields |
|---|
| From [com.google.firebase.inappmessaging.model.InAppMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage) |---|---| | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Button` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#actionButton()` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#campaignId()` | | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CampaignMetadata` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#campaignMetadata()` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#campaignName()` | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/String.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#data()` | | `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#imageUrl()` | | `https://developer.android.com/reference/kotlin/java/lang/Boolean.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#isTestMessage()` | | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/MessageType` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#messageType()` | |

| ### Inherited methods |
|---|
| From [com.google.firebase.inappmessaging.model.InAppMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage) |---|---| | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Button` | `[getActionButton](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getActionButton())()` **This method is deprecated.** Use the message specific methods (see `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ModalMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/BannerMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageOnlyMessage`) instead. <br /> | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `[getCampaignId](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getCampaignId())()` **This method is deprecated.** Use `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getCampaignMetadata()` instead. <br /> | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CampaignMetadata` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getCampaignMetadata()()` Gets the `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CampaignMetadata` of the message | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `[getCampaignName](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getCampaignName())()` **This method is deprecated.** Use `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getCampaignMetadata()` instead. <br /> | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/String.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getData()()` Gets the extra data map of the message. | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `[getImageUrl](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getImageUrl())()` **This method is deprecated.** Use the message specific methods (see `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ModalMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/BannerMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageOnlyMessage`) instead. <br /> | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Boolean.html` | `[getIsTestMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getIsTestMessage())()` **This method is deprecated.** Use `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getCampaignMetadata()` instead. <br /> | | `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/MessageType` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getMessageType()()` Gets the `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/MessageType` of the message | |

## Public fields

### backgroundHexColor

```
public final @NonNull String backgroundHexColor
```

### body

```
public final @Nullable Text body
```

### landscapeImageData

```
public final @Nullable ImageData landscapeImageData
```

### portraitImageData

```
public final @Nullable ImageData portraitImageData
```

### primaryAction

```
public final @NonNull Action primaryAction
```

### secondaryAction

```
public final @Nullable Action secondaryAction
```

### title

```
public final @NonNull Text title
```

!!!!!WARNING!!!!! We are overriding equality in this class. Please add equality checks for all new private class members.

## Public methods

### getAction

```
public @Nullable Action [getAction](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage#getAction())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Use `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage#getPrimaryAction()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage#getSecondaryAction()` instead.

### getBackgroundHexColor

```
public @NonNull String getBackgroundHexColor()
```

Gets the background hex color associated with this message

### getBody

```
public @Nullable Text getBody()
```

Gets the body `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Text` associated with this message

### getImageData

```
public @Nullable ImageData [getImageData](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage#getImageData())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Use `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage#getPortraitImageData()` or `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage#getLandscapeImageData()` instead.

### getLandscapeImageData

```
public @Nullable ImageData getLandscapeImageData()
```

Gets the `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageData` displayed when the phone is in a landscape orientation

### getPortraitImageData

```
public @Nullable ImageData getPortraitImageData()
```

Gets the `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageData` displayed when the phone is in a portrait orientation

### getPrimaryAction

```
public @NonNull Action getPrimaryAction()
```

Gets the primary `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Action` associated with this message. If none is defined, the primary action is 'dismiss'

### getSecondaryAction

```
public @Nullable Action getSecondaryAction()
```

Gets the secondary `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Action` associated with this message

### getTitle

```
public @NonNull Text getTitle()
```

Gets the title `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Text` associated with this message