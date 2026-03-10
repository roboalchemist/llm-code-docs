# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ThinkingConfig.md.txt

# FirebaseAILogic Framework Reference

# ThinkingConfig

    public struct ThinkingConfig : Sendable

    extension ThinkingConfig: Encodable

Configuration for controlling the "thinking" behavior of compatible Gemini models.

Gemini 2.5 series models and newer utilize a thinking process before generating a response. This
allows them to reason through complex problems and plan a more coherent and accurate answer.
See the [thinking documentation](https://firebase.google.com/docs/ai-logic/thinking) for more
details.
- `


  ### [init(thinkingBudget:includeThoughts:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ThinkingConfig#/s:15FirebaseAILogic14ThinkingConfigV14thinkingBudget15includeThoughtsACSiSg_SbSgtcfc)


  ` Initializes a new `ThinkingConfig`.

  #### Declaration

  Swift

      public init(thinkingBudget: Int? = nil, includeThoughts: Bool? = nil)

  #### Parameters

  |---|---|
  | ` thinkingBudget ` | The maximum number of tokens to be used for the model's thinking process. The range of [supported thinking budget values](https://firebase.google.com/docs/ai-logic/thinking#supported-thinking-budget-values) depends on the model. - To use the default thinking budget or thinking level for a model, set this value to `nil` or omit it. - To disable thinking, when supported by the model, set this value to `0`. - To use dynamic thinking, allowing the model to decide on the thinking budget based on the task, set this value to `-1`. <br /> |
  | ` includeThoughts ` | If true, summaries of the model's "thoughts" are included in responses. |

- `


  ### [init(thinkingLevel:includeThoughts:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ThinkingConfig#/s:15FirebaseAILogic14ThinkingConfigV13thinkingLevel15includeThoughtsA2C0cF0V_SbSgtcfc)


  ` Initializes a `ThinkingConfig` with a `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ThinkingConfig/ThinkingLevel.html`.

  If you don't specify a thinking level, Gemini will use the model's default dynamic thinking
  level.
  Important

  Gemini 2.5 series models do not support thinking levels; use
  `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ThinkingConfig.html#/s:15FirebaseAILogic14ThinkingConfigV14thinkingBudget15includeThoughtsACSiSg_SbSgtcfc` to set a thinking budget instead.

  #### Declaration

  Swift

      public init(thinkingLevel: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ThinkingConfig/ThinkingLevel.html, includeThoughts: Bool? = nil)

  #### Parameters

  |---|---|
  | ` thinkingLevel ` | A preset that controls the model's "thinking" process. Use `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ThinkingConfig/ThinkingLevel.html#/s:15FirebaseAILogic14ThinkingConfigV0C5LevelV3lowAEvpZ` for faster responses on less complex tasks, and `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ThinkingConfig/ThinkingLevel.html#/s:15FirebaseAILogic14ThinkingConfigV0C5LevelV4highAEvpZ` for better reasoning on more complex tasks. |
  | ` includeThoughts ` | If true, summaries of the model's "thoughts" are included in responses. |

- `


  ### [ThinkingLevel](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ThinkingConfig/ThinkingLevel.html)


  ` A preset that balances the trade-off between reasoning quality and response speed for a
  model's "thinking" process.

  #### Declaration

  Swift

      struct ThinkingLevel : EncodableProtoEnum, Equatable