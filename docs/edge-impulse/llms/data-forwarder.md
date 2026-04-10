# Source: https://docs.edgeimpulse.com/tools/clis/edge-impulse-cli/data-forwarder.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Data forwarder

The data forwarder is used to easily relay data from any device to Edge Impulse over serial. Devices write sensor values over a serial connection, and the data forwarder collects the data, signs the data and sends the data to the ingestion service. The data forwarder is useful to quickly enable data collection from a wide variety of development boards without having to port the full [remote management protocol](/tools/protocols/remote-management/websocket) and [serial protocol](/tools/protocols/remote-management/serial), but only supports collecting data at relatively low frequencies.

To use the data forwarder, load an application (examples for [Arduino](/tools/clis/edge-impulse-cli/data-forwarder#example-arduino), [Mbed OS](/tools/clis/edge-impulse-cli/data-forwarder#example-mbed-os) and [Zephyr](/tools/clis/edge-impulse-cli/data-forwarder#example-zephyr) below) on your development board, and run:

```
$ edge-impulse-data-forwarder
```

The data forwarder will ask you for the server you want to connect to, prompt you to log in, and then configure the device.

This is an example of the output of the forwarder:

```
Edge Impulse data forwarder v1.5.0
? What is your user name or e-mail address (edgeimpulse.com)? jan@edgeimpulse.com
? What is your password? [hidden]
Endpoints:
    Websocket: wss://remote-mgmt.edgeimpulse.com
    API:       https://studio.edgeimpulse.com
    Ingestion: https://ingestion.edgeimpulse.com

[SER] Connecting to /dev/tty.usbmodem401203
[SER] Serial is connected
[WS ] Connecting to wss://remote-mgmt.edgeimpulse.com
[WS ] Connected to wss://remote-mgmt.edgeimpulse.com
? To which project do you want to add this device? accelerometer-demo-1
? 3 sensor axes detected. What do you want to call them? Separate the names with ',': accX, accY, accZ
? What name do you want to give this device? Jan's DISCO-L475VG
[WS ] Authenticated
```

> **Note:** Your credentials are never stored. When you log in these are exchanged for a token. This token is used to further authenticate requests.

#### Clearing configuration

To clear the configuration, run:

```
$ edge-impulse-data-forwarder --clean
```

#### Overriding the frequency

To override the frequency, use:

```
$ edge-impulse-data-forwarder --frequency 100
```

#### Overriding the baud rate

To set a different baud rate, use:

```
$ edge-impulse-data-forwarder --baud-rate 460800
```

### Protocol

The protocol is very simple. The device should send data on baud rate 115,200 with one line per reading, and individual sensor data should be split with either a `,` or a `TAB`. For example, this is data from a 3-axis accelerometer:

```
-0.12,-6.20,7.90
-0.13,-6.19,7.91
-0.14,-6.20,7.92
-0.13,-6.20,7.90
-0.14,-6.20,7.91
```

The data forwarder will automatically determine the sampling rate and the number of sensors based on the output. If you load a new application where the sampling frequency or the number of axes changes, the data forwarder will automatically be reconfigured.

### Example (Arduino)

This is an example of a sketch that reads data from an accelerometer (tested on the Arduino Nano 33 BLE):

```
#include <Arduino_LSM9DS1.h>

#define CONVERT_G_TO_MS2    9.80665f
#define FREQUENCY_HZ        50
#define INTERVAL_MS         (1000 / (FREQUENCY_HZ + 1))

static unsigned long last_interval_ms = 0;

void setup() {
    Serial.begin(115200);
    Serial.println("Started");

    if (!IMU.begin()) {
        Serial.println("Failed to initialize IMU!");
        while (1);
    }
}

void loop() {
    float x, y, z;

    if (millis() > last_interval_ms + INTERVAL_MS) {
        last_interval_ms = millis();

        IMU.readAcceleration(x, y, z);

        Serial.print(x * CONVERT_G_TO_MS2);
        Serial.print('\t');
        Serial.print(y * CONVERT_G_TO_MS2);
        Serial.print('\t');
        Serial.println(z * CONVERT_G_TO_MS2);
    }
}
```

### Example (Mbed OS)

This is an example of an Mbed OS application that reads data from an accelerometer (tested on the ST IoT Discovery Kit):

```
#include "mbed.h"
#include "stm32l475e_iot01_accelero.h"

static int64_t sampling_freq = 104; // in Hz.
static int64_t time_between_samples_us = (1000000 / (sampling_freq - 1));

// set baud rate of serial port to 115200
static BufferedSerial serial_port(USBTX, USBRX, 115200);
FileHandle *mbed::mbed_override_console(int fd) {
    return &serial_port;
}

int main()
{
    int16_t pDataXYZ[3] = {0};
    Timer t;
    t.start();

    BSP_ACCELERO_Init();

    while(1) {
        int64_t next_tick = t.read_us() + time_between_samples_us;

        BSP_ACCELERO_AccGetXYZ(pDataXYZ);
        pc.printf("%d\t%d\t%d\n", pDataXYZ[0], pDataXYZ[1], pDataXYZ[2]);

        while (t.read_us() < next_tick) {
            /* busy loop */
        }
    }
}
```

There's also a complete example that samples data from both the accelerometer and the gyroscope here: [edgeimpulse/example-dataforwarder-mbed](https://github.com/edgeimpulse/example-dataforwarder-mbed).

### Example (Zephyr)

This is an example of a Zephyr application that reads data from an accelerometer (tested on the Nordic Semiconductor nRF52840 DK with ST X-NUCLEO-IKS02A1 shield), based on the [sensorhub](https://github.com/zephyrproject-rtos/zephyr/tree/master/samples/shields/x_nucleo_iks02a1/sensorhub) example:

```
#include <zephyr.h>
#include <sys/printk.h>
#include <drivers/sensor.h>
#include <stdio.h>
#include <stdlib.h>

static int64_t sampling_freq = 104; // in Hz.
static int64_t time_between_samples_us = (1000000 / (sampling_freq - 1));

int main() {
    // output immediately without buffering
    setvbuf(stdout, NULL, _IONBF, 0);

    // get driver for the accelerometer
    const struct device *iis2dlpc = device_get_binding(DT_LABEL(DT_INST(0, st_iis2dlpc)));
    if (iis2dlpc == NULL) {
        printf("Could not get IIS2DLPC device\n");
        return 1;
    }

    struct sensor_value accel[3];

    while (1) {
        // start a timer that expires when we need to grab the next value
        struct k_timer next_val_timer;
        k_timer_init(&next_val_timer, NULL, NULL);
        k_timer_start(&next_val_timer, K_USEC(time_between_samples_us), K_NO_WAIT);

        // read data from the sensor
        if (sensor_sample_fetch(iis2dlpc) < 0) {
            printf("IIS2DLPC Sensor sample update error\n");
            return 1;
        }

        sensor_channel_get(iis2dlpc, SENSOR_CHAN_ACCEL_XYZ, accel);

        // print over stdout
        printf("%.3f\t%.3f\t%.3f\r\n",
            sensor_value_to_double(&accel[0]),
            sensor_value_to_double(&accel[1]),
            sensor_value_to_double(&accel[2]));

        // busy loop until next value should be grabbed
        while (k_timer_status_get(&next_val_timer) <= 0);
    }
}
```

There's also a complete example that samples data from the accelerometer here: [edgeimpulse/example-dataforwarder-zephyr](https://github.com/edgeimpulse/example-dataforwarder-zephyr).

### Sensor fusion

Using the Data Forwarder, you can relay data from multiple sensors. You can check [Benjamin Cabe's artificial nose](https://github.com/kartben/artificial-nose) for a complete example using NO2, CO, C2H5OH and VOC sensors on a WIO Terminal.

You may also have sensors with different sampling frequencies, such as:

* accelerometer: 3 axis sampled at 100Hz
* RMS current sensor: 1 axis sampled at 5Hz

In this case, you should first upscale to the highest frequency to keep the finest granularity: upscale RMS sensor to 100 Hz by duplicating each value 20 times (100/5). You could also smooth values over between samples.

### Classifying data

To classify data you first deploy your project by following the steps in [Deployments](/hardware/deployments) tutorials - which contains examples for a wide variety of platforms. Then, declare a `features` array, fill it with sensor data, and run the classifier. Here are examples for Arduino, Mbed and Zephyr - but the same applies to any other platform.

> **Note:** These examples collect a full frame of data, then classify this data. This might not be what you want (as classification blocks the collection thread). See [Continuous audio sampling](/tutorials/topics/inference/sample-audio-continuously) for an example on how to implement continuous classification.

#### Classifying data (Arduino)

```cpp  theme={"system"}
// Include the Arduino library here (something like your_project_inference.h)
// In the Arduino IDE see **File > Examples > Your project name - Edge Impulse > Static buffer** to get the exact name
#include <your_project_inference.h>
#include <Arduino_LSM9DS1.h>

#define CONVERT_G_TO_MS2    9.80665f
#define FREQUENCY_HZ        EI_CLASSIFIER_FREQUENCY
#define INTERVAL_MS         (1000 / (FREQUENCY_HZ + 1))

static unsigned long last_interval_ms = 0;
// to classify 1 frame of data you need EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE values
float features[EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE];
// keep track of where we are in the feature array
size_t feature_ix = 0;

void setup() {
    Serial.begin(115200);
    Serial.println("Started");

    if (!IMU.begin()) {
        Serial.println("Failed to initialize IMU!");
        while (1);
    }
}

void loop() {
    float x, y, z;

    if (millis() > last_interval_ms + INTERVAL_MS) {
        last_interval_ms = millis();

        // read sensor data in exactly the same way as in the Data Forwarder example
        IMU.readAcceleration(x, y, z);

        // fill the features buffer
        features[feature_ix++] = x * CONVERT_G_TO_MS2;
        features[feature_ix++] = y * CONVERT_G_TO_MS2;
        features[feature_ix++] = z * CONVERT_G_TO_MS2;

        // features buffer full? then classify!
        if (feature_ix == EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE) {
            ei_impulse_result_t result;

            // create signal from features frame
            signal_t signal;
            numpy::signal_from_buffer(features, EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE, &signal);

            // run classifier
            EI_IMPULSE_ERROR res = run_classifier(&signal, &result, false);
            ei_printf("run_classifier returned: %d\n", res);
            if (res != 0) return;

            // print predictions
            ei_printf("Predictions (DSP: %d ms., Classification: %d ms., Anomaly: %d ms.): \n",
                result.timing.dsp, result.timing.classification, result.timing.anomaly);

            // print the predictions
            for (size_t ix = 0; ix < EI_CLASSIFIER_LABEL_COUNT; ix++) {
                ei_printf("%s:\t%.5f\n", result.classification[ix].label, result.classification[ix].value);
            }
        #if EI_CLASSIFIER_HAS_ANOMALY == 1
            ei_printf("anomaly:\t%.3f\n", result.anomaly);
        #endif

            // reset features frame
            feature_ix = 0;
        }
    }
}

void ei_printf(const char *format, ...) {
    static char print_buf[1024] = { 0 };

    va_list args;
    va_start(args, format);
    int r = vsnprintf(print_buf, sizeof(print_buf), format, args);
    va_end(args);

    if (r > 0) {
        Serial.write(print_buf);
    }
}
```

#### Classifying data (Mbed OS)

```cpp  theme={"system"}
#include "mbed.h"
#include "stm32l475e_iot01_accelero.h"
#include "ei_run_classifier.h"

static int64_t sampling_freq = EI_CLASSIFIER_FREQUENCY; // in Hz.
static int64_t time_between_samples_us = (1000000 / (sampling_freq - 1));

// to classify 1 frame of data you need EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE values
static float features[EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE];

// set baud rate of serial port to 115200
static BufferedSerial serial_port(USBTX, USBRX, 115200);
FileHandle *mbed::mbed_override_console(int fd) {
    return &serial_port;
}

int main()
{
    int16_t pDataXYZ[3] = {0};
    Timer t;
    t.start();

    BSP_ACCELERO_Init();

    while (1) {
        // fill the features array
        for (size_t ix = 0; ix < EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE; ix += EI_CLASSIFIER_RAW_SAMPLES_PER_FRAME) {
            int64_t next_tick = t.read_us() + time_between_samples_us;
            BSP_ACCELERO_AccGetXYZ(pDataXYZ);

            // copy accelerometer data into the features array
            features[ix + 0] = (float)pDataXYZ[0];
            features[ix + 1] = (float)pDataXYZ[0];
            features[ix + 2] = (float)pDataXYZ[0];

            while (t.read_us() < next_tick) {
                /* busy loop */
            }
        }

        // frame full? then classify
        ei_impulse_result_t result = { 0 };

        // create signal from features frame
        signal_t signal;
        numpy::signal_from_buffer(features, EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE, &signal);

        // run classifier
        EI_IMPULSE_ERROR res = run_classifier(&signal, &result, false);
        ei_printf("run_classifier returned: %d\n", res);
        if (res != 0) return 1;

        // print predictions
        ei_printf("Predictions (DSP: %d ms., Classification: %d ms., Anomaly: %d ms.): \n",
            result.timing.dsp, result.timing.classification, result.timing.anomaly);

        // print the predictions
        for (size_t ix = 0; ix < EI_CLASSIFIER_LABEL_COUNT; ix++) {
            ei_printf("%s:\t%.5f\n", result.classification[ix].label, result.classification[ix].value);
        }
    #if EI_CLASSIFIER_HAS_ANOMALY == 1
        ei_printf("anomaly:\t%.3f\n", result.anomaly);
    #endif
    }
}
```

#### Classifying (Zephyr)

Before adding the classifier in Zephyr:

1. Copy the extracted C++ library into your Zephyr project, and add the following to your `CMakeLists.txt` file (where `./model` is where you extracted the library).

```
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_subdirectory(./model)
```

1. Enable C++ and set the stack size of the main thread to at least 4K, by adding the following to `prj.conf`:

```
CONFIG_CPLUSPLUS=y
CONFIG_LIB_CPLUSPLUS=y
CONFIG_NEWLIB_LIBC=y
CONFIG_NEWLIB_LIBC_FLOAT_PRINTF=y

CONFIG_MAIN_STACK_SIZE=8192
```

1. If you're on a Cortex-M target, enable hardware acceleration by adding the following defines to your `CMakeLists.txt` file:

```
add_definitions(-DEIDSP_USE_CMSIS_DSP=1
                -DEIDSP_LOAD_CMSIS_DSP_SOURCES=1
                -DEI_CLASSIFIER_TFLITE_ENABLE_CMSIS_NN=1
                -DARM_MATH_LOOPUNROLL)
```

Then, run the following application:

```cpp  theme={"system"}
#include <zephyr.h>
#include <sys/printk.h>
#include <drivers/sensor.h>
#include <stdio.h>
#include <stdlib.h>
#include "ei_run_classifier.h"

static int64_t sampling_freq = EI_CLASSIFIER_FREQUENCY; // in Hz.
static int64_t time_between_samples_us = (1000000 / (sampling_freq - 1));

// to classify 1 frame of data you need EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE values
static float features[EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE];

int main() {
    // output immediately without buffering
    setvbuf(stdout, NULL, _IONBF, 0);

    // get driver for the accelerometer
    const struct device *iis2dlpc = device_get_binding(DT_LABEL(DT_INST(0, st_iis2dlpc)));
    if (iis2dlpc == NULL) {
        printf("Could not get IIS2DLPC device\n");
        return 1;
    }

    struct sensor_value accel[3];

    while (1) {
        for (size_t ix = 0; ix < EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE; ix += EI_CLASSIFIER_RAW_SAMPLES_PER_FRAME) {
            // start a timer that expires when we need to grab the next value
            struct k_timer next_val_timer;
            k_timer_init(&next_val_timer, NULL, NULL);
            k_timer_start(&next_val_timer, K_USEC(time_between_samples_us), K_NO_WAIT);

            // read data from the sensor
            if (sensor_sample_fetch(iis2dlpc) < 0) {
                printf("IIS2DLPC Sensor sample update error\n");
                return 1;
            }

            sensor_channel_get(iis2dlpc, SENSOR_CHAN_ACCEL_XYZ, accel);

            // fill the features array
            features[ix + 0] = sensor_value_to_double(&accel[0]);
            features[ix + 1] = sensor_value_to_double(&accel[1]);
            features[ix + 2] = sensor_value_to_double(&accel[2]);

            // busy loop until next value should be grabbed
            while (k_timer_status_get(&next_val_timer) <= 0);
        }

        // frame full? then classify
        ei_impulse_result_t result = { 0 };

        // create signal from features frame
        signal_t signal;
        numpy::signal_from_buffer(features, EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE, &signal);

        // run classifier
        EI_IMPULSE_ERROR res = run_classifier(&signal, &result, false);
        printf("run_classifier returned: %d\n", res);
        if (res != 0) return 1;

        // print predictions
        printf("Predictions (DSP: %d ms., Classification: %d ms., Anomaly: %d ms.): \n",
            result.timing.dsp, result.timing.classification, result.timing.anomaly);

        // print the predictions
        for (size_t ix = 0; ix < EI_CLASSIFIER_LABEL_COUNT; ix++) {
            printf("%s:\t%.5f\n", result.classification[ix].label, result.classification[ix].value);
        }
    #if EI_CLASSIFIER_HAS_ANOMALY == 1
        printf("anomaly:\t%.3f\n", result.anomaly);
    #endif
    }
}
```

### Troubleshooting

#### "The execution of scripts is disabled on this system" (Windows)

If you are running the data forwarder on a Windows system, you need to update PowerShell's execution policy to allow running scripts:

```
Set-ExecutionPolicy unrestricted
```


Built with [Mintlify](https://mintlify.com).