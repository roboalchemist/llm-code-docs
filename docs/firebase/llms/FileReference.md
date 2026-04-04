# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/FileReference.md.txt

# FileReference

- [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/FileReference#SCHEMA_REPRESENTATION)

A reference to a file.

|      JSON representation      |
|-------------------------------|
| ``` { "fileUri": string } ``` |

|                                                                                                                                                                                                              Fields                                                                                                                                                                                                              ||
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `fileUri` | `string` The URI of a file stored in Google Cloud Storage. For example: <http://storage.googleapis.com/mybucket/path/to/test.xml> or in gsutil format: <gs://mybucket/path/to/test.xml> with version-specific info, <gs://mybucket/path/to/test.xml#1360383693690000> An INVALID_ARGUMENT error will be returned if the URI format is not supported. - In response: always set - In create/update request: always set |