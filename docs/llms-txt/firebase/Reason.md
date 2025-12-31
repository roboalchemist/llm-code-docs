# Source: https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/Reason.md.txt

# Reason

Possible invalid request reasons.

|                                                  Enums                                                  ||
|------------------------------------|---------------------------------------------------------------------|
| `REASON_UNSPECIFIED`               | No reason has been specified - the default.                         |
| `REQUEST_INVALID`                  | The request is not valid.                                           |
| `RESOURCE_TOO_BIG`                 | One or more of the resources specified in the request is too large. |
| `RESOURCE_NOT_FOUND`               | One or more resources specified in the request cannot be found.     |
| `UNSUPPORTED`                      | This request is not (currently) supported.                          |
| `NOT_IMPLEMENTED`                  | This request is not currently implemented.                          |
| `RESULT_STORAGE_PERMISSION_DENIED` | The caller has no permission for storing the test results           |