# Source: https://learn.microsoft.com/en-us/azure/media-services/latest/stream-live-tutorial-with-api

Title: Stream live with Media Services by using .NET 7.0

URL Source: https://learn.microsoft.com/en-us/azure/media-services/latest/stream-live-tutorial-with-api

Markdown Content:
![Image 1: Media Services logo v3](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/media/media-services-api-logo/azure-media-services-logo-v3.svg)

* * *

Warning

Azure Media Services will be retired June 30th, 2024. For more information, see the [AMS Retirement Guide](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/azure-media-services-retirement).

In Azure Media Services, [live events](https://learn.microsoft.com/en-us/rest/api/media/liveevents) are responsible for processing live streaming content. A live event provides an input endpoint (ingest URL) that you then provide to a live encoder. The live event receives input streams from the live encoder using the RTMP/S or Smooth Streaming protocols and makes them available for streaming through one or more [streaming endpoints](https://learn.microsoft.com/en-us/rest/api/media/streamingendpoints). Live events also provide a preview endpoint (preview URL) that you use to preview and validate your stream before further processing and delivery.

This tutorial shows how to use .NET 7.0 to create a _pass-through_ live event. Pass-through live events are useful when you have an encoder that is capable of multi-bitrate, GOP aligned encoding on premises. It can a way to reduce cloud costs. If you wish to reduce bandwidth and send a single bitrate stream to the cloud for multi-bitrate encoding, you can use a transcoding live event with the 720P or 1080P encoding presets.

In this tutorial, you will:

* Download a sample project.
* Examine the code that performs live streaming.
* Watch the event with Azure Media Player on the [Media Player demo site](https://ampdemo.azureedge.net/).
* Set up Event Grid to monitor the live event.
* Clean up resources.

You need the following items to complete the tutorial:

* Install [Visual Studio Code for Windows/macOS/Linux](https://code.visualstudio.com/) or [Visual Studio 2022 for Windows or Mac](https://visualstudio.microsoft.com/).
* Install [.NET 7.0 SDK](https://dotnet.microsoft.com/download)
* [Create a Media Services account](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/account-create-how-to). Be sure to copy the **API Access** details for the account name, subscription ID, and resource group name in JSON format or store the values needed to connect to the Media Services account in the JSON file format used in this `appsettings.json` file.
* Follow the steps in [Access the Azure Media Services API with the Azure CLI](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/access-api-howto) and save the details. You'll need to use the account name, subscription Id, and resource group name in this sample, and enter them into the `appsettings.json` file.

You also need these items for live-streaming software:

* A camera or a device (like a laptop) that's used to broadcast an event.
* An on-premises software encoder that encodes your camera stream and sends it to the Media Services live-streaming service through the Real-Time Messaging Protocol (RTMP/S). For more information, see [Recommended on-premises live encoders](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/encode-recommended-on-premises-live-encoders). The stream has to be in RTMP/S or Smooth Streaming format. This sample assumes that you'll use Open Broadcaster Software (OBS) Studio to broadcast RTMP/S to the ingest endpoint. [Install OBS Studio](https://obsproject.com/download).
* Alternatively, you can try the [OBS Quickstart](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/live-event-obs-quickstart) to test the entire process with the Azure portal first.

For monitoring the live event using Event Grid and Event Hubs, you can: 1. Follow the steps in [Create and monitor Media Services events with Event Grid using the Azure portal](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/monitor-events-portal-how-to) or, 1. Follow the steps near the end of this tutorial in the [Monitoring Live Events using Event Grid and Event Hubs](https://learn.microsoft.com/en-us/azure/media-services/latest/stream-live-tutorial-with-api#monitoring-live-events-using-event-grid-and-event-hubs) section of this article.

Clone the GitHub repository that contains the live-streaming .NET sample to your machine by using the following command:

```
git clone https://github.com/Azure-Samples/media-services-v3-dotnet.git
```

The live-streaming sample is in the [Live/LiveEventWithDVR](https://github.com/Azure-Samples/media-services-v3-dotnet/tree/main/Live/LiveEventWithDVR) folder.

Open `appsettings.json` in your downloaded project. Replace the values with account name, subscription Id and the resource group name.

Important

This sample uses a unique suffix for each resource. If you cancel the debugging or terminate the app without running it through, you'll end up with multiple live events in your account. Be sure to stop the running live events. Otherwise, _you'll be billed_!

Program.cs creates a reference to the Media Services account resource, using the options from `appsettings.json`:

```
var mediaServicesResourceId = MediaServicesAccountResource.CreateResourceIdentifier(
    subscriptionId: options.AZURE_SUBSCRIPTION_ID.ToString(),
    resourceGroupName: options.AZURE_RESOURCE_GROUP,
    accountName: options.AZURE_MEDIA_SERVICES_ACCOUNT_NAME);
var credential = new DefaultAzureCredential(includeInteractiveCredentials: true);
var armClient = new ArmClient(credential);
var mediaServicesAccount = armClient.GetMediaServicesAccountResource(mediaServicesResourceId);
```

This section shows how to create a _pass-through_ type of live event (LiveEventEncodingType set to None). For information about the available types, see [Live event types](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/live-event-concept). If you want to reduce your overall ingest bandwidth, or you don't have an on-premises multi-bitrate transcoder, you can use a live transcoding event for 720p or 1080p adaptive bitrate cloud encoding.

You might want to specify the following things when you're creating the live event:

* **The ingest protocol for the live event**. Currently, the RTMPS, and Smooth Streaming protocols are supported. You can't change the protocol option while the live event is running. If you need different protocols, create a separate live event for each streaming protocol.

* **IP restrictions on the ingest and preview**. You can define the IP addresses that are allowed to ingest a video to this live event. Allowed IP addresses can be specified as one of these choices:

  * A single IP address (for example, 10.0.0.1 or 2001:db8::1)

  * An IP range that uses an IP address and a Classless Inter-Domain Routing (CIDR) subnet mask (for example, 10.0.0.1/22 or 2001:db8::/48)

  * An IP range that uses an IP address and a dotted decimal subnet mask (for example, 10.0.0.1 255.255.252.0)

If no IP addresses are specified and there's no rule definition, then no IP address will be allowed. To allow any IP address, create a rule and set 0.0.0.0/0 and ::/0. The IP addresses have to be in one of the following formats: IPv4 or IPv6 addresses with four numbers or a CIDR address range. For more information, see [Restrict access to DRM license and AES key delivery using IP allowlists](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/drm-content-protection-key-delivery-ip-allow).

* **Autostart on an event as you create it**. When autostart is set to true, the live event will start after creation. That means the billing starts as soon as the live event starts running. You must explicitly call `Stop` on the live event resource to halt further billing. For more information, see [Live event states and billing](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/live-event-states-billing-concept).

Standby modes are available to start the live event in a lower-cost "allocated" state that makes it faster to move to a running state. It's useful for situations like hot pools that need to hand out channels quickly to streamers.

* **A static host name and a unique GUID**. For an ingest URL to be predictive and easier to maintain in a hardware-based live encoder, set the `useStaticHostname` property to true. For detailed information, see [Live event ingest URLs](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/live-event-concept).

```
var liveEvent = await mediaServicesAccount.GetMediaLiveEvents().CreateOrUpdateAsync(
    WaitUntil.Completed,
    liveEventName,
    new MediaLiveEventData(mediaServicesAccount.Get().Value.Data.Location)
    {
        Description = "Sample Live Event from the .NET SDK sample",
        UseStaticHostname = true,
        // 1) Set up the input settings for the Live event...
        Input = new LiveEventInput(streamingProtocol: LiveEventInputProtocol.Rtmp)
        {
            StreamingProtocol = LiveEventInputProtocol.Rtmp,
            AccessToken = "acf7b6ef-8a37-425f-b8fc-51c2d6a5a86a", // used to make the ingest URL unique
            KeyFrameIntervalDuration = TimeSpan.FromSeconds(2),
            IPAllowedIPs =
            {
                new IPRange
                {
                    Name = "AllowAllIpV4Addresses",
                    Address = IPAddress.Parse("0.0.0.0"),
                    SubnetPrefixLength = 0
                },
                new IPRange
                {
                    Name = "AllowAllIpV6Addresses",
                    Address = IPAddress.Parse("0::"),
                    SubnetPrefixLength = 0
                }
            }
        },
        // 2) Set the live event to use pass-through or cloud encoding modes...
        Encoding = new LiveEventEncoding()
        {
            EncodingType = LiveEventEncodingType.PassthroughBasic
        },
        // 3) Set up the Preview endpoint for monitoring
        Preview = new LiveEventPreview
        {
            IPAllowedIPs =
            {
                new IPRange()
                {
                    Name = "AllowAllIpV4Addresses",
                    Address = IPAddress.Parse("0.0.0.0"),
                    SubnetPrefixLength = 0
                },
                new IPRange()
                {
                    Name = "AllowAllIpV6Addresses",
                    Address = IPAddress.Parse("0::"),
                    SubnetPrefixLength = 0
                }
            }
        },
        // 4) Set up more advanced options on the live event. Low Latency is the most common one. Set
        //    this to Default or Low Latency. When using Low Latency mode, you must configure the Azure
        //    Media Player to use the quick start heuristic profile or you won't notice the change. In
        //    the AMP player client side JS options, set -  heuristicProfile: "Low Latency Heuristic
        //    Profile". To use low latency optimally, you should tune your encoder settings down to 1
        //    second GOP size instead of 2 seconds.
        StreamOptions =
        {
            StreamOptionsFlag.LowLatency
        },
        // 5) Optionally enable live transcriptions if desired. This is only supported on
        //    PassthroughStandard, and the transcoding live event types. It is not supported on Basic
        //    pass-through type.
        // WARNING: This is extra cost, so please check pricing before enabling.
        //Transcriptions =
        //{
        //    new LiveEventTranscription
        //    {
        //        // The value should be in BCP-47 format (e.g: 'en-US'). See https://go.microsoft.com/fwlink/?linkid=2133742
        //        Language = "en-us",
        //        TrackName = "English" // set the name you want to appear in the output manifest
        //    }
        //}
    },
    autoStart: false);
```

After the Live Event is created, you can get ingest URLs that you'll provide to the live encoder. The encoder uses these URLs to input a live stream.

```
// Get the RTMP ingest URL. The endpoints is a collection of RTMP primary and secondary,
// and RTMPS primary and secondary URLs.
Console.WriteLine($"The RTMP ingest URL to enter into OBS Studio is:");
Console.WriteLine(liveEvent.Data.Input.Endpoints.First(x => x.Uri.Scheme == "rtmps").Uri);
Console.WriteLine("Make sure to enter a Stream Key into the OBS Studio settings. It can be");
Console.WriteLine("any value or you can repeat the accessToken used in the ingest URL path.");
Console.WriteLine();
```

Use `previewEndpoint` to preview and verify that the input from the encoder is being received.

Important

Make sure that the video is flowing to the preview URL before you continue.

```
// Use the previewEndpoint to preview and verify that the input from the encoder is actually
// being received The preview endpoint URL also support the addition of various format strings
// for HLS (format=m3u8-cmaf) and DASH (format=mpd-time-cmaf) for example. The default manifest
// is Smooth.
string previewEndpoint = liveEvent.Data.Preview.Endpoints.First().Uri.ToString();
Console.WriteLine($"The preview URL is:");
Console.WriteLine(previewEndpoint);
Console.WriteLine();
Console.WriteLine($"Open the live preview in your browser and use the Azure Media Player to monitor the preview playback:");
Console.WriteLine($"https://ampdemo.azureedge.net/?url={HttpUtility.UrlEncode(previewEndpoint)}&heuristicprofile=lowlatency");
Console.WriteLine();
Console.WriteLine("Start the live stream now, sending the input to the ingest URL and verify");
Console.WriteLine("that it is arriving with the preview URL.");
Console.WriteLine("IMPORTANT: Make sure that the video is flowing to the Preview URL before continuing!");
Console.WriteLine("Press enter to continue...");
Console.ReadLine();
```

After the live stream from the on-premises encoder is streaming to the live event, you can begin the live event by creating an asset, live output, and streaming locator. The stream is archived and is available to viewers through the streaming endpoint.

The next section will walk through the creation of the asset and the live output.

Create an asset for the live output to use.

```
// Create an Asset for the Live Output to use. Think of this as the "tape" that will be recorded
// to. The asset entity points to a folder/container in your Azure Storage account
Console.Write($"Creating the output Asset '{assetName}'...".PadRight(60));
var asset = (await mediaServicesAccount.GetMediaAssets().CreateOrUpdateAsync(
    WaitUntil.Completed,
    assetName,
    new MediaAssetData
    {
        Description = "My video description"
    })).Value;
Console.WriteLine("Done");
```

Live outputs start when they're created and stop when they're deleted. When you delete the live output, you're not deleting the output asset or content in the asset. The asset with the recording is available for on-demand streaming as long as it exists and there's a streaming locator associated with it.

```
// Create the Live Output - think of this as the "tape recorder for the live event". Live
// outputs are optional, but are required if you want to archive the event to storage, use the
// asset for on-demand playback later, or if you want to enable cloud DVR time-shifting. We will
// use the asset created above for the "tape" to record to.
Console.Write($"Creating Live Output...".PadRight(60));
var liveOutput = (await liveEvent.GetMediaLiveOutputs().CreateOrUpdateAsync(
    WaitUntil.Completed,
    liveOutputName,
    new MediaLiveOutputData
    {
        AssetName = asset.Data.Name,
        // The HLS and DASH manifest file name. This is recommended to
        // set if you want a deterministic manifest path up front.
        // archive window can be set from 3 minutes to 25 hours.
        // Content that falls outside of ArchiveWindowLength is
        // continuously discarded from storage and is non-recoverable.
        // For a full event archive, set to the maximum, 25 hours.
        ManifestName = manifestName,
        ArchiveWindowLength = TimeSpan.FromHours(1)
    })).Value;
Console.WriteLine("Done");
```

Note

When your Media Services account is created, a default streaming endpoint is added to your account in the stopped state. To start streaming your content and take advantage of [dynamic packaging](https://learn.microsoft.com/en-us/previous-versions/azure/media-services/latest/encode-dynamic-packaging-concept) and dynamic encryption, the streaming endpoint from which you want to stream content has to be in the running state.

You publish an asset by creating a streaming locator. The live event (up to the DVR window length) is viewable until the streaming locator's expiration or deletion, whichever comes first. It's how you make the video available for your viewing audience to see live and on demand. The same URL can be used to watch the live event, the DVR window, or the on-demand asset when the live event is finished and the live output is deleted.

```
var streamingLocator = (await mediaServicesAccount.GetStreamingLocators().CreateOrUpdateAsync(
    WaitUntil.Completed,
    streamingLocatorName,
    new StreamingLocatorData
    {
        AssetName = asset.Data.Name,
        StreamingPolicyName = "Predefined_ClearStreamingOnly",
        Filters =
        {
            filter.Data.Name
        }
    })).Value;
```

Run the code. Use the output streaming URLs to watch your live event. Copy the streaming locator URL. You can use a media player of your choice. You can use the [Media Player demo site](https://ampdemo.azureedge.net/) to test your stream. Enter the URL into the URL field and select **Update player**.

The sample project can use Event Grid and Event Hubs to monitor the Live Event. You can set up and use Event Grid using the following

To enable monitoring:

1. Use the Azure portal to create Event Hubs Namespace and an Event Hubs
    1.   Search for “Event Hubs” using the text box at the top of the Azure portal.
    2.   Select **Event Hub** from the list, then follow the instructions to create an Event Hubs Namespace.
    3.   Navigate to the Event Hubs Namespace resource.
    4.   Select **Event Hubs** from the **Entities** section of the portal menu.
    5.   Create an Event Hubs in the Event Hubs namespace.
    6.   Navigate to the Event Hubs resource.
    7.   Select **Access control** then **Add**, then **Add role assignment**.
    8.   Select the **Azure Event Hubs Data Receiver** then grant the access to yourself.
    9.   Select **Access control** then **Add**, then **Add role assignment**.
    10.   Select the **Azure Event Hubs Data Sender** then grant it to the Managed Identity created for the Media Services account.

2. Use the Azure portal to create an Azure Storage account.
    1.   After creating the storage account, navigate to the Storage Account resource.
    2.   Select **Access control** then **Add**, then **Add role assignment**.
    3.   Select the **Storage Blob Data Contributor** then grant this access to yourself.

3. Create an Event Subscription
    1.   Navigate to the Media Services account.
    2.   Select **Events** from the portal menu.
    3.   Select **+ Event Subscription**.
    4.   Enter a subscription name and a system article name.
    5.   Set the **Endpoint Type** to `Event Hub`.
    6.   Set the Event Hubs to the previously created Event Hubs and set the Managed Identity to the identity that was previously granted Sender access to the Event Hubs

4. Update the `appsetttings.json` file.
    1.   Set EVENT_HUB_NAMESPACE to the full name of the namespace. It should be similar to `myeventhub.servicebus.windows.net`.
    2.   Set EVENT_HUB_NAME.
    3.   Set AZURE_STORAGE_ACCOUNT_NAME.

Run the sample again. With Event Hubs integration enabled, the sample logs events when the encoder connects and disconnects from the Live Event. Various other events are also logged.

After running the sample, delete the Event Hubs and storage account if they're no longer needed.

If you're done streaming events and want to clean up the resources provisioned earlier, use the following procedure:

1. Stop streaming from the encoder.
2. Stop the live event. After the live event is stopped, it won't incur any charges. When you need to start it again, the same ingest URL can be used so you won't need to reconfigure your encoder.
3. Stop the streaming endpoint, unless you want to continue to provide the archive of your live event as an on-demand stream. If the live event is in a stopped state, it won't incur any charges.

```
if (liveOutput != null)
{
    Console.Write("Deleting the Live Output...".PadRight(60));
    await liveOutput.DeleteAsync(WaitUntil.Completed);
    Console.WriteLine("Done");
}

if (liveEvent?.Data.ResourceState == LiveEventResourceState.Running)
{
    Console.Write("Stopping the Live Event...".PadRight(60));
    await liveEvent.StopAsync(WaitUntil.Completed, new LiveEventActionContent() { RemoveOutputsOnStop = true });
    Console.WriteLine("Done");
}

if (liveEvent != null)
{
    Console.Write("Deleting the Live Event...".PadRight(60));
    await liveEvent.DeleteAsync(WaitUntil.Completed);
    Console.WriteLine("Done");
}

if (streamingLocator != null)
{
    Console.Write("Deleting the Streaming Locator...".PadRight(60));
    await streamingLocator.DeleteAsync(WaitUntil.Completed);
    Console.WriteLine("Done");
}

if (asset != null)
{
    Console.Write("Deleting the Asset...".PadRight(60));
    await asset.DeleteAsync(WaitUntil.Completed);
    Console.WriteLine("Done");
}
```

If you no longer need the Media Services and storage accounts that you created for this tutorial, delete the resource group that you created earlier.

Run the following CLI command:

```
az group delete --name amsResourceGroup
```

You can contact Media Services with questions or follow our updates by one of the following methods:

* [Q & A](https://learn.microsoft.com/en-us/answers/topics/azure-media-services.html)
* [Stack Overflow](https://stackoverflow.com/questions/tagged/azure-media-services). Tag questions with `azure-media-services`.
* [@MSFTAzureMedia](https://twitter.com/MSFTAzureMedia) or use [@AzureSupport](https://twitter.com/azuresupport) to request support.
* Open a support ticket through the Azure portal.
