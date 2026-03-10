# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/BannerMessage.md.txt

# BannerMessage

# BannerMessage


```
class BannerMessage : InAppMessage
```

<br />

|---|---|---|
| [kotlin.Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html) |||
| ↳ | [com.google.firebase.inappmessaging.model.InAppMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage) ||
|   | ↳ | [com.google.firebase.inappmessaging.model.BannerMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/BannerMessage) |

*** ** * ** ***

Encapsulates a Firebase In App Banner Message.

## Summary

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/Action?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/BannerMessage#action()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/BannerMessage#backgroundHexColor()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/Text?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/BannerMessage#body()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/ImageData?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/BannerMessage#imageData()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/Text` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/BannerMessage#title()` !!!!!WARNING!!!!! We are overriding equality in this class. |

| ### Inherited functions |
|---|
| From [com.google.firebase.inappmessaging.model.InAppMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage) |---|---| | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/Button?` | `[getActionButton](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#getActionButton())()` **This function is deprecated.** Use the message specific methods (see `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/CardMessage`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/ModalMessage`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/BannerMessage`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/ImageOnlyMessage`) instead. <br /> | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `[getCampaignId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#getCampaignId())()` **This function is deprecated.** Use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#getCampaignMetadata()` instead. <br /> | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/CampaignMetadata?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#getCampaignMetadata()()` Gets the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/CampaignMetadata` of the message | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `[getCampaignName](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#getCampaignName())()` **This function is deprecated.** Use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#getCampaignMetadata()` instead. <br /> | | `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#getData()()` Gets the extra data map of the message. | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `[getImageUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#getImageUrl())()` **This function is deprecated.** Use the message specific methods (see `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/CardMessage`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/ModalMessage`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/BannerMessage`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/ImageOnlyMessage`) instead. <br /> | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html?` | `[getIsTestMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#getIsTestMessage())()` **This function is deprecated.** Use `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#getCampaignMetadata()` instead. <br /> | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/MessageType?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#getMessageType()()` Gets the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/MessageType` of the message | |

| ### Inherited properties |
|---|
| From [com.google.firebase.inappmessaging.model.InAppMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage) |---|---| | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/Button!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#actionButton()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#campaignId()` | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/CampaignMetadata!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#campaignMetadata()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#campaignName()` | | `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#data()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#imageUrl()` | | `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#isTestMessage()` | | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/MessageType!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#messageType()` | |

## Public properties

### action

```
val action: Action?
```

### backgroundHexColor

```
val backgroundHexColor: String
```

### body

```
val body: Text?
```

### imageData

```
val imageData: ImageData?
```

### title

```
val title: Text
```

!!!!!WARNING!!!!! We are overriding equality in this class. Please add equality checks for all new private class members.