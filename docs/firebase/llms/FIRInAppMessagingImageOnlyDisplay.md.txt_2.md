# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingImageOnlyDisplay.md.txt

# FirebaseInAppMessaging Framework Reference

# FIRInAppMessagingImageOnlyDisplay


    @interface FIRInAppMessagingImageOnlyDisplay : https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingDisplayMessage.html

Class for defining a image-only message for display.
This class is unavailable on macOS, macOS Catalyst, and watchOS.
- `


  ### [imageData](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingImageOnlyDisplay#/c:objc(cs)FIRInAppMessagingImageOnlyDisplay(py)imageData)


  ` Gets the image for this message

  #### Declaration

  Objective-C

      @property (nonatomic, copy, readonly, nonnull) https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingImageData.html *imageData;

- `


  ### [actionURL](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingImageOnlyDisplay#/c:objc(cs)FIRInAppMessagingImageOnlyDisplay(py)actionURL)


  ` Gets the action URL for an image-only fiam message.

  #### Declaration

  Objective-C

      @property (nonatomic, readonly, nullable) NSURL *actionURL;

- `


  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingImageOnlyDisplay#/c:objc(cs)FIRInAppMessagingImageOnlyDisplay(im)init)


  ` Unavailable
  Unavailable.

  #### Declaration

  Objective-C

      - (nonnull instancetype)init;

- `


  ### [-initWithCampaignName:imageData:actionURL:appData:](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingImageOnlyDisplay#/c:objc(cs)FIRInAppMessagingImageOnlyDisplay(im)initWithCampaignName:imageData:actionURL:appData:)


  ` Exposed for unit testing only, or for use in SwiftUI previews. Don't instantiate this in your
  app directly.

  #### Declaration

  Objective-C

      - (nonnull instancetype)
          initWithCampaignName:(nonnull NSString *)campaignName
                     imageData:(nonnull https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingImageData.html *)imageData
                     actionURL:(nullable NSURL *)actionURL
                       appData:(nullable NSDictionary *)appData;