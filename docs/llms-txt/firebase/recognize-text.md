# Source: https://firebase.google.com/docs/ml/recognize-text.md.txt

# Source: https://firebase.google.com/docs/ml/ios/recognize-text.md.txt

# Source: https://firebase.google.com/docs/ml/android/recognize-text.md.txt

# Source: https://firebase.google.com/docs/ml-kit/recognize-text.md.txt

# Source: https://firebase.google.com/docs/ml-kit/android/recognize-text.md.txt

# Source: https://firebase.google.com/docs/ml-kit/ios/recognize-text.md.txt

| This page describes an old version of the Text Recognition API, which was part of ML Kit for Firebase. The functionality of this API has been split into two new APIs ([learn more](https://developers.google.com/ml-kit/migration)):
|
| - [On-device text recognition](https://developers.google.com/ml-kit/vision/text-recognition/ios)is part of the new standalone ML Kit SDK, which you can use with or without Firebase.
- [Cloud text recognition](https://firebase.google.com/docs/ml/ios/recognize-text)is part ofFirebase ML, which includes all of Firebase's cloud-based ML features.  

You can use ML Kit to recognize text in images. ML Kit has both a general-purpose API suitable for recognizing text in images, such as the text of a street sign, and an API optimized for recognizing the text of documents. The general-purpose API has both on-device and cloud-based models. Document text recognition is available only as a cloud-based model. See the[overview](https://firebase.google.com/docs/ml-kit/recognize-text)for a comparison of the cloud and on-device models.

## Before you begin

1. If you have not already added Firebase to your app, do so by following the steps in the[getting started guide](https://firebase.google.com/docs/ios/setup).
2. Include the ML Kit libraries in your Podfile:  

   ```
   pod 'Firebase/MLVision', '6.25.0'
   # If using an on-device API:
   pod 'Firebase/MLVisionTextModel', '6.25.0'
   ```
   After you install or update your project's Pods, be sure to open your Xcode project using its`.xcworkspace`.
3. In your app, import Firebase:  

   #### Swift

   ```swift
   import Firebase
   ```

   #### Objective-C

   ```objective-c
   @import Firebase;
   ```
4. If you want to use the Cloud-based model, and you have not already enabled the Cloud-based APIs for your project, do so now:

   1. Open the[ML Kit APIs page](https://console.firebase.google.com/project/_/ml/apis)of theFirebaseconsole.
   2. If you have not already upgraded your project to a Blaze pricing plan, click**Upgrade**to do so. (You will be prompted to upgrade only if your project isn't on the Blaze plan.)

      Only Blaze-level projects can use Cloud-based APIs.
   3. If Cloud-based APIs aren't already enabled, click**Enable Cloud-based APIs**.

   | Before you deploy to production an app that uses a Cloud API, you should take some additional steps to[prevent and mitigate the effect of unauthorized API access](https://firebase.google.com/docs/ml-kit/ios/secure-api-key).

   If you want to use only the on-device model, you can skip this step.

Now you are ready to start recognizing text in images.

## Input image guidelines

- For ML Kit to accurately recognize text, input images must contain text that is represented by sufficient pixel data. Ideally, for Latin text, each character should be at least 16x16 pixels. For Chinese, Japanese, and Korean text (only supported by the cloud-based APIs), each character should be 24x24 pixels. For all languages, there is generally no accuracy benefit for characters to be larger than 24x24 pixels.

  So, for example, a 640x480 image might work well to scan a business card that occupies the full width of the image. To scan a document printed on letter-sized paper, a 720x1280 pixel image might be required.
- Poor image focus can hurt text recognition accuracy. If you aren't getting acceptable results, try asking the user to recapture the image.

- If you are recognizing text in a real-time application, you might also want to consider the overall dimensions of the input images. Smaller images can be processed faster, so to reduce latency, capture images at lower resolutions (keeping in mind the above accuracy requirements) and ensure that the text occupies as much of the image as possible. Also see[Tips to improve real-time performance](https://firebase.google.com/docs/ml-kit/ios/recognize-text#performance_tips).

*** ** * ** ***

## Recognize text in images

To recognize text in an image using either an on-device or cloud-based model, run the text recognizer as described below.

### 1. Run the text recognizer

Pass the image as a \`UIImage\` or a \`CMSampleBufferRef\` to the \`VisionTextRecognizer\`'s \`process(_:completion:)\` method:

1. Get an instance of`VisionTextRecognizer`by calling either`onDeviceTextRecognizer`or`cloudTextRecognizer`:  

   #### Swift

   To use the on-device model:  

   ```swift
   let vision = Vision.vision()
   let textRecognizer = vision.onDeviceTextRecognizer()
   ```

   To use the cloud model:
   Use of ML Kit to access Cloud ML functionality is subject to the[Google Cloud Platform License Agreement](https://cloud.google.com/terms/)and[Service Specific Terms](https://cloud.google.com/terms/service-terms), and billed accordingly. For billing information, see the Firebase[Pricing](https://firebase.google.com/pricing)page.  

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

   To use the on-device model:  

   ```objective-c
   FIRVision *vision = [FIRVision vision];
   FIRVisionTextRecognizer *textRecognizer = [vision onDeviceTextRecognizer];
   ```

   To use the cloud model:
   Use of ML Kit to access Cloud ML functionality is subject to the[Google Cloud Platform License Agreement](https://cloud.google.com/terms/)and[Service Specific Terms](https://cloud.google.com/terms/service-terms), and billed accordingly. For billing information, see the Firebase[Pricing](https://firebase.google.com/pricing)page.  

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
2. Create a[`VisionImage`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionImage)object using a`UIImage`or a`CMSampleBufferRef`.

   To use a`UIImage`:
   1. If necessary, rotate the image so that its`imageOrientation`property is`.up`.
   2. Create a`VisionImage`object using the correctly-rotated`UIImage`. Do not specify any rotation metadata---the default value,`.topLeft`, must be used.  

      #### Swift

      ```swift
      let image = VisionImage(image: uiImage)
      ```

      #### Objective-C

      ```objective-c
      FIRVisionImage *image = [[FIRVisionImage alloc] initWithImage:uiImage];
      ```

   To use a`CMSampleBufferRef`:
   1. Create a[`VisionImageMetadata`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionImageMetadata)object that specifies the orientation of the image data contained in the`CMSampleBufferRef`buffer.

      To get the image orientation:  

      #### Swift

      ```swift
      func imageOrientation(
          deviceOrientation: UIDeviceOrientation,
          cameraPosition: AVCaptureDevice.Position
          ) -> VisionDetectorImageOrientation {
          switch deviceOrientation {
          case .portrait:
              return cameraPosition == .front ? .leftTop : .rightTop
          case .landscapeLeft:
              return cameraPosition == .front ? .bottomLeft : .topLeft
          case .portraitUpsideDown:
              return cameraPosition == .front ? .rightBottom : .leftBottom
          case .landscapeRight:
              return cameraPosition == .front ? .topRight : .bottomRight
          case .faceDown, .faceUp, .unknown:
              return .leftTop
          }
      }
      ```

      #### Objective-C

      ```objective-c
      - (FIRVisionDetectorImageOrientation)
          imageOrientationFromDeviceOrientation:(UIDeviceOrientation)deviceOrientation
                                 cameraPosition:(AVCaptureDevicePosition)cameraPosition {
        switch (deviceOrientation) {
          case UIDeviceOrientationPortrait:
            if (cameraPosition == AVCaptureDevicePositionFront) {
              return FIRVisionDetectorImageOrientationLeftTop;
            } else {
              return FIRVisionDetectorImageOrientationRightTop;
            }
          case UIDeviceOrientationLandscapeLeft:
            if (cameraPosition == AVCaptureDevicePositionFront) {
              return FIRVisionDetectorImageOrientationBottomLeft;
            } else {
              return FIRVisionDetectorImageOrientationTopLeft;
            }
          case UIDeviceOrientationPortraitUpsideDown:
            if (cameraPosition == AVCaptureDevicePositionFront) {
              return FIRVisionDetectorImageOrientationRightBottom;
            } else {
              return FIRVisionDetectorImageOrientationLeftBottom;
            }
          case UIDeviceOrientationLandscapeRight:
            if (cameraPosition == AVCaptureDevicePositionFront) {
              return FIRVisionDetectorImageOrientationTopRight;
            } else {
              return FIRVisionDetectorImageOrientationBottomRight;
            }
          default:
            return FIRVisionDetectorImageOrientationTopLeft;
        }
      }
      ```

      Then, create the metadata object:  

      #### Swift

      ```swift
      let cameraPosition = AVCaptureDevice.Position.back  // Set to the capture device you used.
      let metadata = VisionImageMetadata()
      metadata.orientation = imageOrientation(
          deviceOrientation: UIDevice.current.orientation,
          cameraPosition: cameraPosition
      )
      ```

      #### Objective-C

      ```objective-c
      FIRVisionImageMetadata *metadata = [[FIRVisionImageMetadata alloc] init];
      AVCaptureDevicePosition cameraPosition =
          AVCaptureDevicePositionBack;  // Set to the capture device you used.
      metadata.orientation =
          [self imageOrientationFromDeviceOrientation:UIDevice.currentDevice.orientation
                                       cameraPosition:cameraPosition];
      ```
   2. Create a`VisionImage`object using the`CMSampleBufferRef`object and the rotation metadata:  

      #### Swift

      ```swift
      let image = VisionImage(buffer: sampleBuffer)
      image.metadata = metadata
      ```

      #### Objective-C

      ```objective-c
      FIRVisionImage *image = [[FIRVisionImage alloc] initWithBuffer:sampleBuffer];
      image.metadata = metadata;
      ```
3. Then, pass the image to the`process(_:completion:)`method:  

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

If the text recognition operation succeeds, it will return a \[\`VisionText\`\]\[VisionText\] object. A \`VisionText\` object contains the full text recognized in the image and zero or more \[\`VisionTextBlock\`\]\[VisionTextBlock\] objects. Each \`VisionTextBlock\` represents a rectangular block of text, which contain zero or more \[\`VisionTextLine\`\]\[VisionTextLine\] objects. Each \`VisionTextLine\` object contains zero or more \[\`VisionTextElement\`\]\[VisionTextElement\] objects, which represent words and word-like entities (dates, numbers, and so on). For each \`VisionTextBlock\`, \`VisionTextLine\`, and \`VisionTextElement\` object, you can get the text recognized in the region and the bounding coordinates of the region. For example:  

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
| **Note:** Recognized languages are provided only when using the cloud model. To identify languages with the on-device model, use ML Kit's[language identification API](https://firebase.google.com/docs/ml-kit/ios/identify-languages).

### Tips to improve real-time performance

If you want use the on-device model to recognize text in a real-time application, follow these guidelines to achieve the best framerates:

- Throttle calls to the text recognizer. If a new video frame becomes available while the text recognizer is running, drop the frame.
- If you are using the output of the text recognizer to overlay graphics on the input image, first get the result from ML Kit, then render the image and overlay in a single step. By doing so, you render to the display surface only once for each input frame. See the[previewOverlayView](https://github.com/firebase/mlkit-material-ios/blob/81bd5a028eabcbdc6b1c9c248de70ff38f0ba84a/ShowcaseApp/ShowcaseApp/Controllers/FIRVideoCamViewController.m#L856)and[FIRDetectionOverlayView](https://github.com/firebase/mlkit-material-ios/blob/81bd5a028eabcbdc6b1c9c248de70ff38f0ba84a/ShowcaseApp/ShowcaseApp/Views/FIRDetectionOverlayView.m)classes in the showcase sample app for an example.
- Consider capturing images at a lower resolution. However, also keep in mind this API's image dimension requirements.

### Next steps

- Before you deploy to production an app that uses a Cloud API, you should take some additional steps to[prevent and mitigate the effect of unauthorized API access](https://firebase.google.com/docs/ml-kit/ios/secure-api-key).

*** ** * ** ***

## Recognize text in images of documents

To recognize the text of a document, configure and run the cloud-based document text recognizer as described below.
| Use of ML Kit to access Cloud ML functionality is subject to the[Google Cloud Platform License Agreement](https://cloud.google.com/terms/)and[Service Specific Terms](https://cloud.google.com/terms/service-terms), and billed accordingly. For billing information, see the Firebase[Pricing](https://firebase.google.com/pricing)page.

The document text recognition API, described below, provides an interface that is intended to be more convenient for working with images of documents. However, if you prefer the interface provided by the sparse text API, you can use it instead to scan documents by configuring the cloud text recognizer to[use the dense text model](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudTextRecognizerOptions#modeltype).

To use the document text recognition API:

### 1. Run the text recognizer

Pass the image as a`UIImage`or a`CMSampleBufferRef`to the`VisionDocumentTextRecognizer`'s`process(_:completion:)`method:

<br />

1. Get an instance of`VisionDocumentTextRecognizer`by calling`cloudDocumentTextRecognizer`:  

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
2. Create a[`VisionImage`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionImage)object using a`UIImage`or a`CMSampleBufferRef`.

   To use a`UIImage`:
   1. If necessary, rotate the image so that its`imageOrientation`property is`.up`.
   2. Create a`VisionImage`object using the correctly-rotated`UIImage`. Do not specify any rotation metadata---the default value,`.topLeft`, must be used.  

      #### Swift

      ```swift
      let image = VisionImage(image: uiImage)
      ```

      #### Objective-C

      ```objective-c
      FIRVisionImage *image = [[FIRVisionImage alloc] initWithImage:uiImage];
      ```

   To use a`CMSampleBufferRef`:
   1. Create a[`VisionImageMetadata`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionImageMetadata)object that specifies the orientation of the image data contained in the`CMSampleBufferRef`buffer.

      To get the image orientation:  

      #### Swift

      ```swift
      func imageOrientation(
          deviceOrientation: UIDeviceOrientation,
          cameraPosition: AVCaptureDevice.Position
          ) -> VisionDetectorImageOrientation {
          switch deviceOrientation {
          case .portrait:
              return cameraPosition == .front ? .leftTop : .rightTop
          case .landscapeLeft:
              return cameraPosition == .front ? .bottomLeft : .topLeft
          case .portraitUpsideDown:
              return cameraPosition == .front ? .rightBottom : .leftBottom
          case .landscapeRight:
              return cameraPosition == .front ? .topRight : .bottomRight
          case .faceDown, .faceUp, .unknown:
              return .leftTop
          }
      }
      ```

      #### Objective-C

      ```objective-c
      - (FIRVisionDetectorImageOrientation)
          imageOrientationFromDeviceOrientation:(UIDeviceOrientation)deviceOrientation
                                 cameraPosition:(AVCaptureDevicePosition)cameraPosition {
        switch (deviceOrientation) {
          case UIDeviceOrientationPortrait:
            if (cameraPosition == AVCaptureDevicePositionFront) {
              return FIRVisionDetectorImageOrientationLeftTop;
            } else {
              return FIRVisionDetectorImageOrientationRightTop;
            }
          case UIDeviceOrientationLandscapeLeft:
            if (cameraPosition == AVCaptureDevicePositionFront) {
              return FIRVisionDetectorImageOrientationBottomLeft;
            } else {
              return FIRVisionDetectorImageOrientationTopLeft;
            }
          case UIDeviceOrientationPortraitUpsideDown:
            if (cameraPosition == AVCaptureDevicePositionFront) {
              return FIRVisionDetectorImageOrientationRightBottom;
            } else {
              return FIRVisionDetectorImageOrientationLeftBottom;
            }
          case UIDeviceOrientationLandscapeRight:
            if (cameraPosition == AVCaptureDevicePositionFront) {
              return FIRVisionDetectorImageOrientationTopRight;
            } else {
              return FIRVisionDetectorImageOrientationBottomRight;
            }
          default:
            return FIRVisionDetectorImageOrientationTopLeft;
        }
      }
      ```

      Then, create the metadata object:  

      #### Swift

      ```swift
      let cameraPosition = AVCaptureDevice.Position.back  // Set to the capture device you used.
      let metadata = VisionImageMetadata()
      metadata.orientation = imageOrientation(
          deviceOrientation: UIDevice.current.orientation,
          cameraPosition: cameraPosition
      )
      ```

      #### Objective-C

      ```objective-c
      FIRVisionImageMetadata *metadata = [[FIRVisionImageMetadata alloc] init];
      AVCaptureDevicePosition cameraPosition =
          AVCaptureDevicePositionBack;  // Set to the capture device you used.
      metadata.orientation =
          [self imageOrientationFromDeviceOrientation:UIDevice.currentDevice.orientation
                                       cameraPosition:cameraPosition];
      ```
   2. Create a`VisionImage`object using the`CMSampleBufferRef`object and the rotation metadata:  

      #### Swift

      ```swift
      let image = VisionImage(buffer: sampleBuffer)
      image.metadata = metadata
      ```

      #### Objective-C

      ```objective-c
      FIRVisionImage *image = [[FIRVisionImage alloc] initWithBuffer:sampleBuffer];
      image.metadata = metadata;
      ```
3. Then, pass the image to the`process(_:completion:)`method:  

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

If the text recognition operation succeeds, it will return a[`VisionDocumentText`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentText)object. A`VisionDocumentText`object contains the full text recognized in the image and a hierarchy of objects that reflect the structure of the recognized document:

<br />

- [`VisionDocumentTextBlock`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextBlock)
- [`VisionDocumentTextParagraph`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextParagraph)
- [`VisionDocumentTextWord`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextWord)
- [`VisionDocumentTextSymbol`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextSymbol)

For each`VisionDocumentTextBlock`,`VisionDocumentTextParagraph`,`VisionDocumentTextWord`, and`VisionDocumentTextSymbol`object, you can get the text recognized in the region and the bounding coordinates of the region.

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

- Before you deploy to production an app that uses a Cloud API, you should take some additional steps to[prevent and mitigate the effect of unauthorized API access](https://firebase.google.com/docs/ml-kit/ios/secure-api-key).