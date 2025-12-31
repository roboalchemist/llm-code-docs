# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/modeldownloader/CustomModel.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ml/modeldownloader/CustomModel.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Structs/CustomModel.md.txt

# FirebaseMLModelDownloader Framework Reference

# CustomModel

    public struct CustomModel : Hashable

A custom model that is stored remotely on the server and downloaded to the device.
- `
  ``
  ``
  `

  ### [name](https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Structs/CustomModel#/s:25FirebaseMLModelDownloader11CustomModelV4nameSSvp)

  `
  `  
  Name of the model.  

  #### Declaration

  Swift  

      public let name: String

- `
  ``
  ``
  `

  ### [size](https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Structs/CustomModel#/s:25FirebaseMLModelDownloader11CustomModelV4sizeSivp)

  `
  `  
  Size of the custom model, provided by the server.  

  #### Declaration

  Swift  

      public let size: Int

- `
  ``
  ``
  `

  ### [path](https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Structs/CustomModel#/s:25FirebaseMLModelDownloader11CustomModelV4pathSSvp)

  `
  `  
  Path where the model is stored on device.  

  #### Declaration

  Swift  

      public let path: String

- `
  ``
  ``
  `

  ### [hash](https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Structs/CustomModel#/s:25FirebaseMLModelDownloader11CustomModelV4hashSSvp)

  `
  `  
  Hash for the model, used for model verification.  

  #### Declaration

  Swift  

      public let hash: String