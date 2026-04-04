# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3

Title: adsense package - google.golang.org/api/adsense/v1.3 - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3

Markdown Content:
Package adsense provides access to the AdSense Management API.

For product documentation, see: [https://developers.google.com/adsense/management/](https://developers.google.com/adsense/management/)

#### Creating a client [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#hdr-Creating_a_client "Go to Creating a client")

Usage example:

import "google.golang.org/api/adsense/v1.3"
...
ctx := context.Background()
adsenseService, err := adsense.NewService(ctx)

In this example, Google Application Default Credentials are used for authentication.

For information on how to create and obtain Application Default Credentials, see [https://developers.google.com/identity/protocols/application-default-credentials](https://developers.google.com/identity/protocols/application-default-credentials).

#### Other authentication options [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#hdr-Other_authentication_options "Go to Other authentication options")

By default, all available scopes (see "Constants") are used to authenticate. To restrict scopes, use option.WithScopes:

adsenseService, err := adsense.NewService(ctx, option.WithScopes(adsense.AdsenseReadonlyScope))

To use an API key for authentication (note: some APIs do not support API keys), use option.WithAPIKey:

adsenseService, err := adsense.NewService(ctx, option.WithAPIKey("AIza..."))

To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow), use option.WithTokenSource:

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
adsenseService, err := adsense.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))

See [https://godoc.org/google.golang.org/api/option/](https://godoc.org/google.golang.org/api/option/) for details on options.

*   [Constants](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#pkg-constants)
*   [type Account](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Account)
*       *   [func (s *Account) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Account.MarshalJSON)

*   [type Accounts](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Accounts)
*       *   [func (s *Accounts) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Accounts.MarshalJSON)

*   [type AccountsAdclientsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdclientsListCall)
*       *   [func (c *AccountsAdclientsListCall) Context(ctx context.Context) *AccountsAdclientsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdclientsListCall.Context)
    *   [func (c *AccountsAdclientsListCall) Do(opts ...googleapi.CallOption) (*AdClients, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdclientsListCall.Do)
    *   [func (c *AccountsAdclientsListCall) Fields(s ...googleapi.Field) *AccountsAdclientsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdclientsListCall.Fields)
    *   [func (c *AccountsAdclientsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdclientsListCall.Header)
    *   [func (c *AccountsAdclientsListCall) IfNoneMatch(entityTag string) *AccountsAdclientsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdclientsListCall.IfNoneMatch)
    *   [func (c *AccountsAdclientsListCall) MaxResults(maxResults int64) *AccountsAdclientsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdclientsListCall.MaxResults)
    *   [func (c *AccountsAdclientsListCall) PageToken(pageToken string) *AccountsAdclientsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdclientsListCall.PageToken)
    *   [func (c *AccountsAdclientsListCall) Pages(ctx context.Context, f func(*AdClients) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdclientsListCall.Pages)

*   [type AccountsAdclientsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdclientsService)
*       *   [func NewAccountsAdclientsService(s *Service) *AccountsAdclientsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#NewAccountsAdclientsService)

*       *   [func (r *AccountsAdclientsService) List(accountId string) *AccountsAdclientsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdclientsService.List)

*   [type AccountsAdunitsCustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsCustomchannelsListCall)
*       *   [func (c *AccountsAdunitsCustomchannelsListCall) Context(ctx context.Context) *AccountsAdunitsCustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsCustomchannelsListCall.Context)
    *   [func (c *AccountsAdunitsCustomchannelsListCall) Do(opts ...googleapi.CallOption) (*CustomChannels, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsCustomchannelsListCall.Do)
    *   [func (c *AccountsAdunitsCustomchannelsListCall) Fields(s ...googleapi.Field) *AccountsAdunitsCustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsCustomchannelsListCall.Fields)
    *   [func (c *AccountsAdunitsCustomchannelsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsCustomchannelsListCall.Header)
    *   [func (c *AccountsAdunitsCustomchannelsListCall) IfNoneMatch(entityTag string) *AccountsAdunitsCustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsCustomchannelsListCall.IfNoneMatch)
    *   [func (c *AccountsAdunitsCustomchannelsListCall) MaxResults(maxResults int64) *AccountsAdunitsCustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsCustomchannelsListCall.MaxResults)
    *   [func (c *AccountsAdunitsCustomchannelsListCall) PageToken(pageToken string) *AccountsAdunitsCustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsCustomchannelsListCall.PageToken)
    *   [func (c *AccountsAdunitsCustomchannelsListCall) Pages(ctx context.Context, f func(*CustomChannels) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsCustomchannelsListCall.Pages)

*   [type AccountsAdunitsCustomchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsCustomchannelsService)
*       *   [func NewAccountsAdunitsCustomchannelsService(s *Service) *AccountsAdunitsCustomchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#NewAccountsAdunitsCustomchannelsService)

*       *   [func (r *AccountsAdunitsCustomchannelsService) List(accountId string, adClientId string, adUnitId string) *AccountsAdunitsCustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsCustomchannelsService.List)

*   [type AccountsAdunitsGetAdCodeCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsGetAdCodeCall)
*       *   [func (c *AccountsAdunitsGetAdCodeCall) Context(ctx context.Context) *AccountsAdunitsGetAdCodeCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsGetAdCodeCall.Context)
    *   [func (c *AccountsAdunitsGetAdCodeCall) Do(opts ...googleapi.CallOption) (*AdCode, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsGetAdCodeCall.Do)
    *   [func (c *AccountsAdunitsGetAdCodeCall) Fields(s ...googleapi.Field) *AccountsAdunitsGetAdCodeCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsGetAdCodeCall.Fields)
    *   [func (c *AccountsAdunitsGetAdCodeCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsGetAdCodeCall.Header)
    *   [func (c *AccountsAdunitsGetAdCodeCall) IfNoneMatch(entityTag string) *AccountsAdunitsGetAdCodeCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsGetAdCodeCall.IfNoneMatch)

*   [type AccountsAdunitsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsGetCall)
*       *   [func (c *AccountsAdunitsGetCall) Context(ctx context.Context) *AccountsAdunitsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsGetCall.Context)
    *   [func (c *AccountsAdunitsGetCall) Do(opts ...googleapi.CallOption) (*AdUnit, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsGetCall.Do)
    *   [func (c *AccountsAdunitsGetCall) Fields(s ...googleapi.Field) *AccountsAdunitsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsGetCall.Fields)
    *   [func (c *AccountsAdunitsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsGetCall.Header)
    *   [func (c *AccountsAdunitsGetCall) IfNoneMatch(entityTag string) *AccountsAdunitsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsGetCall.IfNoneMatch)

*   [type AccountsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsListCall)
*       *   [func (c *AccountsAdunitsListCall) Context(ctx context.Context) *AccountsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsListCall.Context)
    *   [func (c *AccountsAdunitsListCall) Do(opts ...googleapi.CallOption) (*AdUnits, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsListCall.Do)
    *   [func (c *AccountsAdunitsListCall) Fields(s ...googleapi.Field) *AccountsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsListCall.Fields)
    *   [func (c *AccountsAdunitsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsListCall.Header)
    *   [func (c *AccountsAdunitsListCall) IfNoneMatch(entityTag string) *AccountsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsListCall.IfNoneMatch)
    *   [func (c *AccountsAdunitsListCall) IncludeInactive(includeInactive bool) *AccountsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsListCall.IncludeInactive)
    *   [func (c *AccountsAdunitsListCall) MaxResults(maxResults int64) *AccountsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsListCall.MaxResults)
    *   [func (c *AccountsAdunitsListCall) PageToken(pageToken string) *AccountsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsListCall.PageToken)
    *   [func (c *AccountsAdunitsListCall) Pages(ctx context.Context, f func(*AdUnits) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsListCall.Pages)

*   [type AccountsAdunitsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsService)
*       *   [func NewAccountsAdunitsService(s *Service) *AccountsAdunitsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#NewAccountsAdunitsService)

*       *   [func (r *AccountsAdunitsService) Get(accountId string, adClientId string, adUnitId string) *AccountsAdunitsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsService.Get)
    *   [func (r *AccountsAdunitsService) GetAdCode(accountId string, adClientId string, adUnitId string) *AccountsAdunitsGetAdCodeCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsService.GetAdCode)
    *   [func (r *AccountsAdunitsService) List(accountId string, adClientId string) *AccountsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsService.List)

*   [type AccountsAlertsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAlertsListCall)
*       *   [func (c *AccountsAlertsListCall) Context(ctx context.Context) *AccountsAlertsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAlertsListCall.Context)
    *   [func (c *AccountsAlertsListCall) Do(opts ...googleapi.CallOption) (*Alerts, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAlertsListCall.Do)
    *   [func (c *AccountsAlertsListCall) Fields(s ...googleapi.Field) *AccountsAlertsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAlertsListCall.Fields)
    *   [func (c *AccountsAlertsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAlertsListCall.Header)
    *   [func (c *AccountsAlertsListCall) IfNoneMatch(entityTag string) *AccountsAlertsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAlertsListCall.IfNoneMatch)
    *   [func (c *AccountsAlertsListCall) Locale(locale string) *AccountsAlertsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAlertsListCall.Locale)

*   [type AccountsAlertsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAlertsService)
*       *   [func NewAccountsAlertsService(s *Service) *AccountsAlertsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#NewAccountsAlertsService)

*       *   [func (r *AccountsAlertsService) List(accountId string) *AccountsAlertsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAlertsService.List)

*   [type AccountsCustomchannelsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsAdunitsListCall)
*       *   [func (c *AccountsCustomchannelsAdunitsListCall) Context(ctx context.Context) *AccountsCustomchannelsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsAdunitsListCall.Context)
    *   [func (c *AccountsCustomchannelsAdunitsListCall) Do(opts ...googleapi.CallOption) (*AdUnits, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsAdunitsListCall.Do)
    *   [func (c *AccountsCustomchannelsAdunitsListCall) Fields(s ...googleapi.Field) *AccountsCustomchannelsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsAdunitsListCall.Fields)
    *   [func (c *AccountsCustomchannelsAdunitsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsAdunitsListCall.Header)
    *   [func (c *AccountsCustomchannelsAdunitsListCall) IfNoneMatch(entityTag string) *AccountsCustomchannelsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsAdunitsListCall.IfNoneMatch)
    *   [func (c *AccountsCustomchannelsAdunitsListCall) IncludeInactive(includeInactive bool) *AccountsCustomchannelsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsAdunitsListCall.IncludeInactive)
    *   [func (c *AccountsCustomchannelsAdunitsListCall) MaxResults(maxResults int64) *AccountsCustomchannelsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsAdunitsListCall.MaxResults)
    *   [func (c *AccountsCustomchannelsAdunitsListCall) PageToken(pageToken string) *AccountsCustomchannelsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsAdunitsListCall.PageToken)
    *   [func (c *AccountsCustomchannelsAdunitsListCall) Pages(ctx context.Context, f func(*AdUnits) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsAdunitsListCall.Pages)

*   [type AccountsCustomchannelsAdunitsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsAdunitsService)
*       *   [func NewAccountsCustomchannelsAdunitsService(s *Service) *AccountsCustomchannelsAdunitsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#NewAccountsCustomchannelsAdunitsService)

*       *   [func (r *AccountsCustomchannelsAdunitsService) List(accountId string, adClientId string, customChannelId string) *AccountsCustomchannelsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsAdunitsService.List)

*   [type AccountsCustomchannelsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsGetCall)
*       *   [func (c *AccountsCustomchannelsGetCall) Context(ctx context.Context) *AccountsCustomchannelsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsGetCall.Context)
    *   [func (c *AccountsCustomchannelsGetCall) Do(opts ...googleapi.CallOption) (*CustomChannel, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsGetCall.Do)
    *   [func (c *AccountsCustomchannelsGetCall) Fields(s ...googleapi.Field) *AccountsCustomchannelsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsGetCall.Fields)
    *   [func (c *AccountsCustomchannelsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsGetCall.Header)
    *   [func (c *AccountsCustomchannelsGetCall) IfNoneMatch(entityTag string) *AccountsCustomchannelsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsGetCall.IfNoneMatch)

*   [type AccountsCustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsListCall)
*       *   [func (c *AccountsCustomchannelsListCall) Context(ctx context.Context) *AccountsCustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsListCall.Context)
    *   [func (c *AccountsCustomchannelsListCall) Do(opts ...googleapi.CallOption) (*CustomChannels, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsListCall.Do)
    *   [func (c *AccountsCustomchannelsListCall) Fields(s ...googleapi.Field) *AccountsCustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsListCall.Fields)
    *   [func (c *AccountsCustomchannelsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsListCall.Header)
    *   [func (c *AccountsCustomchannelsListCall) IfNoneMatch(entityTag string) *AccountsCustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsListCall.IfNoneMatch)
    *   [func (c *AccountsCustomchannelsListCall) MaxResults(maxResults int64) *AccountsCustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsListCall.MaxResults)
    *   [func (c *AccountsCustomchannelsListCall) PageToken(pageToken string) *AccountsCustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsListCall.PageToken)
    *   [func (c *AccountsCustomchannelsListCall) Pages(ctx context.Context, f func(*CustomChannels) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsListCall.Pages)

*   [type AccountsCustomchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsService)
*       *   [func NewAccountsCustomchannelsService(s *Service) *AccountsCustomchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#NewAccountsCustomchannelsService)

*       *   [func (r *AccountsCustomchannelsService) Get(accountId string, adClientId string, customChannelId string) *AccountsCustomchannelsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsService.Get)
    *   [func (r *AccountsCustomchannelsService) List(accountId string, adClientId string) *AccountsCustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsService.List)

*   [type AccountsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsGetCall)
*       *   [func (c *AccountsGetCall) Context(ctx context.Context) *AccountsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsGetCall.Context)
    *   [func (c *AccountsGetCall) Do(opts ...googleapi.CallOption) (*Account, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsGetCall.Do)
    *   [func (c *AccountsGetCall) Fields(s ...googleapi.Field) *AccountsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsGetCall.Fields)
    *   [func (c *AccountsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsGetCall.Header)
    *   [func (c *AccountsGetCall) IfNoneMatch(entityTag string) *AccountsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsGetCall.IfNoneMatch)
    *   [func (c *AccountsGetCall) Tree(tree bool) *AccountsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsGetCall.Tree)

*   [type AccountsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsListCall)
*       *   [func (c *AccountsListCall) Context(ctx context.Context) *AccountsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsListCall.Context)
    *   [func (c *AccountsListCall) Do(opts ...googleapi.CallOption) (*Accounts, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsListCall.Do)
    *   [func (c *AccountsListCall) Fields(s ...googleapi.Field) *AccountsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsListCall.Fields)
    *   [func (c *AccountsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsListCall.Header)
    *   [func (c *AccountsListCall) IfNoneMatch(entityTag string) *AccountsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsListCall.IfNoneMatch)
    *   [func (c *AccountsListCall) MaxResults(maxResults int64) *AccountsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsListCall.MaxResults)
    *   [func (c *AccountsListCall) PageToken(pageToken string) *AccountsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsListCall.PageToken)
    *   [func (c *AccountsListCall) Pages(ctx context.Context, f func(*Accounts) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsListCall.Pages)

*   [type AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsGenerateCall)
*       *   [func (c *AccountsReportsGenerateCall) Context(ctx context.Context) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsGenerateCall.Context)
    *   [func (c *AccountsReportsGenerateCall) Currency(currency string) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsGenerateCall.Currency)
    *   [func (c *AccountsReportsGenerateCall) Dimension(dimension ...string) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsGenerateCall.Dimension)
    *   [func (c *AccountsReportsGenerateCall) Do(opts ...googleapi.CallOption) (*AdsenseReportsGenerateResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsGenerateCall.Do)
    *   [func (c *AccountsReportsGenerateCall) Download(opts ...googleapi.CallOption) (*http.Response, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsGenerateCall.Download)
    *   [func (c *AccountsReportsGenerateCall) Fields(s ...googleapi.Field) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsGenerateCall.Fields)
    *   [func (c *AccountsReportsGenerateCall) Filter(filter ...string) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsGenerateCall.Filter)
    *   [func (c *AccountsReportsGenerateCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsGenerateCall.Header)
    *   [func (c *AccountsReportsGenerateCall) IfNoneMatch(entityTag string) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsGenerateCall.IfNoneMatch)
    *   [func (c *AccountsReportsGenerateCall) Locale(locale string) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsGenerateCall.Locale)
    *   [func (c *AccountsReportsGenerateCall) MaxResults(maxResults int64) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsGenerateCall.MaxResults)
    *   [func (c *AccountsReportsGenerateCall) Metric(metric ...string) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsGenerateCall.Metric)
    *   [func (c *AccountsReportsGenerateCall) Sort(sort ...string) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsGenerateCall.Sort)
    *   [func (c *AccountsReportsGenerateCall) StartIndex(startIndex int64) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsGenerateCall.StartIndex)
    *   [func (c *AccountsReportsGenerateCall) UseTimezoneReporting(useTimezoneReporting bool) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsGenerateCall.UseTimezoneReporting)

*   [type AccountsReportsSavedGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsSavedGenerateCall)
*       *   [func (c *AccountsReportsSavedGenerateCall) Context(ctx context.Context) *AccountsReportsSavedGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsSavedGenerateCall.Context)
    *   [func (c *AccountsReportsSavedGenerateCall) Do(opts ...googleapi.CallOption) (*AdsenseReportsGenerateResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsSavedGenerateCall.Do)
    *   [func (c *AccountsReportsSavedGenerateCall) Fields(s ...googleapi.Field) *AccountsReportsSavedGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsSavedGenerateCall.Fields)
    *   [func (c *AccountsReportsSavedGenerateCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsSavedGenerateCall.Header)
    *   [func (c *AccountsReportsSavedGenerateCall) IfNoneMatch(entityTag string) *AccountsReportsSavedGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsSavedGenerateCall.IfNoneMatch)
    *   [func (c *AccountsReportsSavedGenerateCall) Locale(locale string) *AccountsReportsSavedGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsSavedGenerateCall.Locale)
    *   [func (c *AccountsReportsSavedGenerateCall) MaxResults(maxResults int64) *AccountsReportsSavedGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsSavedGenerateCall.MaxResults)
    *   [func (c *AccountsReportsSavedGenerateCall) StartIndex(startIndex int64) *AccountsReportsSavedGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsSavedGenerateCall.StartIndex)

*   [type AccountsReportsSavedListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsSavedListCall)
*       *   [func (c *AccountsReportsSavedListCall) Context(ctx context.Context) *AccountsReportsSavedListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsSavedListCall.Context)
    *   [func (c *AccountsReportsSavedListCall) Do(opts ...googleapi.CallOption) (*SavedReports, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsSavedListCall.Do)
    *   [func (c *AccountsReportsSavedListCall) Fields(s ...googleapi.Field) *AccountsReportsSavedListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsSavedListCall.Fields)
    *   [func (c *AccountsReportsSavedListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsSavedListCall.Header)
    *   [func (c *AccountsReportsSavedListCall) IfNoneMatch(entityTag string) *AccountsReportsSavedListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsSavedListCall.IfNoneMatch)
    *   [func (c *AccountsReportsSavedListCall) MaxResults(maxResults int64) *AccountsReportsSavedListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsSavedListCall.MaxResults)
    *   [func (c *AccountsReportsSavedListCall) PageToken(pageToken string) *AccountsReportsSavedListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsSavedListCall.PageToken)
    *   [func (c *AccountsReportsSavedListCall) Pages(ctx context.Context, f func(*SavedReports) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsSavedListCall.Pages)

*   [type AccountsReportsSavedService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsSavedService)
*       *   [func NewAccountsReportsSavedService(s *Service) *AccountsReportsSavedService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#NewAccountsReportsSavedService)

*       *   [func (r *AccountsReportsSavedService) Generate(accountId string, savedReportId string) *AccountsReportsSavedGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsSavedService.Generate)
    *   [func (r *AccountsReportsSavedService) List(accountId string) *AccountsReportsSavedListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsSavedService.List)

*   [type AccountsReportsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsService)
*       *   [func NewAccountsReportsService(s *Service) *AccountsReportsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#NewAccountsReportsService)

*       *   [func (r *AccountsReportsService) Generate(accountId string, startDate string, endDate string) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsService.Generate)

*   [type AccountsSavedadstylesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsSavedadstylesGetCall)
*       *   [func (c *AccountsSavedadstylesGetCall) Context(ctx context.Context) *AccountsSavedadstylesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsSavedadstylesGetCall.Context)
    *   [func (c *AccountsSavedadstylesGetCall) Do(opts ...googleapi.CallOption) (*SavedAdStyle, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsSavedadstylesGetCall.Do)
    *   [func (c *AccountsSavedadstylesGetCall) Fields(s ...googleapi.Field) *AccountsSavedadstylesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsSavedadstylesGetCall.Fields)
    *   [func (c *AccountsSavedadstylesGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsSavedadstylesGetCall.Header)
    *   [func (c *AccountsSavedadstylesGetCall) IfNoneMatch(entityTag string) *AccountsSavedadstylesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsSavedadstylesGetCall.IfNoneMatch)

*   [type AccountsSavedadstylesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsSavedadstylesListCall)
*       *   [func (c *AccountsSavedadstylesListCall) Context(ctx context.Context) *AccountsSavedadstylesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsSavedadstylesListCall.Context)
    *   [func (c *AccountsSavedadstylesListCall) Do(opts ...googleapi.CallOption) (*SavedAdStyles, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsSavedadstylesListCall.Do)
    *   [func (c *AccountsSavedadstylesListCall) Fields(s ...googleapi.Field) *AccountsSavedadstylesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsSavedadstylesListCall.Fields)
    *   [func (c *AccountsSavedadstylesListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsSavedadstylesListCall.Header)
    *   [func (c *AccountsSavedadstylesListCall) IfNoneMatch(entityTag string) *AccountsSavedadstylesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsSavedadstylesListCall.IfNoneMatch)
    *   [func (c *AccountsSavedadstylesListCall) MaxResults(maxResults int64) *AccountsSavedadstylesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsSavedadstylesListCall.MaxResults)
    *   [func (c *AccountsSavedadstylesListCall) PageToken(pageToken string) *AccountsSavedadstylesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsSavedadstylesListCall.PageToken)
    *   [func (c *AccountsSavedadstylesListCall) Pages(ctx context.Context, f func(*SavedAdStyles) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsSavedadstylesListCall.Pages)

*   [type AccountsSavedadstylesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsSavedadstylesService)
*       *   [func NewAccountsSavedadstylesService(s *Service) *AccountsSavedadstylesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#NewAccountsSavedadstylesService)

*       *   [func (r *AccountsSavedadstylesService) Get(accountId string, savedAdStyleId string) *AccountsSavedadstylesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsSavedadstylesService.Get)
    *   [func (r *AccountsSavedadstylesService) List(accountId string) *AccountsSavedadstylesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsSavedadstylesService.List)

*   [type AccountsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsService)
*       *   [func NewAccountsService(s *Service) *AccountsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#NewAccountsService)

*       *   [func (r *AccountsService) Get(accountId string) *AccountsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsService.Get)
    *   [func (r *AccountsService) List() *AccountsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsService.List)

*   [type AccountsUrlchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsUrlchannelsListCall)
*       *   [func (c *AccountsUrlchannelsListCall) Context(ctx context.Context) *AccountsUrlchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsUrlchannelsListCall.Context)
    *   [func (c *AccountsUrlchannelsListCall) Do(opts ...googleapi.CallOption) (*UrlChannels, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsUrlchannelsListCall.Do)
    *   [func (c *AccountsUrlchannelsListCall) Fields(s ...googleapi.Field) *AccountsUrlchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsUrlchannelsListCall.Fields)
    *   [func (c *AccountsUrlchannelsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsUrlchannelsListCall.Header)
    *   [func (c *AccountsUrlchannelsListCall) IfNoneMatch(entityTag string) *AccountsUrlchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsUrlchannelsListCall.IfNoneMatch)
    *   [func (c *AccountsUrlchannelsListCall) MaxResults(maxResults int64) *AccountsUrlchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsUrlchannelsListCall.MaxResults)
    *   [func (c *AccountsUrlchannelsListCall) PageToken(pageToken string) *AccountsUrlchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsUrlchannelsListCall.PageToken)
    *   [func (c *AccountsUrlchannelsListCall) Pages(ctx context.Context, f func(*UrlChannels) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsUrlchannelsListCall.Pages)

*   [type AccountsUrlchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsUrlchannelsService)
*       *   [func NewAccountsUrlchannelsService(s *Service) *AccountsUrlchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#NewAccountsUrlchannelsService)

*       *   [func (r *AccountsUrlchannelsService) List(accountId string, adClientId string) *AccountsUrlchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsUrlchannelsService.List)

*   [type AdClient](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdClient)
*       *   [func (s *AdClient) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdClient.MarshalJSON)

*   [type AdClients](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdClients)
*       *   [func (s *AdClients) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdClients.MarshalJSON)

*   [type AdCode](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdCode)
*       *   [func (s *AdCode) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdCode.MarshalJSON)

*   [type AdStyle](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdStyle)
*       *   [func (s *AdStyle) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdStyle.MarshalJSON)

*   [type AdStyleColors](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdStyleColors)
*       *   [func (s *AdStyleColors) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdStyleColors.MarshalJSON)

*   [type AdStyleFont](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdStyleFont)
*       *   [func (s *AdStyleFont) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdStyleFont.MarshalJSON)

*   [type AdUnit](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdUnit)
*       *   [func (s *AdUnit) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdUnit.MarshalJSON)

*   [type AdUnitContentAdsSettings](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdUnitContentAdsSettings)
*       *   [func (s *AdUnitContentAdsSettings) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdUnitContentAdsSettings.MarshalJSON)

*   [type AdUnitContentAdsSettingsBackupOption](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdUnitContentAdsSettingsBackupOption)
*       *   [func (s *AdUnitContentAdsSettingsBackupOption) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdUnitContentAdsSettingsBackupOption.MarshalJSON)

*   [type AdUnitFeedAdsSettings](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdUnitFeedAdsSettings)
*       *   [func (s *AdUnitFeedAdsSettings) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdUnitFeedAdsSettings.MarshalJSON)

*   [type AdUnitMobileContentAdsSettings](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdUnitMobileContentAdsSettings)
*       *   [func (s *AdUnitMobileContentAdsSettings) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdUnitMobileContentAdsSettings.MarshalJSON)

*   [type AdUnits](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdUnits)
*       *   [func (s *AdUnits) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdUnits.MarshalJSON)

*   [type AdclientsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdclientsListCall)
*       *   [func (c *AdclientsListCall) Context(ctx context.Context) *AdclientsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdclientsListCall.Context)
    *   [func (c *AdclientsListCall) Do(opts ...googleapi.CallOption) (*AdClients, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdclientsListCall.Do)
    *   [func (c *AdclientsListCall) Fields(s ...googleapi.Field) *AdclientsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdclientsListCall.Fields)
    *   [func (c *AdclientsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdclientsListCall.Header)
    *   [func (c *AdclientsListCall) IfNoneMatch(entityTag string) *AdclientsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdclientsListCall.IfNoneMatch)
    *   [func (c *AdclientsListCall) MaxResults(maxResults int64) *AdclientsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdclientsListCall.MaxResults)
    *   [func (c *AdclientsListCall) PageToken(pageToken string) *AdclientsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdclientsListCall.PageToken)
    *   [func (c *AdclientsListCall) Pages(ctx context.Context, f func(*AdClients) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdclientsListCall.Pages)

*   [type AdclientsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdclientsService)
*       *   [func NewAdclientsService(s *Service) *AdclientsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#NewAdclientsService)

*       *   [func (r *AdclientsService) List() *AdclientsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdclientsService.List)

*   [type AdsenseReportsGenerateResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdsenseReportsGenerateResponse)
*       *   [func (s *AdsenseReportsGenerateResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdsenseReportsGenerateResponse.MarshalJSON)

*   [type AdsenseReportsGenerateResponseHeaders](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdsenseReportsGenerateResponseHeaders)
*       *   [func (s *AdsenseReportsGenerateResponseHeaders) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdsenseReportsGenerateResponseHeaders.MarshalJSON)

*   [type AdunitsCustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsCustomchannelsListCall)
*       *   [func (c *AdunitsCustomchannelsListCall) Context(ctx context.Context) *AdunitsCustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsCustomchannelsListCall.Context)
    *   [func (c *AdunitsCustomchannelsListCall) Do(opts ...googleapi.CallOption) (*CustomChannels, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsCustomchannelsListCall.Do)
    *   [func (c *AdunitsCustomchannelsListCall) Fields(s ...googleapi.Field) *AdunitsCustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsCustomchannelsListCall.Fields)
    *   [func (c *AdunitsCustomchannelsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsCustomchannelsListCall.Header)
    *   [func (c *AdunitsCustomchannelsListCall) IfNoneMatch(entityTag string) *AdunitsCustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsCustomchannelsListCall.IfNoneMatch)
    *   [func (c *AdunitsCustomchannelsListCall) MaxResults(maxResults int64) *AdunitsCustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsCustomchannelsListCall.MaxResults)
    *   [func (c *AdunitsCustomchannelsListCall) PageToken(pageToken string) *AdunitsCustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsCustomchannelsListCall.PageToken)
    *   [func (c *AdunitsCustomchannelsListCall) Pages(ctx context.Context, f func(*CustomChannels) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsCustomchannelsListCall.Pages)

*   [type AdunitsCustomchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsCustomchannelsService)
*       *   [func NewAdunitsCustomchannelsService(s *Service) *AdunitsCustomchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#NewAdunitsCustomchannelsService)

*       *   [func (r *AdunitsCustomchannelsService) List(adClientId string, adUnitId string) *AdunitsCustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsCustomchannelsService.List)

*   [type AdunitsGetAdCodeCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsGetAdCodeCall)
*       *   [func (c *AdunitsGetAdCodeCall) Context(ctx context.Context) *AdunitsGetAdCodeCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsGetAdCodeCall.Context)
    *   [func (c *AdunitsGetAdCodeCall) Do(opts ...googleapi.CallOption) (*AdCode, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsGetAdCodeCall.Do)
    *   [func (c *AdunitsGetAdCodeCall) Fields(s ...googleapi.Field) *AdunitsGetAdCodeCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsGetAdCodeCall.Fields)
    *   [func (c *AdunitsGetAdCodeCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsGetAdCodeCall.Header)
    *   [func (c *AdunitsGetAdCodeCall) IfNoneMatch(entityTag string) *AdunitsGetAdCodeCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsGetAdCodeCall.IfNoneMatch)

*   [type AdunitsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsGetCall)
*       *   [func (c *AdunitsGetCall) Context(ctx context.Context) *AdunitsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsGetCall.Context)
    *   [func (c *AdunitsGetCall) Do(opts ...googleapi.CallOption) (*AdUnit, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsGetCall.Do)
    *   [func (c *AdunitsGetCall) Fields(s ...googleapi.Field) *AdunitsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsGetCall.Fields)
    *   [func (c *AdunitsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsGetCall.Header)
    *   [func (c *AdunitsGetCall) IfNoneMatch(entityTag string) *AdunitsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsGetCall.IfNoneMatch)

*   [type AdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsListCall)
*       *   [func (c *AdunitsListCall) Context(ctx context.Context) *AdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsListCall.Context)
    *   [func (c *AdunitsListCall) Do(opts ...googleapi.CallOption) (*AdUnits, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsListCall.Do)
    *   [func (c *AdunitsListCall) Fields(s ...googleapi.Field) *AdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsListCall.Fields)
    *   [func (c *AdunitsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsListCall.Header)
    *   [func (c *AdunitsListCall) IfNoneMatch(entityTag string) *AdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsListCall.IfNoneMatch)
    *   [func (c *AdunitsListCall) IncludeInactive(includeInactive bool) *AdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsListCall.IncludeInactive)
    *   [func (c *AdunitsListCall) MaxResults(maxResults int64) *AdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsListCall.MaxResults)
    *   [func (c *AdunitsListCall) PageToken(pageToken string) *AdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsListCall.PageToken)
    *   [func (c *AdunitsListCall) Pages(ctx context.Context, f func(*AdUnits) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsListCall.Pages)

*   [type AdunitsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsService)
*       *   [func NewAdunitsService(s *Service) *AdunitsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#NewAdunitsService)

*       *   [func (r *AdunitsService) Get(adClientId string, adUnitId string) *AdunitsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsService.Get)
    *   [func (r *AdunitsService) GetAdCode(adClientId string, adUnitId string) *AdunitsGetAdCodeCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsService.GetAdCode)
    *   [func (r *AdunitsService) List(adClientId string) *AdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsService.List)

*   [type Alert](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Alert)
*       *   [func (s *Alert) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Alert.MarshalJSON)

*   [type Alerts](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Alerts)
*       *   [func (s *Alerts) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Alerts.MarshalJSON)

*   [type AlertsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AlertsListCall)
*       *   [func (c *AlertsListCall) Context(ctx context.Context) *AlertsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AlertsListCall.Context)
    *   [func (c *AlertsListCall) Do(opts ...googleapi.CallOption) (*Alerts, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AlertsListCall.Do)
    *   [func (c *AlertsListCall) Fields(s ...googleapi.Field) *AlertsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AlertsListCall.Fields)
    *   [func (c *AlertsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AlertsListCall.Header)
    *   [func (c *AlertsListCall) IfNoneMatch(entityTag string) *AlertsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AlertsListCall.IfNoneMatch)
    *   [func (c *AlertsListCall) Locale(locale string) *AlertsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AlertsListCall.Locale)

*   [type AlertsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AlertsService)
*       *   [func NewAlertsService(s *Service) *AlertsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#NewAlertsService)

*       *   [func (r *AlertsService) List() *AlertsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AlertsService.List)

*   [type CustomChannel](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomChannel)
*       *   [func (s *CustomChannel) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomChannel.MarshalJSON)

*   [type CustomChannelTargetingInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomChannelTargetingInfo)
*       *   [func (s *CustomChannelTargetingInfo) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomChannelTargetingInfo.MarshalJSON)

*   [type CustomChannels](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomChannels)
*       *   [func (s *CustomChannels) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomChannels.MarshalJSON)

*   [type CustomchannelsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsAdunitsListCall)
*       *   [func (c *CustomchannelsAdunitsListCall) Context(ctx context.Context) *CustomchannelsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsAdunitsListCall.Context)
    *   [func (c *CustomchannelsAdunitsListCall) Do(opts ...googleapi.CallOption) (*AdUnits, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsAdunitsListCall.Do)
    *   [func (c *CustomchannelsAdunitsListCall) Fields(s ...googleapi.Field) *CustomchannelsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsAdunitsListCall.Fields)
    *   [func (c *CustomchannelsAdunitsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsAdunitsListCall.Header)
    *   [func (c *CustomchannelsAdunitsListCall) IfNoneMatch(entityTag string) *CustomchannelsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsAdunitsListCall.IfNoneMatch)
    *   [func (c *CustomchannelsAdunitsListCall) IncludeInactive(includeInactive bool) *CustomchannelsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsAdunitsListCall.IncludeInactive)
    *   [func (c *CustomchannelsAdunitsListCall) MaxResults(maxResults int64) *CustomchannelsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsAdunitsListCall.MaxResults)
    *   [func (c *CustomchannelsAdunitsListCall) PageToken(pageToken string) *CustomchannelsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsAdunitsListCall.PageToken)
    *   [func (c *CustomchannelsAdunitsListCall) Pages(ctx context.Context, f func(*AdUnits) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsAdunitsListCall.Pages)

*   [type CustomchannelsAdunitsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsAdunitsService)
*       *   [func NewCustomchannelsAdunitsService(s *Service) *CustomchannelsAdunitsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#NewCustomchannelsAdunitsService)

*       *   [func (r *CustomchannelsAdunitsService) List(adClientId string, customChannelId string) *CustomchannelsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsAdunitsService.List)

*   [type CustomchannelsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsGetCall)
*       *   [func (c *CustomchannelsGetCall) Context(ctx context.Context) *CustomchannelsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsGetCall.Context)
    *   [func (c *CustomchannelsGetCall) Do(opts ...googleapi.CallOption) (*CustomChannel, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsGetCall.Do)
    *   [func (c *CustomchannelsGetCall) Fields(s ...googleapi.Field) *CustomchannelsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsGetCall.Fields)
    *   [func (c *CustomchannelsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsGetCall.Header)
    *   [func (c *CustomchannelsGetCall) IfNoneMatch(entityTag string) *CustomchannelsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsGetCall.IfNoneMatch)

*   [type CustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsListCall)
*       *   [func (c *CustomchannelsListCall) Context(ctx context.Context) *CustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsListCall.Context)
    *   [func (c *CustomchannelsListCall) Do(opts ...googleapi.CallOption) (*CustomChannels, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsListCall.Do)
    *   [func (c *CustomchannelsListCall) Fields(s ...googleapi.Field) *CustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsListCall.Fields)
    *   [func (c *CustomchannelsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsListCall.Header)
    *   [func (c *CustomchannelsListCall) IfNoneMatch(entityTag string) *CustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsListCall.IfNoneMatch)
    *   [func (c *CustomchannelsListCall) MaxResults(maxResults int64) *CustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsListCall.MaxResults)
    *   [func (c *CustomchannelsListCall) PageToken(pageToken string) *CustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsListCall.PageToken)
    *   [func (c *CustomchannelsListCall) Pages(ctx context.Context, f func(*CustomChannels) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsListCall.Pages)

*   [type CustomchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsService)
*       *   [func NewCustomchannelsService(s *Service) *CustomchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#NewCustomchannelsService)

*       *   [func (r *CustomchannelsService) Get(adClientId string, customChannelId string) *CustomchannelsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsService.Get)
    *   [func (r *CustomchannelsService) List(adClientId string) *CustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsService.List)

*   [type Metadata](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Metadata)
*       *   [func (s *Metadata) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Metadata.MarshalJSON)

*   [type MetadataDimensionsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#MetadataDimensionsListCall)
*       *   [func (c *MetadataDimensionsListCall) Context(ctx context.Context) *MetadataDimensionsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#MetadataDimensionsListCall.Context)
    *   [func (c *MetadataDimensionsListCall) Do(opts ...googleapi.CallOption) (*Metadata, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#MetadataDimensionsListCall.Do)
    *   [func (c *MetadataDimensionsListCall) Fields(s ...googleapi.Field) *MetadataDimensionsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#MetadataDimensionsListCall.Fields)
    *   [func (c *MetadataDimensionsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#MetadataDimensionsListCall.Header)
    *   [func (c *MetadataDimensionsListCall) IfNoneMatch(entityTag string) *MetadataDimensionsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#MetadataDimensionsListCall.IfNoneMatch)

*   [type MetadataDimensionsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#MetadataDimensionsService)
*       *   [func NewMetadataDimensionsService(s *Service) *MetadataDimensionsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#NewMetadataDimensionsService)

*       *   [func (r *MetadataDimensionsService) List() *MetadataDimensionsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#MetadataDimensionsService.List)

*   [type MetadataMetricsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#MetadataMetricsListCall)
*       *   [func (c *MetadataMetricsListCall) Context(ctx context.Context) *MetadataMetricsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#MetadataMetricsListCall.Context)
    *   [func (c *MetadataMetricsListCall) Do(opts ...googleapi.CallOption) (*Metadata, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#MetadataMetricsListCall.Do)
    *   [func (c *MetadataMetricsListCall) Fields(s ...googleapi.Field) *MetadataMetricsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#MetadataMetricsListCall.Fields)
    *   [func (c *MetadataMetricsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#MetadataMetricsListCall.Header)
    *   [func (c *MetadataMetricsListCall) IfNoneMatch(entityTag string) *MetadataMetricsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#MetadataMetricsListCall.IfNoneMatch)

*   [type MetadataMetricsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#MetadataMetricsService)
*       *   [func NewMetadataMetricsService(s *Service) *MetadataMetricsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#NewMetadataMetricsService)

*       *   [func (r *MetadataMetricsService) List() *MetadataMetricsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#MetadataMetricsService.List)

*   [type MetadataService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#MetadataService)
*       *   [func NewMetadataService(s *Service) *MetadataService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#NewMetadataService)

*   [type ReportingMetadataEntry](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportingMetadataEntry)
*       *   [func (s *ReportingMetadataEntry) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportingMetadataEntry.MarshalJSON)

*   [type ReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsGenerateCall)
*       *   [func (c *ReportsGenerateCall) AccountId(accountId ...string) *ReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsGenerateCall.AccountId)
    *   [func (c *ReportsGenerateCall) Context(ctx context.Context) *ReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsGenerateCall.Context)
    *   [func (c *ReportsGenerateCall) Currency(currency string) *ReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsGenerateCall.Currency)
    *   [func (c *ReportsGenerateCall) Dimension(dimension ...string) *ReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsGenerateCall.Dimension)
    *   [func (c *ReportsGenerateCall) Do(opts ...googleapi.CallOption) (*AdsenseReportsGenerateResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsGenerateCall.Do)
    *   [func (c *ReportsGenerateCall) Download(opts ...googleapi.CallOption) (*http.Response, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsGenerateCall.Download)
    *   [func (c *ReportsGenerateCall) Fields(s ...googleapi.Field) *ReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsGenerateCall.Fields)
    *   [func (c *ReportsGenerateCall) Filter(filter ...string) *ReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsGenerateCall.Filter)
    *   [func (c *ReportsGenerateCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsGenerateCall.Header)
    *   [func (c *ReportsGenerateCall) IfNoneMatch(entityTag string) *ReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsGenerateCall.IfNoneMatch)
    *   [func (c *ReportsGenerateCall) Locale(locale string) *ReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsGenerateCall.Locale)
    *   [func (c *ReportsGenerateCall) MaxResults(maxResults int64) *ReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsGenerateCall.MaxResults)
    *   [func (c *ReportsGenerateCall) Metric(metric ...string) *ReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsGenerateCall.Metric)
    *   [func (c *ReportsGenerateCall) Sort(sort ...string) *ReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsGenerateCall.Sort)
    *   [func (c *ReportsGenerateCall) StartIndex(startIndex int64) *ReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsGenerateCall.StartIndex)
    *   [func (c *ReportsGenerateCall) UseTimezoneReporting(useTimezoneReporting bool) *ReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsGenerateCall.UseTimezoneReporting)

*   [type ReportsSavedGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsSavedGenerateCall)
*       *   [func (c *ReportsSavedGenerateCall) Context(ctx context.Context) *ReportsSavedGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsSavedGenerateCall.Context)
    *   [func (c *ReportsSavedGenerateCall) Do(opts ...googleapi.CallOption) (*AdsenseReportsGenerateResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsSavedGenerateCall.Do)
    *   [func (c *ReportsSavedGenerateCall) Fields(s ...googleapi.Field) *ReportsSavedGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsSavedGenerateCall.Fields)
    *   [func (c *ReportsSavedGenerateCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsSavedGenerateCall.Header)
    *   [func (c *ReportsSavedGenerateCall) IfNoneMatch(entityTag string) *ReportsSavedGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsSavedGenerateCall.IfNoneMatch)
    *   [func (c *ReportsSavedGenerateCall) Locale(locale string) *ReportsSavedGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsSavedGenerateCall.Locale)
    *   [func (c *ReportsSavedGenerateCall) MaxResults(maxResults int64) *ReportsSavedGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsSavedGenerateCall.MaxResults)
    *   [func (c *ReportsSavedGenerateCall) StartIndex(startIndex int64) *ReportsSavedGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsSavedGenerateCall.StartIndex)

*   [type ReportsSavedListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsSavedListCall)
*       *   [func (c *ReportsSavedListCall) Context(ctx context.Context) *ReportsSavedListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsSavedListCall.Context)
    *   [func (c *ReportsSavedListCall) Do(opts ...googleapi.CallOption) (*SavedReports, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsSavedListCall.Do)
    *   [func (c *ReportsSavedListCall) Fields(s ...googleapi.Field) *ReportsSavedListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsSavedListCall.Fields)
    *   [func (c *ReportsSavedListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsSavedListCall.Header)
    *   [func (c *ReportsSavedListCall) IfNoneMatch(entityTag string) *ReportsSavedListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsSavedListCall.IfNoneMatch)
    *   [func (c *ReportsSavedListCall) MaxResults(maxResults int64) *ReportsSavedListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsSavedListCall.MaxResults)
    *   [func (c *ReportsSavedListCall) PageToken(pageToken string) *ReportsSavedListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsSavedListCall.PageToken)
    *   [func (c *ReportsSavedListCall) Pages(ctx context.Context, f func(*SavedReports) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsSavedListCall.Pages)

*   [type ReportsSavedService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsSavedService)
*       *   [func NewReportsSavedService(s *Service) *ReportsSavedService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#NewReportsSavedService)

*       *   [func (r *ReportsSavedService) Generate(savedReportId string) *ReportsSavedGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsSavedService.Generate)
    *   [func (r *ReportsSavedService) List() *ReportsSavedListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsSavedService.List)

*   [type ReportsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsService)
*       *   [func NewReportsService(s *Service) *ReportsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#NewReportsService)

*       *   [func (r *ReportsService) Generate(startDate string, endDate string) *ReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsService.Generate)

*   [type SavedAdStyle](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#SavedAdStyle)
*       *   [func (s *SavedAdStyle) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#SavedAdStyle.MarshalJSON)

*   [type SavedAdStyles](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#SavedAdStyles)
*       *   [func (s *SavedAdStyles) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#SavedAdStyles.MarshalJSON)

*   [type SavedReport](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#SavedReport)
*       *   [func (s *SavedReport) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#SavedReport.MarshalJSON)

*   [type SavedReports](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#SavedReports)
*       *   [func (s *SavedReports) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#SavedReports.MarshalJSON)

*   [type SavedadstylesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#SavedadstylesGetCall)
*       *   [func (c *SavedadstylesGetCall) Context(ctx context.Context) *SavedadstylesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#SavedadstylesGetCall.Context)
    *   [func (c *SavedadstylesGetCall) Do(opts ...googleapi.CallOption) (*SavedAdStyle, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#SavedadstylesGetCall.Do)
    *   [func (c *SavedadstylesGetCall) Fields(s ...googleapi.Field) *SavedadstylesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#SavedadstylesGetCall.Fields)
    *   [func (c *SavedadstylesGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#SavedadstylesGetCall.Header)
    *   [func (c *SavedadstylesGetCall) IfNoneMatch(entityTag string) *SavedadstylesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#SavedadstylesGetCall.IfNoneMatch)

*   [type SavedadstylesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#SavedadstylesListCall)
*       *   [func (c *SavedadstylesListCall) Context(ctx context.Context) *SavedadstylesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#SavedadstylesListCall.Context)
    *   [func (c *SavedadstylesListCall) Do(opts ...googleapi.CallOption) (*SavedAdStyles, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#SavedadstylesListCall.Do)
    *   [func (c *SavedadstylesListCall) Fields(s ...googleapi.Field) *SavedadstylesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#SavedadstylesListCall.Fields)
    *   [func (c *SavedadstylesListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#SavedadstylesListCall.Header)
    *   [func (c *SavedadstylesListCall) IfNoneMatch(entityTag string) *SavedadstylesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#SavedadstylesListCall.IfNoneMatch)
    *   [func (c *SavedadstylesListCall) MaxResults(maxResults int64) *SavedadstylesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#SavedadstylesListCall.MaxResults)
    *   [func (c *SavedadstylesListCall) PageToken(pageToken string) *SavedadstylesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#SavedadstylesListCall.PageToken)
    *   [func (c *SavedadstylesListCall) Pages(ctx context.Context, f func(*SavedAdStyles) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#SavedadstylesListCall.Pages)

*   [type SavedadstylesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#SavedadstylesService)
*       *   [func NewSavedadstylesService(s *Service) *SavedadstylesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#NewSavedadstylesService)

*       *   [func (r *SavedadstylesService) Get(savedAdStyleId string) *SavedadstylesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#SavedadstylesService.Get)
    *   [func (r *SavedadstylesService) List() *SavedadstylesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#SavedadstylesService.List)

*   [type Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Service)
*       *   [func New(client *http.Client) (*Service, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#New)deprecated
    *   [func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#NewService)

*   [type UrlChannel](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#UrlChannel)
*       *   [func (s *UrlChannel) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#UrlChannel.MarshalJSON)

*   [type UrlChannels](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#UrlChannels)
*       *   [func (s *UrlChannels) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#UrlChannels.MarshalJSON)

*   [type UrlchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#UrlchannelsListCall)
*       *   [func (c *UrlchannelsListCall) Context(ctx context.Context) *UrlchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#UrlchannelsListCall.Context)
    *   [func (c *UrlchannelsListCall) Do(opts ...googleapi.CallOption) (*UrlChannels, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#UrlchannelsListCall.Do)
    *   [func (c *UrlchannelsListCall) Fields(s ...googleapi.Field) *UrlchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#UrlchannelsListCall.Fields)
    *   [func (c *UrlchannelsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#UrlchannelsListCall.Header)
    *   [func (c *UrlchannelsListCall) IfNoneMatch(entityTag string) *UrlchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#UrlchannelsListCall.IfNoneMatch)
    *   [func (c *UrlchannelsListCall) MaxResults(maxResults int64) *UrlchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#UrlchannelsListCall.MaxResults)
    *   [func (c *UrlchannelsListCall) PageToken(pageToken string) *UrlchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#UrlchannelsListCall.PageToken)
    *   [func (c *UrlchannelsListCall) Pages(ctx context.Context, f func(*UrlChannels) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#UrlchannelsListCall.Pages)

*   [type UrlchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#UrlchannelsService)
*       *   [func NewUrlchannelsService(s *Service) *UrlchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#NewUrlchannelsService)

*       *   [func (r *UrlchannelsService) List(adClientId string) *UrlchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#UrlchannelsService.List)

[View Source](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/adsense/v1.3/adsense-gen.go#L82)

const (
	AdsenseScope = "https://www.googleapis.com/auth/adsense"

	AdsenseReadonlyScope = "https://www.googleapis.com/auth/adsense.readonly"
)

OAuth2 scopes used by this API.

This section is empty.

This section is empty.

type Account struct {
	Id [string](https://pkg.go.dev/builtin#string) `json:"id,omitempty"`

	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`

	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`

	Premium [bool](https://pkg.go.dev/builtin#bool) `json:"premium,omitempty"`

	SubAccounts []*[Account](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Account) `json:"subAccounts,omitempty"`

	
	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type Accounts struct {
	Etag [string](https://pkg.go.dev/builtin#string) `json:"etag,omitempty"`

	Items []*[Account](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Account) `json:"items,omitempty"`

	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`

	
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	
	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type AccountsAdclientsListCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.accounts.adclients.list" call. Exactly one of *AdClients or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AdClients.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

MaxResults sets the optional parameter "maxResults": The maximum number of ad clients to include in the response, used for paging.

PageToken sets the optional parameter "pageToken": A continuation token, used to page through ad clients. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsAdclientsService struct {
	
}

func NewAccountsAdclientsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Service)) *[AccountsAdclientsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdclientsService)

List: List all ad clients in the specified account.

type AccountsAdunitsCustomchannelsListCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.accounts.adunits.customchannels.list" call. Exactly one of *CustomChannels or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *CustomChannels.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

MaxResults sets the optional parameter "maxResults": The maximum number of custom channels to include in the response, used for paging.

PageToken sets the optional parameter "pageToken": A continuation token, used to page through custom channels. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsAdunitsCustomchannelsService struct {
	
}

func NewAccountsAdunitsCustomchannelsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Service)) *[AccountsAdunitsCustomchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsCustomchannelsService)

List: List all custom channels which the specified ad unit belongs to.

type AccountsAdunitsGetAdCodeCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.accounts.adunits.getAdCode" call. Exactly one of *AdCode or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AdCode.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type AccountsAdunitsGetCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.accounts.adunits.get" call. Exactly one of *AdUnit or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AdUnit.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type AccountsAdunitsListCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.accounts.adunits.list" call. Exactly one of *AdUnits or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AdUnits.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (c *[AccountsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsListCall)) IncludeInactive(includeInactive [bool](https://pkg.go.dev/builtin#bool)) *[AccountsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsListCall)

IncludeInactive sets the optional parameter "includeInactive": Whether to include inactive ad units. Default: true.

MaxResults sets the optional parameter "maxResults": The maximum number of ad units to include in the response, used for paging.

PageToken sets the optional parameter "pageToken": A continuation token, used to page through ad units. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsAdunitsService struct {
 Customchannels *[AccountsAdunitsCustomchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsCustomchannelsService)	
}

func NewAccountsAdunitsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Service)) *[AccountsAdunitsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsService)

Get: Gets the specified ad unit in the specified ad client for the specified account.

GetAdCode: Get ad code for the specified ad unit.

List: List all ad units in the specified ad client for the specified account.

type AccountsAlertsListCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.accounts.alerts.list" call. Exactly one of *Alerts or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Alerts.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

Locale sets the optional parameter "locale": The locale to use for translating alert messages. The account locale will be used if this is not supplied. The AdSense default (English) will be used if the supplied locale is invalid or unsupported.

type AccountsAlertsService struct {
	
}

func NewAccountsAlertsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Service)) *[AccountsAlertsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAlertsService)

List: List the alerts for the specified AdSense account.

type AccountsCustomchannelsAdunitsListCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.accounts.customchannels.adunits.list" call. Exactly one of *AdUnits or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AdUnits.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

IncludeInactive sets the optional parameter "includeInactive": Whether to include inactive ad units. Default: true.

MaxResults sets the optional parameter "maxResults": The maximum number of ad units to include in the response, used for paging.

PageToken sets the optional parameter "pageToken": A continuation token, used to page through ad units. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsCustomchannelsAdunitsService struct {
	
}

func NewAccountsCustomchannelsAdunitsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Service)) *[AccountsCustomchannelsAdunitsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsAdunitsService)

List: List all ad units in the specified custom channel.

type AccountsCustomchannelsGetCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.accounts.customchannels.get" call. Exactly one of *CustomChannel or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *CustomChannel.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type AccountsCustomchannelsListCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.accounts.customchannels.list" call. Exactly one of *CustomChannels or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *CustomChannels.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

MaxResults sets the optional parameter "maxResults": The maximum number of custom channels to include in the response, used for paging.

PageToken sets the optional parameter "pageToken": A continuation token, used to page through custom channels. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsCustomchannelsService struct {
 Adunits *[AccountsCustomchannelsAdunitsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsAdunitsService)	
}

func NewAccountsCustomchannelsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Service)) *[AccountsCustomchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsService)

Get: Get the specified custom channel from the specified ad client for the specified account.

List: List all custom channels in the specified ad client for the specified account.

type AccountsGetCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.accounts.get" call. Exactly one of *Account or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Account.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

Tree sets the optional parameter "tree": Whether the tree of sub accounts should be returned.

type AccountsListCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.accounts.list" call. Exactly one of *Accounts or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Accounts.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (c *[AccountsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsListCall)) MaxResults(maxResults [int64](https://pkg.go.dev/builtin#int64)) *[AccountsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsListCall)

MaxResults sets the optional parameter "maxResults": The maximum number of accounts to include in the response, used for paging.

PageToken sets the optional parameter "pageToken": A continuation token, used to page through accounts. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsReportsGenerateCall struct {
	
}

Context sets the context to be used in this call's Do and Download methods. Any pending HTTP request will be aborted if the provided context is canceled.

Currency sets the optional parameter "currency": Optional currency to use when reporting on monetary metrics. Defaults to the account's currency if not set.

Dimension sets the optional parameter "dimension": Dimensions to base the report on.

Do executes the "adsense.accounts.reports.generate" call. Exactly one of *AdsenseReportsGenerateResponse or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AdsenseReportsGenerateResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Download fetches the API endpoint's "media" value, instead of the normal API response value. If the returned error is nil, the Response is guaranteed to have a 2xx status code. Callers must close the Response.Body as usual.

Filter sets the optional parameter "filter": Filters to be run on the report.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

Locale sets the optional parameter "locale": Optional locale to use for translating report output to a local language. Defaults to "en_US" if not specified.

MaxResults sets the optional parameter "maxResults": The maximum number of rows of report data to return.

Metric sets the optional parameter "metric": Numeric columns to include in the report.

Sort sets the optional parameter "sort": The name of a dimension or metric to sort the resulting report on, optionally prefixed with "+" to sort ascending or "-" to sort descending. If no prefix is specified, the column is sorted ascending.

StartIndex sets the optional parameter "startIndex": Index of the first row of report data to return.

func (c *[AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsGenerateCall)) UseTimezoneReporting(useTimezoneReporting [bool](https://pkg.go.dev/builtin#bool)) *[AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsGenerateCall)

UseTimezoneReporting sets the optional parameter "useTimezoneReporting": Whether the report should be generated in the AdSense account's local timezone. If false default PST/PDT timezone will be used.

type AccountsReportsSavedGenerateCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.accounts.reports.saved.generate" call. Exactly one of *AdsenseReportsGenerateResponse or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AdsenseReportsGenerateResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

Locale sets the optional parameter "locale": Optional locale to use for translating report output to a local language. Defaults to "en_US" if not specified.

MaxResults sets the optional parameter "maxResults": The maximum number of rows of report data to return.

StartIndex sets the optional parameter "startIndex": Index of the first row of report data to return.

type AccountsReportsSavedListCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.accounts.reports.saved.list" call. Exactly one of *SavedReports or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *SavedReports.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

MaxResults sets the optional parameter "maxResults": The maximum number of saved reports to include in the response, used for paging.

PageToken sets the optional parameter "pageToken": A continuation token, used to page through saved reports. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsReportsSavedService struct {
	
}

func NewAccountsReportsSavedService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Service)) *[AccountsReportsSavedService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsSavedService)

Generate: Generate an AdSense report based on the saved report ID sent in the query parameters.

List: List all saved reports in the specified AdSense account.

type AccountsReportsService struct {
 Saved *[AccountsReportsSavedService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsSavedService)	
}

func NewAccountsReportsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Service)) *[AccountsReportsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsService)

Generate: Generate an AdSense report based on the report request sent in the query parameters. Returns the result as JSON; to retrieve output in CSV format specify "alt=csv" as a query parameter.

type AccountsSavedadstylesGetCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.accounts.savedadstyles.get" call. Exactly one of *SavedAdStyle or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *SavedAdStyle.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type AccountsSavedadstylesListCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.accounts.savedadstyles.list" call. Exactly one of *SavedAdStyles or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *SavedAdStyles.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

MaxResults sets the optional parameter "maxResults": The maximum number of saved ad styles to include in the response, used for paging.

PageToken sets the optional parameter "pageToken": A continuation token, used to page through saved ad styles. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsSavedadstylesService struct {
	
}

func NewAccountsSavedadstylesService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Service)) *[AccountsSavedadstylesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsSavedadstylesService)

Get: List a specific saved ad style for the specified account.

List: List all saved ad styles in the specified account.

type AccountsService struct {
 Adclients *[AccountsAdclientsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdclientsService)
 Adunits *[AccountsAdunitsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAdunitsService)
 Alerts *[AccountsAlertsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsAlertsService)
 Customchannels *[AccountsCustomchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsCustomchannelsService)
 Reports *[AccountsReportsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsReportsService)
 Savedadstyles *[AccountsSavedadstylesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsSavedadstylesService)
 Urlchannels *[AccountsUrlchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsUrlchannelsService)	
}

func NewAccountsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Service)) *[AccountsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsService)

Get: Get information about the selected AdSense account.

func (r *[AccountsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsService)) List() *[AccountsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsListCall)

List: List all accounts available to this AdSense account.

type AccountsUrlchannelsListCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.accounts.urlchannels.list" call. Exactly one of *UrlChannels or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *UrlChannels.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

MaxResults sets the optional parameter "maxResults": The maximum number of URL channels to include in the response, used for paging.

PageToken sets the optional parameter "pageToken": A continuation token, used to page through URL channels. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsUrlchannelsService struct {
	
}

func NewAccountsUrlchannelsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Service)) *[AccountsUrlchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsUrlchannelsService)

List: List all URL channels in the specified ad client for the specified account.

type AdClient struct {
	ArcOptIn [bool](https://pkg.go.dev/builtin#bool) `json:"arcOptIn,omitempty"`

	Id [string](https://pkg.go.dev/builtin#string) `json:"id,omitempty"`

	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`

	
	ProductCode [string](https://pkg.go.dev/builtin#string) `json:"productCode,omitempty"`

	SupportsReporting [bool](https://pkg.go.dev/builtin#bool) `json:"supportsReporting,omitempty"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type AdClients struct {
	Etag [string](https://pkg.go.dev/builtin#string) `json:"etag,omitempty"`

	Items []*[AdClient](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdClient) `json:"items,omitempty"`

	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`

	
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	
	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type AdStyle struct {
	
	
	Colors *[AdStyleColors](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdStyleColors) `json:"colors,omitempty"`

	
	Corners [string](https://pkg.go.dev/builtin#string) `json:"corners,omitempty"`

	Font *[AdStyleFont](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdStyleFont) `json:"font,omitempty"`

	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type AdStyleColors struct {
	Background [string](https://pkg.go.dev/builtin#string) `json:"background,omitempty"`

	Border [string](https://pkg.go.dev/builtin#string) `json:"border,omitempty"`

	Text [string](https://pkg.go.dev/builtin#string) `json:"text,omitempty"`

	Title [string](https://pkg.go.dev/builtin#string) `json:"title,omitempty"`

	Url [string](https://pkg.go.dev/builtin#string) `json:"url,omitempty"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

AdStyleColors: The colors which are included in the style. These are represented as six hexadecimal characters, similar to HTML color codes, but without the leading hash.

type AdStyleFont struct {
	Family [string](https://pkg.go.dev/builtin#string) `json:"family,omitempty"`

	Size [string](https://pkg.go.dev/builtin#string) `json:"size,omitempty"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

AdStyleFont: The font which is included in the style.

type AdUnit struct {
	
	Code [string](https://pkg.go.dev/builtin#string) `json:"code,omitempty"`

	
	ContentAdsSettings *[AdUnitContentAdsSettings](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdUnitContentAdsSettings) `json:"contentAdsSettings,omitempty"`

	CustomStyle *[AdStyle](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdStyle) `json:"customStyle,omitempty"`

	FeedAdsSettings *[AdUnitFeedAdsSettings](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdUnitFeedAdsSettings) `json:"feedAdsSettings,omitempty"`

	
	
	Id [string](https://pkg.go.dev/builtin#string) `json:"id,omitempty"`

	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`

	
	MobileContentAdsSettings *[AdUnitMobileContentAdsSettings](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdUnitMobileContentAdsSettings) `json:"mobileContentAdsSettings,omitempty"`

	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`

	
	SavedStyleId [string](https://pkg.go.dev/builtin#string) `json:"savedStyleId,omitempty"`

	
	
	
	
	
	
	
	
	Status [string](https://pkg.go.dev/builtin#string) `json:"status,omitempty"`

	
	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

#### type [AdUnitContentAdsSettings](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/adsense/v1.3/adsense-gen.go#L813)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdUnitContentAdsSettings "Go to AdUnitContentAdsSettings")

type AdUnitContentAdsSettings struct {
	
	BackupOption *[AdUnitContentAdsSettingsBackupOption](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdUnitContentAdsSettingsBackupOption) `json:"backupOption,omitempty"`

	Size [string](https://pkg.go.dev/builtin#string) `json:"size,omitempty"`

	Type [string](https://pkg.go.dev/builtin#string) `json:"type,omitempty"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

AdUnitContentAdsSettings: Settings specific to content ads (AFC) and highend mobile content ads (AFMC - deprecated).

#### type [AdUnitContentAdsSettingsBackupOption](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/adsense/v1.3/adsense-gen.go#L849)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdUnitContentAdsSettingsBackupOption "Go to AdUnitContentAdsSettingsBackupOption")

type AdUnitContentAdsSettingsBackupOption struct {
	Color [string](https://pkg.go.dev/builtin#string) `json:"color,omitempty"`

	
	Type [string](https://pkg.go.dev/builtin#string) `json:"type,omitempty"`

	Url [string](https://pkg.go.dev/builtin#string) `json:"url,omitempty"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

AdUnitContentAdsSettingsBackupOption: The backup option to be used in instances where no ad is available.

#### func (*AdUnitContentAdsSettingsBackupOption) [MarshalJSON](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/adsense/v1.3/adsense-gen.go#L877)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdUnitContentAdsSettingsBackupOption.MarshalJSON "Go to AdUnitContentAdsSettingsBackupOption.MarshalJSON")

type AdUnitFeedAdsSettings struct {
	AdPosition [string](https://pkg.go.dev/builtin#string) `json:"adPosition,omitempty"`

	
	Frequency [int64](https://pkg.go.dev/builtin#int64) `json:"frequency,omitempty"`

	
	MinimumWordCount [int64](https://pkg.go.dev/builtin#int64) `json:"minimumWordCount,omitempty"`

	Type [string](https://pkg.go.dev/builtin#string) `json:"type,omitempty"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

AdUnitFeedAdsSettings: Settings specific to feed ads (AFF) - deprecated.

#### type [AdUnitMobileContentAdsSettings](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/adsense/v1.3/adsense-gen.go#L925)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdUnitMobileContentAdsSettings "Go to AdUnitMobileContentAdsSettings")

type AdUnitMobileContentAdsSettings struct {
	MarkupLanguage [string](https://pkg.go.dev/builtin#string) `json:"markupLanguage,omitempty"`

	ScriptingLanguage [string](https://pkg.go.dev/builtin#string) `json:"scriptingLanguage,omitempty"`

	Size [string](https://pkg.go.dev/builtin#string) `json:"size,omitempty"`

	Type [string](https://pkg.go.dev/builtin#string) `json:"type,omitempty"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

AdUnitMobileContentAdsSettings: Settings specific to WAP mobile content ads (AFMC) - deprecated.

type AdUnits struct {
	Etag [string](https://pkg.go.dev/builtin#string) `json:"etag,omitempty"`

	Items []*[AdUnit](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdUnit) `json:"items,omitempty"`

	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`

	
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	
	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type AdclientsListCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.adclients.list" call. Exactly one of *AdClients or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AdClients.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

MaxResults sets the optional parameter "maxResults": The maximum number of ad clients to include in the response, used for paging.

PageToken sets the optional parameter "pageToken": A continuation token, used to page through ad clients. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AdclientsService struct {
	
}

func NewAdclientsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Service)) *[AdclientsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdclientsService)

func (r *[AdclientsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdclientsService)) List() *[AdclientsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdclientsListCall)

List: List all ad clients in this AdSense account.

type AdsenseReportsGenerateResponse struct {
	
	
	Averages [][string](https://pkg.go.dev/builtin#string) `json:"averages,omitempty"`

	
	
	Headers []*[AdsenseReportsGenerateResponseHeaders](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdsenseReportsGenerateResponseHeaders) `json:"headers,omitempty"`

	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`

	
	
	
	Rows [][][string](https://pkg.go.dev/builtin#string) `json:"rows,omitempty"`

	
	
	TotalMatchedRows [int64](https://pkg.go.dev/builtin#int64) `json:"totalMatchedRows,omitempty,string"`

	
	
	Totals [][string](https://pkg.go.dev/builtin#string) `json:"totals,omitempty"`

	Warnings [][string](https://pkg.go.dev/builtin#string) `json:"warnings,omitempty"`

	
	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type AdsenseReportsGenerateResponseHeaders struct {
	
	Currency [string](https://pkg.go.dev/builtin#string) `json:"currency,omitempty"`

	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`

	
	Type [string](https://pkg.go.dev/builtin#string) `json:"type,omitempty"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type AdunitsCustomchannelsListCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.adunits.customchannels.list" call. Exactly one of *CustomChannels or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *CustomChannels.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

MaxResults sets the optional parameter "maxResults": The maximum number of custom channels to include in the response, used for paging.

PageToken sets the optional parameter "pageToken": A continuation token, used to page through custom channels. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AdunitsCustomchannelsService struct {
	
}

func NewAdunitsCustomchannelsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Service)) *[AdunitsCustomchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsCustomchannelsService)

List: List all custom channels which the specified ad unit belongs to.

type AdunitsGetAdCodeCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.adunits.getAdCode" call. Exactly one of *AdCode or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AdCode.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type AdunitsGetCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.adunits.get" call. Exactly one of *AdUnit or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AdUnit.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type AdunitsListCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.adunits.list" call. Exactly one of *AdUnits or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AdUnits.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (c *[AdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsListCall)) IncludeInactive(includeInactive [bool](https://pkg.go.dev/builtin#bool)) *[AdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsListCall)

IncludeInactive sets the optional parameter "includeInactive": Whether to include inactive ad units. Default: true.

func (c *[AdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsListCall)) MaxResults(maxResults [int64](https://pkg.go.dev/builtin#int64)) *[AdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsListCall)

MaxResults sets the optional parameter "maxResults": The maximum number of ad units to include in the response, used for paging.

PageToken sets the optional parameter "pageToken": A continuation token, used to page through ad units. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AdunitsService struct {
 Customchannels *[AdunitsCustomchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsCustomchannelsService)	
}

func NewAdunitsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Service)) *[AdunitsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsService)

Get: Gets the specified ad unit in the specified ad client.

GetAdCode: Get ad code for the specified ad unit.

List: List all ad units in the specified ad client for this AdSense account.

type Alert struct {
	
	
	Id [string](https://pkg.go.dev/builtin#string) `json:"id,omitempty"`

	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`

	Message [string](https://pkg.go.dev/builtin#string) `json:"message,omitempty"`

	
	Severity [string](https://pkg.go.dev/builtin#string) `json:"severity,omitempty"`

	
	
	
	Type [string](https://pkg.go.dev/builtin#string) `json:"type,omitempty"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type AlertsListCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.alerts.list" call. Exactly one of *Alerts or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Alerts.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

Locale sets the optional parameter "locale": The locale to use for translating alert messages. The account locale will be used if this is not supplied. The AdSense default (English) will be used if the supplied locale is invalid or unsupported.

type AlertsService struct {
	
}

func NewAlertsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Service)) *[AlertsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AlertsService)

func (r *[AlertsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AlertsService)) List() *[AlertsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AlertsListCall)

List: List the alerts for this AdSense account.

type CustomChannel struct {
	
	Code [string](https://pkg.go.dev/builtin#string) `json:"code,omitempty"`

	
	
	Id [string](https://pkg.go.dev/builtin#string) `json:"id,omitempty"`

	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`

	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`

	
	TargetingInfo *[CustomChannelTargetingInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomChannelTargetingInfo) `json:"targetingInfo,omitempty"`

	
	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type CustomChannelTargetingInfo struct {
	AdsAppearOn [string](https://pkg.go.dev/builtin#string) `json:"adsAppearOn,omitempty"`

	Description [string](https://pkg.go.dev/builtin#string) `json:"description,omitempty"`

	
	
	
	
	
	Location [string](https://pkg.go.dev/builtin#string) `json:"location,omitempty"`

	SiteLanguage [string](https://pkg.go.dev/builtin#string) `json:"siteLanguage,omitempty"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

CustomChannelTargetingInfo: The targeting information of this custom channel, if activated.

type CustomChannels struct {
	Etag [string](https://pkg.go.dev/builtin#string) `json:"etag,omitempty"`

	Items []*[CustomChannel](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomChannel) `json:"items,omitempty"`

	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`

	
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	
	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type CustomchannelsAdunitsListCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.customchannels.adunits.list" call. Exactly one of *AdUnits or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AdUnits.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (c *[CustomchannelsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsAdunitsListCall)) IncludeInactive(includeInactive [bool](https://pkg.go.dev/builtin#bool)) *[CustomchannelsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsAdunitsListCall)

IncludeInactive sets the optional parameter "includeInactive": Whether to include inactive ad units. Default: true.

MaxResults sets the optional parameter "maxResults": The maximum number of ad units to include in the response, used for paging.

PageToken sets the optional parameter "pageToken": A continuation token, used to page through ad units. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type CustomchannelsAdunitsService struct {
	
}

func NewCustomchannelsAdunitsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Service)) *[CustomchannelsAdunitsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsAdunitsService)

List: List all ad units in the specified custom channel.

type CustomchannelsGetCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.customchannels.get" call. Exactly one of *CustomChannel or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *CustomChannel.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type CustomchannelsListCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.customchannels.list" call. Exactly one of *CustomChannels or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *CustomChannels.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

MaxResults sets the optional parameter "maxResults": The maximum number of custom channels to include in the response, used for paging.

PageToken sets the optional parameter "pageToken": A continuation token, used to page through custom channels. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type CustomchannelsService struct {
 Adunits *[CustomchannelsAdunitsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsAdunitsService)	
}

func NewCustomchannelsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Service)) *[CustomchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsService)

Get: Get the specified custom channel from the specified ad client.

List: List all custom channels in the specified ad client for this AdSense account.

type MetadataDimensionsListCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.metadata.dimensions.list" call. Exactly one of *Metadata or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Metadata.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type MetadataDimensionsService struct {
	
}

func NewMetadataDimensionsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Service)) *[MetadataDimensionsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#MetadataDimensionsService)

List: List the metadata for the dimensions available to this AdSense account.

type MetadataMetricsListCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.metadata.metrics.list" call. Exactly one of *Metadata or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Metadata.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type MetadataMetricsService struct {
	
}

func NewMetadataMetricsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Service)) *[MetadataMetricsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#MetadataMetricsService)

List: List the metadata for the metrics available to this AdSense account.

type MetadataService struct {
 Dimensions *[MetadataDimensionsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#MetadataDimensionsService)
 Metrics *[MetadataMetricsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#MetadataMetricsService)	
}

func NewMetadataService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Service)) *[MetadataService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#MetadataService)

type ReportingMetadataEntry struct {
	
	
	CompatibleDimensions [][string](https://pkg.go.dev/builtin#string) `json:"compatibleDimensions,omitempty"`

	
	CompatibleMetrics [][string](https://pkg.go.dev/builtin#string) `json:"compatibleMetrics,omitempty"`

	
	Id [string](https://pkg.go.dev/builtin#string) `json:"id,omitempty"`

	
	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`

	
	
	
	
	RequiredDimensions [][string](https://pkg.go.dev/builtin#string) `json:"requiredDimensions,omitempty"`

	
	
	
	
	RequiredMetrics [][string](https://pkg.go.dev/builtin#string) `json:"requiredMetrics,omitempty"`

	
	SupportedProducts [][string](https://pkg.go.dev/builtin#string) `json:"supportedProducts,omitempty"`

	
	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type ReportsGenerateCall struct {
	
}

AccountId sets the optional parameter "accountId": Accounts upon which to report.

Context sets the context to be used in this call's Do and Download methods. Any pending HTTP request will be aborted if the provided context is canceled.

Currency sets the optional parameter "currency": Optional currency to use when reporting on monetary metrics. Defaults to the account's currency if not set.

Dimension sets the optional parameter "dimension": Dimensions to base the report on.

Do executes the "adsense.reports.generate" call. Exactly one of *AdsenseReportsGenerateResponse or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AdsenseReportsGenerateResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Download fetches the API endpoint's "media" value, instead of the normal API response value. If the returned error is nil, the Response is guaranteed to have a 2xx status code. Callers must close the Response.Body as usual.

Filter sets the optional parameter "filter": Filters to be run on the report.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

Locale sets the optional parameter "locale": Optional locale to use for translating report output to a local language. Defaults to "en_US" if not specified.

MaxResults sets the optional parameter "maxResults": The maximum number of rows of report data to return.

Metric sets the optional parameter "metric": Numeric columns to include in the report.

Sort sets the optional parameter "sort": The name of a dimension or metric to sort the resulting report on, optionally prefixed with "+" to sort ascending or "-" to sort descending. If no prefix is specified, the column is sorted ascending.

StartIndex sets the optional parameter "startIndex": Index of the first row of report data to return.

func (c *[ReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsGenerateCall)) UseTimezoneReporting(useTimezoneReporting [bool](https://pkg.go.dev/builtin#bool)) *[ReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsGenerateCall)

UseTimezoneReporting sets the optional parameter "useTimezoneReporting": Whether the report should be generated in the AdSense account's local timezone. If false default PST/PDT timezone will be used.

type ReportsSavedGenerateCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.reports.saved.generate" call. Exactly one of *AdsenseReportsGenerateResponse or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *AdsenseReportsGenerateResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

Locale sets the optional parameter "locale": Optional locale to use for translating report output to a local language. Defaults to "en_US" if not specified.

MaxResults sets the optional parameter "maxResults": The maximum number of rows of report data to return.

StartIndex sets the optional parameter "startIndex": Index of the first row of report data to return.

type ReportsSavedListCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.reports.saved.list" call. Exactly one of *SavedReports or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *SavedReports.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

MaxResults sets the optional parameter "maxResults": The maximum number of saved reports to include in the response, used for paging.

PageToken sets the optional parameter "pageToken": A continuation token, used to page through saved reports. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ReportsSavedService struct {
	
}

func NewReportsSavedService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Service)) *[ReportsSavedService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsSavedService)

Generate: Generate an AdSense report based on the saved report ID sent in the query parameters.

List: List all saved reports in this AdSense account.

type ReportsService struct {
 Saved *[ReportsSavedService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsSavedService)	
}

func NewReportsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Service)) *[ReportsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsService)

Generate: Generate an AdSense report based on the report request sent in the query parameters. Returns the result as JSON; to retrieve output in CSV format specify "alt=csv" as a query parameter.

type SavedAdStyle struct {
	AdStyle *[AdStyle](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdStyle) `json:"adStyle,omitempty"`

	
	
	Id [string](https://pkg.go.dev/builtin#string) `json:"id,omitempty"`

	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`

	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`

	
	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type SavedAdStyles struct {
	Etag [string](https://pkg.go.dev/builtin#string) `json:"etag,omitempty"`

	Items []*[SavedAdStyle](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#SavedAdStyle) `json:"items,omitempty"`

	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`

	
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	
	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type SavedReport struct {
	Id [string](https://pkg.go.dev/builtin#string) `json:"id,omitempty"`

	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`

	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type SavedReports struct {
	Etag [string](https://pkg.go.dev/builtin#string) `json:"etag,omitempty"`

	Items []*[SavedReport](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#SavedReport) `json:"items,omitempty"`

	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`

	
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	
	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type SavedadstylesGetCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.savedadstyles.get" call. Exactly one of *SavedAdStyle or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *SavedAdStyle.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type SavedadstylesListCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.savedadstyles.list" call. Exactly one of *SavedAdStyles or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *SavedAdStyles.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

MaxResults sets the optional parameter "maxResults": The maximum number of saved ad styles to include in the response, used for paging.

PageToken sets the optional parameter "pageToken": A continuation token, used to page through saved ad styles. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type SavedadstylesService struct {
	
}

func NewSavedadstylesService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Service)) *[SavedadstylesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#SavedadstylesService)

Get: Get a specific saved ad style from the user's account.

List: List all saved ad styles in the user's account.

type Service struct {
 BasePath [string](https://pkg.go.dev/builtin#string)  UserAgent [string](https://pkg.go.dev/builtin#string) 
 Accounts *[AccountsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AccountsService)
 Adclients *[AdclientsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdclientsService)
 Adunits *[AdunitsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AdunitsService)
 Alerts *[AlertsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#AlertsService)
 Customchannels *[CustomchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#CustomchannelsService)
 Metadata *[MetadataService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#MetadataService)
 Reports *[ReportsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#ReportsService)
 Savedadstyles *[SavedadstylesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#SavedadstylesService)
 Urlchannels *[UrlchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#UrlchannelsService)	
}

New creates a new Service. It uses the provided http.Client for requests.

Deprecated: please use NewService instead. To provide a custom HTTP client, use option.WithHTTPClient. If you are using google.golang.org/api/googleapis/transport.APIKey, use option.WithAPIKey with NewService instead.

NewService creates a new Service.

type UrlChannel struct {
	
	
	Id [string](https://pkg.go.dev/builtin#string) `json:"id,omitempty"`

	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`

	
	UrlPattern [string](https://pkg.go.dev/builtin#string) `json:"urlPattern,omitempty"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type UrlChannels struct {
	Etag [string](https://pkg.go.dev/builtin#string) `json:"etag,omitempty"`

	Items []*[UrlChannel](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#UrlChannel) `json:"items,omitempty"`

	Kind [string](https://pkg.go.dev/builtin#string) `json:"kind,omitempty"`

	
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	
	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

type UrlchannelsListCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "adsense.urlchannels.list" call. Exactly one of *UrlChannels or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *UrlChannels.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

MaxResults sets the optional parameter "maxResults": The maximum number of URL channels to include in the response, used for paging.

PageToken sets the optional parameter "pageToken": A continuation token, used to page through URL channels. To retrieve the next page, set this parameter to the value of "nextPageToken" from the previous response.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type UrlchannelsService struct {
	
}

func NewUrlchannelsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#Service)) *[UrlchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v1.3#UrlchannelsService)

List: List all URL channels in the specified ad client for this AdSense account.
