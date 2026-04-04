# Source: https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails.md.txt

# Method: applicationDetailService.getApkDetails

- [HTTP request](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#body.HTTP_TEMPLATE)
- [Query parameters](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#body.QUERY_PARAMETERS)
- [Request body](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#body.request_body)
- [Response body](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#body.response_body)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#body.GetApkDetailsResponse.SCHEMA_REPRESENTATION)
- [Authorization scopes](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#body.aspect)
- [ApkDetail](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#ApkDetail)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#ApkDetail.SCHEMA_REPRESENTATION)
- [ApkManifest](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#ApkManifest)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#ApkManifest.SCHEMA_REPRESENTATION)
- [IntentFilter](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#IntentFilter)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#IntentFilter.SCHEMA_REPRESENTATION)
- [Metadata](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#Metadata)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#Metadata.SCHEMA_REPRESENTATION)
- [UsesFeature](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#UsesFeature)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#UsesFeature.SCHEMA_REPRESENTATION)
- [Service](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#Service)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#Service.SCHEMA_REPRESENTATION)
- [Try it!](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#try-it)

Gets the details of an Android application APK.

### HTTP request

`POST https://testing.googleapis.com/v1/applicationDetailService/getApkDetails`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Query parameters

|                                                                                                 Parameters                                                                                                 ||
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `bundleLocation` | `object (`[FileReference](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices#FileReference)`)` Optional. The App Bundle to be parsed for details. |

### Request body

The request body contains an instance of [FileReference](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/projects.testMatrices#FileReference).

### Response body

Response containing the details of the specified Android application.

If successful, the response body contains data with the following structure:

|                                                                    JSON representation                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "apkDetail": { object (https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#ApkDetail) } } ``` |

|                                                                                         Fields                                                                                          ||
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `apkDetail` | `object (`[ApkDetail](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#ApkDetail)`)` Details of the Android App. |

### Authorization scopes

Requires the following OAuth scope:

- `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## ApkDetail

Android application details based on application manifest and archive contents.

|                                                                      JSON representation                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "apkManifest": { object (https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#ApkManifest) } } ``` |

|                                                                              Fields                                                                               ||
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| `apkManifest` | `object (`[ApkManifest](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#ApkManifest)`)` |

## ApkManifest

An Android app manifest. See <http://developer.android.com/guide/topics/manifest/manifest-intro.html>

|                                                                                                                                                                                                                                                                                                                                                                                                               JSON representation                                                                                                                                                                                                                                                                                                                                                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "packageName": string, "minSdkVersion": integer, "maxSdkVersion": integer, "targetSdkVersion": integer, "applicationLabel": string, "intentFilters": [ { object (https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#IntentFilter) } ], "usesPermission": [ string ], "versionCode": string, "versionName": string, "metadata": [ { object (https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#Metadata) } ], "usesFeature": [ { object (https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#UsesFeature) } ], "services": [ { object (https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#Service) } ] } ``` |

|                                                                                                       Fields                                                                                                       ||
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `packageName`      | `string` Full Java-style package name for this application, e.g. "com.example.foo".                                                                                                            |
| `minSdkVersion`    | `integer` Minimum API level required for the application to run.                                                                                                                               |
| `maxSdkVersion`    | `integer` Maximum API level on which the application is designed to run.                                                                                                                       |
| `targetSdkVersion` | `integer` Specifies the API Level on which the application is designed to run.                                                                                                                 |
| `applicationLabel` | `string` User-readable name for the application.                                                                                                                                               |
| `intentFilters[]`  | `object (`[IntentFilter](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#IntentFilter)`)`                                           |
| `usesPermission[]` | `string` Permissions declared to be used by the application                                                                                                                                    |
| `versionCode`      | `string (`[int64](https://developers.google.com/discovery/v1/type-format)` format)` Version number used internally by the app.                                                                 |
| `versionName`      | `string` Version number shown to users.                                                                                                                                                        |
| `metadata[]`       | `object (`[Metadata](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#Metadata)`)` Meta-data tags defined in the manifest.           |
| `usesFeature[]`    | `object (`[UsesFeature](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#UsesFeature)`)` Feature usage tags defined in the manifest. |
| `services[]`       | `object (`[Service](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#Service)`)` Services contained in the tag.                      |

## IntentFilter

The section of an tag. <https://developer.android.com/guide/topics/manifest/intent-filter-element.html>

|                                  JSON representation                                   |
|----------------------------------------------------------------------------------------|
| ``` { "actionNames": [ string ], "categoryNames": [ string ], "mimeType": string } ``` |

|                               Fields                               ||
|-------------------|-------------------------------------------------|
| `actionNames[]`   | `string` The android:name value of the tag.     |
| `categoryNames[]` | `string` The android:name value of the tag.     |
| `mimeType`        | `string` The android:mimeType value of the tag. |

## Metadata

A tag within a manifest. <https://developer.android.com/guide/topics/manifest/meta-data-element.html>

|             JSON representation             |
|---------------------------------------------|
| ``` { "name": string, "value": string } ``` |

|                  Fields                   ||
|---------|----------------------------------|
| `name`  | `string` The android:name value  |
| `value` | `string` The android:value value |

## UsesFeature

A tag within a manifest. <https://developer.android.com/guide/topics/manifest/uses-feature-element.html>

|                JSON representation                |
|---------------------------------------------------|
| ``` { "name": string, "isRequired": boolean } ``` |

|                       Fields                       ||
|--------------|--------------------------------------|
| `name`       | `string` The android:name value      |
| `isRequired` | `boolean` The android:required value |

## Service

The section of an tag. <https://developer.android.com/guide/topics/manifest/service-element>

|                                                                                 JSON representation                                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "name": string, "intentFilter": [ { object (https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#IntentFilter) } ] } ``` |

|                                                                                                Fields                                                                                                ||
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`           | `string` The android:name value                                                                                                                                                    |
| `intentFilter[]` | `object (`[IntentFilter](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/applicationDetailService/getApkDetails#IntentFilter)`)` Intent filters in the service |