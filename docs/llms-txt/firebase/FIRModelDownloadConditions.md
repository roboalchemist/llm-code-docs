# Source: https://firebase.google.com/docs/reference/ios/firebasemlcommon/api/reference/Classes/FIRModelDownloadConditions.md.txt

# FirebaseMLCommon Framework Reference

# FIRModelDownloadConditions


    @interface FIRModelDownloadConditions : NSObject <NSCopying>

Configurations for model downloading conditions.
- `
  ``
  ``
  `

  ### [allowsCellularAccess](https://firebase.google.com/docs/reference/ios/firebasemlcommon/api/reference/Classes/FIRModelDownloadConditions#/c:objc(cs)FIRModelDownloadConditions(py)allowsCellularAccess)

  `
  `  
  Indicates whether download requests should be made over a cellular network. The default is `YES`.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) BOOL allowsCellularAccess;

- `
  ``
  ``
  `

  ### [allowsBackgroundDownloading](https://firebase.google.com/docs/reference/ios/firebasemlcommon/api/reference/Classes/FIRModelDownloadConditions#/c:objc(cs)FIRModelDownloadConditions(py)allowsBackgroundDownloading)

  `
  `  
  Indicates whether the model can be downloaded while the app is in the background. The default is
  `NO`.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) BOOL allowsBackgroundDownloading;

- `
  ``
  ``
  `

  ### [-initWithAllowsCellularAccess:allowsBackgroundDownloading:](https://firebase.google.com/docs/reference/ios/firebasemlcommon/api/reference/Classes/FIRModelDownloadConditions#/c:objc(cs)FIRModelDownloadConditions(im)initWithAllowsCellularAccess:allowsBackgroundDownloading:)

  `
  `  
  Creates a new instance with the given conditions.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)initWithAllowsCellularAccess:(BOOL)allowsCellularAccess
                               allowsBackgroundDownloading:
                                   (BOOL)allowsBackgroundDownloading;

  #### Parameters

  |-------------------------------------|-------------------------------------------------------------------------|
  | ` `*allowsCellularAccess*` `        | Whether download requests should be made over a cellular network.       |
  | ` `*allowsBackgroundDownloading*` ` | Whether the model can be downloaded while the app is in the background. |

  #### Return Value

  A new `ModelDownloadConditions` instance.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlcommon/api/reference/Classes/FIRModelDownloadConditions#/c:objc(cs)FIRModelDownloadConditions(im)init)

  `
  `  
  Creates a new instance with the default conditions. The default values are specified in the
  documentation for each instance property.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;

  #### Return Value

  A new `ModelDownloadConditions` instance.