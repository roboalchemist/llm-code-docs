# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveServerGoingAwayNotice.md.txt

# FirebaseAILogic Framework Reference

# LiveServerGoingAwayNotice

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, *)
    @available(watchOS, unavailable)
    public struct LiveServerGoingAwayNotice : Sendable

Server will not be able to service client soon.

To learn more about session limits, see the docs on [Maximum session duration](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/multimodal-live#maximum-session-duration).
- `


  ### [timeLeft](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveServerGoingAwayNotice#/s:15FirebaseAILogic25LiveServerGoingAwayNoticeV8timeLeftSdSgvp)


  ` The remaining time before the connection will be terminated as ABORTED.

  The minimal time returned here is specified differently together with
  the rate limits for a given model.

  #### Declaration

  Swift

      public var timeLeft: TimeInterval? { get }