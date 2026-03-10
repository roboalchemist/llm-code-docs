# Source: https://docs.aws.amazon.com/elemental-server/latest/ug/llms.txt

# AWS Elemental Server User Guide

> Describes the components and features that AWS Elemental Server provides and how to use them.

- [What Is AWS Elemental Server?](https://docs.aws.amazon.com/elemental-server/latest/ug/what-is-aws-elemental-server.html)
- [Using SWF Files for Motion Graphic Overlay](https://docs.aws.amazon.com/elemental-server/latest/ug/motion-graphic-overlay-swf.html)
- [Setting Up Audio Channel Mapping](https://docs.aws.amazon.com/elemental-server/latest/ug/aws-elemental-server-audio-channel-mapping.html)
- [Using QVBR Rate Control Mode](https://docs.aws.amazon.com/elemental-server/latest/ug/using-qvbr.html)
- [Using IMF Inputs](https://docs.aws.amazon.com/elemental-server/latest/ug/using-imf-inputs.html)
- [Supported DRM Solutions with AWS Elemental Server](https://docs.aws.amazon.com/elemental-server/latest/ug/drm-support-solutions.html)
- [Document History](https://docs.aws.amazon.com/elemental-server/latest/ug/doc-history.html)

## [Including Inserted Images (Graphic Overlays)](https://docs.aws.amazon.com/elemental-server/latest/ug/graphic-overlay.html)

### [Still Image Inserter](https://docs.aws.amazon.com/elemental-server/latest/ug/setting-up-a-graphic-overlay.html)

The following procedure walks you through setting up a still graphic overlay.

- [Choosing Between Input, Stream, and Global Overlay](https://docs.aws.amazon.com/elemental-server/latest/ug/choosing-between-input-overlay-and-output-overlay.html): Depending on where and when you want your graphic overlays to appear, you might put them on inputs, in streams, or globally throughout the job.
- [Requirements for the Overlay File](https://docs.aws.amazon.com/elemental-server/latest/ug/requirements-for-the-overlay-file.html): Set up your image file for image insertion (graphic overlay) with AWS Elemental Server.
- [Sizing Your Overlay to Account for Scaling](https://docs.aws.amazon.com/elemental-server/latest/ug/about-overlay-scaling.html): Learn how to choose the size of your graphic overlay to account for video scaling.
- [Setting Up When Your Overlay Plays](https://docs.aws.amazon.com/elemental-server/latest/ug/when-your-still-overlay-plays.html): Learn how to set up your still graphic overlay to appear when you want it to play on your video.
- [Setting Up Overlapping Overlays](https://docs.aws.amazon.com/elemental-server/latest/ug/using-multiple-overlays.html): Use the image inserter (graphic overlay) feature with multiple overlays to include more than one image.

### [Motion Image Inserter](https://docs.aws.amazon.com/elemental-server/latest/ug/motion-graphic-overlay.html)

Set up your motion graphic file for image insertion (graphic overlay) with AWS Elemental Server.

- [Requirements for Motion Overlay Files](https://docs.aws.amazon.com/elemental-server/latest/ug/requirements-for-the-motion-overlay-file.html): Learn about the requirements for setting up your image file for image insertion (graphic overlay) with AWS Elemental Server.
- [Specifying the Motion Overlay File Location](https://docs.aws.amazon.com/elemental-server/latest/ug/specifying-the-motion-overlay-location.html): Specify one of the following valid locations for your overlay file:
- [Setting Up When Your Motion Graphic Plays](https://docs.aws.amazon.com/elemental-server/latest/ug/when-your-motion-overlay-plays.html): Learn how to set up your motion graphic overlay to appear when you want it on your video.


## [Including SCTE-35 Markers](https://docs.aws.amazon.com/elemental-server/latest/ug/scte-message-processing.html)

- [Processing Options](https://docs.aws.amazon.com/elemental-server/latest/ug/processing-options.html): Processing Options
- [Scope of Processing Depending on Outputs](https://docs.aws.amazon.com/elemental-server/latest/ug/scope-of-processing-depending-on-outputs.html): Scope of Processing Depending on Outputs
- [Blanking and Passthrough and Manifest Decoration](https://docs.aws.amazon.com/elemental-server/latest/ug/blanking-and-pass-through-and-manifest-decoration.html): Blanking and Passthrough and Manifest Decoration
- [Getting Ready: Setting the Ad Avail Mode](https://docs.aws.amazon.com/elemental-server/latest/ug/getting-ready-setting-the-ad-avail-mode.html): Getting Ready: Setting the Ad Avail Mode
- [Manifest Decoration](https://docs.aws.amazon.com/elemental-server/latest/ug/manifest-decoration.html): Manifest Decoration
- [Ad Avail Blanking and Blackout](https://docs.aws.amazon.com/elemental-server/latest/ug/ad-avail-blanking-and-blackout.html): Ad Avail Blanking and Blackout
- [Passthrough or Removal](https://docs.aws.amazon.com/elemental-server/latest/ug/pass-through-or-removal.html): Passthrough or Removal
- [POIS Conditioning](https://docs.aws.amazon.com/elemental-server/latest/ug/pois-conditioning.html): POIS Conditioning
- [Setting up POIS Conditioning via the REST API](https://docs.aws.amazon.com/elemental-server/latest/ug/setting-up-via-the-rest-api.html): Setting up via the REST API
- [Example Manifests for Apple HLS](https://docs.aws.amazon.com/elemental-server/latest/ug/example-manifests-hls.html): Example Manifests for Apple HLS


## [Tuning Your Video Quality](https://docs.aws.amazon.com/elemental-server/latest/ug/video-quality.html)

### [Image Processing Controls](https://docs.aws.amazon.com/elemental-server/latest/ug/vq-image-processing.html)

Topics

- [Image Processing â Scan Type â Key Controls](https://docs.aws.amazon.com/elemental-server/latest/ug/vq-scan-type-key.html)
- [Image Processing â Scan Type â Secondary Fields](https://docs.aws.amazon.com/elemental-server/latest/ug/vq-scan-type-secondary.html)
- [Image Processing â Noise Reduction](https://docs.aws.amazon.com/elemental-server/latest/ug/vq-noise-reduction.html)
- [Image Processing â framerate Conversion](https://docs.aws.amazon.com/elemental-server/latest/ug/vq-framerate-conversion.html)

### [Encoding Controls](https://docs.aws.amazon.com/elemental-server/latest/ug/vq-encoding-controls.html)

Topics

- [Encoding â Group of Pictures (GOP)](https://docs.aws.amazon.com/elemental-server/latest/ug/vq-gop.html)
- [Encoding â Rate Control](https://docs.aws.amazon.com/elemental-server/latest/ug/vq-rate-control.html)
- [Encoding â Rate Control Modes](https://docs.aws.amazon.com/elemental-server/latest/ug/vq-rate-control-modes.html): For Rate Control Mode, you will generally get the best video quality per bit by using the Quality Variable Bitrate (QVBR) rate control mode.
- [Encoding â Rate Control Tuning](https://docs.aws.amazon.com/elemental-server/latest/ug/vq-rate-control-tuning.html)
- [Encoding â Statmux Rate Control](https://docs.aws.amazon.com/elemental-server/latest/ug/vq-statmux.html)
- [Encoding â Quantization Controls](https://docs.aws.amazon.com/elemental-server/latest/ug/vq-quantization.html)
- [Encoding â Scan Type](https://docs.aws.amazon.com/elemental-server/latest/ug/vq-scan-type.html)
- [Encoding â MPEG-4 AVC (H.264) Controls](https://docs.aws.amazon.com/elemental-server/latest/ug/vq-avc.html)
- [Encoding â HEVC (H.265) Controls](https://docs.aws.amazon.com/elemental-server/latest/ug/vq-hevc.html)


## [Dolby Metadata](https://docs.aws.amazon.com/elemental-server/latest/ug/dolby-metadata.html)

- [Setting Up the Profile or Event Using the Web Interface](https://docs.aws.amazon.com/elemental-server/latest/ug/dolby-metadata-setup.html): This section describes how to set up the project or event using the web interface.
- [Output with the Dolby Digital Codec](https://docs.aws.amazon.com/elemental-server/latest/ug/dolby-metadata-output-dolby-digital-codec.html)
- [Output with Dolby Digital Plus (EC2, EAC3) Codec](https://docs.aws.amazon.com/elemental-server/latest/ug/dolby-metadata-output-dolby-digital-plus-codec.html)


## [Setting up HLS Rendition Groups](https://docs.aws.amazon.com/elemental-server/latest/ug/hls-rendition-groups.html)

- [How Video Is Associated with Audio Rendition Groups](https://docs.aws.amazon.com/elemental-server/latest/ug/hls-rendition-groups-how-video-is-associated-with-audio-rendition-groups.html): The different âsetsâ of media are created as follows:
- [Rules for Rendition Groups](https://docs.aws.amazon.com/elemental-server/latest/ug/hls-rendition-groups-rules.html): Rules exist for associating both audio and video streams in their respective rendition groups.
- [Examples](https://docs.aws.amazon.com/elemental-server/latest/ug/hls-rendition-groups-examples.html)

### [Creating HLS Rendition Groups](https://docs.aws.amazon.com/elemental-server/latest/ug/hls-rendition-groups-create.html)

The key to creating rendition groups is that each output you create must contain only one stream.

- [Getting Ready to Create HLS Rendition Groups](https://docs.aws.amazon.com/elemental-server/latest/ug/hls-rendition-groups-getting-ready-to-create.html)
- [Creating HLS Rendition Groups (Web Interface)](https://docs.aws.amazon.com/elemental-server/latest/ug/hls-rendition-groups-create-using-web-interface.html): Topics
- [Creating HLS Rendition Groups (REST API)](https://docs.aws.amazon.com/elemental-server/latest/ug/hls-rendition-groups-create-using-rest-api.html): The following information assumes that you have read and are therefore familiar with the construction and association of an output containing video and rendition groups.
- [Sample HLS Output Group with Audio Rendition Group Event Manifest](https://docs.aws.amazon.com/elemental-server/latest/ug/hls-rendition-groups-sample-manifest.html)


## [Setting Up Captions](https://docs.aws.amazon.com/elemental-server/latest/ug/setting-up-captions.html)

- [Setting the Timecode Source Settings](https://docs.aws.amazon.com/elemental-server/latest/ug/set-the-timecode-source-settings.html): If the captions in your AWS Elemental Server output don't appear or are not aligned with your video, make sure that you set the input and job-wide timecode source settings correctly.
- [Gathering Required Captions Information](https://docs.aws.amazon.com/elemental-server/latest/ug/gather-required-captions-information.html): **
- [Choose a Supported Output Captions Format](https://docs.aws.amazon.com/elemental-server/latest/ug/choose-a-supported-output-captions-format.html): Choose a Supported Output Captions Format

### [Creating Input Captions Selectors](https://docs.aws.amazon.com/elemental-server/latest/ug/create-input-caption-selectors.html)

When you set up captions, you begin by creating input captions selectors.

- [Ancillary (QuickTime Captions Track or Captions in MXF VANC Data)](https://docs.aws.amazon.com/elemental-server/latest/ug/ancillary.html): If your input captions are in either of the following formats, the service handles them as "ancillary" data:
- [ARIB](https://docs.aws.amazon.com/elemental-server/latest/ug/arib-input.html): For ARIB captions, create one input captions selector.
- [Embedded (CEA/EIA-608, CEA/EIA-708), SCTE-20, and Embedded+SCTE-20, and SCTE-20+Embedded](https://docs.aws.amazon.com/elemental-server/latest/ug/embedded.html): If your input captions are in any of the following formats, AWS Elemental Server handles them as "embedded."
- [DVB-Sub or SCTE-27 Formats](https://docs.aws.amazon.com/elemental-server/latest/ug/dvb-sub-or-scte-27.html): AWS Elemental Server supports DVB-Sub and SCTE-27 formats only in TS inputs.
- [Teletext](https://docs.aws.amazon.com/elemental-server/latest/ug/dvb-teletext.html): You can use Teletext captions in one of the following ways:
- [SCC, SMI, SRT, STL, TTML (Sidecar)](https://docs.aws.amazon.com/elemental-server/latest/ug/scc.html): SCC, SMI, SRT, STL, and TTML are sidecar captions formats.
- [Setting up for 608 XDS Data](https://docs.aws.amazon.com/elemental-server/latest/ug/setting-up-for-608-xds-data.html): Setting up for 608 XDS Data
- [Embedded Captions in Captions in VBI Data](https://docs.aws.amazon.com/elemental-server/latest/ug/embedded-captions-in-vbi-data.html): Captions in VBI Data

### [Including Captions in the Streams and Outputs](https://docs.aws.amazon.com/elemental-server/latest/ug/including-captions-in-outputs.html)

How you set up captions in your outputs depends on the output captions format.For more information, see .

- [Setting Up Output Captions in a Sidecar Format (SCC, SMI, SRT, TTML, WebVTT)](https://docs.aws.amazon.com/elemental-server/latest/ug/setting-up-output-captions-sidecar.html): To set up sidecar captions in an output, you create separate, captions-only streams.

### [Setting Up Output Captions for All Formats Except Sidecar](https://docs.aws.amazon.com/elemental-server/latest/ug/setting-up-output-captions-not-sidecar.html)

To set up output captions in any format other than sidecar, you add captions tabs to the stream that also contains the video and audio.

- [Font Styles for Burn-in](https://docs.aws.amazon.com/elemental-server/latest/ug/font-styles-for-burn-in.html): You can specify the look of the captions if the output captions are Burn-in by changing the font styles.
- [(Font Styles for DVB-Sub)](https://docs.aws.amazon.com/elemental-server/latest/ug/font-styles-for-dvb-sub.html): You can specify the look of the captions if the output captions are DVB-Sub.
- [Setting up the HLS Manifest](https://docs.aws.amazon.com/elemental-server/latest/ug/set-up-the-hls-manifest.html): If the captions are embedded captions and the output is HLS, you can choose to include caption language information in the manifest.
- [About Captions Handling in Outputs](https://docs.aws.amazon.com/elemental-server/latest/ug/caption-handling.html): Depending on the output captions format, AWS Elemental Server creates the captions differently in the outputs.

### [Examples for Setting Up Captions](https://docs.aws.amazon.com/elemental-server/latest/ug/examples.html)

View examples for setting up captions in AWS Elemental Server.

- [One Input Format to a Different Output Format, One Output](https://docs.aws.amazon.com/elemental-server/latest/ug/use-case-1-one-input-format-converted-to-one-different-format-in-one-output.html): Use Case 1: One Input Format Converted to One Different Format in One Output
- [One Input Format to the Same Output Format, One Output](https://docs.aws.amazon.com/elemental-server/latest/ug/use-case-2-one-input-format-to-one-output.html): One Input Format to the Same Output Format, One Output
- [One Input Format to Several Outputs](https://docs.aws.amazon.com/elemental-server/latest/ug/use-case-3-one-input-format-to-several-outputs.html): The input is set up with one format of captions and two or more languages.
- [One Input Format to Multiple Different Formats, One for Each Output](https://docs.aws.amazon.com/elemental-server/latest/ug/use-case-4-one-input-format-converted-to-different-formats-one-format-for-each-output.html): One Input Format to Multiple Different Formats, One for Each Output
- [One Captions Output Shared by Multiple Video Streams](https://docs.aws.amazon.com/elemental-server/latest/ug/use-case-5-one-captions-output-shared-by-multiple-video-streams.html): One Captions Output Shared Across a Streaming Package

### [Reference](https://docs.aws.amazon.com/elemental-server/latest/ug/reference.html)

Reference

- [Supported Containers - Input](https://docs.aws.amazon.com/elemental-server/latest/ug/supported-containers-input.html): Source Captions Are Inside the Input Container
- [Reference: Supported Captions Formats](https://docs.aws.amazon.com/elemental-server/latest/ug/supported-formats.html): The following lists show supported input and output captions types.


## [Creating HDR Outputs](https://docs.aws.amazon.com/elemental-server/latest/ug/working-with-hdr.html)

### [Setting Up HDR Jobs Using the Web Interface](https://docs.aws.amazon.com/elemental-server/latest/ug/setting-up-hdr-jobs-using-the-web-interface.html)

Setting up HDR jobs using the web interface

- [Input > Advanced: Managing Overwrite of Source Metadata](https://docs.aws.amazon.com/elemental-server/latest/ug/input-advanced-managing-overwrite-of-source-metadata.html): Input > Advanced: Managing Overwrite of Source Metadata
- [Stream > Video > Advanced: Include/Exclude Metadata per Output](https://docs.aws.amazon.com/elemental-server/latest/ug/stream-video-advanced-include-exclude-metadata-per-output.html): Stream > Video > Advanced: Include/Exclude Metadata per Output
- [Stream > Video > Advanced > Preprocessors > Color Corrector](https://docs.aws.amazon.com/elemental-server/latest/ug/stream-video-advanced-preprocessors-color-corrector.html): Stream > Video > Advanced > Preprocessors > Color Corrector
- [Setting Up HDR Jobs Using the REST API](https://docs.aws.amazon.com/elemental-server/latest/ug/setting-up-hdr-jobs-using-the-rest-api.html): Setting up HDR jobs using the REST API.


## [Creating Dolby Atmos Outputs](https://docs.aws.amazon.com/elemental-server/latest/ug/dolby-atmos.html)

- [Using Dolby Atmos Passthrough](https://docs.aws.amazon.com/elemental-server/latest/ug/using-dolby-atmos-passthrough.html): Learn how to pass through Dolby Digital Plus with Atmos audio to your AWS Elemental Server outputs.
- [Using Dolby Atmos Encoding](https://docs.aws.amazon.com/elemental-server/latest/ug/using-dolby-atmos-encoding.html): Learn how to encode Dolby Digital Plus with Atmos in your AWS Elemental Server jobs.
