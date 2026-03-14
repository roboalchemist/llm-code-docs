# Source: https://docs.edgeimpulse.com/tools/libraries/sdks/inference/cpp/structs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Structs

Public-facing structs for Edge Impulse C++ SDK.

## ei\_impulse\_result\_classification\_t

```cpp  theme={"system"}
struct ei_impulse_result_classification_t
```

Holds the output of inference, anomaly results, and timing information.

`ei_impulse_result_t` holds the output of `run_classifier()`. If object detection is enabled, then the output results is a pointer to an array of bounding boxes of size `bounding_boxes_count`, as given by [ei\_impulse\_result\_bounding\_box\_t](/tools/libraries/sdks/inference/cpp/structs#ei-impulse-result-bounding-boxt). Otherwise, results are stored as an array of classification scores, as given by [ei\_impulse\_result\_classification\_t](/tools/libraries/sdks/inference/cpp/structs#ei-impulse-result-classificationt).

If anomaly detection is enabled (e.g. `EI_CLASSIFIER_HAS_ANOMALY == 1`), then the anomaly score will be stored as a floating point value in `anomaly`.

Timing information is stored in an [ei\_impulse\_result\_timing\_t](/tools/libraries/sdks/inference/cpp/structs#ei-impulse-result-timingt) struct.

**Source**: [classifier/ei\_classifier\_types.h](https://github.com/edgeimpulse/inferencing-sdk-cpp/blob/master/classifier/ei_classifier_types.h)

**Example**: [standalone inferencing main.cpp](https://github.com/edgeimpulse/example-standalone-inferencing/blob/master/source/main.cpp)

| Member                      | Description                  |
| --------------------------- | ---------------------------- |
| `public const char * label` | Label of the detected object |
| `public float value`        | Value of the detected object |

## ei\_impulse\_visual\_ad\_result\_t

```cpp  theme={"system"}
struct ei_impulse_visual_ad_result_t
```

Holds the output of visual anomaly detection (FOMO-AD)

If visual anomaly detection is enabled (e.g. `EI_CLASSIFIER_HAS_VISUAL_ANOMALY == 1`), then the output results will be a pointer to an array of grid cells of size `visual_ad_count`, as given by [ei\_impulse\_result\_bounding\_box\_t](/tools/libraries/sdks/inference/cpp/structs#ei-impulse-result-bounding-boxt).

The visual anomaly detection result is stored in `visual_ad_result`, which contains the mean and max values of the grid cells.

**Source**: [classifier/ei\_classifier\_types.h](https://github.com/edgeimpulse/inferencing-sdk-cpp/blob/master/classifier/ei_classifier_types.h)

**Example**: [standalone inferencing main.cpp](https://github.com/edgeimpulse/example-standalone-inferencing/blob/master/source/main.cpp)

| Member                    | Description                  |
| ------------------------- | ---------------------------- |
| `public float mean_value` | Mean value of the grid cells |
| `public float max_value`  | Max value of the grid cells  |

## ei\_impulse\_result\_bounding\_box\_t

```cpp  theme={"system"}
struct ei_impulse_result_bounding_box_t
```

Holds information for a single bounding box.

If object detection is enabled (i.e. `EI_CLASSIFIER_OBJECT_DETECTION == 1`), then inference results will be one or more bounding boxes. The bounding boxes with the highest confidence scores (assuming those scores are equal to or greater than `EI_CLASSIFIER_OBJECT_DETECTION_THRESHOLD`), given by the `value` member, are returned from inference. The total number of bounding boxes returned will be at least `EI_CLASSIFIER_OBJECT_DETECTION_COUNT`. The exact number of bounding boxes is stored in `bounding_boxes_count` field of \[ei\_impulse\_result\_t]/C++ Inference SDK Library/structs/ei\_impulse\_result\_t.md).

A bounding box is a rectangle that ideally surrounds the identified object. The (`x`, `y`) coordinates in the struct identify the top-left corner of the box. `label` is the predicted class with the highest confidence score. `value` is the confidence score between \[0.0..1.0] of the given `label`.

**Source**: [classifier/ei\_classifier\_types.h](https://github.com/edgeimpulse/inferencing-sdk-cpp/blob/master/classifier/ei_classifier_types.h)

**Example**: [standalone inferencing main.cpp](https://github.com/edgeimpulse/example-standalone-inferencing/blob/master/source/main.cpp)

| Member                      | Description                                                                                                                                                         |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `public const char * label` | Pointer to a character array describing the associated class of the given bounding box. Taken from one of the elements of `ei_classifier_inferencing_categories[]`. |
| `public uint32_t x`         | x coordinate of the top-left corner of the bounding box                                                                                                             |
| `public uint32_t y`         | y coordinate of the top-left corner of the bounding box                                                                                                             |
| `public uint32_t width`     | Width of the bounding box                                                                                                                                           |
| `public uint32_t height`    | Height of the bounding box                                                                                                                                          |
| `public float value`        | Confidence score of the label describing the bounding box                                                                                                           |

## ei\_impulse\_result\_timing\_t

```cpp  theme={"system"}
struct ei_impulse_result_timing_t
```

Holds timing information about the processing (DSP) and inference blocks.

Records timing information during the execution of the preprocessing (DSP) and inference blocks. Can be used to determine if inference will meet timing requirements on your particular platform.

**Source**: [classifier/ei\_classifier\_types.h](https://github.com/edgeimpulse/inferencing-sdk-cpp/blob/master/classifier/ei_classifier_types.h)

**Example**: [standalone inferencing main.cpp](https://github.com/edgeimpulse/example-standalone-inferencing/blob/master/source/main.cpp)

| Member                             | Description                                                                                                                                                           |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `public int sampling`              | If using `run_impulse()` to perform sampling and inference, it is the amount of time (in milliseconds) it took to fetch raw samples. Not used for `run_classifier()`. |
| `public int dsp`                   | Amount of time (in milliseconds) it took to run the preprocessing (DSP) block                                                                                         |
| `public int classification`        | Amount of time (in milliseconds) it took to run the inference block                                                                                                   |
| `public int anomaly`               | Amount of time (in milliseconds) it took to run anomaly detection. Valid only if `EI_CLASSIFIER_HAS_ANOMALY == 1`.                                                    |
| `public int64_t dsp_us`            | Amount of time (in milliseconds) it took to run the post-processing block                                                                                             |
| `public int64_t classification_us` | Amount of time (in milliseconds) it took to run the inference block                                                                                                   |
| `public int64_t anomaly_us`        | Amount of time (in microseconds) it took to run anomaly detection. Valid only if `EI_CLASSIFIER_HAS_ANOMALY == 1`.                                                    |

## ei\_impulse\_result\_t

```cpp  theme={"system"}
struct ei_impulse_result_t
```

Holds the output of inference, anomaly results, and timing information.

`ei_impulse_result_t` holds the output of `run_classifier()`. If object detection is enabled (e.g. `EI_CLASSIFIER_OBJECT_DETECTION == 1`), then the output results is a pointer to an array of bounding boxes of size `bounding_boxes_count`, as given by [ei\_impulse\_result\_bounding\_box\_t](/tools/libraries/sdks/inference/cpp/structs#ei-impulse-result-bounding-boxt). Otherwise, results are stored as an array of classification scores, as given by [ei\_impulse\_result\_classification\_t](/tools/libraries/sdks/inference/cpp/structs#ei-impulse-result-classificationt).

If anomaly detection is enabled (e.g. `EI_CLASSIFIER_HAS_ANOMALY == 1`), then the anomaly score will be stored as a floating point value in `anomaly`.

Timing information is stored in an [ei\_impulse\_result\_timing\_t](/tools/libraries/sdks/inference/cpp/structs#ei-impulse-result-timingt) struct.

**Source**: [classifier/ei\_classifier\_types.h](https://github.com/edgeimpulse/inferencing-sdk-cpp/blob/master/classifier/ei_classifier_types.h)

**Example**: [standalone inferencing main.cpp](https://github.com/edgeimpulse/example-standalone-inferencing/blob/master/source/main.cpp)

| Member                                                           | Description                                                                                                                                                                                                              |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `public ei_impulse_result_bounding_box_t * bounding_boxes`       | Array of bounding boxes of the detected objects, if object detection is enabled.                                                                                                                                         |
| `public uint32_t bounding_boxes_count`                           | Number of bounding boxes detected. If object detection is not enabled, this will be 0.                                                                                                                                   |
| `public ei_impulse_result_classification_t classification`       | Array of classification results. If object detection is enabled, this will be empty.                                                                                                                                     |
| `public float anomaly`                                           | Anomaly score. If anomaly detection is not enabled, this will be 0. A higher anomaly score indicates greater likelihood of an anomalous sample (e.g. it is farther away from its cluster).                               |
| `public ei_impulse_result_timing_t timing`                       | Timing information for the processing (DSP) and inference blocks.                                                                                                                                                        |
| `public bool copy_output`                                        | Copy the output data to a buffer. If set to false, the output data will be returned as a pointer to the internal buffer. If set to true, the output data will be copied to the buffer provided in `ei_impulse_output_t`. |
| `public ei_impulse_result_bounding_box_t * visual_ad_grid_cells` | Array of grid cells of the detected visual anomalies, if visual anomaly detection is enabled.                                                                                                                            |
| `public uint32_t visual_ad_count`                                | Number of grid cells detected as visual anomalies, if visual anomaly detection is enabled.                                                                                                                               |
| `public ei_impulse_visual_ad_result_t visual_ad_result`          | Visual anomaly detection result, if visual anomaly detection is enabled.                                                                                                                                                 |

## ei\_signal\_t

```cpp  theme={"system"}
struct ei_signal_t
```

Holds the callback pointer for retrieving raw data and the length of data to be retrieved.

Holds the callback function, `get_data(size_t offset, size_t length, float *out_ptr)`. This callback should be implemented by the user and fills the memory location given by `*out_ptr` with raw features. Features must be flattened to a 1-dimensional vector, as described in [this guide](/hardware/deployments/run-cpp#signal-structure).

`get_data()` may be called multiple times during preprocessing or inference (e.g. during execution of [run\_classifier()](/tools/libraries/sdks/inference/cpp/functions#run-classifier) or [run\_classifier\_continuous()](/tools/libraries/sdks/inference/cpp/functions#run-classifier-continuous)). The `offset` argument will update to point to new data, and `length` data must be copied into the location specified by `out_ptr`. This scheme allows raw features to be stored in RAM or flash memory and paged in as necessary.

Note that `get_data()` (even after multiple calls during a single execution of `run_classifier()` or `run_classifier_continuous()`) will never request more than a total number of features as given by `total_length`.

**Source**: [dsp/numpy\_types.h](https://github.com/edgeimpulse/inferencing-sdk-cpp/blob/master/dsp/numpy_types.h)

**Example**: [standalone inferencing main.cpp](https://github.com/edgeimpulse/example-standalone-inferencing/blob/master/source/main.cpp)

| Member                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `public std::function< int(size_t offset, size_t length, float *out_ptr)> get_data` | Callback function to be implemented by the user. Parameters are given as `get_data(size_t offset, size_t length, float *out_ptr)` and should return an int (e.g. `EIDSP_OK` if copying completed successfully). No bytes will be requested outside of the `total_length`. Callback parameters: <br />`offset`: The offset in the signal <br />`length`: The number of samples to write into `out_ptr`<br />`out_ptr`: An out buffer to set the signal data <br /> |
| `public size_t total_length`                                                        | Total number of samples the user will provide (via get\_data). This value should match either the total number of raw features required for a full window (ie, the window size in Studio, but in samples), OR, if using run\_classifier\_continuous(), the number of samples in a single slice) for a new slice (`run_classifier_continuous()`) in order to perform preprocessing and inference.                                                                  |


Built with [Mintlify](https://mintlify.com).