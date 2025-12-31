# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeDetectorOptions.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionBarcodeDetectorOptions


    @interface FIRVisionBarcodeDetectorOptions : NSObject

Options for specifying a Barcode detector.
- `
  ``
  ``
  `

  ### [formats](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeDetectorOptions#/c:objc(cs)FIRVisionBarcodeDetectorOptions(py)formats)

  `
  `  
  The barcode formats detected in an image. Note that the detection time will increase for each
  additional format that is specified.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Enums/FIRVisionBarcodeFormat.html formats;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeDetectorOptions#/c:objc(cs)FIRVisionBarcodeDetectorOptions(im)init)

  `
  `  
  Initializes an instance that detects all supported barcode formats.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;

  #### Return Value

  A new instance of Firebase barcode detector options.
- `
  ``
  ``
  `

  ### [-initWithFormats:](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeDetectorOptions#/c:objc(cs)FIRVisionBarcodeDetectorOptions(im)initWithFormats:)

  `
  `  
  Initializes an instance with the given barcode formats to look for.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)initWithFormats:(https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Enums/FIRVisionBarcodeFormat.html)formats;

  #### Parameters

  |-----------------|-----------------------------------------------------------------|
  | ` `*formats*` ` | The barcode formats to initialize the barcode detector options. |

  #### Return Value

  A new instance of Firebase barcode detector options.