# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1

Title: airquality package - google.golang.org/api/airquality/v1 - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1

Markdown Content:
Package airquality provides access to the Air Quality API.

For product documentation, see: [https://developers.google.com/maps/documentation/air-quality](https://developers.google.com/maps/documentation/air-quality)

#### Library status [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#hdr-Library_status "Go to Library status")

These client libraries are officially supported by Google. However, this library is considered complete and is in maintenance mode. This means that we will address critical bugs and security issues but will not add any new features.

When possible, we recommend using our newer [Cloud Client Libraries for Go]([https://pkg.go.dev/cloud.google.com/go](https://pkg.go.dev/cloud.google.com/go)) that are still actively being worked and iterated on.

#### Creating a client [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#hdr-Creating_a_client "Go to Creating a client")

Usage example:

import "google.golang.org/api/airquality/v1"
...
ctx := context.Background()
airqualityService, err := airquality.NewService(ctx)

In this example, Google Application Default Credentials are used for authentication. For information on how to create and obtain Application Default Credentials, see [https://developers.google.com/identity/protocols/application-default-credentials](https://developers.google.com/identity/protocols/application-default-credentials).

#### Other authentication options [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#hdr-Other_authentication_options "Go to Other authentication options")

To use an API key for authentication (note: some APIs do not support API keys), use [google.golang.org/api/option.WithAPIKey](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#WithAPIKey):

airqualityService, err := airquality.NewService(ctx, option.WithAPIKey("AIza..."))

To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow, use [google.golang.org/api/option.WithTokenSource](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#WithTokenSource):

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
airqualityService, err := airquality.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))

See [google.golang.org/api/option.ClientOption](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#ClientOption) for details on options.

*   [Constants](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#pkg-constants)
*   [type AdditionalInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#AdditionalInfo)
*       *   [func (s AdditionalInfo) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#AdditionalInfo.MarshalJSON)

*   [type AirQualityIndex](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#AirQualityIndex)
*       *   [func (s AirQualityIndex) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#AirQualityIndex.MarshalJSON)

*   [type Color](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#Color)
*       *   [func (s Color) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#Color.MarshalJSON)
    *   [func (s *Color) UnmarshalJSON(data []byte) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#Color.UnmarshalJSON)

*   [type Concentration](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#Concentration)
*       *   [func (s Concentration) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#Concentration.MarshalJSON)
    *   [func (s *Concentration) UnmarshalJSON(data []byte) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#Concentration.UnmarshalJSON)

*   [type CurrentConditionsLookupCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#CurrentConditionsLookupCall)
*       *   [func (c *CurrentConditionsLookupCall) Context(ctx context.Context) *CurrentConditionsLookupCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#CurrentConditionsLookupCall.Context)
    *   [func (c *CurrentConditionsLookupCall) Do(opts ...googleapi.CallOption) (*LookupCurrentConditionsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#CurrentConditionsLookupCall.Do)
    *   [func (c *CurrentConditionsLookupCall) Fields(s ...googleapi.Field) *CurrentConditionsLookupCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#CurrentConditionsLookupCall.Fields)
    *   [func (c *CurrentConditionsLookupCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#CurrentConditionsLookupCall.Header)

*   [type CurrentConditionsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#CurrentConditionsService)
*       *   [func NewCurrentConditionsService(s *Service) *CurrentConditionsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#NewCurrentConditionsService)

*       *   [func (r *CurrentConditionsService) Lookup(lookupcurrentconditionsrequest *LookupCurrentConditionsRequest) *CurrentConditionsLookupCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#CurrentConditionsService.Lookup)

*   [type CustomLocalAqi](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#CustomLocalAqi)
*       *   [func (s CustomLocalAqi) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#CustomLocalAqi.MarshalJSON)

*   [type ForecastLookupCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#ForecastLookupCall)
*       *   [func (c *ForecastLookupCall) Context(ctx context.Context) *ForecastLookupCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#ForecastLookupCall.Context)
    *   [func (c *ForecastLookupCall) Do(opts ...googleapi.CallOption) (*LookupForecastResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#ForecastLookupCall.Do)
    *   [func (c *ForecastLookupCall) Fields(s ...googleapi.Field) *ForecastLookupCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#ForecastLookupCall.Fields)
    *   [func (c *ForecastLookupCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#ForecastLookupCall.Header)
    *   [func (c *ForecastLookupCall) Pages(ctx context.Context, f func(*LookupForecastResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#ForecastLookupCall.Pages)

*   [type ForecastService](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#ForecastService)
*       *   [func NewForecastService(s *Service) *ForecastService](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#NewForecastService)

*       *   [func (r *ForecastService) Lookup(lookupforecastrequest *LookupForecastRequest) *ForecastLookupCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#ForecastService.Lookup)

*   [type HealthRecommendations](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#HealthRecommendations)
*       *   [func (s HealthRecommendations) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#HealthRecommendations.MarshalJSON)

*   [type HistoryLookupCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#HistoryLookupCall)
*       *   [func (c *HistoryLookupCall) Context(ctx context.Context) *HistoryLookupCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#HistoryLookupCall.Context)
    *   [func (c *HistoryLookupCall) Do(opts ...googleapi.CallOption) (*LookupHistoryResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#HistoryLookupCall.Do)
    *   [func (c *HistoryLookupCall) Fields(s ...googleapi.Field) *HistoryLookupCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#HistoryLookupCall.Fields)
    *   [func (c *HistoryLookupCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#HistoryLookupCall.Header)
    *   [func (c *HistoryLookupCall) Pages(ctx context.Context, f func(*LookupHistoryResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#HistoryLookupCall.Pages)

*   [type HistoryService](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#HistoryService)
*       *   [func NewHistoryService(s *Service) *HistoryService](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#NewHistoryService)

*       *   [func (r *HistoryService) Lookup(lookuphistoryrequest *LookupHistoryRequest) *HistoryLookupCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#HistoryService.Lookup)

*   [type HourInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#HourInfo)
*       *   [func (s HourInfo) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#HourInfo.MarshalJSON)

*   [type HourlyForecast](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#HourlyForecast)
*       *   [func (s HourlyForecast) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#HourlyForecast.MarshalJSON)

*   [type HttpBody](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#HttpBody)
*       *   [func (s HttpBody) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#HttpBody.MarshalJSON)

*   [type Interval](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#Interval)
*       *   [func (s Interval) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#Interval.MarshalJSON)

*   [type LatLng](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#LatLng)
*       *   [func (s LatLng) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#LatLng.MarshalJSON)
    *   [func (s *LatLng) UnmarshalJSON(data []byte) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#LatLng.UnmarshalJSON)

*   [type LookupCurrentConditionsRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#LookupCurrentConditionsRequest)
*       *   [func (s LookupCurrentConditionsRequest) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#LookupCurrentConditionsRequest.MarshalJSON)

*   [type LookupCurrentConditionsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#LookupCurrentConditionsResponse)
*       *   [func (s LookupCurrentConditionsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#LookupCurrentConditionsResponse.MarshalJSON)

*   [type LookupForecastRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#LookupForecastRequest)
*       *   [func (s LookupForecastRequest) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#LookupForecastRequest.MarshalJSON)

*   [type LookupForecastResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#LookupForecastResponse)
*       *   [func (s LookupForecastResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#LookupForecastResponse.MarshalJSON)

*   [type LookupHistoryRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#LookupHistoryRequest)
*       *   [func (s LookupHistoryRequest) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#LookupHistoryRequest.MarshalJSON)

*   [type LookupHistoryResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#LookupHistoryResponse)
*       *   [func (s LookupHistoryResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#LookupHistoryResponse.MarshalJSON)

*   [type MapTypesHeatmapTilesLookupHeatmapTileCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#MapTypesHeatmapTilesLookupHeatmapTileCall)
*       *   [func (c *MapTypesHeatmapTilesLookupHeatmapTileCall) Context(ctx context.Context) *MapTypesHeatmapTilesLookupHeatmapTileCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#MapTypesHeatmapTilesLookupHeatmapTileCall.Context)
    *   [func (c *MapTypesHeatmapTilesLookupHeatmapTileCall) Do(opts ...googleapi.CallOption) (*HttpBody, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#MapTypesHeatmapTilesLookupHeatmapTileCall.Do)
    *   [func (c *MapTypesHeatmapTilesLookupHeatmapTileCall) Fields(s ...googleapi.Field) *MapTypesHeatmapTilesLookupHeatmapTileCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#MapTypesHeatmapTilesLookupHeatmapTileCall.Fields)
    *   [func (c *MapTypesHeatmapTilesLookupHeatmapTileCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#MapTypesHeatmapTilesLookupHeatmapTileCall.Header)
    *   [func (c *MapTypesHeatmapTilesLookupHeatmapTileCall) IfNoneMatch(entityTag string) *MapTypesHeatmapTilesLookupHeatmapTileCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#MapTypesHeatmapTilesLookupHeatmapTileCall.IfNoneMatch)

*   [type MapTypesHeatmapTilesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#MapTypesHeatmapTilesService)
*       *   [func NewMapTypesHeatmapTilesService(s *Service) *MapTypesHeatmapTilesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#NewMapTypesHeatmapTilesService)

*       *   [func (r *MapTypesHeatmapTilesService) LookupHeatmapTile(mapType string, zoom int64, x int64, y int64) *MapTypesHeatmapTilesLookupHeatmapTileCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#MapTypesHeatmapTilesService.LookupHeatmapTile)

*   [type MapTypesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#MapTypesService)
*       *   [func NewMapTypesService(s *Service) *MapTypesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#NewMapTypesService)

*   [type Pollutant](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#Pollutant)
*       *   [func (s Pollutant) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#Pollutant.MarshalJSON)

*   [type Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#Service)
*       *   [func New(client *http.Client) (*Service, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#New)deprecated
    *   [func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#NewService)

[View Source](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/airquality/v1/airquality-gen.go#L100)

const (
	
	CloudPlatformScope = "https://www.googleapis.com/auth/cloud-platform"
)

OAuth2 scopes used by this API.

This section is empty.

This section is empty.

type AdditionalInfo struct {
	Effects [string](https://pkg.go.dev/builtin#string) `json:"effects,omitempty"`
	Sources [string](https://pkg.go.dev/builtin#string) `json:"sources,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

AdditionalInfo: The emission sources and health effects of a given pollutant.

type AirQualityIndex struct {
	
	
	
	
	Aqi [int64](https://pkg.go.dev/builtin#int64) `json:"aqi,omitempty"`
	
	
	
	AqiDisplay [string](https://pkg.go.dev/builtin#string) `json:"aqiDisplay,omitempty"`
	
	Category [string](https://pkg.go.dev/builtin#string) `json:"category,omitempty"`
	
	
	Code [string](https://pkg.go.dev/builtin#string) `json:"code,omitempty"`
	Color *[Color](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#Color) `json:"color,omitempty"`
	
	DisplayName [string](https://pkg.go.dev/builtin#string) `json:"displayName,omitempty"`
	
	DominantPollutant [string](https://pkg.go.dev/builtin#string) `json:"dominantPollutant,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

AirQualityIndex: The basic object for representing different air quality metrics. When brought together, these metrics provide a snapshot about the current air quality conditions. There are multiple indexes in the world serving different purposes and groups interested in measuring different aspects of air quality.

type Color struct {
	
	
	
	
	
	
	
	
	Alpha [float64](https://pkg.go.dev/builtin#float64) `json:"alpha,omitempty"`
	Blue [float64](https://pkg.go.dev/builtin#float64) `json:"blue,omitempty"`
	Green [float64](https://pkg.go.dev/builtin#float64) `json:"green,omitempty"`
	Red [float64](https://pkg.go.dev/builtin#float64) `json:"red,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Color: Represents a color in the RGBA color space. This representation is designed for simplicity of conversion to and from color representations in various languages over compactness. For example, the fields of this representation can be trivially provided to the constructor of `java.awt.Color` in Java; it can also be trivially provided to UIColor's `+colorWithRed:green:blue:alpha` method in iOS; and, with just a little work, it can be easily formatted into a CSS `rgba()` string in JavaScript. This reference page doesn't have information about the absolute color space that should be used to interpret the RGB value—for example, sRGB, Adobe RGB, DCI-P3, and BT.2020. By default, applications should assume the sRGB color space. When color equality needs to be decided, implementations, unless documented otherwise, treat two colors as equal if all their red, green, blue, and alpha values each differ by at most `1e-5`. Example (Java): import com.google.type.Color; // ... public static java.awt.Color fromProto(Color protocolor) { float alpha = protocolor.hasAlpha() ? protocolor.getAlpha().getValue() : 1.0; return new java.awt.Color( protocolor.getRed(), protocolor.getGreen(), protocolor.getBlue(), alpha); } public static Color toProto(java.awt.Color color) { float red = (float) color.getRed(); float green = (float) color.getGreen(); float blue = (float) color.getBlue(); float denominator = 255.0; Color.Builder resultBuilder = Color .newBuilder() .setRed(red / denominator) .setGreen(green / denominator) .setBlue(blue / denominator); int alpha = color.getAlpha(); if (alpha != 255) { result.setAlpha( FloatValue .newBuilder() .setValue(((float) alpha) / denominator) .build()); } return resultBuilder.build(); } // ... Example (iOS / Obj-C): // ... static UIColor* fromProto(Color* protocolor) { float red = [protocolor red]; float green = [protocolor green]; float blue = [protocolor blue]; FloatValue* alpha_wrapper = [protocolor alpha]; float alpha = 1.0; if (alpha_wrapper != nil) { alpha = [alpha_wrapper value]; } return [UIColor colorWithRed:red green:green blue:blue alpha:alpha]; } static Color* toProto(UIColor* color) { CGFloat red, green, blue, alpha; if (![color getRed:&red green:&green blue:&blue alpha:&alpha]) { return nil; } Color* result = [[Color alloc] init]; [result setRed:red]; [result setGreen:green]; [result setBlue:blue]; if (alpha <= 0.9999) { [result setAlpha:floatWrapperWithValue(alpha)]; } [result autorelease]; return result; } // ... Example (JavaScript): // ... var protoToCssColor = function(rgb_color) { var redFrac = rgb_color.red || 0.0; var greenFrac = rgb_color.green || 0.0; var blueFrac = rgb_color.blue || 0.0; var red = Math.floor(redFrac * 255); var green = Math.floor(greenFrac * 255); var blue = Math.floor(blueFrac * 255); if (!('alpha' in rgb_color)) { return rgbToCssColor(red, green, blue); } var alphaFrac = rgb_color.alpha.value || 0.0; var rgbParams = [red, green, blue].join(','); return ['rgba(', rgbParams, ',', alphaFrac, ')'].join(”); }; var rgbToCssColor = function(red, green, blue) { var rgbNumber = new Number((red << 16) | (green << 8) | blue); var hexString = rgbNumber.toString(16); var missingZeros = 6 - hexString.length; var resultBuilder = ['#']; for (var i = 0; i < missingZeros; i++) { resultBuilder.push('0'); } resultBuilder.push(hexString); return resultBuilder.join(”); }; // ...

type Concentration struct {
	
	
	
	
	
	
	Units [string](https://pkg.go.dev/builtin#string) `json:"units,omitempty"`
	Value [float64](https://pkg.go.dev/builtin#float64) `json:"value,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Concentration: The concentration of a given pollutant in the air.

type CurrentConditionsLookupCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "airquality.currentConditions.lookup" call. Any non-2xx status code is an error. Response headers are in either *LookupCurrentConditionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type CurrentConditionsService struct {
	
}

func NewCurrentConditionsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#Service)) *[CurrentConditionsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#CurrentConditionsService)

func (r *[CurrentConditionsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#CurrentConditionsService)) Lookup(lookupcurrentconditionsrequest *[LookupCurrentConditionsRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#LookupCurrentConditionsRequest)) *[CurrentConditionsLookupCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#CurrentConditionsLookupCall)

Lookup: The Current Conditions endpoint provides hourly air quality information in more than 100 countries, up to a 500 x 500 meters resolution. Includes over 70 local indexes and global air quality index and categories.

type CustomLocalAqi struct {
	
	Aqi [string](https://pkg.go.dev/builtin#string) `json:"aqi,omitempty"`
	
	
	RegionCode [string](https://pkg.go.dev/builtin#string) `json:"regionCode,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

CustomLocalAqi: Expresses a 'country/region to AQI' relationship. Pairs a country/region with a desired AQI so that air quality data that is required for that country/region will be displayed according to the chosen AQI.

type ForecastLookupCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "airquality.forecast.lookup" call. Any non-2xx status code is an error. Response headers are in either *LookupForecastResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ForecastService struct {
	
}

func NewForecastService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#Service)) *[ForecastService](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#ForecastService)

func (r *[ForecastService](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#ForecastService)) Lookup(lookupforecastrequest *[LookupForecastRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#LookupForecastRequest)) *[ForecastLookupCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#ForecastLookupCall)

Lookup: Returns air quality forecast for a specific location for a given time range.

type HealthRecommendations struct {
	Athletes [string](https://pkg.go.dev/builtin#string) `json:"athletes,omitempty"`
	Children [string](https://pkg.go.dev/builtin#string) `json:"children,omitempty"`
	Elderly [string](https://pkg.go.dev/builtin#string) `json:"elderly,omitempty"`
	GeneralPopulation [string](https://pkg.go.dev/builtin#string) `json:"generalPopulation,omitempty"`
	HeartDiseasePopulation [string](https://pkg.go.dev/builtin#string) `json:"heartDiseasePopulation,omitempty"`
	LungDiseasePopulation [string](https://pkg.go.dev/builtin#string) `json:"lungDiseasePopulation,omitempty"`
	PregnantWomen [string](https://pkg.go.dev/builtin#string) `json:"pregnantWomen,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

HealthRecommendations: Health recommendations for different population groups in a free text format. The recommendations are derived from their associated air quality conditions.

type HistoryLookupCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "airquality.history.lookup" call. Any non-2xx status code is an error. Response headers are in either *LookupHistoryResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type HistoryService struct {
	
}

func NewHistoryService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#Service)) *[HistoryService](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#HistoryService)

func (r *[HistoryService](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#HistoryService)) Lookup(lookuphistoryrequest *[LookupHistoryRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#LookupHistoryRequest)) *[HistoryLookupCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#HistoryLookupCall)

Lookup: Returns air quality history for a specific location for a given time range.

type HourInfo struct {
	
	
	DateTime [string](https://pkg.go.dev/builtin#string) `json:"dateTime,omitempty"`
	
	
	
	HealthRecommendations *[HealthRecommendations](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#HealthRecommendations) `json:"healthRecommendations,omitempty"`
	
	
	
	Indexes []*[AirQualityIndex](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#AirQualityIndex) `json:"indexes,omitempty"`
	
	
	
	Pollutants []*[Pollutant](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#Pollutant) `json:"pollutants,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

HourInfo: Contains the air quality information for each hour in the requested range. For example, if the request is for 48 hours of history there will be 48 elements of hourly info.

type HourlyForecast struct {
	
	DateTime [string](https://pkg.go.dev/builtin#string) `json:"dateTime,omitempty"`
	
	
	
	HealthRecommendations *[HealthRecommendations](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#HealthRecommendations) `json:"healthRecommendations,omitempty"`
	
	
	
	Indexes []*[AirQualityIndex](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#AirQualityIndex) `json:"indexes,omitempty"`
	
	
	
	Pollutants []*[Pollutant](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#Pollutant) `json:"pollutants,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

HourlyForecast: Contains the air quality information for each hour in the requested range. For example, if the request is for 48 hours of forecast there will be 48 elements of hourly forecasts.

#### type [HttpBody](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/airquality/v1/airquality-gen.go#L599)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#HttpBody "Go to HttpBody")

HttpBody: Message that represents an arbitrary HTTP body. It should only be used for payload formats that can't be represented as JSON, such as raw binary or an HTML page. This message can be used both in streaming and non-streaming API methods in the request as well as the response. It can be used as a top-level request field, which is convenient if one wants to extract parameters from either the URL or HTTP template into the request fields and also want access to the raw HTTP body. Example: message GetResourceRequest { // A unique request id. string request_id = 1; // The raw HTTP body is bound to this field. google.api.HttpBody http_body = 2; } service ResourceService { rpc GetResource(GetResourceRequest) returns (google.api.HttpBody); rpc UpdateResource(google.api.HttpBody) returns (google.protobuf.Empty); } Example with streaming methods: service CaldavService { rpc GetCalendar(stream google.api.HttpBody) returns (stream google.api.HttpBody); rpc UpdateCalendar(stream google.api.HttpBody) returns (stream google.api.HttpBody); } Use of this type only changes how the request and response bodies are handled, all other features will continue to work unchanged.

type Interval struct {
	
	EndTime [string](https://pkg.go.dev/builtin#string) `json:"endTime,omitempty"`
	
	
	StartTime [string](https://pkg.go.dev/builtin#string) `json:"startTime,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Interval: Represents a time interval, encoded as a Timestamp start (inclusive) and a Timestamp end (exclusive). The start must be less than or equal to the end. When the start equals the end, the interval is empty (matches no time). When both start and end are unspecified, the interval matches any time.

type LatLng struct {
	Latitude [float64](https://pkg.go.dev/builtin#float64) `json:"latitude,omitempty"`
	
	Longitude [float64](https://pkg.go.dev/builtin#float64) `json:"longitude,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

LatLng: An object that represents a latitude/longitude pair. This is expressed as a pair of doubles to represent degrees latitude and degrees longitude. Unless specified otherwise, this object must conform to the WGS84 standard. Values must be within normalized ranges.

type LookupCurrentConditionsRequest struct {
	
	
	
	
	
	CustomLocalAqis []*[CustomLocalAqi](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#CustomLocalAqi) `json:"customLocalAqis,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	ExtraComputations [][string](https://pkg.go.dev/builtin#string) `json:"extraComputations,omitempty"`
	
	
	
	LanguageCode [string](https://pkg.go.dev/builtin#string) `json:"languageCode,omitempty"`
	
	Location *[LatLng](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#LatLng) `json:"location,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	
	UaqiColorPalette [string](https://pkg.go.dev/builtin#string) `json:"uaqiColorPalette,omitempty"`
	
	UniversalAqi [bool](https://pkg.go.dev/builtin#bool) `json:"universalAqi,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

LookupCurrentConditionsRequest: The request definition of the air quality current conditions.

type LookupCurrentConditionsResponse struct {
	
	
	DateTime [string](https://pkg.go.dev/builtin#string) `json:"dateTime,omitempty"`
	
	
	
	HealthRecommendations *[HealthRecommendations](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#HealthRecommendations) `json:"healthRecommendations,omitempty"`
	
	
	
	Indexes []*[AirQualityIndex](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#AirQualityIndex) `json:"indexes,omitempty"`
	
	
	
	Pollutants []*[Pollutant](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#Pollutant) `json:"pollutants,omitempty"`
	
	
	
	RegionCode [string](https://pkg.go.dev/builtin#string) `json:"regionCode,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type LookupForecastRequest struct {
	
	
	
	
	
	CustomLocalAqis []*[CustomLocalAqi](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#CustomLocalAqi) `json:"customLocalAqis,omitempty"`
	
	
	
	
	DateTime [string](https://pkg.go.dev/builtin#string) `json:"dateTime,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	ExtraComputations [][string](https://pkg.go.dev/builtin#string) `json:"extraComputations,omitempty"`
	
	
	LanguageCode [string](https://pkg.go.dev/builtin#string) `json:"languageCode,omitempty"`
	
	Location *[LatLng](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#LatLng) `json:"location,omitempty"`
	
	PageSize [int64](https://pkg.go.dev/builtin#int64) `json:"pageSize,omitempty"`
	
	PageToken [string](https://pkg.go.dev/builtin#string) `json:"pageToken,omitempty"`
	
	Period *[Interval](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#Interval) `json:"period,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	
	UaqiColorPalette [string](https://pkg.go.dev/builtin#string) `json:"uaqiColorPalette,omitempty"`
	
	UniversalAqi [bool](https://pkg.go.dev/builtin#bool) `json:"universalAqi,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

LookupForecastRequest: The request object of the air quality forecast API.

type LookupForecastResponse struct {
	
	
	HourlyForecasts []*[HourlyForecast](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#HourlyForecast) `json:"hourlyForecasts,omitempty"`
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`
	
	
	
	RegionCode [string](https://pkg.go.dev/builtin#string) `json:"regionCode,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

LookupForecastResponse: The response object of the air quality forecast API.

type LookupHistoryRequest struct {
	
	
	
	
	
	CustomLocalAqis []*[CustomLocalAqi](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#CustomLocalAqi) `json:"customLocalAqis,omitempty"`
	
	
	
	
	
	
	
	DateTime [string](https://pkg.go.dev/builtin#string) `json:"dateTime,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	ExtraComputations [][string](https://pkg.go.dev/builtin#string) `json:"extraComputations,omitempty"`
	
	Hours [int64](https://pkg.go.dev/builtin#int64) `json:"hours,omitempty"`
	
	
	
	LanguageCode [string](https://pkg.go.dev/builtin#string) `json:"languageCode,omitempty"`
	
	Location *[LatLng](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#LatLng) `json:"location,omitempty"`
	
	PageSize [int64](https://pkg.go.dev/builtin#int64) `json:"pageSize,omitempty"`
	
	
	
	PageToken [string](https://pkg.go.dev/builtin#string) `json:"pageToken,omitempty"`
	
	Period *[Interval](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#Interval) `json:"period,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	
	UaqiColorPalette [string](https://pkg.go.dev/builtin#string) `json:"uaqiColorPalette,omitempty"`
	
	UniversalAqi [bool](https://pkg.go.dev/builtin#bool) `json:"universalAqi,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

LookupHistoryRequest: The request object of the air quality history API.

type LookupHistoryResponse struct {
	
	
	HoursInfo []*[HourInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#HourInfo) `json:"hoursInfo,omitempty"`
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`
	
	
	
	RegionCode [string](https://pkg.go.dev/builtin#string) `json:"regionCode,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type MapTypesHeatmapTilesLookupHeatmapTileCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "airquality.mapTypes.heatmapTiles.lookupHeatmapTile" call. Any non-2xx status code is an error. Response headers are in either *HttpBody.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type MapTypesHeatmapTilesService struct {
	
}

func NewMapTypesHeatmapTilesService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#Service)) *[MapTypesHeatmapTilesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#MapTypesHeatmapTilesService)

LookupHeatmapTile: Returns a bytes array containing the data of the tile PNG image.

*   mapType: The type of the air quality heatmap. Defines the pollutant that the map will graphically represent. Allowed values: - UAQI_RED_GREEN (UAQI, red-green palette) - UAQI_INDIGO_PERSIAN (UAQI, indigo-persian palette) - PM25_INDIGO_PERSIAN - GBR_DEFRA - DEU_UBA - CAN_EC - FRA_ATMO - US_AQI.
*   x: Defines the east-west point in the requested tile.
*   y: Defines the north-south point in the requested tile.
*   zoom: The map's zoom level. Defines how large or small the contents of a map appear in a map view. Zoom level 0 is the entire world in a single tile. Zoom level 1 is the entire world in 4 tiles. Zoom level 2 is the entire world in 16 tiles. Zoom level 16 is the entire world in 65,536 tiles. Allowed values: 0-16.

type MapTypesService struct {
 HeatmapTiles *[MapTypesHeatmapTilesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#MapTypesHeatmapTilesService)	
}

func NewMapTypesService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#Service)) *[MapTypesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#MapTypesService)

type Pollutant struct {
	AdditionalInfo *[AdditionalInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#AdditionalInfo) `json:"additionalInfo,omitempty"`
	
	
	Code [string](https://pkg.go.dev/builtin#string) `json:"code,omitempty"`
	
	Concentration *[Concentration](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#Concentration) `json:"concentration,omitempty"`
	DisplayName [string](https://pkg.go.dev/builtin#string) `json:"displayName,omitempty"`
	
	
	FullName [string](https://pkg.go.dev/builtin#string) `json:"fullName,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Pollutant: Data regarding an air quality pollutant.

type Service struct {
 BasePath [string](https://pkg.go.dev/builtin#string)  UserAgent [string](https://pkg.go.dev/builtin#string) 
 CurrentConditions *[CurrentConditionsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#CurrentConditionsService)
 Forecast *[ForecastService](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#ForecastService)
 History *[HistoryService](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#HistoryService)
 MapTypes *[MapTypesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/airquality/v1#MapTypesService)	
}

New creates a new Service. It uses the provided http.Client for requests.

Deprecated: please use NewService instead. To provide a custom HTTP client, use option.WithHTTPClient. If you are using google.golang.org/api/googleapis/transport.APIKey, use option.WithAPIKey with NewService instead.

NewService creates a new Service.
