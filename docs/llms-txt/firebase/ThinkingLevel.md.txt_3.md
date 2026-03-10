# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ThinkingConfig/ThinkingLevel.md.txt

# FirebaseAILogic Framework Reference

# ThinkingLevel

    struct ThinkingLevel : EncodableProtoEnum, Equatable

A preset that balances the trade-off between reasoning quality and response speed for a
model's "thinking" process.
- `


  ### [minimal](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ThinkingConfig/ThinkingLevel#/s:15FirebaseAILogic14ThinkingConfigV0C5LevelV7minimalAEvpZ)


  ` Use this level when you want to minimize latency, allowing for minimal thought. This
  level is faster than `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ThinkingConfig/ThinkingLevel.html#/s:15FirebaseAILogic14ThinkingConfigV0C5LevelV3lowAEvpZ`.

  #### Declaration

  Swift

      public static let minimal: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ThinkingConfig.html.ThinkingLevel

- `


  ### [low](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ThinkingConfig/ThinkingLevel#/s:15FirebaseAILogic14ThinkingConfigV0C5LevelV3lowAEvpZ)


  ` This level is suitable for simpler queries or when speed is the priority. This level is
  faster than `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ThinkingConfig/ThinkingLevel.html#/s:15FirebaseAILogic14ThinkingConfigV0C5LevelV6mediumAEvpZ`.

  #### Declaration

  Swift

      public static let low: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ThinkingConfig.html.ThinkingLevel

- `


  ### [medium](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ThinkingConfig/ThinkingLevel#/s:15FirebaseAILogic14ThinkingConfigV0C5LevelV6mediumAEvpZ)


  ` Offers a balanced approach suitable for tasks of moderate complexity that benefit from
  reasoning but don't require deep, multi-step planning. It provides more reasoning
  capability than `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ThinkingConfig/ThinkingLevel.html#/s:15FirebaseAILogic14ThinkingConfigV0C5LevelV3lowAEvpZ` while maintaining lower latency than `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ThinkingConfig/ThinkingLevel.html#/s:15FirebaseAILogic14ThinkingConfigV0C5LevelV4highAEvpZ`.

  #### Declaration

  Swift

      public static let medium: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ThinkingConfig.html.ThinkingLevel

- `


  ### [high](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ThinkingConfig/ThinkingLevel#/s:15FirebaseAILogic14ThinkingConfigV0C5LevelV4highAEvpZ)


  ` Use this level for complex queries where quality is more important than speed. It allows the
  model to engage in deeper reasoning but increases latency.

  #### Declaration

  Swift

      public static let high: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ThinkingConfig.html.ThinkingLevel