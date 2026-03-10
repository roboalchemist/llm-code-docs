# Source: https://docs.aws.amazon.com/location/latest/developerguide/llms.txt

# Amazon Location Service Developer Guide

> With Amazon Location Service, you can securely add maps, points of interest, geocoding, geofences, and tracking to your applications.

- [Build with AI agents](https://docs.aws.amazon.com/location/latest/developerguide/ai-llms.html)
- [Document history](https://docs.aws.amazon.com/location/latest/developerguide/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/location/latest/developerguide/glossary.html)

## [What is Amazon Location Service](https://docs.aws.amazon.com/location/latest/developerguide/what-is.html)

- [Key features](https://docs.aws.amazon.com/location/latest/developerguide/features.html): Amazon Location offers a comprehensive set of features to enhance your location-based applications and services.
- [Key benefits](https://docs.aws.amazon.com/location/latest/developerguide/benefits.html)
- [Supported regions](https://docs.aws.amazon.com/location/latest/developerguide/location-regions.html): Amazon Location Service is available across multiple AWS regions globally.
- [Pricing model](https://docs.aws.amazon.com/location/latest/developerguide/pricing.html): Amazon Location Service requires no up-front commitment and no minimum fee.
- [Terms of use and data attribution](https://docs.aws.amazon.com/location/latest/developerguide/data-attribution.html): Before you use Amazon Location Service, be sure you can comply with all applicable legal requirements, including license terms applicable to the use of the provider.
- [Data quality and coverage](https://docs.aws.amazon.com/location/latest/developerguide/data-quality.html): Amazon Location Service has extensive global coverage of map data.


## [Get started](https://docs.aws.amazon.com/location/latest/developerguide/getting-started.html)

- [Set up an account for the first time](https://docs.aws.amazon.com/location/latest/developerguide/set-up.html): Describes the prerequisites for using Amazon Location Service, including creating your AWS account and setting up the correct access.
- [Set up authentication for the first time](https://docs.aws.amazon.com/location/latest/developerguide/set-up-auth.html)
- [Choose an API](https://docs.aws.amazon.com/location/latest/developerguide/choose-an-api.html): This topic helps you choose an Amazon Location Service API based on common use cases that you may want to solve with location-based data and services.
- [Create your first Maps and Places application](https://docs.aws.amazon.com/location/latest/developerguide/first-app.html): In this section, you will create your first application with Maps and Places.

### [Create your first Geofences and Trackers application](https://docs.aws.amazon.com/location/latest/developerguide/first-geofence-app.html)

In this section, you'll create an application that demonstrates the key features of using the Amazon Location Geofences and Trackers.

- [iOS](https://docs.aws.amazon.com/location/latest/developerguide/ios-geofence-app.html): Follow these procedures to build an iOS application using Amazon Location Service.
- [Android](https://docs.aws.amazon.com/location/latest/developerguide/android-geofence-app.html): Follow these procedures to build an iOS application using Amazon Location Service.


## [Authentication](https://docs.aws.amazon.com/location/latest/developerguide/access.html)

- [Choose an authentication method](https://docs.aws.amazon.com/location/latest/developerguide/choose-method.html): API keys and Amazon Cognito are used in similar ways for similar scenarios, so why would you choose one instead of the other? The following list highlights some of the differences between the two.
- [Use API keys](https://docs.aws.amazon.com/location/latest/developerguide/using-apikeys.html): In Amazon Location Service, use API keys to grant access to unauthenticated users.
- [Use Amazon Cognito](https://docs.aws.amazon.com/location/latest/developerguide/authenticating-using-cognito.html): You can use Amazon Cognito authentication as an alternative to directly using AWS Identity and Access Management (IAM) users with frontend SDK requests.
- [Use IAM](https://docs.aws.amazon.com/location/latest/developerguide/security-iam.html): How to authenticate requests and manage access to your Amazon Location resources.


## [Maps](https://docs.aws.amazon.com/location/latest/developerguide/maps.html)

### [Map concepts](https://docs.aws.amazon.com/location/latest/developerguide/maps-concepts.html)

Learn about Amazon Location Service Map concepts.

- [Maps terminology](https://docs.aws.amazon.com/location/latest/developerguide/maps-terminology.html): Key terms related to Amazon Location Service Maps, including basemaps, vector and raster data, map rendering, and map styles.
- [Color scheme](https://docs.aws.amazon.com/location/latest/developerguide/maps-color-scheme.html): Amazon Location Service allows you to set the color scheme for maps.
- [Topography](https://docs.aws.amazon.com/location/latest/developerguide/maps-topographic-map.html): Topographic features such as terrain and contour lines display elevation changes and geographic features.
- [Navigation](https://docs.aws.amazon.com/location/latest/developerguide/maps-navigation-map.html): The navigation features such as Traffic and Truck TravelModes provide dynamic visualization tools that enhance navigation and route planning.
- [Localization and internationalization](https://docs.aws.amazon.com/location/latest/developerguide/maps-localization-internationalization.html): Amazon Location Service supports localization features that enable you to customize maps for specific languages and regions.
- [3D Features](https://docs.aws.amazon.com/location/latest/developerguide/maps-3d-map.html): Amazon Location Service's 3D visualization capabilities - terrain and buildings - help users make better decisions by adding depth and perspective to geographic data. 3D terrain reveals elevation changes critical for route optimization, emergency response planning, and outdoor recreation, while 3D buildings provide spatial context for urban navigation, real estate assessment, and landmark identification.

### [Map styles](https://docs.aws.amazon.com/location/latest/developerguide/map-styles.html)

Learn about Amazon Location Service Map styles.

- [Standard map style](https://docs.aws.amazon.com/location/latest/developerguide/standard-map-style.html): The Standard map style offers a clean, modern, and general-purpose map design that can seamlessly fit into almost any application or website.
- [Monochrome map style](https://docs.aws.amazon.com/location/latest/developerguide/monochrome-map-style.html): The Monochrome style is a minimalist canvas with a constrained color palette, designed for use with data visualization overlays.
- [Hybrid map style](https://docs.aws.amazon.com/location/latest/developerguide/hybrid-map-style.html): The Hybrid map style combines global satellite imagery with the same clear labels and configurable points of interest (POI) categories found in the Standard map style.

### [Map APIs](https://docs.aws.amazon.com/location/latest/developerguide/choose-maps-apis.html)

Maps provide access to both dynamic and static map types for a variety of applications.

### [Dynamic maps](https://docs.aws.amazon.com/location/latest/developerguide/dynamic-maps.html)

- [Tiles](https://docs.aws.amazon.com/location/latest/developerguide/tiles.html): Map tiles are pre-rendered, small sections of a larger map, typically displayed as square images.
- [Style dynamic maps](https://docs.aws.amazon.com/location/latest/developerguide/styling-dynamic-maps.html): Amazon Location Service provides two options for styling your dynamic maps: using predesigned AWS Map Styles or customizing the map style using style descriptors.
- [Style iconography with sprites](https://docs.aws.amazon.com/location/latest/developerguide/styling-iconography-with-sprites.html): A sprite is a Portable Network Graphic (PNG) image file that contains small raster images such as icons, markers, and other elements rendered on a map.
- [Style labels with glyphs](https://docs.aws.amazon.com/location/latest/developerguide/styling-labels-with-glyphs.html): Glyphs are binary files containing encoded Unicode characters, which are used by a map renderer to display labels.

### [Static maps](https://docs.aws.amazon.com/location/latest/developerguide/static-maps.html)

- [Customize static maps](https://docs.aws.amazon.com/location/latest/developerguide/customizing-static-maps.html)
- [Overlay on the static map](https://docs.aws.amazon.com/location/latest/developerguide/overlaying-static-map.html): This section explains how to overlay additional information onto static maps using Amazon Location Service.

### [How to](https://docs.aws.amazon.com/location/latest/developerguide/maps-how-to.html)

This section contains a variety of how to guides and examples for how to use Maps APIs.

### [Dynamic maps](https://docs.aws.amazon.com/location/latest/developerguide/dynamic-maps-how-to.html)

These how-to topics offer a comprehensive walkthrough teaching you how to enhance your mapping applications using the Amazon Location Service.

- [Display a map](https://docs.aws.amazon.com/location/latest/developerguide/how-to-display-a-map.html): Amazon Location Service allows you to display both interactive and non-interactive maps using our map styles.
- [Add control on the map](https://docs.aws.amazon.com/location/latest/developerguide/how-to-add-control-on-map.html): Amazon Location Service allows you to add multiple controls to the map, including navigation, geolocation, fullscreen, scale, and attribution controls.
- [Add a marker on the map](https://docs.aws.amazon.com/location/latest/developerguide/how-to-add-marker-on-map.html): With Amazon Location, you can add both fixed and draggable markers, and you can also customize the color of the markers based on your data and preferences.
- [Add an icon on the map](https://docs.aws.amazon.com/location/latest/developerguide/how-to-add-icon-on-map.html): Amazon Location Service enables you to add icons, preferably in PNG format, to the map.
- [Add a line on the map](https://docs.aws.amazon.com/location/latest/developerguide/how-to-add-line-on-map.html): With Amazon Location Service, you can add both pre-recorded GPS traces as line-strings and real-time GPS traces to dynamic maps.
- [Add a polygon on the map](https://docs.aws.amazon.com/location/latest/developerguide/how-to-add-polygon-on-map.html): Amazon Location Service allows you to add polygons to the map.
- [Add a popup to a map](https://docs.aws.amazon.com/location/latest/developerguide/how-to-add-popup-to-map.html): Amazon Location Service allows you to add popups to the map.
- [Set a preferred language for a map](https://docs.aws.amazon.com/location/latest/developerguide/how-to-set-preferred-language-map.html): Amazon Location Service enables you to set the preferred language at the client-side by updating the style descriptor for a specific language.
- [Set the political view of a map](https://docs.aws.amazon.com/location/latest/developerguide/how-to-set-political-view-map.html): Amazon Location Service enables you to set the political view to ensure your application complies with local laws.
- [Filter POI](https://docs.aws.amazon.com/location/latest/developerguide/how-to-filter-poi-map.html): Amazon Location Service allows you to select the POI (point-of-interest) categories relevant to your use case.
- [Topographic maps](https://docs.aws.amazon.com/location/latest/developerguide/how-to-create-topographic-maps.html): Amazon Location Service allows you to create topographic maps using Terrain and Contour density features to visualize elevation changes and geographic characteristics.
- [Show real-time traffic on a map](https://docs.aws.amazon.com/location/latest/developerguide/how-to-set-real-time-traffic-map.html): Using Amazon Location Service you can add traffic features to your map.
- [Create a logistics map](https://docs.aws.amazon.com/location/latest/developerguide/how-to-create-logistic-map.html): The TravelModes feature lets you build logistic maps using Amazon Location Service.
- [Show transit details on a map](https://docs.aws.amazon.com/location/latest/developerguide/how-to-show-transit-details-map.html): Amazon Location Service lets you add transit features to maps.
- [Show 3D features on a map](https://docs.aws.amazon.com/location/latest/developerguide/how-to-show-3d-features-map.html): Amazon Location Service lets you add three-dimensional features to maps, such as Terrain3D to display elevation data as a three-dimensional surface, or Buildings3D to display urban structures with height and volume.

### [Static maps](https://docs.aws.amazon.com/location/latest/developerguide/static-maps-how-to.html)

These how-to topics offer step-by-step guidance for customizing static maps with overlays and visual elements, utilizing the mapping capabilities of Amazon Location Service.

- [Get a static map of a specific position](https://docs.aws.amazon.com/location/latest/developerguide/get-static-map-specific-position.html): In this topic, you will learn how to retrieve static maps from Amazon Location Service based on specific parameters.
- [Get a static map of a specific dimension](https://docs.aws.amazon.com/location/latest/developerguide/get-static-map-specific-dimension.html): In this topic, you will learn how to set the dimensions (height and width) for static maps using Amazon Location Service.
- [Decide between radius and zoom for a static map](https://docs.aws.amazon.com/location/latest/developerguide/choose-radius-vs-zoom.html): In this topic, you will learn how to choose between using radius or zoom when generating static maps with Amazon Location Service.
- [Add scale for a static map](https://docs.aws.amazon.com/location/latest/developerguide/add-scale-static-map.html): In this topic, you will learn how to display a scale on the bottom-right corner of a static map generated with Amazon Location Service.
- [Add a marker to a static map](https://docs.aws.amazon.com/location/latest/developerguide/add-marker-static-map.html): In this topic, you will learn how to add markers to static maps generated with Amazon Location Service.
- [Add a line to a static map](https://docs.aws.amazon.com/location/latest/developerguide/how-to-add-line-static.html): In this topic, you'll learn how to add a line to a static map using Amazon Location Service.
- [Add a route to a static map](https://docs.aws.amazon.com/location/latest/developerguide/how-to-add-route.html): In this topic, you'll learn how to add a route to a static map using Amazon Location Service.
- [Add a polygon to a static map](https://docs.aws.amazon.com/location/latest/developerguide/how-to-add-polygon-static.html): Buildings and locations can be highlighted on a map by designating a polygon around them, for example, the Pentagon (located in Washington, D.C.).
- [Set language for static maps](https://docs.aws.amazon.com/location/latest/developerguide/set-language-static-map.html): You can set the language for a static map, in case you don't want to use the default language.
- [Add proximity circle to a static map](https://docs.aws.amazon.com/location/latest/developerguide/how-to-add-proximity-circle.html): How to add a proximity circle to a static map

### [Manage costs and usage](https://docs.aws.amazon.com/location/latest/developerguide/maps-whats-next.html)

Lean how to manage your Amazon Location mapping costs and usage.

- [Best practices](https://docs.aws.amazon.com/location/latest/developerguide/maps-best-practices.html): When working with Amazon Location Service, adhering to best practices ensures your maps are optimized for performance, accuracy, and user experience.
- [Pricing](https://docs.aws.amazon.com/location/latest/developerguide/maps-pricing.html): Amazon Location Service offers competitive pricing for its Maps API based on the type of map request and the number of API calls made.
- [Quotas and usage](https://docs.aws.amazon.com/location/latest/developerguide/map-quota-and-usage.html): Amazon Location Service imposes specific service quotas and usage limits for both dynamic and static maps.


## [Places](https://docs.aws.amazon.com/location/latest/developerguide/places.html)

### [Places concepts](https://docs.aws.amazon.com/location/latest/developerguide/places-common-concepts.html)

This section covers essential concepts related to the Amazon Location Service Places API, including terminology, querying and biasing, filtering options, localization, and intended use of API results.

- [Places terminology](https://docs.aws.amazon.com/location/latest/developerguide/places-terminology.html): Key terminology related to Amazon Location Service Places, including foundational concepts for working with locations, addresses, and points of interest.
- [Querying and biasing](https://docs.aws.amazon.com/location/latest/developerguide/places-querying-biasing.html): Amazon Location Service Places API offers querying and biasing options to retrieve and search location data.
- [Filtering](https://docs.aws.amazon.com/location/latest/developerguide/places-filtering.html): Amazon Location Service Places API offers filtering options to narrow down search results based on specific criteria.
- [Localization and internationalization](https://docs.aws.amazon.com/location/latest/developerguide/places-localization-internationalization.html): Localization (L10n) and Internationalization (I18n) are key processes in adapting software, content, or applications for different languages, regions, and views.
- [Contacts and opening hours](https://docs.aws.amazon.com/location/latest/developerguide/contacts-opening-hours.html): Amazon Location Service provides details on contacts and opening hours for various points of interest (POIs), enabling applications to offer comprehensive information about business operations.
- [Additional features](https://docs.aws.amazon.com/location/latest/developerguide/additional-features.html): This section provides an overview of additional features supported by the Place APIs.
- [IntendedUse](https://docs.aws.amazon.com/location/latest/developerguide/places-intended-use.html)

### [Places APIs](https://docs.aws.amazon.com/location/latest/developerguide/places-choose-api.html)

Places enable applications to search, find, and retrieve details about points of interest, addresses, and specific locations.

- [Geocode](https://docs.aws.amazon.com/location/latest/developerguide/geocode.html): Geocoding transforms textual addresses or place names into geographic coordinates, along with detailed address components and additional information.
- [Reverse Geocode](https://docs.aws.amazon.com/location/latest/developerguide/reverse-geocode.html): Reverse Geocode converts geographic coordinates into a human-readable address or place.
- [Autocomplete](https://docs.aws.amazon.com/location/latest/developerguide/autocomplete.html): Autocomplete returns complete addresses and address components based on partial input.
- [GetPlace](https://docs.aws.amazon.com/location/latest/developerguide/get-place.html): GetPlace retrieves detailed information about a place using its unique PlaceId.
- [Search Nearby](https://docs.aws.amazon.com/location/latest/developerguide/search-nearby.html): The Search Nearby API allows developers to query for points of interest within a specified radius from central coordinates.
- [Search Text](https://docs.aws.amazon.com/location/latest/developerguide/search-text.html): Search Text allows you to query location data using a single free-form text input, returning place results with optional filters like country, geographic circle, or bounding box.
- [Suggest](https://docs.aws.amazon.com/location/latest/developerguide/suggest.html): Suggest provides predictions or recommendations based on user input or context, such as relevant places, points of interest, query terms, or search categories.

### [How to](https://docs.aws.amazon.com/location/latest/developerguide/places-how-to.html)

Learn about the places how to guides and examples.

### [Use Geocode](https://docs.aws.amazon.com/location/latest/developerguide/how-to-geocode.html)

Learn how to convert addresses and place names to geographic coordinates using the Geocode API with comprehensive examples and filtering options.

- [Geocode an administrative and postal area](https://docs.aws.amazon.com/location/latest/developerguide/how-to-geocode-admin-postal-area.html): The Geocode API allows you to perform geocoding for a geographic area using a query text input, such as the name of a country, region (state or province), or city.
- [Geocode an address](https://docs.aws.amazon.com/location/latest/developerguide/how-to-geocode-address.html): The Geocode API enables you to geocode a specific point address, interpolated address, or street.
- [Geocode POI](https://docs.aws.amazon.com/location/latest/developerguide/how-to-geocode-poi.html): You can use the geocode API to geocode the coordinates of a known place (Point of interest) such as business addresses, landmark, or tourist spot.
- [Geocode address with postal code](https://docs.aws.amazon.com/location/latest/developerguide/how-to-geocode-address-postal-code.html): In countries where postal codes are highly specific (linking only a few addresses on the same street), an address can be found using only the house number and postal code.
- [Geocode using geospatial context](https://docs.aws.amazon.com/location/latest/developerguide/how-to-geocode-geospatial.html): The Geocode API enables you to use geospatial context (such as bias position) to get desired results.
- [Geocode using filters](https://docs.aws.amazon.com/location/latest/developerguide/how-to-geocode-filters.html): The Geocode API enables you to use filters to get desired results.
- [Geocode for time zone](https://docs.aws.amazon.com/location/latest/developerguide/how-to-geocode-timezone.html): You can use the Geocode API to provide time zone information such as UTC offset and time zone name.
- [Geocode in a language](https://docs.aws.amazon.com/location/latest/developerguide/how-to-geocode-specific-language.html): This feature allows the selection of a preferred response language from BCP47-compliant codes.
- [Get secondary addresses](https://docs.aws.amazon.com/location/latest/developerguide/get-secondary-address.html): SecondaryAddresses allows you to retrieve all secondary addresses that are under a main address.
- [Get intersections](https://docs.aws.amazon.com/location/latest/developerguide/get-intersections.html): Intersections allows you to retrieve all nearby intersections.

### [Use ReverseGeocode](https://docs.aws.amazon.com/location/latest/developerguide/reverse-geocode-how-to.html)

Learn how to convert coordinates to meaningful location information using the ReverseGeocode API with practical examples and implementation guidance.

- [Reverse geocode for a position](https://docs.aws.amazon.com/location/latest/developerguide/how-to-reverse-geocode-position.html): The Reverse Geocode API allows you to convert a geocode to a geographic area based on a position query.
- [Reverse geocode for correct result](https://docs.aws.amazon.com/location/latest/developerguide/reverse-geocode-filter-right-result.html): This guide provides methods to refine reverse geocoding results, ensuring that the returned data aligns closely with specific business needs.
- [Reverse geocode in a language](https://docs.aws.amazon.com/location/latest/developerguide/how-to-reverse-geocode-specific-language.html): The feature allows the selection of a preferred response language from BCP47-compliant codes.
- [Reverse geocode for time zone](https://docs.aws.amazon.com/location/latest/developerguide/how-to-reverse-geocode-timezone.html): You can use the Reverse Geocode API to request for time zone information such as UTC offset and time zone name
- [Reverse geocode with political view](https://docs.aws.amazon.com/location/latest/developerguide/reverse-geocode-political-view.html): The Amazon Location Service allows you to specify a political view to ensure your application aligns with local regulations.
- [Get intersections](https://docs.aws.amazon.com/location/latest/developerguide/reverse-how-to-get-intersections.html): ReverseGeocode API can retrieve nearby intersections to the specified location.

### [Use Autocomplete](https://docs.aws.amazon.com/location/latest/developerguide/autocomplete-how-to.html)

Learn how to implement address autocompletion for user input with the Autocomplete API, including filtering options and response customization for enhanced search experiences.

- [How to complete an address](https://docs.aws.amazon.com/location/latest/developerguide/how-to-complete-address.html): Learn how to implement basic address autocompletion that suggests matching addresses as users type, improving search efficiency and user experience with minimal configuration.
- [How to complete an address with filters](https://docs.aws.amazon.com/location/latest/developerguide/how-to-complete-address-with-filters.html): Discover how to enhance address autocompletion with filtering options that narrow results by region, country, or place type, delivering more relevant and targeted address suggestions.

### [Use Get Place](https://docs.aws.amazon.com/location/latest/developerguide/get-place-how-to.html)

Learn how to retrieve detailed place information using the GetPlace API with examples and use cases.

- [Get results for a PlaceId](https://docs.aws.amazon.com/location/latest/developerguide/how-to-get-place-by-id.html): The GetPlace API retrieves detailed information about a place using its unique PlaceId, allowing applications to access comprehensive details about specified locations.
- [Get contacts for a PlaceId](https://docs.aws.amazon.com/location/latest/developerguide/how-to-get-contacts-by-place-id.html): The GetPlace API allows retrieval of contact information associated with a specific PlaceId, providing you with details such as phone numbers and website URLs.
- [Get the time zone for a PlaceId](https://docs.aws.amazon.com/location/latest/developerguide/how-to-get-timezone-by-place-id.html): The GetPlace API allows retrieval of contact information associated with a specific PlaceId, providing you with details such as phone numbers, time zones, and website URLs.
- [Get the details for PlaceId in a specific language](https://docs.aws.amazon.com/location/latest/developerguide/how-to-get-place-details-language-place-id.html): The feature allows you to select a preferred response language from BCP47-compliant codes.
- [Get secondary addresses place ID](https://docs.aws.amazon.com/location/latest/developerguide/how-to-get-secondary-addresses-placeid.html): The SecondaryAddresses API command allows you to retrieve all secondary addresses that are under a main address.

### [Use SearchNearby](https://docs.aws.amazon.com/location/latest/developerguide/search-nearby-how-to.html)

Learn how to find places, businesses, and points of interest near specific coordinates using the SearchNearby API with filtering options and distance parameters.

- [Search nearby from a position](https://docs.aws.amazon.com/location/latest/developerguide/how-to-search-nearby.html): The SearchNearby API enables querying for all nearby places and points of interest (POI) without entering any specific text.
- [Search nearby places based on category](https://docs.aws.amazon.com/location/latest/developerguide/how-to-search-nearby-category.html): The SearchNearby API enables querying for points of interest (POI) with the inclusion or exclusion of specified categories.
- [Search nearby places based on food type](https://docs.aws.amazon.com/location/latest/developerguide/how-to-search-nearby-food.html): The SearchNearby API enables you query nearby restaurants that serve a specific type of food.
- [Search nearby places based on business chain](https://docs.aws.amazon.com/location/latest/developerguide/how-to-search-nearby-business.html): The SearchNearby API enables you to query nearby business chains.
- [Search nearby places within a country](https://docs.aws.amazon.com/location/latest/developerguide/how-to-search-nearby-country.html): The SearchNearby API enables you to search for nearby places within a specific country.
- [Search nearby with geospatial context](https://docs.aws.amazon.com/location/latest/developerguide/how-to-search-nearby-geospatial.html): The SearchNearby API enables you to explore nearby, while restricting results within geospatial context (such as a circle or bounding box).

### [Use SearchText](https://docs.aws.amazon.com/location/latest/developerguide/search-text-how-to.html)

Learn how to search for places, points of interest, and businesses using the SearchText API with filtering options and practical examples.

- [Search for a place, POI, or business using a name](https://docs.aws.amazon.com/location/latest/developerguide/how-to-search-for-place-poi-business.html): The SearchText API allows users to search for a place, POI, or business by name, using free text input.
- [Search for a place using contact information](https://docs.aws.amazon.com/location/latest/developerguide/how-to-search-for-place-using-contact-info.html): The SearchText API allows users to search for a place using a phone number, supporting both international and local formats.
- [Search categories or food types](https://docs.aws.amazon.com/location/latest/developerguide/how-to-search-category-name.html): The SearchText API enables you to search by name of category such as restaurants, schools and more.
- [Search for addresses](https://docs.aws.amazon.com/location/latest/developerguide/how-to-search-address.html): The SearchText API enables you to search for an address.
- [Search within a country](https://docs.aws.amazon.com/location/latest/developerguide/how-to-search-place-in-country.html): The SearchText API enables you limit search results to within one or more countries.
- [Search contact and opening hours](https://docs.aws.amazon.com/location/latest/developerguide/how-to-search-opening-hours.html): The SearchText API enables you to search for contacts and opening hours of a POI (Point of Interest).
- [Search using query ID](https://docs.aws.amazon.com/location/latest/developerguide/how-to-search-query-id.html): The SearchText API enables you get details of the query result returned by .
- [Search in a language](https://docs.aws.amazon.com/location/latest/developerguide/how-to-search-specific-language.html): This feature allows the selection of a preferred response language from BCP47-compliant codes.

### [Use Suggest](https://docs.aws.amazon.com/location/latest/developerguide/suggest-how-to.html)

Learn how to implement predictive place suggestions based on partial user input using the Suggest API with filtering options and response customization.

- [Predict suggestions based on input](https://docs.aws.amazon.com/location/latest/developerguide/how-to-predict-suggestions.html): The Suggest API enables applications to complete user queries for places or categories of results.
- [Get results for a partially typed or misspelled query](https://docs.aws.amazon.com/location/latest/developerguide/how-to-get-results-for-partial-or-misspelled-queries.html): The Suggest API enables applications to complete user queries for places or categories of results.
- [Highlight matched query terms](https://docs.aws.amazon.com/location/latest/developerguide/suggest-highlight-matched-query-terms.html): With the Suggest API, you get real-time autocomplete suggestions as users type their search queries for places or categories.
- [Filter results for a region](https://docs.aws.amazon.com/location/latest/developerguide/suggest-filter-region-country.html): The Suggest API enables completing queries for places or categories of results.
- [Disambiguate results](https://docs.aws.amazon.com/location/latest/developerguide/suggest-disambiguate-results.html): The Suggest API enables you to create queries for places or categories of results.

### [Manage costs and usage](https://docs.aws.amazon.com/location/latest/developerguide/places-whats-next.html)

As you continue exploring Amazon Location Service, it's important to understand how to manage service capacity and costs, ensure you follow usage limits, and get the best results through quota and API optimizations.

- [Best practices](https://docs.aws.amazon.com/location/latest/developerguide/places-best-practices.html): This section outlines best practices for optimizing the performance and accuracy of API interactions in your application.
- [Places pricing](https://docs.aws.amazon.com/location/latest/developerguide/places-pricing.html): The price for the Place APIs is based on the number of API requests.
- [Quotas and usage](https://docs.aws.amazon.com/location/latest/developerguide/places-quota-usage.html): Amazon Location Service places quotas on API usage to manage service capacity and prevent over utilization.


## [Routes](https://docs.aws.amazon.com/location/latest/developerguide/routes.html)

### [Routes concepts](https://docs.aws.amazon.com/location/latest/developerguide/routes-concepts.html)

The Routes concepts in Amazon Location Service provide a robust framework for planning and optimizing journeys, whether for simple navigation or complex logistics.

- [Terminology](https://docs.aws.amazon.com/location/latest/developerguide/routes-terminology.html)
- [Where (origin, destination, waypoint, and traces)](https://docs.aws.amazon.com/location/latest/developerguide/concepts-where.html): Specifies the location for route calculation, including where the route starts, ends, and intermediate stops (or locations to be passed through).
- [When (departure and arrival)](https://docs.aws.amazon.com/location/latest/developerguide/concepts-when.html): Specifies the time for route calculation.
- [How (travel mode, avoidance, and exclusion)](https://docs.aws.amazon.com/location/latest/developerguide/concepts-how.html): Use the following options to specify the travel mode and related features to use for route calculation.
- [Traffic awareness](https://docs.aws.amazon.com/location/latest/developerguide/concepts-traffic-awareness.html): Determines the type of traffic-related information used during route calculation.
- [Optimize route and waypoint sequence](https://docs.aws.amazon.com/location/latest/developerguide/optimize-route-waypoint.html): This section discusses the optimization options available when calculating a route, including both optimizing the overall route and optimizing the waypoint sequence.
- [Driver schedule and notices](https://docs.aws.amazon.com/location/latest/developerguide/driver-schedule-notices.html): This section provides details on configuring driver schedules and managing notices, warnings, and constraints during route calculations.

### [Route APIs](https://docs.aws.amazon.com/location/latest/developerguide/choose-routes-apis.html)

Routes provide capabilities for calculating optimized paths between locations.

### [Calculate routes](https://docs.aws.amazon.com/location/latest/developerguide/calculate-routes.html)

The Routes API calculates routes between two or more locations with or without avoidances for different travel modes such as car, truck, scooter, and pedestrian.

- [Calculate toll cost](https://docs.aws.amazon.com/location/latest/developerguide/calculate-toll-cost.html): This topic provides an overview of the fields and definitions associated with calculating toll costs.
- [Understanding route steps](https://docs.aws.amazon.com/location/latest/developerguide/understanding-route-steps.html): This section defines various actions and steps that need to be taken to complete a leg of a journey.
- [Calculate route matrix](https://docs.aws.amazon.com/location/latest/developerguide/calculate-route-matrix.html): The Matrix Routing service calculates routing matrices, providing travel times or distances between multiple origins and destinations.
- [Calculate isolines](https://docs.aws.amazon.com/location/latest/developerguide/calculate-isolines.html): The Calculate Isolines API allows you to determine areas reachable within specified time or distance limits.
- [Optimize waypoints](https://docs.aws.amazon.com/location/latest/developerguide/actions-optimize-waypoints.html): The Optimize Waypoints API calculates the most efficient sequence for visiting multiple waypoints along a route.
- [Snap to Roads](https://docs.aws.amazon.com/location/latest/developerguide/snap-to-roads.html): The Snap to Road API enhances the accuracy of geographic positioning by aligning GPS coordinates to the nearest road segments on a digital map.

### [How to](https://docs.aws.amazon.com/location/latest/developerguide/routes-how-to.html)

Learn how to use Amazon Location routes.

### [Use CalculateRoutes](https://docs.aws.amazon.com/location/latest/developerguide/calculate-routes-how-to.html)

Learn how to use CalculateRoutes in Amazon Location with examples.

- [Find a route for an origin and destination](https://docs.aws.amazon.com/location/latest/developerguide/calculate-routes-origin-destination-waypoints.html): The CalculateRoutes API helps you find the best routes between origin and destination, as well as the best opportunities for driver resting.
- [Find routes with turn-by-turn directions](https://docs.aws.amazon.com/location/latest/developerguide/how-to-find-turn-by-turn-route.html): The CalculateRoutes API helps you to find the best routes between origin and destination, as well as the best opportunities for driver resting.
- [Find a speed limit for a road span](https://docs.aws.amazon.com/location/latest/developerguide/calculate-routes-speed-limit-road.html): The CalculateRoutes API helps you to find the best routes between origin and destination, as well as the best opportunities for driver resting.
- [Find an alternate route](https://docs.aws.amazon.com/location/latest/developerguide/calculate-routes-alternate.html): The CalculateRoutes API helps you to find the best routes between origin and destination, as well as the best opportunities for driver resting.
- [Calculate tolls for a route](https://docs.aws.amazon.com/location/latest/developerguide/calculate-routes-tolls.html): The CalculateRoutes API helps you to find the best routes between origin and destination, as well as the best opportunities for driver resting.
- [Calculate routes with custom avoidance](https://docs.aws.amazon.com/location/latest/developerguide/calculate-routes-custom-avoidance-poly.html): The CalculateRoutes API helps you to find the best routes between origin and destination, as well as the best opportunities for driver resting.
- [Calculate routes with custom avoidance of several items](https://docs.aws.amazon.com/location/latest/developerguide/calculate-routes-custom-avoidance-multiple.html): The CalculateRoutes API helps you to find the best routes between origin and destination, as well as the best opportunities for driver resting.
- [Calculate the fastest route](https://docs.aws.amazon.com/location/latest/developerguide/calculate-routes-custom-avoidance-fast.html): The CalculateRoutes API helps you to find the fastest routes between origin and destination.
- [Calculate the shortest routes](https://docs.aws.amazon.com/location/latest/developerguide/calculate-routes-custom-avoidance-shortest.html): The CalculateRoutes API helps you to find the shortest routes between origin and destination.

### [Use CalculateIsolines](https://docs.aws.amazon.com/location/latest/developerguide/calculate-isolines-how-to.html)

In this section you learn how to use CalculateIsolines with ranges of time or distance, as well as to set areas to avoid.

- [Calculate a service area based on ranges of time](https://docs.aws.amazon.com/location/latest/developerguide/calculate-service-area-based-on-time.html): The CalculateIsolines API allows you to determine reachable service areas within specified ranges of time or distance, factoring in road networks and traffic conditions.
- [Calculate a service area based on ranges of distance](https://docs.aws.amazon.com/location/latest/developerguide/calculate-service-area-based-on-distance.html): The CalculateIsolines API allows you to determine reachable service areas within specified ranges of time or distance, factoring in road networks and traffic conditions.
- [Calculate a service area based on avoidance](https://docs.aws.amazon.com/location/latest/developerguide/calculate-service-area-based-on-avoidance.html): The CalculateIsolines API allows you to determine reachable service areas within specified ranges of time or distance, factoring in road networks and traffic conditions to avoid.

### [Use CalculateRouteMatrix](https://docs.aws.amazon.com/location/latest/developerguide/calculate-route-matrix-how-to.html)

In this section you learn how to use CalculateRouteMatrix to find efficient routes for multiple origins and destinations.

- [Calculate the route matrix for multiple origins and destinations](https://docs.aws.amazon.com/location/latest/developerguide/calculate-route-matrix-distance.html): The CalculateRouteMatrix API calculates routes and provides travel time and travel distance for each combination of origins and destinations.
- [Calculate route matrix with avoidance](https://docs.aws.amazon.com/location/latest/developerguide/calculate-route-matrix-with-avoidance.html): The CalculateRouteMatrix API computes routes and returns travel time and distance from each origin to each destination in the specified lists.

### [Use OptimizeWaypoints](https://docs.aws.amazon.com/location/latest/developerguide/optimize-waypoints-how-to.html)

Learn how to use OptimizeWaypoints to find the best routes for minimizing travel time or distance.

- [Optimize waypoints for a route](https://docs.aws.amazon.com/location/latest/developerguide/optimize-waypoints.html): The OptimizeWaypoints API calculates the most efficient route between a series of waypoints, minimizing either travel time or total distance.
- [Optimize waypoints for a route with traffic awareness](https://docs.aws.amazon.com/location/latest/developerguide/optimize-waypoints-traffic-awareness.html): The OptimizeWaypoints API calculates the optimal route between multiple waypoints to minimize travel time or total distance.
- [Optimize waypoints for a route with access hours awareness](https://docs.aws.amazon.com/location/latest/developerguide/optimize-waypoints-access-hours.html): The OptimizeWaypoints API also calculates the optimal route between a set of waypoints, with the goal of minimizing either the travel time or the total distance covered.

### [Use SnapToRoads](https://docs.aws.amazon.com/location/latest/developerguide/snap-to-roads-how-to.html)

Learn how to use SnapToRoads with examples.

- [Match GPS traces to road network](https://docs.aws.amazon.com/location/latest/developerguide/how-to-match-gps-traces.html): The SnapToRoads API allows you to match GPS traces onto the road network.

### [Manage costs and usage](https://docs.aws.amazon.com/location/latest/developerguide/routes-whats-next.html)

Learn how to manage your Amazon Location routes costs and usage.

- [Best Practices](https://docs.aws.amazon.com/location/latest/developerguide/routes-best-practices.html): This section covers best practices for using compression and choosing between Simple (GeoJSON) and FlexiblePolyline formats when interacting with the API, providing guidance on optimizing performance, bandwidth, and data handling.
- [Routes pricing](https://docs.aws.amazon.com/location/latest/developerguide/routes-pricing.html): The price for the Routes APIs is based on the number of routes calculated in response.
- [Routes Quota and Usage](https://docs.aws.amazon.com/location/latest/developerguide/routes-quota-usage.html): Amazon Location Service sets default quotas for APIs to help manage service capacity, which can be viewed in the AWS service quotas management console.


## [Geofences](https://docs.aws.amazon.com/location/latest/developerguide/geofences.html)

- [Geofence concepts](https://docs.aws.amazon.com/location/latest/developerguide/geofence-components.html): This section describes some common geofence concepts, including common terminology and how to manage geofences.
- [Get started](https://docs.aws.amazon.com/location/latest/developerguide/geofence-gs.html): Geofences are powerful tools for defining geographic boundaries and triggering actions based on location updates.

### [How to](https://docs.aws.amazon.com/location/latest/developerguide/geofence-how-to.html)

This section provides step-by-step guidance for working with geofence-related tasks in Amazon Location.

- [Evaluate device positions against geofences](https://docs.aws.amazon.com/location/latest/developerguide/evaluate-geofences.html): There are two ways to evaluate positions against geofences to generate geofence events:
- [React to events with EventBridge](https://docs.aws.amazon.com/location/latest/developerguide/location-events.html): Use Amazon EventBridge to initiate automated actions for Amazon Location Service events.
- [Manage resources](https://docs.aws.amazon.com/location/latest/developerguide/managing-geofence-collections.html): Manage your geofence collections using the Amazon Location console, the AWS CLI, or the Amazon Location APIs.

### [Manage costs and usage](https://docs.aws.amazon.com/location/latest/developerguide/geofence-whats-next.html)

Learn how to manage your Amazon Location geofence costs and usage.

- [Pricing](https://docs.aws.amazon.com/location/latest/developerguide/geofence-price.html): For pricing information for tracking and geofencing APIs, see the Amazon Location Service pricing page.
- [Quotas and usage](https://docs.aws.amazon.com/location/latest/developerguide/geofence-quotas.html): This topic provides a summary of rate limits and quotas for Amazon Location Service Geofences.


## [Trackers](https://docs.aws.amazon.com/location/latest/developerguide/trackers.html)

- [Tracker concepts](https://docs.aws.amazon.com/location/latest/developerguide/tracking-components.html): This section details common trackers concepts.

### [Get started](https://docs.aws.amazon.com/location/latest/developerguide/start-tracking.html)

This section provides a comprehensive guide to creating and using trackers with Amazon Location.

- [Create a tracker](https://docs.aws.amazon.com/location/latest/developerguide/start-create-tracker.html): Create a tracker resource to store and process position updates from your devices.
- [Create an unauthenticated identity pool](https://docs.aws.amazon.com/location/latest/developerguide/tracking-identity-pool.html): Once you create a tracker resource and you're ready to begin evaluating device positions against geofences, choose how you would authenticate your requests:
- [Update your tracker with a device position](https://docs.aws.amazon.com/location/latest/developerguide/send-location-updates.html): To track your devices, you can post device position updates to your tracker.
- [Get a device's location history](https://docs.aws.amazon.com/location/latest/developerguide/get-location-history.html): Your Amazon Location tracker resource maintains the location history of all your tracked devices for a period of 30 days.
- [List your device positions](https://docs.aws.amazon.com/location/latest/developerguide/list-device-positions.html): You can view a list device positions for a tracker using the AWS CLI, or the Amazon Location APIs, with the ListDevicePositions API.

### [How to](https://docs.aws.amazon.com/location/latest/developerguide/tracker-how-to.html)

Learn how to use Amazon Location trackers.

- [Verify positions](https://docs.aws.amazon.com/location/latest/developerguide/verify-device-positions.html): To check the integrity of a device position use the VerifyDevicePosition API.
- [Link to a geofence collection](https://docs.aws.amazon.com/location/latest/developerguide/associate-consumer.html): Now that you have a geofence collection and a tracker, you can link them together so that location updates are automatically evaluated against all of your geofences.

### [Track using AWS IoT and MQTT](https://docs.aws.amazon.com/location/latest/developerguide/tracking-using-mqtt.html)

Use MQTT for tracking in Amazon Location Service, using AWS IoT Core.

- [Use AWS Lambda with MQTT](https://docs.aws.amazon.com/location/latest/developerguide/tracking-using-mqtt-with-lambda.html): While using AWS Lambda is no longer required when sending device location data to Amazon Location for tracking, you may still want to use Lambda in some cases.
- [Manage trackers](https://docs.aws.amazon.com/location/latest/developerguide/managing-trackers.html): You can manage your trackers using the Amazon Location console, the AWS CLI, or the Amazon Location APIs.

### [Manage costs and usage](https://docs.aws.amazon.com/location/latest/developerguide/trackers-next-steps.html)

Learn how to manage your Amazon Location trackers costs and usage.

- [Pricing](https://docs.aws.amazon.com/location/latest/developerguide/trackers-pricing.html): For pricing information for tracking and geofencing APIs, see the Amazon Location Service pricing page.
- [Quotas and usage](https://docs.aws.amazon.com/location/latest/developerguide/trackers-quotas.html): This topic provides a summary of rate limits and quotas for Amazon Location Service trackers.


## [Developer tools](https://docs.aws.amazon.com/location/latest/developerguide/developer-tools.html)

### [SDKs and frameworks](https://docs.aws.amazon.com/location/latest/developerguide/dev-sdks.html)

Information on frameworks, SDKs for using Amazon Location Service .

### [Developer tutorials](https://docs.aws.amazon.com/location/latest/developerguide/sdk-how-to.html)

Use this section to learn how to use various aspects of the Amazon Location Service SDK.

- [Use authentication helpers](https://docs.aws.amazon.com/location/latest/developerguide/how-to-auth-helper.html): This section provides additional information about authentication helpers.
- [Use MapLibre Geocoder GL plugin](https://docs.aws.amazon.com/location/latest/developerguide/dev-maplibre-geocoder.html): The Amazon Location MapLibre geocoder plugin is designed to make it easier for you to incorporate Amazon Location functionality into your JavaScript applications, when working with map rendering and geocoding using the maplibre-gl-geocoder library.
- [Use Tracking SDKs](https://docs.aws.amazon.com/location/latest/developerguide/dev-tracking-sdk.html): This topic provides information about how to use Tracking SDKs.
- [Use MapLibre tools](https://docs.aws.amazon.com/location/latest/developerguide/dev-maplibre.html): MapLibre is primarily a rendering engine for displaying maps in a web or mobile application.
- [SDKs by language](https://docs.aws.amazon.com/location/latest/developerguide/dev-by-language.html)
- [Map Rendering SDK by language](https://docs.aws.amazon.com/location/latest/developerguide/map-rendering-by-language.html): We recommend rendering Amazon Location Service maps using the MapLibre rendering engine.
- [Address Form SDK](https://docs.aws.amazon.com/location/latest/developerguide/address-form-sdk.html): Learn how to use the Address Form SDK to build intelligent address forms with autofill capabilities using Amazon Location Service.
- [Examples and Learning Resources](https://docs.aws.amazon.com/location/latest/developerguide/demos-samples.html): This topic provides links and details about our available demos and sample projects.


## [Integrate with AWS](https://docs.aws.amazon.com/location/latest/developerguide/integration.html)

### [Resource Management](https://docs.aws.amazon.com/location/latest/developerguide/resource-management.html)

Resource management provides tools and processes to manage quotas, organize resources with tags, control costs, and automate resource creation using AWS CloudFormation.

- [Manage quotas](https://docs.aws.amazon.com/location/latest/developerguide/manage-quotas.html): Service Quotas console allows you to request quota increases or decrease quota for adjustable quotas.
- [Manage resources with Tags](https://docs.aws.amazon.com/location/latest/developerguide/manage-resources.html): Use resource tagging in Amazon Location to create tags to categorize your resources by purpose, owner, environment, or criteria.
- [Manage billing and costs](https://docs.aws.amazon.com/location/latest/developerguide/manage-billing.html): AWS Billing and Cost Management is a web service that provides features that helps you pay your bills and optimize your costs.
- [Create resources with AWS CloudFormation](https://docs.aws.amazon.com/location/latest/developerguide/cloudformation.html): Amazon Location Service is integrated with CloudFormation, a service that helps you to model and set up your AWS resources so that you can spend less time creating and managing your resources and infrastructure.

### [Monitoring and Auditing](https://docs.aws.amazon.com/location/latest/developerguide/monitoring-auditing.html)

Monitoring and Auditing provides capabilities to track, monitor, and log activities in your Amazon Location Services environment.

- [Monitor with Amazon CloudWatch](https://docs.aws.amazon.com/location/latest/developerguide/cloudwatch.html): Monitor Amazon Location Service to maintain reliability, availability, and performance.
- [Monitor and log with AWS CloudTrail](https://docs.aws.amazon.com/location/latest/developerguide/cloudtrail.html): Describes logging Amazon Location Service with AWS CloudTrail.
- [Best practices](https://docs.aws.amazon.com/location/latest/developerguide/integration-best-practice.html): The following are a few best practices for integrating with Amazon Location Service.


## [Security](https://docs.aws.amazon.com/location/latest/developerguide/security.html)

### [Data protection](https://docs.aws.amazon.com/location/latest/developerguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon Location Service.

- [Data privacy](https://docs.aws.amazon.com/location/latest/developerguide/data-privacy.html): With Amazon Location Service, you retain control of your organizationâs data.
- [Data retention](https://docs.aws.amazon.com/location/latest/developerguide/data-retention.html): The following characteristics relate to how Amazon Location collects and stores data for the service:
- [Data at rest encryption](https://docs.aws.amazon.com/location/latest/developerguide/encryption-at-rest.html): Amazon Location Service provides encryption by default to protect sensitive customer data at rest using AWS owned encryption keys.
- [Data in transit encryption](https://docs.aws.amazon.com/location/latest/developerguide/encryption-in-transit.html): Amazon Location protects data in transit, as it travels to and from the service, by automatically encrypting all inter-network data using the Transport Layer Security (TLS) 1.2 encryption protocol.

### [Incident response](https://docs.aws.amazon.com/location/latest/developerguide/incident-response.html)

Learn about security incident response within Amazon Location Service.

- [Logging and Monitoring](https://docs.aws.amazon.com/location/latest/developerguide/security-logging-and-monitoring.html): Learn how Amazon Location Service isolates service traffic.
- [Compliance validation](https://docs.aws.amazon.com/location/latest/developerguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/location/latest/developerguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon Location Service features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/location/latest/developerguide/infrastructure-security.html): Learn how Amazon Location Service isolates service traffic.
- [AWS PrivateLink for Amazon Location](https://docs.aws.amazon.com/location/latest/developerguide/privatelink-interface-endpoints.html): This section provides information about using AWS PrivateLink for Amazon Location.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/location/latest/developerguide/vulnerability-analysis-and-management.html): Configuration and IT controls are a shared responsibility between AWS and you, our customer.
- [Confused deputy prevention](https://docs.aws.amazon.com/location/latest/developerguide/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
- [Best practices](https://docs.aws.amazon.com/location/latest/developerguide/best-practices.html): This topic provides recommendations for using Amazon Location Service.
