# Source: https://docs.aws.amazon.com/mediapackage/latest/userguide/llms.txt

# AWS Elemental MediaPackage v2 User Guide

> Describes the components and features that AWS Elemental MediaPackage provides and how to use them.

- [IPv6 support](https://docs.aws.amazon.com/mediapackage/latest/userguide/mediapackagev2-ipv6-support.html)
- [Getting started](https://docs.aws.amazon.com/mediapackage/latest/userguide/getting-started.html)
- [Access control](https://docs.aws.amazon.com/mediapackage/latest/userguide/access-control-best-practices.html)
- [Delivering VOD content](https://docs.aws.amazon.com/mediapackage/latest/userguide/vod-content.html)
- [Creating live-to-VOD assets](https://docs.aws.amazon.com/mediapackage/latest/userguide/live-to-vod.html)
- [Data plane APIs](https://docs.aws.amazon.com/mediapackage/latest/userguide/dataplane-apis.html)
- [Tagging resources](https://docs.aws.amazon.com/mediapackage/latest/userguide/tagging.html)
- [Quotas](https://docs.aws.amazon.com/mediapackage/latest/userguide/quotas.html)
- [Document history](https://docs.aws.amazon.com/mediapackage/latest/userguide/doc-history.html)

## [What is AWS Elemental MediaPackage?](https://docs.aws.amazon.com/mediapackage/latest/userguide/what-is.html)

- [Are you a first-time user of MediaPackage?](https://docs.aws.amazon.com/mediapackage/latest/userguide/first-time-user.html): If you're a first-time user of MediaPackage, we recommend that you begin by reading the following sections:
- [Concepts and terminology](https://docs.aws.amazon.com/mediapackage/latest/userguide/what-is-terms.html): The following are AWS Elemental MediaPackage concepts and terms to be familiar with.
- [Supported inputs and outputs](https://docs.aws.amazon.com/mediapackage/latest/userguide/supported-inputs.html): Learn about the input types, input codecs, and output codecs that AWS Elemental MediaPackage supports for live content.

### [How MediaPackage works](https://docs.aws.amazon.com/mediapackage/latest/userguide/what-is-flow.html)

AWS Elemental MediaPackage uses just-in-time format conversion to deliver over-the-top (OTT) video from a single source to a wide variety of playback devices or content delivery networks (CDNs).

- [General live processing flow](https://docs.aws.amazon.com/mediapackage/latest/userguide/what-is-flow-gen.html): The following outlines the general flow of live content in MediaPackage:
- [Live input redundancy processing flow](https://docs.aws.amazon.com/mediapackage/latest/userguide/what-is-flow-ir.html): Achieve input redundancy in AWS Elemental MediaPackage by sending two streams to separate ingest domains on a channel in MediaPackage.
- [Supported features of AWS Elemental MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/userguide/what-is-features.html): MediaPackage supports the following features.
- [Related services](https://docs.aws.amazon.com/mediapackage/latest/userguide/related-services.html): You might use the following services when using MediaPackage.
- [Accessing MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/userguide/accessing-emp.html): You can access MediaPackage using any of the following methods.
- [Pricing for MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/userguide/pricing-for-emp.html): As with other AWS products, there are no contracts or minimum commitments for using MediaPackage.
- [Regions for MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/userguide/regions-and-endpoints.html): To reduce latency in your applications, MediaPackage offers a regional endpoint for your requests.


## [Setting up MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/userguide/setting-up.html)

- [Signing up for AWS](https://docs.aws.amazon.com/mediapackage/latest/userguide/setting-up-aws-sign-up.html)
- [Set up additional IAM permissions](https://docs.aws.amazon.com/mediapackage/latest/userguide/setting-up-iam-permissions.html): Learn how to identify the permissions that you must assign to users and other AWS identities so that they can use AWS Elemental MediaPackage.
- [Allowing MediaPackage to access other AWS services](https://docs.aws.amazon.com/mediapackage/latest/userguide/setting-up-create-trust-rel.html): Learn how to create IAM policies and roles that allow AWS Elemental MediaPackage to access other AWS services for features like CDN authorization and harvesting.
- [Download tools](https://docs.aws.amazon.com/mediapackage/latest/userguide/setting-up-tools.html): The AWS Management Console includes a console for MediaPackage, but if you want to access the services programmatically, see the following:


## [Delivering live content](https://docs.aws.amazon.com/mediapackage/latest/userguide/live-content.html)

### [Working with channel groups](https://docs.aws.amazon.com/mediapackage/latest/userguide/channel-groups.html)

Learn how to work with channel groups in AWS Elemental MediaPackage, including creating, viewing, modifying, and deleting them.

- [Creating a channel group](https://docs.aws.amazon.com/mediapackage/latest/userguide/channel-group-create.html): Learn how to create channel groups in AWS Elemental MediaPackage.
- [Viewing channel group details](https://docs.aws.amazon.com/mediapackage/latest/userguide/channel-group-view.html): Learn how to view channel group details in AWS Elemental MediaPackage.
- [Editing a channel group](https://docs.aws.amazon.com/mediapackage/latest/userguide/channel-group-edit.html): Learn how to edit the description of channel groups in AWS Elemental MediaPackage.
- [Deleting a channel group](https://docs.aws.amazon.com/mediapackage/latest/userguide/channel-group-delete.html): Learn how to delete a channel group to stop AWS Elemental MediaPackage from receiving content.

### [Working with channels](https://docs.aws.amazon.com/mediapackage/latest/userguide/channels.html)

Learn how to use and work with channels in AWS Elemental MediaPackage, including creating, viewing, and modifying them.

- [Creating a channel](https://docs.aws.amazon.com/mediapackage/latest/userguide/channels-create.html): Learn how to create a channel by using the AWS Elemental MediaPackage console, the AWS Command Line Interface (AWS CLI), or the MediaPackage API.
- [Viewing channel details](https://docs.aws.amazon.com/mediapackage/latest/userguide/channels-view.html): Learn how to view channel details by using the MediaPackage console, the AWS Command Line Interface (AWS CLI), or the MediaPackage API.
- [Editing a channel](https://docs.aws.amazon.com/mediapackage/latest/userguide/channels-edit.html): Learn how to edit channels by using the MediaPackage console, the AWS CLI, or the MediaPackage API.
- [Resetting channel history](https://docs.aws.amazon.com/mediapackage/latest/userguide/channel-reset.html): Learn how to reset the history of a channel using the MediaPackage console.
- [Deleting a channel](https://docs.aws.amazon.com/mediapackage/latest/userguide/channels-delete.html): Learn how to delete a channel to stop AWS Elemental MediaPackage from receiving further content.

### [Working with endpoints](https://docs.aws.amazon.com/mediapackage/latest/userguide/endpoints.html)

Learn how to create, view, modify, and delete origin endpoints in MediaPackage.

- [Creating an origin endpoint](https://docs.aws.amazon.com/mediapackage/latest/userguide/endpoints-create.html): Learn how to create origin endpoints in AWS Elemental MediaPackage.
- [Viewing an origin endpoint](https://docs.aws.amazon.com/mediapackage/latest/userguide/endpoints-view.html): Learn how to view a single origin endpoint details in AWS Elemental MediaPackage.
- [Editing an endpoint](https://docs.aws.amazon.com/mediapackage/latest/userguide/endpoints-edit.html): Learn how to edit an origin endpoint in AWS Elemental MediaPackage.
- [Resetting an endpoint](https://docs.aws.amazon.com/mediapackage/latest/userguide/endpoint-reset.html): Learn how to reset an origin endpoint in AWS Elemental MediaPackage.
- [Deleting an endpoint](https://docs.aws.amazon.com/mediapackage/latest/userguide/endpoints-delete.html): Learn how to delete an origin endpoint from AWS Elemental MediaPackage.
- [Previewing a manifest](https://docs.aws.amazon.com/mediapackage/latest/userguide/endpoints-preview.html): Preview an endpoint's manifest to ensure that MediaPackage is receiving the content stream and can package it.


## [MediaPackage features](https://docs.aws.amazon.com/mediapackage/latest/userguide/features-ref.html)

- [DASH](https://docs.aws.amazon.com/mediapackage/latest/userguide/dash-overview.html): Learn about Dynamic Adaptive Streaming over HTTP (DASH) support in AWS Elemental MediaPackage.
- [CMAF ingest](https://docs.aws.amazon.com/mediapackage/latest/userguide/cmaf-ingest.html): Learn how AWS Elemental MediaPackage Version 2 (v2) CMAF ingest delivers content in multiple streaming formats from a single workflow, with enhanced capabilities when using MediaPackage output groups.

### [Content encryption and DRM](https://docs.aws.amazon.com/mediapackage/latest/userguide/using-encryption.html)

Protect your content from unauthorized use through content encryption and digital rights management (DRM) in AWS Elemental MediaPackage.

- [Content key encryption](https://docs.aws.amazon.com/mediapackage/latest/userguide/drm-content-key-encryption.html): Enhance DRM security by encrypting content keys using certificates from AWS Certificate Manager.
- [Key rotation](https://docs.aws.amazon.com/mediapackage/latest/userguide/drm-content-key-rotation.html): Understand how MediaPackage handles key rotation for live content, including retrieval intervals and fallback behavior when keys are unavailable.
- [Managing DRM segment metadata](https://docs.aws.amazon.com/mediapackage/latest/userguide/drm-segment-metadata-management.html): Control DRM segment metadata inclusion in CMAF containers to improve device compatibility.
- [Exclude session keys](https://docs.aws.amazon.com/mediapackage/latest/userguide/drm-session-key-exclusion.html): Exclude session keys from HLS multivariant playlists to improve compatibility with legacy clients and provide granular access control.
- [Encryption presets](https://docs.aws.amazon.com/mediapackage/latest/userguide/drm-content-speke-v2-presets.html): Learn how you can use SPEKE Version 2.0 presets for unencrypted tracks and encrypted tracks with MediaPackage.
- [CMSD headers](https://docs.aws.amazon.com/mediapackage/latest/userguide/cmsd.html): Learn about common media server data (CMSD) headers from AWS Elemental MediaPackage.
- [Cross-Region failover](https://docs.aws.amazon.com/mediapackage/latest/userguide/cross-region-failover.html): Learn how to work with cross-region failover in AWS Elemental MediaPackage.

### [DASH manifest treatments](https://docs.aws.amazon.com/mediapackage/latest/userguide/dash-trtmts.html)

Learn how to change the format of the DASH manifest that AWS Elemental MediaPackage outputs.

- [Multi-period DASH](https://docs.aws.amazon.com/mediapackage/latest/userguide/multi-period.html): Explains how AWS Elemental MediaPackage inserts multiple periods into a DASH manifest.
- [DASH manifest compactness](https://docs.aws.amazon.com/mediapackage/latest/userguide/compacted.html): Learn how AWS Elemental MediaPackage makes DASH manifests shorter and easier to process on low-power devices.
- [HLS and LL-HLS](https://docs.aws.amazon.com/mediapackage/latest/userguide/hls-overview.html): Learn about HTTP Live Streaming (HLS) and Low-Latency HLS (LL-HLS) support in AWS Elemental MediaPackage.

### [Manifest filtering](https://docs.aws.amazon.com/mediapackage/latest/userguide/manifest-filtering.html)

Use MediaPackage manifest filtering to dynamically produce client manifests that include or exclude audio and video streams on a single endpoint.

- [Manifest filtering query parameters](https://docs.aws.amazon.com/mediapackage/latest/userguide/manifest-filter-query-parameters.html): Configure manifest filtering using query parameters appended to playback requests to dynamically filter audio and video streams based on specific criteria.
- [Special conditions for TS and CMAF manifests](https://docs.aws.amazon.com/mediapackage/latest/userguide/special-conditions-TS-CMAF-manifests.html): Understand the special considerations and limitations when using manifest filtering with TS (Transport Stream) and CMAF (Common Media Application Format) manifests.
- [Manifest filtering examples](https://docs.aws.amazon.com/mediapackage/latest/userguide/manifest-filtering-examples.html): Explore practical examples of manifest filtering to target specific devices, restrict premium content, and optimize playback for different scenarios.
- [Manifest filtering error conditions](https://docs.aws.amazon.com/mediapackage/latest/userguide/error-conditions-and-handling.html): Understand common error conditions and HTTP status codes that can occur when using manifest filtering with invalid parameters or malformed queries.
- [Media quality scores](https://docs.aws.amazon.com/mediapackage/latest/userguide/mqcs.html): Learn how AWS Elemental MediaPackage uses and creates quality metrics with Media Quality Confidence Scores (MQCS).
- [Metadata passthrough](https://docs.aws.amazon.com/mediapackage/latest/userguide/metadata-passthrough.html): Describes the metadata that MediaPackage passes through.

### [Microsoft Smooth Streaming](https://docs.aws.amazon.com/mediapackage/latest/userguide/mss-overview.html)

Learn how to deliver adaptive bitrate streaming to legacy devices using Microsoft Smooth Streaming.

- [MSS manifest structure](https://docs.aws.amazon.com/mediapackage/latest/userguide/mss-manifest-structure.html): Learn how to understand and troubleshoot Microsoft Smooth Streaming (MSS) manifest structure for legacy device streaming.
- [MSS encryption](https://docs.aws.amazon.com/mediapackage/latest/userguide/mss-encryption.html): Learn how to protect your Microsoft Smooth Streaming content for legacy devices using PlayReady DRM.
- [Testing MSS playback](https://docs.aws.amazon.com/mediapackage/latest/userguide/mss-testing-playback.html): Learn how to verify Microsoft Smooth Streaming playback on legacy devices like Xbox and smart TVs.
- [Troubleshooting MSS](https://docs.aws.amazon.com/mediapackage/latest/userguide/mss-troubleshooting.html): Learn how to diagnose and resolve common Microsoft Smooth Streaming playback issues on legacy devices.
- [CDN configuration for MSS](https://docs.aws.amazon.com/mediapackage/latest/userguide/mss-cdn-configuration.html): Learn how to configure your CDN for Microsoft Smooth Streaming content to optimize delivery to legacy devices.
- [Rendition groups](https://docs.aws.amazon.com/mediapackage/latest/userguide/rendition-groups.html): Describes how you can use audio rendition groups in MediaPackage.
- [Reset for channels and endpoints](https://docs.aws.amazon.com/mediapackage/latest/userguide/resetting.html): Describes channel and endpoint reset functionality in MediaPackage .

### [SCTE-35 messages](https://docs.aws.amazon.com/mediapackage/latest/userguide/scte.html)

Describes how you can change AWS Elemental MediaPackage handling of SCTE-35 messages.

- [How it works](https://docs.aws.amazon.com/mediapackage/latest/userguide/scte-works.html): Learn how AWS Elemental MediaPackage processes SCTE-35 messages and ad markers.
- [SCTE-35 settings](https://docs.aws.amazon.com/mediapackage/latest/userguide/scte-settings.html): Configure SCTE-35 message handling settings in AWS Elemental MediaPackage origin endpoints.
- [HLS EXT-X-DATERANGE ad markers](https://docs.aws.amazon.com/mediapackage/latest/userguide/ext-x-daterange-ad-marker.html): Describes how to use the SCTE-35 EXT-X-DATERANGE tag to signal ads and program transition events in HLS manifests.
- [HLS CUE tag ad markers](https://docs.aws.amazon.com/mediapackage/latest/userguide/ext-x-cue-ad-marker.html): Describes how to use SCTE-35 enhanced CUE tags to signal ads and program transition events in HLS manifests.
- [DASH ad markers](https://docs.aws.amazon.com/mediapackage/latest/userguide/dash-ad-markers.html): Configure DASH EventStream elements for SCTE-35 ad marker signaling.

### [Time-shifted viewing](https://docs.aws.amazon.com/mediapackage/latest/userguide/time-shifted.html)

Describes how you can enable start-over and catch-up program viewing in MediaPackage.

- [Time-shifted query parameters](https://docs.aws.amazon.com/mediapackage/latest/userguide/msettings-params.html): Learn how to use time-shifted viewing query parameters to control playback of live content from specific points in time.
- [Time delay](https://docs.aws.amazon.com/mediapackage/latest/userguide/time-delay.html)
- [Start and end parameters](https://docs.aws.amazon.com/mediapackage/latest/userguide/start-and-end-parameters-rules.html): MediaPackage accepts requests for up to 24 hours of content.
- [Window duration](https://docs.aws.amazon.com/mediapackage/latest/userguide/window-seconds.html): To dynamically request shorter manifests than the manifest window that's configured on the endpoint, use the ?aws.manifestsettings=manifest_window_seconds: query parameter.
- [Time-shifted viewing examples](https://docs.aws.amazon.com/mediapackage/latest/userguide/time-shift-examples.html): Explore practical examples of time-shifted viewing configurations in AWS Elemental MediaPackage to help you implement features like start-over, catch-up, and DVR functionality.

### [Trick-play](https://docs.aws.amazon.com/mediapackage/latest/userguide/trick-play.html)

Learn how to work with trick-play in AWS Elemental MediaPackage.

- [Using I-frame playlists](https://docs.aws.amazon.com/mediapackage/latest/userguide/using-i-frame-playlists.html): MediaPackage supports live trick-play by creating an I-frame playlist from an existing live stream.
- [Using image media playlists](https://docs.aws.amazon.com/mediapackage/latest/userguide/using-image-media-playlists.html): To use image-based trickplay, in your upstream encoder you create an HLS image media playlist that contains JPEG image segments.


## [Working with CDNs](https://docs.aws.amazon.com/mediapackage/latest/userguide/cdns.html)

- [CDN configuration recommendations](https://docs.aws.amazon.com/mediapackage/latest/userguide/cdn-recommendations.html): To configure your CDN distributions for delivering Apple HLS and low-latency HLS (LL-HLS) streams with MediaPackage, we suggest using the following approach.

### [CDN authorization](https://docs.aws.amazon.com/mediapackage/latest/userguide/cdn-auth.html)

Protect your AWS Elemental MediaPackage content from unauthorized access by configuring CDN authorization between your content delivery network and MediaPackage endpoints using custom HTTP headers and AWS Secrets Manager.

- [Setup CDN authorization](https://docs.aws.amazon.com/mediapackage/latest/userguide/cdn-auth-setup.html): Set up AWS Elemental MediaPackage CDN authorization by configuring custom HTTP headers in your content delivery network, creating secrets in AWS Secrets Manager, and enabling authorization on MediaPackage endpoints.
- [Rotate CDN secrets](https://docs.aws.amazon.com/mediapackage/latest/userguide/cdn-auth-rotate.html): Update and rotate CDN authorization secrets in AWS Elemental MediaPackage by synchronizing custom HTTP header values between your content delivery network and AWS Secrets Manager to maintain secure content access.
- [Troubleshoot CDN authorization](https://docs.aws.amazon.com/mediapackage/latest/userguide/cdn-auth-troubleshooting.html): Resolve common AWS Elemental MediaPackage CDN authorization issues including secret validation failures, IAM permission errors, and header mismatches that prevent content delivery from your MediaPackage endpoints.
- [CDN authorization best practices](https://docs.aws.amazon.com/mediapackage/latest/userguide/cdn-auth-best-practices.html): Implement security best practices for AWS Elemental MediaPackage CDN authorization including UUID secret generation, regular rotation schedules, monitoring strategies, and cost optimization through secret reuse across endpoints.


## [Security](https://docs.aws.amazon.com/mediapackage/latest/userguide/security.html)

### [Data protection](https://docs.aws.amazon.com/mediapackage/latest/userguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in AWS Elemental MediaPackage.

- [Implementing DRM](https://docs.aws.amazon.com/mediapackage/latest/userguide/data-protection-encrypt.html): Use encryption to protect your content from unauthorized access.

### [Identity and Access Management](https://docs.aws.amazon.com/mediapackage/latest/userguide/security-iam.html)

How to authenticate requests and manage access to your MediaPackage resources.

- [How AWS Elemental MediaPackage works with IAM](https://docs.aws.amazon.com/mediapackage/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to MediaPackage, learn what IAM features are available to use with MediaPackage.
- [Identity-based policy examples](https://docs.aws.amazon.com/mediapackage/latest/userguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify MediaPackage resources.

### [Resource-based policy examples](https://docs.aws.amazon.com/mediapackage/latest/userguide/using-iam-policies.html)

Manage MediaPackage resource permissions with IAM policies.

### [Policies and Permissions](https://docs.aws.amazon.com/mediapackage/latest/userguide/policies-permissions.html)

This page provides an overview of resource policies in MediaPackage and describes the basic elements of a policy.

- [Principals](https://docs.aws.amazon.com/mediapackage/latest/userguide/policy-principal.html): How to specify MediaPackage resources in a policy.
- [Actions, resources, and condition keys](https://docs.aws.amazon.com/mediapackage/latest/userguide/actions-resources-conditions-overview.html): AWS Elemental MediaPackage (service prefix: mediapackagev2) provides service-specific resources, actions, and condition context keys for use in IAM permission policies.
- [Ingest authorization](https://docs.aws.amazon.com/mediapackage/latest/userguide/ingest-auth.html): MediaPackage ingest requests usually originate from a video encoder.
- [Origin endpoint authorization](https://docs.aws.amazon.com/mediapackage/latest/userguide/endpoint-auth.html): MediaPackage egress requests usually originate from CDNs, but they may also come from other sources such as customer-owned monitoring scripts or operators using web browsers like Safari or Chrome to view the video stream and identify any issues.
- [AWS managed policies](https://docs.aws.amazon.com/mediapackage/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for MediaPackage and recent changes to those policies.
- [Authenticating Requests](https://docs.aws.amazon.com/mediapackage/latest/userguide/sig-v4-authenticating-requests.html): Use access keys to create a signing key and authenticate your request using AWS Signature Version 4.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/mediapackage/latest/userguide/cross-service-confused-deputy-prevention.html): Learn how to protect your AWS Elemental MediaPackage resources from the confused deputy problem using AWS global condition context keys.
- [Troubleshooting](https://docs.aws.amazon.com/mediapackage/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with MediaPackage and IAM.
- [Compliance validation](https://docs.aws.amazon.com/mediapackage/latest/userguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/mediapackage/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Elemental MediaPackage features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/mediapackage/latest/userguide/infrastructure-security.html): Learn how AWS Elemental MediaPackage isolates service traffic.


## [Logging and monitoring](https://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring.html)

- [Monitoring with CloudWatch metrics](https://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring-cloudwatch.html): You can monitor MediaPackage using CloudWatch, which collects raw data and processes it into readable, near real-time metrics.
- [Monitoring with EventBridge](https://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring-eventbridge-events.html): WIth Amazon EventBridge, you can automate your AWS services and respond automatically to system events such as application availability issues or error conditions.
- [Logging AWS Elemental MediaPackage API calls with AWS CloudTrail](https://docs.aws.amazon.com/mediapackage/latest/userguide/logging-using-cloudtrail.html): Learn about logging MediaPackage with AWS CloudTrail.
- [Access logging](https://docs.aws.amazon.com/mediapackage/latest/userguide/access-logging.html): Learn about AWS Elemental MediaPackage access logging.
- [Monitoring manifest update time in AWS Elemental MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring-manifest-last-updated.html): Learn about the AWS Elemental MediaPackage custom headers that indicate when the service last modified the manifest.
- [MediaPackage response headers](https://docs.aws.amazon.com/mediapackage/latest/userguide/response-headers.html): Learn about MediaPackage response headers as you build your workflows.
