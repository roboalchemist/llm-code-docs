# Source: https://docs.edgeimpulse.com/tools/libraries/sdks/ingestion/c.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# C SDK

The [C Ingestion SDK](https://github.com/edgeimpulse/ingestion-sdk-c) is a portable header-only library written in C99 for data collection on embedded devices. It's designed to reliably store sampled data from sensors at a high frequency in very little memory. On top of this it allows cryptographic signing of the data when sampling is complete. Data can be stored on a POSIX file system, in memory, or on a raw block device.

## Installation instructions

* Add [Mbed TLS](https://github.com/Mbed-TLS/mbedtls) to your project (see [signing contexts](/tools/libraries/sdks/ingestion/c#signing-contexts) to use a different TLS library).
* [Download the SDK](https://github.com/edgeimpulse/ingestion-sdk-c/archive/master.zip).
* Copy the `inc` folder to your project. This contains all headers and source files.

## Usage

The following application:

* Initializes the library.
* Sets up the Mbed TLS signing context with the key `my-hmac-sha256-key`.
* Creates a file with three axes (`accX`, `accY`, `accZ`) and four readings.
* It then prints out the CBOR buffer.

```c  theme={"system"}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "sensor_aq.h"
#include "sensor_aq_mbedtls_hs256.h"

int main() {
  // context to sign data, this object is instantiated below
  sensor_aq_signing_ctx_t signing_ctx;

  // use HMAC-SHA256 signatures, signed with Mbed TLS
  sensor_aq_mbedtls_hs256_ctx_t hs_ctx;
  // initialize the Mbed TLS context which also instantiates signing_ctx
  sensor_aq_init_mbedtls_hs256_context(&signing_ctx, &hs_ctx, "my-hmac-sha256-key");

  // set up the sensor acquisition context
  sensor_aq_ctx ctx = {
    // the SDK requires a single buffer, and does not do any dynamic allocation
    { (unsigned char*)malloc(1024), 1024 },

    // pass in the signing context
    &signing_ctx,

    // pointers to fwrite and fseek - note that these are pluggable so you
    // can work with them on non-POSIX systems too. See the Porting Guide below.
    &fwrite,
    &fseek,
    // if you set the time function this will add the 'iat' (issued at) field to the header
    // you can set this pointer to NULL for device that don't have an accurate clock (not recommended)
    &time
  };

  // payload header
  sensor_aq_payload_info payload = {
    // unique device ID (optional),
    // set this to e.g. MAC address or device EUI **if** your device has one
    "ac:87:a3:0a:2d:1b",
    // device type (required), use the same device type for similar devices
    "DISCO-L475VG-IOT01A",
    // how often new data is sampled in ms. (100Hz = every 10 ms.)
    // (note: this is a float)
    10,
    // the axes which you'll use.
    // the units field needs to comply to SenML units
    // (see https://www.iana.org/assignments/senml/senml.xhtml)
    { { "accX", "m/s2" }, { "accY", "m/s2" }, { "accZ", "m/s2" } }
  };

  // place to write our data
  FILE *file = fopen("encoded.cbor", "w+");

  // initialize the context, this verifies that all requirements are present.
  // it also writes the initial CBOR structure.
  int res;
  res = sensor_aq_init(&ctx, &payload, file);
  if (res != AQ_OK) {
    printf("sensor_aq_init failed (%d)\n", res);
    return 1;
  }

  // Periodically call `sensor_aq_add_data` to append data
  // (according to the frequency in the payload header)
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

  // when you're done call `sensor_aq_finish`
  // this will calculate the finalized signature
  // and close the CBOR file
  res = sensor_aq_finish(&ctx);
  if (res != AQ_OK) {
      printf("sensor_aq_finish failed (%d)\n", res);
      return 1;
  }

  // this would be a good moment to upload 'encoded.cbor'
  // to the Ingestion Service using your HTTP library of choice

  // for convenience we'll print the encoded file.
  // you can paste the output in http://cbor.me to decode
  printf("Encoded file:\n");

  // Print the content of the file here:
  fseek(file, 0, SEEK_END);
  size_t len = ftell(file);
  uint8_t *buffer = (uint8_t*)malloc(len);

  fseek(file, 0, SEEK_SET);
  fread(buffer, len, 1, file);

  for (size_t ix = 0; ix < len; ix++) {
      printf("%02x ", buffer[ix]);
  }
  printf("\n");
}
```

This example is also available in the SDK, and can be built with any modern C compiler:

```bash  theme={"system"}
$ cd ingestion-sdk-c/example
$ make
$ ./sensor-aq-test
a3 69 70 72 6f 74 65 63 74 65 64 a3 63 76 65 72 62 76 31 63 61 6c 67 65 48 53 32 35 36 63 69 61 74 1a 5d 8d f9 06 69 73 69 67 6e 61 74 75 72 65 78 40 63 30 35 62 66 66 36 34 33 39 66 37 39 62 66 32 31 31 38 63 36 34 36 66 36 64 61 30 65 63 66 61 38 32 35 62 33 33 38 37 37 33 66 66 62 35 39 63 37 66 64 34 36 61 38 34 38 64 66 64 37 61 63 37 67 70 61 79 6c 6f 61 64 a5 6b 64 65 76 69 63 65 5f 6e 61 6d 65 71 61 63 3a 38 37 3a 61 33 3a 30 61 3a 32 64 3a 31 62 6b 64 65 76 69 63 65 5f 74 79 70 65 73 44 49 53 43 4f 2d 4c 34 37 35 56 47 2d 49 4f 54 30 31 41 6b 69 6e 74 65 72 76 61 6c 5f 6d 73 0a 67 73 65 6e 73 6f 72 73 83 a2 64 6e 61 6d 65 64 61 63 63 58 65 75 6e 69 74 73 64 6d 2f 73 32 a2 64 6e 61 6d 65 64 61 63 63 59 65 75 6e 69 74 73 64 6d 2f 73 32 a2 64 6e 61 6d 65 64 61 63 63 5a 65 75 6e 69 74 73 64 6d 2f 73 32 66 76 61 6c 75 65 73 9f 83 fa c1 1c f5 c3 fa 3c f5 c2 8f fa 3f 9a e1 48 83 fa c1 1d 47 ae fa 3d 23 d7 0a fa 3f a3 d7 0a 83 fa c1 11 eb 85 fa 3c f5 c2 8f fa 3f 9d 70 a4 83 fa c1 12 3d 71 fa 3c 23 d7 0a f9 3d 00 ff
```

You can paste the output into [cbor.me](http://cbor.me) to decode.

## Signing contexts

If you are using a different TLS library you can implement a custom signing context. Here's an example:

```c  theme={"system"}
/**
 * Example none signing context
 */
#include <string.h>
#include "sensor_aq.h"

// initialization, set up your TLS library here
static int sensor_aq_signing_none_init(sensor_aq_signing_ctx_t *aq_ctx) {
  // you can use `aq_ctx->ctx` to store a reference to your internal TLS context
  // this value will be present in the other calls

  // return code 0 means OK here, any other value means error
  return 0;
}

// called whenever there is new data
static int sensor_aq_signing_none_update(sensor_aq_signing_ctx_t *aq_ctx, const uint8_t *buffer, size_t buffer_size) {
  // update the state of your internal TLS context
  // you can get your context back through `aq_ctx->ctx`

  return 0;
}

// called when there is no more data, calculate the finished signature
static int sensor_aq_signing_none_finish(sensor_aq_signing_ctx_t *aq_ctx, uint8_t *buffer) {
  // the `buffer` field will be equal to `aq_ctx->signature_length`

  // signature will always be zero
  memset(buffer, 0, aq_ctx->signature_length);
  return 0;
}

/**
 * construct a new signing context for none security
 * **NOTE:** This will provide zero verification for your data and data might be rejected by your provider
 *
 * @param aq_ctx An empty signing context (can declare it without arguments)
 */
void sensor_aq_init_none_context(sensor_aq_signing_ctx_t *aq_ctx) {
  // alg field in the header, please adhere to the JWS specification
  aq_ctx->alg = "none";
  // length of the signature
  aq_ctx->signature_length = 1;
  // internal reference to a context, e.g. the TLS context you created
  aq_ctx->ctx = NULL;

  // wire functions to the signing context
  aq_ctx->init = sensor_aq_signing_none_init;
  aq_ctx->update = sensor_aq_signing_none_update;
  aq_ctx->finish = sensor_aq_signing_none_finish;
}
```

### Adding fields to the protected header

The signing context can also add new fields to the protected header, such as an expiration date for the token. We suggest to use the [JWT Claim Names](https://tools.ietf.org/html/rfc7519#section-4.1). You do this by registering a `set_protected` callback:

```c  theme={"system"}
static int my_ctx_set_protected(struct sensor_aq_signing_ctx *aq_ctx, QCBOREncodeContext *cbor_ctx) {
    QCBOREncode_AddInt64ToMap(cbor_ctx, "exp", time(NULL) + 3600); // expires an hour from now

    return 0;
}

// during initialization
aq_ctx->set_protected = &my_ctx_set_protected;
```

## Usage on non-POSIX systems

The storage layer is pluggable. You'll need to set the `EI_SENSOR_AQ_STREAM` macro to an object of your choice, and then implement `fwrite()` and `fseek()` methods to interact with the storage layer. If your system has a clock you can also implement the `time()` method. If not, the `iat` (issued at) field in the header will be omitted.

This is an example of using a memory-backed storage layer:

```c  theme={"system"}
// Override the stream
#define EI_SENSOR_AQ_STREAM         memory_stream_t

// Holder for the stream
typedef struct {
    uint8_t buffer[2048];
    size_t length;
    size_t current_position;
} memory_stream_t;

// fwrite function for the stream
size_t ms_fwrite(const void *ptr, size_t size, size_t count, memory_stream_t *stream) {
    memcpy(stream->buffer + stream->current_position, ptr, size * count);
    stream->current_position += size * count;

    if (stream->current_position > stream->length) {
        stream->length = stream->current_position;
    }

    return count;
}

// set current position in the stream
int ms_fseek(memory_stream_t *stream, long int offset, int origin) {
    if (origin == 0 /* SEEK_SET */) {
        stream->current_position = offset;
    }
    else if (origin == 1 /* SEEK_CUR */) {
        stream->current_position += offset;
    }
    else if (origin == 2 /* SEEK_END */) {
        stream->current_position = stream->length + offset;
    }
    // @todo: do a boundary check here
    return 0;
}

int main() {
    // Set up the sensor acquisition basic context
    sensor_aq_ctx ctx = {
        { (unsigned char*)malloc(1024), 1024 },
        &signing_ctx,
        // custom fwrite / fseek
        &ms_fwrite,
        &ms_fseek,
        NULL // no time on this system
    };

    // Place to write our data.
    memory_stream_t stream;
    stream.length = 0;
    stream.current_position = 0;

    sensor_aq_init(&ctx, &payload, &stream);

    // ...
```


Built with [Mintlify](https://mintlify.com).