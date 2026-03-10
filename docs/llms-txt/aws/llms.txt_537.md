# Source: https://docs.aws.amazon.com/location/previous/developerguide/llms.txt

# Amazon Location Service Developer Guide

> With Amazon Location Service, you can securely add maps, points of interest, geocoding, geofences, and tracking to your applications.

- [Document history](https://docs.aws.amazon.com/location/previous/developerguide/doc-history.html)

## [What is Amazon Location Service](https://docs.aws.amazon.com/location/previous/developerguide/what-is-previous.html)

- [Key features](https://docs.aws.amazon.com/location/previous/developerguide/features.html)
- [Regions and endpoints](https://docs.aws.amazon.com/location/previous/developerguide/location-regions.html)
- [Service quotas](https://docs.aws.amazon.com/location/previous/developerguide/location-quotas.html)
- [Related services](https://docs.aws.amazon.com/location/previous/developerguide/related-services.html)


## [Quick start](https://docs.aws.amazon.com/location/previous/developerguide/getting-started.html)

### [Create a web app](https://docs.aws.amazon.com/location/previous/developerguide/qs-web.html)

In this section, you will create a static webpage with a map and the ability to search at a location.

- [Create resources](https://docs.aws.amazon.com/location/previous/developerguide/qs-create-resources-web.html): If you do not already have them, you must create the Amazon Location resources that your application will use.
- [Set up authentication](https://docs.aws.amazon.com/location/previous/developerguide/qs-setup-authentication-web.html): The application that you create in this tutorial has anonymous usage, meaning that your users are not required to sign into AWS to use the application.
- [Create HTML](https://docs.aws.amazon.com/location/previous/developerguide/qs-create-html.html): In this tutorial, you will create a static HTML page that embeds a map, and allows the user to find what's at a location on the map.
- [Add the map](https://docs.aws.amazon.com/location/previous/developerguide/qs-add-map.html): Now that you have a framework and a div placeholder, you can add the map control to your application.
- [Add search](https://docs.aws.amazon.com/location/previous/developerguide/qs-add-search.html): The last step for your application is to add searching on the map.
- [Review the application](https://docs.aws.amazon.com/location/previous/developerguide/qs-final-review.html): The final source code for this application is included in this section.

### [Create an Android app](https://docs.aws.amazon.com/location/previous/developerguide/qs-android.html)

In this section, you will create an Android application with a map, the ability to search at a location and tracking in the foreground.

- [Create resources](https://docs.aws.amazon.com/location/previous/developerguide/qs-create-resources-android.html): If you do not already have them, you must create the Amazon Location resources that your application will use.
- [Set up authentication](https://docs.aws.amazon.com/location/previous/developerguide/qs-setup-authentication-android.html): The application that you create in this tutorial has anonymous usage, meaning that your users are not required to sign into AWS to use the application.
- [Create the app](https://docs.aws.amazon.com/location/previous/developerguide/qs-create-app-android.html): In this tutorial, you will create an Android application that embeds a map and allows the user to find what's at a location on the map.
- [Add the map](https://docs.aws.amazon.com/location/previous/developerguide/qs-add-map-android.html): Now that you have created a basic application, you can add map control to your application.
- [Add search](https://docs.aws.amazon.com/location/previous/developerguide/qs-add-search-android.html): You will now add reverse geocoding search to your application, where you find the items at a location.
- [Add tracking](https://docs.aws.amazon.com/location/previous/developerguide/qs-add-tracking-android.html): To add tracking to your sample application, follow these steps:

### [Create an iOS app](https://docs.aws.amazon.com/location/previous/developerguide/qs-ios.html)

In this section, you will create an iOS application with the ability to search at a location and tracking in the foreground.

- [Create resources](https://docs.aws.amazon.com/location/previous/developerguide/qs-create-resources-ios.html): If you do not already have them, you must create the Amazon Location resources that your application will use.
- [Set up authentication](https://docs.aws.amazon.com/location/previous/developerguide/qs-setup-authentication-ios.html): The application that you create in this tutorial has anonymous usage, meaning that your users are not required to sign into AWS to use the application.
- [Create the app](https://docs.aws.amazon.com/location/previous/developerguide/qs-ios-create-app.html): In this tutorial, you will create an iOS application that embeds a map, and allows the user to find what's at a location on the map.
- [Set up initial code](https://docs.aws.amazon.com/location/previous/developerguide/qs-ios-create-app-initial-code.html): This page provides the initial code for a sample iOS application that integrates with the Amazon Location Service.
- [Add a map](https://docs.aws.amazon.com/location/previous/developerguide/qs-ios-add-map.html): You will now add the map control to your application.
- [Add search](https://docs.aws.amazon.com/location/previous/developerguide/qs-ios-add-search.html): You now will add reverse geocoding search to the application, where you find the items at a location.
- [Add tracking](https://docs.aws.amazon.com/location/previous/developerguide/qs-ios-add-tracking.html): The last step for your application is to add tracking functionality to your app.


## [Amazon Location concepts](https://docs.aws.amazon.com/location/previous/developerguide/how-it-works.html)

- [Overview](https://docs.aws.amazon.com/location/previous/developerguide/overview.html): Describes Amazon Location Service resources.
- [Learn about Maps resources](https://docs.aws.amazon.com/location/previous/developerguide/map-concepts.html)
- [Learn about Places search](https://docs.aws.amazon.com/location/previous/developerguide/places-concepts.html)
- [Learn about routing](https://docs.aws.amazon.com/location/previous/developerguide/route-concepts.html)

### [Learn about geofences and trackers](https://docs.aws.amazon.com/location/previous/developerguide/geofence-tracker-concepts.html)

This section provides and overview of the concepts of working with Amazon Location Service geofences and trackers.

- [Learn about geofences](https://docs.aws.amazon.com/location/previous/developerguide/geofence-overview.html): Geofence collection resources allow you to store and manage geofencesâvirtual boundaries on a map.
- [Learn about trackers](https://docs.aws.amazon.com/location/previous/developerguide/tracking-overview.html): A tracker stores position updates for a collection of devices.

### [Common use cases](https://docs.aws.amazon.com/location/previous/developerguide/common-usecases.html)

Describes the common business use cases for using Amazon Location, including asset tracking, delivery, and user engagement and geomarketing or geotargeting.

- [User engagement and geomarketing applications](https://docs.aws.amazon.com/location/previous/developerguide/user-engagement-geomarketing.html): The following is an illustration of a user engagement and geomarketing application architecture using Amazon Location:
- [Asset tracking applications](https://docs.aws.amazon.com/location/previous/developerguide/asset-tracking.html): The following is an illustration of an asset tracking application architecture using Amazon Location:
- [Delivery applications](https://docs.aws.amazon.com/location/previous/developerguide/delivery.html): The following is an illustration of a delivery application architecture using Amazon Location.

### [Data providers](https://docs.aws.amazon.com/location/previous/developerguide/what-is-data-provider.html)

Amazon Location enables you to access geolocation resources from multiple data providers through your AWS account.

- [Features by data provider](https://docs.aws.amazon.com/location/previous/developerguide/data-provider-features.html): This section describes the features available in Amazon Location Service, categorized by data provider.
- [Esri](https://docs.aws.amazon.com/location/previous/developerguide/esri.html): Amazon Location Service uses Esri's location services to help AWS customers to use maps, geocode, and calculate routes effectively.
- [GrabMaps](https://docs.aws.amazon.com/location/previous/developerguide/grab.html): Grab is the largest delivery organization in Southeast Asia, with millions of driver partners and customers.
- [HERE Technologies](https://docs.aws.amazon.com/location/previous/developerguide/HERE.html): Amazon Location Service uses HERE Technologiesâ location services to help AWS customers use maps, geocode, and calculate routes effectively.
- [Open Data](https://docs.aws.amazon.com/location/previous/developerguide/open-data.html): Amazon Location Service provides access to open source map data via the Open Data provider.
- [Terms of use and data attribution](https://docs.aws.amazon.com/location/previous/developerguide/data-attribution.html): Before you use a data provider, be sure you can comply with all applicable legal requirements, including license terms applicable to the use of the provider.


## [Develop with Amazon Location](https://docs.aws.amazon.com/location/previous/developerguide/dev-overview.html)

- [Scenarios and use cases](https://docs.aws.amazon.com/location/previous/developerguide/dev-usecases.html): Shows Amazon Location Service typical scenarios and how you might approach developing them.

### [SDKs and tools](https://docs.aws.amazon.com/location/previous/developerguide/dev-sdks.html)

Information on tools, SDKs for using Amazon Location Service .

- [SDKs by language](https://docs.aws.amazon.com/location/previous/developerguide/dev-by-language.html): The following tables provide information about AWS SDKs and MapLibre versions for languages and frameworks, by application type: web, mobile, or backend application.
- [How to use MapLibre](https://docs.aws.amazon.com/location/previous/developerguide/dev-maplibre.html): One of the important tools for creating interactive applications with Amazon Location is MapLibre.

### [How to use Amazon Location SDK](https://docs.aws.amazon.com/location/previous/developerguide/dev-location-libraries.html)

The Amazon Location SDK is a set of open source libraries that provide useful functionality for developing Amazon Location applications.

- [Amazon Location client](https://docs.aws.amazon.com/location/previous/developerguide/loc-sdk-client.html): With AWS SDK v3, the SDK is separated out by service.
- [JavaScript Authentication helper](https://docs.aws.amazon.com/location/previous/developerguide/loc-sdk-auth.html): The Amazon Location JavaScript authentication helper makes it simpler to authenticate when making Amazon Location API calls from your JavaScript application.
- [GeoJSON conversion helpers](https://docs.aws.amazon.com/location/previous/developerguide/loc-sdk-geojson.html): The Amazon Location GeoJSON conversion helpers provide tools to convert Amazon Location Service data types to and from the industry-standard GeoJSON format.
- [Android Mobile Authentication SDK](https://docs.aws.amazon.com/location/previous/developerguide/loc-sdk-auth-mobile-Android.html): These utilities help you authenticate when making Amazon Location Service API calls from your Android applications.
- [iOS Mobile Authentication SDK](https://docs.aws.amazon.com/location/previous/developerguide/loc-sdk-auth-mobile-ios.html): These utilities help you authenticate when making Amazon Location Service API calls from your iOS applications.
- [Android Mobile Tracking SDK](https://docs.aws.amazon.com/location/previous/developerguide/loc-mobile-tracking-android.html): The Amazon Location mobile tracking SDK provides utilities which help easily authenticate, capture device positions, and send position updates to Amazon Location Trackers.
- [iOS Mobile Tracking SDK](https://docs.aws.amazon.com/location/previous/developerguide/loc-mobile-tracking-ios.html): The Amazon Location mobile tracking SDK provides utilities which help easily authenticate, capture device positions, and send position updates to Amazon Location Trackers.

### [Amazon Location APIs](https://docs.aws.amazon.com/location/previous/developerguide/location-actions.html)

Describes the APIs to use in Amazon Location Service.

- [Error message updates](https://docs.aws.amazon.com/location/previous/developerguide/location-actions-errorupdates.html): Beginning August 1, 2023, the Amazon Location team is changing API error messages as described in the following tables.

### [Code examples](https://docs.aws.amazon.com/location/previous/developerguide/samples.html)

Learn more about Amazon Location Service by viewing code examples and tutorials.

- [Amazon Location Demo site](https://docs.aws.amazon.com/location/previous/developerguide/sample-demo-site.html)
- [Tutorial: Quick start](https://docs.aws.amazon.com/location/previous/developerguide/sample-quick-start.html)
- [Tutorial: Database enrichment](https://docs.aws.amazon.com/location/previous/developerguide/example-validate-database.html)
- [Example: Explore app](https://docs.aws.amazon.com/location/previous/developerguide/example-explore.html)
- [Example: Style a map](https://docs.aws.amazon.com/location/previous/developerguide/example-switch-styles.html)
- [Example: Draw markers](https://docs.aws.amazon.com/location/previous/developerguide/example-draw-markers.html)
- [Example: Draw clustered points](https://docs.aws.amazon.com/location/previous/developerguide/example-draw-clusters.html)
- [Example: Draw a polygon](https://docs.aws.amazon.com/location/previous/developerguide/example-draw-polygon.html)
- [Example: Change the map language](https://docs.aws.amazon.com/location/previous/developerguide/example-map-language.html)
- [Blog: Estimated delivery time notifications](https://docs.aws.amazon.com/location/previous/developerguide/example-delivery-notifications.html)
- [Example: Stream Position Updates](https://docs.aws.amazon.com/location/previous/developerguide/example-stream-position-updates.html)
- [Example: Geofencing and Tracking mobile application](https://docs.aws.amazon.com/location/previous/developerguide/example-tracking-geofencing.html): This sample application shows how a tracker and geofence interact using a combination of Lambda, AWS IoT and Amazon Location features.


## [How to use Amazon Location](https://docs.aws.amazon.com/location/previous/developerguide/using-amazon-location.html)

- [Account prerequisites](https://docs.aws.amazon.com/location/previous/developerguide/gs-prereqs.html): Describes the prerequisites for using Amazon Location Service, including creating your AWS account and setting up the correct access.

### [Using maps](https://docs.aws.amazon.com/location/previous/developerguide/using-maps.html)

Use Amazon Location Service to embed maps into your application.

- [Prerequisites for using Amazon Location maps](https://docs.aws.amazon.com/location/previous/developerguide/map-prerequisites.html): Before you start utilizing the mapping capabilities of Amazon Location Service, there are a few prerequisites that need to be fulfilled.

### [Displaying maps](https://docs.aws.amazon.com/location/previous/developerguide/display-map.html)

This section provides tutorials on how to use map rendering tools to display a map in your mobile or web application when using Amazon Location APIs.

### [Tutorial: MapLibre](https://docs.aws.amazon.com/location/previous/developerguide/tutorial-maplibre.html)

The following tutorials walk you through using the MapLibre Library with Amazon Location.

- [MapLibre GL JS](https://docs.aws.amazon.com/location/previous/developerguide/tutorial-maplibre-gl-js.html): Use MapLibre GL JS to embed client-side maps into web applications.
- [MapLibre Native SDK for Android](https://docs.aws.amazon.com/location/previous/developerguide/tutorial-maplibre-android.html): Use MapLibre Native SDK to embed interactive maps into your Android applications.
- [MapLibre Native SDK for iOS](https://docs.aws.amazon.com/location/previous/developerguide/tutorial-maplibre-ios.html): Use MapLibre Native SDK for iOS to embed client-side maps into iOS applications.
- [Tutorial: Amplify JS](https://docs.aws.amazon.com/location/previous/developerguide/tutorial-map-amplify.html): The following tutorial walks you through using AWS Amplify with Amazon Location.

### [Tutorial: Tangram](https://docs.aws.amazon.com/location/previous/developerguide/tutorial-tangram.html)

This section provides the following tutorials on how to integrate Tangram with Amazon Location.

- [Tangram](https://docs.aws.amazon.com/location/previous/developerguide/tutorial-tangram-js.html): Tangram is a flexible mapping engine, designed for real-time rendering of 2D and 3D maps from vector tiles.
- [Tangram ES for Android](https://docs.aws.amazon.com/location/previous/developerguide/tutorial-tangram-es-android.html): Tangram ES is a C++ library for rendering 2D and 3D maps from vector data using OpenGL ES.
- [Tangram ES for iOS](https://docs.aws.amazon.com/location/previous/developerguide/tutorial-tangram-es-ios.html): Tangram ES is a C++ library for rendering 2D and 3D maps from vector data using OpenGL ES.
- [Drawing on a map](https://docs.aws.amazon.com/location/previous/developerguide/drawing-on-a-map.html): After you have an application that renders a map, using Amplify, MapLibre, or Tangram to render the map, a natural next step is to draw features on top of the map.
- [Settings extents for a map](https://docs.aws.amazon.com/location/previous/developerguide/setting-map-extents.html): There are times that you do not want your users to be able to pan or zoom around the entire world.
- [Managing map resources](https://docs.aws.amazon.com/location/previous/developerguide/managing-maps.html): This topic covers the management and configuration of maps within the Amazon Location Service.

### [Places search](https://docs.aws.amazon.com/location/previous/developerguide/searching-for-places.html)

Use Amazon Location Service to add searching for places and other geolocation data into your application.

- [Prerequisites](https://docs.aws.amazon.com/location/previous/developerguide/places-prerequisites.html): Before you begin geocoding, reverse geocoding or searching for places, follow the prerequisite steps:
- [Geocoding](https://docs.aws.amazon.com/location/previous/developerguide/search-place-index-geocoding.html): Geocoding is a process that converts text, such as an address, a region, a business name, or point of interest, into a set of geographic coordinates.
- [Reverse geocoding](https://docs.aws.amazon.com/location/previous/developerguide/search-place-index-reverse-geocode.html): Reverse geocoding is a process that converts a set of coordinates into meaningful text, such as an address, a region, a business name, or point of interest.
- [Autocomplete](https://docs.aws.amazon.com/location/previous/developerguide/search-place-index-autocomplete.html): Autocomplete provides responsive feedback to end users as they are typing their search query.
- [Use place IDs with Amazon Location](https://docs.aws.amazon.com/location/previous/developerguide/search-using-placeids.html): Searching for places returns a list of results.
- [Categories and filtering](https://docs.aws.amazon.com/location/previous/developerguide/category-filtering.html): Places are categorized.
- [Tutorial: Database enrichment](https://docs.aws.amazon.com/location/previous/developerguide/database-address-validation.html): Use Amazon Location Service to format, and visualize addresses stored in a database.
- [Managing place index resources](https://docs.aws.amazon.com/location/previous/developerguide/managing-place-indexes.html): You can manage your place index resources using the Amazon Location console, the AWS CLI, or the Amazon Location APIs.

### [Calculating routes](https://docs.aws.amazon.com/location/previous/developerguide/calculating-routes.html)

Add route optimization features into your application using Amazon Location Service.

- [Prerequisites for calculating routes using Amazon Location](https://docs.aws.amazon.com/location/previous/developerguide/routes-prerequisites.html): Prerequisites for using routing functionality in Amazon Location Service.
- [Calculate route](https://docs.aws.amazon.com/location/previous/developerguide/calculate-route.html): Calculate a single route in Amazon Location Service.
- [Route planning](https://docs.aws.amazon.com/location/previous/developerguide/calculate-route-matrix.html): Calculate a route matrix to support route planning in Amazon Location Service.
- [Positions not located on a road in Amazon Location](https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html): How Amazon Location Service snaps positions when route endpoints are not found on a road.
- [Departure time with Amazon Location](https://docs.aws.amazon.com/location/previous/developerguide/departure-time.html): How Amazon Location Service works with departure time when calculating a route.
- [Travel mode with Amazon Location](https://docs.aws.amazon.com/location/previous/developerguide/travel-mode.html): How to set travel mode, including car, truck, or walking, when calculating a route in Amazon Location Service
- [Managing route resources](https://docs.aws.amazon.com/location/previous/developerguide/managing-route-calculators.html): You can manage your route calculator resources using the Amazon Location console, the AWS CLI, or the Amazon Location APIs.

### [Geofencing and tracking](https://docs.aws.amazon.com/location/previous/developerguide/geofence-an-area.html)

In Amazon Location Service, create a geofence to mark an area of interest on a map, and then track devices as they enter or leave the area.

- [Add geofences](https://docs.aws.amazon.com/location/previous/developerguide/add-geofences.html): Geofences contain points and vertices that form a closed boundary, which defines an area of interest.
- [Start tracking](https://docs.aws.amazon.com/location/previous/developerguide/start-tracking.html): This section guides you through building a tracking application that captures device locations.
- [Tutorial: Link a tracker to a geofence collection](https://docs.aws.amazon.com/location/previous/developerguide/associate-consumer.html): Now that you have a geofence collection and a tracker, you can link them together so that location updates are automatically evaluated against all of your geofences.
- [Evaluate device positions against geofences](https://docs.aws.amazon.com/location/previous/developerguide/evaluate-geofences.html): There are two ways to evaluate positions against geofences to generate geofence events:
- [Tutorial: Verify device positions](https://docs.aws.amazon.com/location/previous/developerguide/verify-device-positions.html): To check the integrity of a device position use the VerifyDevicePosition API.
- [Reacting to events with EventBridge](https://docs.aws.amazon.com/location/previous/developerguide/location-events.html): Use Amazon EventBridge to initiate automated actions for Amazon Location Service events.

### [Track with AWS IoT and MQTT](https://docs.aws.amazon.com/location/previous/developerguide/tracking-using-mqtt.html)

Use MQTT for tracking in Amazon Location Service, using AWS IoT Core.

- [Tutorial: Use AWS Lambda with MQTT](https://docs.aws.amazon.com/location/previous/developerguide/tracking-using-mqtt-with-lambda.html): While using AWS Lambda is no longer required when sending device location data to Amazon Location for tracking, you may still want to use Lambda in some cases.

### [Manage geofence resources](https://docs.aws.amazon.com/location/previous/developerguide/managing-geofence-collections.html)

Manage your geofence collections using the Amazon Location console, the AWS CLI, or the Amazon Location APIs.

- [Tutorial: List your geofence collection resources](https://docs.aws.amazon.com/location/previous/developerguide/viewing-geofence-collections.html): You can view your geofence collection list using the Amazon Location console, the AWS CLI, or the Amazon Location APIs:
- [Tutorial: Get geofence collection details](https://docs.aws.amazon.com/location/previous/developerguide/get-geofence-collection-details.html): You can get details about any geofence collection resource in your AWS account using the Amazon Location console, the AWS CLI, or the Amazon Location APIs:
- [Tutorial: Delete a geofence collection](https://docs.aws.amazon.com/location/previous/developerguide/delete-geofence-collection.html): You can delete a geofence collection from your AWS account using the Amazon Location console, the AWS CLI, or the Amazon Location APIs.
- [Tutorial: List stored geofences](https://docs.aws.amazon.com/location/previous/developerguide/viewing-geofences.html): You can list geofences stored in a specified geofence collection using the Amazon Location console, the AWS CLI, or the Amazon Location APIs.
- [Tutorial: Get geofence details](https://docs.aws.amazon.com/location/previous/developerguide/get-geofence-details.html): You can get the details of a specific geofence, such as the create time, update time, geometry, and status, from a geofence collection using the Amazon Location console, AWS CLI, or the Amazon Location APIs.
- [Tutorial: Delete geofences](https://docs.aws.amazon.com/location/previous/developerguide/delete-geofence.html): You can delete geofences from a geofence collection using the Amazon Location console, the AWS CLI, or the Amazon Location APIs.

### [Manage tracker resources](https://docs.aws.amazon.com/location/previous/developerguide/managing-trackers.html)

You can manage your trackers using the Amazon Location console, the AWS CLI, or the Amazon Location APIs.

- [Tutorial: List your trackers](https://docs.aws.amazon.com/location/previous/developerguide/viewing-trackers.html): You can view your trackers list using the Amazon Location console, the AWS CLI, or the Amazon Location APIs:
- [Tutorial: Disconnect a tracker from a geofence collection](https://docs.aws.amazon.com/location/previous/developerguide/disassociate-tracker.html): You can disconnect a tracker from a geofence collection using the Amazon Location console, the AWS CLI, or the Amazon Location APIs:
- [Tutorial: Get tracker details with Amazon Location](https://docs.aws.amazon.com/location/previous/developerguide/get-tracker-details.html): You can get details about any tracker in your AWS account by using the Amazon Location console, the AWS CLI, or the Amazon Location APIs.
- [Tutorial: Delete a tracker with Amazon Location](https://docs.aws.amazon.com/location/previous/developerguide/delete-tracker.html): You can delete a tracker from your AWS account using the Amazon Location console, the AWS CLI, or the Amazon Location APIs:

### [Sample Geofencing and Tracking mobile application](https://docs.aws.amazon.com/location/previous/developerguide/geofence-tracking-tutorials.html)

This topic covers tutorials designed to demonstrate the key features of using the Amazon Location geofences and trackers in a mobile application.

### [Sample tracking and geofence application for Android](https://docs.aws.amazon.com/location/previous/developerguide/qs-android-tracking.html)

This topic covers the Android tutorial designed to demonstrate the key features of using the Amazon Location geofences and trackers in a mobile application.

- [Tutorial: Create Amazon Location resources for your app](https://docs.aws.amazon.com/location/previous/developerguide/qs-android-tracking-resources.html): To begin you will need to create the required Amazon Location resources.
- [Tutorial: Create a Geofence Collection](https://docs.aws.amazon.com/location/previous/developerguide/qs-android-tracking-geofence.html): Now will you create a geofence collection.
- [Tutorial: Link a tracker to a geofence collection](https://docs.aws.amazon.com/location/previous/developerguide/qs-android-tracking-link-geofence.html): To link a tracker to a geofence collection you can use either the console, API, or CLI.
- [Tutorial: Use AWS Lambda with MQTT](https://docs.aws.amazon.com/location/previous/developerguide/qs-android-tracking-lambda.html): In order to create a connection between AWS IoT and Amazon Location, you need a Lambda function to process messages forwarded by EventBridge CloudWatch events.
- [Tutorial: Set up the sample app code](https://docs.aws.amazon.com/location/previous/developerguide/qs-android-tracking-sample-app-code.html): This page provides a sample Android application code that demonstrates how to integrate the tracking capabilities of Amazon Location Service into your mobile applications.
- [Tutorial: Use the sample app](https://docs.aws.amazon.com/location/previous/developerguide/qs-android-tracking-use.html): This guide walks you through the process of setting up and using the sample Android tracking application.

### [Sample tracking and geofencing application for iOS](https://docs.aws.amazon.com/location/previous/developerguide/qs-ios-tracking.html)

This topic covers the iOS tutorial designed to demonstrate the key features of using the Amazon Location geofences and trackers in a mobile application.

- [Tutorial: Create Amazon Location resources for your app](https://docs.aws.amazon.com/location/previous/developerguide/qs-ios-tracking-resources.html): To begin you will need to create the required Amazon Location resources.
- [Tutorial: Create a Geofence Collection](https://docs.aws.amazon.com/location/previous/developerguide/qs-ios-tracking-geofence.html): Now will you create a geofence collection.
- [Tutorial: Link a tracker to a geofence collection](https://docs.aws.amazon.com/location/previous/developerguide/qs-ios-tracking-link-geofence.html): To link a tracker to a geofence collection you can use either the console, API, or CLI.
- [Tutorial: Use AWS Lambda with MQTT](https://docs.aws.amazon.com/location/previous/developerguide/qs-ios-tracking-lambda.html): In order to create a connection between AWS IoT and Amazon Location, you need a Lambda function to process messages forwarded by EventBridge CloudWatch events.
- [Tutorial: Set up sample app code](https://docs.aws.amazon.com/location/previous/developerguide/qs-ios-tracking-setup-sample.html): In order to setup the sample code you must have the following tools installed:
- [Tutorial: Use the sample app](https://docs.aws.amazon.com/location/previous/developerguide/qs-ios-tracking-usage.html): After setting up the sample code you can now run the app on an iOS simulator or a physical device.

### [Tag your resources](https://docs.aws.amazon.com/location/previous/developerguide/tagging.html)

Create tags for your Amazon Location Service resources to categorize your resources for quick identification or to break down billing by tag.

- [Restrictions](https://docs.aws.amazon.com/location/previous/developerguide/tagging-restrictions.html): Tagging allows you to organize and manage your resources more effectively.
- [Grant permission to tag](https://docs.aws.amazon.com/location/previous/developerguide/tag-permissions.html): You can use IAM policies to control access to your Amazon Location resources and grant permission to tag a resource on creation.
- [Add a tag to a resource](https://docs.aws.amazon.com/location/previous/developerguide/create-tag.html): You can add tags when creating your resources using the Amazon Location console, the AWS CLI, or the Amazon Location APIs:
- [Track cost by tag](https://docs.aws.amazon.com/location/previous/developerguide/cost-by-tag.html): You can use tags for cost allocation to track your AWS cost in detail.
- [Control access to resources using tags](https://docs.aws.amazon.com/location/previous/developerguide/access-by-tag.html): AWS Identity and Access Management (IAM) policies support tag-based conditions, which enables you to manage authorization for your resources based on specific tags key and values.

### [Grant access to Amazon Location](https://docs.aws.amazon.com/location/previous/developerguide/how-to-access.html)

Describes the requirements to grant access to Amazon Location Service.

- [Use API keys](https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html): In Amazon Location Service, use API keys to grant access to unauthenticated users.
- [Use Amazon Cognito](https://docs.aws.amazon.com/location/previous/developerguide/authenticating-using-cognito.html): You can use Amazon Cognito authentication as an alternative to directly using AWS Identity and Access Management (IAM) with both front end SDKs and direct HTTPS requests.

### [Monitor usage and resources](https://docs.aws.amazon.com/location/previous/developerguide/monitoring.html)

When using Amazon Location Service, you can monitor your usage and resources over time by using:

- [Monitor with CloudWatch](https://docs.aws.amazon.com/location/previous/developerguide/monitoring-using-cloudwatch.html): Monitor Amazon Location Service to maintain reliability, availability, and performance.
- [Use CloudTrail with Amazon Location](https://docs.aws.amazon.com/location/previous/developerguide/logging-using-cloudtrail.html): Describes logging Amazon Location Service with AWS CloudTrail.
- [Use AWS CloudFormation to create resources](https://docs.aws.amazon.com/location/previous/developerguide/creating-resources-with-cloudformation.html): Learn about how to create resources for Amazon Location Service using an AWS CloudFormation template.


## [Security](https://docs.aws.amazon.com/location/previous/developerguide/security.html)

### [Data protection](https://docs.aws.amazon.com/location/previous/developerguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon Location Service.

- [Data privacy](https://docs.aws.amazon.com/location/previous/developerguide/data-privacy.html): With Amazon Location Service, you retain control of your organizationâs data.
- [Data retention](https://docs.aws.amazon.com/location/previous/developerguide/data-retention.html): The following characteristics relate to how Amazon Location collects and stores data for the service:
- [Data at rest encryption](https://docs.aws.amazon.com/location/previous/developerguide/encryption-at-rest.html): Amazon Location Service provides encryption by default to protect sensitive customer data at rest using AWS owned encryption keys.
- [Data in transit encryption](https://docs.aws.amazon.com/location/previous/developerguide/encryption-in-transit.html): Amazon Location protects data in transit, as it travels to and from the service, by automatically encrypting all inter-network data using the Transport Layer Security (TLS) 1.2 encryption protocol.

### [Identity and Access Management](https://docs.aws.amazon.com/location/previous/developerguide/security-iam.html)

How to authenticate requests and manage access to your Amazon Location resources.

- [How Amazon Location Service works with IAM](https://docs.aws.amazon.com/location/previous/developerguide/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon Location, learn what IAM features are available to use with Amazon Location.
- [How Amazon Location Service works with unauthenticated users](https://docs.aws.amazon.com/location/previous/developerguide/security_iam_unauthenticated-users.html): Many scenarios for using Amazon Location Service, including showing maps on the web or in a mobile application, require allowing access to users who haven't signed in with IAM.
- [Identity-based policy examples](https://docs.aws.amazon.com/location/previous/developerguide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify Amazon Location resources.
- [Troubleshooting](https://docs.aws.amazon.com/location/previous/developerguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon Location and IAM.

### [Incident response](https://docs.aws.amazon.com/location/previous/developerguide/incident-response.html)

Learn about security incident response within Amazon Location Service.

- [Logging and Monitoring](https://docs.aws.amazon.com/location/previous/developerguide/security-logging-and-monitoring.html): Learn how Amazon Location Service isolates service traffic.
- [Compliance validation](https://docs.aws.amazon.com/location/previous/developerguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/location/previous/developerguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon Location Service features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/location/previous/developerguide/infrastructure-security.html): Learn how Amazon Location Service isolates service traffic.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/location/previous/developerguide/vulnerability-analysis-and-management.html): Configuration and IT controls are a shared responsibility between AWS and you, our customer.
- [Confused deputy prevention](https://docs.aws.amazon.com/location/previous/developerguide/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
- [Best practices](https://docs.aws.amazon.com/location/previous/developerguide/best-practices.html): This topic provides recommendations for using Amazon Location Service.
