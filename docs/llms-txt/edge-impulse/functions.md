# Source: https://docs.edgeimpulse.com/tools/libraries/sdks/inference/cpp/functions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Functions

Public-facing functions for running inference using the Edge Impulse C++ library.

**Source**: [classifier/ei\_run\_classifier.h](https://github.com/edgeimpulse/inferencing-sdk-cpp/blob/master/classifier/ei_run_classifier.h)

## run\_classifier\_init

```cpp  theme={"system"}
public void run_classifier_init(
    void
)
```

**Brief**: Initialize static variables for running preprocessing and inference continuously.

**Description**:
Initializes and clears any internal static variables needed by `run_classifier_continuous()`. This includes the moving average filter (MAF). This function should be called prior to calling `run_classifier_continuous()`.

**Blocking**: yes

**Example**: [nano\_ble33\_sense\_microphone\_continuous.ino](https://github.com/edgeimpulse/example-lacuna-ls200/blob/main/nano_ble33_sense_microphone_continous/nano_ble33_sense_microphone_continuous.ino)

## run\_classifier\_init

```cpp  theme={"system"}
public void run_classifier_init(
    ei_impulse_handle_t * handle
)
```

**Brief**: Initialize static variables for running preprocessing and inference continuously.

**Description**:
Initializes and clears any internal static variables needed by `run_classifier_continuous()`. This includes the moving average filter (MAF). This function should be called prior to calling `run_classifier_continuous()`.

**Blocking**: yes

**Example**: [nano\_ble33\_sense\_microphone\_continuous.ino](https://github.com/edgeimpulse/example-lacuna-ls200/blob/main/nano_ble33_sense_microphone_continous/nano_ble33_sense_microphone_continuous.ino)

#### Parameters

* `handle` struct with information about model and DSP

## run\_classifier\_deinit

```cpp  theme={"system"}
public void run_classifier_deinit(
    void
)
```

**Brief**: Deletes static variables when running preprocessing and inference continuously.

**Description**:
Deletes internal static variables used by `run_classifier_continuous()`, which includes the moving average filter (MAF). This function should be called when you are done running continuous classification.

**Blocking**: yes

**Example**: [ei\_run\_audio\_impulse.cpp](https://github.com/edgeimpulse/firmware-nordic-thingy53/blob/main/src/inference/ei_run_audio_impulse.cpp)

## run\_classifier\_continuous

```cpp  theme={"system"}
public EI_IMPULSE_ERROR run_classifier_continuous(
    signal_t * signal,
    ei_impulse_result_t * result,
    bool debug,
    bool enable_maf
)
```

**Brief**: Run preprocessing (DSP) on new slice of raw features. Add output features to rolling matrix and run inference on full sample.

**Description**:
Accepts a new slice of features give by the callback defined in the `signal` parameter. It performs preprocessing (DSP) on this new slice of features and appends the output to a sliding window of pre-processed features (stored in a static features matrix). The matrix stores the new slice and as many old slices as necessary to make up one full sample for performing inference.

`run_classifier_init()` must be called before making any calls to `run_classifier_continuous().`

For example, if you are doing keyword spotting on 1-second slices of audio and you want to perform inference 4 times per second (given by `EI_CLASSIFIER_SLICES_PER_MODEL_WINDOW`), you would collect 0.25 seconds of audio and call run\_classifier\_continuous(). The function would compute the Mel-Frequency Cepstral Coefficients (MFCCs) for that 0.25 second slice of audio, drop the oldest 0.25 seconds' worth of MFCCs from its internal matrix, and append the newest slice of MFCCs. This process allows the library to keep track of the pre-processed features (e.g. MFCCs) in the window instead of the entire set of raw features (e.g. raw audio data), which can potentially save a lot of space in RAM. After updating the static matrix, inference is performed using the whole matrix, which acts as a sliding window of pre-processed features.

Additionally, a moving average filter (MAF) can be enabled for `run_classifier_continuous()`, which averages (arithmetic mean) the last *n* inference results for each class. *n* is `EI_CLASSIFIER_SLICES_PER_MODEL_WINDOW / 2`. In our example above, if we enabled the MAF, the values in `result` would contain predictions averaged from the previous 2 inferences.

To learn more about `run_classifier_continuous()`, see [this guide](/tutorials/topics/inference/sample-audio-continuously) on continuous audio sampling. While the guide is written for audio signals, the concepts of continuous sampling and inference can be extrapolated to any time-series data.

**Blocking**: yes

**Example**: [nano\_ble33\_sense\_microphone\_continuous.ino](https://github.com/edgeimpulse/example-lacuna-ls200/blob/main/nano_ble33_sense_microphone_continous/nano_ble33_sense_microphone_continuous.ino)

#### Parameters

* `signal` Pointer to a signal\_t struct that contains the number of elements in the slice of raw features (e.g. `EI_CLASSIFIER_SLICE_SIZE`) and a pointer to a callback that reads in the slice of raw features.

* `result` Pointer to an `ei_impulse_result_t` struct that contains the various output results from inference after run\_classifier() returns.

* `debug` Print internal preprocessing and inference debugging information via `ei_printf()`.

* `enable_maf` Enable the moving average filter (MAF) for the classifier.

#### Returns

Error code as defined by `EI_IMPULSE_ERROR` enum. Will be `EI_IMPULSE_OK` if inference completed successfully.

## run\_classifier\_continuous

```cpp  theme={"system"}
public EI_IMPULSE_ERROR run_classifier_continuous(
    ei_impulse_handle_t * impulse,
    signal_t * signal,
    ei_impulse_result_t * result,
    bool debug,
    bool enable_maf
)
```

**Brief**: Run preprocessing (DSP) on new slice of raw features. Add output features to rolling matrix and run inference on full sample.

**Description**:
Accepts a new slice of features give by the callback defined in the `signal` parameter. It performs preprocessing (DSP) on this new slice of features and appends the output to a sliding window of pre-processed features (stored in a static features matrix). The matrix stores the new slice and as many old slices as necessary to make up one full sample for performing inference.

`run_classifier_init()` must be called before making any calls to `run_classifier_continuous().`

For example, if you are doing keyword spotting on 1-second slices of audio and you want to perform inference 4 times per second (given by `EI_CLASSIFIER_SLICES_PER_MODEL_WINDOW`), you would collect 0.25 seconds of audio and call run\_classifier\_continuous(). The function would compute the Mel-Frequency Cepstral Coefficients (MFCCs) for that 0.25 second slice of audio, drop the oldest 0.25 seconds' worth of MFCCs from its internal matrix, and append the newest slice of MFCCs. This process allows the library to keep track of the pre-processed features (e.g. MFCCs) in the window instead of the entire set of raw features (e.g. raw audio data), which can potentially save a lot of space in RAM. After updating the static matrix, inference is performed using the whole matrix, which acts as a sliding window of pre-processed features.

Additionally, a moving average filter (MAF) can be enabled for `run_classifier_continuous()`, which averages (arithmetic mean) the last *n* inference results for each class. *n* is `EI_CLASSIFIER_SLICES_PER_MODEL_WINDOW / 2`. In our example above, if we enabled the MAF, the values in `result` would contain predictions averaged from the previous 2 inferences.

To learn more about `run_classifier_continuous()`, see [this guide](/tutorials/topics/inference/sample-audio-continuously) on continuous audio sampling. While the guide is written for audio signals, the concepts of continuous sampling and inference can be extrapolated to any time-series data.

**Blocking**: yes

**Example**: [nano\_ble33\_sense\_microphone\_continuous.ino](https://github.com/edgeimpulse/example-lacuna-ls200/blob/main/nano_ble33_sense_microphone_continous/nano_ble33_sense_microphone_continuous.ino)

#### Parameters

* `impulse` `ei_impulse_handle_t` struct with information about preprocessing and model.

* `signal` Pointer to a signal\_t struct that contains the number of elements in the slice of raw features (e.g. `EI_CLASSIFIER_SLICE_SIZE`) and a pointer to a callback that reads in the slice of raw features.

* `result` Pointer to an `ei_impulse_result_t` struct that contains the various output results from inference after run\_classifier() returns.

* `debug` Print internal preprocessing and inference debugging information via `ei_printf()`.

* `enable_maf` Enable the moving average filter (MAF) for the classifier.

#### Returns

Error code as defined by `EI_IMPULSE_ERROR` enum. Will be `EI_IMPULSE_OK` if inference completed successfully.

## run\_classifier

```cpp  theme={"system"}
public EI_IMPULSE_ERROR run_classifier(
    signal_t * signal,
    ei_impulse_result_t * result,
    bool debug
)
```

**Brief**: Run the classifier over a raw features array.

**Description**:
Overloaded function [run\_classifier()](/tools/libraries/sdks/inference/cpp/functions#run-classifier) that defaults to the single impulse.

**Blocking**: yes

#### Parameters

* `signal` Pointer to a `signal_t` struct that contains the total length of the raw feature array, which must match EI\_CLASSIFIER\_DSP\_INPUT\_FRAME\_SIZE, and a pointer to a callback that reads in the raw features.

* `result` Pointer to an ei\_impulse\_result\_t struct that will contain the various output results from inference after `run_classifier()` returns.

* `debug` Print internal preprocessing and inference debugging information via `ei_printf()`.

#### Returns

Error code as defined by `EI_IMPULSE_ERROR` enum. Will be `EI_IMPULSE_OK` if inference completed successfully.

## run\_classifier

```cpp  theme={"system"}
public EI_IMPULSE_ERROR run_classifier(
    ei_impulse_handle_t * impulse,
    signal_t * signal,
    ei_impulse_result_t * result,
    bool debug
)
```

**Brief**: Run the classifier over a raw features array.

**Description**:
Accepts a `signal_t` input struct pointing to a callback that reads in pages of raw features. `run_classifier()` performs any necessary preprocessing on the raw features (e.g. DSP, cropping of images, etc.) before performing inference. Results from inference are stored in an `ei_impulse_result_t` struct.

**Blocking**: yes

**Example**: [standalone inferencing main.cpp](https://github.com/edgeimpulse/example-standalone-inferencing/blob/master/source/main.cpp)

#### Parameters

* `impulse` Pointer to an `ei_impulse_handle_t` struct that contains the model and preprocessing information.

* `signal` Pointer to a `signal_t` struct that contains the total length of the raw feature array, which must match EI\_CLASSIFIER\_DSP\_INPUT\_FRAME\_SIZE, and a pointer to a callback that reads in the raw features.

* `result` Pointer to an ei\_impulse\_result\_t struct that will contain the various output results from inference after `run_classifier()` returns.

* `debug` Print internal preprocessing and inference debugging information via `ei_printf()`.

#### Returns

Error code as defined by `EI_IMPULSE_ERROR` enum. Will be `EI_IMPULSE_OK` if inference completed successfully.


Built with [Mintlify](https://mintlify.com).