# Source: https://docs.qualcomm.com/nav/home/building_and_executing_tutorial_linux_host.html?product=1601111740010412

Title: Qualcomm AI Runtime (QAIRT) SDK

URL Source: https://docs.qualcomm.com/nav/home/building_and_executing_tutorial_linux_host.html?product=1601111740010412

Markdown Content:
SNPE Building and Executing a Model Tutorial for Linux Host
-----------------------------------------------------------

This guide will teach you how to build and execute an AI model using the Qualcomm Neural Processing SDK (aka SNPE).

1.   Install and set up SNPE

2.   Download your model

3.   Download and prepare your input data

4.   Build your model into a `.dlc` file

5.   (Optional) Quantize your model

6.   Transfer your model and SNPE files to your target device

7.   Execute your model with `snpe-net-run`

Note

Throughout this tutorial, we define many environment variables, so it is very helpful to keep the same terminal from the Setup steps all the way to the end.

Part 1: Tutorial Setup[](https://docs.qualcomm.com/nav/home/building_and_executing_tutorial_linux_host.html?product=1601111740010412#part-1-tutorial-setup "Click to copy section url")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.   Follow the instructions in the [[Setup](https://docs.qualcomm.com/nav/home/setup_linux.html?product=1601111740010412)](https://docs.qualcomm.com/) to install SNPE.

    1.   Make sure to install the optional Tensorflow dependency as this tutorial will use a Tensorflow model. If you are using another model, ensure you install the proper framework libraries in **Part 3** of the Setup.

### (OPTIONAL) Getting a new terminal if yours closed[](https://docs.qualcomm.com/nav/home/building_and_executing_tutorial_linux_host.html?product=1601111740010412#-optional-getting-a-new-terminal-if-yours-closed "Click to copy section url")

Warning

**You only have to do this if you need to create a new terminal instance because your running one closed.**

1.   Open a new terminal (`Ctrl + Alt + T` on Ubuntu).

2.   Run `echo $SNPE_ROOT` to verify that `SNPE_ROOT` is set to the folder just inside the `qairt` folder (Ex. `.../qairt/2.22.6.240515`).

3.   If `SNPE_ROOT` is not set:

    1.   Navigate to `qairt/<SNPE_ROOT_LOCATION>/bin`.

    2.   Run `source envsetup.sh` to set the environment variable.

Note

These changes will only apply to the current terminal session. 
    3.   Check again by running `echo $SNPE_ROOT`.

4.   Ensure you are in the proper virtual environment for Python.

    1.   If you are not in a `venv`, see Step 2 of Setup to install / activate your environment.

Part 2: Download Your Model[](https://docs.qualcomm.com/nav/home/building_and_executing_tutorial_linux_host.html?product=1601111740010412#part-2-download-your-model "Click to copy section url")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The framework used to generate your model impacts several parts of the process. Each model has specific dependencies in the Setup which must be installed, has a different way of formatting the model data, and has unique optimizations. Throughout these steps we will be using an example Tensorflow model called `Inception_V3` which classifies images. If you want to use another model, just replace any instances where `Inception_V3` is used, and pay attention to callouts indicating what to do (ex. using other flags or model-specific tools instead of Tensorflow-specific tools).

1.   Run `python -m pip show tensorflow` to verify that `tensorflow` is installed properly.

    1.   If `tensorflow` is not found, follow the steps in Part 3: Install Model Frameworks of the [[Setup](https://docs.qualcomm.com/nav/home/setup_linux.html?product=1601111740010412)](https://docs.qualcomm.com/) to install Tensorflow.

2.   Run these 3 commands to set the `TENSORFLOW_HOME` environment variable.

```
tensorflowLocation=$(python -m pip show tensorflow | grep '^Location: ' | awk '{print $2}');
export TENSORFLOW_HOME="${tensorflowLocation}/tensorflow";
echo "export TENSORFLOW_HOME=${TENSORFLOW_HOME}" >> ~/.bashrc
source ~/.bashrc
``` Note

`TENSORFLOW_HOME` is needed in this tutorial because the example data generation script (`setup_inceptionv3.py`) uses TensorFlow utilities like `optimize_for_inference.py`, which are present in the TensorFlow installation directory. 
3.   Verify that the `TENSORFLOW_HOME` variable is set correctly by running:

```
$TENSORFLOW_HOME
``` 
4.   Navigate to the folder we will use to store our example data by running:

```
cd ${SNPE_ROOT}/examples/Models/InceptionV3/data
``` 
5.   Use the pre-packaged example script to download the model and prepare some example input data:

```
python ${SNPE_ROOT}/examples/Models/InceptionV3/scripts/setup_inceptionv3_snpe.py -a . -d
``` 
    *   This script will:

        *   Download the InceptionV3 Model: `${SNPE_ROOT}/examples/Models/InceptionV3/data/inception_v3_2016_08_28_frozen.pb.tar.gz`.

        *   Download sample image data of various objects and their expected outputs: `${SNPE_ROOT}/examples/Models/InceptionV3/data`.

        *   Normalize the image data into the proper format for the model to process at: `${SNPE_ROOT}/examples/Models/InceptionV3/data/cropped`.

    *   For your use case, you can download your model and input data using any methods you wish. Remember though, based on your model type, you will need to install the proper framework files in the [[Setup](https://docs.qualcomm.com/nav/home/setup_linux.html?product=1601111740010412)](https://docs.qualcomm.com/).

6.   Verify that the zipped model was downloaded by running:

```
ls inception_v3*
``` 
You should see the zipped model file `inception_v3_2016_08_28_frozen.pb.tar.gz`.

7.   Unzip the model:

```
tar -xzf inception_v3_2016_08_28_frozen.pb.tar.gz
``` 
8.   Verify the model is unzipped by running

```
ls *.pb
``` 
You should see `inception_v3_2016_08_28_frozen.pb`.

Part 3: Preparing Input Data (No action required)[](https://docs.qualcomm.com/nav/home/building_and_executing_tutorial_linux_host.html?product=1601111740010412#part-3-preparing-input-data-no-action-required "Click to copy section url")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Warning

The example `setup_inceptionv3_snpe.py` script you just called handles downloading and preparing your input data for the Inception V3 model, **so you do not need to do anything in this section to use that model.**

That being said, if you are using your own model or just want to understand how the preparation is happening behind the scenes, read these steps.

There are several sub-scripts located in `${SNPE_ROOT}\examples\Models\InceptionV3\scripts` which help prepare input data for our model:

1.   The `setup_inceptionv3_snpe.py` script downloads `.jpg` files as input data (since Inception V3 is an image classification model).

2.   `setup_inceptionv3_snpe.py` then calls `create_inceptionv3_raws.py` to convert the compressed `.jpg` images into cropped binary `.raw` files with the proper shape for the model: `(1,299,299)`.

3.   These `.raw` files are then saved to a folder called `cropped`.

    *   This folder contains formatted files which can be used by your AI model.

    *   `cropped` also contains `raw_list.txt` which indicates file paths to sample data which should be used to help quantize your model. (This is used by `--input_list` in a future optional step).

Note

You can see the `.jpg` files and the `cropped` folder by running `ls`.

For a real world scenario, you would need to follow these steps to download and prepare your input data:

> 1.   Download the input data. (Similar to how `setup_inceptionv3_snpe.py` does with the `-d` flag).
> 
> 2.   Write custom code to normalize the data into a format your model can interpret. (Similar to how `create_inceptionv3_raws.py` generates the `cropped` folder).
> 
> 
>     *   This may also be where you would choose to generate the equivalent of `cropped\raw_list.txt` to provide paths to calibration data for quantization (which is required for DSP, HTP, and AIP processors).
> 
> 
> 3.   Run the normalization code on your input data. (Similar to us calling `setup_inceptionv3_snpe.py`).
> 
> 4.   Note the folder with the prepared input data for later.
> 
> 
>     *   **We will need to transfer the input data to the target device in Part 5.**

Part 4: Build the `.dlc` File[](https://docs.qualcomm.com/nav/home/building_and_executing_tutorial_linux_host.html?product=1601111740010412#part-4-build-the-dlc-file "Click to copy section url")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In order to use the model on a target device, we must convert it into a `.dlc` file which can be interpreted by SNPE backends. This is done using the `qairt-converter`.

1.   Run the following to see which architecture, OS, and gcc version you have:

```
uname -m
cat /etc/os-release
gcc --version
``` 
You should see an output like:

```
x86_64
PRETTY_NAME="Ubuntu 22.04.4 LTS"
NAME="Ubuntu"
VERSION_ID="22.04"
VERSION="22.04.4 LTS (Jammy Jellyfish)"
VERSION_CODENAME=jammy
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=jammy
gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
``` 
2.   Based on your host machine’s architecture, OS, and gcc version, choose the proper folder:

| **Operating System** | **Architecture** | **GCC Version** | **Folder Name** |
| --- | --- | --- | --- |
| Linux (64-bit) | x86_64 |  | x86_64-linux-clang |
| Android (64-bit devices) | arm64 |  | aarch64-android |
| QNX (Qualcomm) | arm64 |  | aarch64-qnx¹ |
| OpenEmbedded Linux | arm64 | 11.2 | aarch64-oe-linux-gcc11.2 |
| OpenEmbedded Linux | arm64 | 9.3 | aarch64-oe-linux-gcc9.3 |
| OpenEmbedded Linux | arm64 | 8.2 | aarch64-oe-linux-gcc8.2 |
| Ubuntu Linux | arm64 | 9.4 | aarch64-ubuntu-gcc9.4 |
3.   Run the following command with the corresponding folder from above to set your `HOST_MACHINE_ARCH`, for example:

```
export HOST_MACHINE_ARCH="x86_64-linux-clang"
``` 
4.   Set a CLI variable for the [[qairt-converter](https://docs.qualcomm.com/nav/home/SNPE_general_tools.html?product=1601111740010412#qairt-converter)](https://docs.qualcomm.com/) tool. This unified tool supports all model frameworks via different flags.

    1.   See the [[reference docs](https://docs.qualcomm.com/nav/home/SNPE_general_tools.html?product=1601111740010412#qairt-converter)](https://docs.qualcomm.com/) for more details about how to configure `qairt-converter` for other model frameworks. For this tutorial we will show how to use it for Tensorflow.

```
export SNPE_CONVERTER_TOOL="qairt-converter"
``` 

5.   **(Optional)** Inspect your model file to learn information you can pass into flags later on.

    *   For this tutorial, we have already pre-filled the values for the flags we recommend.

    *   You can use the following python script as an example of how to inspect your model file. Each model framework will likely have similar functions for interpreting their files.

    *   You can run the example inspection code below by following these steps:

        1.   Create a new file named `tensorflow-info.py` in the same folder as `inception_v3_2016_08_28_frozen.pb` (located by default at `${SNPE_ROOT}\examples\Models\InceptionV3\data`).

        2.   Copy the code into a file named `tensorflow-info.py`.

        3.   Run `python tensorflow-info.py`.

```
import tensorflow as tf

model_filename = 'inception_v3_2016_08_28_frozen.pb'

with tf.io.gfile.GFile(model_filename, 'rb') as f:
    graph_def = tf.compat.v1.GraphDef()
    graph_def.ParseFromString(f.read())

with tf.Graph().as_default() as graph:
    tf.import_graph_def(graph_def, name='')

    # Print all placeholder/input nodes:
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

6.   Run the following command to build the `.dlc` file:

Warning

The flags required to interpret a model vary slightly based on the input file type, but the data passed in should be similar. ```
qairt-converter \
--input_network inception_v3_2016_08_28_frozen.pb \
--desired_input_shape 'input' 1,299,299,3 \
--out_tensor_node 'InceptionV3/Predictions/Reshape_1' \
--source_model_input_layout 'input' NHWC \
--output_path inception_v3_model.dlc
``` 
Let’s break down what the flags are doing:

| **Field Name** | **Description** | **Type** | **Required?** | **Example** |
| --- | --- | --- | --- | --- |
| `--input_network` | Path to the source TensorFlow model file (`.pb`). This is the original model you want to convert into a `.dlc`. | String | ✅ Yes | `inception_v3_2016_08_28_frozen.pb` |
| `--desired_input_shape` | Specifies the input tensor name and its shape in the format `'name' N,H,W,C`. `N` is batch size, `H` is height, `W` is width, `C` is the number of channels. **Required for TensorFlow and PyTorch models.** | String, Shape | ✅ Yes | `'input' 1,299,299,3` |
| `--out_tensor_node` | The name of the output tensor node from the model. Determines which tensor is used as the model’s final output. **Required for TensorFlow models.** | String | ✅ Yes | `'InceptionV3/Predictions/Reshape_1'` |
| `--source_model_input_layout` | Describes the layout format of the input tensor data. For TensorFlow models, it’s typically `NHWC` (batch, height, width, channels). | String | ❌ No | `'input' NHWC` |
| `--output_path` | The destination path and filename for the generated `.dlc` file. If omitted, the tool will generate a default based on the input file. | String | ❌ No | `inception_v3_model.dlc` |
7.   Verify that the `.dlc` file generated properly by running

```
ls *.dlc
``` 
You should see a file named `inception_v3_model.dlc`.

(Optional) Part 5: Quantization[](https://docs.qualcomm.com/nav/home/building_and_executing_tutorial_linux_host.html?product=1601111740010412#-optional-part-5-quantization "Click to copy section url")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Warning

Quantization is **required** for DSP, HTP and AIP targets.

Quantization is an optional step that allows you to reduce the size of your model from full precision (32 bits) to a smaller bit size (8 bits by default).

In order to quantize your model, you will need several things:

*   Training data to help calibrate the quantized model. This shows the quantizer how the model uses the data, and which weights are more important to the output than others.

*   A file containing a list of file paths to the calibration data. In our case, we named that file `raw_list.txt`.

For this tutorial, we have already generated both of these in the `${SNPE_ROOT}\examples\Models\InceptionV3\data\cropped` folder via the `${SNPE_ROOT}\examples\Models\InceptionV3\scripts\setup_inceptionv3.py` script.

Note

See **“Step 3: Preparing Input Data”** of this tutorial for how to generate the `raw_list.txt` file and the input data that `raw_list.txt` points to.

1.   Go to the folder containing your model and input data by running this command:

```
cd ${SNPE_ROOT}\examples\Models\InceptionV3\data
``` 
2.   Run the following command using `qairt-quantizer` to quantize your model:

Warning

For this tutorial, we have our quantized `.dlc` overwrite our original `.dlc` file to simplify the tutorial (as most of the remaining instructions are the same regardless of whether the model was quantized or not). In practice, it may be worth using a different name like `inception_v3_quantized.dlc` for the quantized model. ```
qairt-quantizer \
  --input_dlc inception_v3_model.dlc \
  --input_list $SNPE_ROOT/examples/Models/InceptionV3/data/cropped/raw_list.txt \
  --output_dlc inception_v3_model.dlc
``` 

Here’s what the command flags above do:

| Field Name | Description | Type | Required? | Example |
| --- | --- | --- | --- | --- |
| `--input_dlc` | Path to the original **unquantized**`.dlc` model that you want to quantize. This is the input model. | String (file path) | ✅ Yes | `inception_v3_model.dlc` |
| `--input_list` | Path to a **text file** listing the raw input data files used for calibration during quantization. Each line in the file should point to one or more raw input binaries. | String (file path) | ✅ Yes | `$SNPE_ROOT/examples/Models/InceptionV3/data/cropped/raw_list.txt` |
| `--output_dlc` | Destination path and filename for the **quantized**`.dlc` model. If omitted, a file named `<original_name>_quantized.dlc` will be automatically created. | String (file path) | ❌ No | `inception_v3_model_quantized.dlc` |

There are many flags which can determine how quantization is done for your model (ex. changing the output bit size). See the [[reference material](https://docs.qualcomm.com/nav/home/SNPE_general_tools.html?product=1601111740010412#qairt-quantizer)](https://docs.qualcomm.com/) for more details on how you can quantize your model.
