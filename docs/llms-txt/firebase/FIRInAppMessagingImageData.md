# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Classes/FIRInAppMessagingImageData.md.txt

# Source: https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingImageData.md.txt

# FirebaseInAppMessagingDisplay Framework Reference

# FIRInAppMessagingImageData


    @interface FIRInAppMessagingImageData : NSObject

Contain display data for an image for a fiam message.
- `
  ``
  ``
  `

  ### [imageURL](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingImageData#/c:objc(cs)FIRInAppMessagingImageData(py)imageURL)

  `
  `  
  Gets the image URL from image data.  

  #### Declaration

  Objective-C  

      @property (readonly, copy, nonatomic, nonnull) NSString *imageURL;

- `
  ``
  ``
  `

  ### [imageRawData](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingImageData#/c:objc(cs)FIRInAppMessagingImageData(py)imageRawData)

  `
  `  
  Gets the downloaded image data. It can be null if headless component fails to load it.  

  #### Declaration

  Objective-C  

      @property (readonly, nonatomic, nullable) NSData *imageRawData;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingImageData#/c:objc(cs)FIRInAppMessagingImageData(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;

- `
  ``
  ``
  `

  ### [-initWithImageURL:imageData:](https://firebase.google.com/docs/reference/ios/firebaseinappmessagingdisplay/api/reference/Classes/FIRInAppMessagingImageData#/c:objc(cs)FIRInAppMessagingImageData(im)initWithImageURL:imageData:)

  `
  `  
  Deprecated, this class shouldn't be directly instantiated.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)initWithImageURL:(nonnull NSString *)imageURL
                                     imageData:(nonnull NSData *)imageData;