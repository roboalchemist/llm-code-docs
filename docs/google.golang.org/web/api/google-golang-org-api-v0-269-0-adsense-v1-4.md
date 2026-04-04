# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.4

Title: adsense package - google.golang.org/api/adsense/v1.4 - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.4

Markdown Content:
Skip to Main Content
Why Go
Learn
Docs
Packages
Community
Discover Packages
 
google.golang.org/api
 
adsense
 
v1.4
adsense
package
Version: v0.269.0 Latest 
Published: Feb 24, 2026 
License: BSD-3-Clause 
Imports: 15 
Imported by: 1
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
Creating a client
Other authentication options

Package adsense provides access to the AdSense Management API.

For product documentation, see: https://developers.google.com/adsense/management/

Creating a client ¶

Usage example:

import "google.golang.org/api/adsense/v1.4"
...
ctx := context.Background()
adsenseService, err := adsense.NewService(ctx)


In this example, Google Application Default Credentials are used for authentication.

For information on how to create and obtain Application Default Credentials, see https://developers.google.com/identity/protocols/application-default-credentials.

Other authentication options ¶

By default, all available scopes (see "Constants") are used to authenticate. To restrict scopes, use option.WithScopes:

adsenseService, err := adsense.NewService(ctx, option.WithScopes(adsense.AdsenseReadonlyScope))


To use an API key for authentication (note: some APIs do not support API keys), use option.WithAPIKey:

adsenseService, err := adsense.NewService(ctx, option.WithAPIKey("AIza..."))


To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow), use option.WithTokenSource:

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
adsenseService, err := adsense.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))


See https://godoc.org/google.golang.org/api/option/ for details on options.

Index ¶
Constants
type Account
func (s *Account) MarshalJSON() ([]byte, error)
type Accounts
func (s *Accounts) MarshalJSON() ([]byte, error)
type AccountsAdclientsGetAdCodeCall
func (c *AccountsAdclientsGetAdCodeCall) Context(ctx context.Context) *AccountsAdclientsGetAdCodeCall
func (c *AccountsAdclientsGetAdCodeCall) Do(opts ...googleapi.CallOption) (*AdCode, error)
func (c *AccountsAdclientsGetAdCodeCall) Fields(s ...googleapi.Field) *AccountsAdclientsGetAdCodeCall
func (c *AccountsAdclientsGetAdCodeCall) Header() http.Header
func (c *AccountsAdclientsGetAdCodeCall) IfNoneMatch(entityTag string) *AccountsAdclientsGetAdCodeCall
func (c *AccountsAdclientsGetAdCodeCall) TagPartner(tagPartner string) *AccountsAdclientsGetAdCodeCall
type AccountsAdclientsListCall
func (c *AccountsAdclientsListCall) Context(ctx context.Context) *AccountsAdclientsListCall
func (c *AccountsAdclientsListCall) Do(opts ...googleapi.CallOption) (*AdClients, error)
func (c *AccountsAdclientsListCall) Fields(s ...googleapi.Field) *AccountsAdclientsListCall
func (c *AccountsAdclientsListCall) Header() http.Header
func (c *AccountsAdclientsListCall) IfNoneMatch(entityTag string) *AccountsAdclientsListCall
func (c *AccountsAdclientsListCall) MaxResults(maxResults int64) *AccountsAdclientsListCall
func (c *AccountsAdclientsListCall) PageToken(pageToken string) *AccountsAdclientsListCall
func (c *AccountsAdclientsListCall) Pages(ctx context.Context, f func(*AdClients) error) error
type AccountsAdclientsService
func NewAccountsAdclientsService(s *Service) *AccountsAdclientsService
func (r *AccountsAdclientsService) GetAdCode(accountId string, adClientId string) *AccountsAdclientsGetAdCodeCall
func (r *AccountsAdclientsService) List(accountId string) *AccountsAdclientsListCall
type AccountsAdunitsCustomchannelsListCall
func (c *AccountsAdunitsCustomchannelsListCall) Context(ctx context.Context) *AccountsAdunitsCustomchannelsListCall
func (c *AccountsAdunitsCustomchannelsListCall) Do(opts ...googleapi.CallOption) (*CustomChannels, error)
func (c *AccountsAdunitsCustomchannelsListCall) Fields(s ...googleapi.Field) *AccountsAdunitsCustomchannelsListCall
func (c *AccountsAdunitsCustomchannelsListCall) Header() http.Header
func (c *AccountsAdunitsCustomchannelsListCall) IfNoneMatch(entityTag string) *AccountsAdunitsCustomchannelsListCall
func (c *AccountsAdunitsCustomchannelsListCall) MaxResults(maxResults int64) *AccountsAdunitsCustomchannelsListCall
func (c *AccountsAdunitsCustomchannelsListCall) PageToken(pageToken string) *AccountsAdunitsCustomchannelsListCall
func (c *AccountsAdunitsCustomchannelsListCall) Pages(ctx context.Context, f func(*CustomChannels) error) error
type AccountsAdunitsCustomchannelsService
func NewAccountsAdunitsCustomchannelsService(s *Service) *AccountsAdunitsCustomchannelsService
func (r *AccountsAdunitsCustomchannelsService) List(accountId string, adClientId string, adUnitId string) *AccountsAdunitsCustomchannelsListCall
type AccountsAdunitsGetAdCodeCall
func (c *AccountsAdunitsGetAdCodeCall) Context(ctx context.Context) *AccountsAdunitsGetAdCodeCall
func (c *AccountsAdunitsGetAdCodeCall) Do(opts ...googleapi.CallOption) (*AdCode, error)
func (c *AccountsAdunitsGetAdCodeCall) Fields(s ...googleapi.Field) *AccountsAdunitsGetAdCodeCall
func (c *AccountsAdunitsGetAdCodeCall) Header() http.Header
func (c *AccountsAdunitsGetAdCodeCall) IfNoneMatch(entityTag string) *AccountsAdunitsGetAdCodeCall
type AccountsAdunitsGetCall
func (c *AccountsAdunitsGetCall) Context(ctx context.Context) *AccountsAdunitsGetCall
func (c *AccountsAdunitsGetCall) Do(opts ...googleapi.CallOption) (*AdUnit, error)
func (c *AccountsAdunitsGetCall) Fields(s ...googleapi.Field) *AccountsAdunitsGetCall
func (c *AccountsAdunitsGetCall) Header() http.Header
func (c *AccountsAdunitsGetCall) IfNoneMatch(entityTag string) *AccountsAdunitsGetCall
type AccountsAdunitsListCall
func (c *AccountsAdunitsListCall) Context(ctx context.Context) *AccountsAdunitsListCall
func (c *AccountsAdunitsListCall) Do(opts ...googleapi.CallOption) (*AdUnits, error)
func (c *AccountsAdunitsListCall) Fields(s ...googleapi.Field) *AccountsAdunitsListCall
func (c *AccountsAdunitsListCall) Header() http.Header
func (c *AccountsAdunitsListCall) IfNoneMatch(entityTag string) *AccountsAdunitsListCall
func (c *AccountsAdunitsListCall) IncludeInactive(includeInactive bool) *AccountsAdunitsListCall
func (c *AccountsAdunitsListCall) MaxResults(maxResults int64) *AccountsAdunitsListCall
func (c *AccountsAdunitsListCall) PageToken(pageToken string) *AccountsAdunitsListCall
func (c *AccountsAdunitsListCall) Pages(ctx context.Context, f func(*AdUnits) error) error
type AccountsAdunitsService
func NewAccountsAdunitsService(s *Service) *AccountsAdunitsService
func (r *AccountsAdunitsService) Get(accountId string, adClientId string, adUnitId string) *AccountsAdunitsGetCall
func (r *AccountsAdunitsService) GetAdCode(accountId string, adClientId string, adUnitId string) *AccountsAdunitsGetAdCodeCall
func (r *AccountsAdunitsService) List(accountId string, adClientId string) *AccountsAdunitsListCall
type AccountsAlertsDeleteCall
func (c *AccountsAlertsDeleteCall) Context(ctx context.Context) *AccountsAlertsDeleteCall
func (c *AccountsAlertsDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *AccountsAlertsDeleteCall) Fields(s ...googleapi.Field) *AccountsAlertsDeleteCall
func (c *AccountsAlertsDeleteCall) Header() http.Header
type AccountsAlertsListCall
func (c *AccountsAlertsListCall) Context(ctx context.Context) *AccountsAlertsListCall
func (c *AccountsAlertsListCall) Do(opts ...googleapi.CallOption) (*Alerts, error)
func (c *AccountsAlertsListCall) Fields(s ...googleapi.Field) *AccountsAlertsListCall
func (c *AccountsAlertsListCall) Header() http.Header
func (c *AccountsAlertsListCall) IfNoneMatch(entityTag string) *AccountsAlertsListCall
func (c *AccountsAlertsListCall) Locale(locale string) *AccountsAlertsListCall
type AccountsAlertsService
func NewAccountsAlertsService(s *Service) *AccountsAlertsService
func (r *AccountsAlertsService) Delete(accountId string, alertId string) *AccountsAlertsDeleteCall
func (r *AccountsAlertsService) List(accountId string) *AccountsAlertsListCall
type AccountsCustomchannelsAdunitsListCall
func (c *AccountsCustomchannelsAdunitsListCall) Context(ctx context.Context) *AccountsCustomchannelsAdunitsListCall
func (c *AccountsCustomchannelsAdunitsListCall) Do(opts ...googleapi.CallOption) (*AdUnits, error)
func (c *AccountsCustomchannelsAdunitsListCall) Fields(s ...googleapi.Field) *AccountsCustomchannelsAdunitsListCall
func (c *AccountsCustomchannelsAdunitsListCall) Header() http.Header
func (c *AccountsCustomchannelsAdunitsListCall) IfNoneMatch(entityTag string) *AccountsCustomchannelsAdunitsListCall
func (c *AccountsCustomchannelsAdunitsListCall) IncludeInactive(includeInactive bool) *AccountsCustomchannelsAdunitsListCall
func (c *AccountsCustomchannelsAdunitsListCall) MaxResults(maxResults int64) *AccountsCustomchannelsAdunitsListCall
func (c *AccountsCustomchannelsAdunitsListCall) PageToken(pageToken string) *AccountsCustomchannelsAdunitsListCall
func (c *AccountsCustomchannelsAdunitsListCall) Pages(ctx context.Context, f func(*AdUnits) error) error
type AccountsCustomchannelsAdunitsService
func NewAccountsCustomchannelsAdunitsService(s *Service) *AccountsCustomchannelsAdunitsService
func (r *AccountsCustomchannelsAdunitsService) List(accountId string, adClientId string, customChannelId string) *AccountsCustomchannelsAdunitsListCall
type AccountsCustomchannelsGetCall
func (c *AccountsCustomchannelsGetCall) Context(ctx context.Context) *AccountsCustomchannelsGetCall
func (c *AccountsCustomchannelsGetCall) Do(opts ...googleapi.CallOption) (*CustomChannel, error)
func (c *AccountsCustomchannelsGetCall) Fields(s ...googleapi.Field) *AccountsCustomchannelsGetCall
func (c *AccountsCustomchannelsGetCall) Header() http.Header
func (c *AccountsCustomchannelsGetCall) IfNoneMatch(entityTag string) *AccountsCustomchannelsGetCall
type AccountsCustomchannelsListCall
func (c *AccountsCustomchannelsListCall) Context(ctx context.Context) *AccountsCustomchannelsListCall
func (c *AccountsCustomchannelsListCall) Do(opts ...googleapi.CallOption) (*CustomChannels, error)
func (c *AccountsCustomchannelsListCall) Fields(s ...googleapi.Field) *AccountsCustomchannelsListCall
func (c *AccountsCustomchannelsListCall) Header() http.Header
func (c *AccountsCustomchannelsListCall) IfNoneMatch(entityTag string) *AccountsCustomchannelsListCall
func (c *AccountsCustomchannelsListCall) MaxResults(maxResults int64) *AccountsCustomchannelsListCall
func (c *AccountsCustomchannelsListCall) PageToken(pageToken string) *AccountsCustomchannelsListCall
func (c *AccountsCustomchannelsListCall) Pages(ctx context.Context, f func(*CustomChannels) error) error
type AccountsCustomchannelsService
func NewAccountsCustomchannelsService(s *Service) *AccountsCustomchannelsService
func (r *AccountsCustomchannelsService) Get(accountId string, adClientId string, customChannelId string) *AccountsCustomchannelsGetCall
func (r *AccountsCustomchannelsService) List(accountId string, adClientId string) *AccountsCustomchannelsListCall
type AccountsGetCall
func (c *AccountsGetCall) Context(ctx context.Context) *AccountsGetCall
func (c *AccountsGetCall) Do(opts ...googleapi.CallOption) (*Account, error)
func (c *AccountsGetCall) Fields(s ...googleapi.Field) *AccountsGetCall
func (c *AccountsGetCall) Header() http.Header
func (c *AccountsGetCall) IfNoneMatch(entityTag string) *AccountsGetCall
func (c *AccountsGetCall) Tree(tree bool) *AccountsGetCall
type AccountsListCall
func (c *AccountsListCall) Context(ctx context.Context) *AccountsListCall
func (c *AccountsListCall) Do(opts ...googleapi.CallOption) (*Accounts, error)
func (c *AccountsListCall) Fields(s ...googleapi.Field) *AccountsListCall
func (c *AccountsListCall) Header() http.Header
func (c *AccountsListCall) IfNoneMatch(entityTag string) *AccountsListCall
func (c *AccountsListCall) MaxResults(maxResults int64) *AccountsListCall
func (c *AccountsListCall) PageToken(pageToken string) *AccountsListCall
func (c *AccountsListCall) Pages(ctx context.Context, f func(*Accounts) error) error
type AccountsPaymentsListCall
func (c *AccountsPaymentsListCall) Context(ctx context.Context) *AccountsPaymentsListCall
func (c *AccountsPaymentsListCall) Do(opts ...googleapi.CallOption) (*Payments, error)
func (c *AccountsPaymentsListCall) Fields(s ...googleapi.Field) *AccountsPaymentsListCall
func (c *AccountsPaymentsListCall) Header() http.Header
func (c *AccountsPaymentsListCall) IfNoneMatch(entityTag string) *AccountsPaymentsListCall
type AccountsPaymentsService
func NewAccountsPaymentsService(s *Service) *AccountsPaymentsService
func (r *AccountsPaymentsService) List(accountId string) *AccountsPaymentsListCall
type AccountsReportsGenerateCall
func (c *AccountsReportsGenerateCall) Context(ctx context.Context) *AccountsReportsGenerateCall
func (c *AccountsReportsGenerateCall) Currency(currency string) *AccountsReportsGenerateCall
func (c *AccountsReportsGenerateCall) Dimension(dimension ...string) *AccountsReportsGenerateCall
func (c *AccountsReportsGenerateCall) Do(opts ...googleapi.CallOption) (*AdsenseReportsGenerateResponse, error)
func (c *AccountsReportsGenerateCall) Download(opts ...googleapi.CallOption) (*http.Response, error)
func (c *AccountsReportsGenerateCall) Fields(s ...googleapi.Field) *AccountsReportsGenerateCall
func (c *AccountsReportsGenerateCall) Filter(filter ...string) *AccountsReportsGenerateCall
func (c *AccountsReportsGenerateCall) Header() http.Header
func (c *AccountsReportsGenerateCall) IfNoneMatch(entityTag string) *AccountsReportsGenerateCall
func (c *AccountsReportsGenerateCall) Locale(locale string) *AccountsReportsGenerateCall
func (c *AccountsReportsGenerateCall) MaxResults(maxResults int64) *AccountsReportsGenerateCall
func (c *AccountsReportsGenerateCall) Metric(metric ...string) *AccountsReportsGenerateCall
func (c *AccountsReportsGenerateCall) Sort(sort ...string) *AccountsReportsGenerateCall
func (c *AccountsReportsGenerateCall) StartIndex(startIndex int64) *AccountsReportsGenerateCall
func (c *AccountsReportsGenerateCall) UseTimezoneReporting(useTimezoneReporting bool) *AccountsReportsGenerateCall
type AccountsReportsSavedGenerateCall
func (c *AccountsReportsSavedGenerateCall) Context(ctx context.Context) *AccountsReportsSavedGenerateCall
func (c *AccountsReportsSavedGenerateCall) Do(opts ...googleapi.CallOption) (*AdsenseReportsGenerateResponse, error)
func (c *AccountsReportsSavedGenerateCall) Fields(s ...googleapi.Field) *AccountsReportsSavedGenerateCall
func (c *AccountsReportsSavedGenerateCall) Header() http.Header
func (c *AccountsReportsSavedGenerateCall) IfNoneMatch(entityTag string) *AccountsReportsSavedGenerateCall
func (c *AccountsReportsSavedGenerateCall) Locale(locale string) *AccountsReportsSavedGenerateCall
func (c *AccountsReportsSavedGenerateCall) MaxResults(maxResults int64) *AccountsReportsSavedGenerateCall
func (c *AccountsReportsSavedGenerateCall) StartIndex(startIndex int64) *AccountsReportsSavedGenerateCall
type AccountsReportsSavedListCall
func (c *AccountsReportsSavedListCall) Context(ctx context.Context) *AccountsReportsSavedListCall
func (c *AccountsReportsSavedListCall) Do(opts ...googleapi.CallOption) (*SavedReports, error)
func (c *AccountsReportsSavedListCall) Fields(s ...googleapi.Field) *AccountsReportsSavedListCall
func (c *AccountsReportsSavedListCall) Header() http.Header
func (c *AccountsReportsSavedListCall) IfNoneMatch(entityTag string) *AccountsReportsSavedListCall
func (c *AccountsReportsSavedListCall) MaxResults(maxResults int64) *AccountsReportsSavedListCall
func (c *AccountsReportsSavedListCall) PageToken(pageToken string) *AccountsReportsSavedListCall
func (c *AccountsReportsSavedListCall) Pages(ctx context.Context, f func(*SavedReports) error) error
type AccountsReportsSavedService
func NewAccountsReportsSavedService(s *Service) *AccountsReportsSavedService
func (r *AccountsReportsSavedService) Generate(accountId string, savedReportId string) *AccountsReportsSavedGenerateCall
func (r *AccountsReportsSavedService) List(accountId string) *AccountsReportsSavedListCall
type AccountsReportsService
func NewAccountsReportsService(s *Service) *AccountsReportsService
func (r *AccountsReportsService) Generate(accountId string, startDate string, endDate string) *AccountsReportsGenerateCall
type AccountsSavedadstylesGetCall
func (c *AccountsSavedadstylesGetCall) Context(ctx context.Context) *AccountsSavedadstylesGetCall
func (c *AccountsSavedadstylesGetCall) Do(opts ...googleapi.CallOption) (*SavedAdStyle, error)
func (c *AccountsSavedadstylesGetCall) Fields(s ...googleapi.Field) *AccountsSavedadstylesGetCall
func (c *AccountsSavedadstylesGetCall) Header() http.Header
func (c *AccountsSavedadstylesGetCall) IfNoneMatch(entityTag string) *AccountsSavedadstylesGetCall
type AccountsSavedadstylesListCall
func (c *AccountsSavedadstylesListCall) Context(ctx context.Context) *AccountsSavedadstylesListCall
func (c *AccountsSavedadstylesListCall) Do(opts ...googleapi.CallOption) (*SavedAdStyles, error)
func (c *AccountsSavedadstylesListCall) Fields(s ...googleapi.Field) *AccountsSavedadstylesListCall
func (c *AccountsSavedadstylesListCall) Header() http.Header
func (c *AccountsSavedadstylesListCall) IfNoneMatch(entityTag string) *AccountsSavedadstylesListCall
func (c *AccountsSavedadstylesListCall) MaxResults(maxResults int64) *AccountsSavedadstylesListCall
func (c *AccountsSavedadstylesListCall) PageToken(pageToken string) *AccountsSavedadstylesListCall
func (c *AccountsSavedadstylesListCall) Pages(ctx context.Context, f func(*SavedAdStyles) error) error
type AccountsSavedadstylesService
func NewAccountsSavedadstylesService(s *Service) *AccountsSavedadstylesService
func (r *AccountsSavedadstylesService) Get(accountId string, savedAdStyleId string) *AccountsSavedadstylesGetCall
func (r *AccountsSavedadstylesService) List(accountId string) *AccountsSavedadstylesListCall
type AccountsService
func NewAccountsService(s *Service) *AccountsService
func (r *AccountsService) Get(accountId string) *AccountsGetCall
func (r *AccountsService) List() *AccountsListCall
type AccountsUrlchannelsListCall
func (c *AccountsUrlchannelsListCall) Context(ctx context.Context) *AccountsUrlchannelsListCall
func (c *AccountsUrlchannelsListCall) Do(opts ...googleapi.CallOption) (*UrlChannels, error)
func (c *AccountsUrlchannelsListCall) Fields(s ...googleapi.Field) *AccountsUrlchannelsListCall
func (c *AccountsUrlchannelsListCall) Header() http.Header
func (c *AccountsUrlchannelsListCall) IfNoneMatch(entityTag string) *AccountsUrlchannelsListCall
func (c *AccountsUrlchannelsListCall) MaxResults(maxResults int64) *AccountsUrlchannelsListCall
func (c *AccountsUrlchannelsListCall) PageToken(pageToken string) *AccountsUrlchannelsListCall
func (c *AccountsUrlchannelsListCall) Pages(ctx context.Context, f func(*UrlChannels) error) error
type AccountsUrlchannelsService
func NewAccountsUrlchannelsService(s *Service) *AccountsUrlchannelsService
func (r *AccountsUrlchannelsService) List(accountId string, adClientId string) *AccountsUrlchannelsListCall
type AdClient
func (s *AdClient) MarshalJSON() ([]byte, error)
type AdClients
func (s *AdClients) MarshalJSON() ([]byte, error)
type AdCode
func (s *AdCode) MarshalJSON() ([]byte, error)
type AdStyle
func (s *AdStyle) MarshalJSON() ([]byte, error)
type AdStyleColors
func (s *AdStyleColors) MarshalJSON() ([]byte, error)
type AdStyleFont
func (s *AdStyleFont) MarshalJSON() ([]byte, error)
type AdUnit
func (s *AdUnit) MarshalJSON() ([]byte, error)
type AdUnitContentAdsSettings
func (s *AdUnitContentAdsSettings) MarshalJSON() ([]byte, error)
type AdUnitContentAdsSettingsBackupOption
func (s *AdUnitContentAdsSettingsBackupOption) MarshalJSON() ([]byte, error)
type AdUnitFeedAdsSettings
func (s *AdUnitFeedAdsSettings) MarshalJSON() ([]byte, error)
type AdUnitMobileContentAdsSettings
func (s *AdUnitMobileContentAdsSettings) MarshalJSON() ([]byte, error)
type AdUnits
func (s *AdUnits) MarshalJSON() ([]byte, error)
type AdclientsListCall
func (c *AdclientsListCall) Context(ctx context.Context) *AdclientsListCall
func (c *AdclientsListCall) Do(opts ...googleapi.CallOption) (*AdClients, error)
func (c *AdclientsListCall) Fields(s ...googleapi.Field) *AdclientsListCall
func (c *AdclientsListCall) Header() http.Header
func (c *AdclientsListCall) IfNoneMatch(entityTag string) *AdclientsListCall
func (c *AdclientsListCall) MaxResults(maxResults int64) *AdclientsListCall
func (c *AdclientsListCall) PageToken(pageToken string) *AdclientsListCall
func (c *AdclientsListCall) Pages(ctx context.Context, f func(*AdClients) error) error
type AdclientsService
func NewAdclientsService(s *Service) *AdclientsService
func (r *AdclientsService) List() *AdclientsListCall
type AdsenseReportsGenerateResponse
func (s *AdsenseReportsGenerateResponse) MarshalJSON() ([]byte, error)
type AdsenseReportsGenerateResponseHeaders
func (s *AdsenseReportsGenerateResponseHeaders) MarshalJSON() ([]byte, error)
type AdunitsCustomchannelsListCall
func (c *AdunitsCustomchannelsListCall) Context(ctx context.Context) *AdunitsCustomchannelsListCall
func (c *AdunitsCustomchannelsListCall) Do(opts ...googleapi.CallOption) (*CustomChannels, error)
func (c *AdunitsCustomchannelsListCall) Fields(s ...googleapi.Field) *AdunitsCustomchannelsListCall
func (c *AdunitsCustomchannelsListCall) Header() http.Header
func (c *AdunitsCustomchannelsListCall) IfNoneMatch(entityTag string) *AdunitsCustomchannelsListCall
func (c *AdunitsCustomchannelsListCall) MaxResults(maxResults int64) *AdunitsCustomchannelsListCall
func (c *AdunitsCustomchannelsListCall) PageToken(pageToken string) *AdunitsCustomchannelsListCall
func (c *AdunitsCustomchannelsListCall) Pages(ctx context.Context, f func(*CustomChannels) error) error
type AdunitsCustomchannelsService
func NewAdunitsCustomchannelsService(s *Service) *AdunitsCustomchannelsService
func (r *AdunitsCustomchannelsService) List(adClientId string, adUnitId string) *AdunitsCustomchannelsListCall
type AdunitsGetAdCodeCall
func (c *AdunitsGetAdCodeCall) Context(ctx context.Context) *AdunitsGetAdCodeCall
func (c *AdunitsGetAdCodeCall) Do(opts ...googleapi.CallOption) (*AdCode, error)
func (c *AdunitsGetAdCodeCall) Fields(s ...googleapi.Field) *AdunitsGetAdCodeCall
func (c *AdunitsGetAdCodeCall) Header() http.Header
func (c *AdunitsGetAdCodeCall) IfNoneMatch(entityTag string) *AdunitsGetAdCodeCall
type AdunitsGetCall
func (c *AdunitsGetCall) Context(ctx context.Context) *AdunitsGetCall
func (c *AdunitsGetCall) Do(opts ...googleapi.CallOption) (*AdUnit, error)
func (c *AdunitsGetCall) Fields(s ...googleapi.Field) *AdunitsGetCall
func (c *AdunitsGetCall) Header() http.Header
func (c *AdunitsGetCall) IfNoneMatch(entityTag string) *AdunitsGetCall
type AdunitsListCall
func (c *AdunitsListCall) Context(ctx context.Context) *AdunitsListCall
func (c *AdunitsListCall) Do(opts ...googleapi.CallOption) (*AdUnits, error)
func (c *AdunitsListCall) Fields(s ...googleapi.Field) *AdunitsListCall
func (c *AdunitsListCall) Header() http.Header
func (c *AdunitsListCall) IfNoneMatch(entityTag string) *AdunitsListCall
func (c *AdunitsListCall) IncludeInactive(includeInactive bool) *AdunitsListCall
func (c *AdunitsListCall) MaxResults(maxResults int64) *AdunitsListCall
func (c *AdunitsListCall) PageToken(pageToken string) *AdunitsListCall
func (c *AdunitsListCall) Pages(ctx context.Context, f func(*AdUnits) error) error
type AdunitsService
func NewAdunitsService(s *Service) *AdunitsService
func (r *AdunitsService) Get(adClientId string, adUnitId string) *AdunitsGetCall
func (r *AdunitsService) GetAdCode(adClientId string, adUnitId string) *AdunitsGetAdCodeCall
func (r *AdunitsService) List(adClientId string) *AdunitsListCall
type Alert
func (s *Alert) MarshalJSON() ([]byte, error)
type Alerts
func (s *Alerts) MarshalJSON() ([]byte, error)
type AlertsDeleteCall
func (c *AlertsDeleteCall) Context(ctx context.Context) *AlertsDeleteCall
func (c *AlertsDeleteCall) Do(opts ...googleapi.CallOption) error
func (c *AlertsDeleteCall) Fields(s ...googleapi.Field) *AlertsDeleteCall
func (c *AlertsDeleteCall) Header() http.Header
type AlertsListCall
func (c *AlertsListCall) Context(ctx context.Context) *AlertsListCall
func (c *AlertsListCall) Do(opts ...googleapi.CallOption) (*Alerts, error)
func (c *AlertsListCall) Fields(s ...googleapi.Field) *AlertsListCall
func (c *AlertsListCall) Header() http.Header
func (c *AlertsListCall) IfNoneMatch(entityTag string) *AlertsListCall
func (c *AlertsListCall) Locale(locale string) *AlertsListCall
type AlertsService
func NewAlertsService(s *Service) *AlertsService
func (r *AlertsService) Delete(alertId string) *AlertsDeleteCall
func (r *AlertsService) List() *AlertsListCall
type CustomChannel
func (s *CustomChannel) MarshalJSON() ([]byte, error)
type CustomChannelTargetingInfo
func (s *CustomChannelTargetingInfo) MarshalJSON() ([]byte, error)
type CustomChannels
func (s *CustomChannels) MarshalJSON() ([]byte, error)
type CustomchannelsAdunitsListCall
func (c *CustomchannelsAdunitsListCall) Context(ctx context.Context) *CustomchannelsAdunitsListCall
func (c *CustomchannelsAdunitsListCall) Do(opts ...googleapi.CallOption) (*AdUnits, error)
func (c *CustomchannelsAdunitsListCall) Fields(s ...googleapi.Field) *CustomchannelsAdunitsListCall
func (c *CustomchannelsAdunitsListCall) Header() http.Header
func (c *CustomchannelsAdunitsListCall) IfNoneMatch(entityTag string) *CustomchannelsAdunitsListCall
func (c *CustomchannelsAdunitsListCall) IncludeInactive(includeInactive bool) *CustomchannelsAdunitsListCall
func (c *CustomchannelsAdunitsListCall) MaxResults(maxResults int64) *CustomchannelsAdunitsListCall
func (c *CustomchannelsAdunitsListCall) PageToken(pageToken string) *CustomchannelsAdunitsListCall
func (c *CustomchannelsAdunitsListCall) Pages(ctx context.Context, f func(*AdUnits) error) error
type CustomchannelsAdunitsService
func NewCustomchannelsAdunitsService(s *Service) *CustomchannelsAdunitsService
func (r *CustomchannelsAdunitsService) List(adClientId string, customChannelId string) *CustomchannelsAdunitsListCall
type CustomchannelsGetCall
func (c *CustomchannelsGetCall) Context(ctx context.Context) *CustomchannelsGetCall
func (c *CustomchannelsGetCall) Do(opts ...googleapi.CallOption) (*CustomChannel, error)
func (c *CustomchannelsGetCall) Fields(s ...googleapi.Field) *CustomchannelsGetCall
func (c *CustomchannelsGetCall) Header() http.Header
func (c *CustomchannelsGetCall) IfNoneMatch(entityTag string) *CustomchannelsGetCall
type CustomchannelsListCall
func (c *CustomchannelsListCall) Context(ctx context.Context) *CustomchannelsListCall
func (c *CustomchannelsListCall) Do(opts ...googleapi.CallOption) (*CustomChannels, error)
func (c *CustomchannelsListCall) Fields(s ...googleapi.Field) *CustomchannelsListCall
func (c *CustomchannelsListCall) Header() http.Header
func (c *CustomchannelsListCall) IfNoneMatch(entityTag string) *CustomchannelsListCall
func (c *CustomchannelsListCall) MaxResults(maxResults int64) *CustomchannelsListCall
func (c *CustomchannelsListCall) PageToken(pageToken string) *CustomchannelsListCall
func (c *CustomchannelsListCall) Pages(ctx context.Context, f func(*CustomChannels) error) error
type CustomchannelsService
func NewCustomchannelsService(s *Service) *CustomchannelsService
func (r *CustomchannelsService) Get(adClientId string, customChannelId string) *CustomchannelsGetCall
func (r *CustomchannelsService) List(adClientId string) *CustomchannelsListCall
type Metadata
func (s *Metadata) MarshalJSON() ([]byte, error)
type MetadataDimensionsListCall
func (c *MetadataDimensionsListCall) Context(ctx context.Context) *MetadataDimensionsListCall
func (c *MetadataDimensionsListCall) Do(opts ...googleapi.CallOption) (*Metadata, error)
func (c *MetadataDimensionsListCall) Fields(s ...googleapi.Field) *MetadataDimensionsListCall
func (c *MetadataDimensionsListCall) Header() http.Header
func (c *MetadataDimensionsListCall) IfNoneMatch(entityTag string) *MetadataDimensionsListCall
type MetadataDimensionsService
func NewMetadataDimensionsService(s *Service) *MetadataDimensionsService
func (r *MetadataDimensionsService) List() *MetadataDimensionsListCall
type MetadataMetricsListCall
func (c *MetadataMetricsListCall) Context(ctx context.Context) *MetadataMetricsListCall
func (c *MetadataMetricsListCall) Do(opts ...googleapi.CallOption) (*Metadata, error)
func (c *MetadataMetricsListCall) Fields(s ...googleapi.Field) *MetadataMetricsListCall
func (c *MetadataMetricsListCall) Header() http.Header
func (c *MetadataMetricsListCall) IfNoneMatch(entityTag string) *MetadataMetricsListCall
type MetadataMetricsService
func NewMetadataMetricsService(s *Service) *MetadataMetricsService
func (r *MetadataMetricsService) List() *MetadataMetricsListCall
type MetadataService
func NewMetadataService(s *Service) *MetadataService
type Payment
func (s *Payment) MarshalJSON() ([]byte, error)
type Payments
func (s *Payments) MarshalJSON() ([]byte, error)
type PaymentsListCall
func (c *PaymentsListCall) Context(ctx context.Context) *PaymentsListCall
func (c *PaymentsListCall) Do(opts ...googleapi.CallOption) (*Payments, error)
func (c *PaymentsListCall) Fields(s ...googleapi.Field) *PaymentsListCall
func (c *PaymentsListCall) Header() http.Header
func (c *PaymentsListCall) IfNoneMatch(entityTag string) *PaymentsListCall
type PaymentsService
func NewPaymentsService(s *Service) *PaymentsService
func (r *PaymentsService) List() *PaymentsListCall
type ReportingMetadataEntry
func (s *ReportingMetadataEntry) MarshalJSON() ([]byte, error)
type ReportsGenerateCall
func (c *ReportsGenerateCall) AccountId(accountId ...string) *ReportsGenerateCall
func (c *ReportsGenerateCall) Context(ctx context.Context) *ReportsGenerateCall
func (c *ReportsGenerateCall) Currency(currency string) *ReportsGenerateCall
func (c *ReportsGenerateCall) Dimension(dimension ...string) *ReportsGenerateCall
func (c *ReportsGenerateCall) Do(opts ...googleapi.CallOption) (*AdsenseReportsGenerateResponse, error)
func (c *ReportsGenerateCall) Download(opts ...googleapi.CallOption) (*http.Response, error)
func (c *ReportsGenerateCall) Fields(s ...googleapi.Field) *ReportsGenerateCall
func (c *ReportsGenerateCall) Filter(filter ...string) *ReportsGenerateCall
func (c *ReportsGenerateCall) Header() http.Header
func (c *ReportsGenerateCall) IfNoneMatch(entityTag string) *ReportsGenerateCall
func (c *ReportsGenerateCall) Locale(locale string) *ReportsGenerateCall
func (c *ReportsGenerateCall) MaxResults(maxResults int64) *ReportsGenerateCall
func (c *ReportsGenerateCall) Metric(metric ...string) *ReportsGenerateCall
func (c *ReportsGenerateCall) Sort(sort ...string) *ReportsGenerateCall
func (c *ReportsGenerateCall) StartIndex(startIndex int64) *ReportsGenerateCall
func (c *ReportsGenerateCall) UseTimezoneReporting(useTimezoneReporting bool) *ReportsGenerateCall
type ReportsSavedGenerateCall
func (c *ReportsSavedGenerateCall) Context(ctx context.Context) *ReportsSavedGenerateCall
func (c *ReportsSavedGenerateCall) Do(opts ...googleapi.CallOption) (*AdsenseReportsGenerateResponse, error)
func (c *ReportsSavedGenerateCall) Fields(s ...googleapi.Field) *ReportsSavedGenerateCall
func (c *ReportsSavedGenerateCall) Header() http.Header
func (c *ReportsSavedGenerateCall) IfNoneMatch(entityTag string) *ReportsSavedGenerateCall
func (c *ReportsSavedGenerateCall) Locale(locale string) *ReportsSavedGenerateCall
func (c *ReportsSavedGenerateCall) MaxResults(maxResults int64) *ReportsSavedGenerateCall
func (c *ReportsSavedGenerateCall) StartIndex(startIndex int64) *ReportsSavedGenerateCall
type ReportsSavedListCall
func (c *ReportsSavedListCall) Context(ctx context.Context) *ReportsSavedListCall
func (c *ReportsSavedListCall) Do(opts ...googleapi.CallOption) (*SavedReports, error)
func (c *ReportsSavedListCall) Fields(s ...googleapi.Field) *ReportsSavedListCall
func (c *ReportsSavedListCall) Header() http.Header
func (c *ReportsSavedListCall) IfNoneMatch(entityTag string) *ReportsSavedListCall
func (c *ReportsSavedListCall) MaxResults(maxResults int64) *ReportsSavedListCall
func (c *ReportsSavedListCall) PageToken(pageToken string) *ReportsSavedListCall
func (c *ReportsSavedListCall) Pages(ctx context.Context, f func(*SavedReports) error) error
type ReportsSavedService
func NewReportsSavedService(s *Service) *ReportsSavedService
func (r *ReportsSavedService) Generate(savedReportId string) *ReportsSavedGenerateCall
func (r *ReportsSavedService) List() *ReportsSavedListCall
type ReportsService
func NewReportsService(s *Service) *ReportsService
func (r *ReportsService) Generate(startDate string, endDate string) *ReportsGenerateCall
type SavedAdStyle
func (s *SavedAdStyle) MarshalJSON() ([]byte, error)
type SavedAdStyles
func (s *SavedAdStyles) MarshalJSON() ([]byte, error)
type SavedReport
func (s *SavedReport) MarshalJSON() ([]byte, error)
type SavedReports
func (s *SavedReports) MarshalJSON() ([]byte, error)
type SavedadstylesGetCall
func (c *SavedadstylesGetCall) Context(ctx context.Context) *SavedadstylesGetCall
func (c *SavedadstylesGetCall) Do(opts ...googleapi.CallOption) (*SavedAdStyle, error)
func (c *SavedadstylesGetCall) Fields(s ...googleapi.Field) *SavedadstylesGetCall
func (c *SavedadstylesGetCall) Header() http.Header
func (c *SavedadstylesGetCall) IfNoneMatch(entityTag string) *SavedadstylesGetCall
type SavedadstylesListCall
func (c *SavedadstylesListCall) Context(ctx context.Context) *SavedadstylesListCall
func (c *SavedadstylesListCall) Do(opts ...googleapi.CallOption) (*SavedAdStyles, error)
func (c *SavedadstylesListCall) Fields(s ...googleapi.Field) *SavedadstylesListCall
func (c *SavedadstylesListCall) Header() http.Header
func (c *SavedadstylesListCall) IfNoneMatch(entityTag string) *SavedadstylesListCall
func (c *SavedadstylesListCall) MaxResults(maxResults int64) *SavedadstylesListCall
func (c *SavedadstylesListCall) PageToken(pageToken string) *SavedadstylesListCall
func (c *SavedadstylesListCall) Pages(ctx context.Context, f func(*SavedAdStyles) error) error
type SavedadstylesService
func NewSavedadstylesService(s *Service) *SavedadstylesService
func (r *SavedadstylesService) Get(savedAdStyleId string) *SavedadstylesGetCall
func (r *SavedadstylesService) List() *SavedadstylesListCall
type Service
func New(client *http.Client) (*Service, error)DEPRECATED
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)
type UrlChannel
func (s *UrlChannel) MarshalJSON() ([]byte, error)
type UrlChannels
func (s *UrlChannels) MarshalJSON() ([]byte, error)
type UrlchannelsListCall
func (c *UrlchannelsListCall) Context(ctx context.Context) *UrlchannelsListCall
func (c *UrlchannelsListCall) Do(opts ...googleapi.CallOption) (*UrlChannels, error)
func (c *UrlchannelsListCall) Fields(s ...googleapi.Field) *UrlchannelsListCall
func (c *UrlchannelsListCall) Header() http.Header
func (c *UrlchannelsListCall) IfNoneMatch(entityTag string) *UrlchannelsListCall
func (c *UrlchannelsListCall) MaxResults(maxResults int64) *UrlchannelsListCall
func (c *UrlchannelsListCall) PageToken(pageToken string) *UrlchannelsListCall
func (c *UrlchannelsListCall) Pages(ctx context.Context, f func(*UrlChannels) error) error
type UrlchannelsService
func NewUrlchannelsService(s *Service) *UrlchannelsService
func (r *UrlchannelsService) List(adClientId string) *UrlchannelsListCall
Constants ¶
View Source
const (
	// View and manage your AdSense data
	AdsenseScope = "https://www.googleapis.com/auth/adsense"

	// View your AdSense data
	AdsenseReadonlyScope = "https://www.googleapis.com/auth/adsense.readonly"
)

OAuth2 scopes used by this API.

Variables ¶

This section is empty.

Functions ¶

This section is empty.

Types ¶
type Account ¶
type Account struct {
	CreationTime int64 `json:"creation_time,omitempty,string"`

	// Id: Unique identifier of this account.
	Id string `json:"id,omitempty"`

	// Kind: Kind of resource this is, in this case adsense#account.
	Kind string `json:"kind,omitempty"`

	// Name: Name of this account.
	Name string `json:"name,omitempty"`

	// Premium: Whether this account is premium.
	Premium bool `json:"premium,omitempty"`

	// SubAccounts: Sub accounts of the this account.
	SubAccounts []*Account `json:"subAccounts,omitempty"`

	// Timezone: AdSense timezone of this account.
	Timezone string `json:"timezone,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "CreationTime") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "CreationTime") to include
	// in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. However, any field with
	// an empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*Account) MarshalJSON ¶
func (s *Account) MarshalJSON() ([]byte, error)
type Accounts ¶
type Accounts struct {
	// Etag: ETag of this response for caching purposes.
	Etag string `json:"etag,omitempty"`

	// Items: The accounts returned in this list response.
	Items []*Account `json:"items,omitempty"`

	// Kind: Kind of list this is, in this case adsense#accounts.
	Kind string `json:"kind,omitempty"`

	// NextPageToken: Continuation token used to page through accounts. To
	// retrieve the next page of results, set the next request's "pageToken"
	// value to this.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "Etag") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Etag") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*Accounts) MarshalJSON ¶
func (s *Accounts) MarshalJSON() ([]byte, error)
type AccountsAdclientsGetAdCodeCall ¶
type AccountsAdclientsGetAdCodeCall struct {
	// contains filtered or unexported fields
}
func (*AccountsAdclientsGetAdCodeCall) Context ¶
func (c *AccountsAdclientsGetAdCodeCall) Context(ctx context.Context) *AccountsAdclientsGetAdCodeCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*AccountsAdclientsGetAdCodeCall) Do ¶
func (c *AccountsAdclientsGetAdCodeCall) Do(opts ...googleapi.CallOption) (*AdCode, error)

Do executes the "adsense.accounts.adclients.getAdCode" call. Exactly one of *AdCode or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AdCode.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsAdclientsGetAdCodeCall) Fields ¶
func (c *AccountsAdclientsGetAdCodeCall) Fields(s ...googleapi.Field) *AccountsAdclientsGetAdCodeCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*AccountsAdclientsGetAdCodeCall) Header ¶
func (c *AccountsAdclientsGetAdCodeCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*AccountsAdclientsGetAdCodeCall) IfNoneMatch ¶
func (c *AccountsAdclientsGetAdCodeCall) IfNoneMatch(entityTag string) *AccountsAdclientsGetAdCodeCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (*AccountsAdclientsGetAdCodeCall) TagPartner ¶
added in v0.33.0
func (c *AccountsAdclientsGetAdCodeCall) TagPartner(tagPartner string) *AccountsAdclientsGetAdCodeCall

TagPartner sets the optional parameter "tagPartner": Tag partner to include in the ad code snippet.

type AccountsAdclientsListCall ¶
type AccountsAdclientsListCall struct {
	// contains filtered or unexported fields
}
func (*AccountsAdclientsListCall) Context ¶
func (c *AccountsAdclientsListCall) Context(ctx context.Context) *AccountsAdclientsListCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*AccountsAdclientsListCall) Do ¶
func (c *AccountsAdclientsListCall) Do(opts ...googleapi.CallOption) (*AdClients, error)

Do executes the "adsense.accounts.adclients.list" call. Exactly one of *AdClients or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AdClients.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsAdclientsListCall) Fields ¶
func (c *AccountsAdclientsListCall) Fields(s ...googleapi.Field) *AccountsAdclientsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*AccountsAdclientsListCall) Header ¶
func (c *AccountsAdclientsListCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*AccountsAdclientsListCall) IfNoneMatch ¶
func (c *AccountsAdclientsListCall) IfNoneMatch(entityTag string) *AccountsAdclientsListCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (*AccountsAdclientsListCall) MaxResults ¶
func (c *AccountsAdclientsListCall) MaxResults(maxResults int64) *AccountsAdclientsListCall

MaxResults sets the optional parameter "maxResults": The maximum number of ad clients to include in the response, used for paging.

func (*AccountsAdclientsListCall) PageToken ¶
func (c *AccountsAdclientsListCall) PageToken(pageToken string) *AccountsAdclientsListCall

PageToken sets the optional parameter "pageToken": A continuation token, used to page through ad clients. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

func (*AccountsAdclientsListCall) Pages ¶
func (c *AccountsAdclientsListCall) Pages(ctx context.Context, f func(*AdClients) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsAdclientsService ¶
type AccountsAdclientsService struct {
	// contains filtered or unexported fields
}
func NewAccountsAdclientsService ¶
func NewAccountsAdclientsService(s *Service) *AccountsAdclientsService
func (*AccountsAdclientsService) GetAdCode ¶
func (r *AccountsAdclientsService) GetAdCode(accountId string, adClientId string) *AccountsAdclientsGetAdCodeCall

GetAdCode: Get Auto ad code for a given ad client.

- accountId: Account which contains the ad client. - adClientId: Ad client to get the code for.

func (*AccountsAdclientsService) List ¶
func (r *AccountsAdclientsService) List(accountId string) *AccountsAdclientsListCall

List: List all ad clients in the specified account.

- accountId: Account for which to list ad clients.

type AccountsAdunitsCustomchannelsListCall ¶
type AccountsAdunitsCustomchannelsListCall struct {
	// contains filtered or unexported fields
}
func (*AccountsAdunitsCustomchannelsListCall) Context ¶
func (c *AccountsAdunitsCustomchannelsListCall) Context(ctx context.Context) *AccountsAdunitsCustomchannelsListCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*AccountsAdunitsCustomchannelsListCall) Do ¶
func (c *AccountsAdunitsCustomchannelsListCall) Do(opts ...googleapi.CallOption) (*CustomChannels, error)

Do executes the "adsense.accounts.adunits.customchannels.list" call. Exactly one of *CustomChannels or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *CustomChannels.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsAdunitsCustomchannelsListCall) Fields ¶
func (c *AccountsAdunitsCustomchannelsListCall) Fields(s ...googleapi.Field) *AccountsAdunitsCustomchannelsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*AccountsAdunitsCustomchannelsListCall) Header ¶
func (c *AccountsAdunitsCustomchannelsListCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*AccountsAdunitsCustomchannelsListCall) IfNoneMatch ¶
func (c *AccountsAdunitsCustomchannelsListCall) IfNoneMatch(entityTag string) *AccountsAdunitsCustomchannelsListCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (*AccountsAdunitsCustomchannelsListCall) MaxResults ¶
func (c *AccountsAdunitsCustomchannelsListCall) MaxResults(maxResults int64) *AccountsAdunitsCustomchannelsListCall

MaxResults sets the optional parameter "maxResults": The maximum number of custom channels to include in the response, used for paging.

func (*AccountsAdunitsCustomchannelsListCall) PageToken ¶
func (c *AccountsAdunitsCustomchannelsListCall) PageToken(pageToken string) *AccountsAdunitsCustomchannelsListCall

PageToken sets the optional parameter "pageToken": A continuation token, used to page through custom channels. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

func (*AccountsAdunitsCustomchannelsListCall) Pages ¶
func (c *AccountsAdunitsCustomchannelsListCall) Pages(ctx context.Context, f func(*CustomChannels) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsAdunitsCustomchannelsService ¶
type AccountsAdunitsCustomchannelsService struct {
	// contains filtered or unexported fields
}
func NewAccountsAdunitsCustomchannelsService ¶
func NewAccountsAdunitsCustomchannelsService(s *Service) *AccountsAdunitsCustomchannelsService
func (*AccountsAdunitsCustomchannelsService) List ¶
func (r *AccountsAdunitsCustomchannelsService) List(accountId string, adClientId string, adUnitId string) *AccountsAdunitsCustomchannelsListCall

List: List all custom channels which the specified ad unit belongs to.

- accountId: Account to which the ad client belongs. - adClientId: Ad client which contains the ad unit. - adUnitId: Ad unit for which to list custom channels.

type AccountsAdunitsGetAdCodeCall ¶
type AccountsAdunitsGetAdCodeCall struct {
	// contains filtered or unexported fields
}
func (*AccountsAdunitsGetAdCodeCall) Context ¶
func (c *AccountsAdunitsGetAdCodeCall) Context(ctx context.Context) *AccountsAdunitsGetAdCodeCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*AccountsAdunitsGetAdCodeCall) Do ¶
func (c *AccountsAdunitsGetAdCodeCall) Do(opts ...googleapi.CallOption) (*AdCode, error)

Do executes the "adsense.accounts.adunits.getAdCode" call. Exactly one of *AdCode or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AdCode.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsAdunitsGetAdCodeCall) Fields ¶
func (c *AccountsAdunitsGetAdCodeCall) Fields(s ...googleapi.Field) *AccountsAdunitsGetAdCodeCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*AccountsAdunitsGetAdCodeCall) Header ¶
func (c *AccountsAdunitsGetAdCodeCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*AccountsAdunitsGetAdCodeCall) IfNoneMatch ¶
func (c *AccountsAdunitsGetAdCodeCall) IfNoneMatch(entityTag string) *AccountsAdunitsGetAdCodeCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type AccountsAdunitsGetCall ¶
type AccountsAdunitsGetCall struct {
	// contains filtered or unexported fields
}
func (*AccountsAdunitsGetCall) Context ¶
func (c *AccountsAdunitsGetCall) Context(ctx context.Context) *AccountsAdunitsGetCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*AccountsAdunitsGetCall) Do ¶
func (c *AccountsAdunitsGetCall) Do(opts ...googleapi.CallOption) (*AdUnit, error)

Do executes the "adsense.accounts.adunits.get" call. Exactly one of *AdUnit or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AdUnit.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsAdunitsGetCall) Fields ¶
func (c *AccountsAdunitsGetCall) Fields(s ...googleapi.Field) *AccountsAdunitsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*AccountsAdunitsGetCall) Header ¶
func (c *AccountsAdunitsGetCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*AccountsAdunitsGetCall) IfNoneMatch ¶
func (c *AccountsAdunitsGetCall) IfNoneMatch(entityTag string) *AccountsAdunitsGetCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type AccountsAdunitsListCall ¶
type AccountsAdunitsListCall struct {
	// contains filtered or unexported fields
}
func (*AccountsAdunitsListCall) Context ¶
func (c *AccountsAdunitsListCall) Context(ctx context.Context) *AccountsAdunitsListCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*AccountsAdunitsListCall) Do ¶
func (c *AccountsAdunitsListCall) Do(opts ...googleapi.CallOption) (*AdUnits, error)

Do executes the "adsense.accounts.adunits.list" call. Exactly one of *AdUnits or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AdUnits.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsAdunitsListCall) Fields ¶
func (c *AccountsAdunitsListCall) Fields(s ...googleapi.Field) *AccountsAdunitsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*AccountsAdunitsListCall) Header ¶
func (c *AccountsAdunitsListCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*AccountsAdunitsListCall) IfNoneMatch ¶
func (c *AccountsAdunitsListCall) IfNoneMatch(entityTag string) *AccountsAdunitsListCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (*AccountsAdunitsListCall) IncludeInactive ¶
func (c *AccountsAdunitsListCall) IncludeInactive(includeInactive bool) *AccountsAdunitsListCall

IncludeInactive sets the optional parameter "includeInactive": Whether to include inactive ad units. Default: true.

func (*AccountsAdunitsListCall) MaxResults ¶
func (c *AccountsAdunitsListCall) MaxResults(maxResults int64) *AccountsAdunitsListCall

MaxResults sets the optional parameter "maxResults": The maximum number of ad units to include in the response, used for paging.

func (*AccountsAdunitsListCall) PageToken ¶
func (c *AccountsAdunitsListCall) PageToken(pageToken string) *AccountsAdunitsListCall

PageToken sets the optional parameter "pageToken": A continuation token, used to page through ad units. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

func (*AccountsAdunitsListCall) Pages ¶
func (c *AccountsAdunitsListCall) Pages(ctx context.Context, f func(*AdUnits) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsAdunitsService ¶
type AccountsAdunitsService struct {
	Customchannels *AccountsAdunitsCustomchannelsService
	// contains filtered or unexported fields
}
func NewAccountsAdunitsService ¶
func NewAccountsAdunitsService(s *Service) *AccountsAdunitsService
func (*AccountsAdunitsService) Get ¶
func (r *AccountsAdunitsService) Get(accountId string, adClientId string, adUnitId string) *AccountsAdunitsGetCall

Get: Gets the specified ad unit in the specified ad client for the specified account.

- accountId: Account to which the ad client belongs. - adClientId: Ad client for which to get the ad unit. - adUnitId: Ad unit to retrieve.

func (*AccountsAdunitsService) GetAdCode ¶
func (r *AccountsAdunitsService) GetAdCode(accountId string, adClientId string, adUnitId string) *AccountsAdunitsGetAdCodeCall

GetAdCode: Get ad code for the specified ad unit.

- accountId: Account which contains the ad client. - adClientId: Ad client with contains the ad unit. - adUnitId: Ad unit to get the code for.

func (*AccountsAdunitsService) List ¶
func (r *AccountsAdunitsService) List(accountId string, adClientId string) *AccountsAdunitsListCall

List: List all ad units in the specified ad client for the specified account.

- accountId: Account to which the ad client belongs. - adClientId: Ad client for which to list ad units.

type AccountsAlertsDeleteCall ¶
type AccountsAlertsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*AccountsAlertsDeleteCall) Context ¶
func (c *AccountsAlertsDeleteCall) Context(ctx context.Context) *AccountsAlertsDeleteCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*AccountsAlertsDeleteCall) Do ¶
func (c *AccountsAlertsDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "adsense.accounts.alerts.delete" call.

func (*AccountsAlertsDeleteCall) Fields ¶
func (c *AccountsAlertsDeleteCall) Fields(s ...googleapi.Field) *AccountsAlertsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*AccountsAlertsDeleteCall) Header ¶
func (c *AccountsAlertsDeleteCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type AccountsAlertsListCall ¶
type AccountsAlertsListCall struct {
	// contains filtered or unexported fields
}
func (*AccountsAlertsListCall) Context ¶
func (c *AccountsAlertsListCall) Context(ctx context.Context) *AccountsAlertsListCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*AccountsAlertsListCall) Do ¶
func (c *AccountsAlertsListCall) Do(opts ...googleapi.CallOption) (*Alerts, error)

Do executes the "adsense.accounts.alerts.list" call. Exactly one of *Alerts or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Alerts.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsAlertsListCall) Fields ¶
func (c *AccountsAlertsListCall) Fields(s ...googleapi.Field) *AccountsAlertsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*AccountsAlertsListCall) Header ¶
func (c *AccountsAlertsListCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*AccountsAlertsListCall) IfNoneMatch ¶
func (c *AccountsAlertsListCall) IfNoneMatch(entityTag string) *AccountsAlertsListCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (*AccountsAlertsListCall) Locale ¶
func (c *AccountsAlertsListCall) Locale(locale string) *AccountsAlertsListCall

Locale sets the optional parameter "locale": The locale to use for translating alert messages. The account locale will be used if this is not supplied. The AdSense default (English) will be used if the supplied locale is invalid or unsupported.

type AccountsAlertsService ¶
type AccountsAlertsService struct {
	// contains filtered or unexported fields
}
func NewAccountsAlertsService ¶
func NewAccountsAlertsService(s *Service) *AccountsAlertsService
func (*AccountsAlertsService) Delete ¶
func (r *AccountsAlertsService) Delete(accountId string, alertId string) *AccountsAlertsDeleteCall

Delete: Dismiss (delete) the specified alert from the specified publisher AdSense account.

- accountId: Account which contains the ad unit. - alertId: Alert to delete.

func (*AccountsAlertsService) List ¶
func (r *AccountsAlertsService) List(accountId string) *AccountsAlertsListCall

List: List the alerts for the specified AdSense account.

- accountId: Account for which to retrieve the alerts.

type AccountsCustomchannelsAdunitsListCall ¶
type AccountsCustomchannelsAdunitsListCall struct {
	// contains filtered or unexported fields
}
func (*AccountsCustomchannelsAdunitsListCall) Context ¶
func (c *AccountsCustomchannelsAdunitsListCall) Context(ctx context.Context) *AccountsCustomchannelsAdunitsListCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*AccountsCustomchannelsAdunitsListCall) Do ¶
func (c *AccountsCustomchannelsAdunitsListCall) Do(opts ...googleapi.CallOption) (*AdUnits, error)

Do executes the "adsense.accounts.customchannels.adunits.list" call. Exactly one of *AdUnits or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AdUnits.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsCustomchannelsAdunitsListCall) Fields ¶
func (c *AccountsCustomchannelsAdunitsListCall) Fields(s ...googleapi.Field) *AccountsCustomchannelsAdunitsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*AccountsCustomchannelsAdunitsListCall) Header ¶
func (c *AccountsCustomchannelsAdunitsListCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*AccountsCustomchannelsAdunitsListCall) IfNoneMatch ¶
func (c *AccountsCustomchannelsAdunitsListCall) IfNoneMatch(entityTag string) *AccountsCustomchannelsAdunitsListCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (*AccountsCustomchannelsAdunitsListCall) IncludeInactive ¶
func (c *AccountsCustomchannelsAdunitsListCall) IncludeInactive(includeInactive bool) *AccountsCustomchannelsAdunitsListCall

IncludeInactive sets the optional parameter "includeInactive": Whether to include inactive ad units. Default: true.

func (*AccountsCustomchannelsAdunitsListCall) MaxResults ¶
func (c *AccountsCustomchannelsAdunitsListCall) MaxResults(maxResults int64) *AccountsCustomchannelsAdunitsListCall

MaxResults sets the optional parameter "maxResults": The maximum number of ad units to include in the response, used for paging.

func (*AccountsCustomchannelsAdunitsListCall) PageToken ¶
func (c *AccountsCustomchannelsAdunitsListCall) PageToken(pageToken string) *AccountsCustomchannelsAdunitsListCall

PageToken sets the optional parameter "pageToken": A continuation token, used to page through ad units. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

func (*AccountsCustomchannelsAdunitsListCall) Pages ¶
func (c *AccountsCustomchannelsAdunitsListCall) Pages(ctx context.Context, f func(*AdUnits) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsCustomchannelsAdunitsService ¶
type AccountsCustomchannelsAdunitsService struct {
	// contains filtered or unexported fields
}
func NewAccountsCustomchannelsAdunitsService ¶
func NewAccountsCustomchannelsAdunitsService(s *Service) *AccountsCustomchannelsAdunitsService
func (*AccountsCustomchannelsAdunitsService) List ¶
func (r *AccountsCustomchannelsAdunitsService) List(accountId string, adClientId string, customChannelId string) *AccountsCustomchannelsAdunitsListCall

List: List all ad units in the specified custom channel.

- accountId: Account to which the ad client belongs. - adClientId: Ad client which contains the custom channel. - customChannelId: Custom channel for which to list ad units.

type AccountsCustomchannelsGetCall ¶
type AccountsCustomchannelsGetCall struct {
	// contains filtered or unexported fields
}
func (*AccountsCustomchannelsGetCall) Context ¶
func (c *AccountsCustomchannelsGetCall) Context(ctx context.Context) *AccountsCustomchannelsGetCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*AccountsCustomchannelsGetCall) Do ¶
func (c *AccountsCustomchannelsGetCall) Do(opts ...googleapi.CallOption) (*CustomChannel, error)

Do executes the "adsense.accounts.customchannels.get" call. Exactly one of *CustomChannel or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *CustomChannel.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsCustomchannelsGetCall) Fields ¶
func (c *AccountsCustomchannelsGetCall) Fields(s ...googleapi.Field) *AccountsCustomchannelsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*AccountsCustomchannelsGetCall) Header ¶
func (c *AccountsCustomchannelsGetCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*AccountsCustomchannelsGetCall) IfNoneMatch ¶
func (c *AccountsCustomchannelsGetCall) IfNoneMatch(entityTag string) *AccountsCustomchannelsGetCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type AccountsCustomchannelsListCall ¶
type AccountsCustomchannelsListCall struct {
	// contains filtered or unexported fields
}
func (*AccountsCustomchannelsListCall) Context ¶
func (c *AccountsCustomchannelsListCall) Context(ctx context.Context) *AccountsCustomchannelsListCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*AccountsCustomchannelsListCall) Do ¶
func (c *AccountsCustomchannelsListCall) Do(opts ...googleapi.CallOption) (*CustomChannels, error)

Do executes the "adsense.accounts.customchannels.list" call. Exactly one of *CustomChannels or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *CustomChannels.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsCustomchannelsListCall) Fields ¶
func (c *AccountsCustomchannelsListCall) Fields(s ...googleapi.Field) *AccountsCustomchannelsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*AccountsCustomchannelsListCall) Header ¶
func (c *AccountsCustomchannelsListCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*AccountsCustomchannelsListCall) IfNoneMatch ¶
func (c *AccountsCustomchannelsListCall) IfNoneMatch(entityTag string) *AccountsCustomchannelsListCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (*AccountsCustomchannelsListCall) MaxResults ¶
func (c *AccountsCustomchannelsListCall) MaxResults(maxResults int64) *AccountsCustomchannelsListCall

MaxResults sets the optional parameter "maxResults": The maximum number of custom channels to include in the response, used for paging.

func (*AccountsCustomchannelsListCall) PageToken ¶
func (c *AccountsCustomchannelsListCall) PageToken(pageToken string) *AccountsCustomchannelsListCall

PageToken sets the optional parameter "pageToken": A continuation token, used to page through custom channels. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

func (*AccountsCustomchannelsListCall) Pages ¶
func (c *AccountsCustomchannelsListCall) Pages(ctx context.Context, f func(*CustomChannels) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsCustomchannelsService ¶
type AccountsCustomchannelsService struct {
	Adunits *AccountsCustomchannelsAdunitsService
	// contains filtered or unexported fields
}
func NewAccountsCustomchannelsService ¶
func NewAccountsCustomchannelsService(s *Service) *AccountsCustomchannelsService
func (*AccountsCustomchannelsService) Get ¶
func (r *AccountsCustomchannelsService) Get(accountId string, adClientId string, customChannelId string) *AccountsCustomchannelsGetCall

Get: Get the specified custom channel from the specified ad client for the specified account.

- accountId: Account to which the ad client belongs. - adClientId: Ad client which contains the custom channel. - customChannelId: Custom channel to retrieve.

func (*AccountsCustomchannelsService) List ¶
func (r *AccountsCustomchannelsService) List(accountId string, adClientId string) *AccountsCustomchannelsListCall

List: List all custom channels in the specified ad client for the specified account.

- accountId: Account to which the ad client belongs. - adClientId: Ad client for which to list custom channels.

type AccountsGetCall ¶
type AccountsGetCall struct {
	// contains filtered or unexported fields
}
func (*AccountsGetCall) Context ¶
func (c *AccountsGetCall) Context(ctx context.Context) *AccountsGetCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*AccountsGetCall) Do ¶
func (c *AccountsGetCall) Do(opts ...googleapi.CallOption) (*Account, error)

Do executes the "adsense.accounts.get" call. Exactly one of *Account or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Account.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsGetCall) Fields ¶
func (c *AccountsGetCall) Fields(s ...googleapi.Field) *AccountsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*AccountsGetCall) Header ¶
func (c *AccountsGetCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*AccountsGetCall) IfNoneMatch ¶
func (c *AccountsGetCall) IfNoneMatch(entityTag string) *AccountsGetCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (*AccountsGetCall) Tree ¶
func (c *AccountsGetCall) Tree(tree bool) *AccountsGetCall

Tree sets the optional parameter "tree": Whether the tree of sub accounts should be returned.

type AccountsListCall ¶
type AccountsListCall struct {
	// contains filtered or unexported fields
}
func (*AccountsListCall) Context ¶
func (c *AccountsListCall) Context(ctx context.Context) *AccountsListCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*AccountsListCall) Do ¶
func (c *AccountsListCall) Do(opts ...googleapi.CallOption) (*Accounts, error)

Do executes the "adsense.accounts.list" call. Exactly one of *Accounts or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Accounts.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsListCall) Fields ¶
func (c *AccountsListCall) Fields(s ...googleapi.Field) *AccountsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*AccountsListCall) Header ¶
func (c *AccountsListCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*AccountsListCall) IfNoneMatch ¶
func (c *AccountsListCall) IfNoneMatch(entityTag string) *AccountsListCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (*AccountsListCall) MaxResults ¶
func (c *AccountsListCall) MaxResults(maxResults int64) *AccountsListCall

MaxResults sets the optional parameter "maxResults": The maximum number of accounts to include in the response, used for paging.

func (*AccountsListCall) PageToken ¶
func (c *AccountsListCall) PageToken(pageToken string) *AccountsListCall

PageToken sets the optional parameter "pageToken": A continuation token, used to page through accounts. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

func (*AccountsListCall) Pages ¶
func (c *AccountsListCall) Pages(ctx context.Context, f func(*Accounts) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsPaymentsListCall ¶
type AccountsPaymentsListCall struct {
	// contains filtered or unexported fields
}
func (*AccountsPaymentsListCall) Context ¶
func (c *AccountsPaymentsListCall) Context(ctx context.Context) *AccountsPaymentsListCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*AccountsPaymentsListCall) Do ¶
func (c *AccountsPaymentsListCall) Do(opts ...googleapi.CallOption) (*Payments, error)

Do executes the "adsense.accounts.payments.list" call. Exactly one of *Payments or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Payments.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsPaymentsListCall) Fields ¶
func (c *AccountsPaymentsListCall) Fields(s ...googleapi.Field) *AccountsPaymentsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*AccountsPaymentsListCall) Header ¶
func (c *AccountsPaymentsListCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*AccountsPaymentsListCall) IfNoneMatch ¶
func (c *AccountsPaymentsListCall) IfNoneMatch(entityTag string) *AccountsPaymentsListCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type AccountsPaymentsService ¶
type AccountsPaymentsService struct {
	// contains filtered or unexported fields
}
func NewAccountsPaymentsService ¶
func NewAccountsPaymentsService(s *Service) *AccountsPaymentsService
func (*AccountsPaymentsService) List ¶
func (r *AccountsPaymentsService) List(accountId string) *AccountsPaymentsListCall

List: List the payments for the specified AdSense account.

- accountId: Account for which to retrieve the payments.

type AccountsReportsGenerateCall ¶
type AccountsReportsGenerateCall struct {
	// contains filtered or unexported fields
}
func (*AccountsReportsGenerateCall) Context ¶
func (c *AccountsReportsGenerateCall) Context(ctx context.Context) *AccountsReportsGenerateCall

Context sets the context to be used in this call's Do and Download methods. Any pending HTTP request will be aborted if the provided context is canceled.

func (*AccountsReportsGenerateCall) Currency ¶
func (c *AccountsReportsGenerateCall) Currency(currency string) *AccountsReportsGenerateCall

Currency sets the optional parameter "currency": Optional currency to use when reporting on monetary metrics. Defaults to the account's currency if not set.

func (*AccountsReportsGenerateCall) Dimension ¶
func (c *AccountsReportsGenerateCall) Dimension(dimension ...string) *AccountsReportsGenerateCall

Dimension sets the optional parameter "dimension": Dimensions to base the report on.

func (*AccountsReportsGenerateCall) Do ¶
func (c *AccountsReportsGenerateCall) Do(opts ...googleapi.CallOption) (*AdsenseReportsGenerateResponse, error)

Do executes the "adsense.accounts.reports.generate" call. Exactly one of *AdsenseReportsGenerateResponse or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AdsenseReportsGenerateResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsReportsGenerateCall) Download ¶
func (c *AccountsReportsGenerateCall) Download(opts ...googleapi.CallOption) (*http.Response, error)

Download fetches the API endpoint's "media" value, instead of the normal API response value. If the returned error is nil, the Response is guaranteed to have a 2xx status code. Callers must close the Response.Body as usual.

func (*AccountsReportsGenerateCall) Fields ¶
func (c *AccountsReportsGenerateCall) Fields(s ...googleapi.Field) *AccountsReportsGenerateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*AccountsReportsGenerateCall) Filter ¶
func (c *AccountsReportsGenerateCall) Filter(filter ...string) *AccountsReportsGenerateCall

Filter sets the optional parameter "filter": Filters to be run on the report.

func (*AccountsReportsGenerateCall) Header ¶
func (c *AccountsReportsGenerateCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*AccountsReportsGenerateCall) IfNoneMatch ¶
func (c *AccountsReportsGenerateCall) IfNoneMatch(entityTag string) *AccountsReportsGenerateCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (*AccountsReportsGenerateCall) Locale ¶
func (c *AccountsReportsGenerateCall) Locale(locale string) *AccountsReportsGenerateCall

Locale sets the optional parameter "locale": Optional locale to use for translating report output to a local language. Defaults to "en_US" if not specified.

func (*AccountsReportsGenerateCall) MaxResults ¶
func (c *AccountsReportsGenerateCall) MaxResults(maxResults int64) *AccountsReportsGenerateCall

MaxResults sets the optional parameter "maxResults": The maximum number of rows of report data to return.

func (*AccountsReportsGenerateCall) Metric ¶
func (c *AccountsReportsGenerateCall) Metric(metric ...string) *AccountsReportsGenerateCall

Metric sets the optional parameter "metric": Numeric columns to include in the report.

func (*AccountsReportsGenerateCall) Sort ¶
func (c *AccountsReportsGenerateCall) Sort(sort ...string) *AccountsReportsGenerateCall

Sort sets the optional parameter "sort": The name of a dimension or metric to sort the resulting report on, optionally prefixed with "+" to sort ascending or "-" to sort descending. If no prefix is specified, the column is sorted ascending.

func (*AccountsReportsGenerateCall) StartIndex ¶
func (c *AccountsReportsGenerateCall) StartIndex(startIndex int64) *AccountsReportsGenerateCall

StartIndex sets the optional parameter "startIndex": Index of the first row of report data to return.

func (*AccountsReportsGenerateCall) UseTimezoneReporting ¶
func (c *AccountsReportsGenerateCall) UseTimezoneReporting(useTimezoneReporting bool) *AccountsReportsGenerateCall

UseTimezoneReporting sets the optional parameter "useTimezoneReporting": Whether the report should be generated in the AdSense account's local timezone. If false default PST/PDT timezone will be used.

type AccountsReportsSavedGenerateCall ¶
type AccountsReportsSavedGenerateCall struct {
	// contains filtered or unexported fields
}
func (*AccountsReportsSavedGenerateCall) Context ¶
func (c *AccountsReportsSavedGenerateCall) Context(ctx context.Context) *AccountsReportsSavedGenerateCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*AccountsReportsSavedGenerateCall) Do ¶
func (c *AccountsReportsSavedGenerateCall) Do(opts ...googleapi.CallOption) (*AdsenseReportsGenerateResponse, error)

Do executes the "adsense.accounts.reports.saved.generate" call. Exactly one of *AdsenseReportsGenerateResponse or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AdsenseReportsGenerateResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsReportsSavedGenerateCall) Fields ¶
func (c *AccountsReportsSavedGenerateCall) Fields(s ...googleapi.Field) *AccountsReportsSavedGenerateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*AccountsReportsSavedGenerateCall) Header ¶
func (c *AccountsReportsSavedGenerateCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*AccountsReportsSavedGenerateCall) IfNoneMatch ¶
func (c *AccountsReportsSavedGenerateCall) IfNoneMatch(entityTag string) *AccountsReportsSavedGenerateCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (*AccountsReportsSavedGenerateCall) Locale ¶
func (c *AccountsReportsSavedGenerateCall) Locale(locale string) *AccountsReportsSavedGenerateCall

Locale sets the optional parameter "locale": Optional locale to use for translating report output to a local language. Defaults to "en_US" if not specified.

func (*AccountsReportsSavedGenerateCall) MaxResults ¶
func (c *AccountsReportsSavedGenerateCall) MaxResults(maxResults int64) *AccountsReportsSavedGenerateCall

MaxResults sets the optional parameter "maxResults": The maximum number of rows of report data to return.

func (*AccountsReportsSavedGenerateCall) StartIndex ¶
func (c *AccountsReportsSavedGenerateCall) StartIndex(startIndex int64) *AccountsReportsSavedGenerateCall

StartIndex sets the optional parameter "startIndex": Index of the first row of report data to return.

type AccountsReportsSavedListCall ¶
type AccountsReportsSavedListCall struct {
	// contains filtered or unexported fields
}
func (*AccountsReportsSavedListCall) Context ¶
func (c *AccountsReportsSavedListCall) Context(ctx context.Context) *AccountsReportsSavedListCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*AccountsReportsSavedListCall) Do ¶
func (c *AccountsReportsSavedListCall) Do(opts ...googleapi.CallOption) (*SavedReports, error)

Do executes the "adsense.accounts.reports.saved.list" call. Exactly one of *SavedReports or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *SavedReports.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsReportsSavedListCall) Fields ¶
func (c *AccountsReportsSavedListCall) Fields(s ...googleapi.Field) *AccountsReportsSavedListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*AccountsReportsSavedListCall) Header ¶
func (c *AccountsReportsSavedListCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*AccountsReportsSavedListCall) IfNoneMatch ¶
func (c *AccountsReportsSavedListCall) IfNoneMatch(entityTag string) *AccountsReportsSavedListCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (*AccountsReportsSavedListCall) MaxResults ¶
func (c *AccountsReportsSavedListCall) MaxResults(maxResults int64) *AccountsReportsSavedListCall

MaxResults sets the optional parameter "maxResults": The maximum number of saved reports to include in the response, used for paging.

func (*AccountsReportsSavedListCall) PageToken ¶
func (c *AccountsReportsSavedListCall) PageToken(pageToken string) *AccountsReportsSavedListCall

PageToken sets the optional parameter "pageToken": A continuation token, used to page through saved reports. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

func (*AccountsReportsSavedListCall) Pages ¶
func (c *AccountsReportsSavedListCall) Pages(ctx context.Context, f func(*SavedReports) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsReportsSavedService ¶
type AccountsReportsSavedService struct {
	// contains filtered or unexported fields
}
func NewAccountsReportsSavedService ¶
func NewAccountsReportsSavedService(s *Service) *AccountsReportsSavedService
func (*AccountsReportsSavedService) Generate ¶
func (r *AccountsReportsSavedService) Generate(accountId string, savedReportId string) *AccountsReportsSavedGenerateCall

Generate: Generate an AdSense report based on the saved report ID sent in the query parameters.

- accountId: Account to which the saved reports belong. - savedReportId: The saved report to retrieve.

func (*AccountsReportsSavedService) List ¶
func (r *AccountsReportsSavedService) List(accountId string) *AccountsReportsSavedListCall

List: List all saved reports in the specified AdSense account.

- accountId: Account to which the saved reports belong.

type AccountsReportsService ¶
type AccountsReportsService struct {
	Saved *AccountsReportsSavedService
	// contains filtered or unexported fields
}
func NewAccountsReportsService ¶
func NewAccountsReportsService(s *Service) *AccountsReportsService
func (*AccountsReportsService) Generate ¶
func (r *AccountsReportsService) Generate(accountId string, startDate string, endDate string) *AccountsReportsGenerateCall

Generate: Generate an AdSense report based on the report request sent in the query parameters. Returns the result as JSON; to retrieve output in CSV format specify "alt=csv" as a query parameter.

accountId: Account upon which to report.
endDate: End of the date range to report on in "YYYY-MM-DD" format, inclusive.
startDate: Start of the date range to report on in "YYYY-MM-DD" format, inclusive.
type AccountsSavedadstylesGetCall ¶
type AccountsSavedadstylesGetCall struct {
	// contains filtered or unexported fields
}
func (*AccountsSavedadstylesGetCall) Context ¶
func (c *AccountsSavedadstylesGetCall) Context(ctx context.Context) *AccountsSavedadstylesGetCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*AccountsSavedadstylesGetCall) Do ¶
func (c *AccountsSavedadstylesGetCall) Do(opts ...googleapi.CallOption) (*SavedAdStyle, error)

Do executes the "adsense.accounts.savedadstyles.get" call. Exactly one of *SavedAdStyle or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *SavedAdStyle.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsSavedadstylesGetCall) Fields ¶
func (c *AccountsSavedadstylesGetCall) Fields(s ...googleapi.Field) *AccountsSavedadstylesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*AccountsSavedadstylesGetCall) Header ¶
func (c *AccountsSavedadstylesGetCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*AccountsSavedadstylesGetCall) IfNoneMatch ¶
func (c *AccountsSavedadstylesGetCall) IfNoneMatch(entityTag string) *AccountsSavedadstylesGetCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type AccountsSavedadstylesListCall ¶
type AccountsSavedadstylesListCall struct {
	// contains filtered or unexported fields
}
func (*AccountsSavedadstylesListCall) Context ¶
func (c *AccountsSavedadstylesListCall) Context(ctx context.Context) *AccountsSavedadstylesListCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*AccountsSavedadstylesListCall) Do ¶
func (c *AccountsSavedadstylesListCall) Do(opts ...googleapi.CallOption) (*SavedAdStyles, error)

Do executes the "adsense.accounts.savedadstyles.list" call. Exactly one of *SavedAdStyles or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *SavedAdStyles.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsSavedadstylesListCall) Fields ¶
func (c *AccountsSavedadstylesListCall) Fields(s ...googleapi.Field) *AccountsSavedadstylesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*AccountsSavedadstylesListCall) Header ¶
func (c *AccountsSavedadstylesListCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*AccountsSavedadstylesListCall) IfNoneMatch ¶
func (c *AccountsSavedadstylesListCall) IfNoneMatch(entityTag string) *AccountsSavedadstylesListCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (*AccountsSavedadstylesListCall) MaxResults ¶
func (c *AccountsSavedadstylesListCall) MaxResults(maxResults int64) *AccountsSavedadstylesListCall

MaxResults sets the optional parameter "maxResults": The maximum number of saved ad styles to include in the response, used for paging.

func (*AccountsSavedadstylesListCall) PageToken ¶
func (c *AccountsSavedadstylesListCall) PageToken(pageToken string) *AccountsSavedadstylesListCall

PageToken sets the optional parameter "pageToken": A continuation token, used to page through saved ad styles. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

func (*AccountsSavedadstylesListCall) Pages ¶
func (c *AccountsSavedadstylesListCall) Pages(ctx context.Context, f func(*SavedAdStyles) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsSavedadstylesService ¶
type AccountsSavedadstylesService struct {
	// contains filtered or unexported fields
}
func NewAccountsSavedadstylesService ¶
func NewAccountsSavedadstylesService(s *Service) *AccountsSavedadstylesService
func (*AccountsSavedadstylesService) Get ¶
func (r *AccountsSavedadstylesService) Get(accountId string, savedAdStyleId string) *AccountsSavedadstylesGetCall

Get: List a specific saved ad style for the specified account.

- accountId: Account for which to get the saved ad style. - savedAdStyleId: Saved ad style to retrieve.

func (*AccountsSavedadstylesService) List ¶
func (r *AccountsSavedadstylesService) List(accountId string) *AccountsSavedadstylesListCall

List: List all saved ad styles in the specified account.

- accountId: Account for which to list saved ad styles.

type AccountsService ¶
type AccountsService struct {
	Adclients *AccountsAdclientsService

	Adunits *AccountsAdunitsService

	Alerts *AccountsAlertsService

	Customchannels *AccountsCustomchannelsService

	Payments *AccountsPaymentsService

	Reports *AccountsReportsService

	Savedadstyles *AccountsSavedadstylesService

	Urlchannels *AccountsUrlchannelsService
	// contains filtered or unexported fields
}
func NewAccountsService ¶
func NewAccountsService(s *Service) *AccountsService
func (*AccountsService) Get ¶
func (r *AccountsService) Get(accountId string) *AccountsGetCall

Get: Get information about the selected AdSense account.

- accountId: Account to get information about.

func (*AccountsService) List ¶
func (r *AccountsService) List() *AccountsListCall

List: List all accounts available to this AdSense account.

type AccountsUrlchannelsListCall ¶
type AccountsUrlchannelsListCall struct {
	// contains filtered or unexported fields
}
func (*AccountsUrlchannelsListCall) Context ¶
func (c *AccountsUrlchannelsListCall) Context(ctx context.Context) *AccountsUrlchannelsListCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*AccountsUrlchannelsListCall) Do ¶
func (c *AccountsUrlchannelsListCall) Do(opts ...googleapi.CallOption) (*UrlChannels, error)

Do executes the "adsense.accounts.urlchannels.list" call. Exactly one of *UrlChannels or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *UrlChannels.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccountsUrlchannelsListCall) Fields ¶
func (c *AccountsUrlchannelsListCall) Fields(s ...googleapi.Field) *AccountsUrlchannelsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*AccountsUrlchannelsListCall) Header ¶
func (c *AccountsUrlchannelsListCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*AccountsUrlchannelsListCall) IfNoneMatch ¶
func (c *AccountsUrlchannelsListCall) IfNoneMatch(entityTag string) *AccountsUrlchannelsListCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (*AccountsUrlchannelsListCall) MaxResults ¶
func (c *AccountsUrlchannelsListCall) MaxResults(maxResults int64) *AccountsUrlchannelsListCall

MaxResults sets the optional parameter "maxResults": The maximum number of URL channels to include in the response, used for paging.

func (*AccountsUrlchannelsListCall) PageToken ¶
func (c *AccountsUrlchannelsListCall) PageToken(pageToken string) *AccountsUrlchannelsListCall

PageToken sets the optional parameter "pageToken": A continuation token, used to page through URL channels. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

func (*AccountsUrlchannelsListCall) Pages ¶
func (c *AccountsUrlchannelsListCall) Pages(ctx context.Context, f func(*UrlChannels) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsUrlchannelsService ¶
type AccountsUrlchannelsService struct {
	// contains filtered or unexported fields
}
func NewAccountsUrlchannelsService ¶
func NewAccountsUrlchannelsService(s *Service) *AccountsUrlchannelsService
func (*AccountsUrlchannelsService) List ¶
func (r *AccountsUrlchannelsService) List(accountId string, adClientId string) *AccountsUrlchannelsListCall

List: List all URL channels in the specified ad client for the specified account.

- accountId: Account to which the ad client belongs. - adClientId: Ad client for which to list URL channels.

type AdClient ¶
type AdClient struct {
	// ArcOptIn: Whether this ad client is opted in to ARC.
	ArcOptIn bool `json:"arcOptIn,omitempty"`

	// Id: Unique identifier of this ad client.
	Id string `json:"id,omitempty"`

	// Kind: Kind of resource this is, in this case adsense#adClient.
	Kind string `json:"kind,omitempty"`

	// ProductCode: This ad client's product code, which corresponds to the
	// PRODUCT_CODE report dimension.
	ProductCode string `json:"productCode,omitempty"`

	// SupportsReporting: Whether this ad client supports being reported on.
	SupportsReporting bool `json:"supportsReporting,omitempty"`

	// ForceSendFields is a list of field names (e.g. "ArcOptIn") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "ArcOptIn") to include in
	// API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*AdClient) MarshalJSON ¶
func (s *AdClient) MarshalJSON() ([]byte, error)
type AdClients ¶
type AdClients struct {
	// Etag: ETag of this response for caching purposes.
	Etag string `json:"etag,omitempty"`

	// Items: The ad clients returned in this list response.
	Items []*AdClient `json:"items,omitempty"`

	// Kind: Kind of list this is, in this case adsense#adClients.
	Kind string `json:"kind,omitempty"`

	// NextPageToken: Continuation token used to page through ad clients. To
	// retrieve the next page of results, set the next request's "pageToken"
	// value to this.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "Etag") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Etag") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*AdClients) MarshalJSON ¶
func (s *AdClients) MarshalJSON() ([]byte, error)
type AdCode ¶
type AdCode struct {
	// AdCode: The Auto ad code snippet. The ad code snippet.
	AdCode string `json:"adCode,omitempty"`

	// AmpBody: The AMP Auto ad code snippet that goes in the body of an AMP
	// page.
	AmpBody string `json:"ampBody,omitempty"`

	// AmpHead: The AMP Auto ad code snippet that goes in the head of an AMP
	// page.
	AmpHead string `json:"ampHead,omitempty"`

	// Kind: Kind this is, in this case adsense#adCode.
	Kind string `json:"kind,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "AdCode") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "AdCode") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*AdCode) MarshalJSON ¶
func (s *AdCode) MarshalJSON() ([]byte, error)
type AdStyle ¶
type AdStyle struct {
	// Colors: The colors which are included in the style. These are
	// represented as six hexadecimal characters, similar to HTML color
	// codes, but without the leading hash.
	Colors *AdStyleColors `json:"colors,omitempty"`

	// Corners: The style of the corners in the ad (deprecated: never
	// populated, ignored).
	Corners string `json:"corners,omitempty"`

	// Font: The font which is included in the style.
	Font *AdStyleFont `json:"font,omitempty"`

	// Kind: Kind this is, in this case adsense#adStyle.
	Kind string `json:"kind,omitempty"`

	// ForceSendFields is a list of field names (e.g. "Colors") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Colors") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*AdStyle) MarshalJSON ¶
func (s *AdStyle) MarshalJSON() ([]byte, error)
type AdStyleColors ¶
type AdStyleColors struct {
	// Background: The color of the ad background.
	Background string `json:"background,omitempty"`

	// Border: The color of the ad border.
	Border string `json:"border,omitempty"`

	// Text: The color of the ad text.
	Text string `json:"text,omitempty"`

	// Title: The color of the ad title.
	Title string `json:"title,omitempty"`

	// Url: The color of the ad url.
	Url string `json:"url,omitempty"`

	// ForceSendFields is a list of field names (e.g. "Background") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Background") to include in
	// API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}

AdStyleColors: The colors which are included in the style. These are represented as six hexadecimal characters, similar to HTML color codes, but without the leading hash.

func (*AdStyleColors) MarshalJSON ¶
func (s *AdStyleColors) MarshalJSON() ([]byte, error)
type AdStyleFont ¶
type AdStyleFont struct {
	// Family: The family of the font.
	Family string `json:"family,omitempty"`

	// Size: The size of the font.
	Size string `json:"size,omitempty"`

	// ForceSendFields is a list of field names (e.g. "Family") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Family") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}

AdStyleFont: The font which is included in the style.

func (*AdStyleFont) MarshalJSON ¶
func (s *AdStyleFont) MarshalJSON() ([]byte, error)
type AdUnit ¶
type AdUnit struct {
	// Code: Identity code of this ad unit, not necessarily unique across ad
	// clients.
	Code string `json:"code,omitempty"`

	// ContentAdsSettings: Settings specific to content ads (AFC) and
	// highend mobile content ads (AFMC - deprecated).
	ContentAdsSettings *AdUnitContentAdsSettings `json:"contentAdsSettings,omitempty"`

	// CustomStyle: Custom style information specific to this ad unit.
	CustomStyle *AdStyle `json:"customStyle,omitempty"`

	// FeedAdsSettings: Settings specific to feed ads (AFF) - deprecated.
	FeedAdsSettings *AdUnitFeedAdsSettings `json:"feedAdsSettings,omitempty"`

	// Id: Unique identifier of this ad unit. This should be considered an
	// opaque identifier; it is not safe to rely on it being in any
	// particular format.
	Id string `json:"id,omitempty"`

	// Kind: Kind of resource this is, in this case adsense#adUnit.
	Kind string `json:"kind,omitempty"`

	// MobileContentAdsSettings: Settings specific to WAP mobile content ads
	// (AFMC) - deprecated.
	MobileContentAdsSettings *AdUnitMobileContentAdsSettings `json:"mobileContentAdsSettings,omitempty"`

	// Name: Name of this ad unit.
	Name string `json:"name,omitempty"`

	// SavedStyleId: ID of the saved ad style which holds this ad unit's
	// style information.
	SavedStyleId string `json:"savedStyleId,omitempty"`

	// Status: Status of this ad unit. Possible values are:
	// NEW: Indicates that the ad unit was created within the last seven
	// days and does not yet have any activity associated with it.
	//
	// ACTIVE: Indicates that there has been activity on this ad unit in the
	// last seven days.
	//
	// INACTIVE: Indicates that there has been no activity on this ad unit
	// in the last seven days.
	Status string `json:"status,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "Code") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Code") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*AdUnit) MarshalJSON ¶
func (s *AdUnit) MarshalJSON() ([]byte, error)
type AdUnitContentAdsSettings ¶
type AdUnitContentAdsSettings struct {
	// BackupOption: The backup option to be used in instances where no ad
	// is available.
	BackupOption *AdUnitContentAdsSettingsBackupOption `json:"backupOption,omitempty"`

	// Size: Size of this ad unit.
	Size string `json:"size,omitempty"`

	// Type: Type of this ad unit.
	Type string `json:"type,omitempty"`

	// ForceSendFields is a list of field names (e.g. "BackupOption") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "BackupOption") to include
	// in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. However, any field with
	// an empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}

AdUnitContentAdsSettings: Settings specific to content ads (AFC) and highend mobile content ads (AFMC - deprecated).

func (*AdUnitContentAdsSettings) MarshalJSON ¶
func (s *AdUnitContentAdsSettings) MarshalJSON() ([]byte, error)
type AdUnitContentAdsSettingsBackupOption ¶
type AdUnitContentAdsSettingsBackupOption struct {
	// Color: Color to use when type is set to COLOR.
	Color string `json:"color,omitempty"`

	// Type: Type of the backup option. Possible values are BLANK, COLOR and
	// URL.
	Type string `json:"type,omitempty"`

	// Url: URL to use when type is set to URL.
	Url string `json:"url,omitempty"`

	// ForceSendFields is a list of field names (e.g. "Color") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Color") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}

AdUnitContentAdsSettingsBackupOption: The backup option to be used in instances where no ad is available.

func (*AdUnitContentAdsSettingsBackupOption) MarshalJSON ¶
func (s *AdUnitContentAdsSettingsBackupOption) MarshalJSON() ([]byte, error)
type AdUnitFeedAdsSettings ¶
type AdUnitFeedAdsSettings struct {
	// AdPosition: The position of the ads relative to the feed entries.
	AdPosition string `json:"adPosition,omitempty"`

	// Frequency: The frequency at which ads should appear in the feed (i.e.
	// every N entries).
	Frequency int64 `json:"frequency,omitempty"`

	// MinimumWordCount: The minimum length an entry should be in order to
	// have attached ads.
	MinimumWordCount int64 `json:"minimumWordCount,omitempty"`

	// Type: The type of ads which should appear.
	Type string `json:"type,omitempty"`

	// ForceSendFields is a list of field names (e.g. "AdPosition") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "AdPosition") to include in
	// API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}

AdUnitFeedAdsSettings: Settings specific to feed ads (AFF) - deprecated.

func (*AdUnitFeedAdsSettings) MarshalJSON ¶
func (s *AdUnitFeedAdsSettings) MarshalJSON() ([]byte, error)
type AdUnitMobileContentAdsSettings ¶
type AdUnitMobileContentAdsSettings struct {
	// MarkupLanguage: The markup language to use for this ad unit.
	MarkupLanguage string `json:"markupLanguage,omitempty"`

	// ScriptingLanguage: The scripting language to use for this ad unit.
	ScriptingLanguage string `json:"scriptingLanguage,omitempty"`

	// Size: Size of this ad unit.
	Size string `json:"size,omitempty"`

	// Type: Type of this ad unit.
	Type string `json:"type,omitempty"`

	// ForceSendFields is a list of field names (e.g. "MarkupLanguage") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "MarkupLanguage") to
	// include in API requests with the JSON null value. By default, fields
	// with empty values are omitted from API requests. However, any field
	// with an empty value appearing in NullFields will be sent to the
	// server as null. It is an error if a field in this list has a
	// non-empty value. This may be used to include null fields in Patch
	// requests.
	NullFields []string `json:"-"`
}

AdUnitMobileContentAdsSettings: Settings specific to WAP mobile content ads (AFMC) - deprecated.

func (*AdUnitMobileContentAdsSettings) MarshalJSON ¶
func (s *AdUnitMobileContentAdsSettings) MarshalJSON() ([]byte, error)
type AdUnits ¶
type AdUnits struct {
	// Etag: ETag of this response for caching purposes.
	Etag string `json:"etag,omitempty"`

	// Items: The ad units returned in this list response.
	Items []*AdUnit `json:"items,omitempty"`

	// Kind: Kind of list this is, in this case adsense#adUnits.
	Kind string `json:"kind,omitempty"`

	// NextPageToken: Continuation token used to page through ad units. To
	// retrieve the next page of results, set the next request's "pageToken"
	// value to this.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "Etag") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Etag") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*AdUnits) MarshalJSON ¶
func (s *AdUnits) MarshalJSON() ([]byte, error)
type AdclientsListCall ¶
type AdclientsListCall struct {
	// contains filtered or unexported fields
}
func (*AdclientsListCall) Context ¶
func (c *AdclientsListCall) Context(ctx context.Context) *AdclientsListCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*AdclientsListCall) Do ¶
func (c *AdclientsListCall) Do(opts ...googleapi.CallOption) (*AdClients, error)

Do executes the "adsense.adclients.list" call. Exactly one of *AdClients or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AdClients.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AdclientsListCall) Fields ¶
func (c *AdclientsListCall) Fields(s ...googleapi.Field) *AdclientsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*AdclientsListCall) Header ¶
func (c *AdclientsListCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*AdclientsListCall) IfNoneMatch ¶
func (c *AdclientsListCall) IfNoneMatch(entityTag string) *AdclientsListCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (*AdclientsListCall) MaxResults ¶
func (c *AdclientsListCall) MaxResults(maxResults int64) *AdclientsListCall

MaxResults sets the optional parameter "maxResults": The maximum number of ad clients to include in the response, used for paging.

func (*AdclientsListCall) PageToken ¶
func (c *AdclientsListCall) PageToken(pageToken string) *AdclientsListCall

PageToken sets the optional parameter "pageToken": A continuation token, used to page through ad clients. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

func (*AdclientsListCall) Pages ¶
func (c *AdclientsListCall) Pages(ctx context.Context, f func(*AdClients) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AdclientsService ¶
type AdclientsService struct {
	// contains filtered or unexported fields
}
func NewAdclientsService ¶
func NewAdclientsService(s *Service) *AdclientsService
func (*AdclientsService) List ¶
func (r *AdclientsService) List() *AdclientsListCall

List: List all ad clients in this AdSense account.

type AdsenseReportsGenerateResponse ¶
type AdsenseReportsGenerateResponse struct {
	// Averages: The averages of the report. This is the same length as any
	// other row in the report; cells corresponding to dimension columns are
	// empty.
	Averages []string `json:"averages,omitempty"`

	// EndDate: The requested end date in yyyy-mm-dd format.
	EndDate string `json:"endDate,omitempty"`

	// Headers: The header information of the columns requested in the
	// report. This is a list of headers; one for each dimension in the
	// request, followed by one for each metric in the request.
	Headers []*AdsenseReportsGenerateResponseHeaders `json:"headers,omitempty"`

	// Kind: Kind this is, in this case adsense#report.
	Kind string `json:"kind,omitempty"`

	// Rows: The output rows of the report. Each row is a list of cells; one
	// for each dimension in the request, followed by one for each metric in
	// the request. The dimension cells contain strings, and the metric
	// cells contain numbers.
	Rows [][]string `json:"rows,omitempty"`

	// StartDate: The requested start date in yyyy-mm-dd format.
	StartDate string `json:"startDate,omitempty"`

	// TotalMatchedRows: The total number of rows matched by the report
	// request. Fewer rows may be returned in the response due to being
	// limited by the row count requested or the report row limit.
	TotalMatchedRows int64 `json:"totalMatchedRows,omitempty,string"`

	// Totals: The totals of the report. This is the same length as any
	// other row in the report; cells corresponding to dimension columns are
	// empty.
	Totals []string `json:"totals,omitempty"`

	// Warnings: Any warnings associated with generation of the report.
	Warnings []string `json:"warnings,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "Averages") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Averages") to include in
	// API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*AdsenseReportsGenerateResponse) MarshalJSON ¶
func (s *AdsenseReportsGenerateResponse) MarshalJSON() ([]byte, error)
type AdsenseReportsGenerateResponseHeaders ¶
type AdsenseReportsGenerateResponseHeaders struct {
	// Currency: The currency of this column. Only present if the header
	// type is METRIC_CURRENCY.
	Currency string `json:"currency,omitempty"`

	// Name: The name of the header.
	Name string `json:"name,omitempty"`

	// Type: The type of the header; one of DIMENSION, METRIC_TALLY,
	// METRIC_RATIO, or METRIC_CURRENCY.
	Type string `json:"type,omitempty"`

	// ForceSendFields is a list of field names (e.g. "Currency") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Currency") to include in
	// API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*AdsenseReportsGenerateResponseHeaders) MarshalJSON ¶
func (s *AdsenseReportsGenerateResponseHeaders) MarshalJSON() ([]byte, error)
type AdunitsCustomchannelsListCall ¶
type AdunitsCustomchannelsListCall struct {
	// contains filtered or unexported fields
}
func (*AdunitsCustomchannelsListCall) Context ¶
func (c *AdunitsCustomchannelsListCall) Context(ctx context.Context) *AdunitsCustomchannelsListCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*AdunitsCustomchannelsListCall) Do ¶
func (c *AdunitsCustomchannelsListCall) Do(opts ...googleapi.CallOption) (*CustomChannels, error)

Do executes the "adsense.adunits.customchannels.list" call. Exactly one of *CustomChannels or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *CustomChannels.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AdunitsCustomchannelsListCall) Fields ¶
func (c *AdunitsCustomchannelsListCall) Fields(s ...googleapi.Field) *AdunitsCustomchannelsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*AdunitsCustomchannelsListCall) Header ¶
func (c *AdunitsCustomchannelsListCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*AdunitsCustomchannelsListCall) IfNoneMatch ¶
func (c *AdunitsCustomchannelsListCall) IfNoneMatch(entityTag string) *AdunitsCustomchannelsListCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (*AdunitsCustomchannelsListCall) MaxResults ¶
func (c *AdunitsCustomchannelsListCall) MaxResults(maxResults int64) *AdunitsCustomchannelsListCall

MaxResults sets the optional parameter "maxResults": The maximum number of custom channels to include in the response, used for paging.

func (*AdunitsCustomchannelsListCall) PageToken ¶
func (c *AdunitsCustomchannelsListCall) PageToken(pageToken string) *AdunitsCustomchannelsListCall

PageToken sets the optional parameter "pageToken": A continuation token, used to page through custom channels. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

func (*AdunitsCustomchannelsListCall) Pages ¶
func (c *AdunitsCustomchannelsListCall) Pages(ctx context.Context, f func(*CustomChannels) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AdunitsCustomchannelsService ¶
type AdunitsCustomchannelsService struct {
	// contains filtered or unexported fields
}
func NewAdunitsCustomchannelsService ¶
func NewAdunitsCustomchannelsService(s *Service) *AdunitsCustomchannelsService
func (*AdunitsCustomchannelsService) List ¶
func (r *AdunitsCustomchannelsService) List(adClientId string, adUnitId string) *AdunitsCustomchannelsListCall

List: List all custom channels which the specified ad unit belongs to.

- adClientId: Ad client which contains the ad unit. - adUnitId: Ad unit for which to list custom channels.

type AdunitsGetAdCodeCall ¶
type AdunitsGetAdCodeCall struct {
	// contains filtered or unexported fields
}
func (*AdunitsGetAdCodeCall) Context ¶
func (c *AdunitsGetAdCodeCall) Context(ctx context.Context) *AdunitsGetAdCodeCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*AdunitsGetAdCodeCall) Do ¶
func (c *AdunitsGetAdCodeCall) Do(opts ...googleapi.CallOption) (*AdCode, error)

Do executes the "adsense.adunits.getAdCode" call. Exactly one of *AdCode or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AdCode.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AdunitsGetAdCodeCall) Fields ¶
func (c *AdunitsGetAdCodeCall) Fields(s ...googleapi.Field) *AdunitsGetAdCodeCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*AdunitsGetAdCodeCall) Header ¶
func (c *AdunitsGetAdCodeCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*AdunitsGetAdCodeCall) IfNoneMatch ¶
func (c *AdunitsGetAdCodeCall) IfNoneMatch(entityTag string) *AdunitsGetAdCodeCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type AdunitsGetCall ¶
type AdunitsGetCall struct {
	// contains filtered or unexported fields
}
func (*AdunitsGetCall) Context ¶
func (c *AdunitsGetCall) Context(ctx context.Context) *AdunitsGetCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*AdunitsGetCall) Do ¶
func (c *AdunitsGetCall) Do(opts ...googleapi.CallOption) (*AdUnit, error)

Do executes the "adsense.adunits.get" call. Exactly one of *AdUnit or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AdUnit.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AdunitsGetCall) Fields ¶
func (c *AdunitsGetCall) Fields(s ...googleapi.Field) *AdunitsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*AdunitsGetCall) Header ¶
func (c *AdunitsGetCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*AdunitsGetCall) IfNoneMatch ¶
func (c *AdunitsGetCall) IfNoneMatch(entityTag string) *AdunitsGetCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type AdunitsListCall ¶
type AdunitsListCall struct {
	// contains filtered or unexported fields
}
func (*AdunitsListCall) Context ¶
func (c *AdunitsListCall) Context(ctx context.Context) *AdunitsListCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*AdunitsListCall) Do ¶
func (c *AdunitsListCall) Do(opts ...googleapi.CallOption) (*AdUnits, error)

Do executes the "adsense.adunits.list" call. Exactly one of *AdUnits or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AdUnits.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AdunitsListCall) Fields ¶
func (c *AdunitsListCall) Fields(s ...googleapi.Field) *AdunitsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*AdunitsListCall) Header ¶
func (c *AdunitsListCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*AdunitsListCall) IfNoneMatch ¶
func (c *AdunitsListCall) IfNoneMatch(entityTag string) *AdunitsListCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (*AdunitsListCall) IncludeInactive ¶
func (c *AdunitsListCall) IncludeInactive(includeInactive bool) *AdunitsListCall

IncludeInactive sets the optional parameter "includeInactive": Whether to include inactive ad units. Default: true.

func (*AdunitsListCall) MaxResults ¶
func (c *AdunitsListCall) MaxResults(maxResults int64) *AdunitsListCall

MaxResults sets the optional parameter "maxResults": The maximum number of ad units to include in the response, used for paging.

func (*AdunitsListCall) PageToken ¶
func (c *AdunitsListCall) PageToken(pageToken string) *AdunitsListCall

PageToken sets the optional parameter "pageToken": A continuation token, used to page through ad units. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

func (*AdunitsListCall) Pages ¶
func (c *AdunitsListCall) Pages(ctx context.Context, f func(*AdUnits) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AdunitsService ¶
type AdunitsService struct {
	Customchannels *AdunitsCustomchannelsService
	// contains filtered or unexported fields
}
func NewAdunitsService ¶
func NewAdunitsService(s *Service) *AdunitsService
func (*AdunitsService) Get ¶
func (r *AdunitsService) Get(adClientId string, adUnitId string) *AdunitsGetCall

Get: Gets the specified ad unit in the specified ad client.

- adClientId: Ad client for which to get the ad unit. - adUnitId: Ad unit to retrieve.

func (*AdunitsService) GetAdCode ¶
func (r *AdunitsService) GetAdCode(adClientId string, adUnitId string) *AdunitsGetAdCodeCall

GetAdCode: Get ad code for the specified ad unit.

- adClientId: Ad client with contains the ad unit. - adUnitId: Ad unit to get the code for.

func (*AdunitsService) List ¶
func (r *AdunitsService) List(adClientId string) *AdunitsListCall

List: List all ad units in the specified ad client for this AdSense account.

- adClientId: Ad client for which to list ad units.

type Alert ¶
type Alert struct {
	// Id: Unique identifier of this alert. This should be considered an
	// opaque identifier; it is not safe to rely on it being in any
	// particular format.
	Id string `json:"id,omitempty"`

	// IsDismissible: Whether this alert can be dismissed.
	IsDismissible bool `json:"isDismissible,omitempty"`

	// Kind: Kind of resource this is, in this case adsense#alert.
	Kind string `json:"kind,omitempty"`

	// Message: The localized alert message.
	Message string `json:"message,omitempty"`

	// Severity: Severity of this alert. Possible values: INFO, WARNING,
	// SEVERE.
	Severity string `json:"severity,omitempty"`

	// Type: Type of this alert. Possible values: SELF_HOLD,
	// MIGRATED_TO_BILLING3, ADDRESS_PIN_VERIFICATION,
	// PHONE_PIN_VERIFICATION, CORPORATE_ENTITY, GRAYLISTED_PUBLISHER,
	// API_HOLD.
	Type string `json:"type,omitempty"`

	// ForceSendFields is a list of field names (e.g. "Id") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Id") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*Alert) MarshalJSON ¶
func (s *Alert) MarshalJSON() ([]byte, error)
type Alerts ¶
type Alerts struct {
	// Items: The alerts returned in this list response.
	Items []*Alert `json:"items,omitempty"`

	// Kind: Kind of list this is, in this case adsense#alerts.
	Kind string `json:"kind,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "Items") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Items") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*Alerts) MarshalJSON ¶
func (s *Alerts) MarshalJSON() ([]byte, error)
type AlertsDeleteCall ¶
type AlertsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*AlertsDeleteCall) Context ¶
func (c *AlertsDeleteCall) Context(ctx context.Context) *AlertsDeleteCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*AlertsDeleteCall) Do ¶
func (c *AlertsDeleteCall) Do(opts ...googleapi.CallOption) error

Do executes the "adsense.alerts.delete" call.

func (*AlertsDeleteCall) Fields ¶
func (c *AlertsDeleteCall) Fields(s ...googleapi.Field) *AlertsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*AlertsDeleteCall) Header ¶
func (c *AlertsDeleteCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type AlertsListCall ¶
type AlertsListCall struct {
	// contains filtered or unexported fields
}
func (*AlertsListCall) Context ¶
func (c *AlertsListCall) Context(ctx context.Context) *AlertsListCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*AlertsListCall) Do ¶
func (c *AlertsListCall) Do(opts ...googleapi.CallOption) (*Alerts, error)

Do executes the "adsense.alerts.list" call. Exactly one of *Alerts or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Alerts.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AlertsListCall) Fields ¶
func (c *AlertsListCall) Fields(s ...googleapi.Field) *AlertsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*AlertsListCall) Header ¶
func (c *AlertsListCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*AlertsListCall) IfNoneMatch ¶
func (c *AlertsListCall) IfNoneMatch(entityTag string) *AlertsListCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (*AlertsListCall) Locale ¶
func (c *AlertsListCall) Locale(locale string) *AlertsListCall

Locale sets the optional parameter "locale": The locale to use for translating alert messages. The account locale will be used if this is not supplied. The AdSense default (English) will be used if the supplied locale is invalid or unsupported.

type AlertsService ¶
type AlertsService struct {
	// contains filtered or unexported fields
}
func NewAlertsService ¶
func NewAlertsService(s *Service) *AlertsService
func (*AlertsService) Delete ¶
func (r *AlertsService) Delete(alertId string) *AlertsDeleteCall

Delete: Dismiss (delete) the specified alert from the publisher's AdSense account.

- alertId: Alert to delete.

func (*AlertsService) List ¶
func (r *AlertsService) List() *AlertsListCall

List: List the alerts for this AdSense account.

type CustomChannel ¶
type CustomChannel struct {
	// Code: Code of this custom channel, not necessarily unique across ad
	// clients.
	Code string `json:"code,omitempty"`

	// Id: Unique identifier of this custom channel. This should be
	// considered an opaque identifier; it is not safe to rely on it being
	// in any particular format.
	Id string `json:"id,omitempty"`

	// Kind: Kind of resource this is, in this case adsense#customChannel.
	Kind string `json:"kind,omitempty"`

	// Name: Name of this custom channel.
	Name string `json:"name,omitempty"`

	// TargetingInfo: The targeting information of this custom channel, if
	// activated.
	TargetingInfo *CustomChannelTargetingInfo `json:"targetingInfo,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "Code") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Code") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*CustomChannel) MarshalJSON ¶
func (s *CustomChannel) MarshalJSON() ([]byte, error)
type CustomChannelTargetingInfo ¶
type CustomChannelTargetingInfo struct {
	// AdsAppearOn: The name used to describe this channel externally.
	AdsAppearOn string `json:"adsAppearOn,omitempty"`

	// Description: The external description of the channel.
	Description string `json:"description,omitempty"`

	// Location: The locations in which ads appear. (Only valid for content
	// and mobile content ads (deprecated)). Acceptable values for content
	// ads are: TOP_LEFT, TOP_CENTER, TOP_RIGHT, MIDDLE_LEFT, MIDDLE_CENTER,
	// MIDDLE_RIGHT, BOTTOM_LEFT, BOTTOM_CENTER, BOTTOM_RIGHT,
	// MULTIPLE_LOCATIONS. Acceptable values for mobile content ads
	// (deprecated) are: TOP, MIDDLE, BOTTOM, MULTIPLE_LOCATIONS.
	Location string `json:"location,omitempty"`

	// SiteLanguage: The language of the sites ads will be displayed on.
	SiteLanguage string `json:"siteLanguage,omitempty"`

	// ForceSendFields is a list of field names (e.g. "AdsAppearOn") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "AdsAppearOn") to include
	// in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. However, any field with
	// an empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}

CustomChannelTargetingInfo: The targeting information of this custom channel, if activated.

func (*CustomChannelTargetingInfo) MarshalJSON ¶
func (s *CustomChannelTargetingInfo) MarshalJSON() ([]byte, error)
type CustomChannels ¶
type CustomChannels struct {
	// Etag: ETag of this response for caching purposes.
	Etag string `json:"etag,omitempty"`

	// Items: The custom channels returned in this list response.
	Items []*CustomChannel `json:"items,omitempty"`

	// Kind: Kind of list this is, in this case adsense#customChannels.
	Kind string `json:"kind,omitempty"`

	// NextPageToken: Continuation token used to page through custom
	// channels. To retrieve the next page of results, set the next
	// request's "pageToken" value to this.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "Etag") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Etag") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*CustomChannels) MarshalJSON ¶
func (s *CustomChannels) MarshalJSON() ([]byte, error)
type CustomchannelsAdunitsListCall ¶
type CustomchannelsAdunitsListCall struct {
	// contains filtered or unexported fields
}
func (*CustomchannelsAdunitsListCall) Context ¶
func (c *CustomchannelsAdunitsListCall) Context(ctx context.Context) *CustomchannelsAdunitsListCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*CustomchannelsAdunitsListCall) Do ¶
func (c *CustomchannelsAdunitsListCall) Do(opts ...googleapi.CallOption) (*AdUnits, error)

Do executes the "adsense.customchannels.adunits.list" call. Exactly one of *AdUnits or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AdUnits.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CustomchannelsAdunitsListCall) Fields ¶
func (c *CustomchannelsAdunitsListCall) Fields(s ...googleapi.Field) *CustomchannelsAdunitsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*CustomchannelsAdunitsListCall) Header ¶
func (c *CustomchannelsAdunitsListCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*CustomchannelsAdunitsListCall) IfNoneMatch ¶
func (c *CustomchannelsAdunitsListCall) IfNoneMatch(entityTag string) *CustomchannelsAdunitsListCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (*CustomchannelsAdunitsListCall) IncludeInactive ¶
func (c *CustomchannelsAdunitsListCall) IncludeInactive(includeInactive bool) *CustomchannelsAdunitsListCall

IncludeInactive sets the optional parameter "includeInactive": Whether to include inactive ad units. Default: true.

func (*CustomchannelsAdunitsListCall) MaxResults ¶
func (c *CustomchannelsAdunitsListCall) MaxResults(maxResults int64) *CustomchannelsAdunitsListCall

MaxResults sets the optional parameter "maxResults": The maximum number of ad units to include in the response, used for paging.

func (*CustomchannelsAdunitsListCall) PageToken ¶
func (c *CustomchannelsAdunitsListCall) PageToken(pageToken string) *CustomchannelsAdunitsListCall

PageToken sets the optional parameter "pageToken": A continuation token, used to page through ad units. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

func (*CustomchannelsAdunitsListCall) Pages ¶
func (c *CustomchannelsAdunitsListCall) Pages(ctx context.Context, f func(*AdUnits) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type CustomchannelsAdunitsService ¶
type CustomchannelsAdunitsService struct {
	// contains filtered or unexported fields
}
func NewCustomchannelsAdunitsService ¶
func NewCustomchannelsAdunitsService(s *Service) *CustomchannelsAdunitsService
func (*CustomchannelsAdunitsService) List ¶
func (r *CustomchannelsAdunitsService) List(adClientId string, customChannelId string) *CustomchannelsAdunitsListCall

List: List all ad units in the specified custom channel.

- adClientId: Ad client which contains the custom channel. - customChannelId: Custom channel for which to list ad units.

type CustomchannelsGetCall ¶
type CustomchannelsGetCall struct {
	// contains filtered or unexported fields
}
func (*CustomchannelsGetCall) Context ¶
func (c *CustomchannelsGetCall) Context(ctx context.Context) *CustomchannelsGetCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*CustomchannelsGetCall) Do ¶
func (c *CustomchannelsGetCall) Do(opts ...googleapi.CallOption) (*CustomChannel, error)

Do executes the "adsense.customchannels.get" call. Exactly one of *CustomChannel or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *CustomChannel.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CustomchannelsGetCall) Fields ¶
func (c *CustomchannelsGetCall) Fields(s ...googleapi.Field) *CustomchannelsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*CustomchannelsGetCall) Header ¶
func (c *CustomchannelsGetCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*CustomchannelsGetCall) IfNoneMatch ¶
func (c *CustomchannelsGetCall) IfNoneMatch(entityTag string) *CustomchannelsGetCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type CustomchannelsListCall ¶
type CustomchannelsListCall struct {
	// contains filtered or unexported fields
}
func (*CustomchannelsListCall) Context ¶
func (c *CustomchannelsListCall) Context(ctx context.Context) *CustomchannelsListCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*CustomchannelsListCall) Do ¶
func (c *CustomchannelsListCall) Do(opts ...googleapi.CallOption) (*CustomChannels, error)

Do executes the "adsense.customchannels.list" call. Exactly one of *CustomChannels or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *CustomChannels.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*CustomchannelsListCall) Fields ¶
func (c *CustomchannelsListCall) Fields(s ...googleapi.Field) *CustomchannelsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*CustomchannelsListCall) Header ¶
func (c *CustomchannelsListCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*CustomchannelsListCall) IfNoneMatch ¶
func (c *CustomchannelsListCall) IfNoneMatch(entityTag string) *CustomchannelsListCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (*CustomchannelsListCall) MaxResults ¶
func (c *CustomchannelsListCall) MaxResults(maxResults int64) *CustomchannelsListCall

MaxResults sets the optional parameter "maxResults": The maximum number of custom channels to include in the response, used for paging.

func (*CustomchannelsListCall) PageToken ¶
func (c *CustomchannelsListCall) PageToken(pageToken string) *CustomchannelsListCall

PageToken sets the optional parameter "pageToken": A continuation token, used to page through custom channels. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

func (*CustomchannelsListCall) Pages ¶
func (c *CustomchannelsListCall) Pages(ctx context.Context, f func(*CustomChannels) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type CustomchannelsService ¶
type CustomchannelsService struct {
	Adunits *CustomchannelsAdunitsService
	// contains filtered or unexported fields
}
func NewCustomchannelsService ¶
func NewCustomchannelsService(s *Service) *CustomchannelsService
func (*CustomchannelsService) Get ¶
func (r *CustomchannelsService) Get(adClientId string, customChannelId string) *CustomchannelsGetCall

Get: Get the specified custom channel from the specified ad client.

- adClientId: Ad client which contains the custom channel. - customChannelId: Custom channel to retrieve.

func (*CustomchannelsService) List ¶
func (r *CustomchannelsService) List(adClientId string) *CustomchannelsListCall

List: List all custom channels in the specified ad client for this AdSense account.

- adClientId: Ad client for which to list custom channels.

type Metadata ¶
type Metadata struct {
	Items []*ReportingMetadataEntry `json:"items,omitempty"`

	// Kind: Kind of list this is, in this case adsense#metadata.
	Kind string `json:"kind,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "Items") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Items") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*Metadata) MarshalJSON ¶
func (s *Metadata) MarshalJSON() ([]byte, error)
type MetadataDimensionsListCall ¶
type MetadataDimensionsListCall struct {
	// contains filtered or unexported fields
}
func (*MetadataDimensionsListCall) Context ¶
func (c *MetadataDimensionsListCall) Context(ctx context.Context) *MetadataDimensionsListCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*MetadataDimensionsListCall) Do ¶
func (c *MetadataDimensionsListCall) Do(opts ...googleapi.CallOption) (*Metadata, error)

Do executes the "adsense.metadata.dimensions.list" call. Exactly one of *Metadata or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Metadata.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MetadataDimensionsListCall) Fields ¶
func (c *MetadataDimensionsListCall) Fields(s ...googleapi.Field) *MetadataDimensionsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*MetadataDimensionsListCall) Header ¶
func (c *MetadataDimensionsListCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*MetadataDimensionsListCall) IfNoneMatch ¶
func (c *MetadataDimensionsListCall) IfNoneMatch(entityTag string) *MetadataDimensionsListCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type MetadataDimensionsService ¶
type MetadataDimensionsService struct {
	// contains filtered or unexported fields
}
func NewMetadataDimensionsService ¶
func NewMetadataDimensionsService(s *Service) *MetadataDimensionsService
func (*MetadataDimensionsService) List ¶
func (r *MetadataDimensionsService) List() *MetadataDimensionsListCall

List: List the metadata for the dimensions available to this AdSense account.

type MetadataMetricsListCall ¶
type MetadataMetricsListCall struct {
	// contains filtered or unexported fields
}
func (*MetadataMetricsListCall) Context ¶
func (c *MetadataMetricsListCall) Context(ctx context.Context) *MetadataMetricsListCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*MetadataMetricsListCall) Do ¶
func (c *MetadataMetricsListCall) Do(opts ...googleapi.CallOption) (*Metadata, error)

Do executes the "adsense.metadata.metrics.list" call. Exactly one of *Metadata or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Metadata.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*MetadataMetricsListCall) Fields ¶
func (c *MetadataMetricsListCall) Fields(s ...googleapi.Field) *MetadataMetricsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*MetadataMetricsListCall) Header ¶
func (c *MetadataMetricsListCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*MetadataMetricsListCall) IfNoneMatch ¶
func (c *MetadataMetricsListCall) IfNoneMatch(entityTag string) *MetadataMetricsListCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type MetadataMetricsService ¶
type MetadataMetricsService struct {
	// contains filtered or unexported fields
}
func NewMetadataMetricsService ¶
func NewMetadataMetricsService(s *Service) *MetadataMetricsService
func (*MetadataMetricsService) List ¶
func (r *MetadataMetricsService) List() *MetadataMetricsListCall

List: List the metadata for the metrics available to this AdSense account.

type MetadataService ¶
type MetadataService struct {
	Dimensions *MetadataDimensionsService

	Metrics *MetadataMetricsService
	// contains filtered or unexported fields
}
func NewMetadataService ¶
func NewMetadataService(s *Service) *MetadataService
type Payment ¶
type Payment struct {
	// Id: Unique identifier of this Payment.
	Id string `json:"id,omitempty"`

	// Kind: Kind of resource this is, in this case adsense#payment.
	Kind string `json:"kind,omitempty"`

	// PaymentAmount: The amount to be paid.
	PaymentAmount string `json:"paymentAmount,omitempty"`

	// PaymentAmountCurrencyCode: The currency code for the amount to be
	// paid.
	PaymentAmountCurrencyCode string `json:"paymentAmountCurrencyCode,omitempty"`

	// PaymentDate: The date this payment was/will be credited to the user,
	// or none if the payment threshold has not been met.
	PaymentDate string `json:"paymentDate,omitempty"`

	// ForceSendFields is a list of field names (e.g. "Id") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Id") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*Payment) MarshalJSON ¶
func (s *Payment) MarshalJSON() ([]byte, error)
type Payments ¶
type Payments struct {
	// Items: The list of Payments for the account. One or both of a) the
	// account's most recent payment; and b) the account's upcoming payment.
	Items []*Payment `json:"items,omitempty"`

	// Kind: Kind of list this is, in this case adsense#payments.
	Kind string `json:"kind,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "Items") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Items") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*Payments) MarshalJSON ¶
func (s *Payments) MarshalJSON() ([]byte, error)
type PaymentsListCall ¶
type PaymentsListCall struct {
	// contains filtered or unexported fields
}
func (*PaymentsListCall) Context ¶
func (c *PaymentsListCall) Context(ctx context.Context) *PaymentsListCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*PaymentsListCall) Do ¶
func (c *PaymentsListCall) Do(opts ...googleapi.CallOption) (*Payments, error)

Do executes the "adsense.payments.list" call. Exactly one of *Payments or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Payments.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PaymentsListCall) Fields ¶
func (c *PaymentsListCall) Fields(s ...googleapi.Field) *PaymentsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*PaymentsListCall) Header ¶
func (c *PaymentsListCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*PaymentsListCall) IfNoneMatch ¶
func (c *PaymentsListCall) IfNoneMatch(entityTag string) *PaymentsListCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type PaymentsService ¶
type PaymentsService struct {
	// contains filtered or unexported fields
}
func NewPaymentsService ¶
func NewPaymentsService(s *Service) *PaymentsService
func (*PaymentsService) List ¶
func (r *PaymentsService) List() *PaymentsListCall

List: List the payments for this AdSense account.

type ReportingMetadataEntry ¶
type ReportingMetadataEntry struct {
	// CompatibleDimensions: For metrics this is a list of dimension IDs
	// which the metric is compatible with, for dimensions it is a list of
	// compatibility groups the dimension belongs to.
	CompatibleDimensions []string `json:"compatibleDimensions,omitempty"`

	// CompatibleMetrics: The names of the metrics the dimension or metric
	// this reporting metadata entry describes is compatible with.
	CompatibleMetrics []string `json:"compatibleMetrics,omitempty"`

	// Id: Unique identifier of this reporting metadata entry, corresponding
	// to the name of the appropriate dimension or metric.
	Id string `json:"id,omitempty"`

	// Kind: Kind of resource this is, in this case
	// adsense#reportingMetadataEntry.
	Kind string `json:"kind,omitempty"`

	// RequiredDimensions: The names of the dimensions which the dimension
	// or metric this reporting metadata entry describes requires to also be
	// present in order for the report to be valid. Omitting these will not
	// cause an error or warning, but may result in data which cannot be
	// correctly interpreted.
	RequiredDimensions []string `json:"requiredDimensions,omitempty"`

	// RequiredMetrics: The names of the metrics which the dimension or
	// metric this reporting metadata entry describes requires to also be
	// present in order for the report to be valid. Omitting these will not
	// cause an error or warning, but may result in data which cannot be
	// correctly interpreted.
	RequiredMetrics []string `json:"requiredMetrics,omitempty"`

	// SupportedProducts: The codes of the projects supported by the
	// dimension or metric this reporting metadata entry describes.
	SupportedProducts []string `json:"supportedProducts,omitempty"`

	// ForceSendFields is a list of field names (e.g.
	// "CompatibleDimensions") to unconditionally include in API requests.
	// By default, fields with empty or default values are omitted from API
	// requests. However, any non-pointer, non-interface field appearing in
	// ForceSendFields will be sent to the server regardless of whether the
	// field is empty or not. This may be used to include empty fields in
	// Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "CompatibleDimensions") to
	// include in API requests with the JSON null value. By default, fields
	// with empty values are omitted from API requests. However, any field
	// with an empty value appearing in NullFields will be sent to the
	// server as null. It is an error if a field in this list has a
	// non-empty value. This may be used to include null fields in Patch
	// requests.
	NullFields []string `json:"-"`
}
func (*ReportingMetadataEntry) MarshalJSON ¶
func (s *ReportingMetadataEntry) MarshalJSON() ([]byte, error)
type ReportsGenerateCall ¶
type ReportsGenerateCall struct {
	// contains filtered or unexported fields
}
func (*ReportsGenerateCall) AccountId ¶
func (c *ReportsGenerateCall) AccountId(accountId ...string) *ReportsGenerateCall

AccountId sets the optional parameter "accountId": Accounts upon which to report.

func (*ReportsGenerateCall) Context ¶
func (c *ReportsGenerateCall) Context(ctx context.Context) *ReportsGenerateCall

Context sets the context to be used in this call's Do and Download methods. Any pending HTTP request will be aborted if the provided context is canceled.

func (*ReportsGenerateCall) Currency ¶
func (c *ReportsGenerateCall) Currency(currency string) *ReportsGenerateCall

Currency sets the optional parameter "currency": Optional currency to use when reporting on monetary metrics. Defaults to the account's currency if not set.

func (*ReportsGenerateCall) Dimension ¶
func (c *ReportsGenerateCall) Dimension(dimension ...string) *ReportsGenerateCall

Dimension sets the optional parameter "dimension": Dimensions to base the report on.

func (*ReportsGenerateCall) Do ¶
func (c *ReportsGenerateCall) Do(opts ...googleapi.CallOption) (*AdsenseReportsGenerateResponse, error)

Do executes the "adsense.reports.generate" call. Exactly one of *AdsenseReportsGenerateResponse or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AdsenseReportsGenerateResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ReportsGenerateCall) Download ¶
func (c *ReportsGenerateCall) Download(opts ...googleapi.CallOption) (*http.Response, error)

Download fetches the API endpoint's "media" value, instead of the normal API response value. If the returned error is nil, the Response is guaranteed to have a 2xx status code. Callers must close the Response.Body as usual.

func (*ReportsGenerateCall) Fields ¶
func (c *ReportsGenerateCall) Fields(s ...googleapi.Field) *ReportsGenerateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*ReportsGenerateCall) Filter ¶
func (c *ReportsGenerateCall) Filter(filter ...string) *ReportsGenerateCall

Filter sets the optional parameter "filter": Filters to be run on the report.

func (*ReportsGenerateCall) Header ¶
func (c *ReportsGenerateCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*ReportsGenerateCall) IfNoneMatch ¶
func (c *ReportsGenerateCall) IfNoneMatch(entityTag string) *ReportsGenerateCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (*ReportsGenerateCall) Locale ¶
func (c *ReportsGenerateCall) Locale(locale string) *ReportsGenerateCall

Locale sets the optional parameter "locale": Optional locale to use for translating report output to a local language. Defaults to "en_US" if not specified.

func (*ReportsGenerateCall) MaxResults ¶
func (c *ReportsGenerateCall) MaxResults(maxResults int64) *ReportsGenerateCall

MaxResults sets the optional parameter "maxResults": The maximum number of rows of report data to return.

func (*ReportsGenerateCall) Metric ¶
func (c *ReportsGenerateCall) Metric(metric ...string) *ReportsGenerateCall

Metric sets the optional parameter "metric": Numeric columns to include in the report.

func (*ReportsGenerateCall) Sort ¶
func (c *ReportsGenerateCall) Sort(sort ...string) *ReportsGenerateCall

Sort sets the optional parameter "sort": The name of a dimension or metric to sort the resulting report on, optionally prefixed with "+" to sort ascending or "-" to sort descending. If no prefix is specified, the column is sorted ascending.

func (*ReportsGenerateCall) StartIndex ¶
func (c *ReportsGenerateCall) StartIndex(startIndex int64) *ReportsGenerateCall

StartIndex sets the optional parameter "startIndex": Index of the first row of report data to return.

func (*ReportsGenerateCall) UseTimezoneReporting ¶
func (c *ReportsGenerateCall) UseTimezoneReporting(useTimezoneReporting bool) *ReportsGenerateCall

UseTimezoneReporting sets the optional parameter "useTimezoneReporting": Whether the report should be generated in the AdSense account's local timezone. If false default PST/PDT timezone will be used.

type ReportsSavedGenerateCall ¶
type ReportsSavedGenerateCall struct {
	// contains filtered or unexported fields
}
func (*ReportsSavedGenerateCall) Context ¶
func (c *ReportsSavedGenerateCall) Context(ctx context.Context) *ReportsSavedGenerateCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*ReportsSavedGenerateCall) Do ¶
func (c *ReportsSavedGenerateCall) Do(opts ...googleapi.CallOption) (*AdsenseReportsGenerateResponse, error)

Do executes the "adsense.reports.saved.generate" call. Exactly one of *AdsenseReportsGenerateResponse or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AdsenseReportsGenerateResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ReportsSavedGenerateCall) Fields ¶
func (c *ReportsSavedGenerateCall) Fields(s ...googleapi.Field) *ReportsSavedGenerateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*ReportsSavedGenerateCall) Header ¶
func (c *ReportsSavedGenerateCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*ReportsSavedGenerateCall) IfNoneMatch ¶
func (c *ReportsSavedGenerateCall) IfNoneMatch(entityTag string) *ReportsSavedGenerateCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (*ReportsSavedGenerateCall) Locale ¶
func (c *ReportsSavedGenerateCall) Locale(locale string) *ReportsSavedGenerateCall

Locale sets the optional parameter "locale": Optional locale to use for translating report output to a local language. Defaults to "en_US" if not specified.

func (*ReportsSavedGenerateCall) MaxResults ¶
func (c *ReportsSavedGenerateCall) MaxResults(maxResults int64) *ReportsSavedGenerateCall

MaxResults sets the optional parameter "maxResults": The maximum number of rows of report data to return.

func (*ReportsSavedGenerateCall) StartIndex ¶
func (c *ReportsSavedGenerateCall) StartIndex(startIndex int64) *ReportsSavedGenerateCall

StartIndex sets the optional parameter "startIndex": Index of the first row of report data to return.

type ReportsSavedListCall ¶
type ReportsSavedListCall struct {
	// contains filtered or unexported fields
}
func (*ReportsSavedListCall) Context ¶
func (c *ReportsSavedListCall) Context(ctx context.Context) *ReportsSavedListCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*ReportsSavedListCall) Do ¶
func (c *ReportsSavedListCall) Do(opts ...googleapi.CallOption) (*SavedReports, error)

Do executes the "adsense.reports.saved.list" call. Exactly one of *SavedReports or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *SavedReports.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ReportsSavedListCall) Fields ¶
func (c *ReportsSavedListCall) Fields(s ...googleapi.Field) *ReportsSavedListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*ReportsSavedListCall) Header ¶
func (c *ReportsSavedListCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*ReportsSavedListCall) IfNoneMatch ¶
func (c *ReportsSavedListCall) IfNoneMatch(entityTag string) *ReportsSavedListCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (*ReportsSavedListCall) MaxResults ¶
func (c *ReportsSavedListCall) MaxResults(maxResults int64) *ReportsSavedListCall

MaxResults sets the optional parameter "maxResults": The maximum number of saved reports to include in the response, used for paging.

func (*ReportsSavedListCall) PageToken ¶
func (c *ReportsSavedListCall) PageToken(pageToken string) *ReportsSavedListCall

PageToken sets the optional parameter "pageToken": A continuation token, used to page through saved reports. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

func (*ReportsSavedListCall) Pages ¶
func (c *ReportsSavedListCall) Pages(ctx context.Context, f func(*SavedReports) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ReportsSavedService ¶
type ReportsSavedService struct {
	// contains filtered or unexported fields
}
func NewReportsSavedService ¶
func NewReportsSavedService(s *Service) *ReportsSavedService
func (*ReportsSavedService) Generate ¶
func (r *ReportsSavedService) Generate(savedReportId string) *ReportsSavedGenerateCall

Generate: Generate an AdSense report based on the saved report ID sent in the query parameters.

- savedReportId: The saved report to retrieve.

func (*ReportsSavedService) List ¶
func (r *ReportsSavedService) List() *ReportsSavedListCall

List: List all saved reports in this AdSense account.

type ReportsService ¶
type ReportsService struct {
	Saved *ReportsSavedService
	// contains filtered or unexported fields
}
func NewReportsService ¶
func NewReportsService(s *Service) *ReportsService
func (*ReportsService) Generate ¶
func (r *ReportsService) Generate(startDate string, endDate string) *ReportsGenerateCall

Generate: Generate an AdSense report based on the report request sent in the query parameters. Returns the result as JSON; to retrieve output in CSV format specify "alt=csv" as a query parameter.

endDate: End of the date range to report on in "YYYY-MM-DD" format, inclusive.
startDate: Start of the date range to report on in "YYYY-MM-DD" format, inclusive.
type SavedAdStyle ¶
type SavedAdStyle struct {
	// AdStyle: The AdStyle itself.
	AdStyle *AdStyle `json:"adStyle,omitempty"`

	// Id: Unique identifier of this saved ad style. This should be
	// considered an opaque identifier; it is not safe to rely on it being
	// in any particular format.
	Id string `json:"id,omitempty"`

	// Kind: Kind of resource this is, in this case adsense#savedAdStyle.
	Kind string `json:"kind,omitempty"`

	// Name: The user selected name of this SavedAdStyle.
	Name string `json:"name,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "AdStyle") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "AdStyle") to include in
	// API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*SavedAdStyle) MarshalJSON ¶
func (s *SavedAdStyle) MarshalJSON() ([]byte, error)
type SavedAdStyles ¶
type SavedAdStyles struct {
	// Etag: ETag of this response for caching purposes.
	Etag string `json:"etag,omitempty"`

	// Items: The saved ad styles returned in this list response.
	Items []*SavedAdStyle `json:"items,omitempty"`

	// Kind: Kind of list this is, in this case adsense#savedAdStyles.
	Kind string `json:"kind,omitempty"`

	// NextPageToken: Continuation token used to page through ad units. To
	// retrieve the next page of results, set the next request's "pageToken"
	// value to this.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "Etag") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Etag") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*SavedAdStyles) MarshalJSON ¶
func (s *SavedAdStyles) MarshalJSON() ([]byte, error)
type SavedReport ¶
type SavedReport struct {
	// Id: Unique identifier of this saved report.
	Id string `json:"id,omitempty"`

	// Kind: Kind of resource this is, in this case adsense#savedReport.
	Kind string `json:"kind,omitempty"`

	// Name: This saved report's name.
	Name string `json:"name,omitempty"`

	// ForceSendFields is a list of field names (e.g. "Id") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Id") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*SavedReport) MarshalJSON ¶
func (s *SavedReport) MarshalJSON() ([]byte, error)
type SavedReports ¶
type SavedReports struct {
	// Etag: ETag of this response for caching purposes.
	Etag string `json:"etag,omitempty"`

	// Items: The saved reports returned in this list response.
	Items []*SavedReport `json:"items,omitempty"`

	// Kind: Kind of list this is, in this case adsense#savedReports.
	Kind string `json:"kind,omitempty"`

	// NextPageToken: Continuation token used to page through saved reports.
	// To retrieve the next page of results, set the next request's
	// "pageToken" value to this.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "Etag") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Etag") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*SavedReports) MarshalJSON ¶
func (s *SavedReports) MarshalJSON() ([]byte, error)
type SavedadstylesGetCall ¶
type SavedadstylesGetCall struct {
	// contains filtered or unexported fields
}
func (*SavedadstylesGetCall) Context ¶
func (c *SavedadstylesGetCall) Context(ctx context.Context) *SavedadstylesGetCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*SavedadstylesGetCall) Do ¶
func (c *SavedadstylesGetCall) Do(opts ...googleapi.CallOption) (*SavedAdStyle, error)

Do executes the "adsense.savedadstyles.get" call. Exactly one of *SavedAdStyle or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *SavedAdStyle.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*SavedadstylesGetCall) Fields ¶
func (c *SavedadstylesGetCall) Fields(s ...googleapi.Field) *SavedadstylesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*SavedadstylesGetCall) Header ¶
func (c *SavedadstylesGetCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*SavedadstylesGetCall) IfNoneMatch ¶
func (c *SavedadstylesGetCall) IfNoneMatch(entityTag string) *SavedadstylesGetCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type SavedadstylesListCall ¶
type SavedadstylesListCall struct {
	// contains filtered or unexported fields
}
func (*SavedadstylesListCall) Context ¶
func (c *SavedadstylesListCall) Context(ctx context.Context) *SavedadstylesListCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*SavedadstylesListCall) Do ¶
func (c *SavedadstylesListCall) Do(opts ...googleapi.CallOption) (*SavedAdStyles, error)

Do executes the "adsense.savedadstyles.list" call. Exactly one of *SavedAdStyles or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *SavedAdStyles.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*SavedadstylesListCall) Fields ¶
func (c *SavedadstylesListCall) Fields(s ...googleapi.Field) *SavedadstylesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*SavedadstylesListCall) Header ¶
func (c *SavedadstylesListCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*SavedadstylesListCall) IfNoneMatch ¶
func (c *SavedadstylesListCall) IfNoneMatch(entityTag string) *SavedadstylesListCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (*SavedadstylesListCall) MaxResults ¶
func (c *SavedadstylesListCall) MaxResults(maxResults int64) *SavedadstylesListCall

MaxResults sets the optional parameter "maxResults": The maximum number of saved ad styles to include in the response, used for paging.

func (*SavedadstylesListCall) PageToken ¶
func (c *SavedadstylesListCall) PageToken(pageToken string) *SavedadstylesListCall

PageToken sets the optional parameter "pageToken": A continuation token, used to page through saved ad styles. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

func (*SavedadstylesListCall) Pages ¶
func (c *SavedadstylesListCall) Pages(ctx context.Context, f func(*SavedAdStyles) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type SavedadstylesService ¶
type SavedadstylesService struct {
	// contains filtered or unexported fields
}
func NewSavedadstylesService ¶
func NewSavedadstylesService(s *Service) *SavedadstylesService
func (*SavedadstylesService) Get ¶
func (r *SavedadstylesService) Get(savedAdStyleId string) *SavedadstylesGetCall

Get: Get a specific saved ad style from the user's account.

- savedAdStyleId: Saved ad style to retrieve.

func (*SavedadstylesService) List ¶
func (r *SavedadstylesService) List() *SavedadstylesListCall

List: List all saved ad styles in the user's account.

type Service ¶
type Service struct {
	BasePath  string // API endpoint base URL
	UserAgent string // optional additional User-Agent fragment

	Accounts *AccountsService

	Adclients *AdclientsService

	Adunits *AdunitsService

	Alerts *AlertsService

	Customchannels *CustomchannelsService

	Metadata *MetadataService

	Payments *PaymentsService

	Reports *ReportsService

	Savedadstyles *SavedadstylesService

	Urlchannels *UrlchannelsService
	// contains filtered or unexported fields
}
func
New
DEPRECATED
func NewService ¶
added in v0.3.0
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)

NewService creates a new Service.

type UrlChannel ¶
type UrlChannel struct {
	// Id: Unique identifier of this URL channel. This should be considered
	// an opaque identifier; it is not safe to rely on it being in any
	// particular format.
	Id string `json:"id,omitempty"`

	// Kind: Kind of resource this is, in this case adsense#urlChannel.
	Kind string `json:"kind,omitempty"`

	// UrlPattern: URL Pattern of this URL channel. Does not include
	// "http://" or "https://". Example: www.example.com/home
	UrlPattern string `json:"urlPattern,omitempty"`

	// ForceSendFields is a list of field names (e.g. "Id") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Id") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*UrlChannel) MarshalJSON ¶
func (s *UrlChannel) MarshalJSON() ([]byte, error)
type UrlChannels ¶
type UrlChannels struct {
	// Etag: ETag of this response for caching purposes.
	Etag string `json:"etag,omitempty"`

	// Items: The URL channels returned in this list response.
	Items []*UrlChannel `json:"items,omitempty"`

	// Kind: Kind of list this is, in this case adsense#urlChannels.
	Kind string `json:"kind,omitempty"`

	// NextPageToken: Continuation token used to page through URL channels.
	// To retrieve the next page of results, set the next request's
	// "pageToken" value to this.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the
	// server.
	googleapi.ServerResponse `json:"-"`

	// ForceSendFields is a list of field names (e.g. "Etag") to
	// unconditionally include in API requests. By default, fields with
	// empty or default values are omitted from API requests. However, any
	// non-pointer, non-interface field appearing in ForceSendFields will be
	// sent to the server regardless of whether the field is empty or not.
	// This may be used to include empty fields in Patch requests.
	ForceSendFields []string `json:"-"`

	// NullFields is a list of field names (e.g. "Etag") to include in API
	// requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. However, any field with an
	// empty value appearing in NullFields will be sent to the server as
	// null. It is an error if a field in this list has a non-empty value.
	// This may be used to include null fields in Patch requests.
	NullFields []string `json:"-"`
}
func (*UrlChannels) MarshalJSON ¶
func (s *UrlChannels) MarshalJSON() ([]byte, error)
type UrlchannelsListCall ¶
type UrlchannelsListCall struct {
	// contains filtered or unexported fields
}
func (*UrlchannelsListCall) Context ¶
func (c *UrlchannelsListCall) Context(ctx context.Context) *UrlchannelsListCall

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

func (*UrlchannelsListCall) Do ¶
func (c *UrlchannelsListCall) Do(opts ...googleapi.CallOption) (*UrlChannels, error)

Do executes the "adsense.urlchannels.list" call. Exactly one of *UrlChannels or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *UrlChannels.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*UrlchannelsListCall) Fields ¶
func (c *UrlchannelsListCall) Fields(s ...googleapi.Field) *UrlchannelsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more information.

func (*UrlchannelsListCall) Header ¶
func (c *UrlchannelsListCall) Header() http.Header

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

func (*UrlchannelsListCall) IfNoneMatch ¶
func (c *UrlchannelsListCall) IfNoneMatch(entityTag string) *UrlchannelsListCall

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (*UrlchannelsListCall) MaxResults ¶
func (c *UrlchannelsListCall) MaxResults(maxResults int64) *UrlchannelsListCall

MaxResults sets the optional parameter "maxResults": The maximum number of URL channels to include in the response, used for paging.

func (*UrlchannelsListCall) PageToken ¶
func (c *UrlchannelsListCall) PageToken(pageToken string) *UrlchannelsListCall

PageToken sets the optional parameter "pageToken": A continuation token, used to page through URL channels. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

func (*UrlchannelsListCall) Pages ¶
func (c *UrlchannelsListCall) Pages(ctx context.Context, f func(*UrlChannels) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type UrlchannelsService ¶
type UrlchannelsService struct {
	// contains filtered or unexported fields
}
func NewUrlchannelsService ¶
func NewUrlchannelsService(s *Service) *UrlchannelsService
func (*UrlchannelsService) List ¶
func (r *UrlchannelsService) List(adClientId string) *UrlchannelsListCall

List: List all URL channels in the specified ad client for this AdSense account.

- adClientId: Ad client for which to list URL channels.

 Source Files ¶
View all Source files
adsense-gen.go
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
