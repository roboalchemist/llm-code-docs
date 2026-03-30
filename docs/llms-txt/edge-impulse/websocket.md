# Source: https://docs.edgeimpulse.com/tools/protocols/remote-management/websocket.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# WebSocket

The remote management server implements a two-way protocol between devices and Edge Impulse, which allows users to control devices (for example to acquire new data) straight from the Studio. Devices can either connect directly to the remote management service over a WebSocket (see the protocol on this page) or can connect through a proxy like the [serial daemon](/tools/clis/edge-impulse-cli/serial-daemon) using the [serial protocol](/tools/protocols/remote-management/serial). The remote management protocol is not used for data ingestion, as a result, you will need to use the [Ingestion API](/apis/ingestion) for this. Devices authenticate to the remote management service with an API key.

Remote Management is a part of the Remote Ingestion system. The general architecture is shown below, while this documentation covers only the part marked with red color.

<Frame caption="Remote Ingestion Architecture">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/remote-management/remote-ingestion-arch-mgmt.png?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=7a8b946074c5cd624516a8f786233684" width="950" height="419" data-path=".assets/images/remote-management/remote-ingestion-arch-mgmt.png" />
</Frame>

Data from and to the remote management API can be encoded in either CBOR or JSON.

A comprehensive test suite for devices implementing this protocol is located here: [edgeimpulse/integration-tests-firmware](https://github.com/edgeimpulse/integration-tests-firmware).

## Connecting

To connect, open a websocket connection to either:

```
wss://remote-mgmt.edgeimpulse.com
```

or:

```
ws://remote-mgmt.edgeimpulse.com
```

Remote management service uses standard ports: 80 or 443.

## Typical flow

The diagram below shows a typical full session of the remote ingestion process that involves both remote management and ingestion services.

<Frame caption="Typical flow">
  <img src="https://mintcdn.com/edgeimpulse/s8dsOgJvVXspqLe-/.assets/images/remote-management/typical-flow.png?fit=max&auto=format&n=s8dsOgJvVXspqLe-&q=85&s=35d9dfa0b35fe81ea574fa264d80020d" width="846" height="828" data-path=".assets/images/remote-management/typical-flow.png" />
</Frame>

## Protocol

After opening the WebSocket connection, the `device` initiates the communication by sending the `Hello` message.
Messages can be encoded as `JSON` or `CBOR`. The format of the `Hello` message sent by the `device` determines the encoding of the messages for the rest of the session.

### `Hello` (request)

This is always the first message in the session. Only the `device` can send this message. The server will respond with the `Hello` response.

```
Sender:   device
Type:     request
Response: Hello
```

<CodeGroup>
  ```json Example Message theme={"system"}
  Example Message
  {
      "hello": {
          "version": 3,
          "apiKey": "ei_8dd502530a5232ff64374815fddc229151e0a82c1d4f23e86097d8acdf882295",
          "deviceId": "15:FE:90:11:1D:18",
          "deviceType": "PORTENTA_H7_M7",
          "connection": "daemon",
          "sensors": [{
              "name": "Camera (320x240)",
              "frequencies": [],
              "maxSampleLengthS": 60000
          }, {
              "name": "Camera (128x96)",
              "frequencies": [],
              "maxSampleLengthS": 60000
          }, {
              "name": "Accelerometer",
              "frequencies": [ 100, 62.5 ],
              "maxSampleLengthS": 600
          } , {
              "name": "Microphone",
              "frequencies": [ 16000 ],
              "maxSampleLengthS": 120
          }],
          "supportsSnapshotStreaming": true
      }
  }
  ```

  ```json JSON Schema theme={"system"}
  JSON Schema
  {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
          "hello": {
              "type": "object",
              "properties": {
                  "version": {
                      "type": "integer",
                      "decription": "API version, currently 3"
                  },
                  "apiKey": {
                      "type": "string",
                      "description": "API key of the Studio project"
                  },
                  "deviceId": {
                      "type": "string",
                      "description": "Unique identifier for this device, usually MAC address. Should be unique across your project in the Studio"
                  },
                  "deviceType": {
                      "type": "string",
                      "description": "Device type, for example the exact model of the device. Should be the same for all similar devices"
                  },
                  "connection": {
                      "type": "string",
                      "description": "How the device is connected, either `ip` (direct connection) or `daemon` (via the serial daemon)"
                  },
                  "sensors": {
                      "type": "array",
                      "description": "List of sensors that the device supports",
                      "items": {
                          "type": "object",
                          "properties": {
                              "name": {
                                  "type": "string",
                                  "description": "Human readable name like Accelerometer or Microphone. For cameras, set the name to `Camera (WIDTHxHEIGHT)`"
                              },
                              "frequencies": {
                                  "type": "array",
                                  "items": {
                                      "type": "number",
                                      "description": "List of supported frequencies by the sensor, in Hz. List can be empty for cameras."
                                  }
                              },
                              "maxSampleLengthS": {
                                  "type": "integer",
                                  "description": "Maximum sample length in seconds. For cameras, this value is ignored but must be a valid number (eg. 60)"
                              }
                          },
                          "required": [
                              "name",
                              "frequencies",
                              "maxSampleLengthS"
                          ]
                      }
                  },
                  "supportsSnapshotStreaming": {
                      "type": "boolean",
                      "description": "Set to `true` if the device supports snapshot streaming"
                  }
              },
              "required": [
                  "version",
                  "apiKey",
                  "deviceId",
                  "deviceType",
                  "connection",
                  "sensors",
                  "supportsSnapshotStreaming"
              ]
          }
      },
  }
  ```
</CodeGroup>

### `Hello` (response)

This is the response to the `Hello` request sent by the `device`. Only the server can send this message.

```
Sender:   server
Type:     response
Response: none
```

<CodeGroup>
  ```json Example Message theme={"system"}
  Example Message
  {
      "hello": true,
      "err": undefined
  }
  ```

  ```json JSON Schema theme={"system"}
  JSON Schema
  {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
          "hello": {
              "type": "boolean",
              "description": "Set to `true` if the device is accepted. `false` otherwise, and the `err` field is set to a string with error description"
          },
          "err": {
              "type": "string",
              "description": "Error message if `hello` is `false`. If `hello` is `true`, this field is `undefined` or may be empty"
          }
      },
      "required": [
          "hello"
      ]
  }
  ```
</CodeGroup>

### `Sample` (request)

When a user requests sampling through the Studio, the following message is sent to the `device`. The `device` needs to perform a handshake with the `hello` message first.  This message can be sent by the `server` only.

```
Sender:   server
Type:     request
Response: Sample
```

<CodeGroup>
  ```json Example Message theme={"system"}
  Example Message
  {
      "sample": {
          "label": "wave",
          "length": 10000,
          "path": "/api/training/data",
          "hmacKey": "15bc5650a2338e083fb74edf6faf6547",
          "interval": 10,
          "sensor": "Accelerometer"
      }
  }
  ```

  ```json JSON Schema theme={"system"}
  JSON Schema
  {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
          "sample": {
              "type": "object",
              "properties": {
                  "label": {
                      "type": "string",
                      "description": "Label for this data. Use this to populate the `x-file-name` header when posting data to the ingestion service"
                  },
                  "length": {
                      "type": "integer",
                      "description": "Sampling length in milliseconds"
                  },
                  "path": {
                      "type": "string",
                      "description": "Path of the URL where to post the data"
                  },
                  "hmacKey": {
                      "type": "string",
                      "description": "Key to sign the data with, the device does not have to adhere to this request"
                  },
                  "interval": {
                      "type": "integer",
                      "description": "Interval between samples. This can also be a float. Devices do not have to adhere to this field, e.g. if the sensor does not support this frequency, or if the value is non-sensical"
                  },
                  "sensor": {
                      "type": "string",
                      "description": "Name of the sensor to sample from. This field is only populated if the `sensors` field in the hello request was populated"
                  }
              },
              "required": [
                  "label",
                  "length",
                  "path",
                  "hmacKey",
                  "interval"
              ]
          }
      },
      "required": [
          "sample"
      ]
  }
  ```
</CodeGroup>

### `Sample` (response)

This is the response to the `Sample` request sent by the Studio. The `device` needs to send this response. Set the `sample` field to `true` if the sampling can start, or to `false` if the sampling cannot start. This can be sent multiple times, for example first send `true` to confirm that the device is ready to sample, and then send `false` if some error occurs.

```
Sender:   device
Type:     response
Response: none
```

<CodeGroup>
  ```json Example Message theme={"system"}
  Example Message
  {
      "sample": true
  }
  ```

  ```json JSON Schema theme={"system"}
  JSON Schema
  {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
          "sample": {
              "type": "boolean",
              "description": "Set to `true` if the `sample` request is correct, sensor can be configured to the desired parameters etc. Set to `false` otherwise, and provide the `err` field with a string with error description"
          },
          "err": {
              "type": "string",
              "description": "Error message if `sample` is `false`. If `sample` is `true`, this field is `undefined` or may be empty"
          }
      },
      "required": [
          "sample"
      ]
  }
  ```
</CodeGroup>

### `Sample started` (notification)

When the sampling starts, send the following message to the Studio. This is a notification, so no response is expected from Studio. This notification is required otherwise, the Studio will report an error to the user.

```
Sender:   device
Type:     notification
Response: none
```

<CodeGroup>
  ```json Example Message theme={"system"}
  Example Message
  {
      "sampleStarted": true
  }
  ```

  ```json JSON Schema theme={"system"}
  JSON Schema
  {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
          "sampleStarted": {
              "type": "boolean",
              "description": "Set to `true` if the sampling started. Set to `false` otherwise"
          },
      },
      "required": [
          "sampleStarted"
      ]
  }
  ```
</CodeGroup>

### `Sample processing` (notification)

If the device is done sampling but is still processing the sample before uploading, such as a device preprocessing audio or signing the file. Send the following message to indicate that the device is processing. This notification is optional.

```
Sender:   device
Type:     notification
Response: none
```

<CodeGroup>
  ```json Example Message theme={"system"}
  Example Message
  {
      "sampleProcessing": true
  }
  ```

  ```json JSON Schema theme={"system"}
  JSON Schema
  {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
          "sampleProcessing": {
              "type": "boolean",
              "description": "This field should always be `true`"
          },
      },
      "required": [
          "sampleStarted"
      ]
  }
  ```
</CodeGroup>

### `Sample reading` (notification)

If the device is not connected directly to the internet, the daemon needs to pull the data from the device over serial, which could be slow for large files. Send the following message to indicate that this process started, and how far the process is along. You can send this message multiple times, and the percentage will be updated in the Studio. This message is optional.

```
Sender:   device / daemon app
Type:     notification
Response: none
```

<CodeGroup>
  ```json Example Message theme={"system"}
  Example Message
  {
      "sampleReading": true,
      "progressPercentage": 33
  }
  ```

  ```json JSON Schema theme={"system"}
  JSON Schema
  {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
          "sampleReading": {
              "type": "boolean",
              "description": "This field should always be `true`"
          },
          "progressPercentage": {
              "type": "integer",
              "description": "Progress percentage of the reading process."
          }
      },
      "required": [
          "sampleReading",
          "progressPercentage"
      ]
  }
  ```
</CodeGroup>

### `Sample uploading` (notification)

Send this message before sending samples to the ingestion service. This message is used to update the UI in the Studio. This message is required.

```
Sender:   device
Type:     notification
Response: none
```

<CodeGroup>
  ```json Example Message theme={"system"}
  Example Message
  {
      "sampleUploading": true
  }
  ```

  ```json JSON Schema theme={"system"}
  JSON Schema
  {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
          "sampleUploading": {
              "type": "boolean",
              "description": "This field should always be `true`"
          },
      },
      "required": [
          "sampleUploading"
      ]
  }
  ```
</CodeGroup>

### `Sample finished` (notification)

Send this notification after sampling is completed and the file is uploaded. This notification is required.

```
Sender:   device
Type:     notification
Response: none
```

<CodeGroup>
  ```json Example Message theme={"system"}
  Example Message
  {
      "sampleFinished": true
  }
  ```

  ```json JSON Schema theme={"system"}
  JSON Schema
  {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
          "sampleFinished": {
              "type": "boolean",
              "description": "This field should always be `true`"
          },
      },
      "required": [
          "sampleFinished"
      ]
  }
  ```
</CodeGroup>

### `Start snapshot` (request)

If the user selects the camera as a sensor on the ingestion page, the following request is sent to the device to start streaming snapshots. This request is optional, and the device does not have to send the response.

```
Sender:   server
Type:     request
Response: none
```

<CodeGroup>
  ```json Example Message theme={"system"}
  Example Message
  {
      "startSnapshot": true
  }
  ```

  ```json JSON Schema theme={"system"}
  JSON Schema
  {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
          "startSnapshot": {
              "type": "boolean",
              "description": "Set to `true` if the device should start streaming snapshots."
          }
      },
      "required": [
          "startSnapshot"
      ]
  }
  ```
</CodeGroup>

### `Stop snapshot` (request)

When snapshot streaming should stop, the following message is sent to the device. This request is optional, and the device does not have to send the response.

```
Sender:   server
Type:     request
Response: none
```

<CodeGroup>
  ```json Example Message theme={"system"}
  Example Message
  {
      "stopSnapshot": true
  }
  ```

  ```json JSON Schema theme={"system"}
  JSON Schema
  {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
          "stopSnapshot": {
              "type": "boolean",
              "description": "Set to `true` if the device should stop streaming snapshots."
          }
      },
      "required": [
          "stopSnapshot"
      ]
  }
  ```
</CodeGroup>

### `Snapshot frame` (notification)

To send a snapshot from the `device`, send the following message. The `snapshotFrame` is a base64 encoded JPG file.
You don't have to send this message too often, 5 times a second is plenty for most use cases.

```
Sender:   device
Type:     notification
Response: none
```

<CodeGroup>
  ```json Example Message theme={"system"}
  Example Message
  {
      "snapshotFrame": "/9j/4AAQSkZJRgABAQAASABIAAD/4QjcRX..."
  }
  ```

  ```json JSON Schema theme={"system"}
  JSON Schema
  {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
          "snapshotFrame": {
              "type": "string",
              "description": "Base64 encoded JPG file"
          }
      },
      "required": [
          "snapshotFrame"
      ]
  }
  ```
</CodeGroup>

## Version history

This lists changes in the remote management protocol.

* v2 - Changed the type of sensors from a string to a complex type describing frequencies and maximum sample length.
  * For devices still registering with version 1 a default max. sample length of 60 seconds will be set, and a default frequency of 100Hz.
  * If a v1 device registers with the sensor name "Built-in accelerometer" the default sample length will be 300 seconds, and the frequencies will be 62.5Hz and 100Hz.
  * If a v1 device registers with the sensor name "Built-in microphone" a default frequency of 16KHz will be set.
* v3 - Add progress percentages for `sampleReading` and commands for snapshot streaming. For v2 devices, the progress percentage is ignored, and `supportsSnapshotStreaming` is set to `false`.


Built with [Mintlify](https://mintlify.com).