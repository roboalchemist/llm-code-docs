# Source: https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/StreamData.md.txt

# StreamData

- [JSON representation](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/StreamData#SCHEMA_REPRESENTATION)
- [Close](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/StreamData#Close)

Data for a stream.

|                                                                                                                                 JSON representation                                                                                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "streamId": integer, // Union field `contents` can be only one of the following: "data": string, "close": { object (https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/StreamData#Close) } // End of list of possible types for union field `contents`. } ``` |

|                                                                       Fields                                                                       ||
|------------|----------------------------------------------------------------------------------------------------------------------------------------|
| `streamId` | `integer` The unique ID of this stream, assigned by the client.                                                                        |
| Union field `contents`. The data of the stream, either bytes or "Close", indicating that the stream is done. `contents` can be only one of the following: ||
| `data`     | `string (`[bytes](https://developers.google.com/discovery/v1/type-format)` format)` Data in the stream. A base64-encoded string.       |
| `close`    | `object (`[Close](https://firebase.google.com/docs/test-lab/reference/testing/rest/v1/StreamData#Close)`)` The stream is closing. EOF. |

## Close

This type has no fields.
Message signifying that the stream closed.