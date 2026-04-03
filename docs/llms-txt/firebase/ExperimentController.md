# Source: https://firebase.google.com/docs/reference/swift/firebaseabtesting/api/reference/Classes/ExperimentController.md.txt

# FirebaseABTesting Framework Reference

# ExperimentController

    class ExperimentController : NSObject

This class is for Firebase services to handle experiments updates to Firebase Analytics.
Experiments can be set, cleared and updated through this controller.
- `
  ``
  ``
  `

  ### [sharedInstance()](https://firebase.google.com/docs/reference/swift/firebaseabtesting/api/reference/Classes/ExperimentController#/c:objc(cs)FIRExperimentController(cm)sharedInstance)

  `
  `  
  Returns the FIRExperimentController singleton.  

  #### Declaration

  Swift  

      class func sharedInstance() -> ExperimentController

- `
  ``
  ``
  `

  ### [-updateExperimentsWithServiceOrigin:events:policy:lastStartTime:payloads:completionHandler:](https://firebase.google.com/docs/reference/swift/firebaseabtesting/api/reference/Classes/ExperimentController#/c:objc(cs)FIRExperimentController(im)updateExperimentsWithServiceOrigin:events:policy:lastStartTime:payloads:completionHandler:)

  `
  `  
  Updates the list of experiments with an optional completion handler. Experiments already
  existing in payloads are not affected, whose state and payload is preserved. This method
  compares whether the experiments have changed or not by their variant ID. This runs in a
  background queue and calls the completion handler when finished executing.  

  #### Parameters

  |---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*origin*` `            | The originating service affected by the experiment.                                                                                                            |
  | ` `*events*` `            | A list of event names to be used for logging experiment lifecycle events, if they are not defined in the payload.                                              |
  | ` `*policy*` `            | The policy to handle new experiments when slots are full.                                                                                                      |
  | ` `*lastStartTime*` `     | The last known experiment start timestamp for this affected service. (Timestamps are specified by the number of seconds from 00:00:00 UTC on 1 January 1970.). |
  | ` `*payloads*` `          | List of experiment metadata.                                                                                                                                   |
  | ` `*completionHandler*` ` | Code to be executed after experiments are updated in the background thread.                                                                                    |

- `
  ``
  ``
  `

  ### [latestExperimentStartTimestampBetweenTimestamp(_:andPayloads:)](https://firebase.google.com/docs/reference/swift/firebaseabtesting/api/reference/Classes/ExperimentController#/c:objc(cs)FIRExperimentController(im)latestExperimentStartTimestampBetweenTimestamp:andPayloads:)

  `
  `  
  Returns the latest experiment start timestamp given a current latest timestamp and a list of
  experiment payloads. Timestamps are specified by the number of seconds from 00:00:00 UTC on 1
  January 1970.  

  #### Declaration

  Swift  

      func latestExperimentStartTimestampBetweenTimestamp(_ timestamp: TimeInterval, andPayloads payloads: [Data]) -> TimeInterval

  #### Parameters

  |-------------------|----------------------------------------------------------------------------------------------|
  | ` `*timestamp*` ` | Current latest experiment start timestamp. If not known, affected service should specify -1; |
  | ` `*payloads*` `  | List of experiment metadata.                                                                 |

- `
  ``
  ``
  `

  ### [validateRunningExperiments(forServiceOrigin:running:)](https://firebase.google.com/docs/reference/swift/firebaseabtesting/api/reference/Classes/ExperimentController#/c:objc(cs)FIRExperimentController(im)validateRunningExperimentsForServiceOrigin:runningExperimentPayloads:)

  `
  `  
  Expires experiments that aren't in the list of running experiment payloads.  

  #### Declaration

  Swift  

      func validateRunningExperiments(forServiceOrigin origin: String, running payloads: [ABTExperimentPayload])

  #### Parameters

  |------------------|-----------------------------------------------------|
  | ` `*origin*` `   | The originating service affected by the experiment. |
  | ` `*payloads*` ` | The list of valid, running experiments.             |

- `
  ``
  ``
  `

  ### [activateExperiment(_:forServiceOrigin:)](https://firebase.google.com/docs/reference/swift/firebaseabtesting/api/reference/Classes/ExperimentController#/c:objc(cs)FIRExperimentController(im)activateExperiment:forServiceOrigin:)

  `
  `  
  Directly sets a given experiment to be active.  

  #### Declaration

  Swift  

      func activateExperiment(_ experimentPayload: ABTExperimentPayload, forServiceOrigin origin: String)

  #### Parameters

  |---------------------------|----------------------------------------------------------|
  | ` `*experimentPayload*` ` | The payload for the experiment that should be activated. |
  | ` `*origin*` `            | The originating service affected by the experiment.      |