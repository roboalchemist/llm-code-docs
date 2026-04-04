# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline/Snapshot.md.txt

# FirebaseFirestore Framework Reference

# Snapshot

    public struct Snapshot : Sendable

A `Pipeline.Snapshot` contains the results of a pipeline execution.
- `


  ### [results](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline/Snapshot#/s:17FirebaseFirestore8PipelineV8SnapshotV7resultsSayAA0C6ResultVGvp)


  ` An array of all the results in the `Pipeline.Snapshot`.

  #### Declaration

  Swift

      public let results: [https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/PipelineResult.html]

- `


  ### [executionTime](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline/Snapshot#/s:17FirebaseFirestore8PipelineV8SnapshotV13executionTimeSo12FIRTimestampCvp)


  ` The time at which the pipeline producing this result was executed.

  #### Declaration

  Swift

      public let executionTime: Timestamp