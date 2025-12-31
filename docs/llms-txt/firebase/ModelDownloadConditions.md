# Source: https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Structs/ModelDownloadConditions.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasemlcommon/api/reference/Classes/ModelDownloadConditions.md.txt

# FirebaseMLCommon Framework Reference

# ModelDownloadConditions

    class ModelDownloadConditions : NSObject, NSCopying

Configurations for model downloading conditions.
- `
  ``
  ``
  `

  ### [allowsCellularAccess](https://firebase.google.com/docs/reference/swift/firebasemlcommon/api/reference/Classes/ModelDownloadConditions#/c:objc(cs)FIRModelDownloadConditions(py)allowsCellularAccess)

  `
  `  
  Indicates whether download requests should be made over a cellular network. The default is `YES`.  

  #### Declaration

  Swift  

      var allowsCellularAccess: Bool { get }

- `
  ``
  ``
  `

  ### [allowsBackgroundDownloading](https://firebase.google.com/docs/reference/swift/firebasemlcommon/api/reference/Classes/ModelDownloadConditions#/c:objc(cs)FIRModelDownloadConditions(py)allowsBackgroundDownloading)

  `
  `  
  Indicates whether the model can be downloaded while the app is in the background. The default is
  `NO`.  

  #### Declaration

  Swift  

      var allowsBackgroundDownloading: Bool { get }

- `
  ``
  ``
  `

  ### [init(allowsCellularAccess:allowsBackgroundDownloading:)](https://firebase.google.com/docs/reference/swift/firebasemlcommon/api/reference/Classes/ModelDownloadConditions#/c:objc(cs)FIRModelDownloadConditions(im)initWithAllowsCellularAccess:allowsBackgroundDownloading:)

  `
  `  
  Creates a new instance with the given conditions.  

  #### Declaration

  Swift  

      init(allowsCellularAccess: Bool, allowsBackgroundDownloading: Bool)

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

  ### [init()](https://firebase.google.com/docs/reference/swift/firebasemlcommon/api/reference/Classes/ModelDownloadConditions#/c:objc(cs)FIRModelDownloadConditions(im)init)

  `
  `  
  Creates a new instance with the default conditions. The default values are specified in the
  documentation for each instance property.  

  #### Declaration

  Swift  

      convenience init()

  #### Return Value

  A new `ModelDownloadConditions` instance.