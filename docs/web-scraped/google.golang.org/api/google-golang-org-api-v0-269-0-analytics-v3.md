# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/analytics/v3

Title: analytics package - google.golang.org/api/analytics/v3 - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/analytics/v3

Markdown Content:
Skip to Main Content
Why Go
Learn
Docs
Packages
Community
Discover Packages
 
google.golang.org/api
 
analytics
 
v3
analytics
package
Version: v0.269.0 Latest 
Published: Feb 24, 2026 
License: BSD-3-Clause 
Imports: 18 
Imported by: 45
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

Package analytics provides access to the Google Analytics API.

For product documentation, see: https://developers.google.com/analytics/

Library status ¶

These client libraries are officially supported by Google. However, this library is considered complete and is in maintenance mode. This means that we will address critical bugs and security issues but will not add any new features.

When possible, we recommend using our newer [Cloud Client Libraries for Go](https://pkg.go.dev/cloud.google.com/go) that are still actively being worked and iterated on.

Creating a client ¶

Usage example:

import "google.golang.org/api/analytics/v3"
...
ctx := context.Background()
analyticsService, err := analytics.NewService(ctx)


In this example, Google Application Default Credentials are used for authentication. For information on how to create and obtain Application Default Credentials, see https://developers.google.com/identity/protocols/application-default-credentials.

Other authentication options ¶

By default, all available scopes (see "Constants") are used to authenticate. To restrict scopes, use google.golang.org/api/option.WithScopes:

analyticsService, err := analytics.NewService(ctx, option.WithScopes(analytics.AnalyticsUserDeletionScope))


To use an API key for authentication (note: some APIs do not support API keys), use google.golang.org/api/option.WithAPIKey:

analyticsService, err := analytics.NewService(ctx, option.WithAPIKey("AIza..."))


To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow, use google.golang.org/api/option.WithTokenSource:

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
analyticsService, err := analytics.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))


See google.golang.org/api/option.ClientOption for details on options.

Index ¶
Constants
type Account
func (s Account) MarshalJSON() ([]byte, error)
type AccountChildLink
func (s AccountChildLink) MarshalJSON() ([]byte, error)
type AccountPermissions
func (s AccountPermissions) MarshalJSON() ([]byte, error)
type AccountRef
func (s AccountRef) MarshalJSON() ([]byte, error)
type AccountSummaries
func (s AccountSummaries) MarshalJSON() ([]byte, error)
type AccountSummary
func (s AccountSummary) MarshalJSON() ([]byte, error)
type AccountTicket
func (s AccountTicket) MarshalJSON() ([]byte, error)
type AccountTreeRequest
func (s AccountTreeRequest) MarshalJSON() ([]byte, error)
type AccountTreeResponse
func (s AccountTreeResponse) MarshalJSON() ([]byte, error)
type Accounts
func (s Accounts) MarshalJSON() ([]byte, error)
type AdWordsAccount
func (s AdWordsAccount) MarshalJSON() ([]byte, error)
type AnalyticsDataimportDeleteUploadDataRequest
func (s AnalyticsDataimportDeleteUploadDataRequest) MarshalJSON() ([]byte, error)
type Column
func (s Column) MarshalJSON() ([]byte, error)
type Columns
func (s Columns) MarshalJSON() ([]byte, error)
type CustomDataSource
func (s CustomDataSource) MarshalJSON() ([]byte, error)
type CustomDataSourceChildLink
func (s CustomDataSourceChildLink) MarshalJSON() ([]byte, error)
type CustomDataSourceParentLink
func (s CustomDataSourceParentLink) MarshalJSON() ([]byte, error)
type CustomDataSources
func (s CustomDataSources) MarshalJSON() ([]byte, error)
type CustomDimension
func (s CustomDimension) MarshalJSON() ([]byte, error)
type CustomDimensionParentLink
func (s CustomDimensionParentLink) MarshalJSON() ([]byte, error)
type CustomDimensions
func (s CustomDimensions) MarshalJSON() ([]byte, error)
type CustomMetric
func (s CustomMetric) MarshalJSON() ([]byte, error)
type CustomMetricParentLink
func (s CustomMetricParentLink) MarshalJSON() ([]byte, error)
type CustomMetrics
func (s CustomMetrics) MarshalJSON() ([]byte, error)
type DataGaGetCall
func (c *DataGaGetCall) Context(ctx context.Context) *DataGaGetCall
func (c *DataGaGetCall) Dimensions(dimensions string) *DataGaGetCall
func (c *DataGaGetCall) Do(opts ...googleapi.CallOption) (*GaData, error)
func (c *DataGaGetCall) Fields(s ...googleapi.Field) *DataGaGetCall
func (c *DataGaGetCall) Filters(filters string) *DataGaGetCall
func (c *DataGaGetCall) Header() http.Header
func (c *DataGaGetCall) IfNoneMatch(entityTag string) *DataGaGetCall
func (c *DataGaGetCall) IncludeEmptyRows(includeEmptyRows bool) *DataGaGetCall
func (c *DataGaGetCall) MaxResults(maxResults int64) *DataGaGetCall
func (c *DataGaGetCall) Output(output string) *DataGaGetCall
func (c *DataGaGetCall) SamplingLevel(samplingLevel string) *DataGaGetCall
func (c *DataGaGetCall) Segment(segment string) *DataGaGetCall
func (c *DataGaGetCall) Sort(sort string) *DataGaGetCall
func (c *DataGaGetCall) StartIndex(startIndex int64) *DataGaGetCall
type DataGaService
func NewDataGaService(s *Service) *DataGaService
func (r *DataGaService) Get(ids string, startDate string, endDate string, metrics string) *DataGaGetCall
type DataMcfGetCall
func (c *DataMcfGetCall) Context(ctx context.Context) *DataMcfGetCall
func (c *DataMcfGetCall) Dimensions(dimensions string) *DataMcfGetCall
func (c *DataMcfGetCall) Do(opts ...googleapi.CallOption) (*McfData, error)
func (c *DataMcfGetCall) Fields(s ...googleapi.Field) *DataMcfGetCall
func (c *DataMcfGetCall) Filters(filters string) *DataMcfGetCall
func (c *DataMcfGetCall) Header() http.Header
func (c *DataMcfGetCall) IfNoneMatch(entityTag string) *DataMcfGetCall
func (c *DataMcfGetCall) MaxResults(maxResults int64) *DataMcfGetCall
func (c *DataMcfGetCall) SamplingLevel(samplingLevel string) *DataMcfGetCall
func (c *DataMcfGetCall) Sort(sort string) *DataMcfGetCall
func (c *DataMcfGetCall) StartIndex(startIndex int64) *DataMcfGetCall
type DataMcfService
func NewDataMcfService(s *Service) *DataMcfService
func (r *DataMcfService) Get(ids string, startDate string, endDate string, metrics string) *DataMcfGetCall
type DataRealtimeGetCall
func (c *DataRealtimeGetCall) Context(ctx context.Context) *DataRealtimeGetCall
func (c *DataRealtimeGetCall) Dimensions(dimensions string) *DataRealtimeGetCall
func (c *DataRealtimeGetCall) Do(opts ...googleapi.CallOption) (*RealtimeData, error)
func (c *DataRealtimeGetCall) Fields(s ...googleapi.Field) *DataRealtimeGetCall
func (c *DataRealtimeGetCall) Filters(filters string) *DataRealtimeGetCall
func (c *DataRealtimeGetCall) Header() http.Header
func (c *DataRealtimeGetCall) IfNoneMatch(entityTag string) *DataRealtimeGetCall
func (c *DataRealtimeGetCall) MaxResults(maxResults int64) *DataRealtimeGetCall
func (c *DataRealtimeGetCall) Sort(sort string) *DataRealtimeGetCall
type DataRealtimeService
func NewDataRealtimeService(s *Service) *DataRealtimeService
func (r *DataRealtimeService) Get(ids string, metrics string) *DataRealtimeGetCall
type DataService
func NewDataService(s *Service) *DataService
type EntityAdWordsLink
func (s EntityAdWordsLink) MarshalJSON() ([]byte, error)
type EntityAdWordsLinkEntity
func (s EntityAdWordsLinkEntity) MarshalJSON() ([]byte, error)
type EntityAdWordsLinks
func (s EntityAdWordsLinks) MarshalJSON() ([]byte, error)
type EntityUserLink
func (s EntityUserLink) MarshalJSON() ([]byte, error)
type EntityUserLinkEntity
func (s EntityUserLinkEntity) MarshalJSON() ([]byte, error)
type EntityUserLinkPermissions
func (s EntityUserLinkPermissions) MarshalJSON() ([]byte, error)
type EntityUserLinks
func (s EntityUserLinks) MarshalJSON() ([]byte, error)
type Experiment
func (s Experiment) MarshalJSON() ([]byte, error)
func (s *Experiment) UnmarshalJSON(data []byte) error
type ExperimentParentLink
func (s ExperimentParentLink) MarshalJSON() ([]byte, error)
type ExperimentVariations
func (s ExperimentVariations) MarshalJSON() ([]byte, error)
func (s *ExperimentVariations) UnmarshalJSON(data []byte) error
type Experiments
func (s Experiments) MarshalJSON() ([]byte, error)
type Filter
func (s Filter) MarshalJSON() ([]byte, error)
type FilterAdvancedDetails
func (s FilterAdvancedDetails) MarshalJSON() ([]byte, error)
type FilterExpression
func (s FilterExpression) MarshalJSON() ([]byte, error)
type FilterLowercaseDetails
func (s FilterLowercaseDetails) MarshalJSON() ([]byte, error)
type FilterParentLink
func (s FilterParentLink) MarshalJSON() ([]byte, error)
type FilterRef
func (s FilterRef) MarshalJSON() ([]byte, error)
type FilterSearchAndReplaceDetails
func (s FilterSearchAndReplaceDetails) MarshalJSON() ([]byte, error)
type FilterUppercaseDetails
func (s FilterUppercaseDetails) MarshalJSON() ([]byte, error)
type Filters
func (s Filters) MarshalJSON() ([]byte, error)
type GaData
func (s GaData) MarshalJSON() ([]byte, error)
type GaDataColumnHeaders
func (s GaDataColumnHeaders) MarshalJSON() ([]byte, error)
type GaDataDataTable
func (s GaDataDataTable) MarshalJSON() ([]byte, error)
type GaDataDataTableCols
func (s GaDataDataTableCols) MarshalJSON() ([]byte, error)
type GaDataDataTableRows
func (s GaDataDataTableRows) MarshalJSON() ([]byte, error)
type GaDataDataTableRowsC
func (s GaDataDataTableRowsC) MarshalJSON() ([]byte, error)
type GaDataProfileInfo
func (s GaDataProfileInfo) MarshalJSON() ([]byte, error)
type GaDataQuery
func (s GaDataQuery) MarshalJSON() ([]byte, error)
type Goal
func (s Goal) MarshalJSON() ([]byte, error)
func (s *Goal) UnmarshalJSON(data []byte) error
type GoalEventDetails
func (s GoalEventDetails) MarshalJSON() ([]byte, error)
type GoalEventDetailsEventConditions
func (s GoalEventDetailsEventConditions) MarshalJSON() ([]byte, error)
type GoalParentLink
func (s GoalParentLink) MarshalJSON() ([]byte, error)
type GoalUrlDestinationDetails
func (s GoalUrlDestinationDetails) MarshalJSON() ([]byte, error)
type GoalUrlDestinationDetailsSteps
func (s GoalUrlDestinationDetailsSteps) MarshalJSON() ([]byte, error)
type GoalVisitNumPagesDetails
func (s GoalVisitNumPagesDetails) MarshalJSON() ([]byte, error)
type GoalVisitTimeOnSiteDetails
func (s GoalVisitTimeOnSiteDetails) MarshalJSON() ([]byte, error)
type Goals
func (s Goals) MarshalJSON() ([]byte, error)
type HashClientIdRequest
func (s HashClientIdRequest) MarshalJSON() ([]byte, error)
type HashClientIdResponse
func (s HashClientIdResponse) MarshalJSON() ([]byte, error)
type IncludeConditions
func (s IncludeConditions) MarshalJSON() ([]byte, error)
type LinkedForeignAccount
func (s LinkedForeignAccount) MarshalJSON() ([]byte, error)
type ManagementAccountSummariesListCall
func (c *ManagementAccountSummariesListCall) Context(ctx context.Context) *ManagementAccountSummariesListCall
func (c *ManagementAccountSummariesListCall) Do(opts ...googleapi.CallOption) (*AccountSummaries, error)
func (c *ManagementAccountSummariesListCall) Fields(s ...googleapi.Field) *ManagementAccountSummariesListCall
func (c *ManagementAccountSummariesListCall) Header() http.Header
func (c *ManagementAccountSummariesListCall) IfNoneMatch(entityTag string) *ManagementAccountSummariesListCall
func (c *ManagementAccountSummariesListCall) MaxResults(maxResults int64) *ManagementAccountSummariesListCall
func (c *ManagementAccountSummariesListCall) StartIndex(startIndex int64) *ManagementAccountSummariesListCall
type ManagementAccountSummariesService
func NewManagementAccountSummariesService(s *Service) *ManagementAccountSummariesService
func (r *ManagementAccountSummariesService) List() *ManagementAccountSummariesListCall
type ManagementAccountUserLinksDeleteCall
func (c *ManagementAccountUserLinksDeleteCall) Context(ctx context.Context) *ManagementAccountUserLinksDeleteCall
func (c *ManagementAccountUserLinksDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *ManagementAccountUserLinksDeleteCall) Fields(s ...googleapi.Field) *ManagementAccountUserLinksDeleteCall
func (c *ManagementAccountUserLinksDeleteCall) Header() http.Header
type ManagementAccountUserLinksInsertCall
func (c *ManagementAccountUserLinksInsertCall) Context(ctx context.Context) *ManagementAccountUserLinksInsertCall
func (c *ManagementAccountUserLinksInsertCall) Do(opts ...googleapi.CallOption) (*EntityUserLink, error)
func (c *ManagementAccountUserLinksInsertCall) Fields(s ...googleapi.Field) *ManagementAccountUserLinksInsertCall
func (c *ManagementAccountUserLinksInsertCall) Header() http.Header
type ManagementAccountUserLinksListCall
func (c *ManagementAccountUserLinksListCall) Context(ctx context.Context) *ManagementAccountUserLinksListCall
func (c *ManagementAccountUserLinksListCall) Do(opts ...googleapi.CallOption) (*EntityUserLinks, error)
func (c *ManagementAccountUserLinksListCall) Fields(s ...googleapi.Field) *ManagementAccountUserLinksListCall
func (c *ManagementAccountUserLinksListCall) Header() http.Header
func (c *ManagementAccountUserLinksListCall) IfNoneMatch(entityTag string) *ManagementAccountUserLinksListCall
func (c *ManagementAccountUserLinksListCall) MaxResults(maxResults int64) *ManagementAccountUserLinksListCall
func (c *ManagementAccountUserLinksListCall) StartIndex(startIndex int64) *ManagementAccountUserLinksListCall
type ManagementAccountUserLinksService
func NewManagementAccountUserLinksService(s *Service) *ManagementAccountUserLinksService
func (r *ManagementAccountUserLinksService) Delete(accountId string, linkId string) *ManagementAccountUserLinksDeleteCall
func (r *ManagementAccountUserLinksService) Insert(accountId string, entityuserlink *EntityUserLink) *ManagementAccountUserLinksInsertCall
func (r *ManagementAccountUserLinksService) List(accountId string) *ManagementAccountUserLinksListCall
func (r *ManagementAccountUserLinksService) Update(accountId string, linkId string, entityuserlink *EntityUserLink) *ManagementAccountUserLinksUpdateCall
type ManagementAccountUserLinksUpdateCall
func (c *ManagementAccountUserLinksUpdateCall) Context(ctx context.Context) *ManagementAccountUserLinksUpdateCall
func (c *ManagementAccountUserLinksUpdateCall) Do(opts ...googleapi.CallOption) (*EntityUserLink, error)
func (c *ManagementAccountUserLinksUpdateCall) Fields(s ...googleapi.Field) *ManagementAccountUserLinksUpdateCall
func (c *ManagementAccountUserLinksUpdateCall) Header() http.Header
type ManagementAccountsListCall
func (c *ManagementAccountsListCall) Context(ctx context.Context) *ManagementAccountsListCall
func (c *ManagementAccountsListCall) Do(opts ...googleapi.CallOption) (*Accounts, error)
func (c *ManagementAccountsListCall) Fields(s ...googleapi.Field) *ManagementAccountsListCall
func (c *ManagementAccountsListCall) Header() http.Header
func (c *ManagementAccountsListCall) IfNoneMatch(entityTag string) *ManagementAccountsListCall
func (c *ManagementAccountsListCall) MaxResults(maxResults int64) *ManagementAccountsListCall
func (c *ManagementAccountsListCall) StartIndex(startIndex int64) *ManagementAccountsListCall
type ManagementAccountsService
func NewManagementAccountsService(s *Service) *ManagementAccountsService
func (r *ManagementAccountsService) List() *ManagementAccountsListCall
type ManagementClientIdHashClientIdCall
func (c *ManagementClientIdHashClientIdCall) Context(ctx context.Context) *ManagementClientIdHashClientIdCall
func (c *ManagementClientIdHashClientIdCall) Do(opts ...googleapi.CallOption) (*HashClientIdResponse, error)
func (c *ManagementClientIdHashClientIdCall) Fields(s ...googleapi.Field) *ManagementClientIdHashClientIdCall
func (c *ManagementClientIdHashClientIdCall) Header() http.Header
type ManagementClientIdService
func NewManagementClientIdService(s *Service) *ManagementClientIdService
func (r *ManagementClientIdService) HashClientId(hashclientidrequest *HashClientIdRequest) *ManagementClientIdHashClientIdCall
type ManagementCustomDataSourcesListCall
func (c *ManagementCustomDataSourcesListCall) Context(ctx context.Context) *ManagementCustomDataSourcesListCall
func (c *ManagementCustomDataSourcesListCall) Do(opts ...googleapi.CallOption) (*CustomDataSources, error)
func (c *ManagementCustomDataSourcesListCall) Fields(s ...googleapi.Field) *ManagementCustomDataSourcesListCall
func (c *ManagementCustomDataSourcesListCall) Header() http.Header
func (c *ManagementCustomDataSourcesListCall) IfNoneMatch(entityTag string) *ManagementCustomDataSourcesListCall
func (c *ManagementCustomDataSourcesListCall) MaxResults(maxResults int64) *ManagementCustomDataSourcesListCall
func (c *ManagementCustomDataSourcesListCall) StartIndex(startIndex int64) *ManagementCustomDataSourcesListCall
type ManagementCustomDataSourcesService
func NewManagementCustomDataSourcesService(s *Service) *ManagementCustomDataSourcesService
func (r *ManagementCustomDataSourcesService) List(accountId string, webPropertyId string) *ManagementCustomDataSourcesListCall
type ManagementCustomDimensionsGetCall
func (c *ManagementCustomDimensionsGetCall) Context(ctx context.Context) *ManagementCustomDimensionsGetCall
func (c *ManagementCustomDimensionsGetCall) Do(opts ...googleapi.CallOption) (*CustomDimension, error)
func (c *ManagementCustomDimensionsGetCall) Fields(s ...googleapi.Field) *ManagementCustomDimensionsGetCall
func (c *ManagementCustomDimensionsGetCall) Header() http.Header
func (c *ManagementCustomDimensionsGetCall) IfNoneMatch(entityTag string) *ManagementCustomDimensionsGetCall
type ManagementCustomDimensionsInsertCall
func (c *ManagementCustomDimensionsInsertCall) Context(ctx context.Context) *ManagementCustomDimensionsInsertCall
func (c *ManagementCustomDimensionsInsertCall) Do(opts ...googleapi.CallOption) (*CustomDimension, error)
func (c *ManagementCustomDimensionsInsertCall) Fields(s ...googleapi.Field) *ManagementCustomDimensionsInsertCall
func (c *ManagementCustomDimensionsInsertCall) Header() http.Header
type ManagementCustomDimensionsListCall
func (c *ManagementCustomDimensionsListCall) Context(ctx context.Context) *ManagementCustomDimensionsListCall
func (c *ManagementCustomDimensionsListCall) Do(opts ...googleapi.CallOption) (*CustomDimensions, error)
func (c *ManagementCustomDimensionsListCall) Fields(s ...googleapi.Field) *ManagementCustomDimensionsListCall
func (c *ManagementCustomDimensionsListCall) Header() http.Header
func (c *ManagementCustomDimensionsListCall) IfNoneMatch(entityTag string) *ManagementCustomDimensionsListCall
func (c *ManagementCustomDimensionsListCall) MaxResults(maxResults int64) *ManagementCustomDimensionsListCall
func (c *ManagementCustomDimensionsListCall) StartIndex(startIndex int64) *ManagementCustomDimensionsListCall
type ManagementCustomDimensionsPatchCall
func (c *ManagementCustomDimensionsPatchCall) Context(ctx context.Context) *ManagementCustomDimensionsPatchCall
func (c *ManagementCustomDimensionsPatchCall) Do(opts ...googleapi.CallOption) (*CustomDimension, error)
func (c *ManagementCustomDimensionsPatchCall) Fields(s ...googleapi.Field) *ManagementCustomDimensionsPatchCall
func (c *ManagementCustomDimensionsPatchCall) Header() http.Header
func (c *ManagementCustomDimensionsPatchCall) IgnoreCustomDataSourceLinks(ignoreCustomDataSourceLinks bool) *ManagementCustomDimensionsPatchCall
type ManagementCustomDimensionsService
func NewManagementCustomDimensionsService(s *Service) *ManagementCustomDimensionsService
func (r *ManagementCustomDimensionsService) Get(accountId string, webPropertyId string, customDimensionId string) *ManagementCustomDimensionsGetCall
func (r *ManagementCustomDimensionsService) Insert(accountId string, webPropertyId string, customdimension *CustomDimension) *ManagementCustomDimensionsInsertCall
func (r *ManagementCustomDimensionsService) List(accountId string, webPropertyId string) *ManagementCustomDimensionsListCall
func (r *ManagementCustomDimensionsService) Patch(accountId string, webPropertyId string, customDimensionId string, ...) *ManagementCustomDimensionsPatchCall
func (r *ManagementCustomDimensionsService) Update(accountId string, webPropertyId string, customDimensionId string, ...) *ManagementCustomDimensionsUpdateCall
type ManagementCustomDimensionsUpdateCall
func (c *ManagementCustomDimensionsUpdateCall) Context(ctx context.Context) *ManagementCustomDimensionsUpdateCall
func (c *ManagementCustomDimensionsUpdateCall) Do(opts ...googleapi.CallOption) (*CustomDimension, error)
func (c *ManagementCustomDimensionsUpdateCall) Fields(s ...googleapi.Field) *ManagementCustomDimensionsUpdateCall
func (c *ManagementCustomDimensionsUpdateCall) Header() http.Header
func (c *ManagementCustomDimensionsUpdateCall) IgnoreCustomDataSourceLinks(ignoreCustomDataSourceLinks bool) *ManagementCustomDimensionsUpdateCall
type ManagementCustomMetricsGetCall
func (c *ManagementCustomMetricsGetCall) Context(ctx context.Context) *ManagementCustomMetricsGetCall
func (c *ManagementCustomMetricsGetCall) Do(opts ...googleapi.CallOption) (*CustomMetric, error)
func (c *ManagementCustomMetricsGetCall) Fields(s ...googleapi.Field) *ManagementCustomMetricsGetCall
func (c *ManagementCustomMetricsGetCall) Header() http.Header
func (c *ManagementCustomMetricsGetCall) IfNoneMatch(entityTag string) *ManagementCustomMetricsGetCall
type ManagementCustomMetricsInsertCall
func (c *ManagementCustomMetricsInsertCall) Context(ctx context.Context) *ManagementCustomMetricsInsertCall
func (c *ManagementCustomMetricsInsertCall) Do(opts ...googleapi.CallOption) (*CustomMetric, error)
func (c *ManagementCustomMetricsInsertCall) Fields(s ...googleapi.Field) *ManagementCustomMetricsInsertCall
func (c *ManagementCustomMetricsInsertCall) Header() http.Header
type ManagementCustomMetricsListCall
func (c *ManagementCustomMetricsListCall) Context(ctx context.Context) *ManagementCustomMetricsListCall
func (c *ManagementCustomMetricsListCall) Do(opts ...googleapi.CallOption) (*CustomMetrics, error)
func (c *ManagementCustomMetricsListCall) Fields(s ...googleapi.Field) *ManagementCustomMetricsListCall
func (c *ManagementCustomMetricsListCall) Header() http.Header
func (c *ManagementCustomMetricsListCall) IfNoneMatch(entityTag string) *ManagementCustomMetricsListCall
func (c *ManagementCustomMetricsListCall) MaxResults(maxResults int64) *ManagementCustomMetricsListCall
func (c *ManagementCustomMetricsListCall) StartIndex(startIndex int64) *ManagementCustomMetricsListCall
type ManagementCustomMetricsPatchCall
func (c *ManagementCustomMetricsPatchCall) Context(ctx context.Context) *ManagementCustomMetricsPatchCall
func (c *ManagementCustomMetricsPatchCall) Do(opts ...googleapi.CallOption) (*CustomMetric, error)
func (c *ManagementCustomMetricsPatchCall) Fields(s ...googleapi.Field) *ManagementCustomMetricsPatchCall
func (c *ManagementCustomMetricsPatchCall) Header() http.Header
func (c *ManagementCustomMetricsPatchCall) IgnoreCustomDataSourceLinks(ignoreCustomDataSourceLinks bool) *ManagementCustomMetricsPatchCall
type ManagementCustomMetricsService
func NewManagementCustomMetricsService(s *Service) *ManagementCustomMetricsService
func (r *ManagementCustomMetricsService) Get(accountId string, webPropertyId string, customMetricId string) *ManagementCustomMetricsGetCall
func (r *ManagementCustomMetricsService) Insert(accountId string, webPropertyId string, custommetric *CustomMetric) *ManagementCustomMetricsInsertCall
func (r *ManagementCustomMetricsService) List(accountId string, webPropertyId string) *ManagementCustomMetricsListCall
func (r *ManagementCustomMetricsService) Patch(accountId string, webPropertyId string, customMetricId string, ...) *ManagementCustomMetricsPatchCall
func (r *ManagementCustomMetricsService) Update(accountId string, webPropertyId string, customMetricId string, ...) *ManagementCustomMetricsUpdateCall
type ManagementCustomMetricsUpdateCall
func (c *ManagementCustomMetricsUpdateCall) Context(ctx context.Context) *ManagementCustomMetricsUpdateCall
func (c *ManagementCustomMetricsUpdateCall) Do(opts ...googleapi.CallOption) (*CustomMetric, error)
func (c *ManagementCustomMetricsUpdateCall) Fields(s ...googleapi.Field) *ManagementCustomMetricsUpdateCall
func (c *ManagementCustomMetricsUpdateCall) Header() http.Header
func (c *ManagementCustomMetricsUpdateCall) IgnoreCustomDataSourceLinks(ignoreCustomDataSourceLinks bool) *ManagementCustomMetricsUpdateCall
type ManagementExperimentsDeleteCall
func (c *ManagementExperimentsDeleteCall) Context(ctx context.Context) *ManagementExperimentsDeleteCall
func (c *ManagementExperimentsDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *ManagementExperimentsDeleteCall) Fields(s ...googleapi.Field) *ManagementExperimentsDeleteCall
func (c *ManagementExperimentsDeleteCall) Header() http.Header
type ManagementExperimentsGetCall
func (c *ManagementExperimentsGetCall) Context(ctx context.Context) *ManagementExperimentsGetCall
func (c *ManagementExperimentsGetCall) Do(opts ...googleapi.CallOption) (*Experiment, error)
func (c *ManagementExperimentsGetCall) Fields(s ...googleapi.Field) *ManagementExperimentsGetCall
func (c *ManagementExperimentsGetCall) Header() http.Header
func (c *ManagementExperimentsGetCall) IfNoneMatch(entityTag string) *ManagementExperimentsGetCall
type ManagementExperimentsInsertCall
func (c *ManagementExperimentsInsertCall) Context(ctx context.Context) *ManagementExperimentsInsertCall
func (c *ManagementExperimentsInsertCall) Do(opts ...googleapi.CallOption) (*Experiment, error)
func (c *ManagementExperimentsInsertCall) Fields(s ...googleapi.Field) *ManagementExperimentsInsertCall
func (c *ManagementExperimentsInsertCall) Header() http.Header
type ManagementExperimentsListCall
func (c *ManagementExperimentsListCall) Context(ctx context.Context) *ManagementExperimentsListCall
func (c *ManagementExperimentsListCall) Do(opts ...googleapi.CallOption) (*Experiments, error)
func (c *ManagementExperimentsListCall) Fields(s ...googleapi.Field) *ManagementExperimentsListCall
func (c *ManagementExperimentsListCall) Header() http.Header
func (c *ManagementExperimentsListCall) IfNoneMatch(entityTag string) *ManagementExperimentsListCall
func (c *ManagementExperimentsListCall) MaxResults(maxResults int64) *ManagementExperimentsListCall
func (c *ManagementExperimentsListCall) StartIndex(startIndex int64) *ManagementExperimentsListCall
type ManagementExperimentsPatchCall
func (c *ManagementExperimentsPatchCall) Context(ctx context.Context) *ManagementExperimentsPatchCall
func (c *ManagementExperimentsPatchCall) Do(opts ...googleapi.CallOption) (*Experiment, error)
func (c *ManagementExperimentsPatchCall) Fields(s ...googleapi.Field) *ManagementExperimentsPatchCall
func (c *ManagementExperimentsPatchCall) Header() http.Header
type ManagementExperimentsService
func NewManagementExperimentsService(s *Service) *ManagementExperimentsService
func (r *ManagementExperimentsService) Delete(accountId string, webPropertyId string, profileId string, experimentId string) *ManagementExperimentsDeleteCall
func (r *ManagementExperimentsService) Get(accountId string, webPropertyId string, profileId string, experimentId string) *ManagementExperimentsGetCall
func (r *ManagementExperimentsService) Insert(accountId string, webPropertyId string, profileId string, ...) *ManagementExperimentsInsertCall
func (r *ManagementExperimentsService) List(accountId string, webPropertyId string, profileId string) *ManagementExperimentsListCall
func (r *ManagementExperimentsService) Patch(accountId string, webPropertyId string, profileId string, experimentId string, ...) *ManagementExperimentsPatchCall
func (r *ManagementExperimentsService) Update(accountId string, webPropertyId string, profileId string, experimentId string, ...) *ManagementExperimentsUpdateCall
type ManagementExperimentsUpdateCall
func (c *ManagementExperimentsUpdateCall) Context(ctx context.Context) *ManagementExperimentsUpdateCall
func (c *ManagementExperimentsUpdateCall) Do(opts ...googleapi.CallOption) (*Experiment, error)
func (c *ManagementExperimentsUpdateCall) Fields(s ...googleapi.Field) *ManagementExperimentsUpdateCall
func (c *ManagementExperimentsUpdateCall) Header() http.Header
type ManagementFiltersDeleteCall
func (c *ManagementFiltersDeleteCall) Context(ctx context.Context) *ManagementFiltersDeleteCall
func (c *ManagementFiltersDeleteCall) Do(opts ...googleapi.CallOption) (*Filter, error)
func (c *ManagementFiltersDeleteCall) Fields(s ...googleapi.Field) *ManagementFiltersDeleteCall
func (c *ManagementFiltersDeleteCall) Header() http.Header
type ManagementFiltersGetCall
func (c *ManagementFiltersGetCall) Context(ctx context.Context) *ManagementFiltersGetCall
func (c *ManagementFiltersGetCall) Do(opts ...googleapi.CallOption) (*Filter, error)
func (c *ManagementFiltersGetCall) Fields(s ...googleapi.Field) *ManagementFiltersGetCall
func (c *ManagementFiltersGetCall) Header() http.Header
func (c *ManagementFiltersGetCall) IfNoneMatch(entityTag string) *ManagementFiltersGetCall
type ManagementFiltersInsertCall
func (c *ManagementFiltersInsertCall) Context(ctx context.Context) *ManagementFiltersInsertCall
func (c *ManagementFiltersInsertCall) Do(opts ...googleapi.CallOption) (*Filter, error)
func (c *ManagementFiltersInsertCall) Fields(s ...googleapi.Field) *ManagementFiltersInsertCall
func (c *ManagementFiltersInsertCall) Header() http.Header
type ManagementFiltersListCall
func (c *ManagementFiltersListCall) Context(ctx context.Context) *ManagementFiltersListCall
func (c *ManagementFiltersListCall) Do(opts ...googleapi.CallOption) (*Filters, error)
func (c *ManagementFiltersListCall) Fields(s ...googleapi.Field) *ManagementFiltersListCall
func (c *ManagementFiltersListCall) Header() http.Header
func (c *ManagementFiltersListCall) IfNoneMatch(entityTag string) *ManagementFiltersListCall
func (c *ManagementFiltersListCall) MaxResults(maxResults int64) *ManagementFiltersListCall
func (c *ManagementFiltersListCall) StartIndex(startIndex int64) *ManagementFiltersListCall
type ManagementFiltersPatchCall
func (c *ManagementFiltersPatchCall) Context(ctx context.Context) *ManagementFiltersPatchCall
func (c *ManagementFiltersPatchCall) Do(opts ...googleapi.CallOption) (*Filter, error)
func (c *ManagementFiltersPatchCall) Fields(s ...googleapi.Field) *ManagementFiltersPatchCall
func (c *ManagementFiltersPatchCall) Header() http.Header
type ManagementFiltersService
func NewManagementFiltersService(s *Service) *ManagementFiltersService
func (r *ManagementFiltersService) Delete(accountId string, filterId string) *ManagementFiltersDeleteCall
func (r *ManagementFiltersService) Get(accountId string, filterId string) *ManagementFiltersGetCall
func (r *ManagementFiltersService) Insert(accountId string, filter *Filter) *ManagementFiltersInsertCall
func (r *ManagementFiltersService) List(accountId string) *ManagementFiltersListCall
func (r *ManagementFiltersService) Patch(accountId string, filterId string, filter *Filter) *ManagementFiltersPatchCall
func (r *ManagementFiltersService) Update(accountId string, filterId string, filter *Filter) *ManagementFiltersUpdateCall
type ManagementFiltersUpdateCall
func (c *ManagementFiltersUpdateCall) Context(ctx context.Context) *ManagementFiltersUpdateCall
func (c *ManagementFiltersUpdateCall) Do(opts ...googleapi.CallOption) (*Filter, error)
func (c *ManagementFiltersUpdateCall) Fields(s ...googleapi.Field) *ManagementFiltersUpdateCall
func (c *ManagementFiltersUpdateCall) Header() http.Header
type ManagementGoalsGetCall
func (c *ManagementGoalsGetCall) Context(ctx context.Context) *ManagementGoalsGetCall
func (c *ManagementGoalsGetCall) Do(opts ...googleapi.CallOption) (*Goal, error)
func (c *ManagementGoalsGetCall) Fields(s ...googleapi.Field) *ManagementGoalsGetCall
func (c *ManagementGoalsGetCall) Header() http.Header
func (c *ManagementGoalsGetCall) IfNoneMatch(entityTag string) *ManagementGoalsGetCall
type ManagementGoalsInsertCall
func (c *ManagementGoalsInsertCall) Context(ctx context.Context) *ManagementGoalsInsertCall
func (c *ManagementGoalsInsertCall) Do(opts ...googleapi.CallOption) (*Goal, error)
func (c *ManagementGoalsInsertCall) Fields(s ...googleapi.Field) *ManagementGoalsInsertCall
func (c *ManagementGoalsInsertCall) Header() http.Header
type ManagementGoalsListCall
func (c *ManagementGoalsListCall) Context(ctx context.Context) *ManagementGoalsListCall
func (c *ManagementGoalsListCall) Do(opts ...googleapi.CallOption) (*Goals, error)
func (c *ManagementGoalsListCall) Fields(s ...googleapi.Field) *ManagementGoalsListCall
func (c *ManagementGoalsListCall) Header() http.Header
func (c *ManagementGoalsListCall) IfNoneMatch(entityTag string) *ManagementGoalsListCall
func (c *ManagementGoalsListCall) MaxResults(maxResults int64) *ManagementGoalsListCall
func (c *ManagementGoalsListCall) StartIndex(startIndex int64) *ManagementGoalsListCall
type ManagementGoalsPatchCall
func (c *ManagementGoalsPatchCall) Context(ctx context.Context) *ManagementGoalsPatchCall
func (c *ManagementGoalsPatchCall) Do(opts ...googleapi.CallOption) (*Goal, error)
func (c *ManagementGoalsPatchCall) Fields(s ...googleapi.Field) *ManagementGoalsPatchCall
func (c *ManagementGoalsPatchCall) Header() http.Header
type ManagementGoalsService
func NewManagementGoalsService(s *Service) *ManagementGoalsService
func (r *ManagementGoalsService) Get(accountId string, webPropertyId string, profileId string, goalId string) *ManagementGoalsGetCall
func (r *ManagementGoalsService) Insert(accountId string, webPropertyId string, profileId string, goal *Goal) *ManagementGoalsInsertCall
func (r *ManagementGoalsService) List(accountId string, webPropertyId string, profileId string) *ManagementGoalsListCall
func (r *ManagementGoalsService) Patch(accountId string, webPropertyId string, profileId string, goalId string, ...) *ManagementGoalsPatchCall
func (r *ManagementGoalsService) Update(accountId string, webPropertyId string, profileId string, goalId string, ...) *ManagementGoalsUpdateCall
type ManagementGoalsUpdateCall
func (c *ManagementGoalsUpdateCall) Context(ctx context.Context) *ManagementGoalsUpdateCall
func (c *ManagementGoalsUpdateCall) Do(opts ...googleapi.CallOption) (*Goal, error)
func (c *ManagementGoalsUpdateCall) Fields(s ...googleapi.Field) *ManagementGoalsUpdateCall
func (c *ManagementGoalsUpdateCall) Header() http.Header
type ManagementProfileFilterLinksDeleteCall
func (c *ManagementProfileFilterLinksDeleteCall) Context(ctx context.Context) *ManagementProfileFilterLinksDeleteCall
func (c *ManagementProfileFilterLinksDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *ManagementProfileFilterLinksDeleteCall) Fields(s ...googleapi.Field) *ManagementProfileFilterLinksDeleteCall
func (c *ManagementProfileFilterLinksDeleteCall) Header() http.Header
type ManagementProfileFilterLinksGetCall
func (c *ManagementProfileFilterLinksGetCall) Context(ctx context.Context) *ManagementProfileFilterLinksGetCall
func (c *ManagementProfileFilterLinksGetCall) Do(opts ...googleapi.CallOption) (*ProfileFilterLink, error)
func (c *ManagementProfileFilterLinksGetCall) Fields(s ...googleapi.Field) *ManagementProfileFilterLinksGetCall
func (c *ManagementProfileFilterLinksGetCall) Header() http.Header
func (c *ManagementProfileFilterLinksGetCall) IfNoneMatch(entityTag string) *ManagementProfileFilterLinksGetCall
type ManagementProfileFilterLinksInsertCall
func (c *ManagementProfileFilterLinksInsertCall) Context(ctx context.Context) *ManagementProfileFilterLinksInsertCall
func (c *ManagementProfileFilterLinksInsertCall) Do(opts ...googleapi.CallOption) (*ProfileFilterLink, error)
func (c *ManagementProfileFilterLinksInsertCall) Fields(s ...googleapi.Field) *ManagementProfileFilterLinksInsertCall
func (c *ManagementProfileFilterLinksInsertCall) Header() http.Header
type ManagementProfileFilterLinksListCall
func (c *ManagementProfileFilterLinksListCall) Context(ctx context.Context) *ManagementProfileFilterLinksListCall
func (c *ManagementProfileFilterLinksListCall) Do(opts ...googleapi.CallOption) (*ProfileFilterLinks, error)
func (c *ManagementProfileFilterLinksListCall) Fields(s ...googleapi.Field) *ManagementProfileFilterLinksListCall
func (c *ManagementProfileFilterLinksListCall) Header() http.Header
func (c *ManagementProfileFilterLinksListCall) IfNoneMatch(entityTag string) *ManagementProfileFilterLinksListCall
func (c *ManagementProfileFilterLinksListCall) MaxResults(maxResults int64) *ManagementProfileFilterLinksListCall
func (c *ManagementProfileFilterLinksListCall) StartIndex(startIndex int64) *ManagementProfileFilterLinksListCall
type ManagementProfileFilterLinksPatchCall
func (c *ManagementProfileFilterLinksPatchCall) Context(ctx context.Context) *ManagementProfileFilterLinksPatchCall
func (c *ManagementProfileFilterLinksPatchCall) Do(opts ...googleapi.CallOption) (*ProfileFilterLink, error)
func (c *ManagementProfileFilterLinksPatchCall) Fields(s ...googleapi.Field) *ManagementProfileFilterLinksPatchCall
func (c *ManagementProfileFilterLinksPatchCall) Header() http.Header
type ManagementProfileFilterLinksService
func NewManagementProfileFilterLinksService(s *Service) *ManagementProfileFilterLinksService
func (r *ManagementProfileFilterLinksService) Delete(accountId string, webPropertyId string, profileId string, linkId string) *ManagementProfileFilterLinksDeleteCall
func (r *ManagementProfileFilterLinksService) Get(accountId string, webPropertyId string, profileId string, linkId string) *ManagementProfileFilterLinksGetCall
func (r *ManagementProfileFilterLinksService) Insert(accountId string, webPropertyId string, profileId string, ...) *ManagementProfileFilterLinksInsertCall
func (r *ManagementProfileFilterLinksService) List(accountId string, webPropertyId string, profileId string) *ManagementProfileFilterLinksListCall
func (r *ManagementProfileFilterLinksService) Patch(accountId string, webPropertyId string, profileId string, linkId string, ...) *ManagementProfileFilterLinksPatchCall
func (r *ManagementProfileFilterLinksService) Update(accountId string, webPropertyId string, profileId string, linkId string, ...) *ManagementProfileFilterLinksUpdateCall
type ManagementProfileFilterLinksUpdateCall
func (c *ManagementProfileFilterLinksUpdateCall) Context(ctx context.Context) *ManagementProfileFilterLinksUpdateCall
func (c *ManagementProfileFilterLinksUpdateCall) Do(opts ...googleapi.CallOption) (*ProfileFilterLink, error)
func (c *ManagementProfileFilterLinksUpdateCall) Fields(s ...googleapi.Field) *ManagementProfileFilterLinksUpdateCall
func (c *ManagementProfileFilterLinksUpdateCall) Header() http.Header
type ManagementProfileUserLinksDeleteCall
func (c *ManagementProfileUserLinksDeleteCall) Context(ctx context.Context) *ManagementProfileUserLinksDeleteCall
func (c *ManagementProfileUserLinksDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *ManagementProfileUserLinksDeleteCall) Fields(s ...googleapi.Field) *ManagementProfileUserLinksDeleteCall
func (c *ManagementProfileUserLinksDeleteCall) Header() http.Header
type ManagementProfileUserLinksInsertCall
func (c *ManagementProfileUserLinksInsertCall) Context(ctx context.Context) *ManagementProfileUserLinksInsertCall
func (c *ManagementProfileUserLinksInsertCall) Do(opts ...googleapi.CallOption) (*EntityUserLink, error)
func (c *ManagementProfileUserLinksInsertCall) Fields(s ...googleapi.Field) *ManagementProfileUserLinksInsertCall
func (c *ManagementProfileUserLinksInsertCall) Header() http.Header
type ManagementProfileUserLinksListCall
func (c *ManagementProfileUserLinksListCall) Context(ctx context.Context) *ManagementProfileUserLinksListCall
func (c *ManagementProfileUserLinksListCall) Do(opts ...googleapi.CallOption) (*EntityUserLinks, error)
func (c *ManagementProfileUserLinksListCall) Fields(s ...googleapi.Field) *ManagementProfileUserLinksListCall
func (c *ManagementProfileUserLinksListCall) Header() http.Header
func (c *ManagementProfileUserLinksListCall) IfNoneMatch(entityTag string) *ManagementProfileUserLinksListCall
func (c *ManagementProfileUserLinksListCall) MaxResults(maxResults int64) *ManagementProfileUserLinksListCall
func (c *ManagementProfileUserLinksListCall) StartIndex(startIndex int64) *ManagementProfileUserLinksListCall
type ManagementProfileUserLinksService
func NewManagementProfileUserLinksService(s *Service) *ManagementProfileUserLinksService
func (r *ManagementProfileUserLinksService) Delete(accountId string, webPropertyId string, profileId string, linkId string) *ManagementProfileUserLinksDeleteCall
func (r *ManagementProfileUserLinksService) Insert(accountId string, webPropertyId string, profileId string, ...) *ManagementProfileUserLinksInsertCall
func (r *ManagementProfileUserLinksService) List(accountId string, webPropertyId string, profileId string) *ManagementProfileUserLinksListCall
func (r *ManagementProfileUserLinksService) Update(accountId string, webPropertyId string, profileId string, linkId string, ...) *ManagementProfileUserLinksUpdateCall
type ManagementProfileUserLinksUpdateCall
func (c *ManagementProfileUserLinksUpdateCall) Context(ctx context.Context) *ManagementProfileUserLinksUpdateCall
func (c *ManagementProfileUserLinksUpdateCall) Do(opts ...googleapi.CallOption) (*EntityUserLink, error)
func (c *ManagementProfileUserLinksUpdateCall) Fields(s ...googleapi.Field) *ManagementProfileUserLinksUpdateCall
func (c *ManagementProfileUserLinksUpdateCall) Header() http.Header
type ManagementProfilesDeleteCall
func (c *ManagementProfilesDeleteCall) Context(ctx context.Context) *ManagementProfilesDeleteCall
func (c *ManagementProfilesDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *ManagementProfilesDeleteCall) Fields(s ...googleapi.Field) *ManagementProfilesDeleteCall
func (c *ManagementProfilesDeleteCall) Header() http.Header
type ManagementProfilesGetCall
func (c *ManagementProfilesGetCall) Context(ctx context.Context) *ManagementProfilesGetCall
func (c *ManagementProfilesGetCall) Do(opts ...googleapi.CallOption) (*Profile, error)
func (c *ManagementProfilesGetCall) Fields(s ...googleapi.Field) *ManagementProfilesGetCall
func (c *ManagementProfilesGetCall) Header() http.Header
func (c *ManagementProfilesGetCall) IfNoneMatch(entityTag string) *ManagementProfilesGetCall
type ManagementProfilesInsertCall
func (c *ManagementProfilesInsertCall) Context(ctx context.Context) *ManagementProfilesInsertCall
func (c *ManagementProfilesInsertCall) Do(opts ...googleapi.CallOption) (*Profile, error)
func (c *ManagementProfilesInsertCall) Fields(s ...googleapi.Field) *ManagementProfilesInsertCall
func (c *ManagementProfilesInsertCall) Header() http.Header
type ManagementProfilesListCall
func (c *ManagementProfilesListCall) Context(ctx context.Context) *ManagementProfilesListCall
func (c *ManagementProfilesListCall) Do(opts ...googleapi.CallOption) (*Profiles, error)
func (c *ManagementProfilesListCall) Fields(s ...googleapi.Field) *ManagementProfilesListCall
func (c *ManagementProfilesListCall) Header() http.Header
func (c *ManagementProfilesListCall) IfNoneMatch(entityTag string) *ManagementProfilesListCall
func (c *ManagementProfilesListCall) MaxResults(maxResults int64) *ManagementProfilesListCall
func (c *ManagementProfilesListCall) StartIndex(startIndex int64) *ManagementProfilesListCall
type ManagementProfilesPatchCall
func (c *ManagementProfilesPatchCall) Context(ctx context.Context) *ManagementProfilesPatchCall
func (c *ManagementProfilesPatchCall) Do(opts ...googleapi.CallOption) (*Profile, error)
func (c *ManagementProfilesPatchCall) Fields(s ...googleapi.Field) *ManagementProfilesPatchCall
func (c *ManagementProfilesPatchCall) Header() http.Header
type ManagementProfilesService
func NewManagementProfilesService(s *Service) *ManagementProfilesService
func (r *ManagementProfilesService) Delete(accountId string, webPropertyId string, profileId string) *ManagementProfilesDeleteCall
func (r *ManagementProfilesService) Get(accountId string, webPropertyId string, profileId string) *ManagementProfilesGetCall
func (r *ManagementProfilesService) Insert(accountId string, webPropertyId string, profile *Profile) *ManagementProfilesInsertCall
func (r *ManagementProfilesService) List(accountId string, webPropertyId string) *ManagementProfilesListCall
func (r *ManagementProfilesService) Patch(accountId string, webPropertyId string, profileId string, profile *Profile) *ManagementProfilesPatchCall
func (r *ManagementProfilesService) Update(accountId string, webPropertyId string, profileId string, profile *Profile) *ManagementProfilesUpdateCall
type ManagementProfilesUpdateCall
func (c *ManagementProfilesUpdateCall) Context(ctx context.Context) *ManagementProfilesUpdateCall
func (c *ManagementProfilesUpdateCall) Do(opts ...googleapi.CallOption) (*Profile, error)
func (c *ManagementProfilesUpdateCall) Fields(s ...googleapi.Field) *ManagementProfilesUpdateCall
func (c *ManagementProfilesUpdateCall) Header() http.Header
type ManagementRemarketingAudienceDeleteCall
func (c *ManagementRemarketingAudienceDeleteCall) Context(ctx context.Context) *ManagementRemarketingAudienceDeleteCall
func (c *ManagementRemarketingAudienceDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *ManagementRemarketingAudienceDeleteCall) Fields(s ...googleapi.Field) *ManagementRemarketingAudienceDeleteCall
func (c *ManagementRemarketingAudienceDeleteCall) Header() http.Header
type ManagementRemarketingAudienceGetCall
func (c *ManagementRemarketingAudienceGetCall) Context(ctx context.Context) *ManagementRemarketingAudienceGetCall
func (c *ManagementRemarketingAudienceGetCall) Do(opts ...googleapi.CallOption) (*RemarketingAudience, error)
func (c *ManagementRemarketingAudienceGetCall) Fields(s ...googleapi.Field) *ManagementRemarketingAudienceGetCall
func (c *ManagementRemarketingAudienceGetCall) Header() http.Header
func (c *ManagementRemarketingAudienceGetCall) IfNoneMatch(entityTag string) *ManagementRemarketingAudienceGetCall
type ManagementRemarketingAudienceInsertCall
func (c *ManagementRemarketingAudienceInsertCall) Context(ctx context.Context) *ManagementRemarketingAudienceInsertCall
func (c *ManagementRemarketingAudienceInsertCall) Do(opts ...googleapi.CallOption) (*RemarketingAudience, error)
func (c *ManagementRemarketingAudienceInsertCall) Fields(s ...googleapi.Field) *ManagementRemarketingAudienceInsertCall
func (c *ManagementRemarketingAudienceInsertCall) Header() http.Header
type ManagementRemarketingAudienceListCall
func (c *ManagementRemarketingAudienceListCall) Context(ctx context.Context) *ManagementRemarketingAudienceListCall
func (c *ManagementRemarketingAudienceListCall) Do(opts ...googleapi.CallOption) (*RemarketingAudiences, error)
func (c *ManagementRemarketingAudienceListCall) Fields(s ...googleapi.Field) *ManagementRemarketingAudienceListCall
func (c *ManagementRemarketingAudienceListCall) Header() http.Header
func (c *ManagementRemarketingAudienceListCall) IfNoneMatch(entityTag string) *ManagementRemarketingAudienceListCall
func (c *ManagementRemarketingAudienceListCall) MaxResults(maxResults int64) *ManagementRemarketingAudienceListCall
func (c *ManagementRemarketingAudienceListCall) StartIndex(startIndex int64) *ManagementRemarketingAudienceListCall
func (c *ManagementRemarketingAudienceListCall) Type(type_ string) *ManagementRemarketingAudienceListCall
type ManagementRemarketingAudiencePatchCall
func (c *ManagementRemarketingAudiencePatchCall) Context(ctx context.Context) *ManagementRemarketingAudiencePatchCall
func (c *ManagementRemarketingAudiencePatchCall) Do(opts ...googleapi.CallOption) (*RemarketingAudience, error)
func (c *ManagementRemarketingAudiencePatchCall) Fields(s ...googleapi.Field) *ManagementRemarketingAudiencePatchCall
func (c *ManagementRemarketingAudiencePatchCall) Header() http.Header
type ManagementRemarketingAudienceService
func NewManagementRemarketingAudienceService(s *Service) *ManagementRemarketingAudienceService
func (r *ManagementRemarketingAudienceService) Delete(accountId string, webPropertyId string, remarketingAudienceId string) *ManagementRemarketingAudienceDeleteCall
func (r *ManagementRemarketingAudienceService) Get(accountId string, webPropertyId string, remarketingAudienceId string) *ManagementRemarketingAudienceGetCall
func (r *ManagementRemarketingAudienceService) Insert(accountId string, webPropertyId string, ...) *ManagementRemarketingAudienceInsertCall
func (r *ManagementRemarketingAudienceService) List(accountId string, webPropertyId string) *ManagementRemarketingAudienceListCall
func (r *ManagementRemarketingAudienceService) Patch(accountId string, webPropertyId string, remarketingAudienceId string, ...) *ManagementRemarketingAudiencePatchCall
func (r *ManagementRemarketingAudienceService) Update(accountId string, webPropertyId string, remarketingAudienceId string, ...) *ManagementRemarketingAudienceUpdateCall
type ManagementRemarketingAudienceUpdateCall
func (c *ManagementRemarketingAudienceUpdateCall) Context(ctx context.Context) *ManagementRemarketingAudienceUpdateCall
func (c *ManagementRemarketingAudienceUpdateCall) Do(opts ...googleapi.CallOption) (*RemarketingAudience, error)
func (c *ManagementRemarketingAudienceUpdateCall) Fields(s ...googleapi.Field) *ManagementRemarketingAudienceUpdateCall
func (c *ManagementRemarketingAudienceUpdateCall) Header() http.Header
type ManagementSegmentsListCall
func (c *ManagementSegmentsListCall) Context(ctx context.Context) *ManagementSegmentsListCall
func (c *ManagementSegmentsListCall) Do(opts ...googleapi.CallOption) (*Segments, error)
func (c *ManagementSegmentsListCall) Fields(s ...googleapi.Field) *ManagementSegmentsListCall
func (c *ManagementSegmentsListCall) Header() http.Header
func (c *ManagementSegmentsListCall) IfNoneMatch(entityTag string) *ManagementSegmentsListCall
func (c *ManagementSegmentsListCall) MaxResults(maxResults int64) *ManagementSegmentsListCall
func (c *ManagementSegmentsListCall) StartIndex(startIndex int64) *ManagementSegmentsListCall
type ManagementSegmentsService
func NewManagementSegmentsService(s *Service) *ManagementSegmentsService
func (r *ManagementSegmentsService) List() *ManagementSegmentsListCall
type ManagementService
func NewManagementService(s *Service) *ManagementService
type ManagementUnsampledReportsDeleteCall
func (c *ManagementUnsampledReportsDeleteCall) Context(ctx context.Context) *ManagementUnsampledReportsDeleteCall
func (c *ManagementUnsampledReportsDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *ManagementUnsampledReportsDeleteCall) Fields(s ...googleapi.Field) *ManagementUnsampledReportsDeleteCall
func (c *ManagementUnsampledReportsDeleteCall) Header() http.Header
type ManagementUnsampledReportsGetCall
func (c *ManagementUnsampledReportsGetCall) Context(ctx context.Context) *ManagementUnsampledReportsGetCall
func (c *ManagementUnsampledReportsGetCall) Do(opts ...googleapi.CallOption) (*UnsampledReport, error)
func (c *ManagementUnsampledReportsGetCall) Fields(s ...googleapi.Field) *ManagementUnsampledReportsGetCall
func (c *ManagementUnsampledReportsGetCall) Header() http.Header
func (c *ManagementUnsampledReportsGetCall) IfNoneMatch(entityTag string) *ManagementUnsampledReportsGetCall
type ManagementUnsampledReportsInsertCall
func (c *ManagementUnsampledReportsInsertCall) Context(ctx context.Context) *ManagementUnsampledReportsInsertCall
func (c *ManagementUnsampledReportsInsertCall) Do(opts ...googleapi.CallOption) (*UnsampledReport, error)
func (c *ManagementUnsampledReportsInsertCall) Fields(s ...googleapi.Field) *ManagementUnsampledReportsInsertCall
func (c *ManagementUnsampledReportsInsertCall) Header() http.Header
type ManagementUnsampledReportsListCall
func (c *ManagementUnsampledReportsListCall) Context(ctx context.Context) *ManagementUnsampledReportsListCall
func (c *ManagementUnsampledReportsListCall) Do(opts ...googleapi.CallOption) (*UnsampledReports, error)
func (c *ManagementUnsampledReportsListCall) Fields(s ...googleapi.Field) *ManagementUnsampledReportsListCall
func (c *ManagementUnsampledReportsListCall) Header() http.Header
func (c *ManagementUnsampledReportsListCall) IfNoneMatch(entityTag string) *ManagementUnsampledReportsListCall
func (c *ManagementUnsampledReportsListCall) MaxResults(maxResults int64) *ManagementUnsampledReportsListCall
func (c *ManagementUnsampledReportsListCall) StartIndex(startIndex int64) *ManagementUnsampledReportsListCall
type ManagementUnsampledReportsService
func NewManagementUnsampledReportsService(s *Service) *ManagementUnsampledReportsService
func (r *ManagementUnsampledReportsService) Delete(accountId string, webPropertyId string, profileId string, ...) *ManagementUnsampledReportsDeleteCall
func (r *ManagementUnsampledReportsService) Get(accountId string, webPropertyId string, profileId string, ...) *ManagementUnsampledReportsGetCall
func (r *ManagementUnsampledReportsService) Insert(accountId string, webPropertyId string, profileId string, ...) *ManagementUnsampledReportsInsertCall
func (r *ManagementUnsampledReportsService) List(accountId string, webPropertyId string, profileId string) *ManagementUnsampledReportsListCall
type ManagementUploadsDeleteUploadDataCall
func (c *ManagementUploadsDeleteUploadDataCall) Context(ctx context.Context) *ManagementUploadsDeleteUploadDataCall
func (c *ManagementUploadsDeleteUploadDataCall) Do(opts ...googleapi.CallOption) error
func (c *ManagementUploadsDeleteUploadDataCall) Fields(s ...googleapi.Field) *ManagementUploadsDeleteUploadDataCall
func (c *ManagementUploadsDeleteUploadDataCall) Header() http.Header
type ManagementUploadsGetCall
func (c *ManagementUploadsGetCall) Context(ctx context.Context) *ManagementUploadsGetCall
func (c *ManagementUploadsGetCall) Do(opts ...googleapi.CallOption) (*Upload, error)
func (c *ManagementUploadsGetCall) Fields(s ...googleapi.Field) *ManagementUploadsGetCall
func (c *ManagementUploadsGetCall) Header() http.Header
func (c *ManagementUploadsGetCall) IfNoneMatch(entityTag string) *ManagementUploadsGetCall
type ManagementUploadsListCall
func (c *ManagementUploadsListCall) Context(ctx context.Context) *ManagementUploadsListCall
func (c *ManagementUploadsListCall) Do(opts ...googleapi.CallOption) (*Uploads, error)
func (c *ManagementUploadsListCall) Fields(s ...googleapi.Field) *ManagementUploadsListCall
func (c *ManagementUploadsListCall) Header() http.Header
func (c *ManagementUploadsListCall) IfNoneMatch(entityTag string) *ManagementUploadsListCall
func (c *ManagementUploadsListCall) MaxResults(maxResults int64) *ManagementUploadsListCall
func (c *ManagementUploadsListCall) StartIndex(startIndex int64) *ManagementUploadsListCall
type ManagementUploadsService
func NewManagementUploadsService(s *Service) *ManagementUploadsService
func (r *ManagementUploadsService) DeleteUploadData(accountId string, webPropertyId string, customDataSourceId string, ...) *ManagementUploadsDeleteUploadDataCall
func (r *ManagementUploadsService) Get(accountId string, webPropertyId string, customDataSourceId string, ...) *ManagementUploadsGetCall
func (r *ManagementUploadsService) List(accountId string, webPropertyId string, customDataSourceId string) *ManagementUploadsListCall
func (r *ManagementUploadsService) UploadData(accountId string, webPropertyId string, customDataSourceId string) *ManagementUploadsUploadDataCall
type ManagementUploadsUploadDataCall
func (c *ManagementUploadsUploadDataCall) Context(ctx context.Context) *ManagementUploadsUploadDataCall
func (c *ManagementUploadsUploadDataCall) Do(opts ...googleapi.CallOption) (*Upload, error)
func (c *ManagementUploadsUploadDataCall) Fields(s ...googleapi.Field) *ManagementUploadsUploadDataCall
func (c *ManagementUploadsUploadDataCall) Header() http.Header
func (c *ManagementUploadsUploadDataCall) Media(r io.Reader, options ...googleapi.MediaOption) *ManagementUploadsUploadDataCall
func (c *ManagementUploadsUploadDataCall) ProgressUpdater(pu googleapi.ProgressUpdater) *ManagementUploadsUploadDataCall
func (c *ManagementUploadsUploadDataCall) ResumableMedia(ctx context.Context, r io.ReaderAt, size int64, mediaType string) *ManagementUploadsUploadDataCallDEPRECATED
type ManagementWebPropertyAdWordsLinksDeleteCall
func (c *ManagementWebPropertyAdWordsLinksDeleteCall) Context(ctx context.Context) *ManagementWebPropertyAdWordsLinksDeleteCall
func (c *ManagementWebPropertyAdWordsLinksDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *ManagementWebPropertyAdWordsLinksDeleteCall) Fields(s ...googleapi.Field) *ManagementWebPropertyAdWordsLinksDeleteCall
func (c *ManagementWebPropertyAdWordsLinksDeleteCall) Header() http.Header
type ManagementWebPropertyAdWordsLinksGetCall
func (c *ManagementWebPropertyAdWordsLinksGetCall) Context(ctx context.Context) *ManagementWebPropertyAdWordsLinksGetCall
func (c *ManagementWebPropertyAdWordsLinksGetCall) Do(opts ...googleapi.CallOption) (*EntityAdWordsLink, error)
func (c *ManagementWebPropertyAdWordsLinksGetCall) Fields(s ...googleapi.Field) *ManagementWebPropertyAdWordsLinksGetCall
func (c *ManagementWebPropertyAdWordsLinksGetCall) Header() http.Header
func (c *ManagementWebPropertyAdWordsLinksGetCall) IfNoneMatch(entityTag string) *ManagementWebPropertyAdWordsLinksGetCall
type ManagementWebPropertyAdWordsLinksInsertCall
func (c *ManagementWebPropertyAdWordsLinksInsertCall) Context(ctx context.Context) *ManagementWebPropertyAdWordsLinksInsertCall
func (c *ManagementWebPropertyAdWordsLinksInsertCall) Do(opts ...googleapi.CallOption) (*EntityAdWordsLink, error)
func (c *ManagementWebPropertyAdWordsLinksInsertCall) Fields(s ...googleapi.Field) *ManagementWebPropertyAdWordsLinksInsertCall
func (c *ManagementWebPropertyAdWordsLinksInsertCall) Header() http.Header
type ManagementWebPropertyAdWordsLinksListCall
func (c *ManagementWebPropertyAdWordsLinksListCall) Context(ctx context.Context) *ManagementWebPropertyAdWordsLinksListCall
func (c *ManagementWebPropertyAdWordsLinksListCall) Do(opts ...googleapi.CallOption) (*EntityAdWordsLinks, error)
func (c *ManagementWebPropertyAdWordsLinksListCall) Fields(s ...googleapi.Field) *ManagementWebPropertyAdWordsLinksListCall
func (c *ManagementWebPropertyAdWordsLinksListCall) Header() http.Header
func (c *ManagementWebPropertyAdWordsLinksListCall) IfNoneMatch(entityTag string) *ManagementWebPropertyAdWordsLinksListCall
func (c *ManagementWebPropertyAdWordsLinksListCall) MaxResults(maxResults int64) *ManagementWebPropertyAdWordsLinksListCall
func (c *ManagementWebPropertyAdWordsLinksListCall) StartIndex(startIndex int64) *ManagementWebPropertyAdWordsLinksListCall
type ManagementWebPropertyAdWordsLinksPatchCall
func (c *ManagementWebPropertyAdWordsLinksPatchCall) Context(ctx context.Context) *ManagementWebPropertyAdWordsLinksPatchCall
func (c *ManagementWebPropertyAdWordsLinksPatchCall) Do(opts ...googleapi.CallOption) (*EntityAdWordsLink, error)
func (c *ManagementWebPropertyAdWordsLinksPatchCall) Fields(s ...googleapi.Field) *ManagementWebPropertyAdWordsLinksPatchCall
func (c *ManagementWebPropertyAdWordsLinksPatchCall) Header() http.Header
type ManagementWebPropertyAdWordsLinksService
func NewManagementWebPropertyAdWordsLinksService(s *Service) *ManagementWebPropertyAdWordsLinksService
func (r *ManagementWebPropertyAdWordsLinksService) Delete(accountId string, webPropertyId string, webPropertyAdWordsLinkId string) *ManagementWebPropertyAdWordsLinksDeleteCall
func (r *ManagementWebPropertyAdWordsLinksService) Get(accountId string, webPropertyId string, webPropertyAdWordsLinkId string) *ManagementWebPropertyAdWordsLinksGetCall
func (r *ManagementWebPropertyAdWordsLinksService) Insert(accountId string, webPropertyId string, entityadwordslink *EntityAdWordsLink) *ManagementWebPropertyAdWordsLinksInsertCall
func (r *ManagementWebPropertyAdWordsLinksService) List(accountId string, webPropertyId string) *ManagementWebPropertyAdWordsLinksListCall
func (r *ManagementWebPropertyAdWordsLinksService) Patch(accountId string, webPropertyId string, webPropertyAdWordsLinkId string, ...) *ManagementWebPropertyAdWordsLinksPatchCall
func (r *ManagementWebPropertyAdWordsLinksService) Update(accountId string, webPropertyId string, webPropertyAdWordsLinkId string, ...) *ManagementWebPropertyAdWordsLinksUpdateCall
type ManagementWebPropertyAdWordsLinksUpdateCall
func (c *ManagementWebPropertyAdWordsLinksUpdateCall) Context(ctx context.Context) *ManagementWebPropertyAdWordsLinksUpdateCall
func (c *ManagementWebPropertyAdWordsLinksUpdateCall) Do(opts ...googleapi.CallOption) (*EntityAdWordsLink, error)
func (c *ManagementWebPropertyAdWordsLinksUpdateCall) Fields(s ...googleapi.Field) *ManagementWebPropertyAdWordsLinksUpdateCall
func (c *ManagementWebPropertyAdWordsLinksUpdateCall) Header() http.Header
type ManagementWebpropertiesGetCall
func (c *ManagementWebpropertiesGetCall) Context(ctx context.Context) *ManagementWebpropertiesGetCall
func (c *ManagementWebpropertiesGetCall) Do(opts ...googleapi.CallOption) (*Webproperty, error)
func (c *ManagementWebpropertiesGetCall) Fields(s ...googleapi.Field) *ManagementWebpropertiesGetCall
func (c *ManagementWebpropertiesGetCall) Header() http.Header
func (c *ManagementWebpropertiesGetCall) IfNoneMatch(entityTag string) *ManagementWebpropertiesGetCall
type ManagementWebpropertiesInsertCall
func (c *ManagementWebpropertiesInsertCall) Context(ctx context.Context) *ManagementWebpropertiesInsertCall
func (c *ManagementWebpropertiesInsertCall) Do(opts ...googleapi.CallOption) (*Webproperty, error)
func (c *ManagementWebpropertiesInsertCall) Fields(s ...googleapi.Field) *ManagementWebpropertiesInsertCall
func (c *ManagementWebpropertiesInsertCall) Header() http.Header
type ManagementWebpropertiesListCall
func (c *ManagementWebpropertiesListCall) Context(ctx context.Context) *ManagementWebpropertiesListCall
func (c *ManagementWebpropertiesListCall) Do(opts ...googleapi.CallOption) (*Webproperties, error)
func (c *ManagementWebpropertiesListCall) Fields(s ...googleapi.Field) *ManagementWebpropertiesListCall
func (c *ManagementWebpropertiesListCall) Header() http.Header
func (c *ManagementWebpropertiesListCall) IfNoneMatch(entityTag string) *ManagementWebpropertiesListCall
func (c *ManagementWebpropertiesListCall) MaxResults(maxResults int64) *ManagementWebpropertiesListCall
func (c *ManagementWebpropertiesListCall) StartIndex(startIndex int64) *ManagementWebpropertiesListCall
type ManagementWebpropertiesPatchCall
func (c *ManagementWebpropertiesPatchCall) Context(ctx context.Context) *ManagementWebpropertiesPatchCall
func (c *ManagementWebpropertiesPatchCall) Do(opts ...googleapi.CallOption) (*Webproperty, error)
func (c *ManagementWebpropertiesPatchCall) Fields(s ...googleapi.Field) *ManagementWebpropertiesPatchCall
func (c *ManagementWebpropertiesPatchCall) Header() http.Header
type ManagementWebpropertiesService
func NewManagementWebpropertiesService(s *Service) *ManagementWebpropertiesService
func (r *ManagementWebpropertiesService) Get(accountId string, webPropertyId string) *ManagementWebpropertiesGetCall
func (r *ManagementWebpropertiesService) Insert(accountId string, webproperty *Webproperty) *ManagementWebpropertiesInsertCall
func (r *ManagementWebpropertiesService) List(accountId string) *ManagementWebpropertiesListCall
func (r *ManagementWebpropertiesService) Patch(accountId string, webPropertyId string, webproperty *Webproperty) *ManagementWebpropertiesPatchCall
func (r *ManagementWebpropertiesService) Update(accountId string, webPropertyId string, webproperty *Webproperty) *ManagementWebpropertiesUpdateCall
type ManagementWebpropertiesUpdateCall
func (c *ManagementWebpropertiesUpdateCall) Context(ctx context.Context) *ManagementWebpropertiesUpdateCall
func (c *ManagementWebpropertiesUpdateCall) Do(opts ...googleapi.CallOption) (*Webproperty, error)
func (c *ManagementWebpropertiesUpdateCall) Fields(s ...googleapi.Field) *ManagementWebpropertiesUpdateCall
func (c *ManagementWebpropertiesUpdateCall) Header() http.Header
type ManagementWebpropertyUserLinksDeleteCall
func (c *ManagementWebpropertyUserLinksDeleteCall) Context(ctx context.Context) *ManagementWebpropertyUserLinksDeleteCall
func (c *ManagementWebpropertyUserLinksDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *ManagementWebpropertyUserLinksDeleteCall) Fields(s ...googleapi.Field) *ManagementWebpropertyUserLinksDeleteCall
func (c *ManagementWebpropertyUserLinksDeleteCall) Header() http.Header
type ManagementWebpropertyUserLinksInsertCall
func (c *ManagementWebpropertyUserLinksInsertCall) Context(ctx context.Context) *ManagementWebpropertyUserLinksInsertCall
func (c *ManagementWebpropertyUserLinksInsertCall) Do(opts ...googleapi.CallOption) (*EntityUserLink, error)
func (c *ManagementWebpropertyUserLinksInsertCall) Fields(s ...googleapi.Field) *ManagementWebpropertyUserLinksInsertCall
func (c *ManagementWebpropertyUserLinksInsertCall) Header() http.Header
type ManagementWebpropertyUserLinksListCall
func (c *ManagementWebpropertyUserLinksListCall) Context(ctx context.Context) *ManagementWebpropertyUserLinksListCall
func (c *ManagementWebpropertyUserLinksListCall) Do(opts ...googleapi.CallOption) (*EntityUserLinks, error)
func (c *ManagementWebpropertyUserLinksListCall) Fields(s ...googleapi.Field) *ManagementWebpropertyUserLinksListCall
func (c *ManagementWebpropertyUserLinksListCall) Header() http.Header
func (c *ManagementWebpropertyUserLinksListCall) IfNoneMatch(entityTag string) *ManagementWebpropertyUserLinksListCall
func (c *ManagementWebpropertyUserLinksListCall) MaxResults(maxResults int64) *ManagementWebpropertyUserLinksListCall
func (c *ManagementWebpropertyUserLinksListCall) StartIndex(startIndex int64) *ManagementWebpropertyUserLinksListCall
type ManagementWebpropertyUserLinksService
func NewManagementWebpropertyUserLinksService(s *Service) *ManagementWebpropertyUserLinksService
func (r *ManagementWebpropertyUserLinksService) Delete(accountId string, webPropertyId string, linkId string) *ManagementWebpropertyUserLinksDeleteCall
func (r *ManagementWebpropertyUserLinksService) Insert(accountId string, webPropertyId string, entityuserlink *EntityUserLink) *ManagementWebpropertyUserLinksInsertCall
func (r *ManagementWebpropertyUserLinksService) List(accountId string, webPropertyId string) *ManagementWebpropertyUserLinksListCall
func (r *ManagementWebpropertyUserLinksService) Update(accountId string, webPropertyId string, linkId string, ...) *ManagementWebpropertyUserLinksUpdateCall
type ManagementWebpropertyUserLinksUpdateCall
func (c *ManagementWebpropertyUserLinksUpdateCall) Context(ctx context.Context) *ManagementWebpropertyUserLinksUpdateCall
func (c *ManagementWebpropertyUserLinksUpdateCall) Do(opts ...googleapi.CallOption) (*EntityUserLink, error)
func (c *ManagementWebpropertyUserLinksUpdateCall) Fields(s ...googleapi.Field) *ManagementWebpropertyUserLinksUpdateCall
func (c *ManagementWebpropertyUserLinksUpdateCall) Header() http.Header
type McfData
func (s McfData) MarshalJSON() ([]byte, error)
type McfDataColumnHeaders
func (s McfDataColumnHeaders) MarshalJSON() ([]byte, error)
type McfDataProfileInfo
func (s McfDataProfileInfo) MarshalJSON() ([]byte, error)
type McfDataQuery
func (s McfDataQuery) MarshalJSON() ([]byte, error)
type McfDataRowsItem
func (s McfDataRowsItem) MarshalJSON() ([]byte, error)
type McfDataRowsItemConversionPathValue
func (s McfDataRowsItemConversionPathValue) MarshalJSON() ([]byte, error)
type MetadataColumnsListCall
func (c *MetadataColumnsListCall) Context(ctx context.Context) *MetadataColumnsListCall
func (c *MetadataColumnsListCall) Do(opts ...googleapi.CallOption) (*Columns, error)
func (c *MetadataColumnsListCall) Fields(s ...googleapi.Field) *MetadataColumnsListCall
func (c *MetadataColumnsListCall) Header() http.Header
func (c *MetadataColumnsListCall) IfNoneMatch(entityTag string) *MetadataColumnsListCall
type MetadataColumnsService
func NewMetadataColumnsService(s *Service) *MetadataColumnsService
func (r *MetadataColumnsService) List(reportType string) *MetadataColumnsListCall
type MetadataService
func NewMetadataService(s *Service) *MetadataService
type Profile
func (s Profile) MarshalJSON() ([]byte, error)
type ProfileChildLink
func (s ProfileChildLink) MarshalJSON() ([]byte, error)
type ProfileFilterLink
func (s ProfileFilterLink) MarshalJSON() ([]byte, error)
type ProfileFilterLinks
func (s ProfileFilterLinks) MarshalJSON() ([]byte, error)
type ProfileParentLink
func (s ProfileParentLink) MarshalJSON() ([]byte, error)
type ProfilePermissions
func (s ProfilePermissions) MarshalJSON() ([]byte, error)
type ProfileRef
func (s ProfileRef) MarshalJSON() ([]byte, error)
type ProfileSummary
func (s ProfileSummary) MarshalJSON() ([]byte, error)
type Profiles
func (s Profiles) MarshalJSON() ([]byte, error)
type ProvisioningCreateAccountTicketCall
func (c *ProvisioningCreateAccountTicketCall) Context(ctx context.Context) *ProvisioningCreateAccountTicketCall
func (c *ProvisioningCreateAccountTicketCall) Do(opts ...googleapi.CallOption) (*AccountTicket, error)
func (c *ProvisioningCreateAccountTicketCall) Fields(s ...googleapi.Field) *ProvisioningCreateAccountTicketCall
func (c *ProvisioningCreateAccountTicketCall) Header() http.Header
type ProvisioningCreateAccountTreeCall
func (c *ProvisioningCreateAccountTreeCall) Context(ctx context.Context) *ProvisioningCreateAccountTreeCall
func (c *ProvisioningCreateAccountTreeCall) Do(opts ...googleapi.CallOption) (*AccountTreeResponse, error)
func (c *ProvisioningCreateAccountTreeCall) Fields(s ...googleapi.Field) *ProvisioningCreateAccountTreeCall
func (c *ProvisioningCreateAccountTreeCall) Header() http.Header
type ProvisioningService
func NewProvisioningService(s *Service) *ProvisioningService
func (r *ProvisioningService) CreateAccountTicket(accountticket *AccountTicket) *ProvisioningCreateAccountTicketCall
func (r *ProvisioningService) CreateAccountTree(accounttreerequest *AccountTreeRequest) *ProvisioningCreateAccountTreeCall
type RealtimeData
func (s RealtimeData) MarshalJSON() ([]byte, error)
type RealtimeDataColumnHeaders
func (s RealtimeDataColumnHeaders) MarshalJSON() ([]byte, error)
type RealtimeDataProfileInfo
func (s RealtimeDataProfileInfo) MarshalJSON() ([]byte, error)
type RealtimeDataQuery
func (s RealtimeDataQuery) MarshalJSON() ([]byte, error)
type RemarketingAudience
func (s RemarketingAudience) MarshalJSON() ([]byte, error)
type RemarketingAudienceAudienceDefinition
func (s RemarketingAudienceAudienceDefinition) MarshalJSON() ([]byte, error)
type RemarketingAudienceStateBasedAudienceDefinition
func (s RemarketingAudienceStateBasedAudienceDefinition) MarshalJSON() ([]byte, error)
type RemarketingAudienceStateBasedAudienceDefinitionExcludeConditions
func (s RemarketingAudienceStateBasedAudienceDefinitionExcludeConditions) MarshalJSON() ([]byte, error)
type RemarketingAudiences
func (s RemarketingAudiences) MarshalJSON() ([]byte, error)
type Segment
func (s Segment) MarshalJSON() ([]byte, error)
type Segments
func (s Segments) MarshalJSON() ([]byte, error)
type Service
func New(client *http.Client) (*Service, error)DEPRECATED
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)
type UnsampledReport
func (s UnsampledReport) MarshalJSON() ([]byte, error)
type UnsampledReportCloudStorageDownloadDetails
func (s UnsampledReportCloudStorageDownloadDetails) MarshalJSON() ([]byte, error)
type UnsampledReportDriveDownloadDetails
func (s UnsampledReportDriveDownloadDetails) MarshalJSON() ([]byte, error)
type UnsampledReports
func (s UnsampledReports) MarshalJSON() ([]byte, error)
type Upload
func (s Upload) MarshalJSON() ([]byte, error)
type Uploads
func (s Uploads) MarshalJSON() ([]byte, error)
type UserDeletionRequest
func (s UserDeletionRequest) MarshalJSON() ([]byte, error)
type UserDeletionRequestId
func (s UserDeletionRequestId) MarshalJSON() ([]byte, error)
type UserDeletionService
func NewUserDeletionService(s *Service) *UserDeletionService
type UserDeletionUserDeletionRequestService
func NewUserDeletionUserDeletionRequestService(s *Service) *UserDeletionUserDeletionRequestService
func (r *UserDeletionUserDeletionRequestService) Upsert(userdeletionrequest *UserDeletionRequest) *UserDeletionUserDeletionRequestUpsertCall
type UserDeletionUserDeletionRequestUpsertCall
func (c *UserDeletionUserDeletionRequestUpsertCall) Context(ctx context.Context) *UserDeletionUserDeletionRequestUpsertCall
func (c *UserDeletionUserDeletionRequestUpsertCall) Do(opts ...googleapi.CallOption) (*UserDeletionRequest, error)
func (c *UserDeletionUserDeletionRequestUpsertCall) Fields(s ...googleapi.Field) *UserDeletionUserDeletionRequestUpsertCall
func (c *UserDeletionUserDeletionRequestUpsertCall) Header() http.Header
type UserRef
func (s UserRef) MarshalJSON() ([]byte, error)
type WebPropertyRef
func (s WebPropertyRef) MarshalJSON() ([]byte, error)
type WebPropertySummary
func (s WebPropertySummary) MarshalJSON() ([]byte, error)
type Webproperties
func (s Webproperties) MarshalJSON() ([]byte, error)
type Webproperty
func (s Webproperty) MarshalJSON() ([]byte, error)
type WebpropertyChildLink
func (s WebpropertyChildLink) MarshalJSON() ([]byte, error)
type WebpropertyParentLink
func (s WebpropertyParentLink) MarshalJSON() ([]byte, error)
type WebpropertyPermissions
func (s WebpropertyPermissions) MarshalJSON() ([]byte, error)
Constants ¶
View Source
const (
	// View and manage your Google Analytics data
	AnalyticsScope = "https://www.googleapis.com/auth/analytics"

	// Edit Google Analytics management entities
	AnalyticsEditScope = "https://www.googleapis.com/auth/analytics.edit"

	// Manage Google Analytics Account users by email address
	AnalyticsManageUsersScope = "https://www.googleapis.com/auth/analytics.manage.users"

	// View Google Analytics user permissions
	AnalyticsManageUsersReadonlyScope = "https://www.googleapis.com/auth/analytics.manage.users.readonly"

	// Create a new Google Analytics account along with its default property and
	// view
	AnalyticsProvisionScope = "https://www.googleapis.com/auth/analytics.provision"

	// View your Google Analytics data
	AnalyticsReadonlyScope = "https://www.googleapis.com/auth/analytics.readonly"

	// Manage Google Analytics user deletion requests
	AnalyticsUserDeletionScope = "https://www.googleapis.com/auth/analytics.user.deletion"
)

OAuth2 scopes used by this API.

Variables ¶

This section is empty.

Functions ¶

This section is empty.

Types ¶
type Account ¶
type Account struct {
	// ChildLink: Child link for an account entry. Points to the list of web
	// properties for this account.
	ChildLink *AccountChildLink `json:"childLink,omitempty"`
	// Created: Time the account was created.
	Created string `json:"created,omitempty"`
	// Id: Account ID.
	Id string `json:"id,omitempty"`
	// Kind: Resource type for Analytics account.
	Kind string `json:"kind,omitempty"`
	// Name: Account name.
	Name string `json:"name,omitempty"`
	// Permissions: Permissions the user has for this account.
	Permissions *AccountPermissions `json:"permissions,omitempty"`
	// SelfLink: Link for this account.
	SelfLink string `json:"selfLink,omitempty"`
	// Starred: Indicates whether this account is starred or not.
	Starred bool `json:"starred,omitempty"`
	// Updated: Time the account was last modified.
	Updated string `json:"updated,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ChildLink") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ChildLink") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Account: JSON template for Analytics account entry.

func (Account) MarshalJSON ¶
func (s Account) MarshalJSON() ([]byte, error)
type AccountChildLink ¶
type AccountChildLink struct {
	// Href: Link to the list of web properties for this account.
	Href string `json:"href,omitempty"`
	// Type: Type of the child link. Its value is "analytics#webproperties".
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Href") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Href") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AccountChildLink: Child link for an account entry. Points to the list of web properties for this account.

func (AccountChildLink) MarshalJSON ¶
func (s AccountChildLink) MarshalJSON() ([]byte, error)
type AccountPermissions ¶
type AccountPermissions struct {
	// Effective: All the permissions that the user has for this account. These
	// include any implied permissions (e.g., EDIT implies VIEW).
	Effective []string `json:"effective,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Effective") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Effective") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AccountPermissions: Permissions the user has for this account.

func (AccountPermissions) MarshalJSON ¶
func (s AccountPermissions) MarshalJSON() ([]byte, error)
type AccountRef ¶
type AccountRef struct {
	// Href: Link for this account.
	Href string `json:"href,omitempty"`
	// Id: Account ID.
	Id string `json:"id,omitempty"`
	// Kind: Analytics account reference.
	Kind string `json:"kind,omitempty"`
	// Name: Account name.
	Name string `json:"name,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Href") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Href") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AccountRef: JSON template for a linked account.

func (AccountRef) MarshalJSON ¶
func (s AccountRef) MarshalJSON() ([]byte, error)
type AccountSummaries ¶
type AccountSummaries struct {
	// Items: A list of AccountSummaries.
	Items []*AccountSummary `json:"items,omitempty"`
	// ItemsPerPage: The maximum number of resources the response can contain,
	// regardless of the actual number of resources returned. Its value ranges from
	// 1 to 1000 with a value of 1000 by default, or otherwise specified by the
	// max-results query parameter.
	ItemsPerPage int64 `json:"itemsPerPage,omitempty"`
	// Kind: Collection type.
	Kind string `json:"kind,omitempty"`
	// NextLink: Link to next page for this AccountSummary collection.
	NextLink string `json:"nextLink,omitempty"`
	// PreviousLink: Link to previous page for this AccountSummary collection.
	PreviousLink string `json:"previousLink,omitempty"`
	// StartIndex: The starting index of the resources, which is 1 by default or
	// otherwise specified by the start-index query parameter.
	StartIndex int64 `json:"startIndex,omitempty"`
	// TotalResults: The total number of results for the query, regardless of the
	// number of results in the response.
	TotalResults int64 `json:"totalResults,omitempty"`
	// Username: Email ID of the authenticated user
	Username string `json:"username,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Items") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Items") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AccountSummaries: An AccountSummary collection lists a summary of accounts, properties and views (profiles) to which the user has access. Each resource in the collection corresponds to a single AccountSummary.

func (AccountSummaries) MarshalJSON ¶
func (s AccountSummaries) MarshalJSON() ([]byte, error)
type AccountSummary ¶
type AccountSummary struct {
	// Id: Account ID.
	Id string `json:"id,omitempty"`
	// Kind: Resource type for Analytics AccountSummary.
	Kind string `json:"kind,omitempty"`
	// Name: Account name.
	Name string `json:"name,omitempty"`
	// Starred: Indicates whether this account is starred or not.
	Starred bool `json:"starred,omitempty"`
	// WebProperties: List of web properties under this account.
	WebProperties []*WebPropertySummary `json:"webProperties,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Id") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Id") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AccountSummary: JSON template for an Analytics AccountSummary. An AccountSummary is a lightweight tree comprised of properties/profiles.

func (AccountSummary) MarshalJSON ¶
func (s AccountSummary) MarshalJSON() ([]byte, error)
type AccountTicket ¶
type AccountTicket struct {
	// Account: Account for this ticket.
	Account *Account `json:"account,omitempty"`
	// Id: Account ticket ID used to access the account ticket.
	Id string `json:"id,omitempty"`
	// Kind: Resource type for account ticket.
	Kind string `json:"kind,omitempty"`
	// Profile: View (Profile) for the account.
	Profile *Profile `json:"profile,omitempty"`
	// RedirectUri: Redirect URI where the user will be sent after accepting Terms
	// of Service. Must be configured in APIs console as a callback URL.
	RedirectUri string `json:"redirectUri,omitempty"`
	// Webproperty: Web property for the account.
	Webproperty *Webproperty `json:"webproperty,omitempty"`

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

AccountTicket: JSON template for an Analytics account ticket. The account ticket consists of the ticket ID and the basic information for the account, property and profile.

func (AccountTicket) MarshalJSON ¶
func (s AccountTicket) MarshalJSON() ([]byte, error)
type AccountTreeRequest ¶
type AccountTreeRequest struct {
	AccountName string `json:"accountName,omitempty"`
	// Kind: Resource type for account ticket.
	Kind            string `json:"kind,omitempty"`
	ProfileName     string `json:"profileName,omitempty"`
	Timezone        string `json:"timezone,omitempty"`
	WebpropertyName string `json:"webpropertyName,omitempty"`
	WebsiteUrl      string `json:"websiteUrl,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AccountName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccountName") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AccountTreeRequest: JSON template for an Analytics account tree requests. The account tree request is used in the provisioning api to create an account, property, and view (profile). It contains the basic information required to make these fields.

func (AccountTreeRequest) MarshalJSON ¶
func (s AccountTreeRequest) MarshalJSON() ([]byte, error)
type AccountTreeResponse ¶
type AccountTreeResponse struct {
	// Account: The account created.
	Account *Account `json:"account,omitempty"`
	// Kind: Resource type for account ticket.
	Kind string `json:"kind,omitempty"`
	// Profile: View (Profile) for the account.
	Profile *Profile `json:"profile,omitempty"`
	// Webproperty: Web property for the account.
	Webproperty *Webproperty `json:"webproperty,omitempty"`

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

AccountTreeResponse: JSON template for an Analytics account tree response. The account tree response is used in the provisioning api to return the result of creating an account, property, and view (profile).

func (AccountTreeResponse) MarshalJSON ¶
func (s AccountTreeResponse) MarshalJSON() ([]byte, error)
type Accounts ¶
type Accounts struct {
	// Items: A list of accounts.
	Items []*Account `json:"items,omitempty"`
	// ItemsPerPage: The maximum number of entries the response can contain,
	// regardless of the actual number of entries returned. Its value ranges from 1
	// to 1000 with a value of 1000 by default, or otherwise specified by the
	// max-results query parameter.
	ItemsPerPage int64 `json:"itemsPerPage,omitempty"`
	// Kind: Collection type.
	Kind string `json:"kind,omitempty"`
	// NextLink: Next link for this account collection.
	NextLink string `json:"nextLink,omitempty"`
	// PreviousLink: Previous link for this account collection.
	PreviousLink string `json:"previousLink,omitempty"`
	// StartIndex: The starting index of the entries, which is 1 by default or
	// otherwise specified by the start-index query parameter.
	StartIndex int64 `json:"startIndex,omitempty"`
	// TotalResults: The total number of results for the query, regardless of the
	// number of results in the response.
	TotalResults int64 `json:"totalResults,omitempty"`
	// Username: Email ID of the authenticated user
	Username string `json:"username,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Items") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Items") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Accounts: An account collection provides a list of Analytics accounts to which a user has access. The account collection is the entry point to all management information. Each resource in the collection corresponds to a single Analytics account.

func (Accounts) MarshalJSON ¶
func (s Accounts) MarshalJSON() ([]byte, error)
type AdWordsAccount ¶
type AdWordsAccount struct {
	// AutoTaggingEnabled: True if auto-tagging is enabled on the Google Ads
	// account. Read-only after the insert operation.
	AutoTaggingEnabled bool `json:"autoTaggingEnabled,omitempty"`
	// CustomerId: Customer ID. This field is required when creating a Google Ads
	// link.
	CustomerId string `json:"customerId,omitempty"`
	// Kind: Resource type for Google Ads account.
	Kind string `json:"kind,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AutoTaggingEnabled") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AutoTaggingEnabled") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AdWordsAccount: JSON template for an Google Ads account.

func (AdWordsAccount) MarshalJSON ¶
func (s AdWordsAccount) MarshalJSON() ([]byte, error)
type AnalyticsDataimportDeleteUploadDataRequest ¶
type AnalyticsDataimportDeleteUploadDataRequest struct {
	// CustomDataImportUids: A list of upload UIDs.
	CustomDataImportUids []string `json:"customDataImportUids,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CustomDataImportUids") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CustomDataImportUids") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AnalyticsDataimportDeleteUploadDataRequest: Request template for the delete upload data request.

func (AnalyticsDataimportDeleteUploadDataRequest) MarshalJSON ¶
func (s AnalyticsDataimportDeleteUploadDataRequest) MarshalJSON() ([]byte, error)
type Column ¶
type Column struct {
	// Attributes: Map of attribute name and value for this column.
	Attributes map[string]string `json:"attributes,omitempty"`
	// Id: Column id.
	Id string `json:"id,omitempty"`
	// Kind: Resource type for Analytics column.
	Kind string `json:"kind,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Attributes") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Attributes") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Column: JSON template for a metadata column.

func (Column) MarshalJSON ¶
func (s Column) MarshalJSON() ([]byte, error)
type Columns ¶
type Columns struct {
	// AttributeNames: List of attributes names returned by columns.
	AttributeNames []string `json:"attributeNames,omitempty"`
	// Etag: Etag of collection. This etag can be compared with the last response
	// etag to check if response has changed.
	Etag string `json:"etag,omitempty"`
	// Items: List of columns for a report type.
	Items []*Column `json:"items,omitempty"`
	// Kind: Collection type.
	Kind string `json:"kind,omitempty"`
	// TotalResults: Total number of columns returned in the response.
	TotalResults int64 `json:"totalResults,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AttributeNames") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AttributeNames") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Columns: Lists columns (dimensions and metrics) for a particular report type.

func (Columns) MarshalJSON ¶
func (s Columns) MarshalJSON() ([]byte, error)
type CustomDataSource ¶
type CustomDataSource struct {
	// AccountId: Account ID to which this custom data source belongs.
	AccountId string                     `json:"accountId,omitempty"`
	ChildLink *CustomDataSourceChildLink `json:"childLink,omitempty"`
	// Created: Time this custom data source was created.
	Created string `json:"created,omitempty"`
	// Description: Description of custom data source.
	Description string `json:"description,omitempty"`
	// Id: Custom data source ID.
	Id             string `json:"id,omitempty"`
	ImportBehavior string `json:"importBehavior,omitempty"`
	// Kind: Resource type for Analytics custom data source.
	Kind string `json:"kind,omitempty"`
	// Name: Name of this custom data source.
	Name string `json:"name,omitempty"`
	// ParentLink: Parent link for this custom data source. Points to the web
	// property to which this custom data source belongs.
	ParentLink *CustomDataSourceParentLink `json:"parentLink,omitempty"`
	// ProfilesLinked: IDs of views (profiles) linked to the custom data source.
	ProfilesLinked []string `json:"profilesLinked,omitempty"`
	// Schema: Collection of schema headers of the custom data source.
	Schema []string `json:"schema,omitempty"`
	// SelfLink: Link for this Analytics custom data source.
	SelfLink string `json:"selfLink,omitempty"`
	// Type: Type of the custom data source.
	Type string `json:"type,omitempty"`
	// Updated: Time this custom data source was last modified.
	Updated string `json:"updated,omitempty"`
	// UploadType: Upload type of the custom data source.
	UploadType string `json:"uploadType,omitempty"`
	// WebPropertyId: Web property ID of the form UA-XXXXX-YY to which this custom
	// data source belongs.
	WebPropertyId string `json:"webPropertyId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AccountId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccountId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CustomDataSource: JSON template for an Analytics custom data source.

func (CustomDataSource) MarshalJSON ¶
func (s CustomDataSource) MarshalJSON() ([]byte, error)
type CustomDataSourceChildLink ¶
type CustomDataSourceChildLink struct {
	// Href: Link to the list of daily uploads for this custom data source. Link to
	// the list of uploads for this custom data source.
	Href string `json:"href,omitempty"`
	// Type: Value is "analytics#dailyUploads". Value is "analytics#uploads".
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Href") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Href") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (CustomDataSourceChildLink) MarshalJSON ¶
func (s CustomDataSourceChildLink) MarshalJSON() ([]byte, error)
type CustomDataSourceParentLink ¶
type CustomDataSourceParentLink struct {
	// Href: Link to the web property to which this custom data source belongs.
	Href string `json:"href,omitempty"`
	// Type: Value is "analytics#webproperty".
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Href") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Href") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CustomDataSourceParentLink: Parent link for this custom data source. Points to the web property to which this custom data source belongs.

func (CustomDataSourceParentLink) MarshalJSON ¶
func (s CustomDataSourceParentLink) MarshalJSON() ([]byte, error)
type CustomDataSources ¶
type CustomDataSources struct {
	// Items: Collection of custom data sources.
	Items []*CustomDataSource `json:"items,omitempty"`
	// ItemsPerPage: The maximum number of resources the response can contain,
	// regardless of the actual number of resources returned. Its value ranges from
	// 1 to 1000 with a value of 1000 by default, or otherwise specified by the
	// max-results query parameter.
	ItemsPerPage int64 `json:"itemsPerPage,omitempty"`
	// Kind: Collection type.
	Kind string `json:"kind,omitempty"`
	// NextLink: Link to next page for this custom data source collection.
	NextLink string `json:"nextLink,omitempty"`
	// PreviousLink: Link to previous page for this custom data source collection.
	PreviousLink string `json:"previousLink,omitempty"`
	// StartIndex: The starting index of the resources, which is 1 by default or
	// otherwise specified by the start-index query parameter.
	StartIndex int64 `json:"startIndex,omitempty"`
	// TotalResults: The total number of results for the query, regardless of the
	// number of results in the response.
	TotalResults int64 `json:"totalResults,omitempty"`
	// Username: Email ID of the authenticated user
	Username string `json:"username,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Items") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Items") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CustomDataSources: Lists Analytics custom data sources to which the user has access. Each resource in the collection corresponds to a single Analytics custom data source.

func (CustomDataSources) MarshalJSON ¶
func (s CustomDataSources) MarshalJSON() ([]byte, error)
type CustomDimension ¶
type CustomDimension struct {
	// AccountId: Account ID.
	AccountId string `json:"accountId,omitempty"`
	// Active: Boolean indicating whether the custom dimension is active.
	Active bool `json:"active,omitempty"`
	// Created: Time the custom dimension was created.
	Created string `json:"created,omitempty"`
	// Id: Custom dimension ID.
	Id string `json:"id,omitempty"`
	// Index: Index of the custom dimension.
	Index int64 `json:"index,omitempty"`
	// Kind: Kind value for a custom dimension. Set to "analytics#customDimension".
	// It is a read-only field.
	Kind string `json:"kind,omitempty"`
	// Name: Name of the custom dimension.
	Name string `json:"name,omitempty"`
	// ParentLink: Parent link for the custom dimension. Points to the property to
	// which the custom dimension belongs.
	ParentLink *CustomDimensionParentLink `json:"parentLink,omitempty"`
	// Scope: Scope of the custom dimension: HIT, SESSION, USER or PRODUCT.
	Scope string `json:"scope,omitempty"`
	// SelfLink: Link for the custom dimension
	SelfLink string `json:"selfLink,omitempty"`
	// Updated: Time the custom dimension was last modified.
	Updated string `json:"updated,omitempty"`
	// WebPropertyId: Property ID.
	WebPropertyId string `json:"webPropertyId,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AccountId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccountId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CustomDimension: JSON template for Analytics Custom Dimension.

func (CustomDimension) MarshalJSON ¶
func (s CustomDimension) MarshalJSON() ([]byte, error)
type CustomDimensionParentLink ¶
type CustomDimensionParentLink struct {
	// Href: Link to the property to which the custom dimension belongs.
	Href string `json:"href,omitempty"`
	// Type: Type of the parent link. Set to "analytics#webproperty".
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Href") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Href") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CustomDimensionParentLink: Parent link for the custom dimension. Points to the property to which the custom dimension belongs.

func (CustomDimensionParentLink) MarshalJSON ¶
func (s CustomDimensionParentLink) MarshalJSON() ([]byte, error)
type CustomDimensions ¶
type CustomDimensions struct {
	// Items: Collection of custom dimensions.
	Items []*CustomDimension `json:"items,omitempty"`
	// ItemsPerPage: The maximum number of resources the response can contain,
	// regardless of the actual number of resources returned. Its value ranges from
	// 1 to 1000 with a value of 1000 by default, or otherwise specified by the
	// max-results query parameter.
	ItemsPerPage int64 `json:"itemsPerPage,omitempty"`
	// Kind: Collection type.
	Kind string `json:"kind,omitempty"`
	// NextLink: Link to next page for this custom dimension collection.
	NextLink string `json:"nextLink,omitempty"`
	// PreviousLink: Link to previous page for this custom dimension collection.
	PreviousLink string `json:"previousLink,omitempty"`
	// StartIndex: The starting index of the resources, which is 1 by default or
	// otherwise specified by the start-index query parameter.
	StartIndex int64 `json:"startIndex,omitempty"`
	// TotalResults: The total number of results for the query, regardless of the
	// number of results in the response.
	TotalResults int64 `json:"totalResults,omitempty"`
	// Username: Email ID of the authenticated user
	Username string `json:"username,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Items") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Items") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CustomDimensions: A custom dimension collection lists Analytics custom dimensions to which the user has access. Each resource in the collection corresponds to a single Analytics custom dimension.

func (CustomDimensions) MarshalJSON ¶
func (s CustomDimensions) MarshalJSON() ([]byte, error)
type CustomMetric ¶
type CustomMetric struct {
	// AccountId: Account ID.
	AccountId string `json:"accountId,omitempty"`
	// Active: Boolean indicating whether the custom metric is active.
	Active bool `json:"active,omitempty"`
	// Created: Time the custom metric was created.
	Created string `json:"created,omitempty"`
	// Id: Custom metric ID.
	Id string `json:"id,omitempty"`
	// Index: Index of the custom metric.
	Index int64 `json:"index,omitempty"`
	// Kind: Kind value for a custom metric. Set to "analytics#customMetric". It is
	// a read-only field.
	Kind string `json:"kind,omitempty"`
	// MaxValue: Max value of custom metric.
	MaxValue string `json:"max_value,omitempty"`
	// MinValue: Min value of custom metric.
	MinValue string `json:"min_value,omitempty"`
	// Name: Name of the custom metric.
	Name string `json:"name,omitempty"`
	// ParentLink: Parent link for the custom metric. Points to the property to
	// which the custom metric belongs.
	ParentLink *CustomMetricParentLink `json:"parentLink,omitempty"`
	// Scope: Scope of the custom metric: HIT or PRODUCT.
	Scope string `json:"scope,omitempty"`
	// SelfLink: Link for the custom metric
	SelfLink string `json:"selfLink,omitempty"`
	// Type: Data type of custom metric.
	Type string `json:"type,omitempty"`
	// Updated: Time the custom metric was last modified.
	Updated string `json:"updated,omitempty"`
	// WebPropertyId: Property ID.
	WebPropertyId string `json:"webPropertyId,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AccountId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccountId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CustomMetric: JSON template for Analytics Custom Metric.

func (CustomMetric) MarshalJSON ¶
func (s CustomMetric) MarshalJSON() ([]byte, error)
type CustomMetricParentLink ¶
type CustomMetricParentLink struct {
	// Href: Link to the property to which the custom metric belongs.
	Href string `json:"href,omitempty"`
	// Type: Type of the parent link. Set to "analytics#webproperty".
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Href") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Href") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CustomMetricParentLink: Parent link for the custom metric. Points to the property to which the custom metric belongs.

func (CustomMetricParentLink) MarshalJSON ¶
func (s CustomMetricParentLink) MarshalJSON() ([]byte, error)
type CustomMetrics ¶
type CustomMetrics struct {
	// Items: Collection of custom metrics.
	Items []*CustomMetric `json:"items,omitempty"`
	// ItemsPerPage: The maximum number of resources the response can contain,
	// regardless of the actual number of resources returned. Its value ranges from
	// 1 to 1000 with a value of 1000 by default, or otherwise specified by the
	// max-results query parameter.
	ItemsPerPage int64 `json:"itemsPerPage,omitempty"`
	// Kind: Collection type.
	Kind string `json:"kind,omitempty"`
	// NextLink: Link to next page for this custom metric collection.
	NextLink string `json:"nextLink,omitempty"`
	// PreviousLink: Link to previous page for this custom metric collection.
	PreviousLink string `json:"previousLink,omitempty"`
	// StartIndex: The starting index of the resources, which is 1 by default or
	// otherwise specified by the start-index query parameter.
	StartIndex int64 `json:"startIndex,omitempty"`
	// TotalResults: The total number of results for the query, regardless of the
	// number of results in the response.
	TotalResults int64 `json:"totalResults,omitempty"`
	// Username: Email ID of the authenticated user
	Username string `json:"username,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Items") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Items") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CustomMetrics: A custom metric collection lists Analytics custom metrics to which the user has access. Each resource in the collection corresponds to a single Analytics custom metric.

func (CustomMetrics) MarshalJSON ¶
func (s CustomMetrics) MarshalJSON() ([]byte, error)
type DataGaGetCall ¶
type DataGaGetCall struct {
	// contains filtered or unexported fields
}
func (*DataGaGetCall) Context ¶
func (c *DataGaGetCall) Context(ctx context.Context) *DataGaGetCall

Context sets the context to be used in this call's Do method.

func (*DataGaGetCall) Dimensions ¶
func (c *DataGaGetCall) Dimensions(dimensions string) *DataGaGetCall

Dimensions sets the optional parameter "dimensions": A comma-separated list of Analytics dimensions. E.g., 'ga:browser,ga:city'.

func (*DataGaGetCall) Do ¶
func (c *DataGaGetCall) Do(opts ...googleapi.CallOption) (*GaData, error)

Do executes the "analytics.data.ga.get" call. Any non-2xx status code is an error. Response headers are in either *GaData.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*DataGaGetCall) Fields ¶
func (c *DataGaGetCall) Fields(s ...googleapi.Field) *DataGaGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*DataGaGetCall) Filters ¶
func (c *DataGaGetCall) Filters(filters string) *DataGaGetCall

Filters sets the optional parameter "filters": A comma-separated list of dimension or metric filters to be applied to Analytics data.

func (*DataGaGetCall) Header ¶
func (c *DataGaGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*DataGaGetCall) IfNoneMatch ¶
func (c *DataGaGetCall) IfNoneMatch(entityTag string) *DataGaGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*DataGaGetCall) IncludeEmptyRows ¶
func (c *DataGaGetCall) IncludeEmptyRows(includeEmptyRows bool) *DataGaGetCall

IncludeEmptyRows sets the optional parameter "include-empty-rows": The response will include empty rows if this parameter is set to true, the default is true

func (*DataGaGetCall) MaxResults ¶
func (c *DataGaGetCall) MaxResults(maxResults int64) *DataGaGetCall

MaxResults sets the optional parameter "max-results": The maximum number of entries to include in this feed.

func (*DataGaGetCall) Output ¶
func (c *DataGaGetCall) Output(output string) *DataGaGetCall

Output sets the optional parameter "output": The selected format for the response. Default format is JSON.

Possible values:

"dataTable" - Returns the response in Google Charts Data Table format.


This is useful in creating visualization using Google Charts.

"json" - Returns the response in standard JSON format.

func (*DataGaGetCall) SamplingLevel ¶
func (c *DataGaGetCall) SamplingLevel(samplingLevel string) *DataGaGetCall

SamplingLevel sets the optional parameter "samplingLevel": The desired sampling level.

Possible values:

"DEFAULT" - Returns response with a sample size that balances speed and


accuracy.

"FASTER" - Returns a fast response with a smaller sample size.
"HIGHER_PRECISION" - Returns a more accurate response using a large sample


size, but this may result in the response being slower.

func (*DataGaGetCall) Segment ¶
func (c *DataGaGetCall) Segment(segment string) *DataGaGetCall

Segment sets the optional parameter "segment": An Analytics segment to be applied to data.

func (*DataGaGetCall) Sort ¶
func (c *DataGaGetCall) Sort(sort string) *DataGaGetCall

Sort sets the optional parameter "sort": A comma-separated list of dimensions or metrics that determine the sort order for Analytics data.

func (*DataGaGetCall) StartIndex ¶
func (c *DataGaGetCall) StartIndex(startIndex int64) *DataGaGetCall

StartIndex sets the optional parameter "start-index": An index of the first entity to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

type DataGaService ¶
type DataGaService struct {
	// contains filtered or unexported fields
}
func NewDataGaService ¶
func NewDataGaService(s *Service) *DataGaService
func (*DataGaService) Get ¶
func (r *DataGaService) Get(ids string, startDate string, endDate string, metrics string) *DataGaGetCall

Get: Returns Analytics data for a view (profile).

endDate: End date for fetching Analytics data. Request can should specify an end date formatted as YYYY-MM-DD, or as a relative date (e.g., today, yesterday, or 7daysAgo). The default value is yesterday.
ids: Unique table ID for retrieving Analytics data. Table ID is of the form ga:XXXX, where XXXX is the Analytics view (profile) ID.
metrics: A comma-separated list of Analytics metrics. E.g., 'ga:sessions,ga:pageviews'. At least one metric must be specified.
startDate: Start date for fetching Analytics data. Requests can specify a start date formatted as YYYY-MM-DD, or as a relative date (e.g., today, yesterday, or 7daysAgo). The default value is 7daysAgo.
type DataMcfGetCall ¶
type DataMcfGetCall struct {
	// contains filtered or unexported fields
}
func (*DataMcfGetCall) Context ¶
func (c *DataMcfGetCall) Context(ctx context.Context) *DataMcfGetCall

Context sets the context to be used in this call's Do method.

func (*DataMcfGetCall) Dimensions ¶
func (c *DataMcfGetCall) Dimensions(dimensions string) *DataMcfGetCall

Dimensions sets the optional parameter "dimensions": A comma-separated list of Multi-Channel Funnels dimensions. E.g., 'mcf:source,mcf:medium'.

func (*DataMcfGetCall) Do ¶
func (c *DataMcfGetCall) Do(opts ...googleapi.CallOption) (*McfData, error)

Do executes the "analytics.data.mcf.get" call. Any non-2xx status code is an error. Response headers are in either *McfData.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*DataMcfGetCall) Fields ¶
func (c *DataMcfGetCall) Fields(s ...googleapi.Field) *DataMcfGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*DataMcfGetCall) Filters ¶
func (c *DataMcfGetCall) Filters(filters string) *DataMcfGetCall

Filters sets the optional parameter "filters": A comma-separated list of dimension or metric filters to be applied to the Analytics data.

func (*DataMcfGetCall) Header ¶
func (c *DataMcfGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*DataMcfGetCall) IfNoneMatch ¶
func (c *DataMcfGetCall) IfNoneMatch(entityTag string) *DataMcfGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*DataMcfGetCall) MaxResults ¶
func (c *DataMcfGetCall) MaxResults(maxResults int64) *DataMcfGetCall

MaxResults sets the optional parameter "max-results": The maximum number of entries to include in this feed.

func (*DataMcfGetCall) SamplingLevel ¶
func (c *DataMcfGetCall) SamplingLevel(samplingLevel string) *DataMcfGetCall

SamplingLevel sets the optional parameter "samplingLevel": The desired sampling level.

Possible values:

"DEFAULT" - Returns response with a sample size that balances speed and


accuracy.

"FASTER" - Returns a fast response with a smaller sample size.
"HIGHER_PRECISION" - Returns a more accurate response using a large sample


size, but this may result in the response being slower.

func (*DataMcfGetCall) Sort ¶
func (c *DataMcfGetCall) Sort(sort string) *DataMcfGetCall

Sort sets the optional parameter "sort": A comma-separated list of dimensions or metrics that determine the sort order for the Analytics data.

func (*DataMcfGetCall) StartIndex ¶
func (c *DataMcfGetCall) StartIndex(startIndex int64) *DataMcfGetCall

StartIndex sets the optional parameter "start-index": An index of the first entity to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

type DataMcfService ¶
type DataMcfService struct {
	// contains filtered or unexported fields
}
func NewDataMcfService ¶
func NewDataMcfService(s *Service) *DataMcfService
func (*DataMcfService) Get ¶
func (r *DataMcfService) Get(ids string, startDate string, endDate string, metrics string) *DataMcfGetCall

Get: Returns Analytics Multi-Channel Funnels data for a view (profile).

endDate: End date for fetching Analytics data. Requests can specify a start date formatted as YYYY-MM-DD, or as a relative date (e.g., today, yesterday, or 7daysAgo). The default value is 7daysAgo.
ids: Unique table ID for retrieving Analytics data. Table ID is of the form ga:XXXX, where XXXX is the Analytics view (profile) ID.
metrics: A comma-separated list of Multi-Channel Funnels metrics. E.g., 'mcf:totalConversions,mcf:totalConversionValue'. At least one metric must be specified.
startDate: Start date for fetching Analytics data. Requests can specify a start date formatted as YYYY-MM-DD, or as a relative date (e.g., today, yesterday, or 7daysAgo). The default value is 7daysAgo.
type DataRealtimeGetCall ¶
type DataRealtimeGetCall struct {
	// contains filtered or unexported fields
}
func (*DataRealtimeGetCall) Context ¶
func (c *DataRealtimeGetCall) Context(ctx context.Context) *DataRealtimeGetCall

Context sets the context to be used in this call's Do method.

func (*DataRealtimeGetCall) Dimensions ¶
func (c *DataRealtimeGetCall) Dimensions(dimensions string) *DataRealtimeGetCall

Dimensions sets the optional parameter "dimensions": A comma-separated list of real time dimensions. E.g., 'rt:medium,rt:city'.

func (*DataRealtimeGetCall) Do ¶
func (c *DataRealtimeGetCall) Do(opts ...googleapi.CallOption) (*RealtimeData, error)

Do executes the "analytics.data.realtime.get" call. Any non-2xx status code is an error. Response headers are in either *RealtimeData.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*DataRealtimeGetCall) Fields ¶
func (c *DataRealtimeGetCall) Fields(s ...googleapi.Field) *DataRealtimeGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*DataRealtimeGetCall) Filters ¶
func (c *DataRealtimeGetCall) Filters(filters string) *DataRealtimeGetCall

Filters sets the optional parameter "filters": A comma-separated list of dimension or metric filters to be applied to real time data.

func (*DataRealtimeGetCall) Header ¶
func (c *DataRealtimeGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*DataRealtimeGetCall) IfNoneMatch ¶
func (c *DataRealtimeGetCall) IfNoneMatch(entityTag string) *DataRealtimeGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*DataRealtimeGetCall) MaxResults ¶
func (c *DataRealtimeGetCall) MaxResults(maxResults int64) *DataRealtimeGetCall

MaxResults sets the optional parameter "max-results": The maximum number of entries to include in this feed.

func (*DataRealtimeGetCall) Sort ¶
func (c *DataRealtimeGetCall) Sort(sort string) *DataRealtimeGetCall

Sort sets the optional parameter "sort": A comma-separated list of dimensions or metrics that determine the sort order for real time data.

type DataRealtimeService ¶
type DataRealtimeService struct {
	// contains filtered or unexported fields
}
func NewDataRealtimeService ¶
func NewDataRealtimeService(s *Service) *DataRealtimeService
func (*DataRealtimeService) Get ¶
func (r *DataRealtimeService) Get(ids string, metrics string) *DataRealtimeGetCall

Get: Returns real time data for a view (profile).

ids: Unique table ID for retrieving real time data. Table ID is of the form ga:XXXX, where XXXX is the Analytics view (profile) ID.
metrics: A comma-separated list of real time metrics. E.g., 'rt:activeUsers'. At least one metric must be specified.
type DataService ¶
type DataService struct {
	Ga *DataGaService

	Mcf *DataMcfService

	Realtime *DataRealtimeService
	// contains filtered or unexported fields
}
func NewDataService ¶
func NewDataService(s *Service) *DataService
type EntityAdWordsLink ¶
type EntityAdWordsLink struct {
	// AdWordsAccounts: A list of Google Ads client accounts. These cannot be MCC
	// accounts. This field is required when creating a Google Ads link. It cannot
	// be empty.
	AdWordsAccounts []*AdWordsAccount `json:"adWordsAccounts,omitempty"`
	// Entity: Web property being linked.
	Entity *EntityAdWordsLinkEntity `json:"entity,omitempty"`
	// Id: Entity Google Ads link ID
	Id string `json:"id,omitempty"`
	// Kind: Resource type for entity Google Ads link.
	Kind string `json:"kind,omitempty"`
	// Name: Name of the link. This field is required when creating a Google Ads
	// link.
	Name string `json:"name,omitempty"`
	// ProfileIds: IDs of linked Views (Profiles) represented as strings.
	ProfileIds []string `json:"profileIds,omitempty"`
	// SelfLink: URL link for this Google Analytics - Google Ads link.
	SelfLink string `json:"selfLink,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AdWordsAccounts") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AdWordsAccounts") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

EntityAdWordsLink: JSON template for Analytics Entity Google Ads Link.

func (EntityAdWordsLink) MarshalJSON ¶
func (s EntityAdWordsLink) MarshalJSON() ([]byte, error)
type EntityAdWordsLinkEntity ¶
type EntityAdWordsLinkEntity struct {
	WebPropertyRef *WebPropertyRef `json:"webPropertyRef,omitempty"`
	// ForceSendFields is a list of field names (e.g. "WebPropertyRef") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "WebPropertyRef") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

EntityAdWordsLinkEntity: Web property being linked.

func (EntityAdWordsLinkEntity) MarshalJSON ¶
func (s EntityAdWordsLinkEntity) MarshalJSON() ([]byte, error)
type EntityAdWordsLinks ¶
type EntityAdWordsLinks struct {
	// Items: A list of entity Google Ads links.
	Items []*EntityAdWordsLink `json:"items,omitempty"`
	// ItemsPerPage: The maximum number of entries the response can contain,
	// regardless of the actual number of entries returned. Its value ranges from 1
	// to 1000 with a value of 1000 by default, or otherwise specified by the
	// max-results query parameter.
	ItemsPerPage int64 `json:"itemsPerPage,omitempty"`
	// Kind: Collection type.
	Kind string `json:"kind,omitempty"`
	// NextLink: Next link for this Google Ads link collection.
	NextLink string `json:"nextLink,omitempty"`
	// PreviousLink: Previous link for this Google Ads link collection.
	PreviousLink string `json:"previousLink,omitempty"`
	// StartIndex: The starting index of the entries, which is 1 by default or
	// otherwise specified by the start-index query parameter.
	StartIndex int64 `json:"startIndex,omitempty"`
	// TotalResults: The total number of results for the query, regardless of the
	// number of results in the response.
	TotalResults int64 `json:"totalResults,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Items") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Items") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

EntityAdWordsLinks: An entity Google Ads link collection provides a list of GA-Google Ads links Each resource in this collection corresponds to a single link.

func (EntityAdWordsLinks) MarshalJSON ¶
func (s EntityAdWordsLinks) MarshalJSON() ([]byte, error)
type EntityUserLink ¶
type EntityUserLink struct {
	// Entity: Entity for this link. It can be an account, a web property, or a
	// view (profile).
	Entity *EntityUserLinkEntity `json:"entity,omitempty"`
	// Id: Entity user link ID
	Id string `json:"id,omitempty"`
	// Kind: Resource type for entity user link.
	Kind string `json:"kind,omitempty"`
	// Permissions: Permissions the user has for this entity.
	Permissions *EntityUserLinkPermissions `json:"permissions,omitempty"`
	// SelfLink: Self link for this resource.
	SelfLink string `json:"selfLink,omitempty"`
	// UserRef: User reference.
	UserRef *UserRef `json:"userRef,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Entity") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Entity") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

EntityUserLink: JSON template for an Analytics Entity-User Link. Returns permissions that a user has for an entity.

func (EntityUserLink) MarshalJSON ¶
func (s EntityUserLink) MarshalJSON() ([]byte, error)
type EntityUserLinkEntity ¶
type EntityUserLinkEntity struct {
	// AccountRef: Account for this link.
	AccountRef *AccountRef `json:"accountRef,omitempty"`
	// ProfileRef: View (Profile) for this link.
	ProfileRef *ProfileRef `json:"profileRef,omitempty"`
	// WebPropertyRef: Web property for this link.
	WebPropertyRef *WebPropertyRef `json:"webPropertyRef,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AccountRef") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccountRef") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

EntityUserLinkEntity: Entity for this link. It can be an account, a web property, or a view (profile).

func (EntityUserLinkEntity) MarshalJSON ¶
func (s EntityUserLinkEntity) MarshalJSON() ([]byte, error)
type EntityUserLinkPermissions ¶
type EntityUserLinkPermissions struct {
	// Effective: Effective permissions represent all the permissions that a user
	// has for this entity. These include any implied permissions (e.g., EDIT
	// implies VIEW) or inherited permissions from the parent entity. Effective
	// permissions are read-only.
	Effective []string `json:"effective,omitempty"`
	// Local: Permissions that a user has been assigned at this very level. Does
	// not include any implied or inherited permissions. Local permissions are
	// modifiable.
	Local []string `json:"local,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Effective") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Effective") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

EntityUserLinkPermissions: Permissions the user has for this entity.

func (EntityUserLinkPermissions) MarshalJSON ¶
func (s EntityUserLinkPermissions) MarshalJSON() ([]byte, error)
type EntityUserLinks ¶
type EntityUserLinks struct {
	// Items: A list of entity user links.
	Items []*EntityUserLink `json:"items,omitempty"`
	// ItemsPerPage: The maximum number of entries the response can contain,
	// regardless of the actual number of entries returned. Its value ranges from 1
	// to 1000 with a value of 1000 by default, or otherwise specified by the
	// max-results query parameter.
	ItemsPerPage int64 `json:"itemsPerPage,omitempty"`
	// Kind: Collection type.
	Kind string `json:"kind,omitempty"`
	// NextLink: Next link for this account collection.
	NextLink string `json:"nextLink,omitempty"`
	// PreviousLink: Previous link for this account collection.
	PreviousLink string `json:"previousLink,omitempty"`
	// StartIndex: The starting index of the entries, which is 1 by default or
	// otherwise specified by the start-index query parameter.
	StartIndex int64 `json:"startIndex,omitempty"`
	// TotalResults: The total number of results for the query, regardless of the
	// number of results in the response.
	TotalResults int64 `json:"totalResults,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Items") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Items") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

EntityUserLinks: An entity user link collection provides a list of Analytics ACL links Each resource in this collection corresponds to a single link.

func (EntityUserLinks) MarshalJSON ¶
func (s EntityUserLinks) MarshalJSON() ([]byte, error)
type Experiment ¶
type Experiment struct {
	// AccountId: Account ID to which this experiment belongs. This field is
	// read-only.
	AccountId string `json:"accountId,omitempty"`
	// Created: Time the experiment was created. This field is read-only.
	Created string `json:"created,omitempty"`
	// Description: Notes about this experiment.
	Description string `json:"description,omitempty"`
	// EditableInGaUi: If true, the end user will be able to edit the experiment
	// via the Google Analytics user interface.
	EditableInGaUi bool `json:"editableInGaUi,omitempty"`
	// EndTime: The ending time of the experiment (the time the status changed from
	// RUNNING to ENDED). This field is present only if the experiment has ended.
	// This field is read-only.
	EndTime string `json:"endTime,omitempty"`
	// EqualWeighting: Boolean specifying whether to distribute traffic evenly
	// across all variations. If the value is False, content experiments follows
	// the default behavior of adjusting traffic dynamically based on variation
	// performance. Optional -- defaults to False. This field may not be changed
	// for an experiment whose status is ENDED.
	EqualWeighting bool `json:"equalWeighting,omitempty"`
	// Id: Experiment ID. Required for patch and update. Disallowed for create.
	Id string `json:"id,omitempty"`
	// InternalWebPropertyId: Internal ID for the web property to which this
	// experiment belongs. This field is read-only.
	InternalWebPropertyId string `json:"internalWebPropertyId,omitempty"`
	// Kind: Resource type for an Analytics experiment. This field is read-only.
	Kind string `json:"kind,omitempty"`
	// MinimumExperimentLengthInDays: An integer number in [3, 90]. Specifies the
	// minimum length of the experiment. Can be changed for a running experiment.
	// This field may not be changed for an experiments whose status is ENDED.
	MinimumExperimentLengthInDays int64 `json:"minimumExperimentLengthInDays,omitempty"`
	// Name: Experiment name. This field may not be changed for an experiment whose
	// status is ENDED. This field is required when creating an experiment.
	Name string `json:"name,omitempty"`
	// ObjectiveMetric: The metric that the experiment is optimizing. Valid values:
	// "ga:goal(n)Completions", "ga:adsenseAdsClicks", "ga:adsenseAdsViewed",
	// "ga:adsenseRevenue", "ga:bounces", "ga:pageviews", "ga:sessionDuration",
	// "ga:transactions", "ga:transactionRevenue". This field is required if status
	// is "RUNNING" and servingFramework is one of "REDIRECT" or "API".
	ObjectiveMetric string `json:"objectiveMetric,omitempty"`
	// OptimizationType: Whether the objectiveMetric should be minimized or
	// maximized. Possible values: "MAXIMUM", "MINIMUM". Optional--defaults to
	// "MAXIMUM". Cannot be specified without objectiveMetric. Cannot be modified
	// when status is "RUNNING" or "ENDED".
	OptimizationType string `json:"optimizationType,omitempty"`
	// ParentLink: Parent link for an experiment. Points to the view (profile) to
	// which this experiment belongs.
	ParentLink *ExperimentParentLink `json:"parentLink,omitempty"`
	// ProfileId: View (Profile) ID to which this experiment belongs. This field is
	// read-only.
	ProfileId string `json:"profileId,omitempty"`
	// ReasonExperimentEnded: Why the experiment ended. Possible values:
	// "STOPPED_BY_USER", "WINNER_FOUND", "EXPERIMENT_EXPIRED",
	// "ENDED_WITH_NO_WINNER", "GOAL_OBJECTIVE_CHANGED". "ENDED_WITH_NO_WINNER"
	// means that the experiment didn't expire but no winner was projected to be
	// found. If the experiment status is changed via the API to ENDED this field
	// is set to STOPPED_BY_USER. This field is read-only.
	ReasonExperimentEnded string `json:"reasonExperimentEnded,omitempty"`
	// RewriteVariationUrlsAsOriginal: Boolean specifying whether variations URLS
	// are rewritten to match those of the original. This field may not be changed
	// for an experiments whose status is ENDED.
	RewriteVariationUrlsAsOriginal bool `json:"rewriteVariationUrlsAsOriginal,omitempty"`
	// SelfLink: Link for this experiment. This field is read-only.
	SelfLink string `json:"selfLink,omitempty"`
	// ServingFramework: The framework used to serve the experiment variations and
	// evaluate the results. One of:
	// - REDIRECT: Google Analytics redirects traffic to different variation pages,
	// reports the chosen variation and evaluates the results.
	// - API: Google Analytics chooses and reports the variation to serve and
	// evaluates the results; the caller is responsible for serving the selected
	// variation.
	// - EXTERNAL: The variations will be served externally and the chosen
	// variation reported to Google Analytics. The caller is responsible for
	// serving the selected variation and evaluating the results.
	ServingFramework string `json:"servingFramework,omitempty"`
	// Snippet: The snippet of code to include on the control page(s). This field
	// is read-only.
	Snippet string `json:"snippet,omitempty"`
	// StartTime: The starting time of the experiment (the time the status changed
	// from READY_TO_RUN to RUNNING). This field is present only if the experiment
	// has started. This field is read-only.
	StartTime string `json:"startTime,omitempty"`
	// Status: Experiment status. Possible values: "DRAFT", "READY_TO_RUN",
	// "RUNNING", "ENDED". Experiments can be created in the "DRAFT",
	// "READY_TO_RUN" or "RUNNING" state. This field is required when creating an
	// experiment.
	Status string `json:"status,omitempty"`
	// TrafficCoverage: A floating-point number in (0, 1]. Specifies the fraction
	// of the traffic that participates in the experiment. Can be changed for a
	// running experiment. This field may not be changed for an experiments whose
	// status is ENDED.
	TrafficCoverage float64 `json:"trafficCoverage,omitempty"`
	// Updated: Time the experiment was last modified. This field is read-only.
	Updated string `json:"updated,omitempty"`
	// Variations: Array of variations. The first variation in the array is the
	// original. The number of variations may not change once an experiment is in
	// the RUNNING state. At least two variations are required before status can be
	// set to RUNNING.
	Variations []*ExperimentVariations `json:"variations,omitempty"`
	// WebPropertyId: Web property ID to which this experiment belongs. The web
	// property ID is of the form UA-XXXXX-YY. This field is read-only.
	WebPropertyId string `json:"webPropertyId,omitempty"`
	// WinnerConfidenceLevel: A floating-point number in (0, 1). Specifies the
	// necessary confidence level to choose a winner. This field may not be changed
	// for an experiments whose status is ENDED.
	WinnerConfidenceLevel float64 `json:"winnerConfidenceLevel,omitempty"`
	// WinnerFound: Boolean specifying whether a winner has been found for this
	// experiment. This field is read-only.
	WinnerFound bool `json:"winnerFound,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AccountId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccountId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Experiment: JSON template for Analytics experiment resource.

func (Experiment) MarshalJSON ¶
func (s Experiment) MarshalJSON() ([]byte, error)
func (*Experiment) UnmarshalJSON ¶
func (s *Experiment) UnmarshalJSON(data []byte) error
type ExperimentParentLink ¶
type ExperimentParentLink struct {
	// Href: Link to the view (profile) to which this experiment belongs. This
	// field is read-only.
	Href string `json:"href,omitempty"`
	// Type: Value is "analytics#profile". This field is read-only.
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Href") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Href") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ExperimentParentLink: Parent link for an experiment. Points to the view (profile) to which this experiment belongs.

func (ExperimentParentLink) MarshalJSON ¶
func (s ExperimentParentLink) MarshalJSON() ([]byte, error)
type ExperimentVariations ¶
type ExperimentVariations struct {
	// Name: The name of the variation. This field is required when creating an
	// experiment. This field may not be changed for an experiment whose status is
	// ENDED.
	Name string `json:"name,omitempty"`
	// Status: Status of the variation. Possible values: "ACTIVE", "INACTIVE".
	// INACTIVE variations are not served. This field may not be changed for an
	// experiment whose status is ENDED.
	Status string `json:"status,omitempty"`
	// Url: The URL of the variation. This field may not be changed for an
	// experiment whose status is RUNNING or ENDED.
	Url string `json:"url,omitempty"`
	// Weight: Weight that this variation should receive. Only present if the
	// experiment is running. This field is read-only.
	Weight float64 `json:"weight,omitempty"`
	// Won: True if the experiment has ended and this variation performed
	// (statistically) significantly better than the original. This field is
	// read-only.
	Won bool `json:"won,omitempty"`
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
func (ExperimentVariations) MarshalJSON ¶
func (s ExperimentVariations) MarshalJSON() ([]byte, error)
func (*ExperimentVariations) UnmarshalJSON ¶
func (s *ExperimentVariations) UnmarshalJSON(data []byte) error
type Experiments ¶
type Experiments struct {
	// Items: A list of experiments.
	Items []*Experiment `json:"items,omitempty"`
	// ItemsPerPage: The maximum number of resources the response can contain,
	// regardless of the actual number of resources returned. Its value ranges from
	// 1 to 1000 with a value of 1000 by default, or otherwise specified by the
	// max-results query parameter.
	ItemsPerPage int64 `json:"itemsPerPage,omitempty"`
	// Kind: Collection type.
	Kind string `json:"kind,omitempty"`
	// NextLink: Link to next page for this experiment collection.
	NextLink string `json:"nextLink,omitempty"`
	// PreviousLink: Link to previous page for this experiment collection.
	PreviousLink string `json:"previousLink,omitempty"`
	// StartIndex: The starting index of the resources, which is 1 by default or
	// otherwise specified by the start-index query parameter.
	StartIndex int64 `json:"startIndex,omitempty"`
	// TotalResults: The total number of results for the query, regardless of the
	// number of resources in the result.
	TotalResults int64 `json:"totalResults,omitempty"`
	// Username: Email ID of the authenticated user
	Username string `json:"username,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Items") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Items") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Experiments: An experiment collection lists Analytics experiments to which the user has access. Each view (profile) can have a set of experiments. Each resource in the Experiment collection corresponds to a single Analytics experiment.

func (Experiments) MarshalJSON ¶
func (s Experiments) MarshalJSON() ([]byte, error)
type Filter ¶
type Filter struct {
	// AccountId: Account ID to which this filter belongs.
	AccountId string `json:"accountId,omitempty"`
	// AdvancedDetails: Details for the filter of the type ADVANCED.
	AdvancedDetails *FilterAdvancedDetails `json:"advancedDetails,omitempty"`
	// Created: Time this filter was created.
	Created string `json:"created,omitempty"`
	// ExcludeDetails: Details for the filter of the type EXCLUDE.
	ExcludeDetails *FilterExpression `json:"excludeDetails,omitempty"`
	// Id: Filter ID.
	Id string `json:"id,omitempty"`
	// IncludeDetails: Details for the filter of the type INCLUDE.
	IncludeDetails *FilterExpression `json:"includeDetails,omitempty"`
	// Kind: Resource type for Analytics filter.
	Kind string `json:"kind,omitempty"`
	// LowercaseDetails: Details for the filter of the type LOWER.
	LowercaseDetails *FilterLowercaseDetails `json:"lowercaseDetails,omitempty"`
	// Name: Name of this filter.
	Name string `json:"name,omitempty"`
	// ParentLink: Parent link for this filter. Points to the account to which this
	// filter belongs.
	ParentLink *FilterParentLink `json:"parentLink,omitempty"`
	// SearchAndReplaceDetails: Details for the filter of the type
	// SEARCH_AND_REPLACE.
	SearchAndReplaceDetails *FilterSearchAndReplaceDetails `json:"searchAndReplaceDetails,omitempty"`
	// SelfLink: Link for this filter.
	SelfLink string `json:"selfLink,omitempty"`
	// Type: Type of this filter. Possible values are INCLUDE, EXCLUDE, LOWERCASE,
	// UPPERCASE, SEARCH_AND_REPLACE and ADVANCED.
	Type string `json:"type,omitempty"`
	// Updated: Time this filter was last modified.
	Updated string `json:"updated,omitempty"`
	// UppercaseDetails: Details for the filter of the type UPPER.
	UppercaseDetails *FilterUppercaseDetails `json:"uppercaseDetails,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AccountId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccountId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Filter: JSON template for an Analytics account filter.

func (Filter) MarshalJSON ¶
func (s Filter) MarshalJSON() ([]byte, error)
type FilterAdvancedDetails ¶
type FilterAdvancedDetails struct {
	// CaseSensitive: Indicates if the filter expressions are case sensitive.
	CaseSensitive bool `json:"caseSensitive,omitempty"`
	// ExtractA: Expression to extract from field A.
	ExtractA string `json:"extractA,omitempty"`
	// ExtractB: Expression to extract from field B.
	ExtractB string `json:"extractB,omitempty"`
	// FieldA: Field A.
	FieldA string `json:"fieldA,omitempty"`
	// FieldAIndex: The Index of the custom dimension. Required if field is a
	// CUSTOM_DIMENSION.
	FieldAIndex int64 `json:"fieldAIndex,omitempty"`
	// FieldARequired: Indicates if field A is required to match.
	FieldARequired bool `json:"fieldARequired,omitempty"`
	// FieldB: Field B.
	FieldB string `json:"fieldB,omitempty"`
	// FieldBIndex: The Index of the custom dimension. Required if field is a
	// CUSTOM_DIMENSION.
	FieldBIndex int64 `json:"fieldBIndex,omitempty"`
	// FieldBRequired: Indicates if field B is required to match.
	FieldBRequired bool `json:"fieldBRequired,omitempty"`
	// OutputConstructor: Expression used to construct the output value.
	OutputConstructor string `json:"outputConstructor,omitempty"`
	// OutputToField: Output field.
	OutputToField string `json:"outputToField,omitempty"`
	// OutputToFieldIndex: The Index of the custom dimension. Required if field is
	// a CUSTOM_DIMENSION.
	OutputToFieldIndex int64 `json:"outputToFieldIndex,omitempty"`
	// OverrideOutputField: Indicates if the existing value of the output field, if
	// any, should be overridden by the output expression.
	OverrideOutputField bool `json:"overrideOutputField,omitempty"`
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

FilterAdvancedDetails: Details for the filter of the type ADVANCED.

func (FilterAdvancedDetails) MarshalJSON ¶
func (s FilterAdvancedDetails) MarshalJSON() ([]byte, error)
type FilterExpression ¶
type FilterExpression struct {
	// CaseSensitive: Determines if the filter is case sensitive.
	CaseSensitive bool `json:"caseSensitive,omitempty"`
	// ExpressionValue: Filter expression value
	ExpressionValue string `json:"expressionValue,omitempty"`
	// Field: Field to filter. Possible values:
	// - Content and Traffic
	// - PAGE_REQUEST_URI,
	// - PAGE_HOSTNAME,
	// - PAGE_TITLE,
	// - REFERRAL,
	// - COST_DATA_URI (Campaign target URL),
	// - HIT_TYPE,
	// - INTERNAL_SEARCH_TERM,
	// - INTERNAL_SEARCH_TYPE,
	// - SOURCE_PROPERTY_TRACKING_ID,
	// - Campaign or AdGroup
	// - CAMPAIGN_SOURCE,
	// - CAMPAIGN_MEDIUM,
	// - CAMPAIGN_NAME,
	// - CAMPAIGN_AD_GROUP,
	// - CAMPAIGN_TERM,
	// - CAMPAIGN_CONTENT,
	// - CAMPAIGN_CODE,
	// - CAMPAIGN_REFERRAL_PATH,
	// - E-Commerce
	// - TRANSACTION_COUNTRY,
	// - TRANSACTION_REGION,
	// - TRANSACTION_CITY,
	// - TRANSACTION_AFFILIATION (Store or order location),
	// - ITEM_NAME,
	// - ITEM_CODE,
	// - ITEM_VARIATION,
	// - TRANSACTION_ID,
	// - TRANSACTION_CURRENCY_CODE,
	// - PRODUCT_ACTION_TYPE,
	// - Audience/Users
	// - BROWSER,
	// - BROWSER_VERSION,
	// - BROWSER_SIZE,
	// - PLATFORM,
	// - PLATFORM_VERSION,
	// - LANGUAGE,
	// - SCREEN_RESOLUTION,
	// - SCREEN_COLORS,
	// - JAVA_ENABLED (Boolean Field),
	// - FLASH_VERSION,
	// - GEO_SPEED (Connection speed),
	// - VISITOR_TYPE,
	// - GEO_ORGANIZATION (ISP organization),
	// - GEO_DOMAIN,
	// - GEO_IP_ADDRESS,
	// - GEO_IP_VERSION,
	// - Location
	// - GEO_COUNTRY,
	// - GEO_REGION,
	// - GEO_CITY,
	// - Event
	// - EVENT_CATEGORY,
	// - EVENT_ACTION,
	// - EVENT_LABEL,
	// - Other
	// - CUSTOM_FIELD_1,
	// - CUSTOM_FIELD_2,
	// - USER_DEFINED_VALUE,
	// - Application
	// - APP_ID,
	// - APP_INSTALLER_ID,
	// - APP_NAME,
	// - APP_VERSION,
	// - SCREEN,
	// - IS_APP (Boolean Field),
	// - IS_FATAL_EXCEPTION (Boolean Field),
	// - EXCEPTION_DESCRIPTION,
	// - Mobile device
	// - IS_MOBILE (Boolean Field, Deprecated. Use DEVICE_CATEGORY=mobile),
	// - IS_TABLET (Boolean Field, Deprecated. Use DEVICE_CATEGORY=tablet),
	// - DEVICE_CATEGORY,
	// - MOBILE_HAS_QWERTY_KEYBOARD (Boolean Field),
	// - MOBILE_HAS_NFC_SUPPORT (Boolean Field),
	// - MOBILE_HAS_CELLULAR_RADIO (Boolean Field),
	// - MOBILE_HAS_WIFI_SUPPORT (Boolean Field),
	// - MOBILE_BRAND_NAME,
	// - MOBILE_MODEL_NAME,
	// - MOBILE_MARKETING_NAME,
	// - MOBILE_POINTING_METHOD,
	// - Social
	// - SOCIAL_NETWORK,
	// - SOCIAL_ACTION,
	// - SOCIAL_ACTION_TARGET,
	// - Custom dimension
	// - CUSTOM_DIMENSION (See accompanying field index),
	Field string `json:"field,omitempty"`
	// FieldIndex: The Index of the custom dimension. Set only if the field is a is
	// CUSTOM_DIMENSION.
	FieldIndex int64 `json:"fieldIndex,omitempty"`
	// Kind: Kind value for filter expression
	Kind string `json:"kind,omitempty"`
	// MatchType: Match type for this filter. Possible values are BEGINS_WITH,
	// EQUAL, ENDS_WITH, CONTAINS, or MATCHES. GEO_DOMAIN, GEO_IP_ADDRESS,
	// PAGE_REQUEST_URI, or PAGE_HOSTNAME filters can use any match type; all other
	// filters must use MATCHES.
	MatchType string `json:"matchType,omitempty"`
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

FilterExpression: JSON template for an Analytics filter expression.

func (FilterExpression) MarshalJSON ¶
func (s FilterExpression) MarshalJSON() ([]byte, error)
type FilterLowercaseDetails ¶
type FilterLowercaseDetails struct {
	// Field: Field to use in the filter.
	Field string `json:"field,omitempty"`
	// FieldIndex: The Index of the custom dimension. Required if field is a
	// CUSTOM_DIMENSION.
	FieldIndex int64 `json:"fieldIndex,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Field") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Field") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

FilterLowercaseDetails: Details for the filter of the type LOWER.

func (FilterLowercaseDetails) MarshalJSON ¶
func (s FilterLowercaseDetails) MarshalJSON() ([]byte, error)
type FilterParentLink ¶
type FilterParentLink struct {
	// Href: Link to the account to which this filter belongs.
	Href string `json:"href,omitempty"`
	// Type: Value is "analytics#account".
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Href") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Href") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

FilterParentLink: Parent link for this filter. Points to the account to which this filter belongs.

func (FilterParentLink) MarshalJSON ¶
func (s FilterParentLink) MarshalJSON() ([]byte, error)
type FilterRef ¶
type FilterRef struct {
	// AccountId: Account ID to which this filter belongs.
	AccountId string `json:"accountId,omitempty"`
	// Href: Link for this filter.
	Href string `json:"href,omitempty"`
	// Id: Filter ID.
	Id string `json:"id,omitempty"`
	// Kind: Kind value for filter reference.
	Kind string `json:"kind,omitempty"`
	// Name: Name of this filter.
	Name string `json:"name,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AccountId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccountId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

FilterRef: JSON template for a profile filter link.

func (FilterRef) MarshalJSON ¶
func (s FilterRef) MarshalJSON() ([]byte, error)
type FilterSearchAndReplaceDetails ¶
type FilterSearchAndReplaceDetails struct {
	// CaseSensitive: Determines if the filter is case sensitive.
	CaseSensitive bool `json:"caseSensitive,omitempty"`
	// Field: Field to use in the filter.
	Field string `json:"field,omitempty"`
	// FieldIndex: The Index of the custom dimension. Required if field is a
	// CUSTOM_DIMENSION.
	FieldIndex int64 `json:"fieldIndex,omitempty"`
	// ReplaceString: Term to replace the search term with.
	ReplaceString string `json:"replaceString,omitempty"`
	// SearchString: Term to search.
	SearchString string `json:"searchString,omitempty"`
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

FilterSearchAndReplaceDetails: Details for the filter of the type SEARCH_AND_REPLACE.

func (FilterSearchAndReplaceDetails) MarshalJSON ¶
func (s FilterSearchAndReplaceDetails) MarshalJSON() ([]byte, error)
type FilterUppercaseDetails ¶
type FilterUppercaseDetails struct {
	// Field: Field to use in the filter.
	Field string `json:"field,omitempty"`
	// FieldIndex: The Index of the custom dimension. Required if field is a
	// CUSTOM_DIMENSION.
	FieldIndex int64 `json:"fieldIndex,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Field") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Field") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

FilterUppercaseDetails: Details for the filter of the type UPPER.

func (FilterUppercaseDetails) MarshalJSON ¶
func (s FilterUppercaseDetails) MarshalJSON() ([]byte, error)
type Filters ¶
type Filters struct {
	// Items: A list of filters.
	Items []*Filter `json:"items,omitempty"`
	// ItemsPerPage: The maximum number of resources the response can contain,
	// regardless of the actual number of resources returned. Its value ranges from
	// 1 to 1,000 with a value of 1000 by default, or otherwise specified by the
	// max-results query parameter.
	ItemsPerPage int64 `json:"itemsPerPage,omitempty"`
	// Kind: Collection type.
	Kind string `json:"kind,omitempty"`
	// NextLink: Link to next page for this filter collection.
	NextLink string `json:"nextLink,omitempty"`
	// PreviousLink: Link to previous page for this filter collection.
	PreviousLink string `json:"previousLink,omitempty"`
	// StartIndex: The starting index of the resources, which is 1 by default or
	// otherwise specified by the start-index query parameter.
	StartIndex int64 `json:"startIndex,omitempty"`
	// TotalResults: The total number of results for the query, regardless of the
	// number of results in the response.
	TotalResults int64 `json:"totalResults,omitempty"`
	// Username: Email ID of the authenticated user
	Username string `json:"username,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Items") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Items") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Filters: A filter collection lists filters created by users in an Analytics account. Each resource in the collection corresponds to a filter.

func (Filters) MarshalJSON ¶
func (s Filters) MarshalJSON() ([]byte, error)
type GaData ¶
type GaData struct {
	// ColumnHeaders: Column headers that list dimension names followed by the
	// metric names. The order of dimensions and metrics is same as specified in
	// the request.
	ColumnHeaders []*GaDataColumnHeaders `json:"columnHeaders,omitempty"`
	// ContainsSampledData: Determines if Analytics data contains samples.
	ContainsSampledData bool `json:"containsSampledData,omitempty"`
	// DataLastRefreshed: The last refreshed time in seconds for Analytics data.
	DataLastRefreshed int64            `json:"dataLastRefreshed,omitempty,string"`
	DataTable         *GaDataDataTable `json:"dataTable,omitempty"`
	// Id: Unique ID for this data response.
	Id string `json:"id,omitempty"`
	// ItemsPerPage: The maximum number of rows the response can contain,
	// regardless of the actual number of rows returned. Its value ranges from 1 to
	// 10,000 with a value of 1000 by default, or otherwise specified by the
	// max-results query parameter.
	ItemsPerPage int64 `json:"itemsPerPage,omitempty"`
	// Kind: Resource type.
	Kind string `json:"kind,omitempty"`
	// NextLink: Link to next page for this Analytics data query.
	NextLink string `json:"nextLink,omitempty"`
	// PreviousLink: Link to previous page for this Analytics data query.
	PreviousLink string `json:"previousLink,omitempty"`
	// ProfileInfo: Information for the view (profile), for which the Analytics
	// data was requested.
	ProfileInfo *GaDataProfileInfo `json:"profileInfo,omitempty"`
	// Query: Analytics data request query parameters.
	Query *GaDataQuery `json:"query,omitempty"`
	// Rows: Analytics data rows, where each row contains a list of dimension
	// values followed by the metric values. The order of dimensions and metrics is
	// same as specified in the request.
	Rows [][]string `json:"rows,omitempty"`
	// SampleSize: The number of samples used to calculate the result.
	SampleSize int64 `json:"sampleSize,omitempty,string"`
	// SampleSpace: Total size of the sample space from which the samples were
	// selected.
	SampleSpace int64 `json:"sampleSpace,omitempty,string"`
	// SelfLink: Link to this page.
	SelfLink string `json:"selfLink,omitempty"`
	// TotalResults: The total number of rows for the query, regardless of the
	// number of rows in the response.
	TotalResults int64 `json:"totalResults,omitempty"`
	// TotalsForAllResults: Total values for the requested metrics over all the
	// results, not just the results returned in this response. The order of the
	// metric totals is same as the metric order specified in the request.
	TotalsForAllResults map[string]string `json:"totalsForAllResults,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ColumnHeaders") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ColumnHeaders") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GaData: Analytics data for a given view (profile).

func (GaData) MarshalJSON ¶
func (s GaData) MarshalJSON() ([]byte, error)
type GaDataColumnHeaders ¶
type GaDataColumnHeaders struct {
	// ColumnType: Column Type. Either DIMENSION or METRIC.
	ColumnType string `json:"columnType,omitempty"`
	// DataType: Data type. Dimension column headers have only STRING as the data
	// type. Metric column headers have data types for metric values such as
	// INTEGER, DOUBLE, CURRENCY etc.
	DataType string `json:"dataType,omitempty"`
	// Name: Column name.
	Name string `json:"name,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ColumnType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ColumnType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (GaDataColumnHeaders) MarshalJSON ¶
func (s GaDataColumnHeaders) MarshalJSON() ([]byte, error)
type GaDataDataTable ¶
type GaDataDataTable struct {
	Cols []*GaDataDataTableCols `json:"cols,omitempty"`
	Rows []*GaDataDataTableRows `json:"rows,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Cols") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Cols") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (GaDataDataTable) MarshalJSON ¶
func (s GaDataDataTable) MarshalJSON() ([]byte, error)
type GaDataDataTableCols ¶
type GaDataDataTableCols struct {
	Id    string `json:"id,omitempty"`
	Label string `json:"label,omitempty"`
	Type  string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Id") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Id") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (GaDataDataTableCols) MarshalJSON ¶
func (s GaDataDataTableCols) MarshalJSON() ([]byte, error)
type GaDataDataTableRows ¶
type GaDataDataTableRows struct {
	C []*GaDataDataTableRowsC `json:"c,omitempty"`
	// ForceSendFields is a list of field names (e.g. "C") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "C") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (GaDataDataTableRows) MarshalJSON ¶
func (s GaDataDataTableRows) MarshalJSON() ([]byte, error)
type GaDataDataTableRowsC ¶
type GaDataDataTableRowsC struct {
	V string `json:"v,omitempty"`
	// ForceSendFields is a list of field names (e.g. "V") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "V") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (GaDataDataTableRowsC) MarshalJSON ¶
func (s GaDataDataTableRowsC) MarshalJSON() ([]byte, error)
type GaDataProfileInfo ¶
type GaDataProfileInfo struct {
	// AccountId: Account ID to which this view (profile) belongs.
	AccountId string `json:"accountId,omitempty"`
	// InternalWebPropertyId: Internal ID for the web property to which this view
	// (profile) belongs.
	InternalWebPropertyId string `json:"internalWebPropertyId,omitempty"`
	// ProfileId: View (Profile) ID.
	ProfileId string `json:"profileId,omitempty"`
	// ProfileName: View (Profile) name.
	ProfileName string `json:"profileName,omitempty"`
	// TableId: Table ID for view (profile).
	TableId string `json:"tableId,omitempty"`
	// WebPropertyId: Web Property ID to which this view (profile) belongs.
	WebPropertyId string `json:"webPropertyId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AccountId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccountId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GaDataProfileInfo: Information for the view (profile), for which the Analytics data was requested.

func (GaDataProfileInfo) MarshalJSON ¶
func (s GaDataProfileInfo) MarshalJSON() ([]byte, error)
type GaDataQuery ¶
type GaDataQuery struct {
	// Dimensions: List of analytics dimensions.
	Dimensions string `json:"dimensions,omitempty"`
	// EndDate: End date.
	EndDate string `json:"end-date,omitempty"`
	// Filters: Comma-separated list of dimension or metric filters.
	Filters string `json:"filters,omitempty"`
	// Ids: Unique table ID.
	Ids string `json:"ids,omitempty"`
	// MaxResults: Maximum results per page.
	MaxResults int64 `json:"max-results,omitempty"`
	// Metrics: List of analytics metrics.
	Metrics []string `json:"metrics,omitempty"`
	// SamplingLevel: Desired sampling level
	SamplingLevel string `json:"samplingLevel,omitempty"`
	// Segment: Analytics advanced segment.
	Segment string `json:"segment,omitempty"`
	// Sort: List of dimensions or metrics based on which Analytics data is sorted.
	Sort []string `json:"sort,omitempty"`
	// StartDate: Start date.
	StartDate string `json:"start-date,omitempty"`
	// StartIndex: Start index.
	StartIndex int64 `json:"start-index,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Dimensions") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Dimensions") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GaDataQuery: Analytics data request query parameters.

func (GaDataQuery) MarshalJSON ¶
func (s GaDataQuery) MarshalJSON() ([]byte, error)
type Goal ¶
type Goal struct {
	// AccountId: Account ID to which this goal belongs.
	AccountId string `json:"accountId,omitempty"`
	// Active: Determines whether this goal is active.
	Active bool `json:"active,omitempty"`
	// Created: Time this goal was created.
	Created string `json:"created,omitempty"`
	// EventDetails: Details for the goal of the type EVENT.
	EventDetails *GoalEventDetails `json:"eventDetails,omitempty"`
	// Id: Goal ID.
	Id string `json:"id,omitempty"`
	// InternalWebPropertyId: Internal ID for the web property to which this goal
	// belongs.
	InternalWebPropertyId string `json:"internalWebPropertyId,omitempty"`
	// Kind: Resource type for an Analytics goal.
	Kind string `json:"kind,omitempty"`
	// Name: Goal name.
	Name string `json:"name,omitempty"`
	// ParentLink: Parent link for a goal. Points to the view (profile) to which
	// this goal belongs.
	ParentLink *GoalParentLink `json:"parentLink,omitempty"`
	// ProfileId: View (Profile) ID to which this goal belongs.
	ProfileId string `json:"profileId,omitempty"`
	// SelfLink: Link for this goal.
	SelfLink string `json:"selfLink,omitempty"`
	// Type: Goal type. Possible values are URL_DESTINATION, VISIT_TIME_ON_SITE,
	// VISIT_NUM_PAGES, AND EVENT.
	Type string `json:"type,omitempty"`
	// Updated: Time this goal was last modified.
	Updated string `json:"updated,omitempty"`
	// UrlDestinationDetails: Details for the goal of the type URL_DESTINATION.
	UrlDestinationDetails *GoalUrlDestinationDetails `json:"urlDestinationDetails,omitempty"`
	// Value: Goal value.
	Value float64 `json:"value,omitempty"`
	// VisitNumPagesDetails: Details for the goal of the type VISIT_NUM_PAGES.
	VisitNumPagesDetails *GoalVisitNumPagesDetails `json:"visitNumPagesDetails,omitempty"`
	// VisitTimeOnSiteDetails: Details for the goal of the type VISIT_TIME_ON_SITE.
	VisitTimeOnSiteDetails *GoalVisitTimeOnSiteDetails `json:"visitTimeOnSiteDetails,omitempty"`
	// WebPropertyId: Web property ID to which this goal belongs. The web property
	// ID is of the form UA-XXXXX-YY.
	WebPropertyId string `json:"webPropertyId,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AccountId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccountId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Goal: JSON template for Analytics goal resource.

func (Goal) MarshalJSON ¶
func (s Goal) MarshalJSON() ([]byte, error)
func (*Goal) UnmarshalJSON ¶
func (s *Goal) UnmarshalJSON(data []byte) error
type GoalEventDetails ¶
type GoalEventDetails struct {
	// EventConditions: List of event conditions.
	EventConditions []*GoalEventDetailsEventConditions `json:"eventConditions,omitempty"`
	// UseEventValue: Determines if the event value should be used as the value for
	// this goal.
	UseEventValue bool `json:"useEventValue,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EventConditions") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EventConditions") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoalEventDetails: Details for the goal of the type EVENT.

func (GoalEventDetails) MarshalJSON ¶
func (s GoalEventDetails) MarshalJSON() ([]byte, error)
type GoalEventDetailsEventConditions ¶
type GoalEventDetailsEventConditions struct {
	// ComparisonType: Type of comparison. Possible values are LESS_THAN,
	// GREATER_THAN or EQUAL.
	ComparisonType string `json:"comparisonType,omitempty"`
	// ComparisonValue: Value used for this comparison.
	ComparisonValue int64 `json:"comparisonValue,omitempty,string"`
	// Expression: Expression used for this match.
	Expression string `json:"expression,omitempty"`
	// MatchType: Type of the match to be performed. Possible values are REGEXP,
	// BEGINS_WITH, or EXACT.
	MatchType string `json:"matchType,omitempty"`
	// Type: Type of this event condition. Possible values are CATEGORY, ACTION,
	// LABEL, or VALUE.
	Type string `json:"type,omitempty"`
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
func (GoalEventDetailsEventConditions) MarshalJSON ¶
func (s GoalEventDetailsEventConditions) MarshalJSON() ([]byte, error)
type GoalParentLink ¶
type GoalParentLink struct {
	// Href: Link to the view (profile) to which this goal belongs.
	Href string `json:"href,omitempty"`
	// Type: Value is "analytics#profile".
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Href") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Href") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoalParentLink: Parent link for a goal. Points to the view (profile) to which this goal belongs.

func (GoalParentLink) MarshalJSON ¶
func (s GoalParentLink) MarshalJSON() ([]byte, error)
type GoalUrlDestinationDetails ¶
type GoalUrlDestinationDetails struct {
	// CaseSensitive: Determines if the goal URL must exactly match the
	// capitalization of visited URLs.
	CaseSensitive bool `json:"caseSensitive,omitempty"`
	// FirstStepRequired: Determines if the first step in this goal is required.
	FirstStepRequired bool `json:"firstStepRequired,omitempty"`
	// MatchType: Match type for the goal URL. Possible values are HEAD, EXACT, or
	// REGEX.
	MatchType string `json:"matchType,omitempty"`
	// Steps: List of steps configured for this goal funnel.
	Steps []*GoalUrlDestinationDetailsSteps `json:"steps,omitempty"`
	// Url: URL for this goal.
	Url string `json:"url,omitempty"`
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

GoalUrlDestinationDetails: Details for the goal of the type URL_DESTINATION.

func (GoalUrlDestinationDetails) MarshalJSON ¶
func (s GoalUrlDestinationDetails) MarshalJSON() ([]byte, error)
type GoalUrlDestinationDetailsSteps ¶
type GoalUrlDestinationDetailsSteps struct {
	// Name: Step name.
	Name string `json:"name,omitempty"`
	// Number: Step number.
	Number int64 `json:"number,omitempty"`
	// Url: URL for this step.
	Url string `json:"url,omitempty"`
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
func (GoalUrlDestinationDetailsSteps) MarshalJSON ¶
func (s GoalUrlDestinationDetailsSteps) MarshalJSON() ([]byte, error)
type GoalVisitNumPagesDetails ¶
type GoalVisitNumPagesDetails struct {
	// ComparisonType: Type of comparison. Possible values are LESS_THAN,
	// GREATER_THAN, or EQUAL.
	ComparisonType string `json:"comparisonType,omitempty"`
	// ComparisonValue: Value used for this comparison.
	ComparisonValue int64 `json:"comparisonValue,omitempty,string"`
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

GoalVisitNumPagesDetails: Details for the goal of the type VISIT_NUM_PAGES.

func (GoalVisitNumPagesDetails) MarshalJSON ¶
func (s GoalVisitNumPagesDetails) MarshalJSON() ([]byte, error)
type GoalVisitTimeOnSiteDetails ¶
type GoalVisitTimeOnSiteDetails struct {
	// ComparisonType: Type of comparison. Possible values are LESS_THAN or
	// GREATER_THAN.
	ComparisonType string `json:"comparisonType,omitempty"`
	// ComparisonValue: Value used for this comparison.
	ComparisonValue int64 `json:"comparisonValue,omitempty,string"`
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

GoalVisitTimeOnSiteDetails: Details for the goal of the type VISIT_TIME_ON_SITE.

func (GoalVisitTimeOnSiteDetails) MarshalJSON ¶
func (s GoalVisitTimeOnSiteDetails) MarshalJSON() ([]byte, error)
type Goals ¶
type Goals struct {
	// Items: A list of goals.
	Items []*Goal `json:"items,omitempty"`
	// ItemsPerPage: The maximum number of resources the response can contain,
	// regardless of the actual number of resources returned. Its value ranges from
	// 1 to 1000 with a value of 1000 by default, or otherwise specified by the
	// max-results query parameter.
	ItemsPerPage int64 `json:"itemsPerPage,omitempty"`
	// Kind: Collection type.
	Kind string `json:"kind,omitempty"`
	// NextLink: Link to next page for this goal collection.
	NextLink string `json:"nextLink,omitempty"`
	// PreviousLink: Link to previous page for this goal collection.
	PreviousLink string `json:"previousLink,omitempty"`
	// StartIndex: The starting index of the resources, which is 1 by default or
	// otherwise specified by the start-index query parameter.
	StartIndex int64 `json:"startIndex,omitempty"`
	// TotalResults: The total number of results for the query, regardless of the
	// number of resources in the result.
	TotalResults int64 `json:"totalResults,omitempty"`
	// Username: Email ID of the authenticated user
	Username string `json:"username,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Items") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Items") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Goals: A goal collection lists Analytics goals to which the user has access. Each view (profile) can have a set of goals. Each resource in the Goal collection corresponds to a single Analytics goal.

func (Goals) MarshalJSON ¶
func (s Goals) MarshalJSON() ([]byte, error)
type HashClientIdRequest ¶
type HashClientIdRequest struct {
	ClientId      string `json:"clientId,omitempty"`
	Kind          string `json:"kind,omitempty"`
	WebPropertyId string `json:"webPropertyId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ClientId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ClientId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

HashClientIdRequest: JSON template for a hash Client Id request resource.

func (HashClientIdRequest) MarshalJSON ¶
func (s HashClientIdRequest) MarshalJSON() ([]byte, error)
type HashClientIdResponse ¶
type HashClientIdResponse struct {
	ClientId       string `json:"clientId,omitempty"`
	HashedClientId string `json:"hashedClientId,omitempty"`
	Kind           string `json:"kind,omitempty"`
	WebPropertyId  string `json:"webPropertyId,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ClientId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ClientId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

HashClientIdResponse: JSON template for a hash Client Id response resource.

func (HashClientIdResponse) MarshalJSON ¶
func (s HashClientIdResponse) MarshalJSON() ([]byte, error)
type IncludeConditions ¶
type IncludeConditions struct {
	// DaysToLookBack: The look-back window lets you specify a time frame for
	// evaluating the behavior that qualifies users for your audience. For example,
	// if your filters include users from Central Asia, and Transactions Greater
	// than 2, and you set the look-back window to 14 days, then any user from
	// Central Asia whose cumulative transactions exceed 2 during the last 14 days
	// is added to the audience.
	DaysToLookBack int64 `json:"daysToLookBack,omitempty"`
	// IsSmartList: Boolean indicating whether this segment is a smart list.
	// https://support.google.com/analytics/answer/4628577
	IsSmartList bool `json:"isSmartList,omitempty"`
	// Kind: Resource type for include conditions.
	Kind string `json:"kind,omitempty"`
	// MembershipDurationDays: Number of days (in the range 1 to 540) a user
	// remains in the audience.
	MembershipDurationDays int64 `json:"membershipDurationDays,omitempty"`
	// Segment: The segment condition that will cause a user to be added to an
	// audience.
	Segment string `json:"segment,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DaysToLookBack") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DaysToLookBack") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

IncludeConditions: JSON template for an Analytics Remarketing Include Conditions.

func (IncludeConditions) MarshalJSON ¶
func (s IncludeConditions) MarshalJSON() ([]byte, error)
type LinkedForeignAccount ¶
type LinkedForeignAccount struct {
	// AccountId: Account ID to which this linked foreign account belongs.
	AccountId string `json:"accountId,omitempty"`
	// EligibleForSearch: Boolean indicating whether this is eligible for search.
	EligibleForSearch bool `json:"eligibleForSearch,omitempty"`
	// Id: Entity ad account link ID.
	Id string `json:"id,omitempty"`
	// InternalWebPropertyId: Internal ID for the web property to which this linked
	// foreign account belongs.
	InternalWebPropertyId string `json:"internalWebPropertyId,omitempty"`
	// Kind: Resource type for linked foreign account.
	Kind string `json:"kind,omitempty"`
	// LinkedAccountId: The foreign account ID. For example the an Google Ads
	// `linkedAccountId` has the following format XXX-XXX-XXXX.
	LinkedAccountId string `json:"linkedAccountId,omitempty"`
	// RemarketingAudienceId: Remarketing audience ID to which this linked foreign
	// account belongs.
	RemarketingAudienceId string `json:"remarketingAudienceId,omitempty"`
	// Status: The status of this foreign account link.
	Status string `json:"status,omitempty"`
	// Type: The type of the foreign account. For example, `ADWORDS_LINKS`,
	// `DBM_LINKS`, `MCC_LINKS` or `OPTIMIZE`.
	Type string `json:"type,omitempty"`
	// WebPropertyId: Web property ID of the form UA-XXXXX-YY to which this linked
	// foreign account belongs.
	WebPropertyId string `json:"webPropertyId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AccountId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccountId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

LinkedForeignAccount: JSON template for an Analytics Remarketing Audience Foreign Link.

func (LinkedForeignAccount) MarshalJSON ¶
func (s LinkedForeignAccount) MarshalJSON() ([]byte, error)
type ManagementAccountSummariesListCall ¶
type ManagementAccountSummariesListCall struct {
	// contains filtered or unexported fields
}
func (*ManagementAccountSummariesListCall) Context ¶
func (c *ManagementAccountSummariesListCall) Context(ctx context.Context) *ManagementAccountSummariesListCall

Context sets the context to be used in this call's Do method.

func (*ManagementAccountSummariesListCall) Do ¶
func (c *ManagementAccountSummariesListCall) Do(opts ...googleapi.CallOption) (*AccountSummaries, error)

Do executes the "analytics.management.accountSummaries.list" call. Any non-2xx status code is an error. Response headers are in either *AccountSummaries.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementAccountSummariesListCall) Fields ¶
func (c *ManagementAccountSummariesListCall) Fields(s ...googleapi.Field) *ManagementAccountSummariesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementAccountSummariesListCall) Header ¶
func (c *ManagementAccountSummariesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementAccountSummariesListCall) IfNoneMatch ¶
func (c *ManagementAccountSummariesListCall) IfNoneMatch(entityTag string) *ManagementAccountSummariesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ManagementAccountSummariesListCall) MaxResults ¶
func (c *ManagementAccountSummariesListCall) MaxResults(maxResults int64) *ManagementAccountSummariesListCall

MaxResults sets the optional parameter "max-results": The maximum number of account summaries to include in this response, where the largest acceptable value is 1000.

func (*ManagementAccountSummariesListCall) StartIndex ¶
func (c *ManagementAccountSummariesListCall) StartIndex(startIndex int64) *ManagementAccountSummariesListCall

StartIndex sets the optional parameter "start-index": An index of the first entity to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

type ManagementAccountSummariesService ¶
type ManagementAccountSummariesService struct {
	// contains filtered or unexported fields
}
func NewManagementAccountSummariesService ¶
func NewManagementAccountSummariesService(s *Service) *ManagementAccountSummariesService
func (*ManagementAccountSummariesService) List ¶
func (r *ManagementAccountSummariesService) List() *ManagementAccountSummariesListCall

List: Lists account summaries (lightweight tree comprised of accounts/properties/profiles) to which the user has access.

type ManagementAccountUserLinksDeleteCall ¶
type ManagementAccountUserLinksDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ManagementAccountUserLinksDeleteCall) Context ¶
func (c *ManagementAccountUserLinksDeleteCall) Context(ctx context.Context) *ManagementAccountUserLinksDeleteCall

Context sets the context to be used in this call's Do method.

func (*ManagementAccountUserLinksDeleteCall) Do ¶
func (c *ManagementAccountUserLinksDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "analytics.management.accountUserLinks.delete" call.

func (*ManagementAccountUserLinksDeleteCall) Fields ¶
func (c *ManagementAccountUserLinksDeleteCall) Fields(s ...googleapi.Field) *ManagementAccountUserLinksDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementAccountUserLinksDeleteCall) Header ¶
func (c *ManagementAccountUserLinksDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementAccountUserLinksInsertCall ¶
type ManagementAccountUserLinksInsertCall struct {
	// contains filtered or unexported fields
}
func (*ManagementAccountUserLinksInsertCall) Context ¶
func (c *ManagementAccountUserLinksInsertCall) Context(ctx context.Context) *ManagementAccountUserLinksInsertCall

Context sets the context to be used in this call's Do method.

func (*ManagementAccountUserLinksInsertCall) Do ¶
func (c *ManagementAccountUserLinksInsertCall) Do(opts ...googleapi.CallOption) (*EntityUserLink, error)

Do executes the "analytics.management.accountUserLinks.insert" call. Any non-2xx status code is an error. Response headers are in either *EntityUserLink.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementAccountUserLinksInsertCall) Fields ¶
func (c *ManagementAccountUserLinksInsertCall) Fields(s ...googleapi.Field) *ManagementAccountUserLinksInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementAccountUserLinksInsertCall) Header ¶
func (c *ManagementAccountUserLinksInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementAccountUserLinksListCall ¶
type ManagementAccountUserLinksListCall struct {
	// contains filtered or unexported fields
}
func (*ManagementAccountUserLinksListCall) Context ¶
func (c *ManagementAccountUserLinksListCall) Context(ctx context.Context) *ManagementAccountUserLinksListCall

Context sets the context to be used in this call's Do method.

func (*ManagementAccountUserLinksListCall) Do ¶
func (c *ManagementAccountUserLinksListCall) Do(opts ...googleapi.CallOption) (*EntityUserLinks, error)

Do executes the "analytics.management.accountUserLinks.list" call. Any non-2xx status code is an error. Response headers are in either *EntityUserLinks.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementAccountUserLinksListCall) Fields ¶
func (c *ManagementAccountUserLinksListCall) Fields(s ...googleapi.Field) *ManagementAccountUserLinksListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementAccountUserLinksListCall) Header ¶
func (c *ManagementAccountUserLinksListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementAccountUserLinksListCall) IfNoneMatch ¶
func (c *ManagementAccountUserLinksListCall) IfNoneMatch(entityTag string) *ManagementAccountUserLinksListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ManagementAccountUserLinksListCall) MaxResults ¶
func (c *ManagementAccountUserLinksListCall) MaxResults(maxResults int64) *ManagementAccountUserLinksListCall

MaxResults sets the optional parameter "max-results": The maximum number of account-user links to include in this response.

func (*ManagementAccountUserLinksListCall) StartIndex ¶
func (c *ManagementAccountUserLinksListCall) StartIndex(startIndex int64) *ManagementAccountUserLinksListCall

StartIndex sets the optional parameter "start-index": An index of the first account-user link to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

type ManagementAccountUserLinksService ¶
type ManagementAccountUserLinksService struct {
	// contains filtered or unexported fields
}
func NewManagementAccountUserLinksService ¶
func NewManagementAccountUserLinksService(s *Service) *ManagementAccountUserLinksService
func (*ManagementAccountUserLinksService) Delete ¶
func (r *ManagementAccountUserLinksService) Delete(accountId string, linkId string) *ManagementAccountUserLinksDeleteCall

Delete: Removes a user from the given account.

- accountId: Account ID to delete the user link for. - linkId: Link ID to delete the user link for.

func (*ManagementAccountUserLinksService) Insert ¶
func (r *ManagementAccountUserLinksService) Insert(accountId string, entityuserlink *EntityUserLink) *ManagementAccountUserLinksInsertCall

Insert: Adds a new user to the given account.

- accountId: Account ID to create the user link for.

func (*ManagementAccountUserLinksService) List ¶
func (r *ManagementAccountUserLinksService) List(accountId string) *ManagementAccountUserLinksListCall

List: Lists account-user links for a given account.

- accountId: Account ID to retrieve the user links for.

func (*ManagementAccountUserLinksService) Update ¶
func (r *ManagementAccountUserLinksService) Update(accountId string, linkId string, entityuserlink *EntityUserLink) *ManagementAccountUserLinksUpdateCall

Update: Updates permissions for an existing user on the given account.

- accountId: Account ID to update the account-user link for. - linkId: Link ID to update the account-user link for.

type ManagementAccountUserLinksUpdateCall ¶
type ManagementAccountUserLinksUpdateCall struct {
	// contains filtered or unexported fields
}
func (*ManagementAccountUserLinksUpdateCall) Context ¶
func (c *ManagementAccountUserLinksUpdateCall) Context(ctx context.Context) *ManagementAccountUserLinksUpdateCall

Context sets the context to be used in this call's Do method.

func (*ManagementAccountUserLinksUpdateCall) Do ¶
func (c *ManagementAccountUserLinksUpdateCall) Do(opts ...googleapi.CallOption) (*EntityUserLink, error)

Do executes the "analytics.management.accountUserLinks.update" call. Any non-2xx status code is an error. Response headers are in either *EntityUserLink.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementAccountUserLinksUpdateCall) Fields ¶
func (c *ManagementAccountUserLinksUpdateCall) Fields(s ...googleapi.Field) *ManagementAccountUserLinksUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementAccountUserLinksUpdateCall) Header ¶
func (c *ManagementAccountUserLinksUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementAccountsListCall ¶
type ManagementAccountsListCall struct {
	// contains filtered or unexported fields
}
func (*ManagementAccountsListCall) Context ¶
func (c *ManagementAccountsListCall) Context(ctx context.Context) *ManagementAccountsListCall

Context sets the context to be used in this call's Do method.

func (*ManagementAccountsListCall) Do ¶
func (c *ManagementAccountsListCall) Do(opts ...googleapi.CallOption) (*Accounts, error)

Do executes the "analytics.management.accounts.list" call. Any non-2xx status code is an error. Response headers are in either *Accounts.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementAccountsListCall) Fields ¶
func (c *ManagementAccountsListCall) Fields(s ...googleapi.Field) *ManagementAccountsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementAccountsListCall) Header ¶
func (c *ManagementAccountsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementAccountsListCall) IfNoneMatch ¶
func (c *ManagementAccountsListCall) IfNoneMatch(entityTag string) *ManagementAccountsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ManagementAccountsListCall) MaxResults ¶
func (c *ManagementAccountsListCall) MaxResults(maxResults int64) *ManagementAccountsListCall

MaxResults sets the optional parameter "max-results": The maximum number of accounts to include in this response.

func (*ManagementAccountsListCall) StartIndex ¶
func (c *ManagementAccountsListCall) StartIndex(startIndex int64) *ManagementAccountsListCall

StartIndex sets the optional parameter "start-index": An index of the first account to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

type ManagementAccountsService ¶
type ManagementAccountsService struct {
	// contains filtered or unexported fields
}
func NewManagementAccountsService ¶
func NewManagementAccountsService(s *Service) *ManagementAccountsService
func (*ManagementAccountsService) List ¶
func (r *ManagementAccountsService) List() *ManagementAccountsListCall

List: Lists all accounts to which the user has access.

type ManagementClientIdHashClientIdCall ¶
type ManagementClientIdHashClientIdCall struct {
	// contains filtered or unexported fields
}
func (*ManagementClientIdHashClientIdCall) Context ¶
func (c *ManagementClientIdHashClientIdCall) Context(ctx context.Context) *ManagementClientIdHashClientIdCall

Context sets the context to be used in this call's Do method.

func (*ManagementClientIdHashClientIdCall) Do ¶
func (c *ManagementClientIdHashClientIdCall) Do(opts ...googleapi.CallOption) (*HashClientIdResponse, error)

Do executes the "analytics.management.clientId.hashClientId" call. Any non-2xx status code is an error. Response headers are in either *HashClientIdResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementClientIdHashClientIdCall) Fields ¶
func (c *ManagementClientIdHashClientIdCall) Fields(s ...googleapi.Field) *ManagementClientIdHashClientIdCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementClientIdHashClientIdCall) Header ¶
func (c *ManagementClientIdHashClientIdCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementClientIdService ¶
type ManagementClientIdService struct {
	// contains filtered or unexported fields
}
func NewManagementClientIdService ¶
func NewManagementClientIdService(s *Service) *ManagementClientIdService
func (*ManagementClientIdService) HashClientId ¶
func (r *ManagementClientIdService) HashClientId(hashclientidrequest *HashClientIdRequest) *ManagementClientIdHashClientIdCall

HashClientId: Hashes the given Client ID.

type ManagementCustomDataSourcesListCall ¶
type ManagementCustomDataSourcesListCall struct {
	// contains filtered or unexported fields
}
func (*ManagementCustomDataSourcesListCall) Context ¶
func (c *ManagementCustomDataSourcesListCall) Context(ctx context.Context) *ManagementCustomDataSourcesListCall

Context sets the context to be used in this call's Do method.

func (*ManagementCustomDataSourcesListCall) Do ¶
func (c *ManagementCustomDataSourcesListCall) Do(opts ...googleapi.CallOption) (*CustomDataSources, error)

Do executes the "analytics.management.customDataSources.list" call. Any non-2xx status code is an error. Response headers are in either *CustomDataSources.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementCustomDataSourcesListCall) Fields ¶
func (c *ManagementCustomDataSourcesListCall) Fields(s ...googleapi.Field) *ManagementCustomDataSourcesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementCustomDataSourcesListCall) Header ¶
func (c *ManagementCustomDataSourcesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementCustomDataSourcesListCall) IfNoneMatch ¶
func (c *ManagementCustomDataSourcesListCall) IfNoneMatch(entityTag string) *ManagementCustomDataSourcesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ManagementCustomDataSourcesListCall) MaxResults ¶
func (c *ManagementCustomDataSourcesListCall) MaxResults(maxResults int64) *ManagementCustomDataSourcesListCall

MaxResults sets the optional parameter "max-results": The maximum number of custom data sources to include in this response.

func (*ManagementCustomDataSourcesListCall) StartIndex ¶
func (c *ManagementCustomDataSourcesListCall) StartIndex(startIndex int64) *ManagementCustomDataSourcesListCall

StartIndex sets the optional parameter "start-index": A 1-based index of the first custom data source to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

type ManagementCustomDataSourcesService ¶
type ManagementCustomDataSourcesService struct {
	// contains filtered or unexported fields
}
func NewManagementCustomDataSourcesService ¶
func NewManagementCustomDataSourcesService(s *Service) *ManagementCustomDataSourcesService
func (*ManagementCustomDataSourcesService) List ¶
func (r *ManagementCustomDataSourcesService) List(accountId string, webPropertyId string) *ManagementCustomDataSourcesListCall

List: List custom data sources to which the user has access.

- accountId: Account Id for the custom data sources to retrieve. - webPropertyId: Web property Id for the custom data sources to retrieve.

type ManagementCustomDimensionsGetCall ¶
type ManagementCustomDimensionsGetCall struct {
	// contains filtered or unexported fields
}
func (*ManagementCustomDimensionsGetCall) Context ¶
func (c *ManagementCustomDimensionsGetCall) Context(ctx context.Context) *ManagementCustomDimensionsGetCall

Context sets the context to be used in this call's Do method.

func (*ManagementCustomDimensionsGetCall) Do ¶
func (c *ManagementCustomDimensionsGetCall) Do(opts ...googleapi.CallOption) (*CustomDimension, error)

Do executes the "analytics.management.customDimensions.get" call. Any non-2xx status code is an error. Response headers are in either *CustomDimension.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementCustomDimensionsGetCall) Fields ¶
func (c *ManagementCustomDimensionsGetCall) Fields(s ...googleapi.Field) *ManagementCustomDimensionsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementCustomDimensionsGetCall) Header ¶
func (c *ManagementCustomDimensionsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementCustomDimensionsGetCall) IfNoneMatch ¶
func (c *ManagementCustomDimensionsGetCall) IfNoneMatch(entityTag string) *ManagementCustomDimensionsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ManagementCustomDimensionsInsertCall ¶
type ManagementCustomDimensionsInsertCall struct {
	// contains filtered or unexported fields
}
func (*ManagementCustomDimensionsInsertCall) Context ¶
func (c *ManagementCustomDimensionsInsertCall) Context(ctx context.Context) *ManagementCustomDimensionsInsertCall

Context sets the context to be used in this call's Do method.

func (*ManagementCustomDimensionsInsertCall) Do ¶
func (c *ManagementCustomDimensionsInsertCall) Do(opts ...googleapi.CallOption) (*CustomDimension, error)

Do executes the "analytics.management.customDimensions.insert" call. Any non-2xx status code is an error. Response headers are in either *CustomDimension.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementCustomDimensionsInsertCall) Fields ¶
func (c *ManagementCustomDimensionsInsertCall) Fields(s ...googleapi.Field) *ManagementCustomDimensionsInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementCustomDimensionsInsertCall) Header ¶
func (c *ManagementCustomDimensionsInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementCustomDimensionsListCall ¶
type ManagementCustomDimensionsListCall struct {
	// contains filtered or unexported fields
}
func (*ManagementCustomDimensionsListCall) Context ¶
func (c *ManagementCustomDimensionsListCall) Context(ctx context.Context) *ManagementCustomDimensionsListCall

Context sets the context to be used in this call's Do method.

func (*ManagementCustomDimensionsListCall) Do ¶
func (c *ManagementCustomDimensionsListCall) Do(opts ...googleapi.CallOption) (*CustomDimensions, error)

Do executes the "analytics.management.customDimensions.list" call. Any non-2xx status code is an error. Response headers are in either *CustomDimensions.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementCustomDimensionsListCall) Fields ¶
func (c *ManagementCustomDimensionsListCall) Fields(s ...googleapi.Field) *ManagementCustomDimensionsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementCustomDimensionsListCall) Header ¶
func (c *ManagementCustomDimensionsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementCustomDimensionsListCall) IfNoneMatch ¶
func (c *ManagementCustomDimensionsListCall) IfNoneMatch(entityTag string) *ManagementCustomDimensionsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ManagementCustomDimensionsListCall) MaxResults ¶
func (c *ManagementCustomDimensionsListCall) MaxResults(maxResults int64) *ManagementCustomDimensionsListCall

MaxResults sets the optional parameter "max-results": The maximum number of custom dimensions to include in this response.

func (*ManagementCustomDimensionsListCall) StartIndex ¶
func (c *ManagementCustomDimensionsListCall) StartIndex(startIndex int64) *ManagementCustomDimensionsListCall

StartIndex sets the optional parameter "start-index": An index of the first entity to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

type ManagementCustomDimensionsPatchCall ¶
type ManagementCustomDimensionsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ManagementCustomDimensionsPatchCall) Context ¶
func (c *ManagementCustomDimensionsPatchCall) Context(ctx context.Context) *ManagementCustomDimensionsPatchCall

Context sets the context to be used in this call's Do method.

func (*ManagementCustomDimensionsPatchCall) Do ¶
func (c *ManagementCustomDimensionsPatchCall) Do(opts ...googleapi.CallOption) (*CustomDimension, error)

Do executes the "analytics.management.customDimensions.patch" call. Any non-2xx status code is an error. Response headers are in either *CustomDimension.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementCustomDimensionsPatchCall) Fields ¶
func (c *ManagementCustomDimensionsPatchCall) Fields(s ...googleapi.Field) *ManagementCustomDimensionsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementCustomDimensionsPatchCall) Header ¶
func (c *ManagementCustomDimensionsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementCustomDimensionsPatchCall) IgnoreCustomDataSourceLinks ¶
func (c *ManagementCustomDimensionsPatchCall) IgnoreCustomDataSourceLinks(ignoreCustomDataSourceLinks bool) *ManagementCustomDimensionsPatchCall

IgnoreCustomDataSourceLinks sets the optional parameter "ignoreCustomDataSourceLinks": Force the update and ignore any warnings related to the custom dimension being linked to a custom data source / data set.

type ManagementCustomDimensionsService ¶
type ManagementCustomDimensionsService struct {
	// contains filtered or unexported fields
}
func NewManagementCustomDimensionsService ¶
func NewManagementCustomDimensionsService(s *Service) *ManagementCustomDimensionsService
func (*ManagementCustomDimensionsService) Get ¶
func (r *ManagementCustomDimensionsService) Get(accountId string, webPropertyId string, customDimensionId string) *ManagementCustomDimensionsGetCall

Get: Get a custom dimension to which the user has access.

- accountId: Account ID for the custom dimension to retrieve. - customDimensionId: The ID of the custom dimension to retrieve. - webPropertyId: Web property ID for the custom dimension to retrieve.

func (*ManagementCustomDimensionsService) Insert ¶
func (r *ManagementCustomDimensionsService) Insert(accountId string, webPropertyId string, customdimension *CustomDimension) *ManagementCustomDimensionsInsertCall

Insert: Create a new custom dimension.

- accountId: Account ID for the custom dimension to create. - webPropertyId: Web property ID for the custom dimension to create.

func (*ManagementCustomDimensionsService) List ¶
func (r *ManagementCustomDimensionsService) List(accountId string, webPropertyId string) *ManagementCustomDimensionsListCall

List: Lists custom dimensions to which the user has access.

- accountId: Account ID for the custom dimensions to retrieve. - webPropertyId: Web property ID for the custom dimensions to retrieve.

func (*ManagementCustomDimensionsService) Patch ¶
func (r *ManagementCustomDimensionsService) Patch(accountId string, webPropertyId string, customDimensionId string, customdimension *CustomDimension) *ManagementCustomDimensionsPatchCall

Patch: Updates an existing custom dimension. This method supports patch semantics.

- accountId: Account ID for the custom dimension to update. - customDimensionId: Custom dimension ID for the custom dimension to update. - webPropertyId: Web property ID for the custom dimension to update.

func (*ManagementCustomDimensionsService) Update ¶
func (r *ManagementCustomDimensionsService) Update(accountId string, webPropertyId string, customDimensionId string, customdimension *CustomDimension) *ManagementCustomDimensionsUpdateCall

Update: Updates an existing custom dimension.

- accountId: Account ID for the custom dimension to update. - customDimensionId: Custom dimension ID for the custom dimension to update. - webPropertyId: Web property ID for the custom dimension to update.

type ManagementCustomDimensionsUpdateCall ¶
type ManagementCustomDimensionsUpdateCall struct {
	// contains filtered or unexported fields
}
func (*ManagementCustomDimensionsUpdateCall) Context ¶
func (c *ManagementCustomDimensionsUpdateCall) Context(ctx context.Context) *ManagementCustomDimensionsUpdateCall

Context sets the context to be used in this call's Do method.

func (*ManagementCustomDimensionsUpdateCall) Do ¶
func (c *ManagementCustomDimensionsUpdateCall) Do(opts ...googleapi.CallOption) (*CustomDimension, error)

Do executes the "analytics.management.customDimensions.update" call. Any non-2xx status code is an error. Response headers are in either *CustomDimension.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementCustomDimensionsUpdateCall) Fields ¶
func (c *ManagementCustomDimensionsUpdateCall) Fields(s ...googleapi.Field) *ManagementCustomDimensionsUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementCustomDimensionsUpdateCall) Header ¶
func (c *ManagementCustomDimensionsUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementCustomDimensionsUpdateCall) IgnoreCustomDataSourceLinks ¶
func (c *ManagementCustomDimensionsUpdateCall) IgnoreCustomDataSourceLinks(ignoreCustomDataSourceLinks bool) *ManagementCustomDimensionsUpdateCall

IgnoreCustomDataSourceLinks sets the optional parameter "ignoreCustomDataSourceLinks": Force the update and ignore any warnings related to the custom dimension being linked to a custom data source / data set.

type ManagementCustomMetricsGetCall ¶
type ManagementCustomMetricsGetCall struct {
	// contains filtered or unexported fields
}
func (*ManagementCustomMetricsGetCall) Context ¶
func (c *ManagementCustomMetricsGetCall) Context(ctx context.Context) *ManagementCustomMetricsGetCall

Context sets the context to be used in this call's Do method.

func (*ManagementCustomMetricsGetCall) Do ¶
func (c *ManagementCustomMetricsGetCall) Do(opts ...googleapi.CallOption) (*CustomMetric, error)

Do executes the "analytics.management.customMetrics.get" call. Any non-2xx status code is an error. Response headers are in either *CustomMetric.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementCustomMetricsGetCall) Fields ¶
func (c *ManagementCustomMetricsGetCall) Fields(s ...googleapi.Field) *ManagementCustomMetricsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementCustomMetricsGetCall) Header ¶
func (c *ManagementCustomMetricsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementCustomMetricsGetCall) IfNoneMatch ¶
func (c *ManagementCustomMetricsGetCall) IfNoneMatch(entityTag string) *ManagementCustomMetricsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ManagementCustomMetricsInsertCall ¶
type ManagementCustomMetricsInsertCall struct {
	// contains filtered or unexported fields
}
func (*ManagementCustomMetricsInsertCall) Context ¶
func (c *ManagementCustomMetricsInsertCall) Context(ctx context.Context) *ManagementCustomMetricsInsertCall

Context sets the context to be used in this call's Do method.

func (*ManagementCustomMetricsInsertCall) Do ¶
func (c *ManagementCustomMetricsInsertCall) Do(opts ...googleapi.CallOption) (*CustomMetric, error)

Do executes the "analytics.management.customMetrics.insert" call. Any non-2xx status code is an error. Response headers are in either *CustomMetric.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementCustomMetricsInsertCall) Fields ¶
func (c *ManagementCustomMetricsInsertCall) Fields(s ...googleapi.Field) *ManagementCustomMetricsInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementCustomMetricsInsertCall) Header ¶
func (c *ManagementCustomMetricsInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementCustomMetricsListCall ¶
type ManagementCustomMetricsListCall struct {
	// contains filtered or unexported fields
}
func (*ManagementCustomMetricsListCall) Context ¶
func (c *ManagementCustomMetricsListCall) Context(ctx context.Context) *ManagementCustomMetricsListCall

Context sets the context to be used in this call's Do method.

func (*ManagementCustomMetricsListCall) Do ¶
func (c *ManagementCustomMetricsListCall) Do(opts ...googleapi.CallOption) (*CustomMetrics, error)

Do executes the "analytics.management.customMetrics.list" call. Any non-2xx status code is an error. Response headers are in either *CustomMetrics.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementCustomMetricsListCall) Fields ¶
func (c *ManagementCustomMetricsListCall) Fields(s ...googleapi.Field) *ManagementCustomMetricsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementCustomMetricsListCall) Header ¶
func (c *ManagementCustomMetricsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementCustomMetricsListCall) IfNoneMatch ¶
func (c *ManagementCustomMetricsListCall) IfNoneMatch(entityTag string) *ManagementCustomMetricsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ManagementCustomMetricsListCall) MaxResults ¶
func (c *ManagementCustomMetricsListCall) MaxResults(maxResults int64) *ManagementCustomMetricsListCall

MaxResults sets the optional parameter "max-results": The maximum number of custom metrics to include in this response.

func (*ManagementCustomMetricsListCall) StartIndex ¶
func (c *ManagementCustomMetricsListCall) StartIndex(startIndex int64) *ManagementCustomMetricsListCall

StartIndex sets the optional parameter "start-index": An index of the first entity to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

type ManagementCustomMetricsPatchCall ¶
type ManagementCustomMetricsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ManagementCustomMetricsPatchCall) Context ¶
func (c *ManagementCustomMetricsPatchCall) Context(ctx context.Context) *ManagementCustomMetricsPatchCall

Context sets the context to be used in this call's Do method.

func (*ManagementCustomMetricsPatchCall) Do ¶
func (c *ManagementCustomMetricsPatchCall) Do(opts ...googleapi.CallOption) (*CustomMetric, error)

Do executes the "analytics.management.customMetrics.patch" call. Any non-2xx status code is an error. Response headers are in either *CustomMetric.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementCustomMetricsPatchCall) Fields ¶
func (c *ManagementCustomMetricsPatchCall) Fields(s ...googleapi.Field) *ManagementCustomMetricsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementCustomMetricsPatchCall) Header ¶
func (c *ManagementCustomMetricsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementCustomMetricsPatchCall) IgnoreCustomDataSourceLinks ¶
func (c *ManagementCustomMetricsPatchCall) IgnoreCustomDataSourceLinks(ignoreCustomDataSourceLinks bool) *ManagementCustomMetricsPatchCall

IgnoreCustomDataSourceLinks sets the optional parameter "ignoreCustomDataSourceLinks": Force the update and ignore any warnings related to the custom metric being linked to a custom data source / data set.

type ManagementCustomMetricsService ¶
type ManagementCustomMetricsService struct {
	// contains filtered or unexported fields
}
func NewManagementCustomMetricsService ¶
func NewManagementCustomMetricsService(s *Service) *ManagementCustomMetricsService
func (*ManagementCustomMetricsService) Get ¶
func (r *ManagementCustomMetricsService) Get(accountId string, webPropertyId string, customMetricId string) *ManagementCustomMetricsGetCall

Get: Get a custom metric to which the user has access.

- accountId: Account ID for the custom metric to retrieve. - customMetricId: The ID of the custom metric to retrieve. - webPropertyId: Web property ID for the custom metric to retrieve.

func (*ManagementCustomMetricsService) Insert ¶
func (r *ManagementCustomMetricsService) Insert(accountId string, webPropertyId string, custommetric *CustomMetric) *ManagementCustomMetricsInsertCall

Insert: Create a new custom metric.

- accountId: Account ID for the custom metric to create. - webPropertyId: Web property ID for the custom dimension to create.

func (*ManagementCustomMetricsService) List ¶
func (r *ManagementCustomMetricsService) List(accountId string, webPropertyId string) *ManagementCustomMetricsListCall

List: Lists custom metrics to which the user has access.

- accountId: Account ID for the custom metrics to retrieve. - webPropertyId: Web property ID for the custom metrics to retrieve.

func (*ManagementCustomMetricsService) Patch ¶
func (r *ManagementCustomMetricsService) Patch(accountId string, webPropertyId string, customMetricId string, custommetric *CustomMetric) *ManagementCustomMetricsPatchCall

Patch: Updates an existing custom metric. This method supports patch semantics.

- accountId: Account ID for the custom metric to update. - customMetricId: Custom metric ID for the custom metric to update. - webPropertyId: Web property ID for the custom metric to update.

func (*ManagementCustomMetricsService) Update ¶
func (r *ManagementCustomMetricsService) Update(accountId string, webPropertyId string, customMetricId string, custommetric *CustomMetric) *ManagementCustomMetricsUpdateCall

Update: Updates an existing custom metric.

- accountId: Account ID for the custom metric to update. - customMetricId: Custom metric ID for the custom metric to update. - webPropertyId: Web property ID for the custom metric to update.

type ManagementCustomMetricsUpdateCall ¶
type ManagementCustomMetricsUpdateCall struct {
	// contains filtered or unexported fields
}
func (*ManagementCustomMetricsUpdateCall) Context ¶
func (c *ManagementCustomMetricsUpdateCall) Context(ctx context.Context) *ManagementCustomMetricsUpdateCall

Context sets the context to be used in this call's Do method.

func (*ManagementCustomMetricsUpdateCall) Do ¶
func (c *ManagementCustomMetricsUpdateCall) Do(opts ...googleapi.CallOption) (*CustomMetric, error)

Do executes the "analytics.management.customMetrics.update" call. Any non-2xx status code is an error. Response headers are in either *CustomMetric.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementCustomMetricsUpdateCall) Fields ¶
func (c *ManagementCustomMetricsUpdateCall) Fields(s ...googleapi.Field) *ManagementCustomMetricsUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementCustomMetricsUpdateCall) Header ¶
func (c *ManagementCustomMetricsUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementCustomMetricsUpdateCall) IgnoreCustomDataSourceLinks ¶
func (c *ManagementCustomMetricsUpdateCall) IgnoreCustomDataSourceLinks(ignoreCustomDataSourceLinks bool) *ManagementCustomMetricsUpdateCall

IgnoreCustomDataSourceLinks sets the optional parameter "ignoreCustomDataSourceLinks": Force the update and ignore any warnings related to the custom metric being linked to a custom data source / data set.

type ManagementExperimentsDeleteCall ¶
type ManagementExperimentsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ManagementExperimentsDeleteCall) Context ¶
func (c *ManagementExperimentsDeleteCall) Context(ctx context.Context) *ManagementExperimentsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ManagementExperimentsDeleteCall) Do ¶
func (c *ManagementExperimentsDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "analytics.management.experiments.delete" call.

func (*ManagementExperimentsDeleteCall) Fields ¶
func (c *ManagementExperimentsDeleteCall) Fields(s ...googleapi.Field) *ManagementExperimentsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementExperimentsDeleteCall) Header ¶
func (c *ManagementExperimentsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementExperimentsGetCall ¶
type ManagementExperimentsGetCall struct {
	// contains filtered or unexported fields
}
func (*ManagementExperimentsGetCall) Context ¶
func (c *ManagementExperimentsGetCall) Context(ctx context.Context) *ManagementExperimentsGetCall

Context sets the context to be used in this call's Do method.

func (*ManagementExperimentsGetCall) Do ¶
func (c *ManagementExperimentsGetCall) Do(opts ...googleapi.CallOption) (*Experiment, error)

Do executes the "analytics.management.experiments.get" call. Any non-2xx status code is an error. Response headers are in either *Experiment.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementExperimentsGetCall) Fields ¶
func (c *ManagementExperimentsGetCall) Fields(s ...googleapi.Field) *ManagementExperimentsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementExperimentsGetCall) Header ¶
func (c *ManagementExperimentsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementExperimentsGetCall) IfNoneMatch ¶
func (c *ManagementExperimentsGetCall) IfNoneMatch(entityTag string) *ManagementExperimentsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ManagementExperimentsInsertCall ¶
type ManagementExperimentsInsertCall struct {
	// contains filtered or unexported fields
}
func (*ManagementExperimentsInsertCall) Context ¶
func (c *ManagementExperimentsInsertCall) Context(ctx context.Context) *ManagementExperimentsInsertCall

Context sets the context to be used in this call's Do method.

func (*ManagementExperimentsInsertCall) Do ¶
func (c *ManagementExperimentsInsertCall) Do(opts ...googleapi.CallOption) (*Experiment, error)

Do executes the "analytics.management.experiments.insert" call. Any non-2xx status code is an error. Response headers are in either *Experiment.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementExperimentsInsertCall) Fields ¶
func (c *ManagementExperimentsInsertCall) Fields(s ...googleapi.Field) *ManagementExperimentsInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementExperimentsInsertCall) Header ¶
func (c *ManagementExperimentsInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementExperimentsListCall ¶
type ManagementExperimentsListCall struct {
	// contains filtered or unexported fields
}
func (*ManagementExperimentsListCall) Context ¶
func (c *ManagementExperimentsListCall) Context(ctx context.Context) *ManagementExperimentsListCall

Context sets the context to be used in this call's Do method.

func (*ManagementExperimentsListCall) Do ¶
func (c *ManagementExperimentsListCall) Do(opts ...googleapi.CallOption) (*Experiments, error)

Do executes the "analytics.management.experiments.list" call. Any non-2xx status code is an error. Response headers are in either *Experiments.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementExperimentsListCall) Fields ¶
func (c *ManagementExperimentsListCall) Fields(s ...googleapi.Field) *ManagementExperimentsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementExperimentsListCall) Header ¶
func (c *ManagementExperimentsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementExperimentsListCall) IfNoneMatch ¶
func (c *ManagementExperimentsListCall) IfNoneMatch(entityTag string) *ManagementExperimentsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ManagementExperimentsListCall) MaxResults ¶
func (c *ManagementExperimentsListCall) MaxResults(maxResults int64) *ManagementExperimentsListCall

MaxResults sets the optional parameter "max-results": The maximum number of experiments to include in this response.

func (*ManagementExperimentsListCall) StartIndex ¶
func (c *ManagementExperimentsListCall) StartIndex(startIndex int64) *ManagementExperimentsListCall

StartIndex sets the optional parameter "start-index": An index of the first experiment to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

type ManagementExperimentsPatchCall ¶
type ManagementExperimentsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ManagementExperimentsPatchCall) Context ¶
func (c *ManagementExperimentsPatchCall) Context(ctx context.Context) *ManagementExperimentsPatchCall

Context sets the context to be used in this call's Do method.

func (*ManagementExperimentsPatchCall) Do ¶
func (c *ManagementExperimentsPatchCall) Do(opts ...googleapi.CallOption) (*Experiment, error)

Do executes the "analytics.management.experiments.patch" call. Any non-2xx status code is an error. Response headers are in either *Experiment.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementExperimentsPatchCall) Fields ¶
func (c *ManagementExperimentsPatchCall) Fields(s ...googleapi.Field) *ManagementExperimentsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementExperimentsPatchCall) Header ¶
func (c *ManagementExperimentsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementExperimentsService ¶
type ManagementExperimentsService struct {
	// contains filtered or unexported fields
}
func NewManagementExperimentsService ¶
func NewManagementExperimentsService(s *Service) *ManagementExperimentsService
func (*ManagementExperimentsService) Delete ¶
func (r *ManagementExperimentsService) Delete(accountId string, webPropertyId string, profileId string, experimentId string) *ManagementExperimentsDeleteCall

Delete: Delete an experiment.

- accountId: Account ID to which the experiment belongs. - experimentId: ID of the experiment to delete. - profileId: View (Profile) ID to which the experiment belongs. - webPropertyId: Web property ID to which the experiment belongs.

func (*ManagementExperimentsService) Get ¶
func (r *ManagementExperimentsService) Get(accountId string, webPropertyId string, profileId string, experimentId string) *ManagementExperimentsGetCall

Get: Returns an experiment to which the user has access.

- accountId: Account ID to retrieve the experiment for. - experimentId: Experiment ID to retrieve the experiment for. - profileId: View (Profile) ID to retrieve the experiment for. - webPropertyId: Web property ID to retrieve the experiment for.

func (*ManagementExperimentsService) Insert ¶
func (r *ManagementExperimentsService) Insert(accountId string, webPropertyId string, profileId string, experiment *Experiment) *ManagementExperimentsInsertCall

Insert: Create a new experiment.

- accountId: Account ID to create the experiment for. - profileId: View (Profile) ID to create the experiment for. - webPropertyId: Web property ID to create the experiment for.

func (*ManagementExperimentsService) List ¶
func (r *ManagementExperimentsService) List(accountId string, webPropertyId string, profileId string) *ManagementExperimentsListCall

List: Lists experiments to which the user has access.

- accountId: Account ID to retrieve experiments for. - profileId: View (Profile) ID to retrieve experiments for. - webPropertyId: Web property ID to retrieve experiments for.

func (*ManagementExperimentsService) Patch ¶
func (r *ManagementExperimentsService) Patch(accountId string, webPropertyId string, profileId string, experimentId string, experiment *Experiment) *ManagementExperimentsPatchCall

Patch: Update an existing experiment. This method supports patch semantics.

- accountId: Account ID of the experiment to update. - experimentId: Experiment ID of the experiment to update. - profileId: View (Profile) ID of the experiment to update. - webPropertyId: Web property ID of the experiment to update.

func (*ManagementExperimentsService) Update ¶
func (r *ManagementExperimentsService) Update(accountId string, webPropertyId string, profileId string, experimentId string, experiment *Experiment) *ManagementExperimentsUpdateCall

Update: Update an existing experiment.

- accountId: Account ID of the experiment to update. - experimentId: Experiment ID of the experiment to update. - profileId: View (Profile) ID of the experiment to update. - webPropertyId: Web property ID of the experiment to update.

type ManagementExperimentsUpdateCall ¶
type ManagementExperimentsUpdateCall struct {
	// contains filtered or unexported fields
}
func (*ManagementExperimentsUpdateCall) Context ¶
func (c *ManagementExperimentsUpdateCall) Context(ctx context.Context) *ManagementExperimentsUpdateCall

Context sets the context to be used in this call's Do method.

func (*ManagementExperimentsUpdateCall) Do ¶
func (c *ManagementExperimentsUpdateCall) Do(opts ...googleapi.CallOption) (*Experiment, error)

Do executes the "analytics.management.experiments.update" call. Any non-2xx status code is an error. Response headers are in either *Experiment.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementExperimentsUpdateCall) Fields ¶
func (c *ManagementExperimentsUpdateCall) Fields(s ...googleapi.Field) *ManagementExperimentsUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementExperimentsUpdateCall) Header ¶
func (c *ManagementExperimentsUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementFiltersDeleteCall ¶
type ManagementFiltersDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ManagementFiltersDeleteCall) Context ¶
func (c *ManagementFiltersDeleteCall) Context(ctx context.Context) *ManagementFiltersDeleteCall

Context sets the context to be used in this call's Do method.

func (*ManagementFiltersDeleteCall) Do ¶
func (c *ManagementFiltersDeleteCall) Do(opts ...googleapi.CallOption) (*Filter, error)

Do executes the "analytics.management.filters.delete" call. Any non-2xx status code is an error. Response headers are in either *Filter.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementFiltersDeleteCall) Fields ¶
func (c *ManagementFiltersDeleteCall) Fields(s ...googleapi.Field) *ManagementFiltersDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementFiltersDeleteCall) Header ¶
func (c *ManagementFiltersDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementFiltersGetCall ¶
type ManagementFiltersGetCall struct {
	// contains filtered or unexported fields
}
func (*ManagementFiltersGetCall) Context ¶
func (c *ManagementFiltersGetCall) Context(ctx context.Context) *ManagementFiltersGetCall

Context sets the context to be used in this call's Do method.

func (*ManagementFiltersGetCall) Do ¶
func (c *ManagementFiltersGetCall) Do(opts ...googleapi.CallOption) (*Filter, error)

Do executes the "analytics.management.filters.get" call. Any non-2xx status code is an error. Response headers are in either *Filter.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementFiltersGetCall) Fields ¶
func (c *ManagementFiltersGetCall) Fields(s ...googleapi.Field) *ManagementFiltersGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementFiltersGetCall) Header ¶
func (c *ManagementFiltersGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementFiltersGetCall) IfNoneMatch ¶
func (c *ManagementFiltersGetCall) IfNoneMatch(entityTag string) *ManagementFiltersGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ManagementFiltersInsertCall ¶
type ManagementFiltersInsertCall struct {
	// contains filtered or unexported fields
}
func (*ManagementFiltersInsertCall) Context ¶
func (c *ManagementFiltersInsertCall) Context(ctx context.Context) *ManagementFiltersInsertCall

Context sets the context to be used in this call's Do method.

func (*ManagementFiltersInsertCall) Do ¶
func (c *ManagementFiltersInsertCall) Do(opts ...googleapi.CallOption) (*Filter, error)

Do executes the "analytics.management.filters.insert" call. Any non-2xx status code is an error. Response headers are in either *Filter.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementFiltersInsertCall) Fields ¶
func (c *ManagementFiltersInsertCall) Fields(s ...googleapi.Field) *ManagementFiltersInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementFiltersInsertCall) Header ¶
func (c *ManagementFiltersInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementFiltersListCall ¶
type ManagementFiltersListCall struct {
	// contains filtered or unexported fields
}
func (*ManagementFiltersListCall) Context ¶
func (c *ManagementFiltersListCall) Context(ctx context.Context) *ManagementFiltersListCall

Context sets the context to be used in this call's Do method.

func (*ManagementFiltersListCall) Do ¶
func (c *ManagementFiltersListCall) Do(opts ...googleapi.CallOption) (*Filters, error)

Do executes the "analytics.management.filters.list" call. Any non-2xx status code is an error. Response headers are in either *Filters.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementFiltersListCall) Fields ¶
func (c *ManagementFiltersListCall) Fields(s ...googleapi.Field) *ManagementFiltersListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementFiltersListCall) Header ¶
func (c *ManagementFiltersListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementFiltersListCall) IfNoneMatch ¶
func (c *ManagementFiltersListCall) IfNoneMatch(entityTag string) *ManagementFiltersListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ManagementFiltersListCall) MaxResults ¶
func (c *ManagementFiltersListCall) MaxResults(maxResults int64) *ManagementFiltersListCall

MaxResults sets the optional parameter "max-results": The maximum number of filters to include in this response.

func (*ManagementFiltersListCall) StartIndex ¶
func (c *ManagementFiltersListCall) StartIndex(startIndex int64) *ManagementFiltersListCall

StartIndex sets the optional parameter "start-index": An index of the first entity to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

type ManagementFiltersPatchCall ¶
type ManagementFiltersPatchCall struct {
	// contains filtered or unexported fields
}
func (*ManagementFiltersPatchCall) Context ¶
func (c *ManagementFiltersPatchCall) Context(ctx context.Context) *ManagementFiltersPatchCall

Context sets the context to be used in this call's Do method.

func (*ManagementFiltersPatchCall) Do ¶
func (c *ManagementFiltersPatchCall) Do(opts ...googleapi.CallOption) (*Filter, error)

Do executes the "analytics.management.filters.patch" call. Any non-2xx status code is an error. Response headers are in either *Filter.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementFiltersPatchCall) Fields ¶
func (c *ManagementFiltersPatchCall) Fields(s ...googleapi.Field) *ManagementFiltersPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementFiltersPatchCall) Header ¶
func (c *ManagementFiltersPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementFiltersService ¶
type ManagementFiltersService struct {
	// contains filtered or unexported fields
}
func NewManagementFiltersService ¶
func NewManagementFiltersService(s *Service) *ManagementFiltersService
func (*ManagementFiltersService) Delete ¶
func (r *ManagementFiltersService) Delete(accountId string, filterId string) *ManagementFiltersDeleteCall

Delete: Delete a filter.

- accountId: Account ID to delete the filter for. - filterId: ID of the filter to be deleted.

func (*ManagementFiltersService) Get ¶
func (r *ManagementFiltersService) Get(accountId string, filterId string) *ManagementFiltersGetCall

Get: Returns filters to which the user has access.

- accountId: Account ID to retrieve filters for. - filterId: Filter ID to retrieve filters for.

func (*ManagementFiltersService) Insert ¶
func (r *ManagementFiltersService) Insert(accountId string, filter *Filter) *ManagementFiltersInsertCall

Insert: Create a new filter.

- accountId: Account ID to create filter for.

func (*ManagementFiltersService) List ¶
func (r *ManagementFiltersService) List(accountId string) *ManagementFiltersListCall

List: Lists all filters for an account

- accountId: Account ID to retrieve filters for.

func (*ManagementFiltersService) Patch ¶
func (r *ManagementFiltersService) Patch(accountId string, filterId string, filter *Filter) *ManagementFiltersPatchCall

Patch: Updates an existing filter. This method supports patch semantics.

- accountId: Account ID to which the filter belongs. - filterId: ID of the filter to be updated.

func (*ManagementFiltersService) Update ¶
func (r *ManagementFiltersService) Update(accountId string, filterId string, filter *Filter) *ManagementFiltersUpdateCall

Update: Updates an existing filter.

- accountId: Account ID to which the filter belongs. - filterId: ID of the filter to be updated.

type ManagementFiltersUpdateCall ¶
type ManagementFiltersUpdateCall struct {
	// contains filtered or unexported fields
}
func (*ManagementFiltersUpdateCall) Context ¶
func (c *ManagementFiltersUpdateCall) Context(ctx context.Context) *ManagementFiltersUpdateCall

Context sets the context to be used in this call's Do method.

func (*ManagementFiltersUpdateCall) Do ¶
func (c *ManagementFiltersUpdateCall) Do(opts ...googleapi.CallOption) (*Filter, error)

Do executes the "analytics.management.filters.update" call. Any non-2xx status code is an error. Response headers are in either *Filter.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementFiltersUpdateCall) Fields ¶
func (c *ManagementFiltersUpdateCall) Fields(s ...googleapi.Field) *ManagementFiltersUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementFiltersUpdateCall) Header ¶
func (c *ManagementFiltersUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementGoalsGetCall ¶
type ManagementGoalsGetCall struct {
	// contains filtered or unexported fields
}
func (*ManagementGoalsGetCall) Context ¶
func (c *ManagementGoalsGetCall) Context(ctx context.Context) *ManagementGoalsGetCall

Context sets the context to be used in this call's Do method.

func (*ManagementGoalsGetCall) Do ¶
func (c *ManagementGoalsGetCall) Do(opts ...googleapi.CallOption) (*Goal, error)

Do executes the "analytics.management.goals.get" call. Any non-2xx status code is an error. Response headers are in either *Goal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementGoalsGetCall) Fields ¶
func (c *ManagementGoalsGetCall) Fields(s ...googleapi.Field) *ManagementGoalsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementGoalsGetCall) Header ¶
func (c *ManagementGoalsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementGoalsGetCall) IfNoneMatch ¶
func (c *ManagementGoalsGetCall) IfNoneMatch(entityTag string) *ManagementGoalsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ManagementGoalsInsertCall ¶
type ManagementGoalsInsertCall struct {
	// contains filtered or unexported fields
}
func (*ManagementGoalsInsertCall) Context ¶
func (c *ManagementGoalsInsertCall) Context(ctx context.Context) *ManagementGoalsInsertCall

Context sets the context to be used in this call's Do method.

func (*ManagementGoalsInsertCall) Do ¶
func (c *ManagementGoalsInsertCall) Do(opts ...googleapi.CallOption) (*Goal, error)

Do executes the "analytics.management.goals.insert" call. Any non-2xx status code is an error. Response headers are in either *Goal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementGoalsInsertCall) Fields ¶
func (c *ManagementGoalsInsertCall) Fields(s ...googleapi.Field) *ManagementGoalsInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementGoalsInsertCall) Header ¶
func (c *ManagementGoalsInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementGoalsListCall ¶
type ManagementGoalsListCall struct {
	// contains filtered or unexported fields
}
func (*ManagementGoalsListCall) Context ¶
func (c *ManagementGoalsListCall) Context(ctx context.Context) *ManagementGoalsListCall

Context sets the context to be used in this call's Do method.

func (*ManagementGoalsListCall) Do ¶
func (c *ManagementGoalsListCall) Do(opts ...googleapi.CallOption) (*Goals, error)

Do executes the "analytics.management.goals.list" call. Any non-2xx status code is an error. Response headers are in either *Goals.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementGoalsListCall) Fields ¶
func (c *ManagementGoalsListCall) Fields(s ...googleapi.Field) *ManagementGoalsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementGoalsListCall) Header ¶
func (c *ManagementGoalsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementGoalsListCall) IfNoneMatch ¶
func (c *ManagementGoalsListCall) IfNoneMatch(entityTag string) *ManagementGoalsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ManagementGoalsListCall) MaxResults ¶
func (c *ManagementGoalsListCall) MaxResults(maxResults int64) *ManagementGoalsListCall

MaxResults sets the optional parameter "max-results": The maximum number of goals to include in this response.

func (*ManagementGoalsListCall) StartIndex ¶
func (c *ManagementGoalsListCall) StartIndex(startIndex int64) *ManagementGoalsListCall

StartIndex sets the optional parameter "start-index": An index of the first goal to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

type ManagementGoalsPatchCall ¶
type ManagementGoalsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ManagementGoalsPatchCall) Context ¶
func (c *ManagementGoalsPatchCall) Context(ctx context.Context) *ManagementGoalsPatchCall

Context sets the context to be used in this call's Do method.

func (*ManagementGoalsPatchCall) Do ¶
func (c *ManagementGoalsPatchCall) Do(opts ...googleapi.CallOption) (*Goal, error)

Do executes the "analytics.management.goals.patch" call. Any non-2xx status code is an error. Response headers are in either *Goal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementGoalsPatchCall) Fields ¶
func (c *ManagementGoalsPatchCall) Fields(s ...googleapi.Field) *ManagementGoalsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementGoalsPatchCall) Header ¶
func (c *ManagementGoalsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementGoalsService ¶
type ManagementGoalsService struct {
	// contains filtered or unexported fields
}
func NewManagementGoalsService ¶
func NewManagementGoalsService(s *Service) *ManagementGoalsService
func (*ManagementGoalsService) Get ¶
func (r *ManagementGoalsService) Get(accountId string, webPropertyId string, profileId string, goalId string) *ManagementGoalsGetCall

Get: Gets a goal to which the user has access.

- accountId: Account ID to retrieve the goal for. - goalId: Goal ID to retrieve the goal for. - profileId: View (Profile) ID to retrieve the goal for. - webPropertyId: Web property ID to retrieve the goal for.

func (*ManagementGoalsService) Insert ¶
func (r *ManagementGoalsService) Insert(accountId string, webPropertyId string, profileId string, goal *Goal) *ManagementGoalsInsertCall

Insert: Create a new goal.

- accountId: Account ID to create the goal for. - profileId: View (Profile) ID to create the goal for. - webPropertyId: Web property ID to create the goal for.

func (*ManagementGoalsService) List ¶
func (r *ManagementGoalsService) List(accountId string, webPropertyId string, profileId string) *ManagementGoalsListCall

List: Lists goals to which the user has access.

accountId: Account ID to retrieve goals for. Can either be a specific account ID or '~all', which refers to all the accounts that user has access to.
profileId: View (Profile) ID to retrieve goals for. Can either be a specific view (profile) ID or '~all', which refers to all the views (profiles) that user has access to.
webPropertyId: Web property ID to retrieve goals for. Can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.
func (*ManagementGoalsService) Patch ¶
func (r *ManagementGoalsService) Patch(accountId string, webPropertyId string, profileId string, goalId string, goal *Goal) *ManagementGoalsPatchCall

Patch: Updates an existing goal. This method supports patch semantics.

- accountId: Account ID to update the goal. - goalId: Index of the goal to be updated. - profileId: View (Profile) ID to update the goal. - webPropertyId: Web property ID to update the goal.

func (*ManagementGoalsService) Update ¶
func (r *ManagementGoalsService) Update(accountId string, webPropertyId string, profileId string, goalId string, goal *Goal) *ManagementGoalsUpdateCall

Update: Updates an existing goal.

- accountId: Account ID to update the goal. - goalId: Index of the goal to be updated. - profileId: View (Profile) ID to update the goal. - webPropertyId: Web property ID to update the goal.

type ManagementGoalsUpdateCall ¶
type ManagementGoalsUpdateCall struct {
	// contains filtered or unexported fields
}
func (*ManagementGoalsUpdateCall) Context ¶
func (c *ManagementGoalsUpdateCall) Context(ctx context.Context) *ManagementGoalsUpdateCall

Context sets the context to be used in this call's Do method.

func (*ManagementGoalsUpdateCall) Do ¶
func (c *ManagementGoalsUpdateCall) Do(opts ...googleapi.CallOption) (*Goal, error)

Do executes the "analytics.management.goals.update" call. Any non-2xx status code is an error. Response headers are in either *Goal.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementGoalsUpdateCall) Fields ¶
func (c *ManagementGoalsUpdateCall) Fields(s ...googleapi.Field) *ManagementGoalsUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementGoalsUpdateCall) Header ¶
func (c *ManagementGoalsUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementProfileFilterLinksDeleteCall ¶
type ManagementProfileFilterLinksDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ManagementProfileFilterLinksDeleteCall) Context ¶
func (c *ManagementProfileFilterLinksDeleteCall) Context(ctx context.Context) *ManagementProfileFilterLinksDeleteCall

Context sets the context to be used in this call's Do method.

func (*ManagementProfileFilterLinksDeleteCall) Do ¶
func (c *ManagementProfileFilterLinksDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "analytics.management.profileFilterLinks.delete" call.

func (*ManagementProfileFilterLinksDeleteCall) Fields ¶
func (c *ManagementProfileFilterLinksDeleteCall) Fields(s ...googleapi.Field) *ManagementProfileFilterLinksDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementProfileFilterLinksDeleteCall) Header ¶
func (c *ManagementProfileFilterLinksDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementProfileFilterLinksGetCall ¶
type ManagementProfileFilterLinksGetCall struct {
	// contains filtered or unexported fields
}
func (*ManagementProfileFilterLinksGetCall) Context ¶
func (c *ManagementProfileFilterLinksGetCall) Context(ctx context.Context) *ManagementProfileFilterLinksGetCall

Context sets the context to be used in this call's Do method.

func (*ManagementProfileFilterLinksGetCall) Do ¶
func (c *ManagementProfileFilterLinksGetCall) Do(opts ...googleapi.CallOption) (*ProfileFilterLink, error)

Do executes the "analytics.management.profileFilterLinks.get" call. Any non-2xx status code is an error. Response headers are in either *ProfileFilterLink.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementProfileFilterLinksGetCall) Fields ¶
func (c *ManagementProfileFilterLinksGetCall) Fields(s ...googleapi.Field) *ManagementProfileFilterLinksGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementProfileFilterLinksGetCall) Header ¶
func (c *ManagementProfileFilterLinksGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementProfileFilterLinksGetCall) IfNoneMatch ¶
func (c *ManagementProfileFilterLinksGetCall) IfNoneMatch(entityTag string) *ManagementProfileFilterLinksGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ManagementProfileFilterLinksInsertCall ¶
type ManagementProfileFilterLinksInsertCall struct {
	// contains filtered or unexported fields
}
func (*ManagementProfileFilterLinksInsertCall) Context ¶
func (c *ManagementProfileFilterLinksInsertCall) Context(ctx context.Context) *ManagementProfileFilterLinksInsertCall

Context sets the context to be used in this call's Do method.

func (*ManagementProfileFilterLinksInsertCall) Do ¶
func (c *ManagementProfileFilterLinksInsertCall) Do(opts ...googleapi.CallOption) (*ProfileFilterLink, error)

Do executes the "analytics.management.profileFilterLinks.insert" call. Any non-2xx status code is an error. Response headers are in either *ProfileFilterLink.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementProfileFilterLinksInsertCall) Fields ¶
func (c *ManagementProfileFilterLinksInsertCall) Fields(s ...googleapi.Field) *ManagementProfileFilterLinksInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementProfileFilterLinksInsertCall) Header ¶
func (c *ManagementProfileFilterLinksInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementProfileFilterLinksListCall ¶
type ManagementProfileFilterLinksListCall struct {
	// contains filtered or unexported fields
}
func (*ManagementProfileFilterLinksListCall) Context ¶
func (c *ManagementProfileFilterLinksListCall) Context(ctx context.Context) *ManagementProfileFilterLinksListCall

Context sets the context to be used in this call's Do method.

func (*ManagementProfileFilterLinksListCall) Do ¶
func (c *ManagementProfileFilterLinksListCall) Do(opts ...googleapi.CallOption) (*ProfileFilterLinks, error)

Do executes the "analytics.management.profileFilterLinks.list" call. Any non-2xx status code is an error. Response headers are in either *ProfileFilterLinks.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementProfileFilterLinksListCall) Fields ¶
func (c *ManagementProfileFilterLinksListCall) Fields(s ...googleapi.Field) *ManagementProfileFilterLinksListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementProfileFilterLinksListCall) Header ¶
func (c *ManagementProfileFilterLinksListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementProfileFilterLinksListCall) IfNoneMatch ¶
func (c *ManagementProfileFilterLinksListCall) IfNoneMatch(entityTag string) *ManagementProfileFilterLinksListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ManagementProfileFilterLinksListCall) MaxResults ¶
func (c *ManagementProfileFilterLinksListCall) MaxResults(maxResults int64) *ManagementProfileFilterLinksListCall

MaxResults sets the optional parameter "max-results": The maximum number of profile filter links to include in this response.

func (*ManagementProfileFilterLinksListCall) StartIndex ¶
func (c *ManagementProfileFilterLinksListCall) StartIndex(startIndex int64) *ManagementProfileFilterLinksListCall

StartIndex sets the optional parameter "start-index": An index of the first entity to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

type ManagementProfileFilterLinksPatchCall ¶
type ManagementProfileFilterLinksPatchCall struct {
	// contains filtered or unexported fields
}
func (*ManagementProfileFilterLinksPatchCall) Context ¶
func (c *ManagementProfileFilterLinksPatchCall) Context(ctx context.Context) *ManagementProfileFilterLinksPatchCall

Context sets the context to be used in this call's Do method.

func (*ManagementProfileFilterLinksPatchCall) Do ¶
func (c *ManagementProfileFilterLinksPatchCall) Do(opts ...googleapi.CallOption) (*ProfileFilterLink, error)

Do executes the "analytics.management.profileFilterLinks.patch" call. Any non-2xx status code is an error. Response headers are in either *ProfileFilterLink.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementProfileFilterLinksPatchCall) Fields ¶
func (c *ManagementProfileFilterLinksPatchCall) Fields(s ...googleapi.Field) *ManagementProfileFilterLinksPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementProfileFilterLinksPatchCall) Header ¶
func (c *ManagementProfileFilterLinksPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementProfileFilterLinksService ¶
type ManagementProfileFilterLinksService struct {
	// contains filtered or unexported fields
}
func NewManagementProfileFilterLinksService ¶
func NewManagementProfileFilterLinksService(s *Service) *ManagementProfileFilterLinksService
func (*ManagementProfileFilterLinksService) Delete ¶
func (r *ManagementProfileFilterLinksService) Delete(accountId string, webPropertyId string, profileId string, linkId string) *ManagementProfileFilterLinksDeleteCall

Delete: Delete a profile filter link.

- accountId: Account ID to which the profile filter link belongs. - linkId: ID of the profile filter link to delete. - profileId: Profile ID to which the filter link belongs. - webPropertyId: Web property Id to which the profile filter link belongs.

func (*ManagementProfileFilterLinksService) Get ¶
func (r *ManagementProfileFilterLinksService) Get(accountId string, webPropertyId string, profileId string, linkId string) *ManagementProfileFilterLinksGetCall

Get: Returns a single profile filter link.

- accountId: Account ID to retrieve profile filter link for. - linkId: ID of the profile filter link. - profileId: Profile ID to retrieve filter link for. - webPropertyId: Web property Id to retrieve profile filter link for.

func (*ManagementProfileFilterLinksService) Insert ¶
func (r *ManagementProfileFilterLinksService) Insert(accountId string, webPropertyId string, profileId string, profilefilterlink *ProfileFilterLink) *ManagementProfileFilterLinksInsertCall

Insert: Create a new profile filter link.

- accountId: Account ID to create profile filter link for. - profileId: Profile ID to create filter link for. - webPropertyId: Web property Id to create profile filter link for.

func (*ManagementProfileFilterLinksService) List ¶
func (r *ManagementProfileFilterLinksService) List(accountId string, webPropertyId string, profileId string) *ManagementProfileFilterLinksListCall

List: Lists all profile filter links for a profile.

accountId: Account ID to retrieve profile filter links for.
profileId: Profile ID to retrieve filter links for. Can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.
webPropertyId: Web property Id for profile filter links for. Can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.
func (*ManagementProfileFilterLinksService) Patch ¶
func (r *ManagementProfileFilterLinksService) Patch(accountId string, webPropertyId string, profileId string, linkId string, profilefilterlink *ProfileFilterLink) *ManagementProfileFilterLinksPatchCall

Patch: Update an existing profile filter link. This method supports patch semantics.

- accountId: Account ID to which profile filter link belongs. - linkId: ID of the profile filter link to be updated. - profileId: Profile ID to which filter link belongs. - webPropertyId: Web property Id to which profile filter link belongs.

func (*ManagementProfileFilterLinksService) Update ¶
func (r *ManagementProfileFilterLinksService) Update(accountId string, webPropertyId string, profileId string, linkId string, profilefilterlink *ProfileFilterLink) *ManagementProfileFilterLinksUpdateCall

Update: Update an existing profile filter link.

- accountId: Account ID to which profile filter link belongs. - linkId: ID of the profile filter link to be updated. - profileId: Profile ID to which filter link belongs. - webPropertyId: Web property Id to which profile filter link belongs.

type ManagementProfileFilterLinksUpdateCall ¶
type ManagementProfileFilterLinksUpdateCall struct {
	// contains filtered or unexported fields
}
func (*ManagementProfileFilterLinksUpdateCall) Context ¶
func (c *ManagementProfileFilterLinksUpdateCall) Context(ctx context.Context) *ManagementProfileFilterLinksUpdateCall

Context sets the context to be used in this call's Do method.

func (*ManagementProfileFilterLinksUpdateCall) Do ¶
func (c *ManagementProfileFilterLinksUpdateCall) Do(opts ...googleapi.CallOption) (*ProfileFilterLink, error)

Do executes the "analytics.management.profileFilterLinks.update" call. Any non-2xx status code is an error. Response headers are in either *ProfileFilterLink.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementProfileFilterLinksUpdateCall) Fields ¶
func (c *ManagementProfileFilterLinksUpdateCall) Fields(s ...googleapi.Field) *ManagementProfileFilterLinksUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementProfileFilterLinksUpdateCall) Header ¶
func (c *ManagementProfileFilterLinksUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementProfileUserLinksDeleteCall ¶
type ManagementProfileUserLinksDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ManagementProfileUserLinksDeleteCall) Context ¶
func (c *ManagementProfileUserLinksDeleteCall) Context(ctx context.Context) *ManagementProfileUserLinksDeleteCall

Context sets the context to be used in this call's Do method.

func (*ManagementProfileUserLinksDeleteCall) Do ¶
func (c *ManagementProfileUserLinksDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "analytics.management.profileUserLinks.delete" call.

func (*ManagementProfileUserLinksDeleteCall) Fields ¶
func (c *ManagementProfileUserLinksDeleteCall) Fields(s ...googleapi.Field) *ManagementProfileUserLinksDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementProfileUserLinksDeleteCall) Header ¶
func (c *ManagementProfileUserLinksDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementProfileUserLinksInsertCall ¶
type ManagementProfileUserLinksInsertCall struct {
	// contains filtered or unexported fields
}
func (*ManagementProfileUserLinksInsertCall) Context ¶
func (c *ManagementProfileUserLinksInsertCall) Context(ctx context.Context) *ManagementProfileUserLinksInsertCall

Context sets the context to be used in this call's Do method.

func (*ManagementProfileUserLinksInsertCall) Do ¶
func (c *ManagementProfileUserLinksInsertCall) Do(opts ...googleapi.CallOption) (*EntityUserLink, error)

Do executes the "analytics.management.profileUserLinks.insert" call. Any non-2xx status code is an error. Response headers are in either *EntityUserLink.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementProfileUserLinksInsertCall) Fields ¶
func (c *ManagementProfileUserLinksInsertCall) Fields(s ...googleapi.Field) *ManagementProfileUserLinksInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementProfileUserLinksInsertCall) Header ¶
func (c *ManagementProfileUserLinksInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementProfileUserLinksListCall ¶
type ManagementProfileUserLinksListCall struct {
	// contains filtered or unexported fields
}
func (*ManagementProfileUserLinksListCall) Context ¶
func (c *ManagementProfileUserLinksListCall) Context(ctx context.Context) *ManagementProfileUserLinksListCall

Context sets the context to be used in this call's Do method.

func (*ManagementProfileUserLinksListCall) Do ¶
func (c *ManagementProfileUserLinksListCall) Do(opts ...googleapi.CallOption) (*EntityUserLinks, error)

Do executes the "analytics.management.profileUserLinks.list" call. Any non-2xx status code is an error. Response headers are in either *EntityUserLinks.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementProfileUserLinksListCall) Fields ¶
func (c *ManagementProfileUserLinksListCall) Fields(s ...googleapi.Field) *ManagementProfileUserLinksListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementProfileUserLinksListCall) Header ¶
func (c *ManagementProfileUserLinksListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementProfileUserLinksListCall) IfNoneMatch ¶
func (c *ManagementProfileUserLinksListCall) IfNoneMatch(entityTag string) *ManagementProfileUserLinksListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ManagementProfileUserLinksListCall) MaxResults ¶
func (c *ManagementProfileUserLinksListCall) MaxResults(maxResults int64) *ManagementProfileUserLinksListCall

MaxResults sets the optional parameter "max-results": The maximum number of profile-user links to include in this response.

func (*ManagementProfileUserLinksListCall) StartIndex ¶
func (c *ManagementProfileUserLinksListCall) StartIndex(startIndex int64) *ManagementProfileUserLinksListCall

StartIndex sets the optional parameter "start-index": An index of the first profile-user link to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

type ManagementProfileUserLinksService ¶
type ManagementProfileUserLinksService struct {
	// contains filtered or unexported fields
}
func NewManagementProfileUserLinksService ¶
func NewManagementProfileUserLinksService(s *Service) *ManagementProfileUserLinksService
func (*ManagementProfileUserLinksService) Delete ¶
func (r *ManagementProfileUserLinksService) Delete(accountId string, webPropertyId string, profileId string, linkId string) *ManagementProfileUserLinksDeleteCall

Delete: Removes a user from the given view (profile).

- accountId: Account ID to delete the user link for. - linkId: Link ID to delete the user link for. - profileId: View (Profile) ID to delete the user link for. - webPropertyId: Web Property ID to delete the user link for.

func (*ManagementProfileUserLinksService) Insert ¶
func (r *ManagementProfileUserLinksService) Insert(accountId string, webPropertyId string, profileId string, entityuserlink *EntityUserLink) *ManagementProfileUserLinksInsertCall

Insert: Adds a new user to the given view (profile).

- accountId: Account ID to create the user link for. - profileId: View (Profile) ID to create the user link for. - webPropertyId: Web Property ID to create the user link for.

func (*ManagementProfileUserLinksService) List ¶
func (r *ManagementProfileUserLinksService) List(accountId string, webPropertyId string, profileId string) *ManagementProfileUserLinksListCall

List: Lists profile-user links for a given view (profile).

accountId: Account ID which the given view (profile) belongs to.
profileId: View (Profile) ID to retrieve the profile-user links for. Can either be a specific profile ID or '~all', which refers to all the profiles that user has access to.
webPropertyId: Web Property ID which the given view (profile) belongs to. Can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.
func (*ManagementProfileUserLinksService) Update ¶
func (r *ManagementProfileUserLinksService) Update(accountId string, webPropertyId string, profileId string, linkId string, entityuserlink *EntityUserLink) *ManagementProfileUserLinksUpdateCall

Update: Updates permissions for an existing user on the given view (profile).

- accountId: Account ID to update the user link for. - linkId: Link ID to update the user link for. - profileId: View (Profile ID) to update the user link for. - webPropertyId: Web Property ID to update the user link for.

type ManagementProfileUserLinksUpdateCall ¶
type ManagementProfileUserLinksUpdateCall struct {
	// contains filtered or unexported fields
}
func (*ManagementProfileUserLinksUpdateCall) Context ¶
func (c *ManagementProfileUserLinksUpdateCall) Context(ctx context.Context) *ManagementProfileUserLinksUpdateCall

Context sets the context to be used in this call's Do method.

func (*ManagementProfileUserLinksUpdateCall) Do ¶
func (c *ManagementProfileUserLinksUpdateCall) Do(opts ...googleapi.CallOption) (*EntityUserLink, error)

Do executes the "analytics.management.profileUserLinks.update" call. Any non-2xx status code is an error. Response headers are in either *EntityUserLink.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementProfileUserLinksUpdateCall) Fields ¶
func (c *ManagementProfileUserLinksUpdateCall) Fields(s ...googleapi.Field) *ManagementProfileUserLinksUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementProfileUserLinksUpdateCall) Header ¶
func (c *ManagementProfileUserLinksUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementProfilesDeleteCall ¶
type ManagementProfilesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ManagementProfilesDeleteCall) Context ¶
func (c *ManagementProfilesDeleteCall) Context(ctx context.Context) *ManagementProfilesDeleteCall

Context sets the context to be used in this call's Do method.

func (*ManagementProfilesDeleteCall) Do ¶
func (c *ManagementProfilesDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "analytics.management.profiles.delete" call.

func (*ManagementProfilesDeleteCall) Fields ¶
func (c *ManagementProfilesDeleteCall) Fields(s ...googleapi.Field) *ManagementProfilesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementProfilesDeleteCall) Header ¶
func (c *ManagementProfilesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementProfilesGetCall ¶
type ManagementProfilesGetCall struct {
	// contains filtered or unexported fields
}
func (*ManagementProfilesGetCall) Context ¶
func (c *ManagementProfilesGetCall) Context(ctx context.Context) *ManagementProfilesGetCall

Context sets the context to be used in this call's Do method.

func (*ManagementProfilesGetCall) Do ¶
func (c *ManagementProfilesGetCall) Do(opts ...googleapi.CallOption) (*Profile, error)

Do executes the "analytics.management.profiles.get" call. Any non-2xx status code is an error. Response headers are in either *Profile.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementProfilesGetCall) Fields ¶
func (c *ManagementProfilesGetCall) Fields(s ...googleapi.Field) *ManagementProfilesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementProfilesGetCall) Header ¶
func (c *ManagementProfilesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementProfilesGetCall) IfNoneMatch ¶
func (c *ManagementProfilesGetCall) IfNoneMatch(entityTag string) *ManagementProfilesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ManagementProfilesInsertCall ¶
type ManagementProfilesInsertCall struct {
	// contains filtered or unexported fields
}
func (*ManagementProfilesInsertCall) Context ¶
func (c *ManagementProfilesInsertCall) Context(ctx context.Context) *ManagementProfilesInsertCall

Context sets the context to be used in this call's Do method.

func (*ManagementProfilesInsertCall) Do ¶
func (c *ManagementProfilesInsertCall) Do(opts ...googleapi.CallOption) (*Profile, error)

Do executes the "analytics.management.profiles.insert" call. Any non-2xx status code is an error. Response headers are in either *Profile.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementProfilesInsertCall) Fields ¶
func (c *ManagementProfilesInsertCall) Fields(s ...googleapi.Field) *ManagementProfilesInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementProfilesInsertCall) Header ¶
func (c *ManagementProfilesInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementProfilesListCall ¶
type ManagementProfilesListCall struct {
	// contains filtered or unexported fields
}
func (*ManagementProfilesListCall) Context ¶
func (c *ManagementProfilesListCall) Context(ctx context.Context) *ManagementProfilesListCall

Context sets the context to be used in this call's Do method.

func (*ManagementProfilesListCall) Do ¶
func (c *ManagementProfilesListCall) Do(opts ...googleapi.CallOption) (*Profiles, error)

Do executes the "analytics.management.profiles.list" call. Any non-2xx status code is an error. Response headers are in either *Profiles.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementProfilesListCall) Fields ¶
func (c *ManagementProfilesListCall) Fields(s ...googleapi.Field) *ManagementProfilesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementProfilesListCall) Header ¶
func (c *ManagementProfilesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementProfilesListCall) IfNoneMatch ¶
func (c *ManagementProfilesListCall) IfNoneMatch(entityTag string) *ManagementProfilesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ManagementProfilesListCall) MaxResults ¶
func (c *ManagementProfilesListCall) MaxResults(maxResults int64) *ManagementProfilesListCall

MaxResults sets the optional parameter "max-results": The maximum number of views (profiles) to include in this response.

func (*ManagementProfilesListCall) StartIndex ¶
func (c *ManagementProfilesListCall) StartIndex(startIndex int64) *ManagementProfilesListCall

StartIndex sets the optional parameter "start-index": An index of the first entity to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

type ManagementProfilesPatchCall ¶
type ManagementProfilesPatchCall struct {
	// contains filtered or unexported fields
}
func (*ManagementProfilesPatchCall) Context ¶
func (c *ManagementProfilesPatchCall) Context(ctx context.Context) *ManagementProfilesPatchCall

Context sets the context to be used in this call's Do method.

func (*ManagementProfilesPatchCall) Do ¶
func (c *ManagementProfilesPatchCall) Do(opts ...googleapi.CallOption) (*Profile, error)

Do executes the "analytics.management.profiles.patch" call. Any non-2xx status code is an error. Response headers are in either *Profile.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementProfilesPatchCall) Fields ¶
func (c *ManagementProfilesPatchCall) Fields(s ...googleapi.Field) *ManagementProfilesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementProfilesPatchCall) Header ¶
func (c *ManagementProfilesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementProfilesService ¶
type ManagementProfilesService struct {
	// contains filtered or unexported fields
}
func NewManagementProfilesService ¶
func NewManagementProfilesService(s *Service) *ManagementProfilesService
func (*ManagementProfilesService) Delete ¶
func (r *ManagementProfilesService) Delete(accountId string, webPropertyId string, profileId string) *ManagementProfilesDeleteCall

Delete: Deletes a view (profile).

- accountId: Account ID to delete the view (profile) for. - profileId: ID of the view (profile) to be deleted. - webPropertyId: Web property ID to delete the view (profile) for.

func (*ManagementProfilesService) Get ¶
func (r *ManagementProfilesService) Get(accountId string, webPropertyId string, profileId string) *ManagementProfilesGetCall

Get: Gets a view (profile) to which the user has access.

- accountId: Account ID to retrieve the view (profile) for. - profileId: View (Profile) ID to retrieve the view (profile) for. - webPropertyId: Web property ID to retrieve the view (profile) for.

func (*ManagementProfilesService) Insert ¶
func (r *ManagementProfilesService) Insert(accountId string, webPropertyId string, profile *Profile) *ManagementProfilesInsertCall

Insert: Create a new view (profile).

- accountId: Account ID to create the view (profile) for. - webPropertyId: Web property ID to create the view (profile) for.

func (*ManagementProfilesService) List ¶
func (r *ManagementProfilesService) List(accountId string, webPropertyId string) *ManagementProfilesListCall

List: Lists views (profiles) to which the user has access.

accountId: Account ID for the view (profiles) to retrieve. Can either be a specific account ID or '~all', which refers to all the accounts to which the user has access.
webPropertyId: Web property ID for the views (profiles) to retrieve. Can either be a specific web property ID or '~all', which refers to all the web properties to which the user has access.
func (*ManagementProfilesService) Patch ¶
func (r *ManagementProfilesService) Patch(accountId string, webPropertyId string, profileId string, profile *Profile) *ManagementProfilesPatchCall

Patch: Updates an existing view (profile). This method supports patch semantics.

- accountId: Account ID to which the view (profile) belongs. - profileId: ID of the view (profile) to be updated. - webPropertyId: Web property ID to which the view (profile) belongs.

func (*ManagementProfilesService) Update ¶
func (r *ManagementProfilesService) Update(accountId string, webPropertyId string, profileId string, profile *Profile) *ManagementProfilesUpdateCall

Update: Updates an existing view (profile).

- accountId: Account ID to which the view (profile) belongs. - profileId: ID of the view (profile) to be updated. - webPropertyId: Web property ID to which the view (profile) belongs.

type ManagementProfilesUpdateCall ¶
type ManagementProfilesUpdateCall struct {
	// contains filtered or unexported fields
}
func (*ManagementProfilesUpdateCall) Context ¶
func (c *ManagementProfilesUpdateCall) Context(ctx context.Context) *ManagementProfilesUpdateCall

Context sets the context to be used in this call's Do method.

func (*ManagementProfilesUpdateCall) Do ¶
func (c *ManagementProfilesUpdateCall) Do(opts ...googleapi.CallOption) (*Profile, error)

Do executes the "analytics.management.profiles.update" call. Any non-2xx status code is an error. Response headers are in either *Profile.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementProfilesUpdateCall) Fields ¶
func (c *ManagementProfilesUpdateCall) Fields(s ...googleapi.Field) *ManagementProfilesUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementProfilesUpdateCall) Header ¶
func (c *ManagementProfilesUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementRemarketingAudienceDeleteCall ¶
type ManagementRemarketingAudienceDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ManagementRemarketingAudienceDeleteCall) Context ¶
func (c *ManagementRemarketingAudienceDeleteCall) Context(ctx context.Context) *ManagementRemarketingAudienceDeleteCall

Context sets the context to be used in this call's Do method.

func (*ManagementRemarketingAudienceDeleteCall) Do ¶
func (c *ManagementRemarketingAudienceDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "analytics.management.remarketingAudience.delete" call.

func (*ManagementRemarketingAudienceDeleteCall) Fields ¶
func (c *ManagementRemarketingAudienceDeleteCall) Fields(s ...googleapi.Field) *ManagementRemarketingAudienceDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementRemarketingAudienceDeleteCall) Header ¶
func (c *ManagementRemarketingAudienceDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementRemarketingAudienceGetCall ¶
type ManagementRemarketingAudienceGetCall struct {
	// contains filtered or unexported fields
}
func (*ManagementRemarketingAudienceGetCall) Context ¶
func (c *ManagementRemarketingAudienceGetCall) Context(ctx context.Context) *ManagementRemarketingAudienceGetCall

Context sets the context to be used in this call's Do method.

func (*ManagementRemarketingAudienceGetCall) Do ¶
func (c *ManagementRemarketingAudienceGetCall) Do(opts ...googleapi.CallOption) (*RemarketingAudience, error)

Do executes the "analytics.management.remarketingAudience.get" call. Any non-2xx status code is an error. Response headers are in either *RemarketingAudience.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementRemarketingAudienceGetCall) Fields ¶
func (c *ManagementRemarketingAudienceGetCall) Fields(s ...googleapi.Field) *ManagementRemarketingAudienceGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementRemarketingAudienceGetCall) Header ¶
func (c *ManagementRemarketingAudienceGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementRemarketingAudienceGetCall) IfNoneMatch ¶
func (c *ManagementRemarketingAudienceGetCall) IfNoneMatch(entityTag string) *ManagementRemarketingAudienceGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ManagementRemarketingAudienceInsertCall ¶
type ManagementRemarketingAudienceInsertCall struct {
	// contains filtered or unexported fields
}
func (*ManagementRemarketingAudienceInsertCall) Context ¶
func (c *ManagementRemarketingAudienceInsertCall) Context(ctx context.Context) *ManagementRemarketingAudienceInsertCall

Context sets the context to be used in this call's Do method.

func (*ManagementRemarketingAudienceInsertCall) Do ¶
func (c *ManagementRemarketingAudienceInsertCall) Do(opts ...googleapi.CallOption) (*RemarketingAudience, error)

Do executes the "analytics.management.remarketingAudience.insert" call. Any non-2xx status code is an error. Response headers are in either *RemarketingAudience.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementRemarketingAudienceInsertCall) Fields ¶
func (c *ManagementRemarketingAudienceInsertCall) Fields(s ...googleapi.Field) *ManagementRemarketingAudienceInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementRemarketingAudienceInsertCall) Header ¶
func (c *ManagementRemarketingAudienceInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementRemarketingAudienceListCall ¶
type ManagementRemarketingAudienceListCall struct {
	// contains filtered or unexported fields
}
func (*ManagementRemarketingAudienceListCall) Context ¶
func (c *ManagementRemarketingAudienceListCall) Context(ctx context.Context) *ManagementRemarketingAudienceListCall

Context sets the context to be used in this call's Do method.

func (*ManagementRemarketingAudienceListCall) Do ¶
func (c *ManagementRemarketingAudienceListCall) Do(opts ...googleapi.CallOption) (*RemarketingAudiences, error)

Do executes the "analytics.management.remarketingAudience.list" call. Any non-2xx status code is an error. Response headers are in either *RemarketingAudiences.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementRemarketingAudienceListCall) Fields ¶
func (c *ManagementRemarketingAudienceListCall) Fields(s ...googleapi.Field) *ManagementRemarketingAudienceListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementRemarketingAudienceListCall) Header ¶
func (c *ManagementRemarketingAudienceListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementRemarketingAudienceListCall) IfNoneMatch ¶
func (c *ManagementRemarketingAudienceListCall) IfNoneMatch(entityTag string) *ManagementRemarketingAudienceListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ManagementRemarketingAudienceListCall) MaxResults ¶
func (c *ManagementRemarketingAudienceListCall) MaxResults(maxResults int64) *ManagementRemarketingAudienceListCall

MaxResults sets the optional parameter "max-results": The maximum number of remarketing audiences to include in this response.

func (*ManagementRemarketingAudienceListCall) StartIndex ¶
func (c *ManagementRemarketingAudienceListCall) StartIndex(startIndex int64) *ManagementRemarketingAudienceListCall

StartIndex sets the optional parameter "start-index": An index of the first entity to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

func (*ManagementRemarketingAudienceListCall) Type ¶
func (c *ManagementRemarketingAudienceListCall) Type(type_ string) *ManagementRemarketingAudienceListCall

Type sets the optional parameter "type":

type ManagementRemarketingAudiencePatchCall ¶
type ManagementRemarketingAudiencePatchCall struct {
	// contains filtered or unexported fields
}
func (*ManagementRemarketingAudiencePatchCall) Context ¶
func (c *ManagementRemarketingAudiencePatchCall) Context(ctx context.Context) *ManagementRemarketingAudiencePatchCall

Context sets the context to be used in this call's Do method.

func (*ManagementRemarketingAudiencePatchCall) Do ¶
func (c *ManagementRemarketingAudiencePatchCall) Do(opts ...googleapi.CallOption) (*RemarketingAudience, error)

Do executes the "analytics.management.remarketingAudience.patch" call. Any non-2xx status code is an error. Response headers are in either *RemarketingAudience.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementRemarketingAudiencePatchCall) Fields ¶
func (c *ManagementRemarketingAudiencePatchCall) Fields(s ...googleapi.Field) *ManagementRemarketingAudiencePatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementRemarketingAudiencePatchCall) Header ¶
func (c *ManagementRemarketingAudiencePatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementRemarketingAudienceService ¶
type ManagementRemarketingAudienceService struct {
	// contains filtered or unexported fields
}
func NewManagementRemarketingAudienceService ¶
func NewManagementRemarketingAudienceService(s *Service) *ManagementRemarketingAudienceService
func (*ManagementRemarketingAudienceService) Delete ¶
func (r *ManagementRemarketingAudienceService) Delete(accountId string, webPropertyId string, remarketingAudienceId string) *ManagementRemarketingAudienceDeleteCall

Delete: Delete a remarketing audience.

- accountId: Account ID to which the remarketing audience belongs. - remarketingAudienceId: The ID of the remarketing audience to delete. - webPropertyId: Web property ID to which the remarketing audience belongs.

func (*ManagementRemarketingAudienceService) Get ¶
func (r *ManagementRemarketingAudienceService) Get(accountId string, webPropertyId string, remarketingAudienceId string) *ManagementRemarketingAudienceGetCall

Get: Gets a remarketing audience to which the user has access.

accountId: The account ID of the remarketing audience to retrieve.
remarketingAudienceId: The ID of the remarketing audience to retrieve.
webPropertyId: The web property ID of the remarketing audience to retrieve.
func (*ManagementRemarketingAudienceService) Insert ¶
func (r *ManagementRemarketingAudienceService) Insert(accountId string, webPropertyId string, remarketingaudience *RemarketingAudience) *ManagementRemarketingAudienceInsertCall

Insert: Creates a new remarketing audience.

accountId: The account ID for which to create the remarketing audience.
webPropertyId: Web property ID for which to create the remarketing audience.
func (*ManagementRemarketingAudienceService) List ¶
func (r *ManagementRemarketingAudienceService) List(accountId string, webPropertyId string) *ManagementRemarketingAudienceListCall

List: Lists remarketing audiences to which the user has access.

accountId: The account ID of the remarketing audiences to retrieve.
webPropertyId: The web property ID of the remarketing audiences to retrieve.
func (*ManagementRemarketingAudienceService) Patch ¶
func (r *ManagementRemarketingAudienceService) Patch(accountId string, webPropertyId string, remarketingAudienceId string, remarketingaudience *RemarketingAudience) *ManagementRemarketingAudiencePatchCall

Patch: Updates an existing remarketing audience. This method supports patch semantics.

- accountId: The account ID of the remarketing audience to update. - remarketingAudienceId: The ID of the remarketing audience to update. - webPropertyId: The web property ID of the remarketing audience to update.

func (*ManagementRemarketingAudienceService) Update ¶
func (r *ManagementRemarketingAudienceService) Update(accountId string, webPropertyId string, remarketingAudienceId string, remarketingaudience *RemarketingAudience) *ManagementRemarketingAudienceUpdateCall

Update: Updates an existing remarketing audience.

- accountId: The account ID of the remarketing audience to update. - remarketingAudienceId: The ID of the remarketing audience to update. - webPropertyId: The web property ID of the remarketing audience to update.

type ManagementRemarketingAudienceUpdateCall ¶
type ManagementRemarketingAudienceUpdateCall struct {
	// contains filtered or unexported fields
}
func (*ManagementRemarketingAudienceUpdateCall) Context ¶
func (c *ManagementRemarketingAudienceUpdateCall) Context(ctx context.Context) *ManagementRemarketingAudienceUpdateCall

Context sets the context to be used in this call's Do method.

func (*ManagementRemarketingAudienceUpdateCall) Do ¶
func (c *ManagementRemarketingAudienceUpdateCall) Do(opts ...googleapi.CallOption) (*RemarketingAudience, error)

Do executes the "analytics.management.remarketingAudience.update" call. Any non-2xx status code is an error. Response headers are in either *RemarketingAudience.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementRemarketingAudienceUpdateCall) Fields ¶
func (c *ManagementRemarketingAudienceUpdateCall) Fields(s ...googleapi.Field) *ManagementRemarketingAudienceUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementRemarketingAudienceUpdateCall) Header ¶
func (c *ManagementRemarketingAudienceUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementSegmentsListCall ¶
type ManagementSegmentsListCall struct {
	// contains filtered or unexported fields
}
func (*ManagementSegmentsListCall) Context ¶
func (c *ManagementSegmentsListCall) Context(ctx context.Context) *ManagementSegmentsListCall

Context sets the context to be used in this call's Do method.

func (*ManagementSegmentsListCall) Do ¶
func (c *ManagementSegmentsListCall) Do(opts ...googleapi.CallOption) (*Segments, error)

Do executes the "analytics.management.segments.list" call. Any non-2xx status code is an error. Response headers are in either *Segments.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementSegmentsListCall) Fields ¶
func (c *ManagementSegmentsListCall) Fields(s ...googleapi.Field) *ManagementSegmentsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementSegmentsListCall) Header ¶
func (c *ManagementSegmentsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementSegmentsListCall) IfNoneMatch ¶
func (c *ManagementSegmentsListCall) IfNoneMatch(entityTag string) *ManagementSegmentsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ManagementSegmentsListCall) MaxResults ¶
func (c *ManagementSegmentsListCall) MaxResults(maxResults int64) *ManagementSegmentsListCall

MaxResults sets the optional parameter "max-results": The maximum number of segments to include in this response.

func (*ManagementSegmentsListCall) StartIndex ¶
func (c *ManagementSegmentsListCall) StartIndex(startIndex int64) *ManagementSegmentsListCall

StartIndex sets the optional parameter "start-index": An index of the first segment to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

type ManagementSegmentsService ¶
type ManagementSegmentsService struct {
	// contains filtered or unexported fields
}
func NewManagementSegmentsService ¶
func NewManagementSegmentsService(s *Service) *ManagementSegmentsService
func (*ManagementSegmentsService) List ¶
func (r *ManagementSegmentsService) List() *ManagementSegmentsListCall

List: Lists segments to which the user has access.

type ManagementService ¶
type ManagementService struct {
	AccountSummaries *ManagementAccountSummariesService

	AccountUserLinks *ManagementAccountUserLinksService

	Accounts *ManagementAccountsService

	ClientId *ManagementClientIdService

	CustomDataSources *ManagementCustomDataSourcesService

	CustomDimensions *ManagementCustomDimensionsService

	CustomMetrics *ManagementCustomMetricsService

	Experiments *ManagementExperimentsService

	Filters *ManagementFiltersService

	Goals *ManagementGoalsService

	ProfileFilterLinks *ManagementProfileFilterLinksService

	ProfileUserLinks *ManagementProfileUserLinksService

	Profiles *ManagementProfilesService

	RemarketingAudience *ManagementRemarketingAudienceService

	Segments *ManagementSegmentsService

	UnsampledReports *ManagementUnsampledReportsService

	Uploads *ManagementUploadsService

	WebPropertyAdWordsLinks *ManagementWebPropertyAdWordsLinksService

	Webproperties *ManagementWebpropertiesService

	WebpropertyUserLinks *ManagementWebpropertyUserLinksService
	// contains filtered or unexported fields
}
func NewManagementService ¶
func NewManagementService(s *Service) *ManagementService
type ManagementUnsampledReportsDeleteCall ¶
type ManagementUnsampledReportsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ManagementUnsampledReportsDeleteCall) Context ¶
func (c *ManagementUnsampledReportsDeleteCall) Context(ctx context.Context) *ManagementUnsampledReportsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ManagementUnsampledReportsDeleteCall) Do ¶
func (c *ManagementUnsampledReportsDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "analytics.management.unsampledReports.delete" call.

func (*ManagementUnsampledReportsDeleteCall) Fields ¶
func (c *ManagementUnsampledReportsDeleteCall) Fields(s ...googleapi.Field) *ManagementUnsampledReportsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementUnsampledReportsDeleteCall) Header ¶
func (c *ManagementUnsampledReportsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementUnsampledReportsGetCall ¶
type ManagementUnsampledReportsGetCall struct {
	// contains filtered or unexported fields
}
func (*ManagementUnsampledReportsGetCall) Context ¶
func (c *ManagementUnsampledReportsGetCall) Context(ctx context.Context) *ManagementUnsampledReportsGetCall

Context sets the context to be used in this call's Do method.

func (*ManagementUnsampledReportsGetCall) Do ¶
func (c *ManagementUnsampledReportsGetCall) Do(opts ...googleapi.CallOption) (*UnsampledReport, error)

Do executes the "analytics.management.unsampledReports.get" call. Any non-2xx status code is an error. Response headers are in either *UnsampledReport.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementUnsampledReportsGetCall) Fields ¶
func (c *ManagementUnsampledReportsGetCall) Fields(s ...googleapi.Field) *ManagementUnsampledReportsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementUnsampledReportsGetCall) Header ¶
func (c *ManagementUnsampledReportsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementUnsampledReportsGetCall) IfNoneMatch ¶
func (c *ManagementUnsampledReportsGetCall) IfNoneMatch(entityTag string) *ManagementUnsampledReportsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ManagementUnsampledReportsInsertCall ¶
type ManagementUnsampledReportsInsertCall struct {
	// contains filtered or unexported fields
}
func (*ManagementUnsampledReportsInsertCall) Context ¶
func (c *ManagementUnsampledReportsInsertCall) Context(ctx context.Context) *ManagementUnsampledReportsInsertCall

Context sets the context to be used in this call's Do method.

func (*ManagementUnsampledReportsInsertCall) Do ¶
func (c *ManagementUnsampledReportsInsertCall) Do(opts ...googleapi.CallOption) (*UnsampledReport, error)

Do executes the "analytics.management.unsampledReports.insert" call. Any non-2xx status code is an error. Response headers are in either *UnsampledReport.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementUnsampledReportsInsertCall) Fields ¶
func (c *ManagementUnsampledReportsInsertCall) Fields(s ...googleapi.Field) *ManagementUnsampledReportsInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementUnsampledReportsInsertCall) Header ¶
func (c *ManagementUnsampledReportsInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementUnsampledReportsListCall ¶
type ManagementUnsampledReportsListCall struct {
	// contains filtered or unexported fields
}
func (*ManagementUnsampledReportsListCall) Context ¶
func (c *ManagementUnsampledReportsListCall) Context(ctx context.Context) *ManagementUnsampledReportsListCall

Context sets the context to be used in this call's Do method.

func (*ManagementUnsampledReportsListCall) Do ¶
func (c *ManagementUnsampledReportsListCall) Do(opts ...googleapi.CallOption) (*UnsampledReports, error)

Do executes the "analytics.management.unsampledReports.list" call. Any non-2xx status code is an error. Response headers are in either *UnsampledReports.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementUnsampledReportsListCall) Fields ¶
func (c *ManagementUnsampledReportsListCall) Fields(s ...googleapi.Field) *ManagementUnsampledReportsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementUnsampledReportsListCall) Header ¶
func (c *ManagementUnsampledReportsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementUnsampledReportsListCall) IfNoneMatch ¶
func (c *ManagementUnsampledReportsListCall) IfNoneMatch(entityTag string) *ManagementUnsampledReportsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ManagementUnsampledReportsListCall) MaxResults ¶
func (c *ManagementUnsampledReportsListCall) MaxResults(maxResults int64) *ManagementUnsampledReportsListCall

MaxResults sets the optional parameter "max-results": The maximum number of unsampled reports to include in this response.

func (*ManagementUnsampledReportsListCall) StartIndex ¶
func (c *ManagementUnsampledReportsListCall) StartIndex(startIndex int64) *ManagementUnsampledReportsListCall

StartIndex sets the optional parameter "start-index": An index of the first unsampled report to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

type ManagementUnsampledReportsService ¶
type ManagementUnsampledReportsService struct {
	// contains filtered or unexported fields
}
func NewManagementUnsampledReportsService ¶
func NewManagementUnsampledReportsService(s *Service) *ManagementUnsampledReportsService
func (*ManagementUnsampledReportsService) Delete ¶
func (r *ManagementUnsampledReportsService) Delete(accountId string, webPropertyId string, profileId string, unsampledReportId string) *ManagementUnsampledReportsDeleteCall

Delete: Deletes an unsampled report.

- accountId: Account ID to delete the unsampled report for. - profileId: View (Profile) ID to delete the unsampled report for. - unsampledReportId: ID of the unsampled report to be deleted. - webPropertyId: Web property ID to delete the unsampled reports for.

func (*ManagementUnsampledReportsService) Get ¶
func (r *ManagementUnsampledReportsService) Get(accountId string, webPropertyId string, profileId string, unsampledReportId string) *ManagementUnsampledReportsGetCall

Get: Returns a single unsampled report.

- accountId: Account ID to retrieve unsampled report for. - profileId: View (Profile) ID to retrieve unsampled report for. - unsampledReportId: ID of the unsampled report to retrieve. - webPropertyId: Web property ID to retrieve unsampled reports for.

func (*ManagementUnsampledReportsService) Insert ¶
func (r *ManagementUnsampledReportsService) Insert(accountId string, webPropertyId string, profileId string, unsampledreport *UnsampledReport) *ManagementUnsampledReportsInsertCall

Insert: Create a new unsampled report.

- accountId: Account ID to create the unsampled report for. - profileId: View (Profile) ID to create the unsampled report for. - webPropertyId: Web property ID to create the unsampled report for.

func (*ManagementUnsampledReportsService) List ¶
func (r *ManagementUnsampledReportsService) List(accountId string, webPropertyId string, profileId string) *ManagementUnsampledReportsListCall

List: Lists unsampled reports to which the user has access.

accountId: Account ID to retrieve unsampled reports for. Must be a specific account ID, ~all is not supported.
profileId: View (Profile) ID to retrieve unsampled reports for. Must be a specific view (profile) ID, ~all is not supported.
webPropertyId: Web property ID to retrieve unsampled reports for. Must be a specific web property ID, ~all is not supported.
type ManagementUploadsDeleteUploadDataCall ¶
type ManagementUploadsDeleteUploadDataCall struct {
	// contains filtered or unexported fields
}
func (*ManagementUploadsDeleteUploadDataCall) Context ¶
func (c *ManagementUploadsDeleteUploadDataCall) Context(ctx context.Context) *ManagementUploadsDeleteUploadDataCall

Context sets the context to be used in this call's Do method.

func (*ManagementUploadsDeleteUploadDataCall) Do ¶
func (c *ManagementUploadsDeleteUploadDataCall) Do(opts ...googleapi.CallOption) error

Do executes the "analytics.management.uploads.deleteUploadData" call.

func (*ManagementUploadsDeleteUploadDataCall) Fields ¶
func (c *ManagementUploadsDeleteUploadDataCall) Fields(s ...googleapi.Field) *ManagementUploadsDeleteUploadDataCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementUploadsDeleteUploadDataCall) Header ¶
func (c *ManagementUploadsDeleteUploadDataCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementUploadsGetCall ¶
type ManagementUploadsGetCall struct {
	// contains filtered or unexported fields
}
func (*ManagementUploadsGetCall) Context ¶
func (c *ManagementUploadsGetCall) Context(ctx context.Context) *ManagementUploadsGetCall

Context sets the context to be used in this call's Do method.

func (*ManagementUploadsGetCall) Do ¶
func (c *ManagementUploadsGetCall) Do(opts ...googleapi.CallOption) (*Upload, error)

Do executes the "analytics.management.uploads.get" call. Any non-2xx status code is an error. Response headers are in either *Upload.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementUploadsGetCall) Fields ¶
func (c *ManagementUploadsGetCall) Fields(s ...googleapi.Field) *ManagementUploadsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementUploadsGetCall) Header ¶
func (c *ManagementUploadsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementUploadsGetCall) IfNoneMatch ¶
func (c *ManagementUploadsGetCall) IfNoneMatch(entityTag string) *ManagementUploadsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ManagementUploadsListCall ¶
type ManagementUploadsListCall struct {
	// contains filtered or unexported fields
}
func (*ManagementUploadsListCall) Context ¶
func (c *ManagementUploadsListCall) Context(ctx context.Context) *ManagementUploadsListCall

Context sets the context to be used in this call's Do method.

func (*ManagementUploadsListCall) Do ¶
func (c *ManagementUploadsListCall) Do(opts ...googleapi.CallOption) (*Uploads, error)

Do executes the "analytics.management.uploads.list" call. Any non-2xx status code is an error. Response headers are in either *Uploads.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementUploadsListCall) Fields ¶
func (c *ManagementUploadsListCall) Fields(s ...googleapi.Field) *ManagementUploadsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementUploadsListCall) Header ¶
func (c *ManagementUploadsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementUploadsListCall) IfNoneMatch ¶
func (c *ManagementUploadsListCall) IfNoneMatch(entityTag string) *ManagementUploadsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ManagementUploadsListCall) MaxResults ¶
func (c *ManagementUploadsListCall) MaxResults(maxResults int64) *ManagementUploadsListCall

MaxResults sets the optional parameter "max-results": The maximum number of uploads to include in this response.

func (*ManagementUploadsListCall) StartIndex ¶
func (c *ManagementUploadsListCall) StartIndex(startIndex int64) *ManagementUploadsListCall

StartIndex sets the optional parameter "start-index": A 1-based index of the first upload to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

type ManagementUploadsService ¶
type ManagementUploadsService struct {
	// contains filtered or unexported fields
}
func NewManagementUploadsService ¶
func NewManagementUploadsService(s *Service) *ManagementUploadsService
func (*ManagementUploadsService) DeleteUploadData ¶
func (r *ManagementUploadsService) DeleteUploadData(accountId string, webPropertyId string, customDataSourceId string, analyticsdataimportdeleteuploaddatarequest *AnalyticsDataimportDeleteUploadDataRequest) *ManagementUploadsDeleteUploadDataCall

DeleteUploadData: Delete data associated with a previous upload.

- accountId: Account Id for the uploads to be deleted. - customDataSourceId: Custom data source Id for the uploads to be deleted. - webPropertyId: Web property Id for the uploads to be deleted.

func (*ManagementUploadsService) Get ¶
func (r *ManagementUploadsService) Get(accountId string, webPropertyId string, customDataSourceId string, uploadId string) *ManagementUploadsGetCall

Get: List uploads to which the user has access.

- accountId: Account Id for the upload to retrieve. - customDataSourceId: Custom data source Id for upload to retrieve. - uploadId: Upload Id to retrieve. - webPropertyId: Web property Id for the upload to retrieve.

func (*ManagementUploadsService) List ¶
func (r *ManagementUploadsService) List(accountId string, webPropertyId string, customDataSourceId string) *ManagementUploadsListCall

List: List uploads to which the user has access.

- accountId: Account Id for the uploads to retrieve. - customDataSourceId: Custom data source Id for uploads to retrieve. - webPropertyId: Web property Id for the uploads to retrieve.

func (*ManagementUploadsService) UploadData ¶
func (r *ManagementUploadsService) UploadData(accountId string, webPropertyId string, customDataSourceId string) *ManagementUploadsUploadDataCall

UploadData: Upload data for a custom data source.

accountId: Account Id associated with the upload.
customDataSourceId: Custom data source Id to which the data being uploaded belongs.
webPropertyId: Web property UA-string associated with the upload.
type ManagementUploadsUploadDataCall ¶
type ManagementUploadsUploadDataCall struct {
	// contains filtered or unexported fields
}
func (*ManagementUploadsUploadDataCall) Context ¶
func (c *ManagementUploadsUploadDataCall) Context(ctx context.Context) *ManagementUploadsUploadDataCall

Context sets the context to be used in this call's Do method. This context will supersede any context previously provided to the ResumableMedia method.

func (*ManagementUploadsUploadDataCall) Do ¶
func (c *ManagementUploadsUploadDataCall) Do(opts ...googleapi.CallOption) (*Upload, error)

Do executes the "analytics.management.uploads.uploadData" call. Any non-2xx status code is an error. Response headers are in either *Upload.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementUploadsUploadDataCall) Fields ¶
func (c *ManagementUploadsUploadDataCall) Fields(s ...googleapi.Field) *ManagementUploadsUploadDataCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementUploadsUploadDataCall) Header ¶
func (c *ManagementUploadsUploadDataCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementUploadsUploadDataCall) Media ¶
func (c *ManagementUploadsUploadDataCall) Media(r io.Reader, options ...googleapi.MediaOption) *ManagementUploadsUploadDataCall

Media specifies the media to upload in one or more chunks. The chunk size may be controlled by supplying a MediaOption generated by googleapi.ChunkSize. The chunk size defaults to googleapi.DefaultUploadChunkSize.The Content-Type header used in the upload request will be determined by sniffing the contents of r, unless a MediaOption generated by googleapi.ContentType is supplied. At most one of Media and ResumableMedia may be set.

func (*ManagementUploadsUploadDataCall) ProgressUpdater ¶
func (c *ManagementUploadsUploadDataCall) ProgressUpdater(pu googleapi.ProgressUpdater) *ManagementUploadsUploadDataCall

ProgressUpdater provides a callback function that will be called after every chunk. It should be a low-latency function in order to not slow down the upload operation. This should only be called when using ResumableMedia (as opposed to Media).

func (*ManagementUploadsUploadDataCall)
ResumableMedia
DEPRECATED
type ManagementWebPropertyAdWordsLinksDeleteCall ¶
type ManagementWebPropertyAdWordsLinksDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ManagementWebPropertyAdWordsLinksDeleteCall) Context ¶
func (c *ManagementWebPropertyAdWordsLinksDeleteCall) Context(ctx context.Context) *ManagementWebPropertyAdWordsLinksDeleteCall

Context sets the context to be used in this call's Do method.

func (*ManagementWebPropertyAdWordsLinksDeleteCall) Do ¶
func (c *ManagementWebPropertyAdWordsLinksDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "analytics.management.webPropertyAdWordsLinks.delete" call.

func (*ManagementWebPropertyAdWordsLinksDeleteCall) Fields ¶
func (c *ManagementWebPropertyAdWordsLinksDeleteCall) Fields(s ...googleapi.Field) *ManagementWebPropertyAdWordsLinksDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementWebPropertyAdWordsLinksDeleteCall) Header ¶
func (c *ManagementWebPropertyAdWordsLinksDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementWebPropertyAdWordsLinksGetCall ¶
type ManagementWebPropertyAdWordsLinksGetCall struct {
	// contains filtered or unexported fields
}
func (*ManagementWebPropertyAdWordsLinksGetCall) Context ¶
func (c *ManagementWebPropertyAdWordsLinksGetCall) Context(ctx context.Context) *ManagementWebPropertyAdWordsLinksGetCall

Context sets the context to be used in this call's Do method.

func (*ManagementWebPropertyAdWordsLinksGetCall) Do ¶
func (c *ManagementWebPropertyAdWordsLinksGetCall) Do(opts ...googleapi.CallOption) (*EntityAdWordsLink, error)

Do executes the "analytics.management.webPropertyAdWordsLinks.get" call. Any non-2xx status code is an error. Response headers are in either *EntityAdWordsLink.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementWebPropertyAdWordsLinksGetCall) Fields ¶
func (c *ManagementWebPropertyAdWordsLinksGetCall) Fields(s ...googleapi.Field) *ManagementWebPropertyAdWordsLinksGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementWebPropertyAdWordsLinksGetCall) Header ¶
func (c *ManagementWebPropertyAdWordsLinksGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementWebPropertyAdWordsLinksGetCall) IfNoneMatch ¶
func (c *ManagementWebPropertyAdWordsLinksGetCall) IfNoneMatch(entityTag string) *ManagementWebPropertyAdWordsLinksGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ManagementWebPropertyAdWordsLinksInsertCall ¶
type ManagementWebPropertyAdWordsLinksInsertCall struct {
	// contains filtered or unexported fields
}
func (*ManagementWebPropertyAdWordsLinksInsertCall) Context ¶
func (c *ManagementWebPropertyAdWordsLinksInsertCall) Context(ctx context.Context) *ManagementWebPropertyAdWordsLinksInsertCall

Context sets the context to be used in this call's Do method.

func (*ManagementWebPropertyAdWordsLinksInsertCall) Do ¶
func (c *ManagementWebPropertyAdWordsLinksInsertCall) Do(opts ...googleapi.CallOption) (*EntityAdWordsLink, error)

Do executes the "analytics.management.webPropertyAdWordsLinks.insert" call. Any non-2xx status code is an error. Response headers are in either *EntityAdWordsLink.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementWebPropertyAdWordsLinksInsertCall) Fields ¶
func (c *ManagementWebPropertyAdWordsLinksInsertCall) Fields(s ...googleapi.Field) *ManagementWebPropertyAdWordsLinksInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementWebPropertyAdWordsLinksInsertCall) Header ¶
func (c *ManagementWebPropertyAdWordsLinksInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementWebPropertyAdWordsLinksListCall ¶
type ManagementWebPropertyAdWordsLinksListCall struct {
	// contains filtered or unexported fields
}
func (*ManagementWebPropertyAdWordsLinksListCall) Context ¶
func (c *ManagementWebPropertyAdWordsLinksListCall) Context(ctx context.Context) *ManagementWebPropertyAdWordsLinksListCall

Context sets the context to be used in this call's Do method.

func (*ManagementWebPropertyAdWordsLinksListCall) Do ¶
func (c *ManagementWebPropertyAdWordsLinksListCall) Do(opts ...googleapi.CallOption) (*EntityAdWordsLinks, error)

Do executes the "analytics.management.webPropertyAdWordsLinks.list" call. Any non-2xx status code is an error. Response headers are in either *EntityAdWordsLinks.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementWebPropertyAdWordsLinksListCall) Fields ¶
func (c *ManagementWebPropertyAdWordsLinksListCall) Fields(s ...googleapi.Field) *ManagementWebPropertyAdWordsLinksListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementWebPropertyAdWordsLinksListCall) Header ¶
func (c *ManagementWebPropertyAdWordsLinksListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementWebPropertyAdWordsLinksListCall) IfNoneMatch ¶
func (c *ManagementWebPropertyAdWordsLinksListCall) IfNoneMatch(entityTag string) *ManagementWebPropertyAdWordsLinksListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ManagementWebPropertyAdWordsLinksListCall) MaxResults ¶
func (c *ManagementWebPropertyAdWordsLinksListCall) MaxResults(maxResults int64) *ManagementWebPropertyAdWordsLinksListCall

MaxResults sets the optional parameter "max-results": The maximum number of webProperty-Google Ads links to include in this response.

func (*ManagementWebPropertyAdWordsLinksListCall) StartIndex ¶
func (c *ManagementWebPropertyAdWordsLinksListCall) StartIndex(startIndex int64) *ManagementWebPropertyAdWordsLinksListCall

StartIndex sets the optional parameter "start-index": An index of the first webProperty-Google Ads link to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

type ManagementWebPropertyAdWordsLinksPatchCall ¶
type ManagementWebPropertyAdWordsLinksPatchCall struct {
	// contains filtered or unexported fields
}
func (*ManagementWebPropertyAdWordsLinksPatchCall) Context ¶
func (c *ManagementWebPropertyAdWordsLinksPatchCall) Context(ctx context.Context) *ManagementWebPropertyAdWordsLinksPatchCall

Context sets the context to be used in this call's Do method.

func (*ManagementWebPropertyAdWordsLinksPatchCall) Do ¶
func (c *ManagementWebPropertyAdWordsLinksPatchCall) Do(opts ...googleapi.CallOption) (*EntityAdWordsLink, error)

Do executes the "analytics.management.webPropertyAdWordsLinks.patch" call. Any non-2xx status code is an error. Response headers are in either *EntityAdWordsLink.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementWebPropertyAdWordsLinksPatchCall) Fields ¶
func (c *ManagementWebPropertyAdWordsLinksPatchCall) Fields(s ...googleapi.Field) *ManagementWebPropertyAdWordsLinksPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementWebPropertyAdWordsLinksPatchCall) Header ¶
func (c *ManagementWebPropertyAdWordsLinksPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementWebPropertyAdWordsLinksService ¶
type ManagementWebPropertyAdWordsLinksService struct {
	// contains filtered or unexported fields
}
func NewManagementWebPropertyAdWordsLinksService ¶
func NewManagementWebPropertyAdWordsLinksService(s *Service) *ManagementWebPropertyAdWordsLinksService
func (*ManagementWebPropertyAdWordsLinksService) Delete ¶
func (r *ManagementWebPropertyAdWordsLinksService) Delete(accountId string, webPropertyId string, webPropertyAdWordsLinkId string) *ManagementWebPropertyAdWordsLinksDeleteCall

Delete: Deletes a web property-Google Ads link.

- accountId: ID of the account which the given web property belongs to. - webPropertyAdWordsLinkId: Web property Google Ads link ID. - webPropertyId: Web property ID to delete the Google Ads link for.

func (*ManagementWebPropertyAdWordsLinksService) Get ¶
func (r *ManagementWebPropertyAdWordsLinksService) Get(accountId string, webPropertyId string, webPropertyAdWordsLinkId string) *ManagementWebPropertyAdWordsLinksGetCall

Get: Returns a web property-Google Ads link to which the user has access.

- accountId: ID of the account which the given web property belongs to. - webPropertyAdWordsLinkId: Web property-Google Ads link ID. - webPropertyId: Web property ID to retrieve the Google Ads link for.

func (*ManagementWebPropertyAdWordsLinksService) Insert ¶
func (r *ManagementWebPropertyAdWordsLinksService) Insert(accountId string, webPropertyId string, entityadwordslink *EntityAdWordsLink) *ManagementWebPropertyAdWordsLinksInsertCall

Insert: Creates a webProperty-Google Ads link.

- accountId: ID of the Google Analytics account to create the link for. - webPropertyId: Web property ID to create the link for.

func (*ManagementWebPropertyAdWordsLinksService) List ¶
func (r *ManagementWebPropertyAdWordsLinksService) List(accountId string, webPropertyId string) *ManagementWebPropertyAdWordsLinksListCall

List: Lists webProperty-Google Ads links for a given web property.

- accountId: ID of the account which the given web property belongs to. - webPropertyId: Web property ID to retrieve the Google Ads links for.

func (*ManagementWebPropertyAdWordsLinksService) Patch ¶
func (r *ManagementWebPropertyAdWordsLinksService) Patch(accountId string, webPropertyId string, webPropertyAdWordsLinkId string, entityadwordslink *EntityAdWordsLink) *ManagementWebPropertyAdWordsLinksPatchCall

Patch: Updates an existing webProperty-Google Ads link. This method supports patch semantics.

- accountId: ID of the account which the given web property belongs to. - webPropertyAdWordsLinkId: Web property-Google Ads link ID. - webPropertyId: Web property ID to retrieve the Google Ads link for.

func (*ManagementWebPropertyAdWordsLinksService) Update ¶
func (r *ManagementWebPropertyAdWordsLinksService) Update(accountId string, webPropertyId string, webPropertyAdWordsLinkId string, entityadwordslink *EntityAdWordsLink) *ManagementWebPropertyAdWordsLinksUpdateCall

Update: Updates an existing webProperty-Google Ads link.

- accountId: ID of the account which the given web property belongs to. - webPropertyAdWordsLinkId: Web property-Google Ads link ID. - webPropertyId: Web property ID to retrieve the Google Ads link for.

type ManagementWebPropertyAdWordsLinksUpdateCall ¶
type ManagementWebPropertyAdWordsLinksUpdateCall struct {
	// contains filtered or unexported fields
}
func (*ManagementWebPropertyAdWordsLinksUpdateCall) Context ¶
func (c *ManagementWebPropertyAdWordsLinksUpdateCall) Context(ctx context.Context) *ManagementWebPropertyAdWordsLinksUpdateCall

Context sets the context to be used in this call's Do method.

func (*ManagementWebPropertyAdWordsLinksUpdateCall) Do ¶
func (c *ManagementWebPropertyAdWordsLinksUpdateCall) Do(opts ...googleapi.CallOption) (*EntityAdWordsLink, error)

Do executes the "analytics.management.webPropertyAdWordsLinks.update" call. Any non-2xx status code is an error. Response headers are in either *EntityAdWordsLink.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementWebPropertyAdWordsLinksUpdateCall) Fields ¶
func (c *ManagementWebPropertyAdWordsLinksUpdateCall) Fields(s ...googleapi.Field) *ManagementWebPropertyAdWordsLinksUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementWebPropertyAdWordsLinksUpdateCall) Header ¶
func (c *ManagementWebPropertyAdWordsLinksUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementWebpropertiesGetCall ¶
type ManagementWebpropertiesGetCall struct {
	// contains filtered or unexported fields
}
func (*ManagementWebpropertiesGetCall) Context ¶
func (c *ManagementWebpropertiesGetCall) Context(ctx context.Context) *ManagementWebpropertiesGetCall

Context sets the context to be used in this call's Do method.

func (*ManagementWebpropertiesGetCall) Do ¶
func (c *ManagementWebpropertiesGetCall) Do(opts ...googleapi.CallOption) (*Webproperty, error)

Do executes the "analytics.management.webproperties.get" call. Any non-2xx status code is an error. Response headers are in either *Webproperty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementWebpropertiesGetCall) Fields ¶
func (c *ManagementWebpropertiesGetCall) Fields(s ...googleapi.Field) *ManagementWebpropertiesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementWebpropertiesGetCall) Header ¶
func (c *ManagementWebpropertiesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementWebpropertiesGetCall) IfNoneMatch ¶
func (c *ManagementWebpropertiesGetCall) IfNoneMatch(entityTag string) *ManagementWebpropertiesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ManagementWebpropertiesInsertCall ¶
type ManagementWebpropertiesInsertCall struct {
	// contains filtered or unexported fields
}
func (*ManagementWebpropertiesInsertCall) Context ¶
func (c *ManagementWebpropertiesInsertCall) Context(ctx context.Context) *ManagementWebpropertiesInsertCall

Context sets the context to be used in this call's Do method.

func (*ManagementWebpropertiesInsertCall) Do ¶
func (c *ManagementWebpropertiesInsertCall) Do(opts ...googleapi.CallOption) (*Webproperty, error)

Do executes the "analytics.management.webproperties.insert" call. Any non-2xx status code is an error. Response headers are in either *Webproperty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementWebpropertiesInsertCall) Fields ¶
func (c *ManagementWebpropertiesInsertCall) Fields(s ...googleapi.Field) *ManagementWebpropertiesInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementWebpropertiesInsertCall) Header ¶
func (c *ManagementWebpropertiesInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementWebpropertiesListCall ¶
type ManagementWebpropertiesListCall struct {
	// contains filtered or unexported fields
}
func (*ManagementWebpropertiesListCall) Context ¶
func (c *ManagementWebpropertiesListCall) Context(ctx context.Context) *ManagementWebpropertiesListCall

Context sets the context to be used in this call's Do method.

func (*ManagementWebpropertiesListCall) Do ¶
func (c *ManagementWebpropertiesListCall) Do(opts ...googleapi.CallOption) (*Webproperties, error)

Do executes the "analytics.management.webproperties.list" call. Any non-2xx status code is an error. Response headers are in either *Webproperties.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementWebpropertiesListCall) Fields ¶
func (c *ManagementWebpropertiesListCall) Fields(s ...googleapi.Field) *ManagementWebpropertiesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementWebpropertiesListCall) Header ¶
func (c *ManagementWebpropertiesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementWebpropertiesListCall) IfNoneMatch ¶
func (c *ManagementWebpropertiesListCall) IfNoneMatch(entityTag string) *ManagementWebpropertiesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ManagementWebpropertiesListCall) MaxResults ¶
func (c *ManagementWebpropertiesListCall) MaxResults(maxResults int64) *ManagementWebpropertiesListCall

MaxResults sets the optional parameter "max-results": The maximum number of web properties to include in this response.

func (*ManagementWebpropertiesListCall) StartIndex ¶
func (c *ManagementWebpropertiesListCall) StartIndex(startIndex int64) *ManagementWebpropertiesListCall

StartIndex sets the optional parameter "start-index": An index of the first entity to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

type ManagementWebpropertiesPatchCall ¶
type ManagementWebpropertiesPatchCall struct {
	// contains filtered or unexported fields
}
func (*ManagementWebpropertiesPatchCall) Context ¶
func (c *ManagementWebpropertiesPatchCall) Context(ctx context.Context) *ManagementWebpropertiesPatchCall

Context sets the context to be used in this call's Do method.

func (*ManagementWebpropertiesPatchCall) Do ¶
func (c *ManagementWebpropertiesPatchCall) Do(opts ...googleapi.CallOption) (*Webproperty, error)

Do executes the "analytics.management.webproperties.patch" call. Any non-2xx status code is an error. Response headers are in either *Webproperty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementWebpropertiesPatchCall) Fields ¶
func (c *ManagementWebpropertiesPatchCall) Fields(s ...googleapi.Field) *ManagementWebpropertiesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementWebpropertiesPatchCall) Header ¶
func (c *ManagementWebpropertiesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementWebpropertiesService ¶
type ManagementWebpropertiesService struct {
	// contains filtered or unexported fields
}
func NewManagementWebpropertiesService ¶
func NewManagementWebpropertiesService(s *Service) *ManagementWebpropertiesService
func (*ManagementWebpropertiesService) Get ¶
func (r *ManagementWebpropertiesService) Get(accountId string, webPropertyId string) *ManagementWebpropertiesGetCall

Get: Gets a web property to which the user has access.

- accountId: Account ID to retrieve the web property for. - webPropertyId: ID to retrieve the web property for.

func (*ManagementWebpropertiesService) Insert ¶
func (r *ManagementWebpropertiesService) Insert(accountId string, webproperty *Webproperty) *ManagementWebpropertiesInsertCall

Insert: Create a new property if the account has fewer than 20 properties. Web properties are visible in the Google Analytics interface only if they have at least one profile.

- accountId: Account ID to create the web property for.

func (*ManagementWebpropertiesService) List ¶
func (r *ManagementWebpropertiesService) List(accountId string) *ManagementWebpropertiesListCall

List: Lists web properties to which the user has access.

accountId: Account ID to retrieve web properties for. Can either be a specific account ID or '~all', which refers to all the accounts that user has access to.
func (*ManagementWebpropertiesService) Patch ¶
func (r *ManagementWebpropertiesService) Patch(accountId string, webPropertyId string, webproperty *Webproperty) *ManagementWebpropertiesPatchCall

Patch: Updates an existing web property. This method supports patch semantics.

- accountId: Account ID to which the web property belongs. - webPropertyId: Web property ID.

func (*ManagementWebpropertiesService) Update ¶
func (r *ManagementWebpropertiesService) Update(accountId string, webPropertyId string, webproperty *Webproperty) *ManagementWebpropertiesUpdateCall

Update: Updates an existing web property.

- accountId: Account ID to which the web property belongs. - webPropertyId: Web property ID.

type ManagementWebpropertiesUpdateCall ¶
type ManagementWebpropertiesUpdateCall struct {
	// contains filtered or unexported fields
}
func (*ManagementWebpropertiesUpdateCall) Context ¶
func (c *ManagementWebpropertiesUpdateCall) Context(ctx context.Context) *ManagementWebpropertiesUpdateCall

Context sets the context to be used in this call's Do method.

func (*ManagementWebpropertiesUpdateCall) Do ¶
func (c *ManagementWebpropertiesUpdateCall) Do(opts ...googleapi.CallOption) (*Webproperty, error)

Do executes the "analytics.management.webproperties.update" call. Any non-2xx status code is an error. Response headers are in either *Webproperty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementWebpropertiesUpdateCall) Fields ¶
func (c *ManagementWebpropertiesUpdateCall) Fields(s ...googleapi.Field) *ManagementWebpropertiesUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementWebpropertiesUpdateCall) Header ¶
func (c *ManagementWebpropertiesUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementWebpropertyUserLinksDeleteCall ¶
type ManagementWebpropertyUserLinksDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ManagementWebpropertyUserLinksDeleteCall) Context ¶
func (c *ManagementWebpropertyUserLinksDeleteCall) Context(ctx context.Context) *ManagementWebpropertyUserLinksDeleteCall

Context sets the context to be used in this call's Do method.

func (*ManagementWebpropertyUserLinksDeleteCall) Do ¶
func (c *ManagementWebpropertyUserLinksDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "analytics.management.webpropertyUserLinks.delete" call.

func (*ManagementWebpropertyUserLinksDeleteCall) Fields ¶
func (c *ManagementWebpropertyUserLinksDeleteCall) Fields(s ...googleapi.Field) *ManagementWebpropertyUserLinksDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementWebpropertyUserLinksDeleteCall) Header ¶
func (c *ManagementWebpropertyUserLinksDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementWebpropertyUserLinksInsertCall ¶
type ManagementWebpropertyUserLinksInsertCall struct {
	// contains filtered or unexported fields
}
func (*ManagementWebpropertyUserLinksInsertCall) Context ¶
func (c *ManagementWebpropertyUserLinksInsertCall) Context(ctx context.Context) *ManagementWebpropertyUserLinksInsertCall

Context sets the context to be used in this call's Do method.

func (*ManagementWebpropertyUserLinksInsertCall) Do ¶
func (c *ManagementWebpropertyUserLinksInsertCall) Do(opts ...googleapi.CallOption) (*EntityUserLink, error)

Do executes the "analytics.management.webpropertyUserLinks.insert" call. Any non-2xx status code is an error. Response headers are in either *EntityUserLink.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementWebpropertyUserLinksInsertCall) Fields ¶
func (c *ManagementWebpropertyUserLinksInsertCall) Fields(s ...googleapi.Field) *ManagementWebpropertyUserLinksInsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementWebpropertyUserLinksInsertCall) Header ¶
func (c *ManagementWebpropertyUserLinksInsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ManagementWebpropertyUserLinksListCall ¶
type ManagementWebpropertyUserLinksListCall struct {
	// contains filtered or unexported fields
}
func (*ManagementWebpropertyUserLinksListCall) Context ¶
func (c *ManagementWebpropertyUserLinksListCall) Context(ctx context.Context) *ManagementWebpropertyUserLinksListCall

Context sets the context to be used in this call's Do method.

func (*ManagementWebpropertyUserLinksListCall) Do ¶
func (c *ManagementWebpropertyUserLinksListCall) Do(opts ...googleapi.CallOption) (*EntityUserLinks, error)

Do executes the "analytics.management.webpropertyUserLinks.list" call. Any non-2xx status code is an error. Response headers are in either *EntityUserLinks.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementWebpropertyUserLinksListCall) Fields ¶
func (c *ManagementWebpropertyUserLinksListCall) Fields(s ...googleapi.Field) *ManagementWebpropertyUserLinksListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementWebpropertyUserLinksListCall) Header ¶
func (c *ManagementWebpropertyUserLinksListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ManagementWebpropertyUserLinksListCall) IfNoneMatch ¶
func (c *ManagementWebpropertyUserLinksListCall) IfNoneMatch(entityTag string) *ManagementWebpropertyUserLinksListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ManagementWebpropertyUserLinksListCall) MaxResults ¶
func (c *ManagementWebpropertyUserLinksListCall) MaxResults(maxResults int64) *ManagementWebpropertyUserLinksListCall

MaxResults sets the optional parameter "max-results": The maximum number of webProperty-user Links to include in this response.

func (*ManagementWebpropertyUserLinksListCall) StartIndex ¶
func (c *ManagementWebpropertyUserLinksListCall) StartIndex(startIndex int64) *ManagementWebpropertyUserLinksListCall

StartIndex sets the optional parameter "start-index": An index of the first webProperty-user link to retrieve. Use this parameter as a pagination mechanism along with the max-results parameter.

type ManagementWebpropertyUserLinksService ¶
type ManagementWebpropertyUserLinksService struct {
	// contains filtered or unexported fields
}
func NewManagementWebpropertyUserLinksService ¶
func NewManagementWebpropertyUserLinksService(s *Service) *ManagementWebpropertyUserLinksService
func (*ManagementWebpropertyUserLinksService) Delete ¶
func (r *ManagementWebpropertyUserLinksService) Delete(accountId string, webPropertyId string, linkId string) *ManagementWebpropertyUserLinksDeleteCall

Delete: Removes a user from the given web property.

- accountId: Account ID to delete the user link for. - linkId: Link ID to delete the user link for. - webPropertyId: Web Property ID to delete the user link for.

func (*ManagementWebpropertyUserLinksService) Insert ¶
func (r *ManagementWebpropertyUserLinksService) Insert(accountId string, webPropertyId string, entityuserlink *EntityUserLink) *ManagementWebpropertyUserLinksInsertCall

Insert: Adds a new user to the given web property.

- accountId: Account ID to create the user link for. - webPropertyId: Web Property ID to create the user link for.

func (*ManagementWebpropertyUserLinksService) List ¶
func (r *ManagementWebpropertyUserLinksService) List(accountId string, webPropertyId string) *ManagementWebpropertyUserLinksListCall

List: Lists webProperty-user links for a given web property.

accountId: Account ID which the given web property belongs to.
webPropertyId: Web Property ID for the webProperty-user links to retrieve. Can either be a specific web property ID or '~all', which refers to all the web properties that user has access to.
func (*ManagementWebpropertyUserLinksService) Update ¶
func (r *ManagementWebpropertyUserLinksService) Update(accountId string, webPropertyId string, linkId string, entityuserlink *EntityUserLink) *ManagementWebpropertyUserLinksUpdateCall

Update: Updates permissions for an existing user on the given web property.

- accountId: Account ID to update the account-user link for. - linkId: Link ID to update the account-user link for. - webPropertyId: Web property ID to update the account-user link for.

type ManagementWebpropertyUserLinksUpdateCall ¶
type ManagementWebpropertyUserLinksUpdateCall struct {
	// contains filtered or unexported fields
}
func (*ManagementWebpropertyUserLinksUpdateCall) Context ¶
func (c *ManagementWebpropertyUserLinksUpdateCall) Context(ctx context.Context) *ManagementWebpropertyUserLinksUpdateCall

Context sets the context to be used in this call's Do method.

func (*ManagementWebpropertyUserLinksUpdateCall) Do ¶
func (c *ManagementWebpropertyUserLinksUpdateCall) Do(opts ...googleapi.CallOption) (*EntityUserLink, error)

Do executes the "analytics.management.webpropertyUserLinks.update" call. Any non-2xx status code is an error. Response headers are in either *EntityUserLink.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ManagementWebpropertyUserLinksUpdateCall) Fields ¶
func (c *ManagementWebpropertyUserLinksUpdateCall) Fields(s ...googleapi.Field) *ManagementWebpropertyUserLinksUpdateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ManagementWebpropertyUserLinksUpdateCall) Header ¶
func (c *ManagementWebpropertyUserLinksUpdateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type McfData ¶
type McfData struct {
	// ColumnHeaders: Column headers that list dimension names followed by the
	// metric names. The order of dimensions and metrics is same as specified in
	// the request.
	ColumnHeaders []*McfDataColumnHeaders `json:"columnHeaders,omitempty"`
	// ContainsSampledData: Determines if the Analytics data contains sampled data.
	ContainsSampledData bool `json:"containsSampledData,omitempty"`
	// Id: Unique ID for this data response.
	Id string `json:"id,omitempty"`
	// ItemsPerPage: The maximum number of rows the response can contain,
	// regardless of the actual number of rows returned. Its value ranges from 1 to
	// 10,000 with a value of 1000 by default, or otherwise specified by the
	// max-results query parameter.
	ItemsPerPage int64 `json:"itemsPerPage,omitempty"`
	// Kind: Resource type.
	Kind string `json:"kind,omitempty"`
	// NextLink: Link to next page for this Analytics data query.
	NextLink string `json:"nextLink,omitempty"`
	// PreviousLink: Link to previous page for this Analytics data query.
	PreviousLink string `json:"previousLink,omitempty"`
	// ProfileInfo: Information for the view (profile), for which the Analytics
	// data was requested.
	ProfileInfo *McfDataProfileInfo `json:"profileInfo,omitempty"`
	// Query: Analytics data request query parameters.
	Query *McfDataQuery `json:"query,omitempty"`
	// Rows: Analytics data rows, where each row contains a list of dimension
	// values followed by the metric values. The order of dimensions and metrics is
	// same as specified in the request.
	Rows [][]*McfDataRowsItem `json:"rows,omitempty"`
	// SampleSize: The number of samples used to calculate the result.
	SampleSize int64 `json:"sampleSize,omitempty,string"`
	// SampleSpace: Total size of the sample space from which the samples were
	// selected.
	SampleSpace int64 `json:"sampleSpace,omitempty,string"`
	// SelfLink: Link to this page.
	SelfLink string `json:"selfLink,omitempty"`
	// TotalResults: The total number of rows for the query, regardless of the
	// number of rows in the response.
	TotalResults int64 `json:"totalResults,omitempty"`
	// TotalsForAllResults: Total values for the requested metrics over all the
	// results, not just the results returned in this response. The order of the
	// metric totals is same as the metric order specified in the request.
	TotalsForAllResults map[string]string `json:"totalsForAllResults,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ColumnHeaders") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ColumnHeaders") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

McfData: Multi-Channel Funnels data for a given view (profile).

func (McfData) MarshalJSON ¶
func (s McfData) MarshalJSON() ([]byte, error)
type McfDataColumnHeaders ¶
type McfDataColumnHeaders struct {
	// ColumnType: Column Type. Either DIMENSION or METRIC.
	ColumnType string `json:"columnType,omitempty"`
	// DataType: Data type. Dimension and metric values data types such as INTEGER,
	// DOUBLE, CURRENCY, MCF_SEQUENCE etc.
	DataType string `json:"dataType,omitempty"`
	// Name: Column name.
	Name string `json:"name,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ColumnType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ColumnType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (McfDataColumnHeaders) MarshalJSON ¶
func (s McfDataColumnHeaders) MarshalJSON() ([]byte, error)
type McfDataProfileInfo ¶
type McfDataProfileInfo struct {
	// AccountId: Account ID to which this view (profile) belongs.
	AccountId string `json:"accountId,omitempty"`
	// InternalWebPropertyId: Internal ID for the web property to which this view
	// (profile) belongs.
	InternalWebPropertyId string `json:"internalWebPropertyId,omitempty"`
	// ProfileId: View (Profile) ID.
	ProfileId string `json:"profileId,omitempty"`
	// ProfileName: View (Profile) name.
	ProfileName string `json:"profileName,omitempty"`
	// TableId: Table ID for view (profile).
	TableId string `json:"tableId,omitempty"`
	// WebPropertyId: Web Property ID to which this view (profile) belongs.
	WebPropertyId string `json:"webPropertyId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AccountId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccountId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

McfDataProfileInfo: Information for the view (profile), for which the Analytics data was requested.

func (McfDataProfileInfo) MarshalJSON ¶
func (s McfDataProfileInfo) MarshalJSON() ([]byte, error)
type McfDataQuery ¶
type McfDataQuery struct {
	// Dimensions: List of analytics dimensions.
	Dimensions string `json:"dimensions,omitempty"`
	// EndDate: End date.
	EndDate string `json:"end-date,omitempty"`
	// Filters: Comma-separated list of dimension or metric filters.
	Filters string `json:"filters,omitempty"`
	// Ids: Unique table ID.
	Ids string `json:"ids,omitempty"`
	// MaxResults: Maximum results per page.
	MaxResults int64 `json:"max-results,omitempty"`
	// Metrics: List of analytics metrics.
	Metrics []string `json:"metrics,omitempty"`
	// SamplingLevel: Desired sampling level
	SamplingLevel string `json:"samplingLevel,omitempty"`
	// Segment: Analytics advanced segment.
	Segment string `json:"segment,omitempty"`
	// Sort: List of dimensions or metrics based on which Analytics data is sorted.
	Sort []string `json:"sort,omitempty"`
	// StartDate: Start date.
	StartDate string `json:"start-date,omitempty"`
	// StartIndex: Start index.
	StartIndex int64 `json:"start-index,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Dimensions") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Dimensions") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

McfDataQuery: Analytics data request query parameters.

func (McfDataQuery) MarshalJSON ¶
func (s McfDataQuery) MarshalJSON() ([]byte, error)
type McfDataRowsItem ¶
type McfDataRowsItem struct {
	// ConversionPathValue: A conversion path dimension value, containing a list of
	// interactions with their attributes.
	ConversionPathValue []*McfDataRowsItemConversionPathValue `json:"conversionPathValue,omitempty"`
	// PrimitiveValue: A primitive dimension value. A primitive metric value.
	PrimitiveValue string `json:"primitiveValue,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ConversionPathValue") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ConversionPathValue") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

McfDataRowsItem: A union object representing a dimension or metric value. Only one of "primitiveValue" or "conversionPathValue" attribute will be populated.

func (McfDataRowsItem) MarshalJSON ¶
func (s McfDataRowsItem) MarshalJSON() ([]byte, error)
type McfDataRowsItemConversionPathValue ¶
type McfDataRowsItemConversionPathValue struct {
	// InteractionType: Type of an interaction on conversion path. Such as CLICK,
	// IMPRESSION etc.
	InteractionType string `json:"interactionType,omitempty"`
	// NodeValue: Node value of an interaction on conversion path. Such as source,
	// medium etc.
	NodeValue string `json:"nodeValue,omitempty"`
	// ForceSendFields is a list of field names (e.g. "InteractionType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "InteractionType") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (McfDataRowsItemConversionPathValue) MarshalJSON ¶
func (s McfDataRowsItemConversionPathValue) MarshalJSON() ([]byte, error)
type MetadataColumnsListCall ¶
type MetadataColumnsListCall struct {
	// contains filtered or unexported fields
}
func (*MetadataColumnsListCall) Context ¶
func (c *MetadataColumnsListCall) Context(ctx context.Context) *MetadataColumnsListCall

Context sets the context to be used in this call's Do method.

func (*MetadataColumnsListCall) Do ¶
func (c *MetadataColumnsListCall) Do(opts ...googleapi.CallOption) (*Columns, error)

Do executes the "analytics.metadata.columns.list" call. Any non-2xx status code is an error. Response headers are in either *Columns.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MetadataColumnsListCall) Fields ¶
func (c *MetadataColumnsListCall) Fields(s ...googleapi.Field) *MetadataColumnsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*MetadataColumnsListCall) Header ¶
func (c *MetadataColumnsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*MetadataColumnsListCall) IfNoneMatch ¶
func (c *MetadataColumnsListCall) IfNoneMatch(entityTag string) *MetadataColumnsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type MetadataColumnsService ¶
type MetadataColumnsService struct {
	// contains filtered or unexported fields
}
func NewMetadataColumnsService ¶
func NewMetadataColumnsService(s *Service) *MetadataColumnsService
func (*MetadataColumnsService) List ¶
func (r *MetadataColumnsService) List(reportType string) *MetadataColumnsListCall

List: Lists all columns for a report type

reportType: Report type. Allowed Values: 'ga'. Where 'ga' corresponds to the Core Reporting API.
type MetadataService ¶
type MetadataService struct {
	Columns *MetadataColumnsService
	// contains filtered or unexported fields
}
func NewMetadataService ¶
func NewMetadataService(s *Service) *MetadataService
type Profile ¶
type Profile struct {
	// AccountId: Account ID to which this view (profile) belongs.
	AccountId string `json:"accountId,omitempty"`
	// BotFilteringEnabled: Indicates whether bot filtering is enabled for this
	// view (profile).
	BotFilteringEnabled bool `json:"botFilteringEnabled,omitempty"`
	// ChildLink: Child link for this view (profile). Points to the list of goals
	// for this view (profile).
	ChildLink *ProfileChildLink `json:"childLink,omitempty"`
	// Created: Time this view (profile) was created.
	Created string `json:"created,omitempty"`
	// Currency: The currency type associated with this view (profile), defaults to
	// USD. The supported values are:
	// USD, JPY, EUR, GBP, AUD, KRW, BRL, CNY, DKK, RUB, SEK, NOK, PLN, TRY, TWD,
	// HKD, THB, IDR, ARS, MXN, VND, PHP, INR, CHF, CAD, CZK, NZD, HUF, BGN, LTL,
	// ZAR, UAH, AED, BOB, CLP, COP, EGP, HRK, ILS, MAD, MYR, PEN, PKR, RON, RSD,
	// SAR, SGD, VEF, LVL
	Currency string `json:"currency,omitempty"`
	// DefaultPage: Default page for this view (profile).
	DefaultPage string `json:"defaultPage,omitempty"`
	// ECommerceTracking: Indicates whether ecommerce tracking is enabled for this
	// view (profile).
	ECommerceTracking bool `json:"eCommerceTracking,omitempty"`
	// EnhancedECommerceTracking: Indicates whether enhanced ecommerce tracking is
	// enabled for this view (profile). This property can only be enabled if
	// ecommerce tracking is enabled.
	EnhancedECommerceTracking bool `json:"enhancedECommerceTracking,omitempty"`
	// ExcludeQueryParameters: The query parameters that are excluded from this
	// view (profile).
	ExcludeQueryParameters string `json:"excludeQueryParameters,omitempty"`
	// Id: View (Profile) ID.
	Id string `json:"id,omitempty"`
	// InternalWebPropertyId: Internal ID for the web property to which this view
	// (profile) belongs.
	InternalWebPropertyId string `json:"internalWebPropertyId,omitempty"`
	// Kind: Resource type for Analytics view (profile).
	Kind string `json:"kind,omitempty"`
	// Name: Name of this view (profile).
	Name string `json:"name,omitempty"`
	// ParentLink: Parent link for this view (profile). Points to the web property
	// to which this view (profile) belongs.
	ParentLink *ProfileParentLink `json:"parentLink,omitempty"`
	// Permissions: Permissions the user has for this view (profile).
	Permissions *ProfilePermissions `json:"permissions,omitempty"`
	// SelfLink: Link for this view (profile).
	SelfLink string `json:"selfLink,omitempty"`
	// SiteSearchCategoryParameters: Site search category parameters for this view
	// (profile).
	SiteSearchCategoryParameters string `json:"siteSearchCategoryParameters,omitempty"`
	// SiteSearchQueryParameters: The site search query parameters for this view
	// (profile).
	SiteSearchQueryParameters string `json:"siteSearchQueryParameters,omitempty"`
	// Starred: Indicates whether this view (profile) is starred or not.
	Starred bool `json:"starred,omitempty"`
	// StripSiteSearchCategoryParameters: Whether or not Analytics will strip
	// search category parameters from the URLs in your reports.
	StripSiteSearchCategoryParameters bool `json:"stripSiteSearchCategoryParameters,omitempty"`
	// StripSiteSearchQueryParameters: Whether or not Analytics will strip search
	// query parameters from the URLs in your reports.
	StripSiteSearchQueryParameters bool `json:"stripSiteSearchQueryParameters,omitempty"`
	// Timezone: Time zone for which this view (profile) has been configured. Time
	// zones are identified by strings from the TZ database.
	Timezone string `json:"timezone,omitempty"`
	// Type: View (Profile) type. Supported types: WEB or APP.
	Type string `json:"type,omitempty"`
	// Updated: Time this view (profile) was last modified.
	Updated string `json:"updated,omitempty"`
	// WebPropertyId: Web property ID of the form UA-XXXXX-YY to which this view
	// (profile) belongs.
	WebPropertyId string `json:"webPropertyId,omitempty"`
	// WebsiteUrl: Website URL for this view (profile).
	WebsiteUrl string `json:"websiteUrl,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AccountId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccountId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Profile: JSON template for an Analytics view (profile).

func (Profile) MarshalJSON ¶
func (s Profile) MarshalJSON() ([]byte, error)
type ProfileChildLink ¶
type ProfileChildLink struct {
	// Href: Link to the list of goals for this view (profile).
	Href string `json:"href,omitempty"`
	// Type: Value is "analytics#goals".
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Href") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Href") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ProfileChildLink: Child link for this view (profile). Points to the list of goals for this view (profile).

func (ProfileChildLink) MarshalJSON ¶
func (s ProfileChildLink) MarshalJSON() ([]byte, error)
type ProfileFilterLink ¶
type ProfileFilterLink struct {
	// FilterRef: Filter for this link.
	FilterRef *FilterRef `json:"filterRef,omitempty"`
	// Id: Profile filter link ID.
	Id string `json:"id,omitempty"`
	// Kind: Resource type for Analytics filter.
	Kind string `json:"kind,omitempty"`
	// ProfileRef: View (Profile) for this link.
	ProfileRef *ProfileRef `json:"profileRef,omitempty"`
	// Rank: The rank of this profile filter link relative to the other filters
	// linked to the same profile.
	// For readonly (i.e., list and get) operations, the rank always starts at
	// 1.
	// For write (i.e., create, update, or delete) operations, you may specify a
	// value between 0 and 255 inclusively, [0, 255]. In order to insert a link at
	// the end of the list, either don't specify a rank or set a rank to a number
	// greater than the largest rank in the list. In order to insert a link to the
	// beginning of the list specify a rank that is less than or equal to 1. The
	// new link will move all existing filters with the same or lower rank down the
	// list. After the link is inserted/updated/deleted all profile filter links
	// will be renumbered starting at 1.
	Rank int64 `json:"rank,omitempty"`
	// SelfLink: Link for this profile filter link.
	SelfLink string `json:"selfLink,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "FilterRef") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "FilterRef") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ProfileFilterLink: JSON template for an Analytics profile filter link.

func (ProfileFilterLink) MarshalJSON ¶
func (s ProfileFilterLink) MarshalJSON() ([]byte, error)
type ProfileFilterLinks ¶
type ProfileFilterLinks struct {
	// Items: A list of profile filter links.
	Items []*ProfileFilterLink `json:"items,omitempty"`
	// ItemsPerPage: The maximum number of resources the response can contain,
	// regardless of the actual number of resources returned. Its value ranges from
	// 1 to 1,000 with a value of 1000 by default, or otherwise specified by the
	// max-results query parameter.
	ItemsPerPage int64 `json:"itemsPerPage,omitempty"`
	// Kind: Collection type.
	Kind string `json:"kind,omitempty"`
	// NextLink: Link to next page for this profile filter link collection.
	NextLink string `json:"nextLink,omitempty"`
	// PreviousLink: Link to previous page for this profile filter link collection.
	PreviousLink string `json:"previousLink,omitempty"`
	// StartIndex: The starting index of the resources, which is 1 by default or
	// otherwise specified by the start-index query parameter.
	StartIndex int64 `json:"startIndex,omitempty"`
	// TotalResults: The total number of results for the query, regardless of the
	// number of results in the response.
	TotalResults int64 `json:"totalResults,omitempty"`
	// Username: Email ID of the authenticated user
	Username string `json:"username,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Items") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Items") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ProfileFilterLinks: A profile filter link collection lists profile filter links between profiles and filters. Each resource in the collection corresponds to a profile filter link.

func (ProfileFilterLinks) MarshalJSON ¶
func (s ProfileFilterLinks) MarshalJSON() ([]byte, error)
type ProfileParentLink ¶
type ProfileParentLink struct {
	// Href: Link to the web property to which this view (profile) belongs.
	Href string `json:"href,omitempty"`
	// Type: Value is "analytics#webproperty".
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Href") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Href") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ProfileParentLink: Parent link for this view (profile). Points to the web property to which this view (profile) belongs.

func (ProfileParentLink) MarshalJSON ¶
func (s ProfileParentLink) MarshalJSON() ([]byte, error)
type ProfilePermissions ¶
type ProfilePermissions struct {
	// Effective: All the permissions that the user has for this view (profile).
	// These include any implied permissions (e.g., EDIT implies VIEW) or inherited
	// permissions from the parent web property.
	Effective []string `json:"effective,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Effective") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Effective") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ProfilePermissions: Permissions the user has for this view (profile).

func (ProfilePermissions) MarshalJSON ¶
func (s ProfilePermissions) MarshalJSON() ([]byte, error)
type ProfileRef ¶
type ProfileRef struct {
	// AccountId: Account ID to which this view (profile) belongs.
	AccountId string `json:"accountId,omitempty"`
	// Href: Link for this view (profile).
	Href string `json:"href,omitempty"`
	// Id: View (Profile) ID.
	Id string `json:"id,omitempty"`
	// InternalWebPropertyId: Internal ID for the web property to which this view
	// (profile) belongs.
	InternalWebPropertyId string `json:"internalWebPropertyId,omitempty"`
	// Kind: Analytics view (profile) reference.
	Kind string `json:"kind,omitempty"`
	// Name: Name of this view (profile).
	Name string `json:"name,omitempty"`
	// WebPropertyId: Web property ID of the form UA-XXXXX-YY to which this view
	// (profile) belongs.
	WebPropertyId string `json:"webPropertyId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AccountId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccountId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ProfileRef: JSON template for a linked view (profile).

func (ProfileRef) MarshalJSON ¶
func (s ProfileRef) MarshalJSON() ([]byte, error)
type ProfileSummary ¶
type ProfileSummary struct {
	// Id: View (profile) ID.
	Id string `json:"id,omitempty"`
	// Kind: Resource type for Analytics ProfileSummary.
	Kind string `json:"kind,omitempty"`
	// Name: View (profile) name.
	Name string `json:"name,omitempty"`
	// Starred: Indicates whether this view (profile) is starred or not.
	Starred bool `json:"starred,omitempty"`
	// Type: View (Profile) type. Supported types: WEB or APP.
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Id") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Id") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ProfileSummary: JSON template for an Analytics ProfileSummary. ProfileSummary returns basic information (i.e., summary) for a profile.

func (ProfileSummary) MarshalJSON ¶
func (s ProfileSummary) MarshalJSON() ([]byte, error)
type Profiles ¶
type Profiles struct {
	// Items: A list of views (profiles).
	Items []*Profile `json:"items,omitempty"`
	// ItemsPerPage: The maximum number of resources the response can contain,
	// regardless of the actual number of resources returned. Its value ranges from
	// 1 to 1000 with a value of 1000 by default, or otherwise specified by the
	// max-results query parameter.
	ItemsPerPage int64 `json:"itemsPerPage,omitempty"`
	// Kind: Collection type.
	Kind string `json:"kind,omitempty"`
	// NextLink: Link to next page for this view (profile) collection.
	NextLink string `json:"nextLink,omitempty"`
	// PreviousLink: Link to previous page for this view (profile) collection.
	PreviousLink string `json:"previousLink,omitempty"`
	// StartIndex: The starting index of the resources, which is 1 by default or
	// otherwise specified by the start-index query parameter.
	StartIndex int64 `json:"startIndex,omitempty"`
	// TotalResults: The total number of results for the query, regardless of the
	// number of results in the response.
	TotalResults int64 `json:"totalResults,omitempty"`
	// Username: Email ID of the authenticated user
	Username string `json:"username,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Items") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Items") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Profiles: A view (profile) collection lists Analytics views (profiles) to which the user has access. Each resource in the collection corresponds to a single Analytics view (profile).

func (Profiles) MarshalJSON ¶
func (s Profiles) MarshalJSON() ([]byte, error)
type ProvisioningCreateAccountTicketCall ¶
type ProvisioningCreateAccountTicketCall struct {
	// contains filtered or unexported fields
}
func (*ProvisioningCreateAccountTicketCall) Context ¶
func (c *ProvisioningCreateAccountTicketCall) Context(ctx context.Context) *ProvisioningCreateAccountTicketCall

Context sets the context to be used in this call's Do method.

func (*ProvisioningCreateAccountTicketCall) Do ¶
func (c *ProvisioningCreateAccountTicketCall) Do(opts ...googleapi.CallOption) (*AccountTicket, error)

Do executes the "analytics.provisioning.createAccountTicket" call. Any non-2xx status code is an error. Response headers are in either *AccountTicket.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProvisioningCreateAccountTicketCall) Fields ¶
func (c *ProvisioningCreateAccountTicketCall) Fields(s ...googleapi.Field) *ProvisioningCreateAccountTicketCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProvisioningCreateAccountTicketCall) Header ¶
func (c *ProvisioningCreateAccountTicketCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProvisioningCreateAccountTreeCall ¶
type ProvisioningCreateAccountTreeCall struct {
	// contains filtered or unexported fields
}
func (*ProvisioningCreateAccountTreeCall) Context ¶
func (c *ProvisioningCreateAccountTreeCall) Context(ctx context.Context) *ProvisioningCreateAccountTreeCall

Context sets the context to be used in this call's Do method.

func (*ProvisioningCreateAccountTreeCall) Do ¶
func (c *ProvisioningCreateAccountTreeCall) Do(opts ...googleapi.CallOption) (*AccountTreeResponse, error)

Do executes the "analytics.provisioning.createAccountTree" call. Any non-2xx status code is an error. Response headers are in either *AccountTreeResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProvisioningCreateAccountTreeCall) Fields ¶
func (c *ProvisioningCreateAccountTreeCall) Fields(s ...googleapi.Field) *ProvisioningCreateAccountTreeCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProvisioningCreateAccountTreeCall) Header ¶
func (c *ProvisioningCreateAccountTreeCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProvisioningService ¶
type ProvisioningService struct {
	// contains filtered or unexported fields
}
func NewProvisioningService ¶
func NewProvisioningService(s *Service) *ProvisioningService
func (*ProvisioningService) CreateAccountTicket ¶
func (r *ProvisioningService) CreateAccountTicket(accountticket *AccountTicket) *ProvisioningCreateAccountTicketCall

CreateAccountTicket: Creates an account ticket.

func (*ProvisioningService) CreateAccountTree ¶
func (r *ProvisioningService) CreateAccountTree(accounttreerequest *AccountTreeRequest) *ProvisioningCreateAccountTreeCall

CreateAccountTree: Provision account.

type RealtimeData ¶
type RealtimeData struct {
	// ColumnHeaders: Column headers that list dimension names followed by the
	// metric names. The order of dimensions and metrics is same as specified in
	// the request.
	ColumnHeaders []*RealtimeDataColumnHeaders `json:"columnHeaders,omitempty"`
	// Id: Unique ID for this data response.
	Id string `json:"id,omitempty"`
	// Kind: Resource type.
	Kind string `json:"kind,omitempty"`
	// ProfileInfo: Information for the view (profile), for which the real time
	// data was requested.
	ProfileInfo *RealtimeDataProfileInfo `json:"profileInfo,omitempty"`
	// Query: Real time data request query parameters.
	Query *RealtimeDataQuery `json:"query,omitempty"`
	// Rows: Real time data rows, where each row contains a list of dimension
	// values followed by the metric values. The order of dimensions and metrics is
	// same as specified in the request.
	Rows [][]string `json:"rows,omitempty"`
	// SelfLink: Link to this page.
	SelfLink string `json:"selfLink,omitempty"`
	// TotalResults: The total number of rows for the query, regardless of the
	// number of rows in the response.
	TotalResults int64 `json:"totalResults,omitempty"`
	// TotalsForAllResults: Total values for the requested metrics over all the
	// results, not just the results returned in this response. The order of the
	// metric totals is same as the metric order specified in the request.
	TotalsForAllResults map[string]string `json:"totalsForAllResults,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ColumnHeaders") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ColumnHeaders") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RealtimeData: Real time data for a given view (profile).

func (RealtimeData) MarshalJSON ¶
func (s RealtimeData) MarshalJSON() ([]byte, error)
type RealtimeDataColumnHeaders ¶
type RealtimeDataColumnHeaders struct {
	// ColumnType: Column Type. Either DIMENSION or METRIC.
	ColumnType string `json:"columnType,omitempty"`
	// DataType: Data type. Dimension column headers have only STRING as the data
	// type. Metric column headers have data types for metric values such as
	// INTEGER, DOUBLE, CURRENCY etc.
	DataType string `json:"dataType,omitempty"`
	// Name: Column name.
	Name string `json:"name,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ColumnType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ColumnType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}
func (RealtimeDataColumnHeaders) MarshalJSON ¶
func (s RealtimeDataColumnHeaders) MarshalJSON() ([]byte, error)
type RealtimeDataProfileInfo ¶
type RealtimeDataProfileInfo struct {
	// AccountId: Account ID to which this view (profile) belongs.
	AccountId string `json:"accountId,omitempty"`
	// InternalWebPropertyId: Internal ID for the web property to which this view
	// (profile) belongs.
	InternalWebPropertyId string `json:"internalWebPropertyId,omitempty"`
	// ProfileId: View (Profile) ID.
	ProfileId string `json:"profileId,omitempty"`
	// ProfileName: View (Profile) name.
	ProfileName string `json:"profileName,omitempty"`
	// TableId: Table ID for view (profile).
	TableId string `json:"tableId,omitempty"`
	// WebPropertyId: Web Property ID to which this view (profile) belongs.
	WebPropertyId string `json:"webPropertyId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AccountId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccountId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RealtimeDataProfileInfo: Information for the view (profile), for which the real time data was requested.

func (RealtimeDataProfileInfo) MarshalJSON ¶
func (s RealtimeDataProfileInfo) MarshalJSON() ([]byte, error)
type RealtimeDataQuery ¶
type RealtimeDataQuery struct {
	// Dimensions: List of real time dimensions.
	Dimensions string `json:"dimensions,omitempty"`
	// Filters: Comma-separated list of dimension or metric filters.
	Filters string `json:"filters,omitempty"`
	// Ids: Unique table ID.
	Ids string `json:"ids,omitempty"`
	// MaxResults: Maximum results per page.
	MaxResults int64 `json:"max-results,omitempty"`
	// Metrics: List of real time metrics.
	Metrics []string `json:"metrics,omitempty"`
	// Sort: List of dimensions or metrics based on which real time data is sorted.
	Sort []string `json:"sort,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Dimensions") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Dimensions") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RealtimeDataQuery: Real time data request query parameters.

func (RealtimeDataQuery) MarshalJSON ¶
func (s RealtimeDataQuery) MarshalJSON() ([]byte, error)
type RemarketingAudience ¶
type RemarketingAudience struct {
	// AccountId: Account ID to which this remarketing audience belongs.
	AccountId string `json:"accountId,omitempty"`
	// AudienceDefinition: The simple audience definition that will cause a user to
	// be added to an audience.
	AudienceDefinition *RemarketingAudienceAudienceDefinition `json:"audienceDefinition,omitempty"`
	// AudienceType: The type of audience, either SIMPLE or STATE_BASED.
	AudienceType string `json:"audienceType,omitempty"`
	// Created: Time this remarketing audience was created.
	Created string `json:"created,omitempty"`
	// Description: The description of this remarketing audience.
	Description string `json:"description,omitempty"`
	// Id: Remarketing Audience ID.
	Id string `json:"id,omitempty"`
	// InternalWebPropertyId: Internal ID for the web property to which this
	// remarketing audience belongs.
	InternalWebPropertyId string `json:"internalWebPropertyId,omitempty"`
	// Kind: Collection type.
	Kind string `json:"kind,omitempty"`
	// LinkedAdAccounts: The linked ad accounts associated with this remarketing
	// audience. A remarketing audience can have only one linkedAdAccount
	// currently.
	LinkedAdAccounts []*LinkedForeignAccount `json:"linkedAdAccounts,omitempty"`
	// LinkedViews: The views (profiles) that this remarketing audience is linked
	// to.
	LinkedViews []string `json:"linkedViews,omitempty"`
	// Name: The name of this remarketing audience.
	Name string `json:"name,omitempty"`
	// StateBasedAudienceDefinition: A state based audience definition that will
	// cause a user to be added or removed from an audience.
	StateBasedAudienceDefinition *RemarketingAudienceStateBasedAudienceDefinition `json:"stateBasedAudienceDefinition,omitempty"`
	// Updated: Time this remarketing audience was last modified.
	Updated string `json:"updated,omitempty"`
	// WebPropertyId: Web property ID of the form UA-XXXXX-YY to which this
	// remarketing audience belongs.
	WebPropertyId string `json:"webPropertyId,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AccountId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccountId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RemarketingAudience: JSON template for an Analytics remarketing audience.

func (RemarketingAudience) MarshalJSON ¶
func (s RemarketingAudience) MarshalJSON() ([]byte, error)
type RemarketingAudienceAudienceDefinition ¶
type RemarketingAudienceAudienceDefinition struct {
	// IncludeConditions: Defines the conditions to include users to the audience.
	IncludeConditions *IncludeConditions `json:"includeConditions,omitempty"`
	// ForceSendFields is a list of field names (e.g. "IncludeConditions") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "IncludeConditions") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RemarketingAudienceAudienceDefinition: The simple audience definition that will cause a user to be added to an audience.

func (RemarketingAudienceAudienceDefinition) MarshalJSON ¶
func (s RemarketingAudienceAudienceDefinition) MarshalJSON() ([]byte, error)
type RemarketingAudienceStateBasedAudienceDefinition ¶
type RemarketingAudienceStateBasedAudienceDefinition struct {
	// ExcludeConditions: Defines the conditions to exclude users from the
	// audience.
	ExcludeConditions *RemarketingAudienceStateBasedAudienceDefinitionExcludeConditions `json:"excludeConditions,omitempty"`
	// IncludeConditions: Defines the conditions to include users to the audience.
	IncludeConditions *IncludeConditions `json:"includeConditions,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ExcludeConditions") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExcludeConditions") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RemarketingAudienceStateBasedAudienceDefinition: A state based audience definition that will cause a user to be added or removed from an audience.

func (RemarketingAudienceStateBasedAudienceDefinition) MarshalJSON ¶
func (s RemarketingAudienceStateBasedAudienceDefinition) MarshalJSON() ([]byte, error)
type RemarketingAudienceStateBasedAudienceDefinitionExcludeConditions ¶
type RemarketingAudienceStateBasedAudienceDefinitionExcludeConditions struct {
	// ExclusionDuration: Whether to make the exclusion TEMPORARY or PERMANENT.
	ExclusionDuration string `json:"exclusionDuration,omitempty"`
	// Segment: The segment condition that will cause a user to be removed from an
	// audience.
	Segment string `json:"segment,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ExclusionDuration") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExclusionDuration") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RemarketingAudienceStateBasedAudienceDefinitionExcludeConditions: Defines the conditions to exclude users from the audience.

func (RemarketingAudienceStateBasedAudienceDefinitionExcludeConditions) MarshalJSON ¶
func (s RemarketingAudienceStateBasedAudienceDefinitionExcludeConditions) MarshalJSON() ([]byte, error)
type RemarketingAudiences ¶
type RemarketingAudiences struct {
	// Items: A list of remarketing audiences.
	Items []*RemarketingAudience `json:"items,omitempty"`
	// ItemsPerPage: The maximum number of resources the response can contain,
	// regardless of the actual number of resources returned. Its value ranges from
	// 1 to 1000 with a value of 1000 by default, or otherwise specified by the
	// max-results query parameter.
	ItemsPerPage int64 `json:"itemsPerPage,omitempty"`
	// Kind: Collection type.
	Kind string `json:"kind,omitempty"`
	// NextLink: Link to next page for this remarketing audience collection.
	NextLink string `json:"nextLink,omitempty"`
	// PreviousLink: Link to previous page for this view (profile) collection.
	PreviousLink string `json:"previousLink,omitempty"`
	// StartIndex: The starting index of the resources, which is 1 by default or
	// otherwise specified by the start-index query parameter.
	StartIndex int64 `json:"startIndex,omitempty"`
	// TotalResults: The total number of results for the query, regardless of the
	// number of results in the response.
	TotalResults int64 `json:"totalResults,omitempty"`
	// Username: Email ID of the authenticated user
	Username string `json:"username,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Items") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Items") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

RemarketingAudiences: A remarketing audience collection lists Analytics remarketing audiences to which the user has access. Each resource in the collection corresponds to a single Analytics remarketing audience.

func (RemarketingAudiences) MarshalJSON ¶
func (s RemarketingAudiences) MarshalJSON() ([]byte, error)
type Segment ¶
type Segment struct {
	// Created: Time the segment was created.
	Created string `json:"created,omitempty"`
	// Definition: Segment definition.
	Definition string `json:"definition,omitempty"`
	// Id: Segment ID.
	Id string `json:"id,omitempty"`
	// Kind: Resource type for Analytics segment.
	Kind string `json:"kind,omitempty"`
	// Name: Segment name.
	Name string `json:"name,omitempty"`
	// SegmentId: Segment ID. Can be used with the 'segment' parameter in Core
	// Reporting API.
	SegmentId string `json:"segmentId,omitempty"`
	// SelfLink: Link for this segment.
	SelfLink string `json:"selfLink,omitempty"`
	// Type: Type for a segment. Possible values are "BUILT_IN" or "CUSTOM".
	Type string `json:"type,omitempty"`
	// Updated: Time the segment was last modified.
	Updated string `json:"updated,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Created") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Created") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Segment: JSON template for an Analytics segment.

func (Segment) MarshalJSON ¶
func (s Segment) MarshalJSON() ([]byte, error)
type Segments ¶
type Segments struct {
	// Items: A list of segments.
	Items []*Segment `json:"items,omitempty"`
	// ItemsPerPage: The maximum number of resources the response can contain,
	// regardless of the actual number of resources returned. Its value ranges from
	// 1 to 1000 with a value of 1000 by default, or otherwise specified by the
	// max-results query parameter.
	ItemsPerPage int64 `json:"itemsPerPage,omitempty"`
	// Kind: Collection type for segments.
	Kind string `json:"kind,omitempty"`
	// NextLink: Link to next page for this segment collection.
	NextLink string `json:"nextLink,omitempty"`
	// PreviousLink: Link to previous page for this segment collection.
	PreviousLink string `json:"previousLink,omitempty"`
	// StartIndex: The starting index of the resources, which is 1 by default or
	// otherwise specified by the start-index query parameter.
	StartIndex int64 `json:"startIndex,omitempty"`
	// TotalResults: The total number of results for the query, regardless of the
	// number of results in the response.
	TotalResults int64 `json:"totalResults,omitempty"`
	// Username: Email ID of the authenticated user
	Username string `json:"username,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Items") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Items") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Segments: An segment collection lists Analytics segments that the user has access to. Each resource in the collection corresponds to a single Analytics segment.

func (Segments) MarshalJSON ¶
func (s Segments) MarshalJSON() ([]byte, error)
type Service ¶
type Service struct {
	BasePath  string // API endpoint base URL
	UserAgent string // optional additional User-Agent fragment

	Data *DataService

	Management *ManagementService

	Metadata *MetadataService

	Provisioning *ProvisioningService

	UserDeletion *UserDeletionService
	// contains filtered or unexported fields
}
func
New
DEPRECATED
func NewService ¶
added in v0.3.0
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)

NewService creates a new Service.

type UnsampledReport ¶
type UnsampledReport struct {
	// AccountId: Account ID to which this unsampled report belongs.
	AccountId string `json:"accountId,omitempty"`
	// CloudStorageDownloadDetails: Download details for a file stored in Google
	// Cloud Storage.
	CloudStorageDownloadDetails *UnsampledReportCloudStorageDownloadDetails `json:"cloudStorageDownloadDetails,omitempty"`
	// Created: Time this unsampled report was created.
	Created string `json:"created,omitempty"`
	// Dimensions: The dimensions for the unsampled report.
	Dimensions string `json:"dimensions,omitempty"`
	// DownloadType: The type of download you need to use for the report data file.
	// Possible values include `GOOGLE_DRIVE` and `GOOGLE_CLOUD_STORAGE`. If the
	// value is `GOOGLE_DRIVE`, see the `driveDownloadDetails` field. If the value
	// is `GOOGLE_CLOUD_STORAGE`, see the `cloudStorageDownloadDetails` field.
	DownloadType string `json:"downloadType,omitempty"`
	// DriveDownloadDetails: Download details for a file stored in Google Drive.
	DriveDownloadDetails *UnsampledReportDriveDownloadDetails `json:"driveDownloadDetails,omitempty"`
	// EndDate: The end date for the unsampled report.
	EndDate string `json:"end-date,omitempty"`
	// Filters: The filters for the unsampled report.
	Filters string `json:"filters,omitempty"`
	// Id: Unsampled report ID.
	Id string `json:"id,omitempty"`
	// Kind: Resource type for an Analytics unsampled report.
	Kind string `json:"kind,omitempty"`
	// Metrics: The metrics for the unsampled report.
	Metrics string `json:"metrics,omitempty"`
	// ProfileId: View (Profile) ID to which this unsampled report belongs.
	ProfileId string `json:"profileId,omitempty"`
	// Segment: The segment for the unsampled report.
	Segment string `json:"segment,omitempty"`
	// SelfLink: Link for this unsampled report.
	SelfLink string `json:"selfLink,omitempty"`
	// StartDate: The start date for the unsampled report.
	StartDate string `json:"start-date,omitempty"`
	// Status: Status of this unsampled report. Possible values are PENDING,
	// COMPLETED, or FAILED.
	Status string `json:"status,omitempty"`
	// Title: Title of the unsampled report.
	Title string `json:"title,omitempty"`
	// Updated: Time this unsampled report was last modified.
	Updated string `json:"updated,omitempty"`
	// WebPropertyId: Web property ID to which this unsampled report belongs. The
	// web property ID is of the form UA-XXXXX-YY.
	WebPropertyId string `json:"webPropertyId,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AccountId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccountId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UnsampledReport: JSON template for Analytics unsampled report resource.

func (UnsampledReport) MarshalJSON ¶
func (s UnsampledReport) MarshalJSON() ([]byte, error)
type UnsampledReportCloudStorageDownloadDetails ¶
type UnsampledReportCloudStorageDownloadDetails struct {
	// BucketId: Id of the bucket the file object is stored in.
	BucketId string `json:"bucketId,omitempty"`
	// ObjectId: Id of the file object containing the report data.
	ObjectId string `json:"objectId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BucketId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BucketId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UnsampledReportCloudStorageDownloadDetails: Download details for a file stored in Google Cloud Storage.

func (UnsampledReportCloudStorageDownloadDetails) MarshalJSON ¶
func (s UnsampledReportCloudStorageDownloadDetails) MarshalJSON() ([]byte, error)
type UnsampledReportDriveDownloadDetails ¶
type UnsampledReportDriveDownloadDetails struct {
	// DocumentId: Id of the document/file containing the report data.
	DocumentId string `json:"documentId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DocumentId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DocumentId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UnsampledReportDriveDownloadDetails: Download details for a file stored in Google Drive.

func (UnsampledReportDriveDownloadDetails) MarshalJSON ¶
func (s UnsampledReportDriveDownloadDetails) MarshalJSON() ([]byte, error)
type UnsampledReports ¶
type UnsampledReports struct {
	// Items: A list of unsampled reports.
	Items []*UnsampledReport `json:"items,omitempty"`
	// ItemsPerPage: The maximum number of resources the response can contain,
	// regardless of the actual number of resources returned. Its value ranges from
	// 1 to 1000 with a value of 1000 by default, or otherwise specified by the
	// max-results query parameter.
	ItemsPerPage int64 `json:"itemsPerPage,omitempty"`
	// Kind: Collection type.
	Kind string `json:"kind,omitempty"`
	// NextLink: Link to next page for this unsampled report collection.
	NextLink string `json:"nextLink,omitempty"`
	// PreviousLink: Link to previous page for this unsampled report collection.
	PreviousLink string `json:"previousLink,omitempty"`
	// StartIndex: The starting index of the resources, which is 1 by default or
	// otherwise specified by the start-index query parameter.
	StartIndex int64 `json:"startIndex,omitempty"`
	// TotalResults: The total number of results for the query, regardless of the
	// number of resources in the result.
	TotalResults int64 `json:"totalResults,omitempty"`
	// Username: Email ID of the authenticated user
	Username string `json:"username,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Items") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Items") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UnsampledReports: An unsampled report collection lists Analytics unsampled reports to which the user has access. Each view (profile) can have a set of unsampled reports. Each resource in the unsampled report collection corresponds to a single Analytics unsampled report.

func (UnsampledReports) MarshalJSON ¶
func (s UnsampledReports) MarshalJSON() ([]byte, error)
type Upload ¶
type Upload struct {
	// AccountId: Account Id to which this upload belongs.
	AccountId int64 `json:"accountId,omitempty,string"`
	// CustomDataSourceId: Custom data source Id to which this data import belongs.
	CustomDataSourceId string `json:"customDataSourceId,omitempty"`
	// Errors: Data import errors collection.
	Errors []string `json:"errors,omitempty"`
	// Id: A unique ID for this upload.
	Id string `json:"id,omitempty"`
	// Kind: Resource type for Analytics upload.
	Kind string `json:"kind,omitempty"`
	// Status: Upload status. Possible values: PENDING, COMPLETED, FAILED,
	// DELETING, DELETED.
	Status string `json:"status,omitempty"`
	// UploadTime: Time this file is uploaded.
	UploadTime string `json:"uploadTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AccountId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccountId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Upload: Metadata returned for an upload operation.

func (Upload) MarshalJSON ¶
func (s Upload) MarshalJSON() ([]byte, error)
type Uploads ¶
type Uploads struct {
	// Items: A list of uploads.
	Items []*Upload `json:"items,omitempty"`
	// ItemsPerPage: The maximum number of resources the response can contain,
	// regardless of the actual number of resources returned. Its value ranges from
	// 1 to 1000 with a value of 1000 by default, or otherwise specified by the
	// max-results query parameter.
	ItemsPerPage int64 `json:"itemsPerPage,omitempty"`
	// Kind: Collection type.
	Kind string `json:"kind,omitempty"`
	// NextLink: Link to next page for this upload collection.
	NextLink string `json:"nextLink,omitempty"`
	// PreviousLink: Link to previous page for this upload collection.
	PreviousLink string `json:"previousLink,omitempty"`
	// StartIndex: The starting index of the resources, which is 1 by default or
	// otherwise specified by the start-index query parameter.
	StartIndex int64 `json:"startIndex,omitempty"`
	// TotalResults: The total number of results for the query, regardless of the
	// number of resources in the result.
	TotalResults int64 `json:"totalResults,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Items") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Items") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Uploads: Upload collection lists Analytics uploads to which the user has access. Each custom data source can have a set of uploads. Each resource in the upload collection corresponds to a single Analytics data upload.

func (Uploads) MarshalJSON ¶
func (s Uploads) MarshalJSON() ([]byte, error)
type UserDeletionRequest ¶
type UserDeletionRequest struct {
	// DeletionRequestTime: This marks the point in time for which all user data
	// before should be deleted
	DeletionRequestTime string `json:"deletionRequestTime,omitempty"`
	// FirebaseProjectId: Firebase Project Id
	FirebaseProjectId string `json:"firebaseProjectId,omitempty"`
	// Id: User ID.
	Id *UserDeletionRequestId `json:"id,omitempty"`
	// Kind: Value is "analytics#userDeletionRequest".
	Kind string `json:"kind,omitempty"`
	// PropertyId: Property ID
	PropertyId string `json:"propertyId,omitempty"`
	// WebPropertyId: Web property ID of the form UA-XXXXX-YY.
	WebPropertyId string `json:"webPropertyId,omitempty"`

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

UserDeletionRequest: JSON template for a user deletion request resource.

func (UserDeletionRequest) MarshalJSON ¶
func (s UserDeletionRequest) MarshalJSON() ([]byte, error)
type UserDeletionRequestId ¶
type UserDeletionRequestId struct {
	// Type: Type of user
	Type string `json:"type,omitempty"`
	// UserId: The User's id
	UserId string `json:"userId,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Type") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Type") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UserDeletionRequestId: User ID.

func (UserDeletionRequestId) MarshalJSON ¶
func (s UserDeletionRequestId) MarshalJSON() ([]byte, error)
type UserDeletionService ¶
type UserDeletionService struct {
	UserDeletionRequest *UserDeletionUserDeletionRequestService
	// contains filtered or unexported fields
}
func NewUserDeletionService ¶
func NewUserDeletionService(s *Service) *UserDeletionService
type UserDeletionUserDeletionRequestService ¶
type UserDeletionUserDeletionRequestService struct {
	// contains filtered or unexported fields
}
func NewUserDeletionUserDeletionRequestService ¶
func NewUserDeletionUserDeletionRequestService(s *Service) *UserDeletionUserDeletionRequestService
func (*UserDeletionUserDeletionRequestService) Upsert ¶
func (r *UserDeletionUserDeletionRequestService) Upsert(userdeletionrequest *UserDeletionRequest) *UserDeletionUserDeletionRequestUpsertCall

Upsert: Insert or update a user deletion requests.

type UserDeletionUserDeletionRequestUpsertCall ¶
type UserDeletionUserDeletionRequestUpsertCall struct {
	// contains filtered or unexported fields
}
func (*UserDeletionUserDeletionRequestUpsertCall) Context ¶
func (c *UserDeletionUserDeletionRequestUpsertCall) Context(ctx context.Context) *UserDeletionUserDeletionRequestUpsertCall

Context sets the context to be used in this call's Do method.

func (*UserDeletionUserDeletionRequestUpsertCall) Do ¶
func (c *UserDeletionUserDeletionRequestUpsertCall) Do(opts ...googleapi.CallOption) (*UserDeletionRequest, error)

Do executes the "analytics.userDeletion.userDeletionRequest.upsert" call. Any non-2xx status code is an error. Response headers are in either *UserDeletionRequest.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*UserDeletionUserDeletionRequestUpsertCall) Fields ¶
func (c *UserDeletionUserDeletionRequestUpsertCall) Fields(s ...googleapi.Field) *UserDeletionUserDeletionRequestUpsertCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*UserDeletionUserDeletionRequestUpsertCall) Header ¶
func (c *UserDeletionUserDeletionRequestUpsertCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type UserRef ¶
type UserRef struct {
	// Email: Email ID of this user.
	Email string `json:"email,omitempty"`
	// Id: User ID.
	Id   string `json:"id,omitempty"`
	Kind string `json:"kind,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Email") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Email") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

UserRef: JSON template for a user reference.

func (UserRef) MarshalJSON ¶
func (s UserRef) MarshalJSON() ([]byte, error)
type WebPropertyRef ¶
type WebPropertyRef struct {
	// AccountId: Account ID to which this web property belongs.
	AccountId string `json:"accountId,omitempty"`
	// Href: Link for this web property.
	Href string `json:"href,omitempty"`
	// Id: Web property ID of the form UA-XXXXX-YY.
	Id string `json:"id,omitempty"`
	// InternalWebPropertyId: Internal ID for this web property.
	InternalWebPropertyId string `json:"internalWebPropertyId,omitempty"`
	// Kind: Analytics web property reference.
	Kind string `json:"kind,omitempty"`
	// Name: Name of this web property.
	Name string `json:"name,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AccountId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccountId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

WebPropertyRef: JSON template for a web property reference.

func (WebPropertyRef) MarshalJSON ¶
func (s WebPropertyRef) MarshalJSON() ([]byte, error)
type WebPropertySummary ¶
type WebPropertySummary struct {
	// Id: Web property ID of the form UA-XXXXX-YY.
	Id string `json:"id,omitempty"`
	// InternalWebPropertyId: Internal ID for this web property.
	InternalWebPropertyId string `json:"internalWebPropertyId,omitempty"`
	// Kind: Resource type for Analytics WebPropertySummary.
	Kind string `json:"kind,omitempty"`
	// Level: Level for this web property. Possible values are STANDARD or PREMIUM.
	Level string `json:"level,omitempty"`
	// Name: Web property name.
	Name string `json:"name,omitempty"`
	// Profiles: List of profiles under this web property.
	Profiles []*ProfileSummary `json:"profiles,omitempty"`
	// Starred: Indicates whether this web property is starred or not.
	Starred bool `json:"starred,omitempty"`
	// WebsiteUrl: Website url for this web property.
	WebsiteUrl string `json:"websiteUrl,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Id") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Id") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

WebPropertySummary: JSON template for an Analytics WebPropertySummary. WebPropertySummary returns basic information (i.e., summary) for a web property.

func (WebPropertySummary) MarshalJSON ¶
func (s WebPropertySummary) MarshalJSON() ([]byte, error)
type Webproperties ¶
type Webproperties struct {
	// Items: A list of web properties.
	Items []*Webproperty `json:"items,omitempty"`
	// ItemsPerPage: The maximum number of resources the response can contain,
	// regardless of the actual number of resources returned. Its value ranges from
	// 1 to 1000 with a value of 1000 by default, or otherwise specified by the
	// max-results query parameter.
	ItemsPerPage int64 `json:"itemsPerPage,omitempty"`
	// Kind: Collection type.
	Kind string `json:"kind,omitempty"`
	// NextLink: Link to next page for this web property collection.
	NextLink string `json:"nextLink,omitempty"`
	// PreviousLink: Link to previous page for this web property collection.
	PreviousLink string `json:"previousLink,omitempty"`
	// StartIndex: The starting index of the resources, which is 1 by default or
	// otherwise specified by the start-index query parameter.
	StartIndex int64 `json:"startIndex,omitempty"`
	// TotalResults: The total number of results for the query, regardless of the
	// number of results in the response.
	TotalResults int64 `json:"totalResults,omitempty"`
	// Username: Email ID of the authenticated user
	Username string `json:"username,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Items") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Items") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Webproperties: A web property collection lists Analytics web properties to which the user has access. Each resource in the collection corresponds to a single Analytics web property.

func (Webproperties) MarshalJSON ¶
func (s Webproperties) MarshalJSON() ([]byte, error)
type Webproperty ¶
type Webproperty struct {
	// AccountId: Account ID to which this web property belongs.
	AccountId string `json:"accountId,omitempty"`
	// ChildLink: Child link for this web property. Points to the list of views
	// (profiles) for this web property.
	ChildLink *WebpropertyChildLink `json:"childLink,omitempty"`
	// Created: Time this web property was created.
	Created string `json:"created,omitempty"`
	// DataRetentionResetOnNewActivity: Set to true to reset the retention period
	// of the user identifier with each new event from that user (thus setting the
	// expiration date to current time plus retention period).
	// Set to false to delete data associated with the user identifier
	// automatically after the rentention period.
	// This property cannot be set on insert.
	DataRetentionResetOnNewActivity bool `json:"dataRetentionResetOnNewActivity,omitempty"`
	// DataRetentionTtl: The length of time for which user and event data is
	// retained.
	// This property cannot be set on insert.
	DataRetentionTtl string `json:"dataRetentionTtl,omitempty"`
	// DefaultProfileId: Default view (profile) ID.
	DefaultProfileId int64 `json:"defaultProfileId,omitempty,string"`
	// Id: Web property ID of the form UA-XXXXX-YY.
	Id string `json:"id,omitempty"`
	// IndustryVertical: The industry vertical/category selected for this web
	// property.
	IndustryVertical string `json:"industryVertical,omitempty"`
	// InternalWebPropertyId: Internal ID for this web property.
	InternalWebPropertyId string `json:"internalWebPropertyId,omitempty"`
	// Kind: Resource type for Analytics WebProperty.
	Kind string `json:"kind,omitempty"`
	// Level: Level for this web property. Possible values are STANDARD or PREMIUM.
	Level string `json:"level,omitempty"`
	// Name: Name of this web property.
	Name string `json:"name,omitempty"`
	// ParentLink: Parent link for this web property. Points to the account to
	// which this web property belongs.
	ParentLink *WebpropertyParentLink `json:"parentLink,omitempty"`
	// Permissions: Permissions the user has for this web property.
	Permissions *WebpropertyPermissions `json:"permissions,omitempty"`
	// ProfileCount: View (Profile) count for this web property.
	ProfileCount int64 `json:"profileCount,omitempty"`
	// SelfLink: Link for this web property.
	SelfLink string `json:"selfLink,omitempty"`
	// Starred: Indicates whether this web property is starred or not.
	Starred bool `json:"starred,omitempty"`
	// Updated: Time this web property was last modified.
	Updated string `json:"updated,omitempty"`
	// WebsiteUrl: Website url for this web property.
	WebsiteUrl string `json:"websiteUrl,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AccountId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccountId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Webproperty: JSON template for an Analytics web property.

func (Webproperty) MarshalJSON ¶
func (s Webproperty) MarshalJSON() ([]byte, error)
type WebpropertyChildLink ¶
type WebpropertyChildLink struct {
	// Href: Link to the list of views (profiles) for this web property.
	Href string `json:"href,omitempty"`
	// Type: Type of the parent link. Its value is "analytics#profiles".
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Href") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Href") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

WebpropertyChildLink: Child link for this web property. Points to the list of views (profiles) for this web property.

func (WebpropertyChildLink) MarshalJSON ¶
func (s WebpropertyChildLink) MarshalJSON() ([]byte, error)
type WebpropertyParentLink ¶
type WebpropertyParentLink struct {
	// Href: Link to the account for this web property.
	Href string `json:"href,omitempty"`
	// Type: Type of the parent link. Its value is "analytics#account".
	Type string `json:"type,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Href") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Href") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

WebpropertyParentLink: Parent link for this web property. Points to the account to which this web property belongs.

func (WebpropertyParentLink) MarshalJSON ¶
func (s WebpropertyParentLink) MarshalJSON() ([]byte, error)
type WebpropertyPermissions ¶
type WebpropertyPermissions struct {
	// Effective: All the permissions that the user has for this web property.
	// These include any implied permissions (e.g., EDIT implies VIEW) or inherited
	// permissions from the parent account.
	Effective []string `json:"effective,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Effective") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Effective") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

WebpropertyPermissions: Permissions the user has for this web property.

func (WebpropertyPermissions) MarshalJSON ¶
func (s WebpropertyPermissions) MarshalJSON() ([]byte, error)
 Source Files ¶
View all Source files
analytics-gen.go
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
