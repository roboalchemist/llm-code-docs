# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2

Title: adsense package - google.golang.org/api/adsense/v2 - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2

Markdown Content:
Package adsense provides access to the AdSense Management API.

For product documentation, see: [https://developers.google.com/adsense/management/](https://developers.google.com/adsense/management/)

#### Library status [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#hdr-Library_status "Go to Library status")

These client libraries are officially supported by Google. However, this library is considered complete and is in maintenance mode. This means that we will address critical bugs and security issues but will not add any new features.

When possible, we recommend using our newer [Cloud Client Libraries for Go]([https://pkg.go.dev/cloud.google.com/go](https://pkg.go.dev/cloud.google.com/go)) that are still actively being worked and iterated on.

#### Creating a client [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#hdr-Creating_a_client "Go to Creating a client")

Usage example:

import "google.golang.org/api/adsense/v2"
...
ctx := context.Background()
adsenseService, err := adsense.NewService(ctx)

In this example, Google Application Default Credentials are used for authentication. For information on how to create and obtain Application Default Credentials, see [https://developers.google.com/identity/protocols/application-default-credentials](https://developers.google.com/identity/protocols/application-default-credentials).

#### Other authentication options [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#hdr-Other_authentication_options "Go to Other authentication options")

By default, all available scopes (see "Constants") are used to authenticate. To restrict scopes, use [google.golang.org/api/option.WithScopes](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#WithScopes):

adsenseService, err := adsense.NewService(ctx, option.WithScopes(adsense.AdsenseReadonlyScope))

To use an API key for authentication (note: some APIs do not support API keys), use [google.golang.org/api/option.WithAPIKey](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#WithAPIKey):

adsenseService, err := adsense.NewService(ctx, option.WithAPIKey("AIza..."))

To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow, use [google.golang.org/api/option.WithTokenSource](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#WithTokenSource):

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
adsenseService, err := adsense.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))

See [google.golang.org/api/option.ClientOption](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#ClientOption) for details on options.

*   [Constants](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#pkg-constants)
*   [type Account](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Account)
*       *   [func (s Account) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Account.MarshalJSON)

*   [type AccountsAdclientsAdunitsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsCreateCall)
*       *   [func (c *AccountsAdclientsAdunitsCreateCall) Context(ctx context.Context) *AccountsAdclientsAdunitsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsCreateCall.Context)
    *   [func (c *AccountsAdclientsAdunitsCreateCall) Do(opts ...googleapi.CallOption) (*AdUnit, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsCreateCall.Do)
    *   [func (c *AccountsAdclientsAdunitsCreateCall) Fields(s ...googleapi.Field) *AccountsAdclientsAdunitsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsCreateCall.Fields)
    *   [func (c *AccountsAdclientsAdunitsCreateCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsCreateCall.Header)

*   [type AccountsAdclientsAdunitsGetAdcodeCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsGetAdcodeCall)
*       *   [func (c *AccountsAdclientsAdunitsGetAdcodeCall) Context(ctx context.Context) *AccountsAdclientsAdunitsGetAdcodeCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsGetAdcodeCall.Context)
    *   [func (c *AccountsAdclientsAdunitsGetAdcodeCall) Do(opts ...googleapi.CallOption) (*AdUnitAdCode, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsGetAdcodeCall.Do)
    *   [func (c *AccountsAdclientsAdunitsGetAdcodeCall) Fields(s ...googleapi.Field) *AccountsAdclientsAdunitsGetAdcodeCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsGetAdcodeCall.Fields)
    *   [func (c *AccountsAdclientsAdunitsGetAdcodeCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsGetAdcodeCall.Header)
    *   [func (c *AccountsAdclientsAdunitsGetAdcodeCall) IfNoneMatch(entityTag string) *AccountsAdclientsAdunitsGetAdcodeCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsGetAdcodeCall.IfNoneMatch)

*   [type AccountsAdclientsAdunitsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsGetCall)
*       *   [func (c *AccountsAdclientsAdunitsGetCall) Context(ctx context.Context) *AccountsAdclientsAdunitsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsGetCall.Context)
    *   [func (c *AccountsAdclientsAdunitsGetCall) Do(opts ...googleapi.CallOption) (*AdUnit, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsGetCall.Do)
    *   [func (c *AccountsAdclientsAdunitsGetCall) Fields(s ...googleapi.Field) *AccountsAdclientsAdunitsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsGetCall.Fields)
    *   [func (c *AccountsAdclientsAdunitsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsGetCall.Header)
    *   [func (c *AccountsAdclientsAdunitsGetCall) IfNoneMatch(entityTag string) *AccountsAdclientsAdunitsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsGetCall.IfNoneMatch)

*   [type AccountsAdclientsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsListCall)
*       *   [func (c *AccountsAdclientsAdunitsListCall) Context(ctx context.Context) *AccountsAdclientsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsListCall.Context)
    *   [func (c *AccountsAdclientsAdunitsListCall) Do(opts ...googleapi.CallOption) (*ListAdUnitsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsListCall.Do)
    *   [func (c *AccountsAdclientsAdunitsListCall) Fields(s ...googleapi.Field) *AccountsAdclientsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsListCall.Fields)
    *   [func (c *AccountsAdclientsAdunitsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsListCall.Header)
    *   [func (c *AccountsAdclientsAdunitsListCall) IfNoneMatch(entityTag string) *AccountsAdclientsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsListCall.IfNoneMatch)
    *   [func (c *AccountsAdclientsAdunitsListCall) PageSize(pageSize int64) *AccountsAdclientsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsListCall.PageSize)
    *   [func (c *AccountsAdclientsAdunitsListCall) PageToken(pageToken string) *AccountsAdclientsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsListCall.PageToken)
    *   [func (c *AccountsAdclientsAdunitsListCall) Pages(ctx context.Context, f func(*ListAdUnitsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsListCall.Pages)

*   [type AccountsAdclientsAdunitsListLinkedCustomChannelsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsListLinkedCustomChannelsCall)
*       *   [func (c *AccountsAdclientsAdunitsListLinkedCustomChannelsCall) Context(ctx context.Context) *AccountsAdclientsAdunitsListLinkedCustomChannelsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsListLinkedCustomChannelsCall.Context)
    *   [func (c *AccountsAdclientsAdunitsListLinkedCustomChannelsCall) Do(opts ...googleapi.CallOption) (*ListLinkedCustomChannelsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsListLinkedCustomChannelsCall.Do)
    *   [func (c *AccountsAdclientsAdunitsListLinkedCustomChannelsCall) Fields(s ...googleapi.Field) *AccountsAdclientsAdunitsListLinkedCustomChannelsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsListLinkedCustomChannelsCall.Fields)
    *   [func (c *AccountsAdclientsAdunitsListLinkedCustomChannelsCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsListLinkedCustomChannelsCall.Header)
    *   [func (c *AccountsAdclientsAdunitsListLinkedCustomChannelsCall) IfNoneMatch(entityTag string) *AccountsAdclientsAdunitsListLinkedCustomChannelsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsListLinkedCustomChannelsCall.IfNoneMatch)
    *   [func (c *AccountsAdclientsAdunitsListLinkedCustomChannelsCall) PageSize(pageSize int64) *AccountsAdclientsAdunitsListLinkedCustomChannelsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsListLinkedCustomChannelsCall.PageSize)
    *   [func (c *AccountsAdclientsAdunitsListLinkedCustomChannelsCall) PageToken(pageToken string) *AccountsAdclientsAdunitsListLinkedCustomChannelsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsListLinkedCustomChannelsCall.PageToken)
    *   [func (c *AccountsAdclientsAdunitsListLinkedCustomChannelsCall) Pages(ctx context.Context, f func(*ListLinkedCustomChannelsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsListLinkedCustomChannelsCall.Pages)

*   [type AccountsAdclientsAdunitsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsPatchCall)
*       *   [func (c *AccountsAdclientsAdunitsPatchCall) Context(ctx context.Context) *AccountsAdclientsAdunitsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsPatchCall.Context)
    *   [func (c *AccountsAdclientsAdunitsPatchCall) Do(opts ...googleapi.CallOption) (*AdUnit, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsPatchCall.Do)
    *   [func (c *AccountsAdclientsAdunitsPatchCall) Fields(s ...googleapi.Field) *AccountsAdclientsAdunitsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsPatchCall.Fields)
    *   [func (c *AccountsAdclientsAdunitsPatchCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsPatchCall.Header)
    *   [func (c *AccountsAdclientsAdunitsPatchCall) UpdateMask(updateMask string) *AccountsAdclientsAdunitsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsPatchCall.UpdateMask)

*   [type AccountsAdclientsAdunitsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsService)
*       *   [func NewAccountsAdclientsAdunitsService(s *Service) *AccountsAdclientsAdunitsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#NewAccountsAdclientsAdunitsService)

*       *   [func (r *AccountsAdclientsAdunitsService) Create(parent string, adunit *AdUnit) *AccountsAdclientsAdunitsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsService.Create)
    *   [func (r *AccountsAdclientsAdunitsService) Get(name string) *AccountsAdclientsAdunitsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsService.Get)
    *   [func (r *AccountsAdclientsAdunitsService) GetAdcode(name string) *AccountsAdclientsAdunitsGetAdcodeCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsService.GetAdcode)
    *   [func (r *AccountsAdclientsAdunitsService) List(parent string) *AccountsAdclientsAdunitsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsService.List)
    *   [func (r *AccountsAdclientsAdunitsService) ListLinkedCustomChannels(parent string) *AccountsAdclientsAdunitsListLinkedCustomChannelsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsService.ListLinkedCustomChannels)
    *   [func (r *AccountsAdclientsAdunitsService) Patch(name string, adunit *AdUnit) *AccountsAdclientsAdunitsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsService.Patch)

*   [type AccountsAdclientsCustomchannelsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsCreateCall)
*       *   [func (c *AccountsAdclientsCustomchannelsCreateCall) Context(ctx context.Context) *AccountsAdclientsCustomchannelsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsCreateCall.Context)
    *   [func (c *AccountsAdclientsCustomchannelsCreateCall) Do(opts ...googleapi.CallOption) (*CustomChannel, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsCreateCall.Do)
    *   [func (c *AccountsAdclientsCustomchannelsCreateCall) Fields(s ...googleapi.Field) *AccountsAdclientsCustomchannelsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsCreateCall.Fields)
    *   [func (c *AccountsAdclientsCustomchannelsCreateCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsCreateCall.Header)

*   [type AccountsAdclientsCustomchannelsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsDeleteCall)
*       *   [func (c *AccountsAdclientsCustomchannelsDeleteCall) Context(ctx context.Context) *AccountsAdclientsCustomchannelsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsDeleteCall.Context)
    *   [func (c *AccountsAdclientsCustomchannelsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsDeleteCall.Do)
    *   [func (c *AccountsAdclientsCustomchannelsDeleteCall) Fields(s ...googleapi.Field) *AccountsAdclientsCustomchannelsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsDeleteCall.Fields)
    *   [func (c *AccountsAdclientsCustomchannelsDeleteCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsDeleteCall.Header)

*   [type AccountsAdclientsCustomchannelsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsGetCall)
*       *   [func (c *AccountsAdclientsCustomchannelsGetCall) Context(ctx context.Context) *AccountsAdclientsCustomchannelsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsGetCall.Context)
    *   [func (c *AccountsAdclientsCustomchannelsGetCall) Do(opts ...googleapi.CallOption) (*CustomChannel, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsGetCall.Do)
    *   [func (c *AccountsAdclientsCustomchannelsGetCall) Fields(s ...googleapi.Field) *AccountsAdclientsCustomchannelsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsGetCall.Fields)
    *   [func (c *AccountsAdclientsCustomchannelsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsGetCall.Header)
    *   [func (c *AccountsAdclientsCustomchannelsGetCall) IfNoneMatch(entityTag string) *AccountsAdclientsCustomchannelsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsGetCall.IfNoneMatch)

*   [type AccountsAdclientsCustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsListCall)
*       *   [func (c *AccountsAdclientsCustomchannelsListCall) Context(ctx context.Context) *AccountsAdclientsCustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsListCall.Context)
    *   [func (c *AccountsAdclientsCustomchannelsListCall) Do(opts ...googleapi.CallOption) (*ListCustomChannelsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsListCall.Do)
    *   [func (c *AccountsAdclientsCustomchannelsListCall) Fields(s ...googleapi.Field) *AccountsAdclientsCustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsListCall.Fields)
    *   [func (c *AccountsAdclientsCustomchannelsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsListCall.Header)
    *   [func (c *AccountsAdclientsCustomchannelsListCall) IfNoneMatch(entityTag string) *AccountsAdclientsCustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsListCall.IfNoneMatch)
    *   [func (c *AccountsAdclientsCustomchannelsListCall) PageSize(pageSize int64) *AccountsAdclientsCustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsListCall.PageSize)
    *   [func (c *AccountsAdclientsCustomchannelsListCall) PageToken(pageToken string) *AccountsAdclientsCustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsListCall.PageToken)
    *   [func (c *AccountsAdclientsCustomchannelsListCall) Pages(ctx context.Context, f func(*ListCustomChannelsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsListCall.Pages)

*   [type AccountsAdclientsCustomchannelsListLinkedAdUnitsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsListLinkedAdUnitsCall)
*       *   [func (c *AccountsAdclientsCustomchannelsListLinkedAdUnitsCall) Context(ctx context.Context) *AccountsAdclientsCustomchannelsListLinkedAdUnitsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsListLinkedAdUnitsCall.Context)
    *   [func (c *AccountsAdclientsCustomchannelsListLinkedAdUnitsCall) Do(opts ...googleapi.CallOption) (*ListLinkedAdUnitsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsListLinkedAdUnitsCall.Do)
    *   [func (c *AccountsAdclientsCustomchannelsListLinkedAdUnitsCall) Fields(s ...googleapi.Field) *AccountsAdclientsCustomchannelsListLinkedAdUnitsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsListLinkedAdUnitsCall.Fields)
    *   [func (c *AccountsAdclientsCustomchannelsListLinkedAdUnitsCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsListLinkedAdUnitsCall.Header)
    *   [func (c *AccountsAdclientsCustomchannelsListLinkedAdUnitsCall) IfNoneMatch(entityTag string) *AccountsAdclientsCustomchannelsListLinkedAdUnitsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsListLinkedAdUnitsCall.IfNoneMatch)
    *   [func (c *AccountsAdclientsCustomchannelsListLinkedAdUnitsCall) PageSize(pageSize int64) *AccountsAdclientsCustomchannelsListLinkedAdUnitsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsListLinkedAdUnitsCall.PageSize)
    *   [func (c *AccountsAdclientsCustomchannelsListLinkedAdUnitsCall) PageToken(pageToken string) *AccountsAdclientsCustomchannelsListLinkedAdUnitsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsListLinkedAdUnitsCall.PageToken)
    *   [func (c *AccountsAdclientsCustomchannelsListLinkedAdUnitsCall) Pages(ctx context.Context, f func(*ListLinkedAdUnitsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsListLinkedAdUnitsCall.Pages)

*   [type AccountsAdclientsCustomchannelsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsPatchCall)
*       *   [func (c *AccountsAdclientsCustomchannelsPatchCall) Context(ctx context.Context) *AccountsAdclientsCustomchannelsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsPatchCall.Context)
    *   [func (c *AccountsAdclientsCustomchannelsPatchCall) Do(opts ...googleapi.CallOption) (*CustomChannel, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsPatchCall.Do)
    *   [func (c *AccountsAdclientsCustomchannelsPatchCall) Fields(s ...googleapi.Field) *AccountsAdclientsCustomchannelsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsPatchCall.Fields)
    *   [func (c *AccountsAdclientsCustomchannelsPatchCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsPatchCall.Header)
    *   [func (c *AccountsAdclientsCustomchannelsPatchCall) UpdateMask(updateMask string) *AccountsAdclientsCustomchannelsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsPatchCall.UpdateMask)

*   [type AccountsAdclientsCustomchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsService)
*       *   [func NewAccountsAdclientsCustomchannelsService(s *Service) *AccountsAdclientsCustomchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#NewAccountsAdclientsCustomchannelsService)

*       *   [func (r *AccountsAdclientsCustomchannelsService) Create(parent string, customchannel *CustomChannel) *AccountsAdclientsCustomchannelsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsService.Create)
    *   [func (r *AccountsAdclientsCustomchannelsService) Delete(name string) *AccountsAdclientsCustomchannelsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsService.Delete)
    *   [func (r *AccountsAdclientsCustomchannelsService) Get(name string) *AccountsAdclientsCustomchannelsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsService.Get)
    *   [func (r *AccountsAdclientsCustomchannelsService) List(parent string) *AccountsAdclientsCustomchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsService.List)
    *   [func (r *AccountsAdclientsCustomchannelsService) ListLinkedAdUnits(parent string) *AccountsAdclientsCustomchannelsListLinkedAdUnitsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsService.ListLinkedAdUnits)
    *   [func (r *AccountsAdclientsCustomchannelsService) Patch(name string, customchannel *CustomChannel) *AccountsAdclientsCustomchannelsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsService.Patch)

*   [type AccountsAdclientsGetAdcodeCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsGetAdcodeCall)
*       *   [func (c *AccountsAdclientsGetAdcodeCall) Context(ctx context.Context) *AccountsAdclientsGetAdcodeCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsGetAdcodeCall.Context)
    *   [func (c *AccountsAdclientsGetAdcodeCall) Do(opts ...googleapi.CallOption) (*AdClientAdCode, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsGetAdcodeCall.Do)
    *   [func (c *AccountsAdclientsGetAdcodeCall) Fields(s ...googleapi.Field) *AccountsAdclientsGetAdcodeCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsGetAdcodeCall.Fields)
    *   [func (c *AccountsAdclientsGetAdcodeCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsGetAdcodeCall.Header)
    *   [func (c *AccountsAdclientsGetAdcodeCall) IfNoneMatch(entityTag string) *AccountsAdclientsGetAdcodeCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsGetAdcodeCall.IfNoneMatch)

*   [type AccountsAdclientsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsGetCall)
*       *   [func (c *AccountsAdclientsGetCall) Context(ctx context.Context) *AccountsAdclientsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsGetCall.Context)
    *   [func (c *AccountsAdclientsGetCall) Do(opts ...googleapi.CallOption) (*AdClient, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsGetCall.Do)
    *   [func (c *AccountsAdclientsGetCall) Fields(s ...googleapi.Field) *AccountsAdclientsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsGetCall.Fields)
    *   [func (c *AccountsAdclientsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsGetCall.Header)
    *   [func (c *AccountsAdclientsGetCall) IfNoneMatch(entityTag string) *AccountsAdclientsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsGetCall.IfNoneMatch)

*   [type AccountsAdclientsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsListCall)
*       *   [func (c *AccountsAdclientsListCall) Context(ctx context.Context) *AccountsAdclientsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsListCall.Context)
    *   [func (c *AccountsAdclientsListCall) Do(opts ...googleapi.CallOption) (*ListAdClientsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsListCall.Do)
    *   [func (c *AccountsAdclientsListCall) Fields(s ...googleapi.Field) *AccountsAdclientsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsListCall.Fields)
    *   [func (c *AccountsAdclientsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsListCall.Header)
    *   [func (c *AccountsAdclientsListCall) IfNoneMatch(entityTag string) *AccountsAdclientsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsListCall.IfNoneMatch)
    *   [func (c *AccountsAdclientsListCall) PageSize(pageSize int64) *AccountsAdclientsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsListCall.PageSize)
    *   [func (c *AccountsAdclientsListCall) PageToken(pageToken string) *AccountsAdclientsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsListCall.PageToken)
    *   [func (c *AccountsAdclientsListCall) Pages(ctx context.Context, f func(*ListAdClientsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsListCall.Pages)

*   [type AccountsAdclientsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsService)
*       *   [func NewAccountsAdclientsService(s *Service) *AccountsAdclientsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#NewAccountsAdclientsService)

*       *   [func (r *AccountsAdclientsService) Get(name string) *AccountsAdclientsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsService.Get)
    *   [func (r *AccountsAdclientsService) GetAdcode(name string) *AccountsAdclientsGetAdcodeCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsService.GetAdcode)
    *   [func (r *AccountsAdclientsService) List(parent string) *AccountsAdclientsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsService.List)

*   [type AccountsAdclientsUrlchannelsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsUrlchannelsGetCall)
*       *   [func (c *AccountsAdclientsUrlchannelsGetCall) Context(ctx context.Context) *AccountsAdclientsUrlchannelsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsUrlchannelsGetCall.Context)
    *   [func (c *AccountsAdclientsUrlchannelsGetCall) Do(opts ...googleapi.CallOption) (*UrlChannel, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsUrlchannelsGetCall.Do)
    *   [func (c *AccountsAdclientsUrlchannelsGetCall) Fields(s ...googleapi.Field) *AccountsAdclientsUrlchannelsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsUrlchannelsGetCall.Fields)
    *   [func (c *AccountsAdclientsUrlchannelsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsUrlchannelsGetCall.Header)
    *   [func (c *AccountsAdclientsUrlchannelsGetCall) IfNoneMatch(entityTag string) *AccountsAdclientsUrlchannelsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsUrlchannelsGetCall.IfNoneMatch)

*   [type AccountsAdclientsUrlchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsUrlchannelsListCall)
*       *   [func (c *AccountsAdclientsUrlchannelsListCall) Context(ctx context.Context) *AccountsAdclientsUrlchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsUrlchannelsListCall.Context)
    *   [func (c *AccountsAdclientsUrlchannelsListCall) Do(opts ...googleapi.CallOption) (*ListUrlChannelsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsUrlchannelsListCall.Do)
    *   [func (c *AccountsAdclientsUrlchannelsListCall) Fields(s ...googleapi.Field) *AccountsAdclientsUrlchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsUrlchannelsListCall.Fields)
    *   [func (c *AccountsAdclientsUrlchannelsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsUrlchannelsListCall.Header)
    *   [func (c *AccountsAdclientsUrlchannelsListCall) IfNoneMatch(entityTag string) *AccountsAdclientsUrlchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsUrlchannelsListCall.IfNoneMatch)
    *   [func (c *AccountsAdclientsUrlchannelsListCall) PageSize(pageSize int64) *AccountsAdclientsUrlchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsUrlchannelsListCall.PageSize)
    *   [func (c *AccountsAdclientsUrlchannelsListCall) PageToken(pageToken string) *AccountsAdclientsUrlchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsUrlchannelsListCall.PageToken)
    *   [func (c *AccountsAdclientsUrlchannelsListCall) Pages(ctx context.Context, f func(*ListUrlChannelsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsUrlchannelsListCall.Pages)

*   [type AccountsAdclientsUrlchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsUrlchannelsService)
*       *   [func NewAccountsAdclientsUrlchannelsService(s *Service) *AccountsAdclientsUrlchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#NewAccountsAdclientsUrlchannelsService)

*       *   [func (r *AccountsAdclientsUrlchannelsService) Get(name string) *AccountsAdclientsUrlchannelsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsUrlchannelsService.Get)
    *   [func (r *AccountsAdclientsUrlchannelsService) List(parent string) *AccountsAdclientsUrlchannelsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsUrlchannelsService.List)

*   [type AccountsAlertsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAlertsListCall)
*       *   [func (c *AccountsAlertsListCall) Context(ctx context.Context) *AccountsAlertsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAlertsListCall.Context)
    *   [func (c *AccountsAlertsListCall) Do(opts ...googleapi.CallOption) (*ListAlertsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAlertsListCall.Do)
    *   [func (c *AccountsAlertsListCall) Fields(s ...googleapi.Field) *AccountsAlertsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAlertsListCall.Fields)
    *   [func (c *AccountsAlertsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAlertsListCall.Header)
    *   [func (c *AccountsAlertsListCall) IfNoneMatch(entityTag string) *AccountsAlertsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAlertsListCall.IfNoneMatch)
    *   [func (c *AccountsAlertsListCall) LanguageCode(languageCode string) *AccountsAlertsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAlertsListCall.LanguageCode)

*   [type AccountsAlertsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAlertsService)
*       *   [func NewAccountsAlertsService(s *Service) *AccountsAlertsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#NewAccountsAlertsService)

*       *   [func (r *AccountsAlertsService) List(parent string) *AccountsAlertsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAlertsService.List)

*   [type AccountsGetAdBlockingRecoveryTagCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsGetAdBlockingRecoveryTagCall)
*       *   [func (c *AccountsGetAdBlockingRecoveryTagCall) Context(ctx context.Context) *AccountsGetAdBlockingRecoveryTagCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsGetAdBlockingRecoveryTagCall.Context)
    *   [func (c *AccountsGetAdBlockingRecoveryTagCall) Do(opts ...googleapi.CallOption) (*AdBlockingRecoveryTag, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsGetAdBlockingRecoveryTagCall.Do)
    *   [func (c *AccountsGetAdBlockingRecoveryTagCall) Fields(s ...googleapi.Field) *AccountsGetAdBlockingRecoveryTagCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsGetAdBlockingRecoveryTagCall.Fields)
    *   [func (c *AccountsGetAdBlockingRecoveryTagCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsGetAdBlockingRecoveryTagCall.Header)
    *   [func (c *AccountsGetAdBlockingRecoveryTagCall) IfNoneMatch(entityTag string) *AccountsGetAdBlockingRecoveryTagCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsGetAdBlockingRecoveryTagCall.IfNoneMatch)

*   [type AccountsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsGetCall)
*       *   [func (c *AccountsGetCall) Context(ctx context.Context) *AccountsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsGetCall.Context)
    *   [func (c *AccountsGetCall) Do(opts ...googleapi.CallOption) (*Account, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsGetCall.Do)
    *   [func (c *AccountsGetCall) Fields(s ...googleapi.Field) *AccountsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsGetCall.Fields)
    *   [func (c *AccountsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsGetCall.Header)
    *   [func (c *AccountsGetCall) IfNoneMatch(entityTag string) *AccountsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsGetCall.IfNoneMatch)

*   [type AccountsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsListCall)
*       *   [func (c *AccountsListCall) Context(ctx context.Context) *AccountsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsListCall.Context)
    *   [func (c *AccountsListCall) Do(opts ...googleapi.CallOption) (*ListAccountsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsListCall.Do)
    *   [func (c *AccountsListCall) Fields(s ...googleapi.Field) *AccountsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsListCall.Fields)
    *   [func (c *AccountsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsListCall.Header)
    *   [func (c *AccountsListCall) IfNoneMatch(entityTag string) *AccountsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsListCall.IfNoneMatch)
    *   [func (c *AccountsListCall) PageSize(pageSize int64) *AccountsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsListCall.PageSize)
    *   [func (c *AccountsListCall) PageToken(pageToken string) *AccountsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsListCall.PageToken)
    *   [func (c *AccountsListCall) Pages(ctx context.Context, f func(*ListAccountsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsListCall.Pages)

*   [type AccountsListChildAccountsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsListChildAccountsCall)
*       *   [func (c *AccountsListChildAccountsCall) Context(ctx context.Context) *AccountsListChildAccountsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsListChildAccountsCall.Context)
    *   [func (c *AccountsListChildAccountsCall) Do(opts ...googleapi.CallOption) (*ListChildAccountsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsListChildAccountsCall.Do)
    *   [func (c *AccountsListChildAccountsCall) Fields(s ...googleapi.Field) *AccountsListChildAccountsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsListChildAccountsCall.Fields)
    *   [func (c *AccountsListChildAccountsCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsListChildAccountsCall.Header)
    *   [func (c *AccountsListChildAccountsCall) IfNoneMatch(entityTag string) *AccountsListChildAccountsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsListChildAccountsCall.IfNoneMatch)
    *   [func (c *AccountsListChildAccountsCall) PageSize(pageSize int64) *AccountsListChildAccountsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsListChildAccountsCall.PageSize)
    *   [func (c *AccountsListChildAccountsCall) PageToken(pageToken string) *AccountsListChildAccountsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsListChildAccountsCall.PageToken)
    *   [func (c *AccountsListChildAccountsCall) Pages(ctx context.Context, f func(*ListChildAccountsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsListChildAccountsCall.Pages)

*   [type AccountsPaymentsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsPaymentsListCall)
*       *   [func (c *AccountsPaymentsListCall) Context(ctx context.Context) *AccountsPaymentsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsPaymentsListCall.Context)
    *   [func (c *AccountsPaymentsListCall) Do(opts ...googleapi.CallOption) (*ListPaymentsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsPaymentsListCall.Do)
    *   [func (c *AccountsPaymentsListCall) Fields(s ...googleapi.Field) *AccountsPaymentsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsPaymentsListCall.Fields)
    *   [func (c *AccountsPaymentsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsPaymentsListCall.Header)
    *   [func (c *AccountsPaymentsListCall) IfNoneMatch(entityTag string) *AccountsPaymentsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsPaymentsListCall.IfNoneMatch)

*   [type AccountsPaymentsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsPaymentsService)
*       *   [func NewAccountsPaymentsService(s *Service) *AccountsPaymentsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#NewAccountsPaymentsService)

*       *   [func (r *AccountsPaymentsService) List(parent string) *AccountsPaymentsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsPaymentsService.List)

*   [type AccountsPolicyIssuesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsPolicyIssuesGetCall)
*       *   [func (c *AccountsPolicyIssuesGetCall) Context(ctx context.Context) *AccountsPolicyIssuesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsPolicyIssuesGetCall.Context)
    *   [func (c *AccountsPolicyIssuesGetCall) Do(opts ...googleapi.CallOption) (*PolicyIssue, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsPolicyIssuesGetCall.Do)
    *   [func (c *AccountsPolicyIssuesGetCall) Fields(s ...googleapi.Field) *AccountsPolicyIssuesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsPolicyIssuesGetCall.Fields)
    *   [func (c *AccountsPolicyIssuesGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsPolicyIssuesGetCall.Header)
    *   [func (c *AccountsPolicyIssuesGetCall) IfNoneMatch(entityTag string) *AccountsPolicyIssuesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsPolicyIssuesGetCall.IfNoneMatch)

*   [type AccountsPolicyIssuesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsPolicyIssuesListCall)
*       *   [func (c *AccountsPolicyIssuesListCall) Context(ctx context.Context) *AccountsPolicyIssuesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsPolicyIssuesListCall.Context)
    *   [func (c *AccountsPolicyIssuesListCall) Do(opts ...googleapi.CallOption) (*ListPolicyIssuesResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsPolicyIssuesListCall.Do)
    *   [func (c *AccountsPolicyIssuesListCall) Fields(s ...googleapi.Field) *AccountsPolicyIssuesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsPolicyIssuesListCall.Fields)
    *   [func (c *AccountsPolicyIssuesListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsPolicyIssuesListCall.Header)
    *   [func (c *AccountsPolicyIssuesListCall) IfNoneMatch(entityTag string) *AccountsPolicyIssuesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsPolicyIssuesListCall.IfNoneMatch)
    *   [func (c *AccountsPolicyIssuesListCall) PageSize(pageSize int64) *AccountsPolicyIssuesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsPolicyIssuesListCall.PageSize)
    *   [func (c *AccountsPolicyIssuesListCall) PageToken(pageToken string) *AccountsPolicyIssuesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsPolicyIssuesListCall.PageToken)
    *   [func (c *AccountsPolicyIssuesListCall) Pages(ctx context.Context, f func(*ListPolicyIssuesResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsPolicyIssuesListCall.Pages)

*   [type AccountsPolicyIssuesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsPolicyIssuesService)
*       *   [func NewAccountsPolicyIssuesService(s *Service) *AccountsPolicyIssuesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#NewAccountsPolicyIssuesService)

*       *   [func (r *AccountsPolicyIssuesService) Get(name string) *AccountsPolicyIssuesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsPolicyIssuesService.Get)
    *   [func (r *AccountsPolicyIssuesService) List(parent string) *AccountsPolicyIssuesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsPolicyIssuesService.List)

*   [type AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCall)
*       *   [func (c *AccountsReportsGenerateCall) Context(ctx context.Context) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCall.Context)
    *   [func (c *AccountsReportsGenerateCall) CurrencyCode(currencyCode string) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCall.CurrencyCode)
    *   [func (c *AccountsReportsGenerateCall) DateRange(dateRange string) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCall.DateRange)
    *   [func (c *AccountsReportsGenerateCall) Dimensions(dimensions ...string) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCall.Dimensions)
    *   [func (c *AccountsReportsGenerateCall) Do(opts ...googleapi.CallOption) (*ReportResult, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCall.Do)
    *   [func (c *AccountsReportsGenerateCall) EndDateDay(endDateDay int64) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCall.EndDateDay)
    *   [func (c *AccountsReportsGenerateCall) EndDateMonth(endDateMonth int64) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCall.EndDateMonth)
    *   [func (c *AccountsReportsGenerateCall) EndDateYear(endDateYear int64) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCall.EndDateYear)
    *   [func (c *AccountsReportsGenerateCall) Fields(s ...googleapi.Field) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCall.Fields)
    *   [func (c *AccountsReportsGenerateCall) Filters(filters ...string) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCall.Filters)
    *   [func (c *AccountsReportsGenerateCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCall.Header)
    *   [func (c *AccountsReportsGenerateCall) IfNoneMatch(entityTag string) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCall.IfNoneMatch)
    *   [func (c *AccountsReportsGenerateCall) LanguageCode(languageCode string) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCall.LanguageCode)
    *   [func (c *AccountsReportsGenerateCall) Limit(limit int64) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCall.Limit)
    *   [func (c *AccountsReportsGenerateCall) Metrics(metrics ...string) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCall.Metrics)
    *   [func (c *AccountsReportsGenerateCall) OrderBy(orderBy ...string) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCall.OrderBy)
    *   [func (c *AccountsReportsGenerateCall) ReportingTimeZone(reportingTimeZone string) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCall.ReportingTimeZone)
    *   [func (c *AccountsReportsGenerateCall) StartDateDay(startDateDay int64) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCall.StartDateDay)
    *   [func (c *AccountsReportsGenerateCall) StartDateMonth(startDateMonth int64) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCall.StartDateMonth)
    *   [func (c *AccountsReportsGenerateCall) StartDateYear(startDateYear int64) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCall.StartDateYear)

*   [type AccountsReportsGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCsvCall)
*       *   [func (c *AccountsReportsGenerateCsvCall) Context(ctx context.Context) *AccountsReportsGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCsvCall.Context)
    *   [func (c *AccountsReportsGenerateCsvCall) CurrencyCode(currencyCode string) *AccountsReportsGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCsvCall.CurrencyCode)
    *   [func (c *AccountsReportsGenerateCsvCall) DateRange(dateRange string) *AccountsReportsGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCsvCall.DateRange)
    *   [func (c *AccountsReportsGenerateCsvCall) Dimensions(dimensions ...string) *AccountsReportsGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCsvCall.Dimensions)
    *   [func (c *AccountsReportsGenerateCsvCall) Do(opts ...googleapi.CallOption) (*HttpBody, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCsvCall.Do)
    *   [func (c *AccountsReportsGenerateCsvCall) EndDateDay(endDateDay int64) *AccountsReportsGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCsvCall.EndDateDay)
    *   [func (c *AccountsReportsGenerateCsvCall) EndDateMonth(endDateMonth int64) *AccountsReportsGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCsvCall.EndDateMonth)
    *   [func (c *AccountsReportsGenerateCsvCall) EndDateYear(endDateYear int64) *AccountsReportsGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCsvCall.EndDateYear)
    *   [func (c *AccountsReportsGenerateCsvCall) Fields(s ...googleapi.Field) *AccountsReportsGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCsvCall.Fields)
    *   [func (c *AccountsReportsGenerateCsvCall) Filters(filters ...string) *AccountsReportsGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCsvCall.Filters)
    *   [func (c *AccountsReportsGenerateCsvCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCsvCall.Header)
    *   [func (c *AccountsReportsGenerateCsvCall) IfNoneMatch(entityTag string) *AccountsReportsGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCsvCall.IfNoneMatch)
    *   [func (c *AccountsReportsGenerateCsvCall) LanguageCode(languageCode string) *AccountsReportsGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCsvCall.LanguageCode)
    *   [func (c *AccountsReportsGenerateCsvCall) Limit(limit int64) *AccountsReportsGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCsvCall.Limit)
    *   [func (c *AccountsReportsGenerateCsvCall) Metrics(metrics ...string) *AccountsReportsGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCsvCall.Metrics)
    *   [func (c *AccountsReportsGenerateCsvCall) OrderBy(orderBy ...string) *AccountsReportsGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCsvCall.OrderBy)
    *   [func (c *AccountsReportsGenerateCsvCall) ReportingTimeZone(reportingTimeZone string) *AccountsReportsGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCsvCall.ReportingTimeZone)
    *   [func (c *AccountsReportsGenerateCsvCall) StartDateDay(startDateDay int64) *AccountsReportsGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCsvCall.StartDateDay)
    *   [func (c *AccountsReportsGenerateCsvCall) StartDateMonth(startDateMonth int64) *AccountsReportsGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCsvCall.StartDateMonth)
    *   [func (c *AccountsReportsGenerateCsvCall) StartDateYear(startDateYear int64) *AccountsReportsGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGenerateCsvCall.StartDateYear)

*   [type AccountsReportsGetSavedCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGetSavedCall)
*       *   [func (c *AccountsReportsGetSavedCall) Context(ctx context.Context) *AccountsReportsGetSavedCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGetSavedCall.Context)
    *   [func (c *AccountsReportsGetSavedCall) Do(opts ...googleapi.CallOption) (*SavedReport, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGetSavedCall.Do)
    *   [func (c *AccountsReportsGetSavedCall) Fields(s ...googleapi.Field) *AccountsReportsGetSavedCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGetSavedCall.Fields)
    *   [func (c *AccountsReportsGetSavedCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGetSavedCall.Header)
    *   [func (c *AccountsReportsGetSavedCall) IfNoneMatch(entityTag string) *AccountsReportsGetSavedCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsGetSavedCall.IfNoneMatch)

*   [type AccountsReportsSavedGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCall)
*       *   [func (c *AccountsReportsSavedGenerateCall) Context(ctx context.Context) *AccountsReportsSavedGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCall.Context)
    *   [func (c *AccountsReportsSavedGenerateCall) CurrencyCode(currencyCode string) *AccountsReportsSavedGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCall.CurrencyCode)
    *   [func (c *AccountsReportsSavedGenerateCall) DateRange(dateRange string) *AccountsReportsSavedGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCall.DateRange)
    *   [func (c *AccountsReportsSavedGenerateCall) Do(opts ...googleapi.CallOption) (*ReportResult, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCall.Do)
    *   [func (c *AccountsReportsSavedGenerateCall) EndDateDay(endDateDay int64) *AccountsReportsSavedGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCall.EndDateDay)
    *   [func (c *AccountsReportsSavedGenerateCall) EndDateMonth(endDateMonth int64) *AccountsReportsSavedGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCall.EndDateMonth)
    *   [func (c *AccountsReportsSavedGenerateCall) EndDateYear(endDateYear int64) *AccountsReportsSavedGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCall.EndDateYear)
    *   [func (c *AccountsReportsSavedGenerateCall) Fields(s ...googleapi.Field) *AccountsReportsSavedGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCall.Fields)
    *   [func (c *AccountsReportsSavedGenerateCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCall.Header)
    *   [func (c *AccountsReportsSavedGenerateCall) IfNoneMatch(entityTag string) *AccountsReportsSavedGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCall.IfNoneMatch)
    *   [func (c *AccountsReportsSavedGenerateCall) LanguageCode(languageCode string) *AccountsReportsSavedGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCall.LanguageCode)
    *   [func (c *AccountsReportsSavedGenerateCall) ReportingTimeZone(reportingTimeZone string) *AccountsReportsSavedGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCall.ReportingTimeZone)
    *   [func (c *AccountsReportsSavedGenerateCall) StartDateDay(startDateDay int64) *AccountsReportsSavedGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCall.StartDateDay)
    *   [func (c *AccountsReportsSavedGenerateCall) StartDateMonth(startDateMonth int64) *AccountsReportsSavedGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCall.StartDateMonth)
    *   [func (c *AccountsReportsSavedGenerateCall) StartDateYear(startDateYear int64) *AccountsReportsSavedGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCall.StartDateYear)

*   [type AccountsReportsSavedGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCsvCall)
*       *   [func (c *AccountsReportsSavedGenerateCsvCall) Context(ctx context.Context) *AccountsReportsSavedGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCsvCall.Context)
    *   [func (c *AccountsReportsSavedGenerateCsvCall) CurrencyCode(currencyCode string) *AccountsReportsSavedGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCsvCall.CurrencyCode)
    *   [func (c *AccountsReportsSavedGenerateCsvCall) DateRange(dateRange string) *AccountsReportsSavedGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCsvCall.DateRange)
    *   [func (c *AccountsReportsSavedGenerateCsvCall) Do(opts ...googleapi.CallOption) (*HttpBody, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCsvCall.Do)
    *   [func (c *AccountsReportsSavedGenerateCsvCall) EndDateDay(endDateDay int64) *AccountsReportsSavedGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCsvCall.EndDateDay)
    *   [func (c *AccountsReportsSavedGenerateCsvCall) EndDateMonth(endDateMonth int64) *AccountsReportsSavedGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCsvCall.EndDateMonth)
    *   [func (c *AccountsReportsSavedGenerateCsvCall) EndDateYear(endDateYear int64) *AccountsReportsSavedGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCsvCall.EndDateYear)
    *   [func (c *AccountsReportsSavedGenerateCsvCall) Fields(s ...googleapi.Field) *AccountsReportsSavedGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCsvCall.Fields)
    *   [func (c *AccountsReportsSavedGenerateCsvCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCsvCall.Header)
    *   [func (c *AccountsReportsSavedGenerateCsvCall) IfNoneMatch(entityTag string) *AccountsReportsSavedGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCsvCall.IfNoneMatch)
    *   [func (c *AccountsReportsSavedGenerateCsvCall) LanguageCode(languageCode string) *AccountsReportsSavedGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCsvCall.LanguageCode)
    *   [func (c *AccountsReportsSavedGenerateCsvCall) ReportingTimeZone(reportingTimeZone string) *AccountsReportsSavedGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCsvCall.ReportingTimeZone)
    *   [func (c *AccountsReportsSavedGenerateCsvCall) StartDateDay(startDateDay int64) *AccountsReportsSavedGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCsvCall.StartDateDay)
    *   [func (c *AccountsReportsSavedGenerateCsvCall) StartDateMonth(startDateMonth int64) *AccountsReportsSavedGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCsvCall.StartDateMonth)
    *   [func (c *AccountsReportsSavedGenerateCsvCall) StartDateYear(startDateYear int64) *AccountsReportsSavedGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedGenerateCsvCall.StartDateYear)

*   [type AccountsReportsSavedListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedListCall)
*       *   [func (c *AccountsReportsSavedListCall) Context(ctx context.Context) *AccountsReportsSavedListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedListCall.Context)
    *   [func (c *AccountsReportsSavedListCall) Do(opts ...googleapi.CallOption) (*ListSavedReportsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedListCall.Do)
    *   [func (c *AccountsReportsSavedListCall) Fields(s ...googleapi.Field) *AccountsReportsSavedListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedListCall.Fields)
    *   [func (c *AccountsReportsSavedListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedListCall.Header)
    *   [func (c *AccountsReportsSavedListCall) IfNoneMatch(entityTag string) *AccountsReportsSavedListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedListCall.IfNoneMatch)
    *   [func (c *AccountsReportsSavedListCall) PageSize(pageSize int64) *AccountsReportsSavedListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedListCall.PageSize)
    *   [func (c *AccountsReportsSavedListCall) PageToken(pageToken string) *AccountsReportsSavedListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedListCall.PageToken)
    *   [func (c *AccountsReportsSavedListCall) Pages(ctx context.Context, f func(*ListSavedReportsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedListCall.Pages)

*   [type AccountsReportsSavedService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedService)
*       *   [func NewAccountsReportsSavedService(s *Service) *AccountsReportsSavedService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#NewAccountsReportsSavedService)

*       *   [func (r *AccountsReportsSavedService) Generate(name string) *AccountsReportsSavedGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedService.Generate)
    *   [func (r *AccountsReportsSavedService) GenerateCsv(name string) *AccountsReportsSavedGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedService.GenerateCsv)
    *   [func (r *AccountsReportsSavedService) List(parent string) *AccountsReportsSavedListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedService.List)

*   [type AccountsReportsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsService)
*       *   [func NewAccountsReportsService(s *Service) *AccountsReportsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#NewAccountsReportsService)

*       *   [func (r *AccountsReportsService) Generate(account string) *AccountsReportsGenerateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsService.Generate)
    *   [func (r *AccountsReportsService) GenerateCsv(account string) *AccountsReportsGenerateCsvCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsService.GenerateCsv)
    *   [func (r *AccountsReportsService) GetSaved(name string) *AccountsReportsGetSavedCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsService.GetSaved)

*   [type AccountsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsService)
*       *   [func NewAccountsService(s *Service) *AccountsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#NewAccountsService)

*       *   [func (r *AccountsService) Get(name string) *AccountsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsService.Get)
    *   [func (r *AccountsService) GetAdBlockingRecoveryTag(name string) *AccountsGetAdBlockingRecoveryTagCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsService.GetAdBlockingRecoveryTag)
    *   [func (r *AccountsService) List() *AccountsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsService.List)
    *   [func (r *AccountsService) ListChildAccounts(parent string) *AccountsListChildAccountsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsService.ListChildAccounts)

*   [type AccountsSitesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsSitesGetCall)
*       *   [func (c *AccountsSitesGetCall) Context(ctx context.Context) *AccountsSitesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsSitesGetCall.Context)
    *   [func (c *AccountsSitesGetCall) Do(opts ...googleapi.CallOption) (*Site, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsSitesGetCall.Do)
    *   [func (c *AccountsSitesGetCall) Fields(s ...googleapi.Field) *AccountsSitesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsSitesGetCall.Fields)
    *   [func (c *AccountsSitesGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsSitesGetCall.Header)
    *   [func (c *AccountsSitesGetCall) IfNoneMatch(entityTag string) *AccountsSitesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsSitesGetCall.IfNoneMatch)

*   [type AccountsSitesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsSitesListCall)
*       *   [func (c *AccountsSitesListCall) Context(ctx context.Context) *AccountsSitesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsSitesListCall.Context)
    *   [func (c *AccountsSitesListCall) Do(opts ...googleapi.CallOption) (*ListSitesResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsSitesListCall.Do)
    *   [func (c *AccountsSitesListCall) Fields(s ...googleapi.Field) *AccountsSitesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsSitesListCall.Fields)
    *   [func (c *AccountsSitesListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsSitesListCall.Header)
    *   [func (c *AccountsSitesListCall) IfNoneMatch(entityTag string) *AccountsSitesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsSitesListCall.IfNoneMatch)
    *   [func (c *AccountsSitesListCall) PageSize(pageSize int64) *AccountsSitesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsSitesListCall.PageSize)
    *   [func (c *AccountsSitesListCall) PageToken(pageToken string) *AccountsSitesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsSitesListCall.PageToken)
    *   [func (c *AccountsSitesListCall) Pages(ctx context.Context, f func(*ListSitesResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsSitesListCall.Pages)

*   [type AccountsSitesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsSitesService)
*       *   [func NewAccountsSitesService(s *Service) *AccountsSitesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#NewAccountsSitesService)

*       *   [func (r *AccountsSitesService) Get(name string) *AccountsSitesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsSitesService.Get)
    *   [func (r *AccountsSitesService) List(parent string) *AccountsSitesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsSitesService.List)

*   [type AdBlockingRecoveryTag](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AdBlockingRecoveryTag)
*       *   [func (s AdBlockingRecoveryTag) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AdBlockingRecoveryTag.MarshalJSON)

*   [type AdClient](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AdClient)
*       *   [func (s AdClient) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AdClient.MarshalJSON)

*   [type AdClientAdCode](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AdClientAdCode)
*       *   [func (s AdClientAdCode) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AdClientAdCode.MarshalJSON)

*   [type AdUnit](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AdUnit)
*       *   [func (s AdUnit) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AdUnit.MarshalJSON)

*   [type AdUnitAdCode](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AdUnitAdCode)
*       *   [func (s AdUnitAdCode) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AdUnitAdCode.MarshalJSON)

*   [type Alert](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Alert)
*       *   [func (s Alert) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Alert.MarshalJSON)

*   [type Cell](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Cell)
*       *   [func (s Cell) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Cell.MarshalJSON)

*   [type ContentAdsSettings](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ContentAdsSettings)
*       *   [func (s ContentAdsSettings) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ContentAdsSettings.MarshalJSON)

*   [type CustomChannel](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#CustomChannel)
*       *   [func (s CustomChannel) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#CustomChannel.MarshalJSON)

*   [type Date](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Date)
*       *   [func (s Date) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Date.MarshalJSON)

*   [type Empty](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Empty)
*   [type Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Header)
*       *   [func (s Header) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Header.MarshalJSON)

*   [type HttpBody](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#HttpBody)
*       *   [func (s HttpBody) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#HttpBody.MarshalJSON)

*   [type ListAccountsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ListAccountsResponse)
*       *   [func (s ListAccountsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ListAccountsResponse.MarshalJSON)

*   [type ListAdClientsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ListAdClientsResponse)
*       *   [func (s ListAdClientsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ListAdClientsResponse.MarshalJSON)

*   [type ListAdUnitsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ListAdUnitsResponse)
*       *   [func (s ListAdUnitsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ListAdUnitsResponse.MarshalJSON)

*   [type ListAlertsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ListAlertsResponse)
*       *   [func (s ListAlertsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ListAlertsResponse.MarshalJSON)

*   [type ListChildAccountsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ListChildAccountsResponse)
*       *   [func (s ListChildAccountsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ListChildAccountsResponse.MarshalJSON)

*   [type ListCustomChannelsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ListCustomChannelsResponse)
*       *   [func (s ListCustomChannelsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ListCustomChannelsResponse.MarshalJSON)

*   [type ListLinkedAdUnitsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ListLinkedAdUnitsResponse)
*       *   [func (s ListLinkedAdUnitsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ListLinkedAdUnitsResponse.MarshalJSON)

*   [type ListLinkedCustomChannelsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ListLinkedCustomChannelsResponse)
*       *   [func (s ListLinkedCustomChannelsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ListLinkedCustomChannelsResponse.MarshalJSON)

*   [type ListPaymentsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ListPaymentsResponse)
*       *   [func (s ListPaymentsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ListPaymentsResponse.MarshalJSON)

*   [type ListPolicyIssuesResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ListPolicyIssuesResponse)
*       *   [func (s ListPolicyIssuesResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ListPolicyIssuesResponse.MarshalJSON)

*   [type ListSavedReportsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ListSavedReportsResponse)
*       *   [func (s ListSavedReportsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ListSavedReportsResponse.MarshalJSON)

*   [type ListSitesResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ListSitesResponse)
*       *   [func (s ListSitesResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ListSitesResponse.MarshalJSON)

*   [type ListUrlChannelsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ListUrlChannelsResponse)
*       *   [func (s ListUrlChannelsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ListUrlChannelsResponse.MarshalJSON)

*   [type Payment](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Payment)
*       *   [func (s Payment) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Payment.MarshalJSON)

*   [type PolicyIssue](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#PolicyIssue)
*       *   [func (s PolicyIssue) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#PolicyIssue.MarshalJSON)

*   [type PolicyTopic](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#PolicyTopic)
*       *   [func (s PolicyTopic) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#PolicyTopic.MarshalJSON)

*   [type ReportResult](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ReportResult)
*       *   [func (s ReportResult) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ReportResult.MarshalJSON)

*   [type Row](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Row)
*       *   [func (s Row) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Row.MarshalJSON)

*   [type SavedReport](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#SavedReport)
*       *   [func (s SavedReport) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#SavedReport.MarshalJSON)

*   [type Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Service)
*       *   [func New(client *http.Client) (*Service, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#New)deprecated
    *   [func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#NewService)

*   [type Site](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Site)
*       *   [func (s Site) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Site.MarshalJSON)

*   [type TimeZone](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#TimeZone)
*       *   [func (s TimeZone) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#TimeZone.MarshalJSON)

*   [type UrlChannel](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#UrlChannel)
*       *   [func (s UrlChannel) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#UrlChannel.MarshalJSON)

[View Source](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/adsense/v2/adsense-gen.go#L105)

const (
	AdsenseScope = "https://www.googleapis.com/auth/adsense"

	AdsenseReadonlyScope = "https://www.googleapis.com/auth/adsense.readonly"
)

OAuth2 scopes used by this API.

This section is empty.

This section is empty.

type Account struct {
	CreateTime [string](https://pkg.go.dev/builtin#string) `json:"createTime,omitempty"`
	DisplayName [string](https://pkg.go.dev/builtin#string) `json:"displayName,omitempty"`
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	
	PendingTasks [][string](https://pkg.go.dev/builtin#string) `json:"pendingTasks,omitempty"`
	
	Premium [bool](https://pkg.go.dev/builtin#bool) `json:"premium,omitempty"`
	
	
	
	
	
	
	
	State [string](https://pkg.go.dev/builtin#string) `json:"state,omitempty"`
	
	
	TimeZone *[TimeZone](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#TimeZone) `json:"timeZone,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Account: Representation of an account.

type AccountsAdclientsAdunitsCreateCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "adsense.accounts.adclients.adunits.create" call. Any non-2xx status code is an error. Response headers are in either *AdUnit.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsAdclientsAdunitsGetAdcodeCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "adsense.accounts.adclients.adunits.getAdcode" call. Any non-2xx status code is an error. Response headers are in either *AdUnitAdCode.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AccountsAdclientsAdunitsGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "adsense.accounts.adclients.adunits.get" call. Any non-2xx status code is an error. Response headers are in either *AdUnit.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AccountsAdclientsAdunitsListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "adsense.accounts.adclients.adunits.list" call. Any non-2xx status code is an error. Response headers are in either *ListAdUnitsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": The maximum number of ad units to include in the response, used for paging. If unspecified, at most 10000 ad units will be returned. The maximum value is 10000; values above 10000 will be coerced to 10000.

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListAdUnits` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListAdUnits` must match the call that provided the page token.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsAdclientsAdunitsListLinkedCustomChannelsCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "adsense.accounts.adclients.adunits.listLinkedCustomChannels" call. Any non-2xx status code is an error. Response headers are in either *ListLinkedCustomChannelsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": The maximum number of custom channels to include in the response, used for paging. If unspecified, at most 10000 custom channels will be returned. The maximum value is 10000; values above 10000 will be coerced to 10000.

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListLinkedCustomChannels` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListLinkedCustomChannels` must match the call that provided the page token.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsAdclientsAdunitsPatchCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "adsense.accounts.adclients.adunits.patch" call. Any non-2xx status code is an error. Response headers are in either *AdUnit.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

UpdateMask sets the optional parameter "updateMask": The list of fields to update. If empty, a full update is performed.

type AccountsAdclientsAdunitsService struct {
	
}

func NewAccountsAdclientsAdunitsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Service)) *[AccountsAdclientsAdunitsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsService)

Create: Creates an ad unit. This method can be called only by a restricted set of projects, which are usually owned by AdSense for Platforms ([https://developers.google.com/adsense/platforms/](https://developers.google.com/adsense/platforms/)) publishers. Contact your account manager if you need to use this method. Note that ad units can only be created for ad clients with an "AFC" product code. For more info see the AdClient resource (/adsense/management/reference/rest/v2/accounts.adclients). For now, this method can only be used to create `DISPLAY` ad units. See: [https://support.google.com/adsense/answer/9183566](https://support.google.com/adsense/answer/9183566)

*   parent: Ad client to create an ad unit under. Format: accounts/{account}/adclients/{adclient}.

Get: Gets an ad unit from a specified account and ad client.

*   name: AdUnit to get information about. Format: accounts/{account}/adclients/{adclient}/adunits/{adunit}.

List: Lists all ad units under a specified account and ad client.

*   parent: The ad client which owns the collection of ad units. Format: accounts/{account}/adclients/{adclient}.

ListLinkedCustomChannels: Lists all the custom channels available for an ad unit.

*   parent: The ad unit which owns the collection of custom channels. Format: accounts/{account}/adclients/{adclient}/adunits/{adunit}.

Patch: Updates an ad unit. This method can be called only by a restricted set of projects, which are usually owned by AdSense for Platforms ([https://developers.google.com/adsense/platforms/](https://developers.google.com/adsense/platforms/)) publishers. Contact your account manager if you need to use this method. For now, this method can only be used to update `DISPLAY` ad units. See: [https://support.google.com/adsense/answer/9183566](https://support.google.com/adsense/answer/9183566)

*   name: Output only. Resource name of the ad unit. Format: accounts/{account}/adclients/{adclient}/adunits/{adunit}.

type AccountsAdclientsCustomchannelsCreateCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "adsense.accounts.adclients.customchannels.create" call. Any non-2xx status code is an error. Response headers are in either *CustomChannel.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsAdclientsCustomchannelsDeleteCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "adsense.accounts.adclients.customchannels.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccountsAdclientsCustomchannelsGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "adsense.accounts.adclients.customchannels.get" call. Any non-2xx status code is an error. Response headers are in either *CustomChannel.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AccountsAdclientsCustomchannelsListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "adsense.accounts.adclients.customchannels.list" call. Any non-2xx status code is an error. Response headers are in either *ListCustomChannelsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": The maximum number of custom channels to include in the response, used for paging. If unspecified, at most 10000 custom channels will be returned. The maximum value is 10000; values above 10000 will be coerced to 10000.

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListCustomChannels` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListCustomChannels` must match the call that provided the page token.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsAdclientsCustomchannelsListLinkedAdUnitsCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "adsense.accounts.adclients.customchannels.listLinkedAdUnits" call. Any non-2xx status code is an error. Response headers are in either *ListLinkedAdUnitsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": The maximum number of ad units to include in the response, used for paging. If unspecified, at most 10000 ad units will be returned. The maximum value is 10000; values above 10000 will be coerced to 10000.

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListLinkedAdUnits` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListLinkedAdUnits` must match the call that provided the page token.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsAdclientsCustomchannelsPatchCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "adsense.accounts.adclients.customchannels.patch" call. Any non-2xx status code is an error. Response headers are in either *CustomChannel.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

UpdateMask sets the optional parameter "updateMask": The list of fields to update. If empty, a full update is performed.

type AccountsAdclientsCustomchannelsService struct {
	
}

func NewAccountsAdclientsCustomchannelsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Service)) *[AccountsAdclientsCustomchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsService)

Create: Creates a custom channel. This method can be called only by a restricted set of projects, which are usually owned by AdSense for Platforms ([https://developers.google.com/adsense/platforms/](https://developers.google.com/adsense/platforms/)) publishers. Contact your account manager if you need to use this method.

*   parent: The ad client to create a custom channel under. Format: accounts/{account}/adclients/{adclient}.

Delete: Deletes a custom channel. This method can be called only by a restricted set of projects, which are usually owned by AdSense for Platforms ([https://developers.google.com/adsense/platforms/](https://developers.google.com/adsense/platforms/)) publishers. Contact your account manager if you need to use this method.

*   name: Name of the custom channel to delete. Format: accounts/{account}/adclients/{adclient}/customchannels/{customchannel}.

Get: Gets information about the selected custom channel.

*   name: Name of the custom channel. Format: accounts/{account}/adclients/{adclient}/customchannels/{customchannel}.

List: Lists all the custom channels available in an ad client.

*   parent: The ad client which owns the collection of custom channels. Format: accounts/{account}/adclients/{adclient}.

ListLinkedAdUnits: Lists all the ad units available for a custom channel.

*   parent: The custom channel which owns the collection of ad units. Format: accounts/{account}/adclients/{adclient}/customchannels/{customchannel}.

Patch: Updates a custom channel. This method can be called only by a restricted set of projects, which are usually owned by AdSense for Platforms ([https://developers.google.com/adsense/platforms/](https://developers.google.com/adsense/platforms/)) publishers. Contact your account manager if you need to use this method.

*   name: Output only. Resource name of the custom channel. Format: accounts/{account}/adclients/{adclient}/customchannels/{customchannel}.

type AccountsAdclientsGetAdcodeCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "adsense.accounts.adclients.getAdcode" call. Any non-2xx status code is an error. Response headers are in either *AdClientAdCode.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AccountsAdclientsGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "adsense.accounts.adclients.get" call. Any non-2xx status code is an error. Response headers are in either *AdClient.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AccountsAdclientsListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "adsense.accounts.adclients.list" call. Any non-2xx status code is an error. Response headers are in either *ListAdClientsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": The maximum number of ad clients to include in the response, used for paging. If unspecified, at most 10000 ad clients will be returned. The maximum value is 10000; values above 10000 will be coerced to 10000.

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListAdClients` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListAdClients` must match the call that provided the page token.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsAdclientsService struct {
 Adunits *[AccountsAdclientsAdunitsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsAdunitsService)
 Customchannels *[AccountsAdclientsCustomchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsCustomchannelsService)
 Urlchannels *[AccountsAdclientsUrlchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsUrlchannelsService)	
}

func NewAccountsAdclientsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Service)) *[AccountsAdclientsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsService)

Get: Gets the ad client from the given resource name.

*   name: The name of the ad client to retrieve. Format: accounts/{account}/adclients/{adclient}.

GetAdcode: Gets the AdSense code for a given ad client. This returns what was previously known as the 'auto ad code'. This is only supported for ad clients with a product_code of AFC. For more information, see About the AdSense code ([https://support.google.com/adsense/answer/9274634](https://support.google.com/adsense/answer/9274634)).

*   name: Name of the ad client for which to get the adcode. Format: accounts/{account}/adclients/{adclient}.

List: Lists all the ad clients available in an account.

*   parent: The account which owns the collection of ad clients. Format: accounts/{account}.

type AccountsAdclientsUrlchannelsGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "adsense.accounts.adclients.urlchannels.get" call. Any non-2xx status code is an error. Response headers are in either *UrlChannel.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AccountsAdclientsUrlchannelsListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "adsense.accounts.adclients.urlchannels.list" call. Any non-2xx status code is an error. Response headers are in either *ListUrlChannelsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": The maximum number of url channels to include in the response, used for paging. If unspecified, at most 10000 url channels will be returned. The maximum value is 10000; values above 10000 will be coerced to 10000.

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListUrlChannels` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListUrlChannels` must match the call that provided the page token.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsAdclientsUrlchannelsService struct {
	
}

func NewAccountsAdclientsUrlchannelsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Service)) *[AccountsAdclientsUrlchannelsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsUrlchannelsService)

Get: Gets information about the selected url channel.

*   name: The name of the url channel to retrieve. Format: accounts/{account}/adclients/{adclient}/urlchannels/{urlchannel}.

List: Lists active url channels.

*   parent: The ad client which owns the collection of url channels. Format: accounts/{account}/adclients/{adclient}.

type AccountsAlertsListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "adsense.accounts.alerts.list" call. Any non-2xx status code is an error. Response headers are in either *ListAlertsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

LanguageCode sets the optional parameter "languageCode": The language to use for translating alert messages. If unspecified, this defaults to the user's display language. If the given language is not supported, alerts will be returned in English. The language is specified as an IETF BCP-47 language code ([https://en.wikipedia.org/wiki/IETF_language_tag](https://en.wikipedia.org/wiki/IETF_language_tag)).

type AccountsAlertsService struct {
	
}

func NewAccountsAlertsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Service)) *[AccountsAlertsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAlertsService)

List: Lists all the alerts available in an account.

*   parent: The account which owns the collection of alerts. Format: accounts/{account}.

type AccountsGetAdBlockingRecoveryTagCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "adsense.accounts.getAdBlockingRecoveryTag" call. Any non-2xx status code is an error. Response headers are in either *AdBlockingRecoveryTag.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AccountsGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "adsense.accounts.get" call. Any non-2xx status code is an error. Response headers are in either *Account.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AccountsListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "adsense.accounts.list" call. Any non-2xx status code is an error. Response headers are in either *ListAccountsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": The maximum number of accounts to include in the response, used for paging. If unspecified, at most 10000 accounts will be returned. The maximum value is 10000; values above 10000 will be coerced to 10000.

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListAccounts` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListAccounts` must match the call that provided the page token.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsListChildAccountsCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "adsense.accounts.listChildAccounts" call. Any non-2xx status code is an error. Response headers are in either *ListChildAccountsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": The maximum number of accounts to include in the response, used for paging. If unspecified, at most 10000 accounts will be returned. The maximum value is 10000; values above 10000 will be coerced to 10000.

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListChildAccounts` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListChildAccounts` must match the call that provided the page token.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsPaymentsListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "adsense.accounts.payments.list" call. Any non-2xx status code is an error. Response headers are in either *ListPaymentsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AccountsPaymentsService struct {
	
}

func NewAccountsPaymentsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Service)) *[AccountsPaymentsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsPaymentsService)

List: Lists all the payments available for an account.

*   parent: The account which owns the collection of payments. Format: accounts/{account}.

type AccountsPolicyIssuesGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "adsense.accounts.policyIssues.get" call. Any non-2xx status code is an error. Response headers are in either *PolicyIssue.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AccountsPolicyIssuesListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "adsense.accounts.policyIssues.list" call. Any non-2xx status code is an error. Response headers are in either *ListPolicyIssuesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": The maximum number of policy issues to include in the response, used for paging. If unspecified, at most 10000 policy issues will be returned. The maximum value is 10000; values above 10000 will be coerced to 10000.

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListPolicyIssues` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListPolicyIssues` must match the call that provided the page token.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsPolicyIssuesService struct {
	
}

func NewAccountsPolicyIssuesService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Service)) *[AccountsPolicyIssuesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsPolicyIssuesService)

Get: Gets information about the selected policy issue.

*   name: Name of the policy issue. Format: accounts/{account}/policyIssues/{policy_issue}.

List: Lists all the policy issues where the specified account is involved, both directly and through any AFP child accounts.

*   parent: The account for which policy issues are being retrieved. Format: accounts/{account}.

type AccountsReportsGenerateCall struct {
	
}

Context sets the context to be used in this call's Do method.

CurrencyCode sets the optional parameter "currencyCode": The ISO-4217 currency code ([https://en.wikipedia.org/wiki/ISO_4217](https://en.wikipedia.org/wiki/ISO_4217)) to use when reporting on monetary metrics. Defaults to the account's currency if not set.

DateRange sets the optional parameter "dateRange": Date range of the report, if unset the range will be considered CUSTOM.

Possible values:

"REPORTING_DATE_RANGE_UNSPECIFIED" - Unspecified date range.
"CUSTOM" - A custom date range specified using the `start_date` and

`end_date` fields. This is the default if no ReportingDateRange is provided.

"TODAY" - Current day.
"YESTERDAY" - Yesterday.
"MONTH_TO_DATE" - From the start of the current month to the current day.

e.g. if the current date is 2020-03-12 then the range will be [2020-03-01, 2020-03-12].

"YEAR_TO_DATE" - From the start of the current year to the current day.

e.g. if the current date is 2020-03-12 then the range will be [2020-01-01, 2020-03-12].

"LAST_7_DAYS" - Last 7 days, excluding current day.
"LAST_30_DAYS" - Last 30 days, excluding current day.

Dimensions sets the optional parameter "dimensions": Dimensions to base the report on.

Possible values:

"DIMENSION_UNSPECIFIED" - Unspecified dimension.
"DATE" - Date dimension in YYYY-MM-DD format (e.g. "2010-02-10").
"WEEK" - Week dimension in YYYY-MM-DD format, representing the first day

of each week (e.g. "2010-02-08"). The first day of the week is determined by the language_code specified in a report generation request (so e.g. this would be a Monday for "en-GB" or "es", but a Sunday for "en" or "fr-CA").

"MONTH" - Month dimension in YYYY-MM format (e.g. "2010-02").
"ACCOUNT_NAME" - Account name. The members of this dimension match the

values from Account.display_name.

"AD_CLIENT_ID" - Unique ID of an ad client. The members of this dimension

match the values from AdClient.reporting_dimension_id.

"HOSTED_AD_CLIENT_ID" - Unique ID of a sub-account's ad client. The

members of this dimension match the values from AdClient.reporting_dimension_id (for the sub-account).

"PRODUCT_NAME" - Localized product name (e.g. "AdSense for Content",

"AdSense for Search").

"PRODUCT_CODE" - Product code (e.g. "AFC", "AFS"). The members of this

dimension match the values from AdClient.product_code.

"AD_UNIT_NAME" - Ad unit name (within which an ad was served). The members

of this dimension match the values from AdUnit.display_name.

"AD_UNIT_ID" - Unique ID of an ad unit (within which an ad was served).

The members of this dimension match the values from AdUnit.reporting_dimension_id.

"AD_UNIT_SIZE_NAME" - Localized size of an ad unit (e.g. "728x90",

"Responsive").

"AD_UNIT_SIZE_CODE" - The size code of an ad unit (e.g. "728x90",

"responsive").

"CUSTOM_CHANNEL_NAME" - Custom channel name. The members of this dimension

match the values from CustomChannel.display_name.

"CUSTOM_CHANNEL_ID" - Unique ID of a custom channel. The members of this

dimension match the values from CustomChannel.reporting_dimension_id.

"HOSTED_CUSTOM_CHANNEL_ID" - Not supported.
"OWNED_SITE_DOMAIN_NAME" - Domain name of a verified site (e.g.

"example.com"). The members of this dimension match the values from Site.domain.

"OWNED_SITE_ID" - Unique ID of a verified site. The members of this

dimension match the values from Site.reporting_dimension_id.

"PAGE_URL" - URL of the page upon which the ad was served. This is a

complete URL including scheme and query parameters. Note that the URL that appears in this dimension may be a canonicalized version of the one that was used in the original request, and so may not exactly match the URL that a user might have seen. Note that there are also some caveats to be aware of when using this dimension. For more information, see [Page URL breakdown]([https://support.google.com/adsense/answer/11988478](https://support.google.com/adsense/answer/11988478)).

"URL_CHANNEL_NAME" - Name of a URL channel. The members of this dimension

match the values from UrlChannel.uri_pattern.

"URL_CHANNEL_ID" - Unique ID of a URL channel. The members of this

dimension match the values from UrlChannel.reporting_dimension_id.

"BUYER_NETWORK_NAME" - Name of an ad network that returned the winning ads

for an ad request (e.g. "Google AdWords"). Note that unlike other "NAME" dimensions, the members of this dimensions are not localized.

"BUYER_NETWORK_ID" - Unique (opaque) ID of an ad network that returned the

winning ads for an ad request.

"BID_TYPE_NAME" - Localized bid type name (e.g. "CPC bids", "CPM bids")

for a served ad.

"BID_TYPE_CODE" - Type of a bid (e.g. "cpc", "cpm") for a served ad.
"CREATIVE_SIZE_NAME" - Localized creative size name (e.g. "728x90",

"Dynamic") of a served ad.

"CREATIVE_SIZE_CODE" - Creative size code (e.g. "728x90", "dynamic") of a

served ad.

"DOMAIN_NAME" - Localized name of a host on which an ad was served, after

IDNA decoding (e.g. "www.google.com", "Web caches and other", "bücher.example").

"DOMAIN_CODE" - Name of a host on which an ad was served (e.g.

"www.google.com", "webcaches", "xn--bcher-kva.example").

"COUNTRY_NAME" - Localized region name of a user viewing an ad (e.g.

"United States", "France").

"COUNTRY_CODE" - CLDR region code of a user viewing an ad (e.g. "US",

"FR").

"PLATFORM_TYPE_NAME" - Localized platform type name (e.g. "High-end mobile

devices", "Desktop").

"PLATFORM_TYPE_CODE" - Platform type code (e.g. "HighEndMobile",

"Desktop").

"TARGETING_TYPE_NAME" - Localized targeting type name (e.g. "Contextual",

"Personalized", "Run of Network").

"TARGETING_TYPE_CODE" - Targeting type code (e.g. "Keyword",

"UserInterest", "RunOfNetwork").

"TRAFFIC_SOURCE_NAME" - Localized traffic source name (e.g. "Google",

"Bing", "Facebook", "Other"). For more information, see [Traffic source breakdown]([https://support.google.com/adsense/answer/16474600](https://support.google.com/adsense/answer/16474600)).

"TRAFFIC_SOURCE_CODE" - Traffic source code (e.g. "GOOGLE", "BING",

"FACEBOOK", "OTHER"). For more information, see [Traffic source breakdown]([https://support.google.com/adsense/answer/16474600](https://support.google.com/adsense/answer/16474600)).

"CONTENT_PLATFORM_NAME" - Localized content platform name an ad request

was made from (e.g. "AMP", "Web").

"CONTENT_PLATFORM_CODE" - Content platform code an ad request was made

from (e.g. "AMP", "HTML").

"AD_PLACEMENT_NAME" - Localized ad placement name (e.g. "Ad unit", "Global

settings", "Manual").

"AD_PLACEMENT_CODE" - Ad placement code (e.g. "AD_UNIT",

"ca-pub-123456:78910", "OTHER").

"REQUESTED_AD_TYPE_NAME" - Localized requested ad type name (e.g.

"Display", "Link unit", "Other").

"REQUESTED_AD_TYPE_CODE" - Requested ad type code (e.g. "IMAGE",

"RADLINK", "OTHER").

"SERVED_AD_TYPE_NAME" - Localized served ad type name (e.g. "Display",

"Link unit", "Other").

"SERVED_AD_TYPE_CODE" - Served ad type code (e.g. "IMAGE", "RADLINK",

"OTHER").

"AD_FORMAT_NAME" - Localized ad format name indicating the way an ad is

shown to the users on your site (e.g. "In-page", "Anchor", "Vignette").

"AD_FORMAT_CODE" - Ad format code indicating the way an ad is shown to the

users on your site (e.g. "ON_PAGE", "ANCHOR", "INTERSTITIAL").

"CUSTOM_SEARCH_STYLE_NAME" - Custom search style name.
"CUSTOM_SEARCH_STYLE_ID" - Custom search style id.
"DOMAIN_REGISTRANT" - Domain registrants.
"WEBSEARCH_QUERY_STRING" - Query strings for web searches.
"OS_TYPE_NAME" - Localized operating system type name (e.g. "Windows",

"MacOS", "Android"). For more information, see [Operating system breakdown]([https://support.google.com/adsense/answer/16853822](https://support.google.com/adsense/answer/16853822)).

"OS_TYPE_CODE" - Operating system type code (e.g. "WINDOWS", "MAC",

"ANDROID"). For more information, see [Operating system breakdown]([https://support.google.com/adsense/answer/16853822](https://support.google.com/adsense/answer/16853822)).

"BROWSER_TYPE_NAME" - Localized browser type name (e.g. "Google Chrome",

"Firefox", "Safari"). For more information, see [Browser breakdown]([https://support.google.com/adsense/answer/16851903](https://support.google.com/adsense/answer/16851903)).

"BROWSER_TYPE_CODE" - Browser type code (e.g. "CHROME", "FIREFOX",

"SAFARI"). For more information, see [Browser breakdown]([https://support.google.com/adsense/answer/16851903](https://support.google.com/adsense/answer/16851903)).

"WEBVIEW_TYPE_NAME" - Localized webview type name (e.g. "Webview

(Uncategorized)", "Non-webview"). For more information, see [Hosting App breakdown]([https://support.google.com/adsense/answer/16853515](https://support.google.com/adsense/answer/16853515)).

"WEBVIEW_TYPE_CODE" - Webview type code (e.g. "UNCATEGORIZED", "NONE").

For more information, see [Hosting App breakdown]([https://support.google.com/adsense/answer/16853515](https://support.google.com/adsense/answer/16853515)).

Do executes the "adsense.accounts.reports.generate" call. Any non-2xx status code is an error. Response headers are in either *ReportResult.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

EndDateDay sets the optional parameter "endDate.day": Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.

EndDateMonth sets the optional parameter "endDate.month": Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.

EndDateYear sets the optional parameter "endDate.year": Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.

Filters sets the optional parameter "filters": A list of filters (/adsense/management/reporting/filtering) to apply to the report. All provided filters must match in order for the data to be included in the report.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

LanguageCode sets the optional parameter "languageCode": The language to use for translating report output. If unspecified, this defaults to English ("en"). If the given language is not supported, report output will be returned in English. The language is specified as an IETF BCP-47 language code ([https://en.wikipedia.org/wiki/IETF_language_tag](https://en.wikipedia.org/wiki/IETF_language_tag)).

Limit sets the optional parameter "limit": The maximum number of rows of report data to return. Reports producing more rows than the requested limit will be truncated. If unset, this defaults to 100,000 rows for `Reports.GenerateReport` and 1,000,000 rows for `Reports.GenerateCsvReport`, which are also the maximum values permitted here. Report truncation can be identified (for `Reports.GenerateReport` only) by comparing the number of rows returned to the value returned in `total_matched_rows`.

Metrics sets the optional parameter "metrics": Required. Reporting metrics.

Possible values:

"METRIC_UNSPECIFIED" - Unspecified metric.
"PAGE_VIEWS" - Number of page views.
"AD_REQUESTS" - Number of ad units that requested ads (for content ads) or

search queries (for search ads). An ad request may result in zero, one, or multiple individual ad impressions depending on the size of the ad unit and whether any ads were available.

"MATCHED_AD_REQUESTS" - Requests that returned at least one ad.
"TOTAL_IMPRESSIONS" - Impressions. An impression is counted for each ad

request where at least one ad has been downloaded to the user's device and has begun to load. It is the number of ad units (for content ads) or search queries (for search ads) that showed ads.

"IMPRESSIONS" - Impressions. An impression is counted for each ad request

where at least one ad has been downloaded to the user's device and has begun to load. It is the number of ad units (for content ads) or search queries (for search ads) that showed ads.

"INDIVIDUAL_AD_IMPRESSIONS" - Ads shown. Different ad formats will display

varying numbers of ads. For example, a vertical banner may consist of 2 or more ads. Also, the number of ads in an ad unit may vary depending on whether the ad unit is displaying standard text ads, expanded text ads or image ads.

"CLICKS" - Number of times a user clicked on a standard content ad.
"PAGE_VIEWS_SPAM_RATIO" - Fraction of page views considered to be spam.

Only available to [premium accounts]([https://developers.google.com/adsense/management/reference/rest/v2/](https://developers.google.com/adsense/management/reference/rest/v2/) accounts#Account.FIELDS.premium).

"AD_REQUESTS_SPAM_RATIO" - Fraction of ad requests considered to be spam.

Only available to [premium accounts]([https://developers.google.com/adsense/management/reference/rest/v2/](https://developers.google.com/adsense/management/reference/rest/v2/) accounts#Account.FIELDS.premium).

"MATCHED_AD_REQUESTS_SPAM_RATIO" - Fraction of ad requests that returned

ads considered to be spam. Only available to [premium accounts]([https://developers.google.com/adsense/management/reference/rest/v2/](https://developers.google.com/adsense/management/reference/rest/v2/) accounts#Account.FIELDS.premium).

"IMPRESSIONS_SPAM_RATIO" - Fraction of impressions considered to be spam.

Only available to [premium accounts]([https://developers.google.com/adsense/management/reference/rest/v2/](https://developers.google.com/adsense/management/reference/rest/v2/) accounts#Account.FIELDS.premium).

"INDIVIDUAL_AD_IMPRESSIONS_SPAM_RATIO" - Fraction of ad impressions

considered to be spam. Only available to [premium accounts]([https://developers.google.com/adsense/management/reference/rest/v2/](https://developers.google.com/adsense/management/reference/rest/v2/) accounts#Account.FIELDS.premium).

"CLICKS_SPAM_RATIO" - Fraction of clicks considered to be spam. Only

available to [premium accounts]([https://developers.google.com/adsense/management/reference/rest/v2/](https://developers.google.com/adsense/management/reference/rest/v2/) accounts#Account.FIELDS.premium).

"AD_REQUESTS_COVERAGE" - Ratio of requested ad units or queries to the

number returned to the site.

"PAGE_VIEWS_CTR" - Ratio of individual page views that resulted in a

click.

"AD_REQUESTS_CTR" - Ratio of ad requests that resulted in a click.
"MATCHED_AD_REQUESTS_CTR" - Ratio of clicks to matched requests.
"IMPRESSIONS_CTR" - Ratio of IMPRESSIONS that resulted in a click.
"INDIVIDUAL_AD_IMPRESSIONS_CTR" - Ratio of individual ad impressions that

resulted in a click.

"ACTIVE_VIEW_MEASURABILITY" - Ratio of requests that were measurable for

viewability.

"ACTIVE_VIEW_VIEWABILITY" - Ratio of requests that were viewable.
"ACTIVE_VIEW_TIME" - Mean time an ad was displayed on screen.
"ESTIMATED_EARNINGS" - Estimated earnings of the publisher. Note that

earnings up to yesterday are accurate, more recent earnings are estimated due to the possibility of spam, or exchange rate fluctuations.

"PAGE_VIEWS_RPM" - Revenue per thousand page views. This is calculated by

dividing the estimated revenue by the number of page views multiplied by 1000.

"AD_REQUESTS_RPM" - Revenue per thousand ad requests. This is calculated

by dividing estimated revenue by the number of ad requests multiplied by 1000.

"MATCHED_AD_REQUESTS_RPM" - Revenue per thousand matched ad requests. This

is calculated by dividing estimated revenue by the number of matched ad requests multiplied by 1000.

"IMPRESSIONS_RPM" - Revenue per thousand ad impressions. This is

calculated by dividing estimated revenue by the number of ad impressions multiplied by 1000.

"INDIVIDUAL_AD_IMPRESSIONS_RPM" - Revenue per thousand individual ad

impressions. This is calculated by dividing estimated revenue by the number of individual ad impressions multiplied by 1000.

"COST_PER_CLICK" - Amount the publisher earns each time a user clicks on

an ad. CPC is calculated by dividing the estimated revenue by the number of clicks received.

"ADS_PER_IMPRESSION" - Number of ad views per impression.
"TOTAL_EARNINGS" - Total earnings are the gross estimated earnings from

revenue shared traffic before any parent and child account revenue share is applied.

"WEBSEARCH_RESULT_PAGES" - Number of results pages. This metric can only

be used when generating a report in the Google timezone, not the account timezone. Since the account timezone is the default for report generation, this metric can only be used by explicitly specifying `reportingTimeZone=GOOGLE_TIME_ZONE`.

"FUNNEL_REQUESTS" - Number of requests for non-ad units (for example a

related search unit). For more information, see [Funnel requests]([https://support.google.com/adsense/answer/11586959](https://support.google.com/adsense/answer/11586959)).

"FUNNEL_IMPRESSIONS" - Number of requests for non-ad units ads that

returned content that was shown to the user. For more information, see [Funnel impressions]([https://support.google.com/adsense/answer/11585767](https://support.google.com/adsense/answer/11585767)).

"FUNNEL_CLICKS" - Number of times a user clicked on a non-ad unit,

triggering further ad requests. For more information, see [Funnel clicks]([https://support.google.com/adsense/answer/11586382](https://support.google.com/adsense/answer/11586382)).

"FUNNEL_RPM" - Revenue per thousand funnel impressions. This is calculated

by dividing estimated revenue by the number of funnel impressions multiplied by 1000. For more information, see [Funnel RPM]([https://support.google.com/adsense/answer/11585979](https://support.google.com/adsense/answer/11585979)).

OrderBy sets the optional parameter "orderBy": The name of a dimension or metric to sort the resulting report on, can be prefixed with "+" to sort ascending or "-" to sort descending. If no prefix is specified, the column is sorted ascending.

ReportingTimeZone sets the optional parameter "reportingTimeZone": Timezone in which to generate the report. If unspecified, this defaults to the account timezone. For more information, see changing the time zone of your reports ([https://support.google.com/adsense/answer/9830725](https://support.google.com/adsense/answer/9830725)).

Possible values:

"REPORTING_TIME_ZONE_UNSPECIFIED" - Unspecified timezone.
"ACCOUNT_TIME_ZONE" - Use the account timezone in the report.
"GOOGLE_TIME_ZONE" - Use the Google timezone in the report

(America/Los_Angeles).

StartDateDay sets the optional parameter "startDate.day": Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.

StartDateMonth sets the optional parameter "startDate.month": Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.

StartDateYear sets the optional parameter "startDate.year": Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.

type AccountsReportsGenerateCsvCall struct {
	
}

Context sets the context to be used in this call's Do method.

CurrencyCode sets the optional parameter "currencyCode": The ISO-4217 currency code ([https://en.wikipedia.org/wiki/ISO_4217](https://en.wikipedia.org/wiki/ISO_4217)) to use when reporting on monetary metrics. Defaults to the account's currency if not set.

DateRange sets the optional parameter "dateRange": Date range of the report, if unset the range will be considered CUSTOM.

Possible values:

"REPORTING_DATE_RANGE_UNSPECIFIED" - Unspecified date range.
"CUSTOM" - A custom date range specified using the `start_date` and

`end_date` fields. This is the default if no ReportingDateRange is provided.

"TODAY" - Current day.
"YESTERDAY" - Yesterday.
"MONTH_TO_DATE" - From the start of the current month to the current day.

e.g. if the current date is 2020-03-12 then the range will be [2020-03-01, 2020-03-12].

"YEAR_TO_DATE" - From the start of the current year to the current day.

e.g. if the current date is 2020-03-12 then the range will be [2020-01-01, 2020-03-12].

"LAST_7_DAYS" - Last 7 days, excluding current day.
"LAST_30_DAYS" - Last 30 days, excluding current day.

Dimensions sets the optional parameter "dimensions": Dimensions to base the report on.

Possible values:

"DIMENSION_UNSPECIFIED" - Unspecified dimension.
"DATE" - Date dimension in YYYY-MM-DD format (e.g. "2010-02-10").
"WEEK" - Week dimension in YYYY-MM-DD format, representing the first day

of each week (e.g. "2010-02-08"). The first day of the week is determined by the language_code specified in a report generation request (so e.g. this would be a Monday for "en-GB" or "es", but a Sunday for "en" or "fr-CA").

"MONTH" - Month dimension in YYYY-MM format (e.g. "2010-02").
"ACCOUNT_NAME" - Account name. The members of this dimension match the

values from Account.display_name.

"AD_CLIENT_ID" - Unique ID of an ad client. The members of this dimension

match the values from AdClient.reporting_dimension_id.

"HOSTED_AD_CLIENT_ID" - Unique ID of a sub-account's ad client. The

members of this dimension match the values from AdClient.reporting_dimension_id (for the sub-account).

"PRODUCT_NAME" - Localized product name (e.g. "AdSense for Content",

"AdSense for Search").

"PRODUCT_CODE" - Product code (e.g. "AFC", "AFS"). The members of this

dimension match the values from AdClient.product_code.

"AD_UNIT_NAME" - Ad unit name (within which an ad was served). The members

of this dimension match the values from AdUnit.display_name.

"AD_UNIT_ID" - Unique ID of an ad unit (within which an ad was served).

The members of this dimension match the values from AdUnit.reporting_dimension_id.

"AD_UNIT_SIZE_NAME" - Localized size of an ad unit (e.g. "728x90",

"Responsive").

"AD_UNIT_SIZE_CODE" - The size code of an ad unit (e.g. "728x90",

"responsive").

"CUSTOM_CHANNEL_NAME" - Custom channel name. The members of this dimension

match the values from CustomChannel.display_name.

"CUSTOM_CHANNEL_ID" - Unique ID of a custom channel. The members of this

dimension match the values from CustomChannel.reporting_dimension_id.

"HOSTED_CUSTOM_CHANNEL_ID" - Not supported.
"OWNED_SITE_DOMAIN_NAME" - Domain name of a verified site (e.g.

"example.com"). The members of this dimension match the values from Site.domain.

"OWNED_SITE_ID" - Unique ID of a verified site. The members of this

dimension match the values from Site.reporting_dimension_id.

"PAGE_URL" - URL of the page upon which the ad was served. This is a

complete URL including scheme and query parameters. Note that the URL that appears in this dimension may be a canonicalized version of the one that was used in the original request, and so may not exactly match the URL that a user might have seen. Note that there are also some caveats to be aware of when using this dimension. For more information, see [Page URL breakdown]([https://support.google.com/adsense/answer/11988478](https://support.google.com/adsense/answer/11988478)).

"URL_CHANNEL_NAME" - Name of a URL channel. The members of this dimension

match the values from UrlChannel.uri_pattern.

"URL_CHANNEL_ID" - Unique ID of a URL channel. The members of this

dimension match the values from UrlChannel.reporting_dimension_id.

"BUYER_NETWORK_NAME" - Name of an ad network that returned the winning ads

for an ad request (e.g. "Google AdWords"). Note that unlike other "NAME" dimensions, the members of this dimensions are not localized.

"BUYER_NETWORK_ID" - Unique (opaque) ID of an ad network that returned the

winning ads for an ad request.

"BID_TYPE_NAME" - Localized bid type name (e.g. "CPC bids", "CPM bids")

for a served ad.

"BID_TYPE_CODE" - Type of a bid (e.g. "cpc", "cpm") for a served ad.
"CREATIVE_SIZE_NAME" - Localized creative size name (e.g. "728x90",

"Dynamic") of a served ad.

"CREATIVE_SIZE_CODE" - Creative size code (e.g. "728x90", "dynamic") of a

served ad.

"DOMAIN_NAME" - Localized name of a host on which an ad was served, after

IDNA decoding (e.g. "www.google.com", "Web caches and other", "bücher.example").

"DOMAIN_CODE" - Name of a host on which an ad was served (e.g.

"www.google.com", "webcaches", "xn--bcher-kva.example").

"COUNTRY_NAME" - Localized region name of a user viewing an ad (e.g.

"United States", "France").

"COUNTRY_CODE" - CLDR region code of a user viewing an ad (e.g. "US",

"FR").

"PLATFORM_TYPE_NAME" - Localized platform type name (e.g. "High-end mobile

devices", "Desktop").

"PLATFORM_TYPE_CODE" - Platform type code (e.g. "HighEndMobile",

"Desktop").

"TARGETING_TYPE_NAME" - Localized targeting type name (e.g. "Contextual",

"Personalized", "Run of Network").

"TARGETING_TYPE_CODE" - Targeting type code (e.g. "Keyword",

"UserInterest", "RunOfNetwork").

"TRAFFIC_SOURCE_NAME" - Localized traffic source name (e.g. "Google",

"Bing", "Facebook", "Other"). For more information, see [Traffic source breakdown]([https://support.google.com/adsense/answer/16474600](https://support.google.com/adsense/answer/16474600)).

"TRAFFIC_SOURCE_CODE" - Traffic source code (e.g. "GOOGLE", "BING",

"FACEBOOK", "OTHER"). For more information, see [Traffic source breakdown]([https://support.google.com/adsense/answer/16474600](https://support.google.com/adsense/answer/16474600)).

"CONTENT_PLATFORM_NAME" - Localized content platform name an ad request

was made from (e.g. "AMP", "Web").

"CONTENT_PLATFORM_CODE" - Content platform code an ad request was made

from (e.g. "AMP", "HTML").

"AD_PLACEMENT_NAME" - Localized ad placement name (e.g. "Ad unit", "Global

settings", "Manual").

"AD_PLACEMENT_CODE" - Ad placement code (e.g. "AD_UNIT",

"ca-pub-123456:78910", "OTHER").

"REQUESTED_AD_TYPE_NAME" - Localized requested ad type name (e.g.

"Display", "Link unit", "Other").

"REQUESTED_AD_TYPE_CODE" - Requested ad type code (e.g. "IMAGE",

"RADLINK", "OTHER").

"SERVED_AD_TYPE_NAME" - Localized served ad type name (e.g. "Display",

"Link unit", "Other").

"SERVED_AD_TYPE_CODE" - Served ad type code (e.g. "IMAGE", "RADLINK",

"OTHER").

"AD_FORMAT_NAME" - Localized ad format name indicating the way an ad is

shown to the users on your site (e.g. "In-page", "Anchor", "Vignette").

"AD_FORMAT_CODE" - Ad format code indicating the way an ad is shown to the

users on your site (e.g. "ON_PAGE", "ANCHOR", "INTERSTITIAL").

"CUSTOM_SEARCH_STYLE_NAME" - Custom search style name.
"CUSTOM_SEARCH_STYLE_ID" - Custom search style id.
"DOMAIN_REGISTRANT" - Domain registrants.
"WEBSEARCH_QUERY_STRING" - Query strings for web searches.
"OS_TYPE_NAME" - Localized operating system type name (e.g. "Windows",

"MacOS", "Android"). For more information, see [Operating system breakdown]([https://support.google.com/adsense/answer/16853822](https://support.google.com/adsense/answer/16853822)).

"OS_TYPE_CODE" - Operating system type code (e.g. "WINDOWS", "MAC",

"ANDROID"). For more information, see [Operating system breakdown]([https://support.google.com/adsense/answer/16853822](https://support.google.com/adsense/answer/16853822)).

"BROWSER_TYPE_NAME" - Localized browser type name (e.g. "Google Chrome",

"Firefox", "Safari"). For more information, see [Browser breakdown]([https://support.google.com/adsense/answer/16851903](https://support.google.com/adsense/answer/16851903)).

"BROWSER_TYPE_CODE" - Browser type code (e.g. "CHROME", "FIREFOX",

"SAFARI"). For more information, see [Browser breakdown]([https://support.google.com/adsense/answer/16851903](https://support.google.com/adsense/answer/16851903)).

"WEBVIEW_TYPE_NAME" - Localized webview type name (e.g. "Webview

(Uncategorized)", "Non-webview"). For more information, see [Hosting App breakdown]([https://support.google.com/adsense/answer/16853515](https://support.google.com/adsense/answer/16853515)).

"WEBVIEW_TYPE_CODE" - Webview type code (e.g. "UNCATEGORIZED", "NONE").

For more information, see [Hosting App breakdown]([https://support.google.com/adsense/answer/16853515](https://support.google.com/adsense/answer/16853515)).

Do executes the "adsense.accounts.reports.generateCsv" call. Any non-2xx status code is an error. Response headers are in either *HttpBody.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

EndDateDay sets the optional parameter "endDate.day": Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.

EndDateMonth sets the optional parameter "endDate.month": Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.

EndDateYear sets the optional parameter "endDate.year": Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.

Filters sets the optional parameter "filters": A list of filters (/adsense/management/reporting/filtering) to apply to the report. All provided filters must match in order for the data to be included in the report.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

LanguageCode sets the optional parameter "languageCode": The language to use for translating report output. If unspecified, this defaults to English ("en"). If the given language is not supported, report output will be returned in English. The language is specified as an IETF BCP-47 language code ([https://en.wikipedia.org/wiki/IETF_language_tag](https://en.wikipedia.org/wiki/IETF_language_tag)).

Limit sets the optional parameter "limit": The maximum number of rows of report data to return. Reports producing more rows than the requested limit will be truncated. If unset, this defaults to 100,000 rows for `Reports.GenerateReport` and 1,000,000 rows for `Reports.GenerateCsvReport`, which are also the maximum values permitted here. Report truncation can be identified (for `Reports.GenerateReport` only) by comparing the number of rows returned to the value returned in `total_matched_rows`.

Metrics sets the optional parameter "metrics": Required. Reporting metrics.

Possible values:

"METRIC_UNSPECIFIED" - Unspecified metric.
"PAGE_VIEWS" - Number of page views.
"AD_REQUESTS" - Number of ad units that requested ads (for content ads) or

search queries (for search ads). An ad request may result in zero, one, or multiple individual ad impressions depending on the size of the ad unit and whether any ads were available.

"MATCHED_AD_REQUESTS" - Requests that returned at least one ad.
"TOTAL_IMPRESSIONS" - Impressions. An impression is counted for each ad

request where at least one ad has been downloaded to the user's device and has begun to load. It is the number of ad units (for content ads) or search queries (for search ads) that showed ads.

"IMPRESSIONS" - Impressions. An impression is counted for each ad request

where at least one ad has been downloaded to the user's device and has begun to load. It is the number of ad units (for content ads) or search queries (for search ads) that showed ads.

"INDIVIDUAL_AD_IMPRESSIONS" - Ads shown. Different ad formats will display

varying numbers of ads. For example, a vertical banner may consist of 2 or more ads. Also, the number of ads in an ad unit may vary depending on whether the ad unit is displaying standard text ads, expanded text ads or image ads.

"CLICKS" - Number of times a user clicked on a standard content ad.
"PAGE_VIEWS_SPAM_RATIO" - Fraction of page views considered to be spam.

Only available to [premium accounts]([https://developers.google.com/adsense/management/reference/rest/v2/](https://developers.google.com/adsense/management/reference/rest/v2/) accounts#Account.FIELDS.premium).

"AD_REQUESTS_SPAM_RATIO" - Fraction of ad requests considered to be spam.

Only available to [premium accounts]([https://developers.google.com/adsense/management/reference/rest/v2/](https://developers.google.com/adsense/management/reference/rest/v2/) accounts#Account.FIELDS.premium).

"MATCHED_AD_REQUESTS_SPAM_RATIO" - Fraction of ad requests that returned

ads considered to be spam. Only available to [premium accounts]([https://developers.google.com/adsense/management/reference/rest/v2/](https://developers.google.com/adsense/management/reference/rest/v2/) accounts#Account.FIELDS.premium).

"IMPRESSIONS_SPAM_RATIO" - Fraction of impressions considered to be spam.

Only available to [premium accounts]([https://developers.google.com/adsense/management/reference/rest/v2/](https://developers.google.com/adsense/management/reference/rest/v2/) accounts#Account.FIELDS.premium).

"INDIVIDUAL_AD_IMPRESSIONS_SPAM_RATIO" - Fraction of ad impressions

considered to be spam. Only available to [premium accounts]([https://developers.google.com/adsense/management/reference/rest/v2/](https://developers.google.com/adsense/management/reference/rest/v2/) accounts#Account.FIELDS.premium).

"CLICKS_SPAM_RATIO" - Fraction of clicks considered to be spam. Only

available to [premium accounts]([https://developers.google.com/adsense/management/reference/rest/v2/](https://developers.google.com/adsense/management/reference/rest/v2/) accounts#Account.FIELDS.premium).

"AD_REQUESTS_COVERAGE" - Ratio of requested ad units or queries to the

number returned to the site.

"PAGE_VIEWS_CTR" - Ratio of individual page views that resulted in a

click.

"AD_REQUESTS_CTR" - Ratio of ad requests that resulted in a click.
"MATCHED_AD_REQUESTS_CTR" - Ratio of clicks to matched requests.
"IMPRESSIONS_CTR" - Ratio of IMPRESSIONS that resulted in a click.
"INDIVIDUAL_AD_IMPRESSIONS_CTR" - Ratio of individual ad impressions that

resulted in a click.

"ACTIVE_VIEW_MEASURABILITY" - Ratio of requests that were measurable for

viewability.

"ACTIVE_VIEW_VIEWABILITY" - Ratio of requests that were viewable.
"ACTIVE_VIEW_TIME" - Mean time an ad was displayed on screen.
"ESTIMATED_EARNINGS" - Estimated earnings of the publisher. Note that

earnings up to yesterday are accurate, more recent earnings are estimated due to the possibility of spam, or exchange rate fluctuations.

"PAGE_VIEWS_RPM" - Revenue per thousand page views. This is calculated by

dividing the estimated revenue by the number of page views multiplied by 1000.

"AD_REQUESTS_RPM" - Revenue per thousand ad requests. This is calculated

by dividing estimated revenue by the number of ad requests multiplied by 1000.

"MATCHED_AD_REQUESTS_RPM" - Revenue per thousand matched ad requests. This

is calculated by dividing estimated revenue by the number of matched ad requests multiplied by 1000.

"IMPRESSIONS_RPM" - Revenue per thousand ad impressions. This is

calculated by dividing estimated revenue by the number of ad impressions multiplied by 1000.

"INDIVIDUAL_AD_IMPRESSIONS_RPM" - Revenue per thousand individual ad

impressions. This is calculated by dividing estimated revenue by the number of individual ad impressions multiplied by 1000.

"COST_PER_CLICK" - Amount the publisher earns each time a user clicks on

an ad. CPC is calculated by dividing the estimated revenue by the number of clicks received.

"ADS_PER_IMPRESSION" - Number of ad views per impression.
"TOTAL_EARNINGS" - Total earnings are the gross estimated earnings from

revenue shared traffic before any parent and child account revenue share is applied.

"WEBSEARCH_RESULT_PAGES" - Number of results pages. This metric can only

be used when generating a report in the Google timezone, not the account timezone. Since the account timezone is the default for report generation, this metric can only be used by explicitly specifying `reportingTimeZone=GOOGLE_TIME_ZONE`.

"FUNNEL_REQUESTS" - Number of requests for non-ad units (for example a

related search unit). For more information, see [Funnel requests]([https://support.google.com/adsense/answer/11586959](https://support.google.com/adsense/answer/11586959)).

"FUNNEL_IMPRESSIONS" - Number of requests for non-ad units ads that

returned content that was shown to the user. For more information, see [Funnel impressions]([https://support.google.com/adsense/answer/11585767](https://support.google.com/adsense/answer/11585767)).

"FUNNEL_CLICKS" - Number of times a user clicked on a non-ad unit,

triggering further ad requests. For more information, see [Funnel clicks]([https://support.google.com/adsense/answer/11586382](https://support.google.com/adsense/answer/11586382)).

"FUNNEL_RPM" - Revenue per thousand funnel impressions. This is calculated

by dividing estimated revenue by the number of funnel impressions multiplied by 1000. For more information, see [Funnel RPM]([https://support.google.com/adsense/answer/11585979](https://support.google.com/adsense/answer/11585979)).

OrderBy sets the optional parameter "orderBy": The name of a dimension or metric to sort the resulting report on, can be prefixed with "+" to sort ascending or "-" to sort descending. If no prefix is specified, the column is sorted ascending.

ReportingTimeZone sets the optional parameter "reportingTimeZone": Timezone in which to generate the report. If unspecified, this defaults to the account timezone. For more information, see changing the time zone of your reports ([https://support.google.com/adsense/answer/9830725](https://support.google.com/adsense/answer/9830725)).

Possible values:

"REPORTING_TIME_ZONE_UNSPECIFIED" - Unspecified timezone.
"ACCOUNT_TIME_ZONE" - Use the account timezone in the report.
"GOOGLE_TIME_ZONE" - Use the Google timezone in the report

(America/Los_Angeles).

StartDateDay sets the optional parameter "startDate.day": Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.

StartDateMonth sets the optional parameter "startDate.month": Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.

StartDateYear sets the optional parameter "startDate.year": Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.

type AccountsReportsGetSavedCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "adsense.accounts.reports.getSaved" call. Any non-2xx status code is an error. Response headers are in either *SavedReport.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AccountsReportsSavedGenerateCall struct {
	
}

Context sets the context to be used in this call's Do method.

CurrencyCode sets the optional parameter "currencyCode": The ISO-4217 currency code ([https://en.wikipedia.org/wiki/ISO_4217](https://en.wikipedia.org/wiki/ISO_4217)) to use when reporting on monetary metrics. Defaults to the account's currency if not set.

DateRange sets the optional parameter "dateRange": Date range of the report, if unset the range will be considered CUSTOM.

Possible values:

"REPORTING_DATE_RANGE_UNSPECIFIED" - Unspecified date range.
"CUSTOM" - A custom date range specified using the `start_date` and

`end_date` fields. This is the default if no ReportingDateRange is provided.

"TODAY" - Current day.
"YESTERDAY" - Yesterday.
"MONTH_TO_DATE" - From the start of the current month to the current day.

e.g. if the current date is 2020-03-12 then the range will be [2020-03-01, 2020-03-12].

"YEAR_TO_DATE" - From the start of the current year to the current day.

e.g. if the current date is 2020-03-12 then the range will be [2020-01-01, 2020-03-12].

"LAST_7_DAYS" - Last 7 days, excluding current day.
"LAST_30_DAYS" - Last 30 days, excluding current day.

Do executes the "adsense.accounts.reports.saved.generate" call. Any non-2xx status code is an error. Response headers are in either *ReportResult.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

EndDateDay sets the optional parameter "endDate.day": Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.

EndDateMonth sets the optional parameter "endDate.month": Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.

EndDateYear sets the optional parameter "endDate.year": Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

LanguageCode sets the optional parameter "languageCode": The language to use for translating report output. If unspecified, this defaults to English ("en"). If the given language is not supported, report output will be returned in English. The language is specified as an IETF BCP-47 language code ([https://en.wikipedia.org/wiki/IETF_language_tag](https://en.wikipedia.org/wiki/IETF_language_tag)).

ReportingTimeZone sets the optional parameter "reportingTimeZone": Timezone in which to generate the report. If unspecified, this defaults to the account timezone. For more information, see changing the time zone of your reports ([https://support.google.com/adsense/answer/9830725](https://support.google.com/adsense/answer/9830725)).

Possible values:

"REPORTING_TIME_ZONE_UNSPECIFIED" - Unspecified timezone.
"ACCOUNT_TIME_ZONE" - Use the account timezone in the report.
"GOOGLE_TIME_ZONE" - Use the Google timezone in the report

(America/Los_Angeles).

StartDateDay sets the optional parameter "startDate.day": Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.

StartDateMonth sets the optional parameter "startDate.month": Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.

StartDateYear sets the optional parameter "startDate.year": Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.

type AccountsReportsSavedGenerateCsvCall struct {
	
}

Context sets the context to be used in this call's Do method.

CurrencyCode sets the optional parameter "currencyCode": The ISO-4217 currency code ([https://en.wikipedia.org/wiki/ISO_4217](https://en.wikipedia.org/wiki/ISO_4217)) to use when reporting on monetary metrics. Defaults to the account's currency if not set.

DateRange sets the optional parameter "dateRange": Date range of the report, if unset the range will be considered CUSTOM.

Possible values:

"REPORTING_DATE_RANGE_UNSPECIFIED" - Unspecified date range.
"CUSTOM" - A custom date range specified using the `start_date` and

`end_date` fields. This is the default if no ReportingDateRange is provided.

"TODAY" - Current day.
"YESTERDAY" - Yesterday.
"MONTH_TO_DATE" - From the start of the current month to the current day.

e.g. if the current date is 2020-03-12 then the range will be [2020-03-01, 2020-03-12].

"YEAR_TO_DATE" - From the start of the current year to the current day.

e.g. if the current date is 2020-03-12 then the range will be [2020-01-01, 2020-03-12].

"LAST_7_DAYS" - Last 7 days, excluding current day.
"LAST_30_DAYS" - Last 30 days, excluding current day.

Do executes the "adsense.accounts.reports.saved.generateCsv" call. Any non-2xx status code is an error. Response headers are in either *HttpBody.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

EndDateDay sets the optional parameter "endDate.day": Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.

EndDateMonth sets the optional parameter "endDate.month": Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.

EndDateYear sets the optional parameter "endDate.year": Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

LanguageCode sets the optional parameter "languageCode": The language to use for translating report output. If unspecified, this defaults to English ("en"). If the given language is not supported, report output will be returned in English. The language is specified as an IETF BCP-47 language code ([https://en.wikipedia.org/wiki/IETF_language_tag](https://en.wikipedia.org/wiki/IETF_language_tag)).

ReportingTimeZone sets the optional parameter "reportingTimeZone": Timezone in which to generate the report. If unspecified, this defaults to the account timezone. For more information, see changing the time zone of your reports ([https://support.google.com/adsense/answer/9830725](https://support.google.com/adsense/answer/9830725)).

Possible values:

"REPORTING_TIME_ZONE_UNSPECIFIED" - Unspecified timezone.
"ACCOUNT_TIME_ZONE" - Use the account timezone in the report.
"GOOGLE_TIME_ZONE" - Use the Google timezone in the report

(America/Los_Angeles).

StartDateDay sets the optional parameter "startDate.day": Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.

StartDateMonth sets the optional parameter "startDate.month": Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.

StartDateYear sets the optional parameter "startDate.year": Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.

type AccountsReportsSavedListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "adsense.accounts.reports.saved.list" call. Any non-2xx status code is an error. Response headers are in either *ListSavedReportsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": The maximum number of reports to include in the response, used for paging. If unspecified, at most 10000 reports will be returned. The maximum value is 10000; values above 10000 will be coerced to 10000.

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListSavedReports` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListSavedReports` must match the call that provided the page token.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsReportsSavedService struct {
	
}

func NewAccountsReportsSavedService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Service)) *[AccountsReportsSavedService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedService)

Generate: Generates a saved report.

*   name: Name of the saved report. Format: accounts/{account}/reports/{report}.

GenerateCsv: Generates a csv formatted saved report.

*   name: Name of the saved report. Format: accounts/{account}/reports/{report}.

List: Lists saved reports.

*   parent: The account which owns the collection of reports. Format: accounts/{account}.

type AccountsReportsService struct {
 Saved *[AccountsReportsSavedService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsSavedService)	
}

func NewAccountsReportsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Service)) *[AccountsReportsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsService)

Generate: Generates an ad hoc report.

*   account: The account which owns the collection of reports. Format: accounts/{account}.

GenerateCsv: Generates a csv formatted ad hoc report.

*   account: The account which owns the collection of reports. Format: accounts/{account}.

GetSaved: Gets the saved report from the given resource name.

*   name: The name of the saved report to retrieve. Format: accounts/{account}/reports/{report}.

type AccountsService struct {
 Adclients *[AccountsAdclientsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAdclientsService)
 Alerts *[AccountsAlertsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsAlertsService)
 Payments *[AccountsPaymentsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsPaymentsService)
 PolicyIssues *[AccountsPolicyIssuesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsPolicyIssuesService)
 Reports *[AccountsReportsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsReportsService)
 Sites *[AccountsSitesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsSitesService)	
}

func NewAccountsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Service)) *[AccountsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsService)

Get: Gets information about the selected AdSense account.

- name: Account to get information about. Format: accounts/{account}.

GetAdBlockingRecoveryTag: Gets the ad blocking recovery tag of an account.

*   name: The name of the account to get the tag for. Format: accounts/{account}.

func (r *[AccountsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsService)) List() *[AccountsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsListCall)

List: Lists all accounts available to this user.

ListChildAccounts: Lists all accounts directly managed by the given AdSense account.

*   parent: The parent account, which owns the child accounts. Format: accounts/{account}.

type AccountsSitesGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "adsense.accounts.sites.get" call. Any non-2xx status code is an error. Response headers are in either *Site.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AccountsSitesListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "adsense.accounts.sites.list" call. Any non-2xx status code is an error. Response headers are in either *ListSitesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": The maximum number of sites to include in the response, used for paging. If unspecified, at most 10000 sites will be returned. The maximum value is 10000; values above 10000 will be coerced to 10000.

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListSites` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListSites` must match the call that provided the page token.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccountsSitesService struct {
	
}

func NewAccountsSitesService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Service)) *[AccountsSitesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AccountsSitesService)

Get: Gets information about the selected site.

- name: Name of the site. Format: accounts/{account}/sites/{site}.

List: Lists all the sites available in an account.

*   parent: The account which owns the collection of sites. Format: accounts/{account}.

type AdClient struct {
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	
	ProductCode [string](https://pkg.go.dev/builtin#string) `json:"productCode,omitempty"`
	
	
	ReportingDimensionId [string](https://pkg.go.dev/builtin#string) `json:"reportingDimensionId,omitempty"`
	
	
	
	
	
	
	
	
	State [string](https://pkg.go.dev/builtin#string) `json:"state,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

AdClient: Representation of an ad client. An ad client represents a user's subscription with a specific AdSense product.

type AdUnit struct {
	ContentAdsSettings *[ContentAdsSettings](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ContentAdsSettings) `json:"contentAdsSettings,omitempty"`
	
	DisplayName [string](https://pkg.go.dev/builtin#string) `json:"displayName,omitempty"`
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	ReportingDimensionId [string](https://pkg.go.dev/builtin#string) `json:"reportingDimensionId,omitempty"`
	
	
	
	
	
	
	
	State [string](https://pkg.go.dev/builtin#string) `json:"state,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

AdUnit: Representation of an ad unit. An ad unit represents a saved ad unit with a specific set of ad settings that have been customized within an account.

type Alert struct {
	
	Message [string](https://pkg.go.dev/builtin#string) `json:"message,omitempty"`
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	
	
	
	
	
	Severity [string](https://pkg.go.dev/builtin#string) `json:"severity,omitempty"`
	
	
	Type [string](https://pkg.go.dev/builtin#string) `json:"type,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Alert: Representation of an alert.

type Cell struct {
	
	Value [string](https://pkg.go.dev/builtin#string) `json:"value,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Cell: Cell representation.

#### type [ContentAdsSettings](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/adsense/v2/adsense-gen.go#L591)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#ContentAdsSettings "Go to ContentAdsSettings")

type ContentAdsSettings struct {
	
	Size [string](https://pkg.go.dev/builtin#string) `json:"size,omitempty"`
	
	
	
	
	
	
	
	
	
	Type [string](https://pkg.go.dev/builtin#string) `json:"type,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ContentAdsSettings: Settings specific to content ads (AFC).

type CustomChannel struct {
	
	Active [bool](https://pkg.go.dev/builtin#bool) `json:"active,omitempty"`
	DisplayName [string](https://pkg.go.dev/builtin#string) `json:"displayName,omitempty"`
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	ReportingDimensionId [string](https://pkg.go.dev/builtin#string) `json:"reportingDimensionId,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

CustomChannel: Representation of a custom channel.

type Date struct {
	
	
	Day [int64](https://pkg.go.dev/builtin#int64) `json:"day,omitempty"`
	
	Month [int64](https://pkg.go.dev/builtin#int64) `json:"month,omitempty"`
	
	Year [int64](https://pkg.go.dev/builtin#int64) `json:"year,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Date: Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following: * A full date, with non-zero year, month, and day values. * A month and day, with a zero year (for example, an anniversary). * A year on its own, with a zero month and a zero day. * A year and month, with a zero day (for example, a credit card expiration date). Related types: * google.type.TimeOfDay * google.type.DateTime * google.protobuf.Timestamp

Empty: A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }

type Header struct {
	
	
	CurrencyCode [string](https://pkg.go.dev/builtin#string) `json:"currencyCode,omitempty"`
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	
	
	
	
	
	
	
	
	Type [string](https://pkg.go.dev/builtin#string) `json:"type,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Header: The header information of the columns requested in the report.

#### type [HttpBody](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/adsense/v2/adsense-gen.go#L759)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#HttpBody "Go to HttpBody")

HttpBody: Message that represents an arbitrary HTTP body. It should only be used for payload formats that can't be represented as JSON, such as raw binary or an HTML page. This message can be used both in streaming and non-streaming API methods in the request as well as the response. It can be used as a top-level request field, which is convenient if one wants to extract parameters from either the URL or HTTP template into the request fields and also want access to the raw HTTP body. Example: message GetResourceRequest { // A unique request id. string request_id = 1; // The raw HTTP body is bound to this field. google.api.HttpBody http_body = 2; } service ResourceService { rpc GetResource(GetResourceRequest) returns (google.api.HttpBody); rpc UpdateResource(google.api.HttpBody) returns (google.protobuf.Empty); } Example with streaming methods: service CaldavService { rpc GetCalendar(stream google.api.HttpBody) returns (stream google.api.HttpBody); rpc UpdateCalendar(stream google.api.HttpBody) returns (stream google.api.HttpBody); } Use of this type only changes how the request and response bodies are handled, all other features will continue to work unchanged.

type ListAccountsResponse struct {
	Accounts []*[Account](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Account) `json:"accounts,omitempty"`
	
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListAccountsResponse: Response definition for the account list rpc.

type ListAdClientsResponse struct {
	AdClients []*[AdClient](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AdClient) `json:"adClients,omitempty"`
	
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListAdClientsResponse: Response definition for the ad client list rpc.

type ListAdUnitsResponse struct {
	AdUnits []*[AdUnit](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AdUnit) `json:"adUnits,omitempty"`
	
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListAdUnitsResponse: Response definition for the adunit list rpc.

ListAlertsResponse: Response definition for the alerts list rpc.

type ListChildAccountsResponse struct {
	Accounts []*[Account](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Account) `json:"accounts,omitempty"`
	
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListChildAccountsResponse: Response definition for the child account list rpc.

type ListCustomChannelsResponse struct {
	CustomChannels []*[CustomChannel](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#CustomChannel) `json:"customChannels,omitempty"`
	
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListCustomChannelsResponse: Response definition for the custom channel list rpc.

type ListLinkedAdUnitsResponse struct {
	AdUnits []*[AdUnit](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#AdUnit) `json:"adUnits,omitempty"`
	
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListLinkedAdUnitsResponse: Response definition for the ad units linked to a custom channel list rpc.

type ListLinkedCustomChannelsResponse struct {
	CustomChannels []*[CustomChannel](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#CustomChannel) `json:"customChannels,omitempty"`
	
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListLinkedCustomChannelsResponse: Response definition for the custom channels linked to an adunit list rpc.

type ListPaymentsResponse struct {
	Payments []*[Payment](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Payment) `json:"payments,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListPaymentsResponse: Response definition for the payments list rpc.

type ListPolicyIssuesResponse struct {
	
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`
	PolicyIssues []*[PolicyIssue](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#PolicyIssue) `json:"policyIssues,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListPolicyIssuesResponse: Response definition for the policy issues list rpc. Policy issues are reported only if the publisher has at least one AFC ad client in READY or GETTING_READY state. If the publisher has no such AFC ad client, the response will be an empty list.

type ListSavedReportsResponse struct {
	
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`
	SavedReports []*[SavedReport](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#SavedReport) `json:"savedReports,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListSavedReportsResponse: Response definition for the saved reports list rpc.

type ListSitesResponse struct {
	
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`
	Sites []*[Site](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Site) `json:"sites,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListSitesResponse: Response definition for the sites list rpc.

type ListUrlChannelsResponse struct {
	
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`
	UrlChannels []*[UrlChannel](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#UrlChannel) `json:"urlChannels,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListUrlChannelsResponse: Response definition for the url channels list rpc.

type PolicyIssue struct {
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	Action [string](https://pkg.go.dev/builtin#string) `json:"action,omitempty"`
	
	
	
	AdClients [][string](https://pkg.go.dev/builtin#string) `json:"adClients,omitempty"`
	
	AdRequestCount [int64](https://pkg.go.dev/builtin#int64) `json:"adRequestCount,omitempty,string"`
	
	
	
	
	
	
	
	
	EntityType [string](https://pkg.go.dev/builtin#string) `json:"entityType,omitempty"`
	
	FirstDetectedDate *[Date](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Date) `json:"firstDetectedDate,omitempty"`
	
	LastDetectedDate *[Date](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Date) `json:"lastDetectedDate,omitempty"`
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	PolicyTopics []*[PolicyTopic](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#PolicyTopic) `json:"policyTopics,omitempty"`
	
	
	Site [string](https://pkg.go.dev/builtin#string) `json:"site,omitempty"`
	
	
	SiteSection [string](https://pkg.go.dev/builtin#string) `json:"siteSection,omitempty"`
	
	
	Uri [string](https://pkg.go.dev/builtin#string) `json:"uri,omitempty"`
	
	
	
	WarningEscalationDate *[Date](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Date) `json:"warningEscalationDate,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

PolicyIssue: Representation of a policy issue for a single entity (site, site-section, or page). All issues for a single entity are represented by a single PolicyIssue resource, though that PolicyIssue can have multiple causes (or "topics") that can change over time. Policy issues are removed if there are no issues detected recently or if there's a recent successful appeal for the entity.

type PolicyTopic struct {
	MustFix [bool](https://pkg.go.dev/builtin#bool) `json:"mustFix,omitempty"`
	
	Topic [string](https://pkg.go.dev/builtin#string) `json:"topic,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	Type [string](https://pkg.go.dev/builtin#string) `json:"type,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

PolicyTopic: Information about a particular policy topic. A policy topic represents a single class of policy issue that can impact ad serving for your site. For example, sexual content or having ads that obscure your content. A single policy issue can have multiple policy topics for a single entity.

type ReportResult struct {
	
	Averages *[Row](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Row) `json:"averages,omitempty"`
	EndDate *[Date](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Date) `json:"endDate,omitempty"`
	
	Headers []*[Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Header) `json:"headers,omitempty"`
	
	
	Rows []*[Row](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Row) `json:"rows,omitempty"`
	StartDate *[Date](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Date) `json:"startDate,omitempty"`
	TotalMatchedRows [int64](https://pkg.go.dev/builtin#int64) `json:"totalMatchedRows,omitempty,string"`
	
	Totals *[Row](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Row) `json:"totals,omitempty"`
	
	Warnings [][string](https://pkg.go.dev/builtin#string) `json:"warnings,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ReportResult: Result of a generated report.

type Row struct {
	Cells []*[Cell](https://pkg.go.dev/google.golang.org/api@v0.269.0/adsense/v2#Cell) `json:"cells,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Row: Row representation.

SavedReport: Representation of a saved report.

New creates a new Service. It uses the provided http.Client for requests.

Deprecated: please use NewService instead. To provide a custom HTTP client, use option.WithHTTPClient. If you are using google.golang.org/api/googleapis/transport.APIKey, use option.WithAPIKey with NewService instead.

NewService creates a new Service.

type Site struct {
	AutoAdsEnabled [bool](https://pkg.go.dev/builtin#bool) `json:"autoAdsEnabled,omitempty"`
	
	
	Domain [string](https://pkg.go.dev/builtin#string) `json:"domain,omitempty"`
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	ReportingDimensionId [string](https://pkg.go.dev/builtin#string) `json:"reportingDimensionId,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	State [string](https://pkg.go.dev/builtin#string) `json:"state,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Site: Representation of a Site.
