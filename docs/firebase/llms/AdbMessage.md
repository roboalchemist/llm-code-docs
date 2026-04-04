# Source: https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/AdbMessage.md.txt

# AdbMessage

- [JSON representation](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/AdbMessage#SCHEMA_REPRESENTATION)
- [Open](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/AdbMessage#Open)
  - [JSON representation](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/AdbMessage#Open.SCHEMA_REPRESENTATION)

A message to an ADB server.

|                                                                                                                                                                   JSON representation                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { // Union field `contents` can be only one of the following: "open": { object (https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/AdbMessage#Open) }, "streamData": { object (https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/StreamData) } // End of list of possible types for union field `contents`. } ``` |

|                                                                     Fields                                                                     ||
|--------------|----------------------------------------------------------------------------------------------------------------------------------|
| Union field `contents`. `contents` can be only one of the following:                                                                           ||
| `open`       | `object (`[Open](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/AdbMessage#Open)`)` Open a new stream.      |
| `streamData` | `object (`[StreamData](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/StreamData)`)` Send data to a stream. |

## Open

Message for opening a new stream.

|                JSON representation                 |
|----------------------------------------------------|
| ``` { "streamId": integer, "service": string } ``` |

|                                                                             Fields                                                                             ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| `streamId` | `integer` The unique ID that will be used to talk to this stream. This should probably just be a number that increments for each new Open request. |
| `service`  | `string` An ADB service to use in the new stream.                                                                                                  |