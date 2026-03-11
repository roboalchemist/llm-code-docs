# Source: https://docs.edgeimpulse.com/knowledge/guides/reference-designs/health-reference-design/transforming-clinical-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Transforming clinical data

<Info>
  **Only available on the Enterprise plan**

  This feature is only available on the Enterprise plan. Review our [plans and pricing](https://edgeimpulse.com/pricing) or sign up for our free [expert-led trial](https://edgeimpulse.com/expert-led-trial) today.
</Info>

Transformation blocks take raw data from your [organizational datasets](/knowledge/guides/reference-designs/health-reference-design/synchronizing-clinical-data) and convert the data into a different dataset or files that can be loaded in an Edge Impulse project. You can use transformation blocks to only include certain parts of individual data files, calculate long-running features like a running mean or derivatives, or efficiently generate features with different window lengths. Transformation blocks can be written in any language, and run on the Edge Impulse infrastructure.

<Info>
  #### No required format for data files

  There is no required format for data files. You can upload data in any format, whether it's CSV, Parquet, or a proprietary data format.

  Parquet is a columnar storage format that is optimized for reading and writing large datasets. It is particularly useful for data that is stored in S3 buckets, as it can be read in parallel and is highly compressed.
</Info>

The PPG-DaLiA dataset is a multimodal collection featuring physiological and motion data recorded from 15 subjects.

In this tutorial we build a Python-based transformation block that loads Parquet files, we process the dataset by calculating features and transforming it into a unified schema suitable for machine learning. If you haven't done so, go through [synchronizing clinical data with a bucket](/knowledge/guides/reference-designs/health-reference-design/synchronizing-clinical-data) first.

#### 1. Prerequisites

You'll need:

* The [Edge Impulse CLI](/tools/clis/edge-impulse-cli/installation).
  * If you receive any warnings that's fine. Run `edge-impulse-blocks` afterwards to verify that the CLI was installed correctly.
* **PPG-DaLiA CSV files**: Download files like `ACC.csv`, `HR.csv`, `EDA.csv`, etc., which contain sensor data.

Transformation blocks use Docker containers, a virtualization technique that lets developers package up an application with all dependencies in a single package. *If you want to test your blocks locally* you'll also need (this is not a requirement):

* [Docker desktop](https://www.docker.com/get-started) installed on your machine.

#### 2. Building your first transformation block

To build a transformation block open a command prompt or terminal window, create a new folder, and run:

```
$ edge-impulse-blocks init
```

This will prompt you to log in, and enter the details for your block. E.g.:

```
Edge Impulse Blocks v1.9.0
? What is your user name or e-mail address (edgeimpulse.com)? user@example.com
? What is your password? [hidden]
Attaching block to organization 'Demo Organization'
? Choose a type of block Transformation block
? Choose an option Create a new block
? Enter the name of your block DaLiA Transformation
? Enter the description of your block Process DaLiA data and extract accelerometer features
Creating block with config: {
  name: 'DaLiA Transformation',
  type: 'transform',
  description: 'Processes accelerometer and activity data from the PPG-DaLiA dataset',
  organizationId: 34
}
```

Then, create the following files in this directory:

**2.1 - `Dockerfile`**

We're building a Python based transformation block. The Dockerfile describes our base image (Python 3.7.5), our dependencies (in `requirements.txt`) and which script to run (`transform.py`).

```
FROM python:3.7.5-stretch

WORKDIR /app

# Python dependencies
COPY requirements.txt ./
RUN pip3 --no-cache-dir install -r requirements.txt

COPY . ./

ENTRYPOINT [ "python3",  "transform.py" ]
```

**Note:** Do not use a `WORKDIR` under `/home`! The `/home` path will be mounted in by Edge Impulse, making your files inaccessible.

<Warning>
  **ENTRYPOINT vs RUN / CMD**

  If you use a different programming language, make sure to use `ENTRYPOINT` to specify the application to execute, rather than `RUN` or `CMD`.
</Warning>

**2.2 - `requirements.txt`**

This file describes the dependencies for the block. We'll be using `pandas` and `pyarrow` to parse the Parquet file, and `numpy` to do some calculations.

```
numpy==1.16.4
pandas==0.23.4
pyarrow==0.16.0
```

**2.3 - `transform.py`**

This file includes the actual application. Transformation blocks are invoked with three parameters (as command line arguments):

* `--in-file` or `--in-directory` - A file (if the block operates on a file), or a directory (if the block operates on a data item) from the organizational dataset. In this case the `unified_data.parquet` file.
* `--out-directory` - Directory to write files to.
* `--hmac-key` - You can use this HMAC key to sign the output files. This is not used in this tutorial.
* `--metadata` - Key/value pairs containing the metadata for the data item, plus additional metadata about the data item in the `dataItemInfo` key. E.g.:\
  \
  `{ "subject": "AAA001", "ei_check": "1", "dataItemInfo": { "id": 101, "dataset": "Human Activity 2022", "bucketName": "edge-impulse-tutorial", "bucketPath": "janjongboom/human_activity/AAA001/", "created": "2022-03-07T09:20:59.772Z", "totalFileCount": 14, "totalFileSize": 6347421 } }`

Add the following content. This takes in the Parquet file, groups data by their label, and then calculates the RMS over the X, Y and Z axes of the accelerometer.

```python  theme={"system"}
import numpy as np
import os
import argparse
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# Parse arguments
parser = argparse.ArgumentParser(description='Simple transformation block for single directory PPG-DaLiA data processing')
parser.add_argument('--in-directory', type=str, required=True, help="Path to the directory containing the CSV files")
parser.add_argument('--out-directory', type=str, required=True, help="Path to save the transformed Parquet file")
args = parser.parse_args()

# Check input and output directories
if not os.path.exists(args.in_directory):
    print(f"Data directory {args.in_directory} does not exist.", flush=True)
    exit(1)

if not os.path.exists(args.out_directory):
    os.makedirs(args.out_directory)

# Define paths to the necessary CSV files
acc_file = os.path.join(args.in_directory, 'ACC.csv')
hr_file = os.path.join(args.in_directory, 'HR.csv')
eda_file = os.path.join(args.in_directory, 'EDA.csv')
bvp_file = os.path.join(args.in_directory, 'BVP.csv')
temp_file = os.path.join(args.in_directory, 'TEMP.csv')
activity_file = os.path.join(args.in_directory, 'S1_activity.csv')

# Check if all required files are available
for file_path in [acc_file, hr_file, eda_file, bvp_file, temp_file, activity_file]:
    if not os.path.exists(file_path):
        print(f"Missing file {file_path}. Skipping processing.", flush=True)
        exit(1)

# Load data from CSV files
acc_data = pd.read_csv(acc_file, header=None, skiprows=2, names=['accX', 'accY', 'accZ'])
hr_data = pd.read_csv(hr_file, header=None, skiprows=2, names=['heart_rate'])
eda_data = pd.read_csv(eda_file, header=None, skiprows=2, names=['eda'])
bvp_data = pd.read_csv(bvp_file, header=None, skiprows=2, names=['bvp'])
temp_data = pd.read_csv(temp_file, header=None, skiprows=2, names=['temperature'])

# Load and clean activity labels
activity_labels = pd.read_csv(activity_file, header=None, skiprows=1, names=['activity', 'start_row'])
activity_labels['activity'] = activity_labels['activity'].str.strip()  # Remove leading/trailing whitespace
activity_labels['start_row'] = pd.to_numeric(activity_labels['start_row'], errors='coerce')  # Convert to numeric, setting invalid parsing to NaN
activity_labels = activity_labels.dropna(subset=['start_row']).reset_index(drop=True)  # Remove invalid rows and reset index
activity_labels['start_row'] = activity_labels['start_row'].astype(int)

# Set default activity and map activities to rows based on start_row intervals
acc_data['activity'] = 'NO_ACTIVITY'  # Default activity
for i in range(len(activity_labels) - 1):
    activity = activity_labels.loc[i, 'activity']
    start_row = activity_labels.loc[i, 'start_row']
    end_row = activity_labels.loc[i + 1, 'start_row']
    acc_data.loc[start_row:end_row - 1, 'activity'] = activity

# Handle the last activity to the end of the dataset
last_activity = activity_labels.iloc[-1]['activity']
last_start_row = activity_labels.iloc[-1]['start_row']
acc_data.loc[last_start_row:, 'activity'] = last_activity

# Calculate features
acc_features = {
    'accX_rms': np.sqrt(np.mean(acc_data['accX']**2)),
    'accY_rms': np.sqrt(np.mean(acc_data['accY']**2)),
    'accZ_rms': np.sqrt(np.mean(acc_data['accZ']**2)),
}
hr_mean = hr_data['heart_rate'].mean()
eda_mean = eda_data['eda'].mean()
bvp_mean = bvp_data['bvp'].mean()
temp_mean = temp_data['temperature'].mean()

# Combine features and unique activity labels
features = {
    **acc_features,
    'heart_rate_mean': hr_mean,
    'eda_mean': eda_mean,
    'bvp_mean': bvp_mean,
    'temperature_mean': temp_mean,
    'activity_labels': [activity_labels['activity'].tolist()]  # Nest the list of activities
}

# Convert features to DataFrame and save as Parquet file
features_df = pd.DataFrame([features])
out_file = os.path.join(args.out_directory, 'unified_data.parquet')
table = pa.Table.from_pandas(features_df)
pq.write_table(table, out_file)

print(f'Written features Parquet file: {out_file}', flush=True)
```

**Docker**

You can also build the container locally via Docker, and test the block. The added benefit is that you don't need any dependencies installed on your local computer, and can thus test that you've included everything that's needed for the block. This requires Docker desktop to be installed.

To build the container and test the block, open a command prompt or terminal window and navigate to the source directory. First, build the container:

```bash  theme={"system"}
docker build -t ppg-dalia-transform .
```

```markdown  theme={"system"}
[+] Building 1.8s (13/13) FINISHED                                                                                                                                          docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                                                        0.0s
 => => transferring dockerfile: 402B                                                                                                                                                        0.0s
 => [internal] load metadata for docker.io/library/ubuntu:20.04                                                                                                                             0.9s
 => [auth] library/ubuntu:pull token for registry-1.docker.io                                                                                                                               0.0s
 => [internal] load .dockerignore                                                                                                                                                           0.0s
 => => transferring context: 2B                                                                                                                                                             0.0s
 => [1/7] FROM docker.io/library/ubuntu:20.04@sha256:8e5c......7555141b                                                                       0.0s
 => [internal] load build context                                                                                                                                                           0.0s
 => => transferring context: 4.75MB                                                                                                                                                         0.0s
 => CACHED [2/7] WORKDIR /app                                                                                                                                                               0.0s
 => CACHED [3/7] RUN apt update && apt install -y python3 python3-distutils wget                                                                                                            0.0s
 => CACHED [4/7] RUN wget https://bootstrap.pypa.io/get-pip.py &&     python3.8 get-pip.py "pip==21.3.1" &&     rm get-pip.py                                                               0.0s
 => CACHED [5/7] COPY requirements.txt ./                                                                                                                                                   0.0s
 => CACHED [6/7] RUN pip3 --no-cache-dir install -r requirements.txt                                                                                                                        0.0s
 => [7/7] COPY . ./                                                                                                                                                                         0.5s
 => exporting to image                                                                                                                                                                      0.3s
 => => exporting layers                                                                                                                                                                     0.3s
 => => writing image sha256:856a1ec5eb879c904.......88e5e48899a                                                                                                0.0s
 => => naming to docker.io/library/ppg-dalia-transform                                                                                                                                      0.0s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/rnpnsjzniokmbvx29fj4cs0x3

What's next:
    View a summary of image vulnerabilities and recommendations → docker scout quickview
```

Then, run the container (make sure `unified_data.parquet` is in the same directory):

```bash  theme={"system"}
$ docker run --rm -v $PWD:/data test-org-transform-parquet-dataset --in-file /data/unified_data.parquet --out-directory /data/out
```

**Seeing the output**

This process has generated a new Parquet file in the `out/` directory containing the RMS of the X, Y and Z axes. If you inspect the content of the file (e.g. using parquet-tools) you'll see the output:

If you don't have `parquet-tools` installed, you can install it via:

```bash  theme={"system"}
$ pip install parquet-tools
```

Then, run:

```bash  theme={"system"}
$  parquet-tools inspect out/unified_data.parquet
```

This will show you the metadata and the columns in the file:

code output block:

```markdown  theme={"system"}
$
a############ file meta data ############
created_by: parquet-cpp-arrow version 18.0.0-SNAPSHOT
num_columns: 7
num_rows: 1
num_row_groups: 1
format_version: 2.6
serialized_size: 4373


############ Columns ############
accX_rms
accY_rms
accZ_rms
heart_rate_mean
eda_mean
bvp_mean
temperature_mean

############ Column(accX_rms) ############
name: accX_rms
path: accX_rms
max_definition_level: 1
max_repetition_level: 0
physical_type: DOUBLE
logical_type: None
converted_type (legacy): NONE
compression: SNAPPY (space_saved: -4%)

############ Column(accY_rms) ############
name: accY_rms
path: accY_rms
max_definition_level: 1
max_repetition_level: 0
physical_type: DOUBLE
logical_type: None
converted_type (legacy): NONE
compression: SNAPPY (space_saved: -4%)

############ Column(accZ_rms) ############
name: accZ_rms
path: accZ_rms
max_definition_level: 1
max_repetition_level: 0
physical_type: DOUBLE
logical_type: None
converted_type (legacy): NONE
compression: SNAPPY (space_saved: -4%)


Success!

```

#### 3. Pushing the transformation block to Edge Impulse

With the block ready we can push it to your organization. Open a command prompt or terminal window, navigate to the folder you created earlier, and run:

```bash  theme={"system"}
$ edge-impulse-blocks push
```

This packages up your folder, sends it to Edge Impulse where it'll be built, and finally is added to your organization.

```markdown  theme={"system"}
Edge Impulse Blocks v1.9.0
Archiving 'tutorial-processing-block'...
Archiving 'tutorial-processing-block' OK (2 KB) /var/folders/3r/fds0qzv914ng4t17nhh5xs5c0000gn/T/ei-transform-block-7812190951a6038c2f442ca02d428c59.tar.gz

Uploading block 'Demo dalia-ppg transformation' to organization 'Moe's Demo Org'...
Uploading block 'Demo dalia-ppg transformation' to organization 'Demo org Inc.' OK

Building transformation block 'Demo dalia-ppg transformation'...
Job started
...
Building transformation block 'Demo dalia-ppg transformation' OK

Your block has been updated, go to https://studio.edgeimpulse.com/organization/34/data to run a new transformation
```

The transformation block is now available in Edge Impulse under **Data transformation > Transformation blocks**.

<Frame caption="The transformation block in Edge Impulse">
  <img src="https://mintcdn.com/edgeimpulse/ykTERfSIYjBmgAC2/.assets/images/health-reference-public/health-ref-transform-1.png?fit=max&auto=format&n=ykTERfSIYjBmgAC2&q=85&s=a725c0e8df95eb677cc66fa02a362c1e" width="1416" height="1000" data-path=".assets/images/health-reference-public/health-ref-transform-1.png" />
</Frame>

If you make any changes to the block, just re-run `edge-impulse-blocks push` and the block will be updated.

#### 4. Uploading unified\_data.parquet to Edge Impulse

Next, upload the `unified_data.parquet` file, by going to **Data > Add data... > Add data item**, setting name as 'Gestures', dataset to 'Transform tutorial', and selecting the Parquet file.

This makes the `unified_data.parquet` file available from the **Data** page.

#### 5. Starting the transformation

With the Parquet file in Edge Impulse and the transformation block configured you can now create a new job. Go to **Data**, and select the Parquet file by setting the filter to `dataset = 'Transform tutorial'`.

<Frame caption="Selecting the transform tutorial dataset">
  <img src="https://mintcdn.com/edgeimpulse/ykTERfSIYjBmgAC2/.assets/images/health-reference-public/create-transform-job.png?fit=max&auto=format&n=ykTERfSIYjBmgAC2&q=85&s=f046155d1dc3c7c0412c02dae1b1c437" width="1588" height="1000" data-path=".assets/images/health-reference-public/create-transform-job.png" />
</Frame>

Click the checkbox next to the data item, and select **Transform selected (1 file)**. On the 'Create transformation job' page select 'Import data into Dataset'. Under 'output dataset', select 'Same dataset as source', and under 'Transformation block' select the new transformation block.

<Frame caption="Configuring the transformation job">
  <img src="https://mintcdn.com/edgeimpulse/ykTERfSIYjBmgAC2/.assets/images/health-reference-public/running-transform-job.png?fit=max&auto=format&n=ykTERfSIYjBmgAC2&q=85&s=b7bfb81d9fc4aee868bc4ea17e5d780d" width="1588" height="1000" data-path=".assets/images/health-reference-public/running-transform-job.png" />
</Frame>

Click **Start transformation job** to start the job. This pulls the data in, starts a transformation job and finally uploads the data back to your dataset. If you have multiple files selected the transformations will also run in parallel.

<Frame caption="Dataset transformation running">
  <img src="https://mintcdn.com/edgeimpulse/ykTERfSIYjBmgAC2/.assets/images/health-reference-public/progress.png?fit=max&auto=format&n=ykTERfSIYjBmgAC2&q=85&s=6109b5be2c6b36d1c7c05d1d1760ba15" width="1588" height="1000" data-path=".assets/images/health-reference-public/progress.png" />
</Frame>

You can now find the transformed file back in your dataset.

#### 6. Next steps

Transformation blocks are a powerful feature which let you set up a data pipeline to turn raw data into actionable machine learning features. It also gives you a reproducible way of transforming many files at once, and is programmable through the [Edge Impulse API](/apis/studio) so you can automatically convert new incoming data. If you're interested in transformation blocks or any of the other enterprise features, [let us know!](https://edgeimpulse.com/contact)

:rocket:

#### Appendix: Advanced features

**Updating metadata from a transformation block**

You can update the metadata of blocks directly from a transformation block by creating a `ei-metadata.json` file in the output directory. The metadata is then applied to the new data item automatically when the transform job finishes. The `ei-metadata.json` file has the following structure:

```json  theme={"system"}
{
    "version": 1,
    "action": "add",
    "metadata": {
        "some-key": "some-value"
    }
}
```

Some notes:

* If `action` is set to `add` the metadata keys are added to the data item. If `action` is set to `replace` all existing metadata keys are removed.

**Environmental variables**

Transformation blocks get access to the following environmental variables, which let you authenticate with the Edge Impulse API. This way you don't have to inject these credentials into the block. The variables are:

* `EI_API_KEY` - an API key with 'member' privileges for the organization.
* `EI_ORGANIZATION_ID` - the organization ID that the block runs in.
* `EI_API_ENDPOINT` - the API endpoint (default: [https://studio.edgeimpulse.com/v1](https://studio.edgeimpulse.com/v1)).

**Custom parameters**

You can specify custom arguments or parameters to your block by adding a [parameters.json](/tools/specifications/files/parameters-json) file in the root of your block directory. This file describes all arguments for your training pipeline, and is used to render custom UI elements for each parameter. For example, this parameters file:

```
[{
    "name": "Bucket",
    "type": "bucket",
    "param": "bucket-name",
    "value": "",
    "help": "The bucket where you're hosting all data"
},
{
    "name": "Bucket prefix",
    "value": "my-test-prefix/",
    "type": "string",
    "param": "bucket-prefix",
    "help": "The prefix in the bucket, where you're hosting the data"
}]
```

Renders the following UI when you run the transformation block:

<Frame caption="Running a transformation block with custom parameters">
  <img src="https://mintcdn.com/edgeimpulse/x9Ga-7v4NxdQ7jXX/.assets/images/image%20(6).png?fit=max&auto=format&n=x9Ga-7v4NxdQ7jXX&q=85&s=122f826b6c39dbd7bfeb9bcbffecd095" alt="" width="1581" height="1000" data-path=".assets/images/image (6).png" />
</Frame>

And the options are passed in as command line arguments to your block:

```
--bucket-name "ei-data-dev" --bucket-prefix "my-test-prefix/"
```

For more information, and all options see [parameters.json](/tools/specifications/files/parameters-json).


Built with [Mintlify](https://mintlify.com).