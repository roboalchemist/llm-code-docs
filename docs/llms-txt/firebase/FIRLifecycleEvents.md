# Source: https://firebase.google.com/docs/reference/ios/firebaseabtesting/api/reference/Classes/FIRLifecycleEvents.md.txt

# FirebaseABTesting Framework Reference

# FIRLifecycleEvents


    @interface FIRLifecycleEvents : NSObject

An Experiment Lifecycle Event Object that specifies the name of the experiment event to be
logged by Firebase Analytics.
- `
  ``
  ``
  `

  ### [setExperimentEventName](https://firebase.google.com/docs/reference/ios/firebaseabtesting/api/reference/Classes/FIRLifecycleEvents#/c:objc(cs)FIRLifecycleEvents(py)setExperimentEventName)

  `
  `  
  Event name for when an experiment is set. It defaults to `SetExperimentEventName` and can be
  overridden. If experiment payload has a valid string of this field, always use
  experiment payload.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy) NSString *_Nonnull setExperimentEventName;

- `
  ``
  ``
  `

  ### [activateExperimentEventName](https://firebase.google.com/docs/reference/ios/firebaseabtesting/api/reference/Classes/FIRLifecycleEvents#/c:objc(cs)FIRLifecycleEvents(py)activateExperimentEventName)

  `
  `  
  Event name for when an experiment is activated. It defaults to `ActivateExperimentEventName`
  and can be overridden. If experiment payload has a valid string of this field, always use
  experiment payload.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy) NSString *_Nonnull activateExperimentEventName;

- `
  ``
  ``
  `

  ### [clearExperimentEventName](https://firebase.google.com/docs/reference/ios/firebaseabtesting/api/reference/Classes/FIRLifecycleEvents#/c:objc(cs)FIRLifecycleEvents(py)clearExperimentEventName)

  `
  `  
  Event name for when an experiment is cleared. It is default to `ClearExperimentEventName` and
  can be overridden. If experiment payload has a valid string of this field, always use experiment
  payload.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy) NSString *_Nonnull clearExperimentEventName;

- `
  ``
  ``
  `

  ### [timeoutExperimentEventName](https://firebase.google.com/docs/reference/ios/firebaseabtesting/api/reference/Classes/FIRLifecycleEvents#/c:objc(cs)FIRLifecycleEvents(py)timeoutExperimentEventName)

  `
  `  
  Event name for when an experiment is timeout from being STANDBY. It is default to
  `TimeoutExperimentEventName` and can be overridden. If experiment payload has a valid string
  of this field, always use experiment payload.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy) NSString *_Nonnull timeoutExperimentEventName;

- `
  ``
  ``
  `

  ### [expireExperimentEventName](https://firebase.google.com/docs/reference/ios/firebaseabtesting/api/reference/Classes/FIRLifecycleEvents#/c:objc(cs)FIRLifecycleEvents(py)expireExperimentEventName)

  `
  `  
  Event name when an experiment is expired when it reaches the end of its TTL.
  It is default to `ExpireExperimentEventName` and can be overridden. If experiment payload has a
  valid string of this field, always use experiment payload.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy) NSString *_Nonnull expireExperimentEventName;