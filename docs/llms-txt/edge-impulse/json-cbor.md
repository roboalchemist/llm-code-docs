# Source: https://docs.edgeimpulse.com/tools/specifications/data-acquisition/json-cbor.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# JSON | CBOR

To send data from any device or any system to Edge Impulse you will need to deliver the data in the Data acquisition format. This is a small specification that describes the type of data, the sensor data itself, and information about the device that generated the data. You can optionally sign this data so you have cryptographic proof on the origin and integrity of the data.

If you have your data already in CSV, JPG, PNG or WAV format, you can also just upload the data either using the [uploader](/studio/projects/data-acquisition/uploader) feature in the Studio, or using the CLI, see [CLI Uploader](/tools/clis/edge-impulse-cli/uploader) for more information. For CSV files, either use [CSV data acquisition](/tools/specifications/data-acquisition/csv) specification or use the [CSV Wizard](/studio/projects/data-acquisition/csv-wizard) feature for more flexibility.

If you are using an [Edge AI hardware with an Edge Impulse firmware](/hardware) it will already send data in this format, and if you want to collect data from other devices the [data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) will automatically convert and sign your data.

## Data acquisition format specification

The Edge Impulse Data Acquisition format is an optimized binary format for time-series data. It allows cryptographic signing of the data when sampling is complete to prove the authenticity of the data. Data is encoded using [CBOR](https://cbor.io) or JSON and signed according to the [JSON Web Signature](https://tools.ietf.org/html/rfc7515) specification.

Example in JSON:

```json  theme={"system"}
{
    "protected": {
        "ver": "v1",
        "alg": "HS256",
        "iat": 1564128599
    },
    "signature": "b0ee0572a1984b93b6bc56e6576e2cbbd6bccd65d0c356e26b31bbc9a48210c6",
    "payload": {
        "device_name": "ac:87:a3:0a:2d:1b",
        "device_type": "DISCO-L475VG-IOT01A",
        "interval_ms": 10,
        "sensors": [
            { "name": "accX", "units": "m/s2" },
            { "name": "accY", "units": "m/s2" },
            { "name": "accZ", "units": "m/s2" }
        ],
        "values": [
            [ -9.81, 0.03, 1.21 ],
            [ -9.83, 0.04, 1.27 ],
            [ -9.12, 0.03, 1.23 ],
            [ -9.14, 0.01, 1.25 ]
        ]
    }
}
```

## Fields

* `protected` - information about the signature format.
  * `ver` - always `v1` (required).
  * `alg` - the algorithm used to sign this file. Either `HS256` (HMAC-SHA256) or `none` (required).
  * `iat` - date when the file was created in seconds since epoch. Only set this when the device creating the file has an accurate clock (optional).
* `signature` - cryptographic signature for this file (required).
* `payload` - sensor data.
  * `device_name` - unique identifier for this device. **Only** set this when the device has a globally unique identifier (e.g. MAC address). If this field is set the device shows up on the 'Devices' page in the studio (optional).
  * `device_type` - device type, for example the exact model of the device. Should be the same for all similar devices (required).
  * `interval_ms` - the frequency of the data in this file (in milliseconds). E.g. for 100Hz fill in `10` (new data every 10 ms.). You can use a float here if you need the precision (required). If you have sensors with different sampling frequencies, you should upscale to the highest frequency to keep the finest granularity. Example: sensor A is 100 Hz, sensor B is 5 Hz. Upscale sensor B to 100 Hz by duplicating each value 20 times (100/5). You could also smooth values over between samples.
  * `sensors` - array with sensor axes.
    * `name` - name of the axis.
    * `units` - type of data on this axis. Needs to comply to [SenML units](https://www.iana.org/assignments/senml/senml.xhtml) (required).
  * `values` - array of sensor values. One array item per interval, and as many items in this array as there are sensor axes. If you have a single sensor, you are allowed to flatten this array to save space. An array of string values can be used to refer to binary attachments sent to the ingestion service using multipart requests.

## Signing data

Files can be signed to establish a trust chain between device and Edge Impulse. Because the `iat` and `device_name` fields are included in the signed file you can validate authenticity of the data, which device created the data, and when the data was captured. Currently data can be signed with a symmetric HMAC key. You can create HMAC keys under 'Dashboard' in the studio.

### HMAC SHA256

To sign data using HMAC SHA256:

1. Set the `signature` field to `0000000000000000000000000000000000000000000000000000000000000000` (64 times ASCII `0`).
2. Create the full CBOR or JSON object.
3. Use your language's crypto module to sign the object with HMAC-SHA256. This should give you a 32 byte signature.
4. Replace the empty signature with the HEX encoded signature (64 characters ASCII).

## Binary notation (CBOR)

This is the same example as above, but in binary. Paste it into the [CBOR playground](http://cbor.me) to decode:

```txt  theme={"system"}
a3 69 70 72 6f 74 65 63 74 65 64 a3 63 76 65 72 62 76 31 63 61 6c 67 65 48 53 32 35 36 63 69 61 74 1a 5d 3a dd 3d 69 73 69 67 6e 61 74 75 72 65 78 40 62 30 65 65 30 35 37 32 61 31 39 38 34 62 39 33 62 36 62 63 35 36 65 36 35 37 36 65 32 63 62 62 64 36 62 63 63 64 36 35 64 30 63 33 35 36 65 32 36 62 33 31 62 62 63 39 61 34 38 32 31 30 63 36 67 70 61 79 6c 6f 61 64 a5 6b 64 65 76 69 63 65 5f 6e 61 6d 65 71 61 63 3a 38 37 3a 61 33 3a 30 61 3a 32 64 3a 31 62 6b 64 65 76 69 63 65 5f 74 79 70 65 73 44 49 53 43 4f 2d 4c 34 37 35 56 47 2d 49 4f 54 30 31 41 6b 69 6e 74 65 72 76 61 6c 5f 6d 73 0a 67 73 65 6e 73 6f 72 73 83 a2 64 6e 61 6d 65 64 61 63 63 58 65 75 6e 69 74 73 64 6d 2f 73 32 a2 64 6e 61 6d 65 64 61 63 63 59 65 75 6e 69 74 73 64 6d 2f 73 32 a2 64 6e 61 6d 65 64 61 63 63 5a 65 75 6e 69 74 73 64 6d 2f 73 32 66 76 61 6c 75 65 73 9f 83 fa c1 1c f5 c3 fa 3c f5 c2 8f fa 3f 9a e1 48 83 fa c1 1d 47 ae fa 3d 23 d7 0a fa 3f a3 d7 0a 83 fa c1 11 eb 85 fa 3c f5 c2 8f fa 3f 9d 70 a4 83 fa c1 12 3d 71 fa 3c 23 d7 0a f9 3d 00 ff
```

## Examples

Data can easily be generated by any language that has a CBOR or JSON library available.

<CodeGroup>
  ```c C theme={"system"}
  // First, add the Edge Impulse C Ingestion SDK to your project.
  //     https://github.com/edgeimpulse/ingestion-sdk-c
  // See 'C SDK Usage Guide' for more information and porting information

  #include "sensor_aq.h"
  #include "sensor_aq_mbedtls_hs256.h"

  const char *hmac_key = "fed53116f20684c067774ebf9e7bcbdc";

  int main() {
      // The sensor format supports signing the data, set up a signing context
      sensor_aq_signing_ctx_t signing_ctx;

      // We'll use HMAC SHA256 signatures, which can be created through Mbed TLS
      // If you use a different crypto library you can implement your own context
      sensor_aq_mbedtls_hs256_ctx_t hs_ctx;
      // Set up the context, the last argument is the HMAC key
      sensor_aq_init_mbedtls_hs256_context(&signing_ctx, &hs_ctx, hmac_key);

      // Set up the sensor acquisition basic context
      sensor_aq_ctx ctx = {
          // We need a single buffer. The library does not require any dynamic allocation (but your TLS library might)
          { (unsigned char*)malloc(1024), 1024 },

          // Pass in the signing context
          &signing_ctx,

          // And pointers to fwrite and fseek - note that these are pluggable so you can work with them on
          // non-POSIX systems too. Just override the EI_SENSOR_AQ_STREAM macro to your custom file type.
          &fwrite,
          &fseek,
          // if you set the time function this will add 'iat' (issued at) field to the header with the current time
          // if you don't include it, this will be omitted
          &time
      };

      // Payload header
      sensor_aq_payload_info payload = {
          // Unique device ID (optional), set this to e.g. MAC address or device EUI **if** your device has one
          "ac:87:a3:0a:2d:1b",
          // Device type (required), use the same device type for similar devices
          "DISCO-L475VG-IOT01A",
          // How often new data is sampled in ms. (100Hz = every 10 ms.)
          10,
          // The axes which you'll use. The units field needs to comply to SenML units (see https://www.iana.org/assignments/senml/senml.xhtml)
          { { "accX", "m/s2" }, { "accY", "m/s2" }, { "accZ", "m/s2" } }
      };

      // Place to write our data.
      // The library streams data, and does not cache everything in buffers
      FILE *file = fopen("test/encoded.cbor", "w+");

      // Initialize the context, this verifies that all requirements are present
      // it also writes the initial CBOR structure
      int res;
      res = sensor_aq_init(&ctx, &payload, file, false);
      if (res != AQ_OK) {
          printf("sensor_aq_init failed (%d)\n", res);
          return 1;
      }

      // Periodically call `sensor_aq_add_data` (every 10 ms. in this example) to append data
      float values[][3] = {
          { -9.81, 0.03, 1.21 },
          { -9.83, 0.04, 1.28 },
          { -9.12, 0.03, 1.23 },
          { -9.14, 0.01, 1.25 }
      };
      for (size_t ix = 0; ix < sizeof(values) / sizeof(values[0]); ix++) {
          res = sensor_aq_add_data(&ctx, values[ix], 3);
          if (res != AQ_OK) {
              printf("sensor_aq_add_data failed (%d)\n", res);
              return 1;
          }
      }

      // When you're done call sensor_aq_finish - this will calculate the finalized signature and close the CBOR file
      res = sensor_aq_finish(&ctx);
      if (res != AQ_OK) {
          printf("sensor_aq_finish failed (%d)\n", res);
          return 1;
      }

      // Use the HTTP libraries available for your platform to upload
      //      test/encoded.cbor
      // to
      //      https://ingestion.edgeimpulse.com/api/training/data
  }
  ```

  ```javascript Javascript theme={"system"}
  const fs = require('fs');
  const crypto = require('crypto');
  const Path = require('path');
  const request = require('request');

  const hmac_key = "fed53116f20684c067774ebf9e7bcbdc";
  const API_KEY = "ei_fd83...";

  // empty signature (all zeros). HS256 gives 32 byte signature, and we encode in hex, so we need 64 characters here
  let emptySignature = Array(64).fill('0').join('');

  let data = {
      protected: {
          ver: "v1",
          alg: "HS256",
          iat: Math.floor(Date.now() / 1000) // epoch time, seconds since 1970
      },
      signature: emptySignature,
      payload: {
          device_name: "ac:87:a3:0a:2d:1b",
          device_type: "DISCO-L475VG-IOT01A",
          interval_ms: 10,
          sensors: [
              { name: "accX", units: "m/s2" },
              { name: "accY", units: "m/s2" },
              { name: "accZ", units: "m/s2" }
          ],
          values: [
              [ -9.81, 0.03, 1.21 ],
              [ -9.83, 0.04, 1.27 ],
              [ -9.12, 0.03, 1.23 ],
              [ -9.14, 0.01, 1.25 ]
          ]
      }
  };

  let encoded = JSON.stringify(data);

  // now calculate the HMAC and fill in the signature
  let hmac = crypto.createHmac('sha256', hmac_key);
  hmac.update(encoded);
  let signature = hmac.digest().toString('hex');

  // update the signature in the message and re-encode
  data.signature = signature;
  encoded = JSON.stringify(data);

  // now upload the buffer to Edge Impulse
  request.post('https://ingestion.edgeimpulse.com/api/training/data', {
    headers: {
      'x-api-key': API_KEY,
      'x-file-name': 'test01',
      'Content-Type': 'application/json'
    },
    body: encoded,
    encoding: 'binary'
  }, function (err, response, body) {
    if (err) return console.error('Request failed', err);

    console.log('Uploaded file to Edge Impulse', response.statusCode, body);
  });
  ```

  ```python Python theme={"system"}
  #    $ pip3 install requests

  import json
  import time, hmac, hashlib
  import requests

  HMAC_KEY = "fed53116f20684c067774ebf9e7bcbdc"
  API_KEY = "ei_fd83..."

  # empty signature (all zeros). HS256 gives 32 byte signature, and we encode in hex, so we need 64 characters here
  emptySignature = ''.join(['0'] * 64)

  data = {
      "protected": {
          "ver": "v1",
          "alg": "HS256",
          "iat": time.time() # epoch time, seconds since 1970
      },
      "signature": emptySignature,
      "payload": {
          "device_name": "ac:87:a3:0a:2d:1b",
          "device_type": "DISCO-L475VG-IOT01A",
          "interval_ms": 10,
          "sensors": [
              { "name": "accX", "units": "m/s2" },
              { "name": "accY", "units": "m/s2" },
              { "name": "accZ", "units": "m/s2" }
          ],
          "values": [
              [ -9.81, 0.03, 1.21 ],
              [ -9.83, 0.04, 1.27 ],
              [ -9.12, 0.03, 1.23 ],
              [ -9.14, 0.01, 1.25 ]
          ]
      }
  }

  # encode in JSON
  encoded = json.dumps(data)

  # sign message
  signature = hmac.new(bytes(HMAC_KEY, 'utf-8'), msg = encoded.encode('utf-8'), digestmod = hashlib.sha256).hexdigest()

  # set the signature again in the message, and encode again
  data['signature'] = signature
  encoded = json.dumps(data)

  # and upload the file
  res = requests.post(url='https://ingestion.edgeimpulse.com/api/training/data',
                      data=encoded,
                      headers={
                          'Content-Type': 'application/json',
                          'x-file-name': 'idle01',
                          'x-api-key': API_KEY
                      })
  if (res.status_code == 200):
      print('Uploaded file to Edge Impulse', res.status_code, res.content)
  else:
      print('Failed to upload file to Edge Impulse', res.status_code, res.content)
  ```
</CodeGroup>

What about applying labels to your samples? You can use the optional `x-label` header parameter when creating your request. See the header parameters available in the [Ingestion API](/apis/ingestion) documentation.

## Binary payloads (e.g. for audio)

For some payloads, like audio data, it's not feasible to convert the raw sensor data into CBOR values while capturing data on the device. For these cases you can send a binary payload. The same header structure as above applies, but instead of writing the values in the `values` CBOR field you can append a binary array at the end of the file (in `uint8`, `uint16`, `uint32`, `int8`, `int16`, `int32` or `float32` format). To do so:

1. Limit your data to a single sensor.
2. Set the value of the `values` field to: `[ "Ref-Binary-i16" ]` (so a string within an array, where `i16` indicates `int16`, alternatively you can use `u16` for `uint16` or `f32` for `float32`).
3. Write the CBOR header. Note that this needs to be a valid CBOR structure, *and* that it requires termination with `0xFF`. The easiest to achieve this is by writing the `values` field as an indefinite length array (which needs to be terminated by `0xFF`.
4. Write your payload (little endian).
   * If you need to align your writes the easiest is to pad the `Ref-Binary-i16` string with spaces on the right.
5. Update the signature with the signature for the full file, including header and payload.
6. Upload the data to the ingestion service with the `Content-Type: application/octet-stream` header.

Here is an example of a valid audio sample that includes a binary payload:

```
a36970726f746563746564a26376657262763163616c67654853323536697369676e6174757265784038346432316234343665323831383561356336303761396437656134636336333735356137363261666164643036343334613136353766623433386237656630677061796c6f6164a56b6465766963655f6e616d657143343a37463a35313a38443a31383a34416b6465766963655f7479706573444953434f5f4c34373556475f494f543031416b696e74657276616c5f6d73f92c006773656e736f727381a2646e616d6565617564696f65756e697473637761766676616c7565739f6e5265662d42494e4152592d693136fff918fa18e718de18e218dd18e118e218f218f018f918f418e918ee18f618f918fc180919101915191119fe18f6180b190e190a19021912191419fc18f218f718
```

The header stops at byte `ff` (you can copy the beginning of the data up until the `ff` into [cbor.me](http://cbor.me) to validate) and the payload starts at `f918fa`.

## Binary attachments (e.g. for images)

For non-time-series data - currently only implemented for images - you can send binary attachments to the ingestion service. Here the same header structure is used as above, but instead of writing the values in the `values` CBOR field, you reference the content type, the size, and the signed hash (with the same HMAC key) of your attachment. You then need to send both the header and the actual file to the [Ingestion API](/apis/ingestion) via a multipart/form request (see 'Multipart requests' section).

**Note:** Including more than 1 binary attachment is currently not supported by the Edge Impulse Studio, such messages won't be rejected by the ingestion service though, these attachments will merely be 'invisible' from the studio.


Built with [Mintlify](https://mintlify.com).