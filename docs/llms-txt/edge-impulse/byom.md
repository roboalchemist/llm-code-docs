# Source: https://docs.edgeimpulse.com/studio/projects/dashboard/byom.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bring your own model (BYOM)

**Bring your own model** or **BYOM** allows you to optimize and deploy your own pretrained model (TensorFlow SavedModel, ONNX, or LiteRT (previously Tensorflow Lite)) to any edge device, directly from your Edge Impulse project.

<iframe src="https://www.youtube.com/embed/Bg8qU0egUMs" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

### Getting Started

First, create a new project in Edge Impulse.

Also make sure you have your own pretrained model available locally on your computer, in one of the following formats: TensorFlow SavedModel (`saved_model.zip`), ONNX model (`.onnx`) or LiteRT (previously Tensorflow Lite) model (`.tflite`)

For this guide, we will be uploading a [pretrained image classification TFLite model for plant disease classification](https://www.kaggle.com/models/agripredict/disease-classification/frameworks/tfLite/variations/disease-classification/versions/1).

Then, from the **Dashboard**, of your Edge Impulse project under "Getting started", select **Upload your model**:

<Frame caption="Edge Impulse project dashboard, showing the project overview and getting started options.">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/dashboard.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=48bdd294ed78a9751c55362ba0454a79" width="1569" height="1000" data-path=".assets/images/dashboard.png" />
</Frame>

### Step 1: Upload your model

1. **Upload your trained model**: Upload a TensorFlow SavedModel (`saved_model.zip`), ONNX model (`.onnx`) or LiteRT (previously Tensorflow Lite) model (`.tflite`) to get started.
2. **Model performance**: Do you want performance characteristics (latency, RAM and ROM) for a specific device? Select "No" to show the performance for a range of device types, or "Yes" to run performance profiling for any of our available officially supported Edge Impulse development platforms.
3. If your model is not already quantized, you can also upload a `.npy` file to **Upload representative features (Optional)** - for example, your validation set - as an `.npy` file. This way, we can automatically quantize this model for better on-device performance. See [quantization](/studio/projects/dashboard/byom#quantization) below.

<Frame caption="Uploading a pretrained .onnx model">
  <img src="https://mintcdn.com/edgeimpulse/MguyU0DkkpALWBaW/.assets/images/upload-a-model-onnx.png?fit=max&auto=format&n=MguyU0DkkpALWBaW&q=85&s=5cfcc8e1969f76508014129a20a117e1" width="1263" height="1000" data-path=".assets/images/upload-a-model-onnx.png" />
</Frame>

After configuring the settings for uploading your model, select **Upload your model** and wait for your model to upload, you can check the upload status via the "Upload progress" section.

#### Quantization

<Info>
  **Quantization is currently only supported for SavedModel or ONNX uploads**

  Quantization requires a sample of data that is representative of the range (maximum and minimum) of values in your training data. In the Studio, we require a [numpy file](https://numpy.org/doc/stable/reference/generated/numpy.save.html) (`.npy`). Each element of the array must have the same shape as your model's input.

  Note that quantization is a form of lossy compression and may result in a reduction in model performance. It's important to evaluate your model after quantization to ensure it still performs well enough for your use case.
</Info>

### Step 2: Process your model

Depending on the model you have uploaded in Step 1, the configuration settings available for Step 2 will change.

The settings in this step determine what type of inputs and outputs your model expects. For input types, you can choose from:

* Image
* Audio
* Other (for example, if your model takes accelerometer data as input)

For output types, you can choose from:

* Classification (for example, if your model classifies images into different categories)
* Regression (for example, if your model predicts a continuous numerical value)
* Object detection (for example, if your model detects and localizes objects within an image)
* Freeform (for example, if your model produces outputs that do not fit into the other categories, such as image denoising, super-resolution, or pose estimation)
* Anomaly detection (for example, if your model predicts a numerical score indicating how anomalous the data is)

For this guide, we have selected the following configuration model settings for optimal processing for an image classification model with input shape `(300, 300, 3)` in **RGB format**, **Classification model output** and **16 output labels**: `Tomato Healthy, Tomato Septoria Leaf Spot, Tomato Bacterial Spot, Tomato Blight, Cabbage Healthy, Tomato Spider Mite, Tomato Leaf Mold, Tomato_Yellow Leaf Curl Virus, Soy_Frogeye_Leaf_Spot, Soy_Downy_Mildew, Maize_Ravi_Corn_Rust, Maize_Healthy, Maize_Grey_Leaf_Spot, Maize_Lethal_Necrosis, Soy_Healthy, Cabbage Black Rot`

After configuring your model settings, select **Save model** to view your model's on-device performance information for both MCUs and microprocessors (if applicable, depending on your model's arena size).

<Frame caption="Step 2: Process your model">
  <img src="https://mintcdn.com/edgeimpulse/iTt6mNOXOy0YNrkb/.assets/images/process-a-model.png?fit=max&auto=format&n=iTt6mNOXOy0YNrkb&q=85&s=1016248b92c6abb7c02ea06752fe7b20" width="1600" height="655" data-path=".assets/images/process-a-model.png" />
</Frame>

#### **Check model behavior**

Optionally upload test data to ensure correct model settings and proper model processing:

<Frame caption="Step 2: Check model behavior">
  <img src="https://mintcdn.com/edgeimpulse/BnOEP1CPlKpl2ntM/.assets/images/check-model-behavior.png?fit=max&auto=format&n=BnOEP1CPlKpl2ntM&q=85&s=82a49f6ebb0e975c0625a6286d0cc97e" width="1000" height="1000" data-path=".assets/images/check-model-behavior.png" />
</Frame>

<br />

<Frame caption="Step 2: Check model behavior results">
  <img src="https://mintcdn.com/edgeimpulse/BnOEP1CPlKpl2ntM/.assets/images/check-model-behavior-results.png?fit=max&auto=format&n=BnOEP1CPlKpl2ntM&q=85&s=a28c0c128bd533810b39b3d27b0167f3" width="838" height="1000" data-path=".assets/images/check-model-behavior-results.png" />
</Frame>

### Limitations

There are a couple of restrictions to converting models with our tooling. For Object Detection, Classification and Regression models, the following restrictions apply:

* The model must have 1 input tensor.
* You need to have a batch dimension (e.g. if your input is an image of 320x320x3 then your input shape should be `(1,320,320,3)`), and the batch size must be equal to 1. For ONNX models you can use a variable batch size (we'll set it to 1).
* For classification and regression models: The model must have 1 output tensor, and the output tensor should have a batch dimension as well. E.g. a classification model with 3 classes should have output shape `(1,3)`.
* Regression models must have an output shape of `(1,1)`.
* For "Freeform models" (see below) you can have multiple output tensors.
* Some operations are not supported some devices, such as MCUs. If your model contains unsupported operations you will see an error during the build step.

For more information on using freeform models, see [Deploy pretrained models with freeform outputs](/tutorials/topics/machine-learning/deploy-freeform-model).

### Troubleshooting

**--saved-model /tmp/saved\_model does not exist:**

If you encountered the following error:

```
Job started
Converting SavedModel...
Scheduling job in cluster...
Job started
Application exited with code 1
INFO: No representative features passed in, won't quantize this model

Extracting saved model...
Extracting saved model OK

--saved-model /tmp/saved_model does not exist

Converting SavedModel failed, see above

Job failed (see above)
```

Make sure to upload a `.zip` archive containing at minimum a `saved_model` directory that contains your `saved_model.pb`.

**Could not profile: No uploaded model yet**

If you encounter the following error:

```
Could not profile: No uploaded model yet
```

This often means that the model you are attempting to upload is unsupported. Only the following model formats are supported at this time:

* TensorFlow SavedModel (in .zip archive)
* ONNX (.onnx)
* LiteRT (previously Tensorflow Lite) (.tflite or .lite)

**This model won’t run on MCUs.**

If you see a message along these lines:

```
This model won’t run on MCUs. Unsupported ops: Pow.
```

Then that means that part of your network is not supported by EON Compiler, and cannot run as-is on MCUs. A list of all supported ops can be found in [our SDK](https://github.com/edgeimpulse/inferencing-sdk-cpp/blob/master/tensorflow/lite/micro/all_ops_resolver.cc); but there might be certain input/output types that are not supported even if the op is in this list (you'll get a proper error code if this is the case). If you're an enterprise customer please contact your solutions engineer, most of the times we can add the missing op within a few days.

### Preprocessing your data using Edge Impulse DSP blocks

If you want to use our built-in [processing blocks](/studio/projects/processing-blocks) to preprocess your data, for example to turn your audio files into spectrograms before training your network, then you should:

1. Use the code in the [edgeimpulse/processing-blocks](https://github.com/edgeimpulse/processing-blocks) repo to preprocess your data before training your model. This contains the Python version of the processing blocks.
2. Then, on the embedded side, call `extract_XXXX_features` to preprocess your sensor data, and pass the resulting features into the `ei_run_classifier` function.

Here's an end-to-end example of the embedded code to preprocess using an MFCC block:

```
#include <stdio.h>
#include "edge-impulse-sdk/classifier/ei_run_classifier.h"

// Audio (int16)
static const int16_t features[] = {
    0, 0, 1, 0, 0, 0, ...rest
};

static const float frequency = 16000.0f;

// We need the audio as float, but don't want to allocate the whole features buffer as float in one go
// as that'd double the required RAM. So dynamically convert i16->f32 when the MFCC algorithm requires.
static int input_signal_get_data(size_t offset, size_t length, float *out_ptr) {
    return numpy::int16_to_float(features + offset, out_ptr, length);
}

int main(int argc, char **argv) {
    // construct input signal (input is i16)
    signal_t input_signal;
    input_signal.total_length = sizeof(features) / sizeof(features[0]);
    input_signal.get_data = &input_signal_get_data;

    // construct an MFCC config (should match the params used to preprocess before training)
    ei_dsp_config_mfcc_t config = {
        1, // uint32_t block_id;
        3, // uint16_t implementation_version;
        1, // int axes;
        13, // int num_cepstral;
        0.032, // float frame_length;
        0.024, // float frame_stride;
        32, // int num_filters;
        256, // int fft_length;
        101, // int win_size;
        300, // int low_frequency;
        0, // int high_frequency;
        0.98f, // float pre_cof;
        1, // int pre_shift;
    };

    // calculate the size of the output matrix
    matrix_size_t out_matrix_size =
        speechpy::feature::calculate_mfcc_buffer_size(
            input_signal.total_length, frequency, config.frame_length, config.frame_stride, config.num_cepstral, config.implementation_version);
    printf("out_matrix_size = %u x %u\n", out_matrix_size.rows, out_matrix_size.cols);

    // create a new output matrix
    matrix_t out_matrix(out_matrix_size.rows, out_matrix_size.cols);
    int mfcc_ret = extract_mfcc_features(&input_signal, &out_matrix, (void *)&config, frequency);
    if (mfcc_ret != EIDSP_OK) {
        printf("ERR: MFCC failed w/ %d", mfcc_ret);
        return 1;
    }

    // print the features so you can check adherence to your Python results
    printf("Features:\n");
    for (size_t ix = 0; ix < out_matrix.rows * out_matrix.cols; ix++) {
        printf("%f ", out_matrix.buffer[ix]);
    }
    printf("\n");

    // this you'll pass into the NN
    signal_t nn_signal;
    ei::numpy::signal_from_buffer(out_matrix.buffer, out_matrix_size.rows * out_matrix_size.cols, &nn_signal);

    // call ei_run_classifier as usual

```


Built with [Mintlify](https://mintlify.com).