# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha

Title: appengine package - google.golang.org/api/appengine/v1alpha - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha

Markdown Content:
Package appengine provides access to the App Engine Admin API.

For product documentation, see: [https://cloud.google.com/appengine/docs/admin-api/](https://cloud.google.com/appengine/docs/admin-api/)

#### Library status [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#hdr-Library_status "Go to Library status")

These client libraries are officially supported by Google. However, this library is considered complete and is in maintenance mode. This means that we will address critical bugs and security issues but will not add any new features.

When possible, we recommend using our newer [Cloud Client Libraries for Go]([https://pkg.go.dev/cloud.google.com/go](https://pkg.go.dev/cloud.google.com/go)) that are still actively being worked and iterated on.

#### Creating a client [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#hdr-Creating_a_client "Go to Creating a client")

Usage example:

import "google.golang.org/api/appengine/v1alpha"
...
ctx := context.Background()
appengineService, err := appengine.NewService(ctx)

In this example, Google Application Default Credentials are used for authentication. For information on how to create and obtain Application Default Credentials, see [https://developers.google.com/identity/protocols/application-default-credentials](https://developers.google.com/identity/protocols/application-default-credentials).

#### Other authentication options [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#hdr-Other_authentication_options "Go to Other authentication options")

By default, all available scopes (see "Constants") are used to authenticate. To restrict scopes, use [google.golang.org/api/option.WithScopes](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#WithScopes):

appengineService, err := appengine.NewService(ctx, option.WithScopes(appengine.CloudPlatformReadOnlyScope))

To use an API key for authentication (note: some APIs do not support API keys), use [google.golang.org/api/option.WithAPIKey](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#WithAPIKey):

appengineService, err := appengine.NewService(ctx, option.WithAPIKey("AIza..."))

To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow, use [google.golang.org/api/option.WithTokenSource](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#WithTokenSource):

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
appengineService, err := appengine.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))

See [google.golang.org/api/option.ClientOption](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#ClientOption) for details on options.

*   [Constants](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#pkg-constants)
*   [type APIService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#APIService)
*       *   [func New(client *http.Client) (*APIService, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#New)deprecated
    *   [func NewService(ctx context.Context, opts ...option.ClientOption) (*APIService, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#NewService)

*   [type AppsAuthorizedCertificatesCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesCreateCall)
*       *   [func (c *AppsAuthorizedCertificatesCreateCall) Context(ctx context.Context) *AppsAuthorizedCertificatesCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesCreateCall.Context)
    *   [func (c *AppsAuthorizedCertificatesCreateCall) Do(opts ...googleapi.CallOption) (*AuthorizedCertificate, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesCreateCall.Do)
    *   [func (c *AppsAuthorizedCertificatesCreateCall) Fields(s ...googleapi.Field) *AppsAuthorizedCertificatesCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesCreateCall.Fields)
    *   [func (c *AppsAuthorizedCertificatesCreateCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesCreateCall.Header)

*   [type AppsAuthorizedCertificatesDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesDeleteCall)
*       *   [func (c *AppsAuthorizedCertificatesDeleteCall) Context(ctx context.Context) *AppsAuthorizedCertificatesDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesDeleteCall.Context)
    *   [func (c *AppsAuthorizedCertificatesDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesDeleteCall.Do)
    *   [func (c *AppsAuthorizedCertificatesDeleteCall) Fields(s ...googleapi.Field) *AppsAuthorizedCertificatesDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesDeleteCall.Fields)
    *   [func (c *AppsAuthorizedCertificatesDeleteCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesDeleteCall.Header)

*   [type AppsAuthorizedCertificatesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesGetCall)
*       *   [func (c *AppsAuthorizedCertificatesGetCall) Context(ctx context.Context) *AppsAuthorizedCertificatesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesGetCall.Context)
    *   [func (c *AppsAuthorizedCertificatesGetCall) Do(opts ...googleapi.CallOption) (*AuthorizedCertificate, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesGetCall.Do)
    *   [func (c *AppsAuthorizedCertificatesGetCall) Fields(s ...googleapi.Field) *AppsAuthorizedCertificatesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesGetCall.Fields)
    *   [func (c *AppsAuthorizedCertificatesGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesGetCall.Header)
    *   [func (c *AppsAuthorizedCertificatesGetCall) IfNoneMatch(entityTag string) *AppsAuthorizedCertificatesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesGetCall.IfNoneMatch)
    *   [func (c *AppsAuthorizedCertificatesGetCall) View(view string) *AppsAuthorizedCertificatesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesGetCall.View)

*   [type AppsAuthorizedCertificatesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesListCall)
*       *   [func (c *AppsAuthorizedCertificatesListCall) Context(ctx context.Context) *AppsAuthorizedCertificatesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesListCall.Context)
    *   [func (c *AppsAuthorizedCertificatesListCall) Do(opts ...googleapi.CallOption) (*ListAuthorizedCertificatesResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesListCall.Do)
    *   [func (c *AppsAuthorizedCertificatesListCall) Fields(s ...googleapi.Field) *AppsAuthorizedCertificatesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesListCall.Fields)
    *   [func (c *AppsAuthorizedCertificatesListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesListCall.Header)
    *   [func (c *AppsAuthorizedCertificatesListCall) IfNoneMatch(entityTag string) *AppsAuthorizedCertificatesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesListCall.IfNoneMatch)
    *   [func (c *AppsAuthorizedCertificatesListCall) PageSize(pageSize int64) *AppsAuthorizedCertificatesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesListCall.PageSize)
    *   [func (c *AppsAuthorizedCertificatesListCall) PageToken(pageToken string) *AppsAuthorizedCertificatesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesListCall.PageToken)
    *   [func (c *AppsAuthorizedCertificatesListCall) Pages(ctx context.Context, f func(*ListAuthorizedCertificatesResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesListCall.Pages)
    *   [func (c *AppsAuthorizedCertificatesListCall) View(view string) *AppsAuthorizedCertificatesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesListCall.View)

*   [type AppsAuthorizedCertificatesPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesPatchCall)
*       *   [func (c *AppsAuthorizedCertificatesPatchCall) Context(ctx context.Context) *AppsAuthorizedCertificatesPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesPatchCall.Context)
    *   [func (c *AppsAuthorizedCertificatesPatchCall) Do(opts ...googleapi.CallOption) (*AuthorizedCertificate, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesPatchCall.Do)
    *   [func (c *AppsAuthorizedCertificatesPatchCall) Fields(s ...googleapi.Field) *AppsAuthorizedCertificatesPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesPatchCall.Fields)
    *   [func (c *AppsAuthorizedCertificatesPatchCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesPatchCall.Header)
    *   [func (c *AppsAuthorizedCertificatesPatchCall) UpdateMask(updateMask string) *AppsAuthorizedCertificatesPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesPatchCall.UpdateMask)

*   [type AppsAuthorizedCertificatesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesService)
*       *   [func NewAppsAuthorizedCertificatesService(s *APIService) *AppsAuthorizedCertificatesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#NewAppsAuthorizedCertificatesService)

*       *   [func (r *AppsAuthorizedCertificatesService) Create(appsId string, authorizedcertificate *AuthorizedCertificate) *AppsAuthorizedCertificatesCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesService.Create)
    *   [func (r *AppsAuthorizedCertificatesService) Delete(appsId string, authorizedCertificatesId string) *AppsAuthorizedCertificatesDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesService.Delete)
    *   [func (r *AppsAuthorizedCertificatesService) Get(appsId string, authorizedCertificatesId string) *AppsAuthorizedCertificatesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesService.Get)
    *   [func (r *AppsAuthorizedCertificatesService) List(appsId string) *AppsAuthorizedCertificatesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesService.List)
    *   [func (r *AppsAuthorizedCertificatesService) Patch(appsId string, authorizedCertificatesId string, ...) *AppsAuthorizedCertificatesPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesService.Patch)

*   [type AppsAuthorizedDomainsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedDomainsListCall)
*       *   [func (c *AppsAuthorizedDomainsListCall) Context(ctx context.Context) *AppsAuthorizedDomainsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedDomainsListCall.Context)
    *   [func (c *AppsAuthorizedDomainsListCall) Do(opts ...googleapi.CallOption) (*ListAuthorizedDomainsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedDomainsListCall.Do)
    *   [func (c *AppsAuthorizedDomainsListCall) Fields(s ...googleapi.Field) *AppsAuthorizedDomainsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedDomainsListCall.Fields)
    *   [func (c *AppsAuthorizedDomainsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedDomainsListCall.Header)
    *   [func (c *AppsAuthorizedDomainsListCall) IfNoneMatch(entityTag string) *AppsAuthorizedDomainsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedDomainsListCall.IfNoneMatch)
    *   [func (c *AppsAuthorizedDomainsListCall) PageSize(pageSize int64) *AppsAuthorizedDomainsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedDomainsListCall.PageSize)
    *   [func (c *AppsAuthorizedDomainsListCall) PageToken(pageToken string) *AppsAuthorizedDomainsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedDomainsListCall.PageToken)
    *   [func (c *AppsAuthorizedDomainsListCall) Pages(ctx context.Context, f func(*ListAuthorizedDomainsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedDomainsListCall.Pages)

*   [type AppsAuthorizedDomainsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedDomainsService)
*       *   [func NewAppsAuthorizedDomainsService(s *APIService) *AppsAuthorizedDomainsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#NewAppsAuthorizedDomainsService)

*       *   [func (r *AppsAuthorizedDomainsService) List(appsId string) *AppsAuthorizedDomainsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedDomainsService.List)

*   [type AppsDomainMappingsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsCreateCall)
*       *   [func (c *AppsDomainMappingsCreateCall) Context(ctx context.Context) *AppsDomainMappingsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsCreateCall.Context)
    *   [func (c *AppsDomainMappingsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsCreateCall.Do)
    *   [func (c *AppsDomainMappingsCreateCall) Fields(s ...googleapi.Field) *AppsDomainMappingsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsCreateCall.Fields)
    *   [func (c *AppsDomainMappingsCreateCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsCreateCall.Header)
    *   [func (c *AppsDomainMappingsCreateCall) NoManagedCertificate(noManagedCertificate bool) *AppsDomainMappingsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsCreateCall.NoManagedCertificate)
    *   [func (c *AppsDomainMappingsCreateCall) OverrideStrategy(overrideStrategy string) *AppsDomainMappingsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsCreateCall.OverrideStrategy)

*   [type AppsDomainMappingsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsDeleteCall)
*       *   [func (c *AppsDomainMappingsDeleteCall) Context(ctx context.Context) *AppsDomainMappingsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsDeleteCall.Context)
    *   [func (c *AppsDomainMappingsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsDeleteCall.Do)
    *   [func (c *AppsDomainMappingsDeleteCall) Fields(s ...googleapi.Field) *AppsDomainMappingsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsDeleteCall.Fields)
    *   [func (c *AppsDomainMappingsDeleteCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsDeleteCall.Header)

*   [type AppsDomainMappingsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsGetCall)
*       *   [func (c *AppsDomainMappingsGetCall) Context(ctx context.Context) *AppsDomainMappingsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsGetCall.Context)
    *   [func (c *AppsDomainMappingsGetCall) Do(opts ...googleapi.CallOption) (*DomainMapping, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsGetCall.Do)
    *   [func (c *AppsDomainMappingsGetCall) Fields(s ...googleapi.Field) *AppsDomainMappingsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsGetCall.Fields)
    *   [func (c *AppsDomainMappingsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsGetCall.Header)
    *   [func (c *AppsDomainMappingsGetCall) IfNoneMatch(entityTag string) *AppsDomainMappingsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsGetCall.IfNoneMatch)

*   [type AppsDomainMappingsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsListCall)
*       *   [func (c *AppsDomainMappingsListCall) Context(ctx context.Context) *AppsDomainMappingsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsListCall.Context)
    *   [func (c *AppsDomainMappingsListCall) Do(opts ...googleapi.CallOption) (*ListDomainMappingsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsListCall.Do)
    *   [func (c *AppsDomainMappingsListCall) Fields(s ...googleapi.Field) *AppsDomainMappingsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsListCall.Fields)
    *   [func (c *AppsDomainMappingsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsListCall.Header)
    *   [func (c *AppsDomainMappingsListCall) IfNoneMatch(entityTag string) *AppsDomainMappingsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsListCall.IfNoneMatch)
    *   [func (c *AppsDomainMappingsListCall) PageSize(pageSize int64) *AppsDomainMappingsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsListCall.PageSize)
    *   [func (c *AppsDomainMappingsListCall) PageToken(pageToken string) *AppsDomainMappingsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsListCall.PageToken)
    *   [func (c *AppsDomainMappingsListCall) Pages(ctx context.Context, f func(*ListDomainMappingsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsListCall.Pages)

*   [type AppsDomainMappingsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsPatchCall)
*       *   [func (c *AppsDomainMappingsPatchCall) Context(ctx context.Context) *AppsDomainMappingsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsPatchCall.Context)
    *   [func (c *AppsDomainMappingsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsPatchCall.Do)
    *   [func (c *AppsDomainMappingsPatchCall) Fields(s ...googleapi.Field) *AppsDomainMappingsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsPatchCall.Fields)
    *   [func (c *AppsDomainMappingsPatchCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsPatchCall.Header)
    *   [func (c *AppsDomainMappingsPatchCall) NoManagedCertificate(noManagedCertificate bool) *AppsDomainMappingsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsPatchCall.NoManagedCertificate)
    *   [func (c *AppsDomainMappingsPatchCall) UpdateMask(updateMask string) *AppsDomainMappingsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsPatchCall.UpdateMask)

*   [type AppsDomainMappingsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsService)
*       *   [func NewAppsDomainMappingsService(s *APIService) *AppsDomainMappingsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#NewAppsDomainMappingsService)

*       *   [func (r *AppsDomainMappingsService) Create(appsId string, domainmapping *DomainMapping) *AppsDomainMappingsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsService.Create)
    *   [func (r *AppsDomainMappingsService) Delete(appsId string, domainMappingsId string) *AppsDomainMappingsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsService.Delete)
    *   [func (r *AppsDomainMappingsService) Get(appsId string, domainMappingsId string) *AppsDomainMappingsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsService.Get)
    *   [func (r *AppsDomainMappingsService) List(appsId string) *AppsDomainMappingsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsService.List)
    *   [func (r *AppsDomainMappingsService) Patch(appsId string, domainMappingsId string, domainmapping *DomainMapping) *AppsDomainMappingsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsService.Patch)

*   [type AppsLocationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsLocationsGetCall)
*       *   [func (c *AppsLocationsGetCall) Context(ctx context.Context) *AppsLocationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsLocationsGetCall.Context)
    *   [func (c *AppsLocationsGetCall) Do(opts ...googleapi.CallOption) (*Location, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsLocationsGetCall.Do)
    *   [func (c *AppsLocationsGetCall) Fields(s ...googleapi.Field) *AppsLocationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsLocationsGetCall.Fields)
    *   [func (c *AppsLocationsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsLocationsGetCall.Header)
    *   [func (c *AppsLocationsGetCall) IfNoneMatch(entityTag string) *AppsLocationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsLocationsGetCall.IfNoneMatch)

*   [type AppsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsLocationsListCall)
*       *   [func (c *AppsLocationsListCall) Context(ctx context.Context) *AppsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsLocationsListCall.Context)
    *   [func (c *AppsLocationsListCall) Do(opts ...googleapi.CallOption) (*ListLocationsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsLocationsListCall.Do)
    *   [func (c *AppsLocationsListCall) ExtraLocationTypes(extraLocationTypes ...string) *AppsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsLocationsListCall.ExtraLocationTypes)
    *   [func (c *AppsLocationsListCall) Fields(s ...googleapi.Field) *AppsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsLocationsListCall.Fields)
    *   [func (c *AppsLocationsListCall) Filter(filter string) *AppsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsLocationsListCall.Filter)
    *   [func (c *AppsLocationsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsLocationsListCall.Header)
    *   [func (c *AppsLocationsListCall) IfNoneMatch(entityTag string) *AppsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsLocationsListCall.IfNoneMatch)
    *   [func (c *AppsLocationsListCall) PageSize(pageSize int64) *AppsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsLocationsListCall.PageSize)
    *   [func (c *AppsLocationsListCall) PageToken(pageToken string) *AppsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsLocationsListCall.PageToken)
    *   [func (c *AppsLocationsListCall) Pages(ctx context.Context, f func(*ListLocationsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsLocationsListCall.Pages)

*   [type AppsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsLocationsService)
*       *   [func NewAppsLocationsService(s *APIService) *AppsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#NewAppsLocationsService)

*       *   [func (r *AppsLocationsService) Get(appsId string, locationsId string) *AppsLocationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsLocationsService.Get)
    *   [func (r *AppsLocationsService) List(appsId string) *AppsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsLocationsService.List)

*   [type AppsOperationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsOperationsGetCall)
*       *   [func (c *AppsOperationsGetCall) Context(ctx context.Context) *AppsOperationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsOperationsGetCall.Context)
    *   [func (c *AppsOperationsGetCall) Do(opts ...googleapi.CallOption) (*Operation, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsOperationsGetCall.Do)
    *   [func (c *AppsOperationsGetCall) Fields(s ...googleapi.Field) *AppsOperationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsOperationsGetCall.Fields)
    *   [func (c *AppsOperationsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsOperationsGetCall.Header)
    *   [func (c *AppsOperationsGetCall) IfNoneMatch(entityTag string) *AppsOperationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsOperationsGetCall.IfNoneMatch)

*   [type AppsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsOperationsListCall)
*       *   [func (c *AppsOperationsListCall) Context(ctx context.Context) *AppsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsOperationsListCall.Context)
    *   [func (c *AppsOperationsListCall) Do(opts ...googleapi.CallOption) (*ListOperationsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsOperationsListCall.Do)
    *   [func (c *AppsOperationsListCall) Fields(s ...googleapi.Field) *AppsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsOperationsListCall.Fields)
    *   [func (c *AppsOperationsListCall) Filter(filter string) *AppsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsOperationsListCall.Filter)
    *   [func (c *AppsOperationsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsOperationsListCall.Header)
    *   [func (c *AppsOperationsListCall) IfNoneMatch(entityTag string) *AppsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsOperationsListCall.IfNoneMatch)
    *   [func (c *AppsOperationsListCall) PageSize(pageSize int64) *AppsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsOperationsListCall.PageSize)
    *   [func (c *AppsOperationsListCall) PageToken(pageToken string) *AppsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsOperationsListCall.PageToken)
    *   [func (c *AppsOperationsListCall) Pages(ctx context.Context, f func(*ListOperationsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsOperationsListCall.Pages)
    *   [func (c *AppsOperationsListCall) ReturnPartialSuccess(returnPartialSuccess bool) *AppsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsOperationsListCall.ReturnPartialSuccess)

*   [type AppsOperationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsOperationsService)
*       *   [func NewAppsOperationsService(s *APIService) *AppsOperationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#NewAppsOperationsService)

*       *   [func (r *AppsOperationsService) Get(appsId string, operationsId string) *AppsOperationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsOperationsService.Get)
    *   [func (r *AppsOperationsService) List(appsId string) *AppsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsOperationsService.List)

*   [type AppsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsService)
*       *   [func NewAppsService(s *APIService) *AppsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#NewAppsService)

*   [type AuthorizedCertificate](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AuthorizedCertificate)
*       *   [func (s AuthorizedCertificate) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AuthorizedCertificate.MarshalJSON)

*   [type AuthorizedDomain](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AuthorizedDomain)
*       *   [func (s AuthorizedDomain) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AuthorizedDomain.MarshalJSON)

*   [type CertificateRawData](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#CertificateRawData)
*       *   [func (s CertificateRawData) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#CertificateRawData.MarshalJSON)

*   [type ContainerState](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ContainerState)
*       *   [func (s ContainerState) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ContainerState.MarshalJSON)

*   [type CreateVersionMetadataV1](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#CreateVersionMetadataV1)
*       *   [func (s CreateVersionMetadataV1) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#CreateVersionMetadataV1.MarshalJSON)

*   [type CreateVersionMetadataV1Alpha](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#CreateVersionMetadataV1Alpha)
*       *   [func (s CreateVersionMetadataV1Alpha) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#CreateVersionMetadataV1Alpha.MarshalJSON)

*   [type CreateVersionMetadataV1Beta](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#CreateVersionMetadataV1Beta)
*       *   [func (s CreateVersionMetadataV1Beta) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#CreateVersionMetadataV1Beta.MarshalJSON)

*   [type DomainMapping](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#DomainMapping)
*       *   [func (s DomainMapping) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#DomainMapping.MarshalJSON)

*   [type Empty](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#Empty)
*   [type GceTag](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#GceTag)
*       *   [func (s GceTag) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#GceTag.MarshalJSON)

*   [type GoogleAppengineV1betaLocationMetadata](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#GoogleAppengineV1betaLocationMetadata)
*       *   [func (s GoogleAppengineV1betaLocationMetadata) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#GoogleAppengineV1betaLocationMetadata.MarshalJSON)

*   [type ListAuthorizedCertificatesResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ListAuthorizedCertificatesResponse)
*       *   [func (s ListAuthorizedCertificatesResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ListAuthorizedCertificatesResponse.MarshalJSON)

*   [type ListAuthorizedDomainsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ListAuthorizedDomainsResponse)
*       *   [func (s ListAuthorizedDomainsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ListAuthorizedDomainsResponse.MarshalJSON)

*   [type ListDomainMappingsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ListDomainMappingsResponse)
*       *   [func (s ListDomainMappingsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ListDomainMappingsResponse.MarshalJSON)

*   [type ListLocationsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ListLocationsResponse)
*       *   [func (s ListLocationsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ListLocationsResponse.MarshalJSON)

*   [type ListOperationsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ListOperationsResponse)
*       *   [func (s ListOperationsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ListOperationsResponse.MarshalJSON)

*   [type Location](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#Location)
*       *   [func (s Location) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#Location.MarshalJSON)

*   [type LocationMetadata](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#LocationMetadata)
*       *   [func (s LocationMetadata) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#LocationMetadata.MarshalJSON)

*   [type ManagedCertificate](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ManagedCertificate)
*       *   [func (s ManagedCertificate) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ManagedCertificate.MarshalJSON)

*   [type Operation](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#Operation)
*       *   [func (s Operation) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#Operation.MarshalJSON)

*   [type OperationMetadataV1](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#OperationMetadataV1)
*       *   [func (s OperationMetadataV1) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#OperationMetadataV1.MarshalJSON)

*   [type OperationMetadataV1Alpha](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#OperationMetadataV1Alpha)
*       *   [func (s OperationMetadataV1Alpha) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#OperationMetadataV1Alpha.MarshalJSON)

*   [type OperationMetadataV1Beta](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#OperationMetadataV1Beta)
*       *   [func (s OperationMetadataV1Beta) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#OperationMetadataV1Beta.MarshalJSON)

*   [type ProjectEvent](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectEvent)
*       *   [func (s ProjectEvent) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectEvent.MarshalJSON)

*   [type ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall)
*       *   [func (c *ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall) Context(ctx context.Context) *ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall.Context)
    *   [func (c *ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall) Do(opts ...googleapi.CallOption) (*AuthorizedCertificate, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall.Do)
    *   [func (c *ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall.Fields)
    *   [func (c *ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall.Header)

*   [type ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall)
*       *   [func (c *ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall) Context(ctx context.Context) *ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall.Context)
    *   [func (c *ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall.Do)
    *   [func (c *ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall.Fields)
    *   [func (c *ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall.Header)

*   [type ProjectsLocationsApplicationsAuthorizedCertificatesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesGetCall)
*       *   [func (c *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall) Context(ctx context.Context) *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesGetCall.Context)
    *   [func (c *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall) Do(opts ...googleapi.CallOption) (*AuthorizedCertificate, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesGetCall.Do)
    *   [func (c *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesGetCall.Fields)
    *   [func (c *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesGetCall.Header)
    *   [func (c *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesGetCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall) View(view string) *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesGetCall.View)

*   [type ProjectsLocationsApplicationsAuthorizedCertificatesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesListCall)
*       *   [func (c *ProjectsLocationsApplicationsAuthorizedCertificatesListCall) Context(ctx context.Context) *ProjectsLocationsApplicationsAuthorizedCertificatesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesListCall.Context)
    *   [func (c *ProjectsLocationsApplicationsAuthorizedCertificatesListCall) Do(opts ...googleapi.CallOption) (*ListAuthorizedCertificatesResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesListCall.Do)
    *   [func (c *ProjectsLocationsApplicationsAuthorizedCertificatesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsAuthorizedCertificatesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesListCall.Fields)
    *   [func (c *ProjectsLocationsApplicationsAuthorizedCertificatesListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesListCall.Header)
    *   [func (c *ProjectsLocationsApplicationsAuthorizedCertificatesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationsAuthorizedCertificatesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesListCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsApplicationsAuthorizedCertificatesListCall) PageSize(pageSize int64) *ProjectsLocationsApplicationsAuthorizedCertificatesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesListCall.PageSize)
    *   [func (c *ProjectsLocationsApplicationsAuthorizedCertificatesListCall) PageToken(pageToken string) *ProjectsLocationsApplicationsAuthorizedCertificatesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesListCall.PageToken)
    *   [func (c *ProjectsLocationsApplicationsAuthorizedCertificatesListCall) Pages(ctx context.Context, f func(*ListAuthorizedCertificatesResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesListCall.Pages)
    *   [func (c *ProjectsLocationsApplicationsAuthorizedCertificatesListCall) View(view string) *ProjectsLocationsApplicationsAuthorizedCertificatesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesListCall.View)

*   [type ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall)
*       *   [func (c *ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall) Context(ctx context.Context) *ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall.Context)
    *   [func (c *ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall) Do(opts ...googleapi.CallOption) (*AuthorizedCertificate, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall.Do)
    *   [func (c *ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall.Fields)
    *   [func (c *ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall.Header)
    *   [func (c *ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall.UpdateMask)

*   [type ProjectsLocationsApplicationsAuthorizedCertificatesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesService)
*       *   [func NewProjectsLocationsApplicationsAuthorizedCertificatesService(s *APIService) *ProjectsLocationsApplicationsAuthorizedCertificatesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#NewProjectsLocationsApplicationsAuthorizedCertificatesService)

*       *   [func (r *ProjectsLocationsApplicationsAuthorizedCertificatesService) Create(projectsId string, locationsId string, applicationsId string, ...) *ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesService.Create)
    *   [func (r *ProjectsLocationsApplicationsAuthorizedCertificatesService) Delete(projectsId string, locationsId string, applicationsId string, ...) *ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesService.Delete)
    *   [func (r *ProjectsLocationsApplicationsAuthorizedCertificatesService) Get(projectsId string, locationsId string, applicationsId string, ...) *ProjectsLocationsApplicationsAuthorizedCertificatesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesService.Get)
    *   [func (r *ProjectsLocationsApplicationsAuthorizedCertificatesService) List(projectsId string, locationsId string, applicationsId string) *ProjectsLocationsApplicationsAuthorizedCertificatesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesService.List)
    *   [func (r *ProjectsLocationsApplicationsAuthorizedCertificatesService) Patch(projectsId string, locationsId string, applicationsId string, ...) *ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesService.Patch)

*   [type ProjectsLocationsApplicationsAuthorizedDomainsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedDomainsListCall)
*       *   [func (c *ProjectsLocationsApplicationsAuthorizedDomainsListCall) Context(ctx context.Context) *ProjectsLocationsApplicationsAuthorizedDomainsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedDomainsListCall.Context)
    *   [func (c *ProjectsLocationsApplicationsAuthorizedDomainsListCall) Do(opts ...googleapi.CallOption) (*ListAuthorizedDomainsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedDomainsListCall.Do)
    *   [func (c *ProjectsLocationsApplicationsAuthorizedDomainsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsAuthorizedDomainsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedDomainsListCall.Fields)
    *   [func (c *ProjectsLocationsApplicationsAuthorizedDomainsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedDomainsListCall.Header)
    *   [func (c *ProjectsLocationsApplicationsAuthorizedDomainsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationsAuthorizedDomainsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedDomainsListCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsApplicationsAuthorizedDomainsListCall) PageSize(pageSize int64) *ProjectsLocationsApplicationsAuthorizedDomainsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedDomainsListCall.PageSize)
    *   [func (c *ProjectsLocationsApplicationsAuthorizedDomainsListCall) PageToken(pageToken string) *ProjectsLocationsApplicationsAuthorizedDomainsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedDomainsListCall.PageToken)
    *   [func (c *ProjectsLocationsApplicationsAuthorizedDomainsListCall) Pages(ctx context.Context, f func(*ListAuthorizedDomainsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedDomainsListCall.Pages)

*   [type ProjectsLocationsApplicationsAuthorizedDomainsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedDomainsService)
*       *   [func NewProjectsLocationsApplicationsAuthorizedDomainsService(s *APIService) *ProjectsLocationsApplicationsAuthorizedDomainsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#NewProjectsLocationsApplicationsAuthorizedDomainsService)

*       *   [func (r *ProjectsLocationsApplicationsAuthorizedDomainsService) List(projectsId string, locationsId string, applicationsId string) *ProjectsLocationsApplicationsAuthorizedDomainsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedDomainsService.List)

*   [type ProjectsLocationsApplicationsDomainMappingsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsCreateCall)
*       *   [func (c *ProjectsLocationsApplicationsDomainMappingsCreateCall) Context(ctx context.Context) *ProjectsLocationsApplicationsDomainMappingsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsCreateCall.Context)
    *   [func (c *ProjectsLocationsApplicationsDomainMappingsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsCreateCall.Do)
    *   [func (c *ProjectsLocationsApplicationsDomainMappingsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsDomainMappingsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsCreateCall.Fields)
    *   [func (c *ProjectsLocationsApplicationsDomainMappingsCreateCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsCreateCall.Header)
    *   [func (c *ProjectsLocationsApplicationsDomainMappingsCreateCall) NoManagedCertificate(noManagedCertificate bool) *ProjectsLocationsApplicationsDomainMappingsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsCreateCall.NoManagedCertificate)
    *   [func (c *ProjectsLocationsApplicationsDomainMappingsCreateCall) OverrideStrategy(overrideStrategy string) *ProjectsLocationsApplicationsDomainMappingsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsCreateCall.OverrideStrategy)

*   [type ProjectsLocationsApplicationsDomainMappingsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsDeleteCall)
*       *   [func (c *ProjectsLocationsApplicationsDomainMappingsDeleteCall) Context(ctx context.Context) *ProjectsLocationsApplicationsDomainMappingsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsDeleteCall.Context)
    *   [func (c *ProjectsLocationsApplicationsDomainMappingsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsDeleteCall.Do)
    *   [func (c *ProjectsLocationsApplicationsDomainMappingsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsDomainMappingsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsDeleteCall.Fields)
    *   [func (c *ProjectsLocationsApplicationsDomainMappingsDeleteCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsDeleteCall.Header)

*   [type ProjectsLocationsApplicationsDomainMappingsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsGetCall)
*       *   [func (c *ProjectsLocationsApplicationsDomainMappingsGetCall) Context(ctx context.Context) *ProjectsLocationsApplicationsDomainMappingsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsGetCall.Context)
    *   [func (c *ProjectsLocationsApplicationsDomainMappingsGetCall) Do(opts ...googleapi.CallOption) (*DomainMapping, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsGetCall.Do)
    *   [func (c *ProjectsLocationsApplicationsDomainMappingsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsDomainMappingsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsGetCall.Fields)
    *   [func (c *ProjectsLocationsApplicationsDomainMappingsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsGetCall.Header)
    *   [func (c *ProjectsLocationsApplicationsDomainMappingsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationsDomainMappingsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsGetCall.IfNoneMatch)

*   [type ProjectsLocationsApplicationsDomainMappingsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsListCall)
*       *   [func (c *ProjectsLocationsApplicationsDomainMappingsListCall) Context(ctx context.Context) *ProjectsLocationsApplicationsDomainMappingsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsListCall.Context)
    *   [func (c *ProjectsLocationsApplicationsDomainMappingsListCall) Do(opts ...googleapi.CallOption) (*ListDomainMappingsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsListCall.Do)
    *   [func (c *ProjectsLocationsApplicationsDomainMappingsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsDomainMappingsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsListCall.Fields)
    *   [func (c *ProjectsLocationsApplicationsDomainMappingsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsListCall.Header)
    *   [func (c *ProjectsLocationsApplicationsDomainMappingsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApplicationsDomainMappingsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsListCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsApplicationsDomainMappingsListCall) PageSize(pageSize int64) *ProjectsLocationsApplicationsDomainMappingsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsListCall.PageSize)
    *   [func (c *ProjectsLocationsApplicationsDomainMappingsListCall) PageToken(pageToken string) *ProjectsLocationsApplicationsDomainMappingsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsListCall.PageToken)
    *   [func (c *ProjectsLocationsApplicationsDomainMappingsListCall) Pages(ctx context.Context, f func(*ListDomainMappingsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsListCall.Pages)

*   [type ProjectsLocationsApplicationsDomainMappingsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsPatchCall)
*       *   [func (c *ProjectsLocationsApplicationsDomainMappingsPatchCall) Context(ctx context.Context) *ProjectsLocationsApplicationsDomainMappingsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsPatchCall.Context)
    *   [func (c *ProjectsLocationsApplicationsDomainMappingsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsPatchCall.Do)
    *   [func (c *ProjectsLocationsApplicationsDomainMappingsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApplicationsDomainMappingsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsPatchCall.Fields)
    *   [func (c *ProjectsLocationsApplicationsDomainMappingsPatchCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsPatchCall.Header)
    *   [func (c *ProjectsLocationsApplicationsDomainMappingsPatchCall) NoManagedCertificate(noManagedCertificate bool) *ProjectsLocationsApplicationsDomainMappingsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsPatchCall.NoManagedCertificate)
    *   [func (c *ProjectsLocationsApplicationsDomainMappingsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApplicationsDomainMappingsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsPatchCall.UpdateMask)

*   [type ProjectsLocationsApplicationsDomainMappingsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsService)
*       *   [func NewProjectsLocationsApplicationsDomainMappingsService(s *APIService) *ProjectsLocationsApplicationsDomainMappingsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#NewProjectsLocationsApplicationsDomainMappingsService)

*       *   [func (r *ProjectsLocationsApplicationsDomainMappingsService) Create(projectsId string, locationsId string, applicationsId string, ...) *ProjectsLocationsApplicationsDomainMappingsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsService.Create)
    *   [func (r *ProjectsLocationsApplicationsDomainMappingsService) Delete(projectsId string, locationsId string, applicationsId string, ...) *ProjectsLocationsApplicationsDomainMappingsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsService.Delete)
    *   [func (r *ProjectsLocationsApplicationsDomainMappingsService) Get(projectsId string, locationsId string, applicationsId string, ...) *ProjectsLocationsApplicationsDomainMappingsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsService.Get)
    *   [func (r *ProjectsLocationsApplicationsDomainMappingsService) List(projectsId string, locationsId string, applicationsId string) *ProjectsLocationsApplicationsDomainMappingsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsService.List)
    *   [func (r *ProjectsLocationsApplicationsDomainMappingsService) Patch(projectsId string, locationsId string, applicationsId string, ...) *ProjectsLocationsApplicationsDomainMappingsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsService.Patch)

*   [type ProjectsLocationsApplicationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsService)
*       *   [func NewProjectsLocationsApplicationsService(s *APIService) *ProjectsLocationsApplicationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#NewProjectsLocationsApplicationsService)

*   [type ProjectsLocationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsGetCall)
*       *   [func (c *ProjectsLocationsGetCall) Context(ctx context.Context) *ProjectsLocationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsGetCall.Context)
    *   [func (c *ProjectsLocationsGetCall) Do(opts ...googleapi.CallOption) (*Location, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsGetCall.Do)
    *   [func (c *ProjectsLocationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsGetCall.Fields)
    *   [func (c *ProjectsLocationsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsGetCall.Header)
    *   [func (c *ProjectsLocationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsGetCall.IfNoneMatch)

*   [type ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsListCall)
*       *   [func (c *ProjectsLocationsListCall) Context(ctx context.Context) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsListCall.Context)
    *   [func (c *ProjectsLocationsListCall) Do(opts ...googleapi.CallOption) (*ListLocationsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsListCall.Do)
    *   [func (c *ProjectsLocationsListCall) ExtraLocationTypes(extraLocationTypes ...string) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsListCall.ExtraLocationTypes)
    *   [func (c *ProjectsLocationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsListCall.Fields)
    *   [func (c *ProjectsLocationsListCall) Filter(filter string) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsListCall.Filter)
    *   [func (c *ProjectsLocationsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsListCall.Header)
    *   [func (c *ProjectsLocationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsListCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsListCall) PageSize(pageSize int64) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsListCall.PageSize)
    *   [func (c *ProjectsLocationsListCall) PageToken(pageToken string) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsListCall.PageToken)
    *   [func (c *ProjectsLocationsListCall) Pages(ctx context.Context, f func(*ListLocationsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsListCall.Pages)

*   [type ProjectsLocationsOperationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsOperationsGetCall)
*       *   [func (c *ProjectsLocationsOperationsGetCall) Context(ctx context.Context) *ProjectsLocationsOperationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsOperationsGetCall.Context)
    *   [func (c *ProjectsLocationsOperationsGetCall) Do(opts ...googleapi.CallOption) (*Operation, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsOperationsGetCall.Do)
    *   [func (c *ProjectsLocationsOperationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsOperationsGetCall.Fields)
    *   [func (c *ProjectsLocationsOperationsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsOperationsGetCall.Header)
    *   [func (c *ProjectsLocationsOperationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsOperationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsOperationsGetCall.IfNoneMatch)

*   [type ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsOperationsListCall)
*       *   [func (c *ProjectsLocationsOperationsListCall) Context(ctx context.Context) *ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsOperationsListCall.Context)
    *   [func (c *ProjectsLocationsOperationsListCall) Do(opts ...googleapi.CallOption) (*ListOperationsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsOperationsListCall.Do)
    *   [func (c *ProjectsLocationsOperationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsOperationsListCall.Fields)
    *   [func (c *ProjectsLocationsOperationsListCall) Filter(filter string) *ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsOperationsListCall.Filter)
    *   [func (c *ProjectsLocationsOperationsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsOperationsListCall.Header)
    *   [func (c *ProjectsLocationsOperationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsOperationsListCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsOperationsListCall) PageSize(pageSize int64) *ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsOperationsListCall.PageSize)
    *   [func (c *ProjectsLocationsOperationsListCall) PageToken(pageToken string) *ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsOperationsListCall.PageToken)
    *   [func (c *ProjectsLocationsOperationsListCall) Pages(ctx context.Context, f func(*ListOperationsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsOperationsListCall.Pages)
    *   [func (c *ProjectsLocationsOperationsListCall) ReturnPartialSuccess(returnPartialSuccess bool) *ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsOperationsListCall.ReturnPartialSuccess)

*   [type ProjectsLocationsOperationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsOperationsService)
*       *   [func NewProjectsLocationsOperationsService(s *APIService) *ProjectsLocationsOperationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#NewProjectsLocationsOperationsService)

*       *   [func (r *ProjectsLocationsOperationsService) Get(projectsId string, locationsId string, operationsId string) *ProjectsLocationsOperationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsOperationsService.Get)
    *   [func (r *ProjectsLocationsOperationsService) List(projectsId string, locationsId string) *ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsOperationsService.List)

*   [type ProjectsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsService)
*       *   [func NewProjectsLocationsService(s *APIService) *ProjectsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#NewProjectsLocationsService)

*       *   [func (r *ProjectsLocationsService) Get(projectsId string, locationsId string) *ProjectsLocationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsService.Get)
    *   [func (r *ProjectsLocationsService) List(projectsId string) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsService.List)

*   [type ProjectsMetadata](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsMetadata)
*       *   [func (s ProjectsMetadata) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsMetadata.MarshalJSON)

*   [type ProjectsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsService)
*       *   [func NewProjectsService(s *APIService) *ProjectsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#NewProjectsService)

*   [type Reasons](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#Reasons)
*       *   [func (s Reasons) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#Reasons.MarshalJSON)

*   [type ResourceEvent](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ResourceEvent)
*       *   [func (s ResourceEvent) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ResourceEvent.MarshalJSON)

*   [type ResourceRecord](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ResourceRecord)
*       *   [func (s ResourceRecord) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ResourceRecord.MarshalJSON)

*   [type SslSettings](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#SslSettings)
*       *   [func (s SslSettings) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#SslSettings.MarshalJSON)

*   [type Status](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#Status)
*       *   [func (s Status) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#Status.MarshalJSON)

[View Source](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L105)

const (
	AppengineAdminScope = "https://www.googleapis.com/auth/appengine.admin"

	
	CloudPlatformScope = "https://www.googleapis.com/auth/cloud-platform"

	
	CloudPlatformReadOnlyScope = "https://www.googleapis.com/auth/cloud-platform.read-only"
)

OAuth2 scopes used by this API.

This section is empty.

This section is empty.

type APIService struct {
 BasePath [string](https://pkg.go.dev/builtin#string)  UserAgent [string](https://pkg.go.dev/builtin#string) 
 Apps *[AppsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsService)
 Projects *[ProjectsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsService)	
}

New creates a new APIService. It uses the provided http.Client for requests.

Deprecated: please use NewService instead. To provide a custom HTTP client, use option.WithHTTPClient. If you are using google.golang.org/api/googleapis/transport.APIKey, use option.WithAPIKey with NewService instead.

NewService creates a new APIService.

type AppsAuthorizedCertificatesCreateCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "appengine.apps.authorizedCertificates.create" call. Any non-2xx status code is an error. Response headers are in either *AuthorizedCertificate.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AppsAuthorizedCertificatesDeleteCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "appengine.apps.authorizedCertificates.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AppsAuthorizedCertificatesGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "appengine.apps.authorizedCertificates.get" call. Any non-2xx status code is an error. Response headers are in either *AuthorizedCertificate.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

View sets the optional parameter "view": Controls the set of fields returned in the GET response.

Possible values:

"BASIC_CERTIFICATE" - Basic certificate information, including applicable

domains and expiration date.

"FULL_CERTIFICATE" - The information from BASIC_CERTIFICATE, plus detailed

information on the domain mappings that have this certificate mapped.

type AppsAuthorizedCertificatesListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "appengine.apps.authorizedCertificates.list" call. Any non-2xx status code is an error. Response headers are in either *ListAuthorizedCertificatesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": Maximum results to return per page.

PageToken sets the optional parameter "pageToken": Continuation token for fetching the next page of results.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

View sets the optional parameter "view": Controls the set of fields returned in the LIST response.

Possible values:

"BASIC_CERTIFICATE" - Basic certificate information, including applicable

domains and expiration date.

"FULL_CERTIFICATE" - The information from BASIC_CERTIFICATE, plus detailed

information on the domain mappings that have this certificate mapped.

type AppsAuthorizedCertificatesPatchCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "appengine.apps.authorizedCertificates.patch" call. Any non-2xx status code is an error. Response headers are in either *AuthorizedCertificate.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

UpdateMask sets the optional parameter "updateMask": Standard field mask for the set of fields to be updated. Updates are only supported on the certificate_raw_data and display_name fields.

type AppsAuthorizedCertificatesService struct {
	
}

func NewAppsAuthorizedCertificatesService(s *[APIService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#APIService)) *[AppsAuthorizedCertificatesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesService)

Create: Uploads the specified SSL certificate.

*   appsId: Part of `parent`. Name of the parent Application resource. Example: apps/myapp.

Delete: Deletes the specified SSL certificate.

*   appsId: Part of `name`. Name of the resource to delete. Example: apps/myapp/authorizedCertificates/12345.
*   authorizedCertificatesId: Part of `name`. See documentation of `appsId`.

Get: Gets the specified SSL certificate.

*   appsId: Part of `name`. Name of the resource requested. Example: apps/myapp/authorizedCertificates/12345.
*   authorizedCertificatesId: Part of `name`. See documentation of `appsId`.

List: Lists all SSL certificates the user is authorized to administer.

*   appsId: Part of `parent`. Name of the parent Application resource. Example: apps/myapp.

Patch: Updates the specified SSL certificate. To renew a certificate and maintain its existing domain mappings, update certificate_data with a new certificate. The new certificate must be applicable to the same domains as the original certificate. The certificate display_name may also be updated.

*   appsId: Part of `name`. Name of the resource to update. Example: apps/myapp/authorizedCertificates/12345.
*   authorizedCertificatesId: Part of `name`. See documentation of `appsId`.

#### type [AppsAuthorizedDomainsListCall](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2089)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedDomainsListCall "Go to AppsAuthorizedDomainsListCall")

type AppsAuthorizedDomainsListCall struct {
	
}

#### func (*AppsAuthorizedDomainsListCall) [Context](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2139)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedDomainsListCall.Context "Go to AppsAuthorizedDomainsListCall.Context")

Context sets the context to be used in this call's Do method.

#### func (*AppsAuthorizedDomainsListCall) [Do](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2180)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedDomainsListCall.Do "Go to AppsAuthorizedDomainsListCall.Do")

Do executes the "appengine.apps.authorizedDomains.list" call. Any non-2xx status code is an error. Response headers are in either *ListAuthorizedDomainsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

#### func (*AppsAuthorizedDomainsListCall) [Header](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2146)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedDomainsListCall.Header "Go to AppsAuthorizedDomainsListCall.Header")

Header returns a http.Header that can be modified by the caller to add headers to the request.

#### func (*AppsAuthorizedDomainsListCall) [IfNoneMatch](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2133)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedDomainsListCall.IfNoneMatch "Go to AppsAuthorizedDomainsListCall.IfNoneMatch")

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

#### func (*AppsAuthorizedDomainsListCall) [PageSize](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2110)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedDomainsListCall.PageSize "Go to AppsAuthorizedDomainsListCall.PageSize")

PageSize sets the optional parameter "pageSize": Maximum results to return per page.

#### func (*AppsAuthorizedDomainsListCall) [PageToken](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2117)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedDomainsListCall.PageToken "Go to AppsAuthorizedDomainsListCall.PageToken")

PageToken sets the optional parameter "pageToken": Continuation token for fetching the next page of results.

#### func (*AppsAuthorizedDomainsListCall) [Pages](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2217)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedDomainsListCall.Pages "Go to AppsAuthorizedDomainsListCall.Pages")

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

#### type [AppsAuthorizedDomainsService](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L212)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedDomainsService "Go to AppsAuthorizedDomainsService")

type AppsAuthorizedDomainsService struct {
	
}

#### func (*AppsAuthorizedDomainsService) [List](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2102)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedDomainsService.List "Go to AppsAuthorizedDomainsService.List")

List: Lists all domains the user is authorized to administer.

*   appsId: Part of `parent`. Name of the parent Application resource. Example: apps/myapp.

#### type [AppsDomainMappingsCreateCall](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2235)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsCreateCall "Go to AppsDomainMappingsCreateCall")

type AppsDomainMappingsCreateCall struct {
	
}

#### func (*AppsDomainMappingsCreateCall) [Context](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2301)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsCreateCall.Context "Go to AppsDomainMappingsCreateCall.Context")

Context sets the context to be used in this call's Do method.

#### func (*AppsDomainMappingsCreateCall) [Do](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2342)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsCreateCall.Do "Go to AppsDomainMappingsCreateCall.Do")

Do executes the "appengine.apps.domainMappings.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

#### func (*AppsDomainMappingsCreateCall) [Header](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2308)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsCreateCall.Header "Go to AppsDomainMappingsCreateCall.Header")

Header returns a http.Header that can be modified by the caller to add headers to the request.

#### func (*AppsDomainMappingsCreateCall) [NoManagedCertificate](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2262)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsCreateCall.NoManagedCertificate "Go to AppsDomainMappingsCreateCall.NoManagedCertificate")

func (c *[AppsDomainMappingsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsCreateCall)) NoManagedCertificate(noManagedCertificate [bool](https://pkg.go.dev/builtin#bool)) *[AppsDomainMappingsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsCreateCall)

NoManagedCertificate sets the optional parameter "noManagedCertificate": Whether a managed certificate should be provided by App Engine. If true, a certificate ID must be manaually set in the DomainMapping resource to configure SSL for this domain. If false, a managed certificate will be provisioned and a certificate ID will be automatically populated.

#### func (*AppsDomainMappingsCreateCall) [OverrideStrategy](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2287)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsCreateCall.OverrideStrategy "Go to AppsDomainMappingsCreateCall.OverrideStrategy")

OverrideStrategy sets the optional parameter "overrideStrategy": Whether the domain creation should override any existing mappings for this domain. By default, overrides are rejected.

Possible values:

"UNSPECIFIED_DOMAIN_OVERRIDE_STRATEGY" - Strategy unspecified. Defaults to

STRICT.

"STRICT" - Overrides not allowed. If a mapping already exists for the

specified domain, the request will return an ALREADY_EXISTS (409).

"OVERRIDE" - Overrides allowed. If a mapping already exists for the

specified domain, the request will overwrite it. Note that this might stop another Google product from serving. For example, if the domain is mapped to another App Engine application, that app will no longer serve from that domain.

#### type [AppsDomainMappingsDeleteCall](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2376)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsDeleteCall "Go to AppsDomainMappingsDeleteCall")

type AppsDomainMappingsDeleteCall struct {
	
}

#### func (*AppsDomainMappingsDeleteCall) [Context](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2408)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsDeleteCall.Context "Go to AppsDomainMappingsDeleteCall.Context")

Context sets the context to be used in this call's Do method.

#### func (*AppsDomainMappingsDeleteCall) [Do](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2446)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsDeleteCall.Do "Go to AppsDomainMappingsDeleteCall.Do")

Do executes the "appengine.apps.domainMappings.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

#### func (*AppsDomainMappingsDeleteCall) [Header](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2415)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsDeleteCall.Header "Go to AppsDomainMappingsDeleteCall.Header")

Header returns a http.Header that can be modified by the caller to add headers to the request.

#### type [AppsDomainMappingsGetCall](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2480)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsGetCall "Go to AppsDomainMappingsGetCall")

type AppsDomainMappingsGetCall struct {
	
}

#### func (*AppsDomainMappingsGetCall) [Context](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2519)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsGetCall.Context "Go to AppsDomainMappingsGetCall.Context")

Context sets the context to be used in this call's Do method.

#### func (*AppsDomainMappingsGetCall) [Do](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2560)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsGetCall.Do "Go to AppsDomainMappingsGetCall.Do")

Do executes the "appengine.apps.domainMappings.get" call. Any non-2xx status code is an error. Response headers are in either *DomainMapping.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

#### func (*AppsDomainMappingsGetCall) [Header](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2526)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsGetCall.Header "Go to AppsDomainMappingsGetCall.Header")

Header returns a http.Header that can be modified by the caller to add headers to the request.

#### func (*AppsDomainMappingsGetCall) [IfNoneMatch](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2513)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsGetCall.IfNoneMatch "Go to AppsDomainMappingsGetCall.IfNoneMatch")

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

#### type [AppsDomainMappingsListCall](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2594)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsListCall "Go to AppsDomainMappingsListCall")

type AppsDomainMappingsListCall struct {
	
}

#### func (*AppsDomainMappingsListCall) [Context](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2644)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsListCall.Context "Go to AppsDomainMappingsListCall.Context")

Context sets the context to be used in this call's Do method.

#### func (*AppsDomainMappingsListCall) [Do](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2685)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsListCall.Do "Go to AppsDomainMappingsListCall.Do")

Do executes the "appengine.apps.domainMappings.list" call. Any non-2xx status code is an error. Response headers are in either *ListDomainMappingsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

#### func (*AppsDomainMappingsListCall) [Header](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2651)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsListCall.Header "Go to AppsDomainMappingsListCall.Header")

Header returns a http.Header that can be modified by the caller to add headers to the request.

#### func (*AppsDomainMappingsListCall) [IfNoneMatch](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2638)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsListCall.IfNoneMatch "Go to AppsDomainMappingsListCall.IfNoneMatch")

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

#### func (*AppsDomainMappingsListCall) [PageSize](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2615)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsListCall.PageSize "Go to AppsDomainMappingsListCall.PageSize")

PageSize sets the optional parameter "pageSize": Maximum results to return per page.

#### func (*AppsDomainMappingsListCall) [PageToken](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2622)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsListCall.PageToken "Go to AppsDomainMappingsListCall.PageToken")

PageToken sets the optional parameter "pageToken": Continuation token for fetching the next page of results.

#### func (*AppsDomainMappingsListCall) [Pages](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2722)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsListCall.Pages "Go to AppsDomainMappingsListCall.Pages")

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

#### type [AppsDomainMappingsPatchCall](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2740)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsPatchCall "Go to AppsDomainMappingsPatchCall")

type AppsDomainMappingsPatchCall struct {
	
}

#### func (*AppsDomainMappingsPatchCall) [Context](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2793)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsPatchCall.Context "Go to AppsDomainMappingsPatchCall.Context")

Context sets the context to be used in this call's Do method.

#### func (*AppsDomainMappingsPatchCall) [Do](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2835)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsPatchCall.Do "Go to AppsDomainMappingsPatchCall.Do")

Do executes the "appengine.apps.domainMappings.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

#### func (*AppsDomainMappingsPatchCall) [Header](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2800)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsPatchCall.Header "Go to AppsDomainMappingsPatchCall.Header")

Header returns a http.Header that can be modified by the caller to add headers to the request.

#### func (*AppsDomainMappingsPatchCall) [NoManagedCertificate](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2772)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsPatchCall.NoManagedCertificate "Go to AppsDomainMappingsPatchCall.NoManagedCertificate")

func (c *[AppsDomainMappingsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsPatchCall)) NoManagedCertificate(noManagedCertificate [bool](https://pkg.go.dev/builtin#bool)) *[AppsDomainMappingsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsPatchCall)

NoManagedCertificate sets the optional parameter "noManagedCertificate": Whether a managed certificate should be provided by App Engine. If true, a certificate ID must be manually set in the DomainMapping resource to configure SSL for this domain. If false, a managed certificate will be provisioned and a certificate ID will be automatically populated. Only applicable if ssl_settings.certificate_id is specified in the update mask.

#### func (*AppsDomainMappingsPatchCall) [UpdateMask](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2779)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsPatchCall.UpdateMask "Go to AppsDomainMappingsPatchCall.UpdateMask")

UpdateMask sets the optional parameter "updateMask": Required. Standard field mask for the set of fields to be updated.

#### type [AppsDomainMappingsService](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L221)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsService "Go to AppsDomainMappingsService")

type AppsDomainMappingsService struct {
	
}

#### func (*AppsDomainMappingsService) [Create](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2250)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsService.Create "Go to AppsDomainMappingsService.Create")

Create: Maps a domain to an application. A user must be authorized to administer a domain in order to map it to an application. For a list of available authorized domains, see AuthorizedDomains.ListAuthorizedDomains.

*   appsId: Part of `parent`. Name of the parent Application resource. Example: apps/myapp.

#### func (*AppsDomainMappingsService) [Delete](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2392)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsService.Delete "Go to AppsDomainMappingsService.Delete")

Delete: Deletes the specified domain mapping. A user must be authorized to administer the associated domain in order to delete a DomainMapping resource.

*   appsId: Part of `name`. Name of the resource to delete. Example: apps/myapp/domainMappings/example.com.
*   domainMappingsId: Part of `name`. See documentation of `appsId`.

#### func (*AppsDomainMappingsService) [Get](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2495)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsService.Get "Go to AppsDomainMappingsService.Get")

Get: Gets the specified domain mapping.

*   appsId: Part of `name`. Name of the resource requested. Example: apps/myapp/domainMappings/example.com.
*   domainMappingsId: Part of `name`. See documentation of `appsId`.

#### func (*AppsDomainMappingsService) [List](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2607)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsService.List "Go to AppsDomainMappingsService.List")

List: Lists the domain mappings on an application.

*   appsId: Part of `parent`. Name of the parent Application resource. Example: apps/myapp.

#### func (*AppsDomainMappingsService) [Patch](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L2758)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsService.Patch "Go to AppsDomainMappingsService.Patch")

Patch: Updates the specified domain mapping. To map an SSL certificate to a domain mapping, update certificate_id to point to an AuthorizedCertificate resource. A user must be authorized to administer the associated domain in order to update a DomainMapping resource.

*   appsId: Part of `name`. Name of the resource to update. Example: apps/myapp/domainMappings/example.com.
*   domainMappingsId: Part of `name`. See documentation of `appsId`.

type AppsLocationsGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "appengine.apps.locations.get" call. Any non-2xx status code is an error. Response headers are in either *Location.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AppsLocationsListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "appengine.apps.locations.list" call. Any non-2xx status code is an error. Response headers are in either *ListLocationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (c *[AppsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsLocationsListCall)) ExtraLocationTypes(extraLocationTypes ...[string](https://pkg.go.dev/builtin#string)) *[AppsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsLocationsListCall)

ExtraLocationTypes sets the optional parameter "extraLocationTypes": Do not use this field. It is unsupported and is ignored unless explicitly documented otherwise. This is primarily for internal usage.

Filter sets the optional parameter "filter": A filter to narrow down results to a preferred subset. The filtering language accepts strings like "displayName=tokyo", and is documented in more detail in AIP-160 ([https://google.aip.dev/160](https://google.aip.dev/160)).

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": The maximum number of results to return. If not set, the service selects a default.

PageToken sets the optional parameter "pageToken": A page token received from the next_page_token field in the response. Send that page token to receive the subsequent page.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AppsLocationsService struct {
	
}

func NewAppsLocationsService(s *[APIService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#APIService)) *[AppsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsLocationsService)

Get: Gets information about a location.

- appsId: Part of `name`. Resource name for the location. - locationsId: Part of `name`. See documentation of `appsId`.

List: Lists information about the supported locations for this service. This method can be called in two ways: List all public locations: Use the path GET /v1/locations. List project-visible locations: Use the path GET /v1/projects/{project_id}/locations. This may include public locations as well as private or other locations specifically visible to the project.

*   appsId: Part of `name`. The resource that owns the locations collection, if applicable.

type AppsOperationsGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "appengine.apps.operations.get" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AppsOperationsListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "appengine.apps.operations.list" call. Any non-2xx status code is an error. Response headers are in either *ListOperationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Filter sets the optional parameter "filter": The standard list filter.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": The standard list page size.

PageToken sets the optional parameter "pageToken": The standard list page token.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (c *[AppsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsOperationsListCall)) ReturnPartialSuccess(returnPartialSuccess [bool](https://pkg.go.dev/builtin#bool)) *[AppsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsOperationsListCall)

ReturnPartialSuccess sets the optional parameter "returnPartialSuccess": When set to true, operations that are reachable are returned as normal, and those that are unreachable are returned in the ListOperationsResponse.unreachable field.This can only be true when reading across collections. For example, when parent is set to "projects/example/locations/-".This field is not supported by default and will result in an UNIMPLEMENTED error if set unless explicitly documented otherwise in service or product specific documentation.

type AppsOperationsService struct {
	
}

func NewAppsOperationsService(s *[APIService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#APIService)) *[AppsOperationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsOperationsService)

Get: Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

- appsId: Part of `name`. The name of the operation resource. - operationsId: Part of `name`. See documentation of `appsId`.

List: Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns UNIMPLEMENTED.

- appsId: Part of `name`. The name of the operation's parent resource.

type AppsService struct {
 AuthorizedCertificates *[AppsAuthorizedCertificatesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedCertificatesService)
 AuthorizedDomains *[AppsAuthorizedDomainsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsAuthorizedDomainsService)
 DomainMappings *[AppsDomainMappingsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsDomainMappingsService)
 Locations *[AppsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsLocationsService)
 Operations *[AppsOperationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsOperationsService)	
}

func NewAppsService(s *[APIService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#APIService)) *[AppsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AppsService)

type AuthorizedCertificate struct {
	
	CertificateRawData *[CertificateRawData](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#CertificateRawData) `json:"certificateRawData,omitempty"`
	
	DisplayName [string](https://pkg.go.dev/builtin#string) `json:"displayName,omitempty"`
	
	
	
	
	DomainMappingsCount [int64](https://pkg.go.dev/builtin#int64) `json:"domainMappingsCount,omitempty"`
	
	
	DomainNames [][string](https://pkg.go.dev/builtin#string) `json:"domainNames,omitempty"`
	
	
	
	ExpireTime [string](https://pkg.go.dev/builtin#string) `json:"expireTime,omitempty"`
	
	
	Id [string](https://pkg.go.dev/builtin#string) `json:"id,omitempty"`
	
	
	
	
	ManagedCertificate *[ManagedCertificate](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ManagedCertificate) `json:"managedCertificate,omitempty"`
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	
	
	
	
	
	
	VisibleDomainMappings [][string](https://pkg.go.dev/builtin#string) `json:"visibleDomainMappings,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

AuthorizedCertificate: An SSL certificate that a user has been authorized to administer. A user is authorized to administer any certificate that applies to one of their authorized domains.

type CertificateRawData struct {
	
	
	
	PrivateKey [string](https://pkg.go.dev/builtin#string) `json:"privateKey,omitempty"`
	
	
	PublicCertificate [string](https://pkg.go.dev/builtin#string) `json:"publicCertificate,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

CertificateRawData: An SSL certificate obtained from a certificate authority.

type ContainerState struct {
 CurrentReasons *[Reasons](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#Reasons) `json:"currentReasons,omitempty"` 	
	
	
	
	
	
	
	
	PreviousReasons *[Reasons](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#Reasons) `json:"previousReasons,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	State [string](https://pkg.go.dev/builtin#string) `json:"state,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ContainerState: ContainerState contains the externally-visible container state that is used to communicate the state and reasoning for that state to the CLH. This data is not persisted by CCFE, but is instead derived from CCFE's internal representation of the container state.

type CreateVersionMetadataV1 struct {
	
	CloudBuildId [string](https://pkg.go.dev/builtin#string) `json:"cloudBuildId,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

CreateVersionMetadataV1: Metadata for the given google.longrunning.Operation during a google.appengine.v1.CreateVersionRequest.

type CreateVersionMetadataV1Alpha struct {
	
	CloudBuildId [string](https://pkg.go.dev/builtin#string) `json:"cloudBuildId,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

CreateVersionMetadataV1Alpha: Metadata for the given google.longrunning.Operation during a google.appengine.v1alpha.CreateVersionRequest.

type CreateVersionMetadataV1Beta struct {
	
	CloudBuildId [string](https://pkg.go.dev/builtin#string) `json:"cloudBuildId,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

CreateVersionMetadataV1Beta: Metadata for the given google.longrunning.Operation during a google.appengine.v1beta.CreateVersionRequest.

#### type [DomainMapping](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L584)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#DomainMapping "Go to DomainMapping")

type DomainMapping struct {
	
	Id [string](https://pkg.go.dev/builtin#string) `json:"id,omitempty"`
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	
	
	ResourceRecords []*[ResourceRecord](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ResourceRecord) `json:"resourceRecords,omitempty"`
	
	SslSettings *[SslSettings](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#SslSettings) `json:"sslSettings,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

DomainMapping: A domain serving an App Engine application.

Empty: A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }

type GceTag struct {
	
	
	Parent [][string](https://pkg.go.dev/builtin#string) `json:"parent,omitempty"`
	Tag [string](https://pkg.go.dev/builtin#string) `json:"tag,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

GceTag: For use only by GCE. GceTag is a wrapper around the GCE administrative tag with parent info.

type GoogleAppengineV1betaLocationMetadata struct {
	
	FlexibleEnvironmentAvailable [bool](https://pkg.go.dev/builtin#bool) `json:"flexibleEnvironmentAvailable,omitempty"`
	
	
	SearchApiAvailable [bool](https://pkg.go.dev/builtin#bool) `json:"searchApiAvailable,omitempty"`
	
	StandardEnvironmentAvailable [bool](https://pkg.go.dev/builtin#bool) `json:"standardEnvironmentAvailable,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

GoogleAppengineV1betaLocationMetadata: Metadata for the given google.cloud.location.Location.

type ListAuthorizedCertificatesResponse struct {
	Certificates []*[AuthorizedCertificate](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AuthorizedCertificate) `json:"certificates,omitempty"`
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListAuthorizedCertificatesResponse: Response message for AuthorizedCertificates.ListAuthorizedCertificates.

#### type [ListAuthorizedDomainsResponse](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L717)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ListAuthorizedDomainsResponse "Go to ListAuthorizedDomainsResponse")

type ListAuthorizedDomainsResponse struct {
	Domains []*[AuthorizedDomain](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#AuthorizedDomain) `json:"domains,omitempty"`
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListAuthorizedDomainsResponse: Response message for AuthorizedDomains.ListAuthorizedDomains.

#### type [ListDomainMappingsResponse](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L745)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ListDomainMappingsResponse "Go to ListDomainMappingsResponse")

type ListDomainMappingsResponse struct {
	DomainMappings []*[DomainMapping](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#DomainMapping) `json:"domainMappings,omitempty"`
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListDomainMappingsResponse: Response message for DomainMappings.ListDomainMappings.

type ListLocationsResponse struct {
	
	Locations []*[Location](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#Location) `json:"locations,omitempty"`
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListLocationsResponse: The response message for Locations.ListLocations.

type ListOperationsResponse struct {
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`
	
	Operations []*[Operation](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#Operation) `json:"operations,omitempty"`
	
	
	
	Unreachable [][string](https://pkg.go.dev/builtin#string) `json:"unreachable,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListOperationsResponse: The response message for Operations.ListOperations.

Location: A resource that represents a Google Cloud location.

type LocationMetadata struct {
	
	FlexibleEnvironmentAvailable [bool](https://pkg.go.dev/builtin#bool) `json:"flexibleEnvironmentAvailable,omitempty"`
	
	
	SearchApiAvailable [bool](https://pkg.go.dev/builtin#bool) `json:"searchApiAvailable,omitempty"`
	
	StandardEnvironmentAvailable [bool](https://pkg.go.dev/builtin#bool) `json:"standardEnvironmentAvailable,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

LocationMetadata: Metadata for the given google.cloud.location.Location.

type ManagedCertificate struct {
	
	
	
	LastRenewalTime [string](https://pkg.go.dev/builtin#string) `json:"lastRenewalTime,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	Status [string](https://pkg.go.dev/builtin#string) `json:"status,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ManagedCertificate: A certificate managed by App Engine.

Operation: This resource represents a long-running operation that is the result of a network API call.

type OperationMetadataV1 struct {
 CreateVersionMetadata *[CreateVersionMetadataV1](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#CreateVersionMetadataV1) `json:"createVersionMetadata,omitempty"` 	EndTime [string](https://pkg.go.dev/builtin#string) `json:"endTime,omitempty"`
	
	EphemeralMessage [string](https://pkg.go.dev/builtin#string) `json:"ephemeralMessage,omitempty"`
	InsertTime [string](https://pkg.go.dev/builtin#string) `json:"insertTime,omitempty"`
	
	Method [string](https://pkg.go.dev/builtin#string) `json:"method,omitempty"`
	
	Target [string](https://pkg.go.dev/builtin#string) `json:"target,omitempty"`
	User [string](https://pkg.go.dev/builtin#string) `json:"user,omitempty"`
	Warning [][string](https://pkg.go.dev/builtin#string) `json:"warning,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

OperationMetadataV1: Metadata for the given google.longrunning.Operation.

type OperationMetadataV1Alpha struct {
 CreateVersionMetadata *[CreateVersionMetadataV1Alpha](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#CreateVersionMetadataV1Alpha) `json:"createVersionMetadata,omitempty"` 	EndTime [string](https://pkg.go.dev/builtin#string) `json:"endTime,omitempty"`
	
	EphemeralMessage [string](https://pkg.go.dev/builtin#string) `json:"ephemeralMessage,omitempty"`
	InsertTime [string](https://pkg.go.dev/builtin#string) `json:"insertTime,omitempty"`
	
	Method [string](https://pkg.go.dev/builtin#string) `json:"method,omitempty"`
	
	Target [string](https://pkg.go.dev/builtin#string) `json:"target,omitempty"`
	User [string](https://pkg.go.dev/builtin#string) `json:"user,omitempty"`
	Warning [][string](https://pkg.go.dev/builtin#string) `json:"warning,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

OperationMetadataV1Alpha: Metadata for the given google.longrunning.Operation.

type OperationMetadataV1Beta struct {
 CreateVersionMetadata *[CreateVersionMetadataV1Beta](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#CreateVersionMetadataV1Beta) `json:"createVersionMetadata,omitempty"` 	EndTime [string](https://pkg.go.dev/builtin#string) `json:"endTime,omitempty"`
	
	EphemeralMessage [string](https://pkg.go.dev/builtin#string) `json:"ephemeralMessage,omitempty"`
	InsertTime [string](https://pkg.go.dev/builtin#string) `json:"insertTime,omitempty"`
	
	Method [string](https://pkg.go.dev/builtin#string) `json:"method,omitempty"`
	
	Target [string](https://pkg.go.dev/builtin#string) `json:"target,omitempty"`
	User [string](https://pkg.go.dev/builtin#string) `json:"user,omitempty"`
	Warning [][string](https://pkg.go.dev/builtin#string) `json:"warning,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

OperationMetadataV1Beta: Metadata for the given google.longrunning.Operation.

type ProjectEvent struct {
	
	EventId [string](https://pkg.go.dev/builtin#string) `json:"eventId,omitempty"`
	
	
	
	
	
	
	
	Phase [string](https://pkg.go.dev/builtin#string) `json:"phase,omitempty"`
	ProjectMetadata *[ProjectsMetadata](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsMetadata) `json:"projectMetadata,omitempty"`
	State *[ContainerState](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ContainerState) `json:"state,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ProjectEvent: The request sent to CLHs during project events.

type ProjectsLocationsApplicationsAuthorizedCertificatesCreateCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "appengine.projects.locations.applications.authorizedCertificates.create" call. Any non-2xx status code is an error. Response headers are in either *AuthorizedCertificate.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApplicationsAuthorizedCertificatesDeleteCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "appengine.projects.locations.applications.authorizedCertificates.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApplicationsAuthorizedCertificatesGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "appengine.projects.locations.applications.authorizedCertificates.get" call. Any non-2xx status code is an error. Response headers are in either *AuthorizedCertificate.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

View sets the optional parameter "view": Controls the set of fields returned in the GET response.

Possible values:

"BASIC_CERTIFICATE" - Basic certificate information, including applicable

domains and expiration date.

"FULL_CERTIFICATE" - The information from BASIC_CERTIFICATE, plus detailed

information on the domain mappings that have this certificate mapped.

type ProjectsLocationsApplicationsAuthorizedCertificatesListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "appengine.projects.locations.applications.authorizedCertificates.list" call. Any non-2xx status code is an error. Response headers are in either *ListAuthorizedCertificatesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": Maximum results to return per page.

PageToken sets the optional parameter "pageToken": Continuation token for fetching the next page of results.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

View sets the optional parameter "view": Controls the set of fields returned in the LIST response.

Possible values:

"BASIC_CERTIFICATE" - Basic certificate information, including applicable

domains and expiration date.

"FULL_CERTIFICATE" - The information from BASIC_CERTIFICATE, plus detailed

information on the domain mappings that have this certificate mapped.

type ProjectsLocationsApplicationsAuthorizedCertificatesPatchCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "appengine.projects.locations.applications.authorizedCertificates.patch" call. Any non-2xx status code is an error. Response headers are in either *AuthorizedCertificate.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

UpdateMask sets the optional parameter "updateMask": Standard field mask for the set of fields to be updated. Updates are only supported on the certificate_raw_data and display_name fields.

type ProjectsLocationsApplicationsAuthorizedCertificatesService struct {
	
}

func NewProjectsLocationsApplicationsAuthorizedCertificatesService(s *[APIService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#APIService)) *[ProjectsLocationsApplicationsAuthorizedCertificatesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesService)

Create: Uploads the specified SSL certificate.

*   applicationsId: Part of `parent`. See documentation of `projectsId`.
*   locationsId: Part of `parent`. See documentation of `projectsId`.
*   projectsId: Part of `parent`. Name of the parent Application resource. Example: apps/myapp.

Delete: Deletes the specified SSL certificate.

*   applicationsId: Part of `name`. See documentation of `projectsId`.
*   authorizedCertificatesId: Part of `name`. See documentation of `projectsId`.
*   locationsId: Part of `name`. See documentation of `projectsId`.
*   projectsId: Part of `name`. Name of the resource to delete. Example: apps/myapp/authorizedCertificates/12345.

Get: Gets the specified SSL certificate.

*   applicationsId: Part of `name`. See documentation of `projectsId`.
*   authorizedCertificatesId: Part of `name`. See documentation of `projectsId`.
*   locationsId: Part of `name`. See documentation of `projectsId`.
*   projectsId: Part of `name`. Name of the resource requested. Example: apps/myapp/authorizedCertificates/12345.

List: Lists all SSL certificates the user is authorized to administer.

*   applicationsId: Part of `parent`. See documentation of `projectsId`.
*   locationsId: Part of `parent`. See documentation of `projectsId`.
*   projectsId: Part of `parent`. Name of the parent Application resource. Example: apps/myapp.

Patch: Updates the specified SSL certificate. To renew a certificate and maintain its existing domain mappings, update certificate_data with a new certificate. The new certificate must be applicable to the same domains as the original certificate. The certificate display_name may also be updated.

*   applicationsId: Part of `name`. See documentation of `projectsId`.
*   authorizedCertificatesId: Part of `name`. See documentation of `projectsId`.
*   locationsId: Part of `name`. See documentation of `projectsId`.
*   projectsId: Part of `name`. Name of the resource to update. Example: apps/myapp/authorizedCertificates/12345.

#### type [ProjectsLocationsApplicationsAuthorizedDomainsListCall](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4376)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedDomainsListCall "Go to ProjectsLocationsApplicationsAuthorizedDomainsListCall")added in v0.168.0

type ProjectsLocationsApplicationsAuthorizedDomainsListCall struct {
	
}

#### func (*ProjectsLocationsApplicationsAuthorizedDomainsListCall) [Context](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4432)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedDomainsListCall.Context "Go to ProjectsLocationsApplicationsAuthorizedDomainsListCall.Context")added in v0.168.0

Context sets the context to be used in this call's Do method.

#### func (*ProjectsLocationsApplicationsAuthorizedDomainsListCall) [Do](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4475)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedDomainsListCall.Do "Go to ProjectsLocationsApplicationsAuthorizedDomainsListCall.Do")added in v0.168.0

Do executes the "appengine.projects.locations.applications.authorizedDomains.list" call. Any non-2xx status code is an error. Response headers are in either *ListAuthorizedDomainsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

#### func (*ProjectsLocationsApplicationsAuthorizedDomainsListCall) [Header](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4439)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedDomainsListCall.Header "Go to ProjectsLocationsApplicationsAuthorizedDomainsListCall.Header")added in v0.168.0

Header returns a http.Header that can be modified by the caller to add headers to the request.

#### func (*ProjectsLocationsApplicationsAuthorizedDomainsListCall) [IfNoneMatch](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4426)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedDomainsListCall.IfNoneMatch "Go to ProjectsLocationsApplicationsAuthorizedDomainsListCall.IfNoneMatch")added in v0.168.0

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

#### func (*ProjectsLocationsApplicationsAuthorizedDomainsListCall) [PageSize](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4403)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedDomainsListCall.PageSize "Go to ProjectsLocationsApplicationsAuthorizedDomainsListCall.PageSize")added in v0.168.0

PageSize sets the optional parameter "pageSize": Maximum results to return per page.

#### func (*ProjectsLocationsApplicationsAuthorizedDomainsListCall) [PageToken](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4410)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedDomainsListCall.PageToken "Go to ProjectsLocationsApplicationsAuthorizedDomainsListCall.PageToken")added in v0.168.0

PageToken sets the optional parameter "pageToken": Continuation token for fetching the next page of results.

#### func (*ProjectsLocationsApplicationsAuthorizedDomainsListCall) [Pages](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4512)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedDomainsListCall.Pages "Go to ProjectsLocationsApplicationsAuthorizedDomainsListCall.Pages")added in v0.168.0

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

#### type [ProjectsLocationsApplicationsAuthorizedDomainsService](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L302)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedDomainsService "Go to ProjectsLocationsApplicationsAuthorizedDomainsService")added in v0.168.0

type ProjectsLocationsApplicationsAuthorizedDomainsService struct {
	
}

#### func (*ProjectsLocationsApplicationsAuthorizedDomainsService) [List](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4393)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedDomainsService.List "Go to ProjectsLocationsApplicationsAuthorizedDomainsService.List")added in v0.168.0

List: Lists all domains the user is authorized to administer.

*   applicationsId: Part of `parent`. See documentation of `projectsId`.
*   locationsId: Part of `parent`. See documentation of `projectsId`.
*   projectsId: Part of `parent`. Name of the parent Application resource. Example: apps/myapp.

#### type [ProjectsLocationsApplicationsDomainMappingsCreateCall](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4530)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsCreateCall "Go to ProjectsLocationsApplicationsDomainMappingsCreateCall")added in v0.239.0

type ProjectsLocationsApplicationsDomainMappingsCreateCall struct {
	
}

#### func (*ProjectsLocationsApplicationsDomainMappingsCreateCall) [Context](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4602)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsCreateCall.Context "Go to ProjectsLocationsApplicationsDomainMappingsCreateCall.Context")added in v0.239.0

Context sets the context to be used in this call's Do method.

#### func (*ProjectsLocationsApplicationsDomainMappingsCreateCall) [Do](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4645)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsCreateCall.Do "Go to ProjectsLocationsApplicationsDomainMappingsCreateCall.Do")added in v0.239.0

Do executes the "appengine.projects.locations.applications.domainMappings.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

#### func (*ProjectsLocationsApplicationsDomainMappingsCreateCall) [Header](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4609)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsCreateCall.Header "Go to ProjectsLocationsApplicationsDomainMappingsCreateCall.Header")added in v0.239.0

Header returns a http.Header that can be modified by the caller to add headers to the request.

#### func (*ProjectsLocationsApplicationsDomainMappingsCreateCall) [NoManagedCertificate](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4563)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsCreateCall.NoManagedCertificate "Go to ProjectsLocationsApplicationsDomainMappingsCreateCall.NoManagedCertificate")added in v0.239.0

NoManagedCertificate sets the optional parameter "noManagedCertificate": Whether a managed certificate should be provided by App Engine. If true, a certificate ID must be manaually set in the DomainMapping resource to configure SSL for this domain. If false, a managed certificate will be provisioned and a certificate ID will be automatically populated.

#### func (*ProjectsLocationsApplicationsDomainMappingsCreateCall) [OverrideStrategy](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4588)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsCreateCall.OverrideStrategy "Go to ProjectsLocationsApplicationsDomainMappingsCreateCall.OverrideStrategy")added in v0.239.0

OverrideStrategy sets the optional parameter "overrideStrategy": Whether the domain creation should override any existing mappings for this domain. By default, overrides are rejected.

Possible values:

"UNSPECIFIED_DOMAIN_OVERRIDE_STRATEGY" - Strategy unspecified. Defaults to

STRICT.

"STRICT" - Overrides not allowed. If a mapping already exists for the

specified domain, the request will return an ALREADY_EXISTS (409).

"OVERRIDE" - Overrides allowed. If a mapping already exists for the

specified domain, the request will overwrite it. Note that this might stop another Google product from serving. For example, if the domain is mapped to another App Engine application, that app will no longer serve from that domain.

#### type [ProjectsLocationsApplicationsDomainMappingsDeleteCall](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4679)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsDeleteCall "Go to ProjectsLocationsApplicationsDomainMappingsDeleteCall")added in v0.252.0

type ProjectsLocationsApplicationsDomainMappingsDeleteCall struct {
	
}

#### func (*ProjectsLocationsApplicationsDomainMappingsDeleteCall) [Context](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4717)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsDeleteCall.Context "Go to ProjectsLocationsApplicationsDomainMappingsDeleteCall.Context")added in v0.252.0

Context sets the context to be used in this call's Do method.

#### func (*ProjectsLocationsApplicationsDomainMappingsDeleteCall) [Do](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4757)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsDeleteCall.Do "Go to ProjectsLocationsApplicationsDomainMappingsDeleteCall.Do")added in v0.252.0

Do executes the "appengine.projects.locations.applications.domainMappings.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

#### func (*ProjectsLocationsApplicationsDomainMappingsDeleteCall) [Header](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4724)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsDeleteCall.Header "Go to ProjectsLocationsApplicationsDomainMappingsDeleteCall.Header")added in v0.252.0

Header returns a http.Header that can be modified by the caller to add headers to the request.

#### type [ProjectsLocationsApplicationsDomainMappingsGetCall](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4791)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsGetCall "Go to ProjectsLocationsApplicationsDomainMappingsGetCall")added in v0.234.0

type ProjectsLocationsApplicationsDomainMappingsGetCall struct {
	
}

#### func (*ProjectsLocationsApplicationsDomainMappingsGetCall) [Context](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4836)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsGetCall.Context "Go to ProjectsLocationsApplicationsDomainMappingsGetCall.Context")added in v0.234.0

Context sets the context to be used in this call's Do method.

#### func (*ProjectsLocationsApplicationsDomainMappingsGetCall) [Do](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4879)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsGetCall.Do "Go to ProjectsLocationsApplicationsDomainMappingsGetCall.Do")added in v0.234.0

Do executes the "appengine.projects.locations.applications.domainMappings.get" call. Any non-2xx status code is an error. Response headers are in either *DomainMapping.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

#### func (*ProjectsLocationsApplicationsDomainMappingsGetCall) [Header](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4843)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsGetCall.Header "Go to ProjectsLocationsApplicationsDomainMappingsGetCall.Header")added in v0.234.0

Header returns a http.Header that can be modified by the caller to add headers to the request.

#### func (*ProjectsLocationsApplicationsDomainMappingsGetCall) [IfNoneMatch](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4830)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsGetCall.IfNoneMatch "Go to ProjectsLocationsApplicationsDomainMappingsGetCall.IfNoneMatch")added in v0.234.0

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

#### type [ProjectsLocationsApplicationsDomainMappingsListCall](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4913)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsListCall "Go to ProjectsLocationsApplicationsDomainMappingsListCall")added in v0.256.0

type ProjectsLocationsApplicationsDomainMappingsListCall struct {
	
}

#### func (*ProjectsLocationsApplicationsDomainMappingsListCall) [Context](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4969)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsListCall.Context "Go to ProjectsLocationsApplicationsDomainMappingsListCall.Context")added in v0.256.0

Context sets the context to be used in this call's Do method.

#### func (*ProjectsLocationsApplicationsDomainMappingsListCall) [Do](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L5012)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsListCall.Do "Go to ProjectsLocationsApplicationsDomainMappingsListCall.Do")added in v0.256.0

Do executes the "appengine.projects.locations.applications.domainMappings.list" call. Any non-2xx status code is an error. Response headers are in either *ListDomainMappingsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

#### func (*ProjectsLocationsApplicationsDomainMappingsListCall) [Header](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4976)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsListCall.Header "Go to ProjectsLocationsApplicationsDomainMappingsListCall.Header")added in v0.256.0

Header returns a http.Header that can be modified by the caller to add headers to the request.

#### func (*ProjectsLocationsApplicationsDomainMappingsListCall) [IfNoneMatch](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4963)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsListCall.IfNoneMatch "Go to ProjectsLocationsApplicationsDomainMappingsListCall.IfNoneMatch")added in v0.256.0

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

#### func (*ProjectsLocationsApplicationsDomainMappingsListCall) [PageSize](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4940)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsListCall.PageSize "Go to ProjectsLocationsApplicationsDomainMappingsListCall.PageSize")added in v0.256.0

PageSize sets the optional parameter "pageSize": Maximum results to return per page.

#### func (*ProjectsLocationsApplicationsDomainMappingsListCall) [PageToken](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4947)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsListCall.PageToken "Go to ProjectsLocationsApplicationsDomainMappingsListCall.PageToken")added in v0.256.0

PageToken sets the optional parameter "pageToken": Continuation token for fetching the next page of results.

#### func (*ProjectsLocationsApplicationsDomainMappingsListCall) [Pages](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L5049)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsListCall.Pages "Go to ProjectsLocationsApplicationsDomainMappingsListCall.Pages")added in v0.256.0

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

#### type [ProjectsLocationsApplicationsDomainMappingsPatchCall](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L5067)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsPatchCall "Go to ProjectsLocationsApplicationsDomainMappingsPatchCall")added in v0.252.0

type ProjectsLocationsApplicationsDomainMappingsPatchCall struct {
	
}

#### func (*ProjectsLocationsApplicationsDomainMappingsPatchCall) [Context](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L5126)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsPatchCall.Context "Go to ProjectsLocationsApplicationsDomainMappingsPatchCall.Context")added in v0.252.0

Context sets the context to be used in this call's Do method.

#### func (*ProjectsLocationsApplicationsDomainMappingsPatchCall) [Do](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L5170)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsPatchCall.Do "Go to ProjectsLocationsApplicationsDomainMappingsPatchCall.Do")added in v0.252.0

Do executes the "appengine.projects.locations.applications.domainMappings.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

#### func (*ProjectsLocationsApplicationsDomainMappingsPatchCall) [Header](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L5133)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsPatchCall.Header "Go to ProjectsLocationsApplicationsDomainMappingsPatchCall.Header")added in v0.252.0

Header returns a http.Header that can be modified by the caller to add headers to the request.

#### func (*ProjectsLocationsApplicationsDomainMappingsPatchCall) [NoManagedCertificate](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L5105)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsPatchCall.NoManagedCertificate "Go to ProjectsLocationsApplicationsDomainMappingsPatchCall.NoManagedCertificate")added in v0.252.0

NoManagedCertificate sets the optional parameter "noManagedCertificate": Whether a managed certificate should be provided by App Engine. If true, a certificate ID must be manually set in the DomainMapping resource to configure SSL for this domain. If false, a managed certificate will be provisioned and a certificate ID will be automatically populated. Only applicable if ssl_settings.certificate_id is specified in the update mask.

#### func (*ProjectsLocationsApplicationsDomainMappingsPatchCall) [UpdateMask](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L5112)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsPatchCall.UpdateMask "Go to ProjectsLocationsApplicationsDomainMappingsPatchCall.UpdateMask")added in v0.252.0

UpdateMask sets the optional parameter "updateMask": Required. Standard field mask for the set of fields to be updated.

#### type [ProjectsLocationsApplicationsDomainMappingsService](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L311)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsService "Go to ProjectsLocationsApplicationsDomainMappingsService")added in v0.234.0

type ProjectsLocationsApplicationsDomainMappingsService struct {
	
}

#### func (*ProjectsLocationsApplicationsDomainMappingsService) [Create](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4549)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsService.Create "Go to ProjectsLocationsApplicationsDomainMappingsService.Create")added in v0.239.0

Create: Maps a domain to an application. A user must be authorized to administer a domain in order to map it to an application. For a list of available authorized domains, see AuthorizedDomains.ListAuthorizedDomains.

*   applicationsId: Part of `parent`. See documentation of `projectsId`.
*   locationsId: Part of `parent`. See documentation of `projectsId`.
*   projectsId: Part of `parent`. Name of the parent Application resource. Example: apps/myapp.

#### func (*ProjectsLocationsApplicationsDomainMappingsService) [Delete](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4699)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsService.Delete "Go to ProjectsLocationsApplicationsDomainMappingsService.Delete")added in v0.252.0

Delete: Deletes the specified domain mapping. A user must be authorized to administer the associated domain in order to delete a DomainMapping resource.

*   applicationsId: Part of `name`. See documentation of `projectsId`.
*   domainMappingsId: Part of `name`. See documentation of `projectsId`.
*   locationsId: Part of `name`. See documentation of `projectsId`.
*   projectsId: Part of `name`. Name of the resource to delete. Example: apps/myapp/domainMappings/example.com.

#### func (*ProjectsLocationsApplicationsDomainMappingsService) [Get](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4810)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsService.Get "Go to ProjectsLocationsApplicationsDomainMappingsService.Get")added in v0.234.0

Get: Gets the specified domain mapping.

*   applicationsId: Part of `name`. See documentation of `projectsId`.
*   domainMappingsId: Part of `name`. See documentation of `projectsId`.
*   locationsId: Part of `name`. See documentation of `projectsId`.
*   projectsId: Part of `name`. Name of the resource requested. Example: apps/myapp/domainMappings/example.com.

#### func (*ProjectsLocationsApplicationsDomainMappingsService) [List](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L4930)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsService.List "Go to ProjectsLocationsApplicationsDomainMappingsService.List")added in v0.256.0

List: Lists the domain mappings on an application.

*   applicationsId: Part of `parent`. See documentation of `projectsId`.
*   locationsId: Part of `parent`. See documentation of `projectsId`.
*   projectsId: Part of `parent`. Name of the parent Application resource. Example: apps/myapp.

#### func (*ProjectsLocationsApplicationsDomainMappingsService) [Patch](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/appengine/v1alpha/appengine-gen.go#L5089)[¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsService.Patch "Go to ProjectsLocationsApplicationsDomainMappingsService.Patch")added in v0.252.0

Patch: Updates the specified domain mapping. To map an SSL certificate to a domain mapping, update certificate_id to point to an AuthorizedCertificate resource. A user must be authorized to administer the associated domain in order to update a DomainMapping resource.

*   applicationsId: Part of `name`. See documentation of `projectsId`.
*   domainMappingsId: Part of `name`. See documentation of `projectsId`.
*   locationsId: Part of `name`. See documentation of `projectsId`.
*   projectsId: Part of `name`. Name of the resource to update. Example: apps/myapp/domainMappings/example.com.

type ProjectsLocationsApplicationsService struct {
 AuthorizedCertificates *[ProjectsLocationsApplicationsAuthorizedCertificatesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedCertificatesService)
 AuthorizedDomains *[ProjectsLocationsApplicationsAuthorizedDomainsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsAuthorizedDomainsService)
 DomainMappings *[ProjectsLocationsApplicationsDomainMappingsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsDomainMappingsService)	
}

func NewProjectsLocationsApplicationsService(s *[APIService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#APIService)) *[ProjectsLocationsApplicationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsService)

type ProjectsLocationsGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "appengine.projects.locations.get" call. Any non-2xx status code is an error. Response headers are in either *Location.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "appengine.projects.locations.list" call. Any non-2xx status code is an error. Response headers are in either *ListLocationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (c *[ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsListCall)) ExtraLocationTypes(extraLocationTypes ...[string](https://pkg.go.dev/builtin#string)) *[ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsListCall)

ExtraLocationTypes sets the optional parameter "extraLocationTypes": Do not use this field. It is unsupported and is ignored unless explicitly documented otherwise. This is primarily for internal usage.

Filter sets the optional parameter "filter": A filter to narrow down results to a preferred subset. The filtering language accepts strings like "displayName=tokyo", and is documented in more detail in AIP-160 ([https://google.aip.dev/160](https://google.aip.dev/160)).

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": The maximum number of results to return. If not set, the service selects a default.

PageToken sets the optional parameter "pageToken": A page token received from the next_page_token field in the response. Send that page token to receive the subsequent page.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsOperationsGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "appengine.projects.locations.operations.get" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsOperationsListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "appengine.projects.locations.operations.list" call. Any non-2xx status code is an error. Response headers are in either *ListOperationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Filter sets the optional parameter "filter": The standard list filter.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": The standard list page size.

PageToken sets the optional parameter "pageToken": The standard list page token.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (c *[ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsOperationsListCall)) ReturnPartialSuccess(returnPartialSuccess [bool](https://pkg.go.dev/builtin#bool)) *[ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsOperationsListCall)

ReturnPartialSuccess sets the optional parameter "returnPartialSuccess": When set to true, operations that are reachable are returned as normal, and those that are unreachable are returned in the ListOperationsResponse.unreachable field.This can only be true when reading across collections. For example, when parent is set to "projects/example/locations/-".This field is not supported by default and will result in an UNIMPLEMENTED error if set unless explicitly documented otherwise in service or product specific documentation.

type ProjectsLocationsOperationsService struct {
	
}

func NewProjectsLocationsOperationsService(s *[APIService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#APIService)) *[ProjectsLocationsOperationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsOperationsService)

Get: Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

- locationsId: Part of `name`. See documentation of `projectsId`. - operationsId: Part of `name`. See documentation of `projectsId`. - projectsId: Part of `name`. The name of the operation resource.

List: Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns UNIMPLEMENTED.

- locationsId: Part of `name`. See documentation of `projectsId`. - projectsId: Part of `name`. The name of the operation's parent resource.

type ProjectsLocationsService struct {
 Applications *[ProjectsLocationsApplicationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsApplicationsService)
 Operations *[ProjectsLocationsOperationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsOperationsService)	
}

func NewProjectsLocationsService(s *[APIService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#APIService)) *[ProjectsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsService)

Get: Gets information about a location.

- locationsId: Part of `name`. See documentation of `projectsId`. - projectsId: Part of `name`. Resource name for the location.

List: Lists information about the supported locations for this service. This method can be called in two ways: List all public locations: Use the path GET /v1/locations. List project-visible locations: Use the path GET /v1/projects/{project_id}/locations. This may include public locations as well as private or other locations specifically visible to the project.

*   projectsId: Part of `name`. The resource that owns the locations collection, if applicable.

type ProjectsMetadata struct {
	ConsumerProjectId [string](https://pkg.go.dev/builtin#string) `json:"consumerProjectId,omitempty"`
	ConsumerProjectNumber [int64](https://pkg.go.dev/builtin#int64) `json:"consumerProjectNumber,omitempty,string"`
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	ConsumerProjectState [string](https://pkg.go.dev/builtin#string) `json:"consumerProjectState,omitempty"`
	
	GceTag []*[GceTag](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#GceTag) `json:"gceTag,omitempty"`
	
	
	
	IsGceProjectDeprovisioning [bool](https://pkg.go.dev/builtin#bool) `json:"isGceProjectDeprovisioning,omitempty"`
	
	P4ServiceAccount [string](https://pkg.go.dev/builtin#string) `json:"p4ServiceAccount,omitempty"`
	ProducerProjectId [string](https://pkg.go.dev/builtin#string) `json:"producerProjectId,omitempty"`
	ProducerProjectNumber [int64](https://pkg.go.dev/builtin#int64) `json:"producerProjectNumber,omitempty,string"`
	TenantProjectId [string](https://pkg.go.dev/builtin#string) `json:"tenantProjectId,omitempty"`
	TenantProjectNumber [int64](https://pkg.go.dev/builtin#int64) `json:"tenantProjectNumber,omitempty,string"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ProjectsMetadata: ProjectsMetadata is the metadata CCFE stores about the all the relevant projects (tenant, consumer, producer).

type ProjectsService struct {
 Locations *[ProjectsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsLocationsService)	
}

func NewProjectsService(s *[APIService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#APIService)) *[ProjectsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ProjectsService)

type Reasons struct {
	
	
	
	
	
	
	
	
	
	
	Abuse [string](https://pkg.go.dev/builtin#string) `json:"abuse,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	Billing [string](https://pkg.go.dev/builtin#string) `json:"billing,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	DataGovernance [string](https://pkg.go.dev/builtin#string) `json:"dataGovernance,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	ServiceActivation [string](https://pkg.go.dev/builtin#string) `json:"serviceActivation,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	ServiceManagement [string](https://pkg.go.dev/builtin#string) `json:"serviceManagement,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Reasons: Containers transition between and within states based on reasons sent from various systems. CCFE will provide the CLH with reasons for the current state per system.The current systems that CCFE supports are: Service Management (Inception) Data Governance (Wipeout) Abuse (Ares) Billing (Internal Cloud Billing API) Service Activation (Service Controller)

type ResourceEvent struct {
	
	EventId [string](https://pkg.go.dev/builtin#string) `json:"eventId,omitempty"`
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	State *[ContainerState](https://pkg.go.dev/google.golang.org/api@v0.269.0/appengine/v1alpha#ContainerState) `json:"state,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ResourceEvent: The request that is passed to CLH during per-resource events. The request will be sent with update semantics in all cases except for data governance purge events. These events will be sent with delete semantics and the CLH is expected to delete the resource receiving this event.

type ResourceRecord struct {
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	Rrdata [string](https://pkg.go.dev/builtin#string) `json:"rrdata,omitempty"`
	
	
	
	
	
	Type [string](https://pkg.go.dev/builtin#string) `json:"type,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ResourceRecord: A DNS resource record.

type SslSettings struct {
	
	
	
	
	
	
	CertificateId [string](https://pkg.go.dev/builtin#string) `json:"certificateId,omitempty"`
	
	
	
	IsManagedCertificate [bool](https://pkg.go.dev/builtin#bool) `json:"isManagedCertificate,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

SslSettings: SSL configuration for a DomainMapping resource.

type Status struct {
	Code [int64](https://pkg.go.dev/builtin#int64) `json:"code,omitempty"`
	
	Details [][googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[RawMessage](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#RawMessage) `json:"details,omitempty"`
	
	
	Message [string](https://pkg.go.dev/builtin#string) `json:"message,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Status: The Status type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by gRPC ([https://github.com/grpc](https://github.com/grpc)). Each Status message contains three pieces of data: error code, error message, and error details.You can find out more about this error model and how to work with it in the API Design Guide ([https://cloud.google.com/apis/design/errors](https://cloud.google.com/apis/design/errors)).
