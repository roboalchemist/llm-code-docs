# Source: https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Structs/ModelDownloadConditions.md.txt

# FirebaseMLModelDownloader Framework Reference

# ModelDownloadConditions

    public struct ModelDownloadConditions

Model download conditions.
- `


  ### [init(allowsCellularAccess:)](https://firebase.google.com/docs/reference/swift/firebasemlmodeldownloader/api/reference/Structs/ModelDownloadConditions#/s:25FirebaseMLModelDownloader23ModelDownloadConditionsV20allowsCellularAccessACSb_tcfc)


  ` Conditions that need to be met to start a model file download.

  #### Declaration

  Swift

      public init(allowsCellularAccess: Bool = true)

  #### Parameters

  |---|---|
  | ` allowsCellularAccess ` | Allow model downloading on a cellular connection. Default is `true`. |