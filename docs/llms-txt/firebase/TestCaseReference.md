# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/TestCaseReference.md.txt

# TestCaseReference

- [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/TestCaseReference#SCHEMA_REPRESENTATION)

A reference to a test case.

Test case references are canonically ordered lexicographically by these three factors: \* First, by testSuiteName. \* Second, by className. \* Third, by name.

|                           JSON representation                            |
|--------------------------------------------------------------------------|
| ``` { "name": string, "className": string, "testSuiteName": string } ``` |

|                                        Fields                                         ||
|-----------------|----------------------------------------------------------------------|
| `name`          | `string` The name of the test case. Required.                        |
| `className`     | `string` The name of the class.                                      |
| `testSuiteName` | `string` The name of the test suite to which this test case belongs. |