# Source: https://docs.edgeimpulse.com/apis/ingestion.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Ingestion API

The Ingestion API is used to send new device data to Edge Impulse. It's available on both HTTP and HTTPS endpoints and requires an API key to authenticate.

The API is available at:

```
http://ingestion.edgeimpulse.com
```

```
https://ingestion.edgeimpulse.com
```

## Supported file types

With the Ingestion API, you can upload the following types of files:

| Data type | Extension        | Acquisition format                                            | Annotation formats                                                                                                                                                                                                                                          |
| --------- | ---------------- | ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sensor    | `.json`, `.cbor` | [JSON CBOR](/tools/specifications/data-acquisition/json-cbor) | [labels](/tools/specifications/data-annotation/ei-labels), [structured labels](/tools/specifications/data-annotation/ei-structured-labels)                                                                                                                  |
| Sensor    | `.csv`           | [CSV](/tools/specifications/data-acquisition/csv)             | [labels](/tools/specifications/data-annotation/ei-labels), [structured labels](/tools/specifications/data-annotation/ei-structured-labels)                                                                                                                  |
| Audio     | `.wav`           | -                                                             | [labels](/tools/specifications/data-annotation/ei-labels), [structured labels](/tools/specifications/data-annotation/ei-structured-labels)                                                                                                                  |
| Image     | `.jpg`, `.png`   | -                                                             | [labels](/tools/specifications/data-annotation/ei-labels), [object detection](/tools/specifications/data-annotation/object-detection)                                                                                                                       |
| Video\*   | `.mp4`, `.avi`   | -                                                             | [labels](/tools/specifications/data-annotation/ei-labels)                                                                                                                                                                                                   |
| Labels    | `.labels`        | -                                                             | [labels](/tools/specifications/data-annotation/ei-labels), [structured labels](/tools/specifications/data-annotation/ei-structured-labels), [object detection](/tools/specifications/data-annotation/object-detection#edge-impulse-object-detection-format) |

*\*Video files can be split into individual frames after uploading to Studio.*

## Endpoints

### Files endpoint

There are three endpoints available:

* `POST /api/training/files` - for gathering training data.
* `POST /api/testing/files` - for gathering testing data. If you have the 'Live classification' page open in your browser the file will automatically be classified against the current impulse.
* `POST /api/anomaly/files` - for anomaly data from deployed devices.

The maximum number of files you can upload in a single request is 1000.
The maximum size of a single file is 100 MB.

The minimal request to the `api/training/files` endpoint is the following:

```
POST https://ingestion.edgeimpulse.com/api/training/files
X-Api-Key: ei_6040df080906d06f090e05013b7090580b707a0b050eb04d00350504070a2040
Content-Length: 442
Content-Type: multipart/form-data; boundary=999e13bfdfc8bcc05b97f4784410806e

b'--999e13bfdfc8bcc05b97f4784410806e\r\nContent-Disposition: form-data; name="data"; filename="test.cbor"\r\nContent-Type: application/cbor\r\n\r\n\xa3gpayload\xa5kdevice_nameq11:22:33:44:55:66kdevice_typelNORDIC_NRF91kinterval_ms\xfb@4\x00\x00\x00\x00\x00\x00gsensors\x83\xa2dnamedaccXeunitsdm/s2\xa2dnamedaccYeunitsdm/s2\xa2dnamedaccZeunitsdm/s2fvalues\x82\x83\xfb?\xc4\xd3\xb6\xc0\x00\x00\x00\xfb\xbf\xe9\xbaE\x00\x00\x00\x00\xfb@#\xa8\xd0`\x00\x00\x00\x83\xfb?\xb1&\xd8\xc0\x00\x00\x00\xfb\xbf\xe8\xcf\x0b`\x00\x00\x00\xfb@#\xd0\x04\xa0\x00\x00\x00iprotected\xa2calgdnonecverbv1isignatureb00\r\n--999e13bfdfc8bcc05b97f4784410806e--\r\n'
```

The request body is presented using Python notation for binary strings for readability purposes. Normally it is a stream of bytes.

### Data endpoint (legacy)

Because the `files` endpoints expect `Content-Type` to be `multipart/form-data`, there are also available legacy endpoints that require simpler requests:

* `POST /api/training/data`
* `POST /api/testing/data`
* `POST /api/anomaly/data`

The minimal request to the `api/training/data` endpoint is the following:

```
POST https://ingestion.edgeimpulse.com/api/training/data
X-Api-Key: ei_6040df080906d06f090e05013b7090580b707a0b050eb04d00350504070a2040
X-File-Name: test.cbor
Content-Type: application/cbor
Content-Length: 265

b'\xa3gpayload\xa5kdevice_nameq11:22:33:44:55:66kdevice_typelNORDIC_NRF91kinterval_ms\xfb@4\x00\x00\x00\x00\x00\x00gsensors\x83\xa2dnamedaccXeunitsdm/s2\xa2dnamedaccYeunitsdm/s2\xa2dnamedaccZeunitsdm/s2fvalues\x82\x83\xfb?\xc4\xd3\xb6\xc0\x00\x00\x00\xfb\xbf\xe9\xbaE\x00\x00\x00\x00\xfb@#\xa8\xd0`\x00\x00\x00\x83\xfb?\xb1&\xd8\xc0\x00\x00\x00\xfb\xbf\xe8\xcf\x0b`\x00\x00\x00\xfb@#\xd0\x04\xa0\x00\x00\x00iprotected\xa2calgdnonecverbv1isignatureb00'
```

The request body is presented using Python notation for binary strings for readability purposes. Normally it is a stream of bytes.

### Header Parameters

* `x-api-key` - API Key (required).
* `x-label` - Label (optional). If this header is not provided a label is automatically inferred from the filename through the following regex: `^[a-zA-Z0-9\s-_]+` - For example: idle.01 will yield the label idle. If you don't want to assign the label nor derive it from the file name, provide an `x-no-label` header with the value `1`.
* `x-disallow-duplicates` - When set, the server checks the hash of the message against your current dataset (optional). We'd recommend setting this header but haven't enabled it by default for backward compatibility.
* `x-add-date-id`: 1 - to add a date ID to the filename. For example: if you upload with filename test.wav the file name will be test - set this option and we'll add a unique ID to the end (this is what we use on the daemon to create unique names).
* `Content-type` - format of data used. Can be `application/cbor`, `application/json`, `multipart/form-data`.

### Responses

All responses are sent with content type `text/plain`. The following response codes may be returned:

* `200` - Stored the file, file name is in the body.
* `400` - Invalid message, e.g. fields are missing, or are invalid. See body for more information.
* `401` - Missing `x-api-key` header, or invalid API key.
* `421` - Missing header, see body for more information.
* `500` - Internal server error, see body for more information.

## Examples

<CodeGroup>
  ```bash curl theme={"system"}
  curl -X POST \
       -H "x-api-key: ei_238fae..." \
       -H "x-label: car" \
       -H "Content-Type: multipart/form-data" \
       -F "data=@one.png" \
       -F "data=@two.png" \
       https://ingestion.edgeimpulse.com/api/training/files
  ```

  ```python python theme={"system"}
  # Install requests via: `pip3 install requests`
  import requests
  import os

  api_key = 'ei_121...'
  # Add the files you want to upload to Edge Impulse
  files = [
      'one.png',
      'two.png',
  ]
  # # Replace the label with your own.
  label = 'car'
  # Upload the file to Edge Impulse using the API, and print the response.
  res = requests.post(url='https://ingestion.edgeimpulse.com/api/training/files',
                      headers={
                          'x-label': label,
                          'x-api-key': api_key,
                      },
                      # Creating the data payload for the request.
                      files=(('data', (os.path.basename(i), open(
                          i, 'rb'), 'image/png')) for i in files)
                      )

  if (res.status_code == 200):
      print('Uploaded file(s) to Edge Impulse\n', res.status_code, res.content)
  else:
      print('Failed to upload file(s) to Edge Impulse\n',
            res.status_code, res.content)
  ```

  ```javascript javascript theme={"system"}
  import fetch, { FormData, fileFromSync } from 'node-fetch';

  const form = new FormData();
  form.append('data', fileFromSync('one.png'));
  form.append('data', fileFromSync('two.png'));

  fetch('https://ingestion.edgeimpulse.com/api/training/files', {
      method: 'POST',
      headers: {
          'x-api-key': 'ei_238fae...',
          'x-label': 'car',
          'Content-Type': 'multipart/form-data'
      },
      body: form
  });
  ```
</CodeGroup>

### Raw requests

On the embedded devices, usually, there are no high-level libraries available to perform HTTP requests. In this case, you can use the following example to prepare an HTTP request to the Ingestion API:

The ingestion service accepts raw requests with data formatted as JSON or CBOR. We will use the following JSON structure as an example sample:

```json  theme={"system"}
{
    "payload": {
        "device_name": "11:22:33:44:55:66",
        "device_type": "NORDIC_NRF91",
        "interval_ms": 20.0,
        "sensors": [
            {
                "name": "accX",
                "units": "m/s2"
            },
            {
                "name": "accY",
                "units": "m/s2"
            },
            {
                "name": "accZ",
                "units": "m/s2"
            }
        ],
        "values": [
            [
                0.1627109944820404,
                -0.803987979888916,
                9.82971477508545
            ],
            [
                0.06699900329113007,
                -0.7752739787101746,
                9.906285285949707
            ]
        ]
    },
    "protected": {
        "alg": "none",
        "ver": "v1"
    },
    "signature": "00"
}
```


Built with [Mintlify](https://mintlify.com).