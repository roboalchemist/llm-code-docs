# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsadmin/v1beta

Title: analyticsadmin package - google.golang.org/api/analyticsadmin/v1beta - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsadmin/v1beta

Markdown Content:
Skip to Main Content
Why Go
Learn
Docs
Packages
Community
Discover Packages
 
google.golang.org/api
 
analyticsadmin
 
v1beta
analyticsadmin
package
Version: v0.269.0 Latest 
Published: Feb 24, 2026 
License: BSD-3-Clause 
Imports: 18 
Imported by: 2
Details
 Valid go.mod file 
 Redistributable license 
 Tagged version 
 Stable version 
Learn more about best practices
Repository
github.com/googleapis/google-api-go-client
Links
 Open Source Insights
Jump to ...
Documentation
Source Files
 Documentation ¶
Overview ¶
Library status
Creating a client
Other authentication options

Package analyticsadmin provides access to the Google Analytics Admin API.

For product documentation, see: http://code.google.com/apis/analytics/docs/mgmt/home.html

Library status ¶

These client libraries are officially supported by Google. However, this library is considered complete and is in maintenance mode. This means that we will address critical bugs and security issues but will not add any new features.

When possible, we recommend using our newer [Cloud Client Libraries for Go](https://pkg.go.dev/cloud.google.com/go) that are still actively being worked and iterated on.

Creating a client ¶

Usage example:

import "google.golang.org/api/analyticsadmin/v1beta"
...
ctx := context.Background()
analyticsadminService, err := analyticsadmin.NewService(ctx)


In this example, Google Application Default Credentials are used for authentication. For information on how to create and obtain Application Default Credentials, see https://developers.google.com/identity/protocols/application-default-credentials.

Other authentication options ¶

By default, all available scopes (see "Constants") are used to authenticate. To restrict scopes, use google.golang.org/api/option.WithScopes:

analyticsadminService, err := analyticsadmin.NewService(ctx, option.WithScopes(analyticsadmin.AnalyticsReadonlyScope))


To use an API key for authentication (note: some APIs do not support API keys), use google.golang.org/api/option.WithAPIKey:

analyticsadminService, err := analyticsadmin.NewService(ctx, option.WithAPIKey("AIza..."))


To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow, use google.golang.org/api/option.WithTokenSource:

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
analyticsadminService, err := analyticsadmin.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))


See google.golang.org/api/option.ClientOption for details on options.

Index ¶
Constants
type AccountSummariesListCall
func (c *AccountSummariesListCall) Context(ctx context.Context) *AccountSummariesListCall
func (c *AccountSummariesListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaListAccountSummariesResponse, error)
func (c *AccountSummariesListCall) Fields(s ...googleapi.Field) *AccountSummariesListCall
func (c *AccountSummariesListCall) Header() http.Header
func (c *AccountSummariesListCall) IfNoneMatch(entityTag string) *AccountSummariesListCall
func (c *AccountSummariesListCall) PageSize(pageSize int64) *AccountSummariesListCall
func (c *AccountSummariesListCall) PageToken(pageToken string) *AccountSummariesListCall
func (c *AccountSummariesListCall) Pages(ctx context.Context, ...) error
type AccountSummariesService
func NewAccountSummariesService(s *Service) *AccountSummariesService
func (r *AccountSummariesService) List() *AccountSummariesListCall
type AccountsDeleteCall
func (c *AccountsDeleteCall) Context(ctx context.Context) *AccountsDeleteCall
func (c *AccountsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *AccountsDeleteCall) Fields(s ...googleapi.Field) *AccountsDeleteCall
func (c *AccountsDeleteCall) Header() http.Header
type AccountsGetCall
func (c *AccountsGetCall) Context(ctx context.Context) *AccountsGetCall
func (c *AccountsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaAccount, error)
func (c *AccountsGetCall) Fields(s ...googleapi.Field) *AccountsGetCall
func (c *AccountsGetCall) Header() http.Header
func (c *AccountsGetCall) IfNoneMatch(entityTag string) *AccountsGetCall
type AccountsGetDataSharingSettingsCall
func (c *AccountsGetDataSharingSettingsCall) Context(ctx context.Context) *AccountsGetDataSharingSettingsCall
func (c *AccountsGetDataSharingSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaDataSharingSettings, error)
func (c *AccountsGetDataSharingSettingsCall) Fields(s ...googleapi.Field) *AccountsGetDataSharingSettingsCall
func (c *AccountsGetDataSharingSettingsCall) Header() http.Header
func (c *AccountsGetDataSharingSettingsCall) IfNoneMatch(entityTag string) *AccountsGetDataSharingSettingsCall
type AccountsListCall
func (c *AccountsListCall) Context(ctx context.Context) *AccountsListCall
func (c *AccountsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaListAccountsResponse, error)
func (c *AccountsListCall) Fields(s ...googleapi.Field) *AccountsListCall
func (c *AccountsListCall) Header() http.Header
func (c *AccountsListCall) IfNoneMatch(entityTag string) *AccountsListCall
func (c *AccountsListCall) PageSize(pageSize int64) *AccountsListCall
func (c *AccountsListCall) PageToken(pageToken string) *AccountsListCall
func (c *AccountsListCall) Pages(ctx context.Context, ...) error
func (c *AccountsListCall) ShowDeleted(showDeleted bool) *AccountsListCall
type AccountsPatchCall
func (c *AccountsPatchCall) Context(ctx context.Context) *AccountsPatchCall
func (c *AccountsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaAccount, error)
func (c *AccountsPatchCall) Fields(s ...googleapi.Field) *AccountsPatchCall
func (c *AccountsPatchCall) Header() http.Header
func (c *AccountsPatchCall) UpdateMask(updateMask string) *AccountsPatchCall
type AccountsProvisionAccountTicketCall
func (c *AccountsProvisionAccountTicketCall) Context(ctx context.Context) *AccountsProvisionAccountTicketCall
func (c *AccountsProvisionAccountTicketCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaProvisionAccountTicketResponse, error)
func (c *AccountsProvisionAccountTicketCall) Fields(s ...googleapi.Field) *AccountsProvisionAccountTicketCall
func (c *AccountsProvisionAccountTicketCall) Header() http.Header
type AccountsRunAccessReportCall
func (c *AccountsRunAccessReportCall) Context(ctx context.Context) *AccountsRunAccessReportCall
func (c *AccountsRunAccessReportCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaRunAccessReportResponse, error)
func (c *AccountsRunAccessReportCall) Fields(s ...googleapi.Field) *AccountsRunAccessReportCall
func (c *AccountsRunAccessReportCall) Header() http.Header
type AccountsSearchChangeHistoryEventsCall
func (c *AccountsSearchChangeHistoryEventsCall) Context(ctx context.Context) *AccountsSearchChangeHistoryEventsCall
func (c *AccountsSearchChangeHistoryEventsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponse, error)
func (c *AccountsSearchChangeHistoryEventsCall) Fields(s ...googleapi.Field) *AccountsSearchChangeHistoryEventsCall
func (c *AccountsSearchChangeHistoryEventsCall) Header() http.Header
func (c *AccountsSearchChangeHistoryEventsCall) Pages(ctx context.Context, ...) error
type AccountsService
func NewAccountsService(s *Service) *AccountsService
func (r *AccountsService) Delete(name string) *AccountsDeleteCall
func (r *AccountsService) Get(name string) *AccountsGetCall
func (r *AccountsService) GetDataSharingSettings(name string) *AccountsGetDataSharingSettingsCall
func (r *AccountsService) List() *AccountsListCall
func (r *AccountsService) Patch(name string, ...) *AccountsPatchCall
func (r *AccountsService) ProvisionAccountTicket(...) *AccountsProvisionAccountTicketCall
func (r *AccountsService) RunAccessReport(entity string, ...) *AccountsRunAccessReportCall
func (r *AccountsService) SearchChangeHistoryEvents(account string, ...) *AccountsSearchChangeHistoryEventsCall
type GoogleAnalyticsAdminV1betaAccessBetweenFilter
func (s GoogleAnalyticsAdminV1betaAccessBetweenFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessDateRange
func (s GoogleAnalyticsAdminV1betaAccessDateRange) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessDimension
func (s GoogleAnalyticsAdminV1betaAccessDimension) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessDimensionHeader
func (s GoogleAnalyticsAdminV1betaAccessDimensionHeader) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessDimensionValue
func (s GoogleAnalyticsAdminV1betaAccessDimensionValue) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessFilter
func (s GoogleAnalyticsAdminV1betaAccessFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessFilterExpression
func (s GoogleAnalyticsAdminV1betaAccessFilterExpression) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessFilterExpressionList
func (s GoogleAnalyticsAdminV1betaAccessFilterExpressionList) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessInListFilter
func (s GoogleAnalyticsAdminV1betaAccessInListFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessMetric
func (s GoogleAnalyticsAdminV1betaAccessMetric) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessMetricHeader
func (s GoogleAnalyticsAdminV1betaAccessMetricHeader) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessMetricValue
func (s GoogleAnalyticsAdminV1betaAccessMetricValue) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessNumericFilter
func (s GoogleAnalyticsAdminV1betaAccessNumericFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessOrderBy
func (s GoogleAnalyticsAdminV1betaAccessOrderBy) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderBy
func (s GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderBy) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderBy
func (s GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderBy) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessQuota
func (s GoogleAnalyticsAdminV1betaAccessQuota) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessQuotaStatus
func (s GoogleAnalyticsAdminV1betaAccessQuotaStatus) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessRow
func (s GoogleAnalyticsAdminV1betaAccessRow) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessStringFilter
func (s GoogleAnalyticsAdminV1betaAccessStringFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccount
func (s GoogleAnalyticsAdminV1betaAccount) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccountSummary
func (s GoogleAnalyticsAdminV1betaAccountSummary) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionRequest
func (s GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionResponse
type GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequest
type GoogleAnalyticsAdminV1betaArchiveCustomMetricRequest
type GoogleAnalyticsAdminV1betaChangeHistoryChange
func (s GoogleAnalyticsAdminV1betaChangeHistoryChange) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResource
func (s GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResource) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaChangeHistoryEvent
func (s GoogleAnalyticsAdminV1betaChangeHistoryEvent) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaConversionEvent
func (s GoogleAnalyticsAdminV1betaConversionEvent) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaConversionEventDefaultConversionValue
func (s GoogleAnalyticsAdminV1betaConversionEventDefaultConversionValue) MarshalJSON() ([]byte, error)
func (s *GoogleAnalyticsAdminV1betaConversionEventDefaultConversionValue) UnmarshalJSON(data []byte) error
type GoogleAnalyticsAdminV1betaCustomDimension
func (s GoogleAnalyticsAdminV1betaCustomDimension) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaCustomMetric
func (s GoogleAnalyticsAdminV1betaCustomMetric) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaDataRetentionSettings
func (s GoogleAnalyticsAdminV1betaDataRetentionSettings) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaDataSharingSettings
func (s GoogleAnalyticsAdminV1betaDataSharingSettings) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaDataStream
func (s GoogleAnalyticsAdminV1betaDataStream) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamData
func (s GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamData) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaDataStreamIosAppStreamData
func (s GoogleAnalyticsAdminV1betaDataStreamIosAppStreamData) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaDataStreamWebStreamData
func (s GoogleAnalyticsAdminV1betaDataStreamWebStreamData) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaFirebaseLink
func (s GoogleAnalyticsAdminV1betaFirebaseLink) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaGoogleAdsLink
func (s GoogleAnalyticsAdminV1betaGoogleAdsLink) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaKeyEvent
func (s GoogleAnalyticsAdminV1betaKeyEvent) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaKeyEventDefaultValue
func (s GoogleAnalyticsAdminV1betaKeyEventDefaultValue) MarshalJSON() ([]byte, error)
func (s *GoogleAnalyticsAdminV1betaKeyEventDefaultValue) UnmarshalJSON(data []byte) error
type GoogleAnalyticsAdminV1betaListAccountSummariesResponse
func (s GoogleAnalyticsAdminV1betaListAccountSummariesResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaListAccountsResponse
func (s GoogleAnalyticsAdminV1betaListAccountsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaListConversionEventsResponse
func (s GoogleAnalyticsAdminV1betaListConversionEventsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaListCustomDimensionsResponse
func (s GoogleAnalyticsAdminV1betaListCustomDimensionsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaListCustomMetricsResponse
func (s GoogleAnalyticsAdminV1betaListCustomMetricsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaListDataStreamsResponse
func (s GoogleAnalyticsAdminV1betaListDataStreamsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaListFirebaseLinksResponse
func (s GoogleAnalyticsAdminV1betaListFirebaseLinksResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponse
func (s GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaListKeyEventsResponse
func (s GoogleAnalyticsAdminV1betaListKeyEventsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponse
func (s GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaListPropertiesResponse
func (s GoogleAnalyticsAdminV1betaListPropertiesResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaMeasurementProtocolSecret
func (s GoogleAnalyticsAdminV1betaMeasurementProtocolSecret) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaNumericValue
func (s GoogleAnalyticsAdminV1betaNumericValue) MarshalJSON() ([]byte, error)
func (s *GoogleAnalyticsAdminV1betaNumericValue) UnmarshalJSON(data []byte) error
type GoogleAnalyticsAdminV1betaProperty
func (s GoogleAnalyticsAdminV1betaProperty) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaPropertySummary
func (s GoogleAnalyticsAdminV1betaPropertySummary) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaProvisionAccountTicketRequest
func (s GoogleAnalyticsAdminV1betaProvisionAccountTicketRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaProvisionAccountTicketResponse
func (s GoogleAnalyticsAdminV1betaProvisionAccountTicketResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaRunAccessReportRequest
func (s GoogleAnalyticsAdminV1betaRunAccessReportRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaRunAccessReportResponse
func (s GoogleAnalyticsAdminV1betaRunAccessReportResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequest
func (s GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponse
func (s GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponse) MarshalJSON() ([]byte, error)
type GoogleProtobufEmpty
type PropertiesAcknowledgeUserDataCollectionCall
func (c *PropertiesAcknowledgeUserDataCollectionCall) Context(ctx context.Context) *PropertiesAcknowledgeUserDataCollectionCall
func (c *PropertiesAcknowledgeUserDataCollectionCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionResponse, error)
func (c *PropertiesAcknowledgeUserDataCollectionCall) Fields(s ...googleapi.Field) *PropertiesAcknowledgeUserDataCollectionCall
func (c *PropertiesAcknowledgeUserDataCollectionCall) Header() http.Header
type PropertiesConversionEventsCreateCall
func (c *PropertiesConversionEventsCreateCall) Context(ctx context.Context) *PropertiesConversionEventsCreateCall
func (c *PropertiesConversionEventsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaConversionEvent, error)
func (c *PropertiesConversionEventsCreateCall) Fields(s ...googleapi.Field) *PropertiesConversionEventsCreateCall
func (c *PropertiesConversionEventsCreateCall) Header() http.Header
type PropertiesConversionEventsDeleteCall
func (c *PropertiesConversionEventsDeleteCall) Context(ctx context.Context) *PropertiesConversionEventsDeleteCall
func (c *PropertiesConversionEventsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesConversionEventsDeleteCall) Fields(s ...googleapi.Field) *PropertiesConversionEventsDeleteCall
func (c *PropertiesConversionEventsDeleteCall) Header() http.Header
type PropertiesConversionEventsGetCall
func (c *PropertiesConversionEventsGetCall) Context(ctx context.Context) *PropertiesConversionEventsGetCall
func (c *PropertiesConversionEventsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaConversionEvent, error)
func (c *PropertiesConversionEventsGetCall) Fields(s ...googleapi.Field) *PropertiesConversionEventsGetCall
func (c *PropertiesConversionEventsGetCall) Header() http.Header
func (c *PropertiesConversionEventsGetCall) IfNoneMatch(entityTag string) *PropertiesConversionEventsGetCall
type PropertiesConversionEventsListCall
func (c *PropertiesConversionEventsListCall) Context(ctx context.Context) *PropertiesConversionEventsListCall
func (c *PropertiesConversionEventsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaListConversionEventsResponse, error)
func (c *PropertiesConversionEventsListCall) Fields(s ...googleapi.Field) *PropertiesConversionEventsListCall
func (c *PropertiesConversionEventsListCall) Header() http.Header
func (c *PropertiesConversionEventsListCall) IfNoneMatch(entityTag string) *PropertiesConversionEventsListCall
func (c *PropertiesConversionEventsListCall) PageSize(pageSize int64) *PropertiesConversionEventsListCall
func (c *PropertiesConversionEventsListCall) PageToken(pageToken string) *PropertiesConversionEventsListCall
func (c *PropertiesConversionEventsListCall) Pages(ctx context.Context, ...) error
type PropertiesConversionEventsPatchCall
func (c *PropertiesConversionEventsPatchCall) Context(ctx context.Context) *PropertiesConversionEventsPatchCall
func (c *PropertiesConversionEventsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaConversionEvent, error)
func (c *PropertiesConversionEventsPatchCall) Fields(s ...googleapi.Field) *PropertiesConversionEventsPatchCall
func (c *PropertiesConversionEventsPatchCall) Header() http.Header
func (c *PropertiesConversionEventsPatchCall) UpdateMask(updateMask string) *PropertiesConversionEventsPatchCall
type PropertiesConversionEventsService
func NewPropertiesConversionEventsService(s *Service) *PropertiesConversionEventsService
func (r *PropertiesConversionEventsService) Create(parent string, ...) *PropertiesConversionEventsCreateCall
func (r *PropertiesConversionEventsService) Delete(name string) *PropertiesConversionEventsDeleteCall
func (r *PropertiesConversionEventsService) Get(name string) *PropertiesConversionEventsGetCall
func (r *PropertiesConversionEventsService) List(parent string) *PropertiesConversionEventsListCall
func (r *PropertiesConversionEventsService) Patch(name string, ...) *PropertiesConversionEventsPatchCall
type PropertiesCreateCall
func (c *PropertiesCreateCall) Context(ctx context.Context) *PropertiesCreateCall
func (c *PropertiesCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaProperty, error)
func (c *PropertiesCreateCall) Fields(s ...googleapi.Field) *PropertiesCreateCall
func (c *PropertiesCreateCall) Header() http.Header
type PropertiesCustomDimensionsArchiveCall
func (c *PropertiesCustomDimensionsArchiveCall) Context(ctx context.Context) *PropertiesCustomDimensionsArchiveCall
func (c *PropertiesCustomDimensionsArchiveCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesCustomDimensionsArchiveCall) Fields(s ...googleapi.Field) *PropertiesCustomDimensionsArchiveCall
func (c *PropertiesCustomDimensionsArchiveCall) Header() http.Header
type PropertiesCustomDimensionsCreateCall
func (c *PropertiesCustomDimensionsCreateCall) Context(ctx context.Context) *PropertiesCustomDimensionsCreateCall
func (c *PropertiesCustomDimensionsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaCustomDimension, error)
func (c *PropertiesCustomDimensionsCreateCall) Fields(s ...googleapi.Field) *PropertiesCustomDimensionsCreateCall
func (c *PropertiesCustomDimensionsCreateCall) Header() http.Header
type PropertiesCustomDimensionsGetCall
func (c *PropertiesCustomDimensionsGetCall) Context(ctx context.Context) *PropertiesCustomDimensionsGetCall
func (c *PropertiesCustomDimensionsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaCustomDimension, error)
func (c *PropertiesCustomDimensionsGetCall) Fields(s ...googleapi.Field) *PropertiesCustomDimensionsGetCall
func (c *PropertiesCustomDimensionsGetCall) Header() http.Header
func (c *PropertiesCustomDimensionsGetCall) IfNoneMatch(entityTag string) *PropertiesCustomDimensionsGetCall
type PropertiesCustomDimensionsListCall
func (c *PropertiesCustomDimensionsListCall) Context(ctx context.Context) *PropertiesCustomDimensionsListCall
func (c *PropertiesCustomDimensionsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaListCustomDimensionsResponse, error)
func (c *PropertiesCustomDimensionsListCall) Fields(s ...googleapi.Field) *PropertiesCustomDimensionsListCall
func (c *PropertiesCustomDimensionsListCall) Header() http.Header
func (c *PropertiesCustomDimensionsListCall) IfNoneMatch(entityTag string) *PropertiesCustomDimensionsListCall
func (c *PropertiesCustomDimensionsListCall) PageSize(pageSize int64) *PropertiesCustomDimensionsListCall
func (c *PropertiesCustomDimensionsListCall) PageToken(pageToken string) *PropertiesCustomDimensionsListCall
func (c *PropertiesCustomDimensionsListCall) Pages(ctx context.Context, ...) error
type PropertiesCustomDimensionsPatchCall
func (c *PropertiesCustomDimensionsPatchCall) Context(ctx context.Context) *PropertiesCustomDimensionsPatchCall
func (c *PropertiesCustomDimensionsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaCustomDimension, error)
func (c *PropertiesCustomDimensionsPatchCall) Fields(s ...googleapi.Field) *PropertiesCustomDimensionsPatchCall
func (c *PropertiesCustomDimensionsPatchCall) Header() http.Header
func (c *PropertiesCustomDimensionsPatchCall) UpdateMask(updateMask string) *PropertiesCustomDimensionsPatchCall
type PropertiesCustomDimensionsService
func NewPropertiesCustomDimensionsService(s *Service) *PropertiesCustomDimensionsService
func (r *PropertiesCustomDimensionsService) Archive(name string, ...) *PropertiesCustomDimensionsArchiveCall
func (r *PropertiesCustomDimensionsService) Create(parent string, ...) *PropertiesCustomDimensionsCreateCall
func (r *PropertiesCustomDimensionsService) Get(name string) *PropertiesCustomDimensionsGetCall
func (r *PropertiesCustomDimensionsService) List(parent string) *PropertiesCustomDimensionsListCall
func (r *PropertiesCustomDimensionsService) Patch(name string, ...) *PropertiesCustomDimensionsPatchCall
type PropertiesCustomMetricsArchiveCall
func (c *PropertiesCustomMetricsArchiveCall) Context(ctx context.Context) *PropertiesCustomMetricsArchiveCall
func (c *PropertiesCustomMetricsArchiveCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesCustomMetricsArchiveCall) Fields(s ...googleapi.Field) *PropertiesCustomMetricsArchiveCall
func (c *PropertiesCustomMetricsArchiveCall) Header() http.Header
type PropertiesCustomMetricsCreateCall
func (c *PropertiesCustomMetricsCreateCall) Context(ctx context.Context) *PropertiesCustomMetricsCreateCall
func (c *PropertiesCustomMetricsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaCustomMetric, error)
func (c *PropertiesCustomMetricsCreateCall) Fields(s ...googleapi.Field) *PropertiesCustomMetricsCreateCall
func (c *PropertiesCustomMetricsCreateCall) Header() http.Header
type PropertiesCustomMetricsGetCall
func (c *PropertiesCustomMetricsGetCall) Context(ctx context.Context) *PropertiesCustomMetricsGetCall
func (c *PropertiesCustomMetricsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaCustomMetric, error)
func (c *PropertiesCustomMetricsGetCall) Fields(s ...googleapi.Field) *PropertiesCustomMetricsGetCall
func (c *PropertiesCustomMetricsGetCall) Header() http.Header
func (c *PropertiesCustomMetricsGetCall) IfNoneMatch(entityTag string) *PropertiesCustomMetricsGetCall
type PropertiesCustomMetricsListCall
func (c *PropertiesCustomMetricsListCall) Context(ctx context.Context) *PropertiesCustomMetricsListCall
func (c *PropertiesCustomMetricsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaListCustomMetricsResponse, error)
func (c *PropertiesCustomMetricsListCall) Fields(s ...googleapi.Field) *PropertiesCustomMetricsListCall
func (c *PropertiesCustomMetricsListCall) Header() http.Header
func (c *PropertiesCustomMetricsListCall) IfNoneMatch(entityTag string) *PropertiesCustomMetricsListCall
func (c *PropertiesCustomMetricsListCall) PageSize(pageSize int64) *PropertiesCustomMetricsListCall
func (c *PropertiesCustomMetricsListCall) PageToken(pageToken string) *PropertiesCustomMetricsListCall
func (c *PropertiesCustomMetricsListCall) Pages(ctx context.Context, ...) error
type PropertiesCustomMetricsPatchCall
func (c *PropertiesCustomMetricsPatchCall) Context(ctx context.Context) *PropertiesCustomMetricsPatchCall
func (c *PropertiesCustomMetricsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaCustomMetric, error)
func (c *PropertiesCustomMetricsPatchCall) Fields(s ...googleapi.Field) *PropertiesCustomMetricsPatchCall
func (c *PropertiesCustomMetricsPatchCall) Header() http.Header
func (c *PropertiesCustomMetricsPatchCall) UpdateMask(updateMask string) *PropertiesCustomMetricsPatchCall
type PropertiesCustomMetricsService
func NewPropertiesCustomMetricsService(s *Service) *PropertiesCustomMetricsService
func (r *PropertiesCustomMetricsService) Archive(name string, ...) *PropertiesCustomMetricsArchiveCall
func (r *PropertiesCustomMetricsService) Create(parent string, ...) *PropertiesCustomMetricsCreateCall
func (r *PropertiesCustomMetricsService) Get(name string) *PropertiesCustomMetricsGetCall
func (r *PropertiesCustomMetricsService) List(parent string) *PropertiesCustomMetricsListCall
func (r *PropertiesCustomMetricsService) Patch(name string, ...) *PropertiesCustomMetricsPatchCall
type PropertiesDataStreamsCreateCall
func (c *PropertiesDataStreamsCreateCall) Context(ctx context.Context) *PropertiesDataStreamsCreateCall
func (c *PropertiesDataStreamsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaDataStream, error)
func (c *PropertiesDataStreamsCreateCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsCreateCall
func (c *PropertiesDataStreamsCreateCall) Header() http.Header
type PropertiesDataStreamsDeleteCall
func (c *PropertiesDataStreamsDeleteCall) Context(ctx context.Context) *PropertiesDataStreamsDeleteCall
func (c *PropertiesDataStreamsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesDataStreamsDeleteCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsDeleteCall
func (c *PropertiesDataStreamsDeleteCall) Header() http.Header
type PropertiesDataStreamsGetCall
func (c *PropertiesDataStreamsGetCall) Context(ctx context.Context) *PropertiesDataStreamsGetCall
func (c *PropertiesDataStreamsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaDataStream, error)
func (c *PropertiesDataStreamsGetCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsGetCall
func (c *PropertiesDataStreamsGetCall) Header() http.Header
func (c *PropertiesDataStreamsGetCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsGetCall
type PropertiesDataStreamsListCall
func (c *PropertiesDataStreamsListCall) Context(ctx context.Context) *PropertiesDataStreamsListCall
func (c *PropertiesDataStreamsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaListDataStreamsResponse, error)
func (c *PropertiesDataStreamsListCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsListCall
func (c *PropertiesDataStreamsListCall) Header() http.Header
func (c *PropertiesDataStreamsListCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsListCall
func (c *PropertiesDataStreamsListCall) PageSize(pageSize int64) *PropertiesDataStreamsListCall
func (c *PropertiesDataStreamsListCall) PageToken(pageToken string) *PropertiesDataStreamsListCall
func (c *PropertiesDataStreamsListCall) Pages(ctx context.Context, ...) error
type PropertiesDataStreamsMeasurementProtocolSecretsCreateCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsCreateCall) Context(ctx context.Context) *PropertiesDataStreamsMeasurementProtocolSecretsCreateCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaMeasurementProtocolSecret, error)
func (c *PropertiesDataStreamsMeasurementProtocolSecretsCreateCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsMeasurementProtocolSecretsCreateCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsCreateCall) Header() http.Header
type PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall) Context(ctx context.Context) *PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall) Header() http.Header
type PropertiesDataStreamsMeasurementProtocolSecretsGetCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsGetCall) Context(ctx context.Context) *PropertiesDataStreamsMeasurementProtocolSecretsGetCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaMeasurementProtocolSecret, error)
func (c *PropertiesDataStreamsMeasurementProtocolSecretsGetCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsMeasurementProtocolSecretsGetCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsGetCall) Header() http.Header
func (c *PropertiesDataStreamsMeasurementProtocolSecretsGetCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsMeasurementProtocolSecretsGetCall
type PropertiesDataStreamsMeasurementProtocolSecretsListCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) Context(ctx context.Context) *PropertiesDataStreamsMeasurementProtocolSecretsListCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponse, error)
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsMeasurementProtocolSecretsListCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) Header() http.Header
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsMeasurementProtocolSecretsListCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) PageSize(pageSize int64) *PropertiesDataStreamsMeasurementProtocolSecretsListCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) PageToken(pageToken string) *PropertiesDataStreamsMeasurementProtocolSecretsListCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) Pages(ctx context.Context, ...) error
type PropertiesDataStreamsMeasurementProtocolSecretsPatchCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsPatchCall) Context(ctx context.Context) *PropertiesDataStreamsMeasurementProtocolSecretsPatchCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaMeasurementProtocolSecret, error)
func (c *PropertiesDataStreamsMeasurementProtocolSecretsPatchCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsMeasurementProtocolSecretsPatchCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsPatchCall) Header() http.Header
func (c *PropertiesDataStreamsMeasurementProtocolSecretsPatchCall) UpdateMask(updateMask string) *PropertiesDataStreamsMeasurementProtocolSecretsPatchCall
type PropertiesDataStreamsMeasurementProtocolSecretsService
func NewPropertiesDataStreamsMeasurementProtocolSecretsService(s *Service) *PropertiesDataStreamsMeasurementProtocolSecretsService
func (r *PropertiesDataStreamsMeasurementProtocolSecretsService) Create(parent string, ...) *PropertiesDataStreamsMeasurementProtocolSecretsCreateCall
func (r *PropertiesDataStreamsMeasurementProtocolSecretsService) Delete(name string) *PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall
func (r *PropertiesDataStreamsMeasurementProtocolSecretsService) Get(name string) *PropertiesDataStreamsMeasurementProtocolSecretsGetCall
func (r *PropertiesDataStreamsMeasurementProtocolSecretsService) List(parent string) *PropertiesDataStreamsMeasurementProtocolSecretsListCall
func (r *PropertiesDataStreamsMeasurementProtocolSecretsService) Patch(name string, ...) *PropertiesDataStreamsMeasurementProtocolSecretsPatchCall
type PropertiesDataStreamsPatchCall
func (c *PropertiesDataStreamsPatchCall) Context(ctx context.Context) *PropertiesDataStreamsPatchCall
func (c *PropertiesDataStreamsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaDataStream, error)
func (c *PropertiesDataStreamsPatchCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsPatchCall
func (c *PropertiesDataStreamsPatchCall) Header() http.Header
func (c *PropertiesDataStreamsPatchCall) UpdateMask(updateMask string) *PropertiesDataStreamsPatchCall
type PropertiesDataStreamsService
func NewPropertiesDataStreamsService(s *Service) *PropertiesDataStreamsService
func (r *PropertiesDataStreamsService) Create(parent string, ...) *PropertiesDataStreamsCreateCall
func (r *PropertiesDataStreamsService) Delete(name string) *PropertiesDataStreamsDeleteCall
func (r *PropertiesDataStreamsService) Get(name string) *PropertiesDataStreamsGetCall
func (r *PropertiesDataStreamsService) List(parent string) *PropertiesDataStreamsListCall
func (r *PropertiesDataStreamsService) Patch(name string, ...) *PropertiesDataStreamsPatchCall
type PropertiesDeleteCall
func (c *PropertiesDeleteCall) Context(ctx context.Context) *PropertiesDeleteCall
func (c *PropertiesDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaProperty, error)
func (c *PropertiesDeleteCall) Fields(s ...googleapi.Field) *PropertiesDeleteCall
func (c *PropertiesDeleteCall) Header() http.Header
type PropertiesFirebaseLinksCreateCall
func (c *PropertiesFirebaseLinksCreateCall) Context(ctx context.Context) *PropertiesFirebaseLinksCreateCall
func (c *PropertiesFirebaseLinksCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaFirebaseLink, error)
func (c *PropertiesFirebaseLinksCreateCall) Fields(s ...googleapi.Field) *PropertiesFirebaseLinksCreateCall
func (c *PropertiesFirebaseLinksCreateCall) Header() http.Header
type PropertiesFirebaseLinksDeleteCall
func (c *PropertiesFirebaseLinksDeleteCall) Context(ctx context.Context) *PropertiesFirebaseLinksDeleteCall
func (c *PropertiesFirebaseLinksDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesFirebaseLinksDeleteCall) Fields(s ...googleapi.Field) *PropertiesFirebaseLinksDeleteCall
func (c *PropertiesFirebaseLinksDeleteCall) Header() http.Header
type PropertiesFirebaseLinksListCall
func (c *PropertiesFirebaseLinksListCall) Context(ctx context.Context) *PropertiesFirebaseLinksListCall
func (c *PropertiesFirebaseLinksListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaListFirebaseLinksResponse, error)
func (c *PropertiesFirebaseLinksListCall) Fields(s ...googleapi.Field) *PropertiesFirebaseLinksListCall
func (c *PropertiesFirebaseLinksListCall) Header() http.Header
func (c *PropertiesFirebaseLinksListCall) IfNoneMatch(entityTag string) *PropertiesFirebaseLinksListCall
func (c *PropertiesFirebaseLinksListCall) PageSize(pageSize int64) *PropertiesFirebaseLinksListCall
func (c *PropertiesFirebaseLinksListCall) PageToken(pageToken string) *PropertiesFirebaseLinksListCall
func (c *PropertiesFirebaseLinksListCall) Pages(ctx context.Context, ...) error
type PropertiesFirebaseLinksService
func NewPropertiesFirebaseLinksService(s *Service) *PropertiesFirebaseLinksService
func (r *PropertiesFirebaseLinksService) Create(parent string, ...) *PropertiesFirebaseLinksCreateCall
func (r *PropertiesFirebaseLinksService) Delete(name string) *PropertiesFirebaseLinksDeleteCall
func (r *PropertiesFirebaseLinksService) List(parent string) *PropertiesFirebaseLinksListCall
type PropertiesGetCall
func (c *PropertiesGetCall) Context(ctx context.Context) *PropertiesGetCall
func (c *PropertiesGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaProperty, error)
func (c *PropertiesGetCall) Fields(s ...googleapi.Field) *PropertiesGetCall
func (c *PropertiesGetCall) Header() http.Header
func (c *PropertiesGetCall) IfNoneMatch(entityTag string) *PropertiesGetCall
type PropertiesGetDataRetentionSettingsCall
func (c *PropertiesGetDataRetentionSettingsCall) Context(ctx context.Context) *PropertiesGetDataRetentionSettingsCall
func (c *PropertiesGetDataRetentionSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaDataRetentionSettings, error)
func (c *PropertiesGetDataRetentionSettingsCall) Fields(s ...googleapi.Field) *PropertiesGetDataRetentionSettingsCall
func (c *PropertiesGetDataRetentionSettingsCall) Header() http.Header
func (c *PropertiesGetDataRetentionSettingsCall) IfNoneMatch(entityTag string) *PropertiesGetDataRetentionSettingsCall
type PropertiesGoogleAdsLinksCreateCall
func (c *PropertiesGoogleAdsLinksCreateCall) Context(ctx context.Context) *PropertiesGoogleAdsLinksCreateCall
func (c *PropertiesGoogleAdsLinksCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaGoogleAdsLink, error)
func (c *PropertiesGoogleAdsLinksCreateCall) Fields(s ...googleapi.Field) *PropertiesGoogleAdsLinksCreateCall
func (c *PropertiesGoogleAdsLinksCreateCall) Header() http.Header
type PropertiesGoogleAdsLinksDeleteCall
func (c *PropertiesGoogleAdsLinksDeleteCall) Context(ctx context.Context) *PropertiesGoogleAdsLinksDeleteCall
func (c *PropertiesGoogleAdsLinksDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesGoogleAdsLinksDeleteCall) Fields(s ...googleapi.Field) *PropertiesGoogleAdsLinksDeleteCall
func (c *PropertiesGoogleAdsLinksDeleteCall) Header() http.Header
type PropertiesGoogleAdsLinksListCall
func (c *PropertiesGoogleAdsLinksListCall) Context(ctx context.Context) *PropertiesGoogleAdsLinksListCall
func (c *PropertiesGoogleAdsLinksListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponse, error)
func (c *PropertiesGoogleAdsLinksListCall) Fields(s ...googleapi.Field) *PropertiesGoogleAdsLinksListCall
func (c *PropertiesGoogleAdsLinksListCall) Header() http.Header
func (c *PropertiesGoogleAdsLinksListCall) IfNoneMatch(entityTag string) *PropertiesGoogleAdsLinksListCall
func (c *PropertiesGoogleAdsLinksListCall) PageSize(pageSize int64) *PropertiesGoogleAdsLinksListCall
func (c *PropertiesGoogleAdsLinksListCall) PageToken(pageToken string) *PropertiesGoogleAdsLinksListCall
func (c *PropertiesGoogleAdsLinksListCall) Pages(ctx context.Context, ...) error
type PropertiesGoogleAdsLinksPatchCall
func (c *PropertiesGoogleAdsLinksPatchCall) Context(ctx context.Context) *PropertiesGoogleAdsLinksPatchCall
func (c *PropertiesGoogleAdsLinksPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaGoogleAdsLink, error)
func (c *PropertiesGoogleAdsLinksPatchCall) Fields(s ...googleapi.Field) *PropertiesGoogleAdsLinksPatchCall
func (c *PropertiesGoogleAdsLinksPatchCall) Header() http.Header
func (c *PropertiesGoogleAdsLinksPatchCall) UpdateMask(updateMask string) *PropertiesGoogleAdsLinksPatchCall
type PropertiesGoogleAdsLinksService
func NewPropertiesGoogleAdsLinksService(s *Service) *PropertiesGoogleAdsLinksService
func (r *PropertiesGoogleAdsLinksService) Create(parent string, ...) *PropertiesGoogleAdsLinksCreateCall
func (r *PropertiesGoogleAdsLinksService) Delete(name string) *PropertiesGoogleAdsLinksDeleteCall
func (r *PropertiesGoogleAdsLinksService) List(parent string) *PropertiesGoogleAdsLinksListCall
func (r *PropertiesGoogleAdsLinksService) Patch(name string, ...) *PropertiesGoogleAdsLinksPatchCall
type PropertiesKeyEventsCreateCall
func (c *PropertiesKeyEventsCreateCall) Context(ctx context.Context) *PropertiesKeyEventsCreateCall
func (c *PropertiesKeyEventsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaKeyEvent, error)
func (c *PropertiesKeyEventsCreateCall) Fields(s ...googleapi.Field) *PropertiesKeyEventsCreateCall
func (c *PropertiesKeyEventsCreateCall) Header() http.Header
type PropertiesKeyEventsDeleteCall
func (c *PropertiesKeyEventsDeleteCall) Context(ctx context.Context) *PropertiesKeyEventsDeleteCall
func (c *PropertiesKeyEventsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesKeyEventsDeleteCall) Fields(s ...googleapi.Field) *PropertiesKeyEventsDeleteCall
func (c *PropertiesKeyEventsDeleteCall) Header() http.Header
type PropertiesKeyEventsGetCall
func (c *PropertiesKeyEventsGetCall) Context(ctx context.Context) *PropertiesKeyEventsGetCall
func (c *PropertiesKeyEventsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaKeyEvent, error)
func (c *PropertiesKeyEventsGetCall) Fields(s ...googleapi.Field) *PropertiesKeyEventsGetCall
func (c *PropertiesKeyEventsGetCall) Header() http.Header
func (c *PropertiesKeyEventsGetCall) IfNoneMatch(entityTag string) *PropertiesKeyEventsGetCall
type PropertiesKeyEventsListCall
func (c *PropertiesKeyEventsListCall) Context(ctx context.Context) *PropertiesKeyEventsListCall
func (c *PropertiesKeyEventsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaListKeyEventsResponse, error)
func (c *PropertiesKeyEventsListCall) Fields(s ...googleapi.Field) *PropertiesKeyEventsListCall
func (c *PropertiesKeyEventsListCall) Header() http.Header
func (c *PropertiesKeyEventsListCall) IfNoneMatch(entityTag string) *PropertiesKeyEventsListCall
func (c *PropertiesKeyEventsListCall) PageSize(pageSize int64) *PropertiesKeyEventsListCall
func (c *PropertiesKeyEventsListCall) PageToken(pageToken string) *PropertiesKeyEventsListCall
func (c *PropertiesKeyEventsListCall) Pages(ctx context.Context, ...) error
type PropertiesKeyEventsPatchCall
func (c *PropertiesKeyEventsPatchCall) Context(ctx context.Context) *PropertiesKeyEventsPatchCall
func (c *PropertiesKeyEventsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaKeyEvent, error)
func (c *PropertiesKeyEventsPatchCall) Fields(s ...googleapi.Field) *PropertiesKeyEventsPatchCall
func (c *PropertiesKeyEventsPatchCall) Header() http.Header
func (c *PropertiesKeyEventsPatchCall) UpdateMask(updateMask string) *PropertiesKeyEventsPatchCall
type PropertiesKeyEventsService
func NewPropertiesKeyEventsService(s *Service) *PropertiesKeyEventsService
func (r *PropertiesKeyEventsService) Create(parent string, ...) *PropertiesKeyEventsCreateCall
func (r *PropertiesKeyEventsService) Delete(name string) *PropertiesKeyEventsDeleteCall
func (r *PropertiesKeyEventsService) Get(name string) *PropertiesKeyEventsGetCall
func (r *PropertiesKeyEventsService) List(parent string) *PropertiesKeyEventsListCall
func (r *PropertiesKeyEventsService) Patch(name string, ...) *PropertiesKeyEventsPatchCall
type PropertiesListCall
func (c *PropertiesListCall) Context(ctx context.Context) *PropertiesListCall
func (c *PropertiesListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaListPropertiesResponse, error)
func (c *PropertiesListCall) Fields(s ...googleapi.Field) *PropertiesListCall
func (c *PropertiesListCall) Filter(filter string) *PropertiesListCall
func (c *PropertiesListCall) Header() http.Header
func (c *PropertiesListCall) IfNoneMatch(entityTag string) *PropertiesListCall
func (c *PropertiesListCall) PageSize(pageSize int64) *PropertiesListCall
func (c *PropertiesListCall) PageToken(pageToken string) *PropertiesListCall
func (c *PropertiesListCall) Pages(ctx context.Context, ...) error
func (c *PropertiesListCall) ShowDeleted(showDeleted bool) *PropertiesListCall
type PropertiesPatchCall
func (c *PropertiesPatchCall) Context(ctx context.Context) *PropertiesPatchCall
func (c *PropertiesPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaProperty, error)
func (c *PropertiesPatchCall) Fields(s ...googleapi.Field) *PropertiesPatchCall
func (c *PropertiesPatchCall) Header() http.Header
func (c *PropertiesPatchCall) UpdateMask(updateMask string) *PropertiesPatchCall
type PropertiesRunAccessReportCall
func (c *PropertiesRunAccessReportCall) Context(ctx context.Context) *PropertiesRunAccessReportCall
func (c *PropertiesRunAccessReportCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaRunAccessReportResponse, error)
func (c *PropertiesRunAccessReportCall) Fields(s ...googleapi.Field) *PropertiesRunAccessReportCall
func (c *PropertiesRunAccessReportCall) Header() http.Header
type PropertiesService
func NewPropertiesService(s *Service) *PropertiesService
func (r *PropertiesService) AcknowledgeUserDataCollection(property string, ...) *PropertiesAcknowledgeUserDataCollectionCall
func (r *PropertiesService) Create(googleanalyticsadminv1betaproperty *GoogleAnalyticsAdminV1betaProperty) *PropertiesCreateCall
func (r *PropertiesService) Delete(name string) *PropertiesDeleteCall
func (r *PropertiesService) Get(name string) *PropertiesGetCall
func (r *PropertiesService) GetDataRetentionSettings(name string) *PropertiesGetDataRetentionSettingsCall
func (r *PropertiesService) List() *PropertiesListCall
func (r *PropertiesService) Patch(name string, ...) *PropertiesPatchCall
func (r *PropertiesService) RunAccessReport(entity string, ...) *PropertiesRunAccessReportCall
func (r *PropertiesService) UpdateDataRetentionSettings(name string, ...) *PropertiesUpdateDataRetentionSettingsCall
type PropertiesUpdateDataRetentionSettingsCall
func (c *PropertiesUpdateDataRetentionSettingsCall) Context(ctx context.Context) *PropertiesUpdateDataRetentionSettingsCall
func (c *PropertiesUpdateDataRetentionSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaDataRetentionSettings, error)
func (c *PropertiesUpdateDataRetentionSettingsCall) Fields(s ...googleapi.Field) *PropertiesUpdateDataRetentionSettingsCall
func (c *PropertiesUpdateDataRetentionSettingsCall) Header() http.Header
func (c *PropertiesUpdateDataRetentionSettingsCall) UpdateMask(updateMask string) *PropertiesUpdateDataRetentionSettingsCall
type Service
func New(client *http.Client) (*Service, error)DEPRECATED
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)
Constants ¶
View Source
const (
	// Edit Google Analytics management entities
	AnalyticsEditScope = "https://www.googleapis.com/auth/analytics.edit"

	// See and download your Google Analytics data
	AnalyticsReadonlyScope = "https://www.googleapis.com/auth/analytics.readonly"
)

OAuth2 scopes used by this API.

Variables ¶

This section is empty.

Functions ¶

This section is empty.

Types ¶
type AccountSummariesListCall ¶
type AccountSummariesListCall struct {
	// contains filtered or unexported fields
}
func (*AccountSummariesListCall) Context ¶
func (c *AccountSummariesListCall) Context(ctx context.Context) *AccountSummariesListCall

Context sets the context to be used in this call's Do method.

func (*AccountSummariesListCall) Do ¶
func (c *AccountSummariesListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaListAccountSummariesResponse, error)

Do executes the "analyticsadmin.accountSummaries.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaListAccountSummariesResponse.ServerResponse.Header

or (if a response was returned at all) in error.(*googleapi.Error).Header.


Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountSummariesListCall) Fields ¶
func (c *AccountSummariesListCall) Fields(s ...googleapi.Field) *AccountSummariesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountSummariesListCall) Header ¶
func (c *AccountSummariesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccountSummariesListCall) IfNoneMatch ¶
func (c *AccountSummariesListCall) IfNoneMatch(entityTag string) *AccountSummariesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*AccountSummariesListCall) PageSize ¶
func (c *AccountSummariesListCall) PageSize(pageSize int64) *AccountSummariesListCall

PageSize sets the optional parameter "pageSize": The maximum number of AccountSummary resources to return. The service may return fewer than this value, even if there are additional pages. If unspecified, at most 50 resources will be returned. The maximum value is 200; (higher values will be coerced to the maximum)

func (*AccountSummariesListCall) PageToken ¶
func (c *AccountSummariesListCall) PageToken(pageToken string) *AccountSummariesListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListAccountSummaries` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListAccountSummaries` must match the call that provided the page token.

func (*AccountSummariesListCall) Pages ¶
func (c *AccountSummariesListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1betaListAccountSummariesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountSummariesService ¶
type AccountSummariesService struct {
	// contains filtered or unexported fields
}
func NewAccountSummariesService ¶
func NewAccountSummariesService(s *Service) *AccountSummariesService
func (*AccountSummariesService) List ¶
func (r *AccountSummariesService) List() *AccountSummariesListCall

List: Returns summaries of all accounts accessible by the caller.

type AccountsDeleteCall ¶
type AccountsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*AccountsDeleteCall) Context ¶
func (c *AccountsDeleteCall) Context(ctx context.Context) *AccountsDeleteCall

Context sets the context to be used in this call's Do method.

func (*AccountsDeleteCall) Do ¶
func (c *AccountsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.accounts.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsDeleteCall) Fields ¶
func (c *AccountsDeleteCall) Fields(s ...googleapi.Field) *AccountsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsDeleteCall) Header ¶
func (c *AccountsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsGetCall ¶
type AccountsGetCall struct {
	// contains filtered or unexported fields
}
func (*AccountsGetCall) Context ¶
func (c *AccountsGetCall) Context(ctx context.Context) *AccountsGetCall

Context sets the context to be used in this call's Do method.

func (*AccountsGetCall) Do ¶
func (c *AccountsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaAccount, error)

Do executes the "analyticsadmin.accounts.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaAccount.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsGetCall) Fields ¶
func (c *AccountsGetCall) Fields(s ...googleapi.Field) *AccountsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsGetCall) Header ¶
func (c *AccountsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccountsGetCall) IfNoneMatch ¶
func (c *AccountsGetCall) IfNoneMatch(entityTag string) *AccountsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AccountsGetDataSharingSettingsCall ¶
type AccountsGetDataSharingSettingsCall struct {
	// contains filtered or unexported fields
}
func (*AccountsGetDataSharingSettingsCall) Context ¶
func (c *AccountsGetDataSharingSettingsCall) Context(ctx context.Context) *AccountsGetDataSharingSettingsCall

Context sets the context to be used in this call's Do method.

func (*AccountsGetDataSharingSettingsCall) Do ¶
func (c *AccountsGetDataSharingSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaDataSharingSettings, error)

Do executes the "analyticsadmin.accounts.getDataSharingSettings" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaDataSharingSettings.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsGetDataSharingSettingsCall) Fields ¶
func (c *AccountsGetDataSharingSettingsCall) Fields(s ...googleapi.Field) *AccountsGetDataSharingSettingsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsGetDataSharingSettingsCall) Header ¶
func (c *AccountsGetDataSharingSettingsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccountsGetDataSharingSettingsCall) IfNoneMatch ¶
func (c *AccountsGetDataSharingSettingsCall) IfNoneMatch(entityTag string) *AccountsGetDataSharingSettingsCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AccountsListCall ¶
type AccountsListCall struct {
	// contains filtered or unexported fields
}
func (*AccountsListCall) Context ¶
func (c *AccountsListCall) Context(ctx context.Context) *AccountsListCall

Context sets the context to be used in this call's Do method.

func (*AccountsListCall) Do ¶
func (c *AccountsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaListAccountsResponse, error)

Do executes the "analyticsadmin.accounts.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaListAccountsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsListCall) Fields ¶
func (c *AccountsListCall) Fields(s ...googleapi.Field) *AccountsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsListCall) Header ¶
func (c *AccountsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccountsListCall) IfNoneMatch ¶
func (c *AccountsListCall) IfNoneMatch(entityTag string) *AccountsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*AccountsListCall) PageSize ¶
func (c *AccountsListCall) PageSize(pageSize int64) *AccountsListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. The service may return fewer than this value, even if there are additional pages. If unspecified, at most 50 resources will be returned. The maximum value is 200; (higher values will be coerced to the maximum)

func (*AccountsListCall) PageToken ¶
func (c *AccountsListCall) PageToken(pageToken string) *AccountsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListAccounts` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListAccounts` must match the call that provided the page token.

func (*AccountsListCall) Pages ¶
func (c *AccountsListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1betaListAccountsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*AccountsListCall) ShowDeleted ¶
func (c *AccountsListCall) ShowDeleted(showDeleted bool) *AccountsListCall

ShowDeleted sets the optional parameter "showDeleted": Whether to include soft-deleted (ie: "trashed") Accounts in the results. Accounts can be inspected to determine whether they are deleted or not.

type AccountsPatchCall ¶
type AccountsPatchCall struct {
	// contains filtered or unexported fields
}
func (*AccountsPatchCall) Context ¶
func (c *AccountsPatchCall) Context(ctx context.Context) *AccountsPatchCall

Context sets the context to be used in this call's Do method.

func (*AccountsPatchCall) Do ¶
func (c *AccountsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaAccount, error)

Do executes the "analyticsadmin.accounts.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaAccount.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsPatchCall) Fields ¶
func (c *AccountsPatchCall) Fields(s ...googleapi.Field) *AccountsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsPatchCall) Header ¶
func (c *AccountsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccountsPatchCall) UpdateMask ¶
func (c *AccountsPatchCall) UpdateMask(updateMask string) *AccountsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated. Field names must be in snake case (for example, "field_to_update"). Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.

type AccountsProvisionAccountTicketCall ¶
type AccountsProvisionAccountTicketCall struct {
	// contains filtered or unexported fields
}
func (*AccountsProvisionAccountTicketCall) Context ¶
func (c *AccountsProvisionAccountTicketCall) Context(ctx context.Context) *AccountsProvisionAccountTicketCall

Context sets the context to be used in this call's Do method.

func (*AccountsProvisionAccountTicketCall) Do ¶
func (c *AccountsProvisionAccountTicketCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaProvisionAccountTicketResponse, error)

Do executes the "analyticsadmin.accounts.provisionAccountTicket" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaProvisionAccountTicketResponse.ServerResponse.Head er or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsProvisionAccountTicketCall) Fields ¶
func (c *AccountsProvisionAccountTicketCall) Fields(s ...googleapi.Field) *AccountsProvisionAccountTicketCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsProvisionAccountTicketCall) Header ¶
func (c *AccountsProvisionAccountTicketCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsRunAccessReportCall ¶
added in v0.112.0
type AccountsRunAccessReportCall struct {
	// contains filtered or unexported fields
}
func (*AccountsRunAccessReportCall) Context ¶
added in v0.112.0
func (c *AccountsRunAccessReportCall) Context(ctx context.Context) *AccountsRunAccessReportCall

Context sets the context to be used in this call's Do method.

func (*AccountsRunAccessReportCall) Do ¶
added in v0.112.0
func (c *AccountsRunAccessReportCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaRunAccessReportResponse, error)

Do executes the "analyticsadmin.accounts.runAccessReport" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaRunAccessReportResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsRunAccessReportCall) Fields ¶
added in v0.112.0
func (c *AccountsRunAccessReportCall) Fields(s ...googleapi.Field) *AccountsRunAccessReportCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsRunAccessReportCall) Header ¶
added in v0.112.0
func (c *AccountsRunAccessReportCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsSearchChangeHistoryEventsCall ¶
type AccountsSearchChangeHistoryEventsCall struct {
	// contains filtered or unexported fields
}
func (*AccountsSearchChangeHistoryEventsCall) Context ¶
func (c *AccountsSearchChangeHistoryEventsCall) Context(ctx context.Context) *AccountsSearchChangeHistoryEventsCall

Context sets the context to be used in this call's Do method.

func (*AccountsSearchChangeHistoryEventsCall) Do ¶
func (c *AccountsSearchChangeHistoryEventsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponse, error)

Do executes the "analyticsadmin.accounts.searchChangeHistoryEvents" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponse.ServerResponse.H eader or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsSearchChangeHistoryEventsCall) Fields ¶
func (c *AccountsSearchChangeHistoryEventsCall) Fields(s ...googleapi.Field) *AccountsSearchChangeHistoryEventsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsSearchChangeHistoryEventsCall) Header ¶
func (c *AccountsSearchChangeHistoryEventsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccountsSearchChangeHistoryEventsCall) Pages ¶
func (c *AccountsSearchChangeHistoryEventsCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsService ¶
type AccountsService struct {
	// contains filtered or unexported fields
}
func NewAccountsService ¶
func NewAccountsService(s *Service) *AccountsService
func (*AccountsService) Delete ¶
func (r *AccountsService) Delete(name string) *AccountsDeleteCall

Delete: Marks target Account as soft-deleted (ie: "trashed") and returns it. This API does not have a method to restore soft-deleted accounts. However, they can be restored using the Trash Can UI. If the accounts are not restored before the expiration time, the account and all child resources (eg: Properties, GoogleAdsLinks, Streams, AccessBindings) will be permanently purged. https://support.google.com/analytics/answer/6154772 Returns an error if the target is not found.

name: The name of the Account to soft-delete. Format: accounts/{account} Example: "accounts/100".
func (*AccountsService) Get ¶
func (r *AccountsService) Get(name string) *AccountsGetCall

Get: Lookup for a single Account.

name: The name of the account to lookup. Format: accounts/{account} Example: "accounts/100".
func (*AccountsService) GetDataSharingSettings ¶
func (r *AccountsService) GetDataSharingSettings(name string) *AccountsGetDataSharingSettingsCall

GetDataSharingSettings: Get data sharing settings on an account. Data sharing settings are singletons.

name: The name of the settings to lookup. Format: accounts/{account}/dataSharingSettings Example: `accounts/1000/dataSharingSettings`.
func (*AccountsService) List ¶
func (r *AccountsService) List() *AccountsListCall

List: Returns all accounts accessible by the caller. Note that these accounts might not currently have GA properties. Soft-deleted (ie: "trashed") accounts are excluded by default. Returns an empty list if no relevant accounts are found.

func (*AccountsService) Patch ¶
func (r *AccountsService) Patch(name string, googleanalyticsadminv1betaaccount *GoogleAnalyticsAdminV1betaAccount) *AccountsPatchCall

Patch: Updates an account.

name: Output only. Resource name of this account. Format: accounts/{account} Example: "accounts/100".
func (*AccountsService) ProvisionAccountTicket ¶
func (r *AccountsService) ProvisionAccountTicket(googleanalyticsadminv1betaprovisionaccountticketrequest *GoogleAnalyticsAdminV1betaProvisionAccountTicketRequest) *AccountsProvisionAccountTicketCall

ProvisionAccountTicket: Requests a ticket for creating an account.

func (*AccountsService) RunAccessReport ¶
added in v0.112.0
func (r *AccountsService) RunAccessReport(entity string, googleanalyticsadminv1betarunaccessreportrequest *GoogleAnalyticsAdminV1betaRunAccessReportRequest) *AccountsRunAccessReportCall

RunAccessReport: Returns a customized report of data access records. The report provides records of each time a user reads Google Analytics reporting data. Access records are retained for up to 2 years. Data Access Reports can be requested for a property. Reports may be requested for any property, but dimensions that aren't related to quota can only be requested on Google Analytics 360 properties. This method is only available to Administrators. These data access records include GA UI Reporting, GA UI Explorations, GA Data API, and other products like Firebase & Admob that can retrieve data from Google Analytics through a linkage. These records don't include property configuration changes like adding a stream or changing a property's time zone. For configuration change history, see searchChangeHistoryEvents (https://developers.google.com/analytics/devguides/config/admin/v1/rest/v1alpha/accounts/searchChangeHistoryEvents). To give your feedback on this API, complete the Google Analytics Access Reports feedback (https://docs.google.com/forms/d/e/1FAIpQLSdmEBUrMzAEdiEKk5TV5dEHvDUZDRlgWYdQdAeSdtR4hVjEhw/viewform) form.

entity: The Data Access Report supports requesting at the property level or account level. If requested at the account level, Data Access Reports include all access for all properties under that account. To request at the property level, entity should be for example 'properties/123' if "123" is your Google Analytics property ID. To request at the account level, entity should be for example 'accounts/1234' if "1234" is your Google Analytics Account ID.
func (*AccountsService) SearchChangeHistoryEvents ¶
func (r *AccountsService) SearchChangeHistoryEvents(account string, googleanalyticsadminv1betasearchchangehistoryeventsrequest *GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequest) *AccountsSearchChangeHistoryEventsCall

SearchChangeHistoryEvents: Searches through all changes to an account or its children given the specified set of filters. Only returns the subset of changes supported by the API. The UI may return additional changes.

account: The account resource for which to return change history resources. Format: accounts/{account} Example: `accounts/100`.
type GoogleAnalyticsAdminV1betaAccessBetweenFilter ¶
added in v0.112.0
type GoogleAnalyticsAdminV1betaAccessBetweenFilter struct {
	// FromValue: Begins with this number.
	FromValue *GoogleAnalyticsAdminV1betaNumericValue `json:"fromValue,omitempty"`
	// ToValue: Ends with this number.
	ToValue *GoogleAnalyticsAdminV1betaNumericValue `json:"toValue,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FromValue") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FromValue") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaAccessBetweenFilter: To express that the result needs to be between two numbers (inclusive).

func (GoogleAnalyticsAdminV1betaAccessBetweenFilter) MarshalJSON ¶
added in v0.112.0
func (s GoogleAnalyticsAdminV1betaAccessBetweenFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessDateRange ¶
added in v0.112.0
type GoogleAnalyticsAdminV1betaAccessDateRange struct {
	// EndDate: The inclusive end date for the query in the format `YYYY-MM-DD`.
	// Cannot be before `startDate`. The format `NdaysAgo`, `yesterday`, or `today`
	// is also accepted, and in that case, the date is inferred based on the
	// current time in the request's time zone.
	EndDate string `json:"endDate,omitempty"`
	// StartDate: The inclusive start date for the query in the format
	// `YYYY-MM-DD`. Cannot be after `endDate`. The format `NdaysAgo`, `yesterday`,
	// or `today` is also accepted, and in that case, the date is inferred based on
	// the current time in the request's time zone.
	StartDate string `json:"startDate,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EndDate") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EndDate") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaAccessDateRange: A contiguous range of days: startDate, startDate + 1, ..., endDate.

func (GoogleAnalyticsAdminV1betaAccessDateRange) MarshalJSON ¶
added in v0.112.0
func (s GoogleAnalyticsAdminV1betaAccessDateRange) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessDimension ¶
added in v0.112.0
type GoogleAnalyticsAdminV1betaAccessDimension struct {
	// DimensionName: The API name of the dimension. See Data Access Schema
	// (https://developers.google.com/analytics/devguides/config/admin/v1/access-api-schema)
	// for the list of dimensions supported in this API. Dimensions are referenced
	// by name in `dimensionFilter` and `orderBys`.
	DimensionName string `json:"dimensionName,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DimensionName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DimensionName") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaAccessDimension: Dimensions are attributes of your data. For example, the dimension `userEmail` indicates the email of the user that accessed reporting data. Dimension values in report responses are strings.

func (GoogleAnalyticsAdminV1betaAccessDimension) MarshalJSON ¶
added in v0.112.0
func (s GoogleAnalyticsAdminV1betaAccessDimension) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessDimensionHeader ¶
added in v0.112.0
type GoogleAnalyticsAdminV1betaAccessDimensionHeader struct {
	// DimensionName: The dimension's name; for example 'userEmail'.
	DimensionName string `json:"dimensionName,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DimensionName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DimensionName") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaAccessDimensionHeader: Describes a dimension column in the report. Dimensions requested in a report produce column entries within rows and DimensionHeaders. However, dimensions used exclusively within filters or expressions do not produce columns in a report; correspondingly, those dimensions do not produce headers.

func (GoogleAnalyticsAdminV1betaAccessDimensionHeader) MarshalJSON ¶
added in v0.112.0
func (s GoogleAnalyticsAdminV1betaAccessDimensionHeader) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessDimensionValue ¶
added in v0.112.0
type GoogleAnalyticsAdminV1betaAccessDimensionValue struct {
	// Value: The dimension value. For example, this value may be 'France' for the
	// 'country' dimension.
	Value string `json:"value,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Value") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Value") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaAccessDimensionValue: The value of a dimension.

func (GoogleAnalyticsAdminV1betaAccessDimensionValue) MarshalJSON ¶
added in v0.112.0
func (s GoogleAnalyticsAdminV1betaAccessDimensionValue) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessFilter ¶
added in v0.112.0
type GoogleAnalyticsAdminV1betaAccessFilter struct {
	// BetweenFilter: A filter for two values.
	BetweenFilter *GoogleAnalyticsAdminV1betaAccessBetweenFilter `json:"betweenFilter,omitempty"`
	// FieldName: The dimension name or metric name.
	FieldName string `json:"fieldName,omitempty"`
	// InListFilter: A filter for in list values.
	InListFilter *GoogleAnalyticsAdminV1betaAccessInListFilter `json:"inListFilter,omitempty"`
	// NumericFilter: A filter for numeric or date values.
	NumericFilter *GoogleAnalyticsAdminV1betaAccessNumericFilter `json:"numericFilter,omitempty"`
	// StringFilter: Strings related filter.
	StringFilter *GoogleAnalyticsAdminV1betaAccessStringFilter `json:"stringFilter,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BetweenFilter") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BetweenFilter") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaAccessFilter: An expression to filter dimension or metric values.

func (GoogleAnalyticsAdminV1betaAccessFilter) MarshalJSON ¶
added in v0.112.0
func (s GoogleAnalyticsAdminV1betaAccessFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessFilterExpression ¶
added in v0.112.0
type GoogleAnalyticsAdminV1betaAccessFilterExpression struct {
	// AccessFilter: A primitive filter. In the same FilterExpression, all of the
	// filter's field names need to be either all dimensions or all metrics.
	AccessFilter *GoogleAnalyticsAdminV1betaAccessFilter `json:"accessFilter,omitempty"`
	// AndGroup: Each of the FilterExpressions in the and_group has an AND
	// relationship.
	AndGroup *GoogleAnalyticsAdminV1betaAccessFilterExpressionList `json:"andGroup,omitempty"`
	// NotExpression: The FilterExpression is NOT of not_expression.
	NotExpression *GoogleAnalyticsAdminV1betaAccessFilterExpression `json:"notExpression,omitempty"`
	// OrGroup: Each of the FilterExpressions in the or_group has an OR
	// relationship.
	OrGroup *GoogleAnalyticsAdminV1betaAccessFilterExpressionList `json:"orGroup,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AccessFilter") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccessFilter") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaAccessFilterExpression: Expresses dimension or metric filters. The fields in the same expression need to be either all dimensions or all metrics.

func (GoogleAnalyticsAdminV1betaAccessFilterExpression) MarshalJSON ¶
added in v0.112.0
func (s GoogleAnalyticsAdminV1betaAccessFilterExpression) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessFilterExpressionList ¶
added in v0.112.0
type GoogleAnalyticsAdminV1betaAccessFilterExpressionList struct {
	// Expressions: A list of filter expressions.
	Expressions []*GoogleAnalyticsAdminV1betaAccessFilterExpression `json:"expressions,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Expressions") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Expressions") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaAccessFilterExpressionList: A list of filter expressions.

func (GoogleAnalyticsAdminV1betaAccessFilterExpressionList) MarshalJSON ¶
added in v0.112.0
func (s GoogleAnalyticsAdminV1betaAccessFilterExpressionList) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessInListFilter ¶
added in v0.112.0
type GoogleAnalyticsAdminV1betaAccessInListFilter struct {
	// CaseSensitive: If true, the string value is case sensitive.
	CaseSensitive bool `json:"caseSensitive,omitempty"`
	// Values: The list of string values. Must be non-empty.
	Values []string `json:"values,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CaseSensitive") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CaseSensitive") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaAccessInListFilter: The result needs to be in a list of string values.

func (GoogleAnalyticsAdminV1betaAccessInListFilter) MarshalJSON ¶
added in v0.112.0
func (s GoogleAnalyticsAdminV1betaAccessInListFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessMetric ¶
added in v0.112.0
type GoogleAnalyticsAdminV1betaAccessMetric struct {
	// MetricName: The API name of the metric. See Data Access Schema
	// (https://developers.google.com/analytics/devguides/config/admin/v1/access-api-schema)
	// for the list of metrics supported in this API. Metrics are referenced by
	// name in `metricFilter` & `orderBys`.
	MetricName string `json:"metricName,omitempty"`
	// ForceSendFields is a list of field names (e.g. "MetricName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "MetricName") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaAccessMetric: The quantitative measurements of a report. For example, the metric `accessCount` is the total number of data access records.

func (GoogleAnalyticsAdminV1betaAccessMetric) MarshalJSON ¶
added in v0.112.0
func (s GoogleAnalyticsAdminV1betaAccessMetric) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessMetricHeader ¶
added in v0.112.0
type GoogleAnalyticsAdminV1betaAccessMetricHeader struct {
	// MetricName: The metric's name; for example 'accessCount'.
	MetricName string `json:"metricName,omitempty"`
	// ForceSendFields is a list of field names (e.g. "MetricName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "MetricName") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaAccessMetricHeader: Describes a metric column in the report. Visible metrics requested in a report produce column entries within rows and MetricHeaders. However, metrics used exclusively within filters or expressions do not produce columns in a report; correspondingly, those metrics do not produce headers.

func (GoogleAnalyticsAdminV1betaAccessMetricHeader) MarshalJSON ¶
added in v0.112.0
func (s GoogleAnalyticsAdminV1betaAccessMetricHeader) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessMetricValue ¶
added in v0.112.0
type GoogleAnalyticsAdminV1betaAccessMetricValue struct {
	// Value: The measurement value. For example, this value may be '13'.
	Value string `json:"value,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Value") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Value") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaAccessMetricValue: The value of a metric.

func (GoogleAnalyticsAdminV1betaAccessMetricValue) MarshalJSON ¶
added in v0.112.0
func (s GoogleAnalyticsAdminV1betaAccessMetricValue) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessNumericFilter ¶
added in v0.112.0
type GoogleAnalyticsAdminV1betaAccessNumericFilter struct {
	// Operation: The operation type for this filter.
	//
	// Possible values:
	//   "OPERATION_UNSPECIFIED" - Unspecified.
	//   "EQUAL" - Equal
	//   "LESS_THAN" - Less than
	//   "LESS_THAN_OR_EQUAL" - Less than or equal
	//   "GREATER_THAN" - Greater than
	//   "GREATER_THAN_OR_EQUAL" - Greater than or equal
	Operation string `json:"operation,omitempty"`
	// Value: A numeric value or a date value.
	Value *GoogleAnalyticsAdminV1betaNumericValue `json:"value,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Operation") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Operation") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaAccessNumericFilter: Filters for numeric or date values.

func (GoogleAnalyticsAdminV1betaAccessNumericFilter) MarshalJSON ¶
added in v0.112.0
func (s GoogleAnalyticsAdminV1betaAccessNumericFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessOrderBy ¶
added in v0.112.0
type GoogleAnalyticsAdminV1betaAccessOrderBy struct {
	// Desc: If true, sorts by descending order. If false or unspecified, sorts in
	// ascending order.
	Desc bool `json:"desc,omitempty"`
	// Dimension: Sorts results by a dimension's values.
	Dimension *GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderBy `json:"dimension,omitempty"`
	// Metric: Sorts results by a metric's values.
	Metric *GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderBy `json:"metric,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Desc") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Desc") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaAccessOrderBy: Order bys define how rows will be sorted in the response. For example, ordering rows by descending access count is one ordering, and ordering rows by the country string is a different ordering.

func (GoogleAnalyticsAdminV1betaAccessOrderBy) MarshalJSON ¶
added in v0.112.0
func (s GoogleAnalyticsAdminV1betaAccessOrderBy) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderBy ¶
added in v0.112.0
type GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderBy struct {
	// DimensionName: A dimension name in the request to order by.
	DimensionName string `json:"dimensionName,omitempty"`
	// OrderType: Controls the rule for dimension value ordering.
	//
	// Possible values:
	//   "ORDER_TYPE_UNSPECIFIED" - Unspecified.
	//   "ALPHANUMERIC" - Alphanumeric sort by Unicode code point. For example, "2"
	// < "A" < "X" < "b" < "z".
	//   "CASE_INSENSITIVE_ALPHANUMERIC" - Case insensitive alphanumeric sort by
	// lower case Unicode code point. For example, "2" < "A" < "b" < "X" < "z".
	//   "NUMERIC" - Dimension values are converted to numbers before sorting. For
	// example in NUMERIC sort, "25" < "100", and in `ALPHANUMERIC` sort, "100" <
	// "25". Non-numeric dimension values all have equal ordering value below all
	// numeric values.
	OrderType string `json:"orderType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DimensionName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DimensionName") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderBy: Sorts by dimension values.

func (GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderBy) MarshalJSON ¶
added in v0.112.0
func (s GoogleAnalyticsAdminV1betaAccessOrderByDimensionOrderBy) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderBy ¶
added in v0.112.0
type GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderBy struct {
	// MetricName: A metric name in the request to order by.
	MetricName string `json:"metricName,omitempty"`
	// ForceSendFields is a list of field names (e.g. "MetricName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "MetricName") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderBy: Sorts by metric values.

func (GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderBy) MarshalJSON ¶
added in v0.112.0
func (s GoogleAnalyticsAdminV1betaAccessOrderByMetricOrderBy) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessQuota ¶
added in v0.112.0
type GoogleAnalyticsAdminV1betaAccessQuota struct {
	// ConcurrentRequests: Properties can use up to 50 concurrent requests.
	ConcurrentRequests *GoogleAnalyticsAdminV1betaAccessQuotaStatus `json:"concurrentRequests,omitempty"`
	// ServerErrorsPerProjectPerHour: Properties and cloud project pairs can have
	// up to 50 server errors per hour.
	ServerErrorsPerProjectPerHour *GoogleAnalyticsAdminV1betaAccessQuotaStatus `json:"serverErrorsPerProjectPerHour,omitempty"`
	// TokensPerDay: Properties can use 250,000 tokens per day. Most requests
	// consume fewer than 10 tokens.
	TokensPerDay *GoogleAnalyticsAdminV1betaAccessQuotaStatus `json:"tokensPerDay,omitempty"`
	// TokensPerHour: Properties can use 50,000 tokens per hour. An API request
	// consumes a single number of tokens, and that number is deducted from all of
	// the hourly, daily, and per project hourly quotas.
	TokensPerHour *GoogleAnalyticsAdminV1betaAccessQuotaStatus `json:"tokensPerHour,omitempty"`
	// TokensPerProjectPerHour: Properties can use up to 25% of their tokens per
	// project per hour. This amounts to Analytics 360 Properties can use 12,500
	// tokens per project per hour. An API request consumes a single number of
	// tokens, and that number is deducted from all of the hourly, daily, and per
	// project hourly quotas.
	TokensPerProjectPerHour *GoogleAnalyticsAdminV1betaAccessQuotaStatus `json:"tokensPerProjectPerHour,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ConcurrentRequests") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ConcurrentRequests") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaAccessQuota: Current state of all quotas for this Analytics property. If any quota for a property is exhausted, all requests to that property will return Resource Exhausted errors.

func (GoogleAnalyticsAdminV1betaAccessQuota) MarshalJSON ¶
added in v0.112.0
func (s GoogleAnalyticsAdminV1betaAccessQuota) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessQuotaStatus ¶
added in v0.112.0
type GoogleAnalyticsAdminV1betaAccessQuotaStatus struct {
	// Consumed: Quota consumed by this request.
	Consumed int64 `json:"consumed,omitempty"`
	// Remaining: Quota remaining after this request.
	Remaining int64 `json:"remaining,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Consumed") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Consumed") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaAccessQuotaStatus: Current state for a particular quota group.

func (GoogleAnalyticsAdminV1betaAccessQuotaStatus) MarshalJSON ¶
added in v0.112.0
func (s GoogleAnalyticsAdminV1betaAccessQuotaStatus) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessRow ¶
added in v0.112.0
type GoogleAnalyticsAdminV1betaAccessRow struct {
	// DimensionValues: List of dimension values. These values are in the same
	// order as specified in the request.
	DimensionValues []*GoogleAnalyticsAdminV1betaAccessDimensionValue `json:"dimensionValues,omitempty"`
	// MetricValues: List of metric values. These values are in the same order as
	// specified in the request.
	MetricValues []*GoogleAnalyticsAdminV1betaAccessMetricValue `json:"metricValues,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DimensionValues") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DimensionValues") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaAccessRow: Access report data for each row.

func (GoogleAnalyticsAdminV1betaAccessRow) MarshalJSON ¶
added in v0.112.0
func (s GoogleAnalyticsAdminV1betaAccessRow) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccessStringFilter ¶
added in v0.112.0
type GoogleAnalyticsAdminV1betaAccessStringFilter struct {
	// CaseSensitive: If true, the string value is case sensitive.
	CaseSensitive bool `json:"caseSensitive,omitempty"`
	// MatchType: The match type for this filter.
	//
	// Possible values:
	//   "MATCH_TYPE_UNSPECIFIED" - Unspecified
	//   "EXACT" - Exact match of the string value.
	//   "BEGINS_WITH" - Begins with the string value.
	//   "ENDS_WITH" - Ends with the string value.
	//   "CONTAINS" - Contains the string value.
	//   "FULL_REGEXP" - Full match for the regular expression with the string
	// value.
	//   "PARTIAL_REGEXP" - Partial match for the regular expression with the
	// string value.
	MatchType string `json:"matchType,omitempty"`
	// Value: The string value used for the matching.
	Value string `json:"value,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CaseSensitive") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CaseSensitive") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaAccessStringFilter: The filter for strings.

func (GoogleAnalyticsAdminV1betaAccessStringFilter) MarshalJSON ¶
added in v0.112.0
func (s GoogleAnalyticsAdminV1betaAccessStringFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccount ¶
type GoogleAnalyticsAdminV1betaAccount struct {
	// CreateTime: Output only. Time when this account was originally created.
	CreateTime string `json:"createTime,omitempty"`
	// Deleted: Output only. Indicates whether this Account is soft-deleted or not.
	// Deleted accounts are excluded from List results unless specifically
	// requested.
	Deleted bool `json:"deleted,omitempty"`
	// DisplayName: Required. Human-readable display name for this account.
	DisplayName string `json:"displayName,omitempty"`
	// GmpOrganization: Output only. The URI for a Google Marketing Platform
	// organization resource. Only set when this account is connected to a GMP
	// organization. Format:
	// marketingplatformadmin.googleapis.com/organizations/{org_id}
	GmpOrganization string `json:"gmpOrganization,omitempty"`
	// Name: Output only. Resource name of this account. Format: accounts/{account}
	// Example: "accounts/100"
	Name string `json:"name,omitempty"`
	// RegionCode: Country of business. Must be a Unicode CLDR region code.
	RegionCode string `json:"regionCode,omitempty"`
	// UpdateTime: Output only. Time when account payload fields were last updated.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "CreateTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CreateTime") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaAccount: A resource message representing a Google Analytics account.

func (GoogleAnalyticsAdminV1betaAccount) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaAccount) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAccountSummary ¶
type GoogleAnalyticsAdminV1betaAccountSummary struct {
	// Account: Resource name of account referred to by this account summary
	// Format: accounts/{account_id} Example: "accounts/1000"
	Account string `json:"account,omitempty"`
	// DisplayName: Display name for the account referred to in this account
	// summary.
	DisplayName string `json:"displayName,omitempty"`
	// Name: Resource name for this account summary. Format:
	// accountSummaries/{account_id} Example: "accountSummaries/1000"
	Name string `json:"name,omitempty"`
	// PropertySummaries: List of summaries for child accounts of this account.
	PropertySummaries []*GoogleAnalyticsAdminV1betaPropertySummary `json:"propertySummaries,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Account") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Account") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaAccountSummary: A virtual resource representing an overview of an account and all its child Google Analytics properties.

func (GoogleAnalyticsAdminV1betaAccountSummary) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaAccountSummary) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionRequest ¶
type GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionRequest struct {
	// Acknowledgement: Required. An acknowledgement that the caller of this method
	// understands the terms of user data collection. This field must contain the
	// exact value: "I acknowledge that I have the necessary privacy disclosures
	// and rights from my end users for the collection and processing of their
	// data, including the association of such data with the visitation information
	// Google Analytics collects from my site and/or app property."
	Acknowledgement string `json:"acknowledgement,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Acknowledgement") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Acknowledgement") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionRequest: Request message for AcknowledgeUserDataCollection RPC.

func (GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionRequest) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionResponse ¶
type GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionResponse struct {
	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
}

GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionResponse: Response message for AcknowledgeUserDataCollection RPC.

type GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequest ¶
type GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequest struct {
}

GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequest: Request message for ArchiveCustomDimension RPC.

type GoogleAnalyticsAdminV1betaArchiveCustomMetricRequest ¶
type GoogleAnalyticsAdminV1betaArchiveCustomMetricRequest struct {
}

GoogleAnalyticsAdminV1betaArchiveCustomMetricRequest: Request message for ArchiveCustomMetric RPC.

type GoogleAnalyticsAdminV1betaChangeHistoryChange ¶
type GoogleAnalyticsAdminV1betaChangeHistoryChange struct {
	// Action: The type of action that changed this resource.
	//
	// Possible values:
	//   "ACTION_TYPE_UNSPECIFIED" - Action type unknown or not specified.
	//   "CREATED" - Resource was created in this change.
	//   "UPDATED" - Resource was updated in this change.
	//   "DELETED" - Resource was deleted in this change.
	Action string `json:"action,omitempty"`
	// Resource: Resource name of the resource whose changes are described by this
	// entry.
	Resource string `json:"resource,omitempty"`
	// ResourceAfterChange: Resource contents from after the change was made. If
	// this resource was deleted in this change, this field will be missing.
	ResourceAfterChange *GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResource `json:"resourceAfterChange,omitempty"`
	// ResourceBeforeChange: Resource contents from before the change was made. If
	// this resource was created in this change, this field will be missing.
	ResourceBeforeChange *GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResource `json:"resourceBeforeChange,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Action") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Action") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaChangeHistoryChange: A description of a change to a single Google Analytics resource.

func (GoogleAnalyticsAdminV1betaChangeHistoryChange) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaChangeHistoryChange) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResource ¶
type GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResource struct {
	// Account: A snapshot of an Account resource in change history.
	Account *GoogleAnalyticsAdminV1betaAccount `json:"account,omitempty"`
	// ConversionEvent: A snapshot of a ConversionEvent resource in change history.
	ConversionEvent *GoogleAnalyticsAdminV1betaConversionEvent `json:"conversionEvent,omitempty"`
	// DataRetentionSettings: A snapshot of a data retention settings resource in
	// change history.
	DataRetentionSettings *GoogleAnalyticsAdminV1betaDataRetentionSettings `json:"dataRetentionSettings,omitempty"`
	// DataStream: A snapshot of a DataStream resource in change history.
	DataStream *GoogleAnalyticsAdminV1betaDataStream `json:"dataStream,omitempty"`
	// FirebaseLink: A snapshot of a FirebaseLink resource in change history.
	FirebaseLink *GoogleAnalyticsAdminV1betaFirebaseLink `json:"firebaseLink,omitempty"`
	// GoogleAdsLink: A snapshot of a GoogleAdsLink resource in change history.
	GoogleAdsLink *GoogleAnalyticsAdminV1betaGoogleAdsLink `json:"googleAdsLink,omitempty"`
	// MeasurementProtocolSecret: A snapshot of a MeasurementProtocolSecret
	// resource in change history.
	MeasurementProtocolSecret *GoogleAnalyticsAdminV1betaMeasurementProtocolSecret `json:"measurementProtocolSecret,omitempty"`
	// Property: A snapshot of a Property resource in change history.
	Property *GoogleAnalyticsAdminV1betaProperty `json:"property,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Account") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Account") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResource: A snapshot of a resource as before or after the result of a change in change history.

func (GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResource) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaChangeHistoryChangeChangeHistoryResource) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaChangeHistoryEvent ¶
type GoogleAnalyticsAdminV1betaChangeHistoryEvent struct {
	// ActorType: The type of actor that made this change.
	//
	// Possible values:
	//   "ACTOR_TYPE_UNSPECIFIED" - Unknown or unspecified actor type.
	//   "USER" - Changes made by the user specified in actor_email.
	//   "SYSTEM" - Changes made by the Google Analytics system.
	//   "SUPPORT" - Changes made by Google Analytics support team staff.
	ActorType string `json:"actorType,omitempty"`
	// ChangeTime: Time when change was made.
	ChangeTime string `json:"changeTime,omitempty"`
	// Changes: A list of changes made in this change history event that fit the
	// filters specified in SearchChangeHistoryEventsRequest.
	Changes []*GoogleAnalyticsAdminV1betaChangeHistoryChange `json:"changes,omitempty"`
	// ChangesFiltered: If true, then the list of changes returned was filtered,
	// and does not represent all changes that occurred in this event.
	ChangesFiltered bool `json:"changesFiltered,omitempty"`
	// Id: ID of this change history event. This ID is unique across Google
	// Analytics.
	Id string `json:"id,omitempty"`
	// UserActorEmail: Email address of the Google account that made the change.
	// This will be a valid email address if the actor field is set to USER, and
	// empty otherwise. Google accounts that have been deleted will cause an error.
	UserActorEmail string `json:"userActorEmail,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ActorType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ActorType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaChangeHistoryEvent: A set of changes within a Google Analytics account or its child properties that resulted from the same cause. Common causes would be updates made in the Google Analytics UI, changes from customer support, or automatic Google Analytics system changes.

func (GoogleAnalyticsAdminV1betaChangeHistoryEvent) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaChangeHistoryEvent) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaConversionEvent ¶
type GoogleAnalyticsAdminV1betaConversionEvent struct {
	// CountingMethod: Optional. The method by which conversions will be counted
	// across multiple events within a session. If this value is not provided, it
	// will be set to `ONCE_PER_EVENT`.
	//
	// Possible values:
	//   "CONVERSION_COUNTING_METHOD_UNSPECIFIED" - Counting method not specified.
	//   "ONCE_PER_EVENT" - Each Event instance is considered a Conversion.
	//   "ONCE_PER_SESSION" - An Event instance is considered a Conversion at most
	// once per session per user.
	CountingMethod string `json:"countingMethod,omitempty"`
	// CreateTime: Output only. Time when this conversion event was created in the
	// property.
	CreateTime string `json:"createTime,omitempty"`
	// Custom: Output only. If set to true, this conversion event refers to a
	// custom event. If set to false, this conversion event refers to a default
	// event in GA. Default events typically have special meaning in GA. Default
	// events are usually created for you by the GA system, but in some cases can
	// be created by property admins. Custom events count towards the maximum
	// number of custom conversion events that may be created per property.
	Custom bool `json:"custom,omitempty"`
	// DefaultConversionValue: Optional. Defines a default value/currency for a
	// conversion event.
	DefaultConversionValue *GoogleAnalyticsAdminV1betaConversionEventDefaultConversionValue `json:"defaultConversionValue,omitempty"`
	// Deletable: Output only. If set, this event can currently be deleted with
	// DeleteConversionEvent.
	Deletable bool `json:"deletable,omitempty"`
	// EventName: Immutable. The event name for this conversion event. Examples:
	// 'click', 'purchase'
	EventName string `json:"eventName,omitempty"`
	// Name: Output only. Resource name of this conversion event. Format:
	// properties/{property}/conversionEvents/{conversion_event}
	Name string `json:"name,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "CountingMethod") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CountingMethod") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaConversionEvent: A conversion event in a Google Analytics property.

func (GoogleAnalyticsAdminV1betaConversionEvent) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaConversionEvent) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaConversionEventDefaultConversionValue ¶
added in v0.149.0
type GoogleAnalyticsAdminV1betaConversionEventDefaultConversionValue struct {
	// CurrencyCode: When a conversion event for this event_name has no set
	// currency, this currency will be applied as the default. Must be in ISO 4217
	// currency code format. See https://en.wikipedia.org/wiki/ISO_4217 for more
	// information.
	CurrencyCode string `json:"currencyCode,omitempty"`
	// Value: This value will be used to populate the value for all conversions of
	// the specified event_name where the event "value" parameter is unset.
	Value float64 `json:"value,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CurrencyCode") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CurrencyCode") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaConversionEventDefaultConversionValue: Defines a default value/currency for a conversion event. Both value and currency must be provided.

func (GoogleAnalyticsAdminV1betaConversionEventDefaultConversionValue) MarshalJSON ¶
added in v0.149.0
func (s GoogleAnalyticsAdminV1betaConversionEventDefaultConversionValue) MarshalJSON() ([]byte, error)
func (*GoogleAnalyticsAdminV1betaConversionEventDefaultConversionValue) UnmarshalJSON ¶
added in v0.149.0
func (s *GoogleAnalyticsAdminV1betaConversionEventDefaultConversionValue) UnmarshalJSON(data []byte) error
type GoogleAnalyticsAdminV1betaCustomDimension ¶
type GoogleAnalyticsAdminV1betaCustomDimension struct {
	// Description: Optional. Description for this custom dimension. Max length of
	// 150 characters.
	Description string `json:"description,omitempty"`
	// DisallowAdsPersonalization: Optional. If set to true, sets this dimension as
	// NPA and excludes it from ads personalization. This is currently only
	// supported by user-scoped custom dimensions.
	DisallowAdsPersonalization bool `json:"disallowAdsPersonalization,omitempty"`
	// DisplayName: Required. Display name for this custom dimension as shown in
	// the Analytics UI. Max length of 82 characters, alphanumeric plus space and
	// underscore starting with a letter. Legacy system-generated display names may
	// contain square brackets, but updates to this field will never permit square
	// brackets.
	DisplayName string `json:"displayName,omitempty"`
	// Name: Output only. Resource name for this CustomDimension resource. Format:
	// properties/{property}/customDimensions/{customDimension}
	Name string `json:"name,omitempty"`
	// ParameterName: Required. Immutable. Tagging parameter name for this custom
	// dimension. If this is a user-scoped dimension, then this is the user
	// property name. If this is an event-scoped dimension, then this is the event
	// parameter name. If this is an item-scoped dimension, then this is the
	// parameter name found in the eCommerce items array. May only contain
	// alphanumeric and underscore characters, starting with a letter. Max length
	// of 24 characters for user-scoped dimensions, 40 characters for event-scoped
	// dimensions.
	ParameterName string `json:"parameterName,omitempty"`
	// Scope: Required. Immutable. The scope of this dimension.
	//
	// Possible values:
	//   "DIMENSION_SCOPE_UNSPECIFIED" - Scope unknown or not specified.
	//   "EVENT" - Dimension scoped to an event.
	//   "USER" - Dimension scoped to a user.
	//   "ITEM" - Dimension scoped to eCommerce items
	Scope string `json:"scope,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Description") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Description") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaCustomDimension: A definition for a CustomDimension.

func (GoogleAnalyticsAdminV1betaCustomDimension) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaCustomDimension) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaCustomMetric ¶
type GoogleAnalyticsAdminV1betaCustomMetric struct {
	// Description: Optional. Description for this custom dimension. Max length of
	// 150 characters.
	Description string `json:"description,omitempty"`
	// DisplayName: Required. Display name for this custom metric as shown in the
	// Analytics UI. Max length of 82 characters, alphanumeric plus space and
	// underscore starting with a letter. Legacy system-generated display names may
	// contain square brackets, but updates to this field will never permit square
	// brackets.
	DisplayName string `json:"displayName,omitempty"`
	// MeasurementUnit: Required. The type for the custom metric's value.
	//
	// Possible values:
	//   "MEASUREMENT_UNIT_UNSPECIFIED" - MeasurementUnit unspecified or missing.
	//   "STANDARD" - This metric uses default units.
	//   "CURRENCY" - This metric measures a currency.
	//   "FEET" - This metric measures feet.
	//   "METERS" - This metric measures meters.
	//   "KILOMETERS" - This metric measures kilometers.
	//   "MILES" - This metric measures miles.
	//   "MILLISECONDS" - This metric measures milliseconds.
	//   "SECONDS" - This metric measures seconds.
	//   "MINUTES" - This metric measures minutes.
	//   "HOURS" - This metric measures hours.
	MeasurementUnit string `json:"measurementUnit,omitempty"`
	// Name: Output only. Resource name for this CustomMetric resource. Format:
	// properties/{property}/customMetrics/{customMetric}
	Name string `json:"name,omitempty"`
	// ParameterName: Required. Immutable. Tagging name for this custom metric. If
	// this is an event-scoped metric, then this is the event parameter name. May
	// only contain alphanumeric and underscore charactes, starting with a letter.
	// Max length of 40 characters for event-scoped metrics.
	ParameterName string `json:"parameterName,omitempty"`
	// RestrictedMetricType: Optional. Types of restricted data that this metric
	// may contain. Required for metrics with CURRENCY measurement unit. Must be
	// empty for metrics with a non-CURRENCY measurement unit.
	//
	// Possible values:
	//   "RESTRICTED_METRIC_TYPE_UNSPECIFIED" - Type unknown or unspecified.
	//   "COST_DATA" - Metric reports cost data.
	//   "REVENUE_DATA" - Metric reports revenue data.
	RestrictedMetricType []string `json:"restrictedMetricType,omitempty"`
	// Scope: Required. Immutable. The scope of this custom metric.
	//
	// Possible values:
	//   "METRIC_SCOPE_UNSPECIFIED" - Scope unknown or not specified.
	//   "EVENT" - Metric scoped to an event.
	Scope string `json:"scope,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Description") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Description") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaCustomMetric: A definition for a custom metric.

func (GoogleAnalyticsAdminV1betaCustomMetric) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaCustomMetric) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaDataRetentionSettings ¶
type GoogleAnalyticsAdminV1betaDataRetentionSettings struct {
	// EventDataRetention: Required. The length of time that event-level data is
	// retained.
	//
	// Possible values:
	//   "RETENTION_DURATION_UNSPECIFIED" - Data retention time duration is not
	// specified.
	//   "TWO_MONTHS" - The data retention time duration is 2 months.
	//   "FOURTEEN_MONTHS" - The data retention time duration is 14 months.
	//   "TWENTY_SIX_MONTHS" - The data retention time duration is 26 months.
	// Available to 360 properties only. Available for event data only.
	//   "THIRTY_EIGHT_MONTHS" - The data retention time duration is 38 months.
	// Available to 360 properties only. Available for event data only.
	//   "FIFTY_MONTHS" - The data retention time duration is 50 months. Available
	// to 360 properties only. Available for event data only.
	EventDataRetention string `json:"eventDataRetention,omitempty"`
	// Name: Output only. Resource name for this DataRetentionSetting resource.
	// Format: properties/{property}/dataRetentionSettings
	Name string `json:"name,omitempty"`
	// ResetUserDataOnNewActivity: If true, reset the retention period for the user
	// identifier with every event from that user.
	ResetUserDataOnNewActivity bool `json:"resetUserDataOnNewActivity,omitempty"`
	// UserDataRetention: Required. The length of time that user-level data is
	// retained.
	//
	// Possible values:
	//   "RETENTION_DURATION_UNSPECIFIED" - Data retention time duration is not
	// specified.
	//   "TWO_MONTHS" - The data retention time duration is 2 months.
	//   "FOURTEEN_MONTHS" - The data retention time duration is 14 months.
	//   "TWENTY_SIX_MONTHS" - The data retention time duration is 26 months.
	// Available to 360 properties only. Available for event data only.
	//   "THIRTY_EIGHT_MONTHS" - The data retention time duration is 38 months.
	// Available to 360 properties only. Available for event data only.
	//   "FIFTY_MONTHS" - The data retention time duration is 50 months. Available
	// to 360 properties only. Available for event data only.
	UserDataRetention string `json:"userDataRetention,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "EventDataRetention") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EventDataRetention") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaDataRetentionSettings: Settings values for data retention. This is a singleton resource.

func (GoogleAnalyticsAdminV1betaDataRetentionSettings) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaDataRetentionSettings) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaDataSharingSettings ¶
type GoogleAnalyticsAdminV1betaDataSharingSettings struct {
	// Name: Output only. Resource name. Format:
	// accounts/{account}/dataSharingSettings Example:
	// "accounts/1000/dataSharingSettings"
	Name string `json:"name,omitempty"`
	// SharingWithGoogleAnySalesEnabled: Deprecated. This field is no longer used
	// and always returns false.
	SharingWithGoogleAnySalesEnabled bool `json:"sharingWithGoogleAnySalesEnabled,omitempty"`
	// SharingWithGoogleAssignedSalesEnabled: Allows Google access to your Google
	// Analytics account data, including account usage and configuration data,
	// product spending, and users associated with your Google Analytics account,
	// so that Google can help you make the most of Google products, providing you
	// with insights, offers, recommendations, and optimization tips across Google
	// Analytics and other Google products for business. This field maps to the
	// "Recommendations for your business" field in the Google Analytics Admin UI.
	SharingWithGoogleAssignedSalesEnabled bool `json:"sharingWithGoogleAssignedSalesEnabled,omitempty"`
	// SharingWithGoogleProductsEnabled: Allows Google to use the data to improve
	// other Google products or services. This fields maps to the "Google products
	// & services" field in the Google Analytics Admin UI.
	SharingWithGoogleProductsEnabled bool `json:"sharingWithGoogleProductsEnabled,omitempty"`
	// SharingWithGoogleSupportEnabled: Allows Google technical support
	// representatives access to your Google Analytics data and account when
	// necessary to provide service and find solutions to technical issues. This
	// field maps to the "Technical support" field in the Google Analytics Admin
	// UI.
	SharingWithGoogleSupportEnabled bool `json:"sharingWithGoogleSupportEnabled,omitempty"`
	// SharingWithOthersEnabled: Enable features like predictions, modeled data,
	// and benchmarking that can provide you with richer business insights when you
	// contribute aggregated measurement data. The data you share (including
	// information about the property from which it is shared) is aggregated and
	// de-identified before being used to generate business insights. This field
	// maps to the "Modeling contributions & business insights" field in the Google
	// Analytics Admin UI.
	SharingWithOthersEnabled bool `json:"sharingWithOthersEnabled,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Name") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Name") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaDataSharingSettings: A resource message representing data sharing settings of a Google Analytics account.

func (GoogleAnalyticsAdminV1betaDataSharingSettings) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaDataSharingSettings) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaDataStream ¶
type GoogleAnalyticsAdminV1betaDataStream struct {
	// AndroidAppStreamData: Data specific to Android app streams. Must be
	// populated if type is ANDROID_APP_DATA_STREAM.
	AndroidAppStreamData *GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamData `json:"androidAppStreamData,omitempty"`
	// CreateTime: Output only. Time when this stream was originally created.
	CreateTime string `json:"createTime,omitempty"`
	// DisplayName: Human-readable display name for the Data Stream. Required for
	// web data streams. The max allowed display name length is 255 UTF-16 code
	// units.
	DisplayName string `json:"displayName,omitempty"`
	// IosAppStreamData: Data specific to iOS app streams. Must be populated if
	// type is IOS_APP_DATA_STREAM.
	IosAppStreamData *GoogleAnalyticsAdminV1betaDataStreamIosAppStreamData `json:"iosAppStreamData,omitempty"`
	// Name: Output only. Resource name of this Data Stream. Format:
	// properties/{property_id}/dataStreams/{stream_id} Example:
	// "properties/1000/dataStreams/2000"
	Name string `json:"name,omitempty"`
	// Type: Required. Immutable. The type of this DataStream resource.
	//
	// Possible values:
	//   "DATA_STREAM_TYPE_UNSPECIFIED" - Type unknown or not specified.
	//   "WEB_DATA_STREAM" - Web data stream.
	//   "ANDROID_APP_DATA_STREAM" - Android app data stream.
	//   "IOS_APP_DATA_STREAM" - iOS app data stream.
	Type string `json:"type,omitempty"`
	// UpdateTime: Output only. Time when stream payload fields were last updated.
	UpdateTime string `json:"updateTime,omitempty"`
	// WebStreamData: Data specific to web streams. Must be populated if type is
	// WEB_DATA_STREAM.
	WebStreamData *GoogleAnalyticsAdminV1betaDataStreamWebStreamData `json:"webStreamData,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AndroidAppStreamData") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AndroidAppStreamData") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaDataStream: A resource message representing a data stream.

func (GoogleAnalyticsAdminV1betaDataStream) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaDataStream) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamData ¶
type GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamData struct {
	// FirebaseAppId: Output only. ID of the corresponding Android app in Firebase,
	// if any. This ID can change if the Android app is deleted and recreated.
	FirebaseAppId string `json:"firebaseAppId,omitempty"`
	// PackageName: Immutable. The package name for the app being measured.
	// Example: "com.example.myandroidapp"
	PackageName string `json:"packageName,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FirebaseAppId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FirebaseAppId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamData: Data specific to Android app streams.

func (GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamData) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaDataStreamAndroidAppStreamData) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaDataStreamIosAppStreamData ¶
type GoogleAnalyticsAdminV1betaDataStreamIosAppStreamData struct {
	// BundleId: Required. Immutable. The Apple App Store Bundle ID for the app
	// Example: "com.example.myiosapp"
	BundleId string `json:"bundleId,omitempty"`
	// FirebaseAppId: Output only. ID of the corresponding iOS app in Firebase, if
	// any. This ID can change if the iOS app is deleted and recreated.
	FirebaseAppId string `json:"firebaseAppId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BundleId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BundleId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaDataStreamIosAppStreamData: Data specific to iOS app streams.

func (GoogleAnalyticsAdminV1betaDataStreamIosAppStreamData) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaDataStreamIosAppStreamData) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaDataStreamWebStreamData ¶
type GoogleAnalyticsAdminV1betaDataStreamWebStreamData struct {
	// DefaultUri: Domain name of the web app being measured, or empty. Example:
	// "http://www.google.com", "https://www.google.com"
	DefaultUri string `json:"defaultUri,omitempty"`
	// FirebaseAppId: Output only. ID of the corresponding web app in Firebase, if
	// any. This ID can change if the web app is deleted and recreated.
	FirebaseAppId string `json:"firebaseAppId,omitempty"`
	// MeasurementId: Output only. Analytics Measurement ID. Example:
	// "G-1A2BCD345E"
	MeasurementId string `json:"measurementId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DefaultUri") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DefaultUri") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaDataStreamWebStreamData: Data specific to web streams.

func (GoogleAnalyticsAdminV1betaDataStreamWebStreamData) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaDataStreamWebStreamData) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaFirebaseLink ¶
type GoogleAnalyticsAdminV1betaFirebaseLink struct {
	// CreateTime: Output only. Time when this FirebaseLink was originally created.
	CreateTime string `json:"createTime,omitempty"`
	// Name: Output only. Example format: properties/1234/firebaseLinks/5678
	Name string `json:"name,omitempty"`
	// Project: Immutable. Firebase project resource name. When creating a
	// FirebaseLink, you may provide this resource name using either a project
	// number or project ID. Once this resource has been created, returned
	// FirebaseLinks will always have a project_name that contains a project
	// number. Format: 'projects/{project number}' Example: 'projects/1234'
	Project string `json:"project,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "CreateTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CreateTime") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaFirebaseLink: A link between a Google Analytics property and a Firebase project.

func (GoogleAnalyticsAdminV1betaFirebaseLink) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaFirebaseLink) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaGoogleAdsLink ¶
type GoogleAnalyticsAdminV1betaGoogleAdsLink struct {
	// AdsPersonalizationEnabled: Enable personalized advertising features with
	// this integration. Automatically publish my Google Analytics audience lists
	// and Google Analytics remarketing events/parameters to the linked Google Ads
	// account. If this field is not set on create/update, it will be defaulted to
	// true.
	AdsPersonalizationEnabled bool `json:"adsPersonalizationEnabled,omitempty"`
	// CanManageClients: Output only. If true, this link is for a Google Ads
	// manager account.
	CanManageClients bool `json:"canManageClients,omitempty"`
	// CreateTime: Output only. Time when this link was originally created.
	CreateTime string `json:"createTime,omitempty"`
	// CreatorEmailAddress: Output only. Email address of the user that created the
	// link. An empty string will be returned if the email address can't be
	// retrieved.
	CreatorEmailAddress string `json:"creatorEmailAddress,omitempty"`
	// CustomerId: Immutable. Google Ads customer ID.
	CustomerId string `json:"customerId,omitempty"`
	// Name: Output only. Format:
	// properties/{propertyId}/googleAdsLinks/{googleAdsLinkId} Note:
	// googleAdsLinkId is not the Google Ads customer ID.
	Name string `json:"name,omitempty"`
	// UpdateTime: Output only. Time when this link was last updated.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AdsPersonalizationEnabled")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AdsPersonalizationEnabled") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaGoogleAdsLink: A link between a Google Analytics property and a Google Ads account.

func (GoogleAnalyticsAdminV1betaGoogleAdsLink) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaGoogleAdsLink) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaKeyEvent ¶
added in v0.173.0
type GoogleAnalyticsAdminV1betaKeyEvent struct {
	// CountingMethod: Required. The method by which Key Events will be counted
	// across multiple events within a session.
	//
	// Possible values:
	//   "COUNTING_METHOD_UNSPECIFIED" - Counting method not specified.
	//   "ONCE_PER_EVENT" - Each Event instance is considered a Key Event.
	//   "ONCE_PER_SESSION" - An Event instance is considered a Key Event at most
	// once per session per user.
	CountingMethod string `json:"countingMethod,omitempty"`
	// CreateTime: Output only. Time when this key event was created in the
	// property.
	CreateTime string `json:"createTime,omitempty"`
	// Custom: Output only. If set to true, this key event refers to a custom
	// event. If set to false, this key event refers to a default event in GA.
	// Default events typically have special meaning in GA. Default events are
	// usually created for you by the GA system, but in some cases can be created
	// by property admins. Custom events count towards the maximum number of custom
	// key events that may be created per property.
	Custom bool `json:"custom,omitempty"`
	// DefaultValue: Optional. Defines a default value/currency for a key event.
	DefaultValue *GoogleAnalyticsAdminV1betaKeyEventDefaultValue `json:"defaultValue,omitempty"`
	// Deletable: Output only. If set to true, this event can be deleted.
	Deletable bool `json:"deletable,omitempty"`
	// EventName: Immutable. The event name for this key event. Examples: 'click',
	// 'purchase'
	EventName string `json:"eventName,omitempty"`
	// Name: Output only. Resource name of this key event. Format:
	// properties/{property}/keyEvents/{key_event}
	Name string `json:"name,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "CountingMethod") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CountingMethod") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaKeyEvent: A key event in a Google Analytics property.

func (GoogleAnalyticsAdminV1betaKeyEvent) MarshalJSON ¶
added in v0.173.0
func (s GoogleAnalyticsAdminV1betaKeyEvent) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaKeyEventDefaultValue ¶
added in v0.173.0
type GoogleAnalyticsAdminV1betaKeyEventDefaultValue struct {
	// CurrencyCode: Required. When an occurrence of this Key Event (specified by
	// event_name) has no set currency this currency will be applied as the
	// default. Must be in ISO 4217 currency code format. See
	// https://en.wikipedia.org/wiki/ISO_4217 for more information.
	CurrencyCode string `json:"currencyCode,omitempty"`
	// NumericValue: Required. This will be used to populate the "value" parameter
	// for all occurrences of this Key Event (specified by event_name) where that
	// parameter is unset.
	NumericValue float64 `json:"numericValue,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CurrencyCode") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CurrencyCode") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaKeyEventDefaultValue: Defines a default value/currency for a key event.

func (GoogleAnalyticsAdminV1betaKeyEventDefaultValue) MarshalJSON ¶
added in v0.173.0
func (s GoogleAnalyticsAdminV1betaKeyEventDefaultValue) MarshalJSON() ([]byte, error)
func (*GoogleAnalyticsAdminV1betaKeyEventDefaultValue) UnmarshalJSON ¶
added in v0.173.0
func (s *GoogleAnalyticsAdminV1betaKeyEventDefaultValue) UnmarshalJSON(data []byte) error
type GoogleAnalyticsAdminV1betaListAccountSummariesResponse ¶
type GoogleAnalyticsAdminV1betaListAccountSummariesResponse struct {
	// AccountSummaries: Account summaries of all accounts the caller has access
	// to.
	AccountSummaries []*GoogleAnalyticsAdminV1betaAccountSummary `json:"accountSummaries,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AccountSummaries") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccountSummaries") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaListAccountSummariesResponse: Response message for ListAccountSummaries RPC.

func (GoogleAnalyticsAdminV1betaListAccountSummariesResponse) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaListAccountSummariesResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaListAccountsResponse ¶
type GoogleAnalyticsAdminV1betaListAccountsResponse struct {
	// Accounts: Results that were accessible to the caller.
	Accounts []*GoogleAnalyticsAdminV1betaAccount `json:"accounts,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Accounts") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Accounts") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaListAccountsResponse: Request message for ListAccounts RPC.

func (GoogleAnalyticsAdminV1betaListAccountsResponse) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaListAccountsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaListConversionEventsResponse ¶
type GoogleAnalyticsAdminV1betaListConversionEventsResponse struct {
	// ConversionEvents: The requested conversion events
	ConversionEvents []*GoogleAnalyticsAdminV1betaConversionEvent `json:"conversionEvents,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ConversionEvents") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ConversionEvents") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaListConversionEventsResponse: Response message for ListConversionEvents RPC.

func (GoogleAnalyticsAdminV1betaListConversionEventsResponse) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaListConversionEventsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaListCustomDimensionsResponse ¶
type GoogleAnalyticsAdminV1betaListCustomDimensionsResponse struct {
	// CustomDimensions: List of CustomDimensions.
	CustomDimensions []*GoogleAnalyticsAdminV1betaCustomDimension `json:"customDimensions,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "CustomDimensions") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CustomDimensions") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaListCustomDimensionsResponse: Response message for ListCustomDimensions RPC.

func (GoogleAnalyticsAdminV1betaListCustomDimensionsResponse) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaListCustomDimensionsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaListCustomMetricsResponse ¶
type GoogleAnalyticsAdminV1betaListCustomMetricsResponse struct {
	// CustomMetrics: List of CustomMetrics.
	CustomMetrics []*GoogleAnalyticsAdminV1betaCustomMetric `json:"customMetrics,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "CustomMetrics") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CustomMetrics") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaListCustomMetricsResponse: Response message for ListCustomMetrics RPC.

func (GoogleAnalyticsAdminV1betaListCustomMetricsResponse) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaListCustomMetricsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaListDataStreamsResponse ¶
type GoogleAnalyticsAdminV1betaListDataStreamsResponse struct {
	// DataStreams: List of DataStreams.
	DataStreams []*GoogleAnalyticsAdminV1betaDataStream `json:"dataStreams,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DataStreams") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DataStreams") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaListDataStreamsResponse: Response message for ListDataStreams RPC.

func (GoogleAnalyticsAdminV1betaListDataStreamsResponse) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaListDataStreamsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaListFirebaseLinksResponse ¶
type GoogleAnalyticsAdminV1betaListFirebaseLinksResponse struct {
	// FirebaseLinks: List of FirebaseLinks. This will have at most one value.
	FirebaseLinks []*GoogleAnalyticsAdminV1betaFirebaseLink `json:"firebaseLinks,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	// Currently, Google Analytics supports only one FirebaseLink per property, so
	// this will never be populated.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "FirebaseLinks") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FirebaseLinks") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaListFirebaseLinksResponse: Response message for ListFirebaseLinks RPC

func (GoogleAnalyticsAdminV1betaListFirebaseLinksResponse) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaListFirebaseLinksResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponse ¶
type GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponse struct {
	// GoogleAdsLinks: List of GoogleAdsLinks.
	GoogleAdsLinks []*GoogleAnalyticsAdminV1betaGoogleAdsLink `json:"googleAdsLinks,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "GoogleAdsLinks") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "GoogleAdsLinks") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponse: Response message for ListGoogleAdsLinks RPC.

func (GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponse) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaListKeyEventsResponse ¶
added in v0.173.0
type GoogleAnalyticsAdminV1betaListKeyEventsResponse struct {
	// KeyEvents: The requested Key Events
	KeyEvents []*GoogleAnalyticsAdminV1betaKeyEvent `json:"keyEvents,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "KeyEvents") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "KeyEvents") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaListKeyEventsResponse: Response message for ListKeyEvents RPC.

func (GoogleAnalyticsAdminV1betaListKeyEventsResponse) MarshalJSON ¶
added in v0.173.0
func (s GoogleAnalyticsAdminV1betaListKeyEventsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponse ¶
type GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponse struct {
	// MeasurementProtocolSecrets: A list of secrets for the parent stream
	// specified in the request.
	MeasurementProtocolSecrets []*GoogleAnalyticsAdminV1betaMeasurementProtocolSecret `json:"measurementProtocolSecrets,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "MeasurementProtocolSecrets")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "MeasurementProtocolSecrets") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponse: Response message for ListMeasurementProtocolSecret RPC

func (GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponse) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaListPropertiesResponse ¶
type GoogleAnalyticsAdminV1betaListPropertiesResponse struct {
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Properties: Results that matched the filter criteria and were accessible to
	// the caller.
	Properties []*GoogleAnalyticsAdminV1betaProperty `json:"properties,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "NextPageToken") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "NextPageToken") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaListPropertiesResponse: Response message for ListProperties RPC.

func (GoogleAnalyticsAdminV1betaListPropertiesResponse) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaListPropertiesResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaMeasurementProtocolSecret ¶
type GoogleAnalyticsAdminV1betaMeasurementProtocolSecret struct {
	// DisplayName: Required. Human-readable display name for this secret.
	DisplayName string `json:"displayName,omitempty"`
	// Name: Output only. Resource name of this secret. This secret may be a child
	// of any type of stream. Format:
	// properties/{property}/dataStreams/{dataStream}/measurementProtocolSecrets/{me
	// asurementProtocolSecret}
	Name string `json:"name,omitempty"`
	// SecretValue: Output only. The measurement protocol secret value. Pass this
	// value to the api_secret field of the Measurement Protocol API when sending
	// hits to this secret's parent property.
	SecretValue string `json:"secretValue,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DisplayName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DisplayName") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaMeasurementProtocolSecret: A secret value used for sending hits to Measurement Protocol.

func (GoogleAnalyticsAdminV1betaMeasurementProtocolSecret) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaMeasurementProtocolSecret) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaNumericValue ¶
added in v0.112.0
type GoogleAnalyticsAdminV1betaNumericValue struct {
	// DoubleValue: Double value
	DoubleValue float64 `json:"doubleValue,omitempty"`
	// Int64Value: Integer value
	Int64Value int64 `json:"int64Value,omitempty,string"`
	// ForceSendFields is a list of field names (e.g. "DoubleValue") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DoubleValue") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaNumericValue: To represent a number.

func (GoogleAnalyticsAdminV1betaNumericValue) MarshalJSON ¶
added in v0.112.0
func (s GoogleAnalyticsAdminV1betaNumericValue) MarshalJSON() ([]byte, error)
func (*GoogleAnalyticsAdminV1betaNumericValue) UnmarshalJSON ¶
added in v0.112.0
func (s *GoogleAnalyticsAdminV1betaNumericValue) UnmarshalJSON(data []byte) error
type GoogleAnalyticsAdminV1betaProperty ¶
type GoogleAnalyticsAdminV1betaProperty struct {
	// Account: Immutable. The resource name of the parent account Format:
	// accounts/{account_id} Example: "accounts/123"
	Account string `json:"account,omitempty"`
	// CreateTime: Output only. Time when the entity was originally created.
	CreateTime string `json:"createTime,omitempty"`
	// CurrencyCode: The currency type used in reports involving monetary values.
	// Format: https://en.wikipedia.org/wiki/ISO_4217 Examples: "USD", "EUR", "JPY"
	CurrencyCode string `json:"currencyCode,omitempty"`
	// DeleteTime: Output only. If set, the time at which this property was
	// trashed. If not set, then this property is not currently in the trash can.
	DeleteTime string `json:"deleteTime,omitempty"`
	// DisplayName: Required. Human-readable display name for this property. The
	// max allowed display name length is 100 UTF-16 code units.
	DisplayName string `json:"displayName,omitempty"`
	// ExpireTime: Output only. If set, the time at which this trashed property
	// will be permanently deleted. If not set, then this property is not currently
	// in the trash can and is not slated to be deleted.
	ExpireTime string `json:"expireTime,omitempty"`
	// IndustryCategory: Industry associated with this property Example:
	// AUTOMOTIVE, FOOD_AND_DRINK
	//
	// Possible values:
	//   "INDUSTRY_CATEGORY_UNSPECIFIED" - Industry category unspecified
	//   "AUTOMOTIVE" - Automotive
	//   "BUSINESS_AND_INDUSTRIAL_MARKETS" - Business and industrial markets
	//   "FINANCE" - Finance
	//   "HEALTHCARE" - Healthcare
	//   "TECHNOLOGY" - Technology
	//   "TRAVEL" - Travel
	//   "OTHER" - Other
	//   "ARTS_AND_ENTERTAINMENT" - Arts and entertainment
	//   "BEAUTY_AND_FITNESS" - Beauty and fitness
	//   "BOOKS_AND_LITERATURE" - Books and literature
	//   "FOOD_AND_DRINK" - Food and drink
	//   "GAMES" - Games
	//   "HOBBIES_AND_LEISURE" - Hobbies and leisure
	//   "HOME_AND_GARDEN" - Home and garden
	//   "INTERNET_AND_TELECOM" - Internet and telecom
	//   "LAW_AND_GOVERNMENT" - Law and government
	//   "NEWS" - News
	//   "ONLINE_COMMUNITIES" - Online communities
	//   "PEOPLE_AND_SOCIETY" - People and society
	//   "PETS_AND_ANIMALS" - Pets and animals
	//   "REAL_ESTATE" - Real estate
	//   "REFERENCE" - Reference
	//   "SCIENCE" - Science
	//   "SPORTS" - Sports
	//   "JOBS_AND_EDUCATION" - Jobs and education
	//   "SHOPPING" - Shopping
	IndustryCategory string `json:"industryCategory,omitempty"`
	// Name: Output only. Resource name of this property. Format:
	// properties/{property_id} Example: "properties/1000"
	Name string `json:"name,omitempty"`
	// Parent: Immutable. Resource name of this property's logical parent. Note:
	// The Property-Moving UI can be used to change the parent. Format:
	// accounts/{account}, properties/{property} Example: "accounts/100",
	// "properties/101"
	Parent string `json:"parent,omitempty"`
	// PropertyType: Immutable. The property type for this Property resource. When
	// creating a property, if the type is "PROPERTY_TYPE_UNSPECIFIED", then
	// "ORDINARY_PROPERTY" will be implied.
	//
	// Possible values:
	//   "PROPERTY_TYPE_UNSPECIFIED" - Unknown or unspecified property type
	//   "PROPERTY_TYPE_ORDINARY" - Ordinary Google Analytics property
	//   "PROPERTY_TYPE_SUBPROPERTY" - Google Analytics subproperty
	//   "PROPERTY_TYPE_ROLLUP" - Google Analytics rollup property
	PropertyType string `json:"propertyType,omitempty"`
	// ServiceLevel: Output only. The Google Analytics service level that applies
	// to this property.
	//
	// Possible values:
	//   "SERVICE_LEVEL_UNSPECIFIED" - Service level not specified or invalid.
	//   "GOOGLE_ANALYTICS_STANDARD" - The standard version of Google Analytics.
	//   "GOOGLE_ANALYTICS_360" - The paid, premium version of Google Analytics.
	ServiceLevel string `json:"serviceLevel,omitempty"`
	// TimeZone: Required. Reporting Time Zone, used as the day boundary for
	// reports, regardless of where the data originates. If the time zone honors
	// DST, Analytics will automatically adjust for the changes. NOTE: Changing the
	// time zone only affects data going forward, and is not applied retroactively.
	// Format: https://www.iana.org/time-zones Example: "America/Los_Angeles"
	TimeZone string `json:"timeZone,omitempty"`
	// UpdateTime: Output only. Time when entity payload fields were last updated.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Account") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Account") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaProperty: A resource message representing a Google Analytics property.

func (GoogleAnalyticsAdminV1betaProperty) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaProperty) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaPropertySummary ¶
type GoogleAnalyticsAdminV1betaPropertySummary struct {
	// DisplayName: Display name for the property referred to in this property
	// summary.
	DisplayName string `json:"displayName,omitempty"`
	// Parent: Resource name of this property's logical parent. Note: The
	// Property-Moving UI can be used to change the parent. Format:
	// accounts/{account}, properties/{property} Example: "accounts/100",
	// "properties/200"
	Parent string `json:"parent,omitempty"`
	// Property: Resource name of property referred to by this property summary
	// Format: properties/{property_id} Example: "properties/1000"
	Property string `json:"property,omitempty"`
	// PropertyType: The property's property type.
	//
	// Possible values:
	//   "PROPERTY_TYPE_UNSPECIFIED" - Unknown or unspecified property type
	//   "PROPERTY_TYPE_ORDINARY" - Ordinary Google Analytics property
	//   "PROPERTY_TYPE_SUBPROPERTY" - Google Analytics subproperty
	//   "PROPERTY_TYPE_ROLLUP" - Google Analytics rollup property
	PropertyType string `json:"propertyType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DisplayName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DisplayName") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaPropertySummary: A virtual resource representing metadata for a Google Analytics property.

func (GoogleAnalyticsAdminV1betaPropertySummary) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaPropertySummary) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaProvisionAccountTicketRequest ¶
type GoogleAnalyticsAdminV1betaProvisionAccountTicketRequest struct {
	// Account: The account to create.
	Account *GoogleAnalyticsAdminV1betaAccount `json:"account,omitempty"`
	// RedirectUri: Redirect URI where the user will be sent after accepting Terms
	// of Service. Must be configured in Cloud Console as a Redirect URI.
	RedirectUri string `json:"redirectUri,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Account") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Account") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaProvisionAccountTicketRequest: Request message for ProvisionAccountTicket RPC.

func (GoogleAnalyticsAdminV1betaProvisionAccountTicketRequest) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaProvisionAccountTicketRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaProvisionAccountTicketResponse ¶
type GoogleAnalyticsAdminV1betaProvisionAccountTicketResponse struct {
	// AccountTicketId: The param to be passed in the ToS link.
	AccountTicketId string `json:"accountTicketId,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AccountTicketId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccountTicketId") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaProvisionAccountTicketResponse: Response message for ProvisionAccountTicket RPC.

func (GoogleAnalyticsAdminV1betaProvisionAccountTicketResponse) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaProvisionAccountTicketResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaRunAccessReportRequest ¶
added in v0.112.0
type GoogleAnalyticsAdminV1betaRunAccessReportRequest struct {
	// DateRanges: Date ranges of access records to read. If multiple date ranges
	// are requested, each response row will contain a zero based date range index.
	// If two date ranges overlap, the access records for the overlapping days is
	// included in the response rows for both date ranges. Requests are allowed up
	// to 2 date ranges.
	DateRanges []*GoogleAnalyticsAdminV1betaAccessDateRange `json:"dateRanges,omitempty"`
	// DimensionFilter: Dimension filters let you restrict report response to
	// specific dimension values which match the filter. For example, filtering on
	// access records of a single user. To learn more, see Fundamentals of
	// Dimension Filters
	// (https://developers.google.com/analytics/devguides/reporting/data/v1/basics#dimension_filters)
	// for examples. Metrics cannot be used in this filter.
	DimensionFilter *GoogleAnalyticsAdminV1betaAccessFilterExpression `json:"dimensionFilter,omitempty"`
	// Dimensions: The dimensions requested and displayed in the response. Requests
	// are allowed up to 9 dimensions.
	Dimensions []*GoogleAnalyticsAdminV1betaAccessDimension `json:"dimensions,omitempty"`
	// ExpandGroups: Optional. Decides whether to return the users within user
	// groups. This field works only when include_all_users is set to true. If
	// true, it will return all users with access to the specified property or
	// account. If false, only the users with direct access will be returned.
	ExpandGroups bool `json:"expandGroups,omitempty"`
	// IncludeAllUsers: Optional. Determines whether to include users who have
	// never made an API call in the response. If true, all users with access to
	// the specified property or account are included in the response, regardless
	// of whether they have made an API call or not. If false, only the users who
	// have made an API call will be included.
	IncludeAllUsers bool `json:"includeAllUsers,omitempty"`
	// Limit: The number of rows to return. If unspecified, 10,000 rows are
	// returned. The API returns a maximum of 100,000 rows per request, no matter
	// how many you ask for. `limit` must be positive. The API may return fewer
	// rows than the requested `limit`, if there aren't as many remaining rows as
	// the `limit`. For instance, there are fewer than 300 possible values for the
	// dimension `country`, so when reporting on only `country`, you can't get more
	// than 300 rows, even if you set `limit` to a higher value. To learn more
	// about this pagination parameter, see Pagination
	// (https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination).
	Limit int64 `json:"limit,omitempty,string"`
	// MetricFilter: Metric filters allow you to restrict report response to
	// specific metric values which match the filter. Metric filters are applied
	// after aggregating the report's rows, similar to SQL having-clause.
	// Dimensions cannot be used in this filter.
	MetricFilter *GoogleAnalyticsAdminV1betaAccessFilterExpression `json:"metricFilter,omitempty"`
	// Metrics: The metrics requested and displayed in the response. Requests are
	// allowed up to 10 metrics.
	Metrics []*GoogleAnalyticsAdminV1betaAccessMetric `json:"metrics,omitempty"`
	// Offset: The row count of the start row. The first row is counted as row 0.
	// If offset is unspecified, it is treated as 0. If offset is zero, then this
	// method will return the first page of results with `limit` entries. To learn
	// more about this pagination parameter, see Pagination
	// (https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination).
	Offset int64 `json:"offset,omitempty,string"`
	// OrderBys: Specifies how rows are ordered in the response.
	OrderBys []*GoogleAnalyticsAdminV1betaAccessOrderBy `json:"orderBys,omitempty"`
	// ReturnEntityQuota: Toggles whether to return the current state of this
	// Analytics Property's quota. Quota is returned in AccessQuota (#AccessQuota).
	// For account-level requests, this field must be false.
	ReturnEntityQuota bool `json:"returnEntityQuota,omitempty"`
	// TimeZone: This request's time zone if specified. If unspecified, the
	// property's time zone is used. The request's time zone is used to interpret
	// the start & end dates of the report. Formatted as strings from the IANA Time
	// Zone database (https://www.iana.org/time-zones); for example
	// "America/New_York" or "Asia/Tokyo".
	TimeZone string `json:"timeZone,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DateRanges") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DateRanges") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaRunAccessReportRequest: The request for a Data Access Record Report.

func (GoogleAnalyticsAdminV1betaRunAccessReportRequest) MarshalJSON ¶
added in v0.112.0
func (s GoogleAnalyticsAdminV1betaRunAccessReportRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaRunAccessReportResponse ¶
added in v0.112.0
type GoogleAnalyticsAdminV1betaRunAccessReportResponse struct {
	// DimensionHeaders: The header for a column in the report that corresponds to
	// a specific dimension. The number of DimensionHeaders and ordering of
	// DimensionHeaders matches the dimensions present in rows.
	DimensionHeaders []*GoogleAnalyticsAdminV1betaAccessDimensionHeader `json:"dimensionHeaders,omitempty"`
	// MetricHeaders: The header for a column in the report that corresponds to a
	// specific metric. The number of MetricHeaders and ordering of MetricHeaders
	// matches the metrics present in rows.
	MetricHeaders []*GoogleAnalyticsAdminV1betaAccessMetricHeader `json:"metricHeaders,omitempty"`
	// Quota: The quota state for this Analytics property including this request.
	// This field doesn't work with account-level requests.
	Quota *GoogleAnalyticsAdminV1betaAccessQuota `json:"quota,omitempty"`
	// RowCount: The total number of rows in the query result. `rowCount` is
	// independent of the number of rows returned in the response, the `limit`
	// request parameter, and the `offset` request parameter. For example if a
	// query returns 175 rows and includes `limit` of 50 in the API request, the
	// response will contain `rowCount` of 175 but only 50 rows. To learn more
	// about this pagination parameter, see Pagination
	// (https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination).
	RowCount int64 `json:"rowCount,omitempty"`
	// Rows: Rows of dimension value combinations and metric values in the report.
	Rows []*GoogleAnalyticsAdminV1betaAccessRow `json:"rows,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DimensionHeaders") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DimensionHeaders") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaRunAccessReportResponse: The customized Data Access Record Report response.

func (GoogleAnalyticsAdminV1betaRunAccessReportResponse) MarshalJSON ¶
added in v0.112.0
func (s GoogleAnalyticsAdminV1betaRunAccessReportResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequest ¶
type GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequest struct {
	// Action: Optional. If set, only return changes that match one or more of
	// these types of actions.
	//
	// Possible values:
	//   "ACTION_TYPE_UNSPECIFIED" - Action type unknown or not specified.
	//   "CREATED" - Resource was created in this change.
	//   "UPDATED" - Resource was updated in this change.
	//   "DELETED" - Resource was deleted in this change.
	Action []string `json:"action,omitempty"`
	// ActorEmail: Optional. If set, only return changes if they are made by a user
	// in this list.
	ActorEmail []string `json:"actorEmail,omitempty"`
	// EarliestChangeTime: Optional. If set, only return changes made after this
	// time (inclusive).
	EarliestChangeTime string `json:"earliestChangeTime,omitempty"`
	// LatestChangeTime: Optional. If set, only return changes made before this
	// time (inclusive).
	LatestChangeTime string `json:"latestChangeTime,omitempty"`
	// PageSize: Optional. The maximum number of ChangeHistoryEvent items to
	// return. If unspecified, at most 50 items will be returned. The maximum value
	// is 200 (higher values will be coerced to the maximum). Note that the service
	// may return a page with fewer items than this value specifies (potentially
	// even zero), and that there still may be additional pages. If you want a
	// particular number of items, you'll need to continue requesting additional
	// pages using `page_token` until you get the needed number.
	PageSize int64 `json:"pageSize,omitempty"`
	// PageToken: Optional. A page token, received from a previous
	// `SearchChangeHistoryEvents` call. Provide this to retrieve the subsequent
	// page. When paginating, all other parameters provided to
	// `SearchChangeHistoryEvents` must match the call that provided the page
	// token.
	PageToken string `json:"pageToken,omitempty"`
	// Property: Optional. Resource name for a child property. If set, only return
	// changes made to this property or its child resources. Format:
	// properties/{propertyId} Example: `properties/100`
	Property string `json:"property,omitempty"`
	// ResourceType: Optional. If set, only return changes if they are for a
	// resource that matches at least one of these types.
	//
	// Possible values:
	//   "CHANGE_HISTORY_RESOURCE_TYPE_UNSPECIFIED" - Resource type unknown or not
	// specified.
	//   "ACCOUNT" - Account resource
	//   "PROPERTY" - Property resource
	//   "FIREBASE_LINK" - FirebaseLink resource
	//   "GOOGLE_ADS_LINK" - GoogleAdsLink resource
	//   "GOOGLE_SIGNALS_SETTINGS" - GoogleSignalsSettings resource
	//   "CONVERSION_EVENT" - ConversionEvent resource
	//   "MEASUREMENT_PROTOCOL_SECRET" - MeasurementProtocolSecret resource
	//   "CUSTOM_DIMENSION" - CustomDimension resource
	//   "CUSTOM_METRIC" - CustomMetric resource
	//   "DATA_RETENTION_SETTINGS" - DataRetentionSettings resource
	//   "DISPLAY_VIDEO_360_ADVERTISER_LINK" - DisplayVideo360AdvertiserLink
	// resource
	//   "DISPLAY_VIDEO_360_ADVERTISER_LINK_PROPOSAL" -
	// DisplayVideo360AdvertiserLinkProposal resource
	//   "DATA_STREAM" - DataStream resource
	//   "ATTRIBUTION_SETTINGS" - AttributionSettings resource
	ResourceType []string `json:"resourceType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Action") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Action") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequest: Request message for SearchChangeHistoryEvents RPC.

func (GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequest) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponse ¶
type GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponse struct {
	// ChangeHistoryEvents: Results that were accessible to the caller.
	ChangeHistoryEvents []*GoogleAnalyticsAdminV1betaChangeHistoryEvent `json:"changeHistoryEvents,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ChangeHistoryEvents") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ChangeHistoryEvents") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponse: Response message for SearchAccounts RPC.

func (GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponse) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponse) MarshalJSON() ([]byte, error)
type GoogleProtobufEmpty ¶
type GoogleProtobufEmpty struct {
	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
}

GoogleProtobufEmpty: A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }

type PropertiesAcknowledgeUserDataCollectionCall ¶
type PropertiesAcknowledgeUserDataCollectionCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesAcknowledgeUserDataCollectionCall) Context ¶
func (c *PropertiesAcknowledgeUserDataCollectionCall) Context(ctx context.Context) *PropertiesAcknowledgeUserDataCollectionCall

Context sets the context to be used in this call's Do method.

func (*PropertiesAcknowledgeUserDataCollectionCall) Do ¶
func (c *PropertiesAcknowledgeUserDataCollectionCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionResponse, error)

Do executes the "analyticsadmin.properties.acknowledgeUserDataCollection" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionResponse.ServerRespon se.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesAcknowledgeUserDataCollectionCall) Fields ¶
func (c *PropertiesAcknowledgeUserDataCollectionCall) Fields(s ...googleapi.Field) *PropertiesAcknowledgeUserDataCollectionCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesAcknowledgeUserDataCollectionCall) Header ¶
func (c *PropertiesAcknowledgeUserDataCollectionCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesConversionEventsCreateCall ¶
type PropertiesConversionEventsCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesConversionEventsCreateCall) Context ¶
func (c *PropertiesConversionEventsCreateCall) Context(ctx context.Context) *PropertiesConversionEventsCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesConversionEventsCreateCall) Do ¶
func (c *PropertiesConversionEventsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaConversionEvent, error)

Do executes the "analyticsadmin.properties.conversionEvents.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaConversionEvent.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesConversionEventsCreateCall) Fields ¶
func (c *PropertiesConversionEventsCreateCall) Fields(s ...googleapi.Field) *PropertiesConversionEventsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesConversionEventsCreateCall) Header ¶
func (c *PropertiesConversionEventsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesConversionEventsDeleteCall ¶
type PropertiesConversionEventsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesConversionEventsDeleteCall) Context ¶
func (c *PropertiesConversionEventsDeleteCall) Context(ctx context.Context) *PropertiesConversionEventsDeleteCall

Context sets the context to be used in this call's Do method.

func (*PropertiesConversionEventsDeleteCall) Do ¶
func (c *PropertiesConversionEventsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.properties.conversionEvents.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesConversionEventsDeleteCall) Fields ¶
func (c *PropertiesConversionEventsDeleteCall) Fields(s ...googleapi.Field) *PropertiesConversionEventsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesConversionEventsDeleteCall) Header ¶
func (c *PropertiesConversionEventsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesConversionEventsGetCall ¶
type PropertiesConversionEventsGetCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesConversionEventsGetCall) Context ¶
func (c *PropertiesConversionEventsGetCall) Context(ctx context.Context) *PropertiesConversionEventsGetCall

Context sets the context to be used in this call's Do method.

func (*PropertiesConversionEventsGetCall) Do ¶
func (c *PropertiesConversionEventsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaConversionEvent, error)

Do executes the "analyticsadmin.properties.conversionEvents.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaConversionEvent.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesConversionEventsGetCall) Fields ¶
func (c *PropertiesConversionEventsGetCall) Fields(s ...googleapi.Field) *PropertiesConversionEventsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesConversionEventsGetCall) Header ¶
func (c *PropertiesConversionEventsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesConversionEventsGetCall) IfNoneMatch ¶
func (c *PropertiesConversionEventsGetCall) IfNoneMatch(entityTag string) *PropertiesConversionEventsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesConversionEventsListCall ¶
type PropertiesConversionEventsListCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesConversionEventsListCall) Context ¶
func (c *PropertiesConversionEventsListCall) Context(ctx context.Context) *PropertiesConversionEventsListCall

Context sets the context to be used in this call's Do method.

func (*PropertiesConversionEventsListCall) Do ¶
func (c *PropertiesConversionEventsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaListConversionEventsResponse, error)

Do executes the "analyticsadmin.properties.conversionEvents.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaListConversionEventsResponse.ServerResponse.Header

or (if a response was returned at all) in error.(*googleapi.Error).Header.


Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesConversionEventsListCall) Fields ¶
func (c *PropertiesConversionEventsListCall) Fields(s ...googleapi.Field) *PropertiesConversionEventsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesConversionEventsListCall) Header ¶
func (c *PropertiesConversionEventsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesConversionEventsListCall) IfNoneMatch ¶
func (c *PropertiesConversionEventsListCall) IfNoneMatch(entityTag string) *PropertiesConversionEventsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesConversionEventsListCall) PageSize ¶
func (c *PropertiesConversionEventsListCall) PageSize(pageSize int64) *PropertiesConversionEventsListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. If unspecified, at most 50 resources will be returned. The maximum value is 200; (higher values will be coerced to the maximum)

func (*PropertiesConversionEventsListCall) PageToken ¶
func (c *PropertiesConversionEventsListCall) PageToken(pageToken string) *PropertiesConversionEventsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListConversionEvents` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListConversionEvents` must match the call that provided the page token.

func (*PropertiesConversionEventsListCall) Pages ¶
func (c *PropertiesConversionEventsListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1betaListConversionEventsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesConversionEventsPatchCall ¶
added in v0.137.0
type PropertiesConversionEventsPatchCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesConversionEventsPatchCall) Context ¶
added in v0.137.0
func (c *PropertiesConversionEventsPatchCall) Context(ctx context.Context) *PropertiesConversionEventsPatchCall

Context sets the context to be used in this call's Do method.

func (*PropertiesConversionEventsPatchCall) Do ¶
added in v0.137.0
func (c *PropertiesConversionEventsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaConversionEvent, error)

Do executes the "analyticsadmin.properties.conversionEvents.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaConversionEvent.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesConversionEventsPatchCall) Fields ¶
added in v0.137.0
func (c *PropertiesConversionEventsPatchCall) Fields(s ...googleapi.Field) *PropertiesConversionEventsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesConversionEventsPatchCall) Header ¶
added in v0.137.0
func (c *PropertiesConversionEventsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesConversionEventsPatchCall) UpdateMask ¶
added in v0.137.0
func (c *PropertiesConversionEventsPatchCall) UpdateMask(updateMask string) *PropertiesConversionEventsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated. Field names must be in snake case (e.g., "field_to_update"). Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.

type PropertiesConversionEventsService ¶
type PropertiesConversionEventsService struct {
	// contains filtered or unexported fields
}
func NewPropertiesConversionEventsService ¶
func NewPropertiesConversionEventsService(s *Service) *PropertiesConversionEventsService
func (*PropertiesConversionEventsService) Create ¶
func (r *PropertiesConversionEventsService) Create(parent string, googleanalyticsadminv1betaconversionevent *GoogleAnalyticsAdminV1betaConversionEvent) *PropertiesConversionEventsCreateCall

Create: Deprecated: Use `CreateKeyEvent` instead. Creates a conversion event with the specified attributes.

parent: The resource name of the parent property where this conversion event will be created. Format: properties/123.
func (*PropertiesConversionEventsService) Delete ¶
func (r *PropertiesConversionEventsService) Delete(name string) *PropertiesConversionEventsDeleteCall

Delete: Deprecated: Use `DeleteKeyEvent` instead. Deletes a conversion event in a property.

name: The resource name of the conversion event to delete. Format: properties/{property}/conversionEvents/{conversion_event} Example: "properties/123/conversionEvents/456".
func (*PropertiesConversionEventsService) Get ¶
func (r *PropertiesConversionEventsService) Get(name string) *PropertiesConversionEventsGetCall

Get: Deprecated: Use `GetKeyEvent` instead. Retrieve a single conversion event.

name: The resource name of the conversion event to retrieve. Format: properties/{property}/conversionEvents/{conversion_event} Example: "properties/123/conversionEvents/456".
func (*PropertiesConversionEventsService) List ¶
func (r *PropertiesConversionEventsService) List(parent string) *PropertiesConversionEventsListCall

List: Deprecated: Use `ListKeyEvents` instead. Returns a list of conversion events in the specified parent property. Returns an empty list if no conversion events are found.

parent: The resource name of the parent property. Example: 'properties/123'.
func (*PropertiesConversionEventsService) Patch ¶
added in v0.137.0
func (r *PropertiesConversionEventsService) Patch(name string, googleanalyticsadminv1betaconversionevent *GoogleAnalyticsAdminV1betaConversionEvent) *PropertiesConversionEventsPatchCall

Patch: Deprecated: Use `UpdateKeyEvent` instead. Updates a conversion event with the specified attributes.

name: Output only. Resource name of this conversion event. Format: properties/{property}/conversionEvents/{conversion_event}.
type PropertiesCreateCall ¶
type PropertiesCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesCreateCall) Context ¶
func (c *PropertiesCreateCall) Context(ctx context.Context) *PropertiesCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesCreateCall) Do ¶
func (c *PropertiesCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaProperty, error)

Do executes the "analyticsadmin.properties.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaProperty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesCreateCall) Fields ¶
func (c *PropertiesCreateCall) Fields(s ...googleapi.Field) *PropertiesCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesCreateCall) Header ¶
func (c *PropertiesCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesCustomDimensionsArchiveCall ¶
type PropertiesCustomDimensionsArchiveCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesCustomDimensionsArchiveCall) Context ¶
func (c *PropertiesCustomDimensionsArchiveCall) Context(ctx context.Context) *PropertiesCustomDimensionsArchiveCall

Context sets the context to be used in this call's Do method.

func (*PropertiesCustomDimensionsArchiveCall) Do ¶
func (c *PropertiesCustomDimensionsArchiveCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.properties.customDimensions.archive" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesCustomDimensionsArchiveCall) Fields ¶
func (c *PropertiesCustomDimensionsArchiveCall) Fields(s ...googleapi.Field) *PropertiesCustomDimensionsArchiveCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesCustomDimensionsArchiveCall) Header ¶
func (c *PropertiesCustomDimensionsArchiveCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesCustomDimensionsCreateCall ¶
type PropertiesCustomDimensionsCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesCustomDimensionsCreateCall) Context ¶
func (c *PropertiesCustomDimensionsCreateCall) Context(ctx context.Context) *PropertiesCustomDimensionsCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesCustomDimensionsCreateCall) Do ¶
func (c *PropertiesCustomDimensionsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaCustomDimension, error)

Do executes the "analyticsadmin.properties.customDimensions.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaCustomDimension.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesCustomDimensionsCreateCall) Fields ¶
func (c *PropertiesCustomDimensionsCreateCall) Fields(s ...googleapi.Field) *PropertiesCustomDimensionsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesCustomDimensionsCreateCall) Header ¶
func (c *PropertiesCustomDimensionsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesCustomDimensionsGetCall ¶
type PropertiesCustomDimensionsGetCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesCustomDimensionsGetCall) Context ¶
func (c *PropertiesCustomDimensionsGetCall) Context(ctx context.Context) *PropertiesCustomDimensionsGetCall

Context sets the context to be used in this call's Do method.

func (*PropertiesCustomDimensionsGetCall) Do ¶
func (c *PropertiesCustomDimensionsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaCustomDimension, error)

Do executes the "analyticsadmin.properties.customDimensions.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaCustomDimension.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesCustomDimensionsGetCall) Fields ¶
func (c *PropertiesCustomDimensionsGetCall) Fields(s ...googleapi.Field) *PropertiesCustomDimensionsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesCustomDimensionsGetCall) Header ¶
func (c *PropertiesCustomDimensionsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesCustomDimensionsGetCall) IfNoneMatch ¶
func (c *PropertiesCustomDimensionsGetCall) IfNoneMatch(entityTag string) *PropertiesCustomDimensionsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesCustomDimensionsListCall ¶
type PropertiesCustomDimensionsListCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesCustomDimensionsListCall) Context ¶
func (c *PropertiesCustomDimensionsListCall) Context(ctx context.Context) *PropertiesCustomDimensionsListCall

Context sets the context to be used in this call's Do method.

func (*PropertiesCustomDimensionsListCall) Do ¶
func (c *PropertiesCustomDimensionsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaListCustomDimensionsResponse, error)

Do executes the "analyticsadmin.properties.customDimensions.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaListCustomDimensionsResponse.ServerResponse.Header

or (if a response was returned at all) in error.(*googleapi.Error).Header.


Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesCustomDimensionsListCall) Fields ¶
func (c *PropertiesCustomDimensionsListCall) Fields(s ...googleapi.Field) *PropertiesCustomDimensionsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesCustomDimensionsListCall) Header ¶
func (c *PropertiesCustomDimensionsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesCustomDimensionsListCall) IfNoneMatch ¶
func (c *PropertiesCustomDimensionsListCall) IfNoneMatch(entityTag string) *PropertiesCustomDimensionsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesCustomDimensionsListCall) PageSize ¶
func (c *PropertiesCustomDimensionsListCall) PageSize(pageSize int64) *PropertiesCustomDimensionsListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. If unspecified, at most 50 resources will be returned. The maximum value is 200 (higher values will be coerced to the maximum).

func (*PropertiesCustomDimensionsListCall) PageToken ¶
func (c *PropertiesCustomDimensionsListCall) PageToken(pageToken string) *PropertiesCustomDimensionsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListCustomDimensions` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListCustomDimensions` must match the call that provided the page token.

func (*PropertiesCustomDimensionsListCall) Pages ¶
func (c *PropertiesCustomDimensionsListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1betaListCustomDimensionsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesCustomDimensionsPatchCall ¶
type PropertiesCustomDimensionsPatchCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesCustomDimensionsPatchCall) Context ¶
func (c *PropertiesCustomDimensionsPatchCall) Context(ctx context.Context) *PropertiesCustomDimensionsPatchCall

Context sets the context to be used in this call's Do method.

func (*PropertiesCustomDimensionsPatchCall) Do ¶
func (c *PropertiesCustomDimensionsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaCustomDimension, error)

Do executes the "analyticsadmin.properties.customDimensions.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaCustomDimension.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesCustomDimensionsPatchCall) Fields ¶
func (c *PropertiesCustomDimensionsPatchCall) Fields(s ...googleapi.Field) *PropertiesCustomDimensionsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesCustomDimensionsPatchCall) Header ¶
func (c *PropertiesCustomDimensionsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesCustomDimensionsPatchCall) UpdateMask ¶
func (c *PropertiesCustomDimensionsPatchCall) UpdateMask(updateMask string) *PropertiesCustomDimensionsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated. Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.

type PropertiesCustomDimensionsService ¶
type PropertiesCustomDimensionsService struct {
	// contains filtered or unexported fields
}
func NewPropertiesCustomDimensionsService ¶
func NewPropertiesCustomDimensionsService(s *Service) *PropertiesCustomDimensionsService
func (*PropertiesCustomDimensionsService) Archive ¶
func (r *PropertiesCustomDimensionsService) Archive(name string, googleanalyticsadminv1betaarchivecustomdimensionrequest *GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequest) *PropertiesCustomDimensionsArchiveCall

Archive: Archives a CustomDimension on a property.

name: The name of the CustomDimension to archive. Example format: properties/1234/customDimensions/5678.
func (*PropertiesCustomDimensionsService) Create ¶
func (r *PropertiesCustomDimensionsService) Create(parent string, googleanalyticsadminv1betacustomdimension *GoogleAnalyticsAdminV1betaCustomDimension) *PropertiesCustomDimensionsCreateCall

Create: Creates a CustomDimension.

- parent: Example format: properties/1234.

func (*PropertiesCustomDimensionsService) Get ¶
func (r *PropertiesCustomDimensionsService) Get(name string) *PropertiesCustomDimensionsGetCall

Get: Lookup for a single CustomDimension.

name: The name of the CustomDimension to get. Example format: properties/1234/customDimensions/5678.
func (*PropertiesCustomDimensionsService) List ¶
func (r *PropertiesCustomDimensionsService) List(parent string) *PropertiesCustomDimensionsListCall

List: Lists CustomDimensions on a property.

- parent: Example format: properties/1234.

func (*PropertiesCustomDimensionsService) Patch ¶
func (r *PropertiesCustomDimensionsService) Patch(name string, googleanalyticsadminv1betacustomdimension *GoogleAnalyticsAdminV1betaCustomDimension) *PropertiesCustomDimensionsPatchCall

Patch: Updates a CustomDimension on a property.

name: Output only. Resource name for this CustomDimension resource. Format: properties/{property}/customDimensions/{customDimension}.
type PropertiesCustomMetricsArchiveCall ¶
type PropertiesCustomMetricsArchiveCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesCustomMetricsArchiveCall) Context ¶
func (c *PropertiesCustomMetricsArchiveCall) Context(ctx context.Context) *PropertiesCustomMetricsArchiveCall

Context sets the context to be used in this call's Do method.

func (*PropertiesCustomMetricsArchiveCall) Do ¶
func (c *PropertiesCustomMetricsArchiveCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.properties.customMetrics.archive" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesCustomMetricsArchiveCall) Fields ¶
func (c *PropertiesCustomMetricsArchiveCall) Fields(s ...googleapi.Field) *PropertiesCustomMetricsArchiveCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesCustomMetricsArchiveCall) Header ¶
func (c *PropertiesCustomMetricsArchiveCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesCustomMetricsCreateCall ¶
type PropertiesCustomMetricsCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesCustomMetricsCreateCall) Context ¶
func (c *PropertiesCustomMetricsCreateCall) Context(ctx context.Context) *PropertiesCustomMetricsCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesCustomMetricsCreateCall) Do ¶
func (c *PropertiesCustomMetricsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaCustomMetric, error)

Do executes the "analyticsadmin.properties.customMetrics.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaCustomMetric.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesCustomMetricsCreateCall) Fields ¶
func (c *PropertiesCustomMetricsCreateCall) Fields(s ...googleapi.Field) *PropertiesCustomMetricsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesCustomMetricsCreateCall) Header ¶
func (c *PropertiesCustomMetricsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesCustomMetricsGetCall ¶
type PropertiesCustomMetricsGetCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesCustomMetricsGetCall) Context ¶
func (c *PropertiesCustomMetricsGetCall) Context(ctx context.Context) *PropertiesCustomMetricsGetCall

Context sets the context to be used in this call's Do method.

func (*PropertiesCustomMetricsGetCall) Do ¶
func (c *PropertiesCustomMetricsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaCustomMetric, error)

Do executes the "analyticsadmin.properties.customMetrics.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaCustomMetric.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesCustomMetricsGetCall) Fields ¶
func (c *PropertiesCustomMetricsGetCall) Fields(s ...googleapi.Field) *PropertiesCustomMetricsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesCustomMetricsGetCall) Header ¶
func (c *PropertiesCustomMetricsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesCustomMetricsGetCall) IfNoneMatch ¶
func (c *PropertiesCustomMetricsGetCall) IfNoneMatch(entityTag string) *PropertiesCustomMetricsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesCustomMetricsListCall ¶
type PropertiesCustomMetricsListCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesCustomMetricsListCall) Context ¶
func (c *PropertiesCustomMetricsListCall) Context(ctx context.Context) *PropertiesCustomMetricsListCall

Context sets the context to be used in this call's Do method.

func (*PropertiesCustomMetricsListCall) Do ¶
func (c *PropertiesCustomMetricsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaListCustomMetricsResponse, error)

Do executes the "analyticsadmin.properties.customMetrics.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaListCustomMetricsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesCustomMetricsListCall) Fields ¶
func (c *PropertiesCustomMetricsListCall) Fields(s ...googleapi.Field) *PropertiesCustomMetricsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesCustomMetricsListCall) Header ¶
func (c *PropertiesCustomMetricsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesCustomMetricsListCall) IfNoneMatch ¶
func (c *PropertiesCustomMetricsListCall) IfNoneMatch(entityTag string) *PropertiesCustomMetricsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesCustomMetricsListCall) PageSize ¶
func (c *PropertiesCustomMetricsListCall) PageSize(pageSize int64) *PropertiesCustomMetricsListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. If unspecified, at most 50 resources will be returned. The maximum value is 200 (higher values will be coerced to the maximum).

func (*PropertiesCustomMetricsListCall) PageToken ¶
func (c *PropertiesCustomMetricsListCall) PageToken(pageToken string) *PropertiesCustomMetricsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListCustomMetrics` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListCustomMetrics` must match the call that provided the page token.

func (*PropertiesCustomMetricsListCall) Pages ¶
func (c *PropertiesCustomMetricsListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1betaListCustomMetricsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesCustomMetricsPatchCall ¶
type PropertiesCustomMetricsPatchCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesCustomMetricsPatchCall) Context ¶
func (c *PropertiesCustomMetricsPatchCall) Context(ctx context.Context) *PropertiesCustomMetricsPatchCall

Context sets the context to be used in this call's Do method.

func (*PropertiesCustomMetricsPatchCall) Do ¶
func (c *PropertiesCustomMetricsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaCustomMetric, error)

Do executes the "analyticsadmin.properties.customMetrics.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaCustomMetric.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesCustomMetricsPatchCall) Fields ¶
func (c *PropertiesCustomMetricsPatchCall) Fields(s ...googleapi.Field) *PropertiesCustomMetricsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesCustomMetricsPatchCall) Header ¶
func (c *PropertiesCustomMetricsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesCustomMetricsPatchCall) UpdateMask ¶
func (c *PropertiesCustomMetricsPatchCall) UpdateMask(updateMask string) *PropertiesCustomMetricsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated. Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.

type PropertiesCustomMetricsService ¶
type PropertiesCustomMetricsService struct {
	// contains filtered or unexported fields
}
func NewPropertiesCustomMetricsService ¶
func NewPropertiesCustomMetricsService(s *Service) *PropertiesCustomMetricsService
func (*PropertiesCustomMetricsService) Archive ¶
func (r *PropertiesCustomMetricsService) Archive(name string, googleanalyticsadminv1betaarchivecustommetricrequest *GoogleAnalyticsAdminV1betaArchiveCustomMetricRequest) *PropertiesCustomMetricsArchiveCall

Archive: Archives a CustomMetric on a property.

name: The name of the CustomMetric to archive. Example format: properties/1234/customMetrics/5678.
func (*PropertiesCustomMetricsService) Create ¶
func (r *PropertiesCustomMetricsService) Create(parent string, googleanalyticsadminv1betacustommetric *GoogleAnalyticsAdminV1betaCustomMetric) *PropertiesCustomMetricsCreateCall

Create: Creates a CustomMetric.

- parent: Example format: properties/1234.

func (*PropertiesCustomMetricsService) Get ¶
func (r *PropertiesCustomMetricsService) Get(name string) *PropertiesCustomMetricsGetCall

Get: Lookup for a single CustomMetric.

name: The name of the CustomMetric to get. Example format: properties/1234/customMetrics/5678.
func (*PropertiesCustomMetricsService) List ¶
func (r *PropertiesCustomMetricsService) List(parent string) *PropertiesCustomMetricsListCall

List: Lists CustomMetrics on a property.

- parent: Example format: properties/1234.

func (*PropertiesCustomMetricsService) Patch ¶
func (r *PropertiesCustomMetricsService) Patch(name string, googleanalyticsadminv1betacustommetric *GoogleAnalyticsAdminV1betaCustomMetric) *PropertiesCustomMetricsPatchCall

Patch: Updates a CustomMetric on a property.

name: Output only. Resource name for this CustomMetric resource. Format: properties/{property}/customMetrics/{customMetric}.
type PropertiesDataStreamsCreateCall ¶
type PropertiesDataStreamsCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsCreateCall) Context ¶
func (c *PropertiesDataStreamsCreateCall) Context(ctx context.Context) *PropertiesDataStreamsCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsCreateCall) Do ¶
func (c *PropertiesDataStreamsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaDataStream, error)

Do executes the "analyticsadmin.properties.dataStreams.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaDataStream.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsCreateCall) Fields ¶
func (c *PropertiesDataStreamsCreateCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsCreateCall) Header ¶
func (c *PropertiesDataStreamsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesDataStreamsDeleteCall ¶
type PropertiesDataStreamsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsDeleteCall) Context ¶
func (c *PropertiesDataStreamsDeleteCall) Context(ctx context.Context) *PropertiesDataStreamsDeleteCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsDeleteCall) Do ¶
func (c *PropertiesDataStreamsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.properties.dataStreams.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsDeleteCall) Fields ¶
func (c *PropertiesDataStreamsDeleteCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsDeleteCall) Header ¶
func (c *PropertiesDataStreamsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesDataStreamsGetCall ¶
type PropertiesDataStreamsGetCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsGetCall) Context ¶
func (c *PropertiesDataStreamsGetCall) Context(ctx context.Context) *PropertiesDataStreamsGetCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsGetCall) Do ¶
func (c *PropertiesDataStreamsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaDataStream, error)

Do executes the "analyticsadmin.properties.dataStreams.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaDataStream.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsGetCall) Fields ¶
func (c *PropertiesDataStreamsGetCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsGetCall) Header ¶
func (c *PropertiesDataStreamsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesDataStreamsGetCall) IfNoneMatch ¶
func (c *PropertiesDataStreamsGetCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesDataStreamsListCall ¶
type PropertiesDataStreamsListCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsListCall) Context ¶
func (c *PropertiesDataStreamsListCall) Context(ctx context.Context) *PropertiesDataStreamsListCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsListCall) Do ¶
func (c *PropertiesDataStreamsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaListDataStreamsResponse, error)

Do executes the "analyticsadmin.properties.dataStreams.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaListDataStreamsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsListCall) Fields ¶
func (c *PropertiesDataStreamsListCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsListCall) Header ¶
func (c *PropertiesDataStreamsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesDataStreamsListCall) IfNoneMatch ¶
func (c *PropertiesDataStreamsListCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesDataStreamsListCall) PageSize ¶
func (c *PropertiesDataStreamsListCall) PageSize(pageSize int64) *PropertiesDataStreamsListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. If unspecified, at most 50 resources will be returned. The maximum value is 200 (higher values will be coerced to the maximum).

func (*PropertiesDataStreamsListCall) PageToken ¶
func (c *PropertiesDataStreamsListCall) PageToken(pageToken string) *PropertiesDataStreamsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListDataStreams` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListDataStreams` must match the call that provided the page token.

func (*PropertiesDataStreamsListCall) Pages ¶
func (c *PropertiesDataStreamsListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1betaListDataStreamsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesDataStreamsMeasurementProtocolSecretsCreateCall ¶
type PropertiesDataStreamsMeasurementProtocolSecretsCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsMeasurementProtocolSecretsCreateCall) Context ¶
func (c *PropertiesDataStreamsMeasurementProtocolSecretsCreateCall) Context(ctx context.Context) *PropertiesDataStreamsMeasurementProtocolSecretsCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsMeasurementProtocolSecretsCreateCall) Do ¶
func (c *PropertiesDataStreamsMeasurementProtocolSecretsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaMeasurementProtocolSecret, error)

Do executes the "analyticsadmin.properties.dataStreams.measurementProtocolSecrets.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaMeasurementProtocolSecret.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsMeasurementProtocolSecretsCreateCall) Fields ¶
func (c *PropertiesDataStreamsMeasurementProtocolSecretsCreateCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsMeasurementProtocolSecretsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsMeasurementProtocolSecretsCreateCall) Header ¶
func (c *PropertiesDataStreamsMeasurementProtocolSecretsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall ¶
type PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall) Context ¶
func (c *PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall) Context(ctx context.Context) *PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall) Do ¶
func (c *PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.properties.dataStreams.measurementProtocolSecrets.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall) Fields ¶
func (c *PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall) Header ¶
func (c *PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesDataStreamsMeasurementProtocolSecretsGetCall ¶
type PropertiesDataStreamsMeasurementProtocolSecretsGetCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsMeasurementProtocolSecretsGetCall) Context ¶
func (c *PropertiesDataStreamsMeasurementProtocolSecretsGetCall) Context(ctx context.Context) *PropertiesDataStreamsMeasurementProtocolSecretsGetCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsMeasurementProtocolSecretsGetCall) Do ¶
func (c *PropertiesDataStreamsMeasurementProtocolSecretsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaMeasurementProtocolSecret, error)

Do executes the "analyticsadmin.properties.dataStreams.measurementProtocolSecrets.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaMeasurementProtocolSecret.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsMeasurementProtocolSecretsGetCall) Fields ¶
func (c *PropertiesDataStreamsMeasurementProtocolSecretsGetCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsMeasurementProtocolSecretsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsMeasurementProtocolSecretsGetCall) Header ¶
func (c *PropertiesDataStreamsMeasurementProtocolSecretsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesDataStreamsMeasurementProtocolSecretsGetCall) IfNoneMatch ¶
func (c *PropertiesDataStreamsMeasurementProtocolSecretsGetCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsMeasurementProtocolSecretsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesDataStreamsMeasurementProtocolSecretsListCall ¶
type PropertiesDataStreamsMeasurementProtocolSecretsListCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsMeasurementProtocolSecretsListCall) Context ¶
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) Context(ctx context.Context) *PropertiesDataStreamsMeasurementProtocolSecretsListCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsMeasurementProtocolSecretsListCall) Do ¶
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponse, error)

Do executes the "analyticsadmin.properties.dataStreams.measurementProtocolSecrets.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponse.ServerRespo nse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsMeasurementProtocolSecretsListCall) Fields ¶
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsMeasurementProtocolSecretsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsMeasurementProtocolSecretsListCall) Header ¶
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesDataStreamsMeasurementProtocolSecretsListCall) IfNoneMatch ¶
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsMeasurementProtocolSecretsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesDataStreamsMeasurementProtocolSecretsListCall) PageSize ¶
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) PageSize(pageSize int64) *PropertiesDataStreamsMeasurementProtocolSecretsListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. If unspecified, at most 10 resources will be returned. The maximum value is 10. Higher values will be coerced to the maximum.

func (*PropertiesDataStreamsMeasurementProtocolSecretsListCall) PageToken ¶
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) PageToken(pageToken string) *PropertiesDataStreamsMeasurementProtocolSecretsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListMeasurementProtocolSecrets` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListMeasurementProtocolSecrets` must match the call that provided the page token.

func (*PropertiesDataStreamsMeasurementProtocolSecretsListCall) Pages ¶
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesDataStreamsMeasurementProtocolSecretsPatchCall ¶
type PropertiesDataStreamsMeasurementProtocolSecretsPatchCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsMeasurementProtocolSecretsPatchCall) Context ¶
func (c *PropertiesDataStreamsMeasurementProtocolSecretsPatchCall) Context(ctx context.Context) *PropertiesDataStreamsMeasurementProtocolSecretsPatchCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsMeasurementProtocolSecretsPatchCall) Do ¶
func (c *PropertiesDataStreamsMeasurementProtocolSecretsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaMeasurementProtocolSecret, error)

Do executes the "analyticsadmin.properties.dataStreams.measurementProtocolSecrets.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaMeasurementProtocolSecret.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsMeasurementProtocolSecretsPatchCall) Fields ¶
func (c *PropertiesDataStreamsMeasurementProtocolSecretsPatchCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsMeasurementProtocolSecretsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsMeasurementProtocolSecretsPatchCall) Header ¶
func (c *PropertiesDataStreamsMeasurementProtocolSecretsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesDataStreamsMeasurementProtocolSecretsPatchCall) UpdateMask ¶
func (c *PropertiesDataStreamsMeasurementProtocolSecretsPatchCall) UpdateMask(updateMask string) *PropertiesDataStreamsMeasurementProtocolSecretsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated. Omitted fields will not be updated.

type PropertiesDataStreamsMeasurementProtocolSecretsService ¶
type PropertiesDataStreamsMeasurementProtocolSecretsService struct {
	// contains filtered or unexported fields
}
func NewPropertiesDataStreamsMeasurementProtocolSecretsService ¶
func NewPropertiesDataStreamsMeasurementProtocolSecretsService(s *Service) *PropertiesDataStreamsMeasurementProtocolSecretsService
func (*PropertiesDataStreamsMeasurementProtocolSecretsService) Create ¶
func (r *PropertiesDataStreamsMeasurementProtocolSecretsService) Create(parent string, googleanalyticsadminv1betameasurementprotocolsecret *GoogleAnalyticsAdminV1betaMeasurementProtocolSecret) *PropertiesDataStreamsMeasurementProtocolSecretsCreateCall

Create: Creates a measurement protocol secret.

parent: The parent resource where this secret will be created. Format: properties/{property}/dataStreams/{dataStream}.
func (*PropertiesDataStreamsMeasurementProtocolSecretsService) Delete ¶
func (r *PropertiesDataStreamsMeasurementProtocolSecretsService) Delete(name string) *PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall

Delete: Deletes target MeasurementProtocolSecret.

name: The name of the MeasurementProtocolSecret to delete. Format: properties/{property}/dataStreams/{dataStream}/measurementProtocolSecrets/{ measurementProtocolSecret}.
func (*PropertiesDataStreamsMeasurementProtocolSecretsService) Get ¶
func (r *PropertiesDataStreamsMeasurementProtocolSecretsService) Get(name string) *PropertiesDataStreamsMeasurementProtocolSecretsGetCall

Get: Lookup for a single MeasurementProtocolSecret.

name: The name of the measurement protocol secret to lookup. Format: properties/{property}/dataStreams/{dataStream}/measurementProtocolSecrets/{ measurementProtocolSecret}.
func (*PropertiesDataStreamsMeasurementProtocolSecretsService) List ¶
func (r *PropertiesDataStreamsMeasurementProtocolSecretsService) List(parent string) *PropertiesDataStreamsMeasurementProtocolSecretsListCall

List: Returns child MeasurementProtocolSecrets under the specified parent Property.

parent: The resource name of the parent stream. Format: properties/{property}/dataStreams/{dataStream}/measurementProtocolSecrets.
func (*PropertiesDataStreamsMeasurementProtocolSecretsService) Patch ¶
func (r *PropertiesDataStreamsMeasurementProtocolSecretsService) Patch(name string, googleanalyticsadminv1betameasurementprotocolsecret *GoogleAnalyticsAdminV1betaMeasurementProtocolSecret) *PropertiesDataStreamsMeasurementProtocolSecretsPatchCall

Patch: Updates a measurement protocol secret.

name: Output only. Resource name of this secret. This secret may be a child of any type of stream. Format: properties/{property}/dataStreams/{dataStream}/measurementProtocolSecrets/{ measurementProtocolSecret}.
type PropertiesDataStreamsPatchCall ¶
type PropertiesDataStreamsPatchCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsPatchCall) Context ¶
func (c *PropertiesDataStreamsPatchCall) Context(ctx context.Context) *PropertiesDataStreamsPatchCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsPatchCall) Do ¶
func (c *PropertiesDataStreamsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaDataStream, error)

Do executes the "analyticsadmin.properties.dataStreams.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaDataStream.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsPatchCall) Fields ¶
func (c *PropertiesDataStreamsPatchCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsPatchCall) Header ¶
func (c *PropertiesDataStreamsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesDataStreamsPatchCall) UpdateMask ¶
func (c *PropertiesDataStreamsPatchCall) UpdateMask(updateMask string) *PropertiesDataStreamsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated. Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.

type PropertiesDataStreamsService ¶
type PropertiesDataStreamsService struct {
	MeasurementProtocolSecrets *PropertiesDataStreamsMeasurementProtocolSecretsService
	// contains filtered or unexported fields
}
func NewPropertiesDataStreamsService ¶
func NewPropertiesDataStreamsService(s *Service) *PropertiesDataStreamsService
func (*PropertiesDataStreamsService) Create ¶
func (r *PropertiesDataStreamsService) Create(parent string, googleanalyticsadminv1betadatastream *GoogleAnalyticsAdminV1betaDataStream) *PropertiesDataStreamsCreateCall

Create: Creates a DataStream.

- parent: Example format: properties/1234.

func (*PropertiesDataStreamsService) Delete ¶
func (r *PropertiesDataStreamsService) Delete(name string) *PropertiesDataStreamsDeleteCall

Delete: Deletes a DataStream on a property.

name: The name of the DataStream to delete. Example format: properties/1234/dataStreams/5678.
func (*PropertiesDataStreamsService) Get ¶
func (r *PropertiesDataStreamsService) Get(name string) *PropertiesDataStreamsGetCall

Get: Lookup for a single DataStream.

name: The name of the DataStream to get. Example format: properties/1234/dataStreams/5678.
func (*PropertiesDataStreamsService) List ¶
func (r *PropertiesDataStreamsService) List(parent string) *PropertiesDataStreamsListCall

List: Lists DataStreams on a property.

- parent: Example format: properties/1234.

func (*PropertiesDataStreamsService) Patch ¶
func (r *PropertiesDataStreamsService) Patch(name string, googleanalyticsadminv1betadatastream *GoogleAnalyticsAdminV1betaDataStream) *PropertiesDataStreamsPatchCall

Patch: Updates a DataStream on a property.

name: Output only. Resource name of this Data Stream. Format: properties/{property_id}/dataStreams/{stream_id} Example: "properties/1000/dataStreams/2000".
type PropertiesDeleteCall ¶
type PropertiesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDeleteCall) Context ¶
func (c *PropertiesDeleteCall) Context(ctx context.Context) *PropertiesDeleteCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDeleteCall) Do ¶
func (c *PropertiesDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaProperty, error)

Do executes the "analyticsadmin.properties.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaProperty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDeleteCall) Fields ¶
func (c *PropertiesDeleteCall) Fields(s ...googleapi.Field) *PropertiesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDeleteCall) Header ¶
func (c *PropertiesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesFirebaseLinksCreateCall ¶
type PropertiesFirebaseLinksCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesFirebaseLinksCreateCall) Context ¶
func (c *PropertiesFirebaseLinksCreateCall) Context(ctx context.Context) *PropertiesFirebaseLinksCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesFirebaseLinksCreateCall) Do ¶
func (c *PropertiesFirebaseLinksCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaFirebaseLink, error)

Do executes the "analyticsadmin.properties.firebaseLinks.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaFirebaseLink.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesFirebaseLinksCreateCall) Fields ¶
func (c *PropertiesFirebaseLinksCreateCall) Fields(s ...googleapi.Field) *PropertiesFirebaseLinksCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesFirebaseLinksCreateCall) Header ¶
func (c *PropertiesFirebaseLinksCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesFirebaseLinksDeleteCall ¶
type PropertiesFirebaseLinksDeleteCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesFirebaseLinksDeleteCall) Context ¶
func (c *PropertiesFirebaseLinksDeleteCall) Context(ctx context.Context) *PropertiesFirebaseLinksDeleteCall

Context sets the context to be used in this call's Do method.

func (*PropertiesFirebaseLinksDeleteCall) Do ¶
func (c *PropertiesFirebaseLinksDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.properties.firebaseLinks.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesFirebaseLinksDeleteCall) Fields ¶
func (c *PropertiesFirebaseLinksDeleteCall) Fields(s ...googleapi.Field) *PropertiesFirebaseLinksDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesFirebaseLinksDeleteCall) Header ¶
func (c *PropertiesFirebaseLinksDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesFirebaseLinksListCall ¶
type PropertiesFirebaseLinksListCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesFirebaseLinksListCall) Context ¶
func (c *PropertiesFirebaseLinksListCall) Context(ctx context.Context) *PropertiesFirebaseLinksListCall

Context sets the context to be used in this call's Do method.

func (*PropertiesFirebaseLinksListCall) Do ¶
func (c *PropertiesFirebaseLinksListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaListFirebaseLinksResponse, error)

Do executes the "analyticsadmin.properties.firebaseLinks.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaListFirebaseLinksResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesFirebaseLinksListCall) Fields ¶
func (c *PropertiesFirebaseLinksListCall) Fields(s ...googleapi.Field) *PropertiesFirebaseLinksListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesFirebaseLinksListCall) Header ¶
func (c *PropertiesFirebaseLinksListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesFirebaseLinksListCall) IfNoneMatch ¶
func (c *PropertiesFirebaseLinksListCall) IfNoneMatch(entityTag string) *PropertiesFirebaseLinksListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesFirebaseLinksListCall) PageSize ¶
func (c *PropertiesFirebaseLinksListCall) PageSize(pageSize int64) *PropertiesFirebaseLinksListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. The service may return fewer than this value, even if there are additional pages. If unspecified, at most 50 resources will be returned. The maximum value is 200; (higher values will be coerced to the maximum)

func (*PropertiesFirebaseLinksListCall) PageToken ¶
func (c *PropertiesFirebaseLinksListCall) PageToken(pageToken string) *PropertiesFirebaseLinksListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListFirebaseLinks` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListFirebaseLinks` must match the call that provided the page token.

func (*PropertiesFirebaseLinksListCall) Pages ¶
func (c *PropertiesFirebaseLinksListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1betaListFirebaseLinksResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesFirebaseLinksService ¶
type PropertiesFirebaseLinksService struct {
	// contains filtered or unexported fields
}
func NewPropertiesFirebaseLinksService ¶
func NewPropertiesFirebaseLinksService(s *Service) *PropertiesFirebaseLinksService
func (*PropertiesFirebaseLinksService) Create ¶
func (r *PropertiesFirebaseLinksService) Create(parent string, googleanalyticsadminv1betafirebaselink *GoogleAnalyticsAdminV1betaFirebaseLink) *PropertiesFirebaseLinksCreateCall

Create: Creates a FirebaseLink. Properties can have at most one FirebaseLink.

- parent: Format: properties/{property_id} Example: `properties/1234`.

func (*PropertiesFirebaseLinksService) Delete ¶
func (r *PropertiesFirebaseLinksService) Delete(name string) *PropertiesFirebaseLinksDeleteCall

Delete: Deletes a FirebaseLink on a property

name: Format: properties/{property_id}/firebaseLinks/{firebase_link_id} Example: `properties/1234/firebaseLinks/5678`.
func (*PropertiesFirebaseLinksService) List ¶
func (r *PropertiesFirebaseLinksService) List(parent string) *PropertiesFirebaseLinksListCall

List: Lists FirebaseLinks on a property. Properties can have at most one FirebaseLink.

- parent: Format: properties/{property_id} Example: `properties/1234`.

type PropertiesGetCall ¶
type PropertiesGetCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesGetCall) Context ¶
func (c *PropertiesGetCall) Context(ctx context.Context) *PropertiesGetCall

Context sets the context to be used in this call's Do method.

func (*PropertiesGetCall) Do ¶
func (c *PropertiesGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaProperty, error)

Do executes the "analyticsadmin.properties.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaProperty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesGetCall) Fields ¶
func (c *PropertiesGetCall) Fields(s ...googleapi.Field) *PropertiesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesGetCall) Header ¶
func (c *PropertiesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesGetCall) IfNoneMatch ¶
func (c *PropertiesGetCall) IfNoneMatch(entityTag string) *PropertiesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesGetDataRetentionSettingsCall ¶
type PropertiesGetDataRetentionSettingsCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesGetDataRetentionSettingsCall) Context ¶
func (c *PropertiesGetDataRetentionSettingsCall) Context(ctx context.Context) *PropertiesGetDataRetentionSettingsCall

Context sets the context to be used in this call's Do method.

func (*PropertiesGetDataRetentionSettingsCall) Do ¶
func (c *PropertiesGetDataRetentionSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaDataRetentionSettings, error)

Do executes the "analyticsadmin.properties.getDataRetentionSettings" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaDataRetentionSettings.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesGetDataRetentionSettingsCall) Fields ¶
func (c *PropertiesGetDataRetentionSettingsCall) Fields(s ...googleapi.Field) *PropertiesGetDataRetentionSettingsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesGetDataRetentionSettingsCall) Header ¶
func (c *PropertiesGetDataRetentionSettingsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesGetDataRetentionSettingsCall) IfNoneMatch ¶
func (c *PropertiesGetDataRetentionSettingsCall) IfNoneMatch(entityTag string) *PropertiesGetDataRetentionSettingsCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesGoogleAdsLinksCreateCall ¶
type PropertiesGoogleAdsLinksCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesGoogleAdsLinksCreateCall) Context ¶
func (c *PropertiesGoogleAdsLinksCreateCall) Context(ctx context.Context) *PropertiesGoogleAdsLinksCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesGoogleAdsLinksCreateCall) Do ¶
func (c *PropertiesGoogleAdsLinksCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaGoogleAdsLink, error)

Do executes the "analyticsadmin.properties.googleAdsLinks.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaGoogleAdsLink.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesGoogleAdsLinksCreateCall) Fields ¶
func (c *PropertiesGoogleAdsLinksCreateCall) Fields(s ...googleapi.Field) *PropertiesGoogleAdsLinksCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesGoogleAdsLinksCreateCall) Header ¶
func (c *PropertiesGoogleAdsLinksCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesGoogleAdsLinksDeleteCall ¶
type PropertiesGoogleAdsLinksDeleteCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesGoogleAdsLinksDeleteCall) Context ¶
func (c *PropertiesGoogleAdsLinksDeleteCall) Context(ctx context.Context) *PropertiesGoogleAdsLinksDeleteCall

Context sets the context to be used in this call's Do method.

func (*PropertiesGoogleAdsLinksDeleteCall) Do ¶
func (c *PropertiesGoogleAdsLinksDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.properties.googleAdsLinks.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesGoogleAdsLinksDeleteCall) Fields ¶
func (c *PropertiesGoogleAdsLinksDeleteCall) Fields(s ...googleapi.Field) *PropertiesGoogleAdsLinksDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesGoogleAdsLinksDeleteCall) Header ¶
func (c *PropertiesGoogleAdsLinksDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesGoogleAdsLinksListCall ¶
type PropertiesGoogleAdsLinksListCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesGoogleAdsLinksListCall) Context ¶
func (c *PropertiesGoogleAdsLinksListCall) Context(ctx context.Context) *PropertiesGoogleAdsLinksListCall

Context sets the context to be used in this call's Do method.

func (*PropertiesGoogleAdsLinksListCall) Do ¶
func (c *PropertiesGoogleAdsLinksListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponse, error)

Do executes the "analyticsadmin.properties.googleAdsLinks.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesGoogleAdsLinksListCall) Fields ¶
func (c *PropertiesGoogleAdsLinksListCall) Fields(s ...googleapi.Field) *PropertiesGoogleAdsLinksListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesGoogleAdsLinksListCall) Header ¶
func (c *PropertiesGoogleAdsLinksListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesGoogleAdsLinksListCall) IfNoneMatch ¶
func (c *PropertiesGoogleAdsLinksListCall) IfNoneMatch(entityTag string) *PropertiesGoogleAdsLinksListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesGoogleAdsLinksListCall) PageSize ¶
func (c *PropertiesGoogleAdsLinksListCall) PageSize(pageSize int64) *PropertiesGoogleAdsLinksListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. If unspecified, at most 50 resources will be returned. The maximum value is 200 (higher values will be coerced to the maximum).

func (*PropertiesGoogleAdsLinksListCall) PageToken ¶
func (c *PropertiesGoogleAdsLinksListCall) PageToken(pageToken string) *PropertiesGoogleAdsLinksListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListGoogleAdsLinks` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListGoogleAdsLinks` must match the call that provided the page token.

func (*PropertiesGoogleAdsLinksListCall) Pages ¶
func (c *PropertiesGoogleAdsLinksListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesGoogleAdsLinksPatchCall ¶
type PropertiesGoogleAdsLinksPatchCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesGoogleAdsLinksPatchCall) Context ¶
func (c *PropertiesGoogleAdsLinksPatchCall) Context(ctx context.Context) *PropertiesGoogleAdsLinksPatchCall

Context sets the context to be used in this call's Do method.

func (*PropertiesGoogleAdsLinksPatchCall) Do ¶
func (c *PropertiesGoogleAdsLinksPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaGoogleAdsLink, error)

Do executes the "analyticsadmin.properties.googleAdsLinks.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaGoogleAdsLink.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesGoogleAdsLinksPatchCall) Fields ¶
func (c *PropertiesGoogleAdsLinksPatchCall) Fields(s ...googleapi.Field) *PropertiesGoogleAdsLinksPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesGoogleAdsLinksPatchCall) Header ¶
func (c *PropertiesGoogleAdsLinksPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesGoogleAdsLinksPatchCall) UpdateMask ¶
func (c *PropertiesGoogleAdsLinksPatchCall) UpdateMask(updateMask string) *PropertiesGoogleAdsLinksPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated. Field names must be in snake case (e.g., "field_to_update"). Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.

type PropertiesGoogleAdsLinksService ¶
type PropertiesGoogleAdsLinksService struct {
	// contains filtered or unexported fields
}
func NewPropertiesGoogleAdsLinksService ¶
func NewPropertiesGoogleAdsLinksService(s *Service) *PropertiesGoogleAdsLinksService
func (*PropertiesGoogleAdsLinksService) Create ¶
func (r *PropertiesGoogleAdsLinksService) Create(parent string, googleanalyticsadminv1betagoogleadslink *GoogleAnalyticsAdminV1betaGoogleAdsLink) *PropertiesGoogleAdsLinksCreateCall

Create: Creates a GoogleAdsLink.

- parent: Example format: properties/1234.

func (*PropertiesGoogleAdsLinksService) Delete ¶
func (r *PropertiesGoogleAdsLinksService) Delete(name string) *PropertiesGoogleAdsLinksDeleteCall

Delete: Deletes a GoogleAdsLink on a property

- name: Example format: properties/1234/googleAdsLinks/5678.

func (*PropertiesGoogleAdsLinksService) List ¶
func (r *PropertiesGoogleAdsLinksService) List(parent string) *PropertiesGoogleAdsLinksListCall

List: Lists GoogleAdsLinks on a property.

- parent: Example format: properties/1234.

func (*PropertiesGoogleAdsLinksService) Patch ¶
func (r *PropertiesGoogleAdsLinksService) Patch(name string, googleanalyticsadminv1betagoogleadslink *GoogleAnalyticsAdminV1betaGoogleAdsLink) *PropertiesGoogleAdsLinksPatchCall

Patch: Updates a GoogleAdsLink on a property

name: Output only. Format: properties/{propertyId}/googleAdsLinks/{googleAdsLinkId} Note: googleAdsLinkId is not the Google Ads customer ID.
type PropertiesKeyEventsCreateCall ¶
added in v0.173.0
type PropertiesKeyEventsCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesKeyEventsCreateCall) Context ¶
added in v0.173.0
func (c *PropertiesKeyEventsCreateCall) Context(ctx context.Context) *PropertiesKeyEventsCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesKeyEventsCreateCall) Do ¶
added in v0.173.0
func (c *PropertiesKeyEventsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaKeyEvent, error)

Do executes the "analyticsadmin.properties.keyEvents.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaKeyEvent.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesKeyEventsCreateCall) Fields ¶
added in v0.173.0
func (c *PropertiesKeyEventsCreateCall) Fields(s ...googleapi.Field) *PropertiesKeyEventsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesKeyEventsCreateCall) Header ¶
added in v0.173.0
func (c *PropertiesKeyEventsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesKeyEventsDeleteCall ¶
added in v0.173.0
type PropertiesKeyEventsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesKeyEventsDeleteCall) Context ¶
added in v0.173.0
func (c *PropertiesKeyEventsDeleteCall) Context(ctx context.Context) *PropertiesKeyEventsDeleteCall

Context sets the context to be used in this call's Do method.

func (*PropertiesKeyEventsDeleteCall) Do ¶
added in v0.173.0
func (c *PropertiesKeyEventsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.properties.keyEvents.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesKeyEventsDeleteCall) Fields ¶
added in v0.173.0
func (c *PropertiesKeyEventsDeleteCall) Fields(s ...googleapi.Field) *PropertiesKeyEventsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesKeyEventsDeleteCall) Header ¶
added in v0.173.0
func (c *PropertiesKeyEventsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesKeyEventsGetCall ¶
added in v0.173.0
type PropertiesKeyEventsGetCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesKeyEventsGetCall) Context ¶
added in v0.173.0
func (c *PropertiesKeyEventsGetCall) Context(ctx context.Context) *PropertiesKeyEventsGetCall

Context sets the context to be used in this call's Do method.

func (*PropertiesKeyEventsGetCall) Do ¶
added in v0.173.0
func (c *PropertiesKeyEventsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaKeyEvent, error)

Do executes the "analyticsadmin.properties.keyEvents.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaKeyEvent.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesKeyEventsGetCall) Fields ¶
added in v0.173.0
func (c *PropertiesKeyEventsGetCall) Fields(s ...googleapi.Field) *PropertiesKeyEventsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesKeyEventsGetCall) Header ¶
added in v0.173.0
func (c *PropertiesKeyEventsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesKeyEventsGetCall) IfNoneMatch ¶
added in v0.173.0
func (c *PropertiesKeyEventsGetCall) IfNoneMatch(entityTag string) *PropertiesKeyEventsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesKeyEventsListCall ¶
added in v0.173.0
type PropertiesKeyEventsListCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesKeyEventsListCall) Context ¶
added in v0.173.0
func (c *PropertiesKeyEventsListCall) Context(ctx context.Context) *PropertiesKeyEventsListCall

Context sets the context to be used in this call's Do method.

func (*PropertiesKeyEventsListCall) Do ¶
added in v0.173.0
func (c *PropertiesKeyEventsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaListKeyEventsResponse, error)

Do executes the "analyticsadmin.properties.keyEvents.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaListKeyEventsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesKeyEventsListCall) Fields ¶
added in v0.173.0
func (c *PropertiesKeyEventsListCall) Fields(s ...googleapi.Field) *PropertiesKeyEventsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesKeyEventsListCall) Header ¶
added in v0.173.0
func (c *PropertiesKeyEventsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesKeyEventsListCall) IfNoneMatch ¶
added in v0.173.0
func (c *PropertiesKeyEventsListCall) IfNoneMatch(entityTag string) *PropertiesKeyEventsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesKeyEventsListCall) PageSize ¶
added in v0.173.0
func (c *PropertiesKeyEventsListCall) PageSize(pageSize int64) *PropertiesKeyEventsListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. If unspecified, at most 50 resources will be returned. The maximum value is 200; (higher values will be coerced to the maximum)

func (*PropertiesKeyEventsListCall) PageToken ¶
added in v0.173.0
func (c *PropertiesKeyEventsListCall) PageToken(pageToken string) *PropertiesKeyEventsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListKeyEvents` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListKeyEvents` must match the call that provided the page token.

func (*PropertiesKeyEventsListCall) Pages ¶
added in v0.173.0
func (c *PropertiesKeyEventsListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1betaListKeyEventsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesKeyEventsPatchCall ¶
added in v0.173.0
type PropertiesKeyEventsPatchCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesKeyEventsPatchCall) Context ¶
added in v0.173.0
func (c *PropertiesKeyEventsPatchCall) Context(ctx context.Context) *PropertiesKeyEventsPatchCall

Context sets the context to be used in this call's Do method.

func (*PropertiesKeyEventsPatchCall) Do ¶
added in v0.173.0
func (c *PropertiesKeyEventsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaKeyEvent, error)

Do executes the "analyticsadmin.properties.keyEvents.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaKeyEvent.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesKeyEventsPatchCall) Fields ¶
added in v0.173.0
func (c *PropertiesKeyEventsPatchCall) Fields(s ...googleapi.Field) *PropertiesKeyEventsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesKeyEventsPatchCall) Header ¶
added in v0.173.0
func (c *PropertiesKeyEventsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesKeyEventsPatchCall) UpdateMask ¶
added in v0.173.0
func (c *PropertiesKeyEventsPatchCall) UpdateMask(updateMask string) *PropertiesKeyEventsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated. Field names must be in snake case (e.g., "field_to_update"). Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.

type PropertiesKeyEventsService ¶
added in v0.173.0
type PropertiesKeyEventsService struct {
	// contains filtered or unexported fields
}
func NewPropertiesKeyEventsService ¶
added in v0.173.0
func NewPropertiesKeyEventsService(s *Service) *PropertiesKeyEventsService
func (*PropertiesKeyEventsService) Create ¶
added in v0.173.0
func (r *PropertiesKeyEventsService) Create(parent string, googleanalyticsadminv1betakeyevent *GoogleAnalyticsAdminV1betaKeyEvent) *PropertiesKeyEventsCreateCall

Create: Creates a Key Event.

parent: The resource name of the parent property where this Key Event will be created. Format: properties/123.
func (*PropertiesKeyEventsService) Delete ¶
added in v0.173.0
func (r *PropertiesKeyEventsService) Delete(name string) *PropertiesKeyEventsDeleteCall

Delete: Deletes a Key Event.

name: The resource name of the Key Event to delete. Format: properties/{property}/keyEvents/{key_event} Example: "properties/123/keyEvents/456".
func (*PropertiesKeyEventsService) Get ¶
added in v0.173.0
func (r *PropertiesKeyEventsService) Get(name string) *PropertiesKeyEventsGetCall

Get: Retrieve a single Key Event.

name: The resource name of the Key Event to retrieve. Format: properties/{property}/keyEvents/{key_event} Example: "properties/123/keyEvents/456".
func (*PropertiesKeyEventsService) List ¶
added in v0.173.0
func (r *PropertiesKeyEventsService) List(parent string) *PropertiesKeyEventsListCall

List: Returns a list of Key Events in the specified parent property. Returns an empty list if no Key Events are found.

parent: The resource name of the parent property. Example: 'properties/123'.
func (*PropertiesKeyEventsService) Patch ¶
added in v0.173.0
func (r *PropertiesKeyEventsService) Patch(name string, googleanalyticsadminv1betakeyevent *GoogleAnalyticsAdminV1betaKeyEvent) *PropertiesKeyEventsPatchCall

Patch: Updates a Key Event.

name: Output only. Resource name of this key event. Format: properties/{property}/keyEvents/{key_event}.
type PropertiesListCall ¶
type PropertiesListCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesListCall) Context ¶
func (c *PropertiesListCall) Context(ctx context.Context) *PropertiesListCall

Context sets the context to be used in this call's Do method.

func (*PropertiesListCall) Do ¶
func (c *PropertiesListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaListPropertiesResponse, error)

Do executes the "analyticsadmin.properties.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaListPropertiesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesListCall) Fields ¶
func (c *PropertiesListCall) Fields(s ...googleapi.Field) *PropertiesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesListCall) Filter ¶
func (c *PropertiesListCall) Filter(filter string) *PropertiesListCall

Filter sets the optional parameter "filter": Required. An expression for filtering the results of the request. Fields eligible for filtering are: `parent:`(The resource name of the parent account/property) or `ancestor:`(The resource name of the parent account) or `firebase_project:`(The id or number of the linked firebase project). Some examples of filters: ``` | Filter | Description | |-----------------------------|-------------------------------------------| | parent:accounts/123 | The account with account id: 123. | | parent:properties/123 | The property with property id: 123. | | ancestor:accounts/123 | The account with account id: 123. | | firebase_project:project-id | The firebase project with id: project-id. | | firebase_project:123 | The firebase project with number: 123. | ```

func (*PropertiesListCall) Header ¶
func (c *PropertiesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesListCall) IfNoneMatch ¶
func (c *PropertiesListCall) IfNoneMatch(entityTag string) *PropertiesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesListCall) PageSize ¶
func (c *PropertiesListCall) PageSize(pageSize int64) *PropertiesListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. The service may return fewer than this value, even if there are additional pages. If unspecified, at most 50 resources will be returned. The maximum value is 200; (higher values will be coerced to the maximum)

func (*PropertiesListCall) PageToken ¶
func (c *PropertiesListCall) PageToken(pageToken string) *PropertiesListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListProperties` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListProperties` must match the call that provided the page token.

func (*PropertiesListCall) Pages ¶
func (c *PropertiesListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1betaListPropertiesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*PropertiesListCall) ShowDeleted ¶
func (c *PropertiesListCall) ShowDeleted(showDeleted bool) *PropertiesListCall

ShowDeleted sets the optional parameter "showDeleted": Whether to include soft-deleted (ie: "trashed") Properties in the results. Properties can be inspected to determine whether they are deleted or not.

type PropertiesPatchCall ¶
type PropertiesPatchCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesPatchCall) Context ¶
func (c *PropertiesPatchCall) Context(ctx context.Context) *PropertiesPatchCall

Context sets the context to be used in this call's Do method.

func (*PropertiesPatchCall) Do ¶
func (c *PropertiesPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaProperty, error)

Do executes the "analyticsadmin.properties.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaProperty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesPatchCall) Fields ¶
func (c *PropertiesPatchCall) Fields(s ...googleapi.Field) *PropertiesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesPatchCall) Header ¶
func (c *PropertiesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesPatchCall) UpdateMask ¶
func (c *PropertiesPatchCall) UpdateMask(updateMask string) *PropertiesPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated. Field names must be in snake case (e.g., "field_to_update"). Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.

type PropertiesRunAccessReportCall ¶
added in v0.112.0
type PropertiesRunAccessReportCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesRunAccessReportCall) Context ¶
added in v0.112.0
func (c *PropertiesRunAccessReportCall) Context(ctx context.Context) *PropertiesRunAccessReportCall

Context sets the context to be used in this call's Do method.

func (*PropertiesRunAccessReportCall) Do ¶
added in v0.112.0
func (c *PropertiesRunAccessReportCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaRunAccessReportResponse, error)

Do executes the "analyticsadmin.properties.runAccessReport" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaRunAccessReportResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesRunAccessReportCall) Fields ¶
added in v0.112.0
func (c *PropertiesRunAccessReportCall) Fields(s ...googleapi.Field) *PropertiesRunAccessReportCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesRunAccessReportCall) Header ¶
added in v0.112.0
func (c *PropertiesRunAccessReportCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesService ¶
type PropertiesService struct {
	ConversionEvents *PropertiesConversionEventsService

	CustomDimensions *PropertiesCustomDimensionsService

	CustomMetrics *PropertiesCustomMetricsService

	DataStreams *PropertiesDataStreamsService

	FirebaseLinks *PropertiesFirebaseLinksService

	GoogleAdsLinks *PropertiesGoogleAdsLinksService

	KeyEvents *PropertiesKeyEventsService
	// contains filtered or unexported fields
}
func NewPropertiesService ¶
func NewPropertiesService(s *Service) *PropertiesService
func (*PropertiesService) AcknowledgeUserDataCollection ¶
func (r *PropertiesService) AcknowledgeUserDataCollection(property string, googleanalyticsadminv1betaacknowledgeuserdatacollectionrequest *GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionRequest) *PropertiesAcknowledgeUserDataCollectionCall

AcknowledgeUserDataCollection: Acknowledges the terms of user data collection for the specified property. This acknowledgement must be completed (either in the Google Analytics UI or through this API) before MeasurementProtocolSecret resources may be created.

- property: The property for which to acknowledge user data collection.

func (*PropertiesService) Create ¶
func (r *PropertiesService) Create(googleanalyticsadminv1betaproperty *GoogleAnalyticsAdminV1betaProperty) *PropertiesCreateCall

Create: Creates a Google Analytics property with the specified location and attributes.

func (*PropertiesService) Delete ¶
func (r *PropertiesService) Delete(name string) *PropertiesDeleteCall

Delete: Marks target Property as soft-deleted (ie: "trashed") and returns it. This API does not have a method to restore soft-deleted properties. However, they can be restored using the Trash Can UI. If the properties are not restored before the expiration time, the Property and all child resources (eg: GoogleAdsLinks, Streams, AccessBindings) will be permanently purged. https://support.google.com/analytics/answer/6154772 Returns an error if the target is not found.

name: The name of the Property to soft-delete. Format: properties/{property_id} Example: "properties/1000".
func (*PropertiesService) Get ¶
func (r *PropertiesService) Get(name string) *PropertiesGetCall

Get: Lookup for a single GA Property.

name: The name of the property to lookup. Format: properties/{property_id} Example: "properties/1000".
func (*PropertiesService) GetDataRetentionSettings ¶
func (r *PropertiesService) GetDataRetentionSettings(name string) *PropertiesGetDataRetentionSettingsCall

GetDataRetentionSettings: Returns the singleton data retention settings for this property.

name: The name of the settings to lookup. Format: properties/{property}/dataRetentionSettings Example: "properties/1000/dataRetentionSettings".
func (*PropertiesService) List ¶
func (r *PropertiesService) List() *PropertiesListCall

List: Returns child Properties under the specified parent Account. Properties will be excluded if the caller does not have access. Soft-deleted (ie: "trashed") properties are excluded by default. Returns an empty list if no relevant properties are found.

func (*PropertiesService) Patch ¶
func (r *PropertiesService) Patch(name string, googleanalyticsadminv1betaproperty *GoogleAnalyticsAdminV1betaProperty) *PropertiesPatchCall

Patch: Updates a property.

name: Output only. Resource name of this property. Format: properties/{property_id} Example: "properties/1000".
func (*PropertiesService) RunAccessReport ¶
added in v0.112.0
func (r *PropertiesService) RunAccessReport(entity string, googleanalyticsadminv1betarunaccessreportrequest *GoogleAnalyticsAdminV1betaRunAccessReportRequest) *PropertiesRunAccessReportCall

RunAccessReport: Returns a customized report of data access records. The report provides records of each time a user reads Google Analytics reporting data. Access records are retained for up to 2 years. Data Access Reports can be requested for a property. Reports may be requested for any property, but dimensions that aren't related to quota can only be requested on Google Analytics 360 properties. This method is only available to Administrators. These data access records include GA UI Reporting, GA UI Explorations, GA Data API, and other products like Firebase & Admob that can retrieve data from Google Analytics through a linkage. These records don't include property configuration changes like adding a stream or changing a property's time zone. For configuration change history, see searchChangeHistoryEvents (https://developers.google.com/analytics/devguides/config/admin/v1/rest/v1alpha/accounts/searchChangeHistoryEvents). To give your feedback on this API, complete the Google Analytics Access Reports feedback (https://docs.google.com/forms/d/e/1FAIpQLSdmEBUrMzAEdiEKk5TV5dEHvDUZDRlgWYdQdAeSdtR4hVjEhw/viewform) form.

entity: The Data Access Report supports requesting at the property level or account level. If requested at the account level, Data Access Reports include all access for all properties under that account. To request at the property level, entity should be for example 'properties/123' if "123" is your Google Analytics property ID. To request at the account level, entity should be for example 'accounts/1234' if "1234" is your Google Analytics Account ID.
func (*PropertiesService) UpdateDataRetentionSettings ¶
func (r *PropertiesService) UpdateDataRetentionSettings(name string, googleanalyticsadminv1betadataretentionsettings *GoogleAnalyticsAdminV1betaDataRetentionSettings) *PropertiesUpdateDataRetentionSettingsCall

UpdateDataRetentionSettings: Updates the singleton data retention settings for this property.

name: Output only. Resource name for this DataRetentionSetting resource. Format: properties/{property}/dataRetentionSettings.
type PropertiesUpdateDataRetentionSettingsCall ¶
type PropertiesUpdateDataRetentionSettingsCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesUpdateDataRetentionSettingsCall) Context ¶
func (c *PropertiesUpdateDataRetentionSettingsCall) Context(ctx context.Context) *PropertiesUpdateDataRetentionSettingsCall

Context sets the context to be used in this call's Do method.

func (*PropertiesUpdateDataRetentionSettingsCall) Do ¶
func (c *PropertiesUpdateDataRetentionSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1betaDataRetentionSettings, error)

Do executes the "analyticsadmin.properties.updateDataRetentionSettings" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1betaDataRetentionSettings.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesUpdateDataRetentionSettingsCall) Fields ¶
func (c *PropertiesUpdateDataRetentionSettingsCall) Fields(s ...googleapi.Field) *PropertiesUpdateDataRetentionSettingsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesUpdateDataRetentionSettingsCall) Header ¶
func (c *PropertiesUpdateDataRetentionSettingsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesUpdateDataRetentionSettingsCall) UpdateMask ¶
func (c *PropertiesUpdateDataRetentionSettingsCall) UpdateMask(updateMask string) *PropertiesUpdateDataRetentionSettingsCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated. Field names must be in snake case (e.g., "field_to_update"). Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.

type Service ¶
type Service struct {
	BasePath  string // API endpoint base URL
	UserAgent string // optional additional User-Agent fragment

	AccountSummaries *AccountSummariesService

	Accounts *AccountsService

	Properties *PropertiesService
	// contains filtered or unexported fields
}
func
New
DEPRECATED
func NewService ¶
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)

NewService creates a new Service.

 Source Files ¶
View all Source files
analyticsadmin-gen.go
Why Go
Use Cases
Case Studies
Get Started
Playground
Tour
Stack Overflow
Help
Packages
Standard Library
Sub-repositories
About Go Packages
About
Download
Blog
Issue Tracker
Release Notes
Brand Guidelines
Code of Conduct
Connect
Twitter
GitHub
Slack
r/golang
Meetup
Golang Weekly
Copyright
Terms of Service
Privacy Policy
Report an Issue

Theme Toggle

Shortcuts Modal
