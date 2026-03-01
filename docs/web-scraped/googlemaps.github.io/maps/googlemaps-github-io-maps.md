# Source: https://pkg.go.dev/googlemaps.github.io/maps

Title: maps package - googlemaps.github.io/maps - Go Packages

URL Source: https://pkg.go.dev/googlemaps.github.io/maps

Markdown Content:
Package maps provides a client library for the Google Maps Web Service APIs. Please see [https://developers.google.com/maps/documentation/webservices/](https://developers.google.com/maps/documentation/webservices/) for an overview of the Maps Web Service API suite.

*   [Constants](https://pkg.go.dev/googlemaps.github.io/maps#pkg-constants)
*   [func Encode(path []LatLng) string](https://pkg.go.dev/googlemaps.github.io/maps#Encode)
*   [func ExperienceIdContext(ctx context.Context, experienceIds ...string) context.Context](https://pkg.go.dev/googlemaps.github.io/maps#ExperienceIdContext)
*   [func ExperienceIdFromContext(ctx context.Context) []string](https://pkg.go.dev/googlemaps.github.io/maps#ExperienceIdFromContext)
*   [type AddressComponent](https://pkg.go.dev/googlemaps.github.io/maps#AddressComponent)
*   [type AddressGeometry](https://pkg.go.dev/googlemaps.github.io/maps#AddressGeometry)
*   [type AddressPlusCode](https://pkg.go.dev/googlemaps.github.io/maps#AddressPlusCode)
*   [type Anchor](https://pkg.go.dev/googlemaps.github.io/maps#Anchor)
*   [type AutocompleteMatchedSubstring](https://pkg.go.dev/googlemaps.github.io/maps#AutocompleteMatchedSubstring)
*   [type AutocompletePlaceType](https://pkg.go.dev/googlemaps.github.io/maps#AutocompletePlaceType)
*       *   [func ParseAutocompletePlaceType(placeType string) (AutocompletePlaceType, error)](https://pkg.go.dev/googlemaps.github.io/maps#ParseAutocompletePlaceType)

*   [type AutocompletePrediction](https://pkg.go.dev/googlemaps.github.io/maps#AutocompletePrediction)
*   [type AutocompleteResponse](https://pkg.go.dev/googlemaps.github.io/maps#AutocompleteResponse)
*   [type AutocompleteStructuredFormatting](https://pkg.go.dev/googlemaps.github.io/maps#AutocompleteStructuredFormatting)
*   [type AutocompleteTermOffset](https://pkg.go.dev/googlemaps.github.io/maps#AutocompleteTermOffset)
*   [type Avoid](https://pkg.go.dev/googlemaps.github.io/maps#Avoid)
*   [type CellTower](https://pkg.go.dev/googlemaps.github.io/maps#CellTower)
*   [type Client](https://pkg.go.dev/googlemaps.github.io/maps#Client)
*       *   [func NewClient(options ...ClientOption) (*Client, error)](https://pkg.go.dev/googlemaps.github.io/maps#NewClient)

*       *   [func (c *Client) Directions(ctx context.Context, r *DirectionsRequest) ([]Route, []GeocodedWaypoint, error)](https://pkg.go.dev/googlemaps.github.io/maps#Client.Directions)
    *   [func (c *Client) DistanceMatrix(ctx context.Context, r *DistanceMatrixRequest) (*DistanceMatrixResponse, error)](https://pkg.go.dev/googlemaps.github.io/maps#Client.DistanceMatrix)
    *   [func (c *Client) Elevation(ctx context.Context, r *ElevationRequest) ([]ElevationResult, error)](https://pkg.go.dev/googlemaps.github.io/maps#Client.Elevation)
    *   [func (c *Client) FindPlaceFromText(ctx context.Context, r *FindPlaceFromTextRequest) (FindPlaceFromTextResponse, error)](https://pkg.go.dev/googlemaps.github.io/maps#Client.FindPlaceFromText)
    *   [func (c *Client) Geocode(ctx context.Context, r *GeocodingRequest) ([]GeocodingResult, error)](https://pkg.go.dev/googlemaps.github.io/maps#Client.Geocode)
    *   [func (c *Client) Geolocate(ctx context.Context, r *GeolocationRequest) (*GeolocationResult, error)](https://pkg.go.dev/googlemaps.github.io/maps#Client.Geolocate)
    *   [func (c *Client) NearbySearch(ctx context.Context, r *NearbySearchRequest) (PlacesSearchResponse, error)](https://pkg.go.dev/googlemaps.github.io/maps#Client.NearbySearch)
    *   [func (c *Client) NearestRoads(ctx context.Context, r *NearestRoadsRequest) (*NearestRoadsResponse, error)](https://pkg.go.dev/googlemaps.github.io/maps#Client.NearestRoads)
    *   [func (c *Client) PlaceAutocomplete(ctx context.Context, r *PlaceAutocompleteRequest) (AutocompleteResponse, error)](https://pkg.go.dev/googlemaps.github.io/maps#Client.PlaceAutocomplete)
    *   [func (c *Client) PlaceDetails(ctx context.Context, r *PlaceDetailsRequest) (PlaceDetailsResult, error)](https://pkg.go.dev/googlemaps.github.io/maps#Client.PlaceDetails)
    *   [func (c *Client) PlacePhoto(ctx context.Context, r *PlacePhotoRequest) (PlacePhotoResponse, error)](https://pkg.go.dev/googlemaps.github.io/maps#Client.PlacePhoto)
    *   [func (c *Client) QueryAutocomplete(ctx context.Context, r *QueryAutocompleteRequest) (AutocompleteResponse, error)](https://pkg.go.dev/googlemaps.github.io/maps#Client.QueryAutocomplete)
    *   [func (c *Client) ReverseGeocode(ctx context.Context, r *GeocodingRequest) ([]GeocodingResult, error)](https://pkg.go.dev/googlemaps.github.io/maps#Client.ReverseGeocode)
    *   [func (c *Client) SnapToRoad(ctx context.Context, r *SnapToRoadRequest) (*SnapToRoadResponse, error)](https://pkg.go.dev/googlemaps.github.io/maps#Client.SnapToRoad)
    *   [func (c *Client) SpeedLimits(ctx context.Context, r *SpeedLimitsRequest) (*SpeedLimitsResponse, error)](https://pkg.go.dev/googlemaps.github.io/maps#Client.SpeedLimits)
    *   [func (c *Client) StaticMap(ctx context.Context, r *StaticMapRequest) (image.Image, error)](https://pkg.go.dev/googlemaps.github.io/maps#Client.StaticMap)
    *   [func (c *Client) TextSearch(ctx context.Context, r *TextSearchRequest) (PlacesSearchResponse, error)](https://pkg.go.dev/googlemaps.github.io/maps#Client.TextSearch)
    *   [func (c *Client) Timezone(ctx context.Context, r *TimezoneRequest) (*TimezoneResult, error)](https://pkg.go.dev/googlemaps.github.io/maps#Client.Timezone)

*   [type ClientOption](https://pkg.go.dev/googlemaps.github.io/maps#ClientOption)
*       *   [func WithAPIKey(apiKey string) ClientOption](https://pkg.go.dev/googlemaps.github.io/maps#WithAPIKey)
    *   [func WithAPIKeyAndSignature(apiKey, signature string) ClientOption](https://pkg.go.dev/googlemaps.github.io/maps#WithAPIKeyAndSignature)
    *   [func WithBaseURL(baseURL string) ClientOption](https://pkg.go.dev/googlemaps.github.io/maps#WithBaseURL)
    *   [func WithChannel(channel string) ClientOption](https://pkg.go.dev/googlemaps.github.io/maps#WithChannel)
    *   [func WithClientIDAndSignature(clientID, signature string) ClientOption](https://pkg.go.dev/googlemaps.github.io/maps#WithClientIDAndSignature)
    *   [func WithExperienceId(ids ...string) ClientOption](https://pkg.go.dev/googlemaps.github.io/maps#WithExperienceId)
    *   [func WithHTTPClient(c *http.Client) ClientOption](https://pkg.go.dev/googlemaps.github.io/maps#WithHTTPClient)
    *   [func WithMetricReporter(reporter metrics.Reporter) ClientOption](https://pkg.go.dev/googlemaps.github.io/maps#WithMetricReporter)
    *   [func WithRateLimit(requestsPerSecond int) ClientOption](https://pkg.go.dev/googlemaps.github.io/maps#WithRateLimit)

*   [type Component](https://pkg.go.dev/googlemaps.github.io/maps#Component)
*   [type CustomIcon](https://pkg.go.dev/googlemaps.github.io/maps#CustomIcon)
*       *   [func (c CustomIcon) String() string](https://pkg.go.dev/googlemaps.github.io/maps#CustomIcon.String)

*   [type DirectionsRequest](https://pkg.go.dev/googlemaps.github.io/maps#DirectionsRequest)
*   [type Distance](https://pkg.go.dev/googlemaps.github.io/maps#Distance)
*   [type DistanceMatrixElement](https://pkg.go.dev/googlemaps.github.io/maps#DistanceMatrixElement)
*       *   [func (dme *DistanceMatrixElement) MarshalJSON() ([]byte, error)](https://pkg.go.dev/googlemaps.github.io/maps#DistanceMatrixElement.MarshalJSON)
    *   [func (dme *DistanceMatrixElement) UnmarshalJSON(data []byte) error](https://pkg.go.dev/googlemaps.github.io/maps#DistanceMatrixElement.UnmarshalJSON)

*   [type DistanceMatrixElementsRow](https://pkg.go.dev/googlemaps.github.io/maps#DistanceMatrixElementsRow)
*   [type DistanceMatrixRequest](https://pkg.go.dev/googlemaps.github.io/maps#DistanceMatrixRequest)
*   [type DistanceMatrixResponse](https://pkg.go.dev/googlemaps.github.io/maps#DistanceMatrixResponse)
*   [type ElevationRequest](https://pkg.go.dev/googlemaps.github.io/maps#ElevationRequest)
*   [type ElevationResult](https://pkg.go.dev/googlemaps.github.io/maps#ElevationResult)
*   [type Fare](https://pkg.go.dev/googlemaps.github.io/maps#Fare)
*   [type FindPlaceFromTextInputType](https://pkg.go.dev/googlemaps.github.io/maps#FindPlaceFromTextInputType)
*   [type FindPlaceFromTextLocationBiasType](https://pkg.go.dev/googlemaps.github.io/maps#FindPlaceFromTextLocationBiasType)
*       *   [func ParseFindPlaceFromTextLocationBiasType(locationBias string) (FindPlaceFromTextLocationBiasType, error)](https://pkg.go.dev/googlemaps.github.io/maps#ParseFindPlaceFromTextLocationBiasType)

*   [type FindPlaceFromTextRequest](https://pkg.go.dev/googlemaps.github.io/maps#FindPlaceFromTextRequest)
*   [type FindPlaceFromTextResponse](https://pkg.go.dev/googlemaps.github.io/maps#FindPlaceFromTextResponse)
*   [type Format](https://pkg.go.dev/googlemaps.github.io/maps#Format)
*   [type GeocodeAccuracy](https://pkg.go.dev/googlemaps.github.io/maps#GeocodeAccuracy)
*   [type GeocodedWaypoint](https://pkg.go.dev/googlemaps.github.io/maps#GeocodedWaypoint)
*   [type GeocodingRequest](https://pkg.go.dev/googlemaps.github.io/maps#GeocodingRequest)
*   [type GeocodingResult](https://pkg.go.dev/googlemaps.github.io/maps#GeocodingResult)
*   [type GeolocationError](https://pkg.go.dev/googlemaps.github.io/maps#GeolocationError)
*   [type GeolocationRequest](https://pkg.go.dev/googlemaps.github.io/maps#GeolocationRequest)
*   [type GeolocationResult](https://pkg.go.dev/googlemaps.github.io/maps#GeolocationResult)
*   [type LatLng](https://pkg.go.dev/googlemaps.github.io/maps#LatLng)
*       *   [func DecodePolyline(poly string) ([]LatLng, error)](https://pkg.go.dev/googlemaps.github.io/maps#DecodePolyline)
    *   [func ParseLatLng(location string) (LatLng, error)](https://pkg.go.dev/googlemaps.github.io/maps#ParseLatLng)
    *   [func ParseLatLngList(locations string) ([]LatLng, error)](https://pkg.go.dev/googlemaps.github.io/maps#ParseLatLngList)

*       *   [func (l *LatLng) AlmostEqual(other *LatLng, epsilon float64) bool](https://pkg.go.dev/googlemaps.github.io/maps#LatLng.AlmostEqual)
    *   [func (l *LatLng) String() string](https://pkg.go.dev/googlemaps.github.io/maps#LatLng.String)

*   [type LatLngBounds](https://pkg.go.dev/googlemaps.github.io/maps#LatLngBounds)
*       *   [func (b *LatLngBounds) String() string](https://pkg.go.dev/googlemaps.github.io/maps#LatLngBounds.String)

*   [type Leg](https://pkg.go.dev/googlemaps.github.io/maps#Leg)
*       *   [func (leg *Leg) MarshalJSON() ([]byte, error)](https://pkg.go.dev/googlemaps.github.io/maps#Leg.MarshalJSON)
    *   [func (leg *Leg) UnmarshalJSON(data []byte) error](https://pkg.go.dev/googlemaps.github.io/maps#Leg.UnmarshalJSON)

*   [type MapType](https://pkg.go.dev/googlemaps.github.io/maps#MapType)
*   [type Marker](https://pkg.go.dev/googlemaps.github.io/maps#Marker)
*       *   [func (m Marker) String() string](https://pkg.go.dev/googlemaps.github.io/maps#Marker.String)

*   [type MarkerSize](https://pkg.go.dev/googlemaps.github.io/maps#MarkerSize)
*   [type Mode](https://pkg.go.dev/googlemaps.github.io/maps#Mode)
*   [type NearbySearchRequest](https://pkg.go.dev/googlemaps.github.io/maps#NearbySearchRequest)
*   [type NearestRoadsRequest](https://pkg.go.dev/googlemaps.github.io/maps#NearestRoadsRequest)
*   [type NearestRoadsResponse](https://pkg.go.dev/googlemaps.github.io/maps#NearestRoadsResponse)
*   [type OpeningHours](https://pkg.go.dev/googlemaps.github.io/maps#OpeningHours)
*   [type OpeningHoursOpenClose](https://pkg.go.dev/googlemaps.github.io/maps#OpeningHoursOpenClose)
*   [type OpeningHoursPeriod](https://pkg.go.dev/googlemaps.github.io/maps#OpeningHoursPeriod)
*   [type Path](https://pkg.go.dev/googlemaps.github.io/maps#Path)
*       *   [func (p Path) String() string](https://pkg.go.dev/googlemaps.github.io/maps#Path.String)

*   [type Photo](https://pkg.go.dev/googlemaps.github.io/maps#Photo)
*   [type PlaceAutocompleteRequest](https://pkg.go.dev/googlemaps.github.io/maps#PlaceAutocompleteRequest)
*   [type PlaceAutocompleteSessionToken](https://pkg.go.dev/googlemaps.github.io/maps#PlaceAutocompleteSessionToken)
*       *   [func NewPlaceAutocompleteSessionToken() PlaceAutocompleteSessionToken](https://pkg.go.dev/googlemaps.github.io/maps#NewPlaceAutocompleteSessionToken)

*   [type PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)
*       *   [func ParsePlaceDetailsFieldMask(placeDetailsFieldMask string) (PlaceDetailsFieldMask, error)](https://pkg.go.dev/googlemaps.github.io/maps#ParsePlaceDetailsFieldMask)

*   [type PlaceDetailsRequest](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsRequest)
*   [type PlaceDetailsResult](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsResult)
*   [type PlaceEditorialSummary](https://pkg.go.dev/googlemaps.github.io/maps#PlaceEditorialSummary)
*   [type PlacePhotoRequest](https://pkg.go.dev/googlemaps.github.io/maps#PlacePhotoRequest)
*   [type PlacePhotoResponse](https://pkg.go.dev/googlemaps.github.io/maps#PlacePhotoResponse)
*       *   [func (resp *PlacePhotoResponse) Image() (image.Image, error)](https://pkg.go.dev/googlemaps.github.io/maps#PlacePhotoResponse.Image)

*   [type PlaceReview](https://pkg.go.dev/googlemaps.github.io/maps#PlaceReview)
*   [type PlaceReviewAspect](https://pkg.go.dev/googlemaps.github.io/maps#PlaceReviewAspect)
*   [type PlaceSearchFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceSearchFieldMask)
*       *   [func ParsePlaceSearchFieldMask(placeSearchFieldMask string) (PlaceSearchFieldMask, error)](https://pkg.go.dev/googlemaps.github.io/maps#ParsePlaceSearchFieldMask)

*   [type PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)
*       *   [func ParsePlaceType(placeType string) (PlaceType, error)](https://pkg.go.dev/googlemaps.github.io/maps#ParsePlaceType)

*   [type PlacesSearchResponse](https://pkg.go.dev/googlemaps.github.io/maps#PlacesSearchResponse)
*   [type PlacesSearchResult](https://pkg.go.dev/googlemaps.github.io/maps#PlacesSearchResult)
*   [type Polyline](https://pkg.go.dev/googlemaps.github.io/maps#Polyline)
*       *   [func (p *Polyline) Decode() ([]LatLng, error)](https://pkg.go.dev/googlemaps.github.io/maps#Polyline.Decode)

*   [type PriceLevel](https://pkg.go.dev/googlemaps.github.io/maps#PriceLevel)
*   [type QueryAutocompleteRequest](https://pkg.go.dev/googlemaps.github.io/maps#QueryAutocompleteRequest)
*   [type RadioType](https://pkg.go.dev/googlemaps.github.io/maps#RadioType)
*   [type RankBy](https://pkg.go.dev/googlemaps.github.io/maps#RankBy)
*   [type Route](https://pkg.go.dev/googlemaps.github.io/maps#Route)
*   [type SnapToRoadRequest](https://pkg.go.dev/googlemaps.github.io/maps#SnapToRoadRequest)
*   [type SnapToRoadResponse](https://pkg.go.dev/googlemaps.github.io/maps#SnapToRoadResponse)
*   [type SnappedPoint](https://pkg.go.dev/googlemaps.github.io/maps#SnappedPoint)
*       *   [func (sp *SnappedPoint) MarshalJSON() ([]byte, error)](https://pkg.go.dev/googlemaps.github.io/maps#SnappedPoint.MarshalJSON)
    *   [func (sp *SnappedPoint) UnmarshalJSON(data []byte) error](https://pkg.go.dev/googlemaps.github.io/maps#SnappedPoint.UnmarshalJSON)

*   [type SpeedLimit](https://pkg.go.dev/googlemaps.github.io/maps#SpeedLimit)
*   [type SpeedLimitsRequest](https://pkg.go.dev/googlemaps.github.io/maps#SpeedLimitsRequest)
*   [type SpeedLimitsResponse](https://pkg.go.dev/googlemaps.github.io/maps#SpeedLimitsResponse)
*   [type StaticMapRequest](https://pkg.go.dev/googlemaps.github.io/maps#StaticMapRequest)
*   [type Step](https://pkg.go.dev/googlemaps.github.io/maps#Step)
*       *   [func (step *Step) MarshalJSON() ([]byte, error)](https://pkg.go.dev/googlemaps.github.io/maps#Step.MarshalJSON)
    *   [func (step *Step) UnmarshalJSON(data []byte) error](https://pkg.go.dev/googlemaps.github.io/maps#Step.UnmarshalJSON)

*   [type TextSearchRequest](https://pkg.go.dev/googlemaps.github.io/maps#TextSearchRequest)
*   [type TimezoneRequest](https://pkg.go.dev/googlemaps.github.io/maps#TimezoneRequest)
*   [type TimezoneResult](https://pkg.go.dev/googlemaps.github.io/maps#TimezoneResult)
*   [type TrafficModel](https://pkg.go.dev/googlemaps.github.io/maps#TrafficModel)
*   [type TransitAgency](https://pkg.go.dev/googlemaps.github.io/maps#TransitAgency)
*       *   [func (transitAgency *TransitAgency) MarshalJSON() ([]byte, error)](https://pkg.go.dev/googlemaps.github.io/maps#TransitAgency.MarshalJSON)
    *   [func (transitAgency *TransitAgency) UnmarshalJSON(data []byte) error](https://pkg.go.dev/googlemaps.github.io/maps#TransitAgency.UnmarshalJSON)

*   [type TransitDetails](https://pkg.go.dev/googlemaps.github.io/maps#TransitDetails)
*       *   [func (transitDetails *TransitDetails) MarshalJSON() ([]byte, error)](https://pkg.go.dev/googlemaps.github.io/maps#TransitDetails.MarshalJSON)
    *   [func (transitDetails *TransitDetails) UnmarshalJSON(data []byte) error](https://pkg.go.dev/googlemaps.github.io/maps#TransitDetails.UnmarshalJSON)

*   [type TransitLine](https://pkg.go.dev/googlemaps.github.io/maps#TransitLine)
*       *   [func (transitLine *TransitLine) MarshalJSON() ([]byte, error)](https://pkg.go.dev/googlemaps.github.io/maps#TransitLine.MarshalJSON)
    *   [func (transitLine *TransitLine) UnmarshalJSON(data []byte) error](https://pkg.go.dev/googlemaps.github.io/maps#TransitLine.UnmarshalJSON)

*   [type TransitLineVehicle](https://pkg.go.dev/googlemaps.github.io/maps#TransitLineVehicle)
*       *   [func (transitLineVehicle *TransitLineVehicle) MarshalJSON() ([]byte, error)](https://pkg.go.dev/googlemaps.github.io/maps#TransitLineVehicle.MarshalJSON)
    *   [func (transitLineVehicle *TransitLineVehicle) UnmarshalJSON(data []byte) error](https://pkg.go.dev/googlemaps.github.io/maps#TransitLineVehicle.UnmarshalJSON)

*   [type TransitMode](https://pkg.go.dev/googlemaps.github.io/maps#TransitMode)
*   [type TransitRoutingPreference](https://pkg.go.dev/googlemaps.github.io/maps#TransitRoutingPreference)
*   [type TransitStop](https://pkg.go.dev/googlemaps.github.io/maps#TransitStop)
*   [type Units](https://pkg.go.dev/googlemaps.github.io/maps#Units)
*   [type ViaWaypoint](https://pkg.go.dev/googlemaps.github.io/maps#ViaWaypoint)
*   [type WiFiAccessPoint](https://pkg.go.dev/googlemaps.github.io/maps#WiFiAccessPoint)

[View Source](https://github.com/googlemaps/google-maps-services-go/blob/v1.7.0/geocoding.go#L129)

const (
	
	GeocodeAccuracyRooftop = [GeocodeAccuracy](https://pkg.go.dev/googlemaps.github.io/maps#GeocodeAccuracy)("ROOFTOP")
	
	GeocodeAccuracyRangeInterpolated = [GeocodeAccuracy](https://pkg.go.dev/googlemaps.github.io/maps#GeocodeAccuracy)("RANGE_INTERPOLATED")
	
	GeocodeAccuracyGeometricCenter = [GeocodeAccuracy](https://pkg.go.dev/googlemaps.github.io/maps#GeocodeAccuracy)("GEOMETRIC_CENTER")
	
	GeocodeAccuracyApproximate = [GeocodeAccuracy](https://pkg.go.dev/googlemaps.github.io/maps#GeocodeAccuracy)("APPROXIMATE")
)

[View Source](https://github.com/googlemaps/google-maps-services-go/blob/v1.7.0/places.go#L961)

const (
 FindPlaceFromTextInputTypeTextQuery = [FindPlaceFromTextInputType](https://pkg.go.dev/googlemaps.github.io/maps#FindPlaceFromTextInputType)("textquery")  FindPlaceFromTextInputTypePhoneNumber = [FindPlaceFromTextInputType](https://pkg.go.dev/googlemaps.github.io/maps#FindPlaceFromTextInputType)("phonenumber") )

The types of FindPlaceFromText Input Types.

[View Source](https://github.com/googlemaps/google-maps-services-go/blob/v1.7.0/places.go#L970)

const (
 FindPlaceFromTextLocationBiasIP = [FindPlaceFromTextLocationBiasType](https://pkg.go.dev/googlemaps.github.io/maps#FindPlaceFromTextLocationBiasType)("ipbias")  FindPlaceFromTextLocationBiasPoint = [FindPlaceFromTextLocationBiasType](https://pkg.go.dev/googlemaps.github.io/maps#FindPlaceFromTextLocationBiasType)("point")  FindPlaceFromTextLocationBiasCircular = [FindPlaceFromTextLocationBiasType](https://pkg.go.dev/googlemaps.github.io/maps#FindPlaceFromTextLocationBiasType)("circle")  FindPlaceFromTextLocationBiasRectangular = [FindPlaceFromTextLocationBiasType](https://pkg.go.dev/googlemaps.github.io/maps#FindPlaceFromTextLocationBiasType)("rectangle") )

The types of FindPlaceFromTextLocationBiasType

[View Source](https://github.com/googlemaps/google-maps-services-go/blob/v1.7.0/roads.go#L185)

const (
	SpeedLimitMPH = "MPH"
	SpeedLimitKPH = "KPH"
)

[View Source](https://github.com/googlemaps/google-maps-services-go/blob/v1.7.0/staticmap.go#L52)

const (
	
	
	RoadMap [MapType](https://pkg.go.dev/googlemaps.github.io/maps#MapType) = "roadmap"
	Satellite [MapType](https://pkg.go.dev/googlemaps.github.io/maps#MapType) = "satellite"
	Terrain [MapType](https://pkg.go.dev/googlemaps.github.io/maps#MapType) = "terrain"
	
	Hybrid [MapType](https://pkg.go.dev/googlemaps.github.io/maps#MapType) = "hybrid"
	PNG8 [Format](https://pkg.go.dev/googlemaps.github.io/maps#Format) = "png8"
	PNG32 [Format](https://pkg.go.dev/googlemaps.github.io/maps#Format) = "png32"
	GIF [Format](https://pkg.go.dev/googlemaps.github.io/maps#Format) = "gif"
	JPG [Format](https://pkg.go.dev/googlemaps.github.io/maps#Format) = "jpg"
	JPGBaseline [Format](https://pkg.go.dev/googlemaps.github.io/maps#Format) = "jpg-baseline"

	Tiny [MarkerSize](https://pkg.go.dev/googlemaps.github.io/maps#MarkerSize) = "tiny"
	Mid [MarkerSize](https://pkg.go.dev/googlemaps.github.io/maps#MarkerSize) = "mid"
	Small [MarkerSize](https://pkg.go.dev/googlemaps.github.io/maps#MarkerSize) = "small"

	Top [Anchor](https://pkg.go.dev/googlemaps.github.io/maps#Anchor) = "top"
	Bottom [Anchor](https://pkg.go.dev/googlemaps.github.io/maps#Anchor) = "Bottom"
	Left [Anchor](https://pkg.go.dev/googlemaps.github.io/maps#Anchor) = "left"
	Right [Anchor](https://pkg.go.dev/googlemaps.github.io/maps#Anchor) = "right"
	Center [Anchor](https://pkg.go.dev/googlemaps.github.io/maps#Anchor) = "center"
	Topleft [Anchor](https://pkg.go.dev/googlemaps.github.io/maps#Anchor) = "topleft"
	Topright [Anchor](https://pkg.go.dev/googlemaps.github.io/maps#Anchor) = "topright"
	Bottomleft [Anchor](https://pkg.go.dev/googlemaps.github.io/maps#Anchor) = "bottomleft"
	Bottomright [Anchor](https://pkg.go.dev/googlemaps.github.io/maps#Anchor) = "bottomright"
)

[View Source](https://github.com/googlemaps/google-maps-services-go/blob/v1.7.0/types.go#L42)

const (
 TravelModeDriving = [Mode](https://pkg.go.dev/googlemaps.github.io/maps#Mode)("driving")  TravelModeWalking = [Mode](https://pkg.go.dev/googlemaps.github.io/maps#Mode)("walking")  TravelModeBicycling = [Mode](https://pkg.go.dev/googlemaps.github.io/maps#Mode)("bicycling")  TravelModeTransit = [Mode](https://pkg.go.dev/googlemaps.github.io/maps#Mode)("transit") )

Travel mode preferences.

[View Source](https://github.com/googlemaps/google-maps-services-go/blob/v1.7.0/types.go#L50)

const (
 AvoidTolls = [Avoid](https://pkg.go.dev/googlemaps.github.io/maps#Avoid)("tolls")  AvoidHighways = [Avoid](https://pkg.go.dev/googlemaps.github.io/maps#Avoid)("highways")  AvoidFerries = [Avoid](https://pkg.go.dev/googlemaps.github.io/maps#Avoid)("ferries") )

Features to avoid.

[View Source](https://github.com/googlemaps/google-maps-services-go/blob/v1.7.0/types.go#L57)

const (
 UnitsMetric = [Units](https://pkg.go.dev/googlemaps.github.io/maps#Units)("metric")  UnitsImperial = [Units](https://pkg.go.dev/googlemaps.github.io/maps#Units)("imperial") )

Units to use on human readable distances.

[View Source](https://github.com/googlemaps/google-maps-services-go/blob/v1.7.0/types.go#L63)

const (
 TransitModeBus = [TransitMode](https://pkg.go.dev/googlemaps.github.io/maps#TransitMode)("bus")  TransitModeSubway = [TransitMode](https://pkg.go.dev/googlemaps.github.io/maps#TransitMode)("subway")  TransitModeTrain = [TransitMode](https://pkg.go.dev/googlemaps.github.io/maps#TransitMode)("train")  TransitModeTram = [TransitMode](https://pkg.go.dev/googlemaps.github.io/maps#TransitMode)("tram")  TransitModeRail = [TransitMode](https://pkg.go.dev/googlemaps.github.io/maps#TransitMode)("rail") )

Transit mode of directions or distance matrix request.

[View Source](https://github.com/googlemaps/google-maps-services-go/blob/v1.7.0/types.go#L72)

const (
 TransitRoutingPreferenceLessWalking = [TransitRoutingPreference](https://pkg.go.dev/googlemaps.github.io/maps#TransitRoutingPreference)("less_walking")  TransitRoutingPreferenceFewerTransfers = [TransitRoutingPreference](https://pkg.go.dev/googlemaps.github.io/maps#TransitRoutingPreference)("fewer_transfers") )

Transit Routing preferences for transit mode requests

[View Source](https://github.com/googlemaps/google-maps-services-go/blob/v1.7.0/types.go#L93)

const (
 TrafficModelBestGuess = [TrafficModel](https://pkg.go.dev/googlemaps.github.io/maps#TrafficModel)("best_guess")  TrafficModelOptimistic = [TrafficModel](https://pkg.go.dev/googlemaps.github.io/maps#TrafficModel)("optimistic")  TrafficModelPessimistic = [TrafficModel](https://pkg.go.dev/googlemaps.github.io/maps#TrafficModel)("pessimistic") )

Traffic prediction model when requesting future directions.

[View Source](https://github.com/googlemaps/google-maps-services-go/blob/v1.7.0/types.go#L103)

const (
 PriceLevelFree = [PriceLevel](https://pkg.go.dev/googlemaps.github.io/maps#PriceLevel)("0")  PriceLevelInexpensive = [PriceLevel](https://pkg.go.dev/googlemaps.github.io/maps#PriceLevel)("1")  PriceLevelModerate = [PriceLevel](https://pkg.go.dev/googlemaps.github.io/maps#PriceLevel)("2")  PriceLevelExpensive = [PriceLevel](https://pkg.go.dev/googlemaps.github.io/maps#PriceLevel)("3")  PriceLevelVeryExpensive = [PriceLevel](https://pkg.go.dev/googlemaps.github.io/maps#PriceLevel)("4") )

Price Levels for the Places API

[View Source](https://github.com/googlemaps/google-maps-services-go/blob/v1.7.0/types.go#L174)

const (
	ComponentRoute = [Component](https://pkg.go.dev/googlemaps.github.io/maps#Component)("route")
	ComponentLocality = [Component](https://pkg.go.dev/googlemaps.github.io/maps#Component)("locality")
	ComponentAdministrativeArea = [Component](https://pkg.go.dev/googlemaps.github.io/maps#Component)("administrative_area")
	ComponentPostalCode = [Component](https://pkg.go.dev/googlemaps.github.io/maps#Component)("postal_code")
	ComponentCountry = [Component](https://pkg.go.dev/googlemaps.github.io/maps#Component)("country")
)

[View Source](https://github.com/googlemaps/google-maps-services-go/blob/v1.7.0/types.go#L191)

const (
 RankByProminence = [RankBy](https://pkg.go.dev/googlemaps.github.io/maps#RankBy)("prominence")  RankByDistance = [RankBy](https://pkg.go.dev/googlemaps.github.io/maps#RankBy)("distance") )

RankBy options for Places Search.

[View Source](https://github.com/googlemaps/google-maps-services-go/blob/v1.7.0/types.go#L201)

const (
 PlaceTypeAccounting = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("accounting")  PlaceTypeAirport = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("airport")  PlaceTypeAmusementPark = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("amusement_park")  PlaceTypeAquarium = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("aquarium")  PlaceTypeArtGallery = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("art_gallery")  PlaceTypeAtm = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("atm")  PlaceTypeBakery = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("bakery")  PlaceTypeBank = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("bank")  PlaceTypeBar = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("bar")  PlaceTypeBeautySalon = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("beauty_salon")  PlaceTypeBicycleStore = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("bicycle_store")  PlaceTypeBookStore = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("book_store")  PlaceTypeBowlingAlley = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("bowling_alley")  PlaceTypeBusStation = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("bus_station")  PlaceTypeCafe = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("cafe")  PlaceTypeCampground = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("campground")  PlaceTypeCarDealer = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("car_dealer")  PlaceTypeCarRental = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("car_rental")  PlaceTypeCarRepair = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("car_repair")  PlaceTypeCarWash = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("car_wash")  PlaceTypeCasino = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("casino")  PlaceTypeCemetery = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("cemetery")  PlaceTypeChurch = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("church")  PlaceTypeCityHall = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("city_hall")  PlaceTypeClothingStore = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("clothing_store")  PlaceTypeConvenienceStore = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("convenience_store")  PlaceTypeCourthouse = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("courthouse")  PlaceTypeDentist = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("dentist")  PlaceTypeDepartmentStore = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("department_store")  PlaceTypeDoctor = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("doctor")  PlaceTypeDrugstore = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("drugstore")  PlaceTypeElectrician = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("electrician")  PlaceTypeElectronicsStore = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("electronics_store")  PlaceTypeEmbassy = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("embassy")  PlaceTypeFireStation = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("fire_station")  PlaceTypeFlorist = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("florist")  PlaceTypeFuneralHome = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("funeral_home")  PlaceTypeFurnitureStore = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("furniture_store")  PlaceTypeGasStation = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("gas_station")  PlaceTypeGym = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("gym")  PlaceTypeHairCare = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("hair_care")  PlaceTypeHardwareStore = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("hardware_store")  PlaceTypeHinduTemple = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("hindu_temple")  PlaceTypeHomeGoodsStore = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("home_goods_store")  PlaceTypeHospital = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("hospital")  PlaceTypeInsuranceAgency = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("insurance_agency")  PlaceTypeJewelryStore = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("jewelry_store")  PlaceTypeLaundry = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("laundry")  PlaceTypeLawyer = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("lawyer")  PlaceTypeLibrary = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("library")  PlaceTypeLightRailStation = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("light_rail_station")  PlaceTypeLiquorStore = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("liquor_store")  PlaceTypeLocalGovernmentOffice = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("local_government_office")  PlaceTypeLocksmith = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("locksmith")  PlaceTypeLodging = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("lodging")  PlaceTypeMealDelivery = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("meal_delivery")  PlaceTypeMealTakeaway = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("meal_takeaway")  PlaceTypeMosque = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("mosque")  PlaceTypeMovieRental = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("movie_rental")  PlaceTypeMovieTheater = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("movie_theater")  PlaceTypeMovingCompany = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("moving_company")  PlaceTypeMuseum = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("museum")  PlaceTypeNightClub = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("night_club")  PlaceTypePainter = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("painter")  PlaceTypePark = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("park")  PlaceTypeParking = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("parking")  PlaceTypePetStore = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("pet_store")  PlaceTypePharmacy = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("pharmacy")  PlaceTypePhysiotherapist = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("physiotherapist")  PlaceTypePlumber = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("plumber")  PlaceTypePolice = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("police")  PlaceTypePostOffice = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("post_office")  PlaceTypePrimarySchool = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("primary_school")  PlaceTypeRealEstateAgency = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("real_estate_agency")  PlaceTypeRestaurant = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("restaurant")  PlaceTypeRoofingContractor = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("roofing_contractor")  PlaceTypeRvPark = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("rv_park")  PlaceTypeSchool = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("school")  PlaceTypeSecondarySchool = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("secondary_school")  PlaceTypeShoeStore = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("shoe_store")  PlaceTypeShoppingMall = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("shopping_mall")  PlaceTypeSpa = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("spa")  PlaceTypeStadium = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("stadium")  PlaceTypeStorage = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("storage")  PlaceTypeStore = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("store")  PlaceTypeSubwayStation = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("subway_station")  PlaceTypeSupermarket = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("supermarket")  PlaceTypeSynagogue = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("synagogue")  PlaceTypeTaxiStand = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("taxi_stand")  PlaceTypeTouristAttraction = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("tourist_attraction")  PlaceTypeTrainStation = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("train_station")  PlaceTypeTransitStation = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("transit_station")  PlaceTypeTravelAgency = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("travel_agency")  PlaceTypeUniversity = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("university")  PlaceTypeVeterinaryCare = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("veterinary_care")  PlaceTypeZoo = [PlaceType](https://pkg.go.dev/googlemaps.github.io/maps#PlaceType)("zoo") )

Place Types for the Places API.

[View Source](https://github.com/googlemaps/google-maps-services-go/blob/v1.7.0/types.go#L505)

const (
 AutocompletePlaceTypeGeocode = [AutocompletePlaceType](https://pkg.go.dev/googlemaps.github.io/maps#AutocompletePlaceType)("geocode")  AutocompletePlaceTypeAddress = [AutocompletePlaceType](https://pkg.go.dev/googlemaps.github.io/maps#AutocompletePlaceType)("address")  AutocompletePlaceTypeEstablishment = [AutocompletePlaceType](https://pkg.go.dev/googlemaps.github.io/maps#AutocompletePlaceType)("establishment")  AutocompletePlaceTypeRegions = [AutocompletePlaceType](https://pkg.go.dev/googlemaps.github.io/maps#AutocompletePlaceType)("(regions)")  AutocompletePlaceTypeCities = [AutocompletePlaceType](https://pkg.go.dev/googlemaps.github.io/maps#AutocompletePlaceType)("(cities)") )

[https://developers.google.com/places/web-service/autocomplete#place_types](https://developers.google.com/places/web-service/autocomplete#place_types)

[View Source](https://github.com/googlemaps/google-maps-services-go/blob/v1.7.0/types.go#L538)

const (
 PlaceDetailsFieldMaskAddressComponent = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("address_component")  PlaceDetailsFieldMaskADRAddress = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("adr_address")  PlaceDetailsFieldMaskBusinessStatus = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("business_status")  PlaceDetailsFieldMaskCurbsidePickup = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("curbside_pickup")  PlaceDetailsFieldMaskDelivery = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("delivery")  PlaceDetailsFieldMaskDineIn = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("dine_in")  PlaceDetailsFieldMaskEditorialSummary = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("editorial_summary")  PlaceDetailsFieldMaskFormattedAddress = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("formatted_address")  PlaceDetailsFieldMaskFormattedPhoneNumber = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("formatted_phone_number")  PlaceDetailsFieldMaskGeometry = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("geometry")  PlaceDetailsFieldMaskGeometryLocation = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("geometry/location")  PlaceDetailsFieldMaskGeometryLocationLat = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("geometry/location/lat")  PlaceDetailsFieldMaskGeometryLocationLng = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("geometry/location/lng")  PlaceDetailsFieldMaskGeometryViewport = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("geometry/viewport")  PlaceDetailsFieldMaskGeometryViewportNortheast = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("geometry/viewport/northeast")  PlaceDetailsFieldMaskGeometryViewportNortheastLat = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("geometry/viewport/northeast/lat")  PlaceDetailsFieldMaskGeometryViewportNortheastLng = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("geometry/viewport/northeast/lng")  PlaceDetailsFieldMaskGeometryViewportSouthwest = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("geometry/viewport/southwest")  PlaceDetailsFieldMaskGeometryViewportSouthwestLat = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("geometry/viewport/southwest/lat")  PlaceDetailsFieldMaskGeometryViewportSouthwestLng = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("geometry/viewport/southwest/lng")  PlaceDetailsFieldMaskIcon = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("icon")  PlaceDetailsFieldMaskID = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("id")  PlaceDetailsFieldMaskInternationalPhoneNumber = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("international_phone_number")  PlaceDetailsFieldMaskName = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("name")  PlaceDetailsFieldMaskOpeningHours = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("opening_hours")  PlaceDetailsFieldMaskCurrentOpeningHours = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("current_opening_hours")  PlaceDetailsFieldMaskSecondaryOpeningHours = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("secondary_opening_hours")  PlaceDetailsFieldMaskPermanentlyClosed = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("permanently_closed")  PlaceDetailsFieldMaskPhotos = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("photos")  PlaceDetailsFieldMaskPlaceID = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("place_id")  PlaceDetailsFieldMaskPriceLevel = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("price_level")  PlaceDetailsFieldMaskRatings = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("rating")  PlaceDetailsFieldMaskUserRatingsTotal = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("user_ratings_total")  PlaceDetailsFieldMaskReservable = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("reservable")  PlaceDetailsFieldMaskReviews = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("reviews")  PlaceDetailsFieldMaskServesBeer = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("serves_beer")  PlaceDetailsFieldMaskServesBreakfast = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("serves_breakfast")  PlaceDetailsFieldMaskServesBrunch = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("serves_brunch")  PlaceDetailsFieldMaskServesDinner = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("serves_dinner")  PlaceDetailsFieldMaskServesLunch = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("serves_lunch")  PlaceDetailsFieldMaskServesVegetarianFood = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("serves_vegetarian_food")  PlaceDetailsFieldMaskServesWine = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("serves_wine")  PlaceDetailsFieldMaskTakeout = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("takeout")  PlaceDetailsFieldMaskTypes = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("types")  PlaceDetailsFieldMaskURL = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("url")  PlaceDetailsFieldMaskUTCOffset = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("utc_offset")  PlaceDetailsFieldMaskVicinity = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("vicinity")  PlaceDetailsFieldMaskWebsite = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("website")  PlaceDetailsFieldMaskWheelchairAccessibleEntrance = [PlaceDetailsFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceDetailsFieldMask)("wheelchair_accessible_entrance") )

The individual Place Details Field Masks.

[View Source](https://github.com/googlemaps/google-maps-services-go/blob/v1.7.0/types.go#L712)

const (
 PlaceSearchFieldMaskBusinessStatus = [PlaceSearchFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceSearchFieldMask)("business_status")  PlaceSearchFieldMaskFormattedAddress = [PlaceSearchFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceSearchFieldMask)("formatted_address")  PlaceSearchFieldMaskGeometry = [PlaceSearchFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceSearchFieldMask)("geometry")  PlaceSearchFieldMaskGeometryLocation = [PlaceSearchFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceSearchFieldMask)("geometry/location")  PlaceSearchFieldMaskGeometryLocationLat = [PlaceSearchFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceSearchFieldMask)("geometry/location/lat")  PlaceSearchFieldMaskGeometryLocationLng = [PlaceSearchFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceSearchFieldMask)("geometry/location/lng")  PlaceSearchFieldMaskGeometryViewport = [PlaceSearchFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceSearchFieldMask)("geometry/viewport")  PlaceSearchFieldMaskGeometryViewportNortheast = [PlaceSearchFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceSearchFieldMask)("geometry/viewport/northeast")  PlaceSearchFieldMaskGeometryViewportNortheastLat = [PlaceSearchFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceSearchFieldMask)("geometry/viewport/northeast/lat")  PlaceSearchFieldMaskGeometryViewportNortheastLng = [PlaceSearchFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceSearchFieldMask)("geometry/viewport/northeast/lng")  PlaceSearchFieldMaskGeometryViewportSouthwest = [PlaceSearchFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceSearchFieldMask)("geometry/viewport/southwest")  PlaceSearchFieldMaskGeometryViewportSouthwestLat = [PlaceSearchFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceSearchFieldMask)("geometry/viewport/southwest/lat")  PlaceSearchFieldMaskGeometryViewportSouthwestLng = [PlaceSearchFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceSearchFieldMask)("geometry/viewport/southwest/lng")  PlaceSearchFieldMaskIcon = [PlaceSearchFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceSearchFieldMask)("icon")  PlaceSearchFieldMaskID = [PlaceSearchFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceSearchFieldMask)("id")  PlaceSearchFieldMaskName = [PlaceSearchFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceSearchFieldMask)("name")  PlaceSearchFieldMaskOpeningHours = [PlaceSearchFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceSearchFieldMask)("opening_hours")  PlaceSearchFieldMaskOpeningHoursOpenNow = [PlaceSearchFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceSearchFieldMask)("opening_hours/open_now")  PlaceSearchFieldMaskPermanentlyClosed = [PlaceSearchFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceSearchFieldMask)("permanently_closed")  PlaceSearchFieldMaskPhotos = [PlaceSearchFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceSearchFieldMask)("photos")  PlaceSearchFieldMaskPlaceID = [PlaceSearchFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceSearchFieldMask)("place_id")  PlaceSearchFieldMaskPriceLevel = [PlaceSearchFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceSearchFieldMask)("price_level")  PlaceSearchFieldMaskRating = [PlaceSearchFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceSearchFieldMask)("rating")  PlaceSearchFieldMaskUserRatingsTotal = [PlaceSearchFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceSearchFieldMask)("user_ratings_total")  PlaceSearchFieldMaskReference = [PlaceSearchFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceSearchFieldMask)("reference")  PlaceSearchFieldMaskTypes = [PlaceSearchFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceSearchFieldMask)("types")  PlaceSearchFieldMaskVicinity = [PlaceSearchFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceSearchFieldMask)("vicinity") )

The individual Place Search Field Masks.

This section is empty.

Encode returns a new encoded Polyline from the given path.

ExperienceIdContext injects the experienceIds in the context, from where they will be pull out in the post/get handlers. Useful if a customer uses one client instance per different experiences calls

ExperienceIdFromContext returns experienceIds from context if presented

type AddressComponent struct {
 LongName [string](https://pkg.go.dev/builtin#string) `json:"long_name"`  ShortName [string](https://pkg.go.dev/builtin#string) `json:"short_name"`  Types [][string](https://pkg.go.dev/builtin#string) `json:"types"` }

AddressComponent is a part of an address

type AddressGeometry struct {
 Location [LatLng](https://pkg.go.dev/googlemaps.github.io/maps#LatLng) `json:"location"`  LocationType [string](https://pkg.go.dev/builtin#string) `json:"location_type"`  Bounds [LatLngBounds](https://pkg.go.dev/googlemaps.github.io/maps#LatLngBounds) `json:"bounds"`  Viewport [LatLngBounds](https://pkg.go.dev/googlemaps.github.io/maps#LatLngBounds) `json:"viewport"`  Types [][string](https://pkg.go.dev/builtin#string) `json:"types"` }

AddressGeometry is the location of a an address

type AddressPlusCode struct {
	GlobalCode [string](https://pkg.go.dev/builtin#string) `json:"global_code"`
	CompoundCode [string](https://pkg.go.dev/builtin#string) `json:"compound_code"`
}

AddressPlusCode (see [https://en.wikipedia.org/wiki/Open_Location_Code](https://en.wikipedia.org/wiki/Open_Location_Code) and [https://plus.codes/](https://plus.codes/)) is an encoded location reference, derived from latitude and longitude coordinates, that represents an area: 1/8000th of a degree by 1/8000th of a degree (about 14m x 14m at the equator) or smaller.

Plus codes can be used as a replacement for street addresses in places where they do not exist (where buildings are not numbered or streets are not named). The plus code is formatted as a global code and a compound code: Typically, both the global code and compound code are returned. However, if the result is in a remote location (for example, an ocean or desert) only the global code may be returned.

Anchor sets how the icon is placed in relation to the specified markers locations

type AutocompleteMatchedSubstring struct {
	Length [int](https://pkg.go.dev/builtin#int) `json:"length"`
	Offset [int](https://pkg.go.dev/builtin#int) `json:"offset"`
}

AutocompleteMatchedSubstring describes the location of the entered term in the prediction result text, so that the term can be highlighted if desired.

type AutocompletePlaceType [string](https://pkg.go.dev/builtin#string)

AutocompletePlaceType restricts Place Autocomplete API to the results to places matching the specified type.

ParseAutocompletePlaceType will parse a string representation of a AutocompletePlaceTypes.

type AutocompletePrediction struct {
	Description [string](https://pkg.go.dev/builtin#string) `json:"description,omitempty"`
	
	DistanceMeters [int](https://pkg.go.dev/builtin#int) `json:"distance_meters,omitempty"`
	PlaceID [string](https://pkg.go.dev/builtin#string) `json:"place_id,omitempty"`
	Types [][string](https://pkg.go.dev/builtin#string) `json:"types,omitempty"`
	
	MatchedSubstrings [][AutocompleteMatchedSubstring](https://pkg.go.dev/googlemaps.github.io/maps#AutocompleteMatchedSubstring) `json:"matched_substrings,omitempty"`
	
	Terms [][AutocompleteTermOffset](https://pkg.go.dev/googlemaps.github.io/maps#AutocompleteTermOffset) `json:"terms,omitempty"`
	StructuredFormatting [AutocompleteStructuredFormatting](https://pkg.go.dev/googlemaps.github.io/maps#AutocompleteStructuredFormatting) `json:"structured_formatting,omitempty"`
}

AutocompletePrediction represents a single Query Autocomplete result returned from the Google Places API Web Service.

type AutocompleteResponse struct {
 Predictions [][AutocompletePrediction](https://pkg.go.dev/googlemaps.github.io/maps#AutocompletePrediction) `json:"predictions"` }

AutocompleteResponse is a response to a Query Autocomplete request.

type AutocompleteStructuredFormatting struct {
 MainText [string](https://pkg.go.dev/builtin#string) `json:"main_text,omitempty"`  MainTextMatchedSubstrings [][AutocompleteMatchedSubstring](https://pkg.go.dev/googlemaps.github.io/maps#AutocompleteMatchedSubstring) `json:"main_text_matched_substrings,omitempty"`  SecondaryText [string](https://pkg.go.dev/builtin#string) `json:"secondary_text,omitempty"` }

AutocompleteStructuredFormatting contains the main and secondary text of an autocomplete prediction

type AutocompleteTermOffset struct {
	Value [string](https://pkg.go.dev/builtin#string) `json:"value,omitempty"`
	
	Offset [int](https://pkg.go.dev/builtin#int) `json:"offset"`
}

AutocompleteTermOffset identifies each section of the returned description (a section of the description is generally terminated with a comma).

Avoid is for specifying routes that avoid certain features.

type CellTower struct {
	CellID [int](https://pkg.go.dev/builtin#int) `json:"cellId,omitempty"`
	
	LocationAreaCode [int](https://pkg.go.dev/builtin#int) `json:"locationAreaCode,omitempty"`
	MobileCountryCode [int](https://pkg.go.dev/builtin#int) `json:"mobileCountryCode,omitempty"`
	
	MobileNetworkCode [int](https://pkg.go.dev/builtin#int) `json:"mobileNetworkCode,omitempty"`
	
	Age [int](https://pkg.go.dev/builtin#int) `json:"age,omitempty"`
	SignalStrength [int](https://pkg.go.dev/builtin#int) `json:"signalStrength,omitempty"`
	
	TimingAdvance [int](https://pkg.go.dev/builtin#int) `json:"timingAdvance,omitempty"`
}

CellTower is a cell tower object for localisation requests

type Client struct {
	
}

Client may be used to make requests to the Google Maps WebService APIs

func NewClient(options ...[ClientOption](https://pkg.go.dev/googlemaps.github.io/maps#ClientOption)) (*[Client](https://pkg.go.dev/googlemaps.github.io/maps#Client), [error](https://pkg.go.dev/builtin#error))

NewClient constructs a new Client which can make requests to the Google Maps WebService APIs.

Directions issues the Directions request and retrieves the Response

DistanceMatrix makes a Distance Matrix API request

Elevation makes an Elevation API request

FindPlaceFromText takes a text input, and returns a place. The text input can be any kind of Places data, for example, a name, address, or phone number.

Geocode makes a Geocoding API request

Geolocate makes a Geolocation API request

NearbySearch lets you search for places within a specified area. You can refine your search request by supplying keywords or specifying the type of place you are searching for.

NearestRoads makes a Nearest Roads API request

PlaceAutocomplete issues the Places API Place Autocomplete request and retrieves the response

PlaceDetails issues the Places API Place Details request and retrieves the response

PlacePhoto issues the Places API Photo request and retrieves the response

QueryAutocomplete issues the Places API Query Autocomplete request and retrieves the response

ReverseGeocode makes a Reverse Geocoding API request

SnapToRoad makes a Snap to Road API request

SpeedLimits makes a Speed Limits API request

StaticMap makes a StaticMap API request.

TextSearch issues the Places API Text Search request and retrieves the Response

Timezone makes a Timezone API request

type ClientOption func(*[Client](https://pkg.go.dev/googlemaps.github.io/maps#Client)) [error](https://pkg.go.dev/builtin#error)

ClientOption is the type of constructor options for NewClient(...).

WithAPIKey configures a Maps API client with an API Key

#### func [WithAPIKeyAndSignature](https://github.com/googlemaps/google-maps-services-go/blob/v1.7.0/client.go#L115)[¶](https://pkg.go.dev/googlemaps.github.io/maps#WithAPIKeyAndSignature "Go to WithAPIKeyAndSignature")

func WithAPIKeyAndSignature(apiKey, signature [string](https://pkg.go.dev/builtin#string)) [ClientOption](https://pkg.go.dev/googlemaps.github.io/maps#ClientOption)

WithAPIKeyAndSignature configures a Maps API client with an API Key and signature. The signature is assumed to be URL modified Base64 encoded.

WithBaseURL configures a Maps API client with a custom base url

WithChannel configures a Maps API client with a Channel

#### func [WithClientIDAndSignature](https://github.com/googlemaps/google-maps-services-go/blob/v1.7.0/client.go#L162)[¶](https://pkg.go.dev/googlemaps.github.io/maps#WithClientIDAndSignature "Go to WithClientIDAndSignature")

func WithClientIDAndSignature(clientID, signature [string](https://pkg.go.dev/builtin#string)) [ClientOption](https://pkg.go.dev/googlemaps.github.io/maps#ClientOption)

WithClientIDAndSignature configures a Maps API client for a Maps for Work application. The signature is assumed to be URL modified Base64 encoded.

func WithExperienceId(ids ...[string](https://pkg.go.dev/builtin#string)) [ClientOption](https://pkg.go.dev/googlemaps.github.io/maps#ClientOption)

WithExperienceId configures the client with an initial experience id that can be changed with the `setExperienceId` method.

WithHTTPClient configures a Maps API client with a http.Client to make requests over.

func WithRateLimit(requestsPerSecond [int](https://pkg.go.dev/builtin#int)) [ClientOption](https://pkg.go.dev/googlemaps.github.io/maps#ClientOption)

WithRateLimit configures the rate limit for back end requests. Default is to limit to 50 requests per second. A value of zero disables rate limiting.

type CustomIcon struct {
	IconURL [string](https://pkg.go.dev/builtin#string)
	Anchor [Anchor](https://pkg.go.dev/googlemaps.github.io/maps#Anchor)
	Scale [int](https://pkg.go.dev/builtin#int)
}

CustomIcon replace the default Map Pin

DirectionsRequest is the functional options struct for directions.Get

type Distance struct {
	
	
	HumanReadable [string](https://pkg.go.dev/builtin#string) `json:"text"`
	
	
	Meters [int](https://pkg.go.dev/builtin#int) `json:"value"`
}

Distance is the API representation for a distance between two points.

type DistanceMatrixElement struct {
 Status [string](https://pkg.go.dev/builtin#string) `json:"status"` 	Duration [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) `json:"duration"`
	
	DurationInTraffic [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) `json:"duration_in_traffic"`
	Distance [Distance](https://pkg.go.dev/googlemaps.github.io/maps#Distance) `json:"distance"`
}

DistanceMatrixElement is the travel distance and time for a pair of origin and destination.

MarshalJSON implements json.Marshaler for DistanceMatrixElement. This encodes Go types back to the API representation.

UnmarshalJSON implements json.Unmarshaler for DistanceMatrixElement. This decodes the API representation into types useful for Go developers.

type DistanceMatrixElementsRow struct {
 Elements []*[DistanceMatrixElement](https://pkg.go.dev/googlemaps.github.io/maps#DistanceMatrixElement) `json:"elements"` }

DistanceMatrixElementsRow is a row of distance elements.

type DistanceMatrixRequest struct {
	
	Origins [][string](https://pkg.go.dev/builtin#string)
	
	Destinations [][string](https://pkg.go.dev/builtin#string)
	
	
	Mode [Mode](https://pkg.go.dev/googlemaps.github.io/maps#Mode)
	Language [string](https://pkg.go.dev/builtin#string)
	
	Avoid [Avoid](https://pkg.go.dev/googlemaps.github.io/maps#Avoid)
	
	Units [Units](https://pkg.go.dev/googlemaps.github.io/maps#Units)
	
	
	DepartureTime [string](https://pkg.go.dev/builtin#string)
	
	
	ArrivalTime [string](https://pkg.go.dev/builtin#string)
	
	
	
	TrafficModel [TrafficModel](https://pkg.go.dev/googlemaps.github.io/maps#TrafficModel)
	
	
	
	TransitMode [][TransitMode](https://pkg.go.dev/googlemaps.github.io/maps#TransitMode)
	
	
	TransitRoutingPreference [TransitRoutingPreference](https://pkg.go.dev/googlemaps.github.io/maps#TransitRoutingPreference)
}

DistanceMatrixRequest is the request struct for Distance Matrix APi

type DistanceMatrixResponse struct {

	
	OriginAddresses [][string](https://pkg.go.dev/builtin#string) `json:"origin_addresses"`
	
	DestinationAddresses [][string](https://pkg.go.dev/builtin#string) `json:"destination_addresses"`
	Rows [][DistanceMatrixElementsRow](https://pkg.go.dev/googlemaps.github.io/maps#DistanceMatrixElementsRow) `json:"rows"`
}

DistanceMatrixResponse represents a Distance Matrix API response.

type ElevationRequest struct {
	
	Locations [][LatLng](https://pkg.go.dev/googlemaps.github.io/maps#LatLng)
	Path [][LatLng](https://pkg.go.dev/googlemaps.github.io/maps#LatLng)
	
	Samples [int](https://pkg.go.dev/builtin#int)
}

ElevationRequest is the request structure for Elevation API. Either Locations or Path must be set.

type ElevationResult struct {
	Location *[LatLng](https://pkg.go.dev/googlemaps.github.io/maps#LatLng) `json:"location"`
	Elevation [float64](https://pkg.go.dev/builtin#float64) `json:"elevation"`
	
	Resolution [float64](https://pkg.go.dev/builtin#float64) `json:"resolution"`
}

ElevationResult is a single elevation at a specific location

type Fare struct {
	
	Currency [string](https://pkg.go.dev/builtin#string) `json:"currency"`

	Value [float64](https://pkg.go.dev/builtin#float64) `json:"value"`

	Text [string](https://pkg.go.dev/builtin#string) `json:"text"`
}

Fare represents the total fare for a route.

type FindPlaceFromTextInputType [string](https://pkg.go.dev/builtin#string)

FindPlaceFromTextInputType is the different types of inputs.

type FindPlaceFromTextLocationBiasType [string](https://pkg.go.dev/builtin#string)

FindPlaceFromTextLocationBiasType is the type of location bias for this request

func ParseFindPlaceFromTextLocationBiasType(locationBias [string](https://pkg.go.dev/builtin#string)) ([FindPlaceFromTextLocationBiasType](https://pkg.go.dev/googlemaps.github.io/maps#FindPlaceFromTextLocationBiasType), [error](https://pkg.go.dev/builtin#error))

ParseFindPlaceFromTextLocationBiasType will parse a string to a FindPlaceFromTextLocationBiasType

type FindPlaceFromTextRequest struct {
	
	Input [string](https://pkg.go.dev/builtin#string)

	InputType [FindPlaceFromTextInputType](https://pkg.go.dev/googlemaps.github.io/maps#FindPlaceFromTextInputType)

	
	Fields [][PlaceSearchFieldMask](https://pkg.go.dev/googlemaps.github.io/maps#PlaceSearchFieldMask)

	Language [string](https://pkg.go.dev/builtin#string)

	LocationBias [FindPlaceFromTextLocationBiasType](https://pkg.go.dev/googlemaps.github.io/maps#FindPlaceFromTextLocationBiasType)

	LocationBiasPoint *[LatLng](https://pkg.go.dev/googlemaps.github.io/maps#LatLng)

	LocationBiasCenter *[LatLng](https://pkg.go.dev/googlemaps.github.io/maps#LatLng)

	LocationBiasRadius [int](https://pkg.go.dev/builtin#int)

	LocationBiasSouthWest *[LatLng](https://pkg.go.dev/googlemaps.github.io/maps#LatLng)

	LocationBiasNorthEast *[LatLng](https://pkg.go.dev/googlemaps.github.io/maps#LatLng)
}

FindPlaceFromTextRequest is the options struct for Find Place From Text API

type FindPlaceFromTextResponse struct {
 Candidates [][PlacesSearchResult](https://pkg.go.dev/googlemaps.github.io/maps#PlacesSearchResult) HTMLAttributions [][string](https://pkg.go.dev/builtin#string)}

FindPlaceFromTextResponse is a response to the Find Place From Text request

Format defines the format of the resulting image

GeocodeAccuracy is the type of a location result from the Geocoding API.

type GeocodedWaypoint struct {
	
	GeocoderStatus [string](https://pkg.go.dev/builtin#string) `json:"geocoder_status"`
	
	PartialMatch [bool](https://pkg.go.dev/builtin#bool) `json:"partial_match"`
	PlaceID [string](https://pkg.go.dev/builtin#string) `json:"place_id"`
	
	Types [][string](https://pkg.go.dev/builtin#string) `json:"types"`
}

GeocodedWaypoint represents the geocoded point for origin, supplied waypoints, or destination for a requested direction request.

GeocodingRequest is the request structure for Geocoding API

type GeocodingResult struct {
 AddressComponents [][AddressComponent](https://pkg.go.dev/googlemaps.github.io/maps#AddressComponent) `json:"address_components"`  FormattedAddress [string](https://pkg.go.dev/builtin#string) `json:"formatted_address"`  Geometry [AddressGeometry](https://pkg.go.dev/googlemaps.github.io/maps#AddressGeometry) `json:"geometry"`  Types [][string](https://pkg.go.dev/builtin#string) `json:"types"`  PlaceID [string](https://pkg.go.dev/builtin#string) `json:"place_id"` 
	
	
	
	
	
	
	
	
	
	
	PartialMatch [bool](https://pkg.go.dev/builtin#bool) `json:"partial_match"`

	
	
	
	
	
	
	
	
	
	
	PlusCode [AddressPlusCode](https://pkg.go.dev/googlemaps.github.io/maps#AddressPlusCode) `json:"plus_code"`
}

GeocodingResult is a single geocoded address

GeolocationError is an error object reporting a request error

type GeolocationRequest struct {
	
	HomeMobileCountryCode [int](https://pkg.go.dev/builtin#int) `json:"homeMobileCountryCode,omitempty"`
	
	HomeMobileNetworkCode [int](https://pkg.go.dev/builtin#int) `json:"homeMobileNetworkCode,omitempty"`
	
	RadioType [RadioType](https://pkg.go.dev/googlemaps.github.io/maps#RadioType) `json:"radioType,omitempty"`
	Carrier [string](https://pkg.go.dev/builtin#string) `json:"carrier,omitempty"`
	
	ConsiderIP [bool](https://pkg.go.dev/builtin#bool) `json:"considerIp"`
	CellTowers [][CellTower](https://pkg.go.dev/googlemaps.github.io/maps#CellTower) `json:"cellTowers,omitempty"`
	WiFiAccessPoints [][WiFiAccessPoint](https://pkg.go.dev/googlemaps.github.io/maps#WiFiAccessPoint) `json:"wifiAccessPoints,omitempty"`
}

GeolocationRequest is the request structure for Geolocation API All fields are optional

type GeolocationResult struct {
	Location [LatLng](https://pkg.go.dev/googlemaps.github.io/maps#LatLng)
	Accuracy [float64](https://pkg.go.dev/builtin#float64)
}

GeolocationResult is an approximate location and accuracy

type LatLng struct {
 Lat [float64](https://pkg.go.dev/builtin#float64) `json:"lat"`  Lng [float64](https://pkg.go.dev/builtin#float64) `json:"lng"` }

LatLng represents a location on the Earth.

DecodePolyline converts a polyline encoded string to an array of LatLng objects.

ParseLatLng will parse a string representation of a Lat,Lng pair.

ParseLatLngList will parse a string of | separated Lat,Lng pairs.

AlmostEqual returns whether this LatLng is almost equal (below epsilon) to the other LatLng.

type LatLngBounds struct {
 NorthEast [LatLng](https://pkg.go.dev/googlemaps.github.io/maps#LatLng) `json:"northeast"`  SouthWest [LatLng](https://pkg.go.dev/googlemaps.github.io/maps#LatLng) `json:"southwest"` }

LatLngBounds represents a bounded square area on the Earth.

type Leg struct {
	
	Steps []*[Step](https://pkg.go.dev/googlemaps.github.io/maps#Step) `json:"steps"`

	[Distance](https://pkg.go.dev/googlemaps.github.io/maps#Distance) `json:"distance"`

	Duration [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) `json:"duration"`

	
	
	DurationInTraffic [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) `json:"duration_in_traffic"`

	
	ArrivalTime [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time) `json:"arrival_time"`

	
	DepartureTime [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time) `json:"departure_time"`

	
	StartLocation [LatLng](https://pkg.go.dev/googlemaps.github.io/maps#LatLng) `json:"start_location"`

	
	EndLocation [LatLng](https://pkg.go.dev/googlemaps.github.io/maps#LatLng) `json:"end_location"`

	
	StartAddress [string](https://pkg.go.dev/builtin#string) `json:"start_address"`

	
	EndAddress [string](https://pkg.go.dev/builtin#string) `json:"end_address"`

	ViaWaypoint []*[ViaWaypoint](https://pkg.go.dev/googlemaps.github.io/maps#ViaWaypoint) `json:"via_waypoint"`
}

Leg represents a single leg of a route.

MarshalJSON implements json.Marshaler for Leg. This encodes Go types back to the API representation.

UnmarshalJSON implements json.Unmarshaler for Leg. This decodes the API representation into types useful for Go developers.

MapType (optional) defines the type of map to construct. There are several possible maptype values, including roadmap, satellite, hybrid, and terrain

Marker is a Map pin

MarkerSize specifies the size of marker from the set {tiny, mid, small}

Mode is for specifying travel mode.

NearbySearchRequest is the functional options struct for NearbySearch

type NearestRoadsRequest struct {
	Points [][LatLng](https://pkg.go.dev/googlemaps.github.io/maps#LatLng)
}

NearestRoadsRequest is the request structure for the Nearest Roads API.

type NearestRoadsResponse struct {
 SnappedPoints [][SnappedPoint](https://pkg.go.dev/googlemaps.github.io/maps#SnappedPoint) `json:"snappedPoints"` }

NearestRoadsResponse is an array of snapped points.

type OpeningHours struct {
	
	OpenNow *[bool](https://pkg.go.dev/builtin#bool) `json:"open_now,omitempty"`
	
	Periods [][OpeningHoursPeriod](https://pkg.go.dev/googlemaps.github.io/maps#OpeningHoursPeriod) `json:"periods,omitempty"`
	
	WeekdayText [][string](https://pkg.go.dev/builtin#string) `json:"weekday_text,omitempty"`
	
	PermanentlyClosed *[bool](https://pkg.go.dev/builtin#bool) `json:"permanently_closed,omitempty"`
}

OpeningHours describes the opening hours for a Place Details result.

type OpeningHoursOpenClose struct {
	
	Day [time](https://pkg.go.dev/time).[Weekday](https://pkg.go.dev/time#Weekday) `json:"day"`
	
	Time [string](https://pkg.go.dev/builtin#string) `json:"time"`
}

OpeningHoursOpenClose describes when the place is open.

type OpeningHoursPeriod struct {
	Open [OpeningHoursOpenClose](https://pkg.go.dev/googlemaps.github.io/maps#OpeningHoursOpenClose) `json:"open"`
	Close [OpeningHoursOpenClose](https://pkg.go.dev/googlemaps.github.io/maps#OpeningHoursOpenClose) `json:"close"`
}

OpeningHoursPeriod is a single OpeningHours day describing when the place opens and closes.

Path defines a single path of two or more connected points to overlay on the image at specified locations

type Photo struct {
	PhotoReference [string](https://pkg.go.dev/builtin#string) `json:"photo_reference"`
	Height [int](https://pkg.go.dev/builtin#int) `json:"height"`
	Width [int](https://pkg.go.dev/builtin#int) `json:"width"`
	HTMLAttributions [][string](https://pkg.go.dev/builtin#string) `json:"html_attributions"`
}

Photo describes a photo available with a Search Result.

PlaceAutocompleteRequest is the functional options struct for Place Autocomplete

type PlaceAutocompleteSessionToken [uuid](https://pkg.go.dev/github.com/google/uuid).[UUID](https://pkg.go.dev/github.com/google/uuid#UUID)

PlaceAutocompleteSessionToken is a session token for Place Autocomplete.

func NewPlaceAutocompleteSessionToken() [PlaceAutocompleteSessionToken](https://pkg.go.dev/googlemaps.github.io/maps#PlaceAutocompleteSessionToken)

NewPlaceAutocompleteSessionToken constructs a new Place Autocomplete session token.

PlaceDetailsRequest is the functional options struct for PlaceDetails

type PlaceDetailsResult struct {
	
	AddressComponents [][AddressComponent](https://pkg.go.dev/googlemaps.github.io/maps#AddressComponent) `json:"address_components,omitempty"`
	FormattedAddress [string](https://pkg.go.dev/builtin#string) `json:"formatted_address,omitempty"`
	AdrAddress [string](https://pkg.go.dev/builtin#string) `json:"adr_address,omitempty"`
	
	BusinessStatus [string](https://pkg.go.dev/builtin#string) `json:"business_status,omitempty"`
	CurbsidePickup [bool](https://pkg.go.dev/builtin#bool) `json:"curbside_pickup,omitempty"`
	Delivery [bool](https://pkg.go.dev/builtin#bool) `json:"delivery,omitempty"`
	DineIn [bool](https://pkg.go.dev/builtin#bool) `json:"dine_in,omitempty"`
	
	
	
	EditorialSummary *[PlaceEditorialSummary](https://pkg.go.dev/googlemaps.github.io/maps#PlaceEditorialSummary) `json:"editorial_summary,omitempty"`
	
	
	FormattedPhoneNumber [string](https://pkg.go.dev/builtin#string) `json:"formatted_phone_number,omitempty"`
	
	
	
	InternationalPhoneNumber [string](https://pkg.go.dev/builtin#string) `json:"international_phone_number,omitempty"`
	
	
	Geometry [AddressGeometry](https://pkg.go.dev/googlemaps.github.io/maps#AddressGeometry) `json:"geometry,omitempty"`
	
	Icon [string](https://pkg.go.dev/builtin#string) `json:"icon,omitempty"`
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	OpeningHours *[OpeningHours](https://pkg.go.dev/googlemaps.github.io/maps#OpeningHours) `json:"opening_hours,omitempty"`
	
	
	
	
	CurrentOpeningHours *[OpeningHours](https://pkg.go.dev/googlemaps.github.io/maps#OpeningHours) `json:"current_opening_hours,omitempty"`
	
	
	
	
	
	
	
	
	SecondaryOpeningHours [][OpeningHours](https://pkg.go.dev/googlemaps.github.io/maps#OpeningHours) `json:"secondary_opening_hours,omitempty"`
	
	
	
	
	PermanentlyClosed [bool](https://pkg.go.dev/builtin#bool) `json:"permanently_closed,omitempty"`
	Photos [][Photo](https://pkg.go.dev/googlemaps.github.io/maps#Photo) `json:"photos,omitempty"`
	PlaceID [string](https://pkg.go.dev/builtin#string) `json:"place_id,omitempty"`
	PriceLevel [int](https://pkg.go.dev/builtin#int) `json:"price_level,omitempty"`
	
	Rating [float32](https://pkg.go.dev/builtin#float32) `json:"rating,omitempty"`
	Reservable [bool](https://pkg.go.dev/builtin#bool) `json:"reservable,omitempty"`
	
	
	Reviews [][PlaceReview](https://pkg.go.dev/googlemaps.github.io/maps#PlaceReview) `json:"reviews,omitempty"`
	ServesBeer [bool](https://pkg.go.dev/builtin#bool) `json:"serves_beer,omitempty"`
	ServesBreakfast [bool](https://pkg.go.dev/builtin#bool) `json:"serves_breakfast,omitempty"`
	ServesBrunch [bool](https://pkg.go.dev/builtin#bool) `json:"serves_brunch,omitempty"`
	ServesDinner [bool](https://pkg.go.dev/builtin#bool) `json:"serves_dinner,omitempty"`
	ServesLunch [bool](https://pkg.go.dev/builtin#bool) `json:"serves_lunch,omitempty"`
	ServesVegetarianFood [bool](https://pkg.go.dev/builtin#bool) `json:"serves_vegetarian_food,omitempty"`
	ServesWine [bool](https://pkg.go.dev/builtin#bool) `json:"serves_wine,omitempty"`
	Takeout [bool](https://pkg.go.dev/builtin#bool) `json:"takeout,omitempty"`
	Types [][string](https://pkg.go.dev/builtin#string) `json:"types,omitempty"`
	
	
	
	
	URL [string](https://pkg.go.dev/builtin#string) `json:"url,omitempty"`
	UserRatingsTotal [int](https://pkg.go.dev/builtin#int) `json:"user_ratings_total,omitempty"`
	
	
	
	UTCOffset *[int](https://pkg.go.dev/builtin#int) `json:"utc_offset,omitempty"`
	Vicinity [string](https://pkg.go.dev/builtin#string) `json:"vicinity,omitempty"`
	
	Website [string](https://pkg.go.dev/builtin#string) `json:"website,omitempty"`
	
	WheelchairAccessibleEntrance [bool](https://pkg.go.dev/builtin#bool) `json:"wheelchair_accessible_entrance,omitempty"`
	
	HTMLAttributions [][string](https://pkg.go.dev/builtin#string) `json:"html_attributions,omitempty"`
}

PlaceDetailsResult is an individual Places API Place Details result

type PlaceEditorialSummary struct {
	Language [string](https://pkg.go.dev/builtin#string) `json:"language,omitempty"`
	Overview [string](https://pkg.go.dev/builtin#string) `json:"overview,omitempty"`
}

PlaceEditorialSummary contains a summary of the place. A summary is comprised of a textual overview, and also includes the language code for these if applicable. Summary text must be presented as-is and can not be modified or altered.

type PlacePhotoRequest struct {
	
	PhotoReference [string](https://pkg.go.dev/builtin#string)
	
	MaxHeight [uint](https://pkg.go.dev/builtin#uint)
	
	MaxWidth [uint](https://pkg.go.dev/builtin#uint)
}

PlacePhotoRequest is the functional options struct for Places Photo API

PlacePhotoResponse is a response to the Place Photo request

Image will read and close response.Data and return it as an image.

type PlaceReview struct {
	
	
	Aspects [][PlaceReviewAspect](https://pkg.go.dev/googlemaps.github.io/maps#PlaceReviewAspect) `json:"aspects,omitempty"`
	
	AuthorName [string](https://pkg.go.dev/builtin#string) `json:"author_name,omitempty"`
	AuthorURL [string](https://pkg.go.dev/builtin#string) `json:"author_url,omitempty"`
	AuthorProfilePhoto [string](https://pkg.go.dev/builtin#string) `json:"profile_photo_url"`
	
	
	Language [string](https://pkg.go.dev/builtin#string) `json:"language,omitempty"`
	
	Rating [int](https://pkg.go.dev/builtin#int) `json:"rating,omitempty"`
	
	RelativeTimeDescription [string](https://pkg.go.dev/builtin#string) `json:"relative_time_description,omitempty"`
	
	
	Text [string](https://pkg.go.dev/builtin#string) `json:"text,omitempty"`
	
	Time [int](https://pkg.go.dev/builtin#int) `json:"time,omitempty"` 
}

PlaceReview is a review of a Place

type PlaceReviewAspect struct {
	Rating [int](https://pkg.go.dev/builtin#int) `json:"rating"`
	
	
	Type [string](https://pkg.go.dev/builtin#string) `json:"type,omitempty"`
}

PlaceReviewAspect provides a rating of a single attribute of the establishment.

PlaceType restricts Place API search to the results to places matching the specified type.

ParsePlaceType will parse a string representation of a PlaceType.

type PlacesSearchResponse struct {
	Results [][PlacesSearchResult](https://pkg.go.dev/googlemaps.github.io/maps#PlacesSearchResult)
	
	HTMLAttributions [][string](https://pkg.go.dev/builtin#string)
	
	NextPageToken [string](https://pkg.go.dev/builtin#string)
}

PlacesSearchResponse is the response to a Places API Search request.

type PlacesSearchResult struct {
	FormattedAddress [string](https://pkg.go.dev/builtin#string) `json:"formatted_address,omitempty"`
	
	
	Geometry [AddressGeometry](https://pkg.go.dev/googlemaps.github.io/maps#AddressGeometry) `json:"geometry,omitempty"`
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	Icon [string](https://pkg.go.dev/builtin#string) `json:"icon,omitempty"`
	PlaceID [string](https://pkg.go.dev/builtin#string) `json:"place_id,omitempty"`
	
	Rating [float32](https://pkg.go.dev/builtin#float32) `json:"rating,omitempty"`
	UserRatingsTotal [int](https://pkg.go.dev/builtin#int) `json:"user_ratings_total,omitempty"`
	Types [][string](https://pkg.go.dev/builtin#string) `json:"types,omitempty"`
	OpeningHours *[OpeningHours](https://pkg.go.dev/googlemaps.github.io/maps#OpeningHours) `json:"opening_hours,omitempty"`
	Photos [][Photo](https://pkg.go.dev/googlemaps.github.io/maps#Photo) `json:"photos,omitempty"`
	PriceLevel [int](https://pkg.go.dev/builtin#int) `json:"price_level,omitempty"`
	Vicinity [string](https://pkg.go.dev/builtin#string) `json:"vicinity,omitempty"`
	
	PermanentlyClosed [bool](https://pkg.go.dev/builtin#bool) `json:"permanently_closed,omitempty"`
	
	BusinessStatus [string](https://pkg.go.dev/builtin#string) `json:"business_status,omitempty"`
	ID [string](https://pkg.go.dev/builtin#string) `json:"id,omitempty"`
}

PlacesSearchResult is an individual Places API search result

PriceLevel is the Price Levels for Places API

type QueryAutocompleteRequest struct {
	
	
	Input [string](https://pkg.go.dev/builtin#string)
	
	
	
	
	Offset [uint](https://pkg.go.dev/builtin#uint)
	Location *[LatLng](https://pkg.go.dev/googlemaps.github.io/maps#LatLng)
	
	
	Radius [uint](https://pkg.go.dev/builtin#uint)
	Language [string](https://pkg.go.dev/builtin#string)
}

QueryAutocompleteRequest is the functional options struct for Query Autocomplete

RadioType defines mobile radio types

const (
 RadioTypeLTE [RadioType](https://pkg.go.dev/googlemaps.github.io/maps#RadioType) = "lte"  RadioTypeGSM [RadioType](https://pkg.go.dev/googlemaps.github.io/maps#RadioType) = "gsm"  RadioTypeCDMA [RadioType](https://pkg.go.dev/googlemaps.github.io/maps#RadioType) = "cdma"  RadioTypeWCDMA [RadioType](https://pkg.go.dev/googlemaps.github.io/maps#RadioType) = "wcdma" )

Allowed radio types

RankBy specifies the order in which results are listed.

type Route struct {
	
	Summary [string](https://pkg.go.dev/builtin#string) `json:"summary"`

	
	
	
	Legs []*[Leg](https://pkg.go.dev/googlemaps.github.io/maps#Leg) `json:"legs"`

	
	WaypointOrder [][int](https://pkg.go.dev/builtin#int) `json:"waypoint_order"`

	
	OverviewPolyline [Polyline](https://pkg.go.dev/googlemaps.github.io/maps#Polyline) `json:"overview_polyline"`

	Bounds [LatLngBounds](https://pkg.go.dev/googlemaps.github.io/maps#LatLngBounds) `json:"bounds"`

	
	Copyrights [string](https://pkg.go.dev/builtin#string) `json:"copyrights"`

	
	Warnings [][string](https://pkg.go.dev/builtin#string) `json:"warnings"`

	
	
	*[Fare](https://pkg.go.dev/googlemaps.github.io/maps#Fare) `json:"fare"`
}

Route represents a single route between an origin and a destination.

type SnapToRoadRequest struct {
	Path [][LatLng](https://pkg.go.dev/googlemaps.github.io/maps#LatLng)

	
	Interpolate [bool](https://pkg.go.dev/builtin#bool)
}

SnapToRoadRequest is the request structure for the Roads Snap to Road API.

type SnapToRoadResponse struct {
 SnappedPoints [][SnappedPoint](https://pkg.go.dev/googlemaps.github.io/maps#SnappedPoint) `json:"snappedPoints"` }

SnapToRoadResponse is an array of snapped points.

type SnappedPoint struct {
	Location [LatLng](https://pkg.go.dev/googlemaps.github.io/maps#LatLng) `json:"location"`

	
	OriginalIndex *[int](https://pkg.go.dev/builtin#int) `json:"originalIndex"`

	PlaceID [string](https://pkg.go.dev/builtin#string) `json:"placeId"`
}

SnappedPoint is the original path point snapped to a road.

MarshalJSON implements json.Marshaler for SnappedPoint. This encodes Go types back to the API representation.

UnmarshalJSON implements json.Unmarshaler for SnappedPoint. This decode the API representation into types useful for Go developers.

type SpeedLimit struct {
	PlaceID [string](https://pkg.go.dev/builtin#string) `json:"placeId"`
	SpeedLimit [float64](https://pkg.go.dev/builtin#float64) `json:"speedLimit"`
	Units speedLimitUnit `json:"units"`
}

SpeedLimit is the speed limit for a PlaceID

type SpeedLimitsRequest struct {
	Path [][LatLng](https://pkg.go.dev/googlemaps.github.io/maps#LatLng)

	PlaceID [][string](https://pkg.go.dev/builtin#string)

	
	Units speedLimitUnit
}

SpeedLimitsRequest is the request structure for the Roads Speed Limits API.

type SpeedLimitsResponse struct {
 SpeedLimits [][SpeedLimit](https://pkg.go.dev/googlemaps.github.io/maps#SpeedLimit) `json:"speedLimits"`  SnappedPoints [][SnappedPoint](https://pkg.go.dev/googlemaps.github.io/maps#SnappedPoint) `json:"snappedPoints"` }

SpeedLimitsResponse is an array of snapped points and an array of speed limits.

StaticMapRequest is the functional options struct for staticMap.Get

type Step struct {
	
	HTMLInstructions [string](https://pkg.go.dev/builtin#string) `json:"html_instructions"`

	[Distance](https://pkg.go.dev/googlemaps.github.io/maps#Distance) `json:"distance"`

	
	[time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) `json:"duration"`

	
	StartLocation [LatLng](https://pkg.go.dev/googlemaps.github.io/maps#LatLng) `json:"start_location"`

	
	EndLocation [LatLng](https://pkg.go.dev/googlemaps.github.io/maps#LatLng) `json:"end_location"`

	
	
	[Polyline](https://pkg.go.dev/googlemaps.github.io/maps#Polyline) `json:"polyline"`

	
	
	Steps []*[Step](https://pkg.go.dev/googlemaps.github.io/maps#Step) `json:"steps"`

	
	TransitDetails *[TransitDetails](https://pkg.go.dev/googlemaps.github.io/maps#TransitDetails) `json:"transit_details"`

	TravelMode [string](https://pkg.go.dev/builtin#string) `json:"travel_mode"`
}

Step represents a single step of a leg.

MarshalJSON implements json.Marshaler for Step. This encodes Go types back to the API representation.

UnmarshalJSON implements json.Unmarshaler for Step. This decodes the API representation into types useful for Go developers.

TextSearchRequest is the functional options struct for TextSearch

type TimezoneRequest struct {
	Location *[LatLng](https://pkg.go.dev/googlemaps.github.io/maps#LatLng)
	
	Timestamp [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time)
	Language [string](https://pkg.go.dev/builtin#string)
}

TimezoneRequest is the request structure for Timezone API.

type TimezoneResult struct {
	DstOffset [int](https://pkg.go.dev/builtin#int) `json:"dstOffset"`
	RawOffset [int](https://pkg.go.dev/builtin#int) `json:"rawOffset"`
	TimeZoneID [string](https://pkg.go.dev/builtin#string) `json:"timeZoneId"`
	TimeZoneName [string](https://pkg.go.dev/builtin#string) `json:"timeZoneName"`
}

TimezoneResult is a single timezone result.

TrafficModel specifies traffic prediction model when requesting future directions.

type TransitAgency struct {
	Name [string](https://pkg.go.dev/builtin#string) `json:"name"`
	URL *[url](https://pkg.go.dev/net/url).[URL](https://pkg.go.dev/net/url#URL) `json:"url"`
	Phone [string](https://pkg.go.dev/builtin#string) `json:"phone"`
}

TransitAgency contains information about the operator of the line

func (transitAgency *[TransitAgency](https://pkg.go.dev/googlemaps.github.io/maps#TransitAgency)) MarshalJSON() ([][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))

MarshalJSON implements json.Marshaler for TransitAgency. This encodes Go types back to the API representation.

func (transitAgency *[TransitAgency](https://pkg.go.dev/googlemaps.github.io/maps#TransitAgency)) UnmarshalJSON(data [][byte](https://pkg.go.dev/builtin#byte)) [error](https://pkg.go.dev/builtin#error)

UnmarshalJSON imlpements json.Unmarshaler for TransitAgency. This decodes the API representation into types useful for Go developers.

type TransitDetails struct {
	
	ArrivalStop [TransitStop](https://pkg.go.dev/googlemaps.github.io/maps#TransitStop) `json:"arrival_stop"`
	
	DepartureStop [TransitStop](https://pkg.go.dev/googlemaps.github.io/maps#TransitStop) `json:"departure_stop"`
	ArrivalTime [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time) `json:"arrival_time"`
	DepartureTime [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time) `json:"departure_time"`
	
	Headsign [string](https://pkg.go.dev/builtin#string) `json:"headsign"`
	
	Headway [time](https://pkg.go.dev/time).[Duration](https://pkg.go.dev/time#Duration) `json:"headway"`
	
	NumStops [uint](https://pkg.go.dev/builtin#uint) `json:"num_stops"`
	Line [TransitLine](https://pkg.go.dev/googlemaps.github.io/maps#TransitLine) `json:"line"`
	
	TripShortName [string](https://pkg.go.dev/builtin#string) `json:"trip_short_name"`
}

TransitDetails contains additional information about the transit stop, transit line and transit agency.

func (transitDetails *[TransitDetails](https://pkg.go.dev/googlemaps.github.io/maps#TransitDetails)) MarshalJSON() ([][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))

MarshalJSON implements json.Marshaler for TransitDetails. This encodes Go types back to the API representation.

func (transitDetails *[TransitDetails](https://pkg.go.dev/googlemaps.github.io/maps#TransitDetails)) UnmarshalJSON(data [][byte](https://pkg.go.dev/builtin#byte)) [error](https://pkg.go.dev/builtin#error)

UnmarshalJSON implements json.Unmarshaler for TransitDetails. This decodes the API representation into types useful for Go developers.

type TransitLine struct {
	Name [string](https://pkg.go.dev/builtin#string) `json:"name"`
	ShortName [string](https://pkg.go.dev/builtin#string) `json:"short_name"`
	Color [string](https://pkg.go.dev/builtin#string) `json:"color"`
	Agencies []*[TransitAgency](https://pkg.go.dev/googlemaps.github.io/maps#TransitAgency) `json:"agencies"`
	URL *[url](https://pkg.go.dev/net/url).[URL](https://pkg.go.dev/net/url#URL) `json:"url"`
	Icon *[url](https://pkg.go.dev/net/url).[URL](https://pkg.go.dev/net/url#URL) `json:"icon"`
	TextColor [string](https://pkg.go.dev/builtin#string) `json:"text_color"`
	Vehicle [TransitLineVehicle](https://pkg.go.dev/googlemaps.github.io/maps#TransitLineVehicle) `json:"vehicle"`
}

TransitLine contains information about the transit line used in this step

MarshalJSON implements json.Marshaler for TransitLine. This encodes Go types back to the API representation.

func (transitLine *[TransitLine](https://pkg.go.dev/googlemaps.github.io/maps#TransitLine)) UnmarshalJSON(data [][byte](https://pkg.go.dev/builtin#byte)) [error](https://pkg.go.dev/builtin#error)

UnmarshalJSON imlpements json.Unmarshaler for TransitLine. This decodes the API representation into types useful for Go developers.

type TransitLineVehicle struct {
	Name [string](https://pkg.go.dev/builtin#string) `json:"name"`
	Type [string](https://pkg.go.dev/builtin#string) `json:"type"`
	Icon *[url](https://pkg.go.dev/net/url).[URL](https://pkg.go.dev/net/url#URL) `json:"icon"`
}

TransitLineVehicle contains the type of vehicle used on this line

func (transitLineVehicle *[TransitLineVehicle](https://pkg.go.dev/googlemaps.github.io/maps#TransitLineVehicle)) MarshalJSON() ([][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))

MarshalJSON implements json.Marshaler for TransitLineVehicle. This encodes Go types back to the API representation.

func (transitLineVehicle *[TransitLineVehicle](https://pkg.go.dev/googlemaps.github.io/maps#TransitLineVehicle)) UnmarshalJSON(data [][byte](https://pkg.go.dev/builtin#byte)) [error](https://pkg.go.dev/builtin#error)

UnmarshalJSON imlpements json.Unmarshaler for TransitLineVehicle. This decodes the API representation into types useful for Go developers.

TransitMode is for specifying a transit mode for a request

type TransitRoutingPreference [string](https://pkg.go.dev/builtin#string)

TransitRoutingPreference biases which routes are returned

type TransitStop struct {
	Location [LatLng](https://pkg.go.dev/googlemaps.github.io/maps#LatLng) `json:"location"`
	Name [string](https://pkg.go.dev/builtin#string) `json:"name"`
}

TransitStop contains information about the stop/station for this part of the trip.

Units specifies which units system to return human readable results in.

type ViaWaypoint struct {
 Location [LatLng](https://pkg.go.dev/googlemaps.github.io/maps#LatLng) `json:"location"`  StepIndex [int](https://pkg.go.dev/builtin#int) `json:"step_index"`  StepInterpolation [float64](https://pkg.go.dev/builtin#float64) `json:"step_interpolation"` }

ViaWaypoint handles waypoints.

type WiFiAccessPoint struct {
	MACAddress [string](https://pkg.go.dev/builtin#string) `json:"macAddress,omitempty"`
	SignalStrength [float64](https://pkg.go.dev/builtin#float64) `json:"signalStrength,omitempty"`
	Age [uint64](https://pkg.go.dev/builtin#uint64) `json:"age,omitempty"`
	
	Channel [int](https://pkg.go.dev/builtin#int) `json:"channel,omitempty"`
	SignalToNoiseRatio [float64](https://pkg.go.dev/builtin#float64) `json:"signalToNoiseRatio,omitempty"`
}

WiFiAccessPoint is a WiFi access point object for localisation requests
