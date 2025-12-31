# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/NonSdkApi.md.txt

# NonSdkApi

- [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/NonSdkApi#SCHEMA_REPRESENTATION)
- [NonSdkApiInsight](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/NonSdkApi#NonSdkApiInsight)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/NonSdkApi#NonSdkApiInsight.SCHEMA_REPRESENTATION)
- [UpgradeInsight](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/NonSdkApi#UpgradeInsight)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/NonSdkApi#UpgradeInsight.SCHEMA_REPRESENTATION)
- [PendingGoogleUpdateInsight](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/NonSdkApi#PendingGoogleUpdateInsight)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/NonSdkApi#PendingGoogleUpdateInsight.SCHEMA_REPRESENTATION)

A non-sdk API and examples of it being called along with other metadata See <https://developer.android.com/distribute/best-practices/develop/restrictions-non-sdk-interfaces>

|                                                                                                                                                             JSON representation                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "apiSignature": string, "invocationCount": integer, "list": enum (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/GreyList), "exampleStackTraces": [ string ], "insights": [ { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/NonSdkApi#NonSdkApiInsight) } ] } ``` |

|                                                                                                          Fields                                                                                                          ||
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `apiSignature`         | `string` The signature of the Non-SDK API                                                                                                                                                        |
| `invocationCount`      | `integer` The total number of times this API was observed to have been called.                                                                                                                   |
| `list`                 | `enum (`[GreyList](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/GreyList)`)` Which list this API appears on                                                      |
| `exampleStackTraces[]` | `string` Example stack traces of this API being called.                                                                                                                                          |
| `insights[]`           | `object (`[NonSdkApiInsight](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/NonSdkApi#NonSdkApiInsight)`)` Optional debugging insights for non-SDK API violations. |

## NonSdkApiInsight

Non-SDK API insights (to address debugging solutions).

|                                                                                                                                                                                                                                      JSON representation                                                                                                                                                                                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "matcherId": string, "exampleTraceMessages": [ string ], // Union field `insight` can be only one of the following: "upgradeInsight": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/NonSdkApi#UpgradeInsight) }, "pendingGoogleUpdateInsight": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/NonSdkApi#PendingGoogleUpdateInsight) } // End of list of possible types for union field `insight`. } ``` |

|                                                                                                                                        Fields                                                                                                                                         ||
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `matcherId`                  | `string` A unique ID, to be used for determining the effectiveness of this particular insight in the context of a matcher. (required)                                                                                                                   |
| `exampleTraceMessages[]`     | `string` Optional sample stack traces, for which this insight applies (there should be at least one).                                                                                                                                                   |
| Union field `insight`. `insight` can be only one of the following:                                                                                                                                                                                                                    ||
| `upgradeInsight`             | `object (`[UpgradeInsight](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/NonSdkApi#UpgradeInsight)`)` An insight indicating that the hidden API usage originates from the use of a library that needs to be upgraded.    |
| `pendingGoogleUpdateInsight` | `object (`[PendingGoogleUpdateInsight](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/NonSdkApi#PendingGoogleUpdateInsight)`)` An insight indicating that the hidden API usage originates from a Google-provided library. |

## UpgradeInsight

This insight is a recommendation to upgrade a given library to the specified version, in order to avoid dependencies on non-SDK APIs.

|                      JSON representation                      |
|---------------------------------------------------------------|
| ``` { "packageName": string, "upgradeToVersion": string } ``` |

|                                                                Fields                                                                 ||
|--------------------|-------------------------------------------------------------------------------------------------------------------|
| `packageName`      | `string` The name of the package to be upgraded.                                                                  |
| `upgradeToVersion` | `string` The suggested version to upgrade to. Optional: In case we are not sure which version solves this problem |

## PendingGoogleUpdateInsight

This insight indicates that the hidden API usage originates from a Google-provided library. Users need not take any action.

|            JSON representation            |
|-------------------------------------------|
| ``` { "nameOfGoogleLibrary": string } ``` |

|                                                  Fields                                                  ||
|-----------------------|-----------------------------------------------------------------------------------|
| `nameOfGoogleLibrary` | `string` The name of the Google-provided library with the non-SDK API dependency. |