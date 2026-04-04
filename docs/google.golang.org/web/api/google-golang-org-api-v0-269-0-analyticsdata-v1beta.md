# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta

Title: analyticsdata package - google.golang.org/api/analyticsdata/v1beta - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta

Markdown Content:
Package analyticsdata provides access to the Google Analytics Data API.

For product documentation, see: [https://developers.google.com/analytics/devguides/reporting/data/v1/](https://developers.google.com/analytics/devguides/reporting/data/v1/)

#### Library status [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#hdr-Library_status "Go to Library status")

These client libraries are officially supported by Google. However, this library is considered complete and is in maintenance mode. This means that we will address critical bugs and security issues but will not add any new features.

When possible, we recommend using our newer [Cloud Client Libraries for Go]([https://pkg.go.dev/cloud.google.com/go](https://pkg.go.dev/cloud.google.com/go)) that are still actively being worked and iterated on.

#### Creating a client [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#hdr-Creating_a_client "Go to Creating a client")

Usage example:

import "google.golang.org/api/analyticsdata/v1beta"
...
ctx := context.Background()
analyticsdataService, err := analyticsdata.NewService(ctx)

In this example, Google Application Default Credentials are used for authentication. For information on how to create and obtain Application Default Credentials, see [https://developers.google.com/identity/protocols/application-default-credentials](https://developers.google.com/identity/protocols/application-default-credentials).

#### Other authentication options [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#hdr-Other_authentication_options "Go to Other authentication options")

By default, all available scopes (see "Constants") are used to authenticate. To restrict scopes, use [google.golang.org/api/option.WithScopes](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#WithScopes):

analyticsdataService, err := analyticsdata.NewService(ctx, option.WithScopes(analyticsdata.AnalyticsReadonlyScope))

To use an API key for authentication (note: some APIs do not support API keys), use [google.golang.org/api/option.WithAPIKey](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#WithAPIKey):

analyticsdataService, err := analyticsdata.NewService(ctx, option.WithAPIKey("AIza..."))

To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow, use [google.golang.org/api/option.WithTokenSource](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#WithTokenSource):

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
analyticsdataService, err := analyticsdata.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))

See [google.golang.org/api/option.ClientOption](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#ClientOption) for details on options.

*   [Constants](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#pkg-constants)
*   [type ActiveMetricRestriction](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#ActiveMetricRestriction)
*       *   [func (s ActiveMetricRestriction) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#ActiveMetricRestriction.MarshalJSON)

*   [type AudienceExport](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#AudienceExport)
*       *   [func (s AudienceExport) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#AudienceExport.MarshalJSON)
    *   [func (s *AudienceExport) UnmarshalJSON(data []byte) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#AudienceExport.UnmarshalJSON)

*   [type AudienceListMetadata](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#AudienceListMetadata)
*   [type BatchRunPivotReportsRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#BatchRunPivotReportsRequest)
*       *   [func (s BatchRunPivotReportsRequest) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#BatchRunPivotReportsRequest.MarshalJSON)

*   [type BatchRunPivotReportsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#BatchRunPivotReportsResponse)
*       *   [func (s BatchRunPivotReportsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#BatchRunPivotReportsResponse.MarshalJSON)

*   [type BatchRunReportsRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#BatchRunReportsRequest)
*       *   [func (s BatchRunReportsRequest) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#BatchRunReportsRequest.MarshalJSON)

*   [type BatchRunReportsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#BatchRunReportsResponse)
*       *   [func (s BatchRunReportsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#BatchRunReportsResponse.MarshalJSON)

*   [type BetweenFilter](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#BetweenFilter)
*       *   [func (s BetweenFilter) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#BetweenFilter.MarshalJSON)

*   [type CaseExpression](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#CaseExpression)
*       *   [func (s CaseExpression) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#CaseExpression.MarshalJSON)

*   [type CheckCompatibilityRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#CheckCompatibilityRequest)
*       *   [func (s CheckCompatibilityRequest) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#CheckCompatibilityRequest.MarshalJSON)

*   [type CheckCompatibilityResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#CheckCompatibilityResponse)
*       *   [func (s CheckCompatibilityResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#CheckCompatibilityResponse.MarshalJSON)

*   [type Cohort](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Cohort)
*       *   [func (s Cohort) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Cohort.MarshalJSON)

*   [type CohortReportSettings](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#CohortReportSettings)
*       *   [func (s CohortReportSettings) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#CohortReportSettings.MarshalJSON)

*   [type CohortSpec](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#CohortSpec)
*       *   [func (s CohortSpec) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#CohortSpec.MarshalJSON)

*   [type CohortsRange](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#CohortsRange)
*       *   [func (s CohortsRange) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#CohortsRange.MarshalJSON)

*   [type Comparison](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Comparison)
*       *   [func (s Comparison) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Comparison.MarshalJSON)

*   [type ComparisonMetadata](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#ComparisonMetadata)
*       *   [func (s ComparisonMetadata) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#ComparisonMetadata.MarshalJSON)

*   [type ConcatenateExpression](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#ConcatenateExpression)
*       *   [func (s ConcatenateExpression) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#ConcatenateExpression.MarshalJSON)

*   [type DateRange](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#DateRange)
*       *   [func (s DateRange) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#DateRange.MarshalJSON)

*   [type Dimension](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Dimension)
*       *   [func (s Dimension) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Dimension.MarshalJSON)

*   [type DimensionCompatibility](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#DimensionCompatibility)
*       *   [func (s DimensionCompatibility) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#DimensionCompatibility.MarshalJSON)

*   [type DimensionExpression](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#DimensionExpression)
*       *   [func (s DimensionExpression) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#DimensionExpression.MarshalJSON)

*   [type DimensionHeader](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#DimensionHeader)
*       *   [func (s DimensionHeader) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#DimensionHeader.MarshalJSON)

*   [type DimensionMetadata](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#DimensionMetadata)
*       *   [func (s DimensionMetadata) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#DimensionMetadata.MarshalJSON)

*   [type DimensionOrderBy](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#DimensionOrderBy)
*       *   [func (s DimensionOrderBy) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#DimensionOrderBy.MarshalJSON)

*   [type DimensionValue](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#DimensionValue)
*       *   [func (s DimensionValue) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#DimensionValue.MarshalJSON)

*   [type EmptyFilter](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#EmptyFilter)
*   [type Filter](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Filter)
*       *   [func (s Filter) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Filter.MarshalJSON)

*   [type FilterExpression](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#FilterExpression)
*       *   [func (s FilterExpression) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#FilterExpression.MarshalJSON)

*   [type FilterExpressionList](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#FilterExpressionList)
*       *   [func (s FilterExpressionList) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#FilterExpressionList.MarshalJSON)

*   [type InListFilter](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#InListFilter)
*       *   [func (s InListFilter) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#InListFilter.MarshalJSON)

*   [type ListAudienceExportsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#ListAudienceExportsResponse)
*       *   [func (s ListAudienceExportsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#ListAudienceExportsResponse.MarshalJSON)

*   [type Metadata](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Metadata)
*       *   [func (s Metadata) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Metadata.MarshalJSON)

*   [type Metric](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Metric)
*       *   [func (s Metric) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Metric.MarshalJSON)

*   [type MetricCompatibility](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#MetricCompatibility)
*       *   [func (s MetricCompatibility) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#MetricCompatibility.MarshalJSON)

*   [type MetricHeader](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#MetricHeader)
*       *   [func (s MetricHeader) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#MetricHeader.MarshalJSON)

*   [type MetricMetadata](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#MetricMetadata)
*       *   [func (s MetricMetadata) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#MetricMetadata.MarshalJSON)

*   [type MetricOrderBy](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#MetricOrderBy)
*       *   [func (s MetricOrderBy) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#MetricOrderBy.MarshalJSON)

*   [type MetricValue](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#MetricValue)
*       *   [func (s MetricValue) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#MetricValue.MarshalJSON)

*   [type MinuteRange](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#MinuteRange)
*       *   [func (s MinuteRange) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#MinuteRange.MarshalJSON)

*   [type NumericFilter](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#NumericFilter)
*       *   [func (s NumericFilter) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#NumericFilter.MarshalJSON)

*   [type NumericValue](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#NumericValue)
*       *   [func (s NumericValue) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#NumericValue.MarshalJSON)
    *   [func (s *NumericValue) UnmarshalJSON(data []byte) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#NumericValue.UnmarshalJSON)

*   [type Operation](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Operation)
*       *   [func (s Operation) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Operation.MarshalJSON)

*   [type OrderBy](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#OrderBy)
*       *   [func (s OrderBy) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#OrderBy.MarshalJSON)

*   [type Pivot](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Pivot)
*       *   [func (s Pivot) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Pivot.MarshalJSON)

*   [type PivotDimensionHeader](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PivotDimensionHeader)
*       *   [func (s PivotDimensionHeader) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PivotDimensionHeader.MarshalJSON)

*   [type PivotHeader](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PivotHeader)
*       *   [func (s PivotHeader) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PivotHeader.MarshalJSON)

*   [type PivotOrderBy](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PivotOrderBy)
*       *   [func (s PivotOrderBy) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PivotOrderBy.MarshalJSON)

*   [type PivotSelection](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PivotSelection)
*       *   [func (s PivotSelection) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PivotSelection.MarshalJSON)

*   [type PropertiesAudienceExportsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsCreateCall)
*       *   [func (c *PropertiesAudienceExportsCreateCall) Context(ctx context.Context) *PropertiesAudienceExportsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsCreateCall.Context)
    *   [func (c *PropertiesAudienceExportsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsCreateCall.Do)
    *   [func (c *PropertiesAudienceExportsCreateCall) Fields(s ...googleapi.Field) *PropertiesAudienceExportsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsCreateCall.Fields)
    *   [func (c *PropertiesAudienceExportsCreateCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsCreateCall.Header)

*   [type PropertiesAudienceExportsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsGetCall)
*       *   [func (c *PropertiesAudienceExportsGetCall) Context(ctx context.Context) *PropertiesAudienceExportsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsGetCall.Context)
    *   [func (c *PropertiesAudienceExportsGetCall) Do(opts ...googleapi.CallOption) (*AudienceExport, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsGetCall.Do)
    *   [func (c *PropertiesAudienceExportsGetCall) Fields(s ...googleapi.Field) *PropertiesAudienceExportsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsGetCall.Fields)
    *   [func (c *PropertiesAudienceExportsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsGetCall.Header)
    *   [func (c *PropertiesAudienceExportsGetCall) IfNoneMatch(entityTag string) *PropertiesAudienceExportsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsGetCall.IfNoneMatch)

*   [type PropertiesAudienceExportsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsListCall)
*       *   [func (c *PropertiesAudienceExportsListCall) Context(ctx context.Context) *PropertiesAudienceExportsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsListCall.Context)
    *   [func (c *PropertiesAudienceExportsListCall) Do(opts ...googleapi.CallOption) (*ListAudienceExportsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsListCall.Do)
    *   [func (c *PropertiesAudienceExportsListCall) Fields(s ...googleapi.Field) *PropertiesAudienceExportsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsListCall.Fields)
    *   [func (c *PropertiesAudienceExportsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsListCall.Header)
    *   [func (c *PropertiesAudienceExportsListCall) IfNoneMatch(entityTag string) *PropertiesAudienceExportsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsListCall.IfNoneMatch)
    *   [func (c *PropertiesAudienceExportsListCall) PageSize(pageSize int64) *PropertiesAudienceExportsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsListCall.PageSize)
    *   [func (c *PropertiesAudienceExportsListCall) PageToken(pageToken string) *PropertiesAudienceExportsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsListCall.PageToken)
    *   [func (c *PropertiesAudienceExportsListCall) Pages(ctx context.Context, f func(*ListAudienceExportsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsListCall.Pages)

*   [type PropertiesAudienceExportsQueryCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsQueryCall)
*       *   [func (c *PropertiesAudienceExportsQueryCall) Context(ctx context.Context) *PropertiesAudienceExportsQueryCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsQueryCall.Context)
    *   [func (c *PropertiesAudienceExportsQueryCall) Do(opts ...googleapi.CallOption) (*QueryAudienceExportResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsQueryCall.Do)
    *   [func (c *PropertiesAudienceExportsQueryCall) Fields(s ...googleapi.Field) *PropertiesAudienceExportsQueryCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsQueryCall.Fields)
    *   [func (c *PropertiesAudienceExportsQueryCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsQueryCall.Header)

*   [type PropertiesAudienceExportsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsService)
*       *   [func NewPropertiesAudienceExportsService(s *Service) *PropertiesAudienceExportsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#NewPropertiesAudienceExportsService)

*       *   [func (r *PropertiesAudienceExportsService) Create(parent string, audienceexport *AudienceExport) *PropertiesAudienceExportsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsService.Create)
    *   [func (r *PropertiesAudienceExportsService) Get(name string) *PropertiesAudienceExportsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsService.Get)
    *   [func (r *PropertiesAudienceExportsService) List(parent string) *PropertiesAudienceExportsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsService.List)
    *   [func (r *PropertiesAudienceExportsService) Query(name string, queryaudienceexportrequest *QueryAudienceExportRequest) *PropertiesAudienceExportsQueryCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsService.Query)

*   [type PropertiesBatchRunPivotReportsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesBatchRunPivotReportsCall)
*       *   [func (c *PropertiesBatchRunPivotReportsCall) Context(ctx context.Context) *PropertiesBatchRunPivotReportsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesBatchRunPivotReportsCall.Context)
    *   [func (c *PropertiesBatchRunPivotReportsCall) Do(opts ...googleapi.CallOption) (*BatchRunPivotReportsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesBatchRunPivotReportsCall.Do)
    *   [func (c *PropertiesBatchRunPivotReportsCall) Fields(s ...googleapi.Field) *PropertiesBatchRunPivotReportsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesBatchRunPivotReportsCall.Fields)
    *   [func (c *PropertiesBatchRunPivotReportsCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesBatchRunPivotReportsCall.Header)

*   [type PropertiesBatchRunReportsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesBatchRunReportsCall)
*       *   [func (c *PropertiesBatchRunReportsCall) Context(ctx context.Context) *PropertiesBatchRunReportsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesBatchRunReportsCall.Context)
    *   [func (c *PropertiesBatchRunReportsCall) Do(opts ...googleapi.CallOption) (*BatchRunReportsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesBatchRunReportsCall.Do)
    *   [func (c *PropertiesBatchRunReportsCall) Fields(s ...googleapi.Field) *PropertiesBatchRunReportsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesBatchRunReportsCall.Fields)
    *   [func (c *PropertiesBatchRunReportsCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesBatchRunReportsCall.Header)

*   [type PropertiesCheckCompatibilityCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesCheckCompatibilityCall)
*       *   [func (c *PropertiesCheckCompatibilityCall) Context(ctx context.Context) *PropertiesCheckCompatibilityCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesCheckCompatibilityCall.Context)
    *   [func (c *PropertiesCheckCompatibilityCall) Do(opts ...googleapi.CallOption) (*CheckCompatibilityResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesCheckCompatibilityCall.Do)
    *   [func (c *PropertiesCheckCompatibilityCall) Fields(s ...googleapi.Field) *PropertiesCheckCompatibilityCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesCheckCompatibilityCall.Fields)
    *   [func (c *PropertiesCheckCompatibilityCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesCheckCompatibilityCall.Header)

*   [type PropertiesGetMetadataCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesGetMetadataCall)
*       *   [func (c *PropertiesGetMetadataCall) Context(ctx context.Context) *PropertiesGetMetadataCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesGetMetadataCall.Context)
    *   [func (c *PropertiesGetMetadataCall) Do(opts ...googleapi.CallOption) (*Metadata, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesGetMetadataCall.Do)
    *   [func (c *PropertiesGetMetadataCall) Fields(s ...googleapi.Field) *PropertiesGetMetadataCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesGetMetadataCall.Fields)
    *   [func (c *PropertiesGetMetadataCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesGetMetadataCall.Header)
    *   [func (c *PropertiesGetMetadataCall) IfNoneMatch(entityTag string) *PropertiesGetMetadataCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesGetMetadataCall.IfNoneMatch)

*   [type PropertiesRunPivotReportCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesRunPivotReportCall)
*       *   [func (c *PropertiesRunPivotReportCall) Context(ctx context.Context) *PropertiesRunPivotReportCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesRunPivotReportCall.Context)
    *   [func (c *PropertiesRunPivotReportCall) Do(opts ...googleapi.CallOption) (*RunPivotReportResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesRunPivotReportCall.Do)
    *   [func (c *PropertiesRunPivotReportCall) Fields(s ...googleapi.Field) *PropertiesRunPivotReportCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesRunPivotReportCall.Fields)
    *   [func (c *PropertiesRunPivotReportCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesRunPivotReportCall.Header)

*   [type PropertiesRunRealtimeReportCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesRunRealtimeReportCall)
*       *   [func (c *PropertiesRunRealtimeReportCall) Context(ctx context.Context) *PropertiesRunRealtimeReportCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesRunRealtimeReportCall.Context)
    *   [func (c *PropertiesRunRealtimeReportCall) Do(opts ...googleapi.CallOption) (*RunRealtimeReportResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesRunRealtimeReportCall.Do)
    *   [func (c *PropertiesRunRealtimeReportCall) Fields(s ...googleapi.Field) *PropertiesRunRealtimeReportCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesRunRealtimeReportCall.Fields)
    *   [func (c *PropertiesRunRealtimeReportCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesRunRealtimeReportCall.Header)

*   [type PropertiesRunReportCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesRunReportCall)
*       *   [func (c *PropertiesRunReportCall) Context(ctx context.Context) *PropertiesRunReportCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesRunReportCall.Context)
    *   [func (c *PropertiesRunReportCall) Do(opts ...googleapi.CallOption) (*RunReportResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesRunReportCall.Do)
    *   [func (c *PropertiesRunReportCall) Fields(s ...googleapi.Field) *PropertiesRunReportCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesRunReportCall.Fields)
    *   [func (c *PropertiesRunReportCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesRunReportCall.Header)

*   [type PropertiesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesService)
*       *   [func NewPropertiesService(s *Service) *PropertiesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#NewPropertiesService)

*       *   [func (r *PropertiesService) BatchRunPivotReports(propertyid string, batchrunpivotreportsrequest *BatchRunPivotReportsRequest) *PropertiesBatchRunPivotReportsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesService.BatchRunPivotReports)
    *   [func (r *PropertiesService) BatchRunReports(propertyid string, batchrunreportsrequest *BatchRunReportsRequest) *PropertiesBatchRunReportsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesService.BatchRunReports)
    *   [func (r *PropertiesService) CheckCompatibility(propertyid string, checkcompatibilityrequest *CheckCompatibilityRequest) *PropertiesCheckCompatibilityCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesService.CheckCompatibility)
    *   [func (r *PropertiesService) GetMetadata(nameid string) *PropertiesGetMetadataCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesService.GetMetadata)
    *   [func (r *PropertiesService) RunPivotReport(propertyid string, runpivotreportrequest *RunPivotReportRequest) *PropertiesRunPivotReportCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesService.RunPivotReport)
    *   [func (r *PropertiesService) RunRealtimeReport(propertyid string, runrealtimereportrequest *RunRealtimeReportRequest) *PropertiesRunRealtimeReportCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesService.RunRealtimeReport)
    *   [func (r *PropertiesService) RunReport(propertyid string, runreportrequest *RunReportRequest) *PropertiesRunReportCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesService.RunReport)

*   [type PropertyQuota](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertyQuota)
*       *   [func (s PropertyQuota) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertyQuota.MarshalJSON)

*   [type QueryAudienceExportRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#QueryAudienceExportRequest)
*       *   [func (s QueryAudienceExportRequest) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#QueryAudienceExportRequest.MarshalJSON)

*   [type QueryAudienceExportResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#QueryAudienceExportResponse)
*       *   [func (s QueryAudienceExportResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#QueryAudienceExportResponse.MarshalJSON)

*   [type QuotaStatus](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#QuotaStatus)
*       *   [func (s QuotaStatus) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#QuotaStatus.MarshalJSON)

*   [type ResponseMetaData](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#ResponseMetaData)
*       *   [func (s ResponseMetaData) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#ResponseMetaData.MarshalJSON)

*   [type Row](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Row)
*       *   [func (s Row) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Row.MarshalJSON)

*   [type RunPivotReportRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#RunPivotReportRequest)
*       *   [func (s RunPivotReportRequest) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#RunPivotReportRequest.MarshalJSON)

*   [type RunPivotReportResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#RunPivotReportResponse)
*       *   [func (s RunPivotReportResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#RunPivotReportResponse.MarshalJSON)

*   [type RunRealtimeReportRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#RunRealtimeReportRequest)
*       *   [func (s RunRealtimeReportRequest) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#RunRealtimeReportRequest.MarshalJSON)

*   [type RunRealtimeReportResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#RunRealtimeReportResponse)
*       *   [func (s RunRealtimeReportResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#RunRealtimeReportResponse.MarshalJSON)

*   [type RunReportRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#RunReportRequest)
*       *   [func (s RunReportRequest) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#RunReportRequest.MarshalJSON)

*   [type RunReportResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#RunReportResponse)
*       *   [func (s RunReportResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#RunReportResponse.MarshalJSON)

*   [type SamplingMetadata](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#SamplingMetadata)
*       *   [func (s SamplingMetadata) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#SamplingMetadata.MarshalJSON)

*   [type SchemaRestrictionResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#SchemaRestrictionResponse)
*       *   [func (s SchemaRestrictionResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#SchemaRestrictionResponse.MarshalJSON)

*   [type Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Service)
*       *   [func New(client *http.Client) (*Service, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#New)deprecated
    *   [func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#NewService)

*   [type Status](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Status)
*       *   [func (s Status) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Status.MarshalJSON)

*   [type StringFilter](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#StringFilter)
*       *   [func (s StringFilter) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#StringFilter.MarshalJSON)

*   [type V1betaAudienceDimension](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#V1betaAudienceDimension)
*       *   [func (s V1betaAudienceDimension) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#V1betaAudienceDimension.MarshalJSON)

*   [type V1betaAudienceDimensionValue](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#V1betaAudienceDimensionValue)
*       *   [func (s V1betaAudienceDimensionValue) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#V1betaAudienceDimensionValue.MarshalJSON)

*   [type V1betaAudienceRow](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#V1betaAudienceRow)
*       *   [func (s V1betaAudienceRow) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#V1betaAudienceRow.MarshalJSON)

[View Source](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/analyticsdata/v1beta/analyticsdata-gen.go#L105)

const (
	AnalyticsScope = "https://www.googleapis.com/auth/analytics"

	AnalyticsReadonlyScope = "https://www.googleapis.com/auth/analytics.readonly"
)

OAuth2 scopes used by this API.

This section is empty.

This section is empty.

type ActiveMetricRestriction struct {
	MetricName [string](https://pkg.go.dev/builtin#string) `json:"metricName,omitempty"`
	
	
	
	
	
	RestrictedMetricTypes [][string](https://pkg.go.dev/builtin#string) `json:"restrictedMetricTypes,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ActiveMetricRestriction: A metric actively restricted in creating the report.

type AudienceExport struct {
	
	
	Audience [string](https://pkg.go.dev/builtin#string) `json:"audience,omitempty"`
	
	AudienceDisplayName [string](https://pkg.go.dev/builtin#string) `json:"audienceDisplayName,omitempty"`
	
	BeginCreatingTime [string](https://pkg.go.dev/builtin#string) `json:"beginCreatingTime,omitempty"`
	
	
	
	CreationQuotaTokensCharged [int64](https://pkg.go.dev/builtin#int64) `json:"creationQuotaTokensCharged,omitempty"`
	
	Dimensions []*[V1betaAudienceDimension](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#V1betaAudienceDimension) `json:"dimensions,omitempty"`
	
	
	ErrorMessage [string](https://pkg.go.dev/builtin#string) `json:"errorMessage,omitempty"`
	
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	PercentageCompleted [float64](https://pkg.go.dev/builtin#float64) `json:"percentageCompleted,omitempty"`
	
	RowCount [int64](https://pkg.go.dev/builtin#int64) `json:"rowCount,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	State [string](https://pkg.go.dev/builtin#string) `json:"state,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

AudienceExport: An audience export is a list of users in an audience at the time of the list's creation. One audience may have multiple audience exports created for different days.

type AudienceListMetadata struct {
}

AudienceListMetadata: This metadata is currently blank.

type BatchRunPivotReportsRequest struct {
	
	Requests []*[RunPivotReportRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#RunPivotReportRequest) `json:"requests,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

BatchRunPivotReportsRequest: The batch request containing multiple pivot report requests.

type BatchRunPivotReportsResponse struct {
	
	
	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`
	
	PivotReports []*[RunPivotReportResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#RunPivotReportResponse) `json:"pivotReports,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

BatchRunPivotReportsResponse: The batch response containing multiple pivot reports.

type BatchRunReportsRequest struct {
	
	Requests []*[RunReportRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#RunReportRequest) `json:"requests,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

BatchRunReportsRequest: The batch request containing multiple report requests.

type BatchRunReportsResponse struct {
	
	
	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`
	Reports []*[RunReportResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#RunReportResponse) `json:"reports,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

BatchRunReportsResponse: The batch response containing multiple reports.

type BetweenFilter struct {
	FromValue *[NumericValue](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#NumericValue) `json:"fromValue,omitempty"`
	ToValue *[NumericValue](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#NumericValue) `json:"toValue,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

BetweenFilter: To express that the result needs to be between two numbers (inclusive).

type CaseExpression struct {
	
	DimensionName [string](https://pkg.go.dev/builtin#string) `json:"dimensionName,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

CaseExpression: Used to convert a dimension value to a single case.

type CheckCompatibilityRequest struct {
	
	
	
	
	
	
	
	
	
	CompatibilityFilter [string](https://pkg.go.dev/builtin#string) `json:"compatibilityFilter,omitempty"`
	
	DimensionFilter *[FilterExpression](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#FilterExpression) `json:"dimensionFilter,omitempty"`
	
	Dimensions []*[Dimension](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Dimension) `json:"dimensions,omitempty"`
	
	MetricFilter *[FilterExpression](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#FilterExpression) `json:"metricFilter,omitempty"`
	
	Metrics []*[Metric](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Metric) `json:"metrics,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

CheckCompatibilityRequest: The request for compatibility information for a report's dimensions and metrics. Check compatibility provides a preview of the compatibility of a report; fields shared with the `runReport` request should be the same values as in your `runReport` request.

type CheckCompatibilityResponse struct {
	DimensionCompatibilities []*[DimensionCompatibility](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#DimensionCompatibility) `json:"dimensionCompatibilities,omitempty"`
	MetricCompatibilities []*[MetricCompatibility](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#MetricCompatibility) `json:"metricCompatibilities,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

CheckCompatibilityResponse: The compatibility response with the compatibility of each dimension & metric.

type Cohort struct {
	
	
	
	
	
	
	
	
	
	
	
	
	
	DateRange *[DateRange](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#DateRange) `json:"dateRange,omitempty"`
	
	Dimension [string](https://pkg.go.dev/builtin#string) `json:"dimension,omitempty"`
	
	
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Cohort: Defines a cohort selection criteria. A cohort is a group of users who share a common characteristic. For example, users with the same `firstSessionDate` belong to the same cohort.

type CohortReportSettings struct {
	
	Accumulate [bool](https://pkg.go.dev/builtin#bool) `json:"accumulate,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

CohortReportSettings: Optional settings of a cohort report.

type CohortSpec struct {
	CohortReportSettings *[CohortReportSettings](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#CohortReportSettings) `json:"cohortReportSettings,omitempty"`
	
	
	Cohorts []*[Cohort](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Cohort) `json:"cohorts,omitempty"`
	
	CohortsRange *[CohortsRange](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#CohortsRange) `json:"cohortsRange,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

CohortSpec: The specification of cohorts for a cohort report. Cohort reports create a time series of user retention for the cohort. For example, you could select the cohort of users that were acquired in the first week of September and follow that cohort for the next six weeks. Selecting the users acquired in the first week of September cohort is specified in the `cohort` object. Following that cohort for the next six weeks is specified in the `cohortsRange` object. For examples, see Cohort Report Examples ([https://developers.google.com/analytics/devguides/reporting/data/v1/advanced#cohort_report_examples](https://developers.google.com/analytics/devguides/reporting/data/v1/advanced#cohort_report_examples)). The report response could show a weekly time series where say your app has retained 60% of this cohort after three weeks and 25% of this cohort after six weeks. These two percentages can be calculated by the metric `cohortActiveUsers/cohortTotalUsers` and will be separate rows in the report.

type CohortsRange struct {
	
	
	
	
	
	
	
	
	
	EndOffset [int64](https://pkg.go.dev/builtin#int64) `json:"endOffset,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	Granularity [string](https://pkg.go.dev/builtin#string) `json:"granularity,omitempty"`
	
	
	
	
	
	
	
	
	StartOffset [int64](https://pkg.go.dev/builtin#int64) `json:"startOffset,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

CohortsRange: Configures the extended reporting date range for a cohort report. Specifies an offset duration to follow the cohorts over.

type Comparison struct {
	
	Comparison [string](https://pkg.go.dev/builtin#string) `json:"comparison,omitempty"`
	DimensionFilter *[FilterExpression](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#FilterExpression) `json:"dimensionFilter,omitempty"`
	
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Comparison: Defines an individual comparison. Most requests will include multiple comparisons so that the report compares between the comparisons.

type ComparisonMetadata struct {
	
	ApiName [string](https://pkg.go.dev/builtin#string) `json:"apiName,omitempty"`
	Description [string](https://pkg.go.dev/builtin#string) `json:"description,omitempty"`
	UiName [string](https://pkg.go.dev/builtin#string) `json:"uiName,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ComparisonMetadata: The metadata for a single comparison.

type ConcatenateExpression struct {
	
	
	
	
	
	Delimiter [string](https://pkg.go.dev/builtin#string) `json:"delimiter,omitempty"`
	
	DimensionNames [][string](https://pkg.go.dev/builtin#string) `json:"dimensionNames,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ConcatenateExpression: Used to combine dimension values to a single dimension.

type DateRange struct {
	
	
	
	EndDate [string](https://pkg.go.dev/builtin#string) `json:"endDate,omitempty"`
	
	
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	
	
	StartDate [string](https://pkg.go.dev/builtin#string) `json:"startDate,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

DateRange: A contiguous set of days: `startDate`, `startDate + 1`, ..., `endDate`. Requests are allowed up to 4 date ranges.

type Dimension struct {
	
	
	DimensionExpression *[DimensionExpression](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#DimensionExpression) `json:"dimensionExpression,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Dimension: Dimensions are attributes of your data. For example, the dimension city indicates the city from which an event originates. Dimension values in report responses are strings; for example, the city could be "Paris" or "New York". Requests are allowed up to 9 dimensions.

type DimensionCompatibility struct {
	
	
	
	
	
	
	
	
	Compatibility [string](https://pkg.go.dev/builtin#string) `json:"compatibility,omitempty"`
	
	
	DimensionMetadata *[DimensionMetadata](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#DimensionMetadata) `json:"dimensionMetadata,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

DimensionCompatibility: The compatibility for a single dimension.

type DimensionExpression struct {
	
	Concatenate *[ConcatenateExpression](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#ConcatenateExpression) `json:"concatenate,omitempty"`
	LowerCase *[CaseExpression](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#CaseExpression) `json:"lowerCase,omitempty"`
	UpperCase *[CaseExpression](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#CaseExpression) `json:"upperCase,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

DimensionExpression: Used to express a dimension which is the result of a formula of multiple dimensions. Example usages: 1) lower_case(dimension) 2) concatenate(dimension1, symbol, dimension2).

type DimensionHeader struct {
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

DimensionHeader: Describes a dimension column in the report. Dimensions requested in a report produce column entries within rows and DimensionHeaders. However, dimensions used exclusively within filters or expressions do not produce columns in a report; correspondingly, those dimensions do not produce headers.

type DimensionMetadata struct {
	
	ApiName [string](https://pkg.go.dev/builtin#string) `json:"apiName,omitempty"`
	
	Category [string](https://pkg.go.dev/builtin#string) `json:"category,omitempty"`
	
	
	
	
	CustomDefinition [bool](https://pkg.go.dev/builtin#bool) `json:"customDefinition,omitempty"`
	
	
	
	DeprecatedApiNames [][string](https://pkg.go.dev/builtin#string) `json:"deprecatedApiNames,omitempty"`
	Description [string](https://pkg.go.dev/builtin#string) `json:"description,omitempty"`
	
	UiName [string](https://pkg.go.dev/builtin#string) `json:"uiName,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

DimensionMetadata: Explains a dimension.

type DimensionOrderBy struct {
	DimensionName [string](https://pkg.go.dev/builtin#string) `json:"dimensionName,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	OrderType [string](https://pkg.go.dev/builtin#string) `json:"orderType,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

DimensionOrderBy: Sorts by dimension values.

type DimensionValue struct {
	Value [string](https://pkg.go.dev/builtin#string) `json:"value,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

DimensionValue: The value of a dimension.

type EmptyFilter struct {
}

EmptyFilter: Filter for empty values.

type Filter struct {
	BetweenFilter *[BetweenFilter](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#BetweenFilter) `json:"betweenFilter,omitempty"`
	EmptyFilter *[EmptyFilter](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#EmptyFilter) `json:"emptyFilter,omitempty"`
	
	
	
	FieldName [string](https://pkg.go.dev/builtin#string) `json:"fieldName,omitempty"`
	InListFilter *[InListFilter](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#InListFilter) `json:"inListFilter,omitempty"`
	NumericFilter *[NumericFilter](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#NumericFilter) `json:"numericFilter,omitempty"`
	StringFilter *[StringFilter](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#StringFilter) `json:"stringFilter,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Filter: An expression to filter dimension or metric values.

type FilterExpression struct {
	AndGroup *[FilterExpressionList](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#FilterExpressionList) `json:"andGroup,omitempty"`
	
	Filter *[Filter](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Filter) `json:"filter,omitempty"`
	NotExpression *[FilterExpression](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#FilterExpression) `json:"notExpression,omitempty"`
	OrGroup *[FilterExpressionList](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#FilterExpressionList) `json:"orGroup,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

FilterExpression: To express dimension or metric filters. The fields in the same FilterExpression need to be either all dimensions or all metrics.

type FilterExpressionList struct {
	Expressions []*[FilterExpression](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#FilterExpression) `json:"expressions,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

FilterExpressionList: A list of filter expressions.

type InListFilter struct {
	CaseSensitive [bool](https://pkg.go.dev/builtin#bool) `json:"caseSensitive,omitempty"`
	Values [][string](https://pkg.go.dev/builtin#string) `json:"values,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

InListFilter: The result needs to be in a list of string values.

type ListAudienceExportsResponse struct {
	AudienceExports []*[AudienceExport](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#AudienceExport) `json:"audienceExports,omitempty"`
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListAudienceExportsResponse: A list of all audience exports for a property.

type Metadata struct {
	Comparisons []*[ComparisonMetadata](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#ComparisonMetadata) `json:"comparisons,omitempty"`
	Dimensions []*[DimensionMetadata](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#DimensionMetadata) `json:"dimensions,omitempty"`
	Metrics []*[MetricMetadata](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#MetricMetadata) `json:"metrics,omitempty"`
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Metadata: The dimensions, metrics and comparisons currently accepted in reporting methods.

type Metric struct {
	
	Expression [string](https://pkg.go.dev/builtin#string) `json:"expression,omitempty"`
	
	
	Invisible [bool](https://pkg.go.dev/builtin#bool) `json:"invisible,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Metric: The quantitative measurements of a report. For example, the metric `eventCount` is the total number of events. Requests are allowed up to 10 metrics.

type MetricCompatibility struct {
	
	
	
	
	
	
	
	
	Compatibility [string](https://pkg.go.dev/builtin#string) `json:"compatibility,omitempty"`
	
	
	MetricMetadata *[MetricMetadata](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#MetricMetadata) `json:"metricMetadata,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

MetricCompatibility: The compatibility for a single metric.

type MetricHeader struct {
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	Type [string](https://pkg.go.dev/builtin#string) `json:"type,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

MetricHeader: Describes a metric column in the report. Visible metrics requested in a report produce column entries within rows and MetricHeaders. However, metrics used exclusively within filters or expressions do not produce columns in a report; correspondingly, those metrics do not produce headers.

type MetricMetadata struct {
	
	ApiName [string](https://pkg.go.dev/builtin#string) `json:"apiName,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	
	
	BlockedReasons [][string](https://pkg.go.dev/builtin#string) `json:"blockedReasons,omitempty"`
	
	Category [string](https://pkg.go.dev/builtin#string) `json:"category,omitempty"`
	CustomDefinition [bool](https://pkg.go.dev/builtin#bool) `json:"customDefinition,omitempty"`
	
	
	
	DeprecatedApiNames [][string](https://pkg.go.dev/builtin#string) `json:"deprecatedApiNames,omitempty"`
	Description [string](https://pkg.go.dev/builtin#string) `json:"description,omitempty"`
	
	
	Expression [string](https://pkg.go.dev/builtin#string) `json:"expression,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	Type [string](https://pkg.go.dev/builtin#string) `json:"type,omitempty"`
	
	UiName [string](https://pkg.go.dev/builtin#string) `json:"uiName,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

MetricMetadata: Explains a metric.

type MetricOrderBy struct {
	MetricName [string](https://pkg.go.dev/builtin#string) `json:"metricName,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

MetricOrderBy: Sorts by metric values.

type MetricValue struct {
	Value [string](https://pkg.go.dev/builtin#string) `json:"value,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

MetricValue: The value of a metric.

type MinuteRange struct {
	
	
	
	
	
	
	
	EndMinutesAgo [int64](https://pkg.go.dev/builtin#int64) `json:"endMinutesAgo,omitempty"`
	
	
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	
	
	
	
	
	StartMinutesAgo [int64](https://pkg.go.dev/builtin#int64) `json:"startMinutesAgo,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

MinuteRange: A contiguous set of minutes: `startMinutesAgo`, `startMinutesAgo + 1`, ..., `endMinutesAgo`. Requests are allowed up to 2 minute ranges.

type NumericFilter struct {
	
	
	
	
	
	
	
	
	Operation [string](https://pkg.go.dev/builtin#string) `json:"operation,omitempty"`
	Value *[NumericValue](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#NumericValue) `json:"value,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

NumericFilter: Filters for numeric or date values.

type NumericValue struct {
	DoubleValue [float64](https://pkg.go.dev/builtin#float64) `json:"doubleValue,omitempty"`
	Int64Value [int64](https://pkg.go.dev/builtin#int64) `json:"int64Value,omitempty,string"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

NumericValue: To represent a number.

Operation: This resource represents a long-running operation that is the result of a network API call.

type OrderBy struct {
	Desc [bool](https://pkg.go.dev/builtin#bool) `json:"desc,omitempty"`
	Dimension *[DimensionOrderBy](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#DimensionOrderBy) `json:"dimension,omitempty"`
	Metric *[MetricOrderBy](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#MetricOrderBy) `json:"metric,omitempty"`
	Pivot *[PivotOrderBy](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PivotOrderBy) `json:"pivot,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

OrderBy: Order bys define how rows will be sorted in the response. For example, ordering rows by descending event count is one ordering, and ordering rows by the event name string is a different ordering.

type Pivot struct {
	
	
	
	FieldNames [][string](https://pkg.go.dev/builtin#string) `json:"fieldNames,omitempty"`
	
	
	
	
	
	Limit [int64](https://pkg.go.dev/builtin#int64) `json:"limit,omitempty,string"`
	
	
	
	
	
	
	
	
	MetricAggregations [][string](https://pkg.go.dev/builtin#string) `json:"metricAggregations,omitempty"`
	Offset [int64](https://pkg.go.dev/builtin#int64) `json:"offset,omitempty,string"`
	
	
	
	
	OrderBys []*[OrderBy](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#OrderBy) `json:"orderBys,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Pivot: Describes the visible dimension columns and rows in the report response.

type PivotDimensionHeader struct {
	DimensionValues []*[DimensionValue](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#DimensionValue) `json:"dimensionValues,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

PivotDimensionHeader: Summarizes dimension values from a row for this pivot.

type PivotHeader struct {
	
	PivotDimensionHeaders []*[PivotDimensionHeader](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PivotDimensionHeader) `json:"pivotDimensionHeaders,omitempty"`
	
	
	RowCount [int64](https://pkg.go.dev/builtin#int64) `json:"rowCount,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

PivotHeader: Dimensions' values in a single pivot.

type PivotOrderBy struct {
	
	MetricName [string](https://pkg.go.dev/builtin#string) `json:"metricName,omitempty"`
	
	
	
	PivotSelections []*[PivotSelection](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PivotSelection) `json:"pivotSelections,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

PivotOrderBy: Sorts by a pivot column group.

type PivotSelection struct {
	DimensionName [string](https://pkg.go.dev/builtin#string) `json:"dimensionName,omitempty"`
	DimensionValue [string](https://pkg.go.dev/builtin#string) `json:"dimensionValue,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

PivotSelection: A pair of dimension names and values. Rows with this dimension pivot pair are ordered by the metric's value. For example if pivots = {{"browser", "Chrome"}} and metric_name = "Sessions", then the rows will be sorted based on Sessions in Chrome. ---------|----------|----------------|----------|---------------- | Chrome | Chrome | Safari | Safari ---------|----------|----------------|----------|---------------- Country | Sessions | Pages/Sessions | Sessions | Pages/Sessions ---------|----------|----------------|----------|---------------- US | 2 | 2 | 3 | 1 ---------|----------|----------------|----------|---------------- Canada | 3 | 1 | 4 | 1 ---------|----------|----------------|----------|----------------

type PropertiesAudienceExportsCreateCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "analyticsdata.properties.audienceExports.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesAudienceExportsGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "analyticsdata.properties.audienceExports.get" call. Any non-2xx status code is an error. Response headers are in either *AudienceExport.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesAudienceExportsListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "analyticsdata.properties.audienceExports.list" call. Any non-2xx status code is an error. Response headers are in either *ListAudienceExportsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": The maximum number of audience exports to return. The service may return fewer than this value. If unspecified, at most 200 audience exports will be returned. The maximum value is 1000 (higher values will be coerced to the maximum).

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListAudienceExports` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListAudienceExports` must match the call that provided the page token.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesAudienceExportsQueryCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "analyticsdata.properties.audienceExports.query" call. Any non-2xx status code is an error. Response headers are in either *QueryAudienceExportResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesAudienceExportsService struct {
	
}

func NewPropertiesAudienceExportsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Service)) *[PropertiesAudienceExportsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsService)

Create: Creates an audience export for later retrieval. This method quickly returns the audience export's resource name and initiates a long running asynchronous request to form an audience export. To export the users in an audience export, first create the audience export through this method and then send the audience resource name to the `QueryAudienceExport` method. See Creating an Audience Export ([https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics)) for an introduction to Audience Exports with examples. An audience export is a snapshot of the users currently in the audience at the time of audience export creation. Creating audience exports for one audience on different days will return different results as users enter and exit the audience. Audiences in Google Analytics 4 allow you to segment your users in the ways that are important to your business. To learn more, see [https://support.google.com/analytics/answer/9267572](https://support.google.com/analytics/answer/9267572). Audience exports contain the users in each audience. Audience Export APIs have some methods at alpha and other methods at beta stability. The intention is to advance methods to beta stability after some feedback and adoption. To give your feedback on this API, complete the Google Analytics Audience Export API Feedback ([https://forms.gle/EeA5u5LW6PEggtCEA](https://forms.gle/EeA5u5LW6PEggtCEA)) form.

*   parent: The parent resource where this audience export will be created. Format: `properties/{property}`.

Get: Gets configuration metadata about a specific audience export. This method can be used to understand an audience export after it has been created. See Creating an Audience Export ([https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics)) for an introduction to Audience Exports with examples. Audience Export APIs have some methods at alpha and other methods at beta stability. The intention is to advance methods to beta stability after some feedback and adoption. To give your feedback on this API, complete the Google Analytics Audience Export API Feedback ([https://forms.gle/EeA5u5LW6PEggtCEA](https://forms.gle/EeA5u5LW6PEggtCEA)) form.

*   name: The audience export resource name. Format: `properties/{property}/audienceExports/{audience_export}`.

List: Lists all audience exports for a property. This method can be used for you to find and reuse existing audience exports rather than creating unnecessary new audience exports. The same audience can have multiple audience exports that represent the export of users that were in an audience on different days. See Creating an Audience Export ([https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics)) for an introduction to Audience Exports with examples. Audience Export APIs have some methods at alpha and other methods at beta stability. The intention is to advance methods to beta stability after some feedback and adoption. To give your feedback on this API, complete the Google Analytics Audience Export API Feedback ([https://forms.gle/EeA5u5LW6PEggtCEA](https://forms.gle/EeA5u5LW6PEggtCEA)) form.

*   parent: All audience exports for this property will be listed in the response. Format: `properties/{property}`.

Query: Retrieves an audience export of users. After creating an audience, the users are not immediately available for exporting. First, a request to `CreateAudienceExport` is necessary to create an audience export of users, and then second, this method is used to retrieve the users in the audience export. See Creating an Audience Export ([https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics](https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-basics)) for an introduction to Audience Exports with examples. Audiences in Google Analytics 4 allow you to segment your users in the ways that are important to your business. To learn more, see [https://support.google.com/analytics/answer/9267572](https://support.google.com/analytics/answer/9267572). Audience Export APIs have some methods at alpha and other methods at beta stability. The intention is to advance methods to beta stability after some feedback and adoption. To give your feedback on this API, complete the Google Analytics Audience Export API Feedback ([https://forms.gle/EeA5u5LW6PEggtCEA](https://forms.gle/EeA5u5LW6PEggtCEA)) form.

*   name: The name of the audience export to retrieve users from. Format: `properties/{property}/audienceExports/{audience_export}`.

type PropertiesBatchRunPivotReportsCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "analyticsdata.properties.batchRunPivotReports" call. Any non-2xx status code is an error. Response headers are in either *BatchRunPivotReportsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesBatchRunReportsCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "analyticsdata.properties.batchRunReports" call. Any non-2xx status code is an error. Response headers are in either *BatchRunReportsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesCheckCompatibilityCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "analyticsdata.properties.checkCompatibility" call. Any non-2xx status code is an error. Response headers are in either *CheckCompatibilityResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesGetMetadataCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "analyticsdata.properties.getMetadata" call. Any non-2xx status code is an error. Response headers are in either *Metadata.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesRunPivotReportCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "analyticsdata.properties.runPivotReport" call. Any non-2xx status code is an error. Response headers are in either *RunPivotReportResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesRunRealtimeReportCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "analyticsdata.properties.runRealtimeReport" call. Any non-2xx status code is an error. Response headers are in either *RunRealtimeReportResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesRunReportCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "analyticsdata.properties.runReport" call. Any non-2xx status code is an error. Response headers are in either *RunReportResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesService struct {
 AudienceExports *[PropertiesAudienceExportsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesAudienceExportsService)	
}

func NewPropertiesService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Service)) *[PropertiesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesService)

func (r *[PropertiesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesService)) BatchRunPivotReports(propertyid [string](https://pkg.go.dev/builtin#string), batchrunpivotreportsrequest *[BatchRunPivotReportsRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#BatchRunPivotReportsRequest)) *[PropertiesBatchRunPivotReportsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesBatchRunPivotReportsCall)

BatchRunPivotReports: Returns multiple pivot reports in a batch. All reports must be for the same Google Analytics property.

*   property: A Google Analytics property identifier whose events are tracked. Specified in the URL path and not the body. To learn more, see where to find your Property ID ([https://developers.google.com/analytics/devguides/reporting/data/v1/property-id](https://developers.google.com/analytics/devguides/reporting/data/v1/property-id)). This property must be specified for the batch. The property within RunPivotReportRequest may either be unspecified or consistent with this property. Example: properties/1234.

func (r *[PropertiesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesService)) BatchRunReports(propertyid [string](https://pkg.go.dev/builtin#string), batchrunreportsrequest *[BatchRunReportsRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#BatchRunReportsRequest)) *[PropertiesBatchRunReportsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesBatchRunReportsCall)

BatchRunReports: Returns multiple reports in a batch. All reports must be for the same Google Analytics property.

*   property: A Google Analytics property identifier whose events are tracked. Specified in the URL path and not the body. To learn more, see where to find your Property ID ([https://developers.google.com/analytics/devguides/reporting/data/v1/property-id](https://developers.google.com/analytics/devguides/reporting/data/v1/property-id)). This property must be specified for the batch. The property within RunReportRequest may either be unspecified or consistent with this property. Example: properties/1234.

func (r *[PropertiesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesService)) CheckCompatibility(propertyid [string](https://pkg.go.dev/builtin#string), checkcompatibilityrequest *[CheckCompatibilityRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#CheckCompatibilityRequest)) *[PropertiesCheckCompatibilityCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesCheckCompatibilityCall)

CheckCompatibility: This compatibility method lists dimensions and metrics that can be added to a report request and maintain compatibility. This method fails if the request's dimensions and metrics are incompatible. In Google Analytics, reports fail if they request incompatible dimensions and/or metrics; in that case, you will need to remove dimensions and/or metrics from the incompatible report until the report is compatible. The Realtime and Core reports have different compatibility rules. This method checks compatibility for Core reports.

*   property: A Google Analytics property identifier whose events are tracked. To learn more, see where to find your Property ID ([https://developers.google.com/analytics/devguides/reporting/data/v1/property-id](https://developers.google.com/analytics/devguides/reporting/data/v1/property-id)). `property` should be the same value as in your `runReport` request. Example: properties/1234.

GetMetadata: Returns metadata for dimensions and metrics available in reporting methods. Used to explore the dimensions and metrics. In this method, a Google Analytics property identifier is specified in the request, and the metadata response includes Custom dimensions and metrics as well as Universal metadata. For example if a custom metric with parameter name `levels_unlocked` is registered to a property, the Metadata response will contain `customEvent:levels_unlocked`. Universal metadata are dimensions and metrics applicable to any property such as `country` and `totalUsers`.

*   name: The resource name of the metadata to retrieve. This name field is specified in the URL path and not URL parameters. Property is a numeric Google Analytics property identifier. To learn more, see where to find your Property ID ([https://developers.google.com/analytics/devguides/reporting/data/v1/property-id](https://developers.google.com/analytics/devguides/reporting/data/v1/property-id)). Example: properties/1234/metadata Set the Property ID to 0 for dimensions and metrics common to all properties. In this special mode, this method will not return custom dimensions and metrics.

func (r *[PropertiesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesService)) RunPivotReport(propertyid [string](https://pkg.go.dev/builtin#string), runpivotreportrequest *[RunPivotReportRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#RunPivotReportRequest)) *[PropertiesRunPivotReportCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesRunPivotReportCall)

RunPivotReport: Returns a customized pivot report of your Google Analytics event data. Pivot reports are more advanced and expressive formats than regular reports. In a pivot report, dimensions are only visible if they are included in a pivot. Multiple pivots can be specified to further dissect your data.

*   property: A Google Analytics property identifier whose events are tracked. Specified in the URL path and not the body. To learn more, see where to find your Property ID ([https://developers.google.com/analytics/devguides/reporting/data/v1/property-id](https://developers.google.com/analytics/devguides/reporting/data/v1/property-id)). Within a batch request, this property should either be unspecified or consistent with the batch-level property. Example: properties/1234.

func (r *[PropertiesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesService)) RunRealtimeReport(propertyid [string](https://pkg.go.dev/builtin#string), runrealtimereportrequest *[RunRealtimeReportRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#RunRealtimeReportRequest)) *[PropertiesRunRealtimeReportCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesRunRealtimeReportCall)

RunRealtimeReport: Returns a customized report of realtime event data for your property. Events appear in realtime reports seconds after they have been sent to the Google Analytics. Realtime reports show events and usage data for the periods of time ranging from the present moment to 30 minutes ago (up to 60 minutes for Google Analytics 360 properties). For a guide to constructing realtime requests & understanding responses, see Creating a Realtime Report ([https://developers.google.com/analytics/devguides/reporting/data/v1/realtime-basics](https://developers.google.com/analytics/devguides/reporting/data/v1/realtime-basics)).

*   property: A Google Analytics property identifier whose events are tracked. Specified in the URL path and not the body. To learn more, see where to find your Property ID ([https://developers.google.com/analytics/devguides/reporting/data/v1/property-id](https://developers.google.com/analytics/devguides/reporting/data/v1/property-id)). Example: properties/1234.

func (r *[PropertiesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesService)) RunReport(propertyid [string](https://pkg.go.dev/builtin#string), runreportrequest *[RunReportRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#RunReportRequest)) *[PropertiesRunReportCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesRunReportCall)

RunReport: Returns a customized report of your Google Analytics event data. Reports contain statistics derived from data collected by the Google Analytics tracking code. The data returned from the API is as a table with columns for the requested dimensions and metrics. Metrics are individual measurements of user activity on your property, such as active users or event count. Dimensions break down metrics across some common criteria, such as country or event name. For a guide to constructing requests & understanding responses, see Creating a Report ([https://developers.google.com/analytics/devguides/reporting/data/v1/basics](https://developers.google.com/analytics/devguides/reporting/data/v1/basics)).

*   property: A Google Analytics property identifier whose events are tracked. Specified in the URL path and not the body. To learn more, see where to find your Property ID ([https://developers.google.com/analytics/devguides/reporting/data/v1/property-id](https://developers.google.com/analytics/devguides/reporting/data/v1/property-id)). Within a batch request, this property should either be unspecified or consistent with the batch-level property. Example: properties/1234.

type PropertyQuota struct {
	
	
	ConcurrentRequests *[QuotaStatus](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#QuotaStatus) `json:"concurrentRequests,omitempty"`
	
	
	
	PotentiallyThresholdedRequestsPerHour *[QuotaStatus](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#QuotaStatus) `json:"potentiallyThresholdedRequestsPerHour,omitempty"`
	
	
	ServerErrorsPerProjectPerHour *[QuotaStatus](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#QuotaStatus) `json:"serverErrorsPerProjectPerHour,omitempty"`
	
	
	TokensPerDay *[QuotaStatus](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#QuotaStatus) `json:"tokensPerDay,omitempty"`
	
	
	
	TokensPerHour *[QuotaStatus](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#QuotaStatus) `json:"tokensPerHour,omitempty"`
	
	
	
	
	
	TokensPerProjectPerHour *[QuotaStatus](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#QuotaStatus) `json:"tokensPerProjectPerHour,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

PropertyQuota: Current state of all quotas for this Analytics Property. If any quota for a property is exhausted, all requests to that property will return Resource Exhausted errors.

type QueryAudienceExportRequest struct {
	
	
	
	
	
	
	Limit [int64](https://pkg.go.dev/builtin#int64) `json:"limit,omitempty,string"`
	
	
	
	
	
	
	Offset [int64](https://pkg.go.dev/builtin#int64) `json:"offset,omitempty,string"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

QueryAudienceExportRequest: A request to list users in an audience export.

type QueryAudienceExportResponse struct {
	
	
	
	AudienceExport *[AudienceExport](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#AudienceExport) `json:"audienceExport,omitempty"`
	
	AudienceRows []*[V1betaAudienceRow](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#V1betaAudienceRow) `json:"audienceRows,omitempty"`
	
	
	
	
	
	
	RowCount [int64](https://pkg.go.dev/builtin#int64) `json:"rowCount,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

QueryAudienceExportResponse: A list of users in an audience export.

type QuotaStatus struct {
	Consumed [int64](https://pkg.go.dev/builtin#int64) `json:"consumed,omitempty"`
	Remaining [int64](https://pkg.go.dev/builtin#int64) `json:"remaining,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

QuotaStatus: Current state for a particular quota group.

type ResponseMetaData struct {
	
	
	
	
	
	
	
	CurrencyCode [string](https://pkg.go.dev/builtin#string) `json:"currencyCode,omitempty"`
	
	
	
	
	
	
	
	
	
	
	DataLossFromOtherRow [bool](https://pkg.go.dev/builtin#bool) `json:"dataLossFromOtherRow,omitempty"`
	
	EmptyReason [string](https://pkg.go.dev/builtin#string) `json:"emptyReason,omitempty"`
	
	
	
	
	
	SamplingMetadatas []*[SamplingMetadata](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#SamplingMetadata) `json:"samplingMetadatas,omitempty"`
	
	
	
	SchemaRestrictionResponse *[SchemaRestrictionResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#SchemaRestrictionResponse) `json:"schemaRestrictionResponse,omitempty"`
	
	
	
	
	
	SubjectToThresholding [bool](https://pkg.go.dev/builtin#bool) `json:"subjectToThresholding,omitempty"`
	
	
	
	TimeZone [string](https://pkg.go.dev/builtin#string) `json:"timeZone,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ResponseMetaData: Response's metadata carrying additional information about the report content.

type Row struct {
	
	DimensionValues []*[DimensionValue](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#DimensionValue) `json:"dimensionValues,omitempty"`
	MetricValues []*[MetricValue](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#MetricValue) `json:"metricValues,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Row: Report data for each row. For example if RunReportRequest contains: ```none "dimensions": [ { "name": "eventName" }, { "name": "countryId" } ], "metrics": [ { "name": "eventCount" } ] ``` One row with 'in_app_purchase' as the eventName, 'JP' as the countryId, and 15 as the eventCount, would be: ```none "dimensionValues": [ { "value": "in_app_purchase" }, { "value": "JP" } ], "metricValues": [ { "value": "15" } ] ```

type RunPivotReportRequest struct {
	
	CohortSpec *[CohortSpec](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#CohortSpec) `json:"cohortSpec,omitempty"`
	
	
	Comparisons []*[Comparison](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Comparison) `json:"comparisons,omitempty"`
	
	
	CurrencyCode [string](https://pkg.go.dev/builtin#string) `json:"currencyCode,omitempty"`
	
	
	
	
	DateRanges []*[DateRange](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#DateRange) `json:"dateRanges,omitempty"`
	
	DimensionFilter *[FilterExpression](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#FilterExpression) `json:"dimensionFilter,omitempty"`
	
	
	Dimensions []*[Dimension](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Dimension) `json:"dimensions,omitempty"`
	
	
	
	
	
	
	KeepEmptyRows [bool](https://pkg.go.dev/builtin#bool) `json:"keepEmptyRows,omitempty"`
	
	
	MetricFilter *[FilterExpression](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#FilterExpression) `json:"metricFilter,omitempty"`
	
	
	Metrics []*[Metric](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Metric) `json:"metrics,omitempty"`
	
	
	
	Pivots []*[Pivot](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Pivot) `json:"pivots,omitempty"`
	
	
	
	
	
	Property [string](https://pkg.go.dev/builtin#string) `json:"property,omitempty"`
	
	
	ReturnPropertyQuota [bool](https://pkg.go.dev/builtin#bool) `json:"returnPropertyQuota,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

RunPivotReportRequest: The request to generate a pivot report.

type RunPivotReportResponse struct {
	
	
	
	Aggregates []*[Row](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Row) `json:"aggregates,omitempty"`
	
	
	DimensionHeaders []*[DimensionHeader](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#DimensionHeader) `json:"dimensionHeaders,omitempty"`
	
	
	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`
	Metadata *[ResponseMetaData](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#ResponseMetaData) `json:"metadata,omitempty"`
	
	MetricHeaders []*[MetricHeader](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#MetricHeader) `json:"metricHeaders,omitempty"`
	
	
	
	
	
	
	
	
	PivotHeaders []*[PivotHeader](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PivotHeader) `json:"pivotHeaders,omitempty"`
	
	PropertyQuota *[PropertyQuota](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertyQuota) `json:"propertyQuota,omitempty"`
	Rows []*[Row](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Row) `json:"rows,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

RunPivotReportResponse: The response pivot report table corresponding to a pivot request.

type RunRealtimeReportRequest struct {
	
	DimensionFilter *[FilterExpression](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#FilterExpression) `json:"dimensionFilter,omitempty"`
	Dimensions []*[Dimension](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Dimension) `json:"dimensions,omitempty"`
	
	
	
	
	
	
	Limit [int64](https://pkg.go.dev/builtin#int64) `json:"limit,omitempty,string"`
	
	
	
	
	
	
	
	
	
	MetricAggregations [][string](https://pkg.go.dev/builtin#string) `json:"metricAggregations,omitempty"`
	
	
	MetricFilter *[FilterExpression](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#FilterExpression) `json:"metricFilter,omitempty"`
	Metrics []*[Metric](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Metric) `json:"metrics,omitempty"`
	
	
	
	
	MinuteRanges []*[MinuteRange](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#MinuteRange) `json:"minuteRanges,omitempty"`
	OrderBys []*[OrderBy](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#OrderBy) `json:"orderBys,omitempty"`
	
	
	ReturnPropertyQuota [bool](https://pkg.go.dev/builtin#bool) `json:"returnPropertyQuota,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

RunRealtimeReportRequest: The request to generate a realtime report.

type RunRealtimeReportResponse struct {
	
	
	DimensionHeaders []*[DimensionHeader](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#DimensionHeader) `json:"dimensionHeaders,omitempty"`
	
	
	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`
	Maximums []*[Row](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Row) `json:"maximums,omitempty"`
	
	MetricHeaders []*[MetricHeader](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#MetricHeader) `json:"metricHeaders,omitempty"`
	Minimums []*[Row](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Row) `json:"minimums,omitempty"`
	
	PropertyQuota *[PropertyQuota](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertyQuota) `json:"propertyQuota,omitempty"`
	
	
	
	
	RowCount [int64](https://pkg.go.dev/builtin#int64) `json:"rowCount,omitempty"`
	Rows []*[Row](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Row) `json:"rows,omitempty"`
	Totals []*[Row](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Row) `json:"totals,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

RunRealtimeReportResponse: The response realtime report table corresponding to a request.

type RunReportRequest struct {
	
	CohortSpec *[CohortSpec](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#CohortSpec) `json:"cohortSpec,omitempty"`
	
	
	Comparisons []*[Comparison](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Comparison) `json:"comparisons,omitempty"`
	
	
	CurrencyCode [string](https://pkg.go.dev/builtin#string) `json:"currencyCode,omitempty"`
	
	
	
	
	DateRanges []*[DateRange](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#DateRange) `json:"dateRanges,omitempty"`
	
	
	
	DimensionFilter *[FilterExpression](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#FilterExpression) `json:"dimensionFilter,omitempty"`
	Dimensions []*[Dimension](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Dimension) `json:"dimensions,omitempty"`
	
	
	
	
	
	
	KeepEmptyRows [bool](https://pkg.go.dev/builtin#bool) `json:"keepEmptyRows,omitempty"`
	
	
	
	
	
	
	
	
	Limit [int64](https://pkg.go.dev/builtin#int64) `json:"limit,omitempty,string"`
	
	
	
	
	
	
	
	
	
	
	MetricAggregations [][string](https://pkg.go.dev/builtin#string) `json:"metricAggregations,omitempty"`
	
	
	MetricFilter *[FilterExpression](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#FilterExpression) `json:"metricFilter,omitempty"`
	Metrics []*[Metric](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Metric) `json:"metrics,omitempty"`
	
	
	
	
	
	
	Offset [int64](https://pkg.go.dev/builtin#int64) `json:"offset,omitempty,string"`
	
	
	OrderBys []*[OrderBy](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#OrderBy) `json:"orderBys,omitempty"`
	
	
	
	
	
	Property [string](https://pkg.go.dev/builtin#string) `json:"property,omitempty"`
	
	
	ReturnPropertyQuota [bool](https://pkg.go.dev/builtin#bool) `json:"returnPropertyQuota,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

RunReportRequest: The request to generate a report.

type RunReportResponse struct {
	
	
	DimensionHeaders []*[DimensionHeader](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#DimensionHeader) `json:"dimensionHeaders,omitempty"`
	
	
	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`
	Maximums []*[Row](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Row) `json:"maximums,omitempty"`
	Metadata *[ResponseMetaData](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#ResponseMetaData) `json:"metadata,omitempty"`
	
	MetricHeaders []*[MetricHeader](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#MetricHeader) `json:"metricHeaders,omitempty"`
	Minimums []*[Row](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Row) `json:"minimums,omitempty"`
	
	PropertyQuota *[PropertyQuota](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertyQuota) `json:"propertyQuota,omitempty"`
	
	
	
	
	
	
	RowCount [int64](https://pkg.go.dev/builtin#int64) `json:"rowCount,omitempty"`
	Rows []*[Row](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Row) `json:"rows,omitempty"`
	Totals []*[Row](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#Row) `json:"totals,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

RunReportResponse: The response report table corresponding to a request.

type SamplingMetadata struct {
	
	
	SamplesReadCount [int64](https://pkg.go.dev/builtin#int64) `json:"samplesReadCount,omitempty,string"`
	
	
	
	
	
	SamplingSpaceSize [int64](https://pkg.go.dev/builtin#int64) `json:"samplingSpaceSize,omitempty,string"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

SamplingMetadata: If this report results is sampled ([https://support.google.com/analytics/answer/13331292](https://support.google.com/analytics/answer/13331292)), this describes the percentage of events used in this report. Sampling is the practice of analyzing a subset of all data in order to uncover the meaningful information in the larger data set.

type SchemaRestrictionResponse struct {
	
	
	
	ActiveMetricRestrictions []*[ActiveMetricRestriction](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#ActiveMetricRestriction) `json:"activeMetricRestrictions,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

SchemaRestrictionResponse: The schema restrictions actively enforced in creating this report. To learn more, see Access and data-restriction management ([https://support.google.com/analytics/answer/10851388](https://support.google.com/analytics/answer/10851388)).

type Service struct {
 BasePath [string](https://pkg.go.dev/builtin#string)  UserAgent [string](https://pkg.go.dev/builtin#string) 
 Properties *[PropertiesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#PropertiesService)	
}

New creates a new Service. It uses the provided http.Client for requests.

Deprecated: please use NewService instead. To provide a custom HTTP client, use option.WithHTTPClient. If you are using google.golang.org/api/googleapis/transport.APIKey, use option.WithAPIKey with NewService instead.

NewService creates a new Service.

type Status struct {
	Code [int64](https://pkg.go.dev/builtin#int64) `json:"code,omitempty"`
	
	Details [][googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[RawMessage](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#RawMessage) `json:"details,omitempty"`
	
	
	Message [string](https://pkg.go.dev/builtin#string) `json:"message,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Status: The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by gRPC ([https://github.com/grpc](https://github.com/grpc)). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the API Design Guide ([https://cloud.google.com/apis/design/errors](https://cloud.google.com/apis/design/errors)).

type StringFilter struct {
	CaseSensitive [bool](https://pkg.go.dev/builtin#bool) `json:"caseSensitive,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	MatchType [string](https://pkg.go.dev/builtin#string) `json:"matchType,omitempty"`
	Value [string](https://pkg.go.dev/builtin#string) `json:"value,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

StringFilter: The filter for string

type V1betaAudienceDimension struct {
	
	
	
	DimensionName [string](https://pkg.go.dev/builtin#string) `json:"dimensionName,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

V1betaAudienceDimension: An audience dimension is a user attribute. Specific user attributed are requested and then later returned in the `QueryAudienceExportResponse`.

type V1betaAudienceDimensionValue struct {
	Value [string](https://pkg.go.dev/builtin#string) `json:"value,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

V1betaAudienceDimensionValue: The value of a dimension.

type V1betaAudienceRow struct {
	
	DimensionValues []*[V1betaAudienceDimensionValue](https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsdata/v1beta#V1betaAudienceDimensionValue) `json:"dimensionValues,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

V1betaAudienceRow: Dimension value attributes for the audience user row.
