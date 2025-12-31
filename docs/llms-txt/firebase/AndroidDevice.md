# Source: https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/AndroidDevice.md.txt

# AndroidDevice

- [JSON representation](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/AndroidDevice#SCHEMA_REPRESENTATION)

A single Android device.

|                                            JSON representation                                            |
|-----------------------------------------------------------------------------------------------------------|
| ``` { "androidModelId": string, "androidVersionId": string, "locale": string, "orientation": string } ``` |

|                                                                        Fields                                                                         ||
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| `androidModelId`   | `string` Required. The id of the Android device to be used. Use the TestEnvironmentDiscoveryService to get supported options.     |
| `androidVersionId` | `string` Required. The id of the Android OS version to be used. Use the TestEnvironmentDiscoveryService to get supported options. |
| `locale`           | `string` Required. The locale the test device used for testing. Use the TestEnvironmentDiscoveryService to get supported options. |
| `orientation`      | `string` Required. How the device is oriented during the test. Use the TestEnvironmentDiscoveryService to get supported options.  |