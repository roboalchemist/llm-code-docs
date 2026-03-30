# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingImageData.md.txt

# FirebaseInAppMessaging Framework Reference

# FIRInAppMessagingImageData


    @interface FIRInAppMessagingImageData : NSObject

Contain display data for an image for a fiam message.

- This class is unavailable on macOS, macOS Catalyst, and watchOS.
- `


  ### [imageURL](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingImageData#/c:objc(cs)FIRInAppMessagingImageData(py)imageURL)


  ` Gets the image URL from image data.

  #### Declaration

  Objective-C

      @property (nonatomic, copy, readonly, nonnull) NSString *imageURL;

- `


  ### [imageRawData](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingImageData#/c:objc(cs)FIRInAppMessagingImageData(py)imageRawData)


  ` Gets the downloaded image data. It can be null if headless component fails to load it.

  #### Declaration

  Objective-C

      @property (nonatomic, readonly, nullable) NSData *imageRawData;

- `


  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingImageData#/c:objc(cs)FIRInAppMessagingImageData(im)init)


  ` Unavailable
  Unavailable.

  #### Declaration

  Objective-C

      - (nonnull instancetype)init;

- `


  ### [-initWithImageURL:imageData:](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingImageData#/c:objc(cs)FIRInAppMessagingImageData(im)initWithImageURL:imageData:)


  ` Exposed for unit testing only, or for use in SwiftUI previews. Don't instantiate this in your
  app directly.

  #### Declaration

  Objective-C

      - (nonnull instancetype)initWithImageURL:(nonnull NSString *)imageURL
                                     imageData:(nonnull NSData *)imageData;