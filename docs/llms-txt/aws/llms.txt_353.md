# Source: https://docs.aws.amazon.com/elemental-live/latest/ug/llms.txt

# AWS Elemental Live User Guide

> Learn about transcoding and encoding video using AWS Elemental Live.

- [Security](https://docs.aws.amazon.com/elemental-live/latest/ug/el-security.html)
- [Document history](https://docs.aws.amazon.com/elemental-live/latest/ug/doc-history.html)

## [What is AWS Elemental Live?](https://docs.aws.amazon.com/elemental-live/latest/ug/what-is-aws-elemental-live.html)

- [Information about using Elemental Live](https://docs.aws.amazon.com/elemental-live/latest/ug/live-finding-info.html): Information about AWS Elemental Live is available in the following guides and resources.
- [Interfaces for Elemental Live](https://docs.aws.amazon.com/elemental-live/latest/ug/live-intro-interfaces.html): Elemental Live can be controlled, configured, and monitored through the following interfaces.
- [How Elemental Live works](https://docs.aws.amazon.com/elemental-live/latest/ug/how-live-works.html): From the point of view of Elemental Live, a live streaming workflow that includes Elemental Live involves three systems:
- [Terminology](https://docs.aws.amazon.com/elemental-live/latest/ug/what-is-terminology.html)


## [Appliance performance](https://docs.aws.amazon.com/elemental-live/latest/ug/appliance_performance.html)

- [Recommended procedure](https://docs.aws.amazon.com/elemental-live/latest/ug/performance-recommended-procedure.html): Learn the recommended testing procedure to test the density of your workflows.
- [Recommendation: Continually upgrade](https://docs.aws.amazon.com/elemental-live/latest/ug/performance-recommended-upgrade.html): We strongly recommend that you always upgrade to the latest version of Elemental Live.

### [Measure performance](https://docs.aws.amazon.com/elemental-live/latest/ug/performance-measures.html)

Learn how to measure appliance performance.

- [CPU usage](https://docs.aws.amazon.com/elemental-live/latest/ug/performance-cpu-usage.html): Learn how to measure the CPU usage for the events running on an Elemental Live appliance.
- [RAM usage](https://docs.aws.amazon.com/elemental-live/latest/ug/performance-ram-usage.html): Learn how to measure RAM usage of events running on an Elemental Live appliance.
- [I/O bandwidth](https://docs.aws.amazon.com/elemental-live/latest/ug/performance-io-bandwidth.html): Learn how to measure the I/O bandwidth of the events running on an Elemental Live appliance.
- [System bandwidth](https://docs.aws.amazon.com/elemental-live/latest/ug/performance-system-bandwidth.html): Learn how to measure the system bandwidth of the events running on an Elemental Live appliance.
- [Log messages for performance](https://docs.aws.amazon.com/elemental-live/latest/ug/performance-via-logs.html): Learn how to read log messages to assess the performance of an Elemental Live appliance
- [Encoding and performance](https://docs.aws.amazon.com/elemental-live/latest/ug/performance-encoding-params.html): Learn about the video encoding parameters that affect the performance of an Elemental Live appliance.
- [Features and performance](https://docs.aws.amazon.com/elemental-live/latest/ug/performance-features.html): Learn about the Elemental Live parameters that affect the performance of an appliance.


## [Inputs](https://docs.aws.amazon.com/elemental-live/latest/ug/container-inputs.html)

### [Reference: Supported live inputs](https://docs.aws.amazon.com/elemental-live/latest/ug/ref-inputs-and-codecs.html)

Find out about the media sources that AWS Elemental Live supports: the source media types and protocols, and the source video and audio codecs.

- [Supported types](https://docs.aws.amazon.com/elemental-live/latest/ug/supported-inputs-live-types.html): Find out about the live media sources that AWS Elemental Live supports.
- [Supported codecs](https://docs.aws.amazon.com/elemental-live/latest/ug/supported-inputs-live-codecs.html): Find out about the video and audio codecs for the live sources types that AWS Elemental Live supports.
- [Ingesting HLS TS](https://docs.aws.amazon.com/elemental-live/latest/ug/codecs-rules-ingesting-hls-ts.html): Read the rules for ingesting content from an HLS TS source into AWS Elemental Live.
- [Ingesting MPEG-TS](https://docs.aws.amazon.com/elemental-live/latest/ug/codecs-rules-ingesting-mpeg-ts.html): Read the rules for ingesting content from MPEG-TS source into AWS Elemental Live.

### [Reference: Supported file inputs](https://docs.aws.amazon.com/elemental-live/latest/ug/ref-file-inputs-and-codecs.html)

Find out about the media sources that AWS Elemental Live supports: the source media types and protocols, and the source video and audio codecs.

- [Supported upstream systems](https://docs.aws.amazon.com/elemental-live/latest/ug/supported-inputs-file-types.html): Find out about the video and audio codecs for each supported type of file source in AWS Elemental Live.
- [Supported containers](https://docs.aws.amazon.com/elemental-live/latest/ug/supported-inputs-file-containers.html): Find out about the types of containers that are supported for file inputs in AWS Elemental Live.
- [Supported codecs](https://docs.aws.amazon.com/elemental-live/latest/ug/supported-inputs-file-codecs.html): Find out about the video and audio codecs for the file source types that AWS Elemental Live supports.
- [Interleave 4K Inputs](https://docs.aws.amazon.com/elemental-live/latest/ug/interleave-2si-inputs.html): Learn how to set up an event to include a 4K input that is formatted as 2SI (2 Sample Interleave).

### [SMPTE 2022-6 inputs](https://docs.aws.amazon.com/elemental-live/latest/ug/input-2022-6.html)

Learn how to set up an AWS Elemental Live event to ingest an uncompressed video source that is compliant with SMPTE 2022-6.

- [Appliance requirements](https://docs.aws.amazon.com/elemental-live/latest/ug/input-2022-6-prereqs.html): Learn about the Elemental Live appliance that you need in order to ingest with SMPTE 2022-6 sources.
- [Supported content](https://docs.aws.amazon.com/elemental-live/latest/ug/2022-6-inputs-supported-content.html): Learn about the characteristics of the uncompressed video, audio, and ancillary data that AWS Elemental Live can ingest from a SMPTE 2022-6 source.
- [Get ready: Remove bonded interfaces](https://docs.aws.amazon.com/elemental-live/latest/ug/s2022-6-setup-bonded-interface.html): Learn how to remove bonded interfaces on the Elemental Live appliance, in order to work with video sources that are compliant with SMPTE 2022-6.
- [Get ready: Reserve processing cores](https://docs.aws.amazon.com/elemental-live/latest/ug/enable-2022-6.html): Learn how to set up the appliance for SMPTE 2022-6 in Elemental Live.
- [Set up the input](https://docs.aws.amazon.com/elemental-live/latest/ug/setup-2022-6-input-2022-7.html): Learn how to set up an AWS Elemental Live event to ingest a SMPTE 2022-6 source input, either including or excluding SMPTE 2022-7 seamless protection switching.

### [SMPTE 2038 ancillary data](https://docs.aws.amazon.com/elemental-live/latest/ug/smpte-2038.html)

Learn how to set up Elemental Live to extract ancillary data from SMPTE 2038 packets that are in a TS source.

- [Supported ancillary data](https://docs.aws.amazon.com/elemental-live/latest/ug/s2038-data-supported.html): Elemental Live can ingest several types of ancillary data.
- [Well-formed SMPTE 2038 source](https://docs.aws.amazon.com/elemental-live/latest/ug/s2038-data-well-formed.html): For Elemental Live to handle the ancillary data, the SMPTE 2038 must meet certain criteria:
- [Enable SMPTE 2038](https://docs.aws.amazon.com/elemental-live/latest/ug/s2038-data-enable.html): You must set up the input to ingest the SMPTE 2038 ancillary data.
- [Set up to use the data](https://docs.aws.amazon.com/elemental-live/latest/ug/s2038-data-use-data.html): After you have enabled SMPTE 2038, you should specify how you want Elemental Live to use the timecode, captions, AFD signals, and SCTE 104 messages that it detects.
- [Set up to pass through custom data](https://docs.aws.amazon.com/elemental-live/latest/ug/s2038-data-passthrough-custom-data.html): After you have enabled SMPTE 2038, you can identify the custom data to extract, and then set up to include that data in your SMPTE 2110 outputs.

### [SMPTE 2110 inputs](https://docs.aws.amazon.com/elemental-live/latest/ug/input-2110.html)

Learn how to set up an AWS Elemental Live event to ingest a video source that is compliant with SMPTE 2110, either with or without NMOS.

- [Get ready](https://docs.aws.amazon.com/elemental-live/latest/ug/input-2110-get-ready.html): Before you set up a SMPTE 2110 input in an event, read the following information:

### [SMPTE 2110 using NMOS](https://docs.aws.amazon.com/elemental-live/latest/ug/setup-2110-input-nmos.html)

Learn how to make use of your organization's NMOS registry and NMOS controller to deliver SMPTE 2110 content to an Elemental Live event.

- [Step 1: Enable NMOS](https://docs.aws.amazon.com/elemental-live/latest/ug/s2110-nmos-configure.html): You must enable NMOS on your appliance.
- [Step 2: Obtain information](https://docs.aws.amazon.com/elemental-live/latest/ug/s2110-nmos-obtain-info.html): Speak to the NMOS operator in your organization to make sure that you are aligned on the content of the streams.
- [Step 3: Determine SDPs to create](https://docs.aws.amazon.com/elemental-live/latest/ug/s2110-nmos-design-sdps.html): Determine the number of SDPs you will create in Elemental Live.
- [Step 4: Create receiver group](https://docs.aws.amazon.com/elemental-live/latest/ug/s2110-nmos-create-receiver-group.html): You must create the SMPTE 2110 receiver groups that you need.
- [Step 5: Create the receiver group input](https://docs.aws.amazon.com/elemental-live/latest/ug/s2110-nmos-create-input.html): You must create a receiver group input that connects to the appropriate SMPTE 2110 receiver streams.
- [Step 6: Configure the resiliency scenario](https://docs.aws.amazon.com/elemental-live/latest/ug/s2110-nmos-scenarios.html): You can configure the receiver groups and inputs in an Elemental Live event or Conductor Live profile to support three scenarios.
- [Scenario A](https://docs.aws.amazon.com/elemental-live/latest/ug/s2110-nmos-scenario-patching.html): With this setup, the NMOS controller can send SDP content that provides patching instructions to Elemental Live.
- [Scenario B](https://docs.aws.amazon.com/elemental-live/latest/ug/s2110-nmos-scenario-patching-plus-failover.html): This scenario adds failover to the patching capabilities of scenario A.
- [Scenario C](https://docs.aws.amazon.com/elemental-live/latest/ug/s2110-nmos-scenario-patching-nw-failover.html): You can set up inputs in a configuration that combines NMOS patching with hot backup and network redundancy.
- [SMPTE 2110 without NMOS](https://docs.aws.amazon.com/elemental-live/latest/ug/setup-input-2110.html): Learn how to ingest a SMPTE 2110 source into an Elemental Live event, when your organization doesn't use an NMOS solution.

### [SRT Inputs](https://docs.aws.amazon.com/elemental-live/latest/ug/input-srt.html)

Learn how to set up AWS Elemental Live to ingest a transport stream (TS) that is sent from an upstream system that is set up as an SRT listener.

- [Get ready](https://docs.aws.amazon.com/elemental-live/latest/ug/input-srt-prereqs.html): Learn about the information that you must collect prior to setting up an SRT input in an AWS Elemental Live event.
- [Set up the input](https://docs.aws.amazon.com/elemental-live/latest/ug/input-srt-setup.html): Learn about how to set up an AWS Elemental Live event to include an SRT input.
- [VSF TR-01 in a TS input](https://docs.aws.amazon.com/elemental-live/latest/ug/expanded-support-for-vsf-tr-01.html): You can extract video and audio from VSF TR-01 in a TS


## [Outputs](https://docs.aws.amazon.com/elemental-live/latest/ug/container-outputs.html)

### [Reference: Supported outputs](https://docs.aws.amazon.com/elemental-live/latest/ug/ref-outputs-and-codecs.html)

Find out about the output packages, output formats, and output codecs that AWS Elemental Live supports.

- [Types for delivery to AWS](https://docs.aws.amazon.com/elemental-live/latest/ug/cc-outputs-aws.html): Find out about the different ways that you can send video output from AWS Elemental Live to another AWS service.
- [Types for delivery to other](https://docs.aws.amazon.com/elemental-live/latest/ug/cc-output-not-aws.html): Find out about the different ways that you can send video output from AWS Elemental Live to destinations that aren't hosted by an AWS service.
- [Codecs for live outputs](https://docs.aws.amazon.com/elemental-live/latest/ug/codec-live-outputs.html): Find out about the video codecs and audio codecs that are supported in the AWS Elemental Live output types that are live types.
- [Codecs for VOD outputs](https://docs.aws.amazon.com/elemental-live/latest/ug/codec-vod-outputs.html): Find out about the video codecs and audio codecs that are supported in the AWS Elemental Live output types that are file types.
- [Definition of containers and codecs](https://docs.aws.amazon.com/elemental-live/latest/ug/codecs-containers-definitions.html): Find detailed information about the video and audio codecs that AWS Elemental Live supports.

### [Details about codecs](https://docs.aws.amazon.com/elemental-live/latest/ug/output-codec-details.html)

- [Audio: Supported codec conversions](https://docs.aws.amazon.com/elemental-live/latest/ug/codec-outputs-supported-conversions.html): Find out about the rules in AWS Elemental Live for converting an audio codec in a source to another audio codec in the output.
- [Audio: Support for Dolby codecs](https://docs.aws.amazon.com/elemental-live/latest/ug/codecs-containers-transcode-support.html): Find detailed information Elemental Live support for transcoding and for passthrough of Dolby audio codecs.
- [Video: H.264 support](https://docs.aws.amazon.com/elemental-live/latest/ug/codecs-containers-h264.html): Find detailed information about the variations of H.264 that Elemental Live supports.
- [Video: HEVC support](https://docs.aws.amazon.com/elemental-live/latest/ug/codecs-containers-hevc.html): Find detailed information about the variations of H.265 (HEVC) that Elemental Live supports.
- [Video: MPEG-2 support](https://docs.aws.amazon.com/elemental-live/latest/ug/codecs-containers-mpeg2.html): Find detailed information about the variations of MPEG-2 (H.262) that Elemental Live supports.
- [CPU and GPU support](https://docs.aws.amazon.com/elemental-live/latest/ug/codecs-containers-CPU-only-GPU-enabled.html): Find detailed information about Elemental Live support for CPU and GPU encoding.

### [MediaConnect](https://docs.aws.amazon.com/elemental-live/latest/ug/setting-up-live-as-contribution-encoder-for-mediaconnect.html)

Lean how to send an AWS Elemental Live output to an AWS Elemental MediaConnect flow.

- [Assumptions](https://docs.aws.amazon.com/elemental-live/latest/ug/setting-up-live-as-contribution-encoder-for-mediaconnect-assumptions.html): This section assumes the following:
- [Setup procedure](https://docs.aws.amazon.com/elemental-live/latest/ug/setup-live-contribution-to-emx-procedure.html)
- [How delivery from Elemental Live to MediaConnect works at runtime](https://docs.aws.amazon.com/elemental-live/latest/ug/setting-up-live-as-contribution-encoder-for-mediaconnect-how-it-works-at-runtime.html): Learn how delivery of an output from AWS Elemental Live to MediaConnect works at runtime.
- [HLS output to MediaPackage](https://docs.aws.amazon.com/elemental-live/latest/ug/output-empV4.html): Learn how to set up Elemental Live for a glass-to-glass low-latency workflow that includes MediaPackage as the origin server.
- [MediaStore](https://docs.aws.amazon.com/elemental-live/latest/ug/sending-elemental-live-output-to-aws-mediastore.html): Learn how to send AWS Elemental Live outputs to AWS Elemental MediaStore

### [SMPTE 2110 output group](https://docs.aws.amazon.com/elemental-live/latest/ug/output-2110.html)

Learn how to set up outputs that are compliant with the SMPTE 2110 with AWS Elemental Live.

- [Step 1: Get ready](https://docs.aws.amazon.com/elemental-live/latest/ug/s2110-output-get-ready.html): Learn how to configure the Elemental Live appliance to handle SMPTE 2110 outputs.
- [Step 2: Design the workflow](https://docs.aws.amazon.com/elemental-live/latest/ug/s2110-out-design-workflow.html): Learn how to design the SMPTE 2110 outputs to include the video, audio, and ancillary data streams that you want to produce.
- [Step 3: Create output group](https://docs.aws.amazon.com/elemental-live/latest/ug/config-output-2110.html): Learn how to create an SMPTE 2110 output group, in order to produce an output that is compliant with SMPTE 2110.
- [Step 4: Download the SDP file](https://docs.aws.amazon.com/elemental-live/latest/ug/locate-sdp.html): Learn how to make sure that the SDP files for an SMPTE 2110 output are available to the SMPTE 2110 receiver.

### [TS output using SRT](https://docs.aws.amazon.com/elemental-live/latest/ug/output-srt.html)

Learn how to deliver transport stream (TS) output using the SRT protocol, with AWS Elemental Live as the SRT caller or as the SRT listener.

- [Get ready](https://docs.aws.amazon.com/elemental-live/latest/ug/output-srt-get-ready.html): Learn about the decisions you must make prior to setting up an SRT output in an AWS Elemental Live event.
- [Create the output](https://docs.aws.amazon.com/elemental-live/latest/ug/output-srt-setup.html): Learn about how to set up an AWS Elemental Live event to include an SRT output.

### [TS output using Zixi](https://docs.aws.amazon.com/elemental-live/latest/ug/delivering-ts-output-using-the-zixi-protocol.html)

Learn how to deliver transport stream (TS) output using the Zixi protocol.

- [Get ready](https://docs.aws.amazon.com/elemental-live/latest/ug/output-zixi-get-ready.html): Before you create a Zixi output in your event, perform the following preparation.
- [Create the output](https://docs.aws.amazon.com/elemental-live/latest/ug/zixi-output-setup.html)


## [Video](https://docs.aws.amazon.com/elemental-live/latest/ug/container-video.html)

### [Color space](https://docs.aws.amazon.com/elemental-live/latest/ug/hdr-working-with.html)

Learn about how Elemental Live supports passthrough and conversion of color space and color space metadata.

- [Color space versus video resolution](https://docs.aws.amazon.com/elemental-live/latest/ug/color-space-vs-resolution.html): Read a quick summary of the difference between SD and SDR, and between HD and HDR.

### [General information](https://docs.aws.amazon.com/elemental-live/latest/ug/about-color-metadata.html)

Read about the different color space standards that Elemental Live supports.

- [Definitions](https://docs.aws.amazon.com/elemental-live/latest/ug/color-space-definitions.html): Learn about the different components of a color space standard.
- [Color space standards](https://docs.aws.amazon.com/elemental-live/latest/ug/color-space-standards.html): Read about how the standards that capture each component of the different color space standards that AWS Elemental Live supports.
- [Requirements for inputs](https://docs.aws.amazon.com/elemental-live/latest/ug/color-space-inputs-requirements.html): Read about the characteristics that a video source must include in order for Elemental Live to be able to work with its color space.
- [Requirements for outputs](https://docs.aws.amazon.com/elemental-live/latest/ug/color-space-output-requirements.html): Read about the characteristics that a video output must include in order for Elemental Live to be able to work with its color space.
- [Support for conversion and passthrough](https://docs.aws.amazon.com/elemental-live/latest/ug/color-space-conversions.html): Read about the ability for Elemental Live to pass through or convert a color space from the video source to the video output.

### [Configuring input](https://docs.aws.amazon.com/elemental-live/latest/ug/hdr-input-handling.html)

Learn about the decisions you must make for processing the source when working with color space in Elemental Live.

- [Step 1: Decide on handling](https://docs.aws.amazon.com/elemental-live/latest/ug/color-space-input-procedure.html): Learn about how to assess the quality of the color space metadata in a source input for AWS Elemental Live.
- [Step 2: Choose a scenario](https://docs.aws.amazon.com/elemental-live/latest/ug/color-space-cleanup-scenarios.html): Learn about changes you might need to make to color space metadata in the source, in order to successfully convert or pass through the color space to an AWS Elemental Live output.
- [Step 3: Set up input](https://docs.aws.amazon.com/elemental-live/latest/ug/color-space-event-input-setup.html): Learn how to configure the color space information in an input in an AWS Elemental Live event.

### [Configuring output](https://docs.aws.amazon.com/elemental-live/latest/ug/hdr-output.html)

Learn about the options for handling color space in AWS Elemental Live outputs.

- [Passing through color space](https://docs.aws.amazon.com/elemental-live/latest/ug/colorspace-output-passthrough.html): Learn how to configure an AWS Elemental Live event to pass through the color space to an output.
- [Converting: Procedure A](https://docs.aws.amazon.com/elemental-live/latest/ug/colorspace-output-procedure.html): Learn how to configure an AWS Elemental Live event to convert the color space that is included in an output.
- [Converting: Procedure B](https://docs.aws.amazon.com/elemental-live/latest/ug/colorspace-output-hdr10.html): Learn how to configure an AWS Elemental Live event to convert the color space to HDR10 or Dolby Vision in the output.
- [Removing metadata](https://docs.aws.amazon.com/elemental-live/latest/ug/colorspace-output-remove.html): Learn how to configure an AWS Elemental Live event to remove the color space metadata from an output.

### [The results of different types of conversions](https://docs.aws.amazon.com/elemental-live/latest/ug/color-space-conversion-results.html)

Learn about the results of different ways of handling color space in an AWS Elemental Live event.

- [SDR to SDR](https://docs.aws.amazon.com/elemental-live/latest/ug/color-space-convert-f.html): Learn about the results of converting from one SDR color space to another in an AWS Elemental Live output.
- [SDR to HDR](https://docs.aws.amazon.com/elemental-live/latest/ug/color-space-convert-a.html): Learn about the results of converting from SDR color space to HDR in an AWS Elemental Live output.
- [HDR to HDR](https://docs.aws.amazon.com/elemental-live/latest/ug/color-space-convert-b.html): Learn about the results of converting from one HDR color space to another in an AWS Elemental Live output.
- [HDR to SDR](https://docs.aws.amazon.com/elemental-live/latest/ug/color-space-convert-c.html): Learn about the results of converting from HDR color space to SDR in an AWS Elemental Live output.
- [HDR10 to Dolby Vision](https://docs.aws.amazon.com/elemental-live/latest/ug/color-space-convert-d.html): Learn about the results of converting from HDR10 color space to Dolby Vision in an AWS Elemental Live output.
- [Other to Dolby Vision](https://docs.aws.amazon.com/elemental-live/latest/ug/color-space-convert-e.html): Learn about the results of converting from a non-HDR10 color space to Dolby Vision in an AWS Elemental Live output.
- [Mixed color space](https://docs.aws.amazon.com/elemental-live/latest/ug/color-space-convert-g.html): Learn about the results of converting video with a mix of color spaces in an AWS Elemental Live output.
- [Location of HDR fields on the web interface](https://docs.aws.amazon.com/elemental-live/latest/ug/hdr-location-of-fields-on-the-web-interface.html): Look up the location of any HDR field on the AWS Elemental Live web interface.
- [Location of HDR fields in the XML](https://docs.aws.amazon.com/elemental-live/latest/ug/hdr-location-of-fields-in-the-xml.html): Look up the location of any HDR field in the AWS Elemental Live event XML.
- [Dolby Vision HDR10](https://docs.aws.amazon.com/elemental-live/latest/ug/dolby-vision-hdr10.html): The information for handling video that is in the Dolby Vision color space has changed.
- [QVBR and rate control mode](https://docs.aws.amazon.com/elemental-live/latest/ug/qvbr-and-rate-control-mode.html): Learn how to set up the rate control mode of an Elemental Live output to use QVBR, VBR or CBR.

### [Scan type](https://docs.aws.amazon.com/elemental-live/latest/ug/vq-scan-type.html)

Learn about converting the scan type of the input videoâ progressive, interlaced or telecineâ to a different type in the output.

- [Key fields](https://docs.aws.amazon.com/elemental-live/latest/ug/vq-scan-type-key.html)
- [Secondary fields](https://docs.aws.amazon.com/elemental-live/latest/ug/vq-scan-type-secondary.html)
- [Adaptive field frame controls](https://docs.aws.amazon.com/elemental-live/latest/ug/vq-scan-type-paff.html)
- [Ultra-low latency](https://docs.aws.amazon.com/elemental-live/latest/ug/video-ull.html): Learn about how to set up for ultra-low latency outputs.

### [Video quality](https://docs.aws.amazon.com/elemental-live/latest/ug/video-quality.html)

Get recommendations for tuning and controlling video quality by setting parameters in the event.

- [Frame rate conversion](https://docs.aws.amazon.com/elemental-live/latest/ug/vq-framerate-conversion.html): Learn about the parameters that can improve the video quality when you convert the frame rate of the video.
- [Group of pictures (GOP) configuration](https://docs.aws.amazon.com/elemental-live/latest/ug/vq-gop.html): Learn how the structure of the group of pictures (GOP) can affect video quality.
- [Miscellaneous video tuning parameters](https://docs.aws.amazon.com/elemental-live/latest/ug/vq-miscellaneous-tuning.html): Learn about individual video tuning parameters that affect video quality.
- [Noise reduction](https://docs.aws.amazon.com/elemental-live/latest/ug/vq-noise-reduction.html): Learn how to apply the noise reducer preprocessor to improve output video quality.
- [Quantization controls](https://docs.aws.amazon.com/elemental-live/latest/ug/vq-quantization.html): Learn about how quantization controls can improve video quality.
- [Rate control mode](https://docs.aws.amazon.com/elemental-live/latest/ug/vq-rate-control-mode.html): The rate control mode of the output video affects video quality.


## [Audio](https://docs.aws.amazon.com/elemental-live/latest/ug/container-audio.html)

- [Dolby Digital Plus with Atmos](https://docs.aws.amazon.com/elemental-live/latest/ug/dolby-atmos-output.html): In AWS Elemental Live, learn how to use convert a Dolby Digital Plus audio source to a Dolby Digital Plus with Atmos audio output, or to pass through an audio source that is already Dolby Digital Plus with Atmos.

### [Dolby metadata](https://docs.aws.amazon.com/elemental-live/latest/ug/dolby-metadata.html)

Learn how to include source metadata if you are passing through Dolby audio to the output.

- [Categories of Metadata](https://docs.aws.amazon.com/elemental-live/latest/ug/dolby-metadata-categories.html): There are two categories of parameters in the Dolby metadata, characterized by how Elemental Live uses it:
- [Source of metadata](https://docs.aws.amazon.com/elemental-live/latest/ug/dolby-metadata-source.html): The metadata that Elemental Live emits can come from one of two sources:
- [Impact on output audio](https://docs.aws.amazon.com/elemental-live/latest/ug/dolby-metadata-impact.html): Regardless of the source of the metadata, it affects the audio (either by manipulating encoder control or by being included in the output metadata) but only if the output codec is Dolby Digital or Dolby Digital Plus.
- [Codec combinations](https://docs.aws.amazon.com/elemental-live/latest/ug/dolby-metadata-impact-combination-input-output-codec.html): The possible input and output codec combinations (in which at least one codec is a Dolby codec) are as follows.
- [Setting up](https://docs.aws.amazon.com/elemental-live/latest/ug/dolby-metadata-setup.html): This section describes how to set up the project or event using the web interface.
- [Output with Dolby Digital](https://docs.aws.amazon.com/elemental-live/latest/ug/dolby-metadata-output-dolby-digital-codec.html)
- [Output with Dolby Digital Plus](https://docs.aws.amazon.com/elemental-live/latest/ug/dolby-metadata-output-dolby-digital-plus-codec.html)

### [HLS rendition groups](https://docs.aws.amazon.com/elemental-live/latest/ug/hls-rendition-groups.html)

Learn how to set up rendition groups in an HLS output group in an AWS Elemental Live event.

- [How video is associated with audio rendition groups](https://docs.aws.amazon.com/elemental-live/latest/ug/hls-rendition-groups-how-video-is-associated-with-audio-rendition-groups.html): The different âsetsâ of media are created as follows:
- [Rules for rendition groups](https://docs.aws.amazon.com/elemental-live/latest/ug/hls-rendition-groups-rules.html): Rules exist for associating both audio and video streams in their respective rendition groups.
- [Examples](https://docs.aws.amazon.com/elemental-live/latest/ug/hls-rendition-groups-examples.html)

### [Creating HLS rendition groups](https://docs.aws.amazon.com/elemental-live/latest/ug/hls-rendition-groups-create.html)

The key to creating rendition groups is that each output you create must contain only one stream.

- [Getting ready](https://docs.aws.amazon.com/elemental-live/latest/ug/hls-rendition-groups-getting-ready-to-create.html)
- [Creating HLS rendition groups (web interface)](https://docs.aws.amazon.com/elemental-live/latest/ug/hls-rendition-groups-create-using-web-interface.html): Topics
- [Creating HLS rendition groups (REST API)](https://docs.aws.amazon.com/elemental-live/latest/ug/hls-rendition-groups-create-using-rest-api.html): The following information assumes that you have read and are therefore familiar with the construction and association of an output containing video and rendition groups.
- [Sample HLS output group](https://docs.aws.amazon.com/elemental-live/latest/ug/hls-rendition-groups-sample-manifest.html)


## [Features](https://docs.aws.amazon.com/elemental-live/latest/ug/container-features.html)

### [Captions](https://docs.aws.amazon.com/elemental-live/latest/ug/captions.html)

Learn how to set up an Elemental Live event to extract captions from a source and include them in outputs, in either the same or a different format.

### [Supported features](https://docs.aws.amazon.com/elemental-live/latest/ug/captions-supported-features.html)

Learn about the captions features that Elemental Live supports.

- [Supported formats](https://docs.aws.amazon.com/elemental-live/latest/ug/supported-formats.html): For information about the captions that Elemental Live can ingest, and the captions that it can produce, see .
- [Definitions of captions categories](https://docs.aws.amazon.com/elemental-live/latest/ug/supported-categories.html): Learn about the captions categories that Elemental Live supports.
- [Support for multiple languages](https://docs.aws.amazon.com/elemental-live/latest/ug/support-for-languages.html): Learn about the ability to include multiple captions languages in Elemental Live outputs.
- [Support for OCR conversion](https://docs.aws.amazon.com/elemental-live/latest/ug/support-for-ocr.html): Learn about Elemental Live support for converting captions using OCR (optical character recognition) conversion.
- [Support for font styles in output captions](https://docs.aws.amazon.com/elemental-live/latest/ug/support-for-font-styles-in-output-captions.html): Learn about Elemental Live support for applying font styling to captions in video output.
- [Captions in events with multiple inputs](https://docs.aws.amazon.com/elemental-live/latest/ug/captions-events-multi-input.html): Learn about the rules for implementing captions in an Elemental Live event that includes multiple inputs.
- [Captions and input switching setups](https://docs.aws.amazon.com/elemental-live/latest/ug/captions-in-input-switching.html): Learn about the rules for implementing captions in an Elemental Live event that includes redundant hot-hot inputs.
- [Typical scenarios](https://docs.aws.amazon.com/elemental-live/latest/ug/typical-scenarios.html): Read about different use cases the illustrate the options for handling captions in an Elemental Live event.

### [Setting up for captions](https://docs.aws.amazon.com/elemental-live/latest/ug/setting-up-for-captions.html)

Learn how to set up an Elemental Live event to handle captions that are present in the source.

- [Step 1: Identify source captions](https://docs.aws.amazon.com/elemental-live/latest/ug/identify-captions-in-the-input.html): Learn how to plan for the Elemental Live event to handle captions that are present in the source.

### [Step 2: Create captions selectors](https://docs.aws.amazon.com/elemental-live/latest/ug/create-caption-selectors.html)

Learn how to set up the Elemental Live event to extract captions that are present in the source.

- [Information for DVB-Sub or SCTE-27](https://docs.aws.amazon.com/elemental-live/latest/ug/dvb-sub-or-scte27.html): Learn how to set up the Elemental Live event to extract DVB-Sub or SCTE-27 captions that are present in the source.

### [Information for embedded](https://docs.aws.amazon.com/elemental-live/latest/ug/embedded.html)

Learn how to set up the Elemental Live event to extract embedded captions that are present in the source.

- [Number of captions selectors](https://docs.aws.amazon.com/elemental-live/latest/ug/determine-number-embedded-caption-selectors.html): To determine the number of captions selectors you need to created in the event, follow these rules:
- [Fields in the selector group](https://docs.aws.amazon.com/elemental-live/latest/ug/fields-embedded-captions-selector.html)
- [Fields for CC channel number](https://docs.aws.amazon.com/elemental-live/latest/ug/cc-fields.html)
- [Information for SCC](https://docs.aws.amazon.com/elemental-live/latest/ug/captions-input-scc.html): Learn how to set up the Elemental Live event to extract SCC captions that are present in the source.
- [Information for SMI, SMPTE-TT, SRT, STL, TTML](https://docs.aws.amazon.com/elemental-live/latest/ug/captions-input-other-sidecars.html): Learn how to set up the Elemental Live event to extract SMI, SMPTE-TT, SRT, STL, and TTML captions that are present in the source.

### [Information for Teletext](https://docs.aws.amazon.com/elemental-live/latest/ug/teletext.html)

Learn how to set up the Elemental Live event to extract Teletext captions that are present in the source.

- [Number of captions selectors](https://docs.aws.amazon.com/elemental-live/latest/ug/determine-number-teletext-caption-selectors.html)
- [Fields in the selector group](https://docs.aws.amazon.com/elemental-live/latest/ug/fields-teletext-caption-selector.html)
- [Information for null](https://docs.aws.amazon.com/elemental-live/latest/ug/captions-input-null.html): Learn about the purpose of the Null option available when you set up an Elemental Live event to extract captions that are present in the source.
- [Step 3: Plan outputs](https://docs.aws.amazon.com/elemental-live/latest/ug/planning-captions-in-the-outputs.html): Learn how to plan for the Elemental Live event to include captions in the outputs.
- [Step 4: Match formats to categories](https://docs.aws.amazon.com/elemental-live/latest/ug/categories-captions.html): Learn about the different categories for handling output captions in an Elemental Live event.

### [Step 5: Create captions encodes](https://docs.aws.amazon.com/elemental-live/latest/ug/create-captions-encodes.html)

Learn how to set up an Elemental Live event to include captions in the outputs.

### [All captions except sidecar or SMPTE-TT in MS Smooth](https://docs.aws.amazon.com/elemental-live/latest/ug/output-embedded-and-more.html)

Learn how to set up an Elemental Live event to include embedded, burn-in, or object captions in the outputs.

- [Font styles](https://docs.aws.amazon.com/elemental-live/latest/ug/font-styles-for-burn-in-or-dvbsub.html): When you set up the captions encode as described in , you can specify the appearance of the captions if the output captions are Burn-in or DVB-Sub.
- [PIDS for ARIB](https://docs.aws.amazon.com/elemental-live/latest/ug/complete-the-pids-for-arib.html): This section applies when you set up the captions encode as described in , if the output group is UDP/TS and the output captions format is ARIB.
- [PIDS for DVB-Sub](https://docs.aws.amazon.com/elemental-live/latest/ug/complete-the-pids-for-dvb-sub.html): This section applies when you set up the captions encode as described in , if the output group is UDP/TS and the output captions format is DVB-Sub.
- [PIDS for Teletext](https://docs.aws.amazon.com/elemental-live/latest/ug/complete-the-pids-for-teletext.html): This section applies when you set up the captions encode as described in , if the output group is UDP/TS and the output captions format is teletext.
- [Set up the HLS Manifest (embedded captions)](https://docs.aws.amazon.com/elemental-live/latest/ug/set-up-the-hls-manifest.html): This section applies when you set up the captions encode as described in , if the output group is HLS and the output captions format is embedded.
- [Sidecar captions or SMPTE-TT captions in MS Smooth](https://docs.aws.amazon.com/elemental-live/latest/ug/output-sidecar-and-smptett-mss.html): Learn how to set up an Elemental Live event to include sidecar captions or SMPTE-TT captions in the outputs.
- [TTML captions wrapped in ID3 data](https://docs.aws.amazon.com/elemental-live/latest/ug/output-ttml-in-id3.html): Learn how to set up an Elemental Live event with outputs that include TTML captions that are wrapped in ID3 data.
- [Setting up for 608 XDS data](https://docs.aws.amazon.com/elemental-live/latest/ug/608-xds-handling.html): Learn how to set up an Elemental Live event to include or strip out 608 XDS data.

### [Examples of implementing use cases](https://docs.aws.amazon.com/elemental-live/latest/ug/examples.html)

Look at examples of incorporating captions in the outputs of an Elemental Live event.

- [Use case 1](https://docs.aws.amazon.com/elemental-live/latest/ug/use-case-one-input-format-to-one-output.html): This example shows how to implement the first use case from the typical scenarios.
- [Use case 2](https://docs.aws.amazon.com/elemental-live/latest/ug/use-case-one-input-format-to-one-different-output-format.html): This example shows how to implement the second use case from the typical scenarios.
- [Use case 3](https://docs.aws.amazon.com/elemental-live/latest/ug/use-case-one-input-format-different-format-for-each-output.html): This example shows how to implement the third use case from the typical scenarios.
- [Use case 4](https://docs.aws.amazon.com/elemental-live/latest/ug/use-case-one-captions-output-shared-by-multiple-video-encode.html): This example shows how to set up captions in an ABR workflow.
- [Passing through VBI data](https://docs.aws.amazon.com/elemental-live/latest/ug/captions-in-vbi-data.html): Learn how to pass through VBI data to the outputs of an Elemental Live event.
- [Reference: OCR languages](https://docs.aws.amazon.com/elemental-live/latest/ug/captions-ocr-languages.html): Read a list of world languages that AWS Elemental Live supports wh en you convert captions using OCR (optical character recognition) technology.

### [Dynamic input switching](https://docs.aws.amazon.com/elemental-live/latest/ug/dynamic-content-switching.html)

Learn how to perform input switching while an AWS Elemental Live event is running.

- [Typical use cases](https://docs.aws.amazon.com/elemental-live/latest/ug/typical-use-cases.html)

### [Procedures](https://docs.aws.amazon.com/elemental-live/latest/ug/content-switching-procedure.html)

The procedures

- [General procedure](https://docs.aws.amazon.com/elemental-live/latest/ug/general-procedure.html): Topics
- [Sample implementations](https://docs.aws.amazon.com/elemental-live/latest/ug/sample-implementations.html)
- [Details on preparing inputs](https://docs.aws.amazon.com/elemental-live/latest/ug/details-on-preparing-inputs.html): Troubleshoot dynamic content switching when inputs are not being prepared as expected.
- [Details on activating inputs](https://docs.aws.amazon.com/elemental-live/latest/ug/details-on-activating-inputs.html): Learn about activating inputs when you are performing dynamic content switching.
- [Monitoring activity through the web interface](https://docs.aws.amazon.com/elemental-live/latest/ug/monitoring-activity-via-web.html): Learn how to monitor dynamic content switching through the web interface.
- [Monitoring activity through the API](https://docs.aws.amazon.com/elemental-live/latest/ug/monitoring-activity-via-api.html): Learn how to monitor dynamic content switching through the API.

### [Using the REST API](https://docs.aws.amazon.com/elemental-live/latest/ug/content-switching-api.html)

Learn about using the REST API to dynamically switch content in an Elemental Live event.

- [List of commands](https://docs.aws.amazon.com/elemental-live/latest/ug/list-of-commands.html): Look up the commands in the REST API for dynamically switching content in an Elemental Live event.
- [Add dynamic playlist inputs](https://docs.aws.amazon.com/elemental-live/latest/ug/add-dynamic-playlist-inputs.html): Look up the REST API command to add inputs to the playlist that is used for dynamic content switching.
- [Replace dynamic playlist](https://docs.aws.amazon.com/elemental-live/latest/ug/replace-dynamic-playlist.html): Look up the REST API command to replace inputs in the playlist that is used for dynamic content switching.
- [Get event](https://docs.aws.amazon.com/elemental-live/latest/ug/get-event.html): Get a list of the inputs in the specified event.
- [Modify one dynamic playlist input](https://docs.aws.amazon.com/elemental-live/latest/ug/modify-one-dynamic-playlist-input.html): Look up the REST API command to modify an input in the playlist that is used for dynamic content switching.
- [Delete dynamic playlist input](https://docs.aws.amazon.com/elemental-live/latest/ug/delete-dynamic-playlist-input.html): Look up the REST API command to delete inputs from the playlist used for dynamic content switching.
- [Prepare dynamic playlist input](https://docs.aws.amazon.com/elemental-live/latest/ug/prepare-dynamic-playlist-input.html): Look up the REST API command to prepare an input in the playlist used for dynamic content switching.
- [Activate dynamic playlist input](https://docs.aws.amazon.com/elemental-live/latest/ug/activate-dynamic-playlist-input.html): Look up the REST API command to activate an input that is in the playlist used for dynamic content switching.
- [Get event status](https://docs.aws.amazon.com/elemental-live/latest/ug/get-event-status.html): Look up the REST API command to get the status of the inputs in an event where you are implementing dynamic content switching.
- [Elements and tags](https://docs.aws.amazon.com/elemental-live/latest/ug/elements-and-tags.html): This section lists all the elements and tags that could appear in the input element of an event XML.
- [Graphic overlay overview](https://docs.aws.amazon.com/elemental-live/latest/ug/graphic-overlay.html): Learn how to insert a graphic onto the video in an AWS Elemental Live event using the graphic overlay feature.

### [Graphic overlay: Motion overlay](https://docs.aws.amazon.com/elemental-live/latest/ug/motion-graphic-overlay.html)

Learn how to insert a motion graphic overlay in AWS Elemental Live for video that it encodes.

### [HTML5](https://docs.aws.amazon.com/elemental-live/latest/ug/how-to-insert-a-motion-overlay-with-html5.html)

You can insert a motion overlay with HTML5.

- [Step A: Choose control method](https://docs.aws.amazon.com/elemental-live/latest/ug/step-design-controls-html5.html): You must speak to the operator of the authoring system and decide how the overlay will be controlled.
- [Step B: Prepare asset](https://docs.aws.amazon.com/elemental-live/latest/ug/step-prepare-the-html5-asset.html): You use an authoring system to create the asset and to manage the content, including implementation of features such as fade or opacity.

### [Step C: Set up event](https://docs.aws.amazon.com/elemental-live/latest/ug/html5-step-set-up-the-event.html)

You configure the event with all the information about the motion overlay.

- [Using the web interface](https://docs.aws.amazon.com/elemental-live/latest/ug/html5-set-up-event-web-interface.html)
- [Using the REST API](https://docs.aws.amazon.com/elemental-live/latest/ug/html5-set-up-event-fields-api.html): This description assumes that you are familiar with using the REST API and with the XML body for a live_event.
- [Fields for an HTML5 asset](https://docs.aws.amazon.com/elemental-live/latest/ug/html5-set-up-event-fields.html)
- [Step D: Show/hide motion overlay](https://docs.aws.amazon.com/elemental-live/latest/ug/html5-step-manage-the-overlay-on-a-running-event.html): If you have configured the motion overlay for REST control, start the event , then enter REST API commands to show and hide the motion overlay.

### [Quicktime MOV](https://docs.aws.amazon.com/elemental-live/latest/ug/how-to-insert-a-motion-overlay-with-quicktime-mov.html)

You can use a .mov file as an asset for the motion image overlay.

- [Step A: Prepare asset](https://docs.aws.amazon.com/elemental-live/latest/ug/step-prepare-the-mov-asset.html)

### [Step B: Set up event](https://docs.aws.amazon.com/elemental-live/latest/ug/mov-step-set-up-the-event.html)

You configure the event with information about the first motion overlay.

- [Using the web interface](https://docs.aws.amazon.com/elemental-live/latest/ug/mov-set-up-event-web-interface.html)
- [Using the REST API](https://docs.aws.amazon.com/elemental-live/latest/ug/mov-set-up-event-fields-api.html): This description assumes that you are familiar with using the REST API and with the XML body for a live_event.
- [Fields for a MOV asset](https://docs.aws.amazon.com/elemental-live/latest/ug/mov-set-up-event-fields.html)
- [Step C: Manage at runtime](https://docs.aws.amazon.com/elemental-live/latest/ug/mov-step-manage-the-overlay-on-a-running-event.html): After the event starts, the motion overlay that is configured in the event runs at the specified time.
- [Step D: Run event again](https://docs.aws.amazon.com/elemental-live/latest/ug/mov-step-run-again.html): You might want to run the same event again.

### [PNG](https://docs.aws.amazon.com/elemental-live/latest/ug/how-to-insert-a-motion-overlay-with-png.html)

You can use a set of .png files as an asset for the motion image overlay.

- [Step A: Prepare asset](https://docs.aws.amazon.com/elemental-live/latest/ug/step-prepare-the-png-asset.html)

### [Step B: Set up event](https://docs.aws.amazon.com/elemental-live/latest/ug/png-step-set-up-the-event.html)

You configure the event with information about the first motion overlay.

- [Using the web interface](https://docs.aws.amazon.com/elemental-live/latest/ug/png-set-up-event-web-interface.html)
- [Using the REST API](https://docs.aws.amazon.com/elemental-live/latest/ug/png-set-up-event-fields-api.html): This description assumes that you are familiar with using the REST API and with the XML body for a live_event.
- [Fields for a PNG asset](https://docs.aws.amazon.com/elemental-live/latest/ug/png-set-up-event-fields.html)
- [Step C: Manage at runtime](https://docs.aws.amazon.com/elemental-live/latest/ug/png-step-manage-the-overlay-on-a-running-event.html): After the event starts, the motion overlay configured in the event runs at the specified time.
- [Step D: Run event again](https://docs.aws.amazon.com/elemental-live/latest/ug/png-step-run-again.html): You might want to run the same event again.

### [Graphic overlay: Static overlay](https://docs.aws.amazon.com/elemental-live/latest/ug/static-graphic-overlay.html)

Learn how to insert a static overlay into an AWS Elemental Live event so that it appears on the video in one or more of the video outputs.

- [Insertion options](https://docs.aws.amazon.com/elemental-live/latest/ug/insertion-options-and-the-effect-on-outputs.html)
- [Multiple Overlays](https://docs.aws.amazon.com/elemental-live/latest/ug/multiple-overlays-and-layers.html): You can set up the event to insert more than one static overlay.
- [Combining overlays and insertion options](https://docs.aws.amazon.com/elemental-live/latest/ug/combining-overlays-and-insertion-options.html): You can set up the event to insert a static overlay in more than one way.

### [Procedure](https://docs.aws.amazon.com/elemental-live/latest/ug/inserting-a-static-graphic-overlay.html)

- [Step A](https://docs.aws.amazon.com/elemental-live/latest/ug/step-a-prepare-the-overlay-asset.html)
- [Step B](https://docs.aws.amazon.com/elemental-live/latest/ug/step-b-initial-setup.html): Create or modify the event as follows:
- [Step C](https://docs.aws.amazon.com/elemental-live/latest/ug/step-c-manage-overlays-on-a-running-event.html): Once the event has started, you can work with static overlays only via the REST API.

### [Static overlays with REST API](https://docs.aws.amazon.com/elemental-live/latest/ug/using-the-rest-api-for-static-overlays.html)

Topics

- [Commands](https://docs.aws.amazon.com/elemental-live/latest/ug/static-graphic-overlay-commands.html)
- [Create or modify a non-running event](https://docs.aws.amazon.com/elemental-live/latest/ug/create-or-modify-a-non-running-event-with-static-graphic-overlay.html): Create or modify an Elemental Live event and include one or more static graphic overlays.
- [Modify static overlay](https://docs.aws.amazon.com/elemental-live/latest/ug/modify-static-overlay-on-a-running-event.html): In a running event, you can use the REST API to add more static overlays, modify the behavior of an existing static overlay, or delete an existing static overlay.
- [Static overlay and content switching](https://docs.aws.amazon.com/elemental-live/latest/ug/graphic-overlay-plus-dynamic-content-switching.html): You can combine the static overlays with the dynamic content switching feature.

### [XML structure](https://docs.aws.amazon.com/elemental-live/latest/ug/xml-structure-static.html)

Topics

- [Static overlay â non-running event](https://docs.aws.amazon.com/elemental-live/latest/ug/static-overlay-creating-and-modifying-a-non-running-event.html)
- [Static overlay â running event](https://docs.aws.amazon.com/elemental-live/latest/ug/static-overlay-modifying-overlay-on-a-running-event.html)
- [Input switching](https://docs.aws.amazon.com/elemental-live/latest/ug/input-switching-overview.html): Learn about the different features that you can implement in order to switch between inputs in an AWS Elemental Live event.

### [Nielsen watermark insertion](https://docs.aws.amazon.com/elemental-live/latest/ug/feature-nielsen-watermark.html)

Learn how to configure an Elemental Live event to insert Nielsen watermarks in the output.

- [Audio requirements](https://docs.aws.amazon.com/elemental-live/latest/ug/nielsen-wmark-requirements.html): Learn about the characteristics required for an audio source in order for you to configure an Elemental Live event to insert Nielsen watermarks in the output.
- [Get ready](https://docs.aws.amazon.com/elemental-live/latest/ug/nielsen-wmark-get-ready.html): Learn about the information you must obtain about Nielsen watermarks, before you configure an Elemental Live event to insert Nielsen watermarks in the output.
- [Setting up Nielsen watermarks](https://docs.aws.amazon.com/elemental-live/latest/ug/nielsen-watermark-procedure.html): Learn how to configure an Elemental Live event to insert Nielsen watermarks in the output.
- [Nielsen watermarks to ID3](https://docs.aws.amazon.com/elemental-live/latest/ug/feature-nielsen-id3.html): Lean how to set up an AWS Elemental Live event to convert Nielsen watermarks to ID3 metadata.

### [Output locking](https://docs.aws.amazon.com/elemental-live/latest/ug/output-locking.html)

Learn to implement output locking in AWS Elemental Live in order to support output redundancy or distributed encoding.

- [Output locking and frame accuracy](https://docs.aws.amazon.com/elemental-live/latest/ug/opl-frame-accuracy.html): Learn how to use the output locking feature of Elemental Live to produce video outputs that are frame accurate with each other.

### [Use cases](https://docs.aws.amazon.com/elemental-live/latest/ug/output-locking-general.html)

Read general information about output locking and epoch locking in Elemental Live.

- [Output redundancy](https://docs.aws.amazon.com/elemental-live/latest/ug/output-locking-output-redundancy.html): Learn about using Elemental Live output locking to enhance output redundancy by producing redundant outputs that are frame accurate with each other.
- [Distributed encoding](https://docs.aws.amazon.com/elemental-live/latest/ug/output-locking-distributed-encoding.html): Learn about usingElemental Live output locking to implement distributed encoding to produce an ABR stack.
- [Distributed encoding with output redundancy](https://docs.aws.amazon.com/elemental-live/latest/ug/output-locking-distrib-plus-redundancy.html): Learn about usingElemental Live output locking to enhance redundancy in a distributed encoding workflow that incorporates redundancy.
- [How output locking works](https://docs.aws.amazon.com/elemental-live/latest/ug/opl-standard-how-it-works.html): Learn how output locking works in an Elemental Live event.
- [How epoch locking works](https://docs.aws.amazon.com/elemental-live/latest/ug/opl-epoch-how-it-works.html): Learn how epoch locking works in an Elemental Live event.
- [Output locking pools](https://docs.aws.amazon.com/elemental-live/latest/ug/opl-pools.html): Learn about the pools that exist in an event when you implement output locking.
- [Output locking pairs](https://docs.aws.amazon.com/elemental-live/latest/ug/opl-redundant-pairs.html): Learn about the redundant pairs that exist when you implement output locking in an output redundancy implementation.
- [Requirements](https://docs.aws.amazon.com/elemental-live/latest/ug/output-locking-requirements.html): Learn about the requirements that inputs and outputs must meet in order for Elemental Live to succeed.

### [Step 1: Design workflow](https://docs.aws.amazon.com/elemental-live/latest/ug/opl-step-get-ready.html)

Learn how to design a workflow that implements Elemental Live output locking.

- [Design the inputs](https://docs.aws.amazon.com/elemental-live/latest/ug/opl-step-design-inputs.html): Learn how to design the inputs in a workflow that implements Elemental Live output locking.
- [Design the outputs](https://docs.aws.amazon.com/elemental-live/latest/ug/opl-step-get-ready-outputs.html): Learn how to design the outputs in a workflow that implements Elemental Live output locking.
- [Example](https://docs.aws.amazon.com/elemental-live/latest/ug/opl-example.html): Look at an example of a design for an Elemental Live workflow that uses output locking to implement distributed encoding.
- [Step 2: Set up inputs](https://docs.aws.amazon.com/elemental-live/latest/ug/output-locking-setup-inputs.html): Learn how to set up inputs in an Elemental Live event that implements output locking.
- [Step 3: Set up global controls](https://docs.aws.amazon.com/elemental-live/latest/ug/output-locking-setup-global.html): Learn to set up global controls and enable output locking and epoch locking in an Elemental Live event.

### [Step 4: Set up output groups](https://docs.aws.amazon.com/elemental-live/latest/ug/opl-setup-output-groups.html)

Learn how to set up output groups and outputs in an Elemental Live event that implements output locking.

- [HLS](https://docs.aws.amazon.com/elemental-live/latest/ug/opl-setup-hls.html): Learn how to set up an HLS output group to implement Elemental Live output locking.
- [MS Smooth](https://docs.aws.amazon.com/elemental-live/latest/ug/output-locking-event-setup-mss-output-fields.html): Learn how to set up an MS Smooth output group to implement Elemental Live output locking.
- [UDP/TS](https://docs.aws.amazon.com/elemental-live/latest/ug/opl-setup-udp.html): Learn how to set up a UDP/TS output group to implement Elemental Live output locking.
- [Step 5: Set up encodes](https://docs.aws.amazon.com/elemental-live/latest/ug/output-locking-event-setup-stream-video-fields.html): Learn how to set up video encode parameters in an event that implements Elemental Live output locking.

### [SCTE-35 and SCTE-104 message processing](https://docs.aws.amazon.com/elemental-live/latest/ug/scte-message-processing.html)

Learn how to set up an Elemental Live event to ingest SCTE-35 and SCTE-104 messages that are in the input, and correctly process them for the output.

### [Eligible messages and streams](https://docs.aws.amazon.com/elemental-live/latest/ug/eligible-messages-and-streams.html)

Learn about the inputs from which Elemental Live can extract SCTE-35 and SCTE-104 messages.

- [Processing options](https://docs.aws.amazon.com/elemental-live/latest/ug/processing-options.html): Learn about the different ways in which Elemental Live can process SCTE-35 and SCTE-104 messages.

### [Scope of processing depending on outputs](https://docs.aws.amazon.com/elemental-live/latest/ug/scope-of-processing-depending-on-outputs.html)

The following table summarizes which options apply to which kind of output.

- [Archive output with MPEG-2 container](https://docs.aws.amazon.com/elemental-live/latest/ug/archive-output-with-mpeg-2-container.html): A transport stream (TS) in an MPEG-2 container supports passthrough of the SCTE-35 messages, but it does not support creation of a manifest.
- [Archive output with other containers](https://docs.aws.amazon.com/elemental-live/latest/ug/archive-output-with-other-containers.html): Other archive outputs do not support passthrough of the SCTE-35 messages or manifest decoration.
- [Apple HLS output](https://docs.aws.amazon.com/elemental-live/latest/ug/apple-hls-output.html): Apple HLS output supports both passthrough of the SCTE-35 messages and manifest decoration.
- [DASH output](https://docs.aws.amazon.com/elemental-live/latest/ug/dash-output.html): DASH ISO output does not support passthrough of the SCTE-35 messages or manifest decoration.
- [MS Smooth output](https://docs.aws.amazon.com/elemental-live/latest/ug/ms-smooth-output.html): MSS output does not support passthrough of the SCTE-35 messages but does support instructions in the sparse track.
- [Adobe RTMP output](https://docs.aws.amazon.com/elemental-live/latest/ug/adobe-rtmp-output.html): Adobe RTMP output does not support passthrough of the SCTE-35 messages but does support manifest decoration.
- [SMPTE 2110 output](https://docs.aws.amazon.com/elemental-live/latest/ug/s35-scope-s2110.html): SMPTE 2110 output supports passthrough of the SCTE-35 messages.
- [UDP/TS output](https://docs.aws.amazon.com/elemental-live/latest/ug/udp-ts-output.html): UDP/TS output supports passthrough of the SCTE-35 messages, but it does not support creation of a manifest.
- [Blanking and passthrough and manifest decoration](https://docs.aws.amazon.com/elemental-live/latest/ug/blanking-and-pass-through-and-manifest-decoration.html): It is important to understand that the logic for blanking ad content works on the video content associated with the âad avail eventâ while the logic for passthrough and manifest decoration works on the actual SCTE-35 message.
- [Set ad avail mode](https://docs.aws.amazon.com/elemental-live/latest/ug/getting-ready-setting-the-ad-avail-mode.html): Read this section if you want to support any of the following features:
- [Manifest decoration](https://docs.aws.amazon.com/elemental-live/latest/ug/manifest-decoration.html): You can choose to interpret SCTE-35 messages from the original input and insert corresponding instructions into the output manifest for the following outputs:

### [Ad avail blanking and blackout](https://docs.aws.amazon.com/elemental-live/latest/ug/ad-avail-blanking-and-blackout.html)

You can turn on one or both of the following features to blank out the content associated with a SCTE-35 event:

- [Blanking is global](https://docs.aws.amazon.com/elemental-live/latest/ug/blanking-is-global.html): Both Ad avail blanking and Blackout apply to all outputs.
- [Scope of blackout of SCTE-35 messages](https://docs.aws.amazon.com/elemental-live/latest/ug/scope-of-blackout.html): All SCTE-35 messages that are âOther typeâ are blanked out as follows:
- [Scope of ad avail blanking of SCTE-35 messages](https://docs.aws.amazon.com/elemental-live/latest/ug/scope-of-ad-avail-blanking.html): For Ad avail blanking (but not for Blackout), the ad avail mode you set controls which SCTE-35 events result in blanking of the content.
- [Procedure to enable ad avail blanking](https://docs.aws.amazon.com/elemental-live/latest/ug/procedure-to-enable-ad-avail-blanking.html)
- [Procedure to enable blackout](https://docs.aws.amazon.com/elemental-live/latest/ug/procedure-to-enable-blackout.html)

### [Passthrough or removal of SCTE messages](https://docs.aws.amazon.com/elemental-live/latest/ug/pass-through-or-removal.html)

SCTE-35 messages from the input can be passed through (included) in the data stream for the following outputs.

- [Archive procedure](https://docs.aws.amazon.com/elemental-live/latest/ug/pass-through-or-removal-archive.html): You enable or disable passthrough at the output level: only in outputs that have an MPEG-2 TS container.
- [Apple HLS passthrough procedure](https://docs.aws.amazon.com/elemental-live/latest/ug/pass-through-or-removal-apple-hls.html): Passthrough is enabled or disabled individually for each output, which means it can be applied differently for different outputs in the same group.
- [UDP/TS procedure](https://docs.aws.amazon.com/elemental-live/latest/ug/pass-through-or-removal-udp-ts.html): Passthrough is enabled or disabled individually for each output, which means it can be applied differently for different outputs in the same group.

### [SCTE-35 message insertion into currently running events](https://docs.aws.amazon.com/elemental-live/latest/ug/scte-35-message-insertion.html)

You can use the Elemental Live REST API to insert SCTE-35 messages into an Elemental Live event that is currently running.

### [Working with splice inserts](https://docs.aws.amazon.com/elemental-live/latest/ug/working-with-splice-inserts.html)

Splice inserts inserted by the REST API are always of type âad avail.â

- [Insert a new splice insert message](https://docs.aws.amazon.com/elemental-live/latest/ug/insert-a-new-splice-insert-message.html): Inserts a SCTE-35 message of type splice_insert in the stream either immediately or at a specified time.
- [Get current time](https://docs.aws.amazon.com/elemental-live/latest/ug/get-current-time.html): You can obtain the timecode of the frame that is currently being processed in the specified event.
- [Insert an end time in an existing ad avail](https://docs.aws.amazon.com/elemental-live/latest/ug/insert-an-end-time-in-an-existing-ad-avail.html): You can insert an end time in the following situations:
- [Cancel a pending ad avail](https://docs.aws.amazon.com/elemental-live/latest/ug/cancel-a-pending-ad-avail.html): If you inserted an ad avail the start time has not yet passed, you can cancel the insertion.
- [Working with time signals](https://docs.aws.amazon.com/elemental-live/latest/ug/working-with-time-signals.html): Time signals inserted by the REST API can be one of the âad availâ types, or some other type, depending on what you specify in the segmentation descriptor in the request.
- [POIS conditioning](https://docs.aws.amazon.com/elemental-live/latest/ug/pois-conditioning.html): Learn how to set up an Elemental Live event so that a POIS server instructs Elemental Live about how to handle SCTE 35 messages that are in the source.
- [Setting up using the REST API](https://docs.aws.amazon.com/elemental-live/latest/ug/setting-up-via-the-rest-api.html): This topic lists the parameters found on the Elemental Live event or profile and specifies the location of those parameters in the XML for an event or profile.
- [Example manifests for Apple HLS](https://docs.aws.amazon.com/elemental-live/latest/ug/example-manifests-hls.html): This section lists example manifests for the Apple HLS manifest styles that AWS Elemental supports.
- [SCTE-35 ad marker EXT-X-DATERANGE](https://docs.aws.amazon.com/elemental-live/latest/ug/scte-35-ad-marker-ext-x-daterange.html): Learn how to set up an Elemental Live output to use the EXT-X-DATERANGE style of SCTE-35 ad marker.
- [SMPTE 2022-6 inputs](https://docs.aws.amazon.com/elemental-live/latest/ug/SMPTE-ST-2022-6.html): Learn about AWS Elemental Live support for ingesting an uncompressed video source that is compliant with SMPTE 2022-6 .

### [SMPTE 2110 inputs and outputs](https://docs.aws.amazon.com/elemental-live/latest/ug/SMPTE-ST-2110.html)

Learn how to use inputs and outputs that are compliant with SMPTE 2110 with Elemental Live.

- [Appliance requirements](https://docs.aws.amazon.com/elemental-live/latest/ug/2110-appliance-reqs.html): Learn about the Elemental Live appliance that you need in order to work with SMPTE 2110 inputs and outputs, either with or without NMOS.
- [Supported content](https://docs.aws.amazon.com/elemental-live/latest/ug/2110-supported-content.html): Learn about the characteristics of the uncompressed video, JPEG XS video, audio, ancillary data, and timecode in SMPTE 2110 inputs and SMPTE 2110 outputs you can work with.

### [About SDP files](https://docs.aws.amazon.com/elemental-live/latest/ug/2110-sdp-about.html)

Learn about how Elemental Live works with the SDP files that the SMPTE 2110 specification relies on.

- [Format of an SDP file for video](https://docs.aws.amazon.com/elemental-live/latest/ug/2120-sdp-video.html): Look at an example of the contents of an SDP file for a SMPTE 2110 stream that contains video.
- [Format of an SDP file for audio](https://docs.aws.amazon.com/elemental-live/latest/ug/2120-sdp-audio.html): Look at an example of the contents of an SDP file for a SMPTE 2110 stream that contains audio.
- [Format of an SDP file for ancillary data](https://docs.aws.amazon.com/elemental-live/latest/ug/2120-sdp-ancillary.html): Look at an example of the contents of an SDP file for a SMPTE 2110 stream that contains ancillary data.
- [SDP file with 2022-7 information](https://docs.aws.amazon.com/elemental-live/latest/ug/2120-sdp-2022-7.html): Look at an example of the contents of an SDP file for a SMPTE 2110 stream that implements SMPTE 2022-7 seamless protection switching.
- [Support for SMPTE 2022-7](https://docs.aws.amazon.com/elemental-live/latest/ug/2110-options.html): Learn about how Elemental Live implements seamless protection switching in conformance with SMPTE 2022 -7.
- [Support for NMOS](https://docs.aws.amazon.com/elemental-live/latest/ug/2110-and-nmos.html): Learn about how Elemental Live supports NMOS IS-04 with SMPTE 2110 inputs and outputs.
- [Setup: Remove bonded interfaces](https://docs.aws.amazon.com/elemental-live/latest/ug/s2110-setup-bonded-if.html): Learn how to remove bonded interfaces on the Elemental Live appliance, in order to work with source inputs and outputs that are compliant with SMPTE 2110.
- [Setup: Reserve processing cores](https://docs.aws.amazon.com/elemental-live/latest/ug/enable-2110.html): Learn how to reserve cores on the interfaces on the Elemental Live appliance, in order to work with source inputs and outputs that are compliant with SMPTE 2110.
- [Setup: Enable PTP](https://docs.aws.amazon.com/elemental-live/latest/ug/enable-ptp.html): Learn how to use Precision Time Protocol (PTP) to synchronize SMPTE 2110 outputs in an Elemental Live event.
- [SRT inputs and outputs](https://docs.aws.amazon.com/elemental-live/latest/ug/srt-in-out.html): Learn how to work with inputs and outputs that use the SRT protocol to handle a transport stream (TS).

### [Trick-play track](https://docs.aws.amazon.com/elemental-live/latest/ug/trick-play-solutions.html)

Trick-play is used in digital video players to mimic some capabilities of analog players, including fast-forward and rewind capabilities.

- [Trick-play track via I-frames](https://docs.aws.amazon.com/elemental-live/latest/ug/trick-play-i-frames.html): In an HLS output group, you can support a trick-play track by providing an I-frame-only manifest.
- [Trick-play track via the Image Media Playlist specification](https://docs.aws.amazon.com/elemental-live/latest/ug/trick-play-roku.html): In an HLS output group, you can support a trick-play track by providing an asset that follows the Image Media Playlist specification, version 0.4.

### [Virtual input switching](https://docs.aws.amazon.com/elemental-live/latest/ug/feature-vips.html)

Learn how to set up the virtual input switching feature for an AWS Elemental Live event, so that a POIS controls switching from one input to another.

- [About virtual input switching](https://docs.aws.amazon.com/elemental-live/latest/ug/vips-about.html)

### [How virtual input switching works](https://docs.aws.amazon.com/elemental-live/latest/ug/vips-about-how.html)

Topics

- [How it works using asynchronous ESAM](https://docs.aws.amazon.com/elemental-live/latest/ug/vips-asynch.html)
- [How it works using SCTE-35 messages](https://docs.aws.amazon.com/elemental-live/latest/ug/vips-s35.html): This type of input switching works with SCTE-35 messages that are in a transport stream source.

### [Setting up for virtual input switching](https://docs.aws.amazon.com/elemental-live/latest/ug/vips-setup.html)

With virtual input switching, the Elemental Live event and the POIS must be set up with identical information.

- [Overview](https://docs.aws.amazon.com/elemental-live/latest/ug/vips-setup-overview.html): The POIS must be set up with the following information:
- [Step 1: Coordinate with the POIS operator](https://docs.aws.amazon.com/elemental-live/latest/ug/vips-setup-step-coordinate.html): Talk to the POIS operator, and agree on the values for this data:
- [Step 2: Set up the event](https://docs.aws.amazon.com/elemental-live/latest/ug/vips-setup-step-event.html): These steps show you how to configure the event with information about the POIS server.
- [Step 3: Set up the inputs in the event](https://docs.aws.amazon.com/elemental-live/latest/ug/vips-setup-step-inputs.html)
- [Step 4: Start the event](https://docs.aws.amazon.com/elemental-live/latest/ug/vips-setup-step-start.html): When you start the event, Elemental Live ingests inputs, starting with the first input listed in the event.


## [Reference](https://docs.aws.amazon.com/elemental-live/latest/ug/container-ref.html)

### [Reference: Supported captions](https://docs.aws.amazon.com/elemental-live/latest/ug/supported-captions.html)

This section provides reference information about the captions formats that Elemental Live supports.

- [Supported caption formats](https://docs.aws.amazon.com/elemental-live/latest/ug/captions-supported-formats.html)
- [Rules for extracting captions](https://docs.aws.amazon.com/elemental-live/latest/ug/supported-containers-inputs.html): To use captions in a source, Elemental Live must be able to extract the captions.

### [Rules for converting captions](https://docs.aws.amazon.com/elemental-live/latest/ug/captions-support-tables.html)

This section helps you to ensure that when creating an event or profile, you select a format that is valid for your output captions.

- [GPP output container](https://docs.aws.amazon.com/elemental-live/latest/ug/captions-gpp-output-container.html): To read this table, find the type of container and captions from your input.
- [DASH output container](https://docs.aws.amazon.com/elemental-live/latest/ug/captions-dash-output-container.html): To read this table, find the type of container and captions from your input.
- [HLS output container](https://docs.aws.amazon.com/elemental-live/latest/ug/captions-hls-output-container.html): To read this table, find the type of container and captions from your input.
- [HLS fMP4 output container](https://docs.aws.amazon.com/elemental-live/latest/ug/captions-hls-fmp4-output-container.html): To read this table, find the type of container and captions from your input.
- [MP4 output container](https://docs.aws.amazon.com/elemental-live/latest/ug/captions-hds-mp4-output-container.html): To read this table, find the type of container and captions from your input.
- [MPEG2-TS or MPEG2-UDP output container](https://docs.aws.amazon.com/elemental-live/latest/ug/captions-mpeg2-ts-file-mpeg2-udp-streaming-output-container.html): The table provides information about captions in an MPEG2-TS file output container or MPEG2-UDP streaming output container.
- [MSS output container](https://docs.aws.amazon.com/elemental-live/latest/ug/captions-mss-output-container.html): To read this table, find the type of container and captions from your input.
- [MXF output container](https://docs.aws.amazon.com/elemental-live/latest/ug/captions-mxf-output-container.html): To read this table, find the type of container and captions from your input.
- [QuickTime output container](https://docs.aws.amazon.com/elemental-live/latest/ug/captions-quicktime-output-container.html): To read this table, find the type of container and captions from your input.
- [Raw output container](https://docs.aws.amazon.com/elemental-live/latest/ug/captions-raw-output-container.html): This table describes the caption formats that can be included in a raw output container that contains video.
- [RTMP output container](https://docs.aws.amazon.com/elemental-live/latest/ug/captions-rtmp-output-container.html): To read this table, find the type of container and captions from your input.
- [Captions-only Output Container](https://docs.aws.amazon.com/elemental-live/latest/ug/captions-captions-only-output-container.html): This table describes the caption formats that can be included on their own in an output.

### [Reference: Supported DRM solutions](https://docs.aws.amazon.com/elemental-live/latest/ug/drm-support-solutions.html)

Look up information about the DRM solutions that AWS Elemental Live supports.

- [DASH output](https://docs.aws.amazon.com/elemental-live/latest/ug/drm-dash-output.html): Encryption mode: Always AES CTR (AES-128)
- [HLS output with Apple FairPlay](https://docs.aws.amazon.com/elemental-live/latest/ug/drm-hls-applefairplay.html): Encryption mode: Always AES CBC (Sample AES)
- [HLS output with PlayReady](https://docs.aws.amazon.com/elemental-live/latest/ug/drm-hls-playready.html): Encryption mode: Always AES CTR (AES-128)
- [HLS output with SecureMedia](https://docs.aws.amazon.com/elemental-live/latest/ug/drm-hls-securemedia.html): Encryption mode: Always AES CTR (AES-128)
- [HLS output with Verimatrix](https://docs.aws.amazon.com/elemental-live/latest/ug/drm-hls-verimatrix.html): Encryption mode: Always AES CTR (AES-128)
- [Microsoft smooth output with PlayReady](https://docs.aws.amazon.com/elemental-live/latest/ug/drm-mss-playready.html): Encryption mode: Always AES CTR (AES-128)
- [UDP/TS outputs with DVB Simulcrypt Standard](https://docs.aws.amazon.com/elemental-live/latest/ug/drm-udp-ts-simulcrypt.html): Encryption mode: Always AES CBC as described in ATIS-0800006

### [Licenses for add-on packages](https://docs.aws.amazon.com/elemental-live/latest/ug/ref-licenses.html)

Learn about add-on packages that you must purchase in order to enable some features of Elemental Live.

- [Purchasing a license](https://docs.aws.amazon.com/elemental-live/latest/ug/ref-licenses-purchase.html): To purchase an add-on package, contact your AWS Elemental sales person.
- [Add-on packages for features](https://docs.aws.amazon.com/elemental-live/latest/ug/ref-license-features.html): Some Elemental Live features require that you purchase an add-on package.
- [Video codec packages](https://docs.aws.amazon.com/elemental-live/latest/ug/ref-license-codecs-video.html): Some video codecs require an add-on package.
- [Audio codec packages](https://docs.aws.amazon.com/elemental-live/latest/ug/ref-license-codecs-audio.html): Some audio codecs require an add-on package.
