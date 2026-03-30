# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsadmin/v1alpha

Title: analyticsadmin package - google.golang.org/api/analyticsadmin/v1alpha - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/analyticsadmin/v1alpha

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
 
v1alpha
analyticsadmin
package
Version: v0.269.0 Latest 
Published: Feb 24, 2026 
License: BSD-3-Clause 
Imports: 18 
Imported by: 0
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
Overview
Index
Constants
Variables
Functions
Types
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

import "google.golang.org/api/analyticsadmin/v1alpha"
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
func (c *AccountSummariesListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListAccountSummariesResponse, error)
func (c *AccountSummariesListCall) Fields(s ...googleapi.Field) *AccountSummariesListCall
func (c *AccountSummariesListCall) Header() http.Header
func (c *AccountSummariesListCall) IfNoneMatch(entityTag string) *AccountSummariesListCall
func (c *AccountSummariesListCall) PageSize(pageSize int64) *AccountSummariesListCall
func (c *AccountSummariesListCall) PageToken(pageToken string) *AccountSummariesListCall
func (c *AccountSummariesListCall) Pages(ctx context.Context, ...) error
type AccountSummariesService
func NewAccountSummariesService(s *Service) *AccountSummariesService
func (r *AccountSummariesService) List() *AccountSummariesListCall
type AccountsAccessBindingsBatchCreateCall
func (c *AccountsAccessBindingsBatchCreateCall) Context(ctx context.Context) *AccountsAccessBindingsBatchCreateCall
func (c *AccountsAccessBindingsBatchCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsResponse, error)
func (c *AccountsAccessBindingsBatchCreateCall) Fields(s ...googleapi.Field) *AccountsAccessBindingsBatchCreateCall
func (c *AccountsAccessBindingsBatchCreateCall) Header() http.Header
type AccountsAccessBindingsBatchDeleteCall
func (c *AccountsAccessBindingsBatchDeleteCall) Context(ctx context.Context) *AccountsAccessBindingsBatchDeleteCall
func (c *AccountsAccessBindingsBatchDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *AccountsAccessBindingsBatchDeleteCall) Fields(s ...googleapi.Field) *AccountsAccessBindingsBatchDeleteCall
func (c *AccountsAccessBindingsBatchDeleteCall) Header() http.Header
type AccountsAccessBindingsBatchGetCall
func (c *AccountsAccessBindingsBatchGetCall) Context(ctx context.Context) *AccountsAccessBindingsBatchGetCall
func (c *AccountsAccessBindingsBatchGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaBatchGetAccessBindingsResponse, error)
func (c *AccountsAccessBindingsBatchGetCall) Fields(s ...googleapi.Field) *AccountsAccessBindingsBatchGetCall
func (c *AccountsAccessBindingsBatchGetCall) Header() http.Header
func (c *AccountsAccessBindingsBatchGetCall) IfNoneMatch(entityTag string) *AccountsAccessBindingsBatchGetCall
func (c *AccountsAccessBindingsBatchGetCall) Names(names ...string) *AccountsAccessBindingsBatchGetCall
type AccountsAccessBindingsBatchUpdateCall
func (c *AccountsAccessBindingsBatchUpdateCall) Context(ctx context.Context) *AccountsAccessBindingsBatchUpdateCall
func (c *AccountsAccessBindingsBatchUpdateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsResponse, error)
func (c *AccountsAccessBindingsBatchUpdateCall) Fields(s ...googleapi.Field) *AccountsAccessBindingsBatchUpdateCall
func (c *AccountsAccessBindingsBatchUpdateCall) Header() http.Header
type AccountsAccessBindingsCreateCall
func (c *AccountsAccessBindingsCreateCall) Context(ctx context.Context) *AccountsAccessBindingsCreateCall
func (c *AccountsAccessBindingsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAccessBinding, error)
func (c *AccountsAccessBindingsCreateCall) Fields(s ...googleapi.Field) *AccountsAccessBindingsCreateCall
func (c *AccountsAccessBindingsCreateCall) Header() http.Header
type AccountsAccessBindingsDeleteCall
func (c *AccountsAccessBindingsDeleteCall) Context(ctx context.Context) *AccountsAccessBindingsDeleteCall
func (c *AccountsAccessBindingsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *AccountsAccessBindingsDeleteCall) Fields(s ...googleapi.Field) *AccountsAccessBindingsDeleteCall
func (c *AccountsAccessBindingsDeleteCall) Header() http.Header
type AccountsAccessBindingsGetCall
func (c *AccountsAccessBindingsGetCall) Context(ctx context.Context) *AccountsAccessBindingsGetCall
func (c *AccountsAccessBindingsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAccessBinding, error)
func (c *AccountsAccessBindingsGetCall) Fields(s ...googleapi.Field) *AccountsAccessBindingsGetCall
func (c *AccountsAccessBindingsGetCall) Header() http.Header
func (c *AccountsAccessBindingsGetCall) IfNoneMatch(entityTag string) *AccountsAccessBindingsGetCall
type AccountsAccessBindingsListCall
func (c *AccountsAccessBindingsListCall) Context(ctx context.Context) *AccountsAccessBindingsListCall
func (c *AccountsAccessBindingsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListAccessBindingsResponse, error)
func (c *AccountsAccessBindingsListCall) Fields(s ...googleapi.Field) *AccountsAccessBindingsListCall
func (c *AccountsAccessBindingsListCall) Header() http.Header
func (c *AccountsAccessBindingsListCall) IfNoneMatch(entityTag string) *AccountsAccessBindingsListCall
func (c *AccountsAccessBindingsListCall) PageSize(pageSize int64) *AccountsAccessBindingsListCall
func (c *AccountsAccessBindingsListCall) PageToken(pageToken string) *AccountsAccessBindingsListCall
func (c *AccountsAccessBindingsListCall) Pages(ctx context.Context, ...) error
type AccountsAccessBindingsPatchCall
func (c *AccountsAccessBindingsPatchCall) Context(ctx context.Context) *AccountsAccessBindingsPatchCall
func (c *AccountsAccessBindingsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAccessBinding, error)
func (c *AccountsAccessBindingsPatchCall) Fields(s ...googleapi.Field) *AccountsAccessBindingsPatchCall
func (c *AccountsAccessBindingsPatchCall) Header() http.Header
type AccountsAccessBindingsService
func NewAccountsAccessBindingsService(s *Service) *AccountsAccessBindingsService
func (r *AccountsAccessBindingsService) BatchCreate(parent string, ...) *AccountsAccessBindingsBatchCreateCall
func (r *AccountsAccessBindingsService) BatchDelete(parent string, ...) *AccountsAccessBindingsBatchDeleteCall
func (r *AccountsAccessBindingsService) BatchGet(parent string) *AccountsAccessBindingsBatchGetCall
func (r *AccountsAccessBindingsService) BatchUpdate(parent string, ...) *AccountsAccessBindingsBatchUpdateCall
func (r *AccountsAccessBindingsService) Create(parent string, ...) *AccountsAccessBindingsCreateCall
func (r *AccountsAccessBindingsService) Delete(name string) *AccountsAccessBindingsDeleteCall
func (r *AccountsAccessBindingsService) Get(name string) *AccountsAccessBindingsGetCall
func (r *AccountsAccessBindingsService) List(parent string) *AccountsAccessBindingsListCall
func (r *AccountsAccessBindingsService) Patch(name string, ...) *AccountsAccessBindingsPatchCall
type AccountsDeleteCall
func (c *AccountsDeleteCall) Context(ctx context.Context) *AccountsDeleteCall
func (c *AccountsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *AccountsDeleteCall) Fields(s ...googleapi.Field) *AccountsDeleteCall
func (c *AccountsDeleteCall) Header() http.Header
type AccountsGetCall
func (c *AccountsGetCall) Context(ctx context.Context) *AccountsGetCall
func (c *AccountsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAccount, error)
func (c *AccountsGetCall) Fields(s ...googleapi.Field) *AccountsGetCall
func (c *AccountsGetCall) Header() http.Header
func (c *AccountsGetCall) IfNoneMatch(entityTag string) *AccountsGetCall
type AccountsGetDataSharingSettingsCall
func (c *AccountsGetDataSharingSettingsCall) Context(ctx context.Context) *AccountsGetDataSharingSettingsCall
func (c *AccountsGetDataSharingSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaDataSharingSettings, error)
func (c *AccountsGetDataSharingSettingsCall) Fields(s ...googleapi.Field) *AccountsGetDataSharingSettingsCall
func (c *AccountsGetDataSharingSettingsCall) Header() http.Header
func (c *AccountsGetDataSharingSettingsCall) IfNoneMatch(entityTag string) *AccountsGetDataSharingSettingsCall
type AccountsListCall
func (c *AccountsListCall) Context(ctx context.Context) *AccountsListCall
func (c *AccountsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListAccountsResponse, error)
func (c *AccountsListCall) Fields(s ...googleapi.Field) *AccountsListCall
func (c *AccountsListCall) Header() http.Header
func (c *AccountsListCall) IfNoneMatch(entityTag string) *AccountsListCall
func (c *AccountsListCall) PageSize(pageSize int64) *AccountsListCall
func (c *AccountsListCall) PageToken(pageToken string) *AccountsListCall
func (c *AccountsListCall) Pages(ctx context.Context, ...) error
func (c *AccountsListCall) ShowDeleted(showDeleted bool) *AccountsListCall
type AccountsPatchCall
func (c *AccountsPatchCall) Context(ctx context.Context) *AccountsPatchCall
func (c *AccountsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAccount, error)
func (c *AccountsPatchCall) Fields(s ...googleapi.Field) *AccountsPatchCall
func (c *AccountsPatchCall) Header() http.Header
func (c *AccountsPatchCall) UpdateMask(updateMask string) *AccountsPatchCall
type AccountsProvisionAccountTicketCall
func (c *AccountsProvisionAccountTicketCall) Context(ctx context.Context) *AccountsProvisionAccountTicketCall
func (c *AccountsProvisionAccountTicketCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaProvisionAccountTicketResponse, error)
func (c *AccountsProvisionAccountTicketCall) Fields(s ...googleapi.Field) *AccountsProvisionAccountTicketCall
func (c *AccountsProvisionAccountTicketCall) Header() http.Header
type AccountsRunAccessReportCall
func (c *AccountsRunAccessReportCall) Context(ctx context.Context) *AccountsRunAccessReportCall
func (c *AccountsRunAccessReportCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaRunAccessReportResponse, error)
func (c *AccountsRunAccessReportCall) Fields(s ...googleapi.Field) *AccountsRunAccessReportCall
func (c *AccountsRunAccessReportCall) Header() http.Header
type AccountsSearchChangeHistoryEventsCall
func (c *AccountsSearchChangeHistoryEventsCall) Context(ctx context.Context) *AccountsSearchChangeHistoryEventsCall
func (c *AccountsSearchChangeHistoryEventsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsResponse, error)
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
type GoogleAnalyticsAdminV1alphaAccessBetweenFilter
func (s GoogleAnalyticsAdminV1alphaAccessBetweenFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessBinding
func (s GoogleAnalyticsAdminV1alphaAccessBinding) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessDateRange
func (s GoogleAnalyticsAdminV1alphaAccessDateRange) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessDimension
func (s GoogleAnalyticsAdminV1alphaAccessDimension) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessDimensionHeader
func (s GoogleAnalyticsAdminV1alphaAccessDimensionHeader) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessDimensionValue
func (s GoogleAnalyticsAdminV1alphaAccessDimensionValue) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessFilter
func (s GoogleAnalyticsAdminV1alphaAccessFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessFilterExpression
func (s GoogleAnalyticsAdminV1alphaAccessFilterExpression) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessFilterExpressionList
func (s GoogleAnalyticsAdminV1alphaAccessFilterExpressionList) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessInListFilter
func (s GoogleAnalyticsAdminV1alphaAccessInListFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessMetric
func (s GoogleAnalyticsAdminV1alphaAccessMetric) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessMetricHeader
func (s GoogleAnalyticsAdminV1alphaAccessMetricHeader) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessMetricValue
func (s GoogleAnalyticsAdminV1alphaAccessMetricValue) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessNumericFilter
func (s GoogleAnalyticsAdminV1alphaAccessNumericFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessOrderBy
func (s GoogleAnalyticsAdminV1alphaAccessOrderBy) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessOrderByDimensionOrderBy
func (s GoogleAnalyticsAdminV1alphaAccessOrderByDimensionOrderBy) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessOrderByMetricOrderBy
func (s GoogleAnalyticsAdminV1alphaAccessOrderByMetricOrderBy) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessQuota
func (s GoogleAnalyticsAdminV1alphaAccessQuota) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessQuotaStatus
func (s GoogleAnalyticsAdminV1alphaAccessQuotaStatus) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessRow
func (s GoogleAnalyticsAdminV1alphaAccessRow) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessStringFilter
func (s GoogleAnalyticsAdminV1alphaAccessStringFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccount
func (s GoogleAnalyticsAdminV1alphaAccount) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccountSummary
func (s GoogleAnalyticsAdminV1alphaAccountSummary) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAcknowledgeUserDataCollectionRequest
func (s GoogleAnalyticsAdminV1alphaAcknowledgeUserDataCollectionRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAcknowledgeUserDataCollectionResponse
type GoogleAnalyticsAdminV1alphaAdSenseLink
func (s GoogleAnalyticsAdminV1alphaAdSenseLink) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaApproveDisplayVideo360AdvertiserLinkProposalRequest
type GoogleAnalyticsAdminV1alphaApproveDisplayVideo360AdvertiserLinkProposalResponse
func (s GoogleAnalyticsAdminV1alphaApproveDisplayVideo360AdvertiserLinkProposalResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaArchiveAudienceRequest
type GoogleAnalyticsAdminV1alphaArchiveCustomDimensionRequest
type GoogleAnalyticsAdminV1alphaArchiveCustomMetricRequest
type GoogleAnalyticsAdminV1alphaAttributionSettings
func (s GoogleAnalyticsAdminV1alphaAttributionSettings) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAudience
func (s GoogleAnalyticsAdminV1alphaAudience) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilter
func (s GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterBetweenFilter
func (s GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterBetweenFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterInListFilter
func (s GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterInListFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericFilter
func (s GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericValue
func (s GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericValue) MarshalJSON() ([]byte, error)
func (s *GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericValue) UnmarshalJSON(data []byte) error
type GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterStringFilter
func (s GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterStringFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAudienceEventFilter
func (s GoogleAnalyticsAdminV1alphaAudienceEventFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAudienceEventTrigger
func (s GoogleAnalyticsAdminV1alphaAudienceEventTrigger) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAudienceFilterClause
func (s GoogleAnalyticsAdminV1alphaAudienceFilterClause) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAudienceFilterExpression
func (s GoogleAnalyticsAdminV1alphaAudienceFilterExpression) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAudienceFilterExpressionList
func (s GoogleAnalyticsAdminV1alphaAudienceFilterExpressionList) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAudienceSequenceFilter
func (s GoogleAnalyticsAdminV1alphaAudienceSequenceFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAudienceSequenceFilterAudienceSequenceStep
func (s GoogleAnalyticsAdminV1alphaAudienceSequenceFilterAudienceSequenceStep) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAudienceSimpleFilter
func (s GoogleAnalyticsAdminV1alphaAudienceSimpleFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsRequest
func (s GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsResponse
func (s GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaBatchDeleteAccessBindingsRequest
func (s GoogleAnalyticsAdminV1alphaBatchDeleteAccessBindingsRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaBatchGetAccessBindingsResponse
func (s GoogleAnalyticsAdminV1alphaBatchGetAccessBindingsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsRequest
func (s GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsResponse
func (s GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaBigQueryLink
func (s GoogleAnalyticsAdminV1alphaBigQueryLink) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaCalculatedMetric
func (s GoogleAnalyticsAdminV1alphaCalculatedMetric) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaCancelDisplayVideo360AdvertiserLinkProposalRequest
type GoogleAnalyticsAdminV1alphaChangeHistoryChange
func (s GoogleAnalyticsAdminV1alphaChangeHistoryChange) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaChangeHistoryChangeChangeHistoryResource
func (s GoogleAnalyticsAdminV1alphaChangeHistoryChangeChangeHistoryResource) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaChangeHistoryEvent
func (s GoogleAnalyticsAdminV1alphaChangeHistoryEvent) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaChannelGroup
func (s GoogleAnalyticsAdminV1alphaChannelGroup) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaChannelGroupFilter
func (s GoogleAnalyticsAdminV1alphaChannelGroupFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaChannelGroupFilterExpression
func (s GoogleAnalyticsAdminV1alphaChannelGroupFilterExpression) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaChannelGroupFilterExpressionList
func (s GoogleAnalyticsAdminV1alphaChannelGroupFilterExpressionList) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaChannelGroupFilterInListFilter
func (s GoogleAnalyticsAdminV1alphaChannelGroupFilterInListFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaChannelGroupFilterStringFilter
func (s GoogleAnalyticsAdminV1alphaChannelGroupFilterStringFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaConversionEvent
func (s GoogleAnalyticsAdminV1alphaConversionEvent) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaConversionEventDefaultConversionValue
func (s GoogleAnalyticsAdminV1alphaConversionEventDefaultConversionValue) MarshalJSON() ([]byte, error)
func (s *GoogleAnalyticsAdminV1alphaConversionEventDefaultConversionValue) UnmarshalJSON(data []byte) error
type GoogleAnalyticsAdminV1alphaConversionValues
func (s GoogleAnalyticsAdminV1alphaConversionValues) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaCreateAccessBindingRequest
func (s GoogleAnalyticsAdminV1alphaCreateAccessBindingRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaCreateRollupPropertyRequest
func (s GoogleAnalyticsAdminV1alphaCreateRollupPropertyRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaCreateRollupPropertyResponse
func (s GoogleAnalyticsAdminV1alphaCreateRollupPropertyResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaCustomDimension
func (s GoogleAnalyticsAdminV1alphaCustomDimension) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaCustomMetric
func (s GoogleAnalyticsAdminV1alphaCustomMetric) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaDataRedactionSettings
func (s GoogleAnalyticsAdminV1alphaDataRedactionSettings) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaDataRetentionSettings
func (s GoogleAnalyticsAdminV1alphaDataRetentionSettings) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaDataSharingSettings
func (s GoogleAnalyticsAdminV1alphaDataSharingSettings) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaDataStream
func (s GoogleAnalyticsAdminV1alphaDataStream) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaDataStreamAndroidAppStreamData
func (s GoogleAnalyticsAdminV1alphaDataStreamAndroidAppStreamData) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaDataStreamIosAppStreamData
func (s GoogleAnalyticsAdminV1alphaDataStreamIosAppStreamData) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaDataStreamWebStreamData
func (s GoogleAnalyticsAdminV1alphaDataStreamWebStreamData) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaDeleteAccessBindingRequest
func (s GoogleAnalyticsAdminV1alphaDeleteAccessBindingRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink
func (s GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal
func (s GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettings
func (s GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettings) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaEventCreateRule
func (s GoogleAnalyticsAdminV1alphaEventCreateRule) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaEventEditRule
func (s GoogleAnalyticsAdminV1alphaEventEditRule) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaEventMapping
func (s GoogleAnalyticsAdminV1alphaEventMapping) MarshalJSON() ([]byte, error)
func (s *GoogleAnalyticsAdminV1alphaEventMapping) UnmarshalJSON(data []byte) error
type GoogleAnalyticsAdminV1alphaExpandedDataSet
func (s GoogleAnalyticsAdminV1alphaExpandedDataSet) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaExpandedDataSetFilter
func (s GoogleAnalyticsAdminV1alphaExpandedDataSetFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaExpandedDataSetFilterExpression
func (s GoogleAnalyticsAdminV1alphaExpandedDataSetFilterExpression) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaExpandedDataSetFilterExpressionList
func (s GoogleAnalyticsAdminV1alphaExpandedDataSetFilterExpressionList) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaExpandedDataSetFilterInListFilter
func (s GoogleAnalyticsAdminV1alphaExpandedDataSetFilterInListFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaExpandedDataSetFilterStringFilter
func (s GoogleAnalyticsAdminV1alphaExpandedDataSetFilterStringFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaFirebaseLink
func (s GoogleAnalyticsAdminV1alphaFirebaseLink) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaGlobalSiteTag
func (s GoogleAnalyticsAdminV1alphaGlobalSiteTag) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaGoogleAdsLink
func (s GoogleAnalyticsAdminV1alphaGoogleAdsLink) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaGoogleSignalsSettings
func (s GoogleAnalyticsAdminV1alphaGoogleSignalsSettings) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaGroupingRule
func (s GoogleAnalyticsAdminV1alphaGroupingRule) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaKeyEvent
func (s GoogleAnalyticsAdminV1alphaKeyEvent) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaKeyEventDefaultValue
func (s GoogleAnalyticsAdminV1alphaKeyEventDefaultValue) MarshalJSON() ([]byte, error)
func (s *GoogleAnalyticsAdminV1alphaKeyEventDefaultValue) UnmarshalJSON(data []byte) error
type GoogleAnalyticsAdminV1alphaLinkProposalStatusDetails
func (s GoogleAnalyticsAdminV1alphaLinkProposalStatusDetails) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListAccessBindingsResponse
func (s GoogleAnalyticsAdminV1alphaListAccessBindingsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListAccountSummariesResponse
func (s GoogleAnalyticsAdminV1alphaListAccountSummariesResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListAccountsResponse
func (s GoogleAnalyticsAdminV1alphaListAccountsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListAdSenseLinksResponse
func (s GoogleAnalyticsAdminV1alphaListAdSenseLinksResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListAudiencesResponse
func (s GoogleAnalyticsAdminV1alphaListAudiencesResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListBigQueryLinksResponse
func (s GoogleAnalyticsAdminV1alphaListBigQueryLinksResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListCalculatedMetricsResponse
func (s GoogleAnalyticsAdminV1alphaListCalculatedMetricsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListChannelGroupsResponse
func (s GoogleAnalyticsAdminV1alphaListChannelGroupsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListConversionEventsResponse
func (s GoogleAnalyticsAdminV1alphaListConversionEventsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListCustomDimensionsResponse
func (s GoogleAnalyticsAdminV1alphaListCustomDimensionsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListCustomMetricsResponse
func (s GoogleAnalyticsAdminV1alphaListCustomMetricsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListDataStreamsResponse
func (s GoogleAnalyticsAdminV1alphaListDataStreamsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinkProposalsResponse
func (s GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinkProposalsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinksResponse
func (s GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinksResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListEventCreateRulesResponse
func (s GoogleAnalyticsAdminV1alphaListEventCreateRulesResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListEventEditRulesResponse
func (s GoogleAnalyticsAdminV1alphaListEventEditRulesResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListExpandedDataSetsResponse
func (s GoogleAnalyticsAdminV1alphaListExpandedDataSetsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListFirebaseLinksResponse
func (s GoogleAnalyticsAdminV1alphaListFirebaseLinksResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListGoogleAdsLinksResponse
func (s GoogleAnalyticsAdminV1alphaListGoogleAdsLinksResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListKeyEventsResponse
func (s GoogleAnalyticsAdminV1alphaListKeyEventsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListMeasurementProtocolSecretsResponse
func (s GoogleAnalyticsAdminV1alphaListMeasurementProtocolSecretsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListPropertiesResponse
func (s GoogleAnalyticsAdminV1alphaListPropertiesResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListReportingDataAnnotationsResponse
func (s GoogleAnalyticsAdminV1alphaListReportingDataAnnotationsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListRollupPropertySourceLinksResponse
func (s GoogleAnalyticsAdminV1alphaListRollupPropertySourceLinksResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListSKAdNetworkConversionValueSchemasResponse
func (s GoogleAnalyticsAdminV1alphaListSKAdNetworkConversionValueSchemasResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListSearchAds360LinksResponse
func (s GoogleAnalyticsAdminV1alphaListSearchAds360LinksResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListSubpropertyEventFiltersResponse
func (s GoogleAnalyticsAdminV1alphaListSubpropertyEventFiltersResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListSubpropertySyncConfigsResponse
func (s GoogleAnalyticsAdminV1alphaListSubpropertySyncConfigsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaMatchingCondition
func (s GoogleAnalyticsAdminV1alphaMatchingCondition) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret
func (s GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaNumericValue
func (s GoogleAnalyticsAdminV1alphaNumericValue) MarshalJSON() ([]byte, error)
func (s *GoogleAnalyticsAdminV1alphaNumericValue) UnmarshalJSON(data []byte) error
type GoogleAnalyticsAdminV1alphaParameterMutation
func (s GoogleAnalyticsAdminV1alphaParameterMutation) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaPostbackWindow
func (s GoogleAnalyticsAdminV1alphaPostbackWindow) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaProperty
func (s GoogleAnalyticsAdminV1alphaProperty) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaPropertySummary
func (s GoogleAnalyticsAdminV1alphaPropertySummary) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaProvisionAccountTicketRequest
func (s GoogleAnalyticsAdminV1alphaProvisionAccountTicketRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaProvisionAccountTicketResponse
func (s GoogleAnalyticsAdminV1alphaProvisionAccountTicketResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaProvisionSubpropertyRequest
func (s GoogleAnalyticsAdminV1alphaProvisionSubpropertyRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaProvisionSubpropertyResponse
func (s GoogleAnalyticsAdminV1alphaProvisionSubpropertyResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaReorderEventEditRulesRequest
func (s GoogleAnalyticsAdminV1alphaReorderEventEditRulesRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaReportingDataAnnotation
func (s GoogleAnalyticsAdminV1alphaReportingDataAnnotation) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaReportingDataAnnotationDateRange
func (s GoogleAnalyticsAdminV1alphaReportingDataAnnotationDateRange) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaReportingIdentitySettings
func (s GoogleAnalyticsAdminV1alphaReportingIdentitySettings) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaRollupPropertySourceLink
func (s GoogleAnalyticsAdminV1alphaRollupPropertySourceLink) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaRunAccessReportRequest
func (s GoogleAnalyticsAdminV1alphaRunAccessReportRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaRunAccessReportResponse
func (s GoogleAnalyticsAdminV1alphaRunAccessReportResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchema
func (s GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchema) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaSearchAds360Link
func (s GoogleAnalyticsAdminV1alphaSearchAds360Link) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsRequest
func (s GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsResponse
func (s GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaSubmitUserDeletionRequest
func (s GoogleAnalyticsAdminV1alphaSubmitUserDeletionRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaSubmitUserDeletionResponse
func (s GoogleAnalyticsAdminV1alphaSubmitUserDeletionResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaSubpropertyEventFilter
func (s GoogleAnalyticsAdminV1alphaSubpropertyEventFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaSubpropertyEventFilterClause
func (s GoogleAnalyticsAdminV1alphaSubpropertyEventFilterClause) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaSubpropertyEventFilterCondition
func (s GoogleAnalyticsAdminV1alphaSubpropertyEventFilterCondition) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaSubpropertyEventFilterConditionStringFilter
func (s GoogleAnalyticsAdminV1alphaSubpropertyEventFilterConditionStringFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaSubpropertyEventFilterExpression
func (s GoogleAnalyticsAdminV1alphaSubpropertyEventFilterExpression) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaSubpropertyEventFilterExpressionList
func (s GoogleAnalyticsAdminV1alphaSubpropertyEventFilterExpressionList) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaSubpropertySyncConfig
func (s GoogleAnalyticsAdminV1alphaSubpropertySyncConfig) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaUpdateAccessBindingRequest
func (s GoogleAnalyticsAdminV1alphaUpdateAccessBindingRequest) MarshalJSON() ([]byte, error)
type GoogleProtobufEmpty
type GoogleTypeDate
func (s GoogleTypeDate) MarshalJSON() ([]byte, error)
type PropertiesAccessBindingsBatchCreateCall
func (c *PropertiesAccessBindingsBatchCreateCall) Context(ctx context.Context) *PropertiesAccessBindingsBatchCreateCall
func (c *PropertiesAccessBindingsBatchCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsResponse, error)
func (c *PropertiesAccessBindingsBatchCreateCall) Fields(s ...googleapi.Field) *PropertiesAccessBindingsBatchCreateCall
func (c *PropertiesAccessBindingsBatchCreateCall) Header() http.Header
type PropertiesAccessBindingsBatchDeleteCall
func (c *PropertiesAccessBindingsBatchDeleteCall) Context(ctx context.Context) *PropertiesAccessBindingsBatchDeleteCall
func (c *PropertiesAccessBindingsBatchDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesAccessBindingsBatchDeleteCall) Fields(s ...googleapi.Field) *PropertiesAccessBindingsBatchDeleteCall
func (c *PropertiesAccessBindingsBatchDeleteCall) Header() http.Header
type PropertiesAccessBindingsBatchGetCall
func (c *PropertiesAccessBindingsBatchGetCall) Context(ctx context.Context) *PropertiesAccessBindingsBatchGetCall
func (c *PropertiesAccessBindingsBatchGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaBatchGetAccessBindingsResponse, error)
func (c *PropertiesAccessBindingsBatchGetCall) Fields(s ...googleapi.Field) *PropertiesAccessBindingsBatchGetCall
func (c *PropertiesAccessBindingsBatchGetCall) Header() http.Header
func (c *PropertiesAccessBindingsBatchGetCall) IfNoneMatch(entityTag string) *PropertiesAccessBindingsBatchGetCall
func (c *PropertiesAccessBindingsBatchGetCall) Names(names ...string) *PropertiesAccessBindingsBatchGetCall
type PropertiesAccessBindingsBatchUpdateCall
func (c *PropertiesAccessBindingsBatchUpdateCall) Context(ctx context.Context) *PropertiesAccessBindingsBatchUpdateCall
func (c *PropertiesAccessBindingsBatchUpdateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsResponse, error)
func (c *PropertiesAccessBindingsBatchUpdateCall) Fields(s ...googleapi.Field) *PropertiesAccessBindingsBatchUpdateCall
func (c *PropertiesAccessBindingsBatchUpdateCall) Header() http.Header
type PropertiesAccessBindingsCreateCall
func (c *PropertiesAccessBindingsCreateCall) Context(ctx context.Context) *PropertiesAccessBindingsCreateCall
func (c *PropertiesAccessBindingsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAccessBinding, error)
func (c *PropertiesAccessBindingsCreateCall) Fields(s ...googleapi.Field) *PropertiesAccessBindingsCreateCall
func (c *PropertiesAccessBindingsCreateCall) Header() http.Header
type PropertiesAccessBindingsDeleteCall
func (c *PropertiesAccessBindingsDeleteCall) Context(ctx context.Context) *PropertiesAccessBindingsDeleteCall
func (c *PropertiesAccessBindingsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesAccessBindingsDeleteCall) Fields(s ...googleapi.Field) *PropertiesAccessBindingsDeleteCall
func (c *PropertiesAccessBindingsDeleteCall) Header() http.Header
type PropertiesAccessBindingsGetCall
func (c *PropertiesAccessBindingsGetCall) Context(ctx context.Context) *PropertiesAccessBindingsGetCall
func (c *PropertiesAccessBindingsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAccessBinding, error)
func (c *PropertiesAccessBindingsGetCall) Fields(s ...googleapi.Field) *PropertiesAccessBindingsGetCall
func (c *PropertiesAccessBindingsGetCall) Header() http.Header
func (c *PropertiesAccessBindingsGetCall) IfNoneMatch(entityTag string) *PropertiesAccessBindingsGetCall
type PropertiesAccessBindingsListCall
func (c *PropertiesAccessBindingsListCall) Context(ctx context.Context) *PropertiesAccessBindingsListCall
func (c *PropertiesAccessBindingsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListAccessBindingsResponse, error)
func (c *PropertiesAccessBindingsListCall) Fields(s ...googleapi.Field) *PropertiesAccessBindingsListCall
func (c *PropertiesAccessBindingsListCall) Header() http.Header
func (c *PropertiesAccessBindingsListCall) IfNoneMatch(entityTag string) *PropertiesAccessBindingsListCall
func (c *PropertiesAccessBindingsListCall) PageSize(pageSize int64) *PropertiesAccessBindingsListCall
func (c *PropertiesAccessBindingsListCall) PageToken(pageToken string) *PropertiesAccessBindingsListCall
func (c *PropertiesAccessBindingsListCall) Pages(ctx context.Context, ...) error
type PropertiesAccessBindingsPatchCall
func (c *PropertiesAccessBindingsPatchCall) Context(ctx context.Context) *PropertiesAccessBindingsPatchCall
func (c *PropertiesAccessBindingsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAccessBinding, error)
func (c *PropertiesAccessBindingsPatchCall) Fields(s ...googleapi.Field) *PropertiesAccessBindingsPatchCall
func (c *PropertiesAccessBindingsPatchCall) Header() http.Header
type PropertiesAccessBindingsService
func NewPropertiesAccessBindingsService(s *Service) *PropertiesAccessBindingsService
func (r *PropertiesAccessBindingsService) BatchCreate(parent string, ...) *PropertiesAccessBindingsBatchCreateCall
func (r *PropertiesAccessBindingsService) BatchDelete(parent string, ...) *PropertiesAccessBindingsBatchDeleteCall
func (r *PropertiesAccessBindingsService) BatchGet(parent string) *PropertiesAccessBindingsBatchGetCall
func (r *PropertiesAccessBindingsService) BatchUpdate(parent string, ...) *PropertiesAccessBindingsBatchUpdateCall
func (r *PropertiesAccessBindingsService) Create(parent string, ...) *PropertiesAccessBindingsCreateCall
func (r *PropertiesAccessBindingsService) Delete(name string) *PropertiesAccessBindingsDeleteCall
func (r *PropertiesAccessBindingsService) Get(name string) *PropertiesAccessBindingsGetCall
func (r *PropertiesAccessBindingsService) List(parent string) *PropertiesAccessBindingsListCall
func (r *PropertiesAccessBindingsService) Patch(name string, ...) *PropertiesAccessBindingsPatchCall
type PropertiesAcknowledgeUserDataCollectionCall
func (c *PropertiesAcknowledgeUserDataCollectionCall) Context(ctx context.Context) *PropertiesAcknowledgeUserDataCollectionCall
func (c *PropertiesAcknowledgeUserDataCollectionCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAcknowledgeUserDataCollectionResponse, error)
func (c *PropertiesAcknowledgeUserDataCollectionCall) Fields(s ...googleapi.Field) *PropertiesAcknowledgeUserDataCollectionCall
func (c *PropertiesAcknowledgeUserDataCollectionCall) Header() http.Header
type PropertiesAdSenseLinksCreateCall
func (c *PropertiesAdSenseLinksCreateCall) Context(ctx context.Context) *PropertiesAdSenseLinksCreateCall
func (c *PropertiesAdSenseLinksCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAdSenseLink, error)
func (c *PropertiesAdSenseLinksCreateCall) Fields(s ...googleapi.Field) *PropertiesAdSenseLinksCreateCall
func (c *PropertiesAdSenseLinksCreateCall) Header() http.Header
type PropertiesAdSenseLinksDeleteCall
func (c *PropertiesAdSenseLinksDeleteCall) Context(ctx context.Context) *PropertiesAdSenseLinksDeleteCall
func (c *PropertiesAdSenseLinksDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesAdSenseLinksDeleteCall) Fields(s ...googleapi.Field) *PropertiesAdSenseLinksDeleteCall
func (c *PropertiesAdSenseLinksDeleteCall) Header() http.Header
type PropertiesAdSenseLinksGetCall
func (c *PropertiesAdSenseLinksGetCall) Context(ctx context.Context) *PropertiesAdSenseLinksGetCall
func (c *PropertiesAdSenseLinksGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAdSenseLink, error)
func (c *PropertiesAdSenseLinksGetCall) Fields(s ...googleapi.Field) *PropertiesAdSenseLinksGetCall
func (c *PropertiesAdSenseLinksGetCall) Header() http.Header
func (c *PropertiesAdSenseLinksGetCall) IfNoneMatch(entityTag string) *PropertiesAdSenseLinksGetCall
type PropertiesAdSenseLinksListCall
func (c *PropertiesAdSenseLinksListCall) Context(ctx context.Context) *PropertiesAdSenseLinksListCall
func (c *PropertiesAdSenseLinksListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListAdSenseLinksResponse, error)
func (c *PropertiesAdSenseLinksListCall) Fields(s ...googleapi.Field) *PropertiesAdSenseLinksListCall
func (c *PropertiesAdSenseLinksListCall) Header() http.Header
func (c *PropertiesAdSenseLinksListCall) IfNoneMatch(entityTag string) *PropertiesAdSenseLinksListCall
func (c *PropertiesAdSenseLinksListCall) PageSize(pageSize int64) *PropertiesAdSenseLinksListCall
func (c *PropertiesAdSenseLinksListCall) PageToken(pageToken string) *PropertiesAdSenseLinksListCall
func (c *PropertiesAdSenseLinksListCall) Pages(ctx context.Context, ...) error
type PropertiesAdSenseLinksService
func NewPropertiesAdSenseLinksService(s *Service) *PropertiesAdSenseLinksService
func (r *PropertiesAdSenseLinksService) Create(parent string, ...) *PropertiesAdSenseLinksCreateCall
func (r *PropertiesAdSenseLinksService) Delete(nameid string) *PropertiesAdSenseLinksDeleteCall
func (r *PropertiesAdSenseLinksService) Get(nameid string) *PropertiesAdSenseLinksGetCall
func (r *PropertiesAdSenseLinksService) List(parent string) *PropertiesAdSenseLinksListCall
type PropertiesAudiencesArchiveCall
func (c *PropertiesAudiencesArchiveCall) Context(ctx context.Context) *PropertiesAudiencesArchiveCall
func (c *PropertiesAudiencesArchiveCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesAudiencesArchiveCall) Fields(s ...googleapi.Field) *PropertiesAudiencesArchiveCall
func (c *PropertiesAudiencesArchiveCall) Header() http.Header
type PropertiesAudiencesCreateCall
func (c *PropertiesAudiencesCreateCall) Context(ctx context.Context) *PropertiesAudiencesCreateCall
func (c *PropertiesAudiencesCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAudience, error)
func (c *PropertiesAudiencesCreateCall) Fields(s ...googleapi.Field) *PropertiesAudiencesCreateCall
func (c *PropertiesAudiencesCreateCall) Header() http.Header
type PropertiesAudiencesGetCall
func (c *PropertiesAudiencesGetCall) Context(ctx context.Context) *PropertiesAudiencesGetCall
func (c *PropertiesAudiencesGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAudience, error)
func (c *PropertiesAudiencesGetCall) Fields(s ...googleapi.Field) *PropertiesAudiencesGetCall
func (c *PropertiesAudiencesGetCall) Header() http.Header
func (c *PropertiesAudiencesGetCall) IfNoneMatch(entityTag string) *PropertiesAudiencesGetCall
type PropertiesAudiencesListCall
func (c *PropertiesAudiencesListCall) Context(ctx context.Context) *PropertiesAudiencesListCall
func (c *PropertiesAudiencesListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListAudiencesResponse, error)
func (c *PropertiesAudiencesListCall) Fields(s ...googleapi.Field) *PropertiesAudiencesListCall
func (c *PropertiesAudiencesListCall) Header() http.Header
func (c *PropertiesAudiencesListCall) IfNoneMatch(entityTag string) *PropertiesAudiencesListCall
func (c *PropertiesAudiencesListCall) PageSize(pageSize int64) *PropertiesAudiencesListCall
func (c *PropertiesAudiencesListCall) PageToken(pageToken string) *PropertiesAudiencesListCall
func (c *PropertiesAudiencesListCall) Pages(ctx context.Context, ...) error
type PropertiesAudiencesPatchCall
func (c *PropertiesAudiencesPatchCall) Context(ctx context.Context) *PropertiesAudiencesPatchCall
func (c *PropertiesAudiencesPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAudience, error)
func (c *PropertiesAudiencesPatchCall) Fields(s ...googleapi.Field) *PropertiesAudiencesPatchCall
func (c *PropertiesAudiencesPatchCall) Header() http.Header
func (c *PropertiesAudiencesPatchCall) UpdateMask(updateMask string) *PropertiesAudiencesPatchCall
type PropertiesAudiencesService
func NewPropertiesAudiencesService(s *Service) *PropertiesAudiencesService
func (r *PropertiesAudiencesService) Archive(name string, ...) *PropertiesAudiencesArchiveCall
func (r *PropertiesAudiencesService) Create(parent string, ...) *PropertiesAudiencesCreateCall
func (r *PropertiesAudiencesService) Get(name string) *PropertiesAudiencesGetCall
func (r *PropertiesAudiencesService) List(parent string) *PropertiesAudiencesListCall
func (r *PropertiesAudiencesService) Patch(name string, ...) *PropertiesAudiencesPatchCall
type PropertiesBigQueryLinksCreateCall
func (c *PropertiesBigQueryLinksCreateCall) Context(ctx context.Context) *PropertiesBigQueryLinksCreateCall
func (c *PropertiesBigQueryLinksCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaBigQueryLink, error)
func (c *PropertiesBigQueryLinksCreateCall) Fields(s ...googleapi.Field) *PropertiesBigQueryLinksCreateCall
func (c *PropertiesBigQueryLinksCreateCall) Header() http.Header
type PropertiesBigQueryLinksDeleteCall
func (c *PropertiesBigQueryLinksDeleteCall) Context(ctx context.Context) *PropertiesBigQueryLinksDeleteCall
func (c *PropertiesBigQueryLinksDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesBigQueryLinksDeleteCall) Fields(s ...googleapi.Field) *PropertiesBigQueryLinksDeleteCall
func (c *PropertiesBigQueryLinksDeleteCall) Header() http.Header
type PropertiesBigQueryLinksGetCall
func (c *PropertiesBigQueryLinksGetCall) Context(ctx context.Context) *PropertiesBigQueryLinksGetCall
func (c *PropertiesBigQueryLinksGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaBigQueryLink, error)
func (c *PropertiesBigQueryLinksGetCall) Fields(s ...googleapi.Field) *PropertiesBigQueryLinksGetCall
func (c *PropertiesBigQueryLinksGetCall) Header() http.Header
func (c *PropertiesBigQueryLinksGetCall) IfNoneMatch(entityTag string) *PropertiesBigQueryLinksGetCall
type PropertiesBigQueryLinksListCall
func (c *PropertiesBigQueryLinksListCall) Context(ctx context.Context) *PropertiesBigQueryLinksListCall
func (c *PropertiesBigQueryLinksListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListBigQueryLinksResponse, error)
func (c *PropertiesBigQueryLinksListCall) Fields(s ...googleapi.Field) *PropertiesBigQueryLinksListCall
func (c *PropertiesBigQueryLinksListCall) Header() http.Header
func (c *PropertiesBigQueryLinksListCall) IfNoneMatch(entityTag string) *PropertiesBigQueryLinksListCall
func (c *PropertiesBigQueryLinksListCall) PageSize(pageSize int64) *PropertiesBigQueryLinksListCall
func (c *PropertiesBigQueryLinksListCall) PageToken(pageToken string) *PropertiesBigQueryLinksListCall
func (c *PropertiesBigQueryLinksListCall) Pages(ctx context.Context, ...) error
type PropertiesBigQueryLinksPatchCall
func (c *PropertiesBigQueryLinksPatchCall) Context(ctx context.Context) *PropertiesBigQueryLinksPatchCall
func (c *PropertiesBigQueryLinksPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaBigQueryLink, error)
func (c *PropertiesBigQueryLinksPatchCall) Fields(s ...googleapi.Field) *PropertiesBigQueryLinksPatchCall
func (c *PropertiesBigQueryLinksPatchCall) Header() http.Header
func (c *PropertiesBigQueryLinksPatchCall) UpdateMask(updateMask string) *PropertiesBigQueryLinksPatchCall
type PropertiesBigQueryLinksService
func NewPropertiesBigQueryLinksService(s *Service) *PropertiesBigQueryLinksService
func (r *PropertiesBigQueryLinksService) Create(parent string, ...) *PropertiesBigQueryLinksCreateCall
func (r *PropertiesBigQueryLinksService) Delete(name string) *PropertiesBigQueryLinksDeleteCall
func (r *PropertiesBigQueryLinksService) Get(name string) *PropertiesBigQueryLinksGetCall
func (r *PropertiesBigQueryLinksService) List(parent string) *PropertiesBigQueryLinksListCall
func (r *PropertiesBigQueryLinksService) Patch(name string, ...) *PropertiesBigQueryLinksPatchCall
type PropertiesCalculatedMetricsCreateCall
func (c *PropertiesCalculatedMetricsCreateCall) CalculatedMetricId(calculatedMetricId string) *PropertiesCalculatedMetricsCreateCall
func (c *PropertiesCalculatedMetricsCreateCall) Context(ctx context.Context) *PropertiesCalculatedMetricsCreateCall
func (c *PropertiesCalculatedMetricsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaCalculatedMetric, error)
func (c *PropertiesCalculatedMetricsCreateCall) Fields(s ...googleapi.Field) *PropertiesCalculatedMetricsCreateCall
func (c *PropertiesCalculatedMetricsCreateCall) Header() http.Header
type PropertiesCalculatedMetricsDeleteCall
func (c *PropertiesCalculatedMetricsDeleteCall) Context(ctx context.Context) *PropertiesCalculatedMetricsDeleteCall
func (c *PropertiesCalculatedMetricsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesCalculatedMetricsDeleteCall) Fields(s ...googleapi.Field) *PropertiesCalculatedMetricsDeleteCall
func (c *PropertiesCalculatedMetricsDeleteCall) Header() http.Header
type PropertiesCalculatedMetricsGetCall
func (c *PropertiesCalculatedMetricsGetCall) Context(ctx context.Context) *PropertiesCalculatedMetricsGetCall
func (c *PropertiesCalculatedMetricsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaCalculatedMetric, error)
func (c *PropertiesCalculatedMetricsGetCall) Fields(s ...googleapi.Field) *PropertiesCalculatedMetricsGetCall
func (c *PropertiesCalculatedMetricsGetCall) Header() http.Header
func (c *PropertiesCalculatedMetricsGetCall) IfNoneMatch(entityTag string) *PropertiesCalculatedMetricsGetCall
type PropertiesCalculatedMetricsListCall
func (c *PropertiesCalculatedMetricsListCall) Context(ctx context.Context) *PropertiesCalculatedMetricsListCall
func (c *PropertiesCalculatedMetricsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListCalculatedMetricsResponse, error)
func (c *PropertiesCalculatedMetricsListCall) Fields(s ...googleapi.Field) *PropertiesCalculatedMetricsListCall
func (c *PropertiesCalculatedMetricsListCall) Header() http.Header
func (c *PropertiesCalculatedMetricsListCall) IfNoneMatch(entityTag string) *PropertiesCalculatedMetricsListCall
func (c *PropertiesCalculatedMetricsListCall) PageSize(pageSize int64) *PropertiesCalculatedMetricsListCall
func (c *PropertiesCalculatedMetricsListCall) PageToken(pageToken string) *PropertiesCalculatedMetricsListCall
func (c *PropertiesCalculatedMetricsListCall) Pages(ctx context.Context, ...) error
type PropertiesCalculatedMetricsPatchCall
func (c *PropertiesCalculatedMetricsPatchCall) Context(ctx context.Context) *PropertiesCalculatedMetricsPatchCall
func (c *PropertiesCalculatedMetricsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaCalculatedMetric, error)
func (c *PropertiesCalculatedMetricsPatchCall) Fields(s ...googleapi.Field) *PropertiesCalculatedMetricsPatchCall
func (c *PropertiesCalculatedMetricsPatchCall) Header() http.Header
func (c *PropertiesCalculatedMetricsPatchCall) UpdateMask(updateMask string) *PropertiesCalculatedMetricsPatchCall
type PropertiesCalculatedMetricsService
func NewPropertiesCalculatedMetricsService(s *Service) *PropertiesCalculatedMetricsService
func (r *PropertiesCalculatedMetricsService) Create(parent string, ...) *PropertiesCalculatedMetricsCreateCall
func (r *PropertiesCalculatedMetricsService) Delete(name string) *PropertiesCalculatedMetricsDeleteCall
func (r *PropertiesCalculatedMetricsService) Get(name string) *PropertiesCalculatedMetricsGetCall
func (r *PropertiesCalculatedMetricsService) List(parent string) *PropertiesCalculatedMetricsListCall
func (r *PropertiesCalculatedMetricsService) Patch(name string, ...) *PropertiesCalculatedMetricsPatchCall
type PropertiesChannelGroupsCreateCall
func (c *PropertiesChannelGroupsCreateCall) Context(ctx context.Context) *PropertiesChannelGroupsCreateCall
func (c *PropertiesChannelGroupsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaChannelGroup, error)
func (c *PropertiesChannelGroupsCreateCall) Fields(s ...googleapi.Field) *PropertiesChannelGroupsCreateCall
func (c *PropertiesChannelGroupsCreateCall) Header() http.Header
type PropertiesChannelGroupsDeleteCall
func (c *PropertiesChannelGroupsDeleteCall) Context(ctx context.Context) *PropertiesChannelGroupsDeleteCall
func (c *PropertiesChannelGroupsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesChannelGroupsDeleteCall) Fields(s ...googleapi.Field) *PropertiesChannelGroupsDeleteCall
func (c *PropertiesChannelGroupsDeleteCall) Header() http.Header
type PropertiesChannelGroupsGetCall
func (c *PropertiesChannelGroupsGetCall) Context(ctx context.Context) *PropertiesChannelGroupsGetCall
func (c *PropertiesChannelGroupsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaChannelGroup, error)
func (c *PropertiesChannelGroupsGetCall) Fields(s ...googleapi.Field) *PropertiesChannelGroupsGetCall
func (c *PropertiesChannelGroupsGetCall) Header() http.Header
func (c *PropertiesChannelGroupsGetCall) IfNoneMatch(entityTag string) *PropertiesChannelGroupsGetCall
type PropertiesChannelGroupsListCall
func (c *PropertiesChannelGroupsListCall) Context(ctx context.Context) *PropertiesChannelGroupsListCall
func (c *PropertiesChannelGroupsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListChannelGroupsResponse, error)
func (c *PropertiesChannelGroupsListCall) Fields(s ...googleapi.Field) *PropertiesChannelGroupsListCall
func (c *PropertiesChannelGroupsListCall) Header() http.Header
func (c *PropertiesChannelGroupsListCall) IfNoneMatch(entityTag string) *PropertiesChannelGroupsListCall
func (c *PropertiesChannelGroupsListCall) PageSize(pageSize int64) *PropertiesChannelGroupsListCall
func (c *PropertiesChannelGroupsListCall) PageToken(pageToken string) *PropertiesChannelGroupsListCall
func (c *PropertiesChannelGroupsListCall) Pages(ctx context.Context, ...) error
type PropertiesChannelGroupsPatchCall
func (c *PropertiesChannelGroupsPatchCall) Context(ctx context.Context) *PropertiesChannelGroupsPatchCall
func (c *PropertiesChannelGroupsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaChannelGroup, error)
func (c *PropertiesChannelGroupsPatchCall) Fields(s ...googleapi.Field) *PropertiesChannelGroupsPatchCall
func (c *PropertiesChannelGroupsPatchCall) Header() http.Header
func (c *PropertiesChannelGroupsPatchCall) UpdateMask(updateMask string) *PropertiesChannelGroupsPatchCall
type PropertiesChannelGroupsService
func NewPropertiesChannelGroupsService(s *Service) *PropertiesChannelGroupsService
func (r *PropertiesChannelGroupsService) Create(parent string, ...) *PropertiesChannelGroupsCreateCall
func (r *PropertiesChannelGroupsService) Delete(name string) *PropertiesChannelGroupsDeleteCall
func (r *PropertiesChannelGroupsService) Get(name string) *PropertiesChannelGroupsGetCall
func (r *PropertiesChannelGroupsService) List(parent string) *PropertiesChannelGroupsListCall
func (r *PropertiesChannelGroupsService) Patch(name string, ...) *PropertiesChannelGroupsPatchCall
type PropertiesConversionEventsCreateCall
func (c *PropertiesConversionEventsCreateCall) Context(ctx context.Context) *PropertiesConversionEventsCreateCall
func (c *PropertiesConversionEventsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaConversionEvent, error)
func (c *PropertiesConversionEventsCreateCall) Fields(s ...googleapi.Field) *PropertiesConversionEventsCreateCall
func (c *PropertiesConversionEventsCreateCall) Header() http.Header
type PropertiesConversionEventsDeleteCall
func (c *PropertiesConversionEventsDeleteCall) Context(ctx context.Context) *PropertiesConversionEventsDeleteCall
func (c *PropertiesConversionEventsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesConversionEventsDeleteCall) Fields(s ...googleapi.Field) *PropertiesConversionEventsDeleteCall
func (c *PropertiesConversionEventsDeleteCall) Header() http.Header
type PropertiesConversionEventsGetCall
func (c *PropertiesConversionEventsGetCall) Context(ctx context.Context) *PropertiesConversionEventsGetCall
func (c *PropertiesConversionEventsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaConversionEvent, error)
func (c *PropertiesConversionEventsGetCall) Fields(s ...googleapi.Field) *PropertiesConversionEventsGetCall
func (c *PropertiesConversionEventsGetCall) Header() http.Header
func (c *PropertiesConversionEventsGetCall) IfNoneMatch(entityTag string) *PropertiesConversionEventsGetCall
type PropertiesConversionEventsListCall
func (c *PropertiesConversionEventsListCall) Context(ctx context.Context) *PropertiesConversionEventsListCall
func (c *PropertiesConversionEventsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListConversionEventsResponse, error)
func (c *PropertiesConversionEventsListCall) Fields(s ...googleapi.Field) *PropertiesConversionEventsListCall
func (c *PropertiesConversionEventsListCall) Header() http.Header
func (c *PropertiesConversionEventsListCall) IfNoneMatch(entityTag string) *PropertiesConversionEventsListCall
func (c *PropertiesConversionEventsListCall) PageSize(pageSize int64) *PropertiesConversionEventsListCall
func (c *PropertiesConversionEventsListCall) PageToken(pageToken string) *PropertiesConversionEventsListCall
func (c *PropertiesConversionEventsListCall) Pages(ctx context.Context, ...) error
type PropertiesConversionEventsPatchCall
func (c *PropertiesConversionEventsPatchCall) Context(ctx context.Context) *PropertiesConversionEventsPatchCall
func (c *PropertiesConversionEventsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaConversionEvent, error)
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
func (c *PropertiesCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaProperty, error)
func (c *PropertiesCreateCall) Fields(s ...googleapi.Field) *PropertiesCreateCall
func (c *PropertiesCreateCall) Header() http.Header
type PropertiesCreateRollupPropertyCall
func (c *PropertiesCreateRollupPropertyCall) Context(ctx context.Context) *PropertiesCreateRollupPropertyCall
func (c *PropertiesCreateRollupPropertyCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaCreateRollupPropertyResponse, error)
func (c *PropertiesCreateRollupPropertyCall) Fields(s ...googleapi.Field) *PropertiesCreateRollupPropertyCall
func (c *PropertiesCreateRollupPropertyCall) Header() http.Header
type PropertiesCustomDimensionsArchiveCall
func (c *PropertiesCustomDimensionsArchiveCall) Context(ctx context.Context) *PropertiesCustomDimensionsArchiveCall
func (c *PropertiesCustomDimensionsArchiveCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesCustomDimensionsArchiveCall) Fields(s ...googleapi.Field) *PropertiesCustomDimensionsArchiveCall
func (c *PropertiesCustomDimensionsArchiveCall) Header() http.Header
type PropertiesCustomDimensionsCreateCall
func (c *PropertiesCustomDimensionsCreateCall) Context(ctx context.Context) *PropertiesCustomDimensionsCreateCall
func (c *PropertiesCustomDimensionsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaCustomDimension, error)
func (c *PropertiesCustomDimensionsCreateCall) Fields(s ...googleapi.Field) *PropertiesCustomDimensionsCreateCall
func (c *PropertiesCustomDimensionsCreateCall) Header() http.Header
type PropertiesCustomDimensionsGetCall
func (c *PropertiesCustomDimensionsGetCall) Context(ctx context.Context) *PropertiesCustomDimensionsGetCall
func (c *PropertiesCustomDimensionsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaCustomDimension, error)
func (c *PropertiesCustomDimensionsGetCall) Fields(s ...googleapi.Field) *PropertiesCustomDimensionsGetCall
func (c *PropertiesCustomDimensionsGetCall) Header() http.Header
func (c *PropertiesCustomDimensionsGetCall) IfNoneMatch(entityTag string) *PropertiesCustomDimensionsGetCall
type PropertiesCustomDimensionsListCall
func (c *PropertiesCustomDimensionsListCall) Context(ctx context.Context) *PropertiesCustomDimensionsListCall
func (c *PropertiesCustomDimensionsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListCustomDimensionsResponse, error)
func (c *PropertiesCustomDimensionsListCall) Fields(s ...googleapi.Field) *PropertiesCustomDimensionsListCall
func (c *PropertiesCustomDimensionsListCall) Header() http.Header
func (c *PropertiesCustomDimensionsListCall) IfNoneMatch(entityTag string) *PropertiesCustomDimensionsListCall
func (c *PropertiesCustomDimensionsListCall) PageSize(pageSize int64) *PropertiesCustomDimensionsListCall
func (c *PropertiesCustomDimensionsListCall) PageToken(pageToken string) *PropertiesCustomDimensionsListCall
func (c *PropertiesCustomDimensionsListCall) Pages(ctx context.Context, ...) error
type PropertiesCustomDimensionsPatchCall
func (c *PropertiesCustomDimensionsPatchCall) Context(ctx context.Context) *PropertiesCustomDimensionsPatchCall
func (c *PropertiesCustomDimensionsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaCustomDimension, error)
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
func (c *PropertiesCustomMetricsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaCustomMetric, error)
func (c *PropertiesCustomMetricsCreateCall) Fields(s ...googleapi.Field) *PropertiesCustomMetricsCreateCall
func (c *PropertiesCustomMetricsCreateCall) Header() http.Header
type PropertiesCustomMetricsGetCall
func (c *PropertiesCustomMetricsGetCall) Context(ctx context.Context) *PropertiesCustomMetricsGetCall
func (c *PropertiesCustomMetricsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaCustomMetric, error)
func (c *PropertiesCustomMetricsGetCall) Fields(s ...googleapi.Field) *PropertiesCustomMetricsGetCall
func (c *PropertiesCustomMetricsGetCall) Header() http.Header
func (c *PropertiesCustomMetricsGetCall) IfNoneMatch(entityTag string) *PropertiesCustomMetricsGetCall
type PropertiesCustomMetricsListCall
func (c *PropertiesCustomMetricsListCall) Context(ctx context.Context) *PropertiesCustomMetricsListCall
func (c *PropertiesCustomMetricsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListCustomMetricsResponse, error)
func (c *PropertiesCustomMetricsListCall) Fields(s ...googleapi.Field) *PropertiesCustomMetricsListCall
func (c *PropertiesCustomMetricsListCall) Header() http.Header
func (c *PropertiesCustomMetricsListCall) IfNoneMatch(entityTag string) *PropertiesCustomMetricsListCall
func (c *PropertiesCustomMetricsListCall) PageSize(pageSize int64) *PropertiesCustomMetricsListCall
func (c *PropertiesCustomMetricsListCall) PageToken(pageToken string) *PropertiesCustomMetricsListCall
func (c *PropertiesCustomMetricsListCall) Pages(ctx context.Context, ...) error
type PropertiesCustomMetricsPatchCall
func (c *PropertiesCustomMetricsPatchCall) Context(ctx context.Context) *PropertiesCustomMetricsPatchCall
func (c *PropertiesCustomMetricsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaCustomMetric, error)
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
func (c *PropertiesDataStreamsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaDataStream, error)
func (c *PropertiesDataStreamsCreateCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsCreateCall
func (c *PropertiesDataStreamsCreateCall) Header() http.Header
type PropertiesDataStreamsDeleteCall
func (c *PropertiesDataStreamsDeleteCall) Context(ctx context.Context) *PropertiesDataStreamsDeleteCall
func (c *PropertiesDataStreamsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesDataStreamsDeleteCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsDeleteCall
func (c *PropertiesDataStreamsDeleteCall) Header() http.Header
type PropertiesDataStreamsEventCreateRulesCreateCall
func (c *PropertiesDataStreamsEventCreateRulesCreateCall) Context(ctx context.Context) *PropertiesDataStreamsEventCreateRulesCreateCall
func (c *PropertiesDataStreamsEventCreateRulesCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaEventCreateRule, error)
func (c *PropertiesDataStreamsEventCreateRulesCreateCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsEventCreateRulesCreateCall
func (c *PropertiesDataStreamsEventCreateRulesCreateCall) Header() http.Header
type PropertiesDataStreamsEventCreateRulesDeleteCall
func (c *PropertiesDataStreamsEventCreateRulesDeleteCall) Context(ctx context.Context) *PropertiesDataStreamsEventCreateRulesDeleteCall
func (c *PropertiesDataStreamsEventCreateRulesDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesDataStreamsEventCreateRulesDeleteCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsEventCreateRulesDeleteCall
func (c *PropertiesDataStreamsEventCreateRulesDeleteCall) Header() http.Header
type PropertiesDataStreamsEventCreateRulesGetCall
func (c *PropertiesDataStreamsEventCreateRulesGetCall) Context(ctx context.Context) *PropertiesDataStreamsEventCreateRulesGetCall
func (c *PropertiesDataStreamsEventCreateRulesGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaEventCreateRule, error)
func (c *PropertiesDataStreamsEventCreateRulesGetCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsEventCreateRulesGetCall
func (c *PropertiesDataStreamsEventCreateRulesGetCall) Header() http.Header
func (c *PropertiesDataStreamsEventCreateRulesGetCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsEventCreateRulesGetCall
type PropertiesDataStreamsEventCreateRulesListCall
func (c *PropertiesDataStreamsEventCreateRulesListCall) Context(ctx context.Context) *PropertiesDataStreamsEventCreateRulesListCall
func (c *PropertiesDataStreamsEventCreateRulesListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListEventCreateRulesResponse, error)
func (c *PropertiesDataStreamsEventCreateRulesListCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsEventCreateRulesListCall
func (c *PropertiesDataStreamsEventCreateRulesListCall) Header() http.Header
func (c *PropertiesDataStreamsEventCreateRulesListCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsEventCreateRulesListCall
func (c *PropertiesDataStreamsEventCreateRulesListCall) PageSize(pageSize int64) *PropertiesDataStreamsEventCreateRulesListCall
func (c *PropertiesDataStreamsEventCreateRulesListCall) PageToken(pageToken string) *PropertiesDataStreamsEventCreateRulesListCall
func (c *PropertiesDataStreamsEventCreateRulesListCall) Pages(ctx context.Context, ...) error
type PropertiesDataStreamsEventCreateRulesPatchCall
func (c *PropertiesDataStreamsEventCreateRulesPatchCall) Context(ctx context.Context) *PropertiesDataStreamsEventCreateRulesPatchCall
func (c *PropertiesDataStreamsEventCreateRulesPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaEventCreateRule, error)
func (c *PropertiesDataStreamsEventCreateRulesPatchCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsEventCreateRulesPatchCall
func (c *PropertiesDataStreamsEventCreateRulesPatchCall) Header() http.Header
func (c *PropertiesDataStreamsEventCreateRulesPatchCall) UpdateMask(updateMask string) *PropertiesDataStreamsEventCreateRulesPatchCall
type PropertiesDataStreamsEventCreateRulesService
func NewPropertiesDataStreamsEventCreateRulesService(s *Service) *PropertiesDataStreamsEventCreateRulesService
func (r *PropertiesDataStreamsEventCreateRulesService) Create(parent string, ...) *PropertiesDataStreamsEventCreateRulesCreateCall
func (r *PropertiesDataStreamsEventCreateRulesService) Delete(name string) *PropertiesDataStreamsEventCreateRulesDeleteCall
func (r *PropertiesDataStreamsEventCreateRulesService) Get(name string) *PropertiesDataStreamsEventCreateRulesGetCall
func (r *PropertiesDataStreamsEventCreateRulesService) List(parent string) *PropertiesDataStreamsEventCreateRulesListCall
func (r *PropertiesDataStreamsEventCreateRulesService) Patch(name string, ...) *PropertiesDataStreamsEventCreateRulesPatchCall
type PropertiesDataStreamsEventEditRulesCreateCall
func (c *PropertiesDataStreamsEventEditRulesCreateCall) Context(ctx context.Context) *PropertiesDataStreamsEventEditRulesCreateCall
func (c *PropertiesDataStreamsEventEditRulesCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaEventEditRule, error)
func (c *PropertiesDataStreamsEventEditRulesCreateCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsEventEditRulesCreateCall
func (c *PropertiesDataStreamsEventEditRulesCreateCall) Header() http.Header
type PropertiesDataStreamsEventEditRulesDeleteCall
func (c *PropertiesDataStreamsEventEditRulesDeleteCall) Context(ctx context.Context) *PropertiesDataStreamsEventEditRulesDeleteCall
func (c *PropertiesDataStreamsEventEditRulesDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesDataStreamsEventEditRulesDeleteCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsEventEditRulesDeleteCall
func (c *PropertiesDataStreamsEventEditRulesDeleteCall) Header() http.Header
type PropertiesDataStreamsEventEditRulesGetCall
func (c *PropertiesDataStreamsEventEditRulesGetCall) Context(ctx context.Context) *PropertiesDataStreamsEventEditRulesGetCall
func (c *PropertiesDataStreamsEventEditRulesGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaEventEditRule, error)
func (c *PropertiesDataStreamsEventEditRulesGetCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsEventEditRulesGetCall
func (c *PropertiesDataStreamsEventEditRulesGetCall) Header() http.Header
func (c *PropertiesDataStreamsEventEditRulesGetCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsEventEditRulesGetCall
type PropertiesDataStreamsEventEditRulesListCall
func (c *PropertiesDataStreamsEventEditRulesListCall) Context(ctx context.Context) *PropertiesDataStreamsEventEditRulesListCall
func (c *PropertiesDataStreamsEventEditRulesListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListEventEditRulesResponse, error)
func (c *PropertiesDataStreamsEventEditRulesListCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsEventEditRulesListCall
func (c *PropertiesDataStreamsEventEditRulesListCall) Header() http.Header
func (c *PropertiesDataStreamsEventEditRulesListCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsEventEditRulesListCall
func (c *PropertiesDataStreamsEventEditRulesListCall) PageSize(pageSize int64) *PropertiesDataStreamsEventEditRulesListCall
func (c *PropertiesDataStreamsEventEditRulesListCall) PageToken(pageToken string) *PropertiesDataStreamsEventEditRulesListCall
func (c *PropertiesDataStreamsEventEditRulesListCall) Pages(ctx context.Context, ...) error
type PropertiesDataStreamsEventEditRulesPatchCall
func (c *PropertiesDataStreamsEventEditRulesPatchCall) Context(ctx context.Context) *PropertiesDataStreamsEventEditRulesPatchCall
func (c *PropertiesDataStreamsEventEditRulesPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaEventEditRule, error)
func (c *PropertiesDataStreamsEventEditRulesPatchCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsEventEditRulesPatchCall
func (c *PropertiesDataStreamsEventEditRulesPatchCall) Header() http.Header
func (c *PropertiesDataStreamsEventEditRulesPatchCall) UpdateMask(updateMask string) *PropertiesDataStreamsEventEditRulesPatchCall
type PropertiesDataStreamsEventEditRulesReorderCall
func (c *PropertiesDataStreamsEventEditRulesReorderCall) Context(ctx context.Context) *PropertiesDataStreamsEventEditRulesReorderCall
func (c *PropertiesDataStreamsEventEditRulesReorderCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesDataStreamsEventEditRulesReorderCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsEventEditRulesReorderCall
func (c *PropertiesDataStreamsEventEditRulesReorderCall) Header() http.Header
type PropertiesDataStreamsEventEditRulesService
func NewPropertiesDataStreamsEventEditRulesService(s *Service) *PropertiesDataStreamsEventEditRulesService
func (r *PropertiesDataStreamsEventEditRulesService) Create(parent string, ...) *PropertiesDataStreamsEventEditRulesCreateCall
func (r *PropertiesDataStreamsEventEditRulesService) Delete(name string) *PropertiesDataStreamsEventEditRulesDeleteCall
func (r *PropertiesDataStreamsEventEditRulesService) Get(name string) *PropertiesDataStreamsEventEditRulesGetCall
func (r *PropertiesDataStreamsEventEditRulesService) List(parent string) *PropertiesDataStreamsEventEditRulesListCall
func (r *PropertiesDataStreamsEventEditRulesService) Patch(name string, ...) *PropertiesDataStreamsEventEditRulesPatchCall
func (r *PropertiesDataStreamsEventEditRulesService) Reorder(parent string, ...) *PropertiesDataStreamsEventEditRulesReorderCall
type PropertiesDataStreamsGetCall
func (c *PropertiesDataStreamsGetCall) Context(ctx context.Context) *PropertiesDataStreamsGetCall
func (c *PropertiesDataStreamsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaDataStream, error)
func (c *PropertiesDataStreamsGetCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsGetCall
func (c *PropertiesDataStreamsGetCall) Header() http.Header
func (c *PropertiesDataStreamsGetCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsGetCall
type PropertiesDataStreamsGetDataRedactionSettingsCall
func (c *PropertiesDataStreamsGetDataRedactionSettingsCall) Context(ctx context.Context) *PropertiesDataStreamsGetDataRedactionSettingsCall
func (c *PropertiesDataStreamsGetDataRedactionSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaDataRedactionSettings, error)
func (c *PropertiesDataStreamsGetDataRedactionSettingsCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsGetDataRedactionSettingsCall
func (c *PropertiesDataStreamsGetDataRedactionSettingsCall) Header() http.Header
func (c *PropertiesDataStreamsGetDataRedactionSettingsCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsGetDataRedactionSettingsCall
type PropertiesDataStreamsGetEnhancedMeasurementSettingsCall
func (c *PropertiesDataStreamsGetEnhancedMeasurementSettingsCall) Context(ctx context.Context) *PropertiesDataStreamsGetEnhancedMeasurementSettingsCall
func (c *PropertiesDataStreamsGetEnhancedMeasurementSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettings, error)
func (c *PropertiesDataStreamsGetEnhancedMeasurementSettingsCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsGetEnhancedMeasurementSettingsCall
func (c *PropertiesDataStreamsGetEnhancedMeasurementSettingsCall) Header() http.Header
func (c *PropertiesDataStreamsGetEnhancedMeasurementSettingsCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsGetEnhancedMeasurementSettingsCall
type PropertiesDataStreamsGetGlobalSiteTagCall
func (c *PropertiesDataStreamsGetGlobalSiteTagCall) Context(ctx context.Context) *PropertiesDataStreamsGetGlobalSiteTagCall
func (c *PropertiesDataStreamsGetGlobalSiteTagCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaGlobalSiteTag, error)
func (c *PropertiesDataStreamsGetGlobalSiteTagCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsGetGlobalSiteTagCall
func (c *PropertiesDataStreamsGetGlobalSiteTagCall) Header() http.Header
func (c *PropertiesDataStreamsGetGlobalSiteTagCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsGetGlobalSiteTagCall
type PropertiesDataStreamsListCall
func (c *PropertiesDataStreamsListCall) Context(ctx context.Context) *PropertiesDataStreamsListCall
func (c *PropertiesDataStreamsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListDataStreamsResponse, error)
func (c *PropertiesDataStreamsListCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsListCall
func (c *PropertiesDataStreamsListCall) Header() http.Header
func (c *PropertiesDataStreamsListCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsListCall
func (c *PropertiesDataStreamsListCall) PageSize(pageSize int64) *PropertiesDataStreamsListCall
func (c *PropertiesDataStreamsListCall) PageToken(pageToken string) *PropertiesDataStreamsListCall
func (c *PropertiesDataStreamsListCall) Pages(ctx context.Context, ...) error
type PropertiesDataStreamsMeasurementProtocolSecretsCreateCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsCreateCall) Context(ctx context.Context) *PropertiesDataStreamsMeasurementProtocolSecretsCreateCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret, error)
func (c *PropertiesDataStreamsMeasurementProtocolSecretsCreateCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsMeasurementProtocolSecretsCreateCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsCreateCall) Header() http.Header
type PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall) Context(ctx context.Context) *PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall) Header() http.Header
type PropertiesDataStreamsMeasurementProtocolSecretsGetCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsGetCall) Context(ctx context.Context) *PropertiesDataStreamsMeasurementProtocolSecretsGetCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret, error)
func (c *PropertiesDataStreamsMeasurementProtocolSecretsGetCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsMeasurementProtocolSecretsGetCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsGetCall) Header() http.Header
func (c *PropertiesDataStreamsMeasurementProtocolSecretsGetCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsMeasurementProtocolSecretsGetCall
type PropertiesDataStreamsMeasurementProtocolSecretsListCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) Context(ctx context.Context) *PropertiesDataStreamsMeasurementProtocolSecretsListCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListMeasurementProtocolSecretsResponse, error)
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsMeasurementProtocolSecretsListCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) Header() http.Header
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsMeasurementProtocolSecretsListCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) PageSize(pageSize int64) *PropertiesDataStreamsMeasurementProtocolSecretsListCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) PageToken(pageToken string) *PropertiesDataStreamsMeasurementProtocolSecretsListCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) Pages(ctx context.Context, ...) error
type PropertiesDataStreamsMeasurementProtocolSecretsPatchCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsPatchCall) Context(ctx context.Context) *PropertiesDataStreamsMeasurementProtocolSecretsPatchCall
func (c *PropertiesDataStreamsMeasurementProtocolSecretsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret, error)
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
func (c *PropertiesDataStreamsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaDataStream, error)
func (c *PropertiesDataStreamsPatchCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsPatchCall
func (c *PropertiesDataStreamsPatchCall) Header() http.Header
func (c *PropertiesDataStreamsPatchCall) UpdateMask(updateMask string) *PropertiesDataStreamsPatchCall
type PropertiesDataStreamsSKAdNetworkConversionValueSchemaCreateCall
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaCreateCall) Context(ctx context.Context) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaCreateCall
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchema, error)
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaCreateCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaCreateCall
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaCreateCall) Header() http.Header
type PropertiesDataStreamsSKAdNetworkConversionValueSchemaDeleteCall
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaDeleteCall) Context(ctx context.Context) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaDeleteCall
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaDeleteCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaDeleteCall
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaDeleteCall) Header() http.Header
type PropertiesDataStreamsSKAdNetworkConversionValueSchemaGetCall
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaGetCall) Context(ctx context.Context) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaGetCall
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchema, error)
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaGetCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaGetCall
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaGetCall) Header() http.Header
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaGetCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaGetCall
type PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall) Context(ctx context.Context) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListSKAdNetworkConversionValueSchemasResponse, ...)
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall) Header() http.Header
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall) PageSize(pageSize int64) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall) PageToken(pageToken string) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall) Pages(ctx context.Context, ...) error
type PropertiesDataStreamsSKAdNetworkConversionValueSchemaPatchCall
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaPatchCall) Context(ctx context.Context) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaPatchCall
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchema, error)
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaPatchCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaPatchCall
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaPatchCall) Header() http.Header
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaPatchCall) UpdateMask(updateMask string) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaPatchCall
type PropertiesDataStreamsSKAdNetworkConversionValueSchemaService
func NewPropertiesDataStreamsSKAdNetworkConversionValueSchemaService(s *Service) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaService
func (r *PropertiesDataStreamsSKAdNetworkConversionValueSchemaService) Create(parent string, ...) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaCreateCall
func (r *PropertiesDataStreamsSKAdNetworkConversionValueSchemaService) Delete(name string) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaDeleteCall
func (r *PropertiesDataStreamsSKAdNetworkConversionValueSchemaService) Get(name string) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaGetCall
func (r *PropertiesDataStreamsSKAdNetworkConversionValueSchemaService) List(parent string) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall
func (r *PropertiesDataStreamsSKAdNetworkConversionValueSchemaService) Patch(name string, ...) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaPatchCall
type PropertiesDataStreamsService
func NewPropertiesDataStreamsService(s *Service) *PropertiesDataStreamsService
func (r *PropertiesDataStreamsService) Create(parent string, ...) *PropertiesDataStreamsCreateCall
func (r *PropertiesDataStreamsService) Delete(name string) *PropertiesDataStreamsDeleteCall
func (r *PropertiesDataStreamsService) Get(name string) *PropertiesDataStreamsGetCall
func (r *PropertiesDataStreamsService) GetDataRedactionSettings(name string) *PropertiesDataStreamsGetDataRedactionSettingsCall
func (r *PropertiesDataStreamsService) GetEnhancedMeasurementSettings(name string) *PropertiesDataStreamsGetEnhancedMeasurementSettingsCall
func (r *PropertiesDataStreamsService) GetGlobalSiteTag(name string) *PropertiesDataStreamsGetGlobalSiteTagCall
func (r *PropertiesDataStreamsService) List(parent string) *PropertiesDataStreamsListCall
func (r *PropertiesDataStreamsService) Patch(name string, ...) *PropertiesDataStreamsPatchCall
func (r *PropertiesDataStreamsService) UpdateDataRedactionSettings(name string, ...) *PropertiesDataStreamsUpdateDataRedactionSettingsCall
func (r *PropertiesDataStreamsService) UpdateEnhancedMeasurementSettings(name string, ...) *PropertiesDataStreamsUpdateEnhancedMeasurementSettingsCall
type PropertiesDataStreamsUpdateDataRedactionSettingsCall
func (c *PropertiesDataStreamsUpdateDataRedactionSettingsCall) Context(ctx context.Context) *PropertiesDataStreamsUpdateDataRedactionSettingsCall
func (c *PropertiesDataStreamsUpdateDataRedactionSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaDataRedactionSettings, error)
func (c *PropertiesDataStreamsUpdateDataRedactionSettingsCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsUpdateDataRedactionSettingsCall
func (c *PropertiesDataStreamsUpdateDataRedactionSettingsCall) Header() http.Header
func (c *PropertiesDataStreamsUpdateDataRedactionSettingsCall) UpdateMask(updateMask string) *PropertiesDataStreamsUpdateDataRedactionSettingsCall
type PropertiesDataStreamsUpdateEnhancedMeasurementSettingsCall
func (c *PropertiesDataStreamsUpdateEnhancedMeasurementSettingsCall) Context(ctx context.Context) *PropertiesDataStreamsUpdateEnhancedMeasurementSettingsCall
func (c *PropertiesDataStreamsUpdateEnhancedMeasurementSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettings, error)
func (c *PropertiesDataStreamsUpdateEnhancedMeasurementSettingsCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsUpdateEnhancedMeasurementSettingsCall
func (c *PropertiesDataStreamsUpdateEnhancedMeasurementSettingsCall) Header() http.Header
func (c *PropertiesDataStreamsUpdateEnhancedMeasurementSettingsCall) UpdateMask(updateMask string) *PropertiesDataStreamsUpdateEnhancedMeasurementSettingsCall
type PropertiesDeleteCall
func (c *PropertiesDeleteCall) Context(ctx context.Context) *PropertiesDeleteCall
func (c *PropertiesDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaProperty, error)
func (c *PropertiesDeleteCall) Fields(s ...googleapi.Field) *PropertiesDeleteCall
func (c *PropertiesDeleteCall) Header() http.Header
type PropertiesDisplayVideo360AdvertiserLinkProposalsApproveCall
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsApproveCall) Context(ctx context.Context) *PropertiesDisplayVideo360AdvertiserLinkProposalsApproveCall
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsApproveCall) Do(opts ...googleapi.CallOption) (...)
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsApproveCall) Fields(s ...googleapi.Field) *PropertiesDisplayVideo360AdvertiserLinkProposalsApproveCall
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsApproveCall) Header() http.Header
type PropertiesDisplayVideo360AdvertiserLinkProposalsCancelCall
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsCancelCall) Context(ctx context.Context) *PropertiesDisplayVideo360AdvertiserLinkProposalsCancelCall
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsCancelCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal, error)
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsCancelCall) Fields(s ...googleapi.Field) *PropertiesDisplayVideo360AdvertiserLinkProposalsCancelCall
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsCancelCall) Header() http.Header
type PropertiesDisplayVideo360AdvertiserLinkProposalsCreateCall
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsCreateCall) Context(ctx context.Context) *PropertiesDisplayVideo360AdvertiserLinkProposalsCreateCall
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal, error)
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsCreateCall) Fields(s ...googleapi.Field) *PropertiesDisplayVideo360AdvertiserLinkProposalsCreateCall
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsCreateCall) Header() http.Header
type PropertiesDisplayVideo360AdvertiserLinkProposalsDeleteCall
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsDeleteCall) Context(ctx context.Context) *PropertiesDisplayVideo360AdvertiserLinkProposalsDeleteCall
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsDeleteCall) Fields(s ...googleapi.Field) *PropertiesDisplayVideo360AdvertiserLinkProposalsDeleteCall
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsDeleteCall) Header() http.Header
type PropertiesDisplayVideo360AdvertiserLinkProposalsGetCall
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsGetCall) Context(ctx context.Context) *PropertiesDisplayVideo360AdvertiserLinkProposalsGetCall
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal, error)
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsGetCall) Fields(s ...googleapi.Field) *PropertiesDisplayVideo360AdvertiserLinkProposalsGetCall
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsGetCall) Header() http.Header
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsGetCall) IfNoneMatch(entityTag string) *PropertiesDisplayVideo360AdvertiserLinkProposalsGetCall
type PropertiesDisplayVideo360AdvertiserLinkProposalsListCall
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsListCall) Context(ctx context.Context) *PropertiesDisplayVideo360AdvertiserLinkProposalsListCall
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinkProposalsResponse, ...)
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsListCall) Fields(s ...googleapi.Field) *PropertiesDisplayVideo360AdvertiserLinkProposalsListCall
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsListCall) Header() http.Header
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsListCall) IfNoneMatch(entityTag string) *PropertiesDisplayVideo360AdvertiserLinkProposalsListCall
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsListCall) PageSize(pageSize int64) *PropertiesDisplayVideo360AdvertiserLinkProposalsListCall
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsListCall) PageToken(pageToken string) *PropertiesDisplayVideo360AdvertiserLinkProposalsListCall
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsListCall) Pages(ctx context.Context, ...) error
type PropertiesDisplayVideo360AdvertiserLinkProposalsService
func NewPropertiesDisplayVideo360AdvertiserLinkProposalsService(s *Service) *PropertiesDisplayVideo360AdvertiserLinkProposalsService
func (r *PropertiesDisplayVideo360AdvertiserLinkProposalsService) Approve(name string, ...) *PropertiesDisplayVideo360AdvertiserLinkProposalsApproveCall
func (r *PropertiesDisplayVideo360AdvertiserLinkProposalsService) Cancel(name string, ...) *PropertiesDisplayVideo360AdvertiserLinkProposalsCancelCall
func (r *PropertiesDisplayVideo360AdvertiserLinkProposalsService) Create(parent string, ...) *PropertiesDisplayVideo360AdvertiserLinkProposalsCreateCall
func (r *PropertiesDisplayVideo360AdvertiserLinkProposalsService) Delete(name string) *PropertiesDisplayVideo360AdvertiserLinkProposalsDeleteCall
func (r *PropertiesDisplayVideo360AdvertiserLinkProposalsService) Get(name string) *PropertiesDisplayVideo360AdvertiserLinkProposalsGetCall
func (r *PropertiesDisplayVideo360AdvertiserLinkProposalsService) List(parent string) *PropertiesDisplayVideo360AdvertiserLinkProposalsListCall
type PropertiesDisplayVideo360AdvertiserLinksCreateCall
func (c *PropertiesDisplayVideo360AdvertiserLinksCreateCall) Context(ctx context.Context) *PropertiesDisplayVideo360AdvertiserLinksCreateCall
func (c *PropertiesDisplayVideo360AdvertiserLinksCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink, error)
func (c *PropertiesDisplayVideo360AdvertiserLinksCreateCall) Fields(s ...googleapi.Field) *PropertiesDisplayVideo360AdvertiserLinksCreateCall
func (c *PropertiesDisplayVideo360AdvertiserLinksCreateCall) Header() http.Header
type PropertiesDisplayVideo360AdvertiserLinksDeleteCall
func (c *PropertiesDisplayVideo360AdvertiserLinksDeleteCall) Context(ctx context.Context) *PropertiesDisplayVideo360AdvertiserLinksDeleteCall
func (c *PropertiesDisplayVideo360AdvertiserLinksDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesDisplayVideo360AdvertiserLinksDeleteCall) Fields(s ...googleapi.Field) *PropertiesDisplayVideo360AdvertiserLinksDeleteCall
func (c *PropertiesDisplayVideo360AdvertiserLinksDeleteCall) Header() http.Header
type PropertiesDisplayVideo360AdvertiserLinksGetCall
func (c *PropertiesDisplayVideo360AdvertiserLinksGetCall) Context(ctx context.Context) *PropertiesDisplayVideo360AdvertiserLinksGetCall
func (c *PropertiesDisplayVideo360AdvertiserLinksGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink, error)
func (c *PropertiesDisplayVideo360AdvertiserLinksGetCall) Fields(s ...googleapi.Field) *PropertiesDisplayVideo360AdvertiserLinksGetCall
func (c *PropertiesDisplayVideo360AdvertiserLinksGetCall) Header() http.Header
func (c *PropertiesDisplayVideo360AdvertiserLinksGetCall) IfNoneMatch(entityTag string) *PropertiesDisplayVideo360AdvertiserLinksGetCall
type PropertiesDisplayVideo360AdvertiserLinksListCall
func (c *PropertiesDisplayVideo360AdvertiserLinksListCall) Context(ctx context.Context) *PropertiesDisplayVideo360AdvertiserLinksListCall
func (c *PropertiesDisplayVideo360AdvertiserLinksListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinksResponse, error)
func (c *PropertiesDisplayVideo360AdvertiserLinksListCall) Fields(s ...googleapi.Field) *PropertiesDisplayVideo360AdvertiserLinksListCall
func (c *PropertiesDisplayVideo360AdvertiserLinksListCall) Header() http.Header
func (c *PropertiesDisplayVideo360AdvertiserLinksListCall) IfNoneMatch(entityTag string) *PropertiesDisplayVideo360AdvertiserLinksListCall
func (c *PropertiesDisplayVideo360AdvertiserLinksListCall) PageSize(pageSize int64) *PropertiesDisplayVideo360AdvertiserLinksListCall
func (c *PropertiesDisplayVideo360AdvertiserLinksListCall) PageToken(pageToken string) *PropertiesDisplayVideo360AdvertiserLinksListCall
func (c *PropertiesDisplayVideo360AdvertiserLinksListCall) Pages(ctx context.Context, ...) error
type PropertiesDisplayVideo360AdvertiserLinksPatchCall
func (c *PropertiesDisplayVideo360AdvertiserLinksPatchCall) Context(ctx context.Context) *PropertiesDisplayVideo360AdvertiserLinksPatchCall
func (c *PropertiesDisplayVideo360AdvertiserLinksPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink, error)
func (c *PropertiesDisplayVideo360AdvertiserLinksPatchCall) Fields(s ...googleapi.Field) *PropertiesDisplayVideo360AdvertiserLinksPatchCall
func (c *PropertiesDisplayVideo360AdvertiserLinksPatchCall) Header() http.Header
func (c *PropertiesDisplayVideo360AdvertiserLinksPatchCall) UpdateMask(updateMask string) *PropertiesDisplayVideo360AdvertiserLinksPatchCall
type PropertiesDisplayVideo360AdvertiserLinksService
func NewPropertiesDisplayVideo360AdvertiserLinksService(s *Service) *PropertiesDisplayVideo360AdvertiserLinksService
func (r *PropertiesDisplayVideo360AdvertiserLinksService) Create(parent string, ...) *PropertiesDisplayVideo360AdvertiserLinksCreateCall
func (r *PropertiesDisplayVideo360AdvertiserLinksService) Delete(name string) *PropertiesDisplayVideo360AdvertiserLinksDeleteCall
func (r *PropertiesDisplayVideo360AdvertiserLinksService) Get(name string) *PropertiesDisplayVideo360AdvertiserLinksGetCall
func (r *PropertiesDisplayVideo360AdvertiserLinksService) List(parent string) *PropertiesDisplayVideo360AdvertiserLinksListCall
func (r *PropertiesDisplayVideo360AdvertiserLinksService) Patch(name string, ...) *PropertiesDisplayVideo360AdvertiserLinksPatchCall
type PropertiesExpandedDataSetsCreateCall
func (c *PropertiesExpandedDataSetsCreateCall) Context(ctx context.Context) *PropertiesExpandedDataSetsCreateCall
func (c *PropertiesExpandedDataSetsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaExpandedDataSet, error)
func (c *PropertiesExpandedDataSetsCreateCall) Fields(s ...googleapi.Field) *PropertiesExpandedDataSetsCreateCall
func (c *PropertiesExpandedDataSetsCreateCall) Header() http.Header
type PropertiesExpandedDataSetsDeleteCall
func (c *PropertiesExpandedDataSetsDeleteCall) Context(ctx context.Context) *PropertiesExpandedDataSetsDeleteCall
func (c *PropertiesExpandedDataSetsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesExpandedDataSetsDeleteCall) Fields(s ...googleapi.Field) *PropertiesExpandedDataSetsDeleteCall
func (c *PropertiesExpandedDataSetsDeleteCall) Header() http.Header
type PropertiesExpandedDataSetsGetCall
func (c *PropertiesExpandedDataSetsGetCall) Context(ctx context.Context) *PropertiesExpandedDataSetsGetCall
func (c *PropertiesExpandedDataSetsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaExpandedDataSet, error)
func (c *PropertiesExpandedDataSetsGetCall) Fields(s ...googleapi.Field) *PropertiesExpandedDataSetsGetCall
func (c *PropertiesExpandedDataSetsGetCall) Header() http.Header
func (c *PropertiesExpandedDataSetsGetCall) IfNoneMatch(entityTag string) *PropertiesExpandedDataSetsGetCall
type PropertiesExpandedDataSetsListCall
func (c *PropertiesExpandedDataSetsListCall) Context(ctx context.Context) *PropertiesExpandedDataSetsListCall
func (c *PropertiesExpandedDataSetsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListExpandedDataSetsResponse, error)
func (c *PropertiesExpandedDataSetsListCall) Fields(s ...googleapi.Field) *PropertiesExpandedDataSetsListCall
func (c *PropertiesExpandedDataSetsListCall) Header() http.Header
func (c *PropertiesExpandedDataSetsListCall) IfNoneMatch(entityTag string) *PropertiesExpandedDataSetsListCall
func (c *PropertiesExpandedDataSetsListCall) PageSize(pageSize int64) *PropertiesExpandedDataSetsListCall
func (c *PropertiesExpandedDataSetsListCall) PageToken(pageToken string) *PropertiesExpandedDataSetsListCall
func (c *PropertiesExpandedDataSetsListCall) Pages(ctx context.Context, ...) error
type PropertiesExpandedDataSetsPatchCall
func (c *PropertiesExpandedDataSetsPatchCall) Context(ctx context.Context) *PropertiesExpandedDataSetsPatchCall
func (c *PropertiesExpandedDataSetsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaExpandedDataSet, error)
func (c *PropertiesExpandedDataSetsPatchCall) Fields(s ...googleapi.Field) *PropertiesExpandedDataSetsPatchCall
func (c *PropertiesExpandedDataSetsPatchCall) Header() http.Header
func (c *PropertiesExpandedDataSetsPatchCall) UpdateMask(updateMask string) *PropertiesExpandedDataSetsPatchCall
type PropertiesExpandedDataSetsService
func NewPropertiesExpandedDataSetsService(s *Service) *PropertiesExpandedDataSetsService
func (r *PropertiesExpandedDataSetsService) Create(parent string, ...) *PropertiesExpandedDataSetsCreateCall
func (r *PropertiesExpandedDataSetsService) Delete(name string) *PropertiesExpandedDataSetsDeleteCall
func (r *PropertiesExpandedDataSetsService) Get(name string) *PropertiesExpandedDataSetsGetCall
func (r *PropertiesExpandedDataSetsService) List(parent string) *PropertiesExpandedDataSetsListCall
func (r *PropertiesExpandedDataSetsService) Patch(name string, ...) *PropertiesExpandedDataSetsPatchCall
type PropertiesFirebaseLinksCreateCall
func (c *PropertiesFirebaseLinksCreateCall) Context(ctx context.Context) *PropertiesFirebaseLinksCreateCall
func (c *PropertiesFirebaseLinksCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaFirebaseLink, error)
func (c *PropertiesFirebaseLinksCreateCall) Fields(s ...googleapi.Field) *PropertiesFirebaseLinksCreateCall
func (c *PropertiesFirebaseLinksCreateCall) Header() http.Header
type PropertiesFirebaseLinksDeleteCall
func (c *PropertiesFirebaseLinksDeleteCall) Context(ctx context.Context) *PropertiesFirebaseLinksDeleteCall
func (c *PropertiesFirebaseLinksDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesFirebaseLinksDeleteCall) Fields(s ...googleapi.Field) *PropertiesFirebaseLinksDeleteCall
func (c *PropertiesFirebaseLinksDeleteCall) Header() http.Header
type PropertiesFirebaseLinksListCall
func (c *PropertiesFirebaseLinksListCall) Context(ctx context.Context) *PropertiesFirebaseLinksListCall
func (c *PropertiesFirebaseLinksListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListFirebaseLinksResponse, error)
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
type PropertiesGetAttributionSettingsCall
func (c *PropertiesGetAttributionSettingsCall) Context(ctx context.Context) *PropertiesGetAttributionSettingsCall
func (c *PropertiesGetAttributionSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAttributionSettings, error)
func (c *PropertiesGetAttributionSettingsCall) Fields(s ...googleapi.Field) *PropertiesGetAttributionSettingsCall
func (c *PropertiesGetAttributionSettingsCall) Header() http.Header
func (c *PropertiesGetAttributionSettingsCall) IfNoneMatch(entityTag string) *PropertiesGetAttributionSettingsCall
type PropertiesGetCall
func (c *PropertiesGetCall) Context(ctx context.Context) *PropertiesGetCall
func (c *PropertiesGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaProperty, error)
func (c *PropertiesGetCall) Fields(s ...googleapi.Field) *PropertiesGetCall
func (c *PropertiesGetCall) Header() http.Header
func (c *PropertiesGetCall) IfNoneMatch(entityTag string) *PropertiesGetCall
type PropertiesGetDataRetentionSettingsCall
func (c *PropertiesGetDataRetentionSettingsCall) Context(ctx context.Context) *PropertiesGetDataRetentionSettingsCall
func (c *PropertiesGetDataRetentionSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaDataRetentionSettings, error)
func (c *PropertiesGetDataRetentionSettingsCall) Fields(s ...googleapi.Field) *PropertiesGetDataRetentionSettingsCall
func (c *PropertiesGetDataRetentionSettingsCall) Header() http.Header
func (c *PropertiesGetDataRetentionSettingsCall) IfNoneMatch(entityTag string) *PropertiesGetDataRetentionSettingsCall
type PropertiesGetGoogleSignalsSettingsCall
func (c *PropertiesGetGoogleSignalsSettingsCall) Context(ctx context.Context) *PropertiesGetGoogleSignalsSettingsCall
func (c *PropertiesGetGoogleSignalsSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaGoogleSignalsSettings, error)
func (c *PropertiesGetGoogleSignalsSettingsCall) Fields(s ...googleapi.Field) *PropertiesGetGoogleSignalsSettingsCall
func (c *PropertiesGetGoogleSignalsSettingsCall) Header() http.Header
func (c *PropertiesGetGoogleSignalsSettingsCall) IfNoneMatch(entityTag string) *PropertiesGetGoogleSignalsSettingsCall
type PropertiesGetReportingIdentitySettingsCall
func (c *PropertiesGetReportingIdentitySettingsCall) Context(ctx context.Context) *PropertiesGetReportingIdentitySettingsCall
func (c *PropertiesGetReportingIdentitySettingsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaReportingIdentitySettings, error)
func (c *PropertiesGetReportingIdentitySettingsCall) Fields(s ...googleapi.Field) *PropertiesGetReportingIdentitySettingsCall
func (c *PropertiesGetReportingIdentitySettingsCall) Header() http.Header
func (c *PropertiesGetReportingIdentitySettingsCall) IfNoneMatch(entityTag string) *PropertiesGetReportingIdentitySettingsCall
type PropertiesGoogleAdsLinksCreateCall
func (c *PropertiesGoogleAdsLinksCreateCall) Context(ctx context.Context) *PropertiesGoogleAdsLinksCreateCall
func (c *PropertiesGoogleAdsLinksCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaGoogleAdsLink, error)
func (c *PropertiesGoogleAdsLinksCreateCall) Fields(s ...googleapi.Field) *PropertiesGoogleAdsLinksCreateCall
func (c *PropertiesGoogleAdsLinksCreateCall) Header() http.Header
type PropertiesGoogleAdsLinksDeleteCall
func (c *PropertiesGoogleAdsLinksDeleteCall) Context(ctx context.Context) *PropertiesGoogleAdsLinksDeleteCall
func (c *PropertiesGoogleAdsLinksDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesGoogleAdsLinksDeleteCall) Fields(s ...googleapi.Field) *PropertiesGoogleAdsLinksDeleteCall
func (c *PropertiesGoogleAdsLinksDeleteCall) Header() http.Header
type PropertiesGoogleAdsLinksListCall
func (c *PropertiesGoogleAdsLinksListCall) Context(ctx context.Context) *PropertiesGoogleAdsLinksListCall
func (c *PropertiesGoogleAdsLinksListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListGoogleAdsLinksResponse, error)
func (c *PropertiesGoogleAdsLinksListCall) Fields(s ...googleapi.Field) *PropertiesGoogleAdsLinksListCall
func (c *PropertiesGoogleAdsLinksListCall) Header() http.Header
func (c *PropertiesGoogleAdsLinksListCall) IfNoneMatch(entityTag string) *PropertiesGoogleAdsLinksListCall
func (c *PropertiesGoogleAdsLinksListCall) PageSize(pageSize int64) *PropertiesGoogleAdsLinksListCall
func (c *PropertiesGoogleAdsLinksListCall) PageToken(pageToken string) *PropertiesGoogleAdsLinksListCall
func (c *PropertiesGoogleAdsLinksListCall) Pages(ctx context.Context, ...) error
type PropertiesGoogleAdsLinksPatchCall
func (c *PropertiesGoogleAdsLinksPatchCall) Context(ctx context.Context) *PropertiesGoogleAdsLinksPatchCall
func (c *PropertiesGoogleAdsLinksPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaGoogleAdsLink, error)
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
func (c *PropertiesKeyEventsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaKeyEvent, error)
func (c *PropertiesKeyEventsCreateCall) Fields(s ...googleapi.Field) *PropertiesKeyEventsCreateCall
func (c *PropertiesKeyEventsCreateCall) Header() http.Header
type PropertiesKeyEventsDeleteCall
func (c *PropertiesKeyEventsDeleteCall) Context(ctx context.Context) *PropertiesKeyEventsDeleteCall
func (c *PropertiesKeyEventsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesKeyEventsDeleteCall) Fields(s ...googleapi.Field) *PropertiesKeyEventsDeleteCall
func (c *PropertiesKeyEventsDeleteCall) Header() http.Header
type PropertiesKeyEventsGetCall
func (c *PropertiesKeyEventsGetCall) Context(ctx context.Context) *PropertiesKeyEventsGetCall
func (c *PropertiesKeyEventsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaKeyEvent, error)
func (c *PropertiesKeyEventsGetCall) Fields(s ...googleapi.Field) *PropertiesKeyEventsGetCall
func (c *PropertiesKeyEventsGetCall) Header() http.Header
func (c *PropertiesKeyEventsGetCall) IfNoneMatch(entityTag string) *PropertiesKeyEventsGetCall
type PropertiesKeyEventsListCall
func (c *PropertiesKeyEventsListCall) Context(ctx context.Context) *PropertiesKeyEventsListCall
func (c *PropertiesKeyEventsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListKeyEventsResponse, error)
func (c *PropertiesKeyEventsListCall) Fields(s ...googleapi.Field) *PropertiesKeyEventsListCall
func (c *PropertiesKeyEventsListCall) Header() http.Header
func (c *PropertiesKeyEventsListCall) IfNoneMatch(entityTag string) *PropertiesKeyEventsListCall
func (c *PropertiesKeyEventsListCall) PageSize(pageSize int64) *PropertiesKeyEventsListCall
func (c *PropertiesKeyEventsListCall) PageToken(pageToken string) *PropertiesKeyEventsListCall
func (c *PropertiesKeyEventsListCall) Pages(ctx context.Context, ...) error
type PropertiesKeyEventsPatchCall
func (c *PropertiesKeyEventsPatchCall) Context(ctx context.Context) *PropertiesKeyEventsPatchCall
func (c *PropertiesKeyEventsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaKeyEvent, error)
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
func (c *PropertiesListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListPropertiesResponse, error)
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
func (c *PropertiesPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaProperty, error)
func (c *PropertiesPatchCall) Fields(s ...googleapi.Field) *PropertiesPatchCall
func (c *PropertiesPatchCall) Header() http.Header
func (c *PropertiesPatchCall) UpdateMask(updateMask string) *PropertiesPatchCall
type PropertiesProvisionSubpropertyCall
func (c *PropertiesProvisionSubpropertyCall) Context(ctx context.Context) *PropertiesProvisionSubpropertyCall
func (c *PropertiesProvisionSubpropertyCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaProvisionSubpropertyResponse, error)
func (c *PropertiesProvisionSubpropertyCall) Fields(s ...googleapi.Field) *PropertiesProvisionSubpropertyCall
func (c *PropertiesProvisionSubpropertyCall) Header() http.Header
type PropertiesReportingDataAnnotationsCreateCall
func (c *PropertiesReportingDataAnnotationsCreateCall) Context(ctx context.Context) *PropertiesReportingDataAnnotationsCreateCall
func (c *PropertiesReportingDataAnnotationsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaReportingDataAnnotation, error)
func (c *PropertiesReportingDataAnnotationsCreateCall) Fields(s ...googleapi.Field) *PropertiesReportingDataAnnotationsCreateCall
func (c *PropertiesReportingDataAnnotationsCreateCall) Header() http.Header
type PropertiesReportingDataAnnotationsDeleteCall
func (c *PropertiesReportingDataAnnotationsDeleteCall) Context(ctx context.Context) *PropertiesReportingDataAnnotationsDeleteCall
func (c *PropertiesReportingDataAnnotationsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesReportingDataAnnotationsDeleteCall) Fields(s ...googleapi.Field) *PropertiesReportingDataAnnotationsDeleteCall
func (c *PropertiesReportingDataAnnotationsDeleteCall) Header() http.Header
type PropertiesReportingDataAnnotationsGetCall
func (c *PropertiesReportingDataAnnotationsGetCall) Context(ctx context.Context) *PropertiesReportingDataAnnotationsGetCall
func (c *PropertiesReportingDataAnnotationsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaReportingDataAnnotation, error)
func (c *PropertiesReportingDataAnnotationsGetCall) Fields(s ...googleapi.Field) *PropertiesReportingDataAnnotationsGetCall
func (c *PropertiesReportingDataAnnotationsGetCall) Header() http.Header
func (c *PropertiesReportingDataAnnotationsGetCall) IfNoneMatch(entityTag string) *PropertiesReportingDataAnnotationsGetCall
type PropertiesReportingDataAnnotationsListCall
func (c *PropertiesReportingDataAnnotationsListCall) Context(ctx context.Context) *PropertiesReportingDataAnnotationsListCall
func (c *PropertiesReportingDataAnnotationsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListReportingDataAnnotationsResponse, error)
func (c *PropertiesReportingDataAnnotationsListCall) Fields(s ...googleapi.Field) *PropertiesReportingDataAnnotationsListCall
func (c *PropertiesReportingDataAnnotationsListCall) Filter(filter string) *PropertiesReportingDataAnnotationsListCall
func (c *PropertiesReportingDataAnnotationsListCall) Header() http.Header
func (c *PropertiesReportingDataAnnotationsListCall) IfNoneMatch(entityTag string) *PropertiesReportingDataAnnotationsListCall
func (c *PropertiesReportingDataAnnotationsListCall) PageSize(pageSize int64) *PropertiesReportingDataAnnotationsListCall
func (c *PropertiesReportingDataAnnotationsListCall) PageToken(pageToken string) *PropertiesReportingDataAnnotationsListCall
func (c *PropertiesReportingDataAnnotationsListCall) Pages(ctx context.Context, ...) error
type PropertiesReportingDataAnnotationsPatchCall
func (c *PropertiesReportingDataAnnotationsPatchCall) Context(ctx context.Context) *PropertiesReportingDataAnnotationsPatchCall
func (c *PropertiesReportingDataAnnotationsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaReportingDataAnnotation, error)
func (c *PropertiesReportingDataAnnotationsPatchCall) Fields(s ...googleapi.Field) *PropertiesReportingDataAnnotationsPatchCall
func (c *PropertiesReportingDataAnnotationsPatchCall) Header() http.Header
func (c *PropertiesReportingDataAnnotationsPatchCall) UpdateMask(updateMask string) *PropertiesReportingDataAnnotationsPatchCall
type PropertiesReportingDataAnnotationsService
func NewPropertiesReportingDataAnnotationsService(s *Service) *PropertiesReportingDataAnnotationsService
func (r *PropertiesReportingDataAnnotationsService) Create(parent string, ...) *PropertiesReportingDataAnnotationsCreateCall
func (r *PropertiesReportingDataAnnotationsService) Delete(name string) *PropertiesReportingDataAnnotationsDeleteCall
func (r *PropertiesReportingDataAnnotationsService) Get(name string) *PropertiesReportingDataAnnotationsGetCall
func (r *PropertiesReportingDataAnnotationsService) List(parent string) *PropertiesReportingDataAnnotationsListCall
func (r *PropertiesReportingDataAnnotationsService) Patch(name string, ...) *PropertiesReportingDataAnnotationsPatchCall
type PropertiesRollupPropertySourceLinksCreateCall
func (c *PropertiesRollupPropertySourceLinksCreateCall) Context(ctx context.Context) *PropertiesRollupPropertySourceLinksCreateCall
func (c *PropertiesRollupPropertySourceLinksCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaRollupPropertySourceLink, error)
func (c *PropertiesRollupPropertySourceLinksCreateCall) Fields(s ...googleapi.Field) *PropertiesRollupPropertySourceLinksCreateCall
func (c *PropertiesRollupPropertySourceLinksCreateCall) Header() http.Header
type PropertiesRollupPropertySourceLinksDeleteCall
func (c *PropertiesRollupPropertySourceLinksDeleteCall) Context(ctx context.Context) *PropertiesRollupPropertySourceLinksDeleteCall
func (c *PropertiesRollupPropertySourceLinksDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesRollupPropertySourceLinksDeleteCall) Fields(s ...googleapi.Field) *PropertiesRollupPropertySourceLinksDeleteCall
func (c *PropertiesRollupPropertySourceLinksDeleteCall) Header() http.Header
type PropertiesRollupPropertySourceLinksGetCall
func (c *PropertiesRollupPropertySourceLinksGetCall) Context(ctx context.Context) *PropertiesRollupPropertySourceLinksGetCall
func (c *PropertiesRollupPropertySourceLinksGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaRollupPropertySourceLink, error)
func (c *PropertiesRollupPropertySourceLinksGetCall) Fields(s ...googleapi.Field) *PropertiesRollupPropertySourceLinksGetCall
func (c *PropertiesRollupPropertySourceLinksGetCall) Header() http.Header
func (c *PropertiesRollupPropertySourceLinksGetCall) IfNoneMatch(entityTag string) *PropertiesRollupPropertySourceLinksGetCall
type PropertiesRollupPropertySourceLinksListCall
func (c *PropertiesRollupPropertySourceLinksListCall) Context(ctx context.Context) *PropertiesRollupPropertySourceLinksListCall
func (c *PropertiesRollupPropertySourceLinksListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListRollupPropertySourceLinksResponse, error)
func (c *PropertiesRollupPropertySourceLinksListCall) Fields(s ...googleapi.Field) *PropertiesRollupPropertySourceLinksListCall
func (c *PropertiesRollupPropertySourceLinksListCall) Header() http.Header
func (c *PropertiesRollupPropertySourceLinksListCall) IfNoneMatch(entityTag string) *PropertiesRollupPropertySourceLinksListCall
func (c *PropertiesRollupPropertySourceLinksListCall) PageSize(pageSize int64) *PropertiesRollupPropertySourceLinksListCall
func (c *PropertiesRollupPropertySourceLinksListCall) PageToken(pageToken string) *PropertiesRollupPropertySourceLinksListCall
func (c *PropertiesRollupPropertySourceLinksListCall) Pages(ctx context.Context, ...) error
type PropertiesRollupPropertySourceLinksService
func NewPropertiesRollupPropertySourceLinksService(s *Service) *PropertiesRollupPropertySourceLinksService
func (r *PropertiesRollupPropertySourceLinksService) Create(parent string, ...) *PropertiesRollupPropertySourceLinksCreateCall
func (r *PropertiesRollupPropertySourceLinksService) Delete(name string) *PropertiesRollupPropertySourceLinksDeleteCall
func (r *PropertiesRollupPropertySourceLinksService) Get(name string) *PropertiesRollupPropertySourceLinksGetCall
func (r *PropertiesRollupPropertySourceLinksService) List(parent string) *PropertiesRollupPropertySourceLinksListCall
type PropertiesRunAccessReportCall
func (c *PropertiesRunAccessReportCall) Context(ctx context.Context) *PropertiesRunAccessReportCall
func (c *PropertiesRunAccessReportCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaRunAccessReportResponse, error)
func (c *PropertiesRunAccessReportCall) Fields(s ...googleapi.Field) *PropertiesRunAccessReportCall
func (c *PropertiesRunAccessReportCall) Header() http.Header
type PropertiesSearchAds360LinksCreateCall
func (c *PropertiesSearchAds360LinksCreateCall) Context(ctx context.Context) *PropertiesSearchAds360LinksCreateCall
func (c *PropertiesSearchAds360LinksCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaSearchAds360Link, error)
func (c *PropertiesSearchAds360LinksCreateCall) Fields(s ...googleapi.Field) *PropertiesSearchAds360LinksCreateCall
func (c *PropertiesSearchAds360LinksCreateCall) Header() http.Header
type PropertiesSearchAds360LinksDeleteCall
func (c *PropertiesSearchAds360LinksDeleteCall) Context(ctx context.Context) *PropertiesSearchAds360LinksDeleteCall
func (c *PropertiesSearchAds360LinksDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesSearchAds360LinksDeleteCall) Fields(s ...googleapi.Field) *PropertiesSearchAds360LinksDeleteCall
func (c *PropertiesSearchAds360LinksDeleteCall) Header() http.Header
type PropertiesSearchAds360LinksGetCall
func (c *PropertiesSearchAds360LinksGetCall) Context(ctx context.Context) *PropertiesSearchAds360LinksGetCall
func (c *PropertiesSearchAds360LinksGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaSearchAds360Link, error)
func (c *PropertiesSearchAds360LinksGetCall) Fields(s ...googleapi.Field) *PropertiesSearchAds360LinksGetCall
func (c *PropertiesSearchAds360LinksGetCall) Header() http.Header
func (c *PropertiesSearchAds360LinksGetCall) IfNoneMatch(entityTag string) *PropertiesSearchAds360LinksGetCall
type PropertiesSearchAds360LinksListCall
func (c *PropertiesSearchAds360LinksListCall) Context(ctx context.Context) *PropertiesSearchAds360LinksListCall
func (c *PropertiesSearchAds360LinksListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListSearchAds360LinksResponse, error)
func (c *PropertiesSearchAds360LinksListCall) Fields(s ...googleapi.Field) *PropertiesSearchAds360LinksListCall
func (c *PropertiesSearchAds360LinksListCall) Header() http.Header
func (c *PropertiesSearchAds360LinksListCall) IfNoneMatch(entityTag string) *PropertiesSearchAds360LinksListCall
func (c *PropertiesSearchAds360LinksListCall) PageSize(pageSize int64) *PropertiesSearchAds360LinksListCall
func (c *PropertiesSearchAds360LinksListCall) PageToken(pageToken string) *PropertiesSearchAds360LinksListCall
func (c *PropertiesSearchAds360LinksListCall) Pages(ctx context.Context, ...) error
type PropertiesSearchAds360LinksPatchCall
func (c *PropertiesSearchAds360LinksPatchCall) Context(ctx context.Context) *PropertiesSearchAds360LinksPatchCall
func (c *PropertiesSearchAds360LinksPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaSearchAds360Link, error)
func (c *PropertiesSearchAds360LinksPatchCall) Fields(s ...googleapi.Field) *PropertiesSearchAds360LinksPatchCall
func (c *PropertiesSearchAds360LinksPatchCall) Header() http.Header
func (c *PropertiesSearchAds360LinksPatchCall) UpdateMask(updateMask string) *PropertiesSearchAds360LinksPatchCall
type PropertiesSearchAds360LinksService
func NewPropertiesSearchAds360LinksService(s *Service) *PropertiesSearchAds360LinksService
func (r *PropertiesSearchAds360LinksService) Create(parent string, ...) *PropertiesSearchAds360LinksCreateCall
func (r *PropertiesSearchAds360LinksService) Delete(name string) *PropertiesSearchAds360LinksDeleteCall
func (r *PropertiesSearchAds360LinksService) Get(name string) *PropertiesSearchAds360LinksGetCall
func (r *PropertiesSearchAds360LinksService) List(parent string) *PropertiesSearchAds360LinksListCall
func (r *PropertiesSearchAds360LinksService) Patch(name string, ...) *PropertiesSearchAds360LinksPatchCall
type PropertiesService
func NewPropertiesService(s *Service) *PropertiesService
func (r *PropertiesService) AcknowledgeUserDataCollection(property string, ...) *PropertiesAcknowledgeUserDataCollectionCall
func (r *PropertiesService) Create(googleanalyticsadminv1alphaproperty *GoogleAnalyticsAdminV1alphaProperty) *PropertiesCreateCall
func (r *PropertiesService) CreateRollupProperty(...) *PropertiesCreateRollupPropertyCall
func (r *PropertiesService) Delete(name string) *PropertiesDeleteCall
func (r *PropertiesService) Get(name string) *PropertiesGetCall
func (r *PropertiesService) GetAttributionSettings(name string) *PropertiesGetAttributionSettingsCall
func (r *PropertiesService) GetDataRetentionSettings(name string) *PropertiesGetDataRetentionSettingsCall
func (r *PropertiesService) GetGoogleSignalsSettings(name string) *PropertiesGetGoogleSignalsSettingsCall
func (r *PropertiesService) GetReportingIdentitySettings(name string) *PropertiesGetReportingIdentitySettingsCall
func (r *PropertiesService) List() *PropertiesListCall
func (r *PropertiesService) Patch(name string, ...) *PropertiesPatchCall
func (r *PropertiesService) ProvisionSubproperty(...) *PropertiesProvisionSubpropertyCall
func (r *PropertiesService) RunAccessReport(entity string, ...) *PropertiesRunAccessReportCall
func (r *PropertiesService) SubmitUserDeletion(name string, ...) *PropertiesSubmitUserDeletionCall
func (r *PropertiesService) UpdateAttributionSettings(name string, ...) *PropertiesUpdateAttributionSettingsCall
func (r *PropertiesService) UpdateDataRetentionSettings(name string, ...) *PropertiesUpdateDataRetentionSettingsCall
func (r *PropertiesService) UpdateGoogleSignalsSettings(name string, ...) *PropertiesUpdateGoogleSignalsSettingsCall
type PropertiesSubmitUserDeletionCall
func (c *PropertiesSubmitUserDeletionCall) Context(ctx context.Context) *PropertiesSubmitUserDeletionCall
func (c *PropertiesSubmitUserDeletionCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaSubmitUserDeletionResponse, error)
func (c *PropertiesSubmitUserDeletionCall) Fields(s ...googleapi.Field) *PropertiesSubmitUserDeletionCall
func (c *PropertiesSubmitUserDeletionCall) Header() http.Header
type PropertiesSubpropertyEventFiltersCreateCall
func (c *PropertiesSubpropertyEventFiltersCreateCall) Context(ctx context.Context) *PropertiesSubpropertyEventFiltersCreateCall
func (c *PropertiesSubpropertyEventFiltersCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaSubpropertyEventFilter, error)
func (c *PropertiesSubpropertyEventFiltersCreateCall) Fields(s ...googleapi.Field) *PropertiesSubpropertyEventFiltersCreateCall
func (c *PropertiesSubpropertyEventFiltersCreateCall) Header() http.Header
type PropertiesSubpropertyEventFiltersDeleteCall
func (c *PropertiesSubpropertyEventFiltersDeleteCall) Context(ctx context.Context) *PropertiesSubpropertyEventFiltersDeleteCall
func (c *PropertiesSubpropertyEventFiltersDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)
func (c *PropertiesSubpropertyEventFiltersDeleteCall) Fields(s ...googleapi.Field) *PropertiesSubpropertyEventFiltersDeleteCall
func (c *PropertiesSubpropertyEventFiltersDeleteCall) Header() http.Header
type PropertiesSubpropertyEventFiltersGetCall
func (c *PropertiesSubpropertyEventFiltersGetCall) Context(ctx context.Context) *PropertiesSubpropertyEventFiltersGetCall
func (c *PropertiesSubpropertyEventFiltersGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaSubpropertyEventFilter, error)
func (c *PropertiesSubpropertyEventFiltersGetCall) Fields(s ...googleapi.Field) *PropertiesSubpropertyEventFiltersGetCall
func (c *PropertiesSubpropertyEventFiltersGetCall) Header() http.Header
func (c *PropertiesSubpropertyEventFiltersGetCall) IfNoneMatch(entityTag string) *PropertiesSubpropertyEventFiltersGetCall
type PropertiesSubpropertyEventFiltersListCall
func (c *PropertiesSubpropertyEventFiltersListCall) Context(ctx context.Context) *PropertiesSubpropertyEventFiltersListCall
func (c *PropertiesSubpropertyEventFiltersListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListSubpropertyEventFiltersResponse, error)
func (c *PropertiesSubpropertyEventFiltersListCall) Fields(s ...googleapi.Field) *PropertiesSubpropertyEventFiltersListCall
func (c *PropertiesSubpropertyEventFiltersListCall) Header() http.Header
func (c *PropertiesSubpropertyEventFiltersListCall) IfNoneMatch(entityTag string) *PropertiesSubpropertyEventFiltersListCall
func (c *PropertiesSubpropertyEventFiltersListCall) PageSize(pageSize int64) *PropertiesSubpropertyEventFiltersListCall
func (c *PropertiesSubpropertyEventFiltersListCall) PageToken(pageToken string) *PropertiesSubpropertyEventFiltersListCall
func (c *PropertiesSubpropertyEventFiltersListCall) Pages(ctx context.Context, ...) error
type PropertiesSubpropertyEventFiltersPatchCall
func (c *PropertiesSubpropertyEventFiltersPatchCall) Context(ctx context.Context) *PropertiesSubpropertyEventFiltersPatchCall
func (c *PropertiesSubpropertyEventFiltersPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaSubpropertyEventFilter, error)
func (c *PropertiesSubpropertyEventFiltersPatchCall) Fields(s ...googleapi.Field) *PropertiesSubpropertyEventFiltersPatchCall
func (c *PropertiesSubpropertyEventFiltersPatchCall) Header() http.Header
func (c *PropertiesSubpropertyEventFiltersPatchCall) UpdateMask(updateMask string) *PropertiesSubpropertyEventFiltersPatchCall
type PropertiesSubpropertyEventFiltersService
func NewPropertiesSubpropertyEventFiltersService(s *Service) *PropertiesSubpropertyEventFiltersService
func (r *PropertiesSubpropertyEventFiltersService) Create(parent string, ...) *PropertiesSubpropertyEventFiltersCreateCall
func (r *PropertiesSubpropertyEventFiltersService) Delete(name string) *PropertiesSubpropertyEventFiltersDeleteCall
func (r *PropertiesSubpropertyEventFiltersService) Get(name string) *PropertiesSubpropertyEventFiltersGetCall
func (r *PropertiesSubpropertyEventFiltersService) List(parent string) *PropertiesSubpropertyEventFiltersListCall
func (r *PropertiesSubpropertyEventFiltersService) Patch(name string, ...) *PropertiesSubpropertyEventFiltersPatchCall
type PropertiesSubpropertySyncConfigsGetCall
func (c *PropertiesSubpropertySyncConfigsGetCall) Context(ctx context.Context) *PropertiesSubpropertySyncConfigsGetCall
func (c *PropertiesSubpropertySyncConfigsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaSubpropertySyncConfig, error)
func (c *PropertiesSubpropertySyncConfigsGetCall) Fields(s ...googleapi.Field) *PropertiesSubpropertySyncConfigsGetCall
func (c *PropertiesSubpropertySyncConfigsGetCall) Header() http.Header
func (c *PropertiesSubpropertySyncConfigsGetCall) IfNoneMatch(entityTag string) *PropertiesSubpropertySyncConfigsGetCall
type PropertiesSubpropertySyncConfigsListCall
func (c *PropertiesSubpropertySyncConfigsListCall) Context(ctx context.Context) *PropertiesSubpropertySyncConfigsListCall
func (c *PropertiesSubpropertySyncConfigsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListSubpropertySyncConfigsResponse, error)
func (c *PropertiesSubpropertySyncConfigsListCall) Fields(s ...googleapi.Field) *PropertiesSubpropertySyncConfigsListCall
func (c *PropertiesSubpropertySyncConfigsListCall) Header() http.Header
func (c *PropertiesSubpropertySyncConfigsListCall) IfNoneMatch(entityTag string) *PropertiesSubpropertySyncConfigsListCall
func (c *PropertiesSubpropertySyncConfigsListCall) PageSize(pageSize int64) *PropertiesSubpropertySyncConfigsListCall
func (c *PropertiesSubpropertySyncConfigsListCall) PageToken(pageToken string) *PropertiesSubpropertySyncConfigsListCall
func (c *PropertiesSubpropertySyncConfigsListCall) Pages(ctx context.Context, ...) error
type PropertiesSubpropertySyncConfigsPatchCall
func (c *PropertiesSubpropertySyncConfigsPatchCall) Context(ctx context.Context) *PropertiesSubpropertySyncConfigsPatchCall
func (c *PropertiesSubpropertySyncConfigsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaSubpropertySyncConfig, error)
func (c *PropertiesSubpropertySyncConfigsPatchCall) Fields(s ...googleapi.Field) *PropertiesSubpropertySyncConfigsPatchCall
func (c *PropertiesSubpropertySyncConfigsPatchCall) Header() http.Header
func (c *PropertiesSubpropertySyncConfigsPatchCall) UpdateMask(updateMask string) *PropertiesSubpropertySyncConfigsPatchCall
type PropertiesSubpropertySyncConfigsService
func NewPropertiesSubpropertySyncConfigsService(s *Service) *PropertiesSubpropertySyncConfigsService
func (r *PropertiesSubpropertySyncConfigsService) Get(name string) *PropertiesSubpropertySyncConfigsGetCall
func (r *PropertiesSubpropertySyncConfigsService) List(parent string) *PropertiesSubpropertySyncConfigsListCall
func (r *PropertiesSubpropertySyncConfigsService) Patch(name string, ...) *PropertiesSubpropertySyncConfigsPatchCall
type PropertiesUpdateAttributionSettingsCall
func (c *PropertiesUpdateAttributionSettingsCall) Context(ctx context.Context) *PropertiesUpdateAttributionSettingsCall
func (c *PropertiesUpdateAttributionSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAttributionSettings, error)
func (c *PropertiesUpdateAttributionSettingsCall) Fields(s ...googleapi.Field) *PropertiesUpdateAttributionSettingsCall
func (c *PropertiesUpdateAttributionSettingsCall) Header() http.Header
func (c *PropertiesUpdateAttributionSettingsCall) UpdateMask(updateMask string) *PropertiesUpdateAttributionSettingsCall
type PropertiesUpdateDataRetentionSettingsCall
func (c *PropertiesUpdateDataRetentionSettingsCall) Context(ctx context.Context) *PropertiesUpdateDataRetentionSettingsCall
func (c *PropertiesUpdateDataRetentionSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaDataRetentionSettings, error)
func (c *PropertiesUpdateDataRetentionSettingsCall) Fields(s ...googleapi.Field) *PropertiesUpdateDataRetentionSettingsCall
func (c *PropertiesUpdateDataRetentionSettingsCall) Header() http.Header
func (c *PropertiesUpdateDataRetentionSettingsCall) UpdateMask(updateMask string) *PropertiesUpdateDataRetentionSettingsCall
type PropertiesUpdateGoogleSignalsSettingsCall
func (c *PropertiesUpdateGoogleSignalsSettingsCall) Context(ctx context.Context) *PropertiesUpdateGoogleSignalsSettingsCall
func (c *PropertiesUpdateGoogleSignalsSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaGoogleSignalsSettings, error)
func (c *PropertiesUpdateGoogleSignalsSettingsCall) Fields(s ...googleapi.Field) *PropertiesUpdateGoogleSignalsSettingsCall
func (c *PropertiesUpdateGoogleSignalsSettingsCall) Header() http.Header
func (c *PropertiesUpdateGoogleSignalsSettingsCall) UpdateMask(updateMask string) *PropertiesUpdateGoogleSignalsSettingsCall
type Service
func New(client *http.Client) (*Service, error)DEPRECATED
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)
Constants ¶
View Source
const (
	// Edit Google Analytics management entities
	AnalyticsEditScope = "https://www.googleapis.com/auth/analytics.edit"

	// Manage Google Analytics Account users by email address
	AnalyticsManageUsersScope = "https://www.googleapis.com/auth/analytics.manage.users"

	// View Google Analytics user permissions
	AnalyticsManageUsersReadonlyScope = "https://www.googleapis.com/auth/analytics.manage.users.readonly"

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
func (c *AccountSummariesListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListAccountSummariesResponse, error)

Do executes the "analyticsadmin.accountSummaries.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaListAccountSummariesResponse.ServerResponse.Heade r or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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
func (c *AccountSummariesListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1alphaListAccountSummariesResponse) error) error

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

type AccountsAccessBindingsBatchCreateCall ¶
added in v0.110.0
type AccountsAccessBindingsBatchCreateCall struct {
	// contains filtered or unexported fields
}
func (*AccountsAccessBindingsBatchCreateCall) Context ¶
added in v0.110.0
func (c *AccountsAccessBindingsBatchCreateCall) Context(ctx context.Context) *AccountsAccessBindingsBatchCreateCall

Context sets the context to be used in this call's Do method.

func (*AccountsAccessBindingsBatchCreateCall) Do ¶
added in v0.110.0
func (c *AccountsAccessBindingsBatchCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsResponse, error)

Do executes the "analyticsadmin.accounts.accessBindings.batchCreate" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsResponse.ServerResponse. Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsAccessBindingsBatchCreateCall) Fields ¶
added in v0.110.0
func (c *AccountsAccessBindingsBatchCreateCall) Fields(s ...googleapi.Field) *AccountsAccessBindingsBatchCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsAccessBindingsBatchCreateCall) Header ¶
added in v0.110.0
func (c *AccountsAccessBindingsBatchCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsAccessBindingsBatchDeleteCall ¶
added in v0.110.0
type AccountsAccessBindingsBatchDeleteCall struct {
	// contains filtered or unexported fields
}
func (*AccountsAccessBindingsBatchDeleteCall) Context ¶
added in v0.110.0
func (c *AccountsAccessBindingsBatchDeleteCall) Context(ctx context.Context) *AccountsAccessBindingsBatchDeleteCall

Context sets the context to be used in this call's Do method.

func (*AccountsAccessBindingsBatchDeleteCall) Do ¶
added in v0.110.0
func (c *AccountsAccessBindingsBatchDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.accounts.accessBindings.batchDelete" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsAccessBindingsBatchDeleteCall) Fields ¶
added in v0.110.0
func (c *AccountsAccessBindingsBatchDeleteCall) Fields(s ...googleapi.Field) *AccountsAccessBindingsBatchDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsAccessBindingsBatchDeleteCall) Header ¶
added in v0.110.0
func (c *AccountsAccessBindingsBatchDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsAccessBindingsBatchGetCall ¶
added in v0.110.0
type AccountsAccessBindingsBatchGetCall struct {
	// contains filtered or unexported fields
}
func (*AccountsAccessBindingsBatchGetCall) Context ¶
added in v0.110.0
func (c *AccountsAccessBindingsBatchGetCall) Context(ctx context.Context) *AccountsAccessBindingsBatchGetCall

Context sets the context to be used in this call's Do method.

func (*AccountsAccessBindingsBatchGetCall) Do ¶
added in v0.110.0
func (c *AccountsAccessBindingsBatchGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaBatchGetAccessBindingsResponse, error)

Do executes the "analyticsadmin.accounts.accessBindings.batchGet" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaBatchGetAccessBindingsResponse.ServerResponse.Hea der or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsAccessBindingsBatchGetCall) Fields ¶
added in v0.110.0
func (c *AccountsAccessBindingsBatchGetCall) Fields(s ...googleapi.Field) *AccountsAccessBindingsBatchGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsAccessBindingsBatchGetCall) Header ¶
added in v0.110.0
func (c *AccountsAccessBindingsBatchGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccountsAccessBindingsBatchGetCall) IfNoneMatch ¶
added in v0.110.0
func (c *AccountsAccessBindingsBatchGetCall) IfNoneMatch(entityTag string) *AccountsAccessBindingsBatchGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*AccountsAccessBindingsBatchGetCall) Names ¶
added in v0.110.0
func (c *AccountsAccessBindingsBatchGetCall) Names(names ...string) *AccountsAccessBindingsBatchGetCall

Names sets the optional parameter "names": Required. The names of the access bindings to retrieve. A maximum of 1000 access bindings can be retrieved in a batch. Formats: - accounts/{account}/accessBindings/{accessBinding} - properties/{property}/accessBindings/{accessBinding}

type AccountsAccessBindingsBatchUpdateCall ¶
added in v0.110.0
type AccountsAccessBindingsBatchUpdateCall struct {
	// contains filtered or unexported fields
}
func (*AccountsAccessBindingsBatchUpdateCall) Context ¶
added in v0.110.0
func (c *AccountsAccessBindingsBatchUpdateCall) Context(ctx context.Context) *AccountsAccessBindingsBatchUpdateCall

Context sets the context to be used in this call's Do method.

func (*AccountsAccessBindingsBatchUpdateCall) Do ¶
added in v0.110.0
func (c *AccountsAccessBindingsBatchUpdateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsResponse, error)

Do executes the "analyticsadmin.accounts.accessBindings.batchUpdate" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsResponse.ServerResponse. Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsAccessBindingsBatchUpdateCall) Fields ¶
added in v0.110.0
func (c *AccountsAccessBindingsBatchUpdateCall) Fields(s ...googleapi.Field) *AccountsAccessBindingsBatchUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsAccessBindingsBatchUpdateCall) Header ¶
added in v0.110.0
func (c *AccountsAccessBindingsBatchUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsAccessBindingsCreateCall ¶
added in v0.110.0
type AccountsAccessBindingsCreateCall struct {
	// contains filtered or unexported fields
}
func (*AccountsAccessBindingsCreateCall) Context ¶
added in v0.110.0
func (c *AccountsAccessBindingsCreateCall) Context(ctx context.Context) *AccountsAccessBindingsCreateCall

Context sets the context to be used in this call's Do method.

func (*AccountsAccessBindingsCreateCall) Do ¶
added in v0.110.0
func (c *AccountsAccessBindingsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAccessBinding, error)

Do executes the "analyticsadmin.accounts.accessBindings.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaAccessBinding.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsAccessBindingsCreateCall) Fields ¶
added in v0.110.0
func (c *AccountsAccessBindingsCreateCall) Fields(s ...googleapi.Field) *AccountsAccessBindingsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsAccessBindingsCreateCall) Header ¶
added in v0.110.0
func (c *AccountsAccessBindingsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsAccessBindingsDeleteCall ¶
added in v0.110.0
type AccountsAccessBindingsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*AccountsAccessBindingsDeleteCall) Context ¶
added in v0.110.0
func (c *AccountsAccessBindingsDeleteCall) Context(ctx context.Context) *AccountsAccessBindingsDeleteCall

Context sets the context to be used in this call's Do method.

func (*AccountsAccessBindingsDeleteCall) Do ¶
added in v0.110.0
func (c *AccountsAccessBindingsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.accounts.accessBindings.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsAccessBindingsDeleteCall) Fields ¶
added in v0.110.0
func (c *AccountsAccessBindingsDeleteCall) Fields(s ...googleapi.Field) *AccountsAccessBindingsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsAccessBindingsDeleteCall) Header ¶
added in v0.110.0
func (c *AccountsAccessBindingsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsAccessBindingsGetCall ¶
added in v0.110.0
type AccountsAccessBindingsGetCall struct {
	// contains filtered or unexported fields
}
func (*AccountsAccessBindingsGetCall) Context ¶
added in v0.110.0
func (c *AccountsAccessBindingsGetCall) Context(ctx context.Context) *AccountsAccessBindingsGetCall

Context sets the context to be used in this call's Do method.

func (*AccountsAccessBindingsGetCall) Do ¶
added in v0.110.0
func (c *AccountsAccessBindingsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAccessBinding, error)

Do executes the "analyticsadmin.accounts.accessBindings.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaAccessBinding.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsAccessBindingsGetCall) Fields ¶
added in v0.110.0
func (c *AccountsAccessBindingsGetCall) Fields(s ...googleapi.Field) *AccountsAccessBindingsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsAccessBindingsGetCall) Header ¶
added in v0.110.0
func (c *AccountsAccessBindingsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccountsAccessBindingsGetCall) IfNoneMatch ¶
added in v0.110.0
func (c *AccountsAccessBindingsGetCall) IfNoneMatch(entityTag string) *AccountsAccessBindingsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AccountsAccessBindingsListCall ¶
added in v0.110.0
type AccountsAccessBindingsListCall struct {
	// contains filtered or unexported fields
}
func (*AccountsAccessBindingsListCall) Context ¶
added in v0.110.0
func (c *AccountsAccessBindingsListCall) Context(ctx context.Context) *AccountsAccessBindingsListCall

Context sets the context to be used in this call's Do method.

func (*AccountsAccessBindingsListCall) Do ¶
added in v0.110.0
func (c *AccountsAccessBindingsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListAccessBindingsResponse, error)

Do executes the "analyticsadmin.accounts.accessBindings.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaListAccessBindingsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsAccessBindingsListCall) Fields ¶
added in v0.110.0
func (c *AccountsAccessBindingsListCall) Fields(s ...googleapi.Field) *AccountsAccessBindingsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsAccessBindingsListCall) Header ¶
added in v0.110.0
func (c *AccountsAccessBindingsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccountsAccessBindingsListCall) IfNoneMatch ¶
added in v0.110.0
func (c *AccountsAccessBindingsListCall) IfNoneMatch(entityTag string) *AccountsAccessBindingsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*AccountsAccessBindingsListCall) PageSize ¶
added in v0.110.0
func (c *AccountsAccessBindingsListCall) PageSize(pageSize int64) *AccountsAccessBindingsListCall

PageSize sets the optional parameter "pageSize": The maximum number of access bindings to return. The service may return fewer than this value. If unspecified, at most 200 access bindings will be returned. The maximum value is 500; values above 500 will be coerced to 500.

func (*AccountsAccessBindingsListCall) PageToken ¶
added in v0.110.0
func (c *AccountsAccessBindingsListCall) PageToken(pageToken string) *AccountsAccessBindingsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListAccessBindings` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListAccessBindings` must match the call that provided the page token.

func (*AccountsAccessBindingsListCall) Pages ¶
added in v0.110.0
func (c *AccountsAccessBindingsListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1alphaListAccessBindingsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsAccessBindingsPatchCall ¶
added in v0.110.0
type AccountsAccessBindingsPatchCall struct {
	// contains filtered or unexported fields
}
func (*AccountsAccessBindingsPatchCall) Context ¶
added in v0.110.0
func (c *AccountsAccessBindingsPatchCall) Context(ctx context.Context) *AccountsAccessBindingsPatchCall

Context sets the context to be used in this call's Do method.

func (*AccountsAccessBindingsPatchCall) Do ¶
added in v0.110.0
func (c *AccountsAccessBindingsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAccessBinding, error)

Do executes the "analyticsadmin.accounts.accessBindings.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaAccessBinding.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsAccessBindingsPatchCall) Fields ¶
added in v0.110.0
func (c *AccountsAccessBindingsPatchCall) Fields(s ...googleapi.Field) *AccountsAccessBindingsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsAccessBindingsPatchCall) Header ¶
added in v0.110.0
func (c *AccountsAccessBindingsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsAccessBindingsService ¶
added in v0.110.0
type AccountsAccessBindingsService struct {
	// contains filtered or unexported fields
}
func NewAccountsAccessBindingsService ¶
added in v0.110.0
func NewAccountsAccessBindingsService(s *Service) *AccountsAccessBindingsService
func (*AccountsAccessBindingsService) BatchCreate ¶
added in v0.110.0
func (r *AccountsAccessBindingsService) BatchCreate(parent string, googleanalyticsadminv1alphabatchcreateaccessbindingsrequest *GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsRequest) *AccountsAccessBindingsBatchCreateCall

BatchCreate: Creates information about multiple access bindings to an account or property. This method is transactional. If any AccessBinding cannot be created, none of the AccessBindings will be created.

parent: The account or property that owns the access bindings. The parent field in the CreateAccessBindingRequest messages must either be empty or match this field. Formats: - accounts/{account} - properties/{property}.
func (*AccountsAccessBindingsService) BatchDelete ¶
added in v0.110.0
func (r *AccountsAccessBindingsService) BatchDelete(parent string, googleanalyticsadminv1alphabatchdeleteaccessbindingsrequest *GoogleAnalyticsAdminV1alphaBatchDeleteAccessBindingsRequest) *AccountsAccessBindingsBatchDeleteCall

BatchDelete: Deletes information about multiple users' links to an account or property.

parent: The account or property that owns the access bindings. The parent of all provided values for the 'names' field in DeleteAccessBindingRequest messages must match this field. Formats: - accounts/{account} - properties/{property}.
func (*AccountsAccessBindingsService) BatchGet ¶
added in v0.110.0
func (r *AccountsAccessBindingsService) BatchGet(parent string) *AccountsAccessBindingsBatchGetCall

BatchGet: Gets information about multiple access bindings to an account or property.

parent: The account or property that owns the access bindings. The parent of all provided values for the 'names' field must match this field. Formats: - accounts/{account} - properties/{property}.
func (*AccountsAccessBindingsService) BatchUpdate ¶
added in v0.110.0
func (r *AccountsAccessBindingsService) BatchUpdate(parent string, googleanalyticsadminv1alphabatchupdateaccessbindingsrequest *GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsRequest) *AccountsAccessBindingsBatchUpdateCall

BatchUpdate: Updates information about multiple access bindings to an account or property.

parent: The account or property that owns the access bindings. The parent of all provided AccessBinding in UpdateAccessBindingRequest messages must match this field. Formats: - accounts/{account} - properties/{property}.
func (*AccountsAccessBindingsService) Create ¶
added in v0.110.0
func (r *AccountsAccessBindingsService) Create(parent string, googleanalyticsadminv1alphaaccessbinding *GoogleAnalyticsAdminV1alphaAccessBinding) *AccountsAccessBindingsCreateCall

Create: Creates an access binding on an account or property.

- parent: Formats: - accounts/{account} - properties/{property}.

func (*AccountsAccessBindingsService) Delete ¶
added in v0.110.0
func (r *AccountsAccessBindingsService) Delete(name string) *AccountsAccessBindingsDeleteCall

Delete: Deletes an access binding on an account or property.

name: Formats: - accounts/{account}/accessBindings/{accessBinding} - properties/{property}/accessBindings/{accessBinding}.
func (*AccountsAccessBindingsService) Get ¶
added in v0.110.0
func (r *AccountsAccessBindingsService) Get(name string) *AccountsAccessBindingsGetCall

Get: Gets information about an access binding.

name: The name of the access binding to retrieve. Formats: - accounts/{account}/accessBindings/{accessBinding} - properties/{property}/accessBindings/{accessBinding}.
func (*AccountsAccessBindingsService) List ¶
added in v0.110.0
func (r *AccountsAccessBindingsService) List(parent string) *AccountsAccessBindingsListCall

List: Lists all access bindings on an account or property.

- parent: Formats: - accounts/{account} - properties/{property}.

func (*AccountsAccessBindingsService) Patch ¶
added in v0.110.0
func (r *AccountsAccessBindingsService) Patch(name string, googleanalyticsadminv1alphaaccessbinding *GoogleAnalyticsAdminV1alphaAccessBinding) *AccountsAccessBindingsPatchCall

Patch: Updates an access binding on an account or property.

name: Output only. Resource name of this binding. Format: accounts/{account}/accessBindings/{access_binding} or properties/{property}/accessBindings/{access_binding} Example: "accounts/100/accessBindings/200".
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
func (c *AccountsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAccount, error)

Do executes the "analyticsadmin.accounts.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaAccount.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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
func (c *AccountsGetDataSharingSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaDataSharingSettings, error)

Do executes the "analyticsadmin.accounts.getDataSharingSettings" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaDataSharingSettings.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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
func (c *AccountsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListAccountsResponse, error)

Do executes the "analyticsadmin.accounts.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaListAccountsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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
func (c *AccountsListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1alphaListAccountsResponse) error) error

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
func (c *AccountsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAccount, error)

Do executes the "analyticsadmin.accounts.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaAccount.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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
func (c *AccountsProvisionAccountTicketCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaProvisionAccountTicketResponse, error)

Do executes the "analyticsadmin.accounts.provisionAccountTicket" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaProvisionAccountTicketResponse.ServerResponse.Hea der or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsProvisionAccountTicketCall) Fields ¶
func (c *AccountsProvisionAccountTicketCall) Fields(s ...googleapi.Field) *AccountsProvisionAccountTicketCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsProvisionAccountTicketCall) Header ¶
func (c *AccountsProvisionAccountTicketCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsRunAccessReportCall ¶
added in v0.111.0
type AccountsRunAccessReportCall struct {
	// contains filtered or unexported fields
}
func (*AccountsRunAccessReportCall) Context ¶
added in v0.111.0
func (c *AccountsRunAccessReportCall) Context(ctx context.Context) *AccountsRunAccessReportCall

Context sets the context to be used in this call's Do method.

func (*AccountsRunAccessReportCall) Do ¶
added in v0.111.0
func (c *AccountsRunAccessReportCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaRunAccessReportResponse, error)

Do executes the "analyticsadmin.accounts.runAccessReport" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaRunAccessReportResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsRunAccessReportCall) Fields ¶
added in v0.111.0
func (c *AccountsRunAccessReportCall) Fields(s ...googleapi.Field) *AccountsRunAccessReportCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsRunAccessReportCall) Header ¶
added in v0.111.0
func (c *AccountsRunAccessReportCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsSearchChangeHistoryEventsCall ¶
added in v0.41.0
type AccountsSearchChangeHistoryEventsCall struct {
	// contains filtered or unexported fields
}
func (*AccountsSearchChangeHistoryEventsCall) Context ¶
added in v0.41.0
func (c *AccountsSearchChangeHistoryEventsCall) Context(ctx context.Context) *AccountsSearchChangeHistoryEventsCall

Context sets the context to be used in this call's Do method.

func (*AccountsSearchChangeHistoryEventsCall) Do ¶
added in v0.41.0
func (c *AccountsSearchChangeHistoryEventsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsResponse, error)

Do executes the "analyticsadmin.accounts.searchChangeHistoryEvents" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsResponse.ServerResponse. Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsSearchChangeHistoryEventsCall) Fields ¶
added in v0.41.0
func (c *AccountsSearchChangeHistoryEventsCall) Fields(s ...googleapi.Field) *AccountsSearchChangeHistoryEventsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccountsSearchChangeHistoryEventsCall) Header ¶
added in v0.41.0
func (c *AccountsSearchChangeHistoryEventsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccountsSearchChangeHistoryEventsCall) Pages ¶
added in v0.41.0
func (c *AccountsSearchChangeHistoryEventsCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsService ¶
type AccountsService struct {
	AccessBindings *AccountsAccessBindingsService
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
func (r *AccountsService) Patch(name string, googleanalyticsadminv1alphaaccount *GoogleAnalyticsAdminV1alphaAccount) *AccountsPatchCall

Patch: Updates an account.

name: Output only. Resource name of this account. Format: accounts/{account} Example: "accounts/100".
func (*AccountsService) ProvisionAccountTicket ¶
func (r *AccountsService) ProvisionAccountTicket(googleanalyticsadminv1alphaprovisionaccountticketrequest *GoogleAnalyticsAdminV1alphaProvisionAccountTicketRequest) *AccountsProvisionAccountTicketCall

ProvisionAccountTicket: Requests a ticket for creating an account.

func (*AccountsService) RunAccessReport ¶
added in v0.111.0
func (r *AccountsService) RunAccessReport(entity string, googleanalyticsadminv1alpharunaccessreportrequest *GoogleAnalyticsAdminV1alphaRunAccessReportRequest) *AccountsRunAccessReportCall

RunAccessReport: Returns a customized report of data access records. The report provides records of each time a user reads Google Analytics reporting data. Access records are retained for up to 2 years. Data Access Reports can be requested for a property. Reports may be requested for any property, but dimensions that aren't related to quota can only be requested on Google Analytics 360 properties. This method is only available to Administrators. These data access records include GA UI Reporting, GA UI Explorations, GA Data API, and other products like Firebase & Admob that can retrieve data from Google Analytics through a linkage. These records don't include property configuration changes like adding a stream or changing a property's time zone. For configuration change history, see searchChangeHistoryEvents (https://developers.google.com/analytics/devguides/config/admin/v1/rest/v1alpha/accounts/searchChangeHistoryEvents). To give your feedback on this API, complete the Google Analytics Access Reports feedback (https://docs.google.com/forms/d/e/1FAIpQLSdmEBUrMzAEdiEKk5TV5dEHvDUZDRlgWYdQdAeSdtR4hVjEhw/viewform) form.

entity: The Data Access Report supports requesting at the property level or account level. If requested at the account level, Data Access Reports include all access for all properties under that account. To request at the property level, entity should be for example 'properties/123' if "123" is your Google Analytics property ID. To request at the account level, entity should be for example 'accounts/1234' if "1234" is your Google Analytics Account ID.
func (*AccountsService) SearchChangeHistoryEvents ¶
added in v0.41.0
func (r *AccountsService) SearchChangeHistoryEvents(account string, googleanalyticsadminv1alphasearchchangehistoryeventsrequest *GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsRequest) *AccountsSearchChangeHistoryEventsCall

SearchChangeHistoryEvents: Searches through all changes to an account or its children given the specified set of filters. Only returns the subset of changes supported by the API. The UI may return additional changes.

account: The account resource for which to return change history resources. Format: accounts/{account} Example: `accounts/100`.
type GoogleAnalyticsAdminV1alphaAccessBetweenFilter ¶
added in v0.86.0
type GoogleAnalyticsAdminV1alphaAccessBetweenFilter struct {
	// FromValue: Begins with this number.
	FromValue *GoogleAnalyticsAdminV1alphaNumericValue `json:"fromValue,omitempty"`
	// ToValue: Ends with this number.
	ToValue *GoogleAnalyticsAdminV1alphaNumericValue `json:"toValue,omitempty"`
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

GoogleAnalyticsAdminV1alphaAccessBetweenFilter: To express that the result needs to be between two numbers (inclusive).

func (GoogleAnalyticsAdminV1alphaAccessBetweenFilter) MarshalJSON ¶
added in v0.86.0
func (s GoogleAnalyticsAdminV1alphaAccessBetweenFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessBinding ¶
added in v0.110.0
type GoogleAnalyticsAdminV1alphaAccessBinding struct {
	// Name: Output only. Resource name of this binding. Format:
	// accounts/{account}/accessBindings/{access_binding} or
	// properties/{property}/accessBindings/{access_binding} Example:
	// "accounts/100/accessBindings/200"
	Name string `json:"name,omitempty"`
	// Roles: A list of roles for to grant to the parent resource. Valid values:
	// predefinedRoles/viewer predefinedRoles/analyst predefinedRoles/editor
	// predefinedRoles/admin predefinedRoles/no-cost-data
	// predefinedRoles/no-revenue-data For users, if an empty list of roles is set,
	// this AccessBinding will be deleted.
	Roles []string `json:"roles,omitempty"`
	// User: If set, the email address of the user to set roles for. Format:
	// "someuser@gmail.com"
	User string `json:"user,omitempty"`

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

GoogleAnalyticsAdminV1alphaAccessBinding: A binding of a user to a set of roles.

func (GoogleAnalyticsAdminV1alphaAccessBinding) MarshalJSON ¶
added in v0.110.0
func (s GoogleAnalyticsAdminV1alphaAccessBinding) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessDateRange ¶
added in v0.86.0
type GoogleAnalyticsAdminV1alphaAccessDateRange struct {
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

GoogleAnalyticsAdminV1alphaAccessDateRange: A contiguous range of days: startDate, startDate + 1, ..., endDate.

func (GoogleAnalyticsAdminV1alphaAccessDateRange) MarshalJSON ¶
added in v0.86.0
func (s GoogleAnalyticsAdminV1alphaAccessDateRange) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessDimension ¶
added in v0.86.0
type GoogleAnalyticsAdminV1alphaAccessDimension struct {
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

GoogleAnalyticsAdminV1alphaAccessDimension: Dimensions are attributes of your data. For example, the dimension `userEmail` indicates the email of the user that accessed reporting data. Dimension values in report responses are strings.

func (GoogleAnalyticsAdminV1alphaAccessDimension) MarshalJSON ¶
added in v0.86.0
func (s GoogleAnalyticsAdminV1alphaAccessDimension) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessDimensionHeader ¶
added in v0.86.0
type GoogleAnalyticsAdminV1alphaAccessDimensionHeader struct {
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

GoogleAnalyticsAdminV1alphaAccessDimensionHeader: Describes a dimension column in the report. Dimensions requested in a report produce column entries within rows and DimensionHeaders. However, dimensions used exclusively within filters or expressions do not produce columns in a report; correspondingly, those dimensions do not produce headers.

func (GoogleAnalyticsAdminV1alphaAccessDimensionHeader) MarshalJSON ¶
added in v0.86.0
func (s GoogleAnalyticsAdminV1alphaAccessDimensionHeader) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessDimensionValue ¶
added in v0.86.0
type GoogleAnalyticsAdminV1alphaAccessDimensionValue struct {
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

GoogleAnalyticsAdminV1alphaAccessDimensionValue: The value of a dimension.

func (GoogleAnalyticsAdminV1alphaAccessDimensionValue) MarshalJSON ¶
added in v0.86.0
func (s GoogleAnalyticsAdminV1alphaAccessDimensionValue) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessFilter ¶
added in v0.86.0
type GoogleAnalyticsAdminV1alphaAccessFilter struct {
	// BetweenFilter: A filter for two values.
	BetweenFilter *GoogleAnalyticsAdminV1alphaAccessBetweenFilter `json:"betweenFilter,omitempty"`
	// FieldName: The dimension name or metric name.
	FieldName string `json:"fieldName,omitempty"`
	// InListFilter: A filter for in list values.
	InListFilter *GoogleAnalyticsAdminV1alphaAccessInListFilter `json:"inListFilter,omitempty"`
	// NumericFilter: A filter for numeric or date values.
	NumericFilter *GoogleAnalyticsAdminV1alphaAccessNumericFilter `json:"numericFilter,omitempty"`
	// StringFilter: Strings related filter.
	StringFilter *GoogleAnalyticsAdminV1alphaAccessStringFilter `json:"stringFilter,omitempty"`
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

GoogleAnalyticsAdminV1alphaAccessFilter: An expression to filter dimension or metric values.

func (GoogleAnalyticsAdminV1alphaAccessFilter) MarshalJSON ¶
added in v0.86.0
func (s GoogleAnalyticsAdminV1alphaAccessFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessFilterExpression ¶
added in v0.86.0
type GoogleAnalyticsAdminV1alphaAccessFilterExpression struct {
	// AccessFilter: A primitive filter. In the same FilterExpression, all of the
	// filter's field names need to be either all dimensions or all metrics.
	AccessFilter *GoogleAnalyticsAdminV1alphaAccessFilter `json:"accessFilter,omitempty"`
	// AndGroup: Each of the FilterExpressions in the and_group has an AND
	// relationship.
	AndGroup *GoogleAnalyticsAdminV1alphaAccessFilterExpressionList `json:"andGroup,omitempty"`
	// NotExpression: The FilterExpression is NOT of not_expression.
	NotExpression *GoogleAnalyticsAdminV1alphaAccessFilterExpression `json:"notExpression,omitempty"`
	// OrGroup: Each of the FilterExpressions in the or_group has an OR
	// relationship.
	OrGroup *GoogleAnalyticsAdminV1alphaAccessFilterExpressionList `json:"orGroup,omitempty"`
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

GoogleAnalyticsAdminV1alphaAccessFilterExpression: Expresses dimension or metric filters. The fields in the same expression need to be either all dimensions or all metrics.

func (GoogleAnalyticsAdminV1alphaAccessFilterExpression) MarshalJSON ¶
added in v0.86.0
func (s GoogleAnalyticsAdminV1alphaAccessFilterExpression) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessFilterExpressionList ¶
added in v0.86.0
type GoogleAnalyticsAdminV1alphaAccessFilterExpressionList struct {
	// Expressions: A list of filter expressions.
	Expressions []*GoogleAnalyticsAdminV1alphaAccessFilterExpression `json:"expressions,omitempty"`
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

GoogleAnalyticsAdminV1alphaAccessFilterExpressionList: A list of filter expressions.

func (GoogleAnalyticsAdminV1alphaAccessFilterExpressionList) MarshalJSON ¶
added in v0.86.0
func (s GoogleAnalyticsAdminV1alphaAccessFilterExpressionList) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessInListFilter ¶
added in v0.86.0
type GoogleAnalyticsAdminV1alphaAccessInListFilter struct {
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

GoogleAnalyticsAdminV1alphaAccessInListFilter: The result needs to be in a list of string values.

func (GoogleAnalyticsAdminV1alphaAccessInListFilter) MarshalJSON ¶
added in v0.86.0
func (s GoogleAnalyticsAdminV1alphaAccessInListFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessMetric ¶
added in v0.86.0
type GoogleAnalyticsAdminV1alphaAccessMetric struct {
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

GoogleAnalyticsAdminV1alphaAccessMetric: The quantitative measurements of a report. For example, the metric `accessCount` is the total number of data access records.

func (GoogleAnalyticsAdminV1alphaAccessMetric) MarshalJSON ¶
added in v0.86.0
func (s GoogleAnalyticsAdminV1alphaAccessMetric) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessMetricHeader ¶
added in v0.86.0
type GoogleAnalyticsAdminV1alphaAccessMetricHeader struct {
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

GoogleAnalyticsAdminV1alphaAccessMetricHeader: Describes a metric column in the report. Visible metrics requested in a report produce column entries within rows and MetricHeaders. However, metrics used exclusively within filters or expressions do not produce columns in a report; correspondingly, those metrics do not produce headers.

func (GoogleAnalyticsAdminV1alphaAccessMetricHeader) MarshalJSON ¶
added in v0.86.0
func (s GoogleAnalyticsAdminV1alphaAccessMetricHeader) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessMetricValue ¶
added in v0.86.0
type GoogleAnalyticsAdminV1alphaAccessMetricValue struct {
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

GoogleAnalyticsAdminV1alphaAccessMetricValue: The value of a metric.

func (GoogleAnalyticsAdminV1alphaAccessMetricValue) MarshalJSON ¶
added in v0.86.0
func (s GoogleAnalyticsAdminV1alphaAccessMetricValue) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessNumericFilter ¶
added in v0.86.0
type GoogleAnalyticsAdminV1alphaAccessNumericFilter struct {
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
	Value *GoogleAnalyticsAdminV1alphaNumericValue `json:"value,omitempty"`
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

GoogleAnalyticsAdminV1alphaAccessNumericFilter: Filters for numeric or date values.

func (GoogleAnalyticsAdminV1alphaAccessNumericFilter) MarshalJSON ¶
added in v0.86.0
func (s GoogleAnalyticsAdminV1alphaAccessNumericFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessOrderBy ¶
added in v0.86.0
type GoogleAnalyticsAdminV1alphaAccessOrderBy struct {
	// Desc: If true, sorts by descending order. If false or unspecified, sorts in
	// ascending order.
	Desc bool `json:"desc,omitempty"`
	// Dimension: Sorts results by a dimension's values.
	Dimension *GoogleAnalyticsAdminV1alphaAccessOrderByDimensionOrderBy `json:"dimension,omitempty"`
	// Metric: Sorts results by a metric's values.
	Metric *GoogleAnalyticsAdminV1alphaAccessOrderByMetricOrderBy `json:"metric,omitempty"`
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

GoogleAnalyticsAdminV1alphaAccessOrderBy: Order bys define how rows will be sorted in the response. For example, ordering rows by descending access count is one ordering, and ordering rows by the country string is a different ordering.

func (GoogleAnalyticsAdminV1alphaAccessOrderBy) MarshalJSON ¶
added in v0.86.0
func (s GoogleAnalyticsAdminV1alphaAccessOrderBy) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessOrderByDimensionOrderBy ¶
added in v0.86.0
type GoogleAnalyticsAdminV1alphaAccessOrderByDimensionOrderBy struct {
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

GoogleAnalyticsAdminV1alphaAccessOrderByDimensionOrderBy: Sorts by dimension values.

func (GoogleAnalyticsAdminV1alphaAccessOrderByDimensionOrderBy) MarshalJSON ¶
added in v0.86.0
func (s GoogleAnalyticsAdminV1alphaAccessOrderByDimensionOrderBy) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessOrderByMetricOrderBy ¶
added in v0.86.0
type GoogleAnalyticsAdminV1alphaAccessOrderByMetricOrderBy struct {
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

GoogleAnalyticsAdminV1alphaAccessOrderByMetricOrderBy: Sorts by metric values.

func (GoogleAnalyticsAdminV1alphaAccessOrderByMetricOrderBy) MarshalJSON ¶
added in v0.86.0
func (s GoogleAnalyticsAdminV1alphaAccessOrderByMetricOrderBy) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessQuota ¶
added in v0.86.0
type GoogleAnalyticsAdminV1alphaAccessQuota struct {
	// ConcurrentRequests: Properties can use up to 50 concurrent requests.
	ConcurrentRequests *GoogleAnalyticsAdminV1alphaAccessQuotaStatus `json:"concurrentRequests,omitempty"`
	// ServerErrorsPerProjectPerHour: Properties and cloud project pairs can have
	// up to 50 server errors per hour.
	ServerErrorsPerProjectPerHour *GoogleAnalyticsAdminV1alphaAccessQuotaStatus `json:"serverErrorsPerProjectPerHour,omitempty"`
	// TokensPerDay: Properties can use 250,000 tokens per day. Most requests
	// consume fewer than 10 tokens.
	TokensPerDay *GoogleAnalyticsAdminV1alphaAccessQuotaStatus `json:"tokensPerDay,omitempty"`
	// TokensPerHour: Properties can use 50,000 tokens per hour. An API request
	// consumes a single number of tokens, and that number is deducted from all of
	// the hourly, daily, and per project hourly quotas.
	TokensPerHour *GoogleAnalyticsAdminV1alphaAccessQuotaStatus `json:"tokensPerHour,omitempty"`
	// TokensPerProjectPerHour: Properties can use up to 25% of their tokens per
	// project per hour. This amounts to Analytics 360 Properties can use 12,500
	// tokens per project per hour. An API request consumes a single number of
	// tokens, and that number is deducted from all of the hourly, daily, and per
	// project hourly quotas.
	TokensPerProjectPerHour *GoogleAnalyticsAdminV1alphaAccessQuotaStatus `json:"tokensPerProjectPerHour,omitempty"`
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

GoogleAnalyticsAdminV1alphaAccessQuota: Current state of all quotas for this Analytics property. If any quota for a property is exhausted, all requests to that property will return Resource Exhausted errors.

func (GoogleAnalyticsAdminV1alphaAccessQuota) MarshalJSON ¶
added in v0.86.0
func (s GoogleAnalyticsAdminV1alphaAccessQuota) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessQuotaStatus ¶
added in v0.86.0
type GoogleAnalyticsAdminV1alphaAccessQuotaStatus struct {
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

GoogleAnalyticsAdminV1alphaAccessQuotaStatus: Current state for a particular quota group.

func (GoogleAnalyticsAdminV1alphaAccessQuotaStatus) MarshalJSON ¶
added in v0.86.0
func (s GoogleAnalyticsAdminV1alphaAccessQuotaStatus) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessRow ¶
added in v0.86.0
type GoogleAnalyticsAdminV1alphaAccessRow struct {
	// DimensionValues: List of dimension values. These values are in the same
	// order as specified in the request.
	DimensionValues []*GoogleAnalyticsAdminV1alphaAccessDimensionValue `json:"dimensionValues,omitempty"`
	// MetricValues: List of metric values. These values are in the same order as
	// specified in the request.
	MetricValues []*GoogleAnalyticsAdminV1alphaAccessMetricValue `json:"metricValues,omitempty"`
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

GoogleAnalyticsAdminV1alphaAccessRow: Access report data for each row.

func (GoogleAnalyticsAdminV1alphaAccessRow) MarshalJSON ¶
added in v0.86.0
func (s GoogleAnalyticsAdminV1alphaAccessRow) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccessStringFilter ¶
added in v0.86.0
type GoogleAnalyticsAdminV1alphaAccessStringFilter struct {
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

GoogleAnalyticsAdminV1alphaAccessStringFilter: The filter for strings.

func (GoogleAnalyticsAdminV1alphaAccessStringFilter) MarshalJSON ¶
added in v0.86.0
func (s GoogleAnalyticsAdminV1alphaAccessStringFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccount ¶
type GoogleAnalyticsAdminV1alphaAccount struct {
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

GoogleAnalyticsAdminV1alphaAccount: A resource message representing a Google Analytics account.

func (GoogleAnalyticsAdminV1alphaAccount) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1alphaAccount) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAccountSummary ¶
type GoogleAnalyticsAdminV1alphaAccountSummary struct {
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
	PropertySummaries []*GoogleAnalyticsAdminV1alphaPropertySummary `json:"propertySummaries,omitempty"`
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

GoogleAnalyticsAdminV1alphaAccountSummary: A virtual resource representing an overview of an account and all its child Google Analytics properties.

func (GoogleAnalyticsAdminV1alphaAccountSummary) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1alphaAccountSummary) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAcknowledgeUserDataCollectionRequest ¶
added in v0.59.0
type GoogleAnalyticsAdminV1alphaAcknowledgeUserDataCollectionRequest struct {
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

GoogleAnalyticsAdminV1alphaAcknowledgeUserDataCollectionRequest: Request message for AcknowledgeUserDataCollection RPC.

func (GoogleAnalyticsAdminV1alphaAcknowledgeUserDataCollectionRequest) MarshalJSON ¶
added in v0.59.0
func (s GoogleAnalyticsAdminV1alphaAcknowledgeUserDataCollectionRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAcknowledgeUserDataCollectionResponse ¶
added in v0.59.0
type GoogleAnalyticsAdminV1alphaAcknowledgeUserDataCollectionResponse struct {
	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
}

GoogleAnalyticsAdminV1alphaAcknowledgeUserDataCollectionResponse: Response message for AcknowledgeUserDataCollection RPC.

type GoogleAnalyticsAdminV1alphaAdSenseLink ¶
added in v0.123.0
type GoogleAnalyticsAdminV1alphaAdSenseLink struct {
	// AdClientCode: Immutable. The AdSense ad client code that the Google
	// Analytics property is linked to. Example format: "ca-pub-1234567890"
	AdClientCode string `json:"adClientCode,omitempty"`
	// Name: Output only. The resource name for this AdSense Link resource. Format:
	// properties/{propertyId}/adSenseLinks/{linkId} Example:
	// properties/1234/adSenseLinks/6789
	Name string `json:"name,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AdClientCode") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AdClientCode") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaAdSenseLink: A link between a Google Analytics property and an AdSense for Content ad client.

func (GoogleAnalyticsAdminV1alphaAdSenseLink) MarshalJSON ¶
added in v0.123.0
func (s GoogleAnalyticsAdminV1alphaAdSenseLink) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaApproveDisplayVideo360AdvertiserLinkProposalRequest ¶
added in v0.51.0
type GoogleAnalyticsAdminV1alphaApproveDisplayVideo360AdvertiserLinkProposalRequest struct {
}

GoogleAnalyticsAdminV1alphaApproveDisplayVideo360AdvertiserLinkProposalReques t: Request message for ApproveDisplayVideo360AdvertiserLinkProposal RPC.

type GoogleAnalyticsAdminV1alphaApproveDisplayVideo360AdvertiserLinkProposalResponse ¶
added in v0.51.0
type GoogleAnalyticsAdminV1alphaApproveDisplayVideo360AdvertiserLinkProposalResponse struct {
	// DisplayVideo360AdvertiserLink: The DisplayVideo360AdvertiserLink created as
	// a result of approving the proposal.
	DisplayVideo360AdvertiserLink *GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink `json:"displayVideo360AdvertiserLink,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g.
	// "DisplayVideo360AdvertiserLink") to unconditionally include in API requests.
	// By default, fields with empty or default values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields
	// for more details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DisplayVideo360AdvertiserLink")
	// to include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaApproveDisplayVideo360AdvertiserLinkProposalRespon se: Response message for ApproveDisplayVideo360AdvertiserLinkProposal RPC.

func (GoogleAnalyticsAdminV1alphaApproveDisplayVideo360AdvertiserLinkProposalResponse) MarshalJSON ¶
added in v0.51.0
func (s GoogleAnalyticsAdminV1alphaApproveDisplayVideo360AdvertiserLinkProposalResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaArchiveAudienceRequest ¶
added in v0.90.0
type GoogleAnalyticsAdminV1alphaArchiveAudienceRequest struct {
}

GoogleAnalyticsAdminV1alphaArchiveAudienceRequest: Request message for ArchiveAudience RPC.

type GoogleAnalyticsAdminV1alphaArchiveCustomDimensionRequest ¶
added in v0.47.0
type GoogleAnalyticsAdminV1alphaArchiveCustomDimensionRequest struct {
}

GoogleAnalyticsAdminV1alphaArchiveCustomDimensionRequest: Request message for ArchiveCustomDimension RPC.

type GoogleAnalyticsAdminV1alphaArchiveCustomMetricRequest ¶
added in v0.47.0
type GoogleAnalyticsAdminV1alphaArchiveCustomMetricRequest struct {
}

GoogleAnalyticsAdminV1alphaArchiveCustomMetricRequest: Request message for ArchiveCustomMetric RPC.

type GoogleAnalyticsAdminV1alphaAttributionSettings ¶
added in v0.84.0
type GoogleAnalyticsAdminV1alphaAttributionSettings struct {
	// AcquisitionConversionEventLookbackWindow: Required. The lookback window
	// configuration for acquisition conversion events. The default window size is
	// 30 days.
	//
	// Possible values:
	//   "ACQUISITION_CONVERSION_EVENT_LOOKBACK_WINDOW_UNSPECIFIED" - Lookback
	// window size unspecified.
	//   "ACQUISITION_CONVERSION_EVENT_LOOKBACK_WINDOW_7_DAYS" - 7-day lookback
	// window.
	//   "ACQUISITION_CONVERSION_EVENT_LOOKBACK_WINDOW_30_DAYS" - 30-day lookback
	// window.
	AcquisitionConversionEventLookbackWindow string `json:"acquisitionConversionEventLookbackWindow,omitempty"`
	// AdsWebConversionDataExportScope: Required. The Conversion Export Scope for
	// data exported to linked Ads Accounts.
	//
	// Possible values:
	//   "ADS_WEB_CONVERSION_DATA_EXPORT_SCOPE_UNSPECIFIED" - Default value. This
	// value is unused.
	//   "NOT_SELECTED_YET" - No data export scope selected yet. Export scope can
	// never be changed back to this value.
	//   "PAID_AND_ORGANIC_CHANNELS" - Paid and organic channels are eligible to
	// receive conversion credit, but only credit assigned to Google Ads channels
	// will appear in your Ads accounts. To learn more, see [Paid and Organic
	// channels](https://support.google.com/analytics/answer/10632359).
	//   "GOOGLE_PAID_CHANNELS" - Only Google Ads paid channels are eligible to
	// receive conversion credit. To learn more, see [Google Paid
	// channels](https://support.google.com/analytics/answer/10632359).
	AdsWebConversionDataExportScope string `json:"adsWebConversionDataExportScope,omitempty"`
	// Name: Output only. Resource name of this attribution settings resource.
	// Format: properties/{property_id}/attributionSettings Example:
	// "properties/1000/attributionSettings"
	Name string `json:"name,omitempty"`
	// OtherConversionEventLookbackWindow: Required. The lookback window for all
	// other, non-acquisition conversion events. The default window size is 90
	// days.
	//
	// Possible values:
	//   "OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_UNSPECIFIED" - Lookback window
	// size unspecified.
	//   "OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_30_DAYS" - 30-day lookback window.
	//   "OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_60_DAYS" - 60-day lookback window.
	//   "OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_90_DAYS" - 90-day lookback window.
	OtherConversionEventLookbackWindow string `json:"otherConversionEventLookbackWindow,omitempty"`
	// ReportingAttributionModel: Required. The reporting attribution model used to
	// calculate conversion credit in this property's reports. Changing the
	// attribution model will apply to both historical and future data. These
	// changes will be reflected in reports with conversion and revenue data. User
	// and session data will be unaffected.
	//
	// Possible values:
	//   "REPORTING_ATTRIBUTION_MODEL_UNSPECIFIED" - Reporting attribution model
	// unspecified.
	//   "PAID_AND_ORGANIC_CHANNELS_DATA_DRIVEN" - Data-driven attribution
	// distributes credit for the conversion based on data for each conversion
	// event. Each Data-driven model is specific to each advertiser and each
	// conversion event. Previously CROSS_CHANNEL_DATA_DRIVEN
	//   "PAID_AND_ORGANIC_CHANNELS_LAST_CLICK" - Ignores direct traffic and
	// attributes 100% of the conversion value to the last channel that the
	// customer clicked through (or engaged view through for YouTube) before
	// converting. Previously CROSS_CHANNEL_LAST_CLICK
	//   "GOOGLE_PAID_CHANNELS_LAST_CLICK" - Attributes 100% of the conversion
	// value to the last Google Paid channel that the customer clicked through
	// before converting. Previously ADS_PREFERRED_LAST_CLICK
	ReportingAttributionModel string `json:"reportingAttributionModel,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g.
	// "AcquisitionConversionEventLookbackWindow") to unconditionally include in
	// API requests. By default, fields with empty or default values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g.
	// "AcquisitionConversionEventLookbackWindow") to include in API requests with
	// the JSON null value. By default, fields with empty values are omitted from
	// API requests. See https://pkg.go.dev/google.golang.org/api#hdr-NullFields
	// for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaAttributionSettings: The attribution settings used for a given property. This is a singleton resource.

func (GoogleAnalyticsAdminV1alphaAttributionSettings) MarshalJSON ¶
added in v0.84.0
func (s GoogleAnalyticsAdminV1alphaAttributionSettings) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAudience ¶
added in v0.90.0
type GoogleAnalyticsAdminV1alphaAudience struct {
	// AdsPersonalizationEnabled: Output only. It is automatically set by GA to
	// false if this is an NPA Audience and is excluded from ads personalization.
	AdsPersonalizationEnabled bool `json:"adsPersonalizationEnabled,omitempty"`
	// CreateTime: Output only. Time when the Audience was created.
	CreateTime string `json:"createTime,omitempty"`
	// Description: Required. The description of the Audience.
	Description string `json:"description,omitempty"`
	// DisplayName: Required. The display name of the Audience.
	DisplayName string `json:"displayName,omitempty"`
	// EventTrigger: Optional. Specifies an event to log when a user joins the
	// Audience. If not set, no event is logged when a user joins the Audience.
	EventTrigger *GoogleAnalyticsAdminV1alphaAudienceEventTrigger `json:"eventTrigger,omitempty"`
	// ExclusionDurationMode: Immutable. Specifies how long an exclusion lasts for
	// users that meet the exclusion filter. It is applied to all EXCLUDE filter
	// clauses and is ignored when there is no EXCLUDE filter clause in the
	// Audience.
	//
	// Possible values:
	//   "AUDIENCE_EXCLUSION_DURATION_MODE_UNSPECIFIED" - Not specified.
	//   "EXCLUDE_TEMPORARILY" - Exclude users from the Audience during periods
	// when they meet the filter clause.
	//   "EXCLUDE_PERMANENTLY" - Exclude users from the Audience if they've ever
	// met the filter clause.
	ExclusionDurationMode string `json:"exclusionDurationMode,omitempty"`
	// FilterClauses: Required. Immutable. Unordered list. Filter clauses that
	// define the Audience. All clauses will be AND’ed together.
	FilterClauses []*GoogleAnalyticsAdminV1alphaAudienceFilterClause `json:"filterClauses,omitempty"`
	// MembershipDurationDays: Required. Immutable. The duration a user should stay
	// in an Audience. It cannot be set to more than 540 days.
	MembershipDurationDays int64 `json:"membershipDurationDays,omitempty"`
	// Name: Output only. The resource name for this Audience resource. Format:
	// properties/{propertyId}/audiences/{audienceId}
	Name string `json:"name,omitempty"`

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

GoogleAnalyticsAdminV1alphaAudience: A resource message representing an Audience.

func (GoogleAnalyticsAdminV1alphaAudience) MarshalJSON ¶
added in v0.90.0
func (s GoogleAnalyticsAdminV1alphaAudience) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilter ¶
added in v0.90.0
type GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilter struct {
	// AtAnyPointInTime: Optional. Indicates whether this filter needs dynamic
	// evaluation or not. If set to true, users join the Audience if they ever met
	// the condition (static evaluation). If unset or set to false, user evaluation
	// for an Audience is dynamic; users are added to an Audience when they meet
	// the conditions and then removed when they no longer meet them. This can only
	// be set when Audience scope is ACROSS_ALL_SESSIONS.
	AtAnyPointInTime bool `json:"atAnyPointInTime,omitempty"`
	// BetweenFilter: A filter for numeric or date values between certain values on
	// a dimension or metric.
	BetweenFilter *GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterBetweenFilter `json:"betweenFilter,omitempty"`
	// FieldName: Required. Immutable. The dimension name or metric name to filter.
	// If the field name refers to a custom dimension or metric, a scope prefix
	// will be added to the front of the custom dimensions or metric name. For more
	// on scope prefixes or custom dimensions/metrics, reference the [Google
	// Analytics Data API documentation]
	// (https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#custom_dimensions).
	FieldName string `json:"fieldName,omitempty"`
	// InAnyNDayPeriod: Optional. If set, specifies the time window for which to
	// evaluate data in number of days. If not set, then audience data is evaluated
	// against lifetime data (For example, infinite time window). For example, if
	// set to 1 day, only the current day's data is evaluated. The reference point
	// is the current day when at_any_point_in_time is unset or false. It can only
	// be set when Audience scope is ACROSS_ALL_SESSIONS and cannot be greater than
	// 60 days.
	InAnyNDayPeriod int64 `json:"inAnyNDayPeriod,omitempty"`
	// InListFilter: A filter for a string dimension that matches a particular list
	// of options.
	InListFilter *GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterInListFilter `json:"inListFilter,omitempty"`
	// NumericFilter: A filter for numeric or date values on a dimension or metric.
	NumericFilter *GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericFilter `json:"numericFilter,omitempty"`
	// StringFilter: A filter for a string-type dimension that matches a particular
	// pattern.
	StringFilter *GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterStringFilter `json:"stringFilter,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AtAnyPointInTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AtAnyPointInTime") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilter: A specific filter for a single dimension or metric.

func (GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilter) MarshalJSON ¶
added in v0.90.0
func (s GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterBetweenFilter ¶
added in v0.90.0
type GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterBetweenFilter struct {
	// FromValue: Required. Begins with this number, inclusive.
	FromValue *GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericValue `json:"fromValue,omitempty"`
	// ToValue: Required. Ends with this number, inclusive.
	ToValue *GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericValue `json:"toValue,omitempty"`
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

GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterBetweenFilter: A filter for numeric or date values between certain values on a dimension or metric.

func (GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterBetweenFilter) MarshalJSON ¶
added in v0.90.0
func (s GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterBetweenFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterInListFilter ¶
added in v0.90.0
type GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterInListFilter struct {
	// CaseSensitive: Optional. If true, the match is case-sensitive. If false, the
	// match is case-insensitive.
	CaseSensitive bool `json:"caseSensitive,omitempty"`
	// Values: Required. The list of possible string values to match against. Must
	// be non-empty.
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

GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterInListFilter: A filter for a string dimension that matches a particular list of options.

func (GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterInListFilter) MarshalJSON ¶
added in v0.90.0
func (s GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterInListFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericFilter ¶
added in v0.90.0
type GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericFilter struct {
	// Operation: Required. The operation applied to a numeric filter.
	//
	// Possible values:
	//   "OPERATION_UNSPECIFIED" - Unspecified.
	//   "EQUAL" - Equal.
	//   "LESS_THAN" - Less than.
	//   "GREATER_THAN" - Greater than.
	Operation string `json:"operation,omitempty"`
	// Value: Required. The numeric or date value to match against.
	Value *GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericValue `json:"value,omitempty"`
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

GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericFilter: A filter for numeric or date values on a dimension or metric.

func (GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericFilter) MarshalJSON ¶
added in v0.90.0
func (s GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericValue ¶
added in v0.90.0
type GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericValue struct {
	// DoubleValue: Double value.
	DoubleValue float64 `json:"doubleValue,omitempty"`
	// Int64Value: Integer value.
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

GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericValue: To represent a number.

func (GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericValue) MarshalJSON ¶
added in v0.90.0
func (s GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericValue) MarshalJSON() ([]byte, error)
func (*GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericValue) UnmarshalJSON ¶
added in v0.90.0
func (s *GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterNumericValue) UnmarshalJSON(data []byte) error
type GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterStringFilter ¶
added in v0.90.0
type GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterStringFilter struct {
	// CaseSensitive: Optional. If true, the match is case-sensitive. If false, the
	// match is case-insensitive.
	CaseSensitive bool `json:"caseSensitive,omitempty"`
	// MatchType: Required. The match type for the string filter.
	//
	// Possible values:
	//   "MATCH_TYPE_UNSPECIFIED" - Unspecified
	//   "EXACT" - Exact match of the string value.
	//   "BEGINS_WITH" - Begins with the string value.
	//   "ENDS_WITH" - Ends with the string value.
	//   "CONTAINS" - Contains the string value.
	//   "FULL_REGEXP" - Full regular expression matches with the string value.
	MatchType string `json:"matchType,omitempty"`
	// Value: Required. The string value to be matched against.
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

GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterStringFilter: A filter for a string-type dimension that matches a particular pattern.

func (GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterStringFilter) MarshalJSON ¶
added in v0.90.0
func (s GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilterStringFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAudienceEventFilter ¶
added in v0.90.0
type GoogleAnalyticsAdminV1alphaAudienceEventFilter struct {
	// EventName: Required. Immutable. The name of the event to match against.
	EventName string `json:"eventName,omitempty"`
	// EventParameterFilterExpression: Optional. If specified, this filter matches
	// events that match both the single event name and the parameter filter
	// expressions. AudienceEventFilter inside the parameter filter expression
	// cannot be set (For example, nested event filters are not supported). This
	// should be a single and_group of dimension_or_metric_filter or
	// not_expression; ANDs of ORs are not supported. Also, if it includes a filter
	// for "eventCount", only that one will be considered; all the other filters
	// will be ignored.
	EventParameterFilterExpression *GoogleAnalyticsAdminV1alphaAudienceFilterExpression `json:"eventParameterFilterExpression,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EventName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EventName") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaAudienceEventFilter: A filter that matches events of a single event name. If an event parameter is specified, only the subset of events that match both the single event name and the parameter filter expressions match this event filter.

func (GoogleAnalyticsAdminV1alphaAudienceEventFilter) MarshalJSON ¶
added in v0.90.0
func (s GoogleAnalyticsAdminV1alphaAudienceEventFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAudienceEventTrigger ¶
added in v0.90.0
type GoogleAnalyticsAdminV1alphaAudienceEventTrigger struct {
	// EventName: Required. The event name that will be logged.
	EventName string `json:"eventName,omitempty"`
	// LogCondition: Required. When to log the event.
	//
	// Possible values:
	//   "LOG_CONDITION_UNSPECIFIED" - Log condition is not specified.
	//   "AUDIENCE_JOINED" - The event should be logged only when a user is joined.
	//   "AUDIENCE_MEMBERSHIP_RENEWED" - The event should be logged whenever the
	// Audience condition is met, even if the user is already a member of the
	// Audience.
	LogCondition string `json:"logCondition,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EventName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EventName") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaAudienceEventTrigger: Specifies an event to log when a user joins the Audience.

func (GoogleAnalyticsAdminV1alphaAudienceEventTrigger) MarshalJSON ¶
added in v0.90.0
func (s GoogleAnalyticsAdminV1alphaAudienceEventTrigger) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAudienceFilterClause ¶
added in v0.90.0
type GoogleAnalyticsAdminV1alphaAudienceFilterClause struct {
	// ClauseType: Required. Specifies whether this is an include or exclude filter
	// clause.
	//
	// Possible values:
	//   "AUDIENCE_CLAUSE_TYPE_UNSPECIFIED" - Unspecified clause type.
	//   "INCLUDE" - Users will be included in the Audience if the filter clause is
	// met.
	//   "EXCLUDE" - Users will be excluded from the Audience if the filter clause
	// is met.
	ClauseType string `json:"clauseType,omitempty"`
	// SequenceFilter: Filters that must occur in a specific order for the user to
	// be a member of the Audience.
	SequenceFilter *GoogleAnalyticsAdminV1alphaAudienceSequenceFilter `json:"sequenceFilter,omitempty"`
	// SimpleFilter: A simple filter that a user must satisfy to be a member of the
	// Audience.
	SimpleFilter *GoogleAnalyticsAdminV1alphaAudienceSimpleFilter `json:"simpleFilter,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ClauseType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ClauseType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaAudienceFilterClause: A clause for defining either a simple or sequence filter. A filter can be inclusive (For example, users satisfying the filter clause are included in the Audience) or exclusive (For example, users satisfying the filter clause are excluded from the Audience).

func (GoogleAnalyticsAdminV1alphaAudienceFilterClause) MarshalJSON ¶
added in v0.90.0
func (s GoogleAnalyticsAdminV1alphaAudienceFilterClause) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAudienceFilterExpression ¶
added in v0.90.0
type GoogleAnalyticsAdminV1alphaAudienceFilterExpression struct {
	// AndGroup: A list of expressions to be AND’ed together. It can only contain
	// AudienceFilterExpressions with or_group. This must be set for the top level
	// AudienceFilterExpression.
	AndGroup *GoogleAnalyticsAdminV1alphaAudienceFilterExpressionList `json:"andGroup,omitempty"`
	// DimensionOrMetricFilter: A filter on a single dimension or metric. This
	// cannot be set on the top level AudienceFilterExpression.
	DimensionOrMetricFilter *GoogleAnalyticsAdminV1alphaAudienceDimensionOrMetricFilter `json:"dimensionOrMetricFilter,omitempty"`
	// EventFilter: Creates a filter that matches a specific event. This cannot be
	// set on the top level AudienceFilterExpression.
	EventFilter *GoogleAnalyticsAdminV1alphaAudienceEventFilter `json:"eventFilter,omitempty"`
	// NotExpression: A filter expression to be NOT'ed (For example, inverted,
	// complemented). It can only include a dimension_or_metric_filter. This cannot
	// be set on the top level AudienceFilterExpression.
	NotExpression *GoogleAnalyticsAdminV1alphaAudienceFilterExpression `json:"notExpression,omitempty"`
	// OrGroup: A list of expressions to OR’ed together. It cannot contain
	// AudienceFilterExpressions with and_group or or_group.
	OrGroup *GoogleAnalyticsAdminV1alphaAudienceFilterExpressionList `json:"orGroup,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AndGroup") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AndGroup") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaAudienceFilterExpression: A logical expression of Audience dimension, metric, or event filters.

func (GoogleAnalyticsAdminV1alphaAudienceFilterExpression) MarshalJSON ¶
added in v0.90.0
func (s GoogleAnalyticsAdminV1alphaAudienceFilterExpression) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAudienceFilterExpressionList ¶
added in v0.90.0
type GoogleAnalyticsAdminV1alphaAudienceFilterExpressionList struct {
	// FilterExpressions: A list of Audience filter expressions.
	FilterExpressions []*GoogleAnalyticsAdminV1alphaAudienceFilterExpression `json:"filterExpressions,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FilterExpressions") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FilterExpressions") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaAudienceFilterExpressionList: A list of Audience filter expressions.

func (GoogleAnalyticsAdminV1alphaAudienceFilterExpressionList) MarshalJSON ¶
added in v0.90.0
func (s GoogleAnalyticsAdminV1alphaAudienceFilterExpressionList) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAudienceSequenceFilter ¶
added in v0.90.0
type GoogleAnalyticsAdminV1alphaAudienceSequenceFilter struct {
	// Scope: Required. Immutable. Specifies the scope for this filter.
	//
	// Possible values:
	//   "AUDIENCE_FILTER_SCOPE_UNSPECIFIED" - Scope is not specified.
	//   "AUDIENCE_FILTER_SCOPE_WITHIN_SAME_EVENT" - User joins the Audience if the
	// filter condition is met within one event.
	//   "AUDIENCE_FILTER_SCOPE_WITHIN_SAME_SESSION" - User joins the Audience if
	// the filter condition is met within one session.
	//   "AUDIENCE_FILTER_SCOPE_ACROSS_ALL_SESSIONS" - User joins the Audience if
	// the filter condition is met by any event across any session.
	Scope string `json:"scope,omitempty"`
	// SequenceMaximumDuration: Optional. Defines the time period in which the
	// whole sequence must occur.
	SequenceMaximumDuration string `json:"sequenceMaximumDuration,omitempty"`
	// SequenceSteps: Required. An ordered sequence of steps. A user must complete
	// each step in order to join the sequence filter.
	SequenceSteps []*GoogleAnalyticsAdminV1alphaAudienceSequenceFilterAudienceSequenceStep `json:"sequenceSteps,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Scope") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Scope") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaAudienceSequenceFilter: Defines filters that must occur in a specific order for the user to be a member of the Audience.

func (GoogleAnalyticsAdminV1alphaAudienceSequenceFilter) MarshalJSON ¶
added in v0.90.0
func (s GoogleAnalyticsAdminV1alphaAudienceSequenceFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAudienceSequenceFilterAudienceSequenceStep ¶
added in v0.90.0
type GoogleAnalyticsAdminV1alphaAudienceSequenceFilterAudienceSequenceStep struct {
	// ConstraintDuration: Optional. When set, this step must be satisfied within
	// the constraint_duration of the previous step (For example, t[i] - t[i-1] <=
	// constraint_duration). If not set, there is no duration requirement (the
	// duration is effectively unlimited). It is ignored for the first step.
	ConstraintDuration string `json:"constraintDuration,omitempty"`
	// FilterExpression: Required. Immutable. A logical expression of Audience
	// dimension, metric, or event filters in each step.
	FilterExpression *GoogleAnalyticsAdminV1alphaAudienceFilterExpression `json:"filterExpression,omitempty"`
	// ImmediatelyFollows: Optional. If true, the event satisfying this step must
	// be the very next event after the event satisfying the last step. If unset or
	// false, this step indirectly follows the prior step; for example, there may
	// be events between the prior step and this step. It is ignored for the first
	// step.
	ImmediatelyFollows bool `json:"immediatelyFollows,omitempty"`
	// Scope: Required. Immutable. Specifies the scope for this step.
	//
	// Possible values:
	//   "AUDIENCE_FILTER_SCOPE_UNSPECIFIED" - Scope is not specified.
	//   "AUDIENCE_FILTER_SCOPE_WITHIN_SAME_EVENT" - User joins the Audience if the
	// filter condition is met within one event.
	//   "AUDIENCE_FILTER_SCOPE_WITHIN_SAME_SESSION" - User joins the Audience if
	// the filter condition is met within one session.
	//   "AUDIENCE_FILTER_SCOPE_ACROSS_ALL_SESSIONS" - User joins the Audience if
	// the filter condition is met by any event across any session.
	Scope string `json:"scope,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ConstraintDuration") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ConstraintDuration") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaAudienceSequenceFilterAudienceSequenceStep: A condition that must occur in the specified step order for this user to match the sequence.

func (GoogleAnalyticsAdminV1alphaAudienceSequenceFilterAudienceSequenceStep) MarshalJSON ¶
added in v0.90.0
func (s GoogleAnalyticsAdminV1alphaAudienceSequenceFilterAudienceSequenceStep) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaAudienceSimpleFilter ¶
added in v0.90.0
type GoogleAnalyticsAdminV1alphaAudienceSimpleFilter struct {
	// FilterExpression: Required. Immutable. A logical expression of Audience
	// dimension, metric, or event filters.
	FilterExpression *GoogleAnalyticsAdminV1alphaAudienceFilterExpression `json:"filterExpression,omitempty"`
	// Scope: Required. Immutable. Specifies the scope for this filter.
	//
	// Possible values:
	//   "AUDIENCE_FILTER_SCOPE_UNSPECIFIED" - Scope is not specified.
	//   "AUDIENCE_FILTER_SCOPE_WITHIN_SAME_EVENT" - User joins the Audience if the
	// filter condition is met within one event.
	//   "AUDIENCE_FILTER_SCOPE_WITHIN_SAME_SESSION" - User joins the Audience if
	// the filter condition is met within one session.
	//   "AUDIENCE_FILTER_SCOPE_ACROSS_ALL_SESSIONS" - User joins the Audience if
	// the filter condition is met by any event across any session.
	Scope string `json:"scope,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FilterExpression") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FilterExpression") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaAudienceSimpleFilter: Defines a simple filter that a user must satisfy to be a member of the Audience.

func (GoogleAnalyticsAdminV1alphaAudienceSimpleFilter) MarshalJSON ¶
added in v0.90.0
func (s GoogleAnalyticsAdminV1alphaAudienceSimpleFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsRequest ¶
added in v0.110.0
type GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsRequest struct {
	// Requests: Required. The requests specifying the access bindings to create. A
	// maximum of 1000 access bindings can be created in a batch.
	Requests []*GoogleAnalyticsAdminV1alphaCreateAccessBindingRequest `json:"requests,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Requests") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Requests") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsRequest: Request message for BatchCreateAccessBindings RPC.

func (GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsRequest) MarshalJSON ¶
added in v0.110.0
func (s GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsResponse ¶
added in v0.110.0
type GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsResponse struct {
	// AccessBindings: The access bindings created.
	AccessBindings []*GoogleAnalyticsAdminV1alphaAccessBinding `json:"accessBindings,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AccessBindings") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccessBindings") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsResponse: Response message for BatchCreateAccessBindings RPC.

func (GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsResponse) MarshalJSON ¶
added in v0.110.0
func (s GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaBatchDeleteAccessBindingsRequest ¶
added in v0.110.0
type GoogleAnalyticsAdminV1alphaBatchDeleteAccessBindingsRequest struct {
	// Requests: Required. The requests specifying the access bindings to delete. A
	// maximum of 1000 access bindings can be deleted in a batch.
	Requests []*GoogleAnalyticsAdminV1alphaDeleteAccessBindingRequest `json:"requests,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Requests") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Requests") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaBatchDeleteAccessBindingsRequest: Request message for BatchDeleteAccessBindings RPC.

func (GoogleAnalyticsAdminV1alphaBatchDeleteAccessBindingsRequest) MarshalJSON ¶
added in v0.110.0
func (s GoogleAnalyticsAdminV1alphaBatchDeleteAccessBindingsRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaBatchGetAccessBindingsResponse ¶
added in v0.110.0
type GoogleAnalyticsAdminV1alphaBatchGetAccessBindingsResponse struct {
	// AccessBindings: The requested access bindings.
	AccessBindings []*GoogleAnalyticsAdminV1alphaAccessBinding `json:"accessBindings,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AccessBindings") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccessBindings") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaBatchGetAccessBindingsResponse: Response message for BatchGetAccessBindings RPC.

func (GoogleAnalyticsAdminV1alphaBatchGetAccessBindingsResponse) MarshalJSON ¶
added in v0.110.0
func (s GoogleAnalyticsAdminV1alphaBatchGetAccessBindingsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsRequest ¶
added in v0.110.0
type GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsRequest struct {
	// Requests: Required. The requests specifying the access bindings to update. A
	// maximum of 1000 access bindings can be updated in a batch.
	Requests []*GoogleAnalyticsAdminV1alphaUpdateAccessBindingRequest `json:"requests,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Requests") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Requests") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsRequest: Request message for BatchUpdateAccessBindings RPC.

func (GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsRequest) MarshalJSON ¶
added in v0.110.0
func (s GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsResponse ¶
added in v0.110.0
type GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsResponse struct {
	// AccessBindings: The access bindings updated.
	AccessBindings []*GoogleAnalyticsAdminV1alphaAccessBinding `json:"accessBindings,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AccessBindings") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccessBindings") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsResponse: Response message for BatchUpdateAccessBindings RPC.

func (GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsResponse) MarshalJSON ¶
added in v0.110.0
func (s GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaBigQueryLink ¶
added in v0.104.0
type GoogleAnalyticsAdminV1alphaBigQueryLink struct {
	// CreateTime: Output only. Time when the link was created.
	CreateTime string `json:"createTime,omitempty"`
	// DailyExportEnabled: If set true, enables daily data export to the linked
	// Google Cloud project.
	DailyExportEnabled bool `json:"dailyExportEnabled,omitempty"`
	// DatasetLocation: Required. Immutable. The geographic location where the
	// created BigQuery dataset should reside. See
	// https://cloud.google.com/bigquery/docs/locations for supported locations.
	DatasetLocation string `json:"datasetLocation,omitempty"`
	// ExcludedEvents: The list of event names that will be excluded from exports.
	ExcludedEvents []string `json:"excludedEvents,omitempty"`
	// ExportStreams: The list of streams under the parent property for which data
	// will be exported. Format: properties/{property_id}/dataStreams/{stream_id}
	// Example: ['properties/1000/dataStreams/2000']
	ExportStreams []string `json:"exportStreams,omitempty"`
	// FreshDailyExportEnabled: If set true, enables fresh daily export to the
	// linked Google Cloud project.
	FreshDailyExportEnabled bool `json:"freshDailyExportEnabled,omitempty"`
	// IncludeAdvertisingId: If set true, exported data will include advertising
	// identifiers for mobile app streams.
	IncludeAdvertisingId bool `json:"includeAdvertisingId,omitempty"`
	// Name: Output only. Resource name of this BigQuery link. Format:
	// 'properties/{property_id}/bigQueryLinks/{bigquery_link_id}' Format:
	// 'properties/1234/bigQueryLinks/abc567'
	Name string `json:"name,omitempty"`
	// Project: Immutable. The linked Google Cloud project. When creating a
	// BigQueryLink, you may provide this resource name using either a project
	// number or project ID. Once this resource has been created, the returned
	// project will always have a project that contains a project number. Format:
	// 'projects/{project number}' Example: 'projects/1234'
	Project string `json:"project,omitempty"`
	// StreamingExportEnabled: If set true, enables streaming export to the linked
	// Google Cloud project.
	StreamingExportEnabled bool `json:"streamingExportEnabled,omitempty"`

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

GoogleAnalyticsAdminV1alphaBigQueryLink: A link between a Google Analytics property and BigQuery project.

func (GoogleAnalyticsAdminV1alphaBigQueryLink) MarshalJSON ¶
added in v0.104.0
func (s GoogleAnalyticsAdminV1alphaBigQueryLink) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaCalculatedMetric ¶
added in v0.157.0
type GoogleAnalyticsAdminV1alphaCalculatedMetric struct {
	// CalculatedMetricId: Output only. The ID to use for the calculated metric. In
	// the UI, this is referred to as the "API name." The calculated_metric_id is
	// used when referencing this calculated metric from external APIs. For
	// example, "calcMetric:{calculated_metric_id}".
	CalculatedMetricId string `json:"calculatedMetricId,omitempty"`
	// Description: Optional. Description for this calculated metric. Max length of
	// 4096 characters.
	Description string `json:"description,omitempty"`
	// DisplayName: Required. Display name for this calculated metric as shown in
	// the Google Analytics UI. Max length 82 characters.
	DisplayName string `json:"displayName,omitempty"`
	// Formula: Required. The calculated metric's definition. Maximum number of
	// unique referenced custom metrics is 5. Formulas supports the following
	// operations: + (addition), - (subtraction), - (negative), * (multiplication),
	// / (division), () (parenthesis). Any valid real numbers are acceptable that
	// fit in a Long (64bit integer) or a Double (64 bit floating point number).
	// Example formula: "( customEvent:parameter_name + cartPurchaseQuantity ) /
	// 2.0"
	Formula string `json:"formula,omitempty"`
	// InvalidMetricReference: Output only. If true, this calculated metric has a
	// invalid metric reference. Anything using a calculated metric with
	// invalid_metric_reference set to true may fail, produce warnings, or produce
	// unexpected results.
	InvalidMetricReference bool `json:"invalidMetricReference,omitempty"`
	// MetricUnit: Required. The type for the calculated metric's value.
	//
	// Possible values:
	//   "METRIC_UNIT_UNSPECIFIED" - MetricUnit unspecified or missing.
	//   "STANDARD" - This metric uses default units.
	//   "CURRENCY" - This metric measures a currency.
	//   "FEET" - This metric measures feet.
	//   "MILES" - This metric measures miles.
	//   "METERS" - This metric measures meters.
	//   "KILOMETERS" - This metric measures kilometers.
	//   "MILLISECONDS" - This metric measures milliseconds.
	//   "SECONDS" - This metric measures seconds.
	//   "MINUTES" - This metric measures minutes.
	//   "HOURS" - This metric measures hours.
	MetricUnit string `json:"metricUnit,omitempty"`
	// Name: Output only. Resource name for this CalculatedMetric. Format:
	// 'properties/{property_id}/calculatedMetrics/{calculated_metric_id}'
	Name string `json:"name,omitempty"`
	// RestrictedMetricType: Output only. Types of restricted data that this metric
	// contains.
	//
	// Possible values:
	//   "RESTRICTED_METRIC_TYPE_UNSPECIFIED" - Type unknown or unspecified.
	//   "COST_DATA" - Metric reports cost data.
	//   "REVENUE_DATA" - Metric reports revenue data.
	RestrictedMetricType []string `json:"restrictedMetricType,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "CalculatedMetricId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CalculatedMetricId") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaCalculatedMetric: A definition for a calculated metric.

func (GoogleAnalyticsAdminV1alphaCalculatedMetric) MarshalJSON ¶
added in v0.157.0
func (s GoogleAnalyticsAdminV1alphaCalculatedMetric) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaCancelDisplayVideo360AdvertiserLinkProposalRequest ¶
added in v0.51.0
type GoogleAnalyticsAdminV1alphaCancelDisplayVideo360AdvertiserLinkProposalRequest struct {
}

GoogleAnalyticsAdminV1alphaCancelDisplayVideo360AdvertiserLinkProposalRequest : Request message for CancelDisplayVideo360AdvertiserLinkProposal RPC.

type GoogleAnalyticsAdminV1alphaChangeHistoryChange ¶
added in v0.41.0
type GoogleAnalyticsAdminV1alphaChangeHistoryChange struct {
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
	ResourceAfterChange *GoogleAnalyticsAdminV1alphaChangeHistoryChangeChangeHistoryResource `json:"resourceAfterChange,omitempty"`
	// ResourceBeforeChange: Resource contents from before the change was made. If
	// this resource was created in this change, this field will be missing.
	ResourceBeforeChange *GoogleAnalyticsAdminV1alphaChangeHistoryChangeChangeHistoryResource `json:"resourceBeforeChange,omitempty"`
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

GoogleAnalyticsAdminV1alphaChangeHistoryChange: A description of a change to a single Google Analytics resource.

func (GoogleAnalyticsAdminV1alphaChangeHistoryChange) MarshalJSON ¶
added in v0.41.0
func (s GoogleAnalyticsAdminV1alphaChangeHistoryChange) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaChangeHistoryChangeChangeHistoryResource ¶
added in v0.41.0
type GoogleAnalyticsAdminV1alphaChangeHistoryChangeChangeHistoryResource struct {
	// Account: A snapshot of an Account resource in change history.
	Account *GoogleAnalyticsAdminV1alphaAccount `json:"account,omitempty"`
	// AdsenseLink: A snapshot of an AdSenseLink resource in change history.
	AdsenseLink *GoogleAnalyticsAdminV1alphaAdSenseLink `json:"adsenseLink,omitempty"`
	// AttributionSettings: A snapshot of AttributionSettings resource in change
	// history.
	AttributionSettings *GoogleAnalyticsAdminV1alphaAttributionSettings `json:"attributionSettings,omitempty"`
	// Audience: A snapshot of an Audience resource in change history.
	Audience *GoogleAnalyticsAdminV1alphaAudience `json:"audience,omitempty"`
	// BigqueryLink: A snapshot of a BigQuery link resource in change history.
	BigqueryLink *GoogleAnalyticsAdminV1alphaBigQueryLink `json:"bigqueryLink,omitempty"`
	// CalculatedMetric: A snapshot of a CalculatedMetric resource in change
	// history.
	CalculatedMetric *GoogleAnalyticsAdminV1alphaCalculatedMetric `json:"calculatedMetric,omitempty"`
	// ChannelGroup: A snapshot of a ChannelGroup resource in change history.
	ChannelGroup *GoogleAnalyticsAdminV1alphaChannelGroup `json:"channelGroup,omitempty"`
	// ConversionEvent: A snapshot of a ConversionEvent resource in change history.
	ConversionEvent *GoogleAnalyticsAdminV1alphaConversionEvent `json:"conversionEvent,omitempty"`
	// CustomDimension: A snapshot of a CustomDimension resource in change history.
	CustomDimension *GoogleAnalyticsAdminV1alphaCustomDimension `json:"customDimension,omitempty"`
	// CustomMetric: A snapshot of a CustomMetric resource in change history.
	CustomMetric *GoogleAnalyticsAdminV1alphaCustomMetric `json:"customMetric,omitempty"`
	// DataRedactionSettings: A snapshot of DataRedactionSettings resource in
	// change history.
	DataRedactionSettings *GoogleAnalyticsAdminV1alphaDataRedactionSettings `json:"dataRedactionSettings,omitempty"`
	// DataRetentionSettings: A snapshot of a data retention settings resource in
	// change history.
	DataRetentionSettings *GoogleAnalyticsAdminV1alphaDataRetentionSettings `json:"dataRetentionSettings,omitempty"`
	// DataStream: A snapshot of a DataStream resource in change history.
	DataStream *GoogleAnalyticsAdminV1alphaDataStream `json:"dataStream,omitempty"`
	// DisplayVideo360AdvertiserLink: A snapshot of a DisplayVideo360AdvertiserLink
	// resource in change history.
	DisplayVideo360AdvertiserLink *GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink `json:"displayVideo360AdvertiserLink,omitempty"`
	// DisplayVideo360AdvertiserLinkProposal: A snapshot of a
	// DisplayVideo360AdvertiserLinkProposal resource in change history.
	DisplayVideo360AdvertiserLinkProposal *GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal `json:"displayVideo360AdvertiserLinkProposal,omitempty"`
	// EnhancedMeasurementSettings: A snapshot of EnhancedMeasurementSettings
	// resource in change history.
	EnhancedMeasurementSettings *GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettings `json:"enhancedMeasurementSettings,omitempty"`
	// EventCreateRule: A snapshot of an EventCreateRule resource in change
	// history.
	EventCreateRule *GoogleAnalyticsAdminV1alphaEventCreateRule `json:"eventCreateRule,omitempty"`
	// ExpandedDataSet: A snapshot of an ExpandedDataSet resource in change
	// history.
	ExpandedDataSet *GoogleAnalyticsAdminV1alphaExpandedDataSet `json:"expandedDataSet,omitempty"`
	// FirebaseLink: A snapshot of a FirebaseLink resource in change history.
	FirebaseLink *GoogleAnalyticsAdminV1alphaFirebaseLink `json:"firebaseLink,omitempty"`
	// GoogleAdsLink: A snapshot of a GoogleAdsLink resource in change history.
	GoogleAdsLink *GoogleAnalyticsAdminV1alphaGoogleAdsLink `json:"googleAdsLink,omitempty"`
	// GoogleSignalsSettings: A snapshot of a GoogleSignalsSettings resource in
	// change history.
	GoogleSignalsSettings *GoogleAnalyticsAdminV1alphaGoogleSignalsSettings `json:"googleSignalsSettings,omitempty"`
	// KeyEvent: A snapshot of a KeyEvent resource in change history.
	KeyEvent *GoogleAnalyticsAdminV1alphaKeyEvent `json:"keyEvent,omitempty"`
	// MeasurementProtocolSecret: A snapshot of a MeasurementProtocolSecret
	// resource in change history.
	MeasurementProtocolSecret *GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret `json:"measurementProtocolSecret,omitempty"`
	// Property: A snapshot of a Property resource in change history.
	Property *GoogleAnalyticsAdminV1alphaProperty `json:"property,omitempty"`
	// ReportingDataAnnotation: A snapshot of a ReportingDataAnnotation resource in
	// change history.
	ReportingDataAnnotation *GoogleAnalyticsAdminV1alphaReportingDataAnnotation `json:"reportingDataAnnotation,omitempty"`
	// ReportingIdentitySettings: A snapshot of a ReportingIdentitySettings
	// resource in change history.
	ReportingIdentitySettings *GoogleAnalyticsAdminV1alphaReportingIdentitySettings `json:"reportingIdentitySettings,omitempty"`
	// SearchAds360Link: A snapshot of a SearchAds360Link resource in change
	// history.
	SearchAds360Link *GoogleAnalyticsAdminV1alphaSearchAds360Link `json:"searchAds360Link,omitempty"`
	// SkadnetworkConversionValueSchema: A snapshot of
	// SKAdNetworkConversionValueSchema resource in change history.
	SkadnetworkConversionValueSchema *GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchema `json:"skadnetworkConversionValueSchema,omitempty"`
	// SubpropertySyncConfig: A snapshot of a SubpropertySyncConfig resource in
	// change history.
	SubpropertySyncConfig *GoogleAnalyticsAdminV1alphaSubpropertySyncConfig `json:"subpropertySyncConfig,omitempty"`
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

GoogleAnalyticsAdminV1alphaChangeHistoryChangeChangeHistoryResource: A snapshot of a resource as before or after the result of a change in change history.

func (GoogleAnalyticsAdminV1alphaChangeHistoryChangeChangeHistoryResource) MarshalJSON ¶
added in v0.41.0
func (s GoogleAnalyticsAdminV1alphaChangeHistoryChangeChangeHistoryResource) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaChangeHistoryEvent ¶
added in v0.41.0
type GoogleAnalyticsAdminV1alphaChangeHistoryEvent struct {
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
	Changes []*GoogleAnalyticsAdminV1alphaChangeHistoryChange `json:"changes,omitempty"`
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

GoogleAnalyticsAdminV1alphaChangeHistoryEvent: A set of changes within a Google Analytics account or its child properties that resulted from the same cause. Common causes would be updates made in the Google Analytics UI, changes from customer support, or automatic Google Analytics system changes.

func (GoogleAnalyticsAdminV1alphaChangeHistoryEvent) MarshalJSON ¶
added in v0.41.0
func (s GoogleAnalyticsAdminV1alphaChangeHistoryEvent) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaChannelGroup ¶
added in v0.117.0
type GoogleAnalyticsAdminV1alphaChannelGroup struct {
	// Description: The description of the Channel Group. Max length of 256
	// characters.
	Description string `json:"description,omitempty"`
	// DisplayName: Required. The display name of the Channel Group. Max length of
	// 80 characters.
	DisplayName string `json:"displayName,omitempty"`
	// GroupingRule: Required. The grouping rules of channels. Maximum number of
	// rules is 50.
	GroupingRule []*GoogleAnalyticsAdminV1alphaGroupingRule `json:"groupingRule,omitempty"`
	// Name: Output only. The resource name for this Channel Group resource.
	// Format: properties/{property}/channelGroups/{channel_group}
	Name string `json:"name,omitempty"`
	// Primary: Optional. If true, this channel group will be used as the default
	// channel group for reports. Only one channel group can be set as `primary` at
	// any time. If the `primary` field gets set on a channel group, it will get
	// unset on the previous primary channel group. The Google Analytics predefined
	// channel group is the primary by default.
	Primary bool `json:"primary,omitempty"`
	// SystemDefined: Output only. If true, then this channel group is the Default
	// Channel Group predefined by Google Analytics. Display name and grouping
	// rules cannot be updated for this channel group.
	SystemDefined bool `json:"systemDefined,omitempty"`

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

GoogleAnalyticsAdminV1alphaChannelGroup: A resource message representing a Channel Group.

func (GoogleAnalyticsAdminV1alphaChannelGroup) MarshalJSON ¶
added in v0.117.0
func (s GoogleAnalyticsAdminV1alphaChannelGroup) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaChannelGroupFilter ¶
added in v0.117.0
type GoogleAnalyticsAdminV1alphaChannelGroupFilter struct {
	// FieldName: Required. Immutable. The dimension name to filter.
	FieldName string `json:"fieldName,omitempty"`
	// InListFilter: A filter for a string dimension that matches a particular list
	// of options.
	InListFilter *GoogleAnalyticsAdminV1alphaChannelGroupFilterInListFilter `json:"inListFilter,omitempty"`
	// StringFilter: A filter for a string-type dimension that matches a particular
	// pattern.
	StringFilter *GoogleAnalyticsAdminV1alphaChannelGroupFilterStringFilter `json:"stringFilter,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FieldName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FieldName") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaChannelGroupFilter: A specific filter for a single dimension.

func (GoogleAnalyticsAdminV1alphaChannelGroupFilter) MarshalJSON ¶
added in v0.117.0
func (s GoogleAnalyticsAdminV1alphaChannelGroupFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaChannelGroupFilterExpression ¶
added in v0.117.0
type GoogleAnalyticsAdminV1alphaChannelGroupFilterExpression struct {
	// AndGroup: A list of expressions to be AND’ed together. It can only contain
	// ChannelGroupFilterExpressions with or_group. This must be set for the top
	// level ChannelGroupFilterExpression.
	AndGroup *GoogleAnalyticsAdminV1alphaChannelGroupFilterExpressionList `json:"andGroup,omitempty"`
	// Filter: A filter on a single dimension. This cannot be set on the top level
	// ChannelGroupFilterExpression.
	Filter *GoogleAnalyticsAdminV1alphaChannelGroupFilter `json:"filter,omitempty"`
	// NotExpression: A filter expression to be NOT'ed (that is inverted,
	// complemented). It can only include a dimension_or_metric_filter. This cannot
	// be set on the top level ChannelGroupFilterExpression.
	NotExpression *GoogleAnalyticsAdminV1alphaChannelGroupFilterExpression `json:"notExpression,omitempty"`
	// OrGroup: A list of expressions to OR’ed together. It cannot contain
	// ChannelGroupFilterExpressions with and_group or or_group.
	OrGroup *GoogleAnalyticsAdminV1alphaChannelGroupFilterExpressionList `json:"orGroup,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AndGroup") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AndGroup") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaChannelGroupFilterExpression: A logical expression of Channel Group dimension filters.

func (GoogleAnalyticsAdminV1alphaChannelGroupFilterExpression) MarshalJSON ¶
added in v0.117.0
func (s GoogleAnalyticsAdminV1alphaChannelGroupFilterExpression) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaChannelGroupFilterExpressionList ¶
added in v0.117.0
type GoogleAnalyticsAdminV1alphaChannelGroupFilterExpressionList struct {
	// FilterExpressions: A list of Channel Group filter expressions.
	FilterExpressions []*GoogleAnalyticsAdminV1alphaChannelGroupFilterExpression `json:"filterExpressions,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FilterExpressions") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FilterExpressions") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaChannelGroupFilterExpressionList: A list of Channel Group filter expressions.

func (GoogleAnalyticsAdminV1alphaChannelGroupFilterExpressionList) MarshalJSON ¶
added in v0.117.0
func (s GoogleAnalyticsAdminV1alphaChannelGroupFilterExpressionList) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaChannelGroupFilterInListFilter ¶
added in v0.117.0
type GoogleAnalyticsAdminV1alphaChannelGroupFilterInListFilter struct {
	// Values: Required. The list of possible string values to match against. Must
	// be non-empty.
	Values []string `json:"values,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Values") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Values") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaChannelGroupFilterInListFilter: A filter for a string dimension that matches a particular list of options. The match is case insensitive.

func (GoogleAnalyticsAdminV1alphaChannelGroupFilterInListFilter) MarshalJSON ¶
added in v0.117.0
func (s GoogleAnalyticsAdminV1alphaChannelGroupFilterInListFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaChannelGroupFilterStringFilter ¶
added in v0.117.0
type GoogleAnalyticsAdminV1alphaChannelGroupFilterStringFilter struct {
	// MatchType: Required. The match type for the string filter.
	//
	// Possible values:
	//   "MATCH_TYPE_UNSPECIFIED" - Default match type.
	//   "EXACT" - Exact match of the string value.
	//   "BEGINS_WITH" - Begins with the string value.
	//   "ENDS_WITH" - Ends with the string value.
	//   "CONTAINS" - Contains the string value.
	//   "FULL_REGEXP" - Full regular expression match with the string value.
	//   "PARTIAL_REGEXP" - Partial regular expression match with the string value.
	MatchType string `json:"matchType,omitempty"`
	// Value: Required. The string value to be matched against.
	Value string `json:"value,omitempty"`
	// ForceSendFields is a list of field names (e.g. "MatchType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "MatchType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaChannelGroupFilterStringFilter: Filter where the field value is a String. The match is case insensitive.

func (GoogleAnalyticsAdminV1alphaChannelGroupFilterStringFilter) MarshalJSON ¶
added in v0.117.0
func (s GoogleAnalyticsAdminV1alphaChannelGroupFilterStringFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaConversionEvent ¶
added in v0.47.0
type GoogleAnalyticsAdminV1alphaConversionEvent struct {
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
	DefaultConversionValue *GoogleAnalyticsAdminV1alphaConversionEventDefaultConversionValue `json:"defaultConversionValue,omitempty"`
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

GoogleAnalyticsAdminV1alphaConversionEvent: A conversion event in a Google Analytics property.

func (GoogleAnalyticsAdminV1alphaConversionEvent) MarshalJSON ¶
added in v0.47.0
func (s GoogleAnalyticsAdminV1alphaConversionEvent) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaConversionEventDefaultConversionValue ¶
added in v0.149.0
type GoogleAnalyticsAdminV1alphaConversionEventDefaultConversionValue struct {
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

GoogleAnalyticsAdminV1alphaConversionEventDefaultConversionValue: Defines a default value/currency for a conversion event. Both value and currency must be provided.

func (GoogleAnalyticsAdminV1alphaConversionEventDefaultConversionValue) MarshalJSON ¶
added in v0.149.0
func (s GoogleAnalyticsAdminV1alphaConversionEventDefaultConversionValue) MarshalJSON() ([]byte, error)
func (*GoogleAnalyticsAdminV1alphaConversionEventDefaultConversionValue) UnmarshalJSON ¶
added in v0.149.0
func (s *GoogleAnalyticsAdminV1alphaConversionEventDefaultConversionValue) UnmarshalJSON(data []byte) error
type GoogleAnalyticsAdminV1alphaConversionValues ¶
added in v0.139.0
type GoogleAnalyticsAdminV1alphaConversionValues struct {
	// CoarseValue: Required. A coarse grained conversion value. This value is not
	// guaranteed to be unique.
	//
	// Possible values:
	//   "COARSE_VALUE_UNSPECIFIED" - Coarse value not specified.
	//   "COARSE_VALUE_LOW" - Coarse value of low.
	//   "COARSE_VALUE_MEDIUM" - Coarse value of medium.
	//   "COARSE_VALUE_HIGH" - Coarse value of high.
	CoarseValue string `json:"coarseValue,omitempty"`
	// DisplayName: Display name of the SKAdNetwork conversion value. The max
	// allowed display name length is 50 UTF-16 code units.
	DisplayName string `json:"displayName,omitempty"`
	// EventMappings: Event conditions that must be met for this Conversion Value
	// to be achieved. The conditions in this list are ANDed together. It must have
	// minimum of 1 entry and maximum of 3 entries, if the postback window is
	// enabled.
	EventMappings []*GoogleAnalyticsAdminV1alphaEventMapping `json:"eventMappings,omitempty"`
	// FineValue: The fine-grained conversion value. This is applicable only to the
	// first postback window. Its valid values are [0,63], both inclusive. It must
	// be set for postback window 1, and must not be set for postback window 2 & 3.
	// This value is not guaranteed to be unique. If the configuration for the
	// first postback window is re-used for second or third postback windows this
	// field has no effect.
	FineValue int64 `json:"fineValue,omitempty"`
	// LockEnabled: If true, the SDK should lock to this conversion value for the
	// current postback window.
	LockEnabled bool `json:"lockEnabled,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CoarseValue") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CoarseValue") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaConversionValues: Conversion value settings for a postback window for SKAdNetwork conversion value schema.

func (GoogleAnalyticsAdminV1alphaConversionValues) MarshalJSON ¶
added in v0.139.0
func (s GoogleAnalyticsAdminV1alphaConversionValues) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaCreateAccessBindingRequest ¶
added in v0.110.0
type GoogleAnalyticsAdminV1alphaCreateAccessBindingRequest struct {
	// AccessBinding: Required. The access binding to create.
	AccessBinding *GoogleAnalyticsAdminV1alphaAccessBinding `json:"accessBinding,omitempty"`
	// Parent: Required. Formats: - accounts/{account} - properties/{property}
	Parent string `json:"parent,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AccessBinding") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccessBinding") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaCreateAccessBindingRequest: Request message for CreateAccessBinding RPC.

func (GoogleAnalyticsAdminV1alphaCreateAccessBindingRequest) MarshalJSON ¶
added in v0.110.0
func (s GoogleAnalyticsAdminV1alphaCreateAccessBindingRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaCreateRollupPropertyRequest ¶
added in v0.144.0
type GoogleAnalyticsAdminV1alphaCreateRollupPropertyRequest struct {
	// RollupProperty: Required. The roll-up property to create.
	RollupProperty *GoogleAnalyticsAdminV1alphaProperty `json:"rollupProperty,omitempty"`
	// SourceProperties: Optional. The resource names of properties that will be
	// sources to the created roll-up property.
	SourceProperties []string `json:"sourceProperties,omitempty"`
	// ForceSendFields is a list of field names (e.g. "RollupProperty") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "RollupProperty") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaCreateRollupPropertyRequest: Request message for CreateRollupProperty RPC.

func (GoogleAnalyticsAdminV1alphaCreateRollupPropertyRequest) MarshalJSON ¶
added in v0.144.0
func (s GoogleAnalyticsAdminV1alphaCreateRollupPropertyRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaCreateRollupPropertyResponse ¶
added in v0.144.0
type GoogleAnalyticsAdminV1alphaCreateRollupPropertyResponse struct {
	// RollupProperty: The created roll-up property.
	RollupProperty *GoogleAnalyticsAdminV1alphaProperty `json:"rollupProperty,omitempty"`
	// RollupPropertySourceLinks: The created roll-up property source links.
	RollupPropertySourceLinks []*GoogleAnalyticsAdminV1alphaRollupPropertySourceLink `json:"rollupPropertySourceLinks,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "RollupProperty") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "RollupProperty") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaCreateRollupPropertyResponse: Response message for CreateRollupProperty RPC.

func (GoogleAnalyticsAdminV1alphaCreateRollupPropertyResponse) MarshalJSON ¶
added in v0.144.0
func (s GoogleAnalyticsAdminV1alphaCreateRollupPropertyResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaCustomDimension ¶
added in v0.47.0
type GoogleAnalyticsAdminV1alphaCustomDimension struct {
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

GoogleAnalyticsAdminV1alphaCustomDimension: A definition for a CustomDimension.

func (GoogleAnalyticsAdminV1alphaCustomDimension) MarshalJSON ¶
added in v0.47.0
func (s GoogleAnalyticsAdminV1alphaCustomDimension) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaCustomMetric ¶
added in v0.47.0
type GoogleAnalyticsAdminV1alphaCustomMetric struct {
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

GoogleAnalyticsAdminV1alphaCustomMetric: A definition for a custom metric.

func (GoogleAnalyticsAdminV1alphaCustomMetric) MarshalJSON ¶
added in v0.47.0
func (s GoogleAnalyticsAdminV1alphaCustomMetric) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaDataRedactionSettings ¶
added in v0.144.0
type GoogleAnalyticsAdminV1alphaDataRedactionSettings struct {
	// EmailRedactionEnabled: If enabled, any event parameter or user property
	// values that look like an email will be redacted.
	EmailRedactionEnabled bool `json:"emailRedactionEnabled,omitempty"`
	// Name: Output only. Name of this Data Redaction Settings resource. Format:
	// properties/{property_id}/dataStreams/{data_stream}/dataRedactionSettings
	// Example: "properties/1000/dataStreams/2000/dataRedactionSettings"
	Name string `json:"name,omitempty"`
	// QueryParameterKeys: The query parameter keys to apply redaction logic to if
	// present in the URL. Query parameter matching is case-insensitive. Must
	// contain at least one element if query_parameter_replacement_enabled is true.
	// Keys cannot contain commas.
	QueryParameterKeys []string `json:"queryParameterKeys,omitempty"`
	// QueryParameterRedactionEnabled: Query Parameter redaction removes the key
	// and value portions of a query parameter if it is in the configured set of
	// query parameters. If enabled, URL query replacement logic will be run for
	// the Stream. Any query parameters defined in query_parameter_keys will be
	// redacted.
	QueryParameterRedactionEnabled bool `json:"queryParameterRedactionEnabled,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "EmailRedactionEnabled") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EmailRedactionEnabled") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaDataRedactionSettings: Settings for client-side data redaction. Singleton resource under a Web Stream.

func (GoogleAnalyticsAdminV1alphaDataRedactionSettings) MarshalJSON ¶
added in v0.144.0
func (s GoogleAnalyticsAdminV1alphaDataRedactionSettings) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaDataRetentionSettings ¶
added in v0.55.0
type GoogleAnalyticsAdminV1alphaDataRetentionSettings struct {
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

GoogleAnalyticsAdminV1alphaDataRetentionSettings: Settings values for data retention. This is a singleton resource.

func (GoogleAnalyticsAdminV1alphaDataRetentionSettings) MarshalJSON ¶
added in v0.55.0
func (s GoogleAnalyticsAdminV1alphaDataRetentionSettings) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaDataSharingSettings ¶
type GoogleAnalyticsAdminV1alphaDataSharingSettings struct {
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

GoogleAnalyticsAdminV1alphaDataSharingSettings: A resource message representing data sharing settings of a Google Analytics account.

func (GoogleAnalyticsAdminV1alphaDataSharingSettings) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1alphaDataSharingSettings) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaDataStream ¶
added in v0.61.0
type GoogleAnalyticsAdminV1alphaDataStream struct {
	// AndroidAppStreamData: Data specific to Android app streams. Must be
	// populated if type is ANDROID_APP_DATA_STREAM.
	AndroidAppStreamData *GoogleAnalyticsAdminV1alphaDataStreamAndroidAppStreamData `json:"androidAppStreamData,omitempty"`
	// CreateTime: Output only. Time when this stream was originally created.
	CreateTime string `json:"createTime,omitempty"`
	// DisplayName: Human-readable display name for the Data Stream. Required for
	// web data streams. The max allowed display name length is 255 UTF-16 code
	// units.
	DisplayName string `json:"displayName,omitempty"`
	// IosAppStreamData: Data specific to iOS app streams. Must be populated if
	// type is IOS_APP_DATA_STREAM.
	IosAppStreamData *GoogleAnalyticsAdminV1alphaDataStreamIosAppStreamData `json:"iosAppStreamData,omitempty"`
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
	WebStreamData *GoogleAnalyticsAdminV1alphaDataStreamWebStreamData `json:"webStreamData,omitempty"`

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

GoogleAnalyticsAdminV1alphaDataStream: A resource message representing a data stream.

func (GoogleAnalyticsAdminV1alphaDataStream) MarshalJSON ¶
added in v0.61.0
func (s GoogleAnalyticsAdminV1alphaDataStream) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaDataStreamAndroidAppStreamData ¶
added in v0.61.0
type GoogleAnalyticsAdminV1alphaDataStreamAndroidAppStreamData struct {
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

GoogleAnalyticsAdminV1alphaDataStreamAndroidAppStreamData: Data specific to Android app streams.

func (GoogleAnalyticsAdminV1alphaDataStreamAndroidAppStreamData) MarshalJSON ¶
added in v0.61.0
func (s GoogleAnalyticsAdminV1alphaDataStreamAndroidAppStreamData) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaDataStreamIosAppStreamData ¶
added in v0.61.0
type GoogleAnalyticsAdminV1alphaDataStreamIosAppStreamData struct {
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

GoogleAnalyticsAdminV1alphaDataStreamIosAppStreamData: Data specific to iOS app streams.

func (GoogleAnalyticsAdminV1alphaDataStreamIosAppStreamData) MarshalJSON ¶
added in v0.61.0
func (s GoogleAnalyticsAdminV1alphaDataStreamIosAppStreamData) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaDataStreamWebStreamData ¶
added in v0.61.0
type GoogleAnalyticsAdminV1alphaDataStreamWebStreamData struct {
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

GoogleAnalyticsAdminV1alphaDataStreamWebStreamData: Data specific to web streams.

func (GoogleAnalyticsAdminV1alphaDataStreamWebStreamData) MarshalJSON ¶
added in v0.61.0
func (s GoogleAnalyticsAdminV1alphaDataStreamWebStreamData) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaDeleteAccessBindingRequest ¶
added in v0.110.0
type GoogleAnalyticsAdminV1alphaDeleteAccessBindingRequest struct {
	// Name: Required. Formats: - accounts/{account}/accessBindings/{accessBinding}
	// - properties/{property}/accessBindings/{accessBinding}
	Name string `json:"name,omitempty"`
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

GoogleAnalyticsAdminV1alphaDeleteAccessBindingRequest: Request message for DeleteAccessBinding RPC.

func (GoogleAnalyticsAdminV1alphaDeleteAccessBindingRequest) MarshalJSON ¶
added in v0.110.0
func (s GoogleAnalyticsAdminV1alphaDeleteAccessBindingRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink ¶
added in v0.51.0
type GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink struct {
	// AdsPersonalizationEnabled: Enables personalized advertising features with
	// this integration. If this field is not set on create/update, it will be
	// defaulted to true.
	AdsPersonalizationEnabled bool `json:"adsPersonalizationEnabled,omitempty"`
	// AdvertiserDisplayName: Output only. The display name of the Display & Video
	// 360 Advertiser.
	AdvertiserDisplayName string `json:"advertiserDisplayName,omitempty"`
	// AdvertiserId: Immutable. The Display & Video 360 Advertiser's advertiser ID.
	AdvertiserId string `json:"advertiserId,omitempty"`
	// CampaignDataSharingEnabled: Immutable. Enables the import of campaign data
	// from Display & Video 360 into the Google Analytics property. After link
	// creation, this can only be updated from the Display & Video 360 product. If
	// this field is not set on create, it will be defaulted to true.
	CampaignDataSharingEnabled bool `json:"campaignDataSharingEnabled,omitempty"`
	// CostDataSharingEnabled: Immutable. Enables the import of cost data from
	// Display & Video 360 into the Google Analytics property. This can only be
	// enabled if `campaign_data_sharing_enabled` is true. After link creation,
	// this can only be updated from the Display & Video 360 product. If this field
	// is not set on create, it will be defaulted to true.
	CostDataSharingEnabled bool `json:"costDataSharingEnabled,omitempty"`
	// Name: Output only. The resource name for this DisplayVideo360AdvertiserLink
	// resource. Format:
	// properties/{propertyId}/displayVideo360AdvertiserLinks/{linkId} Note: linkId
	// is not the Display & Video 360 Advertiser ID
	Name string `json:"name,omitempty"`

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

GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink: A link between a Google Analytics property and a Display & Video 360 advertiser.

func (GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink) MarshalJSON ¶
added in v0.51.0
func (s GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal ¶
added in v0.51.0
type GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal struct {
	// AdsPersonalizationEnabled: Immutable. Enables personalized advertising
	// features with this integration. If this field is not set on create, it will
	// be defaulted to true.
	AdsPersonalizationEnabled bool `json:"adsPersonalizationEnabled,omitempty"`
	// AdvertiserDisplayName: Output only. The display name of the Display & Video
	// Advertiser. Only populated for proposals that originated from Display &
	// Video 360.
	AdvertiserDisplayName string `json:"advertiserDisplayName,omitempty"`
	// AdvertiserId: Immutable. The Display & Video 360 Advertiser's advertiser ID.
	AdvertiserId string `json:"advertiserId,omitempty"`
	// CampaignDataSharingEnabled: Immutable. Enables the import of campaign data
	// from Display & Video 360. If this field is not set on create, it will be
	// defaulted to true.
	CampaignDataSharingEnabled bool `json:"campaignDataSharingEnabled,omitempty"`
	// CostDataSharingEnabled: Immutable. Enables the import of cost data from
	// Display & Video 360. This can only be enabled if
	// campaign_data_sharing_enabled is enabled. If this field is not set on
	// create, it will be defaulted to true.
	CostDataSharingEnabled bool `json:"costDataSharingEnabled,omitempty"`
	// LinkProposalStatusDetails: Output only. The status information for this link
	// proposal.
	LinkProposalStatusDetails *GoogleAnalyticsAdminV1alphaLinkProposalStatusDetails `json:"linkProposalStatusDetails,omitempty"`
	// Name: Output only. The resource name for this
	// DisplayVideo360AdvertiserLinkProposal resource. Format:
	// properties/{propertyId}/displayVideo360AdvertiserLinkProposals/{proposalId}
	// Note: proposalId is not the Display & Video 360 Advertiser ID
	Name string `json:"name,omitempty"`
	// ValidationEmail: Input only. On a proposal being sent to Display & Video
	// 360, this field must be set to the email address of an admin on the target
	// advertiser. This is used to verify that the Google Analytics admin is aware
	// of at least one admin on the Display & Video 360 Advertiser. This does not
	// restrict approval of the proposal to a single user. Any admin on the Display
	// & Video 360 Advertiser may approve the proposal.
	ValidationEmail string `json:"validationEmail,omitempty"`

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

GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal: A proposal for a link between a Google Analytics property and a Display & Video 360 advertiser. A proposal is converted to a DisplayVideo360AdvertiserLink once approved. Google Analytics admins approve inbound proposals while Display & Video 360 admins approve outbound proposals.

func (GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal) MarshalJSON ¶
added in v0.51.0
func (s GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettings ¶
type GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettings struct {
	// FileDownloadsEnabled: If enabled, capture a file download event each time a
	// link is clicked with a common document, compressed file, application, video,
	// or audio extension.
	FileDownloadsEnabled bool `json:"fileDownloadsEnabled,omitempty"`
	// FormInteractionsEnabled: If enabled, capture a form interaction event each
	// time a visitor interacts with a form on your website. False by default.
	FormInteractionsEnabled bool `json:"formInteractionsEnabled,omitempty"`
	// Name: Output only. Resource name of the Enhanced Measurement Settings.
	// Format:
	// properties/{property_id}/dataStreams/{data_stream}/enhancedMeasurementSetting
	// s Example: "properties/1000/dataStreams/2000/enhancedMeasurementSettings"
	Name string `json:"name,omitempty"`
	// OutboundClicksEnabled: If enabled, capture an outbound click event each time
	// a visitor clicks a link that leads them away from your domain.
	OutboundClicksEnabled bool `json:"outboundClicksEnabled,omitempty"`
	// PageChangesEnabled: If enabled, capture a page view event each time the
	// website changes the browser history state.
	PageChangesEnabled bool `json:"pageChangesEnabled,omitempty"`
	// ScrollsEnabled: If enabled, capture scroll events each time a visitor gets
	// to the bottom of a page.
	ScrollsEnabled bool `json:"scrollsEnabled,omitempty"`
	// SearchQueryParameter: Required. URL query parameters to interpret as site
	// search parameters. Max length is 1024 characters. Must not be empty.
	SearchQueryParameter string `json:"searchQueryParameter,omitempty"`
	// SiteSearchEnabled: If enabled, capture a view search results event each time
	// a visitor performs a search on your site (based on a query parameter).
	SiteSearchEnabled bool `json:"siteSearchEnabled,omitempty"`
	// StreamEnabled: Indicates whether Enhanced Measurement Settings will be used
	// to automatically measure interactions and content on this web stream.
	// Changing this value does not affect the settings themselves, but determines
	// whether they are respected.
	StreamEnabled bool `json:"streamEnabled,omitempty"`
	// UriQueryParameter: Additional URL query parameters. Max length is 1024
	// characters.
	UriQueryParameter string `json:"uriQueryParameter,omitempty"`
	// VideoEngagementEnabled: If enabled, capture video play, progress, and
	// complete events as visitors view embedded videos on your site.
	VideoEngagementEnabled bool `json:"videoEngagementEnabled,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "FileDownloadsEnabled") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FileDownloadsEnabled") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettings: Singleton resource under a web DataStream, configuring measurement of additional site interactions and content.

func (GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettings) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettings) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaEventCreateRule ¶
added in v0.122.0
type GoogleAnalyticsAdminV1alphaEventCreateRule struct {
	// DestinationEvent: Required. The name of the new event to be created. This
	// value must: * be less than 40 characters * consist only of letters, digits
	// or _ (underscores) * start with a letter
	DestinationEvent string `json:"destinationEvent,omitempty"`
	// EventConditions: Required. Must have at least one condition, and can have up
	// to 10 max. Conditions on the source event must match for this rule to be
	// applied.
	EventConditions []*GoogleAnalyticsAdminV1alphaMatchingCondition `json:"eventConditions,omitempty"`
	// Name: Output only. Resource name for this EventCreateRule resource. Format:
	// properties/{property}/dataStreams/{data_stream}/eventCreateRules/{event_creat
	// e_rule}
	Name string `json:"name,omitempty"`
	// ParameterMutations: Parameter mutations define parameter behavior on the new
	// event, and are applied in order. A maximum of 20 mutations can be applied.
	ParameterMutations []*GoogleAnalyticsAdminV1alphaParameterMutation `json:"parameterMutations,omitempty"`
	// SourceCopyParameters: If true, the source parameters are copied to the new
	// event. If false, or unset, all non-internal parameters are not copied from
	// the source event. Parameter mutations are applied after the parameters have
	// been copied.
	SourceCopyParameters bool `json:"sourceCopyParameters,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DestinationEvent") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DestinationEvent") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaEventCreateRule: An Event Create Rule defines conditions that will trigger the creation of an entirely new event based upon matched criteria of a source event. Additional mutations of the parameters from the source event can be defined. Unlike Event Edit rules, Event Creation Rules have no defined order. They will all be run independently. Event Edit and Event Create rules can't be used to modify an event created from an Event Create rule.

func (GoogleAnalyticsAdminV1alphaEventCreateRule) MarshalJSON ¶
added in v0.122.0
func (s GoogleAnalyticsAdminV1alphaEventCreateRule) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaEventEditRule ¶
added in v0.190.0
type GoogleAnalyticsAdminV1alphaEventEditRule struct {
	// DisplayName: Required. The display name of this event edit rule. Maximum of
	// 255 characters.
	DisplayName string `json:"displayName,omitempty"`
	// EventConditions: Required. Conditions on the source event must match for
	// this rule to be applied. Must have at least one condition, and can have up
	// to 10 max.
	EventConditions []*GoogleAnalyticsAdminV1alphaMatchingCondition `json:"eventConditions,omitempty"`
	// Name: Identifier. Resource name for this EventEditRule resource. Format:
	// properties/{property}/dataStreams/{data_stream}/eventEditRules/{event_edit_ru
	// le}
	Name string `json:"name,omitempty"`
	// ParameterMutations: Required. Parameter mutations define parameter behavior
	// on the new event, and are applied in order. A maximum of 20 mutations can be
	// applied.
	ParameterMutations []*GoogleAnalyticsAdminV1alphaParameterMutation `json:"parameterMutations,omitempty"`
	// ProcessingOrder: Output only. The order for which this rule will be
	// processed. Rules with an order value lower than this will be processed
	// before this rule, rules with an order value higher than this will be
	// processed after this rule. New event edit rules will be assigned an order
	// value at the end of the order. This value does not apply to event create
	// rules.
	ProcessingOrder int64 `json:"processingOrder,omitempty,string"`

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

GoogleAnalyticsAdminV1alphaEventEditRule: An Event Edit Rule defines conditions that will trigger the creation of an entirely new event based upon matched criteria of a source event. Additional mutations of the parameters from the source event can be defined. Unlike Event Create rules, Event Edit Rules are applied in their defined order. Event Edit rules can't be used to modify an event created from an Event Create rule.

func (GoogleAnalyticsAdminV1alphaEventEditRule) MarshalJSON ¶
added in v0.190.0
func (s GoogleAnalyticsAdminV1alphaEventEditRule) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaEventMapping ¶
added in v0.139.0
type GoogleAnalyticsAdminV1alphaEventMapping struct {
	// EventName: Required. Name of the Google Analytics event. It must always be
	// set. The max allowed display name length is 40 UTF-16 code units.
	EventName string `json:"eventName,omitempty"`
	// MaxEventCount: The maximum number of times the event occurred. If not set,
	// maximum event count won't be checked.
	MaxEventCount int64 `json:"maxEventCount,omitempty,string"`
	// MaxEventValue: The maximum revenue generated due to the event. Revenue
	// currency will be defined at the property level. If not set, maximum event
	// value won't be checked.
	MaxEventValue float64 `json:"maxEventValue,omitempty"`
	// MinEventCount: At least one of the following four min/max values must be
	// set. The values set will be ANDed together to qualify an event. The minimum
	// number of times the event occurred. If not set, minimum event count won't be
	// checked.
	MinEventCount int64 `json:"minEventCount,omitempty,string"`
	// MinEventValue: The minimum revenue generated due to the event. Revenue
	// currency will be defined at the property level. If not set, minimum event
	// value won't be checked.
	MinEventValue float64 `json:"minEventValue,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EventName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EventName") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaEventMapping: Event setting conditions to match an event.

func (GoogleAnalyticsAdminV1alphaEventMapping) MarshalJSON ¶
added in v0.139.0
func (s GoogleAnalyticsAdminV1alphaEventMapping) MarshalJSON() ([]byte, error)
func (*GoogleAnalyticsAdminV1alphaEventMapping) UnmarshalJSON ¶
added in v0.139.0
func (s *GoogleAnalyticsAdminV1alphaEventMapping) UnmarshalJSON(data []byte) error
type GoogleAnalyticsAdminV1alphaExpandedDataSet ¶
added in v0.100.0
type GoogleAnalyticsAdminV1alphaExpandedDataSet struct {
	// DataCollectionStartTime: Output only. Time when expanded data set began (or
	// will begin) collecing data.
	DataCollectionStartTime string `json:"dataCollectionStartTime,omitempty"`
	// Description: Optional. The description of the ExpandedDataSet. Max 50 chars.
	Description string `json:"description,omitempty"`
	// DimensionFilterExpression: Immutable. A logical expression of
	// ExpandedDataSet filters applied to dimension included in the
	// ExpandedDataSet. This filter is used to reduce the number of rows and thus
	// the chance of encountering `other` row.
	DimensionFilterExpression *GoogleAnalyticsAdminV1alphaExpandedDataSetFilterExpression `json:"dimensionFilterExpression,omitempty"`
	// DimensionNames: Immutable. The list of dimensions included in the
	// ExpandedDataSet. See the API Dimensions
	// (https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#dimensions)
	// for the list of dimension names.
	DimensionNames []string `json:"dimensionNames,omitempty"`
	// DisplayName: Required. The display name of the ExpandedDataSet. Max 200
	// chars.
	DisplayName string `json:"displayName,omitempty"`
	// MetricNames: Immutable. The list of metrics included in the ExpandedDataSet.
	// See the API Metrics
	// (https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#metrics)
	// for the list of dimension names.
	MetricNames []string `json:"metricNames,omitempty"`
	// Name: Output only. The resource name for this ExpandedDataSet resource.
	// Format: properties/{property_id}/expandedDataSets/{expanded_data_set}
	Name string `json:"name,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DataCollectionStartTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DataCollectionStartTime") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaExpandedDataSet: A resource message representing an `ExpandedDataSet`.

func (GoogleAnalyticsAdminV1alphaExpandedDataSet) MarshalJSON ¶
added in v0.100.0
func (s GoogleAnalyticsAdminV1alphaExpandedDataSet) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaExpandedDataSetFilter ¶
added in v0.100.0
type GoogleAnalyticsAdminV1alphaExpandedDataSetFilter struct {
	// FieldName: Required. The dimension name to filter.
	FieldName string `json:"fieldName,omitempty"`
	// InListFilter: A filter for a string dimension that matches a particular list
	// of options.
	InListFilter *GoogleAnalyticsAdminV1alphaExpandedDataSetFilterInListFilter `json:"inListFilter,omitempty"`
	// StringFilter: A filter for a string-type dimension that matches a particular
	// pattern.
	StringFilter *GoogleAnalyticsAdminV1alphaExpandedDataSetFilterStringFilter `json:"stringFilter,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FieldName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FieldName") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaExpandedDataSetFilter: A specific filter for a single dimension

func (GoogleAnalyticsAdminV1alphaExpandedDataSetFilter) MarshalJSON ¶
added in v0.100.0
func (s GoogleAnalyticsAdminV1alphaExpandedDataSetFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaExpandedDataSetFilterExpression ¶
added in v0.100.0
type GoogleAnalyticsAdminV1alphaExpandedDataSetFilterExpression struct {
	// AndGroup: A list of expressions to be AND’ed together. It must contain a
	// ExpandedDataSetFilterExpression with either not_expression or
	// dimension_filter. This must be set for the top level
	// ExpandedDataSetFilterExpression.
	AndGroup *GoogleAnalyticsAdminV1alphaExpandedDataSetFilterExpressionList `json:"andGroup,omitempty"`
	// Filter: A filter on a single dimension. This cannot be set on the top level
	// ExpandedDataSetFilterExpression.
	Filter *GoogleAnalyticsAdminV1alphaExpandedDataSetFilter `json:"filter,omitempty"`
	// NotExpression: A filter expression to be NOT'ed (that is, inverted,
	// complemented). It must include a dimension_filter. This cannot be set on the
	// top level ExpandedDataSetFilterExpression.
	NotExpression *GoogleAnalyticsAdminV1alphaExpandedDataSetFilterExpression `json:"notExpression,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AndGroup") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AndGroup") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaExpandedDataSetFilterExpression: A logical expression of EnhancedDataSet dimension filters.

func (GoogleAnalyticsAdminV1alphaExpandedDataSetFilterExpression) MarshalJSON ¶
added in v0.100.0
func (s GoogleAnalyticsAdminV1alphaExpandedDataSetFilterExpression) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaExpandedDataSetFilterExpressionList ¶
added in v0.100.0
type GoogleAnalyticsAdminV1alphaExpandedDataSetFilterExpressionList struct {
	// FilterExpressions: A list of ExpandedDataSet filter expressions.
	FilterExpressions []*GoogleAnalyticsAdminV1alphaExpandedDataSetFilterExpression `json:"filterExpressions,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FilterExpressions") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FilterExpressions") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaExpandedDataSetFilterExpressionList: A list of ExpandedDataSet filter expressions.

func (GoogleAnalyticsAdminV1alphaExpandedDataSetFilterExpressionList) MarshalJSON ¶
added in v0.100.0
func (s GoogleAnalyticsAdminV1alphaExpandedDataSetFilterExpressionList) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaExpandedDataSetFilterInListFilter ¶
added in v0.100.0
type GoogleAnalyticsAdminV1alphaExpandedDataSetFilterInListFilter struct {
	// CaseSensitive: Optional. If true, the match is case-sensitive. If false, the
	// match is case-insensitive. Must be true.
	CaseSensitive bool `json:"caseSensitive,omitempty"`
	// Values: Required. The list of possible string values to match against. Must
	// be non-empty.
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

GoogleAnalyticsAdminV1alphaExpandedDataSetFilterInListFilter: A filter for a string dimension that matches a particular list of options.

func (GoogleAnalyticsAdminV1alphaExpandedDataSetFilterInListFilter) MarshalJSON ¶
added in v0.100.0
func (s GoogleAnalyticsAdminV1alphaExpandedDataSetFilterInListFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaExpandedDataSetFilterStringFilter ¶
added in v0.100.0
type GoogleAnalyticsAdminV1alphaExpandedDataSetFilterStringFilter struct {
	// CaseSensitive: Optional. If true, the match is case-sensitive. If false, the
	// match is case-insensitive. Must be true when match_type is EXACT. Must be
	// false when match_type is CONTAINS.
	CaseSensitive bool `json:"caseSensitive,omitempty"`
	// MatchType: Required. The match type for the string filter.
	//
	// Possible values:
	//   "MATCH_TYPE_UNSPECIFIED" - Unspecified
	//   "EXACT" - Exact match of the string value.
	//   "CONTAINS" - Contains the string value.
	MatchType string `json:"matchType,omitempty"`
	// Value: Required. The string value to be matched against.
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

GoogleAnalyticsAdminV1alphaExpandedDataSetFilterStringFilter: A filter for a string-type dimension that matches a particular pattern.

func (GoogleAnalyticsAdminV1alphaExpandedDataSetFilterStringFilter) MarshalJSON ¶
added in v0.100.0
func (s GoogleAnalyticsAdminV1alphaExpandedDataSetFilterStringFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaFirebaseLink ¶
type GoogleAnalyticsAdminV1alphaFirebaseLink struct {
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

GoogleAnalyticsAdminV1alphaFirebaseLink: A link between a Google Analytics property and a Firebase project.

func (GoogleAnalyticsAdminV1alphaFirebaseLink) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1alphaFirebaseLink) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaGlobalSiteTag ¶
type GoogleAnalyticsAdminV1alphaGlobalSiteTag struct {
	// Name: Output only. Resource name for this GlobalSiteTag resource. Format:
	// properties/{property_id}/dataStreams/{stream_id}/globalSiteTag Example:
	// "properties/123/dataStreams/456/globalSiteTag"
	Name string `json:"name,omitempty"`
	// Snippet: Immutable. JavaScript code snippet to be pasted as the first item
	// into the head tag of every webpage to measure.
	Snippet string `json:"snippet,omitempty"`

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

GoogleAnalyticsAdminV1alphaGlobalSiteTag: Read-only resource with the tag for sending data from a website to a DataStream. Only present for web DataStream resources.

func (GoogleAnalyticsAdminV1alphaGlobalSiteTag) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1alphaGlobalSiteTag) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaGoogleAdsLink ¶
type GoogleAnalyticsAdminV1alphaGoogleAdsLink struct {
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

GoogleAnalyticsAdminV1alphaGoogleAdsLink: A link between a Google Analytics property and a Google Ads account.

func (GoogleAnalyticsAdminV1alphaGoogleAdsLink) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1alphaGoogleAdsLink) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaGoogleSignalsSettings ¶
added in v0.47.0
type GoogleAnalyticsAdminV1alphaGoogleSignalsSettings struct {
	// Consent: Output only. Terms of Service acceptance.
	//
	// Possible values:
	//   "GOOGLE_SIGNALS_CONSENT_UNSPECIFIED" - Google Signals consent value
	// defaults to GOOGLE_SIGNALS_CONSENT_UNSPECIFIED. This will be treated as
	// GOOGLE_SIGNALS_CONSENT_NOT_CONSENTED.
	//   "GOOGLE_SIGNALS_CONSENT_CONSENTED" - Terms of service have been accepted
	//   "GOOGLE_SIGNALS_CONSENT_NOT_CONSENTED" - Terms of service have not been
	// accepted
	Consent string `json:"consent,omitempty"`
	// Name: Output only. Resource name of this setting. Format:
	// properties/{property_id}/googleSignalsSettings Example:
	// "properties/1000/googleSignalsSettings"
	Name string `json:"name,omitempty"`
	// State: Status of this setting.
	//
	// Possible values:
	//   "GOOGLE_SIGNALS_STATE_UNSPECIFIED" - Google Signals status defaults to
	// GOOGLE_SIGNALS_STATE_UNSPECIFIED to represent that the user has not made an
	// explicit choice.
	//   "GOOGLE_SIGNALS_ENABLED" - Google Signals is enabled.
	//   "GOOGLE_SIGNALS_DISABLED" - Google Signals is disabled.
	State string `json:"state,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Consent") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Consent") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaGoogleSignalsSettings: Settings values for Google Signals. This is a singleton resource.

func (GoogleAnalyticsAdminV1alphaGoogleSignalsSettings) MarshalJSON ¶
added in v0.47.0
func (s GoogleAnalyticsAdminV1alphaGoogleSignalsSettings) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaGroupingRule ¶
added in v0.117.0
type GoogleAnalyticsAdminV1alphaGroupingRule struct {
	// DisplayName: Required. Customer defined display name for the channel.
	DisplayName string `json:"displayName,omitempty"`
	// Expression: Required. The Filter Expression that defines the Grouping Rule.
	Expression *GoogleAnalyticsAdminV1alphaChannelGroupFilterExpression `json:"expression,omitempty"`
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

GoogleAnalyticsAdminV1alphaGroupingRule: The rules that govern how traffic is grouped into one channel.

func (GoogleAnalyticsAdminV1alphaGroupingRule) MarshalJSON ¶
added in v0.117.0
func (s GoogleAnalyticsAdminV1alphaGroupingRule) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaKeyEvent ¶
added in v0.173.0
type GoogleAnalyticsAdminV1alphaKeyEvent struct {
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
	DefaultValue *GoogleAnalyticsAdminV1alphaKeyEventDefaultValue `json:"defaultValue,omitempty"`
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

GoogleAnalyticsAdminV1alphaKeyEvent: A key event in a Google Analytics property.

func (GoogleAnalyticsAdminV1alphaKeyEvent) MarshalJSON ¶
added in v0.173.0
func (s GoogleAnalyticsAdminV1alphaKeyEvent) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaKeyEventDefaultValue ¶
added in v0.173.0
type GoogleAnalyticsAdminV1alphaKeyEventDefaultValue struct {
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

GoogleAnalyticsAdminV1alphaKeyEventDefaultValue: Defines a default value/currency for a key event.

func (GoogleAnalyticsAdminV1alphaKeyEventDefaultValue) MarshalJSON ¶
added in v0.173.0
func (s GoogleAnalyticsAdminV1alphaKeyEventDefaultValue) MarshalJSON() ([]byte, error)
func (*GoogleAnalyticsAdminV1alphaKeyEventDefaultValue) UnmarshalJSON ¶
added in v0.173.0
func (s *GoogleAnalyticsAdminV1alphaKeyEventDefaultValue) UnmarshalJSON(data []byte) error
type GoogleAnalyticsAdminV1alphaLinkProposalStatusDetails ¶
added in v0.51.0
type GoogleAnalyticsAdminV1alphaLinkProposalStatusDetails struct {
	// LinkProposalInitiatingProduct: Output only. The source of this proposal.
	//
	// Possible values:
	//   "LINK_PROPOSAL_INITIATING_PRODUCT_UNSPECIFIED" - Unspecified product.
	//   "GOOGLE_ANALYTICS" - This proposal was created by a user from Google
	// Analytics.
	//   "LINKED_PRODUCT" - This proposal was created by a user from a linked
	// product (not Google Analytics).
	LinkProposalInitiatingProduct string `json:"linkProposalInitiatingProduct,omitempty"`
	// LinkProposalState: Output only. The state of this proposal.
	//
	// Possible values:
	//   "LINK_PROPOSAL_STATE_UNSPECIFIED" - Unspecified state
	//   "AWAITING_REVIEW_FROM_GOOGLE_ANALYTICS" - This proposal is awaiting review
	// from a Google Analytics user. This proposal will automatically expire after
	// some time.
	//   "AWAITING_REVIEW_FROM_LINKED_PRODUCT" - This proposal is awaiting review
	// from a user of a linked product. This proposal will automatically expire
	// after some time.
	//   "WITHDRAWN" - This proposal has been withdrawn by an admin on the
	// initiating product. This proposal will be automatically deleted after some
	// time.
	//   "DECLINED" - This proposal has been declined by an admin on the receiving
	// product. This proposal will be automatically deleted after some time.
	//   "EXPIRED" - This proposal expired due to lack of response from an admin on
	// the receiving product. This proposal will be automatically deleted after
	// some time.
	//   "OBSOLETE" - This proposal has become obsolete because a link was directly
	// created to the same external product resource that this proposal specifies.
	// This proposal will be automatically deleted after some time.
	LinkProposalState string `json:"linkProposalState,omitempty"`
	// RequestorEmail: Output only. The email address of the user that proposed
	// this linkage.
	RequestorEmail string `json:"requestorEmail,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "LinkProposalInitiatingProduct") to unconditionally include in API requests.
	// By default, fields with empty or default values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields
	// for more details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "LinkProposalInitiatingProduct")
	// to include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaLinkProposalStatusDetails: Status information for a link proposal.

func (GoogleAnalyticsAdminV1alphaLinkProposalStatusDetails) MarshalJSON ¶
added in v0.51.0
func (s GoogleAnalyticsAdminV1alphaLinkProposalStatusDetails) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListAccessBindingsResponse ¶
added in v0.110.0
type GoogleAnalyticsAdminV1alphaListAccessBindingsResponse struct {
	// AccessBindings: List of AccessBindings. These will be ordered stably, but in
	// an arbitrary order.
	AccessBindings []*GoogleAnalyticsAdminV1alphaAccessBinding `json:"accessBindings,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AccessBindings") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccessBindings") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaListAccessBindingsResponse: Response message for ListAccessBindings RPC.

func (GoogleAnalyticsAdminV1alphaListAccessBindingsResponse) MarshalJSON ¶
added in v0.110.0
func (s GoogleAnalyticsAdminV1alphaListAccessBindingsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListAccountSummariesResponse ¶
type GoogleAnalyticsAdminV1alphaListAccountSummariesResponse struct {
	// AccountSummaries: Account summaries of all accounts the caller has access
	// to.
	AccountSummaries []*GoogleAnalyticsAdminV1alphaAccountSummary `json:"accountSummaries,omitempty"`
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

GoogleAnalyticsAdminV1alphaListAccountSummariesResponse: Response message for ListAccountSummaries RPC.

func (GoogleAnalyticsAdminV1alphaListAccountSummariesResponse) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1alphaListAccountSummariesResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListAccountsResponse ¶
type GoogleAnalyticsAdminV1alphaListAccountsResponse struct {
	// Accounts: Results that were accessible to the caller.
	Accounts []*GoogleAnalyticsAdminV1alphaAccount `json:"accounts,omitempty"`
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

GoogleAnalyticsAdminV1alphaListAccountsResponse: Request message for ListAccounts RPC.

func (GoogleAnalyticsAdminV1alphaListAccountsResponse) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1alphaListAccountsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListAdSenseLinksResponse ¶
added in v0.123.0
type GoogleAnalyticsAdminV1alphaListAdSenseLinksResponse struct {
	// AdsenseLinks: List of AdSenseLinks.
	AdsenseLinks []*GoogleAnalyticsAdminV1alphaAdSenseLink `json:"adsenseLinks,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AdsenseLinks") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AdsenseLinks") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaListAdSenseLinksResponse: Response message for ListAdSenseLinks method.

func (GoogleAnalyticsAdminV1alphaListAdSenseLinksResponse) MarshalJSON ¶
added in v0.123.0
func (s GoogleAnalyticsAdminV1alphaListAdSenseLinksResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListAudiencesResponse ¶
added in v0.90.0
type GoogleAnalyticsAdminV1alphaListAudiencesResponse struct {
	// Audiences: List of Audiences.
	Audiences []*GoogleAnalyticsAdminV1alphaAudience `json:"audiences,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Audiences") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Audiences") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaListAudiencesResponse: Response message for ListAudiences RPC.

func (GoogleAnalyticsAdminV1alphaListAudiencesResponse) MarshalJSON ¶
added in v0.90.0
func (s GoogleAnalyticsAdminV1alphaListAudiencesResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListBigQueryLinksResponse ¶
added in v0.104.0
type GoogleAnalyticsAdminV1alphaListBigQueryLinksResponse struct {
	// BigqueryLinks: List of BigQueryLinks.
	BigqueryLinks []*GoogleAnalyticsAdminV1alphaBigQueryLink `json:"bigqueryLinks,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "BigqueryLinks") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BigqueryLinks") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaListBigQueryLinksResponse: Response message for ListBigQueryLinks RPC

func (GoogleAnalyticsAdminV1alphaListBigQueryLinksResponse) MarshalJSON ¶
added in v0.104.0
func (s GoogleAnalyticsAdminV1alphaListBigQueryLinksResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListCalculatedMetricsResponse ¶
added in v0.157.0
type GoogleAnalyticsAdminV1alphaListCalculatedMetricsResponse struct {
	// CalculatedMetrics: List of CalculatedMetrics.
	CalculatedMetrics []*GoogleAnalyticsAdminV1alphaCalculatedMetric `json:"calculatedMetrics,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "CalculatedMetrics") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CalculatedMetrics") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaListCalculatedMetricsResponse: Response message for ListCalculatedMetrics RPC.

func (GoogleAnalyticsAdminV1alphaListCalculatedMetricsResponse) MarshalJSON ¶
added in v0.157.0
func (s GoogleAnalyticsAdminV1alphaListCalculatedMetricsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListChannelGroupsResponse ¶
added in v0.117.0
type GoogleAnalyticsAdminV1alphaListChannelGroupsResponse struct {
	// ChannelGroups: List of ChannelGroup. These will be ordered stably, but in an
	// arbitrary order.
	ChannelGroups []*GoogleAnalyticsAdminV1alphaChannelGroup `json:"channelGroups,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ChannelGroups") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ChannelGroups") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaListChannelGroupsResponse: Response message for ListChannelGroups RPC.

func (GoogleAnalyticsAdminV1alphaListChannelGroupsResponse) MarshalJSON ¶
added in v0.117.0
func (s GoogleAnalyticsAdminV1alphaListChannelGroupsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListConversionEventsResponse ¶
added in v0.47.0
type GoogleAnalyticsAdminV1alphaListConversionEventsResponse struct {
	// ConversionEvents: The requested conversion events
	ConversionEvents []*GoogleAnalyticsAdminV1alphaConversionEvent `json:"conversionEvents,omitempty"`
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

GoogleAnalyticsAdminV1alphaListConversionEventsResponse: Response message for ListConversionEvents RPC.

func (GoogleAnalyticsAdminV1alphaListConversionEventsResponse) MarshalJSON ¶
added in v0.47.0
func (s GoogleAnalyticsAdminV1alphaListConversionEventsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListCustomDimensionsResponse ¶
added in v0.47.0
type GoogleAnalyticsAdminV1alphaListCustomDimensionsResponse struct {
	// CustomDimensions: List of CustomDimensions.
	CustomDimensions []*GoogleAnalyticsAdminV1alphaCustomDimension `json:"customDimensions,omitempty"`
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

GoogleAnalyticsAdminV1alphaListCustomDimensionsResponse: Response message for ListCustomDimensions RPC.

func (GoogleAnalyticsAdminV1alphaListCustomDimensionsResponse) MarshalJSON ¶
added in v0.47.0
func (s GoogleAnalyticsAdminV1alphaListCustomDimensionsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListCustomMetricsResponse ¶
added in v0.47.0
type GoogleAnalyticsAdminV1alphaListCustomMetricsResponse struct {
	// CustomMetrics: List of CustomMetrics.
	CustomMetrics []*GoogleAnalyticsAdminV1alphaCustomMetric `json:"customMetrics,omitempty"`
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

GoogleAnalyticsAdminV1alphaListCustomMetricsResponse: Response message for ListCustomMetrics RPC.

func (GoogleAnalyticsAdminV1alphaListCustomMetricsResponse) MarshalJSON ¶
added in v0.47.0
func (s GoogleAnalyticsAdminV1alphaListCustomMetricsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListDataStreamsResponse ¶
added in v0.61.0
type GoogleAnalyticsAdminV1alphaListDataStreamsResponse struct {
	// DataStreams: List of DataStreams.
	DataStreams []*GoogleAnalyticsAdminV1alphaDataStream `json:"dataStreams,omitempty"`
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

GoogleAnalyticsAdminV1alphaListDataStreamsResponse: Response message for ListDataStreams RPC.

func (GoogleAnalyticsAdminV1alphaListDataStreamsResponse) MarshalJSON ¶
added in v0.61.0
func (s GoogleAnalyticsAdminV1alphaListDataStreamsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinkProposalsResponse ¶
added in v0.51.0
type GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinkProposalsResponse struct {
	// DisplayVideo360AdvertiserLinkProposals: List of
	// DisplayVideo360AdvertiserLinkProposals.
	DisplayVideo360AdvertiserLinkProposals []*GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal `json:"displayVideo360AdvertiserLinkProposals,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g.
	// "DisplayVideo360AdvertiserLinkProposals") to unconditionally include in API
	// requests. By default, fields with empty or default values are omitted from
	// API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g.
	// "DisplayVideo360AdvertiserLinkProposals") to include in API requests with
	// the JSON null value. By default, fields with empty values are omitted from
	// API requests. See https://pkg.go.dev/google.golang.org/api#hdr-NullFields
	// for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinkProposalsResponse : Response message for ListDisplayVideo360AdvertiserLinkProposals RPC.

func (GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinkProposalsResponse) MarshalJSON ¶
added in v0.51.0
func (s GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinkProposalsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinksResponse ¶
added in v0.51.0
type GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinksResponse struct {
	// DisplayVideo360AdvertiserLinks: List of DisplayVideo360AdvertiserLinks.
	DisplayVideo360AdvertiserLinks []*GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink `json:"displayVideo360AdvertiserLinks,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g.
	// "DisplayVideo360AdvertiserLinks") to unconditionally include in API
	// requests. By default, fields with empty or default values are omitted from
	// API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DisplayVideo360AdvertiserLinks")
	// to include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinksResponse: Response message for ListDisplayVideo360AdvertiserLinks RPC.

func (GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinksResponse) MarshalJSON ¶
added in v0.51.0
func (s GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinksResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListEventCreateRulesResponse ¶
added in v0.122.0
type GoogleAnalyticsAdminV1alphaListEventCreateRulesResponse struct {
	// EventCreateRules: List of EventCreateRules. These will be ordered stably,
	// but in an arbitrary order.
	EventCreateRules []*GoogleAnalyticsAdminV1alphaEventCreateRule `json:"eventCreateRules,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "EventCreateRules") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EventCreateRules") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaListEventCreateRulesResponse: Response message for ListEventCreateRules RPC.

func (GoogleAnalyticsAdminV1alphaListEventCreateRulesResponse) MarshalJSON ¶
added in v0.122.0
func (s GoogleAnalyticsAdminV1alphaListEventCreateRulesResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListEventEditRulesResponse ¶
added in v0.190.0
type GoogleAnalyticsAdminV1alphaListEventEditRulesResponse struct {
	// EventEditRules: List of EventEditRules. These will be ordered stably, but in
	// an arbitrary order.
	EventEditRules []*GoogleAnalyticsAdminV1alphaEventEditRule `json:"eventEditRules,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "EventEditRules") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EventEditRules") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaListEventEditRulesResponse: Response message for ListEventEditRules RPC.

func (GoogleAnalyticsAdminV1alphaListEventEditRulesResponse) MarshalJSON ¶
added in v0.190.0
func (s GoogleAnalyticsAdminV1alphaListEventEditRulesResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListExpandedDataSetsResponse ¶
added in v0.111.0
type GoogleAnalyticsAdminV1alphaListExpandedDataSetsResponse struct {
	// ExpandedDataSets: List of ExpandedDataSet. These will be ordered stably, but
	// in an arbitrary order.
	ExpandedDataSets []*GoogleAnalyticsAdminV1alphaExpandedDataSet `json:"expandedDataSets,omitempty"`
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ExpandedDataSets") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExpandedDataSets") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaListExpandedDataSetsResponse: Response message for ListExpandedDataSets RPC.

func (GoogleAnalyticsAdminV1alphaListExpandedDataSetsResponse) MarshalJSON ¶
added in v0.111.0
func (s GoogleAnalyticsAdminV1alphaListExpandedDataSetsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListFirebaseLinksResponse ¶
type GoogleAnalyticsAdminV1alphaListFirebaseLinksResponse struct {
	// FirebaseLinks: List of FirebaseLinks. This will have at most one value.
	FirebaseLinks []*GoogleAnalyticsAdminV1alphaFirebaseLink `json:"firebaseLinks,omitempty"`
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

GoogleAnalyticsAdminV1alphaListFirebaseLinksResponse: Response message for ListFirebaseLinks RPC

func (GoogleAnalyticsAdminV1alphaListFirebaseLinksResponse) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1alphaListFirebaseLinksResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListGoogleAdsLinksResponse ¶
type GoogleAnalyticsAdminV1alphaListGoogleAdsLinksResponse struct {
	// GoogleAdsLinks: List of GoogleAdsLinks.
	GoogleAdsLinks []*GoogleAnalyticsAdminV1alphaGoogleAdsLink `json:"googleAdsLinks,omitempty"`
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

GoogleAnalyticsAdminV1alphaListGoogleAdsLinksResponse: Response message for ListGoogleAdsLinks RPC.

func (GoogleAnalyticsAdminV1alphaListGoogleAdsLinksResponse) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1alphaListGoogleAdsLinksResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListKeyEventsResponse ¶
added in v0.173.0
type GoogleAnalyticsAdminV1alphaListKeyEventsResponse struct {
	// KeyEvents: The requested Key Events
	KeyEvents []*GoogleAnalyticsAdminV1alphaKeyEvent `json:"keyEvents,omitempty"`
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

GoogleAnalyticsAdminV1alphaListKeyEventsResponse: Response message for ListKeyEvents RPC.

func (GoogleAnalyticsAdminV1alphaListKeyEventsResponse) MarshalJSON ¶
added in v0.173.0
func (s GoogleAnalyticsAdminV1alphaListKeyEventsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListMeasurementProtocolSecretsResponse ¶
added in v0.47.0
type GoogleAnalyticsAdminV1alphaListMeasurementProtocolSecretsResponse struct {
	// MeasurementProtocolSecrets: A list of secrets for the parent stream
	// specified in the request.
	MeasurementProtocolSecrets []*GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret `json:"measurementProtocolSecrets,omitempty"`
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

GoogleAnalyticsAdminV1alphaListMeasurementProtocolSecretsResponse: Response message for ListMeasurementProtocolSecret RPC

func (GoogleAnalyticsAdminV1alphaListMeasurementProtocolSecretsResponse) MarshalJSON ¶
added in v0.47.0
func (s GoogleAnalyticsAdminV1alphaListMeasurementProtocolSecretsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListPropertiesResponse ¶
type GoogleAnalyticsAdminV1alphaListPropertiesResponse struct {
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Properties: Results that matched the filter criteria and were accessible to
	// the caller.
	Properties []*GoogleAnalyticsAdminV1alphaProperty `json:"properties,omitempty"`

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

GoogleAnalyticsAdminV1alphaListPropertiesResponse: Response message for ListProperties RPC.

func (GoogleAnalyticsAdminV1alphaListPropertiesResponse) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1alphaListPropertiesResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListReportingDataAnnotationsResponse ¶
added in v0.229.0
type GoogleAnalyticsAdminV1alphaListReportingDataAnnotationsResponse struct {
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// ReportingDataAnnotations: List of Reporting Data Annotations.
	ReportingDataAnnotations []*GoogleAnalyticsAdminV1alphaReportingDataAnnotation `json:"reportingDataAnnotations,omitempty"`

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

GoogleAnalyticsAdminV1alphaListReportingDataAnnotationsResponse: Response message for ListReportingDataAnnotation RPC.

func (GoogleAnalyticsAdminV1alphaListReportingDataAnnotationsResponse) MarshalJSON ¶
added in v0.229.0
func (s GoogleAnalyticsAdminV1alphaListReportingDataAnnotationsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListRollupPropertySourceLinksResponse ¶
added in v0.144.0
type GoogleAnalyticsAdminV1alphaListRollupPropertySourceLinksResponse struct {
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// RollupPropertySourceLinks: List of RollupPropertySourceLinks.
	RollupPropertySourceLinks []*GoogleAnalyticsAdminV1alphaRollupPropertySourceLink `json:"rollupPropertySourceLinks,omitempty"`

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

GoogleAnalyticsAdminV1alphaListRollupPropertySourceLinksResponse: Response message for ListRollupPropertySourceLinks RPC.

func (GoogleAnalyticsAdminV1alphaListRollupPropertySourceLinksResponse) MarshalJSON ¶
added in v0.144.0
func (s GoogleAnalyticsAdminV1alphaListRollupPropertySourceLinksResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListSKAdNetworkConversionValueSchemasResponse ¶
added in v0.139.0
type GoogleAnalyticsAdminV1alphaListSKAdNetworkConversionValueSchemasResponse struct {
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	// Currently, Google Analytics supports only one
	// SKAdNetworkConversionValueSchema per dataStream, so this will never be
	// populated.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// SkadnetworkConversionValueSchemas: List of
	// SKAdNetworkConversionValueSchemas. This will have at most one value.
	SkadnetworkConversionValueSchemas []*GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchema `json:"skadnetworkConversionValueSchemas,omitempty"`

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

GoogleAnalyticsAdminV1alphaListSKAdNetworkConversionValueSchemasResponse: Response message for ListSKAdNetworkConversionValueSchemas RPC

func (GoogleAnalyticsAdminV1alphaListSKAdNetworkConversionValueSchemasResponse) MarshalJSON ¶
added in v0.139.0
func (s GoogleAnalyticsAdminV1alphaListSKAdNetworkConversionValueSchemasResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListSearchAds360LinksResponse ¶
added in v0.100.0
type GoogleAnalyticsAdminV1alphaListSearchAds360LinksResponse struct {
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// SearchAds360Links: List of SearchAds360Links.
	SearchAds360Links []*GoogleAnalyticsAdminV1alphaSearchAds360Link `json:"searchAds360Links,omitempty"`

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

GoogleAnalyticsAdminV1alphaListSearchAds360LinksResponse: Response message for ListSearchAds360Links RPC.

func (GoogleAnalyticsAdminV1alphaListSearchAds360LinksResponse) MarshalJSON ¶
added in v0.100.0
func (s GoogleAnalyticsAdminV1alphaListSearchAds360LinksResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListSubpropertyEventFiltersResponse ¶
added in v0.144.0
type GoogleAnalyticsAdminV1alphaListSubpropertyEventFiltersResponse struct {
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// SubpropertyEventFilters: List of subproperty event filters.
	SubpropertyEventFilters []*GoogleAnalyticsAdminV1alphaSubpropertyEventFilter `json:"subpropertyEventFilters,omitempty"`

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

GoogleAnalyticsAdminV1alphaListSubpropertyEventFiltersResponse: Response message for ListSubpropertyEventFilter RPC.

func (GoogleAnalyticsAdminV1alphaListSubpropertyEventFiltersResponse) MarshalJSON ¶
added in v0.144.0
func (s GoogleAnalyticsAdminV1alphaListSubpropertyEventFiltersResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaListSubpropertySyncConfigsResponse ¶
added in v0.237.0
type GoogleAnalyticsAdminV1alphaListSubpropertySyncConfigsResponse struct {
	// NextPageToken: A token, which can be sent as `page_token` to retrieve the
	// next page. If this field is omitted, there are no subsequent pages.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// SubpropertySyncConfigs: List of `SubpropertySyncConfig` resources.
	SubpropertySyncConfigs []*GoogleAnalyticsAdminV1alphaSubpropertySyncConfig `json:"subpropertySyncConfigs,omitempty"`

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

GoogleAnalyticsAdminV1alphaListSubpropertySyncConfigsResponse: Response message for ListSubpropertySyncConfigs RPC.

func (GoogleAnalyticsAdminV1alphaListSubpropertySyncConfigsResponse) MarshalJSON ¶
added in v0.237.0
func (s GoogleAnalyticsAdminV1alphaListSubpropertySyncConfigsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaMatchingCondition ¶
added in v0.122.0
type GoogleAnalyticsAdminV1alphaMatchingCondition struct {
	// ComparisonType: Required. The type of comparison to be applied to the value.
	//
	// Possible values:
	//   "COMPARISON_TYPE_UNSPECIFIED" - Unknown
	//   "EQUALS" - Equals, case sensitive
	//   "EQUALS_CASE_INSENSITIVE" - Equals, case insensitive
	//   "CONTAINS" - Contains, case sensitive
	//   "CONTAINS_CASE_INSENSITIVE" - Contains, case insensitive
	//   "STARTS_WITH" - Starts with, case sensitive
	//   "STARTS_WITH_CASE_INSENSITIVE" - Starts with, case insensitive
	//   "ENDS_WITH" - Ends with, case sensitive
	//   "ENDS_WITH_CASE_INSENSITIVE" - Ends with, case insensitive
	//   "GREATER_THAN" - Greater than
	//   "GREATER_THAN_OR_EQUAL" - Greater than or equal
	//   "LESS_THAN" - Less than
	//   "LESS_THAN_OR_EQUAL" - Less than or equal
	//   "REGULAR_EXPRESSION" - regular expression. Only supported for web streams.
	//   "REGULAR_EXPRESSION_CASE_INSENSITIVE" - regular expression, case
	// insensitive. Only supported for web streams.
	ComparisonType string `json:"comparisonType,omitempty"`
	// Field: Required. The name of the field that is compared against for the
	// condition. If 'event_name' is specified this condition will apply to the
	// name of the event. Otherwise the condition will apply to a parameter with
	// the specified name. This value cannot contain spaces.
	Field string `json:"field,omitempty"`
	// Negated: Whether or not the result of the comparison should be negated. For
	// example, if `negated` is true, then 'equals' comparisons would function as
	// 'not equals'.
	Negated bool `json:"negated,omitempty"`
	// Value: Required. The value being compared against for this condition. The
	// runtime implementation may perform type coercion of this value to evaluate
	// this condition based on the type of the parameter value.
	Value string `json:"value,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ComparisonType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ComparisonType") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaMatchingCondition: Defines a condition for when an Event Edit or Event Creation rule applies to an event.

func (GoogleAnalyticsAdminV1alphaMatchingCondition) MarshalJSON ¶
added in v0.122.0
func (s GoogleAnalyticsAdminV1alphaMatchingCondition) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret ¶
added in v0.47.0
type GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret struct {
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

GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret: A secret value used for sending hits to Measurement Protocol.

func (GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret) MarshalJSON ¶
added in v0.47.0
func (s GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaNumericValue ¶
added in v0.86.0
type GoogleAnalyticsAdminV1alphaNumericValue struct {
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

GoogleAnalyticsAdminV1alphaNumericValue: To represent a number.

func (GoogleAnalyticsAdminV1alphaNumericValue) MarshalJSON ¶
added in v0.86.0
func (s GoogleAnalyticsAdminV1alphaNumericValue) MarshalJSON() ([]byte, error)
func (*GoogleAnalyticsAdminV1alphaNumericValue) UnmarshalJSON ¶
added in v0.86.0
func (s *GoogleAnalyticsAdminV1alphaNumericValue) UnmarshalJSON(data []byte) error
type GoogleAnalyticsAdminV1alphaParameterMutation ¶
added in v0.122.0
type GoogleAnalyticsAdminV1alphaParameterMutation struct {
	// Parameter: Required. The name of the parameter to mutate. This value must: *
	// be less than 40 characters. * be unique across across all mutations within
	// the rule * consist only of letters, digits or _ (underscores) For event edit
	// rules, the name may also be set to 'event_name' to modify the event_name in
	// place.
	Parameter string `json:"parameter,omitempty"`
	// ParameterValue: Required. The value mutation to perform. * Must be less than
	// 100 characters. * To specify a constant value for the param, use the value's
	// string. * To copy value from another parameter, use syntax like
	// "[[other_parameter]]" For more details, see this help center article
	// (https://support.google.com/analytics/answer/10085872#modify-an-event&zippy=%2Cin-this-article%2Cmodify-parameters).
	ParameterValue string `json:"parameterValue,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Parameter") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Parameter") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaParameterMutation: Defines an event parameter to mutate.

func (GoogleAnalyticsAdminV1alphaParameterMutation) MarshalJSON ¶
added in v0.122.0
func (s GoogleAnalyticsAdminV1alphaParameterMutation) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaPostbackWindow ¶
added in v0.139.0
type GoogleAnalyticsAdminV1alphaPostbackWindow struct {
	// ConversionValues: Ordering of the repeated field will be used to prioritize
	// the conversion value settings. Lower indexed entries are prioritized higher.
	// The first conversion value setting that evaluates to true will be selected.
	// It must have at least one entry if enable_postback_window_settings is set to
	// true. It can have maximum of 128 entries.
	ConversionValues []*GoogleAnalyticsAdminV1alphaConversionValues `json:"conversionValues,omitempty"`
	// PostbackWindowSettingsEnabled: If enable_postback_window_settings is true,
	// conversion_values must be populated and will be used for determining when
	// and how to set the Conversion Value on a client device and exporting schema
	// to linked Ads accounts. If false, the settings are not used, but are
	// retained in case they may be used in the future. This must always be true
	// for postback_window_one.
	PostbackWindowSettingsEnabled bool `json:"postbackWindowSettingsEnabled,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ConversionValues") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ConversionValues") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaPostbackWindow: Settings for a SKAdNetwork conversion postback window.

func (GoogleAnalyticsAdminV1alphaPostbackWindow) MarshalJSON ¶
added in v0.139.0
func (s GoogleAnalyticsAdminV1alphaPostbackWindow) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaProperty ¶
type GoogleAnalyticsAdminV1alphaProperty struct {
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

GoogleAnalyticsAdminV1alphaProperty: A resource message representing a Google Analytics property.

func (GoogleAnalyticsAdminV1alphaProperty) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1alphaProperty) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaPropertySummary ¶
type GoogleAnalyticsAdminV1alphaPropertySummary struct {
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

GoogleAnalyticsAdminV1alphaPropertySummary: A virtual resource representing metadata for a Google Analytics property.

func (GoogleAnalyticsAdminV1alphaPropertySummary) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1alphaPropertySummary) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaProvisionAccountTicketRequest ¶
type GoogleAnalyticsAdminV1alphaProvisionAccountTicketRequest struct {
	// Account: The account to create.
	Account *GoogleAnalyticsAdminV1alphaAccount `json:"account,omitempty"`
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

GoogleAnalyticsAdminV1alphaProvisionAccountTicketRequest: Request message for ProvisionAccountTicket RPC.

func (GoogleAnalyticsAdminV1alphaProvisionAccountTicketRequest) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1alphaProvisionAccountTicketRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaProvisionAccountTicketResponse ¶
type GoogleAnalyticsAdminV1alphaProvisionAccountTicketResponse struct {
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

GoogleAnalyticsAdminV1alphaProvisionAccountTicketResponse: Response message for ProvisionAccountTicket RPC.

func (GoogleAnalyticsAdminV1alphaProvisionAccountTicketResponse) MarshalJSON ¶
func (s GoogleAnalyticsAdminV1alphaProvisionAccountTicketResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaProvisionSubpropertyRequest ¶
added in v0.191.0
type GoogleAnalyticsAdminV1alphaProvisionSubpropertyRequest struct {
	// CustomDimensionAndMetricSynchronizationMode: Optional. The subproperty
	// feature synchronization mode for Custom Dimensions and Metrics
	//
	// Possible values:
	//   "SYNCHRONIZATION_MODE_UNSPECIFIED" - Synchronization mode unknown or not
	// specified.
	//   "NONE" - Entities are not synchronized. Local edits are allowed on the
	// subproperty.
	//   "ALL" - Entities are synchronized from parent property. Local mutations
	// are not allowed on the subproperty (Create / Update / Delete)
	CustomDimensionAndMetricSynchronizationMode string `json:"customDimensionAndMetricSynchronizationMode,omitempty"`
	// Subproperty: Required. The subproperty to create.
	Subproperty *GoogleAnalyticsAdminV1alphaProperty `json:"subproperty,omitempty"`
	// SubpropertyEventFilter: Optional. The subproperty event filter to create on
	// an ordinary property.
	SubpropertyEventFilter *GoogleAnalyticsAdminV1alphaSubpropertyEventFilter `json:"subpropertyEventFilter,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "CustomDimensionAndMetricSynchronizationMode") to unconditionally include in
	// API requests. By default, fields with empty or default values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g.
	// "CustomDimensionAndMetricSynchronizationMode") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaProvisionSubpropertyRequest: Request message for CreateSubproperty RPC.

func (GoogleAnalyticsAdminV1alphaProvisionSubpropertyRequest) MarshalJSON ¶
added in v0.191.0
func (s GoogleAnalyticsAdminV1alphaProvisionSubpropertyRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaProvisionSubpropertyResponse ¶
added in v0.191.0
type GoogleAnalyticsAdminV1alphaProvisionSubpropertyResponse struct {
	// Subproperty: The created subproperty.
	Subproperty *GoogleAnalyticsAdminV1alphaProperty `json:"subproperty,omitempty"`
	// SubpropertyEventFilter: The created subproperty event filter.
	SubpropertyEventFilter *GoogleAnalyticsAdminV1alphaSubpropertyEventFilter `json:"subpropertyEventFilter,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Subproperty") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Subproperty") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaProvisionSubpropertyResponse: Response message for ProvisionSubproperty RPC.

func (GoogleAnalyticsAdminV1alphaProvisionSubpropertyResponse) MarshalJSON ¶
added in v0.191.0
func (s GoogleAnalyticsAdminV1alphaProvisionSubpropertyResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaReorderEventEditRulesRequest ¶
added in v0.183.0
type GoogleAnalyticsAdminV1alphaReorderEventEditRulesRequest struct {
	// EventEditRules: Required. EventEditRule resource names for the specified
	// data stream, in the needed processing order. All EventEditRules for the
	// stream must be present in the list.
	EventEditRules []string `json:"eventEditRules,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EventEditRules") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EventEditRules") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaReorderEventEditRulesRequest: Request message for ReorderEventEditRules RPC.

func (GoogleAnalyticsAdminV1alphaReorderEventEditRulesRequest) MarshalJSON ¶
added in v0.183.0
func (s GoogleAnalyticsAdminV1alphaReorderEventEditRulesRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaReportingDataAnnotation ¶
added in v0.229.0
type GoogleAnalyticsAdminV1alphaReportingDataAnnotation struct {
	// AnnotationDate: If set, the Reporting Data Annotation is for a specific date
	// represented by this field. The date must be a valid date with year, month
	// and day set. The date may be in the past, present, or future.
	AnnotationDate *GoogleTypeDate `json:"annotationDate,omitempty"`
	// AnnotationDateRange: If set, the Reporting Data Annotation is for a range of
	// dates represented by this field.
	AnnotationDateRange *GoogleAnalyticsAdminV1alphaReportingDataAnnotationDateRange `json:"annotationDateRange,omitempty"`
	// Color: Required. The color used for display of this Reporting Data
	// Annotation.
	//
	// Possible values:
	//   "COLOR_UNSPECIFIED" - Color unknown or not specified.
	//   "PURPLE" - Purple color.
	//   "BROWN" - Brown color.
	//   "BLUE" - Blue color.
	//   "GREEN" - Green color.
	//   "RED" - Red color.
	//   "CYAN" - Cyan color.
	//   "ORANGE" - Orange color. (Only used for system-generated annotations)
	Color string `json:"color,omitempty"`
	// Description: Optional. Description for this Reporting Data Annotation.
	Description string `json:"description,omitempty"`
	// Name: Required. Identifier. Resource name of this Reporting Data Annotation.
	// Format:
	// 'properties/{property_id}/reportingDataAnnotations/{reporting_data_annotation
	// }' Format: 'properties/123/reportingDataAnnotations/456'
	Name string `json:"name,omitempty"`
	// SystemGenerated: Output only. If true, this annotation was generated by the
	// Google Analytics system. System-generated annotations cannot be updated or
	// deleted.
	SystemGenerated bool `json:"systemGenerated,omitempty"`
	// Title: Required. Human-readable title for this Reporting Data Annotation.
	Title string `json:"title,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AnnotationDate") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AnnotationDate") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaReportingDataAnnotation: A Reporting Data Annotation is a comment connected to certain dates for reporting data.

func (GoogleAnalyticsAdminV1alphaReportingDataAnnotation) MarshalJSON ¶
added in v0.229.0
func (s GoogleAnalyticsAdminV1alphaReportingDataAnnotation) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaReportingDataAnnotationDateRange ¶
added in v0.229.0
type GoogleAnalyticsAdminV1alphaReportingDataAnnotationDateRange struct {
	// EndDate: Required. The end date for this range. Must be a valid date with
	// year, month, and day set. This date must be greater than or equal to the
	// start date.
	EndDate *GoogleTypeDate `json:"endDate,omitempty"`
	// StartDate: Required. The start date for this range. Must be a valid date
	// with year, month, and day set. The date may be in the past, present, or
	// future.
	StartDate *GoogleTypeDate `json:"startDate,omitempty"`
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

GoogleAnalyticsAdminV1alphaReportingDataAnnotationDateRange: Represents a Reporting Data Annotation's date range, both start and end dates are inclusive. Time zones are based on the parent property.

func (GoogleAnalyticsAdminV1alphaReportingDataAnnotationDateRange) MarshalJSON ¶
added in v0.229.0
func (s GoogleAnalyticsAdminV1alphaReportingDataAnnotationDateRange) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaReportingIdentitySettings ¶
added in v0.240.0
type GoogleAnalyticsAdminV1alphaReportingIdentitySettings struct {
	// Name: Output only. Identifier. Resource name for this reporting identity
	// settings singleton resource. Format:
	// properties/{property_id}/reportingIdentitySettings Example:
	// "properties/1234/reportingIdentitySettings"
	Name string `json:"name,omitempty"`
	// ReportingIdentity: The strategy used for identifying user identities in
	// reports.
	//
	// Possible values:
	//   "IDENTITY_BLENDING_STRATEGY_UNSPECIFIED" - Unspecified blending strategy.
	//   "BLENDED" - Blended reporting identity strategy.
	//   "OBSERVED" - Observed reporting identity strategy.
	//   "DEVICE_BASED" - Device-based reporting identity strategy.
	ReportingIdentity string `json:"reportingIdentity,omitempty"`

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

GoogleAnalyticsAdminV1alphaReportingIdentitySettings: A resource containing settings related to reporting identity.

func (GoogleAnalyticsAdminV1alphaReportingIdentitySettings) MarshalJSON ¶
added in v0.240.0
func (s GoogleAnalyticsAdminV1alphaReportingIdentitySettings) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaRollupPropertySourceLink ¶
added in v0.144.0
type GoogleAnalyticsAdminV1alphaRollupPropertySourceLink struct {
	// Name: Output only. Resource name of this RollupPropertySourceLink. Format:
	// 'properties/{property_id}/rollupPropertySourceLinks/{rollup_property_source_l
	// ink}' Format: 'properties/123/rollupPropertySourceLinks/456'
	Name string `json:"name,omitempty"`
	// SourceProperty: Immutable. Resource name of the source property. Format:
	// properties/{property_id} Example: "properties/789"
	SourceProperty string `json:"sourceProperty,omitempty"`

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

GoogleAnalyticsAdminV1alphaRollupPropertySourceLink: A link that references a source property under the parent rollup property.

func (GoogleAnalyticsAdminV1alphaRollupPropertySourceLink) MarshalJSON ¶
added in v0.144.0
func (s GoogleAnalyticsAdminV1alphaRollupPropertySourceLink) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaRunAccessReportRequest ¶
added in v0.86.0
type GoogleAnalyticsAdminV1alphaRunAccessReportRequest struct {
	// DateRanges: Date ranges of access records to read. If multiple date ranges
	// are requested, each response row will contain a zero based date range index.
	// If two date ranges overlap, the access records for the overlapping days is
	// included in the response rows for both date ranges. Requests are allowed up
	// to 2 date ranges.
	DateRanges []*GoogleAnalyticsAdminV1alphaAccessDateRange `json:"dateRanges,omitempty"`
	// DimensionFilter: Dimension filters let you restrict report response to
	// specific dimension values which match the filter. For example, filtering on
	// access records of a single user. To learn more, see Fundamentals of
	// Dimension Filters
	// (https://developers.google.com/analytics/devguides/reporting/data/v1/basics#dimension_filters)
	// for examples. Metrics cannot be used in this filter.
	DimensionFilter *GoogleAnalyticsAdminV1alphaAccessFilterExpression `json:"dimensionFilter,omitempty"`
	// Dimensions: The dimensions requested and displayed in the response. Requests
	// are allowed up to 9 dimensions.
	Dimensions []*GoogleAnalyticsAdminV1alphaAccessDimension `json:"dimensions,omitempty"`
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
	MetricFilter *GoogleAnalyticsAdminV1alphaAccessFilterExpression `json:"metricFilter,omitempty"`
	// Metrics: The metrics requested and displayed in the response. Requests are
	// allowed up to 10 metrics.
	Metrics []*GoogleAnalyticsAdminV1alphaAccessMetric `json:"metrics,omitempty"`
	// Offset: The row count of the start row. The first row is counted as row 0.
	// If offset is unspecified, it is treated as 0. If offset is zero, then this
	// method will return the first page of results with `limit` entries. To learn
	// more about this pagination parameter, see Pagination
	// (https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination).
	Offset int64 `json:"offset,omitempty,string"`
	// OrderBys: Specifies how rows are ordered in the response.
	OrderBys []*GoogleAnalyticsAdminV1alphaAccessOrderBy `json:"orderBys,omitempty"`
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

GoogleAnalyticsAdminV1alphaRunAccessReportRequest: The request for a Data Access Record Report.

func (GoogleAnalyticsAdminV1alphaRunAccessReportRequest) MarshalJSON ¶
added in v0.86.0
func (s GoogleAnalyticsAdminV1alphaRunAccessReportRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaRunAccessReportResponse ¶
added in v0.86.0
type GoogleAnalyticsAdminV1alphaRunAccessReportResponse struct {
	// DimensionHeaders: The header for a column in the report that corresponds to
	// a specific dimension. The number of DimensionHeaders and ordering of
	// DimensionHeaders matches the dimensions present in rows.
	DimensionHeaders []*GoogleAnalyticsAdminV1alphaAccessDimensionHeader `json:"dimensionHeaders,omitempty"`
	// MetricHeaders: The header for a column in the report that corresponds to a
	// specific metric. The number of MetricHeaders and ordering of MetricHeaders
	// matches the metrics present in rows.
	MetricHeaders []*GoogleAnalyticsAdminV1alphaAccessMetricHeader `json:"metricHeaders,omitempty"`
	// Quota: The quota state for this Analytics property including this request.
	// This field doesn't work with account-level requests.
	Quota *GoogleAnalyticsAdminV1alphaAccessQuota `json:"quota,omitempty"`
	// RowCount: The total number of rows in the query result. `rowCount` is
	// independent of the number of rows returned in the response, the `limit`
	// request parameter, and the `offset` request parameter. For example if a
	// query returns 175 rows and includes `limit` of 50 in the API request, the
	// response will contain `rowCount` of 175 but only 50 rows. To learn more
	// about this pagination parameter, see Pagination
	// (https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination).
	RowCount int64 `json:"rowCount,omitempty"`
	// Rows: Rows of dimension value combinations and metric values in the report.
	Rows []*GoogleAnalyticsAdminV1alphaAccessRow `json:"rows,omitempty"`

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

GoogleAnalyticsAdminV1alphaRunAccessReportResponse: The customized Data Access Record Report response.

func (GoogleAnalyticsAdminV1alphaRunAccessReportResponse) MarshalJSON ¶
added in v0.86.0
func (s GoogleAnalyticsAdminV1alphaRunAccessReportResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchema ¶
added in v0.139.0
type GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchema struct {
	// ApplyConversionValues: If enabled, the GA SDK will set conversion values
	// using this schema definition, and schema will be exported to any Google Ads
	// accounts linked to this property. If disabled, the GA SDK will not
	// automatically set conversion values, and also the schema will not be
	// exported to Ads.
	ApplyConversionValues bool `json:"applyConversionValues,omitempty"`
	// Name: Output only. Resource name of the schema. This will be child of ONLY
	// an iOS stream, and there can be at most one such child under an iOS stream.
	// Format:
	// properties/{property}/dataStreams/{dataStream}/sKAdNetworkConversionValueSche
	// ma
	Name string `json:"name,omitempty"`
	// PostbackWindowOne: Required. The conversion value settings for the first
	// postback window. These differ from values for postback window two and three
	// in that they contain a "Fine" grained conversion value (a numeric value).
	// Conversion values for this postback window must be set. The other windows
	// are optional and may inherit this window's settings if unset or disabled.
	PostbackWindowOne *GoogleAnalyticsAdminV1alphaPostbackWindow `json:"postbackWindowOne,omitempty"`
	// PostbackWindowThree: The conversion value settings for the third postback
	// window. This field should only be set if the user chose to define different
	// conversion values for this postback window. It is allowed to configure
	// window 3 without setting window 2. In case window 1 & 2 settings are set and
	// enable_postback_window_settings for this postback window is set to false,
	// the schema will inherit settings from postback_window_two.
	PostbackWindowThree *GoogleAnalyticsAdminV1alphaPostbackWindow `json:"postbackWindowThree,omitempty"`
	// PostbackWindowTwo: The conversion value settings for the second postback
	// window. This field should only be configured if there is a need to define
	// different conversion values for this postback window. If
	// enable_postback_window_settings is set to false for this postback window,
	// the values from postback_window_one will be used.
	PostbackWindowTwo *GoogleAnalyticsAdminV1alphaPostbackWindow `json:"postbackWindowTwo,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ApplyConversionValues") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApplyConversionValues") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchema: SKAdNetwork conversion value schema of an iOS stream.

func (GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchema) MarshalJSON ¶
added in v0.139.0
func (s GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchema) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaSearchAds360Link ¶
added in v0.100.0
type GoogleAnalyticsAdminV1alphaSearchAds360Link struct {
	// AdsPersonalizationEnabled: Enables personalized advertising features with
	// this integration. If this field is not set on create, it will be defaulted
	// to true.
	AdsPersonalizationEnabled bool `json:"adsPersonalizationEnabled,omitempty"`
	// AdvertiserDisplayName: Output only. The display name of the Search Ads 360
	// Advertiser. Allows users to easily identify the linked resource.
	AdvertiserDisplayName string `json:"advertiserDisplayName,omitempty"`
	// AdvertiserId: Immutable. This field represents the Advertiser ID of the
	// Search Ads 360 Advertiser. that has been linked.
	AdvertiserId string `json:"advertiserId,omitempty"`
	// CampaignDataSharingEnabled: Immutable. Enables the import of campaign data
	// from Search Ads 360 into the Google Analytics property. After link creation,
	// this can only be updated from the Search Ads 360 product. If this field is
	// not set on create, it will be defaulted to true.
	CampaignDataSharingEnabled bool `json:"campaignDataSharingEnabled,omitempty"`
	// CostDataSharingEnabled: Immutable. Enables the import of cost data from
	// Search Ads 360 to the Google Analytics property. This can only be enabled if
	// campaign_data_sharing_enabled is enabled. After link creation, this can only
	// be updated from the Search Ads 360 product. If this field is not set on
	// create, it will be defaulted to true.
	CostDataSharingEnabled bool `json:"costDataSharingEnabled,omitempty"`
	// Name: Output only. The resource name for this SearchAds360Link resource.
	// Format: properties/{propertyId}/searchAds360Links/{linkId} Note: linkId is
	// not the Search Ads 360 advertiser ID
	Name string `json:"name,omitempty"`
	// SiteStatsSharingEnabled: Enables export of site stats with this integration.
	// If this field is not set on create, it will be defaulted to true.
	SiteStatsSharingEnabled bool `json:"siteStatsSharingEnabled,omitempty"`

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

GoogleAnalyticsAdminV1alphaSearchAds360Link: A link between a Google Analytics property and a Search Ads 360 entity.

func (GoogleAnalyticsAdminV1alphaSearchAds360Link) MarshalJSON ¶
added in v0.100.0
func (s GoogleAnalyticsAdminV1alphaSearchAds360Link) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsRequest ¶
added in v0.41.0
type GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsRequest struct {
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
	//   "SEARCH_ADS_360_LINK" - SearchAds360Link resource
	//   "DATA_STREAM" - DataStream resource
	//   "ATTRIBUTION_SETTINGS" - AttributionSettings resource
	//   "EXPANDED_DATA_SET" - ExpandedDataSet resource
	//   "CHANNEL_GROUP" - ChannelGroup resource
	//   "BIGQUERY_LINK" - BigQuery link resource
	//   "ENHANCED_MEASUREMENT_SETTINGS" - EnhancedMeasurementSettings resource
	//   "DATA_REDACTION_SETTINGS" - DataRedactionSettings resource
	//   "SKADNETWORK_CONVERSION_VALUE_SCHEMA" - SKAdNetworkConversionValueSchema
	// resource
	//   "ADSENSE_LINK" - AdSenseLink resource
	//   "AUDIENCE" - Audience resource
	//   "EVENT_CREATE_RULE" - EventCreateRule resource
	//   "KEY_EVENT" - KeyEvent resource
	//   "CALCULATED_METRIC" - CalculatedMetric resource
	//   "REPORTING_DATA_ANNOTATION" - ReportingDataAnnotation resource
	//   "SUBPROPERTY_SYNC_CONFIG" - SubpropertySyncConfig resource
	//   "REPORTING_IDENTITY_SETTINGS" - ReportingIdentitySettings resource
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

GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsRequest: Request message for SearchChangeHistoryEvents RPC.

func (GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsRequest) MarshalJSON ¶
added in v0.41.0
func (s GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsResponse ¶
added in v0.41.0
type GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsResponse struct {
	// ChangeHistoryEvents: Results that were accessible to the caller.
	ChangeHistoryEvents []*GoogleAnalyticsAdminV1alphaChangeHistoryEvent `json:"changeHistoryEvents,omitempty"`
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

GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsResponse: Response message for SearchAccounts RPC.

func (GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsResponse) MarshalJSON ¶
added in v0.41.0
func (s GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaSubmitUserDeletionRequest ¶
added in v0.244.0
type GoogleAnalyticsAdminV1alphaSubmitUserDeletionRequest struct {
	// AppInstanceId: Firebase application instance ID
	// (https://firebase.google.com/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.html#getAppInstanceId).
	AppInstanceId string `json:"appInstanceId,omitempty"`
	// ClientId: Google Analytics client ID
	// (https://support.google.com/analytics/answer/11593727).
	ClientId string `json:"clientId,omitempty"`
	// UserId: Google Analytics user ID
	// (https://firebase.google.com/docs/analytics/userid).
	UserId string `json:"userId,omitempty"`
	// UserProvidedData: User-provided data
	// (https://support.google.com/analytics/answer/14077171). May contain either
	// one email address or one phone number. Email addresses should be normalized
	// as such: * lowercase * remove periods before @ for gmail.com/googlemail.com
	// addresses * remove all spaces Phone numbers should be normalized as such: *
	// remove all non digit characters * add + prefix
	UserProvidedData string `json:"userProvidedData,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AppInstanceId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AppInstanceId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaSubmitUserDeletionRequest: Request message for SubmitUserDeletion RPC.

func (GoogleAnalyticsAdminV1alphaSubmitUserDeletionRequest) MarshalJSON ¶
added in v0.244.0
func (s GoogleAnalyticsAdminV1alphaSubmitUserDeletionRequest) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaSubmitUserDeletionResponse ¶
added in v0.244.0
type GoogleAnalyticsAdminV1alphaSubmitUserDeletionResponse struct {
	// DeletionRequestTime: Marks the moment for which all visitor data before this
	// point should be deleted. This is set to the time at which the deletion
	// request was received.
	DeletionRequestTime string `json:"deletionRequestTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DeletionRequestTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DeletionRequestTime") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaSubmitUserDeletionResponse: Response message for SubmitUserDeletion RPC.

func (GoogleAnalyticsAdminV1alphaSubmitUserDeletionResponse) MarshalJSON ¶
added in v0.244.0
func (s GoogleAnalyticsAdminV1alphaSubmitUserDeletionResponse) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaSubpropertyEventFilter ¶
added in v0.144.0
type GoogleAnalyticsAdminV1alphaSubpropertyEventFilter struct {
	// ApplyToProperty: Immutable. Resource name of the Subproperty that uses this
	// filter.
	ApplyToProperty string `json:"applyToProperty,omitempty"`
	// FilterClauses: Required. Unordered list. Filter clauses that define the
	// SubpropertyEventFilter. All clauses are AND'ed together to determine what
	// data is sent to the subproperty.
	FilterClauses []*GoogleAnalyticsAdminV1alphaSubpropertyEventFilterClause `json:"filterClauses,omitempty"`
	// Name: Output only. Format:
	// properties/{ordinary_property_id}/subpropertyEventFilters/{sub_property_event
	// _filter} Example: properties/1234/subpropertyEventFilters/5678
	Name string `json:"name,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ApplyToProperty") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApplyToProperty") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaSubpropertyEventFilter: A resource message representing a Google Analytics subproperty event filter.

func (GoogleAnalyticsAdminV1alphaSubpropertyEventFilter) MarshalJSON ¶
added in v0.144.0
func (s GoogleAnalyticsAdminV1alphaSubpropertyEventFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaSubpropertyEventFilterClause ¶
added in v0.144.0
type GoogleAnalyticsAdminV1alphaSubpropertyEventFilterClause struct {
	// FilterClauseType: Required. The type for the filter clause.
	//
	// Possible values:
	//   "FILTER_CLAUSE_TYPE_UNSPECIFIED" - Filter clause type unknown or not
	// specified.
	//   "INCLUDE" - Events will be included in the Sub property if the filter
	// clause is met.
	//   "EXCLUDE" - Events will be excluded from the Sub property if the filter
	// clause is met.
	FilterClauseType string `json:"filterClauseType,omitempty"`
	// FilterExpression: Required. The logical expression for what events are sent
	// to the subproperty.
	FilterExpression *GoogleAnalyticsAdminV1alphaSubpropertyEventFilterExpression `json:"filterExpression,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FilterClauseType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FilterClauseType") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaSubpropertyEventFilterClause: A clause for defining a filter. A filter may be inclusive (events satisfying the filter clause are included in the subproperty's data) or exclusive (events satisfying the filter clause are excluded from the subproperty's data).

func (GoogleAnalyticsAdminV1alphaSubpropertyEventFilterClause) MarshalJSON ¶
added in v0.144.0
func (s GoogleAnalyticsAdminV1alphaSubpropertyEventFilterClause) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaSubpropertyEventFilterCondition ¶
added in v0.144.0
type GoogleAnalyticsAdminV1alphaSubpropertyEventFilterCondition struct {
	// FieldName: Required. The field that is being filtered.
	FieldName string `json:"fieldName,omitempty"`
	// NullFilter: A filter for null values.
	NullFilter bool `json:"nullFilter,omitempty"`
	// StringFilter: A filter for a string-type dimension that matches a particular
	// pattern.
	StringFilter *GoogleAnalyticsAdminV1alphaSubpropertyEventFilterConditionStringFilter `json:"stringFilter,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FieldName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FieldName") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaSubpropertyEventFilterCondition: A specific filter expression

func (GoogleAnalyticsAdminV1alphaSubpropertyEventFilterCondition) MarshalJSON ¶
added in v0.144.0
func (s GoogleAnalyticsAdminV1alphaSubpropertyEventFilterCondition) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaSubpropertyEventFilterConditionStringFilter ¶
added in v0.144.0
type GoogleAnalyticsAdminV1alphaSubpropertyEventFilterConditionStringFilter struct {
	// CaseSensitive: Optional. If true, the string value is case sensitive. If
	// false, the match is case-insensitive.
	CaseSensitive bool `json:"caseSensitive,omitempty"`
	// MatchType: Required. The match type for the string filter.
	//
	// Possible values:
	//   "MATCH_TYPE_UNSPECIFIED" - Match type unknown or not specified.
	//   "EXACT" - Exact match of the string value.
	//   "BEGINS_WITH" - Begins with the string value.
	//   "ENDS_WITH" - Ends with the string value.
	//   "CONTAINS" - Contains the string value.
	//   "FULL_REGEXP" - Full regular expression matches with the string value.
	//   "PARTIAL_REGEXP" - Partial regular expression matches with the string
	// value.
	MatchType string `json:"matchType,omitempty"`
	// Value: Required. The string value used for the matching.
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

GoogleAnalyticsAdminV1alphaSubpropertyEventFilterConditionStringFilter: A filter for a string-type dimension that matches a particular pattern.

func (GoogleAnalyticsAdminV1alphaSubpropertyEventFilterConditionStringFilter) MarshalJSON ¶
added in v0.144.0
func (s GoogleAnalyticsAdminV1alphaSubpropertyEventFilterConditionStringFilter) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaSubpropertyEventFilterExpression ¶
added in v0.144.0
type GoogleAnalyticsAdminV1alphaSubpropertyEventFilterExpression struct {
	// FilterCondition: Creates a filter that matches a specific event. This cannot
	// be set on the top level SubpropertyEventFilterExpression.
	FilterCondition *GoogleAnalyticsAdminV1alphaSubpropertyEventFilterCondition `json:"filterCondition,omitempty"`
	// NotExpression: A filter expression to be NOT'ed (inverted, complemented). It
	// can only include a filter. This cannot be set on the top level
	// SubpropertyEventFilterExpression.
	NotExpression *GoogleAnalyticsAdminV1alphaSubpropertyEventFilterExpression `json:"notExpression,omitempty"`
	// OrGroup: A list of expressions to OR’ed together. Must only contain
	// not_expression or filter_condition expressions.
	OrGroup *GoogleAnalyticsAdminV1alphaSubpropertyEventFilterExpressionList `json:"orGroup,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FilterCondition") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FilterCondition") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaSubpropertyEventFilterExpression: A logical expression of Subproperty event filters.

func (GoogleAnalyticsAdminV1alphaSubpropertyEventFilterExpression) MarshalJSON ¶
added in v0.144.0
func (s GoogleAnalyticsAdminV1alphaSubpropertyEventFilterExpression) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaSubpropertyEventFilterExpressionList ¶
added in v0.144.0
type GoogleAnalyticsAdminV1alphaSubpropertyEventFilterExpressionList struct {
	// FilterExpressions: Required. Unordered list. A list of Subproperty event
	// filter expressions
	FilterExpressions []*GoogleAnalyticsAdminV1alphaSubpropertyEventFilterExpression `json:"filterExpressions,omitempty"`
	// ForceSendFields is a list of field names (e.g. "FilterExpressions") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FilterExpressions") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaSubpropertyEventFilterExpressionList: A list of Subproperty event filter expressions.

func (GoogleAnalyticsAdminV1alphaSubpropertyEventFilterExpressionList) MarshalJSON ¶
added in v0.144.0
func (s GoogleAnalyticsAdminV1alphaSubpropertyEventFilterExpressionList) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaSubpropertySyncConfig ¶
added in v0.237.0
type GoogleAnalyticsAdminV1alphaSubpropertySyncConfig struct {
	// ApplyToProperty: Output only. Immutable. Resource name of the subproperty
	// that these settings apply to.
	ApplyToProperty string `json:"applyToProperty,omitempty"`
	// CustomDimensionAndMetricSyncMode: Required. Specifies the Custom Dimension /
	// Metric synchronization mode for the subproperty. If set to ALL, Custom
	// Dimension / Metric synchronization will be immediately enabled. Local
	// configuration of Custom Dimensions / Metrics will not be allowed on the
	// subproperty so long as the synchronization mode is set to ALL. If set to
	// NONE, Custom Dimensions / Metric synchronization is disabled. Custom
	// Dimensions / Metrics must be configured explicitly on the Subproperty.
	//
	// Possible values:
	//   "SYNCHRONIZATION_MODE_UNSPECIFIED" - Synchronization mode unknown or not
	// specified.
	//   "NONE" - Entities are not synchronized. Local edits are allowed on the
	// subproperty.
	//   "ALL" - Entities are synchronized from parent property. Local mutations
	// are not allowed on the subproperty (Create / Update / Delete)
	CustomDimensionAndMetricSyncMode string `json:"customDimensionAndMetricSyncMode,omitempty"`
	// Name: Output only. Identifier. Format:
	// properties/{ordinary_property_id}/subpropertySyncConfigs/{subproperty_id}
	// Example: properties/1234/subpropertySyncConfigs/5678
	Name string `json:"name,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ApplyToProperty") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApplyToProperty") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaSubpropertySyncConfig: Subproperty synchronization configuration controls how ordinary property configurations are synchronized to subproperties. This resource is provisioned automatically for each subproperty.

func (GoogleAnalyticsAdminV1alphaSubpropertySyncConfig) MarshalJSON ¶
added in v0.237.0
func (s GoogleAnalyticsAdminV1alphaSubpropertySyncConfig) MarshalJSON() ([]byte, error)
type GoogleAnalyticsAdminV1alphaUpdateAccessBindingRequest ¶
added in v0.110.0
type GoogleAnalyticsAdminV1alphaUpdateAccessBindingRequest struct {
	// AccessBinding: Required. The access binding to update.
	AccessBinding *GoogleAnalyticsAdminV1alphaAccessBinding `json:"accessBinding,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AccessBinding") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccessBinding") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleAnalyticsAdminV1alphaUpdateAccessBindingRequest: Request message for UpdateAccessBinding RPC.

func (GoogleAnalyticsAdminV1alphaUpdateAccessBindingRequest) MarshalJSON ¶
added in v0.110.0
func (s GoogleAnalyticsAdminV1alphaUpdateAccessBindingRequest) MarshalJSON() ([]byte, error)
type GoogleProtobufEmpty ¶
type GoogleProtobufEmpty struct {
	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
}

GoogleProtobufEmpty: A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }

type GoogleTypeDate ¶
added in v0.229.0
type GoogleTypeDate struct {
	// Day: Day of a month. Must be from 1 to 31 and valid for the year and month,
	// or 0 to specify a year by itself or a year and month where the day isn't
	// significant.
	Day int64 `json:"day,omitempty"`
	// Month: Month of a year. Must be from 1 to 12, or 0 to specify a year without
	// a month and day.
	Month int64 `json:"month,omitempty"`
	// Year: Year of the date. Must be from 1 to 9999, or 0 to specify a date
	// without a year.
	Year int64 `json:"year,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Day") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Day") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleTypeDate: Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following: * A full date, with non-zero year, month, and day values. * A month and day, with a zero year (for example, an anniversary). * A year on its own, with a zero month and a zero day. * A year and month, with a zero day (for example, a credit card expiration date). Related types: * google.type.TimeOfDay * google.type.DateTime * google.protobuf.Timestamp

func (GoogleTypeDate) MarshalJSON ¶
added in v0.229.0
func (s GoogleTypeDate) MarshalJSON() ([]byte, error)
type PropertiesAccessBindingsBatchCreateCall ¶
added in v0.110.0
type PropertiesAccessBindingsBatchCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesAccessBindingsBatchCreateCall) Context ¶
added in v0.110.0
func (c *PropertiesAccessBindingsBatchCreateCall) Context(ctx context.Context) *PropertiesAccessBindingsBatchCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesAccessBindingsBatchCreateCall) Do ¶
added in v0.110.0
func (c *PropertiesAccessBindingsBatchCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsResponse, error)

Do executes the "analyticsadmin.properties.accessBindings.batchCreate" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsResponse.ServerResponse. Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesAccessBindingsBatchCreateCall) Fields ¶
added in v0.110.0
func (c *PropertiesAccessBindingsBatchCreateCall) Fields(s ...googleapi.Field) *PropertiesAccessBindingsBatchCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesAccessBindingsBatchCreateCall) Header ¶
added in v0.110.0
func (c *PropertiesAccessBindingsBatchCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesAccessBindingsBatchDeleteCall ¶
added in v0.110.0
type PropertiesAccessBindingsBatchDeleteCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesAccessBindingsBatchDeleteCall) Context ¶
added in v0.110.0
func (c *PropertiesAccessBindingsBatchDeleteCall) Context(ctx context.Context) *PropertiesAccessBindingsBatchDeleteCall

Context sets the context to be used in this call's Do method.

func (*PropertiesAccessBindingsBatchDeleteCall) Do ¶
added in v0.110.0
func (c *PropertiesAccessBindingsBatchDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.properties.accessBindings.batchDelete" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesAccessBindingsBatchDeleteCall) Fields ¶
added in v0.110.0
func (c *PropertiesAccessBindingsBatchDeleteCall) Fields(s ...googleapi.Field) *PropertiesAccessBindingsBatchDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesAccessBindingsBatchDeleteCall) Header ¶
added in v0.110.0
func (c *PropertiesAccessBindingsBatchDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesAccessBindingsBatchGetCall ¶
added in v0.110.0
type PropertiesAccessBindingsBatchGetCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesAccessBindingsBatchGetCall) Context ¶
added in v0.110.0
func (c *PropertiesAccessBindingsBatchGetCall) Context(ctx context.Context) *PropertiesAccessBindingsBatchGetCall

Context sets the context to be used in this call's Do method.

func (*PropertiesAccessBindingsBatchGetCall) Do ¶
added in v0.110.0
func (c *PropertiesAccessBindingsBatchGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaBatchGetAccessBindingsResponse, error)

Do executes the "analyticsadmin.properties.accessBindings.batchGet" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaBatchGetAccessBindingsResponse.ServerResponse.Hea der or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesAccessBindingsBatchGetCall) Fields ¶
added in v0.110.0
func (c *PropertiesAccessBindingsBatchGetCall) Fields(s ...googleapi.Field) *PropertiesAccessBindingsBatchGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesAccessBindingsBatchGetCall) Header ¶
added in v0.110.0
func (c *PropertiesAccessBindingsBatchGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesAccessBindingsBatchGetCall) IfNoneMatch ¶
added in v0.110.0
func (c *PropertiesAccessBindingsBatchGetCall) IfNoneMatch(entityTag string) *PropertiesAccessBindingsBatchGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesAccessBindingsBatchGetCall) Names ¶
added in v0.110.0
func (c *PropertiesAccessBindingsBatchGetCall) Names(names ...string) *PropertiesAccessBindingsBatchGetCall

Names sets the optional parameter "names": Required. The names of the access bindings to retrieve. A maximum of 1000 access bindings can be retrieved in a batch. Formats: - accounts/{account}/accessBindings/{accessBinding} - properties/{property}/accessBindings/{accessBinding}

type PropertiesAccessBindingsBatchUpdateCall ¶
added in v0.110.0
type PropertiesAccessBindingsBatchUpdateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesAccessBindingsBatchUpdateCall) Context ¶
added in v0.110.0
func (c *PropertiesAccessBindingsBatchUpdateCall) Context(ctx context.Context) *PropertiesAccessBindingsBatchUpdateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesAccessBindingsBatchUpdateCall) Do ¶
added in v0.110.0
func (c *PropertiesAccessBindingsBatchUpdateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsResponse, error)

Do executes the "analyticsadmin.properties.accessBindings.batchUpdate" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsResponse.ServerResponse. Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesAccessBindingsBatchUpdateCall) Fields ¶
added in v0.110.0
func (c *PropertiesAccessBindingsBatchUpdateCall) Fields(s ...googleapi.Field) *PropertiesAccessBindingsBatchUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesAccessBindingsBatchUpdateCall) Header ¶
added in v0.110.0
func (c *PropertiesAccessBindingsBatchUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesAccessBindingsCreateCall ¶
added in v0.110.0
type PropertiesAccessBindingsCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesAccessBindingsCreateCall) Context ¶
added in v0.110.0
func (c *PropertiesAccessBindingsCreateCall) Context(ctx context.Context) *PropertiesAccessBindingsCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesAccessBindingsCreateCall) Do ¶
added in v0.110.0
func (c *PropertiesAccessBindingsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAccessBinding, error)

Do executes the "analyticsadmin.properties.accessBindings.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaAccessBinding.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesAccessBindingsCreateCall) Fields ¶
added in v0.110.0
func (c *PropertiesAccessBindingsCreateCall) Fields(s ...googleapi.Field) *PropertiesAccessBindingsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesAccessBindingsCreateCall) Header ¶
added in v0.110.0
func (c *PropertiesAccessBindingsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesAccessBindingsDeleteCall ¶
added in v0.110.0
type PropertiesAccessBindingsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesAccessBindingsDeleteCall) Context ¶
added in v0.110.0
func (c *PropertiesAccessBindingsDeleteCall) Context(ctx context.Context) *PropertiesAccessBindingsDeleteCall

Context sets the context to be used in this call's Do method.

func (*PropertiesAccessBindingsDeleteCall) Do ¶
added in v0.110.0
func (c *PropertiesAccessBindingsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.properties.accessBindings.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesAccessBindingsDeleteCall) Fields ¶
added in v0.110.0
func (c *PropertiesAccessBindingsDeleteCall) Fields(s ...googleapi.Field) *PropertiesAccessBindingsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesAccessBindingsDeleteCall) Header ¶
added in v0.110.0
func (c *PropertiesAccessBindingsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesAccessBindingsGetCall ¶
added in v0.110.0
type PropertiesAccessBindingsGetCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesAccessBindingsGetCall) Context ¶
added in v0.110.0
func (c *PropertiesAccessBindingsGetCall) Context(ctx context.Context) *PropertiesAccessBindingsGetCall

Context sets the context to be used in this call's Do method.

func (*PropertiesAccessBindingsGetCall) Do ¶
added in v0.110.0
func (c *PropertiesAccessBindingsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAccessBinding, error)

Do executes the "analyticsadmin.properties.accessBindings.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaAccessBinding.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesAccessBindingsGetCall) Fields ¶
added in v0.110.0
func (c *PropertiesAccessBindingsGetCall) Fields(s ...googleapi.Field) *PropertiesAccessBindingsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesAccessBindingsGetCall) Header ¶
added in v0.110.0
func (c *PropertiesAccessBindingsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesAccessBindingsGetCall) IfNoneMatch ¶
added in v0.110.0
func (c *PropertiesAccessBindingsGetCall) IfNoneMatch(entityTag string) *PropertiesAccessBindingsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesAccessBindingsListCall ¶
added in v0.110.0
type PropertiesAccessBindingsListCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesAccessBindingsListCall) Context ¶
added in v0.110.0
func (c *PropertiesAccessBindingsListCall) Context(ctx context.Context) *PropertiesAccessBindingsListCall

Context sets the context to be used in this call's Do method.

func (*PropertiesAccessBindingsListCall) Do ¶
added in v0.110.0
func (c *PropertiesAccessBindingsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListAccessBindingsResponse, error)

Do executes the "analyticsadmin.properties.accessBindings.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaListAccessBindingsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesAccessBindingsListCall) Fields ¶
added in v0.110.0
func (c *PropertiesAccessBindingsListCall) Fields(s ...googleapi.Field) *PropertiesAccessBindingsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesAccessBindingsListCall) Header ¶
added in v0.110.0
func (c *PropertiesAccessBindingsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesAccessBindingsListCall) IfNoneMatch ¶
added in v0.110.0
func (c *PropertiesAccessBindingsListCall) IfNoneMatch(entityTag string) *PropertiesAccessBindingsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesAccessBindingsListCall) PageSize ¶
added in v0.110.0
func (c *PropertiesAccessBindingsListCall) PageSize(pageSize int64) *PropertiesAccessBindingsListCall

PageSize sets the optional parameter "pageSize": The maximum number of access bindings to return. The service may return fewer than this value. If unspecified, at most 200 access bindings will be returned. The maximum value is 500; values above 500 will be coerced to 500.

func (*PropertiesAccessBindingsListCall) PageToken ¶
added in v0.110.0
func (c *PropertiesAccessBindingsListCall) PageToken(pageToken string) *PropertiesAccessBindingsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListAccessBindings` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListAccessBindings` must match the call that provided the page token.

func (*PropertiesAccessBindingsListCall) Pages ¶
added in v0.110.0
func (c *PropertiesAccessBindingsListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1alphaListAccessBindingsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesAccessBindingsPatchCall ¶
added in v0.110.0
type PropertiesAccessBindingsPatchCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesAccessBindingsPatchCall) Context ¶
added in v0.110.0
func (c *PropertiesAccessBindingsPatchCall) Context(ctx context.Context) *PropertiesAccessBindingsPatchCall

Context sets the context to be used in this call's Do method.

func (*PropertiesAccessBindingsPatchCall) Do ¶
added in v0.110.0
func (c *PropertiesAccessBindingsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAccessBinding, error)

Do executes the "analyticsadmin.properties.accessBindings.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaAccessBinding.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesAccessBindingsPatchCall) Fields ¶
added in v0.110.0
func (c *PropertiesAccessBindingsPatchCall) Fields(s ...googleapi.Field) *PropertiesAccessBindingsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesAccessBindingsPatchCall) Header ¶
added in v0.110.0
func (c *PropertiesAccessBindingsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesAccessBindingsService ¶
added in v0.110.0
type PropertiesAccessBindingsService struct {
	// contains filtered or unexported fields
}
func NewPropertiesAccessBindingsService ¶
added in v0.110.0
func NewPropertiesAccessBindingsService(s *Service) *PropertiesAccessBindingsService
func (*PropertiesAccessBindingsService) BatchCreate ¶
added in v0.110.0
func (r *PropertiesAccessBindingsService) BatchCreate(parent string, googleanalyticsadminv1alphabatchcreateaccessbindingsrequest *GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsRequest) *PropertiesAccessBindingsBatchCreateCall

BatchCreate: Creates information about multiple access bindings to an account or property. This method is transactional. If any AccessBinding cannot be created, none of the AccessBindings will be created.

parent: The account or property that owns the access bindings. The parent field in the CreateAccessBindingRequest messages must either be empty or match this field. Formats: - accounts/{account} - properties/{property}.
func (*PropertiesAccessBindingsService) BatchDelete ¶
added in v0.110.0
func (r *PropertiesAccessBindingsService) BatchDelete(parent string, googleanalyticsadminv1alphabatchdeleteaccessbindingsrequest *GoogleAnalyticsAdminV1alphaBatchDeleteAccessBindingsRequest) *PropertiesAccessBindingsBatchDeleteCall

BatchDelete: Deletes information about multiple users' links to an account or property.

parent: The account or property that owns the access bindings. The parent of all provided values for the 'names' field in DeleteAccessBindingRequest messages must match this field. Formats: - accounts/{account} - properties/{property}.
func (*PropertiesAccessBindingsService) BatchGet ¶
added in v0.110.0
func (r *PropertiesAccessBindingsService) BatchGet(parent string) *PropertiesAccessBindingsBatchGetCall

BatchGet: Gets information about multiple access bindings to an account or property.

parent: The account or property that owns the access bindings. The parent of all provided values for the 'names' field must match this field. Formats: - accounts/{account} - properties/{property}.
func (*PropertiesAccessBindingsService) BatchUpdate ¶
added in v0.110.0
func (r *PropertiesAccessBindingsService) BatchUpdate(parent string, googleanalyticsadminv1alphabatchupdateaccessbindingsrequest *GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsRequest) *PropertiesAccessBindingsBatchUpdateCall

BatchUpdate: Updates information about multiple access bindings to an account or property.

parent: The account or property that owns the access bindings. The parent of all provided AccessBinding in UpdateAccessBindingRequest messages must match this field. Formats: - accounts/{account} - properties/{property}.
func (*PropertiesAccessBindingsService) Create ¶
added in v0.110.0
func (r *PropertiesAccessBindingsService) Create(parent string, googleanalyticsadminv1alphaaccessbinding *GoogleAnalyticsAdminV1alphaAccessBinding) *PropertiesAccessBindingsCreateCall

Create: Creates an access binding on an account or property.

- parent: Formats: - accounts/{account} - properties/{property}.

func (*PropertiesAccessBindingsService) Delete ¶
added in v0.110.0
func (r *PropertiesAccessBindingsService) Delete(name string) *PropertiesAccessBindingsDeleteCall

Delete: Deletes an access binding on an account or property.

name: Formats: - accounts/{account}/accessBindings/{accessBinding} - properties/{property}/accessBindings/{accessBinding}.
func (*PropertiesAccessBindingsService) Get ¶
added in v0.110.0
func (r *PropertiesAccessBindingsService) Get(name string) *PropertiesAccessBindingsGetCall

Get: Gets information about an access binding.

name: The name of the access binding to retrieve. Formats: - accounts/{account}/accessBindings/{accessBinding} - properties/{property}/accessBindings/{accessBinding}.
func (*PropertiesAccessBindingsService) List ¶
added in v0.110.0
func (r *PropertiesAccessBindingsService) List(parent string) *PropertiesAccessBindingsListCall

List: Lists all access bindings on an account or property.

- parent: Formats: - accounts/{account} - properties/{property}.

func (*PropertiesAccessBindingsService) Patch ¶
added in v0.110.0
func (r *PropertiesAccessBindingsService) Patch(name string, googleanalyticsadminv1alphaaccessbinding *GoogleAnalyticsAdminV1alphaAccessBinding) *PropertiesAccessBindingsPatchCall

Patch: Updates an access binding on an account or property.

name: Output only. Resource name of this binding. Format: accounts/{account}/accessBindings/{access_binding} or properties/{property}/accessBindings/{access_binding} Example: "accounts/100/accessBindings/200".
type PropertiesAcknowledgeUserDataCollectionCall ¶
added in v0.59.0
type PropertiesAcknowledgeUserDataCollectionCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesAcknowledgeUserDataCollectionCall) Context ¶
added in v0.59.0
func (c *PropertiesAcknowledgeUserDataCollectionCall) Context(ctx context.Context) *PropertiesAcknowledgeUserDataCollectionCall

Context sets the context to be used in this call's Do method.

func (*PropertiesAcknowledgeUserDataCollectionCall) Do ¶
added in v0.59.0
func (c *PropertiesAcknowledgeUserDataCollectionCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAcknowledgeUserDataCollectionResponse, error)

Do executes the "analyticsadmin.properties.acknowledgeUserDataCollection" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaAcknowledgeUserDataCollectionResponse.ServerRespo nse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesAcknowledgeUserDataCollectionCall) Fields ¶
added in v0.59.0
func (c *PropertiesAcknowledgeUserDataCollectionCall) Fields(s ...googleapi.Field) *PropertiesAcknowledgeUserDataCollectionCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesAcknowledgeUserDataCollectionCall) Header ¶
added in v0.59.0
func (c *PropertiesAcknowledgeUserDataCollectionCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesAdSenseLinksCreateCall ¶
added in v0.123.0
type PropertiesAdSenseLinksCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesAdSenseLinksCreateCall) Context ¶
added in v0.123.0
func (c *PropertiesAdSenseLinksCreateCall) Context(ctx context.Context) *PropertiesAdSenseLinksCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesAdSenseLinksCreateCall) Do ¶
added in v0.123.0
func (c *PropertiesAdSenseLinksCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAdSenseLink, error)

Do executes the "analyticsadmin.properties.adSenseLinks.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaAdSenseLink.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesAdSenseLinksCreateCall) Fields ¶
added in v0.123.0
func (c *PropertiesAdSenseLinksCreateCall) Fields(s ...googleapi.Field) *PropertiesAdSenseLinksCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesAdSenseLinksCreateCall) Header ¶
added in v0.123.0
func (c *PropertiesAdSenseLinksCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesAdSenseLinksDeleteCall ¶
added in v0.123.0
type PropertiesAdSenseLinksDeleteCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesAdSenseLinksDeleteCall) Context ¶
added in v0.123.0
func (c *PropertiesAdSenseLinksDeleteCall) Context(ctx context.Context) *PropertiesAdSenseLinksDeleteCall

Context sets the context to be used in this call's Do method.

func (*PropertiesAdSenseLinksDeleteCall) Do ¶
added in v0.123.0
func (c *PropertiesAdSenseLinksDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.properties.adSenseLinks.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesAdSenseLinksDeleteCall) Fields ¶
added in v0.123.0
func (c *PropertiesAdSenseLinksDeleteCall) Fields(s ...googleapi.Field) *PropertiesAdSenseLinksDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesAdSenseLinksDeleteCall) Header ¶
added in v0.123.0
func (c *PropertiesAdSenseLinksDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesAdSenseLinksGetCall ¶
added in v0.123.0
type PropertiesAdSenseLinksGetCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesAdSenseLinksGetCall) Context ¶
added in v0.123.0
func (c *PropertiesAdSenseLinksGetCall) Context(ctx context.Context) *PropertiesAdSenseLinksGetCall

Context sets the context to be used in this call's Do method.

func (*PropertiesAdSenseLinksGetCall) Do ¶
added in v0.123.0
func (c *PropertiesAdSenseLinksGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAdSenseLink, error)

Do executes the "analyticsadmin.properties.adSenseLinks.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaAdSenseLink.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesAdSenseLinksGetCall) Fields ¶
added in v0.123.0
func (c *PropertiesAdSenseLinksGetCall) Fields(s ...googleapi.Field) *PropertiesAdSenseLinksGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesAdSenseLinksGetCall) Header ¶
added in v0.123.0
func (c *PropertiesAdSenseLinksGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesAdSenseLinksGetCall) IfNoneMatch ¶
added in v0.123.0
func (c *PropertiesAdSenseLinksGetCall) IfNoneMatch(entityTag string) *PropertiesAdSenseLinksGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesAdSenseLinksListCall ¶
added in v0.123.0
type PropertiesAdSenseLinksListCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesAdSenseLinksListCall) Context ¶
added in v0.123.0
func (c *PropertiesAdSenseLinksListCall) Context(ctx context.Context) *PropertiesAdSenseLinksListCall

Context sets the context to be used in this call's Do method.

func (*PropertiesAdSenseLinksListCall) Do ¶
added in v0.123.0
func (c *PropertiesAdSenseLinksListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListAdSenseLinksResponse, error)

Do executes the "analyticsadmin.properties.adSenseLinks.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaListAdSenseLinksResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesAdSenseLinksListCall) Fields ¶
added in v0.123.0
func (c *PropertiesAdSenseLinksListCall) Fields(s ...googleapi.Field) *PropertiesAdSenseLinksListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesAdSenseLinksListCall) Header ¶
added in v0.123.0
func (c *PropertiesAdSenseLinksListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesAdSenseLinksListCall) IfNoneMatch ¶
added in v0.123.0
func (c *PropertiesAdSenseLinksListCall) IfNoneMatch(entityTag string) *PropertiesAdSenseLinksListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesAdSenseLinksListCall) PageSize ¶
added in v0.123.0
func (c *PropertiesAdSenseLinksListCall) PageSize(pageSize int64) *PropertiesAdSenseLinksListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. If unspecified, at most 50 resources will be returned. The maximum value is 200 (higher values will be coerced to the maximum).

func (*PropertiesAdSenseLinksListCall) PageToken ¶
added in v0.123.0
func (c *PropertiesAdSenseLinksListCall) PageToken(pageToken string) *PropertiesAdSenseLinksListCall

PageToken sets the optional parameter "pageToken": A page token received from a previous `ListAdSenseLinks` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListAdSenseLinks` must match the call that provided the page token.

func (*PropertiesAdSenseLinksListCall) Pages ¶
added in v0.123.0
func (c *PropertiesAdSenseLinksListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1alphaListAdSenseLinksResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesAdSenseLinksService ¶
added in v0.123.0
type PropertiesAdSenseLinksService struct {
	// contains filtered or unexported fields
}
func NewPropertiesAdSenseLinksService ¶
added in v0.123.0
func NewPropertiesAdSenseLinksService(s *Service) *PropertiesAdSenseLinksService
func (*PropertiesAdSenseLinksService) Create ¶
added in v0.123.0
func (r *PropertiesAdSenseLinksService) Create(parent string, googleanalyticsadminv1alphaadsenselink *GoogleAnalyticsAdminV1alphaAdSenseLink) *PropertiesAdSenseLinksCreateCall

Create: Creates an AdSenseLink.

parent: The property for which to create an AdSense Link. Format: properties/{propertyId} Example: properties/1234.
func (*PropertiesAdSenseLinksService) Delete ¶
added in v0.123.0
func (r *PropertiesAdSenseLinksService) Delete(nameid string) *PropertiesAdSenseLinksDeleteCall

Delete: Deletes an AdSenseLink.

name: Unique identifier for the AdSense Link to be deleted. Format: properties/{propertyId}/adSenseLinks/{linkId} Example: properties/1234/adSenseLinks/5678.
func (*PropertiesAdSenseLinksService) Get ¶
added in v0.123.0
func (r *PropertiesAdSenseLinksService) Get(nameid string) *PropertiesAdSenseLinksGetCall

Get: Looks up a single AdSenseLink.

name: Unique identifier for the AdSense Link requested. Format: properties/{propertyId}/adSenseLinks/{linkId} Example: properties/1234/adSenseLinks/5678.
func (*PropertiesAdSenseLinksService) List ¶
added in v0.123.0
func (r *PropertiesAdSenseLinksService) List(parent string) *PropertiesAdSenseLinksListCall

List: Lists AdSenseLinks on a property.

parent: Resource name of the parent property. Format: properties/{propertyId} Example: properties/1234.
type PropertiesAudiencesArchiveCall ¶
added in v0.90.0
type PropertiesAudiencesArchiveCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesAudiencesArchiveCall) Context ¶
added in v0.90.0
func (c *PropertiesAudiencesArchiveCall) Context(ctx context.Context) *PropertiesAudiencesArchiveCall

Context sets the context to be used in this call's Do method.

func (*PropertiesAudiencesArchiveCall) Do ¶
added in v0.90.0
func (c *PropertiesAudiencesArchiveCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.properties.audiences.archive" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesAudiencesArchiveCall) Fields ¶
added in v0.90.0
func (c *PropertiesAudiencesArchiveCall) Fields(s ...googleapi.Field) *PropertiesAudiencesArchiveCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesAudiencesArchiveCall) Header ¶
added in v0.90.0
func (c *PropertiesAudiencesArchiveCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesAudiencesCreateCall ¶
added in v0.90.0
type PropertiesAudiencesCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesAudiencesCreateCall) Context ¶
added in v0.90.0
func (c *PropertiesAudiencesCreateCall) Context(ctx context.Context) *PropertiesAudiencesCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesAudiencesCreateCall) Do ¶
added in v0.90.0
func (c *PropertiesAudiencesCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAudience, error)

Do executes the "analyticsadmin.properties.audiences.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaAudience.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesAudiencesCreateCall) Fields ¶
added in v0.90.0
func (c *PropertiesAudiencesCreateCall) Fields(s ...googleapi.Field) *PropertiesAudiencesCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesAudiencesCreateCall) Header ¶
added in v0.90.0
func (c *PropertiesAudiencesCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesAudiencesGetCall ¶
added in v0.90.0
type PropertiesAudiencesGetCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesAudiencesGetCall) Context ¶
added in v0.90.0
func (c *PropertiesAudiencesGetCall) Context(ctx context.Context) *PropertiesAudiencesGetCall

Context sets the context to be used in this call's Do method.

func (*PropertiesAudiencesGetCall) Do ¶
added in v0.90.0
func (c *PropertiesAudiencesGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAudience, error)

Do executes the "analyticsadmin.properties.audiences.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaAudience.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesAudiencesGetCall) Fields ¶
added in v0.90.0
func (c *PropertiesAudiencesGetCall) Fields(s ...googleapi.Field) *PropertiesAudiencesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesAudiencesGetCall) Header ¶
added in v0.90.0
func (c *PropertiesAudiencesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesAudiencesGetCall) IfNoneMatch ¶
added in v0.90.0
func (c *PropertiesAudiencesGetCall) IfNoneMatch(entityTag string) *PropertiesAudiencesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesAudiencesListCall ¶
added in v0.90.0
type PropertiesAudiencesListCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesAudiencesListCall) Context ¶
added in v0.90.0
func (c *PropertiesAudiencesListCall) Context(ctx context.Context) *PropertiesAudiencesListCall

Context sets the context to be used in this call's Do method.

func (*PropertiesAudiencesListCall) Do ¶
added in v0.90.0
func (c *PropertiesAudiencesListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListAudiencesResponse, error)

Do executes the "analyticsadmin.properties.audiences.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaListAudiencesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesAudiencesListCall) Fields ¶
added in v0.90.0
func (c *PropertiesAudiencesListCall) Fields(s ...googleapi.Field) *PropertiesAudiencesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesAudiencesListCall) Header ¶
added in v0.90.0
func (c *PropertiesAudiencesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesAudiencesListCall) IfNoneMatch ¶
added in v0.90.0
func (c *PropertiesAudiencesListCall) IfNoneMatch(entityTag string) *PropertiesAudiencesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesAudiencesListCall) PageSize ¶
added in v0.90.0
func (c *PropertiesAudiencesListCall) PageSize(pageSize int64) *PropertiesAudiencesListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. If unspecified, at most 50 resources will be returned. The maximum value is 200 (higher values will be coerced to the maximum).

func (*PropertiesAudiencesListCall) PageToken ¶
added in v0.90.0
func (c *PropertiesAudiencesListCall) PageToken(pageToken string) *PropertiesAudiencesListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListAudiences` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListAudiences` must match the call that provided the page token.

func (*PropertiesAudiencesListCall) Pages ¶
added in v0.90.0
func (c *PropertiesAudiencesListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1alphaListAudiencesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesAudiencesPatchCall ¶
added in v0.90.0
type PropertiesAudiencesPatchCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesAudiencesPatchCall) Context ¶
added in v0.90.0
func (c *PropertiesAudiencesPatchCall) Context(ctx context.Context) *PropertiesAudiencesPatchCall

Context sets the context to be used in this call's Do method.

func (*PropertiesAudiencesPatchCall) Do ¶
added in v0.90.0
func (c *PropertiesAudiencesPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAudience, error)

Do executes the "analyticsadmin.properties.audiences.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaAudience.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesAudiencesPatchCall) Fields ¶
added in v0.90.0
func (c *PropertiesAudiencesPatchCall) Fields(s ...googleapi.Field) *PropertiesAudiencesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesAudiencesPatchCall) Header ¶
added in v0.90.0
func (c *PropertiesAudiencesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesAudiencesPatchCall) UpdateMask ¶
added in v0.90.0
func (c *PropertiesAudiencesPatchCall) UpdateMask(updateMask string) *PropertiesAudiencesPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated. Field names must be in snake case (e.g., "field_to_update"). Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.

type PropertiesAudiencesService ¶
added in v0.90.0
type PropertiesAudiencesService struct {
	// contains filtered or unexported fields
}
func NewPropertiesAudiencesService ¶
added in v0.90.0
func NewPropertiesAudiencesService(s *Service) *PropertiesAudiencesService
func (*PropertiesAudiencesService) Archive ¶
added in v0.90.0
func (r *PropertiesAudiencesService) Archive(name string, googleanalyticsadminv1alphaarchiveaudiencerequest *GoogleAnalyticsAdminV1alphaArchiveAudienceRequest) *PropertiesAudiencesArchiveCall

Archive: Archives an Audience on a property.

- name: Example format: properties/1234/audiences/5678.

func (*PropertiesAudiencesService) Create ¶
added in v0.90.0
func (r *PropertiesAudiencesService) Create(parent string, googleanalyticsadminv1alphaaudience *GoogleAnalyticsAdminV1alphaAudience) *PropertiesAudiencesCreateCall

Create: Creates an Audience.

- parent: Example format: properties/1234.

func (*PropertiesAudiencesService) Get ¶
added in v0.90.0
func (r *PropertiesAudiencesService) Get(name string) *PropertiesAudiencesGetCall

Get: Lookup for a single Audience. Audiences created before 2020 may not be supported. Default audiences will not show filter definitions.

name: The name of the Audience to get. Example format: properties/1234/audiences/5678.
func (*PropertiesAudiencesService) List ¶
added in v0.90.0
func (r *PropertiesAudiencesService) List(parent string) *PropertiesAudiencesListCall

List: Lists Audiences on a property. Audiences created before 2020 may not be supported. Default audiences will not show filter definitions.

- parent: Example format: properties/1234.

func (*PropertiesAudiencesService) Patch ¶
added in v0.90.0
func (r *PropertiesAudiencesService) Patch(name string, googleanalyticsadminv1alphaaudience *GoogleAnalyticsAdminV1alphaAudience) *PropertiesAudiencesPatchCall

Patch: Updates an Audience on a property.

name: Output only. The resource name for this Audience resource. Format: properties/{propertyId}/audiences/{audienceId}.
type PropertiesBigQueryLinksCreateCall ¶
added in v0.188.0
type PropertiesBigQueryLinksCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesBigQueryLinksCreateCall) Context ¶
added in v0.188.0
func (c *PropertiesBigQueryLinksCreateCall) Context(ctx context.Context) *PropertiesBigQueryLinksCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesBigQueryLinksCreateCall) Do ¶
added in v0.188.0
func (c *PropertiesBigQueryLinksCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaBigQueryLink, error)

Do executes the "analyticsadmin.properties.bigQueryLinks.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaBigQueryLink.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesBigQueryLinksCreateCall) Fields ¶
added in v0.188.0
func (c *PropertiesBigQueryLinksCreateCall) Fields(s ...googleapi.Field) *PropertiesBigQueryLinksCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesBigQueryLinksCreateCall) Header ¶
added in v0.188.0
func (c *PropertiesBigQueryLinksCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesBigQueryLinksDeleteCall ¶
added in v0.188.0
type PropertiesBigQueryLinksDeleteCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesBigQueryLinksDeleteCall) Context ¶
added in v0.188.0
func (c *PropertiesBigQueryLinksDeleteCall) Context(ctx context.Context) *PropertiesBigQueryLinksDeleteCall

Context sets the context to be used in this call's Do method.

func (*PropertiesBigQueryLinksDeleteCall) Do ¶
added in v0.188.0
func (c *PropertiesBigQueryLinksDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.properties.bigQueryLinks.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesBigQueryLinksDeleteCall) Fields ¶
added in v0.188.0
func (c *PropertiesBigQueryLinksDeleteCall) Fields(s ...googleapi.Field) *PropertiesBigQueryLinksDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesBigQueryLinksDeleteCall) Header ¶
added in v0.188.0
func (c *PropertiesBigQueryLinksDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesBigQueryLinksGetCall ¶
added in v0.104.0
type PropertiesBigQueryLinksGetCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesBigQueryLinksGetCall) Context ¶
added in v0.104.0
func (c *PropertiesBigQueryLinksGetCall) Context(ctx context.Context) *PropertiesBigQueryLinksGetCall

Context sets the context to be used in this call's Do method.

func (*PropertiesBigQueryLinksGetCall) Do ¶
added in v0.104.0
func (c *PropertiesBigQueryLinksGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaBigQueryLink, error)

Do executes the "analyticsadmin.properties.bigQueryLinks.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaBigQueryLink.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesBigQueryLinksGetCall) Fields ¶
added in v0.104.0
func (c *PropertiesBigQueryLinksGetCall) Fields(s ...googleapi.Field) *PropertiesBigQueryLinksGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesBigQueryLinksGetCall) Header ¶
added in v0.104.0
func (c *PropertiesBigQueryLinksGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesBigQueryLinksGetCall) IfNoneMatch ¶
added in v0.104.0
func (c *PropertiesBigQueryLinksGetCall) IfNoneMatch(entityTag string) *PropertiesBigQueryLinksGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesBigQueryLinksListCall ¶
added in v0.104.0
type PropertiesBigQueryLinksListCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesBigQueryLinksListCall) Context ¶
added in v0.104.0
func (c *PropertiesBigQueryLinksListCall) Context(ctx context.Context) *PropertiesBigQueryLinksListCall

Context sets the context to be used in this call's Do method.

func (*PropertiesBigQueryLinksListCall) Do ¶
added in v0.104.0
func (c *PropertiesBigQueryLinksListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListBigQueryLinksResponse, error)

Do executes the "analyticsadmin.properties.bigQueryLinks.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaListBigQueryLinksResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesBigQueryLinksListCall) Fields ¶
added in v0.104.0
func (c *PropertiesBigQueryLinksListCall) Fields(s ...googleapi.Field) *PropertiesBigQueryLinksListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesBigQueryLinksListCall) Header ¶
added in v0.104.0
func (c *PropertiesBigQueryLinksListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesBigQueryLinksListCall) IfNoneMatch ¶
added in v0.104.0
func (c *PropertiesBigQueryLinksListCall) IfNoneMatch(entityTag string) *PropertiesBigQueryLinksListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesBigQueryLinksListCall) PageSize ¶
added in v0.104.0
func (c *PropertiesBigQueryLinksListCall) PageSize(pageSize int64) *PropertiesBigQueryLinksListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. The service may return fewer than this value, even if there are additional pages. If unspecified, at most 50 resources will be returned. The maximum value is 200; (higher values will be coerced to the maximum)

func (*PropertiesBigQueryLinksListCall) PageToken ¶
added in v0.104.0
func (c *PropertiesBigQueryLinksListCall) PageToken(pageToken string) *PropertiesBigQueryLinksListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListBigQueryLinks` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListBigQueryLinks` must match the call that provided the page token.

func (*PropertiesBigQueryLinksListCall) Pages ¶
added in v0.104.0
func (c *PropertiesBigQueryLinksListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1alphaListBigQueryLinksResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesBigQueryLinksPatchCall ¶
added in v0.188.0
type PropertiesBigQueryLinksPatchCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesBigQueryLinksPatchCall) Context ¶
added in v0.188.0
func (c *PropertiesBigQueryLinksPatchCall) Context(ctx context.Context) *PropertiesBigQueryLinksPatchCall

Context sets the context to be used in this call's Do method.

func (*PropertiesBigQueryLinksPatchCall) Do ¶
added in v0.188.0
func (c *PropertiesBigQueryLinksPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaBigQueryLink, error)

Do executes the "analyticsadmin.properties.bigQueryLinks.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaBigQueryLink.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesBigQueryLinksPatchCall) Fields ¶
added in v0.188.0
func (c *PropertiesBigQueryLinksPatchCall) Fields(s ...googleapi.Field) *PropertiesBigQueryLinksPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesBigQueryLinksPatchCall) Header ¶
added in v0.188.0
func (c *PropertiesBigQueryLinksPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesBigQueryLinksPatchCall) UpdateMask ¶
added in v0.188.0
func (c *PropertiesBigQueryLinksPatchCall) UpdateMask(updateMask string) *PropertiesBigQueryLinksPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated. Field names must be in snake case (e.g., "field_to_update"). Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.

type PropertiesBigQueryLinksService ¶
added in v0.104.0
type PropertiesBigQueryLinksService struct {
	// contains filtered or unexported fields
}
func NewPropertiesBigQueryLinksService ¶
added in v0.104.0
func NewPropertiesBigQueryLinksService(s *Service) *PropertiesBigQueryLinksService
func (*PropertiesBigQueryLinksService) Create ¶
added in v0.188.0
func (r *PropertiesBigQueryLinksService) Create(parent string, googleanalyticsadminv1alphabigquerylink *GoogleAnalyticsAdminV1alphaBigQueryLink) *PropertiesBigQueryLinksCreateCall

Create: Creates a BigQueryLink.

- parent: Example format: properties/1234.

func (*PropertiesBigQueryLinksService) Delete ¶
added in v0.188.0
func (r *PropertiesBigQueryLinksService) Delete(name string) *PropertiesBigQueryLinksDeleteCall

Delete: Deletes a BigQueryLink on a property.

name: The BigQueryLink to delete. Example format: properties/1234/bigQueryLinks/5678.
func (*PropertiesBigQueryLinksService) Get ¶
added in v0.104.0
func (r *PropertiesBigQueryLinksService) Get(name string) *PropertiesBigQueryLinksGetCall

Get: Lookup for a single BigQuery Link.

name: The name of the BigQuery link to lookup. Format: properties/{property_id}/bigQueryLinks/{bigquery_link_id} Example: properties/123/bigQueryLinks/456.
func (*PropertiesBigQueryLinksService) List ¶
added in v0.104.0
func (r *PropertiesBigQueryLinksService) List(parent string) *PropertiesBigQueryLinksListCall

List: Lists BigQuery Links on a property.

parent: The name of the property to list BigQuery links under. Format: properties/{property_id} Example: properties/1234.
func (*PropertiesBigQueryLinksService) Patch ¶
added in v0.188.0
func (r *PropertiesBigQueryLinksService) Patch(name string, googleanalyticsadminv1alphabigquerylink *GoogleAnalyticsAdminV1alphaBigQueryLink) *PropertiesBigQueryLinksPatchCall

Patch: Updates a BigQueryLink.

name: Output only. Resource name of this BigQuery link. Format: 'properties/{property_id}/bigQueryLinks/{bigquery_link_id}' Format: 'properties/1234/bigQueryLinks/abc567'.
type PropertiesCalculatedMetricsCreateCall ¶
added in v0.157.0
type PropertiesCalculatedMetricsCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesCalculatedMetricsCreateCall) CalculatedMetricId ¶
added in v0.157.0
func (c *PropertiesCalculatedMetricsCreateCall) CalculatedMetricId(calculatedMetricId string) *PropertiesCalculatedMetricsCreateCall

CalculatedMetricId sets the optional parameter "calculatedMetricId": Required. The ID to use for the calculated metric which will become the final component of the calculated metric's resource name. This value should be 1-80 characters and valid characters are /[a-zA-Z0-9_]/, no spaces allowed. calculated_metric_id must be unique between all calculated metrics under a property. The calculated_metric_id is used when referencing this calculated metric from external APIs, for example, "calcMetric:{calculated_metric_id}".

func (*PropertiesCalculatedMetricsCreateCall) Context ¶
added in v0.157.0
func (c *PropertiesCalculatedMetricsCreateCall) Context(ctx context.Context) *PropertiesCalculatedMetricsCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesCalculatedMetricsCreateCall) Do ¶
added in v0.157.0
func (c *PropertiesCalculatedMetricsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaCalculatedMetric, error)

Do executes the "analyticsadmin.properties.calculatedMetrics.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaCalculatedMetric.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesCalculatedMetricsCreateCall) Fields ¶
added in v0.157.0
func (c *PropertiesCalculatedMetricsCreateCall) Fields(s ...googleapi.Field) *PropertiesCalculatedMetricsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesCalculatedMetricsCreateCall) Header ¶
added in v0.157.0
func (c *PropertiesCalculatedMetricsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesCalculatedMetricsDeleteCall ¶
added in v0.157.0
type PropertiesCalculatedMetricsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesCalculatedMetricsDeleteCall) Context ¶
added in v0.157.0
func (c *PropertiesCalculatedMetricsDeleteCall) Context(ctx context.Context) *PropertiesCalculatedMetricsDeleteCall

Context sets the context to be used in this call's Do method.

func (*PropertiesCalculatedMetricsDeleteCall) Do ¶
added in v0.157.0
func (c *PropertiesCalculatedMetricsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.properties.calculatedMetrics.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesCalculatedMetricsDeleteCall) Fields ¶
added in v0.157.0
func (c *PropertiesCalculatedMetricsDeleteCall) Fields(s ...googleapi.Field) *PropertiesCalculatedMetricsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesCalculatedMetricsDeleteCall) Header ¶
added in v0.157.0
func (c *PropertiesCalculatedMetricsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesCalculatedMetricsGetCall ¶
added in v0.157.0
type PropertiesCalculatedMetricsGetCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesCalculatedMetricsGetCall) Context ¶
added in v0.157.0
func (c *PropertiesCalculatedMetricsGetCall) Context(ctx context.Context) *PropertiesCalculatedMetricsGetCall

Context sets the context to be used in this call's Do method.

func (*PropertiesCalculatedMetricsGetCall) Do ¶
added in v0.157.0
func (c *PropertiesCalculatedMetricsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaCalculatedMetric, error)

Do executes the "analyticsadmin.properties.calculatedMetrics.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaCalculatedMetric.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesCalculatedMetricsGetCall) Fields ¶
added in v0.157.0
func (c *PropertiesCalculatedMetricsGetCall) Fields(s ...googleapi.Field) *PropertiesCalculatedMetricsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesCalculatedMetricsGetCall) Header ¶
added in v0.157.0
func (c *PropertiesCalculatedMetricsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesCalculatedMetricsGetCall) IfNoneMatch ¶
added in v0.157.0
func (c *PropertiesCalculatedMetricsGetCall) IfNoneMatch(entityTag string) *PropertiesCalculatedMetricsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesCalculatedMetricsListCall ¶
added in v0.157.0
type PropertiesCalculatedMetricsListCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesCalculatedMetricsListCall) Context ¶
added in v0.157.0
func (c *PropertiesCalculatedMetricsListCall) Context(ctx context.Context) *PropertiesCalculatedMetricsListCall

Context sets the context to be used in this call's Do method.

func (*PropertiesCalculatedMetricsListCall) Do ¶
added in v0.157.0
func (c *PropertiesCalculatedMetricsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListCalculatedMetricsResponse, error)

Do executes the "analyticsadmin.properties.calculatedMetrics.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaListCalculatedMetricsResponse.ServerResponse.Head er or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesCalculatedMetricsListCall) Fields ¶
added in v0.157.0
func (c *PropertiesCalculatedMetricsListCall) Fields(s ...googleapi.Field) *PropertiesCalculatedMetricsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesCalculatedMetricsListCall) Header ¶
added in v0.157.0
func (c *PropertiesCalculatedMetricsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesCalculatedMetricsListCall) IfNoneMatch ¶
added in v0.157.0
func (c *PropertiesCalculatedMetricsListCall) IfNoneMatch(entityTag string) *PropertiesCalculatedMetricsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesCalculatedMetricsListCall) PageSize ¶
added in v0.157.0
func (c *PropertiesCalculatedMetricsListCall) PageSize(pageSize int64) *PropertiesCalculatedMetricsListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. If unspecified, at most 50 resources will be returned. The maximum value is 200 (higher values will be coerced to the maximum).

func (*PropertiesCalculatedMetricsListCall) PageToken ¶
added in v0.157.0
func (c *PropertiesCalculatedMetricsListCall) PageToken(pageToken string) *PropertiesCalculatedMetricsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListCalculatedMetrics` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListCalculatedMetrics` must match the call that provided the page token.

func (*PropertiesCalculatedMetricsListCall) Pages ¶
added in v0.157.0
func (c *PropertiesCalculatedMetricsListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1alphaListCalculatedMetricsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesCalculatedMetricsPatchCall ¶
added in v0.157.0
type PropertiesCalculatedMetricsPatchCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesCalculatedMetricsPatchCall) Context ¶
added in v0.157.0
func (c *PropertiesCalculatedMetricsPatchCall) Context(ctx context.Context) *PropertiesCalculatedMetricsPatchCall

Context sets the context to be used in this call's Do method.

func (*PropertiesCalculatedMetricsPatchCall) Do ¶
added in v0.157.0
func (c *PropertiesCalculatedMetricsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaCalculatedMetric, error)

Do executes the "analyticsadmin.properties.calculatedMetrics.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaCalculatedMetric.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesCalculatedMetricsPatchCall) Fields ¶
added in v0.157.0
func (c *PropertiesCalculatedMetricsPatchCall) Fields(s ...googleapi.Field) *PropertiesCalculatedMetricsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesCalculatedMetricsPatchCall) Header ¶
added in v0.157.0
func (c *PropertiesCalculatedMetricsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesCalculatedMetricsPatchCall) UpdateMask ¶
added in v0.157.0
func (c *PropertiesCalculatedMetricsPatchCall) UpdateMask(updateMask string) *PropertiesCalculatedMetricsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated. Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.

type PropertiesCalculatedMetricsService ¶
added in v0.157.0
type PropertiesCalculatedMetricsService struct {
	// contains filtered or unexported fields
}
func NewPropertiesCalculatedMetricsService ¶
added in v0.157.0
func NewPropertiesCalculatedMetricsService(s *Service) *PropertiesCalculatedMetricsService
func (*PropertiesCalculatedMetricsService) Create ¶
added in v0.157.0
func (r *PropertiesCalculatedMetricsService) Create(parent string, googleanalyticsadminv1alphacalculatedmetric *GoogleAnalyticsAdminV1alphaCalculatedMetric) *PropertiesCalculatedMetricsCreateCall

Create: Creates a CalculatedMetric.

- parent: Format: properties/{property_id} Example: properties/1234.

func (*PropertiesCalculatedMetricsService) Delete ¶
added in v0.157.0
func (r *PropertiesCalculatedMetricsService) Delete(name string) *PropertiesCalculatedMetricsDeleteCall

Delete: Deletes a CalculatedMetric on a property.

name: The name of the CalculatedMetric to delete. Format: properties/{property_id}/calculatedMetrics/{calculated_metric_id} Example: properties/1234/calculatedMetrics/Metric01.
func (*PropertiesCalculatedMetricsService) Get ¶
added in v0.157.0
func (r *PropertiesCalculatedMetricsService) Get(name string) *PropertiesCalculatedMetricsGetCall

Get: Lookup for a single CalculatedMetric.

name: The name of the CalculatedMetric to get. Format: properties/{property_id}/calculatedMetrics/{calculated_metric_id} Example: properties/1234/calculatedMetrics/Metric01.
func (*PropertiesCalculatedMetricsService) List ¶
added in v0.157.0
func (r *PropertiesCalculatedMetricsService) List(parent string) *PropertiesCalculatedMetricsListCall

List: Lists CalculatedMetrics on a property.

- parent: Example format: properties/1234.

func (*PropertiesCalculatedMetricsService) Patch ¶
added in v0.157.0
func (r *PropertiesCalculatedMetricsService) Patch(name string, googleanalyticsadminv1alphacalculatedmetric *GoogleAnalyticsAdminV1alphaCalculatedMetric) *PropertiesCalculatedMetricsPatchCall

Patch: Updates a CalculatedMetric on a property.

name: Output only. Resource name for this CalculatedMetric. Format: 'properties/{property_id}/calculatedMetrics/{calculated_metric_id}'.
type PropertiesChannelGroupsCreateCall ¶
added in v0.117.0
type PropertiesChannelGroupsCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesChannelGroupsCreateCall) Context ¶
added in v0.117.0
func (c *PropertiesChannelGroupsCreateCall) Context(ctx context.Context) *PropertiesChannelGroupsCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesChannelGroupsCreateCall) Do ¶
added in v0.117.0
func (c *PropertiesChannelGroupsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaChannelGroup, error)

Do executes the "analyticsadmin.properties.channelGroups.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaChannelGroup.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesChannelGroupsCreateCall) Fields ¶
added in v0.117.0
func (c *PropertiesChannelGroupsCreateCall) Fields(s ...googleapi.Field) *PropertiesChannelGroupsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesChannelGroupsCreateCall) Header ¶
added in v0.117.0
func (c *PropertiesChannelGroupsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesChannelGroupsDeleteCall ¶
added in v0.117.0
type PropertiesChannelGroupsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesChannelGroupsDeleteCall) Context ¶
added in v0.117.0
func (c *PropertiesChannelGroupsDeleteCall) Context(ctx context.Context) *PropertiesChannelGroupsDeleteCall

Context sets the context to be used in this call's Do method.

func (*PropertiesChannelGroupsDeleteCall) Do ¶
added in v0.117.0
func (c *PropertiesChannelGroupsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.properties.channelGroups.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesChannelGroupsDeleteCall) Fields ¶
added in v0.117.0
func (c *PropertiesChannelGroupsDeleteCall) Fields(s ...googleapi.Field) *PropertiesChannelGroupsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesChannelGroupsDeleteCall) Header ¶
added in v0.117.0
func (c *PropertiesChannelGroupsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesChannelGroupsGetCall ¶
added in v0.117.0
type PropertiesChannelGroupsGetCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesChannelGroupsGetCall) Context ¶
added in v0.117.0
func (c *PropertiesChannelGroupsGetCall) Context(ctx context.Context) *PropertiesChannelGroupsGetCall

Context sets the context to be used in this call's Do method.

func (*PropertiesChannelGroupsGetCall) Do ¶
added in v0.117.0
func (c *PropertiesChannelGroupsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaChannelGroup, error)

Do executes the "analyticsadmin.properties.channelGroups.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaChannelGroup.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesChannelGroupsGetCall) Fields ¶
added in v0.117.0
func (c *PropertiesChannelGroupsGetCall) Fields(s ...googleapi.Field) *PropertiesChannelGroupsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesChannelGroupsGetCall) Header ¶
added in v0.117.0
func (c *PropertiesChannelGroupsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesChannelGroupsGetCall) IfNoneMatch ¶
added in v0.117.0
func (c *PropertiesChannelGroupsGetCall) IfNoneMatch(entityTag string) *PropertiesChannelGroupsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesChannelGroupsListCall ¶
added in v0.117.0
type PropertiesChannelGroupsListCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesChannelGroupsListCall) Context ¶
added in v0.117.0
func (c *PropertiesChannelGroupsListCall) Context(ctx context.Context) *PropertiesChannelGroupsListCall

Context sets the context to be used in this call's Do method.

func (*PropertiesChannelGroupsListCall) Do ¶
added in v0.117.0
func (c *PropertiesChannelGroupsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListChannelGroupsResponse, error)

Do executes the "analyticsadmin.properties.channelGroups.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaListChannelGroupsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesChannelGroupsListCall) Fields ¶
added in v0.117.0
func (c *PropertiesChannelGroupsListCall) Fields(s ...googleapi.Field) *PropertiesChannelGroupsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesChannelGroupsListCall) Header ¶
added in v0.117.0
func (c *PropertiesChannelGroupsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesChannelGroupsListCall) IfNoneMatch ¶
added in v0.117.0
func (c *PropertiesChannelGroupsListCall) IfNoneMatch(entityTag string) *PropertiesChannelGroupsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesChannelGroupsListCall) PageSize ¶
added in v0.117.0
func (c *PropertiesChannelGroupsListCall) PageSize(pageSize int64) *PropertiesChannelGroupsListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. If unspecified, at most 50 resources will be returned. The maximum value is 200 (higher values will be coerced to the maximum).

func (*PropertiesChannelGroupsListCall) PageToken ¶
added in v0.117.0
func (c *PropertiesChannelGroupsListCall) PageToken(pageToken string) *PropertiesChannelGroupsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListChannelGroups` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListChannelGroups` must match the call that provided the page token.

func (*PropertiesChannelGroupsListCall) Pages ¶
added in v0.117.0
func (c *PropertiesChannelGroupsListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1alphaListChannelGroupsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesChannelGroupsPatchCall ¶
added in v0.117.0
type PropertiesChannelGroupsPatchCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesChannelGroupsPatchCall) Context ¶
added in v0.117.0
func (c *PropertiesChannelGroupsPatchCall) Context(ctx context.Context) *PropertiesChannelGroupsPatchCall

Context sets the context to be used in this call's Do method.

func (*PropertiesChannelGroupsPatchCall) Do ¶
added in v0.117.0
func (c *PropertiesChannelGroupsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaChannelGroup, error)

Do executes the "analyticsadmin.properties.channelGroups.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaChannelGroup.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesChannelGroupsPatchCall) Fields ¶
added in v0.117.0
func (c *PropertiesChannelGroupsPatchCall) Fields(s ...googleapi.Field) *PropertiesChannelGroupsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesChannelGroupsPatchCall) Header ¶
added in v0.117.0
func (c *PropertiesChannelGroupsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesChannelGroupsPatchCall) UpdateMask ¶
added in v0.117.0
func (c *PropertiesChannelGroupsPatchCall) UpdateMask(updateMask string) *PropertiesChannelGroupsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated. Field names must be in snake case (e.g., "field_to_update"). Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.

type PropertiesChannelGroupsService ¶
added in v0.117.0
type PropertiesChannelGroupsService struct {
	// contains filtered or unexported fields
}
func NewPropertiesChannelGroupsService ¶
added in v0.117.0
func NewPropertiesChannelGroupsService(s *Service) *PropertiesChannelGroupsService
func (*PropertiesChannelGroupsService) Create ¶
added in v0.117.0
func (r *PropertiesChannelGroupsService) Create(parent string, googleanalyticsadminv1alphachannelgroup *GoogleAnalyticsAdminV1alphaChannelGroup) *PropertiesChannelGroupsCreateCall

Create: Creates a ChannelGroup.

parent: The property for which to create a ChannelGroup. Example format: properties/1234.
func (*PropertiesChannelGroupsService) Delete ¶
added in v0.117.0
func (r *PropertiesChannelGroupsService) Delete(name string) *PropertiesChannelGroupsDeleteCall

Delete: Deletes a ChannelGroup on a property.

name: The ChannelGroup to delete. Example format: properties/1234/channelGroups/5678.
func (*PropertiesChannelGroupsService) Get ¶
added in v0.117.0
func (r *PropertiesChannelGroupsService) Get(name string) *PropertiesChannelGroupsGetCall

Get: Lookup for a single ChannelGroup.

name: The ChannelGroup to get. Example format: properties/1234/channelGroups/5678.
func (*PropertiesChannelGroupsService) List ¶
added in v0.117.0
func (r *PropertiesChannelGroupsService) List(parent string) *PropertiesChannelGroupsListCall

List: Lists ChannelGroups on a property.

parent: The property for which to list ChannelGroups. Example format: properties/1234.
func (*PropertiesChannelGroupsService) Patch ¶
added in v0.117.0
func (r *PropertiesChannelGroupsService) Patch(name string, googleanalyticsadminv1alphachannelgroup *GoogleAnalyticsAdminV1alphaChannelGroup) *PropertiesChannelGroupsPatchCall

Patch: Updates a ChannelGroup.

name: Output only. The resource name for this Channel Group resource. Format: properties/{property}/channelGroups/{channel_group}.
type PropertiesConversionEventsCreateCall ¶
added in v0.47.0
type PropertiesConversionEventsCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesConversionEventsCreateCall) Context ¶
added in v0.47.0
func (c *PropertiesConversionEventsCreateCall) Context(ctx context.Context) *PropertiesConversionEventsCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesConversionEventsCreateCall) Do ¶
added in v0.47.0
func (c *PropertiesConversionEventsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaConversionEvent, error)

Do executes the "analyticsadmin.properties.conversionEvents.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaConversionEvent.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesConversionEventsCreateCall) Fields ¶
added in v0.47.0
func (c *PropertiesConversionEventsCreateCall) Fields(s ...googleapi.Field) *PropertiesConversionEventsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesConversionEventsCreateCall) Header ¶
added in v0.47.0
func (c *PropertiesConversionEventsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesConversionEventsDeleteCall ¶
added in v0.47.0
type PropertiesConversionEventsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesConversionEventsDeleteCall) Context ¶
added in v0.47.0
func (c *PropertiesConversionEventsDeleteCall) Context(ctx context.Context) *PropertiesConversionEventsDeleteCall

Context sets the context to be used in this call's Do method.

func (*PropertiesConversionEventsDeleteCall) Do ¶
added in v0.47.0
func (c *PropertiesConversionEventsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.properties.conversionEvents.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesConversionEventsDeleteCall) Fields ¶
added in v0.47.0
func (c *PropertiesConversionEventsDeleteCall) Fields(s ...googleapi.Field) *PropertiesConversionEventsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesConversionEventsDeleteCall) Header ¶
added in v0.47.0
func (c *PropertiesConversionEventsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesConversionEventsGetCall ¶
added in v0.47.0
type PropertiesConversionEventsGetCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesConversionEventsGetCall) Context ¶
added in v0.47.0
func (c *PropertiesConversionEventsGetCall) Context(ctx context.Context) *PropertiesConversionEventsGetCall

Context sets the context to be used in this call's Do method.

func (*PropertiesConversionEventsGetCall) Do ¶
added in v0.47.0
func (c *PropertiesConversionEventsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaConversionEvent, error)

Do executes the "analyticsadmin.properties.conversionEvents.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaConversionEvent.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesConversionEventsGetCall) Fields ¶
added in v0.47.0
func (c *PropertiesConversionEventsGetCall) Fields(s ...googleapi.Field) *PropertiesConversionEventsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesConversionEventsGetCall) Header ¶
added in v0.47.0
func (c *PropertiesConversionEventsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesConversionEventsGetCall) IfNoneMatch ¶
added in v0.47.0
func (c *PropertiesConversionEventsGetCall) IfNoneMatch(entityTag string) *PropertiesConversionEventsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesConversionEventsListCall ¶
added in v0.47.0
type PropertiesConversionEventsListCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesConversionEventsListCall) Context ¶
added in v0.47.0
func (c *PropertiesConversionEventsListCall) Context(ctx context.Context) *PropertiesConversionEventsListCall

Context sets the context to be used in this call's Do method.

func (*PropertiesConversionEventsListCall) Do ¶
added in v0.47.0
func (c *PropertiesConversionEventsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListConversionEventsResponse, error)

Do executes the "analyticsadmin.properties.conversionEvents.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaListConversionEventsResponse.ServerResponse.Heade r or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesConversionEventsListCall) Fields ¶
added in v0.47.0
func (c *PropertiesConversionEventsListCall) Fields(s ...googleapi.Field) *PropertiesConversionEventsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesConversionEventsListCall) Header ¶
added in v0.47.0
func (c *PropertiesConversionEventsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesConversionEventsListCall) IfNoneMatch ¶
added in v0.47.0
func (c *PropertiesConversionEventsListCall) IfNoneMatch(entityTag string) *PropertiesConversionEventsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesConversionEventsListCall) PageSize ¶
added in v0.47.0
func (c *PropertiesConversionEventsListCall) PageSize(pageSize int64) *PropertiesConversionEventsListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. If unspecified, at most 50 resources will be returned. The maximum value is 200; (higher values will be coerced to the maximum)

func (*PropertiesConversionEventsListCall) PageToken ¶
added in v0.47.0
func (c *PropertiesConversionEventsListCall) PageToken(pageToken string) *PropertiesConversionEventsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListConversionEvents` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListConversionEvents` must match the call that provided the page token.

func (*PropertiesConversionEventsListCall) Pages ¶
added in v0.47.0
func (c *PropertiesConversionEventsListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1alphaListConversionEventsResponse) error) error

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
func (c *PropertiesConversionEventsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaConversionEvent, error)

Do executes the "analyticsadmin.properties.conversionEvents.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaConversionEvent.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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
added in v0.47.0
type PropertiesConversionEventsService struct {
	// contains filtered or unexported fields
}
func NewPropertiesConversionEventsService ¶
added in v0.47.0
func NewPropertiesConversionEventsService(s *Service) *PropertiesConversionEventsService
func (*PropertiesConversionEventsService) Create ¶
added in v0.47.0
func (r *PropertiesConversionEventsService) Create(parent string, googleanalyticsadminv1alphaconversionevent *GoogleAnalyticsAdminV1alphaConversionEvent) *PropertiesConversionEventsCreateCall

Create: Deprecated: Use `CreateKeyEvent` instead. Creates a conversion event with the specified attributes.

parent: The resource name of the parent property where this conversion event will be created. Format: properties/123.
func (*PropertiesConversionEventsService) Delete ¶
added in v0.47.0
func (r *PropertiesConversionEventsService) Delete(name string) *PropertiesConversionEventsDeleteCall

Delete: Deprecated: Use `DeleteKeyEvent` instead. Deletes a conversion event in a property.

name: The resource name of the conversion event to delete. Format: properties/{property}/conversionEvents/{conversion_event} Example: "properties/123/conversionEvents/456".
func (*PropertiesConversionEventsService) Get ¶
added in v0.47.0
func (r *PropertiesConversionEventsService) Get(name string) *PropertiesConversionEventsGetCall

Get: Deprecated: Use `GetKeyEvent` instead. Retrieve a single conversion event.

name: The resource name of the conversion event to retrieve. Format: properties/{property}/conversionEvents/{conversion_event} Example: "properties/123/conversionEvents/456".
func (*PropertiesConversionEventsService) List ¶
added in v0.47.0
func (r *PropertiesConversionEventsService) List(parent string) *PropertiesConversionEventsListCall

List: Deprecated: Use `ListKeyEvents` instead. Returns a list of conversion events in the specified parent property. Returns an empty list if no conversion events are found.

parent: The resource name of the parent property. Example: 'properties/123'.
func (*PropertiesConversionEventsService) Patch ¶
added in v0.137.0
func (r *PropertiesConversionEventsService) Patch(name string, googleanalyticsadminv1alphaconversionevent *GoogleAnalyticsAdminV1alphaConversionEvent) *PropertiesConversionEventsPatchCall

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
func (c *PropertiesCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaProperty, error)

Do executes the "analyticsadmin.properties.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaProperty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesCreateCall) Fields ¶
func (c *PropertiesCreateCall) Fields(s ...googleapi.Field) *PropertiesCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesCreateCall) Header ¶
func (c *PropertiesCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesCreateRollupPropertyCall ¶
added in v0.144.0
type PropertiesCreateRollupPropertyCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesCreateRollupPropertyCall) Context ¶
added in v0.144.0
func (c *PropertiesCreateRollupPropertyCall) Context(ctx context.Context) *PropertiesCreateRollupPropertyCall

Context sets the context to be used in this call's Do method.

func (*PropertiesCreateRollupPropertyCall) Do ¶
added in v0.144.0
func (c *PropertiesCreateRollupPropertyCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaCreateRollupPropertyResponse, error)

Do executes the "analyticsadmin.properties.createRollupProperty" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaCreateRollupPropertyResponse.ServerResponse.Heade r or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesCreateRollupPropertyCall) Fields ¶
added in v0.144.0
func (c *PropertiesCreateRollupPropertyCall) Fields(s ...googleapi.Field) *PropertiesCreateRollupPropertyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesCreateRollupPropertyCall) Header ¶
added in v0.144.0
func (c *PropertiesCreateRollupPropertyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesCustomDimensionsArchiveCall ¶
added in v0.47.0
type PropertiesCustomDimensionsArchiveCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesCustomDimensionsArchiveCall) Context ¶
added in v0.47.0
func (c *PropertiesCustomDimensionsArchiveCall) Context(ctx context.Context) *PropertiesCustomDimensionsArchiveCall

Context sets the context to be used in this call's Do method.

func (*PropertiesCustomDimensionsArchiveCall) Do ¶
added in v0.47.0
func (c *PropertiesCustomDimensionsArchiveCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.properties.customDimensions.archive" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesCustomDimensionsArchiveCall) Fields ¶
added in v0.47.0
func (c *PropertiesCustomDimensionsArchiveCall) Fields(s ...googleapi.Field) *PropertiesCustomDimensionsArchiveCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesCustomDimensionsArchiveCall) Header ¶
added in v0.47.0
func (c *PropertiesCustomDimensionsArchiveCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesCustomDimensionsCreateCall ¶
added in v0.47.0
type PropertiesCustomDimensionsCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesCustomDimensionsCreateCall) Context ¶
added in v0.47.0
func (c *PropertiesCustomDimensionsCreateCall) Context(ctx context.Context) *PropertiesCustomDimensionsCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesCustomDimensionsCreateCall) Do ¶
added in v0.47.0
func (c *PropertiesCustomDimensionsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaCustomDimension, error)

Do executes the "analyticsadmin.properties.customDimensions.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaCustomDimension.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesCustomDimensionsCreateCall) Fields ¶
added in v0.47.0
func (c *PropertiesCustomDimensionsCreateCall) Fields(s ...googleapi.Field) *PropertiesCustomDimensionsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesCustomDimensionsCreateCall) Header ¶
added in v0.47.0
func (c *PropertiesCustomDimensionsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesCustomDimensionsGetCall ¶
added in v0.47.0
type PropertiesCustomDimensionsGetCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesCustomDimensionsGetCall) Context ¶
added in v0.47.0
func (c *PropertiesCustomDimensionsGetCall) Context(ctx context.Context) *PropertiesCustomDimensionsGetCall

Context sets the context to be used in this call's Do method.

func (*PropertiesCustomDimensionsGetCall) Do ¶
added in v0.47.0
func (c *PropertiesCustomDimensionsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaCustomDimension, error)

Do executes the "analyticsadmin.properties.customDimensions.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaCustomDimension.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesCustomDimensionsGetCall) Fields ¶
added in v0.47.0
func (c *PropertiesCustomDimensionsGetCall) Fields(s ...googleapi.Field) *PropertiesCustomDimensionsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesCustomDimensionsGetCall) Header ¶
added in v0.47.0
func (c *PropertiesCustomDimensionsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesCustomDimensionsGetCall) IfNoneMatch ¶
added in v0.47.0
func (c *PropertiesCustomDimensionsGetCall) IfNoneMatch(entityTag string) *PropertiesCustomDimensionsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesCustomDimensionsListCall ¶
added in v0.47.0
type PropertiesCustomDimensionsListCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesCustomDimensionsListCall) Context ¶
added in v0.47.0
func (c *PropertiesCustomDimensionsListCall) Context(ctx context.Context) *PropertiesCustomDimensionsListCall

Context sets the context to be used in this call's Do method.

func (*PropertiesCustomDimensionsListCall) Do ¶
added in v0.47.0
func (c *PropertiesCustomDimensionsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListCustomDimensionsResponse, error)

Do executes the "analyticsadmin.properties.customDimensions.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaListCustomDimensionsResponse.ServerResponse.Heade r or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesCustomDimensionsListCall) Fields ¶
added in v0.47.0
func (c *PropertiesCustomDimensionsListCall) Fields(s ...googleapi.Field) *PropertiesCustomDimensionsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesCustomDimensionsListCall) Header ¶
added in v0.47.0
func (c *PropertiesCustomDimensionsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesCustomDimensionsListCall) IfNoneMatch ¶
added in v0.47.0
func (c *PropertiesCustomDimensionsListCall) IfNoneMatch(entityTag string) *PropertiesCustomDimensionsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesCustomDimensionsListCall) PageSize ¶
added in v0.47.0
func (c *PropertiesCustomDimensionsListCall) PageSize(pageSize int64) *PropertiesCustomDimensionsListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. If unspecified, at most 50 resources will be returned. The maximum value is 200 (higher values will be coerced to the maximum).

func (*PropertiesCustomDimensionsListCall) PageToken ¶
added in v0.47.0
func (c *PropertiesCustomDimensionsListCall) PageToken(pageToken string) *PropertiesCustomDimensionsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListCustomDimensions` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListCustomDimensions` must match the call that provided the page token.

func (*PropertiesCustomDimensionsListCall) Pages ¶
added in v0.47.0
func (c *PropertiesCustomDimensionsListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1alphaListCustomDimensionsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesCustomDimensionsPatchCall ¶
added in v0.47.0
type PropertiesCustomDimensionsPatchCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesCustomDimensionsPatchCall) Context ¶
added in v0.47.0
func (c *PropertiesCustomDimensionsPatchCall) Context(ctx context.Context) *PropertiesCustomDimensionsPatchCall

Context sets the context to be used in this call's Do method.

func (*PropertiesCustomDimensionsPatchCall) Do ¶
added in v0.47.0
func (c *PropertiesCustomDimensionsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaCustomDimension, error)

Do executes the "analyticsadmin.properties.customDimensions.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaCustomDimension.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesCustomDimensionsPatchCall) Fields ¶
added in v0.47.0
func (c *PropertiesCustomDimensionsPatchCall) Fields(s ...googleapi.Field) *PropertiesCustomDimensionsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesCustomDimensionsPatchCall) Header ¶
added in v0.47.0
func (c *PropertiesCustomDimensionsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesCustomDimensionsPatchCall) UpdateMask ¶
added in v0.47.0
func (c *PropertiesCustomDimensionsPatchCall) UpdateMask(updateMask string) *PropertiesCustomDimensionsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated. Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.

type PropertiesCustomDimensionsService ¶
added in v0.47.0
type PropertiesCustomDimensionsService struct {
	// contains filtered or unexported fields
}
func NewPropertiesCustomDimensionsService ¶
added in v0.47.0
func NewPropertiesCustomDimensionsService(s *Service) *PropertiesCustomDimensionsService
func (*PropertiesCustomDimensionsService) Archive ¶
added in v0.47.0
func (r *PropertiesCustomDimensionsService) Archive(name string, googleanalyticsadminv1alphaarchivecustomdimensionrequest *GoogleAnalyticsAdminV1alphaArchiveCustomDimensionRequest) *PropertiesCustomDimensionsArchiveCall

Archive: Archives a CustomDimension on a property.

name: The name of the CustomDimension to archive. Example format: properties/1234/customDimensions/5678.
func (*PropertiesCustomDimensionsService) Create ¶
added in v0.47.0
func (r *PropertiesCustomDimensionsService) Create(parent string, googleanalyticsadminv1alphacustomdimension *GoogleAnalyticsAdminV1alphaCustomDimension) *PropertiesCustomDimensionsCreateCall

Create: Creates a CustomDimension.

- parent: Example format: properties/1234.

func (*PropertiesCustomDimensionsService) Get ¶
added in v0.47.0
func (r *PropertiesCustomDimensionsService) Get(name string) *PropertiesCustomDimensionsGetCall

Get: Lookup for a single CustomDimension.

name: The name of the CustomDimension to get. Example format: properties/1234/customDimensions/5678.
func (*PropertiesCustomDimensionsService) List ¶
added in v0.47.0
func (r *PropertiesCustomDimensionsService) List(parent string) *PropertiesCustomDimensionsListCall

List: Lists CustomDimensions on a property.

- parent: Example format: properties/1234.

func (*PropertiesCustomDimensionsService) Patch ¶
added in v0.47.0
func (r *PropertiesCustomDimensionsService) Patch(name string, googleanalyticsadminv1alphacustomdimension *GoogleAnalyticsAdminV1alphaCustomDimension) *PropertiesCustomDimensionsPatchCall

Patch: Updates a CustomDimension on a property.

name: Output only. Resource name for this CustomDimension resource. Format: properties/{property}/customDimensions/{customDimension}.
type PropertiesCustomMetricsArchiveCall ¶
added in v0.47.0
type PropertiesCustomMetricsArchiveCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesCustomMetricsArchiveCall) Context ¶
added in v0.47.0
func (c *PropertiesCustomMetricsArchiveCall) Context(ctx context.Context) *PropertiesCustomMetricsArchiveCall

Context sets the context to be used in this call's Do method.

func (*PropertiesCustomMetricsArchiveCall) Do ¶
added in v0.47.0
func (c *PropertiesCustomMetricsArchiveCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.properties.customMetrics.archive" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesCustomMetricsArchiveCall) Fields ¶
added in v0.47.0
func (c *PropertiesCustomMetricsArchiveCall) Fields(s ...googleapi.Field) *PropertiesCustomMetricsArchiveCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesCustomMetricsArchiveCall) Header ¶
added in v0.47.0
func (c *PropertiesCustomMetricsArchiveCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesCustomMetricsCreateCall ¶
added in v0.47.0
type PropertiesCustomMetricsCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesCustomMetricsCreateCall) Context ¶
added in v0.47.0
func (c *PropertiesCustomMetricsCreateCall) Context(ctx context.Context) *PropertiesCustomMetricsCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesCustomMetricsCreateCall) Do ¶
added in v0.47.0
func (c *PropertiesCustomMetricsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaCustomMetric, error)

Do executes the "analyticsadmin.properties.customMetrics.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaCustomMetric.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesCustomMetricsCreateCall) Fields ¶
added in v0.47.0
func (c *PropertiesCustomMetricsCreateCall) Fields(s ...googleapi.Field) *PropertiesCustomMetricsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesCustomMetricsCreateCall) Header ¶
added in v0.47.0
func (c *PropertiesCustomMetricsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesCustomMetricsGetCall ¶
added in v0.47.0
type PropertiesCustomMetricsGetCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesCustomMetricsGetCall) Context ¶
added in v0.47.0
func (c *PropertiesCustomMetricsGetCall) Context(ctx context.Context) *PropertiesCustomMetricsGetCall

Context sets the context to be used in this call's Do method.

func (*PropertiesCustomMetricsGetCall) Do ¶
added in v0.47.0
func (c *PropertiesCustomMetricsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaCustomMetric, error)

Do executes the "analyticsadmin.properties.customMetrics.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaCustomMetric.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesCustomMetricsGetCall) Fields ¶
added in v0.47.0
func (c *PropertiesCustomMetricsGetCall) Fields(s ...googleapi.Field) *PropertiesCustomMetricsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesCustomMetricsGetCall) Header ¶
added in v0.47.0
func (c *PropertiesCustomMetricsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesCustomMetricsGetCall) IfNoneMatch ¶
added in v0.47.0
func (c *PropertiesCustomMetricsGetCall) IfNoneMatch(entityTag string) *PropertiesCustomMetricsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesCustomMetricsListCall ¶
added in v0.47.0
type PropertiesCustomMetricsListCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesCustomMetricsListCall) Context ¶
added in v0.47.0
func (c *PropertiesCustomMetricsListCall) Context(ctx context.Context) *PropertiesCustomMetricsListCall

Context sets the context to be used in this call's Do method.

func (*PropertiesCustomMetricsListCall) Do ¶
added in v0.47.0
func (c *PropertiesCustomMetricsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListCustomMetricsResponse, error)

Do executes the "analyticsadmin.properties.customMetrics.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaListCustomMetricsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesCustomMetricsListCall) Fields ¶
added in v0.47.0
func (c *PropertiesCustomMetricsListCall) Fields(s ...googleapi.Field) *PropertiesCustomMetricsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesCustomMetricsListCall) Header ¶
added in v0.47.0
func (c *PropertiesCustomMetricsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesCustomMetricsListCall) IfNoneMatch ¶
added in v0.47.0
func (c *PropertiesCustomMetricsListCall) IfNoneMatch(entityTag string) *PropertiesCustomMetricsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesCustomMetricsListCall) PageSize ¶
added in v0.47.0
func (c *PropertiesCustomMetricsListCall) PageSize(pageSize int64) *PropertiesCustomMetricsListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. If unspecified, at most 50 resources will be returned. The maximum value is 200 (higher values will be coerced to the maximum).

func (*PropertiesCustomMetricsListCall) PageToken ¶
added in v0.47.0
func (c *PropertiesCustomMetricsListCall) PageToken(pageToken string) *PropertiesCustomMetricsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListCustomMetrics` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListCustomMetrics` must match the call that provided the page token.

func (*PropertiesCustomMetricsListCall) Pages ¶
added in v0.47.0
func (c *PropertiesCustomMetricsListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1alphaListCustomMetricsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesCustomMetricsPatchCall ¶
added in v0.47.0
type PropertiesCustomMetricsPatchCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesCustomMetricsPatchCall) Context ¶
added in v0.47.0
func (c *PropertiesCustomMetricsPatchCall) Context(ctx context.Context) *PropertiesCustomMetricsPatchCall

Context sets the context to be used in this call's Do method.

func (*PropertiesCustomMetricsPatchCall) Do ¶
added in v0.47.0
func (c *PropertiesCustomMetricsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaCustomMetric, error)

Do executes the "analyticsadmin.properties.customMetrics.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaCustomMetric.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesCustomMetricsPatchCall) Fields ¶
added in v0.47.0
func (c *PropertiesCustomMetricsPatchCall) Fields(s ...googleapi.Field) *PropertiesCustomMetricsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesCustomMetricsPatchCall) Header ¶
added in v0.47.0
func (c *PropertiesCustomMetricsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesCustomMetricsPatchCall) UpdateMask ¶
added in v0.47.0
func (c *PropertiesCustomMetricsPatchCall) UpdateMask(updateMask string) *PropertiesCustomMetricsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated. Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.

type PropertiesCustomMetricsService ¶
added in v0.47.0
type PropertiesCustomMetricsService struct {
	// contains filtered or unexported fields
}
func NewPropertiesCustomMetricsService ¶
added in v0.47.0
func NewPropertiesCustomMetricsService(s *Service) *PropertiesCustomMetricsService
func (*PropertiesCustomMetricsService) Archive ¶
added in v0.47.0
func (r *PropertiesCustomMetricsService) Archive(name string, googleanalyticsadminv1alphaarchivecustommetricrequest *GoogleAnalyticsAdminV1alphaArchiveCustomMetricRequest) *PropertiesCustomMetricsArchiveCall

Archive: Archives a CustomMetric on a property.

name: The name of the CustomMetric to archive. Example format: properties/1234/customMetrics/5678.
func (*PropertiesCustomMetricsService) Create ¶
added in v0.47.0
func (r *PropertiesCustomMetricsService) Create(parent string, googleanalyticsadminv1alphacustommetric *GoogleAnalyticsAdminV1alphaCustomMetric) *PropertiesCustomMetricsCreateCall

Create: Creates a CustomMetric.

- parent: Example format: properties/1234.

func (*PropertiesCustomMetricsService) Get ¶
added in v0.47.0
func (r *PropertiesCustomMetricsService) Get(name string) *PropertiesCustomMetricsGetCall

Get: Lookup for a single CustomMetric.

name: The name of the CustomMetric to get. Example format: properties/1234/customMetrics/5678.
func (*PropertiesCustomMetricsService) List ¶
added in v0.47.0
func (r *PropertiesCustomMetricsService) List(parent string) *PropertiesCustomMetricsListCall

List: Lists CustomMetrics on a property.

- parent: Example format: properties/1234.

func (*PropertiesCustomMetricsService) Patch ¶
added in v0.47.0
func (r *PropertiesCustomMetricsService) Patch(name string, googleanalyticsadminv1alphacustommetric *GoogleAnalyticsAdminV1alphaCustomMetric) *PropertiesCustomMetricsPatchCall

Patch: Updates a CustomMetric on a property.

name: Output only. Resource name for this CustomMetric resource. Format: properties/{property}/customMetrics/{customMetric}.
type PropertiesDataStreamsCreateCall ¶
added in v0.61.0
type PropertiesDataStreamsCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsCreateCall) Context ¶
added in v0.61.0
func (c *PropertiesDataStreamsCreateCall) Context(ctx context.Context) *PropertiesDataStreamsCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsCreateCall) Do ¶
added in v0.61.0
func (c *PropertiesDataStreamsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaDataStream, error)

Do executes the "analyticsadmin.properties.dataStreams.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaDataStream.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsCreateCall) Fields ¶
added in v0.61.0
func (c *PropertiesDataStreamsCreateCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsCreateCall) Header ¶
added in v0.61.0
func (c *PropertiesDataStreamsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesDataStreamsDeleteCall ¶
added in v0.61.0
type PropertiesDataStreamsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsDeleteCall) Context ¶
added in v0.61.0
func (c *PropertiesDataStreamsDeleteCall) Context(ctx context.Context) *PropertiesDataStreamsDeleteCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsDeleteCall) Do ¶
added in v0.61.0
func (c *PropertiesDataStreamsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.properties.dataStreams.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsDeleteCall) Fields ¶
added in v0.61.0
func (c *PropertiesDataStreamsDeleteCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsDeleteCall) Header ¶
added in v0.61.0
func (c *PropertiesDataStreamsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesDataStreamsEventCreateRulesCreateCall ¶
added in v0.122.0
type PropertiesDataStreamsEventCreateRulesCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsEventCreateRulesCreateCall) Context ¶
added in v0.122.0
func (c *PropertiesDataStreamsEventCreateRulesCreateCall) Context(ctx context.Context) *PropertiesDataStreamsEventCreateRulesCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsEventCreateRulesCreateCall) Do ¶
added in v0.122.0
func (c *PropertiesDataStreamsEventCreateRulesCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaEventCreateRule, error)

Do executes the "analyticsadmin.properties.dataStreams.eventCreateRules.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaEventCreateRule.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsEventCreateRulesCreateCall) Fields ¶
added in v0.122.0
func (c *PropertiesDataStreamsEventCreateRulesCreateCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsEventCreateRulesCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsEventCreateRulesCreateCall) Header ¶
added in v0.122.0
func (c *PropertiesDataStreamsEventCreateRulesCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesDataStreamsEventCreateRulesDeleteCall ¶
added in v0.122.0
type PropertiesDataStreamsEventCreateRulesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsEventCreateRulesDeleteCall) Context ¶
added in v0.122.0
func (c *PropertiesDataStreamsEventCreateRulesDeleteCall) Context(ctx context.Context) *PropertiesDataStreamsEventCreateRulesDeleteCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsEventCreateRulesDeleteCall) Do ¶
added in v0.122.0
func (c *PropertiesDataStreamsEventCreateRulesDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.properties.dataStreams.eventCreateRules.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsEventCreateRulesDeleteCall) Fields ¶
added in v0.122.0
func (c *PropertiesDataStreamsEventCreateRulesDeleteCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsEventCreateRulesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsEventCreateRulesDeleteCall) Header ¶
added in v0.122.0
func (c *PropertiesDataStreamsEventCreateRulesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesDataStreamsEventCreateRulesGetCall ¶
added in v0.122.0
type PropertiesDataStreamsEventCreateRulesGetCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsEventCreateRulesGetCall) Context ¶
added in v0.122.0
func (c *PropertiesDataStreamsEventCreateRulesGetCall) Context(ctx context.Context) *PropertiesDataStreamsEventCreateRulesGetCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsEventCreateRulesGetCall) Do ¶
added in v0.122.0
func (c *PropertiesDataStreamsEventCreateRulesGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaEventCreateRule, error)

Do executes the "analyticsadmin.properties.dataStreams.eventCreateRules.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaEventCreateRule.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsEventCreateRulesGetCall) Fields ¶
added in v0.122.0
func (c *PropertiesDataStreamsEventCreateRulesGetCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsEventCreateRulesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsEventCreateRulesGetCall) Header ¶
added in v0.122.0
func (c *PropertiesDataStreamsEventCreateRulesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesDataStreamsEventCreateRulesGetCall) IfNoneMatch ¶
added in v0.122.0
func (c *PropertiesDataStreamsEventCreateRulesGetCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsEventCreateRulesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesDataStreamsEventCreateRulesListCall ¶
added in v0.122.0
type PropertiesDataStreamsEventCreateRulesListCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsEventCreateRulesListCall) Context ¶
added in v0.122.0
func (c *PropertiesDataStreamsEventCreateRulesListCall) Context(ctx context.Context) *PropertiesDataStreamsEventCreateRulesListCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsEventCreateRulesListCall) Do ¶
added in v0.122.0
func (c *PropertiesDataStreamsEventCreateRulesListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListEventCreateRulesResponse, error)

Do executes the "analyticsadmin.properties.dataStreams.eventCreateRules.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaListEventCreateRulesResponse.ServerResponse.Heade r or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsEventCreateRulesListCall) Fields ¶
added in v0.122.0
func (c *PropertiesDataStreamsEventCreateRulesListCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsEventCreateRulesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsEventCreateRulesListCall) Header ¶
added in v0.122.0
func (c *PropertiesDataStreamsEventCreateRulesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesDataStreamsEventCreateRulesListCall) IfNoneMatch ¶
added in v0.122.0
func (c *PropertiesDataStreamsEventCreateRulesListCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsEventCreateRulesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesDataStreamsEventCreateRulesListCall) PageSize ¶
added in v0.122.0
func (c *PropertiesDataStreamsEventCreateRulesListCall) PageSize(pageSize int64) *PropertiesDataStreamsEventCreateRulesListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. If unspecified, at most 50 resources will be returned. The maximum value is 200 (higher values will be coerced to the maximum).

func (*PropertiesDataStreamsEventCreateRulesListCall) PageToken ¶
added in v0.122.0
func (c *PropertiesDataStreamsEventCreateRulesListCall) PageToken(pageToken string) *PropertiesDataStreamsEventCreateRulesListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListEventCreateRules` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListEventCreateRules` must match the call that provided the page token.

func (*PropertiesDataStreamsEventCreateRulesListCall) Pages ¶
added in v0.122.0
func (c *PropertiesDataStreamsEventCreateRulesListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1alphaListEventCreateRulesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesDataStreamsEventCreateRulesPatchCall ¶
added in v0.122.0
type PropertiesDataStreamsEventCreateRulesPatchCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsEventCreateRulesPatchCall) Context ¶
added in v0.122.0
func (c *PropertiesDataStreamsEventCreateRulesPatchCall) Context(ctx context.Context) *PropertiesDataStreamsEventCreateRulesPatchCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsEventCreateRulesPatchCall) Do ¶
added in v0.122.0
func (c *PropertiesDataStreamsEventCreateRulesPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaEventCreateRule, error)

Do executes the "analyticsadmin.properties.dataStreams.eventCreateRules.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaEventCreateRule.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsEventCreateRulesPatchCall) Fields ¶
added in v0.122.0
func (c *PropertiesDataStreamsEventCreateRulesPatchCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsEventCreateRulesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsEventCreateRulesPatchCall) Header ¶
added in v0.122.0
func (c *PropertiesDataStreamsEventCreateRulesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesDataStreamsEventCreateRulesPatchCall) UpdateMask ¶
added in v0.122.0
func (c *PropertiesDataStreamsEventCreateRulesPatchCall) UpdateMask(updateMask string) *PropertiesDataStreamsEventCreateRulesPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated. Field names must be in snake case (e.g., "field_to_update"). Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.

type PropertiesDataStreamsEventCreateRulesService ¶
added in v0.122.0
type PropertiesDataStreamsEventCreateRulesService struct {
	// contains filtered or unexported fields
}
func NewPropertiesDataStreamsEventCreateRulesService ¶
added in v0.122.0
func NewPropertiesDataStreamsEventCreateRulesService(s *Service) *PropertiesDataStreamsEventCreateRulesService
func (*PropertiesDataStreamsEventCreateRulesService) Create ¶
added in v0.122.0
func (r *PropertiesDataStreamsEventCreateRulesService) Create(parent string, googleanalyticsadminv1alphaeventcreaterule *GoogleAnalyticsAdminV1alphaEventCreateRule) *PropertiesDataStreamsEventCreateRulesCreateCall

Create: Creates an EventCreateRule.

- parent: Example format: properties/123/dataStreams/456.

func (*PropertiesDataStreamsEventCreateRulesService) Delete ¶
added in v0.122.0
func (r *PropertiesDataStreamsEventCreateRulesService) Delete(name string) *PropertiesDataStreamsEventCreateRulesDeleteCall

Delete: Deletes an EventCreateRule.

- name: Example format: properties/123/dataStreams/456/eventCreateRules/789.

func (*PropertiesDataStreamsEventCreateRulesService) Get ¶
added in v0.122.0
func (r *PropertiesDataStreamsEventCreateRulesService) Get(name string) *PropertiesDataStreamsEventCreateRulesGetCall

Get: Lookup for a single EventCreateRule.

name: The name of the EventCreateRule to get. Example format: properties/123/dataStreams/456/eventCreateRules/789.
func (*PropertiesDataStreamsEventCreateRulesService) List ¶
added in v0.122.0
func (r *PropertiesDataStreamsEventCreateRulesService) List(parent string) *PropertiesDataStreamsEventCreateRulesListCall

List: Lists EventCreateRules on a web data stream.

- parent: Example format: properties/123/dataStreams/456.

func (*PropertiesDataStreamsEventCreateRulesService) Patch ¶
added in v0.122.0
func (r *PropertiesDataStreamsEventCreateRulesService) Patch(name string, googleanalyticsadminv1alphaeventcreaterule *GoogleAnalyticsAdminV1alphaEventCreateRule) *PropertiesDataStreamsEventCreateRulesPatchCall

Patch: Updates an EventCreateRule.

name: Output only. Resource name for this EventCreateRule resource. Format: properties/{property}/dataStreams/{data_stream}/eventCreateRules/{event_cre ate_rule}.
type PropertiesDataStreamsEventEditRulesCreateCall ¶
added in v0.190.0
type PropertiesDataStreamsEventEditRulesCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsEventEditRulesCreateCall) Context ¶
added in v0.190.0
func (c *PropertiesDataStreamsEventEditRulesCreateCall) Context(ctx context.Context) *PropertiesDataStreamsEventEditRulesCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsEventEditRulesCreateCall) Do ¶
added in v0.190.0
func (c *PropertiesDataStreamsEventEditRulesCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaEventEditRule, error)

Do executes the "analyticsadmin.properties.dataStreams.eventEditRules.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaEventEditRule.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsEventEditRulesCreateCall) Fields ¶
added in v0.190.0
func (c *PropertiesDataStreamsEventEditRulesCreateCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsEventEditRulesCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsEventEditRulesCreateCall) Header ¶
added in v0.190.0
func (c *PropertiesDataStreamsEventEditRulesCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesDataStreamsEventEditRulesDeleteCall ¶
added in v0.190.0
type PropertiesDataStreamsEventEditRulesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsEventEditRulesDeleteCall) Context ¶
added in v0.190.0
func (c *PropertiesDataStreamsEventEditRulesDeleteCall) Context(ctx context.Context) *PropertiesDataStreamsEventEditRulesDeleteCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsEventEditRulesDeleteCall) Do ¶
added in v0.190.0
func (c *PropertiesDataStreamsEventEditRulesDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.properties.dataStreams.eventEditRules.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsEventEditRulesDeleteCall) Fields ¶
added in v0.190.0
func (c *PropertiesDataStreamsEventEditRulesDeleteCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsEventEditRulesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsEventEditRulesDeleteCall) Header ¶
added in v0.190.0
func (c *PropertiesDataStreamsEventEditRulesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesDataStreamsEventEditRulesGetCall ¶
added in v0.190.0
type PropertiesDataStreamsEventEditRulesGetCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsEventEditRulesGetCall) Context ¶
added in v0.190.0
func (c *PropertiesDataStreamsEventEditRulesGetCall) Context(ctx context.Context) *PropertiesDataStreamsEventEditRulesGetCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsEventEditRulesGetCall) Do ¶
added in v0.190.0
func (c *PropertiesDataStreamsEventEditRulesGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaEventEditRule, error)

Do executes the "analyticsadmin.properties.dataStreams.eventEditRules.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaEventEditRule.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsEventEditRulesGetCall) Fields ¶
added in v0.190.0
func (c *PropertiesDataStreamsEventEditRulesGetCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsEventEditRulesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsEventEditRulesGetCall) Header ¶
added in v0.190.0
func (c *PropertiesDataStreamsEventEditRulesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesDataStreamsEventEditRulesGetCall) IfNoneMatch ¶
added in v0.190.0
func (c *PropertiesDataStreamsEventEditRulesGetCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsEventEditRulesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesDataStreamsEventEditRulesListCall ¶
added in v0.190.0
type PropertiesDataStreamsEventEditRulesListCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsEventEditRulesListCall) Context ¶
added in v0.190.0
func (c *PropertiesDataStreamsEventEditRulesListCall) Context(ctx context.Context) *PropertiesDataStreamsEventEditRulesListCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsEventEditRulesListCall) Do ¶
added in v0.190.0
func (c *PropertiesDataStreamsEventEditRulesListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListEventEditRulesResponse, error)

Do executes the "analyticsadmin.properties.dataStreams.eventEditRules.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaListEventEditRulesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsEventEditRulesListCall) Fields ¶
added in v0.190.0
func (c *PropertiesDataStreamsEventEditRulesListCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsEventEditRulesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsEventEditRulesListCall) Header ¶
added in v0.190.0
func (c *PropertiesDataStreamsEventEditRulesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesDataStreamsEventEditRulesListCall) IfNoneMatch ¶
added in v0.190.0
func (c *PropertiesDataStreamsEventEditRulesListCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsEventEditRulesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesDataStreamsEventEditRulesListCall) PageSize ¶
added in v0.190.0
func (c *PropertiesDataStreamsEventEditRulesListCall) PageSize(pageSize int64) *PropertiesDataStreamsEventEditRulesListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. If unspecified, at most 50 resources will be returned. The maximum value is 200 (higher values will be coerced to the maximum).

func (*PropertiesDataStreamsEventEditRulesListCall) PageToken ¶
added in v0.190.0
func (c *PropertiesDataStreamsEventEditRulesListCall) PageToken(pageToken string) *PropertiesDataStreamsEventEditRulesListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListEventEditRules` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListEventEditRules` must match the call that provided the page token.

func (*PropertiesDataStreamsEventEditRulesListCall) Pages ¶
added in v0.190.0
func (c *PropertiesDataStreamsEventEditRulesListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1alphaListEventEditRulesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesDataStreamsEventEditRulesPatchCall ¶
added in v0.190.0
type PropertiesDataStreamsEventEditRulesPatchCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsEventEditRulesPatchCall) Context ¶
added in v0.190.0
func (c *PropertiesDataStreamsEventEditRulesPatchCall) Context(ctx context.Context) *PropertiesDataStreamsEventEditRulesPatchCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsEventEditRulesPatchCall) Do ¶
added in v0.190.0
func (c *PropertiesDataStreamsEventEditRulesPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaEventEditRule, error)

Do executes the "analyticsadmin.properties.dataStreams.eventEditRules.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaEventEditRule.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsEventEditRulesPatchCall) Fields ¶
added in v0.190.0
func (c *PropertiesDataStreamsEventEditRulesPatchCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsEventEditRulesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsEventEditRulesPatchCall) Header ¶
added in v0.190.0
func (c *PropertiesDataStreamsEventEditRulesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesDataStreamsEventEditRulesPatchCall) UpdateMask ¶
added in v0.190.0
func (c *PropertiesDataStreamsEventEditRulesPatchCall) UpdateMask(updateMask string) *PropertiesDataStreamsEventEditRulesPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated. Field names must be in snake case (e.g., "field_to_update"). Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.

type PropertiesDataStreamsEventEditRulesReorderCall ¶
added in v0.183.0
type PropertiesDataStreamsEventEditRulesReorderCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsEventEditRulesReorderCall) Context ¶
added in v0.183.0
func (c *PropertiesDataStreamsEventEditRulesReorderCall) Context(ctx context.Context) *PropertiesDataStreamsEventEditRulesReorderCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsEventEditRulesReorderCall) Do ¶
added in v0.183.0
func (c *PropertiesDataStreamsEventEditRulesReorderCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.properties.dataStreams.eventEditRules.reorder" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsEventEditRulesReorderCall) Fields ¶
added in v0.183.0
func (c *PropertiesDataStreamsEventEditRulesReorderCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsEventEditRulesReorderCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsEventEditRulesReorderCall) Header ¶
added in v0.183.0
func (c *PropertiesDataStreamsEventEditRulesReorderCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesDataStreamsEventEditRulesService ¶
added in v0.183.0
type PropertiesDataStreamsEventEditRulesService struct {
	// contains filtered or unexported fields
}
func NewPropertiesDataStreamsEventEditRulesService ¶
added in v0.183.0
func NewPropertiesDataStreamsEventEditRulesService(s *Service) *PropertiesDataStreamsEventEditRulesService
func (*PropertiesDataStreamsEventEditRulesService) Create ¶
added in v0.190.0
func (r *PropertiesDataStreamsEventEditRulesService) Create(parent string, googleanalyticsadminv1alphaeventeditrule *GoogleAnalyticsAdminV1alphaEventEditRule) *PropertiesDataStreamsEventEditRulesCreateCall

Create: Creates an EventEditRule.

- parent: Example format: properties/123/dataStreams/456.

func (*PropertiesDataStreamsEventEditRulesService) Delete ¶
added in v0.190.0
func (r *PropertiesDataStreamsEventEditRulesService) Delete(name string) *PropertiesDataStreamsEventEditRulesDeleteCall

Delete: Deletes an EventEditRule.

- name: Example format: properties/123/dataStreams/456/eventEditRules/789.

func (*PropertiesDataStreamsEventEditRulesService) Get ¶
added in v0.190.0
func (r *PropertiesDataStreamsEventEditRulesService) Get(name string) *PropertiesDataStreamsEventEditRulesGetCall

Get: Lookup for a single EventEditRule.

name: The name of the EventEditRule to get. Example format: properties/123/dataStreams/456/eventEditRules/789.
func (*PropertiesDataStreamsEventEditRulesService) List ¶
added in v0.190.0
func (r *PropertiesDataStreamsEventEditRulesService) List(parent string) *PropertiesDataStreamsEventEditRulesListCall

List: Lists EventEditRules on a web data stream.

- parent: Example format: properties/123/dataStreams/456.

func (*PropertiesDataStreamsEventEditRulesService) Patch ¶
added in v0.190.0
func (r *PropertiesDataStreamsEventEditRulesService) Patch(name string, googleanalyticsadminv1alphaeventeditrule *GoogleAnalyticsAdminV1alphaEventEditRule) *PropertiesDataStreamsEventEditRulesPatchCall

Patch: Updates an EventEditRule.

name: Identifier. Resource name for this EventEditRule resource. Format: properties/{property}/dataStreams/{data_stream}/eventEditRules/{event_edit_ rule}.
func (*PropertiesDataStreamsEventEditRulesService) Reorder ¶
added in v0.183.0
func (r *PropertiesDataStreamsEventEditRulesService) Reorder(parent string, googleanalyticsadminv1alphareordereventeditrulesrequest *GoogleAnalyticsAdminV1alphaReorderEventEditRulesRequest) *PropertiesDataStreamsEventEditRulesReorderCall

Reorder: Changes the processing order of event edit rules on the specified stream.

- parent: Example format: properties/123/dataStreams/456.

type PropertiesDataStreamsGetCall ¶
added in v0.61.0
type PropertiesDataStreamsGetCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsGetCall) Context ¶
added in v0.61.0
func (c *PropertiesDataStreamsGetCall) Context(ctx context.Context) *PropertiesDataStreamsGetCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsGetCall) Do ¶
added in v0.61.0
func (c *PropertiesDataStreamsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaDataStream, error)

Do executes the "analyticsadmin.properties.dataStreams.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaDataStream.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsGetCall) Fields ¶
added in v0.61.0
func (c *PropertiesDataStreamsGetCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsGetCall) Header ¶
added in v0.61.0
func (c *PropertiesDataStreamsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesDataStreamsGetCall) IfNoneMatch ¶
added in v0.61.0
func (c *PropertiesDataStreamsGetCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesDataStreamsGetDataRedactionSettingsCall ¶
added in v0.144.0
type PropertiesDataStreamsGetDataRedactionSettingsCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsGetDataRedactionSettingsCall) Context ¶
added in v0.144.0
func (c *PropertiesDataStreamsGetDataRedactionSettingsCall) Context(ctx context.Context) *PropertiesDataStreamsGetDataRedactionSettingsCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsGetDataRedactionSettingsCall) Do ¶
added in v0.144.0
func (c *PropertiesDataStreamsGetDataRedactionSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaDataRedactionSettings, error)

Do executes the "analyticsadmin.properties.dataStreams.getDataRedactionSettings" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaDataRedactionSettings.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsGetDataRedactionSettingsCall) Fields ¶
added in v0.144.0
func (c *PropertiesDataStreamsGetDataRedactionSettingsCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsGetDataRedactionSettingsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsGetDataRedactionSettingsCall) Header ¶
added in v0.144.0
func (c *PropertiesDataStreamsGetDataRedactionSettingsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesDataStreamsGetDataRedactionSettingsCall) IfNoneMatch ¶
added in v0.144.0
func (c *PropertiesDataStreamsGetDataRedactionSettingsCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsGetDataRedactionSettingsCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesDataStreamsGetEnhancedMeasurementSettingsCall ¶
added in v0.112.0
type PropertiesDataStreamsGetEnhancedMeasurementSettingsCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsGetEnhancedMeasurementSettingsCall) Context ¶
added in v0.112.0
func (c *PropertiesDataStreamsGetEnhancedMeasurementSettingsCall) Context(ctx context.Context) *PropertiesDataStreamsGetEnhancedMeasurementSettingsCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsGetEnhancedMeasurementSettingsCall) Do ¶
added in v0.112.0
func (c *PropertiesDataStreamsGetEnhancedMeasurementSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettings, error)

Do executes the "analyticsadmin.properties.dataStreams.getEnhancedMeasurementSettings" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettings.ServerResponse.Header

or (if a response was returned at all) in error.(*googleapi.Error).Header.


Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsGetEnhancedMeasurementSettingsCall) Fields ¶
added in v0.112.0
func (c *PropertiesDataStreamsGetEnhancedMeasurementSettingsCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsGetEnhancedMeasurementSettingsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsGetEnhancedMeasurementSettingsCall) Header ¶
added in v0.112.0
func (c *PropertiesDataStreamsGetEnhancedMeasurementSettingsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesDataStreamsGetEnhancedMeasurementSettingsCall) IfNoneMatch ¶
added in v0.112.0
func (c *PropertiesDataStreamsGetEnhancedMeasurementSettingsCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsGetEnhancedMeasurementSettingsCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesDataStreamsGetGlobalSiteTagCall ¶
added in v0.67.0
type PropertiesDataStreamsGetGlobalSiteTagCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsGetGlobalSiteTagCall) Context ¶
added in v0.67.0
func (c *PropertiesDataStreamsGetGlobalSiteTagCall) Context(ctx context.Context) *PropertiesDataStreamsGetGlobalSiteTagCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsGetGlobalSiteTagCall) Do ¶
added in v0.67.0
func (c *PropertiesDataStreamsGetGlobalSiteTagCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaGlobalSiteTag, error)

Do executes the "analyticsadmin.properties.dataStreams.getGlobalSiteTag" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaGlobalSiteTag.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsGetGlobalSiteTagCall) Fields ¶
added in v0.67.0
func (c *PropertiesDataStreamsGetGlobalSiteTagCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsGetGlobalSiteTagCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsGetGlobalSiteTagCall) Header ¶
added in v0.67.0
func (c *PropertiesDataStreamsGetGlobalSiteTagCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesDataStreamsGetGlobalSiteTagCall) IfNoneMatch ¶
added in v0.67.0
func (c *PropertiesDataStreamsGetGlobalSiteTagCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsGetGlobalSiteTagCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesDataStreamsListCall ¶
added in v0.61.0
type PropertiesDataStreamsListCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsListCall) Context ¶
added in v0.61.0
func (c *PropertiesDataStreamsListCall) Context(ctx context.Context) *PropertiesDataStreamsListCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsListCall) Do ¶
added in v0.61.0
func (c *PropertiesDataStreamsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListDataStreamsResponse, error)

Do executes the "analyticsadmin.properties.dataStreams.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaListDataStreamsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsListCall) Fields ¶
added in v0.61.0
func (c *PropertiesDataStreamsListCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsListCall) Header ¶
added in v0.61.0
func (c *PropertiesDataStreamsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesDataStreamsListCall) IfNoneMatch ¶
added in v0.61.0
func (c *PropertiesDataStreamsListCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesDataStreamsListCall) PageSize ¶
added in v0.61.0
func (c *PropertiesDataStreamsListCall) PageSize(pageSize int64) *PropertiesDataStreamsListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. If unspecified, at most 50 resources will be returned. The maximum value is 200 (higher values will be coerced to the maximum).

func (*PropertiesDataStreamsListCall) PageToken ¶
added in v0.61.0
func (c *PropertiesDataStreamsListCall) PageToken(pageToken string) *PropertiesDataStreamsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListDataStreams` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListDataStreams` must match the call that provided the page token.

func (*PropertiesDataStreamsListCall) Pages ¶
added in v0.61.0
func (c *PropertiesDataStreamsListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1alphaListDataStreamsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesDataStreamsMeasurementProtocolSecretsCreateCall ¶
added in v0.66.0
type PropertiesDataStreamsMeasurementProtocolSecretsCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsMeasurementProtocolSecretsCreateCall) Context ¶
added in v0.66.0
func (c *PropertiesDataStreamsMeasurementProtocolSecretsCreateCall) Context(ctx context.Context) *PropertiesDataStreamsMeasurementProtocolSecretsCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsMeasurementProtocolSecretsCreateCall) Do ¶
added in v0.66.0
func (c *PropertiesDataStreamsMeasurementProtocolSecretsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret, error)

Do executes the "analyticsadmin.properties.dataStreams.measurementProtocolSecrets.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsMeasurementProtocolSecretsCreateCall) Fields ¶
added in v0.66.0
func (c *PropertiesDataStreamsMeasurementProtocolSecretsCreateCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsMeasurementProtocolSecretsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsMeasurementProtocolSecretsCreateCall) Header ¶
added in v0.66.0
func (c *PropertiesDataStreamsMeasurementProtocolSecretsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall ¶
added in v0.66.0
type PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall) Context ¶
added in v0.66.0
func (c *PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall) Context(ctx context.Context) *PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall) Do ¶
added in v0.66.0
func (c *PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.properties.dataStreams.measurementProtocolSecrets.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall) Fields ¶
added in v0.66.0
func (c *PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall) Header ¶
added in v0.66.0
func (c *PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesDataStreamsMeasurementProtocolSecretsGetCall ¶
added in v0.66.0
type PropertiesDataStreamsMeasurementProtocolSecretsGetCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsMeasurementProtocolSecretsGetCall) Context ¶
added in v0.66.0
func (c *PropertiesDataStreamsMeasurementProtocolSecretsGetCall) Context(ctx context.Context) *PropertiesDataStreamsMeasurementProtocolSecretsGetCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsMeasurementProtocolSecretsGetCall) Do ¶
added in v0.66.0
func (c *PropertiesDataStreamsMeasurementProtocolSecretsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret, error)

Do executes the "analyticsadmin.properties.dataStreams.measurementProtocolSecrets.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsMeasurementProtocolSecretsGetCall) Fields ¶
added in v0.66.0
func (c *PropertiesDataStreamsMeasurementProtocolSecretsGetCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsMeasurementProtocolSecretsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsMeasurementProtocolSecretsGetCall) Header ¶
added in v0.66.0
func (c *PropertiesDataStreamsMeasurementProtocolSecretsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesDataStreamsMeasurementProtocolSecretsGetCall) IfNoneMatch ¶
added in v0.66.0
func (c *PropertiesDataStreamsMeasurementProtocolSecretsGetCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsMeasurementProtocolSecretsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesDataStreamsMeasurementProtocolSecretsListCall ¶
added in v0.66.0
type PropertiesDataStreamsMeasurementProtocolSecretsListCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsMeasurementProtocolSecretsListCall) Context ¶
added in v0.66.0
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) Context(ctx context.Context) *PropertiesDataStreamsMeasurementProtocolSecretsListCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsMeasurementProtocolSecretsListCall) Do ¶
added in v0.66.0
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListMeasurementProtocolSecretsResponse, error)

Do executes the "analyticsadmin.properties.dataStreams.measurementProtocolSecrets.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaListMeasurementProtocolSecretsResponse.ServerResp onse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsMeasurementProtocolSecretsListCall) Fields ¶
added in v0.66.0
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsMeasurementProtocolSecretsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsMeasurementProtocolSecretsListCall) Header ¶
added in v0.66.0
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesDataStreamsMeasurementProtocolSecretsListCall) IfNoneMatch ¶
added in v0.66.0
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsMeasurementProtocolSecretsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesDataStreamsMeasurementProtocolSecretsListCall) PageSize ¶
added in v0.66.0
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) PageSize(pageSize int64) *PropertiesDataStreamsMeasurementProtocolSecretsListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. If unspecified, at most 10 resources will be returned. The maximum value is 10. Higher values will be coerced to the maximum.

func (*PropertiesDataStreamsMeasurementProtocolSecretsListCall) PageToken ¶
added in v0.66.0
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) PageToken(pageToken string) *PropertiesDataStreamsMeasurementProtocolSecretsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListMeasurementProtocolSecrets` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListMeasurementProtocolSecrets` must match the call that provided the page token.

func (*PropertiesDataStreamsMeasurementProtocolSecretsListCall) Pages ¶
added in v0.66.0
func (c *PropertiesDataStreamsMeasurementProtocolSecretsListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1alphaListMeasurementProtocolSecretsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesDataStreamsMeasurementProtocolSecretsPatchCall ¶
added in v0.66.0
type PropertiesDataStreamsMeasurementProtocolSecretsPatchCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsMeasurementProtocolSecretsPatchCall) Context ¶
added in v0.66.0
func (c *PropertiesDataStreamsMeasurementProtocolSecretsPatchCall) Context(ctx context.Context) *PropertiesDataStreamsMeasurementProtocolSecretsPatchCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsMeasurementProtocolSecretsPatchCall) Do ¶
added in v0.66.0
func (c *PropertiesDataStreamsMeasurementProtocolSecretsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret, error)

Do executes the "analyticsadmin.properties.dataStreams.measurementProtocolSecrets.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsMeasurementProtocolSecretsPatchCall) Fields ¶
added in v0.66.0
func (c *PropertiesDataStreamsMeasurementProtocolSecretsPatchCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsMeasurementProtocolSecretsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsMeasurementProtocolSecretsPatchCall) Header ¶
added in v0.66.0
func (c *PropertiesDataStreamsMeasurementProtocolSecretsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesDataStreamsMeasurementProtocolSecretsPatchCall) UpdateMask ¶
added in v0.66.0
func (c *PropertiesDataStreamsMeasurementProtocolSecretsPatchCall) UpdateMask(updateMask string) *PropertiesDataStreamsMeasurementProtocolSecretsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated. Omitted fields will not be updated.

type PropertiesDataStreamsMeasurementProtocolSecretsService ¶
added in v0.66.0
type PropertiesDataStreamsMeasurementProtocolSecretsService struct {
	// contains filtered or unexported fields
}
func NewPropertiesDataStreamsMeasurementProtocolSecretsService ¶
added in v0.66.0
func NewPropertiesDataStreamsMeasurementProtocolSecretsService(s *Service) *PropertiesDataStreamsMeasurementProtocolSecretsService
func (*PropertiesDataStreamsMeasurementProtocolSecretsService) Create ¶
added in v0.66.0
func (r *PropertiesDataStreamsMeasurementProtocolSecretsService) Create(parent string, googleanalyticsadminv1alphameasurementprotocolsecret *GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret) *PropertiesDataStreamsMeasurementProtocolSecretsCreateCall

Create: Creates a measurement protocol secret.

parent: The parent resource where this secret will be created. Format: properties/{property}/dataStreams/{dataStream}.
func (*PropertiesDataStreamsMeasurementProtocolSecretsService) Delete ¶
added in v0.66.0
func (r *PropertiesDataStreamsMeasurementProtocolSecretsService) Delete(name string) *PropertiesDataStreamsMeasurementProtocolSecretsDeleteCall

Delete: Deletes target MeasurementProtocolSecret.

name: The name of the MeasurementProtocolSecret to delete. Format: properties/{property}/dataStreams/{dataStream}/measurementProtocolSecrets/{ measurementProtocolSecret}.
func (*PropertiesDataStreamsMeasurementProtocolSecretsService) Get ¶
added in v0.66.0
func (r *PropertiesDataStreamsMeasurementProtocolSecretsService) Get(name string) *PropertiesDataStreamsMeasurementProtocolSecretsGetCall

Get: Lookup for a single MeasurementProtocolSecret.

name: The name of the measurement protocol secret to lookup. Format: properties/{property}/dataStreams/{dataStream}/measurementProtocolSecrets/{ measurementProtocolSecret}.
func (*PropertiesDataStreamsMeasurementProtocolSecretsService) List ¶
added in v0.66.0
func (r *PropertiesDataStreamsMeasurementProtocolSecretsService) List(parent string) *PropertiesDataStreamsMeasurementProtocolSecretsListCall

List: Returns child MeasurementProtocolSecrets under the specified parent Property.

parent: The resource name of the parent stream. Format: properties/{property}/dataStreams/{dataStream}/measurementProtocolSecrets.
func (*PropertiesDataStreamsMeasurementProtocolSecretsService) Patch ¶
added in v0.66.0
func (r *PropertiesDataStreamsMeasurementProtocolSecretsService) Patch(name string, googleanalyticsadminv1alphameasurementprotocolsecret *GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret) *PropertiesDataStreamsMeasurementProtocolSecretsPatchCall

Patch: Updates a measurement protocol secret.

name: Output only. Resource name of this secret. This secret may be a child of any type of stream. Format: properties/{property}/dataStreams/{dataStream}/measurementProtocolSecrets/{ measurementProtocolSecret}.
type PropertiesDataStreamsPatchCall ¶
added in v0.61.0
type PropertiesDataStreamsPatchCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsPatchCall) Context ¶
added in v0.61.0
func (c *PropertiesDataStreamsPatchCall) Context(ctx context.Context) *PropertiesDataStreamsPatchCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsPatchCall) Do ¶
added in v0.61.0
func (c *PropertiesDataStreamsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaDataStream, error)

Do executes the "analyticsadmin.properties.dataStreams.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaDataStream.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsPatchCall) Fields ¶
added in v0.61.0
func (c *PropertiesDataStreamsPatchCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsPatchCall) Header ¶
added in v0.61.0
func (c *PropertiesDataStreamsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesDataStreamsPatchCall) UpdateMask ¶
added in v0.61.0
func (c *PropertiesDataStreamsPatchCall) UpdateMask(updateMask string) *PropertiesDataStreamsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated. Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.

type PropertiesDataStreamsSKAdNetworkConversionValueSchemaCreateCall ¶
added in v0.139.0
type PropertiesDataStreamsSKAdNetworkConversionValueSchemaCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsSKAdNetworkConversionValueSchemaCreateCall) Context ¶
added in v0.139.0
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaCreateCall) Context(ctx context.Context) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsSKAdNetworkConversionValueSchemaCreateCall) Do ¶
added in v0.139.0
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchema, error)

Do executes the "analyticsadmin.properties.dataStreams.sKAdNetworkConversionValueSchema.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchema.ServerResponse.H eader or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsSKAdNetworkConversionValueSchemaCreateCall) Fields ¶
added in v0.139.0
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaCreateCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsSKAdNetworkConversionValueSchemaCreateCall) Header ¶
added in v0.139.0
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesDataStreamsSKAdNetworkConversionValueSchemaDeleteCall ¶
added in v0.139.0
type PropertiesDataStreamsSKAdNetworkConversionValueSchemaDeleteCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsSKAdNetworkConversionValueSchemaDeleteCall) Context ¶
added in v0.139.0
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaDeleteCall) Context(ctx context.Context) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaDeleteCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsSKAdNetworkConversionValueSchemaDeleteCall) Do ¶
added in v0.139.0
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.properties.dataStreams.sKAdNetworkConversionValueSchema.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsSKAdNetworkConversionValueSchemaDeleteCall) Fields ¶
added in v0.139.0
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaDeleteCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsSKAdNetworkConversionValueSchemaDeleteCall) Header ¶
added in v0.139.0
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesDataStreamsSKAdNetworkConversionValueSchemaGetCall ¶
added in v0.139.0
type PropertiesDataStreamsSKAdNetworkConversionValueSchemaGetCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsSKAdNetworkConversionValueSchemaGetCall) Context ¶
added in v0.139.0
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaGetCall) Context(ctx context.Context) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaGetCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsSKAdNetworkConversionValueSchemaGetCall) Do ¶
added in v0.139.0
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchema, error)

Do executes the "analyticsadmin.properties.dataStreams.sKAdNetworkConversionValueSchema.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchema.ServerResponse.H eader or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsSKAdNetworkConversionValueSchemaGetCall) Fields ¶
added in v0.139.0
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaGetCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsSKAdNetworkConversionValueSchemaGetCall) Header ¶
added in v0.139.0
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesDataStreamsSKAdNetworkConversionValueSchemaGetCall) IfNoneMatch ¶
added in v0.139.0
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaGetCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall ¶
added in v0.139.0
type PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall) Context ¶
added in v0.139.0
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall) Context(ctx context.Context) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall) Do ¶
added in v0.139.0
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListSKAdNetworkConversionValueSchemasResponse, error)

Do executes the "analyticsadmin.properties.dataStreams.sKAdNetworkConversionValueSchema.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaListSKAdNetworkConversionValueSchemasResponse.Ser verResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall) Fields ¶
added in v0.139.0
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall) Header ¶
added in v0.139.0
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall) IfNoneMatch ¶
added in v0.139.0
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall) IfNoneMatch(entityTag string) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall) PageSize ¶
added in v0.139.0
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall) PageSize(pageSize int64) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. The service may return fewer than this value, even if there are additional pages. If unspecified, at most 50 resources will be returned. The maximum value is 200; (higher values will be coerced to the maximum)

func (*PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall) PageToken ¶
added in v0.139.0
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall) PageToken(pageToken string) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListSKAdNetworkConversionValueSchemas` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListSKAdNetworkConversionValueSchema` must match the call that provided the page token.

func (*PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall) Pages ¶
added in v0.139.0
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1alphaListSKAdNetworkConversionValueSchemasResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesDataStreamsSKAdNetworkConversionValueSchemaPatchCall ¶
added in v0.139.0
type PropertiesDataStreamsSKAdNetworkConversionValueSchemaPatchCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsSKAdNetworkConversionValueSchemaPatchCall) Context ¶
added in v0.139.0
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaPatchCall) Context(ctx context.Context) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaPatchCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsSKAdNetworkConversionValueSchemaPatchCall) Do ¶
added in v0.139.0
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchema, error)

Do executes the "analyticsadmin.properties.dataStreams.sKAdNetworkConversionValueSchema.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchema.ServerResponse.H eader or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsSKAdNetworkConversionValueSchemaPatchCall) Fields ¶
added in v0.139.0
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaPatchCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsSKAdNetworkConversionValueSchemaPatchCall) Header ¶
added in v0.139.0
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesDataStreamsSKAdNetworkConversionValueSchemaPatchCall) UpdateMask ¶
added in v0.139.0
func (c *PropertiesDataStreamsSKAdNetworkConversionValueSchemaPatchCall) UpdateMask(updateMask string) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated. Omitted fields will not be updated.

type PropertiesDataStreamsSKAdNetworkConversionValueSchemaService ¶
added in v0.139.0
type PropertiesDataStreamsSKAdNetworkConversionValueSchemaService struct {
	// contains filtered or unexported fields
}
func NewPropertiesDataStreamsSKAdNetworkConversionValueSchemaService ¶
added in v0.139.0
func NewPropertiesDataStreamsSKAdNetworkConversionValueSchemaService(s *Service) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaService
func (*PropertiesDataStreamsSKAdNetworkConversionValueSchemaService) Create ¶
added in v0.139.0
func (r *PropertiesDataStreamsSKAdNetworkConversionValueSchemaService) Create(parent string, googleanalyticsadminv1alphaskadnetworkconversionvalueschema *GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchema) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaCreateCall

Create: Creates a SKAdNetworkConversionValueSchema.

parent: The parent resource where this schema will be created. Format: properties/{property}/dataStreams/{dataStream}.
func (*PropertiesDataStreamsSKAdNetworkConversionValueSchemaService) Delete ¶
added in v0.139.0
func (r *PropertiesDataStreamsSKAdNetworkConversionValueSchemaService) Delete(name string) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaDeleteCall

Delete: Deletes target SKAdNetworkConversionValueSchema.

name: The name of the SKAdNetworkConversionValueSchema to delete. Format: properties/{property}/dataStreams/{dataStream}/sKAdNetworkConversionValueSc hema/{skadnetwork_conversion_value_schema}.
func (*PropertiesDataStreamsSKAdNetworkConversionValueSchemaService) Get ¶
added in v0.139.0
func (r *PropertiesDataStreamsSKAdNetworkConversionValueSchemaService) Get(name string) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaGetCall

Get: Looks up a single SKAdNetworkConversionValueSchema.

name: The resource name of SKAdNetwork conversion value schema to look up. Format: properties/{property}/dataStreams/{dataStream}/sKAdNetworkConversionValueSc hema/{skadnetwork_conversion_value_schema}.
func (*PropertiesDataStreamsSKAdNetworkConversionValueSchemaService) List ¶
added in v0.139.0
func (r *PropertiesDataStreamsSKAdNetworkConversionValueSchemaService) List(parent string) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaListCall

List: Lists SKAdNetworkConversionValueSchema on a stream. Properties can have at most one SKAdNetworkConversionValueSchema.

parent: The DataStream resource to list schemas for. Format: properties/{property_id}/dataStreams/{dataStream} Example: properties/1234/dataStreams/5678.
func (*PropertiesDataStreamsSKAdNetworkConversionValueSchemaService) Patch ¶
added in v0.139.0
func (r *PropertiesDataStreamsSKAdNetworkConversionValueSchemaService) Patch(name string, googleanalyticsadminv1alphaskadnetworkconversionvalueschema *GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchema) *PropertiesDataStreamsSKAdNetworkConversionValueSchemaPatchCall

Patch: Updates a SKAdNetworkConversionValueSchema.

name: Output only. Resource name of the schema. This will be child of ONLY an iOS stream, and there can be at most one such child under an iOS stream. Format: properties/{property}/dataStreams/{dataStream}/sKAdNetworkConversionValueSc hema.
type PropertiesDataStreamsService ¶
added in v0.61.0
type PropertiesDataStreamsService struct {
	EventCreateRules *PropertiesDataStreamsEventCreateRulesService

	EventEditRules *PropertiesDataStreamsEventEditRulesService

	MeasurementProtocolSecrets *PropertiesDataStreamsMeasurementProtocolSecretsService

	SKAdNetworkConversionValueSchema *PropertiesDataStreamsSKAdNetworkConversionValueSchemaService
	// contains filtered or unexported fields
}
func NewPropertiesDataStreamsService ¶
added in v0.61.0
func NewPropertiesDataStreamsService(s *Service) *PropertiesDataStreamsService
func (*PropertiesDataStreamsService) Create ¶
added in v0.61.0
func (r *PropertiesDataStreamsService) Create(parent string, googleanalyticsadminv1alphadatastream *GoogleAnalyticsAdminV1alphaDataStream) *PropertiesDataStreamsCreateCall

Create: Creates a DataStream.

- parent: Example format: properties/1234.

func (*PropertiesDataStreamsService) Delete ¶
added in v0.61.0
func (r *PropertiesDataStreamsService) Delete(name string) *PropertiesDataStreamsDeleteCall

Delete: Deletes a DataStream on a property.

name: The name of the DataStream to delete. Example format: properties/1234/dataStreams/5678.
func (*PropertiesDataStreamsService) Get ¶
added in v0.61.0
func (r *PropertiesDataStreamsService) Get(name string) *PropertiesDataStreamsGetCall

Get: Lookup for a single DataStream.

name: The name of the DataStream to get. Example format: properties/1234/dataStreams/5678.
func (*PropertiesDataStreamsService) GetDataRedactionSettings ¶
added in v0.144.0
func (r *PropertiesDataStreamsService) GetDataRedactionSettings(name string) *PropertiesDataStreamsGetDataRedactionSettingsCall

GetDataRedactionSettings: Lookup for a single DataRedactionSettings.

name: The name of the settings to lookup. Format: properties/{property}/dataStreams/{data_stream}/dataRedactionSettings Example: "properties/1000/dataStreams/2000/dataRedactionSettings".
func (*PropertiesDataStreamsService) GetEnhancedMeasurementSettings ¶
added in v0.112.0
func (r *PropertiesDataStreamsService) GetEnhancedMeasurementSettings(name string) *PropertiesDataStreamsGetEnhancedMeasurementSettingsCall

GetEnhancedMeasurementSettings: Returns the enhanced measurement settings for this data stream. Note that the stream must enable enhanced measurement for these settings to take effect.

name: The name of the settings to lookup. Format: properties/{property}/dataStreams/{data_stream}/enhancedMeasurementSettings Example: "properties/1000/dataStreams/2000/enhancedMeasurementSettings".
func (*PropertiesDataStreamsService) GetGlobalSiteTag ¶
added in v0.67.0
func (r *PropertiesDataStreamsService) GetGlobalSiteTag(name string) *PropertiesDataStreamsGetGlobalSiteTagCall

GetGlobalSiteTag: Returns the Site Tag for the specified web stream. Site Tags are immutable singletons.

name: The name of the site tag to lookup. Note that site tags are singletons and do not have unique IDs. Format: properties/{property_id}/dataStreams/{stream_id}/globalSiteTag Example: `properties/123/dataStreams/456/globalSiteTag`.
func (*PropertiesDataStreamsService) List ¶
added in v0.61.0
func (r *PropertiesDataStreamsService) List(parent string) *PropertiesDataStreamsListCall

List: Lists DataStreams on a property.

- parent: Example format: properties/1234.

func (*PropertiesDataStreamsService) Patch ¶
added in v0.61.0
func (r *PropertiesDataStreamsService) Patch(name string, googleanalyticsadminv1alphadatastream *GoogleAnalyticsAdminV1alphaDataStream) *PropertiesDataStreamsPatchCall

Patch: Updates a DataStream on a property.

name: Output only. Resource name of this Data Stream. Format: properties/{property_id}/dataStreams/{stream_id} Example: "properties/1000/dataStreams/2000".
func (*PropertiesDataStreamsService) UpdateDataRedactionSettings ¶
added in v0.144.0
func (r *PropertiesDataStreamsService) UpdateDataRedactionSettings(name string, googleanalyticsadminv1alphadataredactionsettings *GoogleAnalyticsAdminV1alphaDataRedactionSettings) *PropertiesDataStreamsUpdateDataRedactionSettingsCall

UpdateDataRedactionSettings: Updates a DataRedactionSettings on a property.

name: Output only. Name of this Data Redaction Settings resource. Format: properties/{property_id}/dataStreams/{data_stream}/dataRedactionSettings Example: "properties/1000/dataStreams/2000/dataRedactionSettings".
func (*PropertiesDataStreamsService) UpdateEnhancedMeasurementSettings ¶
added in v0.112.0
func (r *PropertiesDataStreamsService) UpdateEnhancedMeasurementSettings(name string, googleanalyticsadminv1alphaenhancedmeasurementsettings *GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettings) *PropertiesDataStreamsUpdateEnhancedMeasurementSettingsCall

UpdateEnhancedMeasurementSettings: Updates the enhanced measurement settings for this data stream. Note that the stream must enable enhanced measurement for these settings to take effect.

name: Output only. Resource name of the Enhanced Measurement Settings. Format: properties/{property_id}/dataStreams/{data_stream}/enhancedMeasurementSetti ngs Example: "properties/1000/dataStreams/2000/enhancedMeasurementSettings".
type PropertiesDataStreamsUpdateDataRedactionSettingsCall ¶
added in v0.144.0
type PropertiesDataStreamsUpdateDataRedactionSettingsCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsUpdateDataRedactionSettingsCall) Context ¶
added in v0.144.0
func (c *PropertiesDataStreamsUpdateDataRedactionSettingsCall) Context(ctx context.Context) *PropertiesDataStreamsUpdateDataRedactionSettingsCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsUpdateDataRedactionSettingsCall) Do ¶
added in v0.144.0
func (c *PropertiesDataStreamsUpdateDataRedactionSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaDataRedactionSettings, error)

Do executes the "analyticsadmin.properties.dataStreams.updateDataRedactionSettings" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaDataRedactionSettings.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsUpdateDataRedactionSettingsCall) Fields ¶
added in v0.144.0
func (c *PropertiesDataStreamsUpdateDataRedactionSettingsCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsUpdateDataRedactionSettingsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsUpdateDataRedactionSettingsCall) Header ¶
added in v0.144.0
func (c *PropertiesDataStreamsUpdateDataRedactionSettingsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesDataStreamsUpdateDataRedactionSettingsCall) UpdateMask ¶
added in v0.144.0
func (c *PropertiesDataStreamsUpdateDataRedactionSettingsCall) UpdateMask(updateMask string) *PropertiesDataStreamsUpdateDataRedactionSettingsCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated. Field names must be in snake case (e.g., "field_to_update"). Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.

type PropertiesDataStreamsUpdateEnhancedMeasurementSettingsCall ¶
added in v0.112.0
type PropertiesDataStreamsUpdateEnhancedMeasurementSettingsCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDataStreamsUpdateEnhancedMeasurementSettingsCall) Context ¶
added in v0.112.0
func (c *PropertiesDataStreamsUpdateEnhancedMeasurementSettingsCall) Context(ctx context.Context) *PropertiesDataStreamsUpdateEnhancedMeasurementSettingsCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDataStreamsUpdateEnhancedMeasurementSettingsCall) Do ¶
added in v0.112.0
func (c *PropertiesDataStreamsUpdateEnhancedMeasurementSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettings, error)

Do executes the "analyticsadmin.properties.dataStreams.updateEnhancedMeasurementSettings" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettings.ServerResponse.Header

or (if a response was returned at all) in error.(*googleapi.Error).Header.


Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDataStreamsUpdateEnhancedMeasurementSettingsCall) Fields ¶
added in v0.112.0
func (c *PropertiesDataStreamsUpdateEnhancedMeasurementSettingsCall) Fields(s ...googleapi.Field) *PropertiesDataStreamsUpdateEnhancedMeasurementSettingsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDataStreamsUpdateEnhancedMeasurementSettingsCall) Header ¶
added in v0.112.0
func (c *PropertiesDataStreamsUpdateEnhancedMeasurementSettingsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesDataStreamsUpdateEnhancedMeasurementSettingsCall) UpdateMask ¶
added in v0.112.0
func (c *PropertiesDataStreamsUpdateEnhancedMeasurementSettingsCall) UpdateMask(updateMask string) *PropertiesDataStreamsUpdateEnhancedMeasurementSettingsCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated. Field names must be in snake case (e.g., "field_to_update"). Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.

type PropertiesDeleteCall ¶
type PropertiesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDeleteCall) Context ¶
func (c *PropertiesDeleteCall) Context(ctx context.Context) *PropertiesDeleteCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDeleteCall) Do ¶
func (c *PropertiesDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaProperty, error)

Do executes the "analyticsadmin.properties.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaProperty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDeleteCall) Fields ¶
func (c *PropertiesDeleteCall) Fields(s ...googleapi.Field) *PropertiesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDeleteCall) Header ¶
func (c *PropertiesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesDisplayVideo360AdvertiserLinkProposalsApproveCall ¶
added in v0.51.0
type PropertiesDisplayVideo360AdvertiserLinkProposalsApproveCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDisplayVideo360AdvertiserLinkProposalsApproveCall) Context ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsApproveCall) Context(ctx context.Context) *PropertiesDisplayVideo360AdvertiserLinkProposalsApproveCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDisplayVideo360AdvertiserLinkProposalsApproveCall) Do ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsApproveCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaApproveDisplayVideo360AdvertiserLinkProposalResponse, error)

Do executes the "analyticsadmin.properties.displayVideo360AdvertiserLinkProposals.approve" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaApproveDisplayVideo360AdvertiserLinkProposalRespo nse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDisplayVideo360AdvertiserLinkProposalsApproveCall) Fields ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsApproveCall) Fields(s ...googleapi.Field) *PropertiesDisplayVideo360AdvertiserLinkProposalsApproveCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDisplayVideo360AdvertiserLinkProposalsApproveCall) Header ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsApproveCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesDisplayVideo360AdvertiserLinkProposalsCancelCall ¶
added in v0.51.0
type PropertiesDisplayVideo360AdvertiserLinkProposalsCancelCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDisplayVideo360AdvertiserLinkProposalsCancelCall) Context ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsCancelCall) Context(ctx context.Context) *PropertiesDisplayVideo360AdvertiserLinkProposalsCancelCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDisplayVideo360AdvertiserLinkProposalsCancelCall) Do ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsCancelCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal, error)

Do executes the "analyticsadmin.properties.displayVideo360AdvertiserLinkProposals.cancel" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal.ServerRespo nse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDisplayVideo360AdvertiserLinkProposalsCancelCall) Fields ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsCancelCall) Fields(s ...googleapi.Field) *PropertiesDisplayVideo360AdvertiserLinkProposalsCancelCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDisplayVideo360AdvertiserLinkProposalsCancelCall) Header ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsCancelCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesDisplayVideo360AdvertiserLinkProposalsCreateCall ¶
added in v0.51.0
type PropertiesDisplayVideo360AdvertiserLinkProposalsCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDisplayVideo360AdvertiserLinkProposalsCreateCall) Context ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsCreateCall) Context(ctx context.Context) *PropertiesDisplayVideo360AdvertiserLinkProposalsCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDisplayVideo360AdvertiserLinkProposalsCreateCall) Do ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal, error)

Do executes the "analyticsadmin.properties.displayVideo360AdvertiserLinkProposals.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal.ServerRespo nse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDisplayVideo360AdvertiserLinkProposalsCreateCall) Fields ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsCreateCall) Fields(s ...googleapi.Field) *PropertiesDisplayVideo360AdvertiserLinkProposalsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDisplayVideo360AdvertiserLinkProposalsCreateCall) Header ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesDisplayVideo360AdvertiserLinkProposalsDeleteCall ¶
added in v0.51.0
type PropertiesDisplayVideo360AdvertiserLinkProposalsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDisplayVideo360AdvertiserLinkProposalsDeleteCall) Context ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsDeleteCall) Context(ctx context.Context) *PropertiesDisplayVideo360AdvertiserLinkProposalsDeleteCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDisplayVideo360AdvertiserLinkProposalsDeleteCall) Do ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.properties.displayVideo360AdvertiserLinkProposals.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDisplayVideo360AdvertiserLinkProposalsDeleteCall) Fields ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsDeleteCall) Fields(s ...googleapi.Field) *PropertiesDisplayVideo360AdvertiserLinkProposalsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDisplayVideo360AdvertiserLinkProposalsDeleteCall) Header ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesDisplayVideo360AdvertiserLinkProposalsGetCall ¶
added in v0.51.0
type PropertiesDisplayVideo360AdvertiserLinkProposalsGetCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDisplayVideo360AdvertiserLinkProposalsGetCall) Context ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsGetCall) Context(ctx context.Context) *PropertiesDisplayVideo360AdvertiserLinkProposalsGetCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDisplayVideo360AdvertiserLinkProposalsGetCall) Do ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal, error)

Do executes the "analyticsadmin.properties.displayVideo360AdvertiserLinkProposals.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal.ServerRespo nse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDisplayVideo360AdvertiserLinkProposalsGetCall) Fields ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsGetCall) Fields(s ...googleapi.Field) *PropertiesDisplayVideo360AdvertiserLinkProposalsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDisplayVideo360AdvertiserLinkProposalsGetCall) Header ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesDisplayVideo360AdvertiserLinkProposalsGetCall) IfNoneMatch ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsGetCall) IfNoneMatch(entityTag string) *PropertiesDisplayVideo360AdvertiserLinkProposalsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesDisplayVideo360AdvertiserLinkProposalsListCall ¶
added in v0.51.0
type PropertiesDisplayVideo360AdvertiserLinkProposalsListCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDisplayVideo360AdvertiserLinkProposalsListCall) Context ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsListCall) Context(ctx context.Context) *PropertiesDisplayVideo360AdvertiserLinkProposalsListCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDisplayVideo360AdvertiserLinkProposalsListCall) Do ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinkProposalsResponse, error)

Do executes the "analyticsadmin.properties.displayVideo360AdvertiserLinkProposals.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinkProposalsRespons e.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDisplayVideo360AdvertiserLinkProposalsListCall) Fields ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsListCall) Fields(s ...googleapi.Field) *PropertiesDisplayVideo360AdvertiserLinkProposalsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDisplayVideo360AdvertiserLinkProposalsListCall) Header ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesDisplayVideo360AdvertiserLinkProposalsListCall) IfNoneMatch ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsListCall) IfNoneMatch(entityTag string) *PropertiesDisplayVideo360AdvertiserLinkProposalsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesDisplayVideo360AdvertiserLinkProposalsListCall) PageSize ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsListCall) PageSize(pageSize int64) *PropertiesDisplayVideo360AdvertiserLinkProposalsListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. If unspecified, at most 50 resources will be returned. The maximum value is 200 (higher values will be coerced to the maximum).

func (*PropertiesDisplayVideo360AdvertiserLinkProposalsListCall) PageToken ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsListCall) PageToken(pageToken string) *PropertiesDisplayVideo360AdvertiserLinkProposalsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListDisplayVideo360AdvertiserLinkProposals` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListDisplayVideo360AdvertiserLinkProposals` must match the call that provided the page token.

func (*PropertiesDisplayVideo360AdvertiserLinkProposalsListCall) Pages ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinkProposalsListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinkProposalsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesDisplayVideo360AdvertiserLinkProposalsService ¶
added in v0.51.0
type PropertiesDisplayVideo360AdvertiserLinkProposalsService struct {
	// contains filtered or unexported fields
}
func NewPropertiesDisplayVideo360AdvertiserLinkProposalsService ¶
added in v0.51.0
func NewPropertiesDisplayVideo360AdvertiserLinkProposalsService(s *Service) *PropertiesDisplayVideo360AdvertiserLinkProposalsService
func (*PropertiesDisplayVideo360AdvertiserLinkProposalsService) Approve ¶
added in v0.51.0
func (r *PropertiesDisplayVideo360AdvertiserLinkProposalsService) Approve(name string, googleanalyticsadminv1alphaapprovedisplayvideo360advertiserlinkproposalrequest *GoogleAnalyticsAdminV1alphaApproveDisplayVideo360AdvertiserLinkProposalRequest) *PropertiesDisplayVideo360AdvertiserLinkProposalsApproveCall

Approve: Approves a DisplayVideo360AdvertiserLinkProposal. The DisplayVideo360AdvertiserLinkProposal will be deleted and a new DisplayVideo360AdvertiserLink will be created.

name: The name of the DisplayVideo360AdvertiserLinkProposal to approve. Example format: properties/1234/displayVideo360AdvertiserLinkProposals/5678.
func (*PropertiesDisplayVideo360AdvertiserLinkProposalsService) Cancel ¶
added in v0.51.0
func (r *PropertiesDisplayVideo360AdvertiserLinkProposalsService) Cancel(name string, googleanalyticsadminv1alphacanceldisplayvideo360advertiserlinkproposalrequest *GoogleAnalyticsAdminV1alphaCancelDisplayVideo360AdvertiserLinkProposalRequest) *PropertiesDisplayVideo360AdvertiserLinkProposalsCancelCall

Cancel: Cancels a DisplayVideo360AdvertiserLinkProposal. Cancelling can mean either: - Declining a proposal initiated from Display & Video 360 - Withdrawing a proposal initiated from Google Analytics After being cancelled, a proposal will eventually be deleted automatically.

name: The name of the DisplayVideo360AdvertiserLinkProposal to cancel. Example format: properties/1234/displayVideo360AdvertiserLinkProposals/5678.
func (*PropertiesDisplayVideo360AdvertiserLinkProposalsService) Create ¶
added in v0.51.0
func (r *PropertiesDisplayVideo360AdvertiserLinkProposalsService) Create(parent string, googleanalyticsadminv1alphadisplayvideo360advertiserlinkproposal *GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal) *PropertiesDisplayVideo360AdvertiserLinkProposalsCreateCall

Create: Creates a DisplayVideo360AdvertiserLinkProposal.

- parent: Example format: properties/1234.

func (*PropertiesDisplayVideo360AdvertiserLinkProposalsService) Delete ¶
added in v0.51.0
func (r *PropertiesDisplayVideo360AdvertiserLinkProposalsService) Delete(name string) *PropertiesDisplayVideo360AdvertiserLinkProposalsDeleteCall

Delete: Deletes a DisplayVideo360AdvertiserLinkProposal on a property. This can only be used on cancelled proposals.

name: The name of the DisplayVideo360AdvertiserLinkProposal to delete. Example format: properties/1234/displayVideo360AdvertiserLinkProposals/5678.
func (*PropertiesDisplayVideo360AdvertiserLinkProposalsService) Get ¶
added in v0.51.0
func (r *PropertiesDisplayVideo360AdvertiserLinkProposalsService) Get(name string) *PropertiesDisplayVideo360AdvertiserLinkProposalsGetCall

Get: Lookup for a single DisplayVideo360AdvertiserLinkProposal.

name: The name of the DisplayVideo360AdvertiserLinkProposal to get. Example format: properties/1234/displayVideo360AdvertiserLinkProposals/5678.
func (*PropertiesDisplayVideo360AdvertiserLinkProposalsService) List ¶
added in v0.51.0
func (r *PropertiesDisplayVideo360AdvertiserLinkProposalsService) List(parent string) *PropertiesDisplayVideo360AdvertiserLinkProposalsListCall

List: Lists DisplayVideo360AdvertiserLinkProposals on a property.

- parent: Example format: properties/1234.

type PropertiesDisplayVideo360AdvertiserLinksCreateCall ¶
added in v0.51.0
type PropertiesDisplayVideo360AdvertiserLinksCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDisplayVideo360AdvertiserLinksCreateCall) Context ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinksCreateCall) Context(ctx context.Context) *PropertiesDisplayVideo360AdvertiserLinksCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDisplayVideo360AdvertiserLinksCreateCall) Do ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinksCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink, error)

Do executes the "analyticsadmin.properties.displayVideo360AdvertiserLinks.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink.ServerResponse.Head er or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDisplayVideo360AdvertiserLinksCreateCall) Fields ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinksCreateCall) Fields(s ...googleapi.Field) *PropertiesDisplayVideo360AdvertiserLinksCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDisplayVideo360AdvertiserLinksCreateCall) Header ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinksCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesDisplayVideo360AdvertiserLinksDeleteCall ¶
added in v0.51.0
type PropertiesDisplayVideo360AdvertiserLinksDeleteCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDisplayVideo360AdvertiserLinksDeleteCall) Context ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinksDeleteCall) Context(ctx context.Context) *PropertiesDisplayVideo360AdvertiserLinksDeleteCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDisplayVideo360AdvertiserLinksDeleteCall) Do ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinksDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.properties.displayVideo360AdvertiserLinks.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDisplayVideo360AdvertiserLinksDeleteCall) Fields ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinksDeleteCall) Fields(s ...googleapi.Field) *PropertiesDisplayVideo360AdvertiserLinksDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDisplayVideo360AdvertiserLinksDeleteCall) Header ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinksDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesDisplayVideo360AdvertiserLinksGetCall ¶
added in v0.51.0
type PropertiesDisplayVideo360AdvertiserLinksGetCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDisplayVideo360AdvertiserLinksGetCall) Context ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinksGetCall) Context(ctx context.Context) *PropertiesDisplayVideo360AdvertiserLinksGetCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDisplayVideo360AdvertiserLinksGetCall) Do ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinksGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink, error)

Do executes the "analyticsadmin.properties.displayVideo360AdvertiserLinks.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink.ServerResponse.Head er or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDisplayVideo360AdvertiserLinksGetCall) Fields ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinksGetCall) Fields(s ...googleapi.Field) *PropertiesDisplayVideo360AdvertiserLinksGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDisplayVideo360AdvertiserLinksGetCall) Header ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinksGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesDisplayVideo360AdvertiserLinksGetCall) IfNoneMatch ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinksGetCall) IfNoneMatch(entityTag string) *PropertiesDisplayVideo360AdvertiserLinksGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesDisplayVideo360AdvertiserLinksListCall ¶
added in v0.51.0
type PropertiesDisplayVideo360AdvertiserLinksListCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDisplayVideo360AdvertiserLinksListCall) Context ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinksListCall) Context(ctx context.Context) *PropertiesDisplayVideo360AdvertiserLinksListCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDisplayVideo360AdvertiserLinksListCall) Do ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinksListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinksResponse, error)

Do executes the "analyticsadmin.properties.displayVideo360AdvertiserLinks.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinksResponse.Server Response.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDisplayVideo360AdvertiserLinksListCall) Fields ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinksListCall) Fields(s ...googleapi.Field) *PropertiesDisplayVideo360AdvertiserLinksListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDisplayVideo360AdvertiserLinksListCall) Header ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinksListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesDisplayVideo360AdvertiserLinksListCall) IfNoneMatch ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinksListCall) IfNoneMatch(entityTag string) *PropertiesDisplayVideo360AdvertiserLinksListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesDisplayVideo360AdvertiserLinksListCall) PageSize ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinksListCall) PageSize(pageSize int64) *PropertiesDisplayVideo360AdvertiserLinksListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. If unspecified, at most 50 resources will be returned. The maximum value is 200 (higher values will be coerced to the maximum).

func (*PropertiesDisplayVideo360AdvertiserLinksListCall) PageToken ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinksListCall) PageToken(pageToken string) *PropertiesDisplayVideo360AdvertiserLinksListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListDisplayVideo360AdvertiserLinks` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListDisplayVideo360AdvertiserLinks` must match the call that provided the page token.

func (*PropertiesDisplayVideo360AdvertiserLinksListCall) Pages ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinksListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinksResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesDisplayVideo360AdvertiserLinksPatchCall ¶
added in v0.51.0
type PropertiesDisplayVideo360AdvertiserLinksPatchCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesDisplayVideo360AdvertiserLinksPatchCall) Context ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinksPatchCall) Context(ctx context.Context) *PropertiesDisplayVideo360AdvertiserLinksPatchCall

Context sets the context to be used in this call's Do method.

func (*PropertiesDisplayVideo360AdvertiserLinksPatchCall) Do ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinksPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink, error)

Do executes the "analyticsadmin.properties.displayVideo360AdvertiserLinks.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink.ServerResponse.Head er or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesDisplayVideo360AdvertiserLinksPatchCall) Fields ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinksPatchCall) Fields(s ...googleapi.Field) *PropertiesDisplayVideo360AdvertiserLinksPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesDisplayVideo360AdvertiserLinksPatchCall) Header ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinksPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesDisplayVideo360AdvertiserLinksPatchCall) UpdateMask ¶
added in v0.51.0
func (c *PropertiesDisplayVideo360AdvertiserLinksPatchCall) UpdateMask(updateMask string) *PropertiesDisplayVideo360AdvertiserLinksPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated. Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.

type PropertiesDisplayVideo360AdvertiserLinksService ¶
added in v0.51.0
type PropertiesDisplayVideo360AdvertiserLinksService struct {
	// contains filtered or unexported fields
}
func NewPropertiesDisplayVideo360AdvertiserLinksService ¶
added in v0.51.0
func NewPropertiesDisplayVideo360AdvertiserLinksService(s *Service) *PropertiesDisplayVideo360AdvertiserLinksService
func (*PropertiesDisplayVideo360AdvertiserLinksService) Create ¶
added in v0.51.0
func (r *PropertiesDisplayVideo360AdvertiserLinksService) Create(parent string, googleanalyticsadminv1alphadisplayvideo360advertiserlink *GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink) *PropertiesDisplayVideo360AdvertiserLinksCreateCall

Create: Creates a DisplayVideo360AdvertiserLink. This can only be utilized by users who have proper authorization both on the Google Analytics property and on the Display & Video 360 advertiser. Users who do not have access to the Display & Video 360 advertiser should instead seek to create a DisplayVideo360LinkProposal.

- parent: Example format: properties/1234.

func (*PropertiesDisplayVideo360AdvertiserLinksService) Delete ¶
added in v0.51.0
func (r *PropertiesDisplayVideo360AdvertiserLinksService) Delete(name string) *PropertiesDisplayVideo360AdvertiserLinksDeleteCall

Delete: Deletes a DisplayVideo360AdvertiserLink on a property.

name: The name of the DisplayVideo360AdvertiserLink to delete. Example format: properties/1234/displayVideo360AdvertiserLinks/5678.
func (*PropertiesDisplayVideo360AdvertiserLinksService) Get ¶
added in v0.51.0
func (r *PropertiesDisplayVideo360AdvertiserLinksService) Get(name string) *PropertiesDisplayVideo360AdvertiserLinksGetCall

Get: Look up a single DisplayVideo360AdvertiserLink

name: The name of the DisplayVideo360AdvertiserLink to get. Example format: properties/1234/displayVideo360AdvertiserLink/5678.
func (*PropertiesDisplayVideo360AdvertiserLinksService) List ¶
added in v0.51.0
func (r *PropertiesDisplayVideo360AdvertiserLinksService) List(parent string) *PropertiesDisplayVideo360AdvertiserLinksListCall

List: Lists all DisplayVideo360AdvertiserLinks on a property.

- parent: Example format: properties/1234.

func (*PropertiesDisplayVideo360AdvertiserLinksService) Patch ¶
added in v0.51.0
func (r *PropertiesDisplayVideo360AdvertiserLinksService) Patch(name string, googleanalyticsadminv1alphadisplayvideo360advertiserlink *GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink) *PropertiesDisplayVideo360AdvertiserLinksPatchCall

Patch: Updates a DisplayVideo360AdvertiserLink on a property.

name: Output only. The resource name for this DisplayVideo360AdvertiserLink resource. Format: properties/{propertyId}/displayVideo360AdvertiserLinks/{linkId} Note: linkId is not the Display & Video 360 Advertiser ID.
type PropertiesExpandedDataSetsCreateCall ¶
added in v0.111.0
type PropertiesExpandedDataSetsCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesExpandedDataSetsCreateCall) Context ¶
added in v0.111.0
func (c *PropertiesExpandedDataSetsCreateCall) Context(ctx context.Context) *PropertiesExpandedDataSetsCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesExpandedDataSetsCreateCall) Do ¶
added in v0.111.0
func (c *PropertiesExpandedDataSetsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaExpandedDataSet, error)

Do executes the "analyticsadmin.properties.expandedDataSets.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaExpandedDataSet.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesExpandedDataSetsCreateCall) Fields ¶
added in v0.111.0
func (c *PropertiesExpandedDataSetsCreateCall) Fields(s ...googleapi.Field) *PropertiesExpandedDataSetsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesExpandedDataSetsCreateCall) Header ¶
added in v0.111.0
func (c *PropertiesExpandedDataSetsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesExpandedDataSetsDeleteCall ¶
added in v0.111.0
type PropertiesExpandedDataSetsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesExpandedDataSetsDeleteCall) Context ¶
added in v0.111.0
func (c *PropertiesExpandedDataSetsDeleteCall) Context(ctx context.Context) *PropertiesExpandedDataSetsDeleteCall

Context sets the context to be used in this call's Do method.

func (*PropertiesExpandedDataSetsDeleteCall) Do ¶
added in v0.111.0
func (c *PropertiesExpandedDataSetsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.properties.expandedDataSets.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesExpandedDataSetsDeleteCall) Fields ¶
added in v0.111.0
func (c *PropertiesExpandedDataSetsDeleteCall) Fields(s ...googleapi.Field) *PropertiesExpandedDataSetsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesExpandedDataSetsDeleteCall) Header ¶
added in v0.111.0
func (c *PropertiesExpandedDataSetsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesExpandedDataSetsGetCall ¶
added in v0.111.0
type PropertiesExpandedDataSetsGetCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesExpandedDataSetsGetCall) Context ¶
added in v0.111.0
func (c *PropertiesExpandedDataSetsGetCall) Context(ctx context.Context) *PropertiesExpandedDataSetsGetCall

Context sets the context to be used in this call's Do method.

func (*PropertiesExpandedDataSetsGetCall) Do ¶
added in v0.111.0
func (c *PropertiesExpandedDataSetsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaExpandedDataSet, error)

Do executes the "analyticsadmin.properties.expandedDataSets.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaExpandedDataSet.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesExpandedDataSetsGetCall) Fields ¶
added in v0.111.0
func (c *PropertiesExpandedDataSetsGetCall) Fields(s ...googleapi.Field) *PropertiesExpandedDataSetsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesExpandedDataSetsGetCall) Header ¶
added in v0.111.0
func (c *PropertiesExpandedDataSetsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesExpandedDataSetsGetCall) IfNoneMatch ¶
added in v0.111.0
func (c *PropertiesExpandedDataSetsGetCall) IfNoneMatch(entityTag string) *PropertiesExpandedDataSetsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesExpandedDataSetsListCall ¶
added in v0.111.0
type PropertiesExpandedDataSetsListCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesExpandedDataSetsListCall) Context ¶
added in v0.111.0
func (c *PropertiesExpandedDataSetsListCall) Context(ctx context.Context) *PropertiesExpandedDataSetsListCall

Context sets the context to be used in this call's Do method.

func (*PropertiesExpandedDataSetsListCall) Do ¶
added in v0.111.0
func (c *PropertiesExpandedDataSetsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListExpandedDataSetsResponse, error)

Do executes the "analyticsadmin.properties.expandedDataSets.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaListExpandedDataSetsResponse.ServerResponse.Heade r or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesExpandedDataSetsListCall) Fields ¶
added in v0.111.0
func (c *PropertiesExpandedDataSetsListCall) Fields(s ...googleapi.Field) *PropertiesExpandedDataSetsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesExpandedDataSetsListCall) Header ¶
added in v0.111.0
func (c *PropertiesExpandedDataSetsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesExpandedDataSetsListCall) IfNoneMatch ¶
added in v0.111.0
func (c *PropertiesExpandedDataSetsListCall) IfNoneMatch(entityTag string) *PropertiesExpandedDataSetsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesExpandedDataSetsListCall) PageSize ¶
added in v0.111.0
func (c *PropertiesExpandedDataSetsListCall) PageSize(pageSize int64) *PropertiesExpandedDataSetsListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. If unspecified, at most 50 resources will be returned. The maximum value is 200 (higher values will be coerced to the maximum).

func (*PropertiesExpandedDataSetsListCall) PageToken ¶
added in v0.111.0
func (c *PropertiesExpandedDataSetsListCall) PageToken(pageToken string) *PropertiesExpandedDataSetsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListExpandedDataSets` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListExpandedDataSet` must match the call that provided the page token.

func (*PropertiesExpandedDataSetsListCall) Pages ¶
added in v0.111.0
func (c *PropertiesExpandedDataSetsListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1alphaListExpandedDataSetsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesExpandedDataSetsPatchCall ¶
added in v0.111.0
type PropertiesExpandedDataSetsPatchCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesExpandedDataSetsPatchCall) Context ¶
added in v0.111.0
func (c *PropertiesExpandedDataSetsPatchCall) Context(ctx context.Context) *PropertiesExpandedDataSetsPatchCall

Context sets the context to be used in this call's Do method.

func (*PropertiesExpandedDataSetsPatchCall) Do ¶
added in v0.111.0
func (c *PropertiesExpandedDataSetsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaExpandedDataSet, error)

Do executes the "analyticsadmin.properties.expandedDataSets.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaExpandedDataSet.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesExpandedDataSetsPatchCall) Fields ¶
added in v0.111.0
func (c *PropertiesExpandedDataSetsPatchCall) Fields(s ...googleapi.Field) *PropertiesExpandedDataSetsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesExpandedDataSetsPatchCall) Header ¶
added in v0.111.0
func (c *PropertiesExpandedDataSetsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesExpandedDataSetsPatchCall) UpdateMask ¶
added in v0.111.0
func (c *PropertiesExpandedDataSetsPatchCall) UpdateMask(updateMask string) *PropertiesExpandedDataSetsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated. Field names must be in snake case (e.g., "field_to_update"). Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.

type PropertiesExpandedDataSetsService ¶
added in v0.111.0
type PropertiesExpandedDataSetsService struct {
	// contains filtered or unexported fields
}
func NewPropertiesExpandedDataSetsService ¶
added in v0.111.0
func NewPropertiesExpandedDataSetsService(s *Service) *PropertiesExpandedDataSetsService
func (*PropertiesExpandedDataSetsService) Create ¶
added in v0.111.0
func (r *PropertiesExpandedDataSetsService) Create(parent string, googleanalyticsadminv1alphaexpandeddataset *GoogleAnalyticsAdminV1alphaExpandedDataSet) *PropertiesExpandedDataSetsCreateCall

Create: Creates a ExpandedDataSet.

- parent: Example format: properties/1234.

func (*PropertiesExpandedDataSetsService) Delete ¶
added in v0.111.0
func (r *PropertiesExpandedDataSetsService) Delete(name string) *PropertiesExpandedDataSetsDeleteCall

Delete: Deletes a ExpandedDataSet on a property.

- name: Example format: properties/1234/expandedDataSets/5678.

func (*PropertiesExpandedDataSetsService) Get ¶
added in v0.111.0
func (r *PropertiesExpandedDataSetsService) Get(name string) *PropertiesExpandedDataSetsGetCall

Get: Lookup for a single ExpandedDataSet.

name: The name of the ExpandedDataSet to get. Example format: properties/1234/expandedDataSets/5678.
func (*PropertiesExpandedDataSetsService) List ¶
added in v0.111.0
func (r *PropertiesExpandedDataSetsService) List(parent string) *PropertiesExpandedDataSetsListCall

List: Lists ExpandedDataSets on a property.

- parent: Example format: properties/1234.

func (*PropertiesExpandedDataSetsService) Patch ¶
added in v0.111.0
func (r *PropertiesExpandedDataSetsService) Patch(name string, googleanalyticsadminv1alphaexpandeddataset *GoogleAnalyticsAdminV1alphaExpandedDataSet) *PropertiesExpandedDataSetsPatchCall

Patch: Updates a ExpandedDataSet on a property.

name: Output only. The resource name for this ExpandedDataSet resource. Format: properties/{property_id}/expandedDataSets/{expanded_data_set}.
type PropertiesFirebaseLinksCreateCall ¶
type PropertiesFirebaseLinksCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesFirebaseLinksCreateCall) Context ¶
func (c *PropertiesFirebaseLinksCreateCall) Context(ctx context.Context) *PropertiesFirebaseLinksCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesFirebaseLinksCreateCall) Do ¶
func (c *PropertiesFirebaseLinksCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaFirebaseLink, error)

Do executes the "analyticsadmin.properties.firebaseLinks.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaFirebaseLink.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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
func (c *PropertiesFirebaseLinksListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListFirebaseLinksResponse, error)

Do executes the "analyticsadmin.properties.firebaseLinks.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaListFirebaseLinksResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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
added in v0.37.0
func (c *PropertiesFirebaseLinksListCall) PageSize(pageSize int64) *PropertiesFirebaseLinksListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. The service may return fewer than this value, even if there are additional pages. If unspecified, at most 50 resources will be returned. The maximum value is 200; (higher values will be coerced to the maximum)

func (*PropertiesFirebaseLinksListCall) PageToken ¶
added in v0.37.0
func (c *PropertiesFirebaseLinksListCall) PageToken(pageToken string) *PropertiesFirebaseLinksListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListFirebaseLinks` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListFirebaseLinks` must match the call that provided the page token.

func (*PropertiesFirebaseLinksListCall) Pages ¶
added in v0.37.0
func (c *PropertiesFirebaseLinksListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1alphaListFirebaseLinksResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesFirebaseLinksService ¶
type PropertiesFirebaseLinksService struct {
	// contains filtered or unexported fields
}
func NewPropertiesFirebaseLinksService ¶
func NewPropertiesFirebaseLinksService(s *Service) *PropertiesFirebaseLinksService
func (*PropertiesFirebaseLinksService) Create ¶
func (r *PropertiesFirebaseLinksService) Create(parent string, googleanalyticsadminv1alphafirebaselink *GoogleAnalyticsAdminV1alphaFirebaseLink) *PropertiesFirebaseLinksCreateCall

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

type PropertiesGetAttributionSettingsCall ¶
added in v0.84.0
type PropertiesGetAttributionSettingsCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesGetAttributionSettingsCall) Context ¶
added in v0.84.0
func (c *PropertiesGetAttributionSettingsCall) Context(ctx context.Context) *PropertiesGetAttributionSettingsCall

Context sets the context to be used in this call's Do method.

func (*PropertiesGetAttributionSettingsCall) Do ¶
added in v0.84.0
func (c *PropertiesGetAttributionSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAttributionSettings, error)

Do executes the "analyticsadmin.properties.getAttributionSettings" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaAttributionSettings.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesGetAttributionSettingsCall) Fields ¶
added in v0.84.0
func (c *PropertiesGetAttributionSettingsCall) Fields(s ...googleapi.Field) *PropertiesGetAttributionSettingsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesGetAttributionSettingsCall) Header ¶
added in v0.84.0
func (c *PropertiesGetAttributionSettingsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesGetAttributionSettingsCall) IfNoneMatch ¶
added in v0.84.0
func (c *PropertiesGetAttributionSettingsCall) IfNoneMatch(entityTag string) *PropertiesGetAttributionSettingsCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesGetCall ¶
type PropertiesGetCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesGetCall) Context ¶
func (c *PropertiesGetCall) Context(ctx context.Context) *PropertiesGetCall

Context sets the context to be used in this call's Do method.

func (*PropertiesGetCall) Do ¶
func (c *PropertiesGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaProperty, error)

Do executes the "analyticsadmin.properties.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaProperty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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
added in v0.55.0
type PropertiesGetDataRetentionSettingsCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesGetDataRetentionSettingsCall) Context ¶
added in v0.55.0
func (c *PropertiesGetDataRetentionSettingsCall) Context(ctx context.Context) *PropertiesGetDataRetentionSettingsCall

Context sets the context to be used in this call's Do method.

func (*PropertiesGetDataRetentionSettingsCall) Do ¶
added in v0.55.0
func (c *PropertiesGetDataRetentionSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaDataRetentionSettings, error)

Do executes the "analyticsadmin.properties.getDataRetentionSettings" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaDataRetentionSettings.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesGetDataRetentionSettingsCall) Fields ¶
added in v0.55.0
func (c *PropertiesGetDataRetentionSettingsCall) Fields(s ...googleapi.Field) *PropertiesGetDataRetentionSettingsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesGetDataRetentionSettingsCall) Header ¶
added in v0.55.0
func (c *PropertiesGetDataRetentionSettingsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesGetDataRetentionSettingsCall) IfNoneMatch ¶
added in v0.55.0
func (c *PropertiesGetDataRetentionSettingsCall) IfNoneMatch(entityTag string) *PropertiesGetDataRetentionSettingsCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesGetGoogleSignalsSettingsCall ¶
added in v0.47.0
type PropertiesGetGoogleSignalsSettingsCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesGetGoogleSignalsSettingsCall) Context ¶
added in v0.47.0
func (c *PropertiesGetGoogleSignalsSettingsCall) Context(ctx context.Context) *PropertiesGetGoogleSignalsSettingsCall

Context sets the context to be used in this call's Do method.

func (*PropertiesGetGoogleSignalsSettingsCall) Do ¶
added in v0.47.0
func (c *PropertiesGetGoogleSignalsSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaGoogleSignalsSettings, error)

Do executes the "analyticsadmin.properties.getGoogleSignalsSettings" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaGoogleSignalsSettings.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesGetGoogleSignalsSettingsCall) Fields ¶
added in v0.47.0
func (c *PropertiesGetGoogleSignalsSettingsCall) Fields(s ...googleapi.Field) *PropertiesGetGoogleSignalsSettingsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesGetGoogleSignalsSettingsCall) Header ¶
added in v0.47.0
func (c *PropertiesGetGoogleSignalsSettingsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesGetGoogleSignalsSettingsCall) IfNoneMatch ¶
added in v0.47.0
func (c *PropertiesGetGoogleSignalsSettingsCall) IfNoneMatch(entityTag string) *PropertiesGetGoogleSignalsSettingsCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesGetReportingIdentitySettingsCall ¶
added in v0.240.0
type PropertiesGetReportingIdentitySettingsCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesGetReportingIdentitySettingsCall) Context ¶
added in v0.240.0
func (c *PropertiesGetReportingIdentitySettingsCall) Context(ctx context.Context) *PropertiesGetReportingIdentitySettingsCall

Context sets the context to be used in this call's Do method.

func (*PropertiesGetReportingIdentitySettingsCall) Do ¶
added in v0.240.0
func (c *PropertiesGetReportingIdentitySettingsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaReportingIdentitySettings, error)

Do executes the "analyticsadmin.properties.getReportingIdentitySettings" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaReportingIdentitySettings.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesGetReportingIdentitySettingsCall) Fields ¶
added in v0.240.0
func (c *PropertiesGetReportingIdentitySettingsCall) Fields(s ...googleapi.Field) *PropertiesGetReportingIdentitySettingsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesGetReportingIdentitySettingsCall) Header ¶
added in v0.240.0
func (c *PropertiesGetReportingIdentitySettingsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesGetReportingIdentitySettingsCall) IfNoneMatch ¶
added in v0.240.0
func (c *PropertiesGetReportingIdentitySettingsCall) IfNoneMatch(entityTag string) *PropertiesGetReportingIdentitySettingsCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesGoogleAdsLinksCreateCall ¶
type PropertiesGoogleAdsLinksCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesGoogleAdsLinksCreateCall) Context ¶
func (c *PropertiesGoogleAdsLinksCreateCall) Context(ctx context.Context) *PropertiesGoogleAdsLinksCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesGoogleAdsLinksCreateCall) Do ¶
func (c *PropertiesGoogleAdsLinksCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaGoogleAdsLink, error)

Do executes the "analyticsadmin.properties.googleAdsLinks.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaGoogleAdsLink.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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
func (c *PropertiesGoogleAdsLinksListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListGoogleAdsLinksResponse, error)

Do executes the "analyticsadmin.properties.googleAdsLinks.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaListGoogleAdsLinksResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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
func (c *PropertiesGoogleAdsLinksListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1alphaListGoogleAdsLinksResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesGoogleAdsLinksPatchCall ¶
type PropertiesGoogleAdsLinksPatchCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesGoogleAdsLinksPatchCall) Context ¶
func (c *PropertiesGoogleAdsLinksPatchCall) Context(ctx context.Context) *PropertiesGoogleAdsLinksPatchCall

Context sets the context to be used in this call's Do method.

func (*PropertiesGoogleAdsLinksPatchCall) Do ¶
func (c *PropertiesGoogleAdsLinksPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaGoogleAdsLink, error)

Do executes the "analyticsadmin.properties.googleAdsLinks.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaGoogleAdsLink.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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
func (r *PropertiesGoogleAdsLinksService) Create(parent string, googleanalyticsadminv1alphagoogleadslink *GoogleAnalyticsAdminV1alphaGoogleAdsLink) *PropertiesGoogleAdsLinksCreateCall

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
func (r *PropertiesGoogleAdsLinksService) Patch(name string, googleanalyticsadminv1alphagoogleadslink *GoogleAnalyticsAdminV1alphaGoogleAdsLink) *PropertiesGoogleAdsLinksPatchCall

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
func (c *PropertiesKeyEventsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaKeyEvent, error)

Do executes the "analyticsadmin.properties.keyEvents.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaKeyEvent.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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
func (c *PropertiesKeyEventsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaKeyEvent, error)

Do executes the "analyticsadmin.properties.keyEvents.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaKeyEvent.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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
func (c *PropertiesKeyEventsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListKeyEventsResponse, error)

Do executes the "analyticsadmin.properties.keyEvents.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaListKeyEventsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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
func (c *PropertiesKeyEventsListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1alphaListKeyEventsResponse) error) error

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
func (c *PropertiesKeyEventsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaKeyEvent, error)

Do executes the "analyticsadmin.properties.keyEvents.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaKeyEvent.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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
func (r *PropertiesKeyEventsService) Create(parent string, googleanalyticsadminv1alphakeyevent *GoogleAnalyticsAdminV1alphaKeyEvent) *PropertiesKeyEventsCreateCall

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
func (r *PropertiesKeyEventsService) Patch(name string, googleanalyticsadminv1alphakeyevent *GoogleAnalyticsAdminV1alphaKeyEvent) *PropertiesKeyEventsPatchCall

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
func (c *PropertiesListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListPropertiesResponse, error)

Do executes the "analyticsadmin.properties.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaListPropertiesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

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
func (c *PropertiesListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1alphaListPropertiesResponse) error) error

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
func (c *PropertiesPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaProperty, error)

Do executes the "analyticsadmin.properties.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaProperty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesPatchCall) Fields ¶
func (c *PropertiesPatchCall) Fields(s ...googleapi.Field) *PropertiesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesPatchCall) Header ¶
func (c *PropertiesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesPatchCall) UpdateMask ¶
func (c *PropertiesPatchCall) UpdateMask(updateMask string) *PropertiesPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated. Field names must be in snake case (e.g., "field_to_update"). Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.

type PropertiesProvisionSubpropertyCall ¶
added in v0.191.0
type PropertiesProvisionSubpropertyCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesProvisionSubpropertyCall) Context ¶
added in v0.191.0
func (c *PropertiesProvisionSubpropertyCall) Context(ctx context.Context) *PropertiesProvisionSubpropertyCall

Context sets the context to be used in this call's Do method.

func (*PropertiesProvisionSubpropertyCall) Do ¶
added in v0.191.0
func (c *PropertiesProvisionSubpropertyCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaProvisionSubpropertyResponse, error)

Do executes the "analyticsadmin.properties.provisionSubproperty" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaProvisionSubpropertyResponse.ServerResponse.Heade r or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesProvisionSubpropertyCall) Fields ¶
added in v0.191.0
func (c *PropertiesProvisionSubpropertyCall) Fields(s ...googleapi.Field) *PropertiesProvisionSubpropertyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesProvisionSubpropertyCall) Header ¶
added in v0.191.0
func (c *PropertiesProvisionSubpropertyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesReportingDataAnnotationsCreateCall ¶
added in v0.229.0
type PropertiesReportingDataAnnotationsCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesReportingDataAnnotationsCreateCall) Context ¶
added in v0.229.0
func (c *PropertiesReportingDataAnnotationsCreateCall) Context(ctx context.Context) *PropertiesReportingDataAnnotationsCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesReportingDataAnnotationsCreateCall) Do ¶
added in v0.229.0
func (c *PropertiesReportingDataAnnotationsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaReportingDataAnnotation, error)

Do executes the "analyticsadmin.properties.reportingDataAnnotations.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaReportingDataAnnotation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesReportingDataAnnotationsCreateCall) Fields ¶
added in v0.229.0
func (c *PropertiesReportingDataAnnotationsCreateCall) Fields(s ...googleapi.Field) *PropertiesReportingDataAnnotationsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesReportingDataAnnotationsCreateCall) Header ¶
added in v0.229.0
func (c *PropertiesReportingDataAnnotationsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesReportingDataAnnotationsDeleteCall ¶
added in v0.229.0
type PropertiesReportingDataAnnotationsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesReportingDataAnnotationsDeleteCall) Context ¶
added in v0.229.0
func (c *PropertiesReportingDataAnnotationsDeleteCall) Context(ctx context.Context) *PropertiesReportingDataAnnotationsDeleteCall

Context sets the context to be used in this call's Do method.

func (*PropertiesReportingDataAnnotationsDeleteCall) Do ¶
added in v0.229.0
func (c *PropertiesReportingDataAnnotationsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.properties.reportingDataAnnotations.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesReportingDataAnnotationsDeleteCall) Fields ¶
added in v0.229.0
func (c *PropertiesReportingDataAnnotationsDeleteCall) Fields(s ...googleapi.Field) *PropertiesReportingDataAnnotationsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesReportingDataAnnotationsDeleteCall) Header ¶
added in v0.229.0
func (c *PropertiesReportingDataAnnotationsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesReportingDataAnnotationsGetCall ¶
added in v0.229.0
type PropertiesReportingDataAnnotationsGetCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesReportingDataAnnotationsGetCall) Context ¶
added in v0.229.0
func (c *PropertiesReportingDataAnnotationsGetCall) Context(ctx context.Context) *PropertiesReportingDataAnnotationsGetCall

Context sets the context to be used in this call's Do method.

func (*PropertiesReportingDataAnnotationsGetCall) Do ¶
added in v0.229.0
func (c *PropertiesReportingDataAnnotationsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaReportingDataAnnotation, error)

Do executes the "analyticsadmin.properties.reportingDataAnnotations.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaReportingDataAnnotation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesReportingDataAnnotationsGetCall) Fields ¶
added in v0.229.0
func (c *PropertiesReportingDataAnnotationsGetCall) Fields(s ...googleapi.Field) *PropertiesReportingDataAnnotationsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesReportingDataAnnotationsGetCall) Header ¶
added in v0.229.0
func (c *PropertiesReportingDataAnnotationsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesReportingDataAnnotationsGetCall) IfNoneMatch ¶
added in v0.229.0
func (c *PropertiesReportingDataAnnotationsGetCall) IfNoneMatch(entityTag string) *PropertiesReportingDataAnnotationsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesReportingDataAnnotationsListCall ¶
added in v0.229.0
type PropertiesReportingDataAnnotationsListCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesReportingDataAnnotationsListCall) Context ¶
added in v0.229.0
func (c *PropertiesReportingDataAnnotationsListCall) Context(ctx context.Context) *PropertiesReportingDataAnnotationsListCall

Context sets the context to be used in this call's Do method.

func (*PropertiesReportingDataAnnotationsListCall) Do ¶
added in v0.229.0
func (c *PropertiesReportingDataAnnotationsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListReportingDataAnnotationsResponse, error)

Do executes the "analyticsadmin.properties.reportingDataAnnotations.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaListReportingDataAnnotationsResponse.ServerRespon se.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesReportingDataAnnotationsListCall) Fields ¶
added in v0.229.0
func (c *PropertiesReportingDataAnnotationsListCall) Fields(s ...googleapi.Field) *PropertiesReportingDataAnnotationsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesReportingDataAnnotationsListCall) Filter ¶
added in v0.229.0
func (c *PropertiesReportingDataAnnotationsListCall) Filter(filter string) *PropertiesReportingDataAnnotationsListCall

Filter sets the optional parameter "filter": Filter that restricts which reporting data annotations under the parent property are listed. Supported fields are: * 'name' * `title` * `description` * `annotation_date` * `annotation_date_range` * `color` Additionally, this API provides the following helper functions: * annotation_duration() : the duration that this annotation marks, durations (https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/duration.proto). expect a numeric representation of seconds followed by an `s` suffix. * is_annotation_in_range(start_date, end_date) : if the annotation is in the range specified by the `start_date` and `end_date`. The dates are in ISO-8601 format, for example `2031-06-28`. Supported operations: * `=` : equals * `!=` : not equals * `<` : less than * `>` : greater than * `<=` : less than or equals * `>=` : greater than or equals * `:` : has operator * `=~` : regular expression (https://github.com/google/re2/wiki/Syntax) match * `!~` : regular expression (https://github.com/google/re2/wiki/Syntax) does not match * `NOT` : Logical not * `AND` : Logical and * `OR` : Logical or Examples: 1. `title="Holiday Sale" 2. `description=~"[Bb]ig [Gg]ame.*[Ss]ale" 3. `is_annotation_in_range("2025-12-25", "2026-01-16") = true` 4. `annotation_duration() >= 172800s AND title:BOGO`

func (*PropertiesReportingDataAnnotationsListCall) Header ¶
added in v0.229.0
func (c *PropertiesReportingDataAnnotationsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesReportingDataAnnotationsListCall) IfNoneMatch ¶
added in v0.229.0
func (c *PropertiesReportingDataAnnotationsListCall) IfNoneMatch(entityTag string) *PropertiesReportingDataAnnotationsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesReportingDataAnnotationsListCall) PageSize ¶
added in v0.229.0
func (c *PropertiesReportingDataAnnotationsListCall) PageSize(pageSize int64) *PropertiesReportingDataAnnotationsListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. The service may return fewer than this value, even if there are additional pages. If unspecified, at most 50 resources will be returned. The maximum value is 200; (higher values will be coerced to the maximum)

func (*PropertiesReportingDataAnnotationsListCall) PageToken ¶
added in v0.229.0
func (c *PropertiesReportingDataAnnotationsListCall) PageToken(pageToken string) *PropertiesReportingDataAnnotationsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListReportingDataAnnotations` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListReportingDataAnnotations` must match the call that provided the page token.

func (*PropertiesReportingDataAnnotationsListCall) Pages ¶
added in v0.229.0
func (c *PropertiesReportingDataAnnotationsListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1alphaListReportingDataAnnotationsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesReportingDataAnnotationsPatchCall ¶
added in v0.229.0
type PropertiesReportingDataAnnotationsPatchCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesReportingDataAnnotationsPatchCall) Context ¶
added in v0.229.0
func (c *PropertiesReportingDataAnnotationsPatchCall) Context(ctx context.Context) *PropertiesReportingDataAnnotationsPatchCall

Context sets the context to be used in this call's Do method.

func (*PropertiesReportingDataAnnotationsPatchCall) Do ¶
added in v0.229.0
func (c *PropertiesReportingDataAnnotationsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaReportingDataAnnotation, error)

Do executes the "analyticsadmin.properties.reportingDataAnnotations.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaReportingDataAnnotation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesReportingDataAnnotationsPatchCall) Fields ¶
added in v0.229.0
func (c *PropertiesReportingDataAnnotationsPatchCall) Fields(s ...googleapi.Field) *PropertiesReportingDataAnnotationsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesReportingDataAnnotationsPatchCall) Header ¶
added in v0.229.0
func (c *PropertiesReportingDataAnnotationsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesReportingDataAnnotationsPatchCall) UpdateMask ¶
added in v0.229.0
func (c *PropertiesReportingDataAnnotationsPatchCall) UpdateMask(updateMask string) *PropertiesReportingDataAnnotationsPatchCall

UpdateMask sets the optional parameter "updateMask": The list of fields to update. Field names must be in snake case (for example, "field_to_update"). Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.

type PropertiesReportingDataAnnotationsService ¶
added in v0.229.0
type PropertiesReportingDataAnnotationsService struct {
	// contains filtered or unexported fields
}
func NewPropertiesReportingDataAnnotationsService ¶
added in v0.229.0
func NewPropertiesReportingDataAnnotationsService(s *Service) *PropertiesReportingDataAnnotationsService
func (*PropertiesReportingDataAnnotationsService) Create ¶
added in v0.229.0
func (r *PropertiesReportingDataAnnotationsService) Create(parent string, googleanalyticsadminv1alphareportingdataannotation *GoogleAnalyticsAdminV1alphaReportingDataAnnotation) *PropertiesReportingDataAnnotationsCreateCall

Create: Creates a Reporting Data Annotation.

parent: The property for which to create a Reporting Data Annotation. Format: properties/property_id Example: properties/123.
func (*PropertiesReportingDataAnnotationsService) Delete ¶
added in v0.229.0
func (r *PropertiesReportingDataAnnotationsService) Delete(name string) *PropertiesReportingDataAnnotationsDeleteCall

Delete: Deletes a Reporting Data Annotation.

name: Resource name of the Reporting Data Annotation to delete. Format: properties/property_id/reportingDataAnnotations/reporting_data_annotation Example: properties/123/reportingDataAnnotations/456.
func (*PropertiesReportingDataAnnotationsService) Get ¶
added in v0.229.0
func (r *PropertiesReportingDataAnnotationsService) Get(name string) *PropertiesReportingDataAnnotationsGetCall

Get: Lookup a single Reporting Data Annotation.

name: Resource name of the Reporting Data Annotation to lookup. Format: properties/property_id/reportingDataAnnotations/reportingDataAnnotation Example: properties/123/reportingDataAnnotations/456.
func (*PropertiesReportingDataAnnotationsService) List ¶
added in v0.229.0
func (r *PropertiesReportingDataAnnotationsService) List(parent string) *PropertiesReportingDataAnnotationsListCall

List: List all Reporting Data Annotations on a property.

parent: Resource name of the property. Format: properties/property_id Example: properties/123.
func (*PropertiesReportingDataAnnotationsService) Patch ¶
added in v0.229.0
func (r *PropertiesReportingDataAnnotationsService) Patch(name string, googleanalyticsadminv1alphareportingdataannotation *GoogleAnalyticsAdminV1alphaReportingDataAnnotation) *PropertiesReportingDataAnnotationsPatchCall

Patch: Updates a Reporting Data Annotation.

name: Identifier. Resource name of this Reporting Data Annotation. Format: 'properties/{property_id}/reportingDataAnnotations/{reporting_data_annotati on}' Format: 'properties/123/reportingDataAnnotations/456'.
type PropertiesRollupPropertySourceLinksCreateCall ¶
added in v0.144.0
type PropertiesRollupPropertySourceLinksCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesRollupPropertySourceLinksCreateCall) Context ¶
added in v0.144.0
func (c *PropertiesRollupPropertySourceLinksCreateCall) Context(ctx context.Context) *PropertiesRollupPropertySourceLinksCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesRollupPropertySourceLinksCreateCall) Do ¶
added in v0.144.0
func (c *PropertiesRollupPropertySourceLinksCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaRollupPropertySourceLink, error)

Do executes the "analyticsadmin.properties.rollupPropertySourceLinks.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaRollupPropertySourceLink.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesRollupPropertySourceLinksCreateCall) Fields ¶
added in v0.144.0
func (c *PropertiesRollupPropertySourceLinksCreateCall) Fields(s ...googleapi.Field) *PropertiesRollupPropertySourceLinksCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesRollupPropertySourceLinksCreateCall) Header ¶
added in v0.144.0
func (c *PropertiesRollupPropertySourceLinksCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesRollupPropertySourceLinksDeleteCall ¶
added in v0.144.0
type PropertiesRollupPropertySourceLinksDeleteCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesRollupPropertySourceLinksDeleteCall) Context ¶
added in v0.144.0
func (c *PropertiesRollupPropertySourceLinksDeleteCall) Context(ctx context.Context) *PropertiesRollupPropertySourceLinksDeleteCall

Context sets the context to be used in this call's Do method.

func (*PropertiesRollupPropertySourceLinksDeleteCall) Do ¶
added in v0.144.0
func (c *PropertiesRollupPropertySourceLinksDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.properties.rollupPropertySourceLinks.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesRollupPropertySourceLinksDeleteCall) Fields ¶
added in v0.144.0
func (c *PropertiesRollupPropertySourceLinksDeleteCall) Fields(s ...googleapi.Field) *PropertiesRollupPropertySourceLinksDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesRollupPropertySourceLinksDeleteCall) Header ¶
added in v0.144.0
func (c *PropertiesRollupPropertySourceLinksDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesRollupPropertySourceLinksGetCall ¶
added in v0.144.0
type PropertiesRollupPropertySourceLinksGetCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesRollupPropertySourceLinksGetCall) Context ¶
added in v0.144.0
func (c *PropertiesRollupPropertySourceLinksGetCall) Context(ctx context.Context) *PropertiesRollupPropertySourceLinksGetCall

Context sets the context to be used in this call's Do method.

func (*PropertiesRollupPropertySourceLinksGetCall) Do ¶
added in v0.144.0
func (c *PropertiesRollupPropertySourceLinksGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaRollupPropertySourceLink, error)

Do executes the "analyticsadmin.properties.rollupPropertySourceLinks.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaRollupPropertySourceLink.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesRollupPropertySourceLinksGetCall) Fields ¶
added in v0.144.0
func (c *PropertiesRollupPropertySourceLinksGetCall) Fields(s ...googleapi.Field) *PropertiesRollupPropertySourceLinksGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesRollupPropertySourceLinksGetCall) Header ¶
added in v0.144.0
func (c *PropertiesRollupPropertySourceLinksGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesRollupPropertySourceLinksGetCall) IfNoneMatch ¶
added in v0.144.0
func (c *PropertiesRollupPropertySourceLinksGetCall) IfNoneMatch(entityTag string) *PropertiesRollupPropertySourceLinksGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesRollupPropertySourceLinksListCall ¶
added in v0.144.0
type PropertiesRollupPropertySourceLinksListCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesRollupPropertySourceLinksListCall) Context ¶
added in v0.144.0
func (c *PropertiesRollupPropertySourceLinksListCall) Context(ctx context.Context) *PropertiesRollupPropertySourceLinksListCall

Context sets the context to be used in this call's Do method.

func (*PropertiesRollupPropertySourceLinksListCall) Do ¶
added in v0.144.0
func (c *PropertiesRollupPropertySourceLinksListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListRollupPropertySourceLinksResponse, error)

Do executes the "analyticsadmin.properties.rollupPropertySourceLinks.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaListRollupPropertySourceLinksResponse.ServerRespo nse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesRollupPropertySourceLinksListCall) Fields ¶
added in v0.144.0
func (c *PropertiesRollupPropertySourceLinksListCall) Fields(s ...googleapi.Field) *PropertiesRollupPropertySourceLinksListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesRollupPropertySourceLinksListCall) Header ¶
added in v0.144.0
func (c *PropertiesRollupPropertySourceLinksListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesRollupPropertySourceLinksListCall) IfNoneMatch ¶
added in v0.144.0
func (c *PropertiesRollupPropertySourceLinksListCall) IfNoneMatch(entityTag string) *PropertiesRollupPropertySourceLinksListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesRollupPropertySourceLinksListCall) PageSize ¶
added in v0.144.0
func (c *PropertiesRollupPropertySourceLinksListCall) PageSize(pageSize int64) *PropertiesRollupPropertySourceLinksListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. The service may return fewer than this value, even if there are additional pages. If unspecified, at most 50 resources will be returned. The maximum value is 200; (higher values will be coerced to the maximum)

func (*PropertiesRollupPropertySourceLinksListCall) PageToken ¶
added in v0.144.0
func (c *PropertiesRollupPropertySourceLinksListCall) PageToken(pageToken string) *PropertiesRollupPropertySourceLinksListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListRollupPropertySourceLinks` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListRollupPropertySourceLinks` must match the call that provided the page token.

func (*PropertiesRollupPropertySourceLinksListCall) Pages ¶
added in v0.144.0
func (c *PropertiesRollupPropertySourceLinksListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1alphaListRollupPropertySourceLinksResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesRollupPropertySourceLinksService ¶
added in v0.144.0
type PropertiesRollupPropertySourceLinksService struct {
	// contains filtered or unexported fields
}
func NewPropertiesRollupPropertySourceLinksService ¶
added in v0.144.0
func NewPropertiesRollupPropertySourceLinksService(s *Service) *PropertiesRollupPropertySourceLinksService
func (*PropertiesRollupPropertySourceLinksService) Create ¶
added in v0.144.0
func (r *PropertiesRollupPropertySourceLinksService) Create(parent string, googleanalyticsadminv1alpharolluppropertysourcelink *GoogleAnalyticsAdminV1alphaRollupPropertySourceLink) *PropertiesRollupPropertySourceLinksCreateCall

Create: Creates a roll-up property source link. Only roll-up properties can have source links, so this method will throw an error if used on other types of properties.

- parent: Format: properties/{property_id} Example: properties/1234.

func (*PropertiesRollupPropertySourceLinksService) Delete ¶
added in v0.144.0
func (r *PropertiesRollupPropertySourceLinksService) Delete(name string) *PropertiesRollupPropertySourceLinksDeleteCall

Delete: Deletes a roll-up property source link. Only roll-up properties can have source links, so this method will throw an error if used on other types of properties.

name: Format: properties/{property_id}/rollupPropertySourceLinks/{rollup_property_source_ link_id} Example: properties/1234/rollupPropertySourceLinks/5678.
func (*PropertiesRollupPropertySourceLinksService) Get ¶
added in v0.144.0
func (r *PropertiesRollupPropertySourceLinksService) Get(name string) *PropertiesRollupPropertySourceLinksGetCall

Get: Lookup for a single roll-up property source Link. Only roll-up properties can have source links, so this method will throw an error if used on other types of properties.

name: The name of the roll-up property source link to lookup. Format: properties/{property_id}/rollupPropertySourceLinks/{rollup_property_source_ link_id} Example: properties/123/rollupPropertySourceLinks/456.
func (*PropertiesRollupPropertySourceLinksService) List ¶
added in v0.144.0
func (r *PropertiesRollupPropertySourceLinksService) List(parent string) *PropertiesRollupPropertySourceLinksListCall

List: Lists roll-up property source Links on a property. Only roll-up properties can have source links, so this method will throw an error if used on other types of properties.

parent: The name of the roll-up property to list roll-up property source links under. Format: properties/{property_id} Example: properties/1234.
type PropertiesRunAccessReportCall ¶
added in v0.86.0
type PropertiesRunAccessReportCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesRunAccessReportCall) Context ¶
added in v0.86.0
func (c *PropertiesRunAccessReportCall) Context(ctx context.Context) *PropertiesRunAccessReportCall

Context sets the context to be used in this call's Do method.

func (*PropertiesRunAccessReportCall) Do ¶
added in v0.86.0
func (c *PropertiesRunAccessReportCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaRunAccessReportResponse, error)

Do executes the "analyticsadmin.properties.runAccessReport" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaRunAccessReportResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesRunAccessReportCall) Fields ¶
added in v0.86.0
func (c *PropertiesRunAccessReportCall) Fields(s ...googleapi.Field) *PropertiesRunAccessReportCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesRunAccessReportCall) Header ¶
added in v0.86.0
func (c *PropertiesRunAccessReportCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesSearchAds360LinksCreateCall ¶
added in v0.100.0
type PropertiesSearchAds360LinksCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesSearchAds360LinksCreateCall) Context ¶
added in v0.100.0
func (c *PropertiesSearchAds360LinksCreateCall) Context(ctx context.Context) *PropertiesSearchAds360LinksCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesSearchAds360LinksCreateCall) Do ¶
added in v0.100.0
func (c *PropertiesSearchAds360LinksCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaSearchAds360Link, error)

Do executes the "analyticsadmin.properties.searchAds360Links.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaSearchAds360Link.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesSearchAds360LinksCreateCall) Fields ¶
added in v0.100.0
func (c *PropertiesSearchAds360LinksCreateCall) Fields(s ...googleapi.Field) *PropertiesSearchAds360LinksCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesSearchAds360LinksCreateCall) Header ¶
added in v0.100.0
func (c *PropertiesSearchAds360LinksCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesSearchAds360LinksDeleteCall ¶
added in v0.100.0
type PropertiesSearchAds360LinksDeleteCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesSearchAds360LinksDeleteCall) Context ¶
added in v0.100.0
func (c *PropertiesSearchAds360LinksDeleteCall) Context(ctx context.Context) *PropertiesSearchAds360LinksDeleteCall

Context sets the context to be used in this call's Do method.

func (*PropertiesSearchAds360LinksDeleteCall) Do ¶
added in v0.100.0
func (c *PropertiesSearchAds360LinksDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.properties.searchAds360Links.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesSearchAds360LinksDeleteCall) Fields ¶
added in v0.100.0
func (c *PropertiesSearchAds360LinksDeleteCall) Fields(s ...googleapi.Field) *PropertiesSearchAds360LinksDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesSearchAds360LinksDeleteCall) Header ¶
added in v0.100.0
func (c *PropertiesSearchAds360LinksDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesSearchAds360LinksGetCall ¶
added in v0.100.0
type PropertiesSearchAds360LinksGetCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesSearchAds360LinksGetCall) Context ¶
added in v0.100.0
func (c *PropertiesSearchAds360LinksGetCall) Context(ctx context.Context) *PropertiesSearchAds360LinksGetCall

Context sets the context to be used in this call's Do method.

func (*PropertiesSearchAds360LinksGetCall) Do ¶
added in v0.100.0
func (c *PropertiesSearchAds360LinksGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaSearchAds360Link, error)

Do executes the "analyticsadmin.properties.searchAds360Links.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaSearchAds360Link.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesSearchAds360LinksGetCall) Fields ¶
added in v0.100.0
func (c *PropertiesSearchAds360LinksGetCall) Fields(s ...googleapi.Field) *PropertiesSearchAds360LinksGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesSearchAds360LinksGetCall) Header ¶
added in v0.100.0
func (c *PropertiesSearchAds360LinksGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesSearchAds360LinksGetCall) IfNoneMatch ¶
added in v0.100.0
func (c *PropertiesSearchAds360LinksGetCall) IfNoneMatch(entityTag string) *PropertiesSearchAds360LinksGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesSearchAds360LinksListCall ¶
added in v0.100.0
type PropertiesSearchAds360LinksListCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesSearchAds360LinksListCall) Context ¶
added in v0.100.0
func (c *PropertiesSearchAds360LinksListCall) Context(ctx context.Context) *PropertiesSearchAds360LinksListCall

Context sets the context to be used in this call's Do method.

func (*PropertiesSearchAds360LinksListCall) Do ¶
added in v0.100.0
func (c *PropertiesSearchAds360LinksListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListSearchAds360LinksResponse, error)

Do executes the "analyticsadmin.properties.searchAds360Links.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaListSearchAds360LinksResponse.ServerResponse.Head er or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesSearchAds360LinksListCall) Fields ¶
added in v0.100.0
func (c *PropertiesSearchAds360LinksListCall) Fields(s ...googleapi.Field) *PropertiesSearchAds360LinksListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesSearchAds360LinksListCall) Header ¶
added in v0.100.0
func (c *PropertiesSearchAds360LinksListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesSearchAds360LinksListCall) IfNoneMatch ¶
added in v0.100.0
func (c *PropertiesSearchAds360LinksListCall) IfNoneMatch(entityTag string) *PropertiesSearchAds360LinksListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesSearchAds360LinksListCall) PageSize ¶
added in v0.100.0
func (c *PropertiesSearchAds360LinksListCall) PageSize(pageSize int64) *PropertiesSearchAds360LinksListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. If unspecified, at most 50 resources will be returned. The maximum value is 200 (higher values will be coerced to the maximum).

func (*PropertiesSearchAds360LinksListCall) PageToken ¶
added in v0.100.0
func (c *PropertiesSearchAds360LinksListCall) PageToken(pageToken string) *PropertiesSearchAds360LinksListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListSearchAds360Links` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListSearchAds360Links` must match the call that provided the page token.

func (*PropertiesSearchAds360LinksListCall) Pages ¶
added in v0.100.0
func (c *PropertiesSearchAds360LinksListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1alphaListSearchAds360LinksResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesSearchAds360LinksPatchCall ¶
added in v0.100.0
type PropertiesSearchAds360LinksPatchCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesSearchAds360LinksPatchCall) Context ¶
added in v0.100.0
func (c *PropertiesSearchAds360LinksPatchCall) Context(ctx context.Context) *PropertiesSearchAds360LinksPatchCall

Context sets the context to be used in this call's Do method.

func (*PropertiesSearchAds360LinksPatchCall) Do ¶
added in v0.100.0
func (c *PropertiesSearchAds360LinksPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaSearchAds360Link, error)

Do executes the "analyticsadmin.properties.searchAds360Links.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaSearchAds360Link.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesSearchAds360LinksPatchCall) Fields ¶
added in v0.100.0
func (c *PropertiesSearchAds360LinksPatchCall) Fields(s ...googleapi.Field) *PropertiesSearchAds360LinksPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesSearchAds360LinksPatchCall) Header ¶
added in v0.100.0
func (c *PropertiesSearchAds360LinksPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesSearchAds360LinksPatchCall) UpdateMask ¶
added in v0.100.0
func (c *PropertiesSearchAds360LinksPatchCall) UpdateMask(updateMask string) *PropertiesSearchAds360LinksPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated. Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.

type PropertiesSearchAds360LinksService ¶
added in v0.100.0
type PropertiesSearchAds360LinksService struct {
	// contains filtered or unexported fields
}
func NewPropertiesSearchAds360LinksService ¶
added in v0.100.0
func NewPropertiesSearchAds360LinksService(s *Service) *PropertiesSearchAds360LinksService
func (*PropertiesSearchAds360LinksService) Create ¶
added in v0.100.0
func (r *PropertiesSearchAds360LinksService) Create(parent string, googleanalyticsadminv1alphasearchads360link *GoogleAnalyticsAdminV1alphaSearchAds360Link) *PropertiesSearchAds360LinksCreateCall

Create: Creates a SearchAds360Link.

- parent: Example format: properties/1234.

func (*PropertiesSearchAds360LinksService) Delete ¶
added in v0.100.0
func (r *PropertiesSearchAds360LinksService) Delete(name string) *PropertiesSearchAds360LinksDeleteCall

Delete: Deletes a SearchAds360Link on a property.

name: The name of the SearchAds360Link to delete. Example format: properties/1234/SearchAds360Links/5678.
func (*PropertiesSearchAds360LinksService) Get ¶
added in v0.100.0
func (r *PropertiesSearchAds360LinksService) Get(name string) *PropertiesSearchAds360LinksGetCall

Get: Look up a single SearchAds360Link

name: The name of the SearchAds360Link to get. Example format: properties/1234/SearchAds360Link/5678.
func (*PropertiesSearchAds360LinksService) List ¶
added in v0.100.0
func (r *PropertiesSearchAds360LinksService) List(parent string) *PropertiesSearchAds360LinksListCall

List: Lists all SearchAds360Links on a property.

- parent: Example format: properties/1234.

func (*PropertiesSearchAds360LinksService) Patch ¶
added in v0.100.0
func (r *PropertiesSearchAds360LinksService) Patch(name string, googleanalyticsadminv1alphasearchads360link *GoogleAnalyticsAdminV1alphaSearchAds360Link) *PropertiesSearchAds360LinksPatchCall

Patch: Updates a SearchAds360Link on a property.

name: Output only. The resource name for this SearchAds360Link resource. Format: properties/{propertyId}/searchAds360Links/{linkId} Note: linkId is not the Search Ads 360 advertiser ID.
type PropertiesService ¶
type PropertiesService struct {
	AccessBindings *PropertiesAccessBindingsService

	AdSenseLinks *PropertiesAdSenseLinksService

	Audiences *PropertiesAudiencesService

	BigQueryLinks *PropertiesBigQueryLinksService

	CalculatedMetrics *PropertiesCalculatedMetricsService

	ChannelGroups *PropertiesChannelGroupsService

	ConversionEvents *PropertiesConversionEventsService

	CustomDimensions *PropertiesCustomDimensionsService

	CustomMetrics *PropertiesCustomMetricsService

	DataStreams *PropertiesDataStreamsService

	DisplayVideo360AdvertiserLinkProposals *PropertiesDisplayVideo360AdvertiserLinkProposalsService

	DisplayVideo360AdvertiserLinks *PropertiesDisplayVideo360AdvertiserLinksService

	ExpandedDataSets *PropertiesExpandedDataSetsService

	FirebaseLinks *PropertiesFirebaseLinksService

	GoogleAdsLinks *PropertiesGoogleAdsLinksService

	KeyEvents *PropertiesKeyEventsService

	ReportingDataAnnotations *PropertiesReportingDataAnnotationsService

	RollupPropertySourceLinks *PropertiesRollupPropertySourceLinksService

	SearchAds360Links *PropertiesSearchAds360LinksService

	SubpropertyEventFilters *PropertiesSubpropertyEventFiltersService

	SubpropertySyncConfigs *PropertiesSubpropertySyncConfigsService
	// contains filtered or unexported fields
}
func NewPropertiesService ¶
func NewPropertiesService(s *Service) *PropertiesService
func (*PropertiesService) AcknowledgeUserDataCollection ¶
added in v0.59.0
func (r *PropertiesService) AcknowledgeUserDataCollection(property string, googleanalyticsadminv1alphaacknowledgeuserdatacollectionrequest *GoogleAnalyticsAdminV1alphaAcknowledgeUserDataCollectionRequest) *PropertiesAcknowledgeUserDataCollectionCall

AcknowledgeUserDataCollection: Acknowledges the terms of user data collection for the specified property. This acknowledgement must be completed (either in the Google Analytics UI or through this API) before MeasurementProtocolSecret resources may be created.

- property: The property for which to acknowledge user data collection.

func (*PropertiesService) Create ¶
func (r *PropertiesService) Create(googleanalyticsadminv1alphaproperty *GoogleAnalyticsAdminV1alphaProperty) *PropertiesCreateCall

Create: Creates a Google Analytics property with the specified location and attributes.

func (*PropertiesService) CreateRollupProperty ¶
added in v0.144.0
func (r *PropertiesService) CreateRollupProperty(googleanalyticsadminv1alphacreaterolluppropertyrequest *GoogleAnalyticsAdminV1alphaCreateRollupPropertyRequest) *PropertiesCreateRollupPropertyCall

CreateRollupProperty: Create a roll-up property and all roll-up property source links.

func (*PropertiesService) Delete ¶
func (r *PropertiesService) Delete(name string) *PropertiesDeleteCall

Delete: Marks target Property as soft-deleted (ie: "trashed") and returns it. This API does not have a method to restore soft-deleted properties. However, they can be restored using the Trash Can UI. If the properties are not restored before the expiration time, the Property and all child resources (eg: GoogleAdsLinks, Streams, AccessBindings) will be permanently purged. https://support.google.com/analytics/answer/6154772 Returns an error if the target is not found.

name: The name of the Property to soft-delete. Format: properties/{property_id} Example: "properties/1000".
func (*PropertiesService) Get ¶
func (r *PropertiesService) Get(name string) *PropertiesGetCall

Get: Lookup for a single GA Property.

name: The name of the property to lookup. Format: properties/{property_id} Example: "properties/1000".
func (*PropertiesService) GetAttributionSettings ¶
added in v0.84.0
func (r *PropertiesService) GetAttributionSettings(name string) *PropertiesGetAttributionSettingsCall

GetAttributionSettings: Lookup for a AttributionSettings singleton.

name: The name of the attribution settings to retrieve. Format: properties/{property}/attributionSettings.
func (*PropertiesService) GetDataRetentionSettings ¶
added in v0.55.0
func (r *PropertiesService) GetDataRetentionSettings(name string) *PropertiesGetDataRetentionSettingsCall

GetDataRetentionSettings: Returns the singleton data retention settings for this property.

name: The name of the settings to lookup. Format: properties/{property}/dataRetentionSettings Example: "properties/1000/dataRetentionSettings".
func (*PropertiesService) GetGoogleSignalsSettings ¶
added in v0.47.0
func (r *PropertiesService) GetGoogleSignalsSettings(name string) *PropertiesGetGoogleSignalsSettingsCall

GetGoogleSignalsSettings: Lookup for Google Signals settings for a property.

name: The name of the google signals settings to retrieve. Format: properties/{property}/googleSignalsSettings.
func (*PropertiesService) GetReportingIdentitySettings ¶
added in v0.240.0
func (r *PropertiesService) GetReportingIdentitySettings(name string) *PropertiesGetReportingIdentitySettingsCall

GetReportingIdentitySettings: Returns the reporting identity settings for this property.

name: The name of the settings to lookup. Format: properties/{property}/reportingIdentitySettings Example: "properties/1000/reportingIdentitySettings".
func (*PropertiesService) List ¶
func (r *PropertiesService) List() *PropertiesListCall

List: Returns child Properties under the specified parent Account. Properties will be excluded if the caller does not have access. Soft-deleted (ie: "trashed") properties are excluded by default. Returns an empty list if no relevant properties are found.

func (*PropertiesService) Patch ¶
func (r *PropertiesService) Patch(name string, googleanalyticsadminv1alphaproperty *GoogleAnalyticsAdminV1alphaProperty) *PropertiesPatchCall

Patch: Updates a property.

name: Output only. Resource name of this property. Format: properties/{property_id} Example: "properties/1000".
func (*PropertiesService) ProvisionSubproperty ¶
added in v0.191.0
func (r *PropertiesService) ProvisionSubproperty(googleanalyticsadminv1alphaprovisionsubpropertyrequest *GoogleAnalyticsAdminV1alphaProvisionSubpropertyRequest) *PropertiesProvisionSubpropertyCall

ProvisionSubproperty: Create a subproperty and a subproperty event filter that applies to the created subproperty.

func (*PropertiesService) RunAccessReport ¶
added in v0.86.0
func (r *PropertiesService) RunAccessReport(entity string, googleanalyticsadminv1alpharunaccessreportrequest *GoogleAnalyticsAdminV1alphaRunAccessReportRequest) *PropertiesRunAccessReportCall

RunAccessReport: Returns a customized report of data access records. The report provides records of each time a user reads Google Analytics reporting data. Access records are retained for up to 2 years. Data Access Reports can be requested for a property. Reports may be requested for any property, but dimensions that aren't related to quota can only be requested on Google Analytics 360 properties. This method is only available to Administrators. These data access records include GA UI Reporting, GA UI Explorations, GA Data API, and other products like Firebase & Admob that can retrieve data from Google Analytics through a linkage. These records don't include property configuration changes like adding a stream or changing a property's time zone. For configuration change history, see searchChangeHistoryEvents (https://developers.google.com/analytics/devguides/config/admin/v1/rest/v1alpha/accounts/searchChangeHistoryEvents). To give your feedback on this API, complete the Google Analytics Access Reports feedback (https://docs.google.com/forms/d/e/1FAIpQLSdmEBUrMzAEdiEKk5TV5dEHvDUZDRlgWYdQdAeSdtR4hVjEhw/viewform) form.

entity: The Data Access Report supports requesting at the property level or account level. If requested at the account level, Data Access Reports include all access for all properties under that account. To request at the property level, entity should be for example 'properties/123' if "123" is your Google Analytics property ID. To request at the account level, entity should be for example 'accounts/1234' if "1234" is your Google Analytics Account ID.
func (*PropertiesService) SubmitUserDeletion ¶
added in v0.244.0
func (r *PropertiesService) SubmitUserDeletion(name string, googleanalyticsadminv1alphasubmituserdeletionrequest *GoogleAnalyticsAdminV1alphaSubmitUserDeletionRequest) *PropertiesSubmitUserDeletionCall

SubmitUserDeletion: Submits a request for user deletion for a property.

- name: The name of the property to submit user deletion for.

func (*PropertiesService) UpdateAttributionSettings ¶
added in v0.84.0
func (r *PropertiesService) UpdateAttributionSettings(name string, googleanalyticsadminv1alphaattributionsettings *GoogleAnalyticsAdminV1alphaAttributionSettings) *PropertiesUpdateAttributionSettingsCall

UpdateAttributionSettings: Updates attribution settings on a property.

name: Output only. Resource name of this attribution settings resource. Format: properties/{property_id}/attributionSettings Example: "properties/1000/attributionSettings".
func (*PropertiesService) UpdateDataRetentionSettings ¶
added in v0.55.0
func (r *PropertiesService) UpdateDataRetentionSettings(name string, googleanalyticsadminv1alphadataretentionsettings *GoogleAnalyticsAdminV1alphaDataRetentionSettings) *PropertiesUpdateDataRetentionSettingsCall

UpdateDataRetentionSettings: Updates the singleton data retention settings for this property.

name: Output only. Resource name for this DataRetentionSetting resource. Format: properties/{property}/dataRetentionSettings.
func (*PropertiesService) UpdateGoogleSignalsSettings ¶
added in v0.47.0
func (r *PropertiesService) UpdateGoogleSignalsSettings(name string, googleanalyticsadminv1alphagooglesignalssettings *GoogleAnalyticsAdminV1alphaGoogleSignalsSettings) *PropertiesUpdateGoogleSignalsSettingsCall

UpdateGoogleSignalsSettings: Updates Google Signals settings for a property.

name: Output only. Resource name of this setting. Format: properties/{property_id}/googleSignalsSettings Example: "properties/1000/googleSignalsSettings".
type PropertiesSubmitUserDeletionCall ¶
added in v0.244.0
type PropertiesSubmitUserDeletionCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesSubmitUserDeletionCall) Context ¶
added in v0.244.0
func (c *PropertiesSubmitUserDeletionCall) Context(ctx context.Context) *PropertiesSubmitUserDeletionCall

Context sets the context to be used in this call's Do method.

func (*PropertiesSubmitUserDeletionCall) Do ¶
added in v0.244.0
func (c *PropertiesSubmitUserDeletionCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaSubmitUserDeletionResponse, error)

Do executes the "analyticsadmin.properties.submitUserDeletion" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaSubmitUserDeletionResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesSubmitUserDeletionCall) Fields ¶
added in v0.244.0
func (c *PropertiesSubmitUserDeletionCall) Fields(s ...googleapi.Field) *PropertiesSubmitUserDeletionCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesSubmitUserDeletionCall) Header ¶
added in v0.244.0
func (c *PropertiesSubmitUserDeletionCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesSubpropertyEventFiltersCreateCall ¶
added in v0.144.0
type PropertiesSubpropertyEventFiltersCreateCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesSubpropertyEventFiltersCreateCall) Context ¶
added in v0.144.0
func (c *PropertiesSubpropertyEventFiltersCreateCall) Context(ctx context.Context) *PropertiesSubpropertyEventFiltersCreateCall

Context sets the context to be used in this call's Do method.

func (*PropertiesSubpropertyEventFiltersCreateCall) Do ¶
added in v0.144.0
func (c *PropertiesSubpropertyEventFiltersCreateCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaSubpropertyEventFilter, error)

Do executes the "analyticsadmin.properties.subpropertyEventFilters.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaSubpropertyEventFilter.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesSubpropertyEventFiltersCreateCall) Fields ¶
added in v0.144.0
func (c *PropertiesSubpropertyEventFiltersCreateCall) Fields(s ...googleapi.Field) *PropertiesSubpropertyEventFiltersCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesSubpropertyEventFiltersCreateCall) Header ¶
added in v0.144.0
func (c *PropertiesSubpropertyEventFiltersCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesSubpropertyEventFiltersDeleteCall ¶
added in v0.144.0
type PropertiesSubpropertyEventFiltersDeleteCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesSubpropertyEventFiltersDeleteCall) Context ¶
added in v0.144.0
func (c *PropertiesSubpropertyEventFiltersDeleteCall) Context(ctx context.Context) *PropertiesSubpropertyEventFiltersDeleteCall

Context sets the context to be used in this call's Do method.

func (*PropertiesSubpropertyEventFiltersDeleteCall) Do ¶
added in v0.144.0
func (c *PropertiesSubpropertyEventFiltersDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleProtobufEmpty, error)

Do executes the "analyticsadmin.properties.subpropertyEventFilters.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleProtobufEmpty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesSubpropertyEventFiltersDeleteCall) Fields ¶
added in v0.144.0
func (c *PropertiesSubpropertyEventFiltersDeleteCall) Fields(s ...googleapi.Field) *PropertiesSubpropertyEventFiltersDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesSubpropertyEventFiltersDeleteCall) Header ¶
added in v0.144.0
func (c *PropertiesSubpropertyEventFiltersDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type PropertiesSubpropertyEventFiltersGetCall ¶
added in v0.144.0
type PropertiesSubpropertyEventFiltersGetCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesSubpropertyEventFiltersGetCall) Context ¶
added in v0.144.0
func (c *PropertiesSubpropertyEventFiltersGetCall) Context(ctx context.Context) *PropertiesSubpropertyEventFiltersGetCall

Context sets the context to be used in this call's Do method.

func (*PropertiesSubpropertyEventFiltersGetCall) Do ¶
added in v0.144.0
func (c *PropertiesSubpropertyEventFiltersGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaSubpropertyEventFilter, error)

Do executes the "analyticsadmin.properties.subpropertyEventFilters.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaSubpropertyEventFilter.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesSubpropertyEventFiltersGetCall) Fields ¶
added in v0.144.0
func (c *PropertiesSubpropertyEventFiltersGetCall) Fields(s ...googleapi.Field) *PropertiesSubpropertyEventFiltersGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesSubpropertyEventFiltersGetCall) Header ¶
added in v0.144.0
func (c *PropertiesSubpropertyEventFiltersGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesSubpropertyEventFiltersGetCall) IfNoneMatch ¶
added in v0.144.0
func (c *PropertiesSubpropertyEventFiltersGetCall) IfNoneMatch(entityTag string) *PropertiesSubpropertyEventFiltersGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesSubpropertyEventFiltersListCall ¶
added in v0.144.0
type PropertiesSubpropertyEventFiltersListCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesSubpropertyEventFiltersListCall) Context ¶
added in v0.144.0
func (c *PropertiesSubpropertyEventFiltersListCall) Context(ctx context.Context) *PropertiesSubpropertyEventFiltersListCall

Context sets the context to be used in this call's Do method.

func (*PropertiesSubpropertyEventFiltersListCall) Do ¶
added in v0.144.0
func (c *PropertiesSubpropertyEventFiltersListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListSubpropertyEventFiltersResponse, error)

Do executes the "analyticsadmin.properties.subpropertyEventFilters.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaListSubpropertyEventFiltersResponse.ServerRespons e.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesSubpropertyEventFiltersListCall) Fields ¶
added in v0.144.0
func (c *PropertiesSubpropertyEventFiltersListCall) Fields(s ...googleapi.Field) *PropertiesSubpropertyEventFiltersListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesSubpropertyEventFiltersListCall) Header ¶
added in v0.144.0
func (c *PropertiesSubpropertyEventFiltersListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesSubpropertyEventFiltersListCall) IfNoneMatch ¶
added in v0.144.0
func (c *PropertiesSubpropertyEventFiltersListCall) IfNoneMatch(entityTag string) *PropertiesSubpropertyEventFiltersListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesSubpropertyEventFiltersListCall) PageSize ¶
added in v0.144.0
func (c *PropertiesSubpropertyEventFiltersListCall) PageSize(pageSize int64) *PropertiesSubpropertyEventFiltersListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. The service may return fewer than this value, even if there are additional pages. If unspecified, at most 50 resources will be returned. The maximum value is 200; (higher values will be coerced to the maximum)

func (*PropertiesSubpropertyEventFiltersListCall) PageToken ¶
added in v0.144.0
func (c *PropertiesSubpropertyEventFiltersListCall) PageToken(pageToken string) *PropertiesSubpropertyEventFiltersListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListSubpropertyEventFilters` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListSubpropertyEventFilters` must match the call that provided the page token.

func (*PropertiesSubpropertyEventFiltersListCall) Pages ¶
added in v0.144.0
func (c *PropertiesSubpropertyEventFiltersListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1alphaListSubpropertyEventFiltersResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesSubpropertyEventFiltersPatchCall ¶
added in v0.144.0
type PropertiesSubpropertyEventFiltersPatchCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesSubpropertyEventFiltersPatchCall) Context ¶
added in v0.144.0
func (c *PropertiesSubpropertyEventFiltersPatchCall) Context(ctx context.Context) *PropertiesSubpropertyEventFiltersPatchCall

Context sets the context to be used in this call's Do method.

func (*PropertiesSubpropertyEventFiltersPatchCall) Do ¶
added in v0.144.0
func (c *PropertiesSubpropertyEventFiltersPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaSubpropertyEventFilter, error)

Do executes the "analyticsadmin.properties.subpropertyEventFilters.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaSubpropertyEventFilter.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesSubpropertyEventFiltersPatchCall) Fields ¶
added in v0.144.0
func (c *PropertiesSubpropertyEventFiltersPatchCall) Fields(s ...googleapi.Field) *PropertiesSubpropertyEventFiltersPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesSubpropertyEventFiltersPatchCall) Header ¶
added in v0.144.0
func (c *PropertiesSubpropertyEventFiltersPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesSubpropertyEventFiltersPatchCall) UpdateMask ¶
added in v0.144.0
func (c *PropertiesSubpropertyEventFiltersPatchCall) UpdateMask(updateMask string) *PropertiesSubpropertyEventFiltersPatchCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to update. Field names must be in snake case (for example, "field_to_update"). Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.

type PropertiesSubpropertyEventFiltersService ¶
added in v0.144.0
type PropertiesSubpropertyEventFiltersService struct {
	// contains filtered or unexported fields
}
func NewPropertiesSubpropertyEventFiltersService ¶
added in v0.144.0
func NewPropertiesSubpropertyEventFiltersService(s *Service) *PropertiesSubpropertyEventFiltersService
func (*PropertiesSubpropertyEventFiltersService) Create ¶
added in v0.144.0
func (r *PropertiesSubpropertyEventFiltersService) Create(parent string, googleanalyticsadminv1alphasubpropertyeventfilter *GoogleAnalyticsAdminV1alphaSubpropertyEventFilter) *PropertiesSubpropertyEventFiltersCreateCall

Create: Creates a subproperty Event Filter.

parent: The ordinary property for which to create a subproperty event filter. Format: properties/property_id Example: properties/123.
func (*PropertiesSubpropertyEventFiltersService) Delete ¶
added in v0.144.0
func (r *PropertiesSubpropertyEventFiltersService) Delete(name string) *PropertiesSubpropertyEventFiltersDeleteCall

Delete: Deletes a subproperty event filter.

name: Resource name of the subproperty event filter to delete. Format: properties/property_id/subpropertyEventFilters/subproperty_event_filter Example: properties/123/subpropertyEventFilters/456.
func (*PropertiesSubpropertyEventFiltersService) Get ¶
added in v0.144.0
func (r *PropertiesSubpropertyEventFiltersService) Get(name string) *PropertiesSubpropertyEventFiltersGetCall

Get: Lookup for a single subproperty Event Filter.

name: Resource name of the subproperty event filter to lookup. Format: properties/property_id/subpropertyEventFilters/subproperty_event_filter Example: properties/123/subpropertyEventFilters/456.
func (*PropertiesSubpropertyEventFiltersService) List ¶
added in v0.144.0
func (r *PropertiesSubpropertyEventFiltersService) List(parent string) *PropertiesSubpropertyEventFiltersListCall

List: List all subproperty Event Filters on a property.

parent: Resource name of the ordinary property. Format: properties/property_id Example: properties/123.
func (*PropertiesSubpropertyEventFiltersService) Patch ¶
added in v0.144.0
func (r *PropertiesSubpropertyEventFiltersService) Patch(name string, googleanalyticsadminv1alphasubpropertyeventfilter *GoogleAnalyticsAdminV1alphaSubpropertyEventFilter) *PropertiesSubpropertyEventFiltersPatchCall

Patch: Updates a subproperty Event Filter.

name: Output only. Format: properties/{ordinary_property_id}/subpropertyEventFilters/{sub_property_eve nt_filter} Example: properties/1234/subpropertyEventFilters/5678.
type PropertiesSubpropertySyncConfigsGetCall ¶
added in v0.237.0
type PropertiesSubpropertySyncConfigsGetCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesSubpropertySyncConfigsGetCall) Context ¶
added in v0.237.0
func (c *PropertiesSubpropertySyncConfigsGetCall) Context(ctx context.Context) *PropertiesSubpropertySyncConfigsGetCall

Context sets the context to be used in this call's Do method.

func (*PropertiesSubpropertySyncConfigsGetCall) Do ¶
added in v0.237.0
func (c *PropertiesSubpropertySyncConfigsGetCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaSubpropertySyncConfig, error)

Do executes the "analyticsadmin.properties.subpropertySyncConfigs.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaSubpropertySyncConfig.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesSubpropertySyncConfigsGetCall) Fields ¶
added in v0.237.0
func (c *PropertiesSubpropertySyncConfigsGetCall) Fields(s ...googleapi.Field) *PropertiesSubpropertySyncConfigsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesSubpropertySyncConfigsGetCall) Header ¶
added in v0.237.0
func (c *PropertiesSubpropertySyncConfigsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesSubpropertySyncConfigsGetCall) IfNoneMatch ¶
added in v0.237.0
func (c *PropertiesSubpropertySyncConfigsGetCall) IfNoneMatch(entityTag string) *PropertiesSubpropertySyncConfigsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type PropertiesSubpropertySyncConfigsListCall ¶
added in v0.237.0
type PropertiesSubpropertySyncConfigsListCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesSubpropertySyncConfigsListCall) Context ¶
added in v0.237.0
func (c *PropertiesSubpropertySyncConfigsListCall) Context(ctx context.Context) *PropertiesSubpropertySyncConfigsListCall

Context sets the context to be used in this call's Do method.

func (*PropertiesSubpropertySyncConfigsListCall) Do ¶
added in v0.237.0
func (c *PropertiesSubpropertySyncConfigsListCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaListSubpropertySyncConfigsResponse, error)

Do executes the "analyticsadmin.properties.subpropertySyncConfigs.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaListSubpropertySyncConfigsResponse.ServerResponse .Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesSubpropertySyncConfigsListCall) Fields ¶
added in v0.237.0
func (c *PropertiesSubpropertySyncConfigsListCall) Fields(s ...googleapi.Field) *PropertiesSubpropertySyncConfigsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesSubpropertySyncConfigsListCall) Header ¶
added in v0.237.0
func (c *PropertiesSubpropertySyncConfigsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesSubpropertySyncConfigsListCall) IfNoneMatch ¶
added in v0.237.0
func (c *PropertiesSubpropertySyncConfigsListCall) IfNoneMatch(entityTag string) *PropertiesSubpropertySyncConfigsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PropertiesSubpropertySyncConfigsListCall) PageSize ¶
added in v0.237.0
func (c *PropertiesSubpropertySyncConfigsListCall) PageSize(pageSize int64) *PropertiesSubpropertySyncConfigsListCall

PageSize sets the optional parameter "pageSize": The maximum number of resources to return. The service may return fewer than this value, even if there are additional pages. If unspecified, at most 50 resources will be returned. The maximum value is 200; (higher values will be coerced to the maximum)

func (*PropertiesSubpropertySyncConfigsListCall) PageToken ¶
added in v0.237.0
func (c *PropertiesSubpropertySyncConfigsListCall) PageToken(pageToken string) *PropertiesSubpropertySyncConfigsListCall

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListSubpropertySyncConfig` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListSubpropertySyncConfig` must match the call that provided the page token.

func (*PropertiesSubpropertySyncConfigsListCall) Pages ¶
added in v0.237.0
func (c *PropertiesSubpropertySyncConfigsListCall) Pages(ctx context.Context, f func(*GoogleAnalyticsAdminV1alphaListSubpropertySyncConfigsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PropertiesSubpropertySyncConfigsPatchCall ¶
added in v0.237.0
type PropertiesSubpropertySyncConfigsPatchCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesSubpropertySyncConfigsPatchCall) Context ¶
added in v0.237.0
func (c *PropertiesSubpropertySyncConfigsPatchCall) Context(ctx context.Context) *PropertiesSubpropertySyncConfigsPatchCall

Context sets the context to be used in this call's Do method.

func (*PropertiesSubpropertySyncConfigsPatchCall) Do ¶
added in v0.237.0
func (c *PropertiesSubpropertySyncConfigsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaSubpropertySyncConfig, error)

Do executes the "analyticsadmin.properties.subpropertySyncConfigs.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaSubpropertySyncConfig.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesSubpropertySyncConfigsPatchCall) Fields ¶
added in v0.237.0
func (c *PropertiesSubpropertySyncConfigsPatchCall) Fields(s ...googleapi.Field) *PropertiesSubpropertySyncConfigsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesSubpropertySyncConfigsPatchCall) Header ¶
added in v0.237.0
func (c *PropertiesSubpropertySyncConfigsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesSubpropertySyncConfigsPatchCall) UpdateMask ¶
added in v0.237.0
func (c *PropertiesSubpropertySyncConfigsPatchCall) UpdateMask(updateMask string) *PropertiesSubpropertySyncConfigsPatchCall

UpdateMask sets the optional parameter "updateMask": The list of fields to update. Field names must be in snake case (for example, "field_to_update"). Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.

type PropertiesSubpropertySyncConfigsService ¶
added in v0.237.0
type PropertiesSubpropertySyncConfigsService struct {
	// contains filtered or unexported fields
}
func NewPropertiesSubpropertySyncConfigsService ¶
added in v0.237.0
func NewPropertiesSubpropertySyncConfigsService(s *Service) *PropertiesSubpropertySyncConfigsService
func (*PropertiesSubpropertySyncConfigsService) Get ¶
added in v0.237.0
func (r *PropertiesSubpropertySyncConfigsService) Get(name string) *PropertiesSubpropertySyncConfigsGetCall

Get: Lookup for a single `SubpropertySyncConfig`.

name: Resource name of the SubpropertySyncConfig to lookup. Format: properties/{ordinary_property_id}/subpropertySyncConfigs/{subproperty_id} Example: properties/1234/subpropertySyncConfigs/5678.
func (*PropertiesSubpropertySyncConfigsService) List ¶
added in v0.237.0
func (r *PropertiesSubpropertySyncConfigsService) List(parent string) *PropertiesSubpropertySyncConfigsListCall

List: List all `SubpropertySyncConfig` resources for a property.

parent: Resource name of the property. Format: properties/property_id Example: properties/123.
func (*PropertiesSubpropertySyncConfigsService) Patch ¶
added in v0.237.0
func (r *PropertiesSubpropertySyncConfigsService) Patch(name string, googleanalyticsadminv1alphasubpropertysyncconfig *GoogleAnalyticsAdminV1alphaSubpropertySyncConfig) *PropertiesSubpropertySyncConfigsPatchCall

Patch: Updates a `SubpropertySyncConfig`.

name: Output only. Identifier. Format: properties/{ordinary_property_id}/subpropertySyncConfigs/{subproperty_id} Example: properties/1234/subpropertySyncConfigs/5678.
type PropertiesUpdateAttributionSettingsCall ¶
added in v0.84.0
type PropertiesUpdateAttributionSettingsCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesUpdateAttributionSettingsCall) Context ¶
added in v0.84.0
func (c *PropertiesUpdateAttributionSettingsCall) Context(ctx context.Context) *PropertiesUpdateAttributionSettingsCall

Context sets the context to be used in this call's Do method.

func (*PropertiesUpdateAttributionSettingsCall) Do ¶
added in v0.84.0
func (c *PropertiesUpdateAttributionSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaAttributionSettings, error)

Do executes the "analyticsadmin.properties.updateAttributionSettings" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaAttributionSettings.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesUpdateAttributionSettingsCall) Fields ¶
added in v0.84.0
func (c *PropertiesUpdateAttributionSettingsCall) Fields(s ...googleapi.Field) *PropertiesUpdateAttributionSettingsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesUpdateAttributionSettingsCall) Header ¶
added in v0.84.0
func (c *PropertiesUpdateAttributionSettingsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesUpdateAttributionSettingsCall) UpdateMask ¶
added in v0.84.0
func (c *PropertiesUpdateAttributionSettingsCall) UpdateMask(updateMask string) *PropertiesUpdateAttributionSettingsCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated. Field names must be in snake case (e.g., "field_to_update"). Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.

type PropertiesUpdateDataRetentionSettingsCall ¶
added in v0.55.0
type PropertiesUpdateDataRetentionSettingsCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesUpdateDataRetentionSettingsCall) Context ¶
added in v0.55.0
func (c *PropertiesUpdateDataRetentionSettingsCall) Context(ctx context.Context) *PropertiesUpdateDataRetentionSettingsCall

Context sets the context to be used in this call's Do method.

func (*PropertiesUpdateDataRetentionSettingsCall) Do ¶
added in v0.55.0
func (c *PropertiesUpdateDataRetentionSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaDataRetentionSettings, error)

Do executes the "analyticsadmin.properties.updateDataRetentionSettings" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaDataRetentionSettings.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesUpdateDataRetentionSettingsCall) Fields ¶
added in v0.55.0
func (c *PropertiesUpdateDataRetentionSettingsCall) Fields(s ...googleapi.Field) *PropertiesUpdateDataRetentionSettingsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesUpdateDataRetentionSettingsCall) Header ¶
added in v0.55.0
func (c *PropertiesUpdateDataRetentionSettingsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesUpdateDataRetentionSettingsCall) UpdateMask ¶
added in v0.55.0
func (c *PropertiesUpdateDataRetentionSettingsCall) UpdateMask(updateMask string) *PropertiesUpdateDataRetentionSettingsCall

UpdateMask sets the optional parameter "updateMask": Required. The list of fields to be updated. Field names must be in snake case (e.g., "field_to_update"). Omitted fields will not be updated. To replace the entire entity, use one path with the string "*" to match all fields.

type PropertiesUpdateGoogleSignalsSettingsCall ¶
added in v0.47.0
type PropertiesUpdateGoogleSignalsSettingsCall struct {
	// contains filtered or unexported fields
}
func (*PropertiesUpdateGoogleSignalsSettingsCall) Context ¶
added in v0.47.0
func (c *PropertiesUpdateGoogleSignalsSettingsCall) Context(ctx context.Context) *PropertiesUpdateGoogleSignalsSettingsCall

Context sets the context to be used in this call's Do method.

func (*PropertiesUpdateGoogleSignalsSettingsCall) Do ¶
added in v0.47.0
func (c *PropertiesUpdateGoogleSignalsSettingsCall) Do(opts ...googleapi.CallOption) (*GoogleAnalyticsAdminV1alphaGoogleSignalsSettings, error)

Do executes the "analyticsadmin.properties.updateGoogleSignalsSettings" call. Any non-2xx status code is an error. Response headers are in either *GoogleAnalyticsAdminV1alphaGoogleSignalsSettings.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PropertiesUpdateGoogleSignalsSettingsCall) Fields ¶
added in v0.47.0
func (c *PropertiesUpdateGoogleSignalsSettingsCall) Fields(s ...googleapi.Field) *PropertiesUpdateGoogleSignalsSettingsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PropertiesUpdateGoogleSignalsSettingsCall) Header ¶
added in v0.47.0
func (c *PropertiesUpdateGoogleSignalsSettingsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PropertiesUpdateGoogleSignalsSettingsCall) UpdateMask ¶
added in v0.47.0
func (c *PropertiesUpdateGoogleSignalsSettingsCall) UpdateMask(updateMask string) *PropertiesUpdateGoogleSignalsSettingsCall

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

go.dev uses cookies from Google to deliver and enhance the quality of its services and to analyze traffic. Learn more.
Okay
