# Source: https://firebase.google.com/docs/reference/ios/firebaseabtesting/api/reference/Constants.md.txt

# FirebaseABTesting Framework Reference

# Constants

The following constants are available globally.
- `


  ### [FIRDefaultExperimentOverflowPolicy](https://firebase.google.com/docs/reference/ios/firebaseabtesting/api/reference/Constants#/c:@FIRDefaultExperimentOverflowPolicy)


  ` The default experiment overflow policy, that is to discard the experiment with the oldest start
  time when users start the experiment on the web console.

  #### Declaration

  Objective-C

      extern const https://firebase.google.com/docs/reference/ios/firebaseabtesting/api/reference/Enums#/c:@E@ABTExperimentPayloadExperimentOverflowPolicy
          FIRDefaultExperimentOverflowPolicy

- `


  ### [FIRSetExperimentEventName](https://firebase.google.com/docs/reference/ios/firebaseabtesting/api/reference/Constants#/c:@FIRSetExperimentEventName)


  ` Default event name for when an experiment is set.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(DefaultSetExperimentEventName) NSString *const
          FIRSetExperimentEventName

- `


  ### [FIRActivateExperimentEventName](https://firebase.google.com/docs/reference/ios/firebaseabtesting/api/reference/Constants#/c:@FIRActivateExperimentEventName)


  ` Default event name for when an experiment is activated.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(DefaultActivateExperimentEventName) NSString *const
          FIRActivateExperimentEventName

- `


  ### [FIRClearExperimentEventName](https://firebase.google.com/docs/reference/ios/firebaseabtesting/api/reference/Constants#/c:@FIRClearExperimentEventName)


  ` Default event name for when an experiment is cleared.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(DefaultClearExperimentEventName) NSString *const
          FIRClearExperimentEventName

- `


  ### [FIRTimeoutExperimentEventName](https://firebase.google.com/docs/reference/ios/firebaseabtesting/api/reference/Constants#/c:@FIRTimeoutExperimentEventName)


  ` Default event name for when an experiment times out for being activated.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(DefaultTimeoutExperimentEventName) NSString *const
          FIRTimeoutExperimentEventName

- `


  ### [FIRExpireExperimentEventName](https://firebase.google.com/docs/reference/ios/firebaseabtesting/api/reference/Constants#/c:@FIRExpireExperimentEventName)


  ` Default event name for when an experiment is expired as it reaches the end of TTL.

  #### Declaration

  Objective-C

      extern NS_SWIFT_NAME(DefaultExpireExperimentEventName) NSString *const
          FIRExpireExperimentEventName