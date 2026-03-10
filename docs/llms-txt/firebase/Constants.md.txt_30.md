# Source: https://firebase.google.com/docs/reference/swift/firebaseabtesting/api/reference/Constants.md.txt

# FirebaseABTesting Framework Reference

# Constants

The following constants are available globally.
- `


  ### [FIRDefaultExperimentOverflowPolicy](https://firebase.google.com/docs/reference/swift/firebaseabtesting/api/reference/Constants#/c:@FIRDefaultExperimentOverflowPolicy)


  ` The default experiment overflow policy, that is to discard the experiment with the oldest start
  time when users start the experiment on the web console.

  #### Declaration

  Swift

      let FIRDefaultExperimentOverflowPolicy: <<error type>>

- `


  ### [DefaultSetExperimentEventName](https://firebase.google.com/docs/reference/swift/firebaseabtesting/api/reference/Constants#/c:@FIRSetExperimentEventName)


  ` Default event name for when an experiment is set.

  #### Declaration

  Swift

      let DefaultSetExperimentEventName: String

- `


  ### [DefaultActivateExperimentEventName](https://firebase.google.com/docs/reference/swift/firebaseabtesting/api/reference/Constants#/c:@FIRActivateExperimentEventName)


  ` Default event name for when an experiment is activated.

  #### Declaration

  Swift

      let DefaultActivateExperimentEventName: String

- `


  ### [DefaultClearExperimentEventName](https://firebase.google.com/docs/reference/swift/firebaseabtesting/api/reference/Constants#/c:@FIRClearExperimentEventName)


  ` Default event name for when an experiment is cleared.

  #### Declaration

  Swift

      let DefaultClearExperimentEventName: String

- `


  ### [DefaultTimeoutExperimentEventName](https://firebase.google.com/docs/reference/swift/firebaseabtesting/api/reference/Constants#/c:@FIRTimeoutExperimentEventName)


  ` Default event name for when an experiment times out for being activated.

  #### Declaration

  Swift

      let DefaultTimeoutExperimentEventName: String

- `


  ### [DefaultExpireExperimentEventName](https://firebase.google.com/docs/reference/swift/firebaseabtesting/api/reference/Constants#/c:@FIRExpireExperimentEventName)


  ` Default event name for when an experiment is expired as it reaches the end of TTL.

  #### Declaration

  Swift

      let DefaultExpireExperimentEventName: String