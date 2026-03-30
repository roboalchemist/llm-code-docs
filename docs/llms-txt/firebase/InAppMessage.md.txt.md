# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage.md.txt

# InAppMessage

# InAppMessage


```
public abstract class InAppMessage
```

<br />

Known direct subclasses [BannerMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/BannerMessage), [CardMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage), [ImageOnlyMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageOnlyMessage), [ModalMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ModalMessage)

|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/BannerMessage` | Encapsulates a Firebase In App Banner Message. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage` | Encapsulates a Firebase In App Card Message. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageOnlyMessage` | Encapsulates a Firebase In App ImageOnly Message. |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ModalMessage` | Encapsulates a Firebase In App Modal Message. |

*** ** * ** ***

Encapsulates a Firebase In App Message.

## Summary

| ### Public fields |
|---|---|
| `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Button` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#actionButton()` |
| `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#backgroundHexColor()` |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Text` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#body()` |
| `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#campaignId()` |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CampaignMetadata` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#campaignMetadata()` |
| `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#campaignName()` |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/String.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#data()` |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageData` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#imageData()` |
| `https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#imageUrl()` |
| `https://developer.android.com/reference/kotlin/java/lang/Boolean.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#isTestMessage()` |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/MessageType` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#messageType()` |
| `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Text` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#title()` |

| ### Public methods |
|---|---|
| `abstract @https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Action` | `[getAction](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getAction())()` **This method is deprecated.** Use the message specific methods (see `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ModalMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/BannerMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageOnlyMessage`) instead. <br /> |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Button` | `[getActionButton](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getActionButton())()` **This method is deprecated.** Use the message specific methods (see `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ModalMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/BannerMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageOnlyMessage`) instead. <br /> |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `[getBackgroundHexColor](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getBackgroundHexColor())()` **This method is deprecated.** Use the message specific methods (see `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ModalMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/BannerMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageOnlyMessage`) instead. <br /> |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Text` | `[getBody](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getBody())()` **This method is deprecated.** Use the message specific methods (see `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ModalMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/BannerMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageOnlyMessage`) instead. <br /> |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `[getCampaignId](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getCampaignId())()` **This method is deprecated.** Use `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getCampaignMetadata()` instead. <br /> |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CampaignMetadata` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getCampaignMetadata()()` Gets the `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CampaignMetadata` of the message |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `[getCampaignName](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getCampaignName())()` **This method is deprecated.** Use `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getCampaignMetadata()` instead. <br /> |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/util/Map.html<https://developer.android.com/reference/kotlin/java/lang/String.html, https://developer.android.com/reference/kotlin/java/lang/String.html>` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getData()()` Gets the extra data map of the message. |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageData` | `[getImageData](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getImageData())()` **This method is deprecated.** Use the message specific methods (see `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ModalMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/BannerMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageOnlyMessage`) instead. <br /> |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `[getImageUrl](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getImageUrl())()` **This method is deprecated.** Use the message specific methods (see `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ModalMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/BannerMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageOnlyMessage`) instead. <br /> |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://developer.android.com/reference/kotlin/java/lang/Boolean.html` | `[getIsTestMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getIsTestMessage())()` **This method is deprecated.** Use `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getCampaignMetadata()` instead. <br /> |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/MessageType` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getMessageType()()` Gets the `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/MessageType` of the message |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/Nullable.html https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/Text` | `[getTitle](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getTitle())()` **This method is deprecated.** Use the message specific methods (see `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ModalMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/BannerMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageOnlyMessage`) instead. <br /> |

## Public fields

### actionButton

```
public Button actionButton
```

### backgroundHexColor

```
public String backgroundHexColor
```

### body

```
public Text body
```

### campaignId

```
public String campaignId
```

### campaignMetadata

```
public CampaignMetadata campaignMetadata
```

### campaignName

```
public String campaignName
```

### data

```
public @Nullable Map<String, String> data
```

### imageData

```
public ImageData imageData
```

### imageUrl

```
public String imageUrl
```

### isTestMessage

```
public Boolean isTestMessage
```

### messageType

```
public MessageType messageType
```

### title

```
public Text title
```

## Public methods

### getAction

```
public abstract @Nullable Action [getAction](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getAction())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Use the message specific methods (see `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ModalMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/BannerMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageOnlyMessage`) instead.

### getActionButton

```
public @Nullable Button [getActionButton](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getActionButton())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Use the message specific methods (see `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ModalMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/BannerMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageOnlyMessage`) instead.

### getBackgroundHexColor

```
public @Nullable String [getBackgroundHexColor](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getBackgroundHexColor())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Use the message specific methods (see `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ModalMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/BannerMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageOnlyMessage`) instead.

### getBody

```
public @Nullable Text [getBody](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getBody())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Use the message specific methods (see `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ModalMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/BannerMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageOnlyMessage`) instead.

### getCampaignId

```
public @Nullable String [getCampaignId](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getCampaignId())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Use `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getCampaignMetadata()` instead.

### getCampaignMetadata

```
public @Nullable CampaignMetadata getCampaignMetadata()
```

Gets the `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CampaignMetadata` of the message

### getCampaignName

```
public @Nullable String [getCampaignName](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getCampaignName())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Use `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getCampaignMetadata()` instead.

### getData

```
public @Nullable Map<String, String> getData()
```

Gets the extra data map of the message. This is defined in the Firebase Console for each campaign.

### getImageData

```
public @Nullable ImageData [getImageData](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getImageData())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Use the message specific methods (see `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ModalMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/BannerMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageOnlyMessage`) instead.

### getImageUrl

```
public @Nullable String [getImageUrl](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getImageUrl())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Use the message specific methods (see `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ModalMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/BannerMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageOnlyMessage`) instead.

### getIsTestMessage

```
public @Nullable Boolean [getIsTestMessage](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getIsTestMessage())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Use `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getCampaignMetadata()` instead.

### getMessageType

```
public @Nullable MessageType getMessageType()
```

Gets the `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/MessageType` of the message

### getTitle

```
public @Nullable Text [getTitle](https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage#getTitle())()
```

> [!CAUTION]
> **This method is deprecated.**   
>
> Use the message specific methods (see `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CardMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ModalMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/BannerMessage`, `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/ImageOnlyMessage`) instead.