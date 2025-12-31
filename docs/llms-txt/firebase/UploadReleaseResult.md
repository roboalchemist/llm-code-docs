# Source: https://firebase.google.com/docs/reference/app-distribution/rest/v1/UploadReleaseResult.md.txt

# UploadReleaseResult

Possible results of the upload release call.

|                                                            Enums                                                             ||
|-------------------------------------|-----------------------------------------------------------------------------------------|
| `UPLOAD_RELEASE_RESULT_UNSPECIFIED` | Upload binary result unspecified                                                        |
| `RELEASE_CREATED`                   | Upload binary resulted in a new release                                                 |
| `RELEASE_UPDATED`                   | Upload binary updated an existing release                                               |
| `RELEASE_UNMODIFIED`                | Upload binary resulted in a no-op. A release with the exact same binary already exists. |