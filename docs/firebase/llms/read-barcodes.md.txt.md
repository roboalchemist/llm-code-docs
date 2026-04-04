# Source: https://firebase.google.com/docs/ml-kit/ios/read-barcodes.md.txt

> [!CAUTION]
> This page describes an old version of the Barcode Scanning API, which was part
> of ML Kit for Firebase. Development of this API has been moved to the
> standalone ML Kit SDK, which you can use with or without Firebase.
> [Learn more](https://developers.google.com/ml-kit/migration).
>
> See
> [Scan Barcodes with ML Kit on iOS](https://developers.google.com/ml-kit/vision/barcode-scanning/ios)
> for the latest documentation.


You can use ML Kit to recognize and decode barcodes.

<br />

Version 0.19.0 of `MLVisionBarcodeModel` introduces a new
barcode scanning model with significant improvements in both latency and
accuracy. In addition, with the newest API, you now can access the raw bytes
for non UTF-8 encoded barcode data.

Update your project's pods to use the new model.

## Before you begin

1. If you have not already added Firebase to your app, do so by following the steps in the [getting started guide](https://firebase.google.com/docs/ios/setup).
2. Include the ML Kit libraries in your Podfile:

   ```
   pod 'Firebase/MLVision'
   pod 'Firebase/MLVisionBarcodeModel'
   ```
   After you install or update your project's Pods, be sure to open your Xcode project using its `.xcworkspace`.
3. In your app, import Firebase:

   #### Swift

   ```swift
   import Firebase
   ```

   #### Objective-C

   ```objective-c
   @import Firebase;
   ```

## Input image guidelines

- For ML Kit to accurately read barcodes, input images must contain
  barcodes that are represented by sufficient pixel data.

  The specific pixel data requirements are dependent on both the type of
  barcode and the amount of data that is encoded in it (since most barcodes
  support a variable length payload). In general, the smallest meaningful
  unit of the barcode should be at least 2 pixels wide (and for
  2-dimensional codes, 2 pixels tall).

  For example, EAN-13 barcodes are made up of bars and spaces that are 1,
  2, 3, or 4 units wide, so an EAN-13 barcode image ideally has bars and
  spaces that are at least 2, 4, 6, and 8 pixels wide. Because an EAN-13
  barcode is 95 units wide in total, the barcode should be at least 190
  pixels wide.

  Denser formats, such as PDF417, need greater pixel dimensions for
  ML Kit to reliably read them. For example, a PDF417 code can have up to
  34 17-unit wide "words" in a single row, which would ideally be at least
  1156 pixels wide.
- Poor image focus can hurt scanning accuracy. If you aren't getting
  acceptable results, try asking the user to recapture the image.

- For typical applications, it is recommended to provide a higher
  resolution image (such as 1280x720 or 1920x1080), which makes barcodes
  detectable from a larger distance away from the camera.

  However, in applications where latency is critical, you can improve
  performance by capturing images at a lower resolution, but requiring that
  the barcode make up the majority of the input image. Also see
  [Tips to improve real-time performance](https://firebase.google.com/docs/ml-kit/ios/read-barcodes#performance_tips).

## 1. Configure the barcode detector

If you know which barcode formats you expect to read, you can improve the speed of the barcode detector by configuring it to only detect those formats.

<br />

For example, to detect only Aztec code and QR codes, build a
[`VisionBarcodeDetectorOptions`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeDetectorOptions) object as in the
following example:

#### Swift

```swift
let format = VisionBarcodeFormat.all
let barcodeOptions = VisionBarcodeDetectorOptions(formats: format)
```

The following formats are supported:

- Code128
- Code39
- Code93
- CodaBar
- EAN13
- EAN8
- ITF
- UPCA
- UPCE
- QRCode
- PDF417
- Aztec
- DataMatrix

#### Objective-C

```objective-c
FIRVisionBarcodeDetectorOptions *options =
    [[FIRVisionBarcodeDetectorOptions alloc]
     initWithFormats: FIRVisionBarcodeFormatQRCode | FIRVisionBarcodeFormatAztec];
```

The following formats are supported:

- Code 128 (`FIRVisionBarcodeFormatCode128`)
- Code 39 (`FIRVisionBarcodeFormatCode39`)
- Code 93 (`FIRVisionBarcodeFormatCode93`)
- Codabar (`FIRVisionBarcodeFormatCodaBar`)
- EAN-13 (`FIRVisionBarcodeFormatEAN13`)
- EAN-8 (`FIRVisionBarcodeFormatEAN8`)
- ITF (`FIRVisionBarcodeFormatITF`)
- UPC-A (`FIRVisionBarcodeFormatUPCA`)
- UPC-E (`FIRVisionBarcodeFormatUPCE`)
- QR Code (`FIRVisionBarcodeFormatQRCode`)
- PDF417 (`FIRVisionBarcodeFormatPDF417`)
- Aztec (`FIRVisionBarcodeFormatAztec`)
- Data Matrix (`FIRVisionBarcodeFormatDataMatrix`)

> [!NOTE]
> **Note:** For a Data Matrix code to be recognized, the code must intersect the center point of the input image. Consequently, only one Data Matrix code can be recognized in an image.

## 2. Run the barcode detector

To scan barcodes in an image, pass the image as a `UIImage` or a `CMSampleBufferRef` to the `VisionBarcodeDetector`'s `detect(in:)` method:

<br />

1. Get an instance of [`VisionBarcodeDetector`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeDetector):

   #### Swift

   ```swift
   lazy var vision = Vision.vision()

   let barcodeDetector = vision.barcodeDetector(options: barcodeOptions)
   ```

   #### Objective-C

   ```objective-c
   FIRVision *vision = [FIRVision vision];
   FIRVisionBarcodeDetector *barcodeDetector = [vision barcodeDetector];
   // Or, to change the default settings:
   // FIRVisionBarcodeDetector *barcodeDetector =
   //     [vision barcodeDetectorWithOptions:options];
   ```
2. Create a [`VisionImage`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionImage) object using a `UIImage` or a
   `CMSampleBufferRef`.

   To use a `UIImage`:
   1. If necessary, rotate the image so that its `imageOrientation` property is `.up`.
   2. Create a `VisionImage` object using the correctly-rotated `UIImage`. Do not specify any rotation metadata---the default value, `.topLeft`, must be used.

      #### Swift

      ```swift
      let image = VisionImage(image: uiImage)
      ```

      #### Objective-C

      ```objective-c
      FIRVisionImage *image = [[FIRVisionImage alloc] initWithImage:uiImage];
      ```

   To use a `CMSampleBufferRef`:
   1. Create a [`VisionImageMetadata`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionImageMetadata) object that specifies the
      orientation of the image data contained in the
      `CMSampleBufferRef` buffer.

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
   2. Create a `VisionImage` object using the `CMSampleBufferRef` object and the rotation metadata:

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
3. Then, pass the image to the `detect(in:)` method:

   #### Swift

   ```swift
   barcodeDetector.detect(in: visionImage) { features, error in
     guard error == nil, let features = features, !features.isEmpty else {
       // ...
       return
     }

     // ...
   }
   ```

   #### Objective-C

   ```objective-c
   [barcodeDetector detectInImage:image
                       completion:^(NSArray<FIRVisionBarcode *> *barcodes,
                                    NSError *error) {
     if (error != nil) {
       return;
     } else if (barcodes != nil) {
       // Recognized barcodes
       // ...
     }
   }];
   ```

## 3. Get information from barcodes

If the barcode recognition operation succeeds, the detector returns an array of [`VisionBarcode`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcode) objects. Each `VisionBarcode` object represents a barcode that was detected in the image. For each barcode, you can get its bounding coordinates in the input image, as well as the raw data encoded by the barcode. Also, if the barcode detector was able to determine the type of data encoded by the barcode, you can get an object containing parsed data.

<br />

For example:

#### Swift

```swift
for barcode in barcodes {
  let corners = barcode.cornerPoints

  let displayValue = barcode.displayValue
  let rawValue = barcode.rawValue

  let valueType = barcode.valueType
  switch valueType {
  case .wiFi:
    let ssid = barcode.wifi!.ssid
    let password = barcode.wifi!.password
    let encryptionType = barcode.wifi!.type
  case .URL:
    let title = barcode.url!.title
    let url = barcode.url!.url
  default:
    // See API reference for all supported value types
  }
}
```

#### Objective-C

```objective-c
 for (FIRVisionBarcode *barcode in barcodes) {
   NSArray *corners = barcode.cornerPoints;

   NSString *displayValue = barcode.displayValue;
   NSString *rawValue = barcode.rawValue;

   FIRVisionBarcodeValueType valueType = barcode.valueType;
   switch (valueType) {
     case FIRVisionBarcodeValueTypeWiFi:
       // ssid = barcode.wifi.ssid;
       // password = barcode.wifi.password;
       // encryptionType = barcode.wifi.type;
       break;
     case FIRVisionBarcodeValueTypeURL:
       // url = barcode.URL.url;
       // title = barcode.URL.title;
       break;
     // ...
     default:
       break;
   }
 }
```

## Tips to improve real-time performance

If you want to scan barcodes in a real-time application, follow these
guidelines to achieve the best framerates:

- Don't capture input at the camera's native resolution. On some devices,
  capturing input at the native resolution produces extremely large (10+
  megapixels) images, which results in very poor latency with no benefit to
  accuracy. Instead, only request the size from the camera that is required
  for barcode detection: usually no more than 2 megapixels.

  The named capture session presets---`AVCaptureSessionPresetDefault`,
  `AVCaptureSessionPresetLow`, `AVCaptureSessionPresetMedium`,
  and so on)---are not recommended, however, as they can map to
  unsuitable resolutions on some devices. Instead, use the specific presets
  such as `AVCaptureSessionPreset1280x720`.

  If scanning speed is important, you can further lower the image capture
  resolution. However, bear in mind the minimum barcode size requirements
  outlined above.
- Throttle calls to the detector. If a new video frame becomes available while the detector is running, drop the frame.
- If you are using the output of the detector to overlay graphics on the input image, first get the result from ML Kit, then render the image and overlay in a single step. By doing so, you render to the display surface only once for each input frame. See the [previewOverlayView](https://github.com/firebase/mlkit-material-ios/blob/81bd5a028eabcbdc6b1c9c248de70ff38f0ba84a/ShowcaseApp/ShowcaseApp/Controllers/FIRVideoCamViewController.m#L856) and [FIRDetectionOverlayView](https://github.com/firebase/mlkit-material-ios/blob/81bd5a028eabcbdc6b1c9c248de70ff38f0ba84a/ShowcaseApp/ShowcaseApp/Views/FIRDetectionOverlayView.m) classes in the showcase sample app for an example.