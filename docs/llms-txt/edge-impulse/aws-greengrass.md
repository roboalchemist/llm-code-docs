# Source: https://docs.edgeimpulse.com/tutorials/integrations/aws-greengrass.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# AWS IoT Greengrass

AWS IoT Greengrass is an AWS IoT service that enables edge devices with customizable/downloadable/installable "components" that can be run to augment what's running on the edge device itself.  AWS IoT Greengrass permits the creation and publication of a "Greengrass Component" that is effectively a set of instructions and artifacts that, when installed and run, create and initiate a custom specified service.

For more information about AWS IoT Core and AWS Greengrass please review: [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html)

## Overview

The Edge Impulse integration with AWS IoT Core and AWS IoT Greengrass is as follows:

<Frame caption="Architecture">
  <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/Greengrass/Architecture.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=bf9b51fcf673a30b279d2b24c66901c0" width="1106" height="729" data-path=".assets/images/Greengrass/Architecture.png" />
</Frame>

A few notable items:

* Edge Impulse Linux/Runner services now have a "--greengrass" option that enables the integration.
* AWS Secrets Manager is used to protect the Edge Impulse API Key by removing it from view via command line arguments
* The Greengrass Token Exchange Role must have Secrets Manager and IoT Core publication permission for the integration to operate correctly.
* Edge Impulse has several custom Greengrass components that can be deployed and run on the Greengrass-enabled edge device for several purposes outlined below. The component recipes and artifacts can be found here: [Repo](https://github.com/edgeimpulse/aws-greengrass-components).

For more information regarding the Edge Impulse Linux/Runner please review: [Edge Impulse for Linux Node.js SDK](/tools/libraries/sdks/inference/linux/node-js).

#### "EdgeImpulseLinuxServiceComponent" Greengrass Component

The "edge-impulse-linux-service" allows a linux-based edge device to register itself to the Edge Impulse studio service as a device capable of relaying its sensory (typically, camera, microphone, etc...) to the Edge Impulse service to be used for data creation and model testing. The associated Greengrass component for this service allows for easy/scalable deployment of this service to edge devices.

<Info>
  This component will attempt to capture camera devices so typically it cannot be installed in the same edge device that has the "edge-impulse-linux-runner" component (described below) at the same time.
</Info>

#### "EdgeImpulseLinuxRunnerServiceComponent" Greengrass Component

The "edge-impulse-linux-runner" service downloads, configures, installs, and executes an Edge Impulse model, developed for the specific edge device, and provides the ability to retrieve model inference results.  In this case, our component for this service will relay the inference results into AWS IoT Core under the following topic:

```
/edgeimpulse/device/<EdgeImpulseDeviceName>/inference/output
```

<Info>
  This component will attempt to capture camera devices so typically it cannot be installed in the same edge device that has the "edge-impulse-linux-runner" component (described prior) at the same time.
</Info>

#### "EdgeImpulseSerialRunnerServiceComponent" Greengrass Component

The "edge-impulse-run-impulse" service is typically used when you want to utilize a MCU-based device to run the Edge Impulse model and you further want that device tethered to an edge device via serial/usb connections to allow its inference results to be relayed upstream.  Like with the "edge-impulse-linux-runner" service, the "edge-impulse-run-impulse" component will relay inference results into AWS IoT Core via the same topic structure:

```
/edgeimpulse/device/<EdgeImpulseDeviceName>/inference/output
```

## Installation

The following sections outline how one installs AWS IoT Greengrass... then installs the Edge Impulse custom components for inclusion into a Greengrass deployment down to edge devices.

### 1. Install AWS IoT Greengrass Prerequisites

AWS IoT Greengrass is based on Java and thus a Java runtime must be installed. For most linux-based devices a suitable Java can be run by simply typing:

Debian-based Linux:

```
% sudo apt install -y default-jdk
```

Redhat-based Linux:

```
% sudo yum install -y default-jdk
```

Additionally, its recommended to update your linux device with the latest security patches and updates if available.

### 2. Install AWS IoT Greengrass

Greengrass is typically installed from within the AWS Console -> AWS IoT Core -> Greengrass -> Core Devices menu... select/press "Set up one core device". There are multiple ways to install Greengrass - "Nucleus Classic" is the version of Greengrass that is based on Java.  "Nucleus Lite" is a native version of Greengrass that is typically part of a Yocto-image based implementation.

In this example, we choose the "Linux" device type and we are going to download the installer for Greengrass and invoke it as part of the installation of a "Nucleus Classic" instance:

<Frame caption="CreateDevice">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/Greengrass/GG_Install_Device.png?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=3f42ccc1768b90c5c8c5647a1ad7fae3" width="1600" height="829" data-path=".assets/images/Greengrass/GG_Install_Device.png" />
</Frame>

Lower down in the menu, you will see the specific instructions that are custom-crafted for you to download and invoke the "Nucleus Classic" installer. Note that you will have to have previously created and set, within your shell environment, an AWS Access Key (typically with Administrator privilege) in order to run the installer:

<Frame caption="CreateDevice">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/Greengrass/GG_Install_Device2.png?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=5a40938bcb4c2178ded234b24e97cde0" width="1600" height="772" data-path=".assets/images/Greengrass/GG_Install_Device2.png" />
</Frame>

### 3. Install defaulted AWS IoT Greengrass components

When doing a Greengrass installation/deployment, a default deployment for the target device will typically get created and that deployment will install the two components below.  If one is not created, it is recommended that you create a deployment in Greengrass for your newly added Greengrass edge device and add the following available AWS Components:

```
aws.greengrass.Cli
aws.greengrass.Nucleus
```

### 4. Modify the Greengrass TokenExchange Role with additional permissions

When you run a Greengrass component within Greengrass, a service user (typically a linux user called "ggc\_user" for "Nucleus Classic" installations) invokes the component, as specified in the lifecycle section of your recipe. Credentials are passed to the invoked process via its environment (NOT by the login environment of the "Greengrassc\_user"...) during the invocation spawning process. These credentials are used by by the spawned process (typically via the AWS SDK which is part of the spawned process...) to connect back to AWS and "do stuff". These permissions are controlled by a AWS IAM Role called "GreengrassV2TokenExchangeRole".  We need to modify that role and add "Full AWS IoT Core Permission" as well as "AWS Secrets Manager Read/Write" permission.

To modify the role, from the AWS Console -> IAM -> Roles search for "GreengrassV2TokenExchangeRole", Then:

1. Select "GreengrassV2TokenExchangeRole" in the search results list
2. Select "Add Permissions" -> "Attach Policies"
3. Search for "AWSIoTFullAccess", select it, then press "Add Permission" down at the bottom
4. Repeat the search for "S3FullAccess" and "SecretsManagerReadWrite"

<Frame caption="TERUpdate">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/Greengrass/IAM_TER_Update.png?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=38e5fb5d8c0cb7f0d283255351444677" width="1600" height="773" data-path=".assets/images/Greengrass/IAM_TER_Update.png" />
</Frame>

When done, your GreengrassV2TokenExchangeRole should now show that it has "AWSIoTFullAccess", "S3FullAccess" and "SecretsManagerReadWrite" permissions added to it.

### 5. Clone the repo to acquire the Edge Impulse Component recipes and artifacts

Clone this repo to retrieve the Edge Impulse component recipes (yaml files) and the associated artifacts: [Repo](https://github.com/edgeimpulse/aws-greengrass-components).

### 6. Upload Edge Impulse Greengrass Component artifacts into AWS S3

First, you need to go to the S3 console in AWS via AWS Console -> S3. From there, you will create an S3 bucket.  For sake of example, we name this bucket "MyS3Bucket123".

<Frame caption="CreateS3Bucket">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/Greengrass/S3_Create_Bucket.png?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=3ad3add5e346b6354fb3bb0471f9226a" width="1099" height="917" data-path=".assets/images/Greengrass/S3_Create_Bucket.png" />
</Frame>

Next, the following directory structure needs to be created your new bucket:

```
./artifacts/EdgeImpulseServiceComponent/1.0.0
```

Next, navigate to the "1.0.0" directory in your S3 bucket and then press "Upload" to upload the artifacts into the bucket. You need to upload the following files (these will be located in the ./artifacts/EdgeImpulseServiceComponent/1.0.0 from your cloned repo starting in the "AWSGreengrassComponents" subdirectory). Please upload ALL of these files into S3 at the above directory location:

```
	aws-iotcore-connector.ts
	launch.sh
	run.sh
	aws-iotcore-serial-scraper.ts
	launch_serial.sh
	run_serial.sh
	install.sh
	package.json
	stop.sh
	install_serial.sh
	parser.sh
```

Your S3 Bucket contents should look like this:

<Frame caption="UploadToS3">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/Greengrass/S3_Upload_Artifacts.png?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=9c27b14da46283c87f00847d059d9446" width="1549" height="636" data-path=".assets/images/Greengrass/S3_Upload_Artifacts.png" />
</Frame>

### 7. Customize the component recipe files

Next we need to customize our Greengrass component recipe files to reflect the actual location of our artifacts stored in S3.  Please replace ALL occurrences of "YOUR\_S3\_ARTIFACT\_BUCKET" with your S3 bucket name (i.e. "MyS3Bucket123"). Please do this for each of the 3 yaml files you have in your cloned repo under "./AWSGreengrassComponents".

Additionally, we can customize the defaulted configuration of your custom component by  editing, within each yaml file, the default configuration JSON.  Each yaml file's JSON is DIFFERENT... so don't edit one then copy to the other 2 yaml files... that will break your components.  You must edit each yaml file separately without copy/paste of this json information.

The default configuration contains the following attributes:

```
EdgeImpulseLinuxServiceComponent.yaml:
{
	"node_version": "20.12.1",
	"vips_version": "8.12.1",
	"device_name": "MyEdgeImpulseDevice",
	"launch": "linux",
	"sleep_time_sec": 10,
	"lock_filename": "/tmp/ei_lockfile_linux",
	"gst_args": "__none__",
	"eiparams": "--greengrass",
	"iotcore_backoff": "5",
	"iotcore_qos": "1",
	"ei_bindir": "/usr/local/bin",
	"ei_sm_secret_id": "EI_API_KEY",
	"ei_sm_secret_name": "ei_api_key",
	"ei_ggc_user_groups": "video audio input users",
	"install_kvssink": "no",
	"publish_inference_base64_image": "no",
	"enable_cache_to_file": "no",
	"ei_poll_sleeptime_ms": 2500,
	"ei_local_model_file": "__none__",
	"ei_shutdown_behavior": "__none__",
	"cache_file_directory": "__none__",
	"enable_threshold_limit": "no",
	"metrics_sleeptime_ms": 30000,
	"default_threshold": 50.0,
	"threshold_criteria": "ge",
	"enable_cache_to_s3": "no",
	"s3_bucket": "__none__",
}

EdgeImpulseLinuxRunnerServiceComponent.yaml:
{
	"node_version": "20.12.1",
	"vips_version": "8.12.1",
	"device_name": "MyEdgeImpulseDevice",
	"launch": "runner",
	"sleep_time_sec": 10,
	"lock_filename": "/tmp/ei_lockfile_runner",
	"gst_args": "__none__",
	"eiparams": "--greengrass",
	"iotcore_backoff": "5",
	"iotcore_qos": "1",
	"ei_bindir": "/usr/local/bin",
	"ei_sm_secret_id": "EI_API_KEY",
	"ei_sm_secret_name": "ei_api_key",
	"ei_ggc_user_groups": "video audio input users",
	"install_kvssink": "no",
	"publish_inference_base64_image": "no",
	"enable_cache_to_file": "no",
	"ei_poll_sleeptime_ms": 2500,
	"ei_local_model_file": "__none__",
	"ei_shutdown_behavior": "__none__",
	"cache_file_directory": "__none__",
	"enable_threshold_limit": "no",
	"metrics_sleeptime_ms": 30000,
	"default_threshold": 50.0,
	"threshold_criteria": "ge",
	"enable_cache_to_s3": "no",
	"s3_bucket": "__none__",
}

EdgeImpulseSerialRunnerServiceComponent.yaml:
{
	"node_version": "20.12.1",
	"device_name": "MyEdgeImpulseDevice",
	"sleep_time_sec": 10,
	"lock_filename": "/tmp/ei_lockfile_serial_runner",
	"iotcore_backoff": "5",
	"iotcore_qos": "1",
	"ei_bindir": "/usr/local/bin",
	"ei_ggc_user_groups": "video audio input users dialout"
}
```

#### Attribute Description

The attributes in each of the above default configurations is outlined below:

* **node\_version**: Version of NodeJS to be installed by the component
* **vips\_version**: Version of the libvips library to be compiled/installed by the component
* **device\_name**:  Template for the name of the device in EdgeImpulse... a unique suffix will be added to the name to prevent collisions when deploying to groups of devices
* **launch**: service launch type (typically just leave this as-is)
* **sleep\_time\_sec**: wait loop sleep time (component lifecycle stuff... leave as-is)
* **lock\_filename**: name of lock file for this component (leave as-is)
* **gst\_args**: optional GStreamer args, spaces replaced with ":", for custom video invocations
* **eiparams**: additional parameters for launching the Edge Impulse service (leave as-is)
* **iotcore\_backoff**:  number of inferences to "skip" before publication to AWS IoTCore... this is used to control publication frequency (AWS \$\$...)
* **iotcore\_qos**: MQTT QoS (typically leave as-is)
* **ei\_bindir**: Typical location of where the Edge Impulse services are installed (leave as-is)
* **ei\_ggc\_user\_groups**: A list of additional groups the Greengrass service user account will need to be a member of to allow the Edge Impulse service to invoke and operate correctly (typically leave as-is). For JetPack v6.x and above, please add "render" as an additional group.
* **ei\_sm\_secret\_id**: ID of the Edge Impulse API Key within AWS Secret Manager
* **ei\_sm\_secret\_name**: Name of the Edge Impulse API Key within AWS Secret Manager
* **install\_kvssink**: Option (default: "no", on: "yes") to build and make ready the kvssink gstreamer plugin
* **publish\_inference\_base64\_image**: Option (default: "no", on: "yes") to include a base64 encoded image that the inference result was based on
* **enable\_cache\_to\_file**: Option (default: "no", on: "yes") to enable both inference and associated image to get written to a specified local directory as a pair: `<guid>.img`  and `<guid>.json` for each inference identified with a `<guid>`
* **cache\_file\_directory**: Option (default: "**none**") to specify the local directory when enable\_cache\_to\_file is set to "yes"

#### New options (January 2025 Integration Enhancements)

In the 2025 updated integration, the following additional component recipe attributes are required:

* **ei\_poll\_sleeptime\_ms**: time (in ms) for the long polling message processor (typically leave as-is)
* **ei\_local\_model\_file**: option to utilize a previously installed local model file
* **ei\_shutdown\_behavior**: option to alter the shutdown behavior of the linux runner process. (can be set to "wait\_for\_restart" to cause the runner to pause after running the model and wait for the "restart" command to be issued (see "Commands" below for more details on the "restart" command))
* **enable\_threshold\_limit**: option to enable/disable the threshold confidence filter (must be "yes" or "no". Default is "no")
* **metrics\_sleeptime\_ms**: option to publish the model metrics statistics (time specified in ms).
* **default\_threshold**: option to specify threshold confidence filter "limit" (a value between 0 \< x \<= 1.0). Default setting is 0.7
* **threshold\_criteria**:  option to specify the threshold confidence filter criteria (must be one of: "gt", "ge", "eq", "le", or "lt")
* **enable\_cache\_to\_s3**: option to enable caching the inference image/result to an AWS S3 bucket
* **s3\_bucket**: name of the optional S3 bucket to cache results into

### 8. Gather and install an EdgeImpulse API Key into AWS Secrets Manager

First we have to create an API Key in Edge Impulse via the Studio.

Next, we will go into AWS Console -> Secrets Manager and press "Store a new secret". From there we will specify:

1. Select "Other type of secret"
2. Enter "ei\_api\_key" as the key NAME for the secret (goes in the "Key" section)
3. Enter our actual API Key (goes in the "Value" section)
4. Press "Next"
5. Enter "EI\_API\_KEY" for the "Secret Name" (actually, this is its Secret ID...)
6. Press "Next"
7. Press "Next"
8. Press "Store"

<Frame caption="CreateSecret">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/Greengrass/SM_Create_Secret.png?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=ad32e040ab8275dbeeb32180c2422ae1" width="1600" height="626" data-path=".assets/images/Greengrass/SM_Create_Secret.png" />
</Frame>

### 9. Register the custom component via its recipe file

From the AWS Console -> IoT Core -> Greengrass -> Components, select "Create component". Then:

1. Select the "yaml" option to Enter the recipe
2. Clear the text box to remove the default "hello world" yaml recipe
3. Copy/Paste the entire/edited contents of your EdgeImpulseLinuxServiceComponent.yaml file
4. Press "Create Component"

<Frame caption="CreateComponent">
  <img src="https://mintcdn.com/edgeimpulse/U4x1b15m-R6msMsX/.assets/images/Greengrass/GG_Create_Component.png?fit=max&auto=format&n=U4x1b15m-R6msMsX&q=85&s=5903205bf79b5040757f959352c0350a" width="1050" height="1000" data-path=".assets/images/Greengrass/GG_Create_Component.png" />
</Frame>

If formatting and artifact access checks out OK, you should have a newly created component listed in your Custom Components AWS dashboard.  You will need to repeat these steps for the other 2 components:

```
EdgeImpulseLinuxRunnerServiceComponent.yaml
EdgeImpulseSerialRunnerServiceComponent.yaml
```

### 10. Deploy the custom component to a selected Greengrass edge device or group of edge devices.

Almost done!  We can now go back to the AWS Console -> IoT Core -> Greengrass -> Deployments page and select a deployment (or create a new one!) to deploy our component down to as selected gateway or group of gateways as needed.

<Frame caption="GGDeploy">
  <img src="https://mintcdn.com/edgeimpulse/8kB6BRmB5KYHTUny/.assets/images/Greengrass/GG_Create_Deployment.png?fit=max&auto=format&n=8kB6BRmB5KYHTUny&q=85&s=a53fa2ac80532889f435ba64238eb8a7" width="1316" height="851" data-path=".assets/images/Greengrass/GG_Create_Deployment.png" />
</Frame>

When performing the deployment, its quite common to, when selecting one of our newly created custom components, to then "Customize" that component by selecting it for "Customization" and entering a new JSON structure (same structure as what's found in the component's associated YAML file for the default configuration) that can be adjusted for a specific deployment (i.e. perhaps your want to change the DeviceName for this particular deployment or specify "gst\_args" for a specific edge device(s) camera, etc...). This highlights the power and utility of the component and its deployment mechanism in AWS IoT Greengrass.

## Running

After the deployment is initiated, on the FIRST invocation of a given deployment, expect to wait several moments (upwards of 5-10 min in fact) while the component installs all of the necessary pre-requisites that the component requires... this can take some time so be patient. You can also log into the edge gateway, receiving the component, and examine log files found in /greengrass/v2/logs. There you will see each components' current log file (same name as the component itself... ie. EdgeImpulseLinuxServiceComponent.log...) were you can watch the installation and invocation as it happens... any errors you might suspect will be shown in those log files.

While the components are running, in addition to the /greengrass/v2/logs directory, each component has a runtime log in /tmp.  The format of the log file is: "ei\_lockfile\_\[linux | runner | serial]\_\<EI DEVICE>.log.  Users can "tail" that log file to watch the component while it is running.

Additionally, for Jetson-based devices where the model has been compiled specifically for that platform, one can expect to have a 2-3 minute delay in the model being loaded into the GPU memory for the first time.  Subsequent invocations will be very short.

## Model Metrics (January 2025 Integration Enhancements)

Basic model metrics are now accumulated and published in the integration into IoT Core. The metrics will be published at specified intervals (per the "metrics\_sleeptime\_ms" component configuration parameter) to the following IoT Core topic:

```
/edgeimpulse/device/<EdgeImpulseDeviceName>/model/metrics
```

The metrics published are:

* **accumulated mean**: running accumulation of the average confidences from the linux runner while running the current model
* **accumulated standard deviation**: running accumulation of the standard deviation from the linux runner while running the current model

The format of the model metrics output is as follows:

```
{
	"mean_confidence": 0.696142,
	"standard_deviation": 0.095282,
	"confidence_trend": "decr",
	"details": {
	"n": 5,
	"sum_confidences": 3.480711,
	"sum_confidences_squared": 2.468464
	},
	"ts": 1736016142920,
	"id": "e4faa78b-2a09-40d1-adfd-8e5fc32feb11"
}
```

## Commands (January 2025 Integration Enhancements)

In the 2025 January integration update, the following commands are now available with the Edge Impulse Greengrass Linux Runner Greengrass integration. The following commands are dispatched via the integration's IoT Core Topic as a JSON:

```
/edgeimpulse/device/<EdgeImpulseDeviceName>/command/input
```

Results from the command can be found using the following topic:

```
/edgeimpulse/device/<EdgeImpulseDeviceName>/command/output
```

Command JSON structure is defined as follows:

```
{
	"cmd": <command verb>,
	"value": <if command is a "set" command, setting value goes here>
}
```

The currently supported commands are described below:

### Initial Invocation

When the runner process is started/restarted, the following JSON will be published to the command output topic above:

```
{
	"result": {
	"status": "started",
	"ts": 1736026956853,
	"id": "5c4e627e-6e9d-4382-bba7-00c0129705c4"
	}
}
```

This JSON can be used to flag a new invocation of the runner service (or a restart of the runner service). If there are any previous runtime changes made (i.e. confidence filter settings for example... see below), those changes can be resent to the newly invoked runtime.

### Restart Command

##### Command JSON:

```
{
	"cmd": "restart"
}
```

##### Command Description:

This command directs the integration to "restart" the Edge Impulse linux runner process. In conjunction with the "ei\_shutdown\_behavior" option being set to "wait\_for\_restart", the linux runner process will continue operating after the model has completed its operation. The linux runner process will continue to process input commands and will restart the linux runner via dispatching this command.

### Enable Threshold Filter Command

##### Command JSON:

```
{
	"cmd": "enable_threshold_filter"
}
```

##### Command Description:

This command directs the integration to enable the threshold filter.  The filter will control which inferences will get published into IoT Core. By default the filter is disabled so that all inferences reported are sent into IoT Core.

##### Command Result:

The command output will be published as follows and will include the filter config:

```
{
	"result": {
	"threshold_filter_config": {
		"enabled": "yes",
		"confidence_threshold": 0.7,
		"threshold_criteria": "ge"
	}
	}
}
```

### Disable Threshold Filter Command

##### Command JSON:

```
{
	"cmd": "disable_threshold_filter"
}
```

##### Command Description:

This command directs the integration to disable the threshold filter.

##### Command Result:

The command output will be published as follows and will include the filter config:

```
{
	"result": {
	"threshold_filter_config": {
		"enabled": "no",
		"confidence_threshold": 0.7,
		"threshold_criteria": "ge"
	}
	}
}
```

### Set Threshold Filter Criteria Command

##### Command JSON:

```
{
	"cmd": "set_threshold_filter_criteria",
	"value": "ge"
}
```

##### Command Description:

This command directs the integration to set the threshold filter criteria. The available options for the criteria are:

* **"gt"**: publish if inference confidence is "greater than"...
* **"ge"**: publish if inference confidence is "greater than or equal to"...
* **"eq"**: publish if inference confidence is "equal to"...
* **"le"**: publish if inference confidence is "less than or equal to"...
* **"gt"**: publish if inference confidence is "less than"...

##### Command Result:

The command output will be published as follows:

```
{
	"result": {
	"criteria": "gt"
	}
}
```

### Get Threshold Filter Criteria Command

##### Command JSON:

```
{
	"cmd": "get_threshold_filter_criteria"
}
```

##### Command Description:

This command directs the integration to get the threshold filter criteria. The currently set threshold criteria is published to the command output topic above.

##### Command Result:

The command output will be published as follows with the configured criteria:

```
{
	"result": {
	"criteria": "gt"
	}
}
```

### Set Threshold Filter Confidence Command

##### Command JSON:

```
{
	"cmd": "set_threshold_filter_confidence",
	"value": 0.756
}
```

##### Command Description:

This command directs the integration to set the threshold filter confidence bar. The value set must be a value 0 \< x \<= 1.0

##### Command Result:

The command output will be published as follows with the specified confidence bar:

```
{
	"result": {
	"confidence_threshold": "0.756"
	}
}
```

### Get Threshold Filter Confidence Command

##### Command JSON:

```
{
	"cmd": "get_threshold_filter_confidence"
}
```

##### Command Description:

This command directs the integration to get the threshold filter confidence bar. The currently set threshold confidence value is published to the command output topic above.

##### Command Result:

The command output will be published as follows with the currently configured confidence bar:

```
{
	"result": {
	"confidence_threshold": "0.756"
	}
}
```

### Get Threshold Filter Config Command

##### Command JSON:

```
{
	"cmd": "get_threshold_filter_config"
}
```

##### Command Description:

This command directs the integration to retrieve the current threshold filter config. The currently set threshold filter config is published to the command output topic above.

##### Command Result:

The command output will be published as follows with the currently configured filter config:

```
{
	"result": {
	"threshold_filter_config": {
		"enabled": "no",
		"confidence_threshold": "0.756",
		"threshold_criteria": "gt"
	}
	}
}
```

### Get Model Info Command

##### Command JSON:

```
{
	"cmd": "get_model_info"
}
```

##### Command Description:

This command directs the integration to retrieve the currently running model information. The model information is published to the command output topic above.

##### Command Result:

The command output will be published as follows with the current model information:

```
{
	"result": {
	"model_info": {
		"model_name": "occupant_counter",
		"model_version": "v25",
		"model_params": {
		"axis_count": 1,
		"frequency": 0,
		"has_anomaly": 0,
		"image_channel_count": 3,
		"image_input_frames": 1,
		"image_input_height": 640,
		"image_input_width": 640,
		"image_resize_mode": "fit-longest",
		"inferencing_engine": 6,
		"input_features_count": 409600,
		"interval_ms": 1,
		"label_count": 1,
		"labels": [
			"person"
		],
		"model_type": "object_detection",
		"sensor": 3,
		"slice_size": 102400,
		"threshold": 0.5,
		"use_continuous_mode": false,
		"sensorType": "camera"
		}
	}
	}
}
```

### Reset Model Metrics Command

##### Command JSON:

```
{
	"cmd": "reset_metrics"
}
```

##### Command Description:

This command directs the integration to reset the model metrics counters.

##### Command Result:

The command output will be published as follows to indicate the metrics counters are reset:

```
{
	"result": {
	"metrics_reset": "OK"
	}
}
```

### Clear Cache Command

##### Command JSON:

```
{
	"cmd": "clear_cache"
}
```

##### Command Description:

This command directs the integration to clear the currently configured inference image cache. The entire cache will be cleared. This command is sensitive to the Greengrass component configuration (i.e. which inference caches are enabled/disabled). This command will clear ALL caches that are currently enabled in the component configuration.

##### Command Result:

The command output will be published as follows with the clear cache results:

```
{
	"result": {
	"clear_cache": {
		"local": "OK",
		"s3": "OK"
	}
	}
}
```

### Clear Specified File From Cache Command

##### Command JSON:

```
{
	"cmd": "clear_cache_file"
	"value": <uuid>
}
```

##### Command Description:

This command directs the integration to clear the specified file (by its uuid) from within the inference cache.  This command is sensitive to the Greengrass component configuration (i.e. which inference caches are enabled/disabled).  This command will clear the specified file from ALL enabled caches per the component configuration.

##### Command Result:

The command output will be published as follows with the clear cache results for the specified UUID:

```
{
	"result": {
	"clear_cache_file": {
		"local": "OK",
		"s3": "OK",
		"uuid": "e4faa78b-2a09-40d1-adfd-8e5fc32feb11"
	}
	}
}
```


Built with [Mintlify](https://mintlify.com).