# Source: https://learn.microsoft.com/en-us/azure/media-services/latest/stream-live-streaming-concept

Title: Overview of Live streaming

URL Source: https://learn.microsoft.com/en-us/azure/media-services/latest/stream-live-streaming-concept

Markdown Content:
![Image 1: Media Services logo v3](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/media/media-services-api-logo/azure-media-services-logo-v3.svg)

* * *

Warning

Azure Media Services will be retired June 30th, 2024. For more information, see the [AMS Retirement Guide](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/azure-media-services-retirement).

Azure Media Services enables you to deliver live events to your customers on the Azure cloud. To stream your live events with Media Services, you'll need to set up a live video encoder that converts signals from a camera (or another device, like a laptop) into a contribution feed that is sent to Media Services. The contribution feed can include signals related to advertising, such as SCTE-35 markers. For a list of recommended live streaming encoders, see [live streaming encoders](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/encode-recommended-on-premises-live-encoders).

If you haven't used an on-premises encoder before, try the [Create an Azure Media Services live stream with OBS](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/live-event-obs-quickstart) quickstart.

With Media Services, you can take advantage of [dynamic packaging](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/encode-dynamic-packaging-concept), which allows you to preview and broadcast your live streams in [MPEG DASH, HLS, and Smooth Streaming formats](https://en.wikipedia.org/wiki/Adaptive_bitrate_streaming) from the contribution feed. Your viewers can play back the live stream with any HLS, DASH, or Smooth Streaming compatible players. See the [list of tested players](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/player-media-players-concept) and try the [Media Services 3rd-party player samples](https://github.com/Azure-Samples/media-services-3rdparty-player-samples).

[Live events](https://learn.microsoft.com/en-us/rest/api/media/liveevents) are ingest and process live video feeds. A live event can be set to either:

* _pass-through_ when an on-premises live encoder sends a multiple bitrate stream, or
* _live encoding_ when an on-premises live encoder sends a single bitrate stream. For details about live outputs, see [Live events and live outputs](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/live-event-concept).

When using the pass-through **Live Event** (basic or standard), you rely on your on-premises live encoder to generate a multiple bitrate video stream and send that as the contribution feed to the Live Event (using RTMP or fragmented-MP4 input protocol). The Live Event then passes the incoming video stream to the dynamic packager (Streaming Endpoint) without any further processing. A pass-through Live Event is optimized for long-running live events or 24x365 linear live streaming.

![Image 2: pass through streaming](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/media/diagrams/pass-through.svg)

To use live encoding, configure your on-premises live encoder to send a single bitrate video (up to 32Mbps aggregate) to the Live Event (using RTMP or fragmented-MP4 input protocol). The Live Event transcodes the incoming single bitrate stream into multiple bitrate video streams at varying resolutions. This improves delivery for playback devices with industry standard protocols like MPEG-DASH, Apple HTTP Live Streaming (HLS), and Microsoft Smooth Streaming.

![Image 3: live encoding streaming](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/media/diagrams/live-encoding.svg)

Dynamic encryption enables you to dynamically encrypt your live or on-demand content with AES-128 or any of the three major digital rights management (DRM) systems: Microsoft PlayReady, Google Widevine, and Apple FairPlay. Media Services also provides a service for delivering AES keys and DRM (PlayReady, Widevine, and FairPlay) licenses to authorized clients. For more information, see [dynamic encryption](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/drm-content-protection-concept).

Widevine is a service provided by Google Inc. and subject to the terms of service and Privacy Policy of Google, Inc.

Dynamic filtering is used to control the number of tracks, formats, bitrates, and presentation time windows that are sent out to the players. For more information, see [filters and dynamic manifests](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/filters-dynamic-manifest-concept).

Live transcription is a feature you can use with live events that are either pass-through or live encoding. For more information, see [live transcription](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/live-event-live-transcription-how-to). When this feature is enabled, the service uses the [Speech-To-Text](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-to-text) feature of Cognitive Services to transcribe the spoken words in the incoming audio into text. This text is then made available for delivery along with video and audio in MPEG-DASH and HLS protocols.

Important

You _should_ use GOP sizes of 2 seconds for live events. You **must** use GOP sizes of 4 seconds or below for passthrough live events with live transcriptions in order to get correct transcription data. If you choose to use higher GOP size, the transcription data might have defects, e.g. missing content.

The dynamic encryption and DRM features of Azure Media Services has limits to consider when attempting to secure content delivery that includes live transcriptions, captions, subtitles, or timed-metadata. The DRM subsystems, including PlayReady, FairPlay, and Widevine do not support the encryption and licensing of text tracks. The lack of DRM encryption for text tracks limits your ability to secure the contents of live transcriptions, manual inserted captions, uploaded subtitles, or timed-metadata signals that may be inserted as separate tracks.

To secure your captions, subtitles, or timed-metadata tracks, follow these guidelines:

1. Use AES-128 Clear Key encryption. When enabling AES-128 clear key encryption, the text tracks can be configured to be encrypted using a full "envelope" encryption technique that follows the same encryption pattern as the audio and video segments. These segments can then be decrypted by a client application after requesting the decryption key from the Media Services Key Delivery service using an authenticated JWT token. This method is supported by the Azure Media Player, but may not be supported on all devices and can require some client-side development work to make sure it succeeds on all platforms.
2. Use CDN token authentication to protect the text (subtitle, captions, metadata) tracks being delivered with short form tokenized URLs that are restricted to geo, IP, or other configurable settings in the CDN portal. Enable the CDN security features using Verizon Premium CDN or other 3rd-party CDN configured to connect to your Media Services streaming endpoints.

Warning

If you do not follow one of the guidelines above, your subtitles, captions, or timed-metadata text will be accessible as un-encrypted content that could be intercepted or shared outside of your intended client delivery path. This can result in leaked information. If you are concerned about the contents of the captions or subtitles being leaked in a secure delivery scenario, reach out to the Media Services support team for more information on the above guidelines for securing your content delivery.

To understand the live streaming workflow in Media Services v3, you have to first review and understand the following concepts:

* [Streaming endpoints](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/stream-streaming-endpoint-concept)
* [Live events and live outputs](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/live-event-concept)
* [Streaming locators](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/stream-streaming-locators-concept)

1. In your Media Services account, make sure the **streaming endpoint** (origin) is running.

2. Create a [live event](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/live-event-concept).

When creating the event, you can specify to autostart it. Alternatively, you can start the event when you are ready to start streaming.

 When autostart is set to true, the Live Event will be started right after creation. The billing starts as soon as the Live Event starts running. You must explicitly call Stop on the live event resource to halt further billing. For more information, see [live event states and billing](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/live-event-states-billing-concept).

1. Get the ingest URL(s) and configure your on-premises encoder to use the URL to send the contribution feed.

See [recommended live encoders](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/encode-recommended-on-premises-live-encoders).

1. Get the preview URL and use it to verify that the input from the encoder is actually being received.

2. Create a new **asset** object.

Each live output is associated with an asset, which it uses to record the video into the associated Azure blob storage container.

1. Create a **live output** and use the asset name that you created so that the stream can be archived into the asset.

Live Outputs start on creation and stop when deleted. When you delete the Live Output, you are not deleting the underlying asset and content in the asset.

1. Create a **streaming locator** with the [built-in streaming policy types](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/stream-streaming-policy-concept).

To publish the live output, you must create a streaming locator for the associated asset.

1. List the paths on the **streaming locator** to get back the URLs to use (these are deterministic).

2. Get the hostname for the **streaming endpoint** (Origin) you wish to stream from.

3. Combine the URL from step 8 with the hostname in step 9 to get the full URL.

4. If you wish to stop making your **live event** viewable, you need to stop streaming the event and delete the **streaming locator**.

5. If you are done streaming events and want to clean up the resources provisioned earlier, follow the following procedure.

    *   Stop pushing the stream from the encoder.
    *   Stop the live event. Once the live event is stopped, it will not incur any charges. When you need to start it again, it will have the same ingest URL so you won't need to reconfigure your encoder.
    *   You can stop your streaming endpoint, unless you want to continue to provide the archive of your live event as an on-demand stream. If the live event is in stopped state, it will not incur any charges. However, if the streaming endpoint is still running, it will incur charges.

The asset that the live output is archiving to, automatically becomes an on-demand asset when the live output is deleted. You must delete all live outputs before a live event can be stopped. You can use an optional flag [removeOutputsOnStop](https://learn.microsoft.com/en-us/rest/api/media/liveevents/stop#request-body) to automatically remove live outputs on stop.

* [Recommended live encoders](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/encode-recommended-on-premises-live-encoders)
* [Using a cloud DVR](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/live-event-cloud-dvr-time-how-to)
* [Live event types feature comparison](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/live-event-types-comparison-reference)
* [States and billing](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/live-event-states-billing-concept)
* [Latency](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/live-event-latency-reference)
* [Quotas and limits](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/limits-quotas-constraints-reference)

See the [live streaming questions in the FAQ](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/frequently-asked-questions).

You can contact Media Services with questions or follow our updates by one of the following methods:

* [Q & A](https://learn.microsoft.com/en-us/answers/topics/azure-media-services.html)
* [Stack Overflow](https://stackoverflow.com/questions/tagged/azure-media-services). Tag questions with `azure-media-services`.
* [@MSFTAzureMedia](https://twitter.com/MSFTAzureMedia) or use [@AzureSupport](https://twitter.com/azuresupport) to request support.
* Open a support ticket through the Azure portal.
