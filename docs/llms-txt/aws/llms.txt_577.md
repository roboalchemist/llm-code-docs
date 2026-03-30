# Source: https://docs.aws.amazon.com/mediatailor/latest/ug/llms.txt

# AWS Elemental MediaTailor User Guide

> Use AWS Elemental MediaTailor to insert ads into your media service content. With MediaTailor, you can serve targeted ads to viewers while maintaining broadcast quality in over-the-top (OTT) video applications.

- [Setting up](https://docs.aws.amazon.com/mediatailor/latest/ug/setting-up.html)
- [Quotas](https://docs.aws.amazon.com/mediatailor/latest/ug/quotas.html)
- [MediaTailor resources](https://docs.aws.amazon.com/mediatailor/latest/ug/resources.html)
- [Document history](https://docs.aws.amazon.com/mediatailor/latest/ug/document-history.html)

## [What is AWS Elemental MediaTailor?](https://docs.aws.amazon.com/mediatailor/latest/ug/what-is.html)

### [MediaTailor concepts](https://docs.aws.amazon.com/mediatailor/latest/ug/what-is-terms.html)

Here's an overview of the concepts that are used throughout the AWS Elemental MediaTailor User Guide.

- [HLS playlist types](https://docs.aws.amazon.com/mediatailor/latest/ug/hls-playlist-types.html): Learn about the different types of HLS playlists used in streaming workflows with AWS Elemental MediaTailor.

### [DASH manifest types](https://docs.aws.amazon.com/mediatailor/latest/ug/dash-manifest-types.html)

Learn about the different types of DASH manifests used in streaming workflows with AWS Elemental MediaTailor.

- [Advanced concepts](https://docs.aws.amazon.com/mediatailor/latest/ug/dash-manifest-advanced-concepts.html): When working with DASH manifests in MediaTailor, understanding the following advanced concepts can help you configure and troubleshoot your streaming workflows more effectively:

### [How ad insertion works](https://docs.aws.amazon.com/mediatailor/latest/ug/what-is-flow.html)

AWS Elemental MediaTailor interacts between your content delivery network (CDN), origin server, and ad decision server (ADS) to stitch personalized ads into ad breaks within live and video on demand content.

- [Ad insertion event flow](https://docs.aws.amazon.com/mediatailor/latest/ug/mediatailor-event-flow.html): Learn the chronological sequence of events during ad insertion to understand how MediaTailor processes ad opportunities.


## [Getting started with MediaTailor](https://docs.aws.amazon.com/mediatailor/latest/ug/getting-started.html)

- [Getting started with MediaTailor ad insertion](https://docs.aws.amazon.com/mediatailor/latest/ug/getting-started-ad-insertion.html): To use AWS Elemental MediaTailor, you need an AWS account and permissions to access, view, and edit MediaTailor configurations.
- [Getting started with MediaTailor channel assembly](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-getting-started.html): This Getting Started tutorial shows you how to perform the following tasks:


## [Inserting ads](https://docs.aws.amazon.com/mediatailor/latest/ug/configurations.html)

- [Understanding ad insertion behavior](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html): Describes how AWS Elemental MediaTailor performs ad stitching for live and VOD content.

### [Server-guided ad insertion overview](https://docs.aws.amazon.com/mediatailor/latest/ug/server-guided.html)

Learn how MediaTailor server-guided ad insertion improves performance through cacheable manifests and client-side ad insertion.

- [SGAI feature compatibility](https://docs.aws.amazon.com/mediatailor/latest/ug/sgai-feature-compatibility.html): Compare MediaTailor feature compatibility between server-side ad insertion and server-guided ad insertion methods.
- [SGAI live configuration](https://docs.aws.amazon.com/mediatailor/latest/ug/sgai-live-configuration.html): Configure MediaTailor server-guided ad insertion for live streams to enable cacheable manifest personalization, reduce origin load, and improve scalability during live broadcasts.
- [SGAI VOD configuration](https://docs.aws.amazon.com/mediatailor/latest/ug/sgai-vod-configuration.html): Configure MediaTailor server-guided ad insertion for video-on-demand content to enable cacheable manifest personalization, improve CDN efficiency, and reduce origin load for VOD libraries.
- [Ad server integration requirements](https://docs.aws.amazon.com/mediatailor/latest/ug/vast.html): Learn the technical requirements for integrating ad servers with MediaTailor using VAST, VMAP, and VPAID standards for successful ad insertion workflows.

### [Configuration management](https://docs.aws.amazon.com/mediatailor/latest/ug/working-with-configurations.html)

Learn how to manage MediaTailor playback configurations including creating new configurations, viewing existing ones, editing settings, and deleting unused configurations.

- [Creating a configuration](https://docs.aws.amazon.com/mediatailor/latest/ug/configurations-create.html): Learn how to create a new MediaTailor playback configuration to establish content streams and provide access points for downstream playback devices.
- [Viewing configuration details](https://docs.aws.amazon.com/mediatailor/latest/ug/configurations-view.html): Learn how to view detailed information about existing MediaTailor playback configurations including settings, endpoints, and access URLs.
- [Editing configuration settings](https://docs.aws.amazon.com/mediatailor/latest/ug/configurations-edit.html): Learn how to edit existing MediaTailor playback configurations to update origin servers, ad decision servers, and CDN integration settings.
- [Deleting configurations](https://docs.aws.amazon.com/mediatailor/latest/ug/configurations-delete.html): Learn how to delete unused MediaTailor playback configurations to remove them from availability for playback requests.

### [Integrating a content source](https://docs.aws.amazon.com/mediatailor/latest/ug/integrating-origin.html)

Describes how to integrate a content source from an origin server with MediaTailor.

- [Input source requirements](https://docs.aws.amazon.com/mediatailor/latest/ug/stream-reqmts.html): A input source must meet the following requirements to work with MediaTailor:

### [Integrating an HLS source](https://docs.aws.amazon.com/mediatailor/latest/ug/manifest-hls.html)

AWS Elemental MediaTailor supports .m3u8 HLS manifests with an EXT-X-VERSION of 3 or higher for live streaming and video on demand (VOD).

- [Ad markers](https://docs.aws.amazon.com/mediatailor/latest/ug/hls-ad-markers.html): Learn about AWS Elemental MediaTailor requirements for ad markers in an HLS manifest.
- [Enabling ad marker passthrough](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-marker-passthrough.html): By default for HLS, MediaTailor personalized manifests don't include the SCTE-35 ad markers from the origin manifests.
- [Tag handling](https://docs.aws.amazon.com/mediatailor/latest/ug/manifest-hls-tags.html): This section describes how AWS Elemental MediaTailor manages tags in the personalized output manifest.
- [HLS manifest examples](https://docs.aws.amazon.com/mediatailor/latest/ug/manifest-hls-example.html): Examples of HLS origin manifests and personalized manifests used in AWS Elemental MediaTailor workflows.

### [Integrating an MPEG-DASH source](https://docs.aws.amazon.com/mediatailor/latest/ug/manifest-dash.html)

AWS Elemental MediaTailor supports .mpd live and video on demand (VOD) manifests that follow the guidelines for the DASH dynamic profile.

- [Ad markers](https://docs.aws.amazon.com/mediatailor/latest/ug/dash-ad-markers.html): Learn about AWS Elemental MediaTailor requirements for ad markers in a DASH manifest.
- [Ad avail duration](https://docs.aws.amazon.com/mediatailor/latest/ug/dash-ad-avail-duration.html): How AWS Elemental MediaTailor determines how many ads to use in an ad avail.
- [Segment numbering](https://docs.aws.amazon.com/mediatailor/latest/ug/dash-manifest-segment-numbering.html): MediaTailor supports media segments in <SegmentTemplate> that are defined using <SegmentTimeline> and the media attribute.
- [DASH MPD examples](https://docs.aws.amazon.com/mediatailor/latest/ug/manifest-dash-example.html): Examples of DASH origin MPDs and personalized MPDs used in AWS Elemental MediaTailor workflows.
- [Location feature](https://docs.aws.amazon.com/mediatailor/latest/ug/dash-location-feature.html): Learn how to use the DASH location feature for players that don't support sticky HTTP redirects.
- [Securing origin interactions with SigV4](https://docs.aws.amazon.com/mediatailor/latest/ug/origin-sigv4.html): Signature Version 4 (SigV4) is a signing protocol used to authenticate MediaTailor requests to supported origins over HTTPS.

### [Integrating with Google Ad Manager](https://docs.aws.amazon.com/mediatailor/latest/ug/gam-integration.html)

Learn about using GAM with AWS Elemental MediaTailor.

- [Server-side integration](https://docs.aws.amazon.com/mediatailor/latest/ug/gam-integration-ssl.html): Server-side ad requests to Google Ad Manager (Ad Manager) must include the SSL certificate that Ad Manager has issued to MediaTailor to authorize programmatic transactions.
- [Client-side integration](https://docs.aws.amazon.com/mediatailor/latest/ug/gam-integration-pal.html): A MediaTailor client-side integration is required to use the Google Ad Manager Programmatic Access Libraries (PAL) SDKs.
- [Customizing ad break behavior with ad break suppression](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-rules.html): Learn about customizing ad break behavior, configuring ad break suppression, avail suppression mode, and related parameters.
- [Bumper ad insertion](https://docs.aws.amazon.com/mediatailor/latest/ug/bumpers.html): Learn how to configure and insert short, non-skippable bumper ads at the beginning or end of ad breaks using MediaTailor.
- [Pre-roll ad insertion](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior-preroll.html): Learn how to configure and insert pre-roll ads at the beginning of live playback sessions before main content starts with MediaTailor.
- [Slate ad insertion](https://docs.aws.amazon.com/mediatailor/latest/ug/slate-management.html): Learn how to configure and use slate ads as default content to fill unfilled ad time and handle error conditions in MediaTailor live workflows.

### [Prefetching ads](https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html)

Learn how to use MediaTailor ad prefetching to reduce peak load on ad decision servers and decrease manifest delivery latency.

- [How prefetching works](https://docs.aws.amazon.com/mediatailor/latest/ug/understanding-prefetching.html): Understand how MediaTailor evaluates prefetch schedules and processes retrieval and consumption components for both single and recurring prefetch schedules.
- [Creating prefetch schedules](https://docs.aws.amazon.com/mediatailor/latest/ug/creating-prefetch-schedules.html): Learn how to create single and recurring prefetch schedules using the MediaTailor console, including configuring retrieval windows, consumption settings, and traffic shaping options.
- [TPS-based traffic shaping](https://docs.aws.amazon.com/mediatailor/latest/ug/tps-traffic-shaping.html): Learn about TPS-based traffic shaping as an alternative to time-window approaches, providing intuitive configuration based on ADS capacity limits and concurrent users.
- [Deleting prefetch schedules](https://docs.aws.amazon.com/mediatailor/latest/ug/deleting-prefetch-schedules.html): Learn how to delete prefetch schedules using the MediaTailor console when they are no longer needed for your ad insertion workflow.
- [Preconditioned ads](https://docs.aws.amazon.com/mediatailor/latest/ug/precondition-ads.html): In a typical ad insertion workflow, MediaTailor dynamically transcodes ads to match the content stream, saves them, and stitches the ads into the live stream.

### [Dynamic ad variables](https://docs.aws.amazon.com/mediatailor/latest/ug/variables.html)

Configure MediaTailor dynamic ad variables for ADS requests including session data, player parameters, domain variables, and configuration aliases to optimize ad targeting.

- [Session variables](https://docs.aws.amazon.com/mediatailor/latest/ug/variables-session.html): Configure MediaTailor session variables for ADS requests including SCTE-35 data, avail information, and session identifiers to enhance ad targeting accuracy.
- [Player variables](https://docs.aws.amazon.com/mediatailor/latest/ug/variables-player.html): Configure MediaTailor player variables for ADS requests using player_params query parameters and key-value pairs in template URLs for custom ad targeting.
- [Domain variables](https://docs.aws.amazon.com/mediatailor/latest/ug/variables-domains.html): Configure MediaTailor domain variables for multiple content and ad sources using dynamic domain configuration with URI parameters for flexible routing.

### [Configuration aliases](https://docs.aws.amazon.com/mediatailor/latest/ug/configuration-aliases-overview.html)

Learn how MediaTailor configuration aliases enable dynamic variable replacement for flexible URL routing.

- [Creating and using](https://docs.aws.amazon.com/mediatailor/latest/ug/creating-configuration-aliases.html): Learn how to create configuration aliases and use them as domain replacement variables during session initialization.
- [Example flow](https://docs.aws.amazon.com/mediatailor/latest/ug/configuration-aliases-examples.html): Review complete examples of configuration aliases and session initialization.
- [Passing ADS parameters](https://docs.aws.amazon.com/mediatailor/latest/ug/passing-paramters-to-the-ads.html): Configure MediaTailor parameter passing to ADS using session initialization methods with POST and GET requests for dynamic variables and custom targeting.
- [Parameter routing](https://docs.aws.amazon.com/mediatailor/latest/ug/parameter-routing-behavior.html): Understand how MediaTailor routes different types of query parameters to origin servers, ad decision servers, and CDN endpoints based on parameter prefixes.
- [MediaPackage integration](https://docs.aws.amazon.com/mediatailor/latest/ug/mediapackage-integration-param.html): Configure MediaTailor to work with MediaPackage time-shifted viewing using start and end query parameters for startover and catch-up functionality with live streams.
- [Session behavior](https://docs.aws.amazon.com/mediatailor/latest/ug/parameter-session-behavior.html): Understand how MediaTailor handles parameters during session initialization, persistence, and the limitations for parameter modification during active sessions.
- [Parameter reference](https://docs.aws.amazon.com/mediatailor/latest/ug/parameter-comprehensive-reference.html): Reference MediaTailor parameter character restrictions, length limitations, and supported formats for manifest and ADS parameters with validation requirements.
- [Parameter troubleshooting](https://docs.aws.amazon.com/mediatailor/latest/ug/parameter-troubleshooting.html): Troubleshoot MediaTailor parameter issues including character restrictions, URL encoding problems, and configuration alias errors with resolution steps.
- [Alias troubleshooting](https://docs.aws.amazon.com/mediatailor/latest/ug/configuration-aliases-troubleshooting.html): Troubleshoot MediaTailor configuration aliases issues including validation errors, resolution problems, and HTTP 400 error scenarios with systematic debugging.

### [MediaTailor manifest query parameters](https://docs.aws.amazon.com/mediatailor/latest/ug/manifest-query-parameters.html)

Configure MediaTailor to preserve and pass query parameters from session initialization to manifest URLs for CDN routing and token authorization workflows.

- [Origin query parameters](https://docs.aws.amazon.com/mediatailor/latest/ug/origin-query-parameters.html): Understand how MediaTailor handles query parameters in requests to content origins, including time-shifted viewing with MediaPackage start and end parameters.
- [MediaTailor character restrictions](https://docs.aws.amazon.com/mediatailor/latest/ug/manifest-query-parameters-character-restrictions.html): Understand MediaTailor character restrictions and URL-encoding support for manifest query parameters with validation requirements.
- [MediaTailor HLS implicit sessions](https://docs.aws.amazon.com/mediatailor/latest/ug/manifest-query-parameters-hls-implicit-session-initialization.html): Configure MediaTailor HLS implicit session initialization with manifest query parameters for multivariant and media playlist URLs.
- [MediaTailor DASH implicit sessions](https://docs.aws.amazon.com/mediatailor/latest/ug/manifest-query-parameters-dash-implicit-session-initialization.html): Configure MediaTailor DASH implicit session initialization with manifest query parameters for Location elements and SegmentTemplate attributes.
- [MediaTailor explicit session initialization](https://docs.aws.amazon.com/mediatailor/latest/ug/manifest-query-parameters-hls-and-dash-explicit-session-initialization.html): Configure MediaTailor explicit session initialization with manifestParams for HLS and DASH using POST or GET methods.
- [MediaTailor protocol-specific behavior](https://docs.aws.amazon.com/mediatailor/latest/ug/manifest-query-parameters-protocol-differences.html): Compare MediaTailor manifest query parameter behavior between HLS and DASH protocols with application locations and processing methods.
- [MediaTailor CDN integration](https://docs.aws.amazon.com/mediatailor/latest/ug/manifest-query-parameters-cdn-integration.html): Implement MediaTailor CDN integration with manifest query parameters for dynamic routing, authorization, and load balancing scenarios.

### [Reporting ad tracking data](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-reporting.html)

Provides steps for initiating server-side or client-side ad reporting in AWS Elemental MediaTailor.

### [Server-side tracking](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-reporting-server-side.html)

Configure MediaTailor server-side ad tracking to automatically report ad impressions, quartiles, and completion events to ad servers without requiring player-side implementation.

- [Beacon glossary](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-reporting-server-side-beacon-glossary.html): Comprehensive reference of all beacon types fired by MediaTailor during server-side tracking, including when they're fired, their purpose, and timing details.
- [Timing and caching behavior](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-reporting-server-side-timing-behavior.html): Understand how MediaTailor server-side tracking events are fired in relation to player caching and pre-loading behavior.
- [Tracking features](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-reporting-server-side-features.html): Explore the advanced capabilities that enhance MediaTailor server-side tracking reliability, accuracy, and performance.

### [Client-side tracking](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-reporting-client-side.html)

Learn about MediaTailor client-side tracking.

- [Ad-tracking schema and properties](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-reporting-client-side-ad-tracking-schema.html): Learn about the MediaTailor client-side ad-tracking schema and its properties.
- [Activity timing](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-reporting-client-side-ad-tracking-schema-activity-timing.html): Learn about ad-tracking activity timing for MediaTailor.
- [Player controls](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-reporting-client-side-ad-tracking-schema-player-controls.html): Learn about various player controls that MediaTailor client-side tracking metadata supports.
- [Beaconing](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-reporting-client-side-beaconing.html): Learn about the MediaTailor client-side beaconing and its properties.
- [Hybrid mode](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-reporting-hybrid-mode.html): Learn about the MediaTailor hybrid mode with server-side ad beacons.
- [Ad-tracking integrations](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-reporting-client-side-ad-tracking-integrations.html): Learn about client-side ad-tracking integrations in MediaTailor.

### [Overlay ads](https://docs.aws.amazon.com/mediatailor/latest/ug/overlay-ads.html)

Learn about AWS Elemental MediaTailor overlay ad support.

- [Prerequisites for using overlay ads](https://docs.aws.amazon.com/mediatailor/latest/ug/overlay-ads-prerequisites.html): Learn about prerequisites for using overlay ads with MediaTailor.

### [Getting started](https://docs.aws.amazon.com/mediatailor/latest/ug/overlay-ads-getting-started.html)

Learn how to get started using overlay ads with MediaTailor.

### [Enabling overlays](https://docs.aws.amazon.com/mediatailor/latest/ug/overlay-ads-getting-started-enabling.html)

Learn how to enable overlay-ad support in MediaTailor.

- [Manifest signaling](https://docs.aws.amazon.com/mediatailor/latest/ug/overlay-ads-manifest-signaling.html): Learn how to perform manifest signaling for overlay-ad support in MediaTailor.
- [ADS response](https://docs.aws.amazon.com/mediatailor/latest/ug/overlay-ads-ads-response.html): Learn how to configure the Ad Decision Server (ADS) response to work with overlay ads in MediaTailor.
- [Client-side tracking metadata](https://docs.aws.amazon.com/mediatailor/latest/ug/overlay-ads-client-side-tracking-metadata.html): MediaTailor places the overlay ads in the nonLinearAdsList of the avail.
- [Logging and metrics](https://docs.aws.amazon.com/mediatailor/latest/ug/overlay-ads-logging-and-metrics.html): Learn how to use logging and metrics with overlay ads in MediaTailor.
- [Billing for overlay ads in MediaTailor](https://docs.aws.amazon.com/mediatailor/latest/ug/overlay-ads-billing.html): Learn about how MediaTailor bills for using overlay ads.

### [Ad ID decoration](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-id-decoration.html)

Learn about AWS Elemental MediaTailor ad ID decoration in manifests.

- [Session State](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-id-session-state.html): The ad ID signaling feature must be enabled during session initialization.

### [Manifests and ad metadata insertion](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-id-manifest.html)

During the ad stitching process, MediaTailor adds to the manifest the unique ID associated with each creative being stitched.

- [HLS](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-id-manifest-hls.html): For a live HLS stream, MediaTailor only adds metadata when the stream contains PROGRAM-DATA-TIME tags, at least once per manifest duration.
- [DASH](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-id-manifest-dash.html): MediaTailor personalizes the manifest with creatives returned by the Ad Decision Server (ADS).
- [Ad Decision Server (ADS) interactions](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-id-ads-interactions.html): MediaTailor uses the creative id attribute value from the VAST response as a value in the ad ID signaling.
- [Client-side tracking API](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-id-client-side-tracking-api.html): The following example shows how a player SDK links the ad metadata in the manifest with the full tracking event data in the client-side tracking response payload with creativeId and adId.


## [Creating linear assembled streams](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly.html)

### [Working with source locations](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-source-locations.html)

Learn how to create and manage source locations for your channel assembly workflows.

- [Creating a source location](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-creating-source-locations.html): Learn how to create a source location using the MediaTailor console or API.

### [Configuring authentication for your source location](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-source-locations-access-configuration.html)

Learn how to set up authentication methods for your source location to secure access to your content.

- [Authenticating requests to Amazon S3 with SigV4](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-access-configuration-sigv4.html): Learn how to use Signature Version 4 (SigV4) to authenticate requests to your Amazon S3 origin.
- [Working with SigV4 for MediaPackage Version 2](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-access-configuration-sigv4-empv2.html): Learn how to use Signature Version 4 (SigV4) to authenticate requests to your MediaPackage Version 2 origin.

### [Working with AWS Secrets Manager access token authentication](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-access-configuration-access-token.html)

Learn how to use AWS Secrets Manager access tokens to authenticate requests between MediaTailor and your origin.

- [Configuring AWS Secrets Manager access token authentication](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-access-configuration-access-configuring.html): Learn the step-by-step process for setting up AWS Secrets Manager access token authentication for your source location.
- [Integrating with MediaPackage endpoints that use CDN authorization](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-access-configuration-access-token-integrating-emp-cdn-auth.html): Learn how to integrate MediaTailor with MediaPackage endpoints that use CDN authorization for secure content delivery.
- [How MediaTailor Secrets Manager access token authentication works](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-access-configuration-overview.html): Understand the workflow and process of how MediaTailor uses Secrets Manager access token authentication to secure communication with your origin.

### [Working with VOD sources](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-working-vod-sources.html)

Learn how to add and manage video on demand (VOD) sources for your channel assembly workflows.

- [Adding VOD sources to your source location](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-add-vod-source.html): Learn how to add VOD sources to your source location and set up package configurations for playback.

### [Working with live sources](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-working-live-sources.html)

Learn about live sources, adding them to a source location, and setting up MediaTailor and AWS Elemental MediaPackage workflows to use them.

- [Adding live sources to your source location](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-add-live-sources.html): Learn how to add live sources to a source location.
- [Using package configurations](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-package-configurations.html): Learn how to work with package configurations to support different streaming formats and device playback requirements.
- [Manifest caching](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-manifest-caching.html): Understand how MediaTailor caches source playlists and how to refresh cached manifests when needed.

### [Working with channels](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html)

Learn how to create, configure, and manage channels for your linear streaming workflows.

- [Create a channel](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-creating-channels.html): Learn how to create a channel using the MediaTailor console, including configuration options for playback modes, tiers, and outputs.
- [Using source groups with your channel's outputs](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-source-groups.html): Learn how source groups connect package configurations with channel outputs to create a cohesive playback experience.
- [Delete a channel](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-starting-stopping-channels.html): Learn how to properly stop and delete a channel when you no longer need it.

### [Adding a program](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-programs.html)

Learn how to add programs to your channel's schedule and configure them for playback.

- [Creating a program](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-adding-programs.html): Learn how to create programs for your channel schedule, including configuration options for VOD and live sources.
- [Defining audience cohorts and alternate content](https://docs.aws.amazon.com/mediatailor/latest/ug/working-with-program-rules.html): Learn how to create and work with program rules.
- [Generating audience-specific manifests](https://docs.aws.amazon.com/mediatailor/latest/ug/generating-audience-specific-manifests.html): Learn how to create audience-specific manifests for program rules.

### [Insert ads and ad breaks](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-integrating-mediatailor-ssai.html)

Learn how to insert personalized ads in your stream and set up ad breaks in your channel with MediaTailor.

- [Set up ad insertion](https://docs.aws.amazon.com/mediatailor/latest/ug/ca-setting-up-emt-ssai.topic.html): Learn how to set up MediaTailor for personalized ad insertion in your channel's stream.
- [SCTE-35 messages for ad breaks](https://docs.aws.amazon.com/mediatailor/latest/ug/ca-scte-35-messages.html): With MediaTailor, you can create a content channel based off of source location and VOD source resources.
- [Time-shifting a channel's playback](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-time-shift.html): Learn how to enable time-shifted viewing for your channel assembly streams.


## [Using a CDN](https://docs.aws.amazon.com/mediatailor/latest/ug/integrating-cdn.html)

- [CDN selection](https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-selection-guidance.html): Evaluate and select the optimal CDN provider for your AWS Elemental MediaTailor implementation based on geographic coverage, integration capabilities, features, and cost considerations.

### [Plan CDN integration](https://docs.aws.amazon.com/mediatailor/latest/ug/planning-cdn-integration.html)

Learn how to plan an effective CDN integration with AWS Elemental MediaTailor to improve viewer experience, reduce latency, and ensure reliable ad delivery.

- [Estimate traffic requirements](https://docs.aws.amazon.com/mediatailor/latest/ug/estimate-traffic.html): Learn how to accurately calculate viewer concurrency, bandwidth needs, and capacity requirements for your MediaTailor content delivery network (CDN) integration to ensure smooth content delivery during peak traffic periods.
- [Configure optimization strategies](https://docs.aws.amazon.com/mediatailor/latest/ug/optimize-cdn-config.html): Implement effective CDN optimization strategies for MediaTailor including origin shield configuration, caching policies, and edge node deployment to improve performance and reduce latency.
- [Customize planning](https://docs.aws.amazon.com/mediatailor/latest/ug/plan-for-workflow.html): Tailor your CDN integration strategy based on your specific MediaTailor workflow type - ad insertion, channel assembly, or combined workflows - to optimize performance and reliability.
- [Set up monitoring and scaling](https://docs.aws.amazon.com/mediatailor/latest/ug/setup-monitoring.html): Implement effective monitoring, alerting, and scaling strategies for your MediaTailor CDN integration to maintain optimal performance during normal operations and high-traffic events.
- [Optimize costs](https://docs.aws.amazon.com/mediatailor/latest/ug/optimize-costs.html): Balance performance with cost efficiency for your MediaTailor CDN integration using strategies like traffic pattern analysis, reserved capacity agreements, and effective caching policies.
- [Test your implementation](https://docs.aws.amazon.com/mediatailor/latest/ug/test-implementation.html): Ensure reliable viewer experiences by thoroughly testing your MediaTailor CDN integration with load testing, failover scenarios, and gradual ramp-up strategies before production deployment.
- [Troubleshoot common issues](https://docs.aws.amazon.com/mediatailor/latest/ug/troubleshooting-cdn.html): Identify and resolve common MediaTailor CDN integration challenges including manifest delivery problems, segment delivery issues, and performance bottlenecks before they impact your viewers.

### [Set up CDN integration](https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-configuration.html)

Learn how to integrate AWS Elemental MediaTailor with a content delivery network (CDN) to improve performance, scalability, and viewer experience.

- [Set up CDN routing behaviors](https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-routing-behaviors.html): Learn how to configure your CDN to route different types of requests appropriately for AWS Elemental MediaTailor integration.
- [Set up CDN mapping](https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-mapping-mediatailor.html): Learn how to configure AWS Elemental MediaTailor to use your CDN domain names for content and ad segment delivery.
- [Security best practices](https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-security-best-practices.html): Learn how to implement security best practices for your AWS Elemental MediaTailor CDN integration.

### [Ad insertion with CDN](https://docs.aws.amazon.com/mediatailor/latest/ug/ssai-cdn-workflow.html)

Learn how to set up server-side ad insertion (SSAI) with a content delivery network (CDN) for AWS Elemental MediaTailor to deliver targeted, personalized ads in your video streams.

- [Understand CDN architecture](https://docs.aws.amazon.com/mediatailor/latest/ug/ssai-cdn-architecture-overview.html): Learn the fundamental architecture concepts for integrating AWS Elemental MediaTailor server-side ad insertion with content delivery networks (CDNs).
- [Set up basic ad insertion](https://docs.aws.amazon.com/mediatailor/latest/ug/configuring-ssai-cdn.html): Follow step-by-step instructions to configure AWS Elemental MediaTailor server-side ad insertion with a content delivery network (CDN) for maximum revenue potential.
- [SSAI with channel assembly](https://docs.aws.amazon.com/mediatailor/latest/ug/ssai-ca-integration.html): Learn how to combine AWS Elemental MediaTailor server-side ad insertion (SSAI) with channel assembly to create revenue-generating linear channels with targeted advertising.
- [Optimize CDN performance](https://docs.aws.amazon.com/mediatailor/latest/ug/ssai-cdn-performance.html): Learn how to optimize the performance of your server-side ad insertion (SSAI) implementation with content delivery networks (CDNs) to deliver broadcast-quality streaming experiences.
- [Monitor CDN operations](https://docs.aws.amazon.com/mediatailor/latest/ug/ssai-cdn-monitor.html): Learn how to implement comprehensive monitoring and analytics for your server-side ad insertion (SSAI) implementation with content delivery networks (CDNs).
- [Troubleshoot ad insertion with CDNs](https://docs.aws.amazon.com/mediatailor/latest/ug/troubleshooting-ssai-cdn.html): Diagnose and resolve common issues with AWS Elemental MediaTailor server-side ad insertion and CDN integration to ensure uninterrupted revenue streams.

### [Channel assembly with CDN](https://docs.aws.amazon.com/mediatailor/latest/ug/ca-cdn-wflw.html)

Follow these steps to implement and optimize AWS Elemental MediaTailor channel assembly with a content delivery network (CDN) for improved performance, reliability, and viewer experience.

- [Understand CDN architecture](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-cdn-architecture.html): Learn how AWS Elemental MediaTailor channel assembly integrates with content delivery networks (CDNs) to deliver linear streaming channels with improved performance and global reach.
- [Basic setup](https://docs.aws.amazon.com/mediatailor/latest/ug/ca-cdn-setup-basic.html): Follow these step-by-step instructions to configure a basic integration between AWS Elemental MediaTailor channel assembly and a content delivery network (CDN).
- [Configure base URLs](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-cdn-baseurl.html): Learn how to properly configure base URLs in AWS Elemental MediaTailor channel assembly to work with your content delivery network (CDN).
- [Implement ad insertion](https://docs.aws.amazon.com/mediatailor/latest/ug/ca-cdn-setup-advanced.html): Learn how to combine AWS Elemental MediaTailor channel assembly with server-side ad insertion (SSAI) and CDN delivery to create monetized linear channels with personalized advertising.
- [Configure time-shifted viewing](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-cdn-timeshift.html): Learn how to enable DVR-like functionality such as pause, rewind, and start-over for your AWS Elemental MediaTailor channel assembly linear channels.
- [Monitor CDN operations](https://docs.aws.amazon.com/mediatailor/latest/ug/ca-cdn-monitor.html): Learn how to implement effective monitoring for your AWS Elemental MediaTailor channel assembly and CDN integration.
- [Complete optimization guide](https://docs.aws.amazon.com/mediatailor/latest/ug/ca-cdn-optimize-reference.html): For comprehensive CDN optimization guidance for channel assembly implementations, see the consolidated optimization guide.

### [MediaPackage CDN integration](https://docs.aws.amazon.com/mediatailor/latest/ug/mediapackage-integration.html)

Learn how to integrate AWS Elemental MediaTailor with AWS Elemental MediaPackage and a content delivery network (CDN) to deliver personalized video ads at scale with optimal streaming performance and global reach.

- [Manifest filtering](https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-emp-manifest-filtering.html): Implement AWS Elemental MediaPackage manifest filtering with AWS Elemental MediaTailor to dynamically customize video stream delivery for different viewers, optimize content for specific devices, and create tiered subscription services with personalized ad insertion.
- [CDN caching](https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-emp-caching.html): Optimize your CDN caching configuration for AWS Elemental MediaPackage and AWS Elemental MediaTailor integration to improve streaming performance, reduce origin server load, and minimize bandwidth costs through efficient cache policies and TTL settings.
- [CDN performance](https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-emp-monitoring.html): Set up comprehensive monitoring for your AWS Elemental MediaPackage and CDN integration with AWS Elemental MediaTailor to track performance metrics, optimize cache efficiency, monitor streaming quality, and quickly identify issues before they impact viewers.
- [CDN integration troubleshooting](https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-emp-troubleshooting.html): Diagnose and resolve common issues with AWS Elemental MediaPackage and CDN integration when using AWS Elemental MediaTailor for ad insertion, including manifest filtering errors, cache performance problems, and playback issues.

### [CloudFront integration](https://docs.aws.amazon.com/mediatailor/latest/ug/cloudfront-specific-recommendations.html)

Learn how to integrate AWS Elemental MediaTailor with Amazon CloudFront to improve content delivery performance and reliability.

- [Basic CloudFront setup](https://docs.aws.amazon.com/mediatailor/latest/ug/cloudfront-basic-setup.html): Learn how to set up a basic Amazon CloudFront distribution for AWS Elemental MediaTailor to improve content delivery performance.
- [Performance optimization](https://docs.aws.amazon.com/mediatailor/latest/ug/cloudfront-performance-optimization.html): Learn how to enhance your AWS Elemental MediaTailor and Amazon CloudFront integration with advanced performance features.
- [Multi-Region resilience](https://docs.aws.amazon.com/mediatailor/latest/ug/media-quality-resiliency.html): Learn how to implement Media Quality-Aware Resiliency (MQAR) to automatically select the highest quality content source in a multi-Region deployment.
- [Monitoring and troubleshooting](https://docs.aws.amazon.com/mediatailor/latest/ug/monitoring-and-troubleshooting.html): Learn how to monitor performance and troubleshoot issues with your Amazon CloudFront and AWS Elemental MediaTailor integration.
- [Third-party CDN setup](https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-provider-specific.html): Learn how to configure third-party CDNs like Akamai and Fastly to deliver personalized ads with AWS Elemental MediaTailor.

### [CDN performance optimization](https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-optimization.html)

Learn how to optimize CDN performance for AWS Elemental MediaTailor implementations including server-side ad insertion (SSAI), channel assembly, and combined workflows.

- [Caching optimization](https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-optimize-caching.html): Configure optimal caching settings for AWS Elemental MediaTailor CDN integrations across different workflow types and content formats.
- [Request routing optimization](https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-optimize-routing.html): Configure optimal request routing for AWS Elemental MediaTailor CDN integrations to improve performance and reliability.
- [Performance benchmarks](https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-performance-benchmarks.html): Performance targets and benchmarks for AWS Elemental MediaTailor CDN integrations across all workflow types.

### [Advanced optimization](https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-advanced-optimization.html)

Advanced optimization techniques for AWS Elemental MediaTailor CDN integrations including origin shield, compression, and regional optimization.

- [CDN architecture](https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-architecture-considerations.html): Learn how to position your CDN, implement cache behaviors, and configure error handling to create a robust and scalable AWS Elemental MediaTailor architecture that maximizes performance and reliability.
- [Advanced CDN features](https://docs.aws.amazon.com/mediatailor/latest/ug/advanced-cdn-features.html): Optimize viewer experience and content delivery by implementing advanced CDN features including Media Quality-Aware Routing (MQAR), manifest filtering, and multi-CDN strategies with AWS Elemental MediaTailor.
- [CDN monitoring](https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-monitoring.html): Monitor your AWS Elemental MediaTailor and CDN integration to ensure reliable content delivery and optimal performance.

### [CDN integration testing](https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-integration-testing.html)

Validate MediaTailor CDN integration with systematic testing approaches including environment setup, load testing, and deployment strategies.

- [Testing prerequisites](https://docs.aws.amazon.com/mediatailor/latest/ug/testing-prerequisites.html): Prepare MediaTailor CDN integration testing environment with required resources, tools, and configurations for comprehensive validation.
- [Systematic testing methodology](https://docs.aws.amazon.com/mediatailor/latest/ug/systematic-testing-approach.html): Follow systematic MediaTailor CDN integration testing methodology with phased approach for comprehensive validation and issue identification.
- [Pre-deployment checklist](https://docs.aws.amazon.com/mediatailor/latest/ug/testing-checklist.html): Complete MediaTailor CDN integration testing checklist to ensure readiness for production deployment and optimal performance.
- [Testing tools reference](https://docs.aws.amazon.com/mediatailor/latest/ug/testing-tools-reference.html): Reference guide for MediaTailor CDN integration testing tools including command-line utilities, browser tools, and debugging resources.

### [Troubleshoot CDN integration](https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-troubleshooting.html)

Resolve MediaTailor CDN integration issues including manifest errors, segment delivery problems, and performance optimization.

- [Quick diagnostic checklist](https://docs.aws.amazon.com/mediatailor/latest/ug/quick-diagnostic-checklist.html): Use this MediaTailor CDN diagnostic checklist to quickly identify integration issues and determine the appropriate troubleshooting approach.
- [Integration testing](https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-testing-procedures.html): Comprehensive testing procedures to validate your MediaTailor CDN integration before production deployment.
- [Manifest 404 errors](https://docs.aws.amazon.com/mediatailor/latest/ug/common-integration-issues.html): Resolve MediaTailor CDN manifest 404 errors including multivariant playlist, media playlist, and MPD delivery failures with step-by-step troubleshooting.
- [Manifest delivery issues](https://docs.aws.amazon.com/mediatailor/latest/ug/diagnose-manifest-issues.html): Troubleshoot MediaTailor CDN manifest delivery issues including incorrect ads, caching problems, and playlist loading failures.
- [Segment delivery issues](https://docs.aws.amazon.com/mediatailor/latest/ug/diagnose-segment-issues.html): Resolve MediaTailor CDN segment delivery issues including buffering problems, CORS errors, and routing configuration failures.
- [Session management issues](https://docs.aws.amazon.com/mediatailor/latest/ug/diagnose-session-issues.html): Resolve MediaTailor CDN session management issues including session ID inconsistencies and initialization problems.
- [Ad break timing issues](https://docs.aws.amazon.com/mediatailor/latest/ug/diagnose-timing-issues.html): Fix MediaTailor CDN ad break timing issues including SCTE-35 synchronization problems and timing drift caused by caching.
- [Performance and latency issues](https://docs.aws.amazon.com/mediatailor/latest/ug/diagnose-performance-issues.html): Diagnose and resolve MediaTailor CDN performance issues including slow response times, latency problems, and cache optimization.
- [Inconsistent device behavior](https://docs.aws.amazon.com/mediatailor/latest/ug/resolve-inconsistent-behavior.html): Resolve MediaTailor CDN inconsistent behavior across devices including player compatibility issues and device-specific targeting problems.

### [CDN integration log analysis reference](https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-log-error-reference.html)

Analyze CDN logs and MediaTailor error codes to identify root causes of CDN integration issues and optimize performance.

- [CDN log interpretation](https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-log-interpretation.html): Interpret MediaTailor CDN log entries, HTTP status codes, and cache behaviors to identify performance issues and optimization opportunities.
- [Error codes reference](https://docs.aws.amazon.com/mediatailor/latest/ug/emt-error-codes-reference.html): Understand MediaTailor error codes in CDN context and learn how to troubleshoot common integration issues and HTTP status codes.
- [Log analysis tools](https://docs.aws.amazon.com/mediatailor/latest/ug/log-analysis-techniques.html): Use advanced MediaTailor CDN log analysis tools and monitoring techniques to automate troubleshooting and optimize performance.

### [CloudFormation automation](https://docs.aws.amazon.com/mediatailor/latest/ug/automating-cdn-integration.html)

Learn how to use AWS CloudFormation to deploy AWS Elemental MediaTailor with Amazon CloudFront integration, including preparation, deployment, testing, and customization steps.

- [Why use AWS CloudFormation](https://docs.aws.amazon.com/mediatailor/latest/ug/cloudformation-benefits.html): Learn the benefits of using CloudFormation to deploy MediaTailor with CloudFront integration, including automated resource provisioning and consistent infrastructure as code.
- [Prepare for deployment](https://docs.aws.amazon.com/mediatailor/latest/ug/prepare-cloudformation-deployment.html): Learn how to prepare for deploying MediaTailor with CloudFront using CloudFormation, including prerequisites, account setup, and gathering required information.
- [Deploy the template](https://docs.aws.amazon.com/mediatailor/latest/ug/deploy-cloudformation-template.html): Step-by-step instructions for deploying the CloudFormation template that sets up MediaTailor with CloudFront integration, including console navigation and parameter configuration.
- [Use the deployed resources](https://docs.aws.amazon.com/mediatailor/latest/ug/use-deployed-resources.html): Learn how to use resources deployed by the CloudFormation template, including accessing MediaTailor configuration, understanding CloudFront distribution settings, and integrating with your workflow.
- [Test and validate your deployment](https://docs.aws.amazon.com/mediatailor/latest/ug/test-validate-deployment.html): Methods for testing your CloudFormation deployment of MediaTailor with CloudFront, including verification of resource creation, configuration testing, and end-to-end playback validation.
- [Troubleshoot deployment issues](https://docs.aws.amazon.com/mediatailor/latest/ug/troubleshoot-deployment-issues.html): Solutions for common issues when deploying MediaTailor with CloudFront using CloudFormation, including stack creation failures, resource configuration problems, and service integration challenges.
- [Customize the template](https://docs.aws.amazon.com/mediatailor/latest/ug/customize-cloudformation-template.html): Guidelines for customizing the CloudFormation template for MediaTailor and CloudFront integration, including modifying resource configurations and extending for specific use cases.
- [Template reference](https://docs.aws.amazon.com/mediatailor/latest/ug/cloudformation-template-reference.html): Detailed reference for the CloudFormation template that deploys MediaTailor with CloudFront integration, including parameters, resources, outputs, and mappings defined in the template.
- [Production CloudFront configuration](https://docs.aws.amazon.com/mediatailor/latest/ug/cf-comprehensive-configuration.html): Get a complete, production-ready CloudFront distribution configuration for MediaTailor that you can implement immediately.
- [Get CDN integration support](https://docs.aws.amazon.com/mediatailor/latest/ug/cdn-get-help.html): Learn when to escalate MediaTailor CDN integration issues to AWS Support and what information to gather for faster resolution.


## [Security](https://docs.aws.amazon.com/mediatailor/latest/ug/security.html)

- [Data protection](https://docs.aws.amazon.com/mediatailor/latest/ug/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in MediaTailor.

### [Identity and Access Management](https://docs.aws.amazon.com/mediatailor/latest/ug/security-iam.html)

How to authenticate requests and manage access to your MediaTailor resources.

- [How AWS Elemental MediaTailor works with IAM](https://docs.aws.amazon.com/mediatailor/latest/ug/security_iam_service-with-iam.html): Before you use IAM to manage access to MediaTailor, learn what IAM features are available to use with MediaTailor.
- [Identity-based policy examples](https://docs.aws.amazon.com/mediatailor/latest/ug/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify MediaTailor resources.
- [Resource-based policy examples](https://docs.aws.amazon.com/mediatailor/latest/ug/security_iam_resource-based-policy-examples.html): Learn about resource-based policy examples for AWS Elemental MediaTailor, including anonymous access and cross-account access.
- [AWS managed policies](https://docs.aws.amazon.com/mediatailor/latest/ug/security-iam-awsmanpol.html): Learn about AWS managed policies for MediaTailor and recent changes to those policies.

### [Using service-linked roles](https://docs.aws.amazon.com/mediatailor/latest/ug/using-service-linked-roles.html)

How to use service-linked roles to give MediaTailor access to resources in your AWS account.

- [Service-linked role permissions](https://docs.aws.amazon.com/mediatailor/latest/ug/slr-permissions.html): MediaTailor uses the service-linked role named AWSServiceRoleForMediaTailor â MediaTailor uses this service-linked role to invoke CloudWatch to create and manage log groups, log streams, and log events.
- [Creating a service-linked role](https://docs.aws.amazon.com/mediatailor/latest/ug/create-slr.html): You don't need to manually create a service-linked role.
- [Editing a service-linked role](https://docs.aws.amazon.com/mediatailor/latest/ug/edit-slr.html): MediaTailor does not allow you to edit the AWSServiceRoleForMediaTailor service-linked role.
- [Deleting a service-linked role](https://docs.aws.amazon.com/mediatailor/latest/ug/delete-slr.html): If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role.
- [Troubleshooting identity and access](https://docs.aws.amazon.com/mediatailor/latest/ug/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with MediaTailor and IAM.
- [Compliance validation](https://docs.aws.amazon.com/mediatailor/latest/ug/servicename-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/mediatailor/latest/ug/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy.
- [Infrastructure security](https://docs.aws.amazon.com/mediatailor/latest/ug/infrastructure-security.html): Learn how AWS Elemental MediaTailor isolates service traffic.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/mediatailor/latest/ug/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
- [Logging and monitoring](https://docs.aws.amazon.com/mediatailor/latest/ug/security-log-monitor.html): Monitoring is an important part of maintaining the reliability, availability, and performance of AWS Elemental MediaTailor and your AWS solutions.


## [Monitoring and tagging](https://docs.aws.amazon.com/mediatailor/latest/ug/monitoring.html)

### [Viewing logs](https://docs.aws.amazon.com/mediatailor/latest/ug/monitoring-through-logs.html)

Learn how to view and analyze MediaTailor logs to monitor workflow activities, troubleshoot issues, and gain visibility into ad insertion processes.

- [ADS logs](https://docs.aws.amazon.com/mediatailor/latest/ug/ads-log-format.html): Understand the structure and event types of AdDecisionServerInteractions logs that MediaTailor emits during interactions with ad decision servers.
- [Manifest logs](https://docs.aws.amazon.com/mediatailor/latest/ug/log-types.html): Learn what types of logs and their events that MediaTailor emits.
- [Transcode logs](https://docs.aws.amazon.com/mediatailor/latest/ug/tm-log-format.html): Learn about TranscodeService logs that MediaTailor emits during ad creative transcoding and preparation for ad stitching.

### [Using vended logs](https://docs.aws.amazon.com/mediatailor/latest/ug/vended-logs.html)

Learn how to send session activity logs to Amazon Simple Storage Service (Amazon S3) and Amazon Data Firehose.

- [Migrating the logging strategy](https://docs.aws.amazon.com/mediatailor/latest/ug/vended-logs-migrate.html): Learn the suggested path for migrating from legacy MediaTailor logging to vended logs.

### [Writing logs to CloudWatch Logs](https://docs.aws.amazon.com/mediatailor/latest/ug/monitoring-cw-logs.html)

MediaTailor produces logs that contain detailed information about session activity and ad decision server interactions, and writes them to Amazon CloudWatch.

- [Permissions for CloudWatch Logs](https://docs.aws.amazon.com/mediatailor/latest/ug/monitoring-permissions.html): Use AWS Identity and Access Management (IAM) to create a role that gives AWS Elemental MediaTailor access to Amazon CloudWatch.

### [Channel Assembly "As Run" log](https://docs.aws.amazon.com/mediatailor/latest/ug/as-run-log.html)

Learn how to enable the As Run log to troubleshoot playback issues in channel assembly.

- [Enabling](https://docs.aws.amazon.com/mediatailor/latest/ug/enabling-as-run-log.html): To enable the As Run log, specify the channel name and enable the As Run log type for that channel.
- [Disabling](https://docs.aws.amazon.com/mediatailor/latest/ug/disabling-as-run-log.html): To disable the As Run log for a channel that has it enabled, specify the channel name and disable the As Run log type for that channel.

### [CloudWatch Logs Insights](https://docs.aws.amazon.com/mediatailor/latest/ug/monitor-cloudwatch-ads-logs.html)

You can view and query AWS Elemental MediaTailor ad decision server (ADS) logs using Amazon CloudWatch Logs Insights.

- [Querying the ADS logs](https://docs.aws.amazon.com/mediatailor/latest/ug/querying-the-ads-logs.html): Querying the ADS Logs
- [Controlling the volume of ad insertion session logs](https://docs.aws.amazon.com/mediatailor/latest/ug/log-configuration.html): Configure the percentage of ad insertion session logs that MediaTailor sends to CloudWatch Logs to manage log costs and volume.
- [Filtering logs and events](https://docs.aws.amazon.com/mediatailor/latest/ug/logs-filter.html): Configure log filtering to control which log events MediaTailor emits for sessions and playback configurations, reducing log volume and focusing on relevant events.
- [Generating debug logs](https://docs.aws.amazon.com/mediatailor/latest/ug/debug-log-mode.html): Describes how to set the log mode to debug, and read the logs to troubleshoot playback session issues.

### [Monitoring with CloudWatch metrics](https://docs.aws.amazon.com/mediatailor/latest/ug/monitoring-cloudwatch-metrics.html)

You can monitor AWS Elemental MediaTailor metrics using CloudWatch.

- [Using metrics to diagnose stale manifests](https://docs.aws.amazon.com/mediatailor/latest/ug/stale-manifest-diagnose.html): Learn about metrics that can help you to diagnose the cause of stale manifests.
- [Recording API calls](https://docs.aws.amazon.com/mediatailor/latest/ug/logging-using-cloudtrail.html): Learn about logging AWS Elemental MediaTailor with AWS CloudTrail.
- [Receiving Channel Assembly alerts](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-alerts.html): MediaTailor creates alerts for issues or potential issues that occur with your channel assembly resources.
- [Tagging resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html): Create, view, edit, and delete tags on resources in AWS Elemental MediaTailor.

### [Workflow monitor](https://docs.aws.amazon.com/mediatailor/latest/ug/monitor-with-workflow-monitor.html)

Analyze AWS media services and create signal maps between those services.

### [Configuring workflow monitor](https://docs.aws.amazon.com/mediatailor/latest/ug/monitor-with-workflow-monitor-configure.html)

To setup workflow monitor for the first time; you create the alarm and event templates, and discover signal maps that are used to monitor your media workflows.

### [Getting started](https://docs.aws.amazon.com/mediatailor/latest/ug/monitor-with-workflow-monitor-configure-getting-started.html)

The following steps provide a basic overview of using workflow monitor for the first time.

- [Workflow monitor IAM policies](https://docs.aws.amazon.com/mediatailor/latest/ug/monitor-with-workflow-monitor-configure-getting-started-IAM.html): Workflow monitor interacts with multiple AWS services to create signal maps, build CloudWatch and EventBridge resources, and CloudFormation templates.

### [Templates](https://docs.aws.amazon.com/mediatailor/latest/ug/monitor-with-workflow-monitor-configure-templates.html)

Learn how to configure the alarm and event templates that will be used to monitor your workflow.

### [CloudWatch alarms](https://docs.aws.amazon.com/mediatailor/latest/ug/monitor-with-workflow-monitor-configure-alarms.html)

Learn how to configure the alarm groups and templates that will be used to monitor your workflow.

- [Recommended templates](https://docs.aws.amazon.com/mediatailor/latest/ug/monitor-with-workflow-monitor-configure-alarms-recommended-templates.html): Learn how to use the recommended alarm templates created by AWS.
- [EventBridge rules](https://docs.aws.amazon.com/mediatailor/latest/ug/monitor-with-workflow-monitor-configure-notifications.html): Learn how to configure the EventBridge groups and templates that will be used to monitor your workflow.

### [Signal maps](https://docs.aws.amazon.com/mediatailor/latest/ug/monitor-with-workflow-monitor-configure-signal-maps.html)

Learn how to configure the workflow monitor signal maps.

- [Creating signal maps](https://docs.aws.amazon.com/mediatailor/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-create.html): Learn how to create the workflow monitor signal maps using the automatic discovery process.
- [Viewing signal maps](https://docs.aws.amazon.com/mediatailor/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-view.html): Workflow monitor signal maps allow you to see a visual mapping of all connected AWS resources in your media workflow.
- [Attaching templates](https://docs.aws.amazon.com/mediatailor/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-attach.html): After you have created alarm and event templates, you need to attach these to a signal map.
- [Deploying monitoring templates](https://docs.aws.amazon.com/mediatailor/latest/ug/monitor-with-workflow-monitor-configure-deploy.html): After you have attached the alarm and event templates to your signal map, you must deploy the monitoring.
- [Updating signal maps](https://docs.aws.amazon.com/mediatailor/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-update.html): If a change is made to your workflow, you might need to rediscover the signal map and redeploy monitoring resources.
- [Deleting signal maps](https://docs.aws.amazon.com/mediatailor/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-delete.html): If you not longer need a signal map, it can be deleted.
- [Quotas](https://docs.aws.amazon.com/mediatailor/latest/ug/monitor-with-workflow-monitor-configure-quotas.html): The following section contains quotas for workflow monitor resources.

### [Using workflow monitor](https://docs.aws.amazon.com/mediatailor/latest/ug/monitor-with-workflow-monitor-operate.html)

Use the overview and signal maps sections of the workflow monitor console to review the current status of the workflows and any associated alarms, metrics, and logs.

- [Overview](https://docs.aws.amazon.com/mediatailor/latest/ug/monitor-with-workflow-monitor-operate-overview.html): The Overview section of the workflow monitor console is a dashboard that provides at-a-glance information about your signal maps.
- [Logs and metrics](https://docs.aws.amazon.com/mediatailor/latest/ug/monitor-with-workflow-monitor-operate-logs-metrics.html): To view CloudWatch metrics and logs for a signal map, select the radio button next to the name of the signal map.
- [Using signal maps](https://docs.aws.amazon.com/mediatailor/latest/ug/monitor-with-workflow-monitor-operate-signal-maps.html): From the overview section of the console, you can select a specific signal map to view more information about that signal map and its attached monitoring resources.


## [Troubleshooting](https://docs.aws.amazon.com/mediatailor/latest/ug/troubleshooting.html)

- [Event flow troubleshooting](https://docs.aws.amazon.com/mediatailor/latest/ug/troubleshooting-event-flow.html): Use MediaTailor event flow knowledge to diagnose and resolve ad insertion issues through systematic analysis of event sequences, timing, and patterns.
- [Playback troubleshooting](https://docs.aws.amazon.com/mediatailor/latest/ug/playback-errors.html): Describes AWS Elemental MediaTailor codes for errors that are returned during playback.

### [Ad skipping troubleshooting](https://docs.aws.amazon.com/mediatailor/latest/ug/troubleshooting-ad-skipping-overview.html)

Comprehensive guide to troubleshooting ad skipping issues in AWS Elemental MediaTailor, including common causes, resolution steps, and monitoring best practices.

- [NEW_CREATIVE skipping](https://docs.aws.amazon.com/mediatailor/latest/ug/troubleshooting-new-creative-skipping.html): Step-by-step guide to resolve AWS Elemental MediaTailor ad skipping caused by NEW_CREATIVE skip reasons, including transcoding issues and creative ID conflicts.
- [ADS timeout skipping](https://docs.aws.amazon.com/mediatailor/latest/ug/troubleshooting-ads-timeout-skipping.html): Comprehensive guide to resolve AWS Elemental MediaTailor ad skipping caused by ad decision server connectivity issues, timeouts, and performance problems.
- [VAST parsing skipping](https://docs.aws.amazon.com/mediatailor/latest/ug/troubleshooting-vast-parsing-skipping.html): Complete troubleshooting guide for AWS Elemental MediaTailor ad skipping caused by VAST response errors, media file issues, and wrapper problems.
- [Duration mismatch skipping](https://docs.aws.amazon.com/mediatailor/latest/ug/troubleshooting-duration-mismatch-skipping.html): Troubleshooting guide for AWS Elemental MediaTailor ad skipping caused by duration mismatches, format issues, and EXT-X-CUE-OUT tag problems.
- [Session variable skipping](https://docs.aws.amazon.com/mediatailor/latest/ug/troubleshooting-session-variables-skipping.html): Complete troubleshooting guide for AWS Elemental MediaTailor ad skipping caused by session variable configuration issues, SCTE-35 UPID parsing problems, and variable resolution failures.
- [Monitoring ad skipping](https://docs.aws.amazon.com/mediatailor/latest/ug/monitoring-ad-skipping-issues.html): Comprehensive guide to monitoring AWS Elemental MediaTailor ad skipping issues with CloudWatch metrics, alarms, and advanced log analysis queries.
- [Prevention best practices](https://docs.aws.amazon.com/mediatailor/latest/ug/preventing-ad-skipping-best-practices.html): Proactive measures and implementation guidelines to minimize AWS Elemental MediaTailor ad skipping issues and ensure optimal ad insertion performance.
- [Reference materials](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-skipping-reference-materials.html): Complete reference guide for AWS Elemental MediaTailor ad skip reasons, error codes, and related troubleshooting resources.
