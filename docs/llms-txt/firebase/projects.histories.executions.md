# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions.md.txt

# REST Resource: projects.histories.executions

- [Resource: Execution](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#Execution)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#Execution.SCHEMA_REPRESENTATION)
- [MatrixDimensionDefinition](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#MatrixDimensionDefinition)
- [Specification](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#Specification)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#Specification.SCHEMA_REPRESENTATION)
- [AndroidTest](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#AndroidTest)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#AndroidTest.SCHEMA_REPRESENTATION)
- [AndroidAppInfo](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#AndroidAppInfo)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#AndroidAppInfo.SCHEMA_REPRESENTATION)
- [AndroidInstrumentationTest](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#AndroidInstrumentationTest)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#AndroidInstrumentationTest.SCHEMA_REPRESENTATION)
- [AndroidRoboTest](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#AndroidRoboTest)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#AndroidRoboTest.SCHEMA_REPRESENTATION)
- [AndroidTestLoop](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#AndroidTestLoop)
- [IosTest](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#IosTest)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#IosTest.SCHEMA_REPRESENTATION)
- [IosAppInfo](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#IosAppInfo)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#IosAppInfo.SCHEMA_REPRESENTATION)
- [IosXcTest](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#IosXcTest)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#IosXcTest.SCHEMA_REPRESENTATION)
- [IosTestLoop](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#IosTestLoop)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#IosTestLoop.SCHEMA_REPRESENTATION)
- [IosRoboTest](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#IosRoboTest)
- [Methods](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#METHODS_SUMMARY)

## Resource: Execution

An Execution represents a collection of Steps. For instance, it could represent: - a mobile test executed across a range of device configurations - a jenkins job with a build step followed by a test step

The maximum size of an execution message is 1 MiB.

An Execution can be updated until its state is set to COMPLETE at which point it becomes immutable.

|                                                                                                                                                                                                                                                                                                                                                                                                                           JSON representation                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "executionId": string, "state": enum (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/State), "creationTime": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Timestamp) }, "completionTime": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Timestamp) }, "outcome": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Outcome) }, "dimensionDefinitions": [ { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#MatrixDimensionDefinition) } ], "specification": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#Specification) }, "testExecutionMatrixId": string } ``` |

|                                                                                                                                                                                                                                                                                                                                                    Fields                                                                                                                                                                                                                                                                                                                                                    ||
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `executionId`            | `string` A unique identifier within a History for this Execution. Returns INVALID_ARGUMENT if this field is set or overwritten by the caller. - In response always set - In create/update request: never set                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `state`                  | `enum (`[State](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/State)`)` The initial state is IN_PROGRESS. The only legal state transitions is from IN_PROGRESS to COMPLETE. A PRECONDITION_FAILED will be returned if an invalid transition is requested. The state can only be set to COMPLETE once. A FAILED_PRECONDITION will be returned if the state is set to COMPLETE multiple times. If the state is set to COMPLETE, all the in-progress steps within the execution will be set as COMPLETE. If the outcome of the step is not set, the outcome will be set to INCONCLUSIVE. - In response always set - In create/update request: optional |
| `creationTime`           | `object (`[Timestamp](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Timestamp)`)` The time when the Execution was created. This value will be set automatically when executions.create is called. - In response: always set - In create/update request: never set                                                                                                                                                                                                                                                                                                                                                                                   |
| `completionTime`         | `object (`[Timestamp](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Timestamp)`)` The time when the Execution status transitioned to COMPLETE. This value will be set automatically when state transitions to COMPLETE. - In response: set if the execution state is COMPLETE. - In create/update request: never set                                                                                                                                                                                                                                                                                                                                |
| `outcome`                | `object (`[Outcome](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Outcome)`)` Classify the result, for example into SUCCESS or FAILURE - In response: present if set by create/update request - In create/update request: optional                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `dimensionDefinitions[]` | `object (`[MatrixDimensionDefinition](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#MatrixDimensionDefinition)`)` The dimensions along which different steps in this execution may vary. This must remain fixed over the life of the execution. Returns INVALID_ARGUMENT if this field is set in an update request. Returns INVALID_ARGUMENT if the same name occurs in more than one dimension_definition. Returns INVALID_ARGUMENT if the size of the list is over 100. - In response: present if set by create - In create request: optional - In update request: never set                                        |
| `specification`          | `object (`[Specification](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#Specification)`)` Lightweight information about execution request. - In response: present if set by create - In create: optional - In update: optional                                                                                                                                                                                                                                                                                                                                                                                        |
| `testExecutionMatrixId`  | `string` TestExecution Matrix ID that the TestExecutionService uses. - In response: present if set by create - In create: optional - In update: never set                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## MatrixDimensionDefinition

This type has no fields.
One dimension of the matrix of different runs of a step.

## Specification

The details about how to run the execution.

|                                                                                                                                                                                                              JSON representation                                                                                                                                                                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { // Union field `specification` can be only one of the following: "androidTest": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#AndroidTest) }, "iosTest": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#IosTest) } // End of list of possible types for union field `specification`. } ``` |

|                                                                                                      Fields                                                                                                       ||
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Union field `specification`. `specification` can be only one of the following:                                                                                                                                    ||
| `androidTest` | `object (`[AndroidTest](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#AndroidTest)`)` An Android mobile test execution specification. |
| `iosTest`     | `object (`[IosTest](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#IosTest)`)` An iOS mobile test execution specification.             |

## AndroidTest

An Android mobile test specification.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                JSON representation                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "androidAppInfo": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#AndroidAppInfo) }, "testTimeout": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Duration) }, // Union field `test` can be only one of the following: "androidInstrumentationTest": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#AndroidInstrumentationTest) }, "androidRoboTest": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#AndroidRoboTest) }, "androidTestLoop": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#AndroidTestLoop) } // End of list of possible types for union field `test`. } ``` |

|                                                                                                                     Fields                                                                                                                      ||
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `androidAppInfo`             | `object (`[AndroidAppInfo](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#AndroidAppInfo)`)` Information about the application under test.            |
| `testTimeout`                | `object (`[Duration](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Duration)`)` Max time a test is allowed to run before it is automatically cancelled.                            |
| Union field `test`. `test` can be only one of the following:                                                                                                                                                                                    ||
| `androidInstrumentationTest` | `object (`[AndroidInstrumentationTest](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#AndroidInstrumentationTest)`)` An Android instrumentation test. |
| `androidRoboTest`            | `object (`[AndroidRoboTest](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#AndroidRoboTest)`)` An Android robo test.                                  |
| `androidTestLoop`            | `object (`[AndroidTestLoop](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#AndroidTestLoop)`)` An Android test loop.                                  |

## AndroidAppInfo

Android app information.

|                                       JSON representation                                       |
|-------------------------------------------------------------------------------------------------|
| ``` { "name": string, "packageName": string, "versionName": string, "versionCode": string } ``` |

|                                 Fields                                  ||
|---------------|----------------------------------------------------------|
| `name`        | `string` The name of the app. Optional                   |
| `packageName` | `string` The package name of the app. Required.          |
| `versionName` | `string` The version name of the app. Optional.          |
| `versionCode` | `string` The internal version code of the app. Optional. |

## AndroidInstrumentationTest

A test of an Android application that can control an Android component independently of its normal lifecycle.

See <https://developer.android.com/training/testing/fundamentals> for more information on types of Android tests.

|                                                  JSON representation                                                  |
|-----------------------------------------------------------------------------------------------------------------------|
| ``` { "testPackageId": string, "testRunnerClass": string, "testTargets": [ string ], "useOrchestrator": boolean } ``` |

|                                                                                                                                       Fields                                                                                                                                        ||
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `testPackageId`   | `string` The java package for the test to be executed. Required                                                                                                                                                                                                  |
| `testRunnerClass` | `string` The InstrumentationTestRunner class. Required                                                                                                                                                                                                           |
| `testTargets[]`   | `string` Each target must be fully qualified with the package name or class name, in one of these formats: - "package packageName" - "class packageName.class_name" - "class packageName.class_name#methodName" If empty, all targets in the module will be run. |
| `useOrchestrator` | `boolean` The flag indicates whether Android Test Orchestrator will be used to run test or not.                                                                                                                                                                  |

## AndroidRoboTest

A test of an android application that explores the application on a virtual or physical Android device, finding culprits and crashes as it goes.

|                                                               JSON representation                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "appInitialActivity": string, "bootstrapPackageId": string, "bootstrapRunnerClass": string, "maxDepth": integer, "maxSteps": integer } ``` |

|                                                        Fields                                                         ||
|------------------------|-----------------------------------------------------------------------------------------------|
| `appInitialActivity`   | `string` The initial activity that should be used to start the app. Optional                  |
| `bootstrapPackageId`   | `string` The java package for the bootstrap. Optional                                         |
| `bootstrapRunnerClass` | `string` The runner class for the bootstrap. Optional                                         |
| `maxDepth`             | `integer` The max depth of the traversal stack Robo can explore. Optional                     |
| `maxSteps`             | `integer` The max number of steps/actions Robo can execute. Default is no limit (0). Optional |

## AndroidTestLoop

This type has no fields.
Test Loops are tests that can be launched by the app itself, determining when to run by listening for an intent.

## IosTest

A iOS mobile test specification

|                                                                                                                                                                                                                                                                                                                                                                                                                   JSON representation                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "iosAppInfo": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#IosAppInfo) }, "testTimeout": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Duration) }, // Union field `test` can be only one of the following: "iosXcTest": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#IosXcTest) }, "iosTestLoop": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#IosTestLoop) }, "iosRoboTest": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#IosRoboTest) } // End of list of possible types for union field `test`. } ``` |

|                                                                                                    Fields                                                                                                     ||
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `iosAppInfo`  | `object (`[IosAppInfo](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#IosAppInfo)`)` Information about the application under test. |
| `testTimeout` | `object (`[Duration](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Duration)`)` Max time a test is allowed to run before it is automatically cancelled.         |
| Union field `test`. `test` can be only one of the following:                                                                                                                                                  ||
| `iosXcTest`   | `object (`[IosXcTest](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#IosXcTest)`)` An iOS XCTest.                                  |
| `iosTestLoop` | `object (`[IosTestLoop](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#IosTestLoop)`)` An iOS test loop.                           |
| `iosRoboTest` | `object (`[IosRoboTest](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions#IosRoboTest)`)` An iOS Robo test.                           |

## IosAppInfo

iOS app information

|    JSON representation     |
|----------------------------|
| ``` { "name": string } ``` |

|                     Fields                     ||
|--------|----------------------------------------|
| `name` | `string` The name of the app. Required |

## IosXcTest

A test of an iOS application that uses the XCTest framework.

|                  JSON representation                   |
|--------------------------------------------------------|
| ``` { "bundleId": string, "xcodeVersion": string } ``` |

|                               Fields                               ||
|----------------|----------------------------------------------------|
| `bundleId`     | `string` Bundle ID of the app.                     |
| `xcodeVersion` | `string` Xcode version that the test was run with. |

## IosTestLoop

A game loop test of an iOS application.

|      JSON representation       |
|--------------------------------|
| ``` { "bundleId": string } ``` |

|                   Fields                   ||
|------------|--------------------------------|
| `bundleId` | `string` Bundle ID of the app. |

## IosRoboTest

This type has no fields.
A Robo test for an iOS application.

|                                                                                            ## Methods                                                                                            ||
|---------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| ### [create](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions/create) | Creates an Execution.                                           |
| ### [get](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions/get)       | Gets an Execution.                                              |
| ### [list](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions/list)     | Lists Executions for a given History.                           |
| ### [patch](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/projects.histories.executions/patch)   | Updates an existing Execution with the supplied partial entity. |