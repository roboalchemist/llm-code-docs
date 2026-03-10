# Source: https://docs.aws.amazon.com/location/previous/APIReference/llms.txt

# Amazon Location Service API Reference

> With Amazon Location Service API, you can securely add maps, points of interest, geocoding, geofences, and tracking to your applications.

- [Welcome](https://docs.aws.amazon.com/location/previous/APIReference/welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/location/previous/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/location/previous/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/location/previous/APIReference/API_Operations.html)

### [Maps](https://docs.aws.amazon.com/location/previous/APIReference/API_Operations-Maps.html)

The following actions are supported for Maps:

- [CreateMap](https://docs.aws.amazon.com/location/previous/APIReference/API_CreateMap.html)
- [DeleteMap](https://docs.aws.amazon.com/location/previous/APIReference/API_DeleteMap.html)
- [DescribeMap](https://docs.aws.amazon.com/location/previous/APIReference/API_DescribeMap.html)
- [GetMapGlyphs](https://docs.aws.amazon.com/location/previous/APIReference/API_GetMapGlyphs.html)
- [GetMapSprites](https://docs.aws.amazon.com/location/previous/APIReference/API_GetMapSprites.html)
- [GetMapStyleDescriptor](https://docs.aws.amazon.com/location/previous/APIReference/API_GetMapStyleDescriptor.html)
- [GetMapTile](https://docs.aws.amazon.com/location/previous/APIReference/API_GetMapTile.html)
- [ListMaps](https://docs.aws.amazon.com/location/previous/APIReference/API_ListMaps.html)
- [UpdateMap](https://docs.aws.amazon.com/location/previous/APIReference/API_UpdateMap.html)

### [Places](https://docs.aws.amazon.com/location/previous/APIReference/API_Operations-Places.html)

The following actions are supported for Places:

- [CreatePlaceIndex](https://docs.aws.amazon.com/location/previous/APIReference/API_CreatePlaceIndex.html)
- [DeletePlaceIndex](https://docs.aws.amazon.com/location/previous/APIReference/API_DeletePlaceIndex.html)
- [DescribePlaceIndex](https://docs.aws.amazon.com/location/previous/APIReference/API_DescribePlaceIndex.html)
- [GetPlace](https://docs.aws.amazon.com/location/previous/APIReference/API_GetPlace.html)
- [ListPlaceIndexes](https://docs.aws.amazon.com/location/previous/APIReference/API_ListPlaceIndexes.html)
- [SearchPlaceIndexForPosition](https://docs.aws.amazon.com/location/previous/APIReference/API_SearchPlaceIndexForPosition.html)
- [SearchPlaceIndexForSuggestions](https://docs.aws.amazon.com/location/previous/APIReference/API_SearchPlaceIndexForSuggestions.html)
- [SearchPlaceIndexForText](https://docs.aws.amazon.com/location/previous/APIReference/API_SearchPlaceIndexForText.html)
- [UpdatePlaceIndex](https://docs.aws.amazon.com/location/previous/APIReference/API_UpdatePlaceIndex.html)

### [Routes](https://docs.aws.amazon.com/location/previous/APIReference/API_Operations-Routes.html)

The following actions are supported for Routes:

- [CalculateRoute](https://docs.aws.amazon.com/location/previous/APIReference/API_CalculateRoute.html)
- [CalculateRouteMatrix](https://docs.aws.amazon.com/location/previous/APIReference/API_CalculateRouteMatrix.html)
- [CreateRouteCalculator](https://docs.aws.amazon.com/location/previous/APIReference/API_CreateRouteCalculator.html)
- [DeleteRouteCalculator](https://docs.aws.amazon.com/location/previous/APIReference/API_DeleteRouteCalculator.html)
- [DescribeRouteCalculator](https://docs.aws.amazon.com/location/previous/APIReference/API_DescribeRouteCalculator.html)
- [ListRouteCalculators](https://docs.aws.amazon.com/location/previous/APIReference/API_ListRouteCalculators.html)
- [UpdateRouteCalculator](https://docs.aws.amazon.com/location/previous/APIReference/API_UpdateRouteCalculator.html)

### [Geofences](https://docs.aws.amazon.com/location/previous/APIReference/API_Operations-Geofences.html)

The following actions are supported for Geofences:

- [BatchDeleteGeofence](https://docs.aws.amazon.com/location/previous/APIReference/API_BatchDeleteGeofence.html): Deletes a batch of geofences from a geofence collection.
- [BatchEvaluateGeofences](https://docs.aws.amazon.com/location/previous/APIReference/API_BatchEvaluateGeofences.html): Evaluates device positions against the geofence geometries from a given geofence collection.
- [BatchPutGeofence](https://docs.aws.amazon.com/location/previous/APIReference/API_BatchPutGeofence.html): A batch request for storing geofence geometries into a given geofence collection, or updates the geometry of an existing geofence if a geofence ID is included in the request.
- [CreateGeofenceCollection](https://docs.aws.amazon.com/location/previous/APIReference/API_CreateGeofenceCollection.html): Creates a geofence collection, which manages and stores geofences.
- [DeleteGeofenceCollection](https://docs.aws.amazon.com/location/previous/APIReference/API_DeleteGeofenceCollection.html): Deletes a geofence collection from your AWS account.
- [DescribeGeofenceCollection](https://docs.aws.amazon.com/location/previous/APIReference/API_DescribeGeofenceCollection.html): Retrieves the geofence collection details.
- [ForecastGeofenceEvents](https://docs.aws.amazon.com/location/previous/APIReference/API_ForecastGeofenceEvents.html): This action forecasts future geofence events that are likely to occur within a specified time horizon if a device continues moving at its current speed.
- [GetGeofence](https://docs.aws.amazon.com/location/previous/APIReference/API_GetGeofence.html): Retrieves the geofence details from a geofence collection.
- [ListGeofenceCollections](https://docs.aws.amazon.com/location/previous/APIReference/API_ListGeofenceCollections.html): Lists geofence collections in your AWS account.
- [ListGeofences](https://docs.aws.amazon.com/location/previous/APIReference/API_ListGeofences.html): Lists geofences stored in a given geofence collection.
- [PutGeofence](https://docs.aws.amazon.com/location/previous/APIReference/API_PutGeofence.html): Stores a geofence geometry in a given geofence collection, or updates the geometry of an existing geofence if a geofence ID is included in the request.
- [UpdateGeofenceCollection](https://docs.aws.amazon.com/location/previous/APIReference/API_UpdateGeofenceCollection.html): Updates the specified properties of a given geofence collection.

### [Trackers](https://docs.aws.amazon.com/location/previous/APIReference/API_Operations-Trackers.html)

The following actions are supported for Trackers:

- [AssociateTrackerConsumer](https://docs.aws.amazon.com/location/previous/APIReference/API_AssociateTrackerConsumer.html): Creates an association between a geofence collection and a tracker resource.
- [BatchDeleteDevicePositionHistory](https://docs.aws.amazon.com/location/previous/APIReference/API_BatchDeleteDevicePositionHistory.html): Deletes the position history of one or more devices from a tracker resource.
- [BatchGetDevicePosition](https://docs.aws.amazon.com/location/previous/APIReference/API_BatchGetDevicePosition.html): Lists the latest device positions for requested devices.
- [BatchUpdateDevicePosition](https://docs.aws.amazon.com/location/previous/APIReference/API_BatchUpdateDevicePosition.html): Uploads position update data for one or more devices to a tracker resource (up to 10 devices per batch).
- [CreateTracker](https://docs.aws.amazon.com/location/previous/APIReference/API_CreateTracker.html): Creates a tracker resource in your AWS account, which lets you retrieve current and historical location of devices.
- [DeleteTracker](https://docs.aws.amazon.com/location/previous/APIReference/API_DeleteTracker.html): Deletes a tracker resource from your AWS account.
- [DescribeTracker](https://docs.aws.amazon.com/location/previous/APIReference/API_DescribeTracker.html): Retrieves the tracker resource details.
- [DisassociateTrackerConsumer](https://docs.aws.amazon.com/location/previous/APIReference/API_DisassociateTrackerConsumer.html): Removes the association between a tracker resource and a geofence collection.
- [GetDevicePosition](https://docs.aws.amazon.com/location/previous/APIReference/API_GetDevicePosition.html): Retrieves a device's most recent position according to its sample time.
- [GetDevicePositionHistory](https://docs.aws.amazon.com/location/previous/APIReference/API_GetDevicePositionHistory.html): Retrieves the device position history from a tracker resource within a specified range of time.
- [ListDevicePositions](https://docs.aws.amazon.com/location/previous/APIReference/API_ListDevicePositions.html): A batch request to retrieve all device positions.
- [ListTrackerConsumers](https://docs.aws.amazon.com/location/previous/APIReference/API_ListTrackerConsumers.html): Lists geofence collections currently associated to the given tracker resource.
- [ListTrackers](https://docs.aws.amazon.com/location/previous/APIReference/API_ListTrackers.html): Lists tracker resources in your AWS account.
- [UpdateTracker](https://docs.aws.amazon.com/location/previous/APIReference/API_UpdateTracker.html): Updates the specified properties of a given tracker resource.
- [VerifyDevicePosition](https://docs.aws.amazon.com/location/previous/APIReference/API_VerifyDevicePosition.html): Verifies the integrity of the device's position by determining if it was reported behind a proxy, and by comparing it to an inferred position estimated based on the device's state.

### [API keys](https://docs.aws.amazon.com/location/previous/APIReference/API_Operations-Keys.html)

The following actions are supported for API keys:

- [CreateKey](https://docs.aws.amazon.com/location/previous/APIReference/API_CreateKey.html): Creates an API key resource in your AWS account, which lets you grant actions for Amazon Location resources to the API key bearer.
- [DeleteKey](https://docs.aws.amazon.com/location/previous/APIReference/API_DeleteKey.html): Deletes the specified API key.
- [DescribeKey](https://docs.aws.amazon.com/location/previous/APIReference/API_DescribeKey.html): Retrieves the API key resource details.
- [ListKeys](https://docs.aws.amazon.com/location/previous/APIReference/API_ListKeys.html): Lists API key resources in your AWS account.
- [UpdateKey](https://docs.aws.amazon.com/location/previous/APIReference/API_UpdateKey.html): Updates the specified properties of a given API key resource.

### [Tags](https://docs.aws.amazon.com/location/previous/APIReference/API_Operations-Tags.html)

The following actions are supported for Tags:

- [ListTagsForResource](https://docs.aws.amazon.com/location/previous/APIReference/API_ListTagsForResource.html): Returns a list of tags that are applied to the specified Amazon Location resource.
- [TagResource](https://docs.aws.amazon.com/location/previous/APIReference/API_TagResource.html): Assigns one or more tags (key-value pairs) to the specified Amazon Location Service resource.
- [UntagResource](https://docs.aws.amazon.com/location/previous/APIReference/API_UntagResource.html): Removes one or more tags from the specified Amazon Location resource.


## [Data Types](https://docs.aws.amazon.com/location/previous/APIReference/API_Types.html)

### [Maps](https://docs.aws.amazon.com/location/previous/APIReference/API_Types_Maps.html)

The following data types are supported by Maps:

- [ListMapsResponseEntry](https://docs.aws.amazon.com/location/previous/APIReference/API_ListMapsResponseEntry.html): Contains details of an existing map resource in your AWS account.
- [MapConfiguration](https://docs.aws.amazon.com/location/previous/APIReference/API_MapConfiguration.html): Specifies the map tile style selected from an available provider.
- [MapConfigurationUpdate](https://docs.aws.amazon.com/location/previous/APIReference/API_MapConfigurationUpdate.html): Specifies the political view for the style.

### [Places](https://docs.aws.amazon.com/location/previous/APIReference/API_Types_Places.html)

The following data types are supported by Places:

- [DataSourceConfiguration](https://docs.aws.amazon.com/location/previous/APIReference/API_DataSourceConfiguration.html): Specifies the data storage option chosen for requesting Places.
- [ListPlaceIndexesResponseEntry](https://docs.aws.amazon.com/location/previous/APIReference/API_ListPlaceIndexesResponseEntry.html): A place index resource listed in your AWS account.
- [Place](https://docs.aws.amazon.com/location/previous/APIReference/API_Place.html): Contains details about addresses or points of interest that match the search criteria.
- [PlaceGeometry](https://docs.aws.amazon.com/location/previous/APIReference/API_PlaceGeometry.html): Places uses a point geometry to specify a location or a Place.
- [SearchForPositionResult](https://docs.aws.amazon.com/location/previous/APIReference/API_SearchForPositionResult.html): Contains a search result from a position search query that is run on a place index resource.
- [SearchForSuggestionsResult](https://docs.aws.amazon.com/location/previous/APIReference/API_SearchForSuggestionsResult.html): Contains a place suggestion resulting from a place suggestion query that is run on a place index resource.
- [SearchForTextResult](https://docs.aws.amazon.com/location/previous/APIReference/API_SearchForTextResult.html): Contains a search result from a text search query that is run on a place index resource.
- [SearchPlaceIndexForPositionSummary](https://docs.aws.amazon.com/location/previous/APIReference/API_SearchPlaceIndexForPositionSummary.html): A summary of the request sent by using SearchPlaceIndexForPosition.
- [SearchPlaceIndexForSuggestionsSummary](https://docs.aws.amazon.com/location/previous/APIReference/API_SearchPlaceIndexForSuggestionsSummary.html): A summary of the request sent by using SearchPlaceIndexForSuggestions.
- [SearchPlaceIndexForTextSummary](https://docs.aws.amazon.com/location/previous/APIReference/API_SearchPlaceIndexForTextSummary.html): A summary of the request sent by using SearchPlaceIndexForText.
- [TimeZone](https://docs.aws.amazon.com/location/previous/APIReference/API_TimeZone.html): Information about a time zone.

### [Routes](https://docs.aws.amazon.com/location/previous/APIReference/API_Types_Routes.html)

The following data types are supported by Routes:

- [CalculateRouteCarModeOptions](https://docs.aws.amazon.com/location/previous/APIReference/API_CalculateRouteCarModeOptions.html): Contains details about additional route preferences for requests that specify TravelMode as Car.
- [CalculateRouteMatrixSummary](https://docs.aws.amazon.com/location/previous/APIReference/API_CalculateRouteMatrixSummary.html): A summary of the calculated route matrix.
- [CalculateRouteSummary](https://docs.aws.amazon.com/location/previous/APIReference/API_CalculateRouteSummary.html): A summary of the calculated route.
- [CalculateRouteTruckModeOptions](https://docs.aws.amazon.com/location/previous/APIReference/API_CalculateRouteTruckModeOptions.html): Contains details about additional route preferences for requests that specify TravelMode as Truck.
- [Leg](https://docs.aws.amazon.com/location/previous/APIReference/API_Leg.html): Contains the calculated route's details for each path between a pair of positions.
- [LegGeometry](https://docs.aws.amazon.com/location/previous/APIReference/API_LegGeometry.html): Contains the geometry details for each path between a pair of positions.
- [ListRouteCalculatorsResponseEntry](https://docs.aws.amazon.com/location/previous/APIReference/API_ListRouteCalculatorsResponseEntry.html): A route calculator resource listed in your AWS account.
- [RouteMatrixEntry](https://docs.aws.amazon.com/location/previous/APIReference/API_RouteMatrixEntry.html): The result for the calculated route of one DeparturePosition DestinationPosition pair.
- [RouteMatrixEntryError](https://docs.aws.amazon.com/location/previous/APIReference/API_RouteMatrixEntryError.html): An error corresponding to the calculation of a route between the DeparturePosition and DestinationPosition.
- [Step](https://docs.aws.amazon.com/location/previous/APIReference/API_Step.html): Represents an element of a leg within a route.
- [TruckDimensions](https://docs.aws.amazon.com/location/previous/APIReference/API_TruckDimensions.html): Contains details about the truck dimensions in the unit of measurement that you specify.
- [TruckWeight](https://docs.aws.amazon.com/location/previous/APIReference/API_TruckWeight.html): Contains details about the truck's weight specifications.

### [Geofences](https://docs.aws.amazon.com/location/previous/APIReference/API_Types_Geofences.html)

The following data types are supported by Geofences:

- [BatchDeleteGeofenceError](https://docs.aws.amazon.com/location/previous/APIReference/API_BatchDeleteGeofenceError.html): Contains error details for each geofence that failed to delete from the geofence collection.
- [BatchEvaluateGeofencesError](https://docs.aws.amazon.com/location/previous/APIReference/API_BatchEvaluateGeofencesError.html): Contains error details for each device that failed to evaluate its position against the geofences in a given geofence collection.
- [BatchPutGeofenceError](https://docs.aws.amazon.com/location/previous/APIReference/API_BatchPutGeofenceError.html): Contains error details for each geofence that failed to be stored in a given geofence collection.
- [BatchPutGeofenceRequestEntry](https://docs.aws.amazon.com/location/previous/APIReference/API_BatchPutGeofenceRequestEntry.html): Contains geofence geometry details.
- [BatchPutGeofenceSuccess](https://docs.aws.amazon.com/location/previous/APIReference/API_BatchPutGeofenceSuccess.html): Contains a summary of each geofence that was successfully stored in a given geofence collection.
- [ForecastedEvent](https://docs.aws.amazon.com/location/previous/APIReference/API_ForecastedEvent.html): A forecasted event represents a geofence event in relation to the requested device state, that may occur given the provided device state and time horizon.
- [ForecastGeofenceEventsDeviceState](https://docs.aws.amazon.com/location/previous/APIReference/API_ForecastGeofenceEventsDeviceState.html): The device's position and speed.
- [GeofenceGeometry](https://docs.aws.amazon.com/location/previous/APIReference/API_GeofenceGeometry.html): Contains the geofence geometry details.
- [ListGeofenceCollectionsResponseEntry](https://docs.aws.amazon.com/location/previous/APIReference/API_ListGeofenceCollectionsResponseEntry.html): Contains the geofence collection details.
- [ListGeofenceResponseEntry](https://docs.aws.amazon.com/location/previous/APIReference/API_ListGeofenceResponseEntry.html): Contains a list of geofences stored in a given geofence collection.

### [Trackers](https://docs.aws.amazon.com/location/previous/APIReference/API_Types_Trackers.html)

The following data types are supported by Trackers:

- [BatchDeleteDevicePositionHistoryError](https://docs.aws.amazon.com/location/previous/APIReference/API_BatchDeleteDevicePositionHistoryError.html): Contains the tracker resource details.
- [BatchGetDevicePositionError](https://docs.aws.amazon.com/location/previous/APIReference/API_BatchGetDevicePositionError.html): Contains error details for each device that didn't return a position.
- [BatchUpdateDevicePositionError](https://docs.aws.amazon.com/location/previous/APIReference/API_BatchUpdateDevicePositionError.html): Contains error details for each device that failed to update its position.
- [DevicePosition](https://docs.aws.amazon.com/location/previous/APIReference/API_DevicePosition.html): Contains the device position details.
- [DeviceState](https://docs.aws.amazon.com/location/previous/APIReference/API_DeviceState.html): The device's position, IP address, and Wi-Fi access points.
- [InferredState](https://docs.aws.amazon.com/location/previous/APIReference/API_InferredState.html): The inferred state of the device, given the provided position, IP address, cellular signals, and Wi-Fi- access points.
- [ListDevicePositionsResponseEntry](https://docs.aws.amazon.com/location/previous/APIReference/API_ListDevicePositionsResponseEntry.html): Contains the tracker resource details.
- [ListTrackersResponseEntry](https://docs.aws.amazon.com/location/previous/APIReference/API_ListTrackersResponseEntry.html): Contains the tracker resource details.
- [TrackingFilterGeometry](https://docs.aws.amazon.com/location/previous/APIReference/API_TrackingFilterGeometry.html): The geomerty used to filter device positions.
- [LteCellDetails](https://docs.aws.amazon.com/location/previous/APIReference/API_LteCellDetails.html): Details about the Long-Term Evolution (LTE) network.
- [CellSignals](https://docs.aws.amazon.com/location/previous/APIReference/API_CellSignals.html): The cellular network communication infrastructure that the device uses.
- [LteLocalId](https://docs.aws.amazon.com/location/previous/APIReference/API_LteLocalId.html): LTE local identification information (local ID).
- [LteNetworkMeasurements](https://docs.aws.amazon.com/location/previous/APIReference/API_LteNetworkMeasurements.html): LTE network measurements.
- [WiFiAccessPoint](https://docs.aws.amazon.com/location/previous/APIReference/API_WiFiAccessPoint.html): Wi-Fi access point.

### [API keys](https://docs.aws.amazon.com/location/previous/APIReference/API_Types_Keys.html)

The following data types are supported by API keys:

- [ApiKeyFilter](https://docs.aws.amazon.com/location/previous/APIReference/API_ApiKeyFilter.html): Options for filtering API keys.
- [ApiKeyRestrictions](https://docs.aws.amazon.com/location/previous/APIReference/API_ApiKeyRestrictions.html): API Restrictions on the allowed actions, resources, and referers for an API key resource.
- [ListKeysResponseEntry](https://docs.aws.amazon.com/location/previous/APIReference/API_ListKeysResponseEntry.html): An API key resource listed in your AWS account.

### [Common data types](https://docs.aws.amazon.com/location/previous/APIReference/API_Types_Common.html)

The following data types are common across Amazon Location Service:

- [BatchItemError](https://docs.aws.amazon.com/location/previous/APIReference/API_BatchItemError.html): Contains the batch request error details associated with the request.
- [Circle](https://docs.aws.amazon.com/location/previous/APIReference/API_Circle.html): A circle on the earth, as defined by a center point and a radius.
- [DevicePositionUpdate](https://docs.aws.amazon.com/location/previous/APIReference/API_DevicePositionUpdate.html): Contains the position update details for a device.
- [PositionalAccuracy](https://docs.aws.amazon.com/location/previous/APIReference/API_PositionalAccuracy.html): Defines the level of certainty of the position.
- [ValidationExceptionField](https://docs.aws.amazon.com/location/previous/APIReference/API_ValidationExceptionField.html): The input failed to meet the constraints specified by the AWS service in a specified field.
