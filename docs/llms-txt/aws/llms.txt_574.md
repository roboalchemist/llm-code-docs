# Source: https://docs.aws.amazon.com/mediapackage/latest/ug/llms.txt

# AWS Elemental MediaPackage User Guide

> Describes the components and features that AWS Elemental MediaPackage provides and how to use them.

- [IPv6 support](https://docs.aws.amazon.com/mediapackage/latest/ug/mediapackage-ipv6-support.html)
- [Tagging resources](https://docs.aws.amazon.com/mediapackage/latest/ug/tagging.html)
- [Working with AWS SDKs](https://docs.aws.amazon.com/mediapackage/latest/ug/sdk-general-information-section.html)
- [Related information](https://docs.aws.amazon.com/mediapackage/latest/ug/resources.html)
- [Document history](https://docs.aws.amazon.com/mediapackage/latest/ug/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/mediapackage/latest/ug/glossary.html)

## [What is AWS Elemental MediaPackage?](https://docs.aws.amazon.com/mediapackage/latest/ug/what-is.html)

- [Are you a first-time user of MediaPackage?](https://docs.aws.amazon.com/mediapackage/latest/ug/first-time-user.html): If you're a first-time user of MediaPackage, we recommend that you begin by reading the following sections:
- [Concepts and terminology](https://docs.aws.amazon.com/mediapackage/latest/ug/what-is-terms.html): AWS Elemental MediaPackage (MediaPackage) includes the following components:

### [Supported inputs and outputs](https://docs.aws.amazon.com/mediapackage/latest/ug/supported-inputs.html)

This section describes the input types, input codecs, and output codecs that AWS Elemental MediaPackage supports for live and video on demand (VOD) content.

- [Live supported codecs and input types](https://docs.aws.amazon.com/mediapackage/latest/ug/supported-inputs-live.html): The following sections describe supported input types, input codecs, and output codecs for live streaming content.
- [Live-to-VOD supported codecs and input types](https://docs.aws.amazon.com/mediapackage/latest/ug/supported-inputs-ltov.html): The following sections describe supported input types, input codecs, and output codecs for live-to-VOD assets that are harvested from streaming content in AWS Elemental MediaPackage.

### [VOD supported codecs and input types](https://docs.aws.amazon.com/mediapackage/latest/ug/supported-inputs-vod.html)

The following sections describe supported input types, input codecs, and output codecs for file-based video on demand (VOD) content.

- [Requirements for .smil manifests](https://docs.aws.amazon.com/mediapackage/latest/ug/supported-inputs-vod-smil.html): When sending a VOD MP4 asset to AWS Elemental MediaPackage, a .smil manifest must be included.

### [How MediaPackage works](https://docs.aws.amazon.com/mediapackage/latest/ug/what-is-flow.html)

AWS Elemental MediaPackage (MediaPackage) uses just-in-time format conversion to deliver over-the-top (OTT) video from a single source to a wide variety of playback devices or content delivery networks (CDNs).

### [Live content processing](https://docs.aws.amazon.com/mediapackage/latest/ug/what-is-flow-live.html)

In the processing flow for live content, encoders send live HLS streams to MediaPackage.

- [General live processing flow](https://docs.aws.amazon.com/mediapackage/latest/ug/what-is-flow-gen.html): The following outlines the general flow of live content in MediaPackage:
- [Live input redundancy processing flow](https://docs.aws.amazon.com/mediapackage/latest/ug/what-is-flow-ir.html): Achieve input redundancy in AWS Elemental MediaPackage by sending two streams to separate input URLs on a channel in MediaPackage.
- [VOD Content Processing](https://docs.aws.amazon.com/mediapackage/latest/ug/what-is-flow-vod.html): In the processing flow for VOD content, AWS Elemental MediaPackage ingests file-based video content from Amazon S3.

### [Live and VOD manifest reference](https://docs.aws.amazon.com/mediapackage/latest/ug/what-is-manifest.html)

AWS Elemental MediaPackage delivers live and video on demand (VOD) manifests to requesting devices.

- [Manifest properties](https://docs.aws.amazon.com/mediapackage/latest/ug/manifest-properties.html): These are the main properties in a manifest that determine if it's live or VOD:
- [Features of AWS Elemental MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/ug/what-is-features.html): MediaPackage supports the following features:
- [Related services](https://docs.aws.amazon.com/mediapackage/latest/ug/related-services.html)
- [Accessing MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/ug/accessing-emp.html): You can access MediaPackage using any of the following methods.
- [Pricing for MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/ug/pricing-for-emp.html): As with other AWS products, there are no contracts or minimum commitments for using MediaPackage.
- [Regions for MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/ug/regions-and-endpoints.html): To reduce latency in your applications, MediaPackage offers a regional endpoint for your requests.


## [Setting up](https://docs.aws.amazon.com/mediapackage/latest/ug/setting-up.html)

- [Signing up for AWS](https://docs.aws.amazon.com/mediapackage/latest/ug/setting-up-aws-sign-up.html)
- [Creating policies and non-administrative roles](https://docs.aws.amazon.com/mediapackage/latest/ug/setting-up-create-non-admin-iam.html): Create policies and non-administrative roles.
- [Allowing AWS Elemental MediaPackage to access other AWS services](https://docs.aws.amazon.com/mediapackage/latest/ug/setting-up-create-trust-rel.html): Some features require you to allow MediaPackage to access other AWS services, such as Amazon S3 and AWS Secrets Manager (Secrets Manager).
- [(Optional) Setting up encryption](https://docs.aws.amazon.com/mediapackage/latest/ug/set-up-encryption.html): Use encryption to protect your content from unauthorized use.
- [(Optional) Installing the AWS CLI](https://docs.aws.amazon.com/mediapackage/latest/ug/setting-up-install-cli.html): Install the AWS CLI if you want to use a unified tool to manage your AWS services from a command line.


## [Getting started](https://docs.aws.amazon.com/mediapackage/latest/ug/getting-started.html)

- [Live content delivery](https://docs.aws.amazon.com/mediapackage/latest/ug/getting-started-live.html): This Getting Started tutorial shows you how to use the AWS Elemental MediaPackage (MediaPackage) console to create a channel and endpoints for streaming live videos.
- [Live-to-VOD content delivery](https://docs.aws.amazon.com/mediapackage/latest/ug/getting-started-ltov.html): This Getting Started tutorial shows you how to use the AWS Elemental MediaPackage console to create a live-to-VOD (video on demand) asset and make it available for playback.
- [VOD content delivery](https://docs.aws.amazon.com/mediapackage/latest/ug/getting-started-vod.html): This Getting Started tutorial shows you how to use the AWS Elemental MediaPackage console to ingest video on demand (VOD) content and make it available for playback.


## [Delivering live content](https://docs.aws.amazon.com/mediapackage/latest/ug/live-content.html)

### [Working with channels](https://docs.aws.amazon.com/mediapackage/latest/ug/channels.html)

Provides steps for creating, viewing, modifying, and deleting channels in AWS Elemental MediaPackage.

- [Creating a channel](https://docs.aws.amazon.com/mediapackage/latest/ug/channels-create.html): Create a channel to start receiving content streams.
- [Viewing channel details](https://docs.aws.amazon.com/mediapackage/latest/ug/channels-view.html): View all channels that are configured in AWS Elemental MediaPackage, or view the details of a specific channel, including the endpoints that are associated with it.
- [Editing a channel](https://docs.aws.amazon.com/mediapackage/latest/ug/channels-edit.html): Edit a channel's description for easier identification later.
- [Rotating credentials on an input URL](https://docs.aws.amazon.com/mediapackage/latest/ug/channels-rotate-creds.html): Rotate credentials on an input URL to generate a new WebDAV user name and password.
- [Deleting a channel](https://docs.aws.amazon.com/mediapackage/latest/ug/channels-delete.html): Delete a channel to stop AWS Elemental MediaPackage from receiving further content.
- [Adding an endpoint to a channel](https://docs.aws.amazon.com/mediapackage/latest/ug/channels-add-endpoint.html): Add an endpoint to a channel to allow downstream video players and content delivery networks (CDNs) to start requesting content playback.

### [Working with endpoints](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints.html)

Provides steps to create, view, modify, and delete endpoints in AWS Elemental MediaPackage.

### [Creating an endpoint](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-create.html)

Create an endpoint on a channel to define how AWS Elemental MediaPackage prepares content for delivery.

### [Creating an HLS endpoint](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-hls.html)

Create an endpoint that formats content for devices that support Apple HLS.

- [New endpoint fields](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-hls-new.html): When you're creating an endpoint, don't put sensitive identifying information like customer account numbers into free-form fields such as the Name field.
- [Packager settings fields](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-hls-packager.html): The Packager settings fields hold general information about the endpoint.
- [Package encryption fields](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-hls-encryption.html): Protect your content from unauthorized use through content encryption and digital rights management (DRM).
- [Access control settings fields](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-hls-access-control.html): Define the access control values.
- [Stream selection fields](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-hls-include-streams.html): Define the streams to include.

### [Creating a DASH endpoint](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-dash.html)

Create an endpoint that formats content for devices that support MPEG-DASH.

- [New endpoint fields](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-dash-new.html): When you're creating an endpoint, don't put sensitive identifying information like customer account numbers into free-form fields such as the Name field.
- [Packager settings fields](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-dash-packager.html)
- [Package encryption fields](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-dash-encryption.html): Protect your content from unauthorized use through content encryption and digital rights management (DRM).
- [Access control settings fields](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-dash-access-control.html): Define the access control values.
- [Stream selection fields](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-dash-include-streams.html): Define the streams to include.

### [Creating a Microsoft Smooth Streaming endpoint](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-smooth.html)

Create an endpoint that formats content for devices that support Microsoft Smooth Streaming.

- [New endpoint fields](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-smooth-new.html): When you're creating an endpoint, don't put sensitive identifying information like customer account numbers into free-form fields such as the Name field.
- [Packager settings fields](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-smooth-packager.html): The Packager settings fields hold general information about the endpoint.
- [Package encryption fields](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-smooth-encryption.html): Protect your content from unauthorized use through content encryption and digital rights management (DRM).
- [Access control settings fields](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-smooth-access-control.html): Define the access control values.
- [Stream selection fields](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-smooth-include-streams.html): Define the streams to include.

### [Creating a CMAF endpoint](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-cmaf.html)

Create an endpoint that formats content for devices that support Apple HLS fragmented MP4 (fMP4).

- [New endpoint fields](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-cmaf-new.html): When you're creating an endpoint, don't put sensitive identifying information like customer account numbers into free-form fields such as the Name field.
- [Packager settings fields](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-cmaf-packager.html): The Packager settings fields hold general information about the endpoint.
- [Package encryption fields](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-cmaf-encryption.html): Protect your content from unauthorized use through content encryption and digital rights management (DRM).
- [Access control settings fields](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-cmaf-access-control.html): Define the access control values.
- [Stream selection fields](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-cmaf-include-streams.html): Define the streams to include.
- [Viewing all endpoints associated with a channel](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-view-all.html): View all endpoints that are associated with a specific channel to ensure that the content is available in all necessary stream formats.
- [Viewing a single endpoint](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-view-one.html): View the details about a specific endpoint to obtain its playback URL and to view the packaging settings that it's currently using.
- [Editing an endpoint](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-edit.html): Edit the packaging preferences on an endpoint to optimize the viewing experience.
- [Deleting an endpoint](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-delete.html): Endpoints can serve content until they're deleted.
- [Previewing an endpoint](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-preview.html): Preview an endpoint's playback to ensure that AWS Elemental MediaPackage is receiving the content stream and can package it.


## [Delivering VOD content](https://docs.aws.amazon.com/mediapackage/latest/ug/vod-content.html)

### [Working with packaging groups](https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-group.html)

Provides steps for creating, viewing, and deleting packaging groups in AWS Elemental MediaPackage.

- [Creating a packaging group](https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-group-create.html): Create a packaging group to hold all of the packaging configurations for an asset.
- [Viewing packaging group details](https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-group-view.html): You can view all packaging groups that are configured in AWS Elemental MediaPackage or the details of a specific packaging group, including the packaging configurations that are associated with it.
- [Editing a packaging group](https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-group-edit.html): Edit the packaging group to configure access control settings.
- [Deleting a packaging group](https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-group-delete.html): To stop AWS Elemental MediaPackage from delivering more content from an asset, delete the packaging group.
- [Adding a packaging configuration to a packaging group](https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-group-add-cfig.html): To define how AWS Elemental MediaPackage formats outputs from an asset, add a packaging configuration to a packaging group.

### [Working with packaging configurations](https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-cfig.html)

Provides steps for creating, viewing, and deleting packaging configurations in AWS Elemental MediaPackage.

### [Creating a packaging configuration](https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-cfig-create.html)

Create a packaging configuration to define how AWS Elemental MediaPackage prepares content for delivery from an asset.

### [Creating an HLS packaging configuration](https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-cfig-create-hls.html)

Create a packaging configuration that formats content for devices that support Apple HLS.

- [General settings fields](https://docs.aws.amazon.com/mediapackage/latest/ug/cfigs-hls-new.html): Provide general settings that apply to the entire packaging configuration.
- [Manifest settings fields](https://docs.aws.amazon.com/mediapackage/latest/ug/cfigs-hls-manset.html): Specify the format of the manifest that AWS Elemental MediaPackage delivers from an asset that uses this packaging configuration.
- [Stream selection fields](https://docs.aws.amazon.com/mediapackage/latest/ug/cfigs-hls-include-streams.html): Limit what incoming bitrates are available for playback and sort the streams in the output of an asset that uses this packaging configuration.
- [Encryption fields](https://docs.aws.amazon.com/mediapackage/latest/ug/cfigs-hls-encryption.html): Protect your content from unauthorized use through content encryption and digital rights management (DRM).

### [Creating a DASH packaging configuration](https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-cfig-create-dash.html)

Create a packaging configuration that formats content for devices that support DASH-ISO.

- [General settings fields](https://docs.aws.amazon.com/mediapackage/latest/ug/cfigs-dash-new.html): Provide general settings that apply to the entire packaging configuration.
- [Manifest settings fields](https://docs.aws.amazon.com/mediapackage/latest/ug/cfigs-dash-manset.html): Specify the format of the manifest that AWS Elemental MediaPackage delivers from an asset that uses this packaging configuration.
- [Stream selection fields](https://docs.aws.amazon.com/mediapackage/latest/ug/cfigs-dash-include-streams.html): Limit which incoming bitrates are available for playback and sort the streams in the output of an asset that uses this packaging configuration.
- [Encryption fields](https://docs.aws.amazon.com/mediapackage/latest/ug/cfigs-dash-encryption.html): Protect your content from unauthorized use through content encryption and digital rights management (DRM).

### [Creating a Microsoft Smooth packaging configuration](https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-cfig-create-mss.html)

Create a packaging configuration that formats content for devices that support Microsoft Smooth.

- [General settings fields](https://docs.aws.amazon.com/mediapackage/latest/ug/cfigs-mss-new.html): Provide general settings that apply to the entire packaging configuration.
- [Manifest settings fields](https://docs.aws.amazon.com/mediapackage/latest/ug/cfigs-mss-manset.html): Specify the format of the manifest that AWS Elemental MediaPackage delivers from an asset that uses this packaging configuration.
- [Stream selection fields](https://docs.aws.amazon.com/mediapackage/latest/ug/cfigs-mss-include-streams.html): Limit which incoming bitrates are available for playback and sort the streams in the output of an asset that uses this packaging configuration.
- [Encryption fields](https://docs.aws.amazon.com/mediapackage/latest/ug/cfigs-mss-encryption.html): Protect your content from unauthorized use through content encryption and digital rights management (DRM).

### [Creating a CMAF packaging configuration](https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-cfig-create-cmaf.html)

Create a packaging configuration that formats content for devices that support Apple HLS fragmented MP4 (fMP4).

- [General settings fields](https://docs.aws.amazon.com/mediapackage/latest/ug/cfigs-cmaf-new.html): Provide general settings that apply to the entire packaging configuration.
- [Manifest settings fields](https://docs.aws.amazon.com/mediapackage/latest/ug/cfigs-cmaf-manset.html): Specify the format of the manifest that AWS Elemental MediaPackage delivers from an asset that uses this packaging configuration.
- [Stream selection fields](https://docs.aws.amazon.com/mediapackage/latest/ug/cfigs-cmaf-include-streams.html): Limit which incoming bitrates are available for playback and sort the streams in the output of an asset that uses this packaging configuration.
- [Encryption fields](https://docs.aws.amazon.com/mediapackage/latest/ug/cfigs-cmaf-encryption.html): Protect your content from unauthorized use through content encryption and digital rights management (DRM).
- [Viewing packaging configuration details](https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-cfig-view.html): To ensure that the content is available in all necessary stream formats, view all packaging configurations that are associated with a specific packaging group or with an asset.
- [Editing a packaging configuration](https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-cfig-edit.html): You can't edit a packaging configuration.
- [Deleting a packaging configuration](https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-cfig-delete.html): To remove a playback endpoint from an asset, delete the packaging configuration.

### [Working with assets](https://docs.aws.amazon.com/mediapackage/latest/ug/asset.html)

Provides steps for creating, viewing, and deleting assets in AWS Elemental MediaPackage.

### [Ingesting an asset](https://docs.aws.amazon.com/mediapackage/latest/ug/asset-create.html)

To ingest source content, create an asset in AWS Elemental MediaPackage.

- [Asset access fields](https://docs.aws.amazon.com/mediapackage/latest/ug/asset-create-access.html): The following fields describe how AWS Elemental MediaPackage accesses the source content in your Amazon S3 bucket.
- [Asset details fields](https://docs.aws.amazon.com/mediapackage/latest/ug/asset-create-details.html): The following fields describe the source content that this asset uses.
- [Packaging settings field](https://docs.aws.amazon.com/mediapackage/latest/ug/asset-create-pkg.html): The following field determines how AWS Elemental MediaPackage packages outputs from this asset.
- [Viewing asset details](https://docs.aws.amazon.com/mediapackage/latest/ug/asset-view.html): You can view all assets that are configured in AWS Elemental MediaPackage or the details of a specific asset, including the packaging configurations that are associated with it.
- [Editing an asset](https://docs.aws.amazon.com/mediapackage/latest/ug/asset-edit.html): You can't edit an asset.
- [Deleting an asset](https://docs.aws.amazon.com/mediapackage/latest/ug/asset-delete.html): To remove the packaging group URLs and to stop AWS Elemental MediaPackage from delivering further content, delete an asset.


## [Creating live-to-VOD assets](https://docs.aws.amazon.com/mediapackage/latest/ug/ltov.html)

- [Live-to-VOD requirements](https://docs.aws.amazon.com/mediapackage/latest/ug/ltov-reqmts.html): Keep in mind these requirements when you're creating live-to-VOD assets in AWS Elemental MediaPackage.
- [How live-to-VOD works](https://docs.aws.amazon.com/mediapackage/latest/ug/ltov-how.html): In the processing flow for live-to-VOD (video on demand) content, AWS Elemental MediaPackage extracts a clip of video from a live content stream.

### [Working with harvest jobs](https://docs.aws.amazon.com/mediapackage/latest/ug/harvest-jobs.html)

A harvest job represents a request to extract a live-to-VOD (video on demand) asset from an endpoint for a specific timeframe in the past.

- [Creating a harvest job](https://docs.aws.amazon.com/mediapackage/latest/ug/hj-create.html): Create a harvest job to extract a live-to-VOD asset from an encrypted or clear (unencrypted) live HLS or DASH stream.
- [Viewing harvest job details](https://docs.aws.amazon.com/mediapackage/latest/ug/hj-view.html): View all harvest jobs that you created within the last 90 days.
- [Editing a harvest job](https://docs.aws.amazon.com/mediapackage/latest/ug/hj-edit.html): You can't edit a harvest job.
- [Deleting a harvest job](https://docs.aws.amazon.com/mediapackage/latest/ug/hj-delete.html): You can't delete a harvest job.


## [MediaPackage features](https://docs.aws.amazon.com/mediapackage/latest/ug/features-ref.html)

### [CDN authorization](https://docs.aws.amazon.com/mediapackage/latest/ug/cdn-auth.html)

Content Delivery Network (CDN) authorization helps you to protect your content from unauthorized use.

- [Setting up CDN authorization](https://docs.aws.amazon.com/mediapackage/latest/ug/cdn-auth-setup.html): Complete the following steps to set up CDN authorization.
- [Rotating the CDN header value](https://docs.aws.amazon.com/mediapackage/latest/ug/cdn-auth-rotate.html): If you change the CDN custom origin HTTP header value, you need to rotate the stored secret value in Secrets Manager.

### [Content encryption and DRM](https://docs.aws.amazon.com/mediapackage/latest/ug/using-encryption.html)

Protect your content from unauthorized use through content encryption and digital rights management (DRM) in AWS Elemental MediaPackage.

- [Choosing the right SPEKE Version](https://docs.aws.amazon.com/mediapackage/latest/ug/encryption-choosing-speke-version.html): SPEKE Version 1 supports the use of a single encryption key for all audio and video tracks, and uses CPIX Version 2.0.
- [Deploying SPEKE](https://docs.aws.amazon.com/mediapackage/latest/ug/encryption-deploying-speke.html): Your digital rights management (DRM) solution provider can help you get set up to use DRM encryption in MediaPackage.
- [Preparing and managing certificates for use with content keys](https://docs.aws.amazon.com/mediapackage/latest/ug/drm-content-key-encryption.html): AWS Elemental MediaPackage uses a Content Protection Information Exchange (CPIX) document to communicate with SPEKE about content keys that are used to encrypt your content.
- [Understanding key rotation behavior](https://docs.aws.amazon.com/mediapackage/latest/ug/drm-content-key-rotation.html): When you enable key rotation on live content from HLS, CMAF, and DASH endpoints, AWS Elemental MediaPackage retrieves content keys before the live content begins.
- [SPEKE Version 2.0 presets](https://docs.aws.amazon.com/mediapackage/latest/ug/drm-content-speke-v2-presets.html): Learn how you can use SPEKE Version 2.0 presets for unencrypted tracks and encrypted tracks with MediaPackage.
- [Removing tags from the parent manifest](https://docs.aws.amazon.com/mediapackage/latest/ug/drm-query-param.html): MediaPackage signals in the parent manifest the #EXT-X-SESSION-KEY tag for every track type on an HLS or CMAF endpoint.

### [DASH manifest treatments](https://docs.aws.amazon.com/mediapackage/latest/ug/dash-trtmts.html)

Learn how to change the format of the DASH manifest that AWS Elemental MediaPackage outputs.

- [Multi-period DASH](https://docs.aws.amazon.com/mediapackage/latest/ug/multi-period.html): Explains how AWS Elemental MediaPackage inserts multiple periods into a DASH manifest.
- [Compacted DASH manifests](https://docs.aws.amazon.com/mediapackage/latest/ug/compacted.html): Learn how AWS Elemental MediaPackage makes DASH manifests shorter and easier to process on low-power devices.

### [DASH manifest segment template format](https://docs.aws.amazon.com/mediapackage/latest/ug/segtemp-format.html)

Explains the format options for the SegmentTemplate object of the DASH manifest.

- [media Attribute](https://docs.aws.amazon.com/mediapackage/latest/ug/segtemp-format-media.html): The media attribute in the SegmentTemplate properties defines the URL where playback devices send segment requests.
- [duration Attribute](https://docs.aws.amazon.com/mediapackage/latest/ug/segtemp-format-duration.html): In a default DASH manifest, SegmentTemplate holds a SegmentTimeline.
- [Manifest filtering](https://docs.aws.amazon.com/mediapackage/latest/ug/manifest-filtering.html): Use MediaPackage manifest filtering to dynamically produce client manifests that include or exclude audio and video streams on a single endpoint.
- [Metadata passthrough](https://docs.aws.amazon.com/mediapackage/latest/ug/metadata-passthrough.html): Describes the metadata that MediaPackage passes through.
- [Rendition groups](https://docs.aws.amazon.com/mediapackage/latest/ug/rendition-groups.html): Describes how you can use audio rendition groups in MediaPackage.
- [SCTE-35 messages](https://docs.aws.amazon.com/mediapackage/latest/ug/scte.html): Describes how you can change AWS Elemental MediaPackage handling of SCTE-35 messages.
- [Time-shifted viewing](https://docs.aws.amazon.com/mediapackage/latest/ug/time-shifted.html): Describes how you can enable start-over and catch-up program viewing in AWS Elemental MediaPackage.
- [Trick-play](https://docs.aws.amazon.com/mediapackage/latest/ug/trick-play.html): Learn how to work with trick-play in AWS Elemental MediaPackage.


## [Security](https://docs.aws.amazon.com/mediapackage/latest/ug/security.html)

### [Data protection](https://docs.aws.amazon.com/mediapackage/latest/ug/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in AWS Elemental MediaPackage.

- [Implementing DRM](https://docs.aws.amazon.com/mediapackage/latest/ug/data-protection-encrypt.html): Use encryption to protect your content from unauthorized access.
- [Implementing CDN authorization](https://docs.aws.amazon.com/mediapackage/latest/ug/encryption-static-key-set-up.html): Use content delivery network (CDN) authorization to ensure only authorized devices can access your content.

### [Identity and Access Management](https://docs.aws.amazon.com/mediapackage/latest/ug/security-iam.html)

How to authenticate requests and manage access to your MediaPackage resources.

- [How AWS Elemental MediaPackage works with IAM](https://docs.aws.amazon.com/mediapackage/latest/ug/security_iam_service-with-iam.html): Before you use IAM to manage access to MediaPackage, learn what IAM features are available to use with MediaPackage.
- [Identity-based policy examples](https://docs.aws.amazon.com/mediapackage/latest/ug/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify MediaPackage resources.
- [Policy examples for secrets in AWS Secrets Manager](https://docs.aws.amazon.com/mediapackage/latest/ug/iam-policy-examples-asm-secrets.html): During setup, you create an IAM policy that you assign to AWS Elemental MediaPackage.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/mediapackage/latest/ug/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
- [Troubleshooting](https://docs.aws.amazon.com/mediapackage/latest/ug/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with MediaPackage and IAM.
- [Using Service-Linked Roles](https://docs.aws.amazon.com/mediapackage/latest/ug/using-service-linked-roles.html): How to use service-linked roles to give MediaPackage access to resources in your AWS account.
- [Logging and monitoring](https://docs.aws.amazon.com/mediapackage/latest/ug/security-log-monitor.html): Monitoring is an important part of maintaining the reliability, availability, and performance of MediaPackage and your AWS solutions.
- [Compliance validation](https://docs.aws.amazon.com/mediapackage/latest/ug/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/mediapackage/latest/ug/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Elemental MediaPackage features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/mediapackage/latest/ug/infrastructure-security.html): Learn how AWS Elemental MediaPackage isolates service traffic.


## [Logging and monitoring](https://docs.aws.amazon.com/mediapackage/latest/ug/monitoring.html)

### [Monitoring with CloudWatch metrics](https://docs.aws.amazon.com/mediapackage/latest/ug/monitoring-cloudwatch.html)

You can monitor AWS Elemental MediaPackage using CloudWatch, which collects raw data and processes it into readable, near real-time metrics.

- [Live content metrics](https://docs.aws.amazon.com/mediapackage/latest/ug/metrics.html): The AWS/MediaPackage namespace includes the following metrics for live content.
- [VOD content metrics](https://docs.aws.amazon.com/mediapackage/latest/ug/metrics-vod.html): The AWS/MediaPackage namespace includes the following metrics for video on demand (VOD) content.

### [Monitoring with CloudWatch Events](https://docs.aws.amazon.com/mediapackage/latest/ug/monitoring-cloudwatch-events.html)

Amazon CloudWatch Events enables you to automate your AWS services and respond automatically to system events such as application availability issues or error conditions.

- [AWS Elemental MediaPackage events](https://docs.aws.amazon.com/mediapackage/latest/ug/cloudwatch-events-example.html): AWS Elemental MediaPackage integrates with Amazon CloudWatch Events to notify you of certain events that affect your channels and endpoints.
- [Creating event notifications](https://docs.aws.amazon.com/mediapackage/latest/ug/cloudwatch-events-notification.html): You can use Amazon CloudWatch Events and Amazon Simple Notification Service (Amazon SNS) to notify you of new events.
- [Logging AWS Elemental MediaPackage API calls with AWS CloudTrail](https://docs.aws.amazon.com/mediapackage/latest/ug/logging-using-cloudtrail.html): Learn about logging AWS Elemental MediaPackage with AWS CloudTrail.
- [Access logging](https://docs.aws.amazon.com/mediapackage/latest/ug/access-logging.html): Learn about AWS Elemental MediaPackage access logging.
- [Monitoring manifest update time](https://docs.aws.amazon.com/mediapackage/latest/ug/monitoring-manifest-last-updated.html): Learn about the AWS Elemental MediaPackage custom headers that indicate when the service last modified the manifest.

### [Workflow monitor](https://docs.aws.amazon.com/mediapackage/latest/ug/monitor-with-workflow-monitor.html)

Analyze AWS media services and create signal maps between those services.

### [Configuring workflow monitor](https://docs.aws.amazon.com/mediapackage/latest/ug/monitor-with-workflow-monitor-configure.html)

To setup workflow monitor for the first time; you create the alarm and event templates, and discover signal maps that are used to monitor your media workflows.

### [Getting started](https://docs.aws.amazon.com/mediapackage/latest/ug/monitor-with-workflow-monitor-configure-getting-started.html)

The following steps provide a basic overview of using workflow monitor for the first time.

- [Workflow monitor IAM policies](https://docs.aws.amazon.com/mediapackage/latest/ug/monitor-with-workflow-monitor-configure-getting-started-IAM.html): Workflow monitor interacts with multiple AWS services to create signal maps, build CloudWatch and EventBridge resources, and CloudFormation templates.

### [Templates](https://docs.aws.amazon.com/mediapackage/latest/ug/monitor-with-workflow-monitor-configure-templates.html)

Learn how to configure the alarm and event templates that will be used to monitor your workflow.

### [CloudWatch alarms](https://docs.aws.amazon.com/mediapackage/latest/ug/monitor-with-workflow-monitor-configure-alarms.html)

Learn how to configure the alarm groups and templates that will be used to monitor your workflow.

- [Recommended templates](https://docs.aws.amazon.com/mediapackage/latest/ug/monitor-with-workflow-monitor-configure-alarms-recommended-templates.html): Learn how to use the recommended alarm templates created by AWS.
- [EventBridge rules](https://docs.aws.amazon.com/mediapackage/latest/ug/monitor-with-workflow-monitor-configure-notifications.html): Learn how to configure the EventBridge groups and templates that will be used to monitor your workflow.

### [Signal maps](https://docs.aws.amazon.com/mediapackage/latest/ug/monitor-with-workflow-monitor-configure-signal-maps.html)

Learn how to configure the workflow monitor signal maps.

- [Creating signal maps](https://docs.aws.amazon.com/mediapackage/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-create.html): Learn how to create the workflow monitor signal maps using the automatic discovery process.
- [Viewing signal maps](https://docs.aws.amazon.com/mediapackage/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-view.html): Workflow monitor signal maps allow you to see a visual mapping of all connected AWS resources in your media workflow.
- [Attaching templates](https://docs.aws.amazon.com/mediapackage/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-attach.html): After you have created alarm and event templates, you need to attach these to a signal map.
- [Deploying monitoring templates](https://docs.aws.amazon.com/mediapackage/latest/ug/monitor-with-workflow-monitor-configure-deploy.html): After you have attached the alarm and event templates to your signal map, you must deploy the monitoring.
- [Updating signal maps](https://docs.aws.amazon.com/mediapackage/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-update.html): If a change is made to your workflow, you might need to rediscover the signal map and redeploy monitoring resources.
- [Deleting signal maps](https://docs.aws.amazon.com/mediapackage/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-delete.html): If you not longer need a signal map, it can be deleted.
- [Quotas](https://docs.aws.amazon.com/mediapackage/latest/ug/monitor-with-workflow-monitor-configure-quotas.html): The following section contains quotas for workflow monitor resources.

### [Using workflow monitor](https://docs.aws.amazon.com/mediapackage/latest/ug/monitor-with-workflow-monitor-operate.html)

Use the overview and signal maps sections of the workflow monitor console to review the current status of the workflows and any associated alarms, metrics, and logs.

- [Overview](https://docs.aws.amazon.com/mediapackage/latest/ug/monitor-with-workflow-monitor-operate-overview.html): The Overview section of the workflow monitor console is a dashboard that provides at-a-glance information about your signal maps.
- [Logs and metrics](https://docs.aws.amazon.com/mediapackage/latest/ug/monitor-with-workflow-monitor-operate-logs-metrics.html): To view CloudWatch metrics and logs for a signal map, select the radio button next to the name of the signal map.
- [Using signal maps](https://docs.aws.amazon.com/mediapackage/latest/ug/monitor-with-workflow-monitor-operate-signal-maps.html): From the overview section of the console, you can select a specific signal map to view more information about that signal map and its attached monitoring resources.


## [Working with CDNs](https://docs.aws.amazon.com/mediapackage/latest/ug/cdns.html)

### [Creating a Distribution](https://docs.aws.amazon.com/mediapackage/latest/ug/cdns-create.html)

A distribution in Amazon CloudFront holds all information about content delivery, including where content is coming from and how it's tracked and managed.

- [From Amazon CloudFront](https://docs.aws.amazon.com/mediapackage/latest/ug/cdns-create-cf.html): After you create a channel and its endpoints in AWS Elemental MediaPackage, note the URLs for each of the endpoints.
- [Viewing a Distribution](https://docs.aws.amazon.com/mediapackage/latest/ug/cdns-view.html): As described in , you can view basic information about a distribution that was created in MediaPackage, such as the distribution ID and description.
- [Editing a Distribution](https://docs.aws.amazon.com/mediapackage/latest/ug/cdns-edit.html): Edit an Amazon CloudFront distribution from the CloudFront console.
- [Deleting a Distribution](https://docs.aws.amazon.com/mediapackage/latest/ug/cdns-delete.html): Delete an Amazon CloudFront distribution from the CloudFront console.


## [Code examples](https://docs.aws.amazon.com/mediapackage/latest/ug/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/mediapackage/latest/ug/service_code_examples_basics.html)

The following code examples show how to use the basics of MediaPackage with AWS SDKs.

### [Actions](https://docs.aws.amazon.com/mediapackage/latest/ug/service_code_examples_actions.html)

The following code examples show how to use MediaPackage with AWS SDKs.

- [ListChannels](https://docs.aws.amazon.com/mediapackage/latest/ug/example_mediapackage_ListChannels_section.html): Use ListChannels with an AWS SDK or CLI
- [ListOriginEndpoints](https://docs.aws.amazon.com/mediapackage/latest/ug/example_mediapackage_ListOriginEndpoints_section.html): Use ListOriginEndpoints with an AWS SDK or CLI


## [Quotas](https://docs.aws.amazon.com/mediapackage/latest/ug/quotas.html)

- [Live content quotas](https://docs.aws.amazon.com/mediapackage/latest/ug/live-quotas.html): This section describes the quotas for live content in AWS Elemental MediaPackage.
- [VOD content quotas](https://docs.aws.amazon.com/mediapackage/latest/ug/vod-quotas.html): This section describes the quotas for video on demand (VOD) content in AWS Elemental MediaPackage.
