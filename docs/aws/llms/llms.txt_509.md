# Source: https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/llms.txt

# Amazon Kinesis Video Streams Developer Guide

- [Set up notifications](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/notifications.html)
- [Troubleshooting](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/troubleshooting.html)
- [Document history](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/doc-history.html)

## [What is Amazon Kinesis Video Streams?](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/what-is-kinesis-video.html)

- [Region availability](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/availability.html): Amazon Kinesis Video Streams is available in the following regions:

### [How it works](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-it-works.html)

Overview of how you can stream video from devices to the AWS Cloud using Kinesis Video Streams.

- [API and producer libraries](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-it-works-kinesis-video-api-producer-sdk.html): Use the Kinesis Video Streams APIs to create and manage video streams and read or write data to and from a video stream.
- [Data model](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-data.html): Description of the model Kinesis Video Streams uses to store and read data.
- [System requirements](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/system-requirements.html): Information about software and hardware requirements for Kinesis Video Streams.
- [Quotas](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/limits.html): API service quotas for Amazon Kinesis Video Streams.
- [Tiered Storage](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/tiered-storage.html): Information about tiered storage for Kinesis Video Streams.
- [Set up an account](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-account.html): Before you use Amazon Kinesis Video Streams for the first time, complete the following tasks.
- [Benefits](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/benefits.html): Benefits of using Kinesis Video Streams include the following:


## [Getting started](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/getting-started.html)

- [Create an Amazon Kinesis video stream](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-createstream.html): Use the Amazon Kinesis Video Streams console or AWS CLI to create your first Kinesis video stream.
- [Send data to an Amazon Kinesis video stream](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-send-data.html): This section describes how to send media data from a camera to the Kinesis video stream that you created in the previous section.
- [Consume media data](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-consume-data.html): You can consume media data by either viewing it in the console, or by creating an application that reads media data from a stream using Hypertext Live Streaming (HLS).


## [Upload to Kinesis Video Streams](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-sdk.html)

### [Java](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-sdk-javaapi.html)

Download, install, configure, and run the Java producer library for Kinesis Video Streams.

- [Prerequisites](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-javaapi-prerequisites.html): Prerequisites for using the Java producer SDK procedure.
- [Download and configure the code](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-javaapi-downloadcode.html): Java producer library procedures to download and import the Java example code and configure the library locations.
- [Write and examine the code](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-javaapi-writecode.html): Java producer library procedures to write and examine the Java example code.
- [Clean up resources](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-javaapi-cleanup.html): Java Producer Library procedure - clean up resources.
- [Run and verify the code](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-javaapi-reviewcode.html): Java producer library procedure to run and verify the Java example code.

### [Android](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-sdk-android.html)

Download, install, configure, and run the Android producer library for Kinesis Video Streams.

- [Prerequisites](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-android-prerequisites.html): Prerequisites for using the Java producer SDK procedure.
- [Download and configure the code](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-android-downloadcode.html): Android producer library procedure to download and import the example code.
- [Examine the code](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-android-writecode.html): Android producer library procedures to examine the example code.
- [Run and verify the code](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-android-reviewcode.html): Android producer library procedure to run and verify the example code.

### [C++](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-sdk-cpp.html)

Download, install, configure, and run the C++ producer code example for Kinesis Video Streams.

- [Prerequisites](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-sdk-cpp-prerequisites.html): C++ producer SDK prerequisites.
- [Download and configure the code](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-cpp-download.html): C++ producer library procedures to download the C++ library and configure the sample application to use your credentials.
- [Write and examine the code](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-cpp-write.html): C++ producer library procedures to write the code and examine it in the C++ test harness.
- [Run and verify the code](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-cpp-test.html): C++ producer library procedures to run and verify the code.
- [Use the SDK as a GStreamer plugin](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-sdk-cpp-gstreamer.html): Procedures to use the C++ producer SDK as a GStreamer plugin.
- [Use the C++ producer SDK as a GStreamer plugin in a Docker container](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-sdk-cpp-gstreamer-docker.html): Procedures to use the C++ producer SDK as a GStreamer plugin in a Docker container.
- [Use logging](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-sdk-cpp-logging.html): Configure logging for C++ producer SDK applications in Kinesis Video Streams.

### [C producer](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-sdk-c-api.html)

Download, install, configure, and run the C producer code example for Kinesis Video Streams.

- [Prerequisites](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-sdk-c-prerequisites.html): Before you set up the C producer SDK, ensure that you have the following prerequisites:
- [Download the code](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-c-download.html): C producer library procedures to download the C library.
- [Write and examine the code](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-c-write.html): C producer library procedures to write the code and examine it in the C test harness.
- [Run and verify the code](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-c-test.html): C producer library procedures to run and verify the C code.

### [C++ on Raspberry Pi](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-cpp-rpi.html)

The Raspberry Pi is a small, inexpensive computer that can be used to teach and learn basic computer programming skills.

- [Prerequisites](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-cpp-rpi-prerequisites.html): Before you set up the C++ producer SDK on your Raspberry Pi, ensure that you have the following prerequisites:
- [Create a user](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-cpp-rpi-iam.html): If you haven't already done so, set up an AWS Identity and Access Management (IAM) user with permissions to write to a Kinesis video stream.
- [Join your network](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-cpp-rpi-wifi.html): If you are using an attached monitor and keyboard, proceed to .
- [Connect remotely](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-cpp-rpi-connect.html): If you are using an attached monitor and keyboard, proceed to .
- [Configure the camera](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-cpp-rpi-camera.html): Follow these steps to configure the Raspberry Pi camera module to send video from the device to a Kinesis video stream.
- [Install software prerequisites](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-cpp-rpi-software.html): The C++ producer SDK requires that you install the following software prerequisites on Raspberry Pi.
- [Download and build the C++ producer SDK](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-cpp-rpi-download.html): Follow the procedures below to download and build the Kinesis Video Streams C++ producer SDK.
- [Stream a live stream](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-cpp-rpi-run.html): To run the sample application, you need the following information:
- [Play back media](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producersdk-cpp-rpi-playback.html): Open the Kinesis Video Streams console and select the Stream name for the stream you created.
- [Troubleshooting](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/troubleshoot-rpi.html): If you encounter a build issue and want to try different CMake arguments, make sure to perform a clean build.
- [Error code reference](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-sdk-errors.html): Find information about errors and status codes for the Kinesis Video Streams Producer libraries.
- [NAL adaptation flags](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-reference-nal.html): Details about the flags that are available for the StreamInfo.NalAdaptationFlags enumeration in the Kinesis Video Streams Producer SDK.
- [Producer structures](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-reference-structures-producer.html): Details about the structures that are used to provide data in the Kinesis Video Streams Producer SDK.
- [Stream structures](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-reference-structures-stream.html): Use these structures to provide data to a video stream instance in Kinesis Video Streams.
- [Callbacks](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-reference-callbacks.html): Callback patterns that the Kinesis Video Streams Producer SDK uses to interact with applications.
- [Using streaming metadata](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-meta.html): Embed metadata in a Kinesis video stream.
- [Use IPv6 with Kinesis Video Streams](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/ipv6-support.html): You can configure Kinesis Video Streams to use IPv6 for both control plane and data plane operations.


## [Video playback](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-playback.html)

- [Playback requirements](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/video-playback-requirements.html): Amazon Kinesis Video Streams supports media encoded in multiple formats.
- [Playback with HLS](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/hls-playback.html): How to use HTTP Live Streaming (HLS) playback method to access Kinesis Video Streams.
- [Playback with MPEG-DASH](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/dash-playback.html): How to use MPEG-DASH playback method to access Kinesis Video Streams


## [Extract images from video streams](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/images.html)

### [Real-time image generation](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/s3-real-time-image-create.html)

Use Amazon Kinesis Video Streams to automatically extract images from video data in real-time and deliver them to Amazon S3.

- [Troubleshooting](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/s3-image-troubleshooting.html)


## [Access video analytics](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/access-video-analytics.html)

- [Consume metadata](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-meta-consume.html): To consume the metadata in a Kinesis video stream, use an implementation of MkvTagProcessor:

### [Stream using parser library](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/parser-library.html)

Describes how to set up and use the Kinesis video stream parser library.

- [Download the code](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/parser-library-download.html): In this section, you download the Java library and test code, and import the project into your Java IDE.
- [Examine the code](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/parser-library-write.html): In this section, you examine the Java library and test code, and learn how to use the tools from the library in your own code.
- [Run the code](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/parser-library-run.html): The Kinesis video stream parser library contains tools that are intended for you to use in your own projects.

### [Monitoring](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/monitoring.html)

Use this section to learn more about monitoring with Amazon Kinesis Video Streams.

- [Monitor metrics with CloudWatch](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/monitoring-cloudwatch.html): Use this section to monitor Amazon Kinesis Video Streams metrics with CloudWatch
- [Monitor the Amazon Kinesis Video Streams Edge Agent with CloudWatch](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/monitoring-edge-cloudwatch.html): Use this page to monitor Amazon Kinesis Video Streams Edge Agent via CloudWatch.
- [Log API Calls with CloudTrail](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/monitoring-cloudtrail.html): Overview of how you can use CloudTrail to log information about API calls in Amazon Kinesis Video Streams.


## [Schedule video recording and storage](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/edge.html)

### [Deploy in non-AWS IoT Greengrass mode](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-edge-outside.html)

Use this section to run the Amazon Kinesis Video Streams Edge Agent in non-AWS IoT Greengrass mode.

- [Install dependencies](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-install-dependencies.html): Use this topic to install dependencies on the device in order to run the Amazon Kinesis Video Streams Edge Agent.
- [Create resources for your IP camera RTSP URLs](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-create-resources-standalone.html): Use this topic to create Amazon Kinesis Video Streams and AWS Secrets Manager resources for your IP camera RTSP URLs.
- [Create an IAM permissions policy](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-iam-role.html): Use this topic to create an IAM permissions policy.
- [Create an IAM role](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-create-role.html): Use this topic to create an IAM role that can be assumed by AWS IoT in order to obtain temporary credentials from the AWS Security Token Service (AWS STS).
- [Create the AWS IoT role alias](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-create-role-alias.html): Use this topic to create an AWS IoT role alias for the IAM role.
- [Create the AWS IoT policy](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-create-policy.html): Use this topic to create an AWS IoT policy that will be attached to the device certificate.
- [Create an AWS IoT thing and get AWS IoT Core credentials](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-create-thing.html): Use this topic to create an AWS IoT thing and obtain credentials for AWS IoT Core.
- [Build the Edge Agent](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-build-agent.html): Use this topic to build the Amazon Kinesis Video Streams Edge Agent.
- [Install the CloudWatch agent](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-install-cloudwatch.html): Use this topic to install the CloudWatch agent on the device.
- [Run Edge Agent as a native process](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-run.html): Use this topic to run the Amazon Kinesis Video Streams Edge Agent as a native process.

### [Deploy to AWS IoT Greengrass](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-edge-gg.html)

Use this topic to deploy the Amazon Kinesis Video Streams Edge Agent to AWS IoT Greengrass to record and upload media from IP cameras.

- [Create an Ubuntu instance](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-ubuntu.html): Use this section to create an Ubuntu Amazon EC2 instance.
- [Set up the AWS IoT Greengrass core device](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-setup-gg.html): Use this section to install the AWS IoT Greengrass core nucleus software on the Amazon EC2 instance.
- [Create resources for your IP camera RTSP URLs](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-create-resources.html): Use this section to create the streams and secrets needed in AWS Secrets Manager.
- [Add permissions to the TES role](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-add-permissions.html): Use this topic to add permissions to the token exchange service (TES) role.
- [Install the Secret Manager component](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-install-secrets-manager.html): Use this section to install the AWS IoT Greengrass Secret Manager component on the device.
- [Deploy Edge Agent on the device](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-deploy-edge.html): Use this section to deploy the Amazon Kinesis Video Streams Edge Agent AWS IoT Greengrass component on the device.
- [Install the AWS IoT Greengrass log manager component](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-publish-edge.html): Use this topic to configure the Amazon Kinesis Video Streams Edge Agent logs to automatically upload to CloudWatch using the AWS IoT Greengrass log manager component.
- [FAQ](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/edge-faq.html): Use this section to answer commonly asked questions about Amazon Kinesis Video Streams Edge Agent service.


## [Stream video through a VPC](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/vpc-endpoint.html)

- [VPC endpoint procedures](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/vpce-landing.html)


## [Examples](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/examples.html)

### [GStreamer Plugin - kvssink](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/examples-gstreamer-plugin.html)

Send video from a GStreamer plugin to the Kinesis Video Streams producer SDK.

- [Parameter reference](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/examples-gstreamer-plugin-parameters.html): Information about kvssink required and optional parameters for Kinesis Video Streams.
- [PutMedia API](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/examples-putmedia.html): Download and configure the Kinesis Video Streams PutMedia sample application.
- [RTSP and Docker](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/examples-rtsp.html): Sample application for Kinesis Video Streams that runs in a Docker container and streams video from an RTSP source.
- [Renderer](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/examples-renderer.html): Download and configure the Kinesis Video Streams Renderer example application.


## [API Reference](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_Reference.html)

### [Actions](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_Operations.html)

The following actions are supported by Amazon Kinesis Video Streams:

### [Amazon Kinesis Video Streams](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_Operations_Amazon_Kinesis_Video_Streams.html)

The following actions are supported by Amazon Kinesis Video Streams:

- [CreateSignalingChannel](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_CreateSignalingChannel.html): Creates a signaling channel.
- [CreateStream](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_CreateStream.html): Creates a new Kinesis video stream.
- [DeleteEdgeConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DeleteEdgeConfiguration.html): An asynchronous API that deletes a streamâs existing edge configuration, as well as the corresponding media from the Edge Agent.
- [DeleteSignalingChannel](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DeleteSignalingChannel.html): Deletes a specified signaling channel.
- [DeleteStream](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DeleteStream.html): Deletes a Kinesis video stream and the data contained in the stream.
- [DescribeEdgeConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeEdgeConfiguration.html): Describes a streamâs edge configuration that was set using the StartEdgeConfigurationUpdate API and the latest status of the edge agent's recorder and uploader jobs.
- [DescribeImageGenerationConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeImageGenerationConfiguration.html): Gets the ImageGenerationConfiguration for a given Kinesis video stream.
- [DescribeMappedResourceConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeMappedResourceConfiguration.html): Returns the most current information about the stream.
- [DescribeMediaStorageConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeMediaStorageConfiguration.html): Returns the most current information about the channel.
- [DescribeNotificationConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeNotificationConfiguration.html): Gets the NotificationConfiguration for a given Kinesis video stream.
- [DescribeSignalingChannel](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeSignalingChannel.html): Returns the most current information about the signaling channel.
- [DescribeStream](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeStream.html): Returns the most current information about the specified stream.
- [DescribeStreamStorageConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DescribeStreamStorageConfiguration.html): Retrieves the current storage configuration for the specified Kinesis video stream.
- [GetDataEndpoint](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_GetDataEndpoint.html): Gets an endpoint for a specified stream for either reading or writing.
- [GetSignalingChannelEndpoint](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_GetSignalingChannelEndpoint.html): Provides an endpoint for the specified signaling channel to send and receive messages.
- [ListEdgeAgentConfigurations](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_ListEdgeAgentConfigurations.html): Returns an array of edge configurations associated with the specified Edge Agent.
- [ListSignalingChannels](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_ListSignalingChannels.html): Returns an array of ChannelInfo objects.
- [ListStreams](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_ListStreams.html): Returns an array of StreamInfo objects.
- [ListTagsForResource](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_ListTagsForResource.html): Returns a list of tags associated with the specified signaling channel.
- [ListTagsForStream](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_ListTagsForStream.html): Returns a list of tags associated with the specified stream.
- [StartEdgeConfigurationUpdate](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_StartEdgeConfigurationUpdate.html): An asynchronous API that updates a streamâs existing edge configuration.
- [TagResource](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_TagResource.html): Adds one or more tags to a signaling channel only.
- [TagStream](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_TagStream.html): Adds one or more tags to a stream.
- [UntagResource](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_UntagResource.html): Removes one or more tags from a signaling channel only.
- [UntagStream](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_UntagStream.html): Removes one or more tags from a stream.
- [UpdateDataRetention](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_UpdateDataRetention.html): Increases or decreases the stream's data retention period by the value that you specify.
- [UpdateImageGenerationConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_UpdateImageGenerationConfiguration.html): Updates the StreamInfo and ImageProcessingConfiguration fields.
- [UpdateMediaStorageConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_UpdateMediaStorageConfiguration.html): Associates a SignalingChannel to a stream to store the media.
- [UpdateNotificationConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_UpdateNotificationConfiguration.html): Updates the notification information for a stream.
- [UpdateSignalingChannel](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_UpdateSignalingChannel.html): Updates the existing signaling channel.
- [UpdateStream](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_UpdateStream.html): Updates stream metadata, such as the device name and media type.
- [UpdateStreamStorageConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_UpdateStreamStorageConfiguration.html): Updates the storage configuration for an existing Kinesis video stream.

### [Amazon Kinesis Video Streams Media](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_Operations_Amazon_Kinesis_Video_Streams_Media.html)

The following actions are supported by Amazon Kinesis Video Streams Media:

- [GetMedia](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_dataplane_GetMedia.html): Use this API to retrieve media content from a Kinesis video stream.
- [PutMedia](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_dataplane_PutMedia.html): Use this API to send media data to a Kinesis video stream.

### [Amazon Kinesis Video Streams Archived Media](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_Operations_Amazon_Kinesis_Video_Streams_Archived_Media.html)

The following actions are supported by Amazon Kinesis Video Streams Archived Media:

- [GetClip](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_GetClip.html): Downloads an MP4 file (clip) containing the archived, on-demand media from the specified video stream over the specified time range.
- [GetDASHStreamingSessionURL](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_GetDASHStreamingSessionURL.html): Retrieves an MPEG Dynamic Adaptive Streaming over HTTP (DASH) URL for the stream.
- [GetHLSStreamingSessionURL](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_GetHLSStreamingSessionURL.html): Retrieves an HTTP Live Streaming (HLS) URL for the stream.
- [GetImages](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_GetImages.html): Managed support for images provides a fully managed way to get images from the video data streamed and stored in Kinesis Video Streams.
- [GetMediaForFragmentList](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_GetMediaForFragmentList.html): Gets media for a list of fragments (specified by fragment number) from the archived data in an Amazon Kinesis video stream.
- [ListFragments](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_ListFragments.html): Returns a list of objects from the specified stream and timestamp range within the archived data.

### [Amazon Kinesis Video Signaling Channels](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_Operations_Amazon_Kinesis_Video_Signaling_Channels.html)

The following actions are supported by Amazon Kinesis Video Signaling Channels:

- [GetIceServerConfig](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_signaling_GetIceServerConfig.html): Note: Before using this API, you must call the GetSignalingChannelEndpoint API to request the HTTPS endpoint.
- [SendAlexaOfferToMaster](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_signaling_SendAlexaOfferToMaster.html)

### [Amazon Kinesis Video WebRTC Storage](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_Operations_Amazon_Kinesis_Video_WebRTC_Storage.html)

The following actions are supported by Amazon Kinesis Video WebRTC Storage:

- [JoinStorageSession](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSession.html)
- [JoinStorageSessionAsViewer](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_webrtc_JoinStorageSessionAsViewer.html)

### [Data Types](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_Types.html)

The following data types are supported by Amazon Kinesis Video Streams:

### [Amazon Kinesis Video Streams](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_Types_Amazon_Kinesis_Video_Streams.html)

The following data types are supported by Amazon Kinesis Video Streams:

- [ChannelInfo](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_ChannelInfo.html): A structure that encapsulates a signaling channel's metadata and properties.
- [ChannelNameCondition](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_ChannelNameCondition.html): An optional input parameter for the ListSignalingChannels API.
- [DeletionConfig](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_DeletionConfig.html): The configuration details required to delete the connection of the stream from the Edge Agent.
- [EdgeAgentStatus](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_EdgeAgentStatus.html): An object that contains the latest status details for an edge agent's recorder and uploader jobs.
- [EdgeConfig](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_EdgeConfig.html): A description of the stream's edge configuration that will be used to sync with the Edge Agent IoT Greengrass component.
- [ImageGenerationConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_ImageGenerationConfiguration.html): The structure that contains the information required for the KVS images delivery.
- [ImageGenerationDestinationConfig](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_ImageGenerationDestinationConfig.html): The structure that contains the information required to deliver images to a customer.
- [LastRecorderStatus](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_LastRecorderStatus.html): The latest status of a stream's edge recording job.
- [LastUploaderStatus](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_LastUploaderStatus.html): The latest status of a streamâs edge to cloud uploader job.
- [ListEdgeAgentConfigurationsEdgeConfig](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_ListEdgeAgentConfigurationsEdgeConfig.html): A description of a single stream's edge configuration.
- [LocalSizeConfig](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_LocalSizeConfig.html): The configuration details that include the maximum size of the media (MaxLocalMediaSizeInMB) that you want to store for a stream on the Edge Agent, as well as the strategy that should be used (StrategyOnFullSize) when a stream's maximum size has been reached.
- [MappedResourceConfigurationListItem](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_MappedResourceConfigurationListItem.html): A structure that encapsulates, or contains, the media storage configuration properties.
- [MediaSourceConfig](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_MediaSourceConfig.html): The configuration details that consist of the credentials required (MediaUriSecretArn and MediaUriType) to access the media files that are streamed to the camera.
- [MediaStorageConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_MediaStorageConfiguration.html): A structure that encapsulates, or contains, the media storage configuration properties.
- [NotificationConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_NotificationConfiguration.html): Use this API to configure Amazon Simple Notification Service (Amazon SNS) notifications for when fragments become available in a stream.
- [NotificationDestinationConfig](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_NotificationDestinationConfig.html): The structure that contains the information required to deliver a notification to a customer.
- [RecorderConfig](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_RecorderConfig.html): The recorder configuration consists of the local MediaSourceConfig details that are used as credentials to access the local media files streamed on the camera.
- [ResourceEndpointListItem](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_ResourceEndpointListItem.html): An object that describes the endpoint of the signaling channel returned by the GetSignalingChannelEndpoint API.
- [ScheduleConfig](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_ScheduleConfig.html): This API enables you to specify the duration that the camera, or local media file, should record onto the Edge Agent.
- [SingleMasterChannelEndpointConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_SingleMasterChannelEndpointConfiguration.html): An object that contains the endpoint configuration for the SINGLE_MASTER channel type.
- [SingleMasterConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_SingleMasterConfiguration.html): A structure that contains the configuration for the SINGLE_MASTER channel type.
- [StreamInfo](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_StreamInfo.html): An object describing a Kinesis video stream.
- [StreamNameCondition](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_StreamNameCondition.html): Specifies the condition that streams must satisfy to be returned when you list streams (see the ListStreams API).
- [StreamStorageConfiguration](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_StreamStorageConfiguration.html): The configuration for stream storage, including the default storage tier for stream data.
- [Tag](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_Tag.html): A key and value pair that is associated with the specified signaling channel.
- [UploaderConfig](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_UploaderConfig.html): The configuration that consists of the ScheduleExpression and the DurationInMinutes details that specify the scheduling to record from a camera, or local media file, onto the Edge Agent.

### [Amazon Kinesis Video Streams Media](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_Types_Amazon_Kinesis_Video_Streams_Media.html)

The following data types are supported by Amazon Kinesis Video Streams Media:

- [StartSelector](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_dataplane_StartSelector.html): Identifies the chunk on the Kinesis video stream where you want the GetMedia API to start returning media data.

### [Amazon Kinesis Video Streams Archived Media](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_Types_Amazon_Kinesis_Video_Streams_Archived_Media.html)

The following data types are supported by Amazon Kinesis Video Streams Archived Media:

- [ClipFragmentSelector](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_ClipFragmentSelector.html): Describes the timestamp range and timestamp origin of a range of fragments.
- [ClipTimestampRange](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_ClipTimestampRange.html): The range of timestamps for which to return fragments.
- [DASHFragmentSelector](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_DASHFragmentSelector.html): Contains the range of timestamps for the requested media, and the source of the timestamps.
- [DASHTimestampRange](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_DASHTimestampRange.html): The start and end of the timestamp range for the requested media.
- [Fragment](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_Fragment.html): Represents a segment of video or other time-delimited data.
- [FragmentSelector](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_FragmentSelector.html): Describes the timestamp range and timestamp origin of a range of fragments.
- [HLSFragmentSelector](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_HLSFragmentSelector.html): Contains the range of timestamps for the requested media, and the source of the timestamps.
- [HLSTimestampRange](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_HLSTimestampRange.html): The start and end of the timestamp range for the requested media.
- [Image](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_Image.html): A structure that contains the Timestamp, Error, and ImageContent.
- [TimestampRange](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_reader_TimestampRange.html): The range of timestamps for which to return fragments.

### [Amazon Kinesis Video Signaling Channels](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_Types_Amazon_Kinesis_Video_Signaling_Channels.html)

The following data types are supported by Amazon Kinesis Video Signaling Channels:

- [IceServer](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_signaling_IceServer.html): A structure for the ICE server connection data.
- [Amazon Kinesis Video WebRTC Storage](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_Types_Amazon_Kinesis_Video_WebRTC_Storage.html): The following data types are supported by Amazon Kinesis Video WebRTC Storage:
- [Common Errors](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/CommonErrors.html): This section lists the errors common to the API actions of all AWS services.
- [Common Parameters](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/CommonParameters.html): The following list contains the parameters that all actions use for signing Signature Version 4 requests with a query string.


## [Security](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/security.html)

- [Data Protection](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-kms.html): How to use server-side encryption to protect data in Kinesis Video Streams.
- [Controlling access to Kinesis Video Streams resources using IAM](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-iam.html): How to use IAM roles and permissions to control access to Kinesis Video Streams resources
- [Controlling access to Kinesis Video Streams resources using AWS IoT](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-iot.html): How to use AWS IoT credentials and IAM roles and permissions to control access to Kinesis Video Streams resources.
- [Compliance Validation](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/akda-java-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy as well as specific Kinesis Video Streams features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/infrastructure-security.html): Learn how Amazon Kinesis Video Streams isolates service traffic.
- [Security Best Practices](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/security-best-practices.html): Amazon Kinesis Video Streams provides a number of security features to consider as you develop and implement your own security policies.
