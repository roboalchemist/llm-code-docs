# Source: https://docs.edgeimpulse.com/tutorials/topics/lifecycle-management/acquire-process-golioth.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Acquire and process data using Golioth on AI

In this tutorial we will demonstrate how to securely collect and process sensor data from a managed device with the [Golioth on AI](https://blog.golioth.io/golioth-for-ai/?utm_source=press-release\&utm_medium=link\&utm_campaign=ai-launch\&utm_term=globe-newswire) example project. The managed device is connected via cellular and streams labeled but unstructured data to a mutually accessible Object Storage (S3 Bucket), by collecting labeled sensor data in this method we can also demonstrate a common use for this form of data acquisition, performing automated Data processing or Data Quality steps to the collected data via custom  transformation blocks.

We will then apply data processing steps on the collected data using the custom CBOR transformation block to convert this data to a format we can use to later train a model. This same process can be adapted to perform Data Quality techniques that would typically be performed by an ML engineer.

## Prerequisites

To follow along with this example, ensure that you have the following:

* [Golioth account](https://console.golioth.io/) with an organization and a connected compatible device (e.g., nrf9160).
* Edge Impulse enterprise account.
* Trained Edge Impulse project ready for deployment.
* AWS account with access to S3.
* Basic knowledge of AWS S3, Docker, and Zephyr.
* Example from the Golioth on AI tutorial repository [here](https://github.com/golioth/example-edge-impulse)

This tutorial was created for the Golioth on AI launch see the associated video on youtube [Read it here](https://blog.golioth.io/golioth-for-ai/?utm_source=press-release\&utm_medium=link\&utm_campaign=ai-launch\&utm_term=globe-newswire).

<iframe src="https://www.youtube.com/embed/9EThibFTZOY" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

### Step 1: Create a Managed Golioth Device with Configured Firmware

Before proceeding with the integration, ensure that your Golioth device is set up with the appropriate firmware. For detailed instructions on initializing your Zephyr workspace, building, and flashing the firmware, please refer to the [Golioth on AI repository README](https://github.com/golioth/example-edge-impulse).

### 1. Initialize the Zephyr workspace:

* Clone the Golioth on AI repository and initialize the Zephyr workspace with the provided manifest file.

```bash  theme={"system"}
  west init -m https://github.com/golioth/example-edge-impulse.git --mf west-ncs.yml
  west update
```

### 2. Create a project on Golioth.

* Log in to Golioth and create a new project. This project will handle the routing of sensor data and classification results.

### 3. Create a project on Edge Impulse.

* Log in to Edge Impulse Studio and create a new project. This project will receive and process the raw accelerometer data uploaded from the S3 bucket.

## Step 2: Create Golioth Pipelines

Once your device is set up, follow the instructions in the repository README to create the necessary Golioth pipelines. This includes setting up the Classification Results Pipeline and the Accelerometer Data Pipeline. Latest detailed steps can be found in the repository [Golioth on AI repository README](https://github.com/golioth/example-edge-impulse).

Golioth Pipelines allows you to route data between different services and devices efficiently. You will need to configure two pipelines for this demo:

### 1. Classification Results Pipeline:

* This pipeline routes classification results (e.g., gesture predictions) to Golioth's LightDB Stream, which stores data in a timeseries format.

* You will configure a path for classification results (e.g., /class) and ensure that the data is converted to JSON format.

### 2. Accelerometer Data Pipeline to S3:

* This pipeline handles raw accelerometer data by forwarding it to an S3 object storage bucket. Ensure the pipeline is set up to transfer binary data.

* Important: Configure your AWS credentials by creating secrets in Golioth for AWS\_ACCESS\_KEY and AWS\_SECRET\_KEY, and specify the target bucket name and region.

## Step 3: Deploy the Edge Impulse Inferencing Library

### 1. Generate the Model:

* Follow the instructions in the continuous motion recognition tutorial to generate a gesture recognition model.

### 2. Download and Extract the Library:

* Download the generated library from Edge Impulse Studio and extract the contents.

```bash  theme={"system"}
mkdir ei-generated
unzip -q <path-to-generated>.zip -d ei-generated/
mv ei-generated/edge-impulse-sdk/ .
mv ei-generated/model-parameters/ .
mv ei-generated/tflite-model/ .
```

### 3. Build and Flash Firmware:

* Build the firmware:

```bash  theme={"system"}
west build -p -b thingy91_nrf9160_ns app/
west flash

```

* Set Golioth Credentials::

```bash  theme={"system"}
  uart:~$ settings set golioth/psk-id <my-psk-id@my-project>
  uart:~$ settings set golioth/psk <my-psk>
```

* Add the same configuration to the Golioth secret store
* Navigate to your Golioth Secret Store:
  `https://console.golioth.io/org/<organization>/project/<application>/secrets`
* Add your AWS credentials (Access Key ID and Secret Access Key) and the S3 bucket details to the Golioth secret store.

<Frame caption="Golioth Secret Store">
  <img src="https://mintcdn.com/edgeimpulse/dNgo5Z6P3-vY-IBI/.assets/images/goliothai-2.png?fit=max&auto=format&n=dNgo5Z6P3-vY-IBI&q=85&s=bb3ab00e4c75a9183a63fc3932ff5e10" width="1600" height="821" data-path=".assets/images/goliothai-2.png" />
</Frame>

## Step 4: Data Acquisition

### 1. Trigger Data Acquisition:

* Press the button on the Nordic Thingy91 to start sampling data from the device's accelerometer.

### 2. Data Routing:

* Raw accelerometer data will be automatically routed to your S3 bucket via the Golioth pipeline. You can later import this data into Edge Impulse Studio for further model training.

### 3. View Classification Results:

* Classification results will be stored in Golioth's LightDB Stream. You can access this data for further analysis or visualization.

## Step 5: Import Data into Edge Impulse

### 1. Access Data from S3:

* In Edge Impulse Studio, use the Data acquisition page to import your raw accelerometer data directly from the S3 bucket

### 2. Label and Organize Data:

Once imported, label your data appropriately to prepare it for model training.

### Example Classification and Raw Data

Below is an example of classification data you can expect to see in the Golioth console:

```json  theme={"system"}

  {
    "idle": 0.28515625,
    "snake": 0.16796875,
    "updown": 0.21875,
    "wave": 0.328125
  }
```

Raw accelerometer data uploaded to S3 can be imported as an array of X-Y-Z float values, which will appear in the Edge Impulse Studio as time-series data.

## Step 6: Data Processing

From here we can perform a number of data processing steps on the collected data:

### 1. Data Transformation:

* Use the custom CBOR transformation block to convert raw accelerometer data to a format suitable for training a model in Edge Impulse.

### 2. Data Quality:

* Apply custom transformation blocks to perform data quality checks or preprocessing steps on the collected data.

### 3. Model Training:

* Import the transformed data into Edge Impulse Studio and train a new model using the collected accelerometer data.

### 4. Model Deployment:

* Deploy the trained model back to the Golioth device for real-time gesture recognition.

## Summary

In this tutorial, we demonstrated how to securely collect and process sensor data from a managed device using Golioth and Edge Impulse. By leveraging Golioth's data routing capabilities and Edge Impulse's machine learning tools, you can easily build and deploy custom models for gesture recognition or other applications. This example showcases the end-to-end workflow from data acquisition to model training and deployment, highlighting the seamless integration between Golioth and Edge Impulse.

For more information on Golioth and Edge Impulse, visit the official documentation and tutorials:

* [Golioth Documentation](https://docs.golioth.io)
* [Golioth on AI - Blog](https://blog.golioth.io/golioth-for-ai/?utm_source=press-release\&utm_medium=link\&utm_campaign=ai-launch\&utm_term=globe-newswire)


Built with [Mintlify](https://mintlify.com).