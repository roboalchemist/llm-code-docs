# Source: https://docs.edgeimpulse.com/studio/projects/processing-blocks/blocks/hr-hrv.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# HR/HRV

<Info>
  **Enterprise deployment only**

  All Edge Impulse developers can access this feature for evaluation purposes. However, deployment of this feature to an edge device is only available for enterprise users. If you are an enterprise user, please contact your Solutions Engineer for deployment options.
</Info>

The **HR/HRV Features** block processes physiological signals like photoplethysmogram (PPG) or electrocardiogram (ECG), with optional accelerometer inputs for enhanced accuracy in motion-prone applications, to extract key metrics such as heart rate (HR) and heart rate variability (HRV). HR measures the number of beats per minute, while HRV measures the time variance between successive heartbeats, also known as the interbeat interval (IBI).

The block offers real-time HR estimation and HRV analysis on resource-constrained edge devices and leverages cutting-edge algorithms for precise feature extraction. The extracted features can be used on their own or to inform downstream machine learning tasks such as stress detection or heart health analysis.

To see a demonstration of how to use the HR/HRV Features block, refer to our tutorial: [Processing PPG input with HR/HRV Features Block](/tutorials/end-to-end/hr-hrv-estimation).

<Frame caption="HR/HRV features processing block configuration">
  <img src="https://mintcdn.com/edgeimpulse/C0SzOGcUNl7GskyL/.assets/images/hr-hrv-features-config.png?fit=max&auto=format&n=C0SzOGcUNl7GskyL&q=85&s=eb84dd8192c24d055b90d82e76dcbefd" width="1490" height="1000" data-path=".assets/images/hr-hrv-features-config.png" />
</Frame>

## Configuration

<Info>
  **Tip**: Use accelerometer data whenever possible to enhance the accuracy of heart rate and HRV estimation in dynamic environments.
</Info>

By configuring the HR/HRV Features block, you can obtain critical metrics like heart rate and HRV in real-time, enabling applications such as fitness tracking, stress monitoring, and health diagnostics. The extracted features can be fine-tuned to match the performance and constraints of edge devices, ensuring both efficiency and accuracy.

<Frame caption="HR/HRV features processing block impulse configuration">
  <img src="https://mintcdn.com/edgeimpulse/C0SzOGcUNl7GskyL/.assets/images/hr-hrv-features-impulse.png?fit=max&auto=format&n=C0SzOGcUNl7GskyL&q=85&s=a5c8b419a20f8058af8a3e5190baa9ed" width="1600" height="745" data-path=".assets/images/hr-hrv-features-impulse.png" />
</Frame>

### Input block

When using the HR/HRV Features block, it is important to also configure the input block for your impulse appropriately.

#### Window size

There are minimum input block window size requirements depending on your configuration of the HR/HRV Features block. If you are using HRV features, the input block window size must be greater than or equal to the HRV update interval. If you are not using HRV features, the input block window size must be greater than or equal to 2 seconds.

The minimum window size of 2 seconds is determined by the fact that the heart rate calculation is performed once for every 2 second period. When the window size is increased beyond 2 seconds, more heart rate values will be provided to the learning block. For example, a 2 second window will pass 1 heart rate value per window whereas a 10 second window will pass 5 heart rate values per window.

#### Window increase (stride)

For optimal performance, it is recommended to set the window increase (stride) equal to the window size.

#### Frequency (Hz)

All input signals (PPG or ECG, and accelerometer) must have a frequency of either 25 Hz (tolerance +/- 1 Hz) or 50 Hz (tolerance +/- 3 Hz).

### Selecting features passed to learning block

Heart rate values, HRV features, or both can be passed to the learning block. To only send heart rate values, select `none` for the HRV features parameter. To send only HRV features, select your desired HRV features parameter value (other than `none`) and deselect the include calculated heart rates parameter. To send both heart rate values and HRV features, select your desired HRV features parameter value (other than `none`) and select the include calculated heart rates parameter.

### Parameter definitions

<Info>
  **Compatible with the DSP Autotuner**

  Picking the right parameters for DSP algorithms can be difficult. It often requires a lot of experience and experimenting. The autotuning function makes this process easier by recommending a set of parameters that is tuned for your dataset.
</Info>

The following parameters are available for configuring the HR/HRV Features block. Note that all heart rate and accelerometer settings can be estimated using the autotuning of parameters, and is the suggested approach.

<Frame caption="HR/HRV features processing block parameters">
  <img src="https://mintcdn.com/edgeimpulse/C0SzOGcUNl7GskyL/.assets/images/hr-hrv-features-parameters.png?fit=max&auto=format&n=C0SzOGcUNl7GskyL&q=85&s=8645147748f5a36deb6b96d97e2bcc14" width="830" height="690" data-path=".assets/images/hr-hrv-features-parameters.png" />
</Frame>

#### Heart rate settings

| Parameter          | Description                                                                                                                          |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Filter preset**  | Sets the aggressiveness of the input signal filter.                                                                                  |
| **HR window size** | The signal history used when calculating the heart rate. The larger the value, the smoother and more averaged the heart rate values. |

#### Accelerometer settings

| Parameter                                    | Description                                                                                                                                                                              |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Sensitivity**                              | The sensitivity to motion artifacts.                                                                                                                                                     |
| **Accelerometer signal level while resting** | The sum of the standard deviation of all three axes; the accelerometer noise floor. The value is dependent on hardware design, yet can be estimated from the signal using the autotuner. |

#### HRV settings

| Parameter                                              | Description                                                                                                                                                                                               |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **HRV features**                                       | The group of HRV features to use.                                                                                                                                                                         |
| **Include calculated heart rates in classifier input** | Whether or not to include heart rate values in addition to HRV features.                                                                                                                                  |
| **HRV update interval**                                | How often new HRV features are calculated. Typically a fraction of the input block window size, e.g. 30 seconds update interval for a 90 seconds input window size.                                       |
| **HRV window size**                                    | The signal history used when calculating the HRV features. The larger the value, the smoother and more averaged the HRV features. There are minimums based on the HRV features group selected, see below. |

### Minimum HRV window sizes

| HRV Features Group | Min. HRV Window Size (s) |
| ------------------ | ------------------------ |
| `none`             | N/A                      |
| `rmssd`            | 10                       |
| `time-domain`      | 30                       |
| `all`              | 90                       |

## Outputs

The HR/HRV Features block outputs heart rate values and HRV features based on your configuration. The HRV features contain time-domain and frequency-domain features as shown below.

**Heart rate**

* Heart Rate Values

**HRV time-domain features**

* IBI Slope
* HR Mean
* HR Slope
* RMSSD Slope
* RMSSD
* AVNN
* SDNN
* Range NN
* MAD NN
* pNN50
* NN Percentile (10)
* NN Percentile (25)
* NN Percentile (75)
* NN Percentile (90)
* IQR
* SDSD
* SD1
* SD2
* SD2/SD1 Ratio

**HRV frequency-domain features**

* Raw VLF Energy
* Raw LF Energy
* Raw HF Energy
* Raw Total Energy
* Relative VLF Energy
* Relative LF Energy
* Relative HF Energy
* LF/HF Ratio
* Peak VLF Energy
* Peak LF Energy
* Peak HF Energy

### HRV features groups

Instead of individually selecting the HRV features that are output, you can select a group that contains multiple features. The HRV features associated with each group are defined below.

| HRV Features Group | Features Included                |
| ------------------ | -------------------------------- |
| `none`             | None                             |
| `rmssd`            | RMSSD                            |
| `time-domain`      | Time-domain                      |
| `all`              | Time-domain and frequency-domain |

### Number of processed features

The number of processed features will depend on your configuration of the input block and HR/HRV Features block. For example if you have an input window of 90 seconds, selected `all` for the HRV features group (30 features), enabled including heart rate values being passed to the learning block, and have an HRV update interval of 30 seconds, there will be 135 processed features - 45 heart rate values (90 seconds input window / 2 seconds per heart rate value) and 90 HRV features (90 seconds input window / 30 seconds update interval x 30 features).

## Deployment

<Info>
  If you are an Enterprise customer, please contact your Solutions Engineer to enable deployment.
</Info>

The HR/HRV Features block has industry leading efficiency for RAM and flash usage and can be deployed into a wide range of devices, including fitness trackers, health monitors, and stress detection systems. The functionality can be deployed either as C++ or C bindings.

### Optimizing for MCU-based deployments

To optimize for MCU-based systems, your enterprise representative can provide a MAP file. This file contains a detailed breakdown of the memory footprint (flash and RAM) for the HR/HRV Features block, including the IBI processing components. This data is critical for fine-tuning and optimizing the deployment of the block on resource-constrained devices.

## Examples

### Accessing heart rate values at runtime

One important note when working with the HR/HRV Features block is that you can extract heart rate values even when running a classifier. This is particularly useful if your model is performing classification tasks but you'd also like to access heart rate data. The code snippet below demonstrates how to access the heart rate information during inference and print the results in a C++ application.

```cpp  theme={"system"}
#include "edge-impulse-sdk/classifier/ei_run_classifier.h"

int main() {
    // Initialize signal (PPG data, etc.)
    signal_t signal;
    ei_impulse_result_t result;

    // Run the classifier and print the results
    run_classifier(&signal, &result, false);
    printf("Heart rate: %.2f BPM\n", results.hr_calcs.heart_rate);

    return 0;
}
```

### Outputting heart rate values without classification

If you want to use the HR/HRV Features block solely for heart rate values without any classification in Studio, you can configure a regression learning block to "pass through" the result. This can be achieved by using expert mode for the block to set up a simple neural network.

```python  theme={"system"}
import tensorflow as tf

# Example: Setting up a basic HR model in Edge Impulse
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.InputLayer(input_shape=1))
model.add(tf.keras.layers.Dense(1, name='y_pred', activation='linear'))

```

After saving and training the model (though there's effectively no training needed in this case), you can then use Model Testing or Live Classification to evaluate the heart rate estimation.

If you also would like to deploy the HR/HRV Features block without running a classifier on device, when compiling define the following macro via CMake or Makefile to avoid flash overhead for the unused learn block.

```cpp  theme={"system"}
#define EI_CLASSIFIER_DSP_ONLY 1
```

### Minimizing RAM Usage

When running classifiers that make use of a large window size, such as for HRV features, you can avoid buffering the entire window of PPG or ECG data by leveraging the callback structure of signal\_t. `get_data()` will only ask for 2 seconds of samples on each invocation, so if you block (either via RTOS sleep or a while loop on bare metal) while waiting for each 2 seconds of PPG or ECG data, you can avoid allocating the entire input window. Note also that the SDK does not internally buffer the entire window; each 2 seconds is immediately processed down to IBIs.

```cpp  theme={"system"}
// Callback: fill a section of the out_ptr buffer when requested
static int get_signal_data(size_t offset, size_t length, float *out_ptr) {
    // Zephyr RTOS, for instance
    k_sem_take(&ppg_2s_data_ready_sem, K_FOREVER);
    for (size_t i = 0; i < length; i++) {
        out_ptr[i] = ppg_buffer[i]; // don't need offset b/c we're filling in realtime
    }
    k_sem_give(&ppg_2s_data_ready_sem);

    return EIDSP_OK;
}
```

## Conclusion

The **HR/HRV Features** block enables real-time extraction of key metrics such as heart rate and heart rate variability from physiological signals like PPG or ECG. These metrics are critical for applications in fitness tracking, stress detection, and medical diagnostics. To go further, follow our step-by-step guides in the tutorials section.


Built with [Mintlify](https://mintlify.com).