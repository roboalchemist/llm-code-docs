# Source: https://documentation.onesignal.com/docs/en/adobe-audience-manager.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Adobe Audience Manager

> Learn how to integrate OneSignal with Adobe Audience Manager to sync audience segments and behavioral data, enabling targeted, multi-channel messaging campaigns that drive engagement, conversions, and revenue growth.

Integrating Adobe Audience Manager with OneSignal allows you to bring powerful audience segmentation from Adobe into OneSignal's customer engagement platform. This enables personalized, behavior-based messaging that increases user retention and monetization.

## Capabilities

OneSignal and Adobe Audience Manager integration supports:

* **Real-time segment sync**: Automatically import segments from Adobe Audience Manager into OneSignal.
* **Cross-channel targeting**: Use imported segments to send push notifications, emails, SMS, and in-app messages via OneSignal.
* **ECID-based user matching**: Ensure users in OneSignal align with Adobe identities for accurate targeting.

***

## Requirements

* A [paid OneSignal account](https://onesignal.com/pricing).
* Users must be matched using Adobe's Marketing Cloud ID (MID or ECID).
  * Ensure the `external_id` field in OneSignal is set to the Adobe ECID.
  * If you prefer to use a different identifier, contact OneSignal Support.

***

## Setup

### Connection parameters

You’ll need the Client ID to configure the Adobe Destination:

* Go to your OneSignal Dashboard.
* Navigate to: **Data > Integrations > Adobe**.
* Copy the Client ID displayed there.

<Frame caption="Navigate to your Organization">
  <img src="https://mintcdn.com/onesignal/jBdBk5XvQR5eKOks/images/docs/73abd3d-client-id-smaller.png?fit=max&auto=format&n=jBdBk5XvQR5eKOks&q=85&s=21705ed30787e46ef3884773734bf308" width="1280" height="1015" data-path="images/docs/73abd3d-client-id-smaller.png" />
</Frame>

### Set up with Adobe

Contact your Adobe representative (Adobe consultant or CustomerCare) who will review the integration request and will work with you to activate the OneSignal Destination. You'll need to provide the following information to the Adobe representative:

* the Client ID

Once the Adobe representative has set up the OneSignal Destination, the segments should start flowing to OneSignal.

### Optional: Configure segment friendly names

By default, each segment synced between OneSignal and Adobe Audience Manager will be identified with a numeric Adobe Audience Manager Segment ID. If you'd like to instead use a "friendly" name to identify the Segment within the OneSignal Dashboard, please follow these steps:

1. Log in to Adobe Audience Manager
2. Follow the path to Audience Data > Segments
3. Select all the segments you wish to add to the OneSignal destination
4. Click "Add To Destination"
5. Select the Destination
6. Click Add To Selected Destination
7. Enter the friendly name for each Segment in the "Destination Value" fields

<Frame caption="Map friendly names in Adobe Audience Manager">
  <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/docs/03546e9-image001.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=25fb3c8bd4373a65b72cba711887d6c3" width="1070" height="348" data-path="images/docs/03546e9-image001.png" />
</Frame>

1. Click Save
2. The Segment "friendly" name has now been mapped to the Segment and the destination

***

<Info>
  Need help?

  Chat with our Support team or email `support@onesignal.com`

  Please include:

* Details of the issue you're experiencing and steps to reproduce if available
* Your OneSignal App ID
* The External ID or Subscription ID if applicable
* The URL to the message you tested in the OneSignal Dashboard if applicable
* Any relevant [logs or error messages](/docs/en/capturing-a-debug-log)

  We're happy to help!
</Info>

***

Built with [Mintlify](https://mintlify.com).
