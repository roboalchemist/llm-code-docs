# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Outcome.md.txt

# Outcome

- [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Outcome#SCHEMA_REPRESENTATION)
- [SuccessDetail](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Outcome#SuccessDetail)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Outcome#SuccessDetail.SCHEMA_REPRESENTATION)
- [FailureDetail](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Outcome#FailureDetail)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Outcome#FailureDetail.SCHEMA_REPRESENTATION)
- [InconclusiveDetail](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Outcome#InconclusiveDetail)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Outcome#InconclusiveDetail.SCHEMA_REPRESENTATION)
- [SkippedDetail](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Outcome#SkippedDetail)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Outcome#SkippedDetail.SCHEMA_REPRESENTATION)

Interprets a result so that humans and machines can act on it.

|                                                                                                                                                                                                                                                                                                                                                                                       JSON representation                                                                                                                                                                                                                                                                                                                                                                                        |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "summary": enum (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/OutcomeSummary), // Union field `detail` can be only one of the following: "successDetail": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Outcome#SuccessDetail) }, "failureDetail": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Outcome#FailureDetail) }, "inconclusiveDetail": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Outcome#InconclusiveDetail) }, "skippedDetail": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Outcome#SkippedDetail) } // End of list of possible types for union field `detail`. } ``` |

|                                                                                                                                                    Fields                                                                                                                                                    ||
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `summary`            | `enum (`[OutcomeSummary](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/OutcomeSummary)`)` The simplest way to interpret a result. Required                                                                                                              |
| Union field `detail`. Details for individual outcomes. LINT.IfChange `detail` can be only one of the following:                                                                                                                                                                                              ||
| `successDetail`      | `object (`[SuccessDetail](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Outcome#SuccessDetail)`)` More information about a SUCCESS outcome. Returns INVALID_ARGUMENT if this field is set but the summary is not SUCCESS. Optional                      |
| `failureDetail`      | `object (`[FailureDetail](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Outcome#FailureDetail)`)` More information about a FAILURE outcome. Returns INVALID_ARGUMENT if this field is set but the summary is not FAILURE. Optional                      |
| `inconclusiveDetail` | `object (`[InconclusiveDetail](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Outcome#InconclusiveDetail)`)` More information about an INCONCLUSIVE outcome. Returns INVALID_ARGUMENT if this field is set but the summary is not INCONCLUSIVE. Optional |
| `skippedDetail`      | `object (`[SkippedDetail](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Outcome#SkippedDetail)`)` More information about a SKIPPED outcome. Returns INVALID_ARGUMENT if this field is set but the summary is not SKIPPED. Optional                      |

## SuccessDetail

Details for an outcome with a SUCCESS outcome summary. LINT.IfChange

|           JSON representation           |
|-----------------------------------------|
| ``` { "otherNativeCrash": boolean } ``` |

|                                    Fields                                     ||
|--------------------|-----------------------------------------------------------|
| `otherNativeCrash` | `boolean` If a native process other than the app crashed. |

## FailureDetail

Details for an outcome with a FAILURE outcome summary.

|                                                                                      JSON representation                                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "crashed": boolean, "timedOut": boolean, "notInstalled": boolean, "otherNativeCrash": boolean, "unableToCrawl": boolean, "failedRoboscript": boolean, "deviceOutOfMemory": boolean } ``` |

|                                                                                                    Fields                                                                                                    ||
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `crashed`           | `boolean` If the failure was severe because the system (app) under test crashed.                                                                                                        |
| `timedOut`          | `boolean` If the test overran some time limit, and that is why it failed.                                                                                                               |
| `notInstalled`      | `boolean` If an app is not installed and thus no test can be run with the app. This might be caused by trying to run a test on an unsupported platform.                                 |
| `otherNativeCrash`  | `boolean` If a native process (including any other than the app) crashed.                                                                                                               |
| `unableToCrawl`     | `boolean` If the robo was unable to crawl the app; perhaps because the app did not start.                                                                                               |
| `failedRoboscript`  | `boolean` If the Roboscript failed to complete successfully, e.g., because a Roboscript action or assertion failed or a Roboscript action could not be matched during the entire crawl. |
| `deviceOutOfMemory` | `boolean` If the device ran out of memory during a test, causing the test to crash.                                                                                                     |

## InconclusiveDetail

Details for an outcome with an INCONCLUSIVE outcome summary.

|                                       JSON representation                                       |
|-------------------------------------------------------------------------------------------------|
| ``` { "infrastructureFailure": boolean, "abortedByUser": boolean, "hasErrorLogs": boolean } ``` |

|                                                                                                                                                 Fields                                                                                                                                                 ||
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `infrastructureFailure` | `boolean` If the test runner could not determine success or failure because the test depends on a component other than the system under test which failed. For example, a mobile test requires provisioning a device where the test executes, and that provisioning can fail. |
| `abortedByUser`         | `boolean` If the end user aborted the test execution before a pass or fail could be determined. For example, the user pressed ctrl-c which sent a kill signal to the test runner while the test was running.                                                                  |
| `hasErrorLogs`          | `boolean` If results are being provided to the user in certain cases of infrastructure failures                                                                                                                                                                               |

## SkippedDetail

Details for an outcome with a SKIPPED outcome summary.

|                                                JSON representation                                                |
|-------------------------------------------------------------------------------------------------------------------|
| ``` { "incompatibleDevice": boolean, "incompatibleAppVersion": boolean, "incompatibleArchitecture": boolean } ``` |

|                                                    Fields                                                    ||
|----------------------------|----------------------------------------------------------------------------------|
| `incompatibleDevice`       | `boolean` If the requested OS version doesn't run on the specific device model.  |
| `incompatibleAppVersion`   | `boolean` If the App doesn't support the specific API level.                     |
| `incompatibleArchitecture` | `boolean` If the App doesn't run on the specific architecture, for example, x86. |