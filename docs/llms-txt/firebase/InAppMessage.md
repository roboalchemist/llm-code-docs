# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/InAppMessage.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage.md.txt

# InAppMessage

# InAppMessage


```
abstract class InAppMessage
```

<br />

Known direct subclasses  
[BannerMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/BannerMessage), [CardMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/CardMessage), [ImageOnlyMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/ImageOnlyMessage), [ModalMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/ModalMessage)  

|---------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| [BannerMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/BannerMessage)       | Encapsulates a Firebase In App Banner Message.    |
| [CardMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/CardMessage)           | Encapsulates a Firebase In App Card Message.      |
| [ImageOnlyMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/ImageOnlyMessage) | Encapsulates a Firebase In App ImageOnly Message. |
| [ModalMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/ModalMessage)         | Encapsulates a Firebase In App Modal Message.     |

*** ** * ** ***

Encapsulates a Firebase In App Message.

## Summary

|                                                   ### Public functions                                                    |
|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `abstract `[Action](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/Action)`?` | ~~[getAction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#getAction())~~`()` **This function is deprecated.** Use the message specific methods (see [CardMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/CardMessage), [ModalMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/ModalMessage), [BannerMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/BannerMessage), [ImageOnlyMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/ImageOnlyMessage)) instead. <br /> |

|                                                                                                                                                                            ### Public properties                                                                                                                                                                            |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| [Button](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/Button)`!`                                                                                                                                                                                                                                                              | [actionButton](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#actionButton())             |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!`                                                                                                                                                                                                                                                                                         | [backgroundHexColor](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#backgroundHexColor()) |
| [Text](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/Text)`!`                                                                                                                                                                                                                                                                  | [body](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#body())                             |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!`                                                                                                                                                                                                                                                                                         | [campaignId](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#campaignId())                 |
| [CampaignMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/CampaignMetadata)`!`                                                                                                                                                                                                                                          | [campaignMetadata](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#campaignMetadata())     |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!`                                                                                                                                                                                                                                                                                         | [campaignName](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#campaignName())             |
| `(`[Mutable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-map/index.html)`)`[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-map/index.html)`<`[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!, `[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!>?` | [data](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#data())                             |
| [ImageData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/ImageData)`!`                                                                                                                                                                                                                                                        | [imageData](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#imageData())                   |
| [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html)`!`                                                                                                                                                                                                                                                                                         | [imageUrl](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#imageUrl())                     |
| [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-boolean/index.html)`!`                                                                                                                                                                                                                                                                                       | [isTestMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#isTestMessage())           |
| [MessageType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/MessageType)`!`                                                                                                                                                                                                                                                    | [messageType](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#messageType())               |
| [Text](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/Text)`!`                                                                                                                                                                                                                                                                  | [title](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#title())                           |

## Public functions

### getAction

```
abstractÂ funÂ [getAction](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/InAppMessage#getAction())():Â Action?
```
| **This function is deprecated.**   
|
Use the message specific methods (see [CardMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/CardMessage), [ModalMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/ModalMessage), [BannerMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/BannerMessage), [ImageOnlyMessage](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/inappmessaging/model/ImageOnlyMessage)) instead.  

## Public properties

### actionButton

```
valÂ actionButton:Â Button!
```  

### backgroundHexColor

```
valÂ backgroundHexColor:Â String!
```  

### body

```
valÂ body:Â Text!
```  

### campaignId

```
valÂ campaignId:Â String!
```  

### campaignMetadata

```
valÂ campaignMetadata:Â CampaignMetadata!
```  

### campaignName

```
valÂ campaignName:Â String!
```  

### data

```
valÂ data:Â (Mutable)Map<String!,Â String!>?
```  

### imageData

```
valÂ imageData:Â ImageData!
```  

### imageUrl

```
valÂ imageUrl:Â String!
```  

### isTestMessage

```
valÂ isTestMessage:Â Boolean!
```  

### messageType

```
valÂ messageType:Â MessageType!
```  

### title

```
valÂ title:Â Text!
```