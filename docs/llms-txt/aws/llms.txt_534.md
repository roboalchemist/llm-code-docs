# Source: https://docs.aws.amazon.com/location/latest/APIReference/llms.txt

# Amazon Location Service API Reference

## [Amazon Location Service Routes V2](https://docs.aws.amazon.com/location/latest/APIReference/Welcome_Amazon_Location_Service_Routes_V2.html)

With the Amazon Location Routes API you can calculate routes and estimate travel time based on up-to-date road network and live traffic information.

Calculate optimal travel routes and estimate travel times using up-to-date road network and traffic data. Key features include:

- Point-to-point routing with estimated travel time, distance, and turn-by-turn directions
- Multi-point route optimization to minimize travel time or distance
- Route matrices for efficient multi-destination planning
- Isoline calculations to determine reachable areas within specified time or distance thresholds
- Map-matching to align GPS traces with the road network

### Actions

- [CalculateIsolines](https://docs.aws.amazon.com/location/latest/APIReference/API_CalculateIsolines.html): Calculates areas that can be reached within specified time or distance thresholds from a given point.
- [CalculateRouteMatrix](https://docs.aws.amazon.com/location/latest/APIReference/API_CalculateRouteMatrix.html): Use CalculateRouteMatrix to compute results for all pairs of Origins to Destinations.
- [CalculateRoutes](https://docs.aws.amazon.com/location/latest/APIReference/API_CalculateRoutes.html): CalculateRoutes computes routes given the following required parameters: Origin and Destination.
- [OptimizeWaypoints](https://docs.aws.amazon.com/location/latest/APIReference/API_OptimizeWaypoints.html): OptimizeWaypoints calculates the optimal order to travel between a set of waypoints to minimize either the travel time or the distance travelled during the journey, based on road network restrictions and the traffic pattern data.
- [SnapToRoads](https://docs.aws.amazon.com/location/latest/APIReference/API_SnapToRoads.html): SnapToRoads matches GPS trace to roads most likely traveled on.

### Data Types

- [Circle](https://docs.aws.amazon.com/location/latest/APIReference/API_Circle.html): Geometry defined as a circle.
- [Corridor](https://docs.aws.amazon.com/location/latest/APIReference/API_Corridor.html): Geometry defined as a corridor - a LineString with a radius that defines the width of the corridor.
- [Isoline](https://docs.aws.amazon.com/location/latest/APIReference/API_Isoline.html): Represents a single reachable area calculated for a specific threshold.
- [IsolineAllowOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineAllowOptions.html): Special road types or features that should be considered available for routing.
- [IsolineAvoidanceArea](https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineAvoidanceArea.html): Defines an area to avoid when calculating routes.
- [IsolineAvoidanceAreaGeometry](https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineAvoidanceAreaGeometry.html): Defines an area to avoid during calculations using one of several supported geometry types.
- [IsolineAvoidanceOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineAvoidanceOptions.html): Specifies features of the road network to avoid when calculating reachable areas.
- [IsolineAvoidanceZoneCategory](https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineAvoidanceZoneCategory.html): Types of regulated zones that may affect routing.
- [IsolineCarOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineCarOptions.html): Vehicle characteristics and preferences that affect routing for passenger cars.
- [IsolineConnection](https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineConnection.html): Represents a segment of the transportation network that connects separate parts of a reachable area.
- [IsolineConnectionGeometry](https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineConnectionGeometry.html): Represents the geometry of connections between non-contiguous parts of an isoline.
- [IsolineDestinationOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineDestinationOptions.html): Options that control how the destination point is interpreted and matched to the road network when calculating reachable areas.
- [IsolineGranularityOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineGranularityOptions.html): Controls the detail level and smoothness of generated isolines.
- [IsolineMatchingOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineMatchingOptions.html): Controls how origin and destination points are matched to the road network when they don't fall exactly on a road.
- [IsolineOriginOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineOriginOptions.html): Options that control how the origin point is interpreted when calculating reachable areas.
- [IsolineScooterOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineScooterOptions.html): Vehicle characteristics that affect which roads and paths can be used when calculating reachable areas for scooters.
- [IsolineShapeGeometry](https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineShapeGeometry.html): Represents the shape of a reachable area.
- [IsolineSideOfStreetOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineSideOfStreetOptions.html): Controls how points are matched to specific sides of streets.
- [IsolineThresholds](https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineThresholds.html): Specifies the time or distance limits used to calculate reachable areas.
- [IsolineTrafficOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineTrafficOptions.html): Controls how real-time and historical traffic data is used when calculating reachable areas.
- [IsolineTrailerOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineTrailerOptions.html): Additional specifications when the vehicle includes one or more trailers.
- [IsolineTravelModeOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineTravelModeOptions.html): Mode-specific routing options that further refine how reachable areas are calculated.
- [IsolineTruckOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineTruckOptions.html): Vehicle characteristics and restrictions that affect which roads can be used when calculating reachable areas for trucks.
- [IsolineVehicleLicensePlate](https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineVehicleLicensePlate.html): License plate information used in regions where road access or routing restrictions are based on license plate numbers.
- [LocalizedString](https://docs.aws.amazon.com/location/latest/APIReference/API_LocalizedString.html): The localized string.
- [PolylineCorridor](https://docs.aws.amazon.com/location/latest/APIReference/API_PolylineCorridor.html): Geometry defined as an encoded corridor - an encoded polyline with a radius that defines the width of the corridor.
- [RoadSnapNotice](https://docs.aws.amazon.com/location/latest/APIReference/API_RoadSnapNotice.html): Notices provide information around factors that may have influenced snapping in a manner atypical to the standard use cases.
- [RoadSnapSnappedGeometry](https://docs.aws.amazon.com/location/latest/APIReference/API_RoadSnapSnappedGeometry.html): Interpolated geometry for the snapped route that is overlay-able onto a map.
- [RoadSnapSnappedTracePoint](https://docs.aws.amazon.com/location/latest/APIReference/API_RoadSnapSnappedTracePoint.html): TracePoints snapped onto the road network.
- [RoadSnapTracePoint](https://docs.aws.amazon.com/location/latest/APIReference/API_RoadSnapTracePoint.html): TracePoint indices for which the provided notice code corresponds to.
- [RoadSnapTrailerOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RoadSnapTrailerOptions.html): Trailer options corresponding to the vehicle.
- [RoadSnapTravelModeOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RoadSnapTravelModeOptions.html): Travel mode related options for the provided travel mode.
- [RoadSnapTruckOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RoadSnapTruckOptions.html): Travel mode options when the provided travel mode is "Truck".
- [Route](https://docs.aws.amazon.com/location/latest/APIReference/API_Route.html): The route.
- [RouteAllowOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteAllowOptions.html): Features that are allowed while calculating a route.
- [RouteAvoidanceArea](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteAvoidanceArea.html): Areas to be avoided.
- [RouteAvoidanceAreaGeometry](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteAvoidanceAreaGeometry.html): Geometry of the area to be avoided.
- [RouteAvoidanceOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteAvoidanceOptions.html): Specifies options for areas to avoid when calculating the route.
- [RouteAvoidanceZoneCategory](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteAvoidanceZoneCategory.html): Zone categories to be avoided.
- [RouteCarOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteCarOptions.html): Travel mode options when the provided travel mode is Car.
- [RouteContinueHighwayStepDetails](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteContinueHighwayStepDetails.html): Details related to the continue highway step.
- [RouteContinueStepDetails](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteContinueStepDetails.html): Details related to the continue step.
- [RouteDestinationOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteDestinationOptions.html): Options related to the destination.
- [RouteDriverOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteDriverOptions.html): Driver related options.
- [RouteDriverScheduleInterval](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteDriverScheduleInterval.html): Interval of the driver work-rest schedule.
- [RouteEmissionType](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteEmissionType.html): Type of the emission.
- [RouteEnterHighwayStepDetails](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteEnterHighwayStepDetails.html): Details related to the enter highway step.
- [RouteExclusionOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteExclusionOptions.html): Specifies strict exclusion options for the route calculation.
- [RouteExitStepDetails](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteExitStepDetails.html): Details related to the exit step.
- [RouteFerryAfterTravelStep](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteFerryAfterTravelStep.html): Steps of a leg that must be performed after the travel portion of the leg.
- [RouteFerryArrival](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteFerryArrival.html): Details corresponding to the arrival for the leg.
- [RouteFerryBeforeTravelStep](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteFerryBeforeTravelStep.html): Steps of a leg that must be performed before the travel portion of the leg.
- [RouteFerryDeparture](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteFerryDeparture.html): Details corresponding to the departure for the leg.
- [RouteFerryLegDetails](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteFerryLegDetails.html): FerryLegDetails is populated when the Leg type is Ferry, and provides additional information that is specific
- [RouteFerryNotice](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteFerryNotice.html): Notices are additional information returned that indicate issues that occurred during route calculation.
- [RouteFerryOverviewSummary](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteFerryOverviewSummary.html): Summarized details of the leg.
- [RouteFerryPlace](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteFerryPlace.html): Position provided in the request.
- [RouteFerrySpan](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteFerrySpan.html): Span computed for the requested SpanAdditionalFeatures.
- [RouteFerrySummary](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteFerrySummary.html): Summarized details for the leg including travel steps only.
- [RouteFerryTravelOnlySummary](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteFerryTravelOnlySummary.html): Summarized details for the leg including travel steps only.
- [RouteFerryTravelStep](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteFerryTravelStep.html): Steps of a leg that must be performed during the travel portion of the leg.
- [RouteKeepStepDetails](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteKeepStepDetails.html): Details that are specific to a Keep step.
- [RouteLeg](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteLeg.html): A leg is a section of a route from one waypoint to the next.
- [RouteLegGeometry](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteLegGeometry.html): The returned Route leg geometry.
- [RouteMajorRoadLabel](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMajorRoadLabel.html): Important labels including names and route numbers that differentiate the current route from the alternatives presented.
- [RouteMatchingOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatchingOptions.html): Options related to route matching.
- [RouteMatrixAllowOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixAllowOptions.html): Allow Options related to the route matrix.
- [RouteMatrixAutoCircle](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixAutoCircle.html): Provides the circle that was used while calculating the route.
- [RouteMatrixAvoidanceArea](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixAvoidanceArea.html): Area to be avoided.
- [RouteMatrixAvoidanceAreaGeometry](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixAvoidanceAreaGeometry.html): Geometry of the area to be avoided.
- [RouteMatrixAvoidanceOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixAvoidanceOptions.html): Specifies options for areas to avoid when calculating the route.
- [RouteMatrixAvoidanceZoneCategory](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixAvoidanceZoneCategory.html): Zone categories to be avoided.
- [RouteMatrixBoundary](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixBoundary.html): Boundary within which the matrix is to be calculated.
- [RouteMatrixBoundaryGeometry](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixBoundaryGeometry.html): Geometry of the routing boundary.
- [RouteMatrixCarOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixCarOptions.html): Travel mode options when the provided travel mode is Car.
- [RouteMatrixDestination](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixDestination.html): The route destination.
- [RouteMatrixDestinationOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixDestinationOptions.html): Options related to the destination.
- [RouteMatrixEntry](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixEntry.html): The calculated route matrix containing the results for all pairs of Origins to Destination positions.
- [RouteMatrixExclusionOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixExclusionOptions.html): Specifies strict exclusion options for the route calculation.
- [RouteMatrixMatchingOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixMatchingOptions.html): Matching options.
- [RouteMatrixOrigin](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixOrigin.html): The start position for the route in World Geodetic System (WGS 84) format: [longitude, latitude].
- [RouteMatrixOriginOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixOriginOptions.html): Origin related options.
- [RouteMatrixScooterOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixScooterOptions.html): Travel mode options when the provided travel mode is Scooter
- [RouteMatrixSideOfStreetOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixSideOfStreetOptions.html): Options to configure matching the provided position to a side of the street.
- [RouteMatrixTrafficOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixTrafficOptions.html): Traffic related options.
- [RouteMatrixTrailerOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixTrailerOptions.html): Trailer options corresponding to the vehicle.
- [RouteMatrixTravelModeOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixTravelModeOptions.html): Travel mode related options for the provided travel mode.
- [RouteMatrixTruckOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixTruckOptions.html): Travel mode options when the provided travel mode is "Truck"
- [RouteMatrixVehicleLicensePlate](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixVehicleLicensePlate.html): The vehicle License Plate.
- [RouteNoticeDetailRange](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteNoticeDetailRange.html): Notice Detail that is a range.
- [RouteNumber](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteNumber.html): The route number.
- [RouteOriginOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteOriginOptions.html): Origin related options.
- [RoutePassThroughPlace](https://docs.aws.amazon.com/location/latest/APIReference/API_RoutePassThroughPlace.html): The place where the waypoint is passed through and not treated as a stop.
- [RoutePassThroughWaypoint](https://docs.aws.amazon.com/location/latest/APIReference/API_RoutePassThroughWaypoint.html): If the waypoint should be treated as a stop.
- [RoutePedestrianArrival](https://docs.aws.amazon.com/location/latest/APIReference/API_RoutePedestrianArrival.html): Details corresponding to the arrival for a leg.
- [RoutePedestrianDeparture](https://docs.aws.amazon.com/location/latest/APIReference/API_RoutePedestrianDeparture.html): Details corresponding to the departure for a leg.
- [RoutePedestrianLegDetails](https://docs.aws.amazon.com/location/latest/APIReference/API_RoutePedestrianLegDetails.html): Details that are specific to a pedestrian leg.
- [RoutePedestrianNotice](https://docs.aws.amazon.com/location/latest/APIReference/API_RoutePedestrianNotice.html): Notices are additional information returned that indicate issues that occurred during route calculation.
- [RoutePedestrianOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RoutePedestrianOptions.html): Options related to the pedestrian.
- [RoutePedestrianOverviewSummary](https://docs.aws.amazon.com/location/latest/APIReference/API_RoutePedestrianOverviewSummary.html): Provides a summary of a pedestrian route step.
- [RoutePedestrianPlace](https://docs.aws.amazon.com/location/latest/APIReference/API_RoutePedestrianPlace.html): Place details corresponding to the arrival or departure.
- [RoutePedestrianSpan](https://docs.aws.amazon.com/location/latest/APIReference/API_RoutePedestrianSpan.html): Span computed for the requested SpanAdditionalFeatures.
- [RoutePedestrianSummary](https://docs.aws.amazon.com/location/latest/APIReference/API_RoutePedestrianSummary.html): Summarized details for the leg including before travel, travel and after travel steps.
- [RoutePedestrianTravelOnlySummary](https://docs.aws.amazon.com/location/latest/APIReference/API_RoutePedestrianTravelOnlySummary.html): Summarized details for the leg including travel steps.
- [RoutePedestrianTravelStep](https://docs.aws.amazon.com/location/latest/APIReference/API_RoutePedestrianTravelStep.html): Steps of a leg that must be performed during the travel portion of the leg.
- [RouteRampStepDetails](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteRampStepDetails.html): Details that are specific to a ramp step.
- [RouteResponseNotice](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteResponseNotice.html): Notices are additional information returned that indicate issues that occurred during route calculation.
- [RouteRoad](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteRoad.html): The road on the route.
- [RouteRoundaboutEnterStepDetails](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteRoundaboutEnterStepDetails.html): Details about the roundabout leg.
- [RouteRoundaboutExitStepDetails](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteRoundaboutExitStepDetails.html): Details about the roundabout step.
- [RouteRoundaboutPassStepDetails](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteRoundaboutPassStepDetails.html): Details about the step.
- [RouteScooterOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteScooterOptions.html): Travel mode options when the provided travel mode is Scooter
- [RouteSideOfStreetOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteSideOfStreetOptions.html): Options to configure matching the provided position to a side of the street.
- [RouteSignpost](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteSignpost.html): Sign post information of the action, applicable only for TurnByTurn steps.
- [RouteSignpostLabel](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteSignpostLabel.html): Labels presented on the sign post.
- [RouteSpanDynamicSpeedDetails](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteSpanDynamicSpeedDetails.html): Details about the dynamic speed.
- [RouteSpanSpeedLimitDetails](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteSpanSpeedLimitDetails.html): Details about the speed limit corresponding to the span.
- [RouteSummary](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteSummary.html): Summarized details for the leg including travel steps only.
- [RouteToll](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteToll.html): Provides details about toll information along a route, including the payment sites, applicable toll rates, toll systems, and the country associated with the toll collection.
- [RouteTollOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTollOptions.html): Options related to Tolls on a route.
- [RouteTollPass](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTollPass.html): Details if the toll rate can be a pass that supports multiple trips.
- [RouteTollPassValidityPeriod](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTollPassValidityPeriod.html): Period for which the pass is valid.
- [RouteTollPaymentSite](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTollPaymentSite.html): Locations or sites where the toll fare is collected.
- [RouteTollPrice](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTollPrice.html): The toll price.
- [RouteTollPriceSummary](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTollPriceSummary.html): Summary of the route and toll price.
- [RouteTollPriceValueRange](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTollPriceValueRange.html): Price range with a minimum and maximum value, if a range.
- [RouteTollRate](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTollRate.html): The toll rate.
- [RouteTollSummary](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTollSummary.html): The toll summary for the complete route.
- [RouteTollSystem](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTollSystem.html): Toll systems are authorities that collect payments for the toll.
- [RouteTrafficOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTrafficOptions.html): Traffic options for the route.
- [RouteTrailerOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTrailerOptions.html): Trailer options corresponding to the vehicle.
- [RouteTransponder](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTransponder.html): Transponders for which this toll can be applied.
- [RouteTravelModeOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTravelModeOptions.html): Travel mode related options for the provided travel mode.
- [RouteTruckOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTruckOptions.html): Travel mode options when the provided travel mode is "Truck"
- [RouteTurnStepDetails](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTurnStepDetails.html): Details related to the turn step.
- [RouteUTurnStepDetails](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteUTurnStepDetails.html): Details related to the U-turn step.
- [RouteVehicleArrival](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteVehicleArrival.html): Details corresponding to the arrival for a leg.
- [RouteVehicleDeparture](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteVehicleDeparture.html): Details corresponding to the departure for the leg.
- [RouteVehicleIncident](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteVehicleIncident.html): Incidents corresponding to this leg of the route.
- [RouteVehicleLegDetails](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteVehicleLegDetails.html): Steps of a leg that correspond to the travel portion of the leg.
- [RouteVehicleLicensePlate](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteVehicleLicensePlate.html): License plate information of the vehicle.
- [RouteVehicleNotice](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteVehicleNotice.html): Notices are additional information returned that indicate issues that occurred during route calculation.
- [RouteVehicleNoticeDetail](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteVehicleNoticeDetail.html): Additional details of the notice.
- [RouteVehicleOverviewSummary](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteVehicleOverviewSummary.html): Summarized details of the leg.
- [RouteVehiclePlace](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteVehiclePlace.html): Place details corresponding to the arrival or departure.
- [RouteVehicleSpan](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteVehicleSpan.html): Span computed for the requested SpanAdditionalFeatures.
- [RouteVehicleSummary](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteVehicleSummary.html): Summarized details of the route.
- [RouteVehicleTravelOnlySummary](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteVehicleTravelOnlySummary.html): Summarized details of the route.
- [RouteVehicleTravelStep](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteVehicleTravelStep.html): Steps of a leg that correspond to the travel portion of the leg.
- [RouteViolatedConstraints](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteViolatedConstraints.html): This property contains a summary of violated constraints.
- [RouteWaypoint](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteWaypoint.html): Waypoint between the Origin and Destination.
- [RouteWeightConstraint](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteWeightConstraint.html): The weight constraint for the route.
- [RouteZone](https://docs.aws.amazon.com/location/latest/APIReference/API_RouteZone.html): The zone.
- [ValidationExceptionField](https://docs.aws.amazon.com/location/latest/APIReference/API_ValidationExceptionField.html): The input fails to satisfy the constraints specified by the Amazon Location service.
- [WaypointOptimizationAccessHours](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationAccessHours.html): Access hours corresponding to when a destination can be visited.
- [WaypointOptimizationAccessHoursEntry](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationAccessHoursEntry.html): Hours of entry.
- [WaypointOptimizationAvoidanceArea](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationAvoidanceArea.html): The area to be avoided.
- [WaypointOptimizationAvoidanceAreaGeometry](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationAvoidanceAreaGeometry.html): Geometry of the area to be avoided.
- [WaypointOptimizationAvoidanceOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationAvoidanceOptions.html): Specifies options for areas to avoid.
- [WaypointOptimizationClusteringOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationClusteringOptions.html): Options for WaypointOptimizationClustering.
- [WaypointOptimizationConnection](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationConnection.html): This contains information such as distance and duration from one waypoint to the next waypoint in the sequence.
- [WaypointOptimizationDestinationOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationDestinationOptions.html): Destination related options.
- [WaypointOptimizationDriverOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationDriverOptions.html): Driver related options.
- [WaypointOptimizationDrivingDistanceOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationDrivingDistanceOptions.html): Driving distance related options.
- [WaypointOptimizationExclusionOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationExclusionOptions.html): Specifies strict exclusion options for the route calculation.
- [WaypointOptimizationFailedConstraint](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationFailedConstraint.html): The failed constraint.
- [WaypointOptimizationImpedingWaypoint](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationImpedingWaypoint.html): The impeding waypoint.
- [WaypointOptimizationOptimizedWaypoint](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationOptimizedWaypoint.html): The optimized waypoint.
- [WaypointOptimizationOriginOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationOriginOptions.html): Origin related options.
- [WaypointOptimizationPedestrianOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationPedestrianOptions.html): Options related to a pedestrian.
- [WaypointOptimizationRestCycleDurations](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationRestCycleDurations.html): Driver work-rest schedules defined by a short and long cycle.
- [WaypointOptimizationRestCycles](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationRestCycles.html): Resting phase of the cycle.
- [WaypointOptimizationRestProfile](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationRestProfile.html): Pre defined rest profiles for a driver schedule.
- [WaypointOptimizationSideOfStreetOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationSideOfStreetOptions.html): Options to configure matching the provided position to a side of the street.
- [WaypointOptimizationTimeBreakdown](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationTimeBreakdown.html): Time breakdown for the sequence.
- [WaypointOptimizationTrafficOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationTrafficOptions.html): Options related to traffic.
- [WaypointOptimizationTrailerOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationTrailerOptions.html): Trailer options corresponding to the vehicle.
- [WaypointOptimizationTravelModeOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationTravelModeOptions.html): Travel mode related options for the provided travel mode.
- [WaypointOptimizationTruckOptions](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationTruckOptions.html): Travel mode options when the provided travel mode is "Truck"
- [WaypointOptimizationWaypoint](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationWaypoint.html): Waypoint between the Origin and Destination.
- [WeightPerAxleGroup](https://docs.aws.amazon.com/location/latest/APIReference/API_WeightPerAxleGroup.html): Specifies the total weight for different axle group configurations.

## [Amazon Location Service Maps V2](https://docs.aws.amazon.com/location/latest/APIReference/Welcome_Amazon_Location_Service_Maps_V2.html)

Integrate high-quality base map data into your applications using [MapLibre](https://maplibre.org). Capabilities include:

- Access to comprehensive base map data, allowing you to tailor the map display to your specific needs.
- Multiple pre-designed map styles suited for various application types, such as navigation, logistics, or data visualization.
- Generation of static map images for scenarios where interactive maps aren't suitable, such as:
  - Embedding in emails or documents
  - Displaying in low-bandwidth environments
  - Creating printable maps
  - Enhancing application performance by reducing client-side rendering

### Actions

- [GetGlyphs](https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetGlyphs.html): GetGlyphs returns the map's glyphs.
- [GetSprites](https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetSprites.html): GetSprites returns the map's sprites.
- [GetStaticMap](https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetStaticMap.html): GetStaticMap provides high-quality static map images with customizable options.
- [GetStyleDescriptor](https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetStyleDescriptor.html): GetStyleDescriptor returns information about the style.
- [GetTile](https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetTile.html): GetTile returns a tile.

### Data Types

- [ValidationExceptionField](https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_ValidationExceptionField.html): The input fails to satisfy the constraints specified by the Amazon Location service.

## [Amazon Location Service Places V2](https://docs.aws.amazon.com/location/latest/APIReference/Welcome_Amazon_Location_Service_Places_V2.html)

The Places API enables powerful location search and geocoding capabilities for your applications, offering global coverage with rich, detailed information. Key features include:

- Forward and reverse geocoding for addresses and coordinates
- Comprehensive place searches with detailed information, including:
  - Business names and addresses
  - Contact information
  - Hours of operation
  - POI (Points of Interest) categories
  - Food types for restaurants
  - Chain affiliation for relevant businesses
- Global data coverage with a wide range of POI categories
- Regular data updates to ensure accuracy and relevance

### Actions

- [Autocomplete](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Autocomplete.html): Autocomplete completes potential places and addresses as the user types, based on the partial input.
- [Geocode](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Geocode.html): Geocode converts a textual address or place into geographic coordinates.
- [GetPlace](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_GetPlace.html): GetPlace finds a place by its unique ID.
- [ReverseGeocode](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_ReverseGeocode.html): ReverseGeocode converts geographic coordinates into a human-readable address or place.
- [SearchNearby](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SearchNearby.html): SearchNearby queries for points of interest within a radius from a central coordinates, returning place results with optional filters such as categories, business chains, food types and more.
- [SearchText](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SearchText.html): SearchText searches for geocode and place information.
- [Suggest](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Suggest.html): Suggest provides intelligent predictions or recommendations based on the user's input or context, such as relevant places, points of interest, query terms or search category.

### Data Types

- [AccessPoint](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_AccessPoint.html): Position of the access point represented by longitude and latitude for a vehicle.
- [AccessRestriction](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_AccessRestriction.html): Indicates if the access location is restricted.
- [Address](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Address.html): The place address.
- [AddressComponentMatchScores](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_AddressComponentMatchScores.html): Indicates how well the entire input matches the returned.
- [AddressComponentPhonemes](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_AddressComponentPhonemes.html): How to pronounce the various components of the address or place.
- [AutocompleteAddressHighlights](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_AutocompleteAddressHighlights.html): Describes how the parts of the response element matched the input query by returning the sections of the response which matched to input query terms.
- [AutocompleteFilter](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_AutocompleteFilter.html): Autocomplete structure which contains a set of inclusion/exclusion properties that results must possess in order to be returned as a result.
- [AutocompleteHighlights](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_AutocompleteHighlights.html): Describes how the parts of the response element matched the input query by returning the sections of the response which matched to input query terms.
- [AutocompleteResultItem](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_AutocompleteResultItem.html): A result matching the input query text.
- [BusinessChain](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_BusinessChain.html): A businesschain is a chain of businesses that belong to the same brand.
- [Category](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Category.html): Category of the Place returned.
- [ComponentMatchScores](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_ComponentMatchScores.html): Indicates how well the returned title and address components matches the input TextQuery.
- [ContactDetails](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_ContactDetails.html): Details related to contacts.
- [Contacts](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Contacts.html): A list of potential contact methods for the result/place.
- [Country](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Country.html): The alpha-2 or alpha-3 character code for the country that the results will be present in.
- [CountryHighlights](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_CountryHighlights.html): Indicates the starting and ending index of the country in the text query that match the found title.
- [FilterCircle](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_FilterCircle.html): The Circle that all results must be in.
- [FoodType](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_FoodType.html): List of Food types offered by this result.
- [GeocodeFilter](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_GeocodeFilter.html): Geocode structure which contains a set of inclusion/exclusion properties that results must possess in order to be returned as a result.
- [GeocodeParsedQuery](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_GeocodeParsedQuery.html): Parsed components in the provided QueryText.
- [GeocodeParsedQueryAddressComponents](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_GeocodeParsedQueryAddressComponents.html): Parsed address components in the provided QueryText.
- [GeocodeQueryComponents](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_GeocodeQueryComponents.html): A structured free text query allows you to search for places by the name or text representation of specific properties of the place.
- [GeocodeResultItem](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_GeocodeResultItem.html): The Geocoded result.
- [Highlight](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Highlight.html): Indicates the starting and ending index of the text query that match the found title.
- [Intersection](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Intersection.html): All Intersections that are near the provided address.
- [MatchScoreDetails](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_MatchScoreDetails.html): Details related to the match score.
- [OpeningHours](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_OpeningHours.html): List of opening hours objects.
- [OpeningHoursComponents](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_OpeningHoursComponents.html): Components of the opening hours object.
- [ParsedQueryComponent](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_ParsedQueryComponent.html): Parsed components in the provided QueryText.
- [ParsedQuerySecondaryAddressComponent](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_ParsedQuerySecondaryAddressComponent.html): Information about a secondary address component parsed from the query text.
- [PhonemeDetails](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_PhonemeDetails.html): The phoneme details.
- [PhonemeTranscription](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_PhonemeTranscription.html): How to pronounce the various components of the address or place.
- [PostalCodeDetails](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_PostalCodeDetails.html): Contains details about the postal code of the place or result.
- [QueryRefinement](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_QueryRefinement.html): Suggestions for refining individual query terms.
- [Region](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Region.html): The region or state results should be to be present in.
- [RegionHighlights](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_RegionHighlights.html): Indicates the starting and ending index of the region in the text query that match the found title.
- [RelatedPlace](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_RelatedPlace.html): Place that is related to the result item.
- [ReverseGeocodeFilter](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_ReverseGeocodeFilter.html): The included place types.
- [ReverseGeocodeResultItem](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_ReverseGeocodeResultItem.html): The returned location from the Reverse Geocode action.
- [SearchNearbyFilter](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SearchNearbyFilter.html): SearchNearby structure which contains a set of inclusion/exclusion properties that results must possess in order to be returned as a result.
- [SearchNearbyResultItem](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SearchNearbyResultItem.html): The search results of nearby places.
- [SearchTextFilter](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SearchTextFilter.html): SearchText structure which contains a set of inclusion/exclusion properties that results must possess in order to be returned as a result.
- [SearchTextResultItem](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SearchTextResultItem.html): The text search result.
- [SecondaryAddressComponent](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SecondaryAddressComponent.html): Components that correspond to secondary identifiers on an address.
- [SecondaryAddressComponentMatchScore](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SecondaryAddressComponentMatchScore.html): Match score for a secondary address component in the result.
- [StreetComponents](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_StreetComponents.html): Components of a street.
- [SubRegion](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SubRegion.html): The sub-region.
- [SubRegionHighlights](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SubRegionHighlights.html): Indicates the starting and ending index of the sub-region in the text query that match the found title.
- [SuggestAddressHighlights](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SuggestAddressHighlights.html): Describes how the parts of the textQuery matched the input query by returning the sections of the response which matched to textQuery terms.
- [SuggestFilter](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SuggestFilter.html): SuggestFilter structure which contains a set of inclusion/exclusion properties that results must possess in order to be returned as a result.
- [SuggestHighlights](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SuggestHighlights.html): Describes how the parts of the textQuery matched the input query by returning the sections of the response which matched to textQuery terms.
- [SuggestPlaceResult](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SuggestPlaceResult.html): The suggested place results.
- [SuggestQueryResult](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SuggestQueryResult.html): The suggested query results.
- [SuggestResultItem](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SuggestResultItem.html): The resulting item from the suggested query.
- [TimeZone](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_TimeZone.html): The time zone in which the place is located.
- [UspsZip](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_UspsZip.html): The USPS zip code.
- [UspsZipPlus4](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_UspsZipPlus4.html): The USPS zip+4 code.
- [ValidationExceptionField](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_ValidationExceptionField.html): The input fails to satisfy the constraints specified by the Amazon Location service.

## [Amazon Location Service Tagging](https://docs.aws.amazon.com/location/latest/APIReference/Welcome_Amazon_Location_Service_Tagging.html)

Use resource tagging in Amazon Location Service to create tags to categorize your resources by purpose, owner, environment, or criteria. Tagging your resources helps you manage, identify, organize, search, and filter your resources.

For more information about [tagging your Amazon Location resources](https://docs.aws.amazon.com/location/latest/developerguide/manage-resources.html), see the Amazon Location Service Developer Guide. It provides definitions, tutorials, code examples, and instructions about how to integrate Amazon Location features into your application.

### Actions

- [CreateKey](https://docs.aws.amazon.com/location/latest/APIReference/API_geotags_CreateKey.html): Creates an API key resource in your AWS account, which lets you grant actions for Amazon Location resources to the API key bearer.
- [DeleteKey](https://docs.aws.amazon.com/location/latest/APIReference/API_geotags_DeleteKey.html): Deletes the specified API key.
- [DescribeKey](https://docs.aws.amazon.com/location/latest/APIReference/API_geotags_DescribeKey.html): Retrieves the API key resource details.
- [ListKeys](https://docs.aws.amazon.com/location/latest/APIReference/API_geotags_ListKeys.html): Lists API key resources in your AWS account.
- [ListTagsForResource](https://docs.aws.amazon.com/location/latest/APIReference/API_geotags_ListTagsForResource.html): Returns a list of tags that are applied to the specified Amazon Location resource.
- [TagResource](https://docs.aws.amazon.com/location/latest/APIReference/API_geotags_TagResource.html): Assigns one or more tags (key-value pairs) to the specified Amazon Location Service resource.
- [UntagResource](https://docs.aws.amazon.com/location/latest/APIReference/API_geotags_UntagResource.html): Removes one or more tags from the specified Amazon Location resource.
- [UpdateKey](https://docs.aws.amazon.com/location/latest/APIReference/API_geotags_UpdateKey.html): Updates the specified properties of a given API key resource.

### Data Types

- [AndroidApp](https://docs.aws.amazon.com/location/latest/APIReference/API_geotags_AndroidApp.html): Unique identifying information for an Android app.
- [ApiKeyFilter](https://docs.aws.amazon.com/location/latest/APIReference/API_geotags_ApiKeyFilter.html): Options for filtering API keys.
- [ApiKeyRestrictions](https://docs.aws.amazon.com/location/latest/APIReference/API_geotags_ApiKeyRestrictions.html): API Restrictions on the allowed actions, resources, referers, Android apps, and Apple apps for an API key resource.
- [AppleApp](https://docs.aws.amazon.com/location/latest/APIReference/API_geotags_AppleApp.html): Unique identifying information for an Apple app (iOS, macOS, tvOS and watchOS).
- [ListKeysResponseEntry](https://docs.aws.amazon.com/location/latest/APIReference/API_geotags_ListKeysResponseEntry.html): An API key resource listed in your AWS account.
- [ValidationExceptionField](https://docs.aws.amazon.com/location/latest/APIReference/API_geotags_ValidationExceptionField.html)

## [Amazon Location Service Geofences](https://docs.aws.amazon.com/location/latest/APIReference/Welcome_Amazon_Location_Service_Geofences.html)

Amazon Location Geofences lets you give your application the ability to detect and act when a tracked device enters or exits a defined geographical boundary known as a geofence.

With Amazon Location Geofences, you can automatically send an exit or entry event to Amazon EventBridge when a geofence breach is detected. This lets you trigger downstream actions such as sending a notification to a target. For additional information, see the [Amazon Location Service Developer Guide](https://docs.aws.amazon.com/location/latest/developerguide/what-is.html). It provides definitions, tutorials, code examples, and instructions about how to integrate features into web or mobile apps.

### Actions

- [BatchDeleteGeofence](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_BatchDeleteGeofence.html): Deletes a batch of geofences from a geofence collection.
- [BatchEvaluateGeofences](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_BatchEvaluateGeofences.html): Evaluates device positions against the geofence geometries from a given geofence collection.
- [BatchPutGeofence](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_BatchPutGeofence.html): A batch request for storing geofence geometries into a given geofence collection, or updates the geometry of an existing geofence if a geofence ID is included in the request.
- [CreateGeofenceCollection](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_CreateGeofenceCollection.html): Creates a geofence collection, which manages and stores geofences.
- [DeleteGeofenceCollection](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_DeleteGeofenceCollection.html): Deletes a geofence collection from your AWS account.
- [DescribeGeofenceCollection](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_DescribeGeofenceCollection.html): Retrieves the geofence collection details.
- [ForecastGeofenceEvents](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_ForecastGeofenceEvents.html): This action forecasts future geofence events that are likely to occur within a specified time horizon if a device continues moving at its current speed.
- [GetGeofence](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_GetGeofence.html): Retrieves the geofence details from a geofence collection.
- [ListGeofenceCollections](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_ListGeofenceCollections.html): Lists geofence collections in your AWS account.
- [ListGeofences](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_ListGeofences.html): Lists geofences stored in a given geofence collection.
- [PutGeofence](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_PutGeofence.html): Stores a geofence geometry in a given geofence collection, or updates the geometry of an existing geofence if a geofence ID is included in the request.
- [UpdateGeofenceCollection](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_UpdateGeofenceCollection.html): Updates the specified properties of a given geofence collection.

### Data Types

- [BatchDeleteGeofenceError](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_BatchDeleteGeofenceError.html): Contains error details for each geofence that failed to delete from the geofence collection.
- [BatchEvaluateGeofencesError](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_BatchEvaluateGeofencesError.html): Contains error details for each device that failed to evaluate its position against the geofences in a given geofence collection.
- [BatchItemError](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_BatchItemError.html)
- [BatchPutGeofenceError](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_BatchPutGeofenceError.html): Contains error details for each geofence that failed to be stored in a given geofence collection.
- [BatchPutGeofenceRequestEntry](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_BatchPutGeofenceRequestEntry.html): Contains geofence geometry details.
- [BatchPutGeofenceSuccess](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_BatchPutGeofenceSuccess.html): Contains a summary of each geofence that was successfully stored in a given geofence collection.
- [Circle](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_Circle.html)
- [DevicePositionUpdate](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_DevicePositionUpdate.html)
- [ForecastedEvent](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_ForecastedEvent.html): A forecasted event represents a geofence event in relation to the requested device state, that may occur given the provided device state and time horizon.
- [ForecastGeofenceEventsDeviceState](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_ForecastGeofenceEventsDeviceState.html): The device's position and speed.
- [GeofenceGeometry](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_GeofenceGeometry.html): Contains the geofence geometry details.
- [ListGeofenceCollectionsResponseEntry](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_ListGeofenceCollectionsResponseEntry.html): Contains the geofence collection details.
- [ListGeofenceResponseEntry](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_ListGeofenceResponseEntry.html): Contains a list of geofences stored in a given geofence collection.
- [PositionalAccuracy](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_PositionalAccuracy.html)
- [ValidationExceptionField](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointGeofencing_ValidationExceptionField.html)

## [Amazon Location Service Trackers](https://docs.aws.amazon.com/location/latest/APIReference/Welcome_Amazon_Location_Service_Trackers.html)

Use trackers to store position updates for a collection of devices. The tracker can be used to query the devices' current location or location history. It stores the updates, but reduces storage space and visual noise by filtering the locations before storing them.

For more information, see the [Amazon Location Service Developer Guide](https://docs.aws.amazon.com/location/latest/developerguide/what-is.html). It provides definitions, tutorials, code examples, and instructions about how to integrate Amazon Location features into your application.

### Actions

- [AssociateTrackerConsumer](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_AssociateTrackerConsumer.html): Creates an association between a geofence collection and a tracker resource.
- [BatchDeleteDevicePositionHistory](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_BatchDeleteDevicePositionHistory.html): Deletes the position history of one or more devices from a tracker resource.
- [BatchGetDevicePosition](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_BatchGetDevicePosition.html): Lists the latest device positions for requested devices.
- [BatchUpdateDevicePosition](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_BatchUpdateDevicePosition.html): Uploads position update data for one or more devices to a tracker resource (up to 10 devices per batch).
- [CreateTracker](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_CreateTracker.html): Creates a tracker resource in your AWS account, which lets you retrieve current and historical location of devices.
- [DeleteTracker](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_DeleteTracker.html): Deletes a tracker resource from your AWS account.
- [DescribeTracker](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_DescribeTracker.html): Retrieves the tracker resource details.
- [DisassociateTrackerConsumer](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_DisassociateTrackerConsumer.html): Removes the association between a tracker resource and a geofence collection.
- [GetDevicePosition](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_GetDevicePosition.html): Retrieves a device's most recent position according to its sample time.
- [GetDevicePositionHistory](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_GetDevicePositionHistory.html): Retrieves the device position history from a tracker resource within a specified range of time.
- [ListDevicePositions](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_ListDevicePositions.html): A batch request to retrieve all device positions.
- [ListTrackerConsumers](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_ListTrackerConsumers.html): Lists geofence collections currently associated to the given tracker resource.
- [ListTrackers](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_ListTrackers.html): Lists tracker resources in your AWS account.
- [UpdateTracker](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_UpdateTracker.html): Updates the specified properties of a given tracker resource.
- [VerifyDevicePosition](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_VerifyDevicePosition.html): Verifies the integrity of the device's position by determining if it was reported behind a proxy, and by comparing it to an inferred position estimated based on the device's state.

### Data Types

- [BatchDeleteDevicePositionHistoryError](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_BatchDeleteDevicePositionHistoryError.html): Contains the tracker resource details.
- [BatchGetDevicePositionError](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_BatchGetDevicePositionError.html): Contains error details for each device that didn't return a position.
- [BatchItemError](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_BatchItemError.html)
- [BatchUpdateDevicePositionError](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_BatchUpdateDevicePositionError.html): Contains error details for each device that failed to update its position.
- [CellSignals](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_CellSignals.html): The cellular network communication infrastructure that the device uses.
- [DevicePosition](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_DevicePosition.html): Contains the device position details.
- [DevicePositionUpdate](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_DevicePositionUpdate.html)
- [DeviceState](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_DeviceState.html): The device's position, IP address, and Wi-Fi access points.
- [InferredState](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_InferredState.html): The inferred state of the device, given the provided position, IP address, cellular signals, and Wi-Fi- access points.
- [ListDevicePositionsResponseEntry](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_ListDevicePositionsResponseEntry.html): Contains the tracker resource details.
- [ListTrackersResponseEntry](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_ListTrackersResponseEntry.html): Contains the tracker resource details.
- [LteCellDetails](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_LteCellDetails.html): Details about the Long-Term Evolution (LTE) network.
- [LteLocalId](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_LteLocalId.html): LTE local identification information (local ID).
- [LteNetworkMeasurements](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_LteNetworkMeasurements.html): LTE network measurements.
- [PositionalAccuracy](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_PositionalAccuracy.html)
- [TrackingFilterGeometry](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_TrackingFilterGeometry.html): The geometry used to filter device positions.
- [ValidationExceptionField](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_ValidationExceptionField.html)
- [WiFiAccessPoint](https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_WiFiAccessPoint.html): Wi-Fi access point.

## Common

- [Common Parameters](https://docs.aws.amazon.com/location/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/location/latest/APIReference/CommonErrors.html)