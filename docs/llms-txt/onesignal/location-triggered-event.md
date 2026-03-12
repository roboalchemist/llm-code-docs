# Source: https://documentation.onesignal.com/docs/en/location-triggered-event.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Location-based messages

> Learn how to target users with location-based messages using OneSignal. Set up segments by country, coordinates, or geofencing with optional integrations like Radar.

## Overview

Location-based segmentation allows you to send messages based on where your users are. OneSignal can segment users by Country, GPS coordinates, or custom tags which can be used to create timely, relevant outreach based on physical location.

This guide explains how to configure segments by the available location options. As users interact with your app, their location data is updated in near real time and can be used to send messages via Journeys or any of our message creation tools.

***

## Target by country

Country is tracked based on the IP Address. This will automatically update each time the user opens your app.

Use the `country` Data Filter in [Segments](./segmentation) or API `filters`.

***

## Target by location (latitude, longitude, & radius)

If your mobile app collects GPS location and shares it with OneSignal, our SDK updates the user's coordinates approximately every 5 minutes (based on permission and system rules). Note that if the app becomes force stopped, the location can not be tracked until the user opens it again.

<Note>
  Your app must be setup to both:

  1. Share location updates with OneSignal
  2. Request and receive user permission to access location data

  See our [Mobile SDK location guide](./mobile-sdk-reference#location) for setup details.
</Note>

Once location tracking is enabled, you can:

* Create segments using the `location` filter (radius targeting).
* Trigger messages using the [Create message API](/reference/create-message).

<Frame caption="Location filter in Segments">
  <img src="https://mintcdn.com/onesignal/3zq1PvSaqvUE2bIx/images/docs/3109479-Screen_Shot_2021-02-09_at_8.28.43_AM.png?fit=max&auto=format&n=3zq1PvSaqvUE2bIx&q=85&s=13644c44bf75d4907e7fbda8641ae1bd" alt="Location filter in Segments" width="1440" height="938" data-path="images/docs/3109479-Screen_Shot_2021-02-09_at_8.28.43_AM.png" />
</Frame>

### Web push latitude and longitude tracking

OneSignal **does not collect** latitude/longitude for web-only users or users that do not have location tracking enabled for your mobile app. However, you can use data tags to set the location from your web app or use the [Update User API](/reference/update-user) to set the location points from your server.

**Tagging example:**

1. Ask for location access in your web app. Here is a great [Medium Post about this](https://medium.com/better-programming/how-to-detect-the-location-of-your-websites-visitor-using-javascript-92f9e91c095f).
2. Use JavaScript to detect the user's coordinates.
3. Send those coordinates to OneSignal using [Data Tags](./add-user-data-tags).

Example using `sendTags` SDK method:

```javascript  theme={null}
OneSignal.User.addTags({
  lat: "37.160",
  long: "-117.773"
});
```

Once the tags are set, you can create geofenced segments with range filters like so:

Example Segment: Tag `"long" > 37 AND "long" < 38 AND "lat" > -118 AND "lat" < -117`

***

## Target by city or custom location

OneSignal does not natively detect city or area codes. To target by city or custom location:

* Let users input a city/region in a form.
* Or use JavaScript + reverse geocoding (e.g., Google Maps API) to infer city from coordinates.
* Send the city name as a [Data Tag](./add-user-data-tags).

```javascript  theme={null}
OneSignal.User.addTag("city", "San Francisco");
```

We have also partnered with [Radar](https://radar.io/documentation/integrations/onesignal) to enrich and automate location tracking.

### Target based on a Geofence (Radar Integration)

OneSignal supports advanced geofencing through [Radar](https://radar.com/), a leading geolocation platform.

With Radar’s SDKs and APIs, you can:

* Trigger notifications when users enter/exit defined areas.
* Track delivery/pickup activity.
* Verify presence at a location.
* Power store locators, location-based offers, and more.

To get started:

* Visit the [Radar integration docs](https://radar.com/documentation/integrations/onesignal).
* Or [contact Radar](https://radar.com/contact) for onboarding support.

***

<Check>
  You can now send location-based messages. Automate with [Journeys](./journeys-overview) or [create one-off messages](/reference/create-message).
</Check>

***

Built with [Mintlify](https://mintlify.com).
