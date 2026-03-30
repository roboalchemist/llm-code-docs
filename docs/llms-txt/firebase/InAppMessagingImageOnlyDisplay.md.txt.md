# Source: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingImageOnlyDisplay.md.txt

# FirebaseInAppMessagingDisplay Framework Reference

# InAppMessagingImageOnlyDisplay

    class InAppMessagingImageOnlyDisplay : https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingDisplayMessage.html

Class for defining a image-only message for display.
- `


  ### [imageData](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingImageOnlyDisplay#/c:objc(cs)FIRInAppMessagingImageOnlyDisplay(py)imageData)


  ` Gets the image for this message

  #### Declaration

  Swift

      @NSCopying var imageData: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingImageData.html { get }

- `


  ### [actionURL](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingImageOnlyDisplay#/c:objc(cs)FIRInAppMessagingImageOnlyDisplay(py)actionURL)


  ` Gets the action URL for an image-only fiam message.

  #### Declaration

  Swift

      var actionURL: URL? { get }

- `


  ### [-init](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingImageOnlyDisplay#/c:objc(cs)FIRInAppMessagingImageOnlyDisplay(im)init)


  ` Unavailable.
- `


  ### [init(messageID:campaignName:renderAsTestMessage:triggerType:imageData:actionURL:)](https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingImageOnlyDisplay#/c:objc(cs)FIRInAppMessagingImageOnlyDisplay(im)initWithMessageID:campaignName:renderAsTestMessage:triggerType:imageData:actionURL:)


  ` Deprecated, this class shouldn't be directly instantiated.

  #### Declaration

  Swift

      init(messageID: String, campaignName: String, renderAsTestMessage: Bool, triggerType: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Enums/FIRInAppMessagingDisplayTriggerType.html, imageData: https://firebase.google.com/docs/reference/swift/firebaseinappmessagingdisplay/api/reference/Classes/InAppMessagingImageData.html?, actionURL: URL?)