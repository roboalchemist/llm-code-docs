# Source: https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/DeviceMessage.md.txt

# DeviceMessage

- [JSON representation](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/DeviceMessage#SCHEMA_REPRESENTATION)
- [StatusUpdate](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/DeviceMessage#StatusUpdate)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/DeviceMessage#StatusUpdate.SCHEMA_REPRESENTATION)
- [StreamStatus](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/DeviceMessage#StreamStatus)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/DeviceMessage#StreamStatus.SCHEMA_REPRESENTATION)
- [Okay](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/DeviceMessage#Okay)
- [Fail](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/DeviceMessage#Fail)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/DeviceMessage#Fail.SCHEMA_REPRESENTATION)

A message returned from a device.

|                                                                                                                                                                                                                                           JSON representation                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { // Union field `contents` can be only one of the following: "statusUpdate": { object (https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/DeviceMessage#StatusUpdate) }, "streamStatus": { object (https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/DeviceMessage#StreamStatus) }, "streamData": { object (https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/StreamData) } // End of list of possible types for union field `contents`. } ``` |

|                                                                                       Fields                                                                                        ||
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Union field `contents`. `contents` can be only one of the following:                                                                                                                ||
| `statusUpdate` | `object (`[StatusUpdate](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/DeviceMessage#StatusUpdate)`)` Information about the device's state.   |
| `streamStatus` | `object (`[StreamStatus](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/DeviceMessage#StreamStatus)`)` The result of a device stream from ADB. |
| `streamData`   | `object (`[StreamData](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/StreamData)`)` Data from an open stream.                                 |

## StatusUpdate

A StatusUpdate message given over the ADB protocol for the device state.

|                                                                          JSON representation                                                                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "state": enum (https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/DeviceState), "properties": { string: string, ... }, "features": string } ``` |

|                                                                                                            Fields                                                                                                             ||
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `state`      | `enum (`[DeviceState](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/DeviceState)`)` The device's state                                                                                    |
| `properties` | `map (key: string, value: string)` A map of properties with information about this device. An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`. |
| `features`   | `string` A comma-separated list of "features" that this device supports.                                                                                                                                        |

## StreamStatus

The result of a stream.

|                                                                                                                                                                              JSON representation                                                                                                                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "streamId": integer, // Union field `status` can be only one of the following: "okay": { object (https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/DeviceMessage#Okay) }, "fail": { object (https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/DeviceMessage#Fail) } // End of list of possible types for union field `status`. } ``` |

|                                                                  Fields                                                                   ||
|------------|-------------------------------------------------------------------------------------------------------------------------------|
| `streamId` | `integer` The unique ID of this stream, assigned by the client.                                                               |
| Union field `status`. The result of the stream. Either "Okay" for success or "Fail" for failure. `status` can be only one of the following: ||
| `okay`     | `object (`[Okay](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/DeviceMessage#Okay)`)` Okay for success. |
| `fail`     | `object (`[Fail](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/DeviceMessage#Fail)`)` Fail for failure. |

## Okay

This type has no fields.
Message signifying that the stream is open

## Fail

Message signifying that the stream failed to open

|     JSON representation      |
|------------------------------|
| ``` { "reason": string } ``` |

|                        Fields                         ||
|----------|---------------------------------------------|
| `reason` | `string` A user-displayable failure reason. |