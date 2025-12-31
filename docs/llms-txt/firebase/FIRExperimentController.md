# Source: https://firebase.google.com/docs/reference/ios/firebaseabtesting/api/reference/Classes/FIRExperimentController.md.txt

# FirebaseABTesting Framework Reference

# FIRExperimentController


    @interface FIRExperimentController : NSObject

This class is for Firebase services to handle experiments updates to Firebase Analytics.
Experiments can be set, cleared and updated through this controller.
- `
  ``
  ``
  `

  ### [+sharedInstance](https://firebase.google.com/docs/reference/ios/firebaseabtesting/api/reference/Classes/FIRExperimentController#/c:objc(cs)FIRExperimentController(cm)sharedInstance)

  `
  `  
  Returns the FIRExperimentController singleton.  

  #### Declaration

  Objective-C  

      + (nonnull FIRExperimentController *)sharedInstance;

- `
  ``
  ``
  `

  ### [-updateExperimentsWithServiceOrigin:events:policy:lastStartTime:payloads:completionHandler:](https://firebase.google.com/docs/reference/ios/firebaseabtesting/api/reference/Classes/FIRExperimentController#/c:objc(cs)FIRExperimentController(im)updateExperimentsWithServiceOrigin:events:policy:lastStartTime:payloads:completionHandler:)

  `
  `  
  Updates the list of experiments with an optional completion handler. Experiments already
  existing in payloads are not affected, whose state and payload is preserved. This method
  compares whether the experiments have changed or not by their variant ID. This runs in a
  background queue and calls the completion handler when finished executing.  

  #### Declaration

  Objective-C  

      - (void)
          updateExperimentsWithServiceOrigin:(nonnull NSString *)origin
                                      events:(nonnull https://firebase.google.com/docs/reference/ios/firebaseabtesting/api/reference/Classes/FIRLifecycleEvents.html *)events
                                      policy:
                                          (https://firebase.google.com/docs/reference/ios/firebaseabtesting/api/reference/Enums.html#/c:@E@ABTExperimentPayloadExperimentOverflowPolicy)
                                              policy
                               lastStartTime:(NSTimeInterval)lastStartTime
                                    payloads:(nonnull NSArray<NSData *> *)payloads
                           completionHandler:(nullable void (^)(NSError *_Nullable))
                                                 completionHandler;

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

  ### [-latestExperimentStartTimestampBetweenTimestamp:andPayloads:](https://firebase.google.com/docs/reference/ios/firebaseabtesting/api/reference/Classes/FIRExperimentController#/c:objc(cs)FIRExperimentController(im)latestExperimentStartTimestampBetweenTimestamp:andPayloads:)

  `
  `  
  Returns the latest experiment start timestamp given a current latest timestamp and a list of
  experiment payloads. Timestamps are specified by the number of seconds from 00:00:00 UTC on 1
  January 1970.  

  #### Declaration

  Objective-C  

      - (NSTimeInterval)
          latestExperimentStartTimestampBetweenTimestamp:(NSTimeInterval)timestamp
                                             andPayloads:(nonnull NSArray<NSData *> *)
                                                             payloads;

  #### Parameters

  |-------------------|----------------------------------------------------------------------------------------------|
  | ` `*timestamp*` ` | Current latest experiment start timestamp. If not known, affected service should specify -1; |
  | ` `*payloads*` `  | List of experiment metadata.                                                                 |

- `
  ``
  ``
  `

  ### [-validateRunningExperimentsForServiceOrigin:runningExperimentPayloads:](https://firebase.google.com/docs/reference/ios/firebaseabtesting/api/reference/Classes/FIRExperimentController#/c:objc(cs)FIRExperimentController(im)validateRunningExperimentsForServiceOrigin:runningExperimentPayloads:)

  `
  `  
  Expires experiments that aren't in the list of running experiment payloads.  

  #### Declaration

  Objective-C  

      - (void)validateRunningExperimentsForServiceOrigin:(nonnull NSString *)origin
                               runningExperimentPayloads:
                                   (nonnull NSArray<ABTExperimentPayload *> *)
                                       payloads;

  #### Parameters

  |------------------|-----------------------------------------------------|
  | ` `*origin*` `   | The originating service affected by the experiment. |
  | ` `*payloads*` ` | The list of valid, running experiments.             |

- `
  ``
  ``
  `

  ### [-activateExperiment:forServiceOrigin:](https://firebase.google.com/docs/reference/ios/firebaseabtesting/api/reference/Classes/FIRExperimentController#/c:objc(cs)FIRExperimentController(im)activateExperiment:forServiceOrigin:)

  `
  `  
  Directly sets a given experiment to be active.  

  #### Declaration

  Objective-C  

      - (void)activateExperiment:(nonnull ABTExperimentPayload *)experimentPayload
                forServiceOrigin:(nonnull NSString *)origin;

  #### Parameters

  |---------------------------|----------------------------------------------------------|
  | ` `*experimentPayload*` ` | The payload for the experiment that should be activated. |
  | ` `*origin*` `            | The originating service affected by the experiment.      |