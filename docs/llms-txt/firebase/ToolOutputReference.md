# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/ToolOutputReference.md.txt

# ToolOutputReference

- [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/ToolOutputReference#SCHEMA_REPRESENTATION)

A reference to a ToolExecution output file.

|                                                                                                                                                                             JSON representation                                                                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "output": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/FileReference) }, "creationTime": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Timestamp) }, "testCase": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/TestCaseReference) } } ``` |

|                                                                                                                                            Fields                                                                                                                                             ||
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `output`       | `object (`[FileReference](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/FileReference)`)` A FileReference to an output file. - In response: always set - In create/update request: always set                                                  |
| `creationTime` | `object (`[Timestamp](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Timestamp)`)` The creation time of the file. - In response: present if set by create/update request - In create/update request: optional                                   |
| `testCase`     | `object (`[TestCaseReference](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/TestCaseReference)`)` The test case to which this output file belongs. - In response: present if set by create/update request - In create/update request: optional |