# Source: https://docs.qualcomm.com/nav/home/building_and_executing_tutorial_windows_host.html?product=1601111740010412

Title: Qualcomm AI Runtime (QAIRT) SDK

URL Source: https://docs.qualcomm.com/nav/home/building_and_executing_tutorial_windows_host.html?product=1601111740010412

Markdown Content:
SNPE Building and Executing Your Model for Windows Host
-------------------------------------------------------

This guide will teach you how to build and execute an AI model using the Qualcomm Neural Processing SDK (aka SNPE). While this tutorial will use a Tensorflow model as an example, it will also point you towards all the resources, decisions, and steps you will need regardless of the model, host OS, target device, or processors you need to run your AI model on.

If you want to use your own model, you can still use this tutorial as a reference for the steps you will need to do, and where to look for context on your situation.

This tutorial will walk you through how to:

1.   Install and set up SNPE

2.   Download your model

3.   Download and prepare your input data

4.   Build your model into a `.dlc` file

5.   (Optional) Quantize your model

6.   Transfer your model and SNPE files to your target device

7.   Execute your model with `snpe-net-run`

Note

Throughout this tutorial, we define many environment variables, so it is very helpful to keep the same PowerShell session from the Setup tutorial.

Part 1: Tutorial Setup[](https://docs.qualcomm.com/nav/home/building_and_executing_tutorial_windows_host.html?product=1601111740010412#part-1-tutorial-setup "Click to copy section url")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.   Follow the instructions in the [[Setup](https://docs.qualcomm.com/nav/home/setup_windows.html?product=1601111740010412)](https://docs.qualcomm.com/) to install SNPE.

    *   In Step 3 of SNPE Windows Setup, make sure to install the optional Tensorflow dependency as this tutorial uses a TensorFlow-based model. If you’re using a different model format (_ex., PyTorch or ONNX_), be sure to install the appropriate framework libraries.

    *   Once the [[Setup](https://docs.qualcomm.com/nav/home/setup_windows.html?product=1601111740010412)](https://docs.qualcomm.com/) is complete, please continue to Part 2 below.

Part 2: Download Your Model[](https://docs.qualcomm.com/nav/home/building_and_executing_tutorial_windows_host.html?product=1601111740010412#part-2-download-your-model "Click to copy section url")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The framework used to generate your model impacts several parts of the process. Each model has specific dependencies in the Setup which must be installed, has a different way of formatting the model data, and has unique optimizations.

Throughout these steps we will be using an example Tensorflow model called `Inception_V3` which classifies images.

Warning

If you want to use another model, sub out any instances where `Inception_V3` is used, and pay attention to callouts indicating what to do (ex. using other flags or model-specific tools instead of Tensorflow-specific tools).

1.   Run `python -m pip show tensorflow` to verify that `tensorflow` is installed properly.

    *   If `tensorflow` is not found, follow the steps in Part 3 of the [[SNPE Windows Setup](https://docs.qualcomm.com/nav/home/setup_windows.html?product=1601111740010412)](https://docs.qualcomm.com/) instructions to install Tensorflow, then retry the above command to verify it is installed.

2.   Run these 3 commands to set the `TENSORFLOW_HOME` environment variable.

```
$tensorflowLocation = (python -m pip show tensorflow | Select-String -Pattern '^Location: ' | ForEach-Object { $_.ToString().Split(' ')[1].Trim() });
[System.Environment]::SetEnvironmentVariable('TENSORFLOW_HOME', "$tensorflowLocation\tensorflow", 'User');
$env:TENSORFLOW_HOME = [System.Environment]::GetEnvironmentVariable('TENSORFLOW_HOME', 'User');
``` Note

`TENSORFLOW_HOME` is needed because the `setup_inceptionv3.py` script uses TensorFlow utilities like `optimize_for_inference.py`, which are present in the TensorFlow installation directory. Not all models will need this, and other model frameworks can skip this. 
3.   Run the following to verify that the environment variable was set properly:

```
$env:TENSORFLOW_HOME
``` 
4.   Navigate to where the example files will live by running:

```
cd "$env:SNPE_ROOT\examples\Models\InceptionV3\data"
``` 
5.   Run the following script to download the example model and data:

```
python "$env:SNPE_ROOT\examples\Models\InceptionV3\scripts\setup_inceptionv3_snpe.py" -a . -d
``` 
This script will:

    1.   Download the InceptionV3 Model: `$env:SNPE_ROOT\examples\Models\InceptionV3\data\inception_v3_2016_08_28_frozen.pb.tar.gz`

    2.   Download sample image data of various objects and their expected outputs: `$env:SNPE_ROOT\examples\Models\InceptionV3\data`

    3.   Normalize the image data into the proper format for the model to process at: `$env:SNPE_ROOT\examples\Models\InceptionV3\data\cropped`

Warning

If you encounter the error “Missing `qti` Module” you should add the `lib` folder to your `PYTHONPATH` by running: `$env:PYTHONPATH = "$env:SNPE_ROOT\lib\python"`

Note

To use other models, you will need to download your model and your input data using whichever method you want, then use that data folder going forward.

6.   Run the following command to verify that the model was downloaded:

```
ls inception_v3*
``` 
You should see the zipped model file `inception_v3_2016_08_28_frozen.pb.tar.gz`.

7.   Run the following to unzip the model:

```
tar -xzf inception_v3_2016_08_28_frozen.pb.tar.gz
``` 
8.   Verify the model is unzipped by running:

```
ls *.pb
``` 
You should see `inception_v3_2016_08_28_frozen.pb`.

Part 3: Preparing Input Data (No action required for the example)[](https://docs.qualcomm.com/nav/home/building_and_executing_tutorial_windows_host.html?product=1601111740010412#part-3-preparing-input-data-no-action-required-for-the-example "Click to copy section url")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Warning

The example `setup_inceptionv3_snpe.py` script you just called handles downloading and preparing your input data for the Inception V3 model, **so you do not need to do anything in this section to use the example Inception V3 model.**

That being said, if you are using your own model or just want to understand how the preparation is happening behind the scenes, read these steps.

There are several sub-scripts located in `$SNPE_ROOT\examples\Models\InceptionV3\scripts` which helped prepare the input data for our model:

1.   The `setup_inceptionv3_snpe.py` script downloads `.jpg` files as input data (since Inception V3 is an image classification model).

2.   `setup_inceptionv3_snpe.py` then calls `create_inceptionv3_raws.py` to convert the compressed `.jpg` images into cropped binary `.raw` files with the proper shape for the model: `(1,299,299)`.

3.   These `.raw` files are then saved to a folder called `cropped`.

    *   This folder contains formatted files which can be used by your AI model.

    *   `cropped` also contains `raw_list.txt` which indicates file paths to sample data which should be used to help quantize your model. (This is used by `--input_list` in a future optional step).

Note

You can see the `.jpg` files and the `cropped` folder by running `ls`.

For a real world scenario, you would need to follow these steps to download and prepare your input data:

Note

1.   Download the input data. (Similar to how `setup_inceptionv3_snpe.py` does with the `-d` flag)

2.   Write custom code to normalize the data into a format your model can interpret. (Similar to how `create_inceptionv3_raws.py` generates the `cropped` folder)

This may also be where you would choose to generate the equivalent of `cropped\raw_list.txt` to provide paths to calibration data for quantization (which is required for DSP, HTP, and AIP processors).

3.   Run the normalization code on your input data. (Similar to us calling `setup_inceptionv3_snpe.py`)

4.   Create an input_list for testing your inferences later on. In this case, `target_raw_list.txt` contains the relative paths to data

5.   Note the folder with the prepared input data for later.

**We will need to transfer the input data to the target device in Step 5.**

Part 4: Build the `.dlc` File[](https://docs.qualcomm.com/nav/home/building_and_executing_tutorial_windows_host.html?product=1601111740010412#part-4-build-the-dlc-file "Click to copy section url")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In order to use the model on a target device, we must convert it into a `.dlc` file which can be interpreted by SNPE backends. This is done using model conversion tools like `snpe-tensorflow-to-dlc`.

1.   Check which architecture your host machine is using by running:

```
$env:PROCESSOR_ARCHITECTURE
``` 
2.   Use this table to determine which folder contains the proper files for your host machine’s OS and architecture:

| Operating System | Architecture | Folder Name |
| --- | --- | --- |
| **Windows** | x86_64 (aka ”AMD64”) | x86_64-windows-msvc |
| **SnapDragon on Windows** | arm64x | arm64x-windows-msvc |
| **Windows** | ARM64 | aarch64-windows-msvc |
3.   Replace the below `x86_64-windows-msvc` with the folder you chose above, then run the command:

```
$env:HOST_MACHINE_ARCH = "x86_64-windows-msvc"
Write-Output "Set HOST_MACHINE_ARCH to '$($env:HOST_MACHINE_ARCH)'"
``` 
4.   Choose the proper conversion tool based on your model type:

Note

In this case, we are using a TensorFlow model, so need to use the **``snpe-tensorflow-to-dlc``**. In a practical situation however, you may need to use a different converter. Note

`qairt-converter` is the most modern version of the tool (which works for all model types), but as of writing this tutorial, it is not supported on Windows host machines. See the documentation [[here](https://docs.qualcomm.com/nav/home/SNPE_general_tools.html?product=1601111740010412#tools)](https://docs.qualcomm.com/). 
| Model Framework | Tool Name |
| --- | --- |
| ONNX | [[snpe-onnx-to-dlc](https://docs.qualcomm.com/nav/home/SNPE_general_tools.html?product=1601111740010412#snpe-onnx-to-dlc)](https://docs.qualcomm.com/) |
| PyTorch | [[snpe-pytorch-to-dlc](https://docs.qualcomm.com/nav/home/SNPE_general_tools.html?product=1601111740010412#snpe-pytorch-to-dlc)](https://docs.qualcomm.com/) |
| TensorFlow | [[snpe-tensorflow-to-dlc](https://docs.qualcomm.com/nav/home/SNPE_general_tools.html?product=1601111740010412#snpe-tensorflow-to-dlc)](https://docs.qualcomm.com/) |
| TensorFlow Lite | [[snpe-tflite-to-dlc](https://docs.qualcomm.com/nav/home/SNPE_general_tools.html?product=1601111740010412#snpe-tflite-to-dlc)](https://docs.qualcomm.com/) |
| Other | See the [[Tools](https://docs.qualcomm.com/nav/home/SNPE_general_tools.html?product=1601111740010412#tools)](https://docs.qualcomm.com/) page for other options |
5.   Set a command line variable for the tool you chose, for example:

```
$env:SNPE_CONVERTER_TOOL = "snpe-tensorflow-to-dlc"
Write-Output "Set SNPE_CONVERTER_TOOL to '$($env:SNPE_CONVERTER_TOOL)'"
``` 
6.   **(Optional)** Review the [[reference documentation](https://docs.qualcomm.com/nav/home/SNPE_general_tools.html?product=1601111740010412#tools)](https://docs.qualcomm.com/) for the tool you chose in order to evaluate which flags are relevant. Each model converter tool uses similar inputs, but may have slightly different names for flags and fields.

    1.   For this tutorial, the recommended flags have been chosen ahead of time. Continue to see the example command.

7.   **(Optional)** Inspect your model file to learn what information can be passed into flags you chose to use later on.

    1.   For this tutorial, we have already pre-filled the values for the flags we recommend.

    2.   You can use the following python script as an example of how to inspect your model file. Each model framework will likely have similar functions for interpreting their files.

    3.   You can run the example inspection code below by following these steps:

        1.   Create a new file named `tensorflow-info.py` in the same folder as `inception_v3_2016_08_28_frozen.pb` (by default: `$env:SNPE_ROOT\examples\Models\InceptionV3\data`).

        2.   Copy the below code into `tensorflow-info.py`.

        3.   Run `python tensorflow-info.py`.

```
import tensorflow as tf

model_filename = 'inception_v3_2016_08_28_frozen.pb'

with tf.io.gfile.GFile(model_filename, 'rb') as f:
    graph_def = tf.compat.v1.GraphDef()
    graph_def.ParseFromString(f.read())

with tf.Graph().as_default() as graph:
    tf.import_graph_def(graph_def, name='')

    # Print all placeholder\input nodes:
    print("Input nodes (Placeholders):")
    for op in graph.get_operations():
        if op.type == "Placeholder":
            print(op.name, op.outputs[0].shape)

    # Optionally print output nodes (typical types are Softmax, Reshape, etc.)
    print("\nPossible output nodes:")
    for op in graph.get_operations():
        if op.type in ["Softmax", "Reshape", "Identity"]:
            print(op.name, op.type, op.outputs[0].shape)
```

Example output:

```
...
InceptionV3/Mixed_7c/Branch_3/Conv2d_0b_1x1/BatchNorm/moving_mean/read Identity (192,)
InceptionV3/Mixed_7c/Branch_3/Conv2d_0b_1x1/BatchNorm/moving_variance/read Identity (192,)
InceptionV3/Logits/Dropout_1b/Identity Identity (1, 1, 1, 2048)
InceptionV3/Logits/Conv2d_1c_1x1/weights/read Identity (1, 1, 2048, 1001)
InceptionV3/Logits/Conv2d_1c_1x1/biases/read Identity (1001,)
InceptionV3/Predictions/Reshape Reshape (1, 1001)
InceptionV3/Predictions/Softmax Softmax (1, 1001)
InceptionV3/Predictions/Reshape_1 Reshape (1, 1001)
```

8.   Navigate to the build output folder:

```
cd $env:SNPE_ROOT\examples\Models\InceptionV3\dlc
``` 
9.   Run the following command to build the `.dlc` file:

Warning

The flags required to interpret a model vary slightly based on the input file type, but the data passed in should be similar. See the [[reference material](https://docs.qualcomm.com/nav/home/SNPE_general_tools.html?product=1601111740010412#tools)](https://docs.qualcomm.com/) for the exact flags. This shows the command for using the `snpe-tensorflow-to-dlc` command. ```
python "$env:SNPE_ROOT\bin\$env:HOST_MACHINE_ARCH\$env:SNPE_CONVERTER_TOOL" `
  --input_network $env:SNPE_ROOT\examples\Models\InceptionV3\data\inception_v3_2016_08_28_frozen.pb `
  --input_dim 'input' 1,299,299,3 `
  --out_node 'InceptionV3/Predictions/Reshape_1' `
  --input_layout 'input' NHWC `
  --output_path './inception_v3_model.dlc'
``` 
Let’s break down what the flags are doing:

| Field Name | Description | Type | Required? | Example |
| --- | --- | --- | --- | --- |
| `--input_network` | Path to your TensorFlow model file (`.pb`). | String | ✅ Yes | `inception_v3_2016_08_28_frozen.pb` |
| `--input_dim` | Specifies the input tensor name and its shape using the format `'name' N,H,W,C`. Here, `N` is the batch size, `H` is image height, `W` is width, and `C` is the number of channels (e.g., 3 for RGB). **This is required for Tensorflow models, but not necessarily other models.** | String, Shape | ✅ Yes | `'input' 1,299,299,3` |
| `--out_node` | The exact name of your model’s output tensor node. This determines which part of the graph is returned as the output during inference. **This is required for Tensorflow models, but not necessarily other models.** You can use any of the nodes mentioned when running the example python script `tensorflow-info` from step 8 above. | String | ✅ Yes | `'InceptionV3\Predictions\Reshape_1'` |
| `--input_layout` | Specifies the layout of the input tensor data. For TensorFlow, the layout is usually `NHWC`, meaning [batch, height, width, channels]. | String | ❌ No | `'input' NHWC` |
| `--output_path` | The destination path and filename for the converted `.dlc` file. If omitted, a default path based on the input model name may be used. | String | ❌ No | `inception_v3_model.dlc` |
10.   Verify that the `.dlc` file generated properly by running:

```
ls *.dlc
``` 
You should see a file named `inception_v3_model.dlc`.

Part 5: Quantization (Optional)[](https://docs.qualcomm.com/nav/home/building_and_executing_tutorial_windows_host.html?product=1601111740010412#part-5-quantization-optional "Click to copy section url")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Warning

Quantization is **required** for DSP, HTP and AIP target devices.

Quantization is an optional step that allows you to reduce the size of your model from full precision (32 bits) to a smaller bit size (8 bits by default).

In order to quantize your model, you will need several things:

1.   Training data to help calibrate the quantized model. This shows the quantizer how the model uses the data, and which weights are more important to the output than others.

2.   A file containing a list of file paths to the calibration data. In our case, we named that file `raw_list.txt`.

For this tutorial, we have already generated both of these in the `$env:SNPE_ROOT\examples\Models\InceptionV3\data\cropped` folder via the `$env:SNPE_ROOT\examples\Models\InceptionV3\scripts\setup_inceptionv3.py` script.

Note

See **“Part 3: Preparing Input Data”** of this tutorial for how to generate the `raw_list.txt` file and the input data that `raw_list.txt` points to.

1.   Go to the folder containing your model and input data by running this command:

```
cd $env:SNPE_ROOT\examples\Models\InceptionV3\data
``` 
2.   Run the following command using [[snpe-dlc-quant](https://docs.qualcomm.com/nav/home/SNPE_general_tools.html?product=1601111740010412#snpe-dlc-quant)](https://docs.qualcomm.com/) to quantize your model:

Warning

For this tutorial, we have our quantized `.dlc` overwrite our original `.dlc` file to simplify the tutorial (as most of the remaining instructions are the same regardless of whether the model was quantized or not). In practice, it may be worth using a different name like `inception_v3_quantized.dlc` for the quantized model. ```
& "$env:SNPE_ROOT\bin\$env:HOST_MACHINE_ARCH\snpe-dlc-quant.exe" `
  --input_dlc $env:SNPE_ROOT\examples\Models\InceptionV3\dlc\inception_v3_model.dlc `
  --input_list $env:SNPE_ROOT\examples\Models\InceptionV3\data\cropped\raw_list.txt `
  --output_dlc $env:SNPE_ROOT\examples\Models\InceptionV3\dlc\inception_v3_model.dlc
``` Note

The most up-to-date quantization tool is `qairt-quantizer`, but as of writing this tutorial it did not support a Windows host. You can check whether that has changed [[here](https://docs.qualcomm.com/nav/home/SNPE_general_tools.html?product=1601111740010412#qairt-quantizer)](https://docs.qualcomm.com/) and learn how to use that tool. 
3.   You can verify that the `.dlc` file is now quantized by re-running the above command – it should fail saying:

```
“Tensor: InceptionV3/Conv2d_1a_3x3/weights/read:0 must be of type float to be quantizable, but it's: QNN_DATATYPE_UFIXED_POINT_8”
``` 

### DSP / HTP / AIP Additional Required Step - Offline Prepare[](https://docs.qualcomm.com/nav/home/building_and_executing_tutorial_windows_host.html?product=1601111740010412#dsp-htp-aip-additional-required-step-offline-prepare "Click to copy section url")

Warning

This is only needed to use chips with DSP / HTP / AIP processors. If you are planning to use a CPU or GPU, you should skip this section.

In order to avoid compiling on-device, there is one additional step here for HTP devices. Specifically, we need to use `snpe-dlc-graph-prepare` to generate an offline-compile cache to speed up inference on-device.

In order to use this tool, we need the following files (which we already have for this tutorial):

1.   A quantized `.dlc` model like we created above (`inception_v3.dlc`).

2.   A list of input data for calibration (`raw_list.txt`)

3.   The specific system on chip (SoC) name (ex. `sm8650`)

4.   `HtpPrepare.dll` within the same folder as `snpe-dlc-graph-prepare` as a core dependency.

**Follow these steps to create the context binary:**

1.   Look up the name of your system on chip (SoC) by scanning the [[list of device names](https://docs.qualcomm.com/nav/home/SNPE_general_overview.html?product=1601111740010412#supported-snapdragon-devices)](https://docs.qualcomm.com/).

The value should be all lowercase and a single word (ex. `sm8650`).

2.   Use that name to set this environment variable:

```
$env:SNPE_SOC_NAME = "sm8650"
Write-Host "Using SoC: $env:SNPE_SOC_NAME"
``` 
3.   Run the following command to add the `HtpPrepare.dll` folder to your `PATH`:

```
$env:SNPE_HTP_BIN = "$env:SNPE_ROOT\lib\x86_64-windows-msvc"
$env:PATH = "$env:SNPE_HTP_BIN;$env:PATH"
``` 
4.   Run the following to build a cache file which can be used alongside your model on your target device:

```
& "$env:SNPE_ROOT\bin\x86_64-windows-msvc\snpe-dlc-graph-prepare.exe" `
    --input_dlc   "$env:SNPE_ROOT\examples\Models\InceptionV3\dlc\inception_v3_model.dlc" `
    --input_list  "$env:SNPE_ROOT\examples\Models\InceptionV3\data\cropped\raw_list.txt" `
    --htp_socs     $env:SNPE_SOC_NAME `
    --output_dlc  "$env:SNPE_ROOT\examples\Models\InceptionV3\dlc\inception_v3_model_cached.dlc"
``` 
5.   Run the following to confirm that the cache was created:

```
ls $env:SNPE_ROOT\examples\Models\InceptionV3\dlc\ *.dlc
``` 
You should see `inception_v3_model_cached.dlc`.
