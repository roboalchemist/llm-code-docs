# Source: https://firebase.google.com/docs/reference/swift/firebaseabtesting/api/reference/Classes/LifecycleEvents.md.txt

# FirebaseABTesting Framework Reference

# LifecycleEvents

    class LifecycleEvents : NSObject

An Experiment Lifecycle Event Object that specifies the name of the experiment event to be
logged by Firebase Analytics.
- `
  ``
  ``
  `

  ### [setExperimentEventName](https://firebase.google.com/docs/reference/swift/firebaseabtesting/api/reference/Classes/LifecycleEvents#/c:objc(cs)FIRLifecycleEvents(py)setExperimentEventName)

  `
  `  
  Event name for when an experiment is set. It defaults to `SetExperimentEventName` and can be
  overridden. If experiment payload has a valid string of this field, always use
  experiment payload.  

  #### Declaration

  Swift  

      var setExperimentEventName: String { get set }

- `
  ``
  ``
  `

  ### [activateExperimentEventName](https://firebase.google.com/docs/reference/swift/firebaseabtesting/api/reference/Classes/LifecycleEvents#/c:objc(cs)FIRLifecycleEvents(py)activateExperimentEventName)

  `
  `  
  Event name for when an experiment is activated. It defaults to `ActivateExperimentEventName`
  and can be overridden. If experiment payload has a valid string of this field, always use
  experiment payload.  

  #### Declaration

  Swift  

      var activateExperimentEventName: String { get set }

- `
  ``
  ``
  `

  ### [clearExperimentEventName](https://firebase.google.com/docs/reference/swift/firebaseabtesting/api/reference/Classes/LifecycleEvents#/c:objc(cs)FIRLifecycleEvents(py)clearExperimentEventName)

  `
  `  
  Event name for when an experiment is cleared. It is default to `ClearExperimentEventName` and
  can be overridden. If experiment payload has a valid string of this field, always use experiment
  payload.  

  #### Declaration

  Swift  

      var clearExperimentEventName: String { get set }

- `
  ``
  ``
  `

  ### [timeoutExperimentEventName](https://firebase.google.com/docs/reference/swift/firebaseabtesting/api/reference/Classes/LifecycleEvents#/c:objc(cs)FIRLifecycleEvents(py)timeoutExperimentEventName)

  `
  `  
  Event name for when an experiment is timeout from being STANDBY. It is default to
  `TimeoutExperimentEventName` and can be overridden. If experiment payload has a valid string
  of this field, always use experiment payload.  

  #### Declaration

  Swift  

      var timeoutExperimentEventName: String { get set }

- `
  ``
  ``
  `

  ### [expireExperimentEventName](https://firebase.google.com/docs/reference/swift/firebaseabtesting/api/reference/Classes/LifecycleEvents#/c:objc(cs)FIRLifecycleEvents(py)expireExperimentEventName)

  `
  `  
  Event name when an experiment is expired when it reaches the end of its TTL.
  It is default to `ExpireExperimentEventName` and can be overridden. If experiment payload has a
  valid string of this field, always use experiment payload.  

  #### Declaration

  Swift  

      var expireExperimentEventName: String { get set }