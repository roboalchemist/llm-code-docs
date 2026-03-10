# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage.md.txt

# InAppMessage

# InAppMessage


```
abstract class InAppMessage
```

<br />

Known direct subclasses [BannerMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/BannerMessage), [CardMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/CardMessage), [ImageOnlyMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/ImageOnlyMessage), [ModalMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/ModalMessage)

|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/BannerMessage` | Encapsulates a Firebase In App Banner Message. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/CardMessage` | Encapsulates a Firebase In App Card Message. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/ImageOnlyMessage` | Encapsulates a Firebase In App ImageOnly Message. |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/ModalMessage` | Encapsulates a Firebase In App Modal Message. |

*** ** * ** ***

Encapsulates a Firebase In App Message.

## Summary

| ### Public functions |
|---|---|
| `abstract https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/Action?` | `[getAction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#getAction())()` **This function is deprecated.** Use the message specific methods (see `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/CardMessage`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/ModalMessage`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/BannerMessage`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/ImageOnlyMessage`) instead. <br /> |

| ### Public properties |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/Button!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#actionButton()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#backgroundHexColor()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/Text!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#body()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#campaignId()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/CampaignMetadata!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#campaignMetadata()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#campaignName()` |
| `(https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html<https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!, https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!>?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#data()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/ImageData!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#imageData()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#imageUrl()` |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#isTestMessage()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/MessageType!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#messageType()` |
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/Text!` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#title()` |

## Public functions

### getAction

```
abstract fun [getAction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#getAction())(): Action?
```

> [!CAUTION]
> **This function is deprecated.**   
>
> Use the message specific methods (see `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/CardMessage`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/ModalMessage`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/BannerMessage`, `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/ImageOnlyMessage`) instead.

## Public properties

### actionButton

```
val actionButton: Button!
```

### backgroundHexColor

```
val backgroundHexColor: String!
```

### body

```
val body: Text!
```

### campaignId

```
val campaignId: String!
```

### campaignMetadata

```
val campaignMetadata: CampaignMetadata!
```

### campaignName

```
val campaignName: String!
```

### data

```
val data: (Mutable)Map<String!, String!>?
```

### imageData

```
val imageData: ImageData!
```

### imageUrl

```
val imageUrl: String!
```

### isTestMessage

```
val isTestMessage: Boolean!
```

### messageType

```
val messageType: MessageType!
```

### title

```
val title: Text!
```