# Source: https://docs.edgeimpulse.com/studio/organizations/multi-project-deployment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Multi-project deployment

<Info>
  **Only available on the Enterprise plan**

  This feature is only available on the Enterprise plan. Review our [plans and pricing](https://edgeimpulse.com/pricing) or sign up for our free [expert-led trial](https://edgeimpulse.com/expert-led-trial) today.
</Info>

Multi-project deployment enables you to bundle and run **multiple Edge Impulse projects and impulses within a single deployment**. This unlocks more advanced on-device pipelines, such as model cascades or running multiple independent models on the same MCU or Linux device — all using the standard Edge Impulse SDK.

Key benefits:

* **Multiple impulses in one SDK build**
* **Mix and match projects**
  * Different projects
  * Different impulses
  * Quantized and non-quantized models
  * Object detection and non–object detection models together
* **No additional RAM or flash overhead** when deploying only a single impulse
* Works across **all Edge Impulse supported development platforms**

Some examples:

* **Model cascades**:
  * An object detection model to locate text
  * Followed by an OCR or classification model on the detected regions
* **Multiple independent models on one device**:
  * Running several sensor-based models side-by-side on a single MCU
  * Supporting different modalities or use cases simultaneously

<Frame caption="Multi-project deployment">
  <img src="https://mintcdn.com/edgeimpulse/aDgDbq9qykrFMknX/.assets/images/multi-project/multi-full.png?fit=max&auto=format&n=aDgDbq9qykrFMknX&q=85&s=910aa8ab05f8128962947632dc1730a5" width="2660" height="1872" data-path=".assets/images/multi-project/multi-full.png" />
</Frame>

## Multi-project deployment

Multi-project deployment is enabled at the **organization level**.

1. Go to **Multi-project deployments** in your organization
2. Add one or more entries, each specifying:
   * **Project ID**
   * **Impulse ID**
   * **Variant** (e.g. quantized or non-quantized, `int8` or `float32`)

For example, with the following tutorial projects added to your organization:

* [Tutorial: Responding to your voice](https://studio.edgeimpulse.com/public/14225/latest)
* [Tutorial: Adding sight to your sensors](https://studio.edgeimpulse.com/public/14227/latest)
* [Tutorial: object detection](https://studio.edgeimpulse.com/public/25483/latest)

Copy and paste the following example configuration (with **projectIds** changed to the IDs for projects in your organization):

```json  theme={"system"}
[
    { "projectId": 14225, "impulseId": 2, "variant": "int8" },
    { "projectId": 14227, "impulseId": 1, "variant": "int8" },
    { "projectId": 25483, "impulseId": 1, "variant": "float32" }
]
```

<Frame caption="Multi-project deployment with impulses configuration">
  <img src="https://mintcdn.com/edgeimpulse/aDgDbq9qykrFMknX/.assets/images/multi-project/org.png?fit=max&auto=format&n=aDgDbq9qykrFMknX&q=85&s=059822d7e9fc394a29eac3a34e4efb16" width="2650" height="1402" data-path=".assets/images/multi-project/org.png" />
</Frame>

## Inference runtime

After defining  your projects and impulses, choose your inference runtime:

* **EON Compiler**
* **EON Compiler (RAM Optimized)**
* **TensorFlow Lite**

<Frame caption="Deployment build configuration and runtime selection">
  <img src="https://mintcdn.com/edgeimpulse/aDgDbq9qykrFMknX/.assets/images/multi-project/runtime.png?fit=max&auto=format&n=aDgDbq9qykrFMknX&q=85&s=ac95919c94ec26b5893dd6845c039c54" width="2044" height="1222" data-path=".assets/images/multi-project/runtime.png" />
</Frame>

After building, Edge Impulse generates a **ZIP file**, similar to a standard C++ deployment.

You can load previous multi-project deployment configurations into the 'Impulses' field, by selecting the button to the right of the Job ID:

<Frame caption="Load previous multi-project deployment configurations">
  <img src="https://mintcdn.com/edgeimpulse/aDgDbq9qykrFMknX/.assets/images/multi-project/previous-deployments.png?fit=max&auto=format&n=aDgDbq9qykrFMknX&q=85&s=3bcdb55140855086f93540ce1991a8f1" width="2008" height="606" data-path=".assets/images/multi-project/previous-deployments.png" />
</Frame>

## Deployment package structure

The generated `.tar.gz` looks like a normal C++ deployment, with one key difference: it now contains **multiple models**, one per configured impulse.

<Frame caption="Example multi-project deployment structure">
  <img src="https://mintcdn.com/edgeimpulse/aDgDbq9qykrFMknX/.assets/images/multi-project/deployment.png?fit=max&auto=format&n=aDgDbq9qykrFMknX&q=85&s=24fab2a1972e9abc45639d91bebeb894" width="2024" height="820" data-path=".assets/images/multi-project/deployment.png" />
</Frame>

Each deployed model has:

* Its own model file
* Its corresponding model parameters

<Frame caption="Example multi-project deployment structure for 3 deployed models">
  <img src="https://mintcdn.com/edgeimpulse/aDgDbq9qykrFMknX/.assets/images/multi-project/deployment-multi.png?fit=max&auto=format&n=aDgDbq9qykrFMknX&q=85&s=f1b71a134e9f831b82f71cbd24886c1f" width="1854" height="824" data-path=".assets/images/multi-project/deployment-multi.png" />
</Frame>

## New orchestration entry point

Multi-project deployments ship with an updated `main.cpp` example file. This file contains **all orchestration logic** required to run multiple deployed impulses in your application.

## Working with multiple impulses in code

<Expandable title="example of a deployed `main.cpp` with 3 different impulses">
  ```cpp  theme={"system"}
  /*
  * Copyright (c) 2025 EdgeImpulse Inc.
  *
  * Generated by Edge Impulse and licensed under the applicable Edge Impulse
  * Terms of Service. Community and Professional Terms of Service
  * (https://edgeimpulse.com/legal/terms-of-service) or Enterprise Terms of
  * Service (https://edgeimpulse.com/legal/enterprise-terms-of-service),
  * according to your product plan subscription (the “License”).
  *
  * This software, documentation and other associated files (collectively referred
  * to as the “Software”) is a single SDK variation generated by the Edge Impulse
  * platform and requires an active paid Edge Impulse subscription to use this
  * Software for any purpose.
  *
  * You may NOT use this Software unless you have an active Edge Impulse subscription
  * that meets the eligibility requirements for the applicable License, subject to
  * your full and continued compliance with the terms and conditions of the License,
  * including without limitation any usage restrictions under the applicable License.
  *
  * If you do not have an active Edge Impulse product plan subscription, or if use
  * of this Software exceeds the usage limitations of your Edge Impulse product plan
  * subscription, you are not permitted to use this Software and must immediately
  * delete and erase all copies of this Software within your control or possession.
  * Edge Impulse reserves all rights and remedies available to enforce its rights.
  *
  * Unless required by applicable law or agreed to in writing, the Software is
  * distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
  * either express or implied. See the License for the specific language governing
  * permissions, disclaimers and limitations under the License.
  */

  #include <stdio.h>
  #include "edge-impulse-sdk/classifier/ei_run_classifier.h"

  // Raw features copied from test sample
  static const float features_impulse_14225_2[] = {
      // Copy raw features here (e.g. from the 'Live classification' page) for project 14225, impulse 2
      // https://studio.edgeimpulse.com/studio/14225/impulse/2/classification
  };

  static const float features_impulse_14227_1[] = {
      // Copy raw features here (e.g. from the 'Live classification' page) for project 14227, impulse 1
      // https://studio.edgeimpulse.com/studio/14227/impulse/1/classification
  };

  static const float features_impulse_25483_1[] = {
      // Copy raw features here (e.g. from the 'Live classification' page) for project 25483, impulse 1
      // https://studio.edgeimpulse.com/studio/25483/impulse/1/classification
  };

  int main(int argc, char **argv) {

      // project 14225, impulse 2
      {
          ei_printf("Impulse #1 (project 14225, impulse 2):\n");

          signal_t signal;            // Wrapper for raw input buffer
          ei_impulse_result_t result; // Used to store inference output
          EI_IMPULSE_ERROR res;       // Return code from inference

          const ei_impulse_t& impulse = impulse_14225_2;
          ei_impulse_handle_t& impulse_handle = impulse_handle_14225_2;

          run_classifier_init(&impulse_handle);

          // Calculate the length of the buffer
          size_t buf_len = sizeof(features_impulse_14225_2) / sizeof(features_impulse_14225_2[0]);

          // Make sure that the length of the buffer matches expected input length
          if (buf_len != impulse.dsp_input_frame_size) {
              ei_printf("ERROR: The size of the input buffer is not correct.\n");
              ei_printf("Expected %d items, but got %d\n",
                      impulse.dsp_input_frame_size,
                      (int)buf_len);
              return 1;
          }

          int err = numpy::signal_from_buffer(features_impulse_14225_2, impulse.dsp_input_frame_size, &signal);
          if (err != 0) {
              ei_printf("signal_from_buffer failed (%d)\n", err);
              return 1;
          }

          // Perform DSP pre-processing and inference
          res = run_classifier(&impulse_handle, &signal, &result, false);
          if (res != EI_IMPULSE_OK) {
              ei_printf("run_classifier returned: %d\n", res);
              return 1;
          }

          // See how to modify this in edge-impulse-sdk/classifier/ei_print_results.h
          ei_print_results(&impulse_handle, &result);
          ei_printf("\n");

          run_classifier_deinit(&impulse_handle);
      }


      // project 14227, impulse 1
      {
          ei_printf("Impulse #2 (project 14227, impulse 1):\n");

          signal_t signal;            // Wrapper for raw input buffer
          ei_impulse_result_t result; // Used to store inference output
          EI_IMPULSE_ERROR res;       // Return code from inference

          const ei_impulse_t& impulse = impulse_14227_1;
          ei_impulse_handle_t& impulse_handle = impulse_handle_14227_1;

          run_classifier_init(&impulse_handle);

          // Calculate the length of the buffer
          size_t buf_len = sizeof(features_impulse_14227_1) / sizeof(features_impulse_14227_1[0]);

          // Make sure that the length of the buffer matches expected input length
          if (buf_len != impulse.dsp_input_frame_size) {
              ei_printf("ERROR: The size of the input buffer is not correct.\n");
              ei_printf("Expected %d items, but got %d\n",
                      impulse.dsp_input_frame_size,
                      (int)buf_len);
              return 1;
          }

          int err = numpy::signal_from_buffer(features_impulse_14227_1, impulse.dsp_input_frame_size, &signal);
          if (err != 0) {
              ei_printf("signal_from_buffer failed (%d)\n", err);
              return 1;
          }

          // Perform DSP pre-processing and inference
          res = run_classifier(&impulse_handle, &signal, &result, false);
          if (res != EI_IMPULSE_OK) {
              ei_printf("run_classifier returned: %d\n", res);
              return 1;
          }

          // See how to modify this in edge-impulse-sdk/classifier/ei_print_results.h
          ei_print_results(&impulse_handle, &result);
          ei_printf("\n");

          run_classifier_deinit(&impulse_handle);
      }


      // project 25483, impulse 1
      {
          ei_printf("Impulse #3 (project 25483, impulse 1):\n");

          signal_t signal;            // Wrapper for raw input buffer
          ei_impulse_result_t result; // Used to store inference output
          EI_IMPULSE_ERROR res;       // Return code from inference

          const ei_impulse_t& impulse = impulse_25483_1;
          ei_impulse_handle_t& impulse_handle = impulse_handle_25483_1;

          run_classifier_init(&impulse_handle);

          // Calculate the length of the buffer
          size_t buf_len = sizeof(features_impulse_25483_1) / sizeof(features_impulse_25483_1[0]);

          // Make sure that the length of the buffer matches expected input length
          if (buf_len != impulse.dsp_input_frame_size) {
              ei_printf("ERROR: The size of the input buffer is not correct.\n");
              ei_printf("Expected %d items, but got %d\n",
                      impulse.dsp_input_frame_size,
                      (int)buf_len);
              return 1;
          }

          int err = numpy::signal_from_buffer(features_impulse_25483_1, impulse.dsp_input_frame_size, &signal);
          if (err != 0) {
              ei_printf("signal_from_buffer failed (%d)\n", err);
              return 1;
          }

          // Perform DSP pre-processing and inference
          res = run_classifier(&impulse_handle, &signal, &result, false);
          if (res != EI_IMPULSE_OK) {
              ei_printf("run_classifier returned: %d\n", res);
              return 1;
          }

          // See how to modify this in edge-impulse-sdk/classifier/ei_print_results.h
          ei_print_results(&impulse_handle, &result);
          ei_printf("\n");

          run_classifier_deinit(&impulse_handle);
      }

  }
  ```
</Expandable>

### Features arrays

Instead of a single `features[]` array, you now have **one features array per impulse**.

For example, with three impulses:

* Impulse 1: Quantized (int8) classification / anomaly detection
* Impulse 2: Free-form impulse
* Impulse 3: Object detection (e.g. FOMO, float32)

Each impulse:

* Has its own input features
* Produces its own output tensors

### Running inference

At runtime, inference is straightforward:

1. Initialize each impulse
2. Populate the corresponding features array
3. Call `run_classifier()` **once per impulse**, using the appropriate impulse handle
4. Read and interpret the results per model

All remaining logic is standard Edge Impulse inference orchestration.

### Example output

In a single application run, you might see:

* **Impulse 1**
  * Classification result: `wave ≈ 0.1`
  * Anomaly score: `≈ 1.1`

* **Impulse 2**
  * Free-form outputs
  * Multiple output tensors

* **Impulse 3**
  * Object detection result
  * Single detected object class (e.g. person, or object of interest)

## Troubleshooting

<Info>
  No common issues have been identified thus far. If you encounter an issue, please reach out on the [forum](https://forum.edgeimpulse.com) or, if you are on the Enterprise plan, through your support channels.
</Info>

## Additional resources

* [Deployment](/studio/projects/deployment)
* [EON Compiler](/studio/projects/deployment/eon-compiler)


Built with [Mintlify](https://mintlify.com).