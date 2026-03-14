# Source: https://docs.edgeimpulse.com/tutorials/topics/zephyr/zephyr-module-microphone-kws.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Microphone Keyword Spotting on Zephyr

> Run Edge Impulse audio keyword spotting models on Zephyr RTOS using PDM microphones

Deploy audio keyword spotting models on Zephyr using the Edge Impulse Zephyr Module. Drop in your model → build → flash → get real-time audio inference.

<Info>
  This tutorial adapts the [IMU inference example](./zephyr-module-imu) for audio keyword spotting. The key differences are replacing the IMU sensor driver with Zephyr's DMIC (Digital Microphone) API and adjusting the inference pipeline for continuous audio classification.\
  Reference code: [https://github.com/edgeimpulse/ei-zephyr-mic-kws-inference](https://github.com/edgeimpulse/ei-zephyr-mic-kws-inference)
</Info>

## What You'll Build

A Zephyr application that:

* Captures real-time audio from PDM microphone
* Runs continuous keyword spotting inference
* Displays classification results via serial
* Works on any Zephyr board with PDM microphone support

## Prerequisites

* **Edge Impulse Zephyr Module workspace**: See [Edge Impulse Zephyr Module Deployment Guide](/hardware/deployments/run-zephyr-module)
* **Trained audio model**: e.g., the [Keyword Spotting](/tutorials/end-to-end/keyword-spotting) tutorial
* **Zephyr-supported board** with PDM microphone (Nordic Thingy:53, nRF5340 Audio DK, etc.)
* **Development tools**:
  * Zephyr SDK 0.17.4+
  * West 1.5.0+

## Supported Microphones

PDM microphones accessible through Zephyr's DMIC (Digital Microphone) driver are compatible:

| Board                   | Microphone | Driver                                                                                               |
| ----------------------- | ---------- | ---------------------------------------------------------------------------------------------------- |
| Nordic Thingy:53        | PDM        | `CONFIG_AUDIO_DMIC=y`                                                                                |
| nRF5340 Audio DK        | PDM        | `CONFIG_AUDIO_DMIC=y`                                                                                |
| STM32 boards with DFSDM | PDM        | `CONFIG_AUDIO_DMIC=y`                                                                                |
| Custom boards           | I2S/PDM    | See [Zephyr Audio Docs](https://docs.zephyrproject.org/latest/hardware/peripherals/audio/index.html) |

## 1. Initialize the Repository

```bash  theme={"system"}
west init -m https://github.com/edgeimpulse/ei-zephyr-mic-kws-inference
cd ei-zephyr-mic-kws-inference
west update
```

This fetches:

* Zephyr RTOS
* Edge Impulse Zephyr SDK module
* All dependencies

## 2. Deploy Your Audio Model

In Edge Impulse Studio:

1. Go to **Deployment**
2. Select **Zephyr library**
3. Click **Build**
4. Download the model `.zip`

Extract into `model/`:

```bash  theme={"system"}
unzip -o ~/Downloads/your-model.zip -d model/
```

Ensure `model/` contains:

* `CMakeLists.txt`
* `edge-impulse-sdk/`
* `model-parameters/`
* `tflite-model/`

## 3. Build

Select your board:

```bash  theme={"system"}
west build --pristine -b thingy53/nrf5340/cpuapp
```

Or configure in `.west/config`:

```ini  theme={"system"}
[build]
board = thingy53/nrf5340/cpuapp
```

Then build:

```bash  theme={"system"}
west build --pristine
```

## 4. Flash

```bash  theme={"system"}
west flash
```

Alternative flash runners:

```bash  theme={"system"}
west flash --runner jlink
west flash --runner nrfjprog
west flash --runner openocd
```

## 5. Monitor Output

```bash  theme={"system"}
minicom -D /dev/ttyACM0 -b 115200
```

Expected output:

```
Starting microphone inference...
Recording audio...
Predictions (DSP: 124 ms, Classification: 8 ms):
    noise: 0.05
    go: 0.92
    stop: 0.03
```

## How It Works

### Adapting from IMU to Audio

This example follows the same architecture as the [IMU inference tutorial](./zephyr-module-imu), with these key changes:

| Component         | IMU Example                    | Audio Example                    |
| ----------------- | ------------------------------ | -------------------------------- |
| **Sensor API**    | Zephyr Sensor API (`sensor.h`) | Zephyr DMIC API (`audio/dmic.h`) |
| **Data Source**   | I²C/SPI accelerometer/gyro     | PDM microphone                   |
| **Sample Rate**   | 100 Hz (typical)               | 16 kHz                           |
| **Data Type**     | 3-axis or 6-axis float         | Mono audio int16                 |
| **Buffer Size**   | 200-300 samples (2-3s)         | 16000 samples (1s)               |
| **Driver Config** | `CONFIG_SENSOR=y`              | `CONFIG_AUDIO_DMIC=y`            |

The inference loop, circular buffer, and Edge Impulse integration remain the same—only the sensor interface changes.

### Code Flow

1. **Initialize** - Set up microphone via Zephyr DMIC API
2. **Sample** - Continuous audio data collection at model frequency
3. **Buffer** - Circular buffer stores audio samples
4. **Infer** - Run classifier when buffer is full
5. **Output** - Print classification results
6. **Loop** - Repeat

## Project Structure

```
ei-zephyr-mic-kws-inference/
├── model/                  # Your Edge Impulse model (Zephyr library)
├── src/
│   ├── main.cpp            # App entry point
│   ├── inference/          # Inference state machine
│   │   └── inference.cpp
│   └── microphone/         # Microphone interface
│       ├── microphone.cpp
│       └── microphone.h
├── CMakeLists.txt          # Build configuration
├── prj.conf                # Zephyr config
└── west.yml                # Manifest (declares Edge Impulse SDK module)
```

## Customizing the Example

### Adjust Audio Sampling

In `prj.conf`:

```ini  theme={"system"}
# Audio configuration
CONFIG_AUDIO=y
CONFIG_AUDIO_DMIC=y

# Sample rate (must match your model)
CONFIG_AUDIO_SAMPLE_RATE_16000=y

# Buffer size
CONFIG_AUDIO_DMIC_BUFFER_SIZE=4096
```

### Change Inference Frequency

In `src/main.cpp`:

```cpp  theme={"system"}
// Run inference every 500ms instead of continuous
#define INFERENCE_INTERVAL_MS 500

static uint32_t last_inference_time = 0;

void loop() {
    uint32_t current_time = k_uptime_get_32();
    
    if (current_time - last_inference_time >= INFERENCE_INTERVAL_MS) {
        run_inference();
        last_inference_time = current_time;
    }
}
```

### Increase Memory for Larger Models

In `prj.conf`:

```ini  theme={"system"}
CONFIG_MAIN_STACK_SIZE=16384
CONFIG_HEAP_MEM_POOL_SIZE=32768
```

### Add Logging

```ini  theme={"system"}
CONFIG_LOG=y
CONFIG_AUDIO_LOG_LEVEL_DBG=y
CONFIG_SENSOR_LOG_LEVEL_DBG=y
```

## Understanding the Code

### Microphone Initialization

```cpp  theme={"system"}
// src/microphone/microphone.cpp
#include <zephyr/audio/dmic.h>

static const struct device *dmic_dev;
static struct dmic_cfg cfg;

int microphone_init(void) {
    dmic_dev = DEVICE_DT_GET(DT_NODELABEL(dmic0));
    
    if (!device_is_ready(dmic_dev)) {
        printk("DMIC device not ready\n");
        return -ENODEV;
    }
    
    // Configure DMIC
    cfg.io.min_pdm_clk_freq = 1000000;  // 1 MHz
    cfg.io.max_pdm_clk_freq = 3500000;  // 3.5 MHz
    cfg.streams[0].pcm_width = 16;
    cfg.streams[0].pcm_rate = 16000;    // 16 kHz
    
    return dmic_configure(dmic_dev, &cfg);
}
```

### Audio Capture

```cpp  theme={"system"}
// src/microphone/microphone.cpp
static int16_t audio_buffer[AUDIO_BUFFER_SIZE];
static size_t buffer_idx = 0;

int microphone_record(int16_t *buffer, size_t length) {
    struct dmic_buf dmic_buffer;
    
    // Start DMIC stream
    dmic_trigger(dmic_dev, DMIC_TRIGGER_START);
    
    while (buffer_idx < length) {
        // Read audio samples
        dmic_read(dmic_dev, 0, &dmic_buffer, WAIT_FOR_BUFFER);
        
        // Copy to buffer
        memcpy(&buffer[buffer_idx], 
               dmic_buffer.data, 
               dmic_buffer.size);
        
        buffer_idx += dmic_buffer.size / sizeof(int16_t);
    }
    
    // Stop DMIC stream
    dmic_trigger(dmic_dev, DMIC_TRIGGER_STOP);
    
    buffer_idx = 0;
    return 0;
}
```

### Inference Integration

```cpp  theme={"system"}
// src/inference/inference.cpp
#include "edge-impulse-sdk/classifier/ei_run_classifier.h"

static float features[EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE];

int run_classifier_continuous(void) {
    // Record audio
    microphone_record(audio_samples, EI_CLASSIFIER_SLICE_SIZE);
    
    // Convert to float features
    for (size_t i = 0; i < EI_CLASSIFIER_SLICE_SIZE; i++) {
        features[i] = (float)audio_samples[i] / 32768.0f;
    }
    
    // Create signal
    signal_t signal;
    signal.total_length = EI_CLASSIFIER_DSP_INPUT_FRAME_SIZE;
    signal.get_data = &get_signal_data;
    
    // Run classifier
    ei_impulse_result_t result = {0};
    EI_IMPULSE_ERROR res = run_classifier(&signal, &result, false);
    
    if (res != EI_IMPULSE_OK) {
        return -1;
    }
    
    // Print results
    print_inference_result(&result);
    
    return 0;
}
```

### Main Loop

```cpp  theme={"system"}
// src/main.cpp
void main(void) {
    printk("Starting microphone inference...\n");
    
    // Initialize microphone
    if (microphone_init() != 0) {
        printk("Failed to initialize microphone\n");
        return;
    }
    
    printk("Microphone initialized\n");
    
    while (1) {
        printk("Recording audio...\n");
        
        // Run inference
        if (run_classifier_continuous() != 0) {
            printk("Inference failed\n");
        }
        
        // Small delay
        k_sleep(K_MSEC(100));
    }
}
```

## Device Tree Configuration

For boards without built-in DMIC, add to your `.overlay` file:

```dts  theme={"system"}
/ {
    dmic_dev: dmic {
        compatible = "nordic,nrf-pdm";
        status = "okay";
        pinctrl-0 = <&pdm_default>;
        pinctrl-names = "default";
        clock-source = "PCLK32M_HFXO";
        
        // Configure pins
        din-gpios = <&gpio0 26 0>;
        clk-gpios = <&gpio0 25 0>;
    };
};

&pinctrl {
    pdm_default: pdm_default {
        group1 {
            psels = <NRF_PSEL(PDM_CLK, 0, 25)>,
                    <NRF_PSEL(PDM_DIN, 0, 26)>;
        };
    };
};
```

## Troubleshooting

<AccordionGroup>
  <Accordion title="Module not found">
    **Cause**: Edge Impulse SDK not fetched

    **Solution**:

    ```bash  theme={"system"}
    west update
    ```
  </Accordion>

  <Accordion title="Insufficient memory">
    **Cause**: Model too large for available RAM

    **Solution**: Increase stack size in `prj.conf`:

    ```ini  theme={"system"}
    CONFIG_MAIN_STACK_SIZE=16384
    CONFIG_HEAP_MEM_POOL_SIZE=32768
    ```

    Or enable EON Compiler when deploying from Studio.
  </Accordion>

  <Accordion title="Microphone not detected">
    **Cause**: DMIC device not configured or pins incorrect

    **Solution**: Enable debug logging:

    ```ini  theme={"system"}
    CONFIG_AUDIO_LOG_LEVEL_DBG=y
    CONFIG_LOG=y
    ```

    Check device tree configuration matches your board's microphone pins.
  </Accordion>

  <Accordion title="Audio quality issues">
    **Causes & Solutions**:

    1. **Wrong sample rate**: Verify `CONFIG_AUDIO_SAMPLE_RATE_16000=y` matches your model
    2. **Buffer underrun**: Increase buffer size:

    ```ini  theme={"system"}
    CONFIG_AUDIO_DMIC_BUFFER_SIZE=8192
    ```

    3. **Clock configuration**: Check PDM clock frequency in device tree
  </Accordion>

  <Accordion title="Poor classification accuracy">
    **Causes & Solutions**:

    1. **Background noise**: Train model with noise samples
    2. **Microphone gain**: Adjust in device tree:

    ```dts  theme={"system"}
    dmic_dev: dmic {
        gain-left = <20>;   // Increase gain
        gain-right = <20>;
    };
    ```

    3. **Sample rate mismatch**: Ensure DMIC sample rate matches training data
  </Accordion>
</AccordionGroup>

## Using in Your Own Project

### Option 1: Add to Existing Zephyr Project

Update your `west.yml`:

```yaml  theme={"system"}
manifest:
  projects:
    - name: edge-impulse-sdk-zephyr
      path: modules/edge-impulse-sdk-zephyr
      revision: v1.80.0  # See https://github.com/edgeimpulse/edge-impulse-sdk-zephyr/tags
      url: https://github.com/edgeimpulse/edge-impulse-sdk-zephyr
```

Then:

```bash  theme={"system"}
west update
```

Add to your `CMakeLists.txt`:

```cmake  theme={"system"}
list(APPEND ZEPHYR_EXTRA_MODULES ${CMAKE_CURRENT_SOURCE_DIR}/model)
```

### Option 2: Clone This Repository

```bash  theme={"system"}
git clone https://github.com/edgeimpulse/ei-zephyr-mic-kws-inference.git
cd ei-zephyr-mic-kws-inference
west init --local .
west update
```

## Advanced Features

### Voice Activity Detection (VAD)

Only run inference when speech is detected:

```cpp  theme={"system"}
bool has_voice_activity(int16_t *samples, size_t length) {
    int64_t energy = 0;
    
    for (size_t i = 0; i < length; i++) {
        energy += (int64_t)samples[i] * samples[i];
    }
    
    energy /= length;
    
    return energy > VAD_THRESHOLD;
}

void main(void) {
    while (1) {
        microphone_record(audio_samples, BUFFER_SIZE);
        
        if (has_voice_activity(audio_samples, BUFFER_SIZE)) {
            run_classifier_continuous();
        }
    }
}
```

### Continuous Sliding Window

```cpp  theme={"system"}
#define WINDOW_SIZE 16000      // 1 second at 16kHz
#define SLIDE_SIZE 8000        // 0.5 second slide

static int16_t ring_buffer[WINDOW_SIZE];
static size_t buffer_pos = 0;

void sliding_window_inference(void) {
    // Record new samples
    microphone_record(&ring_buffer[buffer_pos], SLIDE_SIZE);
    
    // Update position
    buffer_pos = (buffer_pos + SLIDE_SIZE) % WINDOW_SIZE;
    
    // Run inference on full window
    run_inference(ring_buffer, WINDOW_SIZE);
}
```

### Wake Word Detection

```cpp  theme={"system"}
static bool wake_word_detected = false;
static const char* wake_word = "hey_device";

void process_classification(ei_impulse_result_t *result) {
    for (size_t i = 0; i < EI_CLASSIFIER_LABEL_COUNT; i++) {
        if (strcmp(result->classification[i].label, wake_word) == 0 &&
            result->classification[i].value > 0.8f) {
            
            wake_word_detected = true;
            printk("Wake word detected!\n");
            
            // Start listening for command
            start_command_mode();
        }
    }
}
```

## Performance Optimization

### Reduce Power Consumption

```ini  theme={"system"}
# In prj.conf
CONFIG_PM=y                           # Enable power management
CONFIG_PM_DEVICE=y                    # Device runtime PM
CONFIG_PM_DEVICE_RUNTIME=y

# Put microphone to sleep when idle
CONFIG_PM_DEVICE_RUNTIME_EXCLUSIVE=y
```

### Use DMA for Audio Transfer

```ini  theme={"system"}
CONFIG_DMA=y
CONFIG_AUDIO_DMIC_USE_DMA=y
```

### Optimize for Size

```ini  theme={"system"}
CONFIG_SIZE_OPTIMIZATIONS=y
CONFIG_COMPILER_OPT="-Os"
```

## Next Steps

<CardGroup cols={2}>
  <Card title="IMU Inference" icon="rotate" href="/tutorials/topics/zephyr/zephyr-module-imu">
    Add motion recognition
  </Card>

  <Card title="Porting Between Boards" icon="arrows-rotate" href="/tutorials/topics/zephyr/porting-between-boards">
    Deploy to different hardware
  </Card>
</CardGroup>

## Additional Resources

* [GitHub: ei-zephyr-mic-kws-inference](https://github.com/edgeimpulse/ei-zephyr-mic-kws-inference)
* [Zephyr Audio Documentation](https://docs.zephyrproject.org/latest/hardware/peripherals/audio/index.html)
* [Keyword Spotting Tutorial](/tutorials/end-to-end/keyword-spotting)
* [Edge Impulse Forum](https://forum.edgeimpulse.com/)

## Summary

You now have microphone-based keyword spotting running on Zephyr! The Edge Impulse Zephyr Module handles:

* Audio capture from PDM microphones
* Continuous inference pipeline
* Model integration
* Memory management

Focus on building your application logic while the module handles the ML complexity.

For more information:

* [Edge Impulse Forum](https://forum.edgeimpulse.com/)
* [GitHub Issues](https://github.com/edgeimpulse/ei-zephyr-mic-kws-inference/issues)
* [Zephyr Project](https://zephyrproject.org/)


Built with [Mintlify](https://mintlify.com).