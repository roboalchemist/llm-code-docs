# Source: https://firebase.google.com/docs/ml/ios/recognize-text-deprecated.md.txt

> [!CAUTION]
> This page describes an old version of recognizing text in images using the
> deprecated Firebase ML Vision sdk. As an alternative, you may
> [call
> Cloud Vision APIs using Firebase Auth and Callable Functions](https://firebase.google.com/docs/ml/ios/recognize-text) to allow only users logged
> into your app to access the API.

[Video](https://www.youtube.com/watch?v=T9TAsurJdmk)

You can use Firebase ML to recognize text in images. Firebase ML has
both a general-purpose API suitable for recognizing text in images, such as
the text of a street sign, and an API optimized for recognizing the text of
documents.
Use of the Cloud Vision APIs is subject to the [Google Cloud Platform License
Agreement](https://cloud.google.com/terms/) and [Service
Specific Terms](https://cloud.google.com/terms/service-terms), and billed accordingly. For billing information, see the [Pricing](https://cloud.google.com/vision/pricing) page.

> [!NOTE]
> **Looking for on-device text recognition?** Try the [standalone ML Kit library](https://developers.google.com/ml-kit/vision/text-recognition).

<br />

## Before you begin

If you have not already added Firebase to your app, do so by following the steps in the [getting started guide](https://firebase.google.com/docs/ios/setup).
1. Use Swift Package Manager to install and manage Firebase dependencies.

> [!NOTE]
> Visit [our installation guide](https://firebase.google.com/docs/ios/installation-methods) to learn about the different ways you can add Firebase SDKs to your Apple project.

1. In Xcode, with your app project open, navigate to **File \> Add Packages**.
2. When prompted, add the Firebase Apple platforms SDK repository:

```
  https://github.com/firebase/firebase-ios-sdk.git
```

> [!NOTE]
> **Note:** New projects should use the default (latest) SDK version, but you can choose an older version if needed.

3. Choose the Firebase ML library.
4. Add the `-ObjC` flag to the *Other Linker Flags* section of your target's build settings.
5. When finished, Xcode will automatically begin resolving and downloading your dependencies in the background.
2. Next, perform some in-app setup:
1. In your app, import Firebase:

   #### Swift

   ```swift
   import FirebaseMLModelDownloader
   ```

   #### Objective-C

   ```objective-c
   @import FirebaseMLModelDownloader;
   ```
3. If you haven't already enabled Cloud-based APIs for your project, do so
   now:

   1. Open the [Firebase ML
      APIs page](https://console.firebase.google.com/project/_/ml/apis) in the Firebase console.
   2. If you haven't already upgraded your project to the
      [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing), click **Upgrade** to do so. (You'll be
      prompted to upgrade only if your project isn't on the
      Blaze pricing plan.)

      Only projects on the Blaze pricing plan can use
      Cloud-based APIs.
   3. If Cloud-based APIs aren't already enabled, click **Enable Cloud-based APIs**.

   Before you deploy to production an app that uses a Cloud API, you should take some additional steps to [prevent and mitigate the
   effect of unauthorized API access](https://firebase.google.com/docs/ml/ios/secure-api-key).

Now you are ready to start recognizing text in images.

## Input image guidelines

- For Firebase ML to accurately recognize text, input images must contain
  text that is represented by sufficient pixel data. Ideally, for Latin
  text, each character should be at least 16x16 pixels. For Chinese,
  Japanese, and Korean text, each
  character should be 24x24 pixels. For all languages, there is generally no
  accuracy benefit for characters to be larger than 24x24 pixels.

  So, for example, a 640x480 image might work well to scan a business card
  that occupies the full width of the image. To scan a document printed on
  letter-sized paper, a 720x1280 pixel image might be required.
- Poor image focus can hurt text recognition accuracy. If you aren't
  getting acceptable results, try asking the user to recapture the image.

*** ** * ** ***

## Recognize text in images

To recognize text in an image, run the text recognizer as described
below.

### 1. Run the text recognizer

Pass the image as a `UIImage` or a `CMSampleBufferRef` to the `VisionTextRecognizer`'s `process(_:completion:)` method:

<br />

1. Get an instance of `VisionTextRecognizer` by calling `cloudTextRecognizer`:

   #### Swift

   ```swift
   let vision = Vision.vision()
   let textRecognizer = vision.cloudTextRecognizer()

   // Or, to provide language hints to assist with language detection:
   // See https://cloud.google.com/vision/docs/languages for supported languages
   let options = VisionCloudTextRecognizerOptions()
   options.languageHints = ["en", "hi"]
   let textRecognizer = vision.cloudTextRecognizer(options: options)
   ```

   #### Objective-C

   ```objective-c
   FIRVision *vision = [FIRVision vision];
   FIRVisionTextRecognizer *textRecognizer = [vision cloudTextRecognizer];

   // Or, to provide language hints to assist with language detection:
   // See https://cloud.google.com/vision/docs/languages for supported languages
   FIRVisionCloudTextRecognizerOptions *options =
           [[FIRVisionCloudTextRecognizerOptions alloc] init];
   options.languageHints = @[@"en", @"hi"];
   FIRVisionTextRecognizer *textRecognizer = [vision cloudTextRecognizerWithOptions:options];
   ```
2. In order to call Cloud Vision, the image must be formatted as a base64-encoded string. To process a `UIImage`:

   #### Swift

   ```swift
   guard let imageData = uiImage.jpegData(compressionQuality: 1.0) else { return }
   let base64encodedImage = imageData.base64EncodedString()
   ```

   #### Objective-C

   ```objective-c
   NSData *imageData = UIImageJPEGRepresentation(uiImage, 1.0f);
   NSString *base64encodedImage =
     [imageData base64EncodedStringWithOptions:NSDataBase64Encoding76CharacterLineLength];
   ```
3. Then, pass the image to the `process(_:completion:)` method:

   #### Swift

   ```swift
   textRecognizer.process(visionImage) { result, error in
     guard error == nil, let result = result else {
       // ...
       return
     }

     // Recognized text
   }
   ```

   #### Objective-C

   ```objective-c
   [textRecognizer processImage:image
                     completion:^(FIRVisionText *_Nullable result,
                                  NSError *_Nullable error) {
     if (error != nil || result == nil) {
       // ...
       return;
     }

     // Recognized text
   }];
   ```

### 2. Extract text from blocks of recognized text

If the text recognition operation succeeds, it will return a [`VisionText`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionText) object. A `VisionText` object contains the full text recognized in the image and zero or more [`VisionTextBlock`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextBlock) objects.

<br />

Each `VisionTextBlock` represents a rectangular block of text, which contain
zero or more [`VisionTextLine`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextLine) objects. Each `VisionTextLine`
object contains zero or more [`VisionTextElement`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextElement) objects,
which represent words and word-like entities (dates, numbers, and so on).

For each `VisionTextBlock`, `VisionTextLine`, and `VisionTextElement` object,
you can get the text recognized in the region and the bounding coordinates of
the region.

For example:

#### Swift

```swift
let resultText = result.text
for block in result.blocks {
    let blockText = block.text
    let blockConfidence = block.confidence
    let blockLanguages = block.recognizedLanguages
    let blockCornerPoints = block.cornerPoints
    let blockFrame = block.frame
    for line in block.lines {
        let lineText = line.text
        let lineConfidence = line.confidence
        let lineLanguages = line.recognizedLanguages
        let lineCornerPoints = line.cornerPoints
        let lineFrame = line.frame
        for element in line.elements {
            let elementText = element.text
            let elementConfidence = element.confidence
            let elementLanguages = element.recognizedLanguages
            let elementCornerPoints = element.cornerPoints
            let elementFrame = element.frame
        }
    }
}
```

#### Objective-C

```objective-c
NSString *resultText = result.text;
for (FIRVisionTextBlock *block in result.blocks) {
  NSString *blockText = block.text;
  NSNumber *blockConfidence = block.confidence;
  NSArray<FIRVisionTextRecognizedLanguage *> *blockLanguages = block.recognizedLanguages;
  NSArray<NSValue *> *blockCornerPoints = block.cornerPoints;
  CGRect blockFrame = block.frame;
  for (FIRVisionTextLine *line in block.lines) {
    NSString *lineText = line.text;
    NSNumber *lineConfidence = line.confidence;
    NSArray<FIRVisionTextRecognizedLanguage *> *lineLanguages = line.recognizedLanguages;
    NSArray<NSValue *> *lineCornerPoints = line.cornerPoints;
    CGRect lineFrame = line.frame;
    for (FIRVisionTextElement *element in line.elements) {
      NSString *elementText = element.text;
      NSNumber *elementConfidence = element.confidence;
      NSArray<FIRVisionTextRecognizedLanguage *> *elementLanguages = element.recognizedLanguages;
      NSArray<NSValue *> *elementCornerPoints = element.cornerPoints;
      CGRect elementFrame = element.frame;
    }
  }
}
```

### Next steps

- Before you deploy to production an app that uses a Cloud API, you should take some additional steps to [prevent and mitigate the
  effect of unauthorized API access](https://firebase.google.com/docs/ml/ios/secure-api-key).

*** ** * ** ***

## Recognize text in images of documents

To recognize the text of a document, configure and run the
document text recognizer as described below.

The document text recognition API, described below, provides an interface that
is intended to be more convenient for working with images of documents. However,
if you prefer the interface provided by the sparse text API, you can use it
instead to scan documents by configuring the cloud text recognizer to
[use the dense text model](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudTextRecognizerOptions#modeltype).

To use the document text recognition API:

### 1. Run the text recognizer

Pass the image as a `UIImage` or a `CMSampleBufferRef` to the `VisionDocumentTextRecognizer`'s `process(_:completion:)` method:

<br />

1. Get an instance of `VisionDocumentTextRecognizer` by calling `cloudDocumentTextRecognizer`:

   #### Swift

   ```swift
   let vision = Vision.vision()
   let textRecognizer = vision.cloudDocumentTextRecognizer()

   // Or, to provide language hints to assist with language detection:
   // See https://cloud.google.com/vision/docs/languages for supported languages
   let options = VisionCloudDocumentTextRecognizerOptions()
   options.languageHints = ["en", "hi"]
   let textRecognizer = vision.cloudDocumentTextRecognizer(options: options)
   ```

   #### Objective-C

   ```objective-c
   FIRVision *vision = [FIRVision vision];
   FIRVisionDocumentTextRecognizer *textRecognizer = [vision cloudDocumentTextRecognizer];

   // Or, to provide language hints to assist with language detection:
   // See https://cloud.google.com/vision/docs/languages for supported languages
   FIRVisionCloudDocumentTextRecognizerOptions *options =
           [[FIRVisionCloudDocumentTextRecognizerOptions alloc] init];
   options.languageHints = @[@"en", @"hi"];
   FIRVisionDocumentTextRecognizer *textRecognizer = [vision cloudDocumentTextRecognizerWithOptions:options];
   ```
2. In order to call Cloud Vision, the image must be formatted as a base64-encoded string. To process a `UIImage`:

   #### Swift

   ```swift
   guard let imageData = uiImage.jpegData(compressionQuality: 1.0) else { return }
   let base64encodedImage = imageData.base64EncodedString()
   ```

   #### Objective-C

   ```objective-c
   NSData *imageData = UIImageJPEGRepresentation(uiImage, 1.0f);
   NSString *base64encodedImage =
     [imageData base64EncodedStringWithOptions:NSDataBase64Encoding76CharacterLineLength];
   ```
3. Then, pass the image to the `process(_:completion:)` method:

   #### Swift

   ```swift
   textRecognizer.process(visionImage) { result, error in
     guard error == nil, let result = result else {
       // ...
       return
     }

     // Recognized text
   }
   ```

   #### Objective-C

   ```objective-c
   [textRecognizer processImage:image
                     completion:^(FIRVisionDocumentText *_Nullable result,
                                  NSError *_Nullable error) {
     if (error != nil || result == nil) {
       // ...
       return;
     }

       // Recognized text
   }];
   ```

### 2. Extract text from blocks of recognized text

If the text recognition operation succeeds, it will return a [`VisionDocumentText`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentText) object. A `VisionDocumentText` object contains the full text recognized in the image and a hierarchy of objects that reflect the structure of the recognized document:

<br />

- [`VisionDocumentTextBlock`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextBlock)
- [`VisionDocumentTextParagraph`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextParagraph)
- [`VisionDocumentTextWord`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextWord)
- [`VisionDocumentTextSymbol`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextSymbol)

For each `VisionDocumentTextBlock`, `VisionDocumentTextParagraph`,
`VisionDocumentTextWord`, and `VisionDocumentTextSymbol` object, you can get the
text recognized in the region and the bounding coordinates of the region.

For example:

#### Swift

```swift
let resultText = result.text
for block in result.blocks {
    let blockText = block.text
    let blockConfidence = block.confidence
    let blockRecognizedLanguages = block.recognizedLanguages
    let blockBreak = block.recognizedBreak
    let blockCornerPoints = block.cornerPoints
    let blockFrame = block.frame
    for paragraph in block.paragraphs {
        let paragraphText = paragraph.text
        let paragraphConfidence = paragraph.confidence
        let paragraphRecognizedLanguages = paragraph.recognizedLanguages
        let paragraphBreak = paragraph.recognizedBreak
        let paragraphCornerPoints = paragraph.cornerPoints
        let paragraphFrame = paragraph.frame
        for word in paragraph.words {
            let wordText = word.text
            let wordConfidence = word.confidence
            let wordRecognizedLanguages = word.recognizedLanguages
            let wordBreak = word.recognizedBreak
            let wordCornerPoints = word.cornerPoints
            let wordFrame = word.frame
            for symbol in word.symbols {
                let symbolText = symbol.text
                let symbolConfidence = symbol.confidence
                let symbolRecognizedLanguages = symbol.recognizedLanguages
                let symbolBreak = symbol.recognizedBreak
                let symbolCornerPoints = symbol.cornerPoints
                let symbolFrame = symbol.frame
            }
        }
    }
}
```

#### Objective-C

```objective-c
NSString *resultText = result.text;
for (FIRVisionDocumentTextBlock *block in result.blocks) {
  NSString *blockText = block.text;
  NSNumber *blockConfidence = block.confidence;
  NSArray<FIRVisionTextRecognizedLanguage *> *blockRecognizedLanguages = block.recognizedLanguages;
  FIRVisionTextRecognizedBreak *blockBreak = block.recognizedBreak;
  CGRect blockFrame = block.frame;
  for (FIRVisionDocumentTextParagraph *paragraph in block.paragraphs) {
    NSString *paragraphText = paragraph.text;
    NSNumber *paragraphConfidence = paragraph.confidence;
    NSArray<FIRVisionTextRecognizedLanguage *> *paragraphRecognizedLanguages = paragraph.recognizedLanguages;
    FIRVisionTextRecognizedBreak *paragraphBreak = paragraph.recognizedBreak;
    CGRect paragraphFrame = paragraph.frame;
    for (FIRVisionDocumentTextWord *word in paragraph.words) {
      NSString *wordText = word.text;
      NSNumber *wordConfidence = word.confidence;
      NSArray<FIRVisionTextRecognizedLanguage *> *wordRecognizedLanguages = word.recognizedLanguages;
      FIRVisionTextRecognizedBreak *wordBreak = word.recognizedBreak;
      CGRect wordFrame = word.frame;
      for (FIRVisionDocumentTextSymbol *symbol in word.symbols) {
        NSString *symbolText = symbol.text;
        NSNumber *symbolConfidence = symbol.confidence;
        NSArray<FIRVisionTextRecognizedLanguage *> *symbolRecognizedLanguages = symbol.recognizedLanguages;
        FIRVisionTextRecognizedBreak *symbolBreak = symbol.recognizedBreak;
        CGRect symbolFrame = symbol.frame;
      }
    }
  }
}
```

### Next steps

- Before you deploy to production an app that uses a Cloud API, you should take some additional steps to [prevent and mitigate the
  effect of unauthorized API access](https://firebase.google.com/docs/ml/ios/secure-api-key).