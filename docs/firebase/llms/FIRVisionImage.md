# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionImage.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionImage


    @interface FIRVisionImage : NSObject

An image or image buffer used in vision detection, with optional metadata.
- `
  ``
  ``
  `

  ### [metadata](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionImage#/c:objc(cs)FIRVisionImage(py)metadata)

  `
  `  
  Metadata about the image (e.g. image orientation). If metadata is not specified, the default
  metadata values are used.  

  #### Declaration

  Objective-C  

      @property (nonatomic, nullable) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionImageMetadata.html *metadata;

- `
  ``
  ``
  `

  ### [-initWithImage:](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionImage#/c:objc(cs)FIRVisionImage(im)initWithImage:)

  `
  `  
  Initializes a `VisionImage` object with the given image.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)initWithImage:(nonnull UIImage *)image;

  #### Parameters

  |---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*image*` ` | Image to use in vision detection. The given image should be rotated, so its `imageOrientation` property is set to `UIImageOrientationUp` value. The `UIImage` must have non-NULL `CGImage` property. |

  #### Return Value

  A `VisionImage` instance with the given image.
- `
  ``
  ``
  `

  ### [-initWithBuffer:](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionImage#/c:objc(cs)FIRVisionImage(im)initWithBuffer:)

  `
  `  
  Initializes a `VisionImage` object with the given image buffer. To improve performance, it is
  recommended to minimize the lifespan and number of instances of this class when initializing with
  a `CMSampleBufferRef`.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)initWithBuffer:(nonnull CMSampleBufferRef)sampleBuffer;

  #### Parameters

  |----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*sampleBuffer*` ` | Image buffer to use in vision detection. The buffer must be based on a pixel buffer (not compressed data), and the pixel format must be one of: - `kCVPixelFormatType_32BGRA` - `kCVPixelFormatType_420YpCbCr8BiPlanarFullRange` - `kCVPixelFormatType_420YpCbCr8BiPlanarVideoRange` In practice: this works with the video output of the phone's camera, but not other arbitrary sources of `CMSampleBufferRef`s. |

  #### Return Value

  A `VisionImage` instance with the given image buffer.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionImage#/c:objc(cs)FIRVisionImage(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;