# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1

Title: biglake package - google.golang.org/api/biglake/v1 - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1

Markdown Content:
Package biglake provides access to the BigLake API.

For product documentation, see: [https://cloud.google.com/bigquery/](https://cloud.google.com/bigquery/)

#### Library status [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#hdr-Library_status "Go to Library status")

These client libraries are officially supported by Google. However, this library is considered complete and is in maintenance mode. This means that we will address critical bugs and security issues but will not add any new features.

When possible, we recommend using our newer [Cloud Client Libraries for Go]([https://pkg.go.dev/cloud.google.com/go](https://pkg.go.dev/cloud.google.com/go)) that are still actively being worked and iterated on.

#### Creating a client [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#hdr-Creating_a_client "Go to Creating a client")

Usage example:

import "google.golang.org/api/biglake/v1"
...
ctx := context.Background()
biglakeService, err := biglake.NewService(ctx)

In this example, Google Application Default Credentials are used for authentication. For information on how to create and obtain Application Default Credentials, see [https://developers.google.com/identity/protocols/application-default-credentials](https://developers.google.com/identity/protocols/application-default-credentials).

#### Other authentication options [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#hdr-Other_authentication_options "Go to Other authentication options")

By default, all available scopes (see "Constants") are used to authenticate. To restrict scopes, use [google.golang.org/api/option.WithScopes](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#WithScopes):

biglakeService, err := biglake.NewService(ctx, option.WithScopes(biglake.CloudPlatformScope))

To use an API key for authentication (note: some APIs do not support API keys), use [google.golang.org/api/option.WithAPIKey](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#WithAPIKey):

biglakeService, err := biglake.NewService(ctx, option.WithAPIKey("AIza..."))

To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow, use [google.golang.org/api/option.WithTokenSource](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#WithTokenSource):

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
biglakeService, err := biglake.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))

See [google.golang.org/api/option.ClientOption](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#ClientOption) for details on options.

*   [Constants](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#pkg-constants)
*   [type AuditConfig](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#AuditConfig)
*       *   [func (s AuditConfig) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#AuditConfig.MarshalJSON)

*   [type AuditLogConfig](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#AuditLogConfig)
*       *   [func (s AuditLogConfig) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#AuditLogConfig.MarshalJSON)

*   [type Binding](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#Binding)
*       *   [func (s Binding) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#Binding.MarshalJSON)

*   [type Catalog](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#Catalog)
*       *   [func (s Catalog) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#Catalog.MarshalJSON)

*   [type Database](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#Database)
*       *   [func (s Database) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#Database.MarshalJSON)

*   [type Expr](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#Expr)
*       *   [func (s Expr) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#Expr.MarshalJSON)

*   [type HiveDatabaseOptions](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#HiveDatabaseOptions)
*       *   [func (s HiveDatabaseOptions) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#HiveDatabaseOptions.MarshalJSON)

*   [type HiveTableOptions](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#HiveTableOptions)
*       *   [func (s HiveTableOptions) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#HiveTableOptions.MarshalJSON)

*   [type ListCatalogsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ListCatalogsResponse)
*       *   [func (s ListCatalogsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ListCatalogsResponse.MarshalJSON)

*   [type ListDatabasesResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ListDatabasesResponse)
*       *   [func (s ListDatabasesResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ListDatabasesResponse.MarshalJSON)

*   [type ListTablesResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ListTablesResponse)
*       *   [func (s ListTablesResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ListTablesResponse.MarshalJSON)

*   [type Policy](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#Policy)
*       *   [func (s Policy) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#Policy.MarshalJSON)

*   [type ProjectsCatalogsGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsGetIamPolicyCall)
*       *   [func (c *ProjectsCatalogsGetIamPolicyCall) Context(ctx context.Context) *ProjectsCatalogsGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsGetIamPolicyCall.Context)
    *   [func (c *ProjectsCatalogsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsGetIamPolicyCall.Do)
    *   [func (c *ProjectsCatalogsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsCatalogsGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsGetIamPolicyCall.Fields)
    *   [func (c *ProjectsCatalogsGetIamPolicyCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsGetIamPolicyCall.Header)
    *   [func (c *ProjectsCatalogsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsCatalogsGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsGetIamPolicyCall.IfNoneMatch)
    *   [func (c *ProjectsCatalogsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsCatalogsGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsGetIamPolicyCall.OptionsRequestedPolicyVersion)

*   [type ProjectsCatalogsNamespacesGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesGetIamPolicyCall)
*       *   [func (c *ProjectsCatalogsNamespacesGetIamPolicyCall) Context(ctx context.Context) *ProjectsCatalogsNamespacesGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesGetIamPolicyCall.Context)
    *   [func (c *ProjectsCatalogsNamespacesGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesGetIamPolicyCall.Do)
    *   [func (c *ProjectsCatalogsNamespacesGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsCatalogsNamespacesGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesGetIamPolicyCall.Fields)
    *   [func (c *ProjectsCatalogsNamespacesGetIamPolicyCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesGetIamPolicyCall.Header)
    *   [func (c *ProjectsCatalogsNamespacesGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsCatalogsNamespacesGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesGetIamPolicyCall.IfNoneMatch)
    *   [func (c *ProjectsCatalogsNamespacesGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsCatalogsNamespacesGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesGetIamPolicyCall.OptionsRequestedPolicyVersion)

*   [type ProjectsCatalogsNamespacesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesService)
*       *   [func NewProjectsCatalogsNamespacesService(s *Service) *ProjectsCatalogsNamespacesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#NewProjectsCatalogsNamespacesService)

*       *   [func (r *ProjectsCatalogsNamespacesService) GetIamPolicy(resource string) *ProjectsCatalogsNamespacesGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesService.GetIamPolicy)
    *   [func (r *ProjectsCatalogsNamespacesService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsCatalogsNamespacesSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesService.SetIamPolicy)
    *   [func (r *ProjectsCatalogsNamespacesService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsCatalogsNamespacesTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesService.TestIamPermissions)

*   [type ProjectsCatalogsNamespacesSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesSetIamPolicyCall)
*       *   [func (c *ProjectsCatalogsNamespacesSetIamPolicyCall) Context(ctx context.Context) *ProjectsCatalogsNamespacesSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesSetIamPolicyCall.Context)
    *   [func (c *ProjectsCatalogsNamespacesSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesSetIamPolicyCall.Do)
    *   [func (c *ProjectsCatalogsNamespacesSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsCatalogsNamespacesSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesSetIamPolicyCall.Fields)
    *   [func (c *ProjectsCatalogsNamespacesSetIamPolicyCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesSetIamPolicyCall.Header)

*   [type ProjectsCatalogsNamespacesTablesGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesTablesGetIamPolicyCall)
*       *   [func (c *ProjectsCatalogsNamespacesTablesGetIamPolicyCall) Context(ctx context.Context) *ProjectsCatalogsNamespacesTablesGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesTablesGetIamPolicyCall.Context)
    *   [func (c *ProjectsCatalogsNamespacesTablesGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesTablesGetIamPolicyCall.Do)
    *   [func (c *ProjectsCatalogsNamespacesTablesGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsCatalogsNamespacesTablesGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesTablesGetIamPolicyCall.Fields)
    *   [func (c *ProjectsCatalogsNamespacesTablesGetIamPolicyCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesTablesGetIamPolicyCall.Header)
    *   [func (c *ProjectsCatalogsNamespacesTablesGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsCatalogsNamespacesTablesGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesTablesGetIamPolicyCall.IfNoneMatch)
    *   [func (c *ProjectsCatalogsNamespacesTablesGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsCatalogsNamespacesTablesGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesTablesGetIamPolicyCall.OptionsRequestedPolicyVersion)

*   [type ProjectsCatalogsNamespacesTablesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesTablesService)
*       *   [func NewProjectsCatalogsNamespacesTablesService(s *Service) *ProjectsCatalogsNamespacesTablesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#NewProjectsCatalogsNamespacesTablesService)

*       *   [func (r *ProjectsCatalogsNamespacesTablesService) GetIamPolicy(resource string) *ProjectsCatalogsNamespacesTablesGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesTablesService.GetIamPolicy)
    *   [func (r *ProjectsCatalogsNamespacesTablesService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsCatalogsNamespacesTablesSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesTablesService.SetIamPolicy)
    *   [func (r *ProjectsCatalogsNamespacesTablesService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsCatalogsNamespacesTablesTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesTablesService.TestIamPermissions)

*   [type ProjectsCatalogsNamespacesTablesSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesTablesSetIamPolicyCall)
*       *   [func (c *ProjectsCatalogsNamespacesTablesSetIamPolicyCall) Context(ctx context.Context) *ProjectsCatalogsNamespacesTablesSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesTablesSetIamPolicyCall.Context)
    *   [func (c *ProjectsCatalogsNamespacesTablesSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesTablesSetIamPolicyCall.Do)
    *   [func (c *ProjectsCatalogsNamespacesTablesSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsCatalogsNamespacesTablesSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesTablesSetIamPolicyCall.Fields)
    *   [func (c *ProjectsCatalogsNamespacesTablesSetIamPolicyCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesTablesSetIamPolicyCall.Header)

*   [type ProjectsCatalogsNamespacesTablesTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesTablesTestIamPermissionsCall)
*       *   [func (c *ProjectsCatalogsNamespacesTablesTestIamPermissionsCall) Context(ctx context.Context) *ProjectsCatalogsNamespacesTablesTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesTablesTestIamPermissionsCall.Context)
    *   [func (c *ProjectsCatalogsNamespacesTablesTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesTablesTestIamPermissionsCall.Do)
    *   [func (c *ProjectsCatalogsNamespacesTablesTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsCatalogsNamespacesTablesTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesTablesTestIamPermissionsCall.Fields)
    *   [func (c *ProjectsCatalogsNamespacesTablesTestIamPermissionsCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesTablesTestIamPermissionsCall.Header)

*   [type ProjectsCatalogsNamespacesTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesTestIamPermissionsCall)
*       *   [func (c *ProjectsCatalogsNamespacesTestIamPermissionsCall) Context(ctx context.Context) *ProjectsCatalogsNamespacesTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesTestIamPermissionsCall.Context)
    *   [func (c *ProjectsCatalogsNamespacesTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesTestIamPermissionsCall.Do)
    *   [func (c *ProjectsCatalogsNamespacesTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsCatalogsNamespacesTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesTestIamPermissionsCall.Fields)
    *   [func (c *ProjectsCatalogsNamespacesTestIamPermissionsCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesTestIamPermissionsCall.Header)

*   [type ProjectsCatalogsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsService)
*       *   [func NewProjectsCatalogsService(s *Service) *ProjectsCatalogsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#NewProjectsCatalogsService)

*       *   [func (r *ProjectsCatalogsService) GetIamPolicy(resource string) *ProjectsCatalogsGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsService.GetIamPolicy)
    *   [func (r *ProjectsCatalogsService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *ProjectsCatalogsSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsService.SetIamPolicy)
    *   [func (r *ProjectsCatalogsService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *ProjectsCatalogsTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsService.TestIamPermissions)

*   [type ProjectsCatalogsSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsSetIamPolicyCall)
*       *   [func (c *ProjectsCatalogsSetIamPolicyCall) Context(ctx context.Context) *ProjectsCatalogsSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsSetIamPolicyCall.Context)
    *   [func (c *ProjectsCatalogsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsSetIamPolicyCall.Do)
    *   [func (c *ProjectsCatalogsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsCatalogsSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsSetIamPolicyCall.Fields)
    *   [func (c *ProjectsCatalogsSetIamPolicyCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsSetIamPolicyCall.Header)

*   [type ProjectsCatalogsTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsTestIamPermissionsCall)
*       *   [func (c *ProjectsCatalogsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsCatalogsTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsTestIamPermissionsCall.Context)
    *   [func (c *ProjectsCatalogsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsTestIamPermissionsCall.Do)
    *   [func (c *ProjectsCatalogsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsCatalogsTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsTestIamPermissionsCall.Fields)
    *   [func (c *ProjectsCatalogsTestIamPermissionsCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsTestIamPermissionsCall.Header)

*   [type ProjectsLocationsCatalogsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsCreateCall)
*       *   [func (c *ProjectsLocationsCatalogsCreateCall) CatalogId(catalogId string) *ProjectsLocationsCatalogsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsCreateCall.CatalogId)
    *   [func (c *ProjectsLocationsCatalogsCreateCall) Context(ctx context.Context) *ProjectsLocationsCatalogsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsCreateCall.Context)
    *   [func (c *ProjectsLocationsCatalogsCreateCall) Do(opts ...googleapi.CallOption) (*Catalog, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsCreateCall.Do)
    *   [func (c *ProjectsLocationsCatalogsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsCatalogsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsCreateCall.Fields)
    *   [func (c *ProjectsLocationsCatalogsCreateCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsCreateCall.Header)

*   [type ProjectsLocationsCatalogsDatabasesCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesCreateCall)
*       *   [func (c *ProjectsLocationsCatalogsDatabasesCreateCall) Context(ctx context.Context) *ProjectsLocationsCatalogsDatabasesCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesCreateCall.Context)
    *   [func (c *ProjectsLocationsCatalogsDatabasesCreateCall) DatabaseId(databaseId string) *ProjectsLocationsCatalogsDatabasesCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesCreateCall.DatabaseId)
    *   [func (c *ProjectsLocationsCatalogsDatabasesCreateCall) Do(opts ...googleapi.CallOption) (*Database, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesCreateCall.Do)
    *   [func (c *ProjectsLocationsCatalogsDatabasesCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsCatalogsDatabasesCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesCreateCall.Fields)
    *   [func (c *ProjectsLocationsCatalogsDatabasesCreateCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesCreateCall.Header)

*   [type ProjectsLocationsCatalogsDatabasesDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesDeleteCall)
*       *   [func (c *ProjectsLocationsCatalogsDatabasesDeleteCall) Context(ctx context.Context) *ProjectsLocationsCatalogsDatabasesDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesDeleteCall.Context)
    *   [func (c *ProjectsLocationsCatalogsDatabasesDeleteCall) Do(opts ...googleapi.CallOption) (*Database, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesDeleteCall.Do)
    *   [func (c *ProjectsLocationsCatalogsDatabasesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsCatalogsDatabasesDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesDeleteCall.Fields)
    *   [func (c *ProjectsLocationsCatalogsDatabasesDeleteCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesDeleteCall.Header)

*   [type ProjectsLocationsCatalogsDatabasesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesGetCall)
*       *   [func (c *ProjectsLocationsCatalogsDatabasesGetCall) Context(ctx context.Context) *ProjectsLocationsCatalogsDatabasesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesGetCall.Context)
    *   [func (c *ProjectsLocationsCatalogsDatabasesGetCall) Do(opts ...googleapi.CallOption) (*Database, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesGetCall.Do)
    *   [func (c *ProjectsLocationsCatalogsDatabasesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsCatalogsDatabasesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesGetCall.Fields)
    *   [func (c *ProjectsLocationsCatalogsDatabasesGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesGetCall.Header)
    *   [func (c *ProjectsLocationsCatalogsDatabasesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsCatalogsDatabasesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesGetCall.IfNoneMatch)

*   [type ProjectsLocationsCatalogsDatabasesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesListCall)
*       *   [func (c *ProjectsLocationsCatalogsDatabasesListCall) Context(ctx context.Context) *ProjectsLocationsCatalogsDatabasesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesListCall.Context)
    *   [func (c *ProjectsLocationsCatalogsDatabasesListCall) Do(opts ...googleapi.CallOption) (*ListDatabasesResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesListCall.Do)
    *   [func (c *ProjectsLocationsCatalogsDatabasesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsCatalogsDatabasesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesListCall.Fields)
    *   [func (c *ProjectsLocationsCatalogsDatabasesListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesListCall.Header)
    *   [func (c *ProjectsLocationsCatalogsDatabasesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsCatalogsDatabasesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesListCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsCatalogsDatabasesListCall) PageSize(pageSize int64) *ProjectsLocationsCatalogsDatabasesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesListCall.PageSize)
    *   [func (c *ProjectsLocationsCatalogsDatabasesListCall) PageToken(pageToken string) *ProjectsLocationsCatalogsDatabasesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesListCall.PageToken)
    *   [func (c *ProjectsLocationsCatalogsDatabasesListCall) Pages(ctx context.Context, f func(*ListDatabasesResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesListCall.Pages)

*   [type ProjectsLocationsCatalogsDatabasesPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesPatchCall)
*       *   [func (c *ProjectsLocationsCatalogsDatabasesPatchCall) Context(ctx context.Context) *ProjectsLocationsCatalogsDatabasesPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesPatchCall.Context)
    *   [func (c *ProjectsLocationsCatalogsDatabasesPatchCall) Do(opts ...googleapi.CallOption) (*Database, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesPatchCall.Do)
    *   [func (c *ProjectsLocationsCatalogsDatabasesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsCatalogsDatabasesPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesPatchCall.Fields)
    *   [func (c *ProjectsLocationsCatalogsDatabasesPatchCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesPatchCall.Header)
    *   [func (c *ProjectsLocationsCatalogsDatabasesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsCatalogsDatabasesPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesPatchCall.UpdateMask)

*   [type ProjectsLocationsCatalogsDatabasesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesService)
*       *   [func NewProjectsLocationsCatalogsDatabasesService(s *Service) *ProjectsLocationsCatalogsDatabasesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#NewProjectsLocationsCatalogsDatabasesService)

*       *   [func (r *ProjectsLocationsCatalogsDatabasesService) Create(parent string, database *Database) *ProjectsLocationsCatalogsDatabasesCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesService.Create)
    *   [func (r *ProjectsLocationsCatalogsDatabasesService) Delete(name string) *ProjectsLocationsCatalogsDatabasesDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesService.Delete)
    *   [func (r *ProjectsLocationsCatalogsDatabasesService) Get(name string) *ProjectsLocationsCatalogsDatabasesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesService.Get)
    *   [func (r *ProjectsLocationsCatalogsDatabasesService) List(parent string) *ProjectsLocationsCatalogsDatabasesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesService.List)
    *   [func (r *ProjectsLocationsCatalogsDatabasesService) Patch(name string, database *Database) *ProjectsLocationsCatalogsDatabasesPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesService.Patch)

*   [type ProjectsLocationsCatalogsDatabasesTablesCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesCreateCall)
*       *   [func (c *ProjectsLocationsCatalogsDatabasesTablesCreateCall) Context(ctx context.Context) *ProjectsLocationsCatalogsDatabasesTablesCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesCreateCall.Context)
    *   [func (c *ProjectsLocationsCatalogsDatabasesTablesCreateCall) Do(opts ...googleapi.CallOption) (*Table, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesCreateCall.Do)
    *   [func (c *ProjectsLocationsCatalogsDatabasesTablesCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsCatalogsDatabasesTablesCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesCreateCall.Fields)
    *   [func (c *ProjectsLocationsCatalogsDatabasesTablesCreateCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesCreateCall.Header)
    *   [func (c *ProjectsLocationsCatalogsDatabasesTablesCreateCall) TableId(tableId string) *ProjectsLocationsCatalogsDatabasesTablesCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesCreateCall.TableId)

*   [type ProjectsLocationsCatalogsDatabasesTablesDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesDeleteCall)
*       *   [func (c *ProjectsLocationsCatalogsDatabasesTablesDeleteCall) Context(ctx context.Context) *ProjectsLocationsCatalogsDatabasesTablesDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesDeleteCall.Context)
    *   [func (c *ProjectsLocationsCatalogsDatabasesTablesDeleteCall) Do(opts ...googleapi.CallOption) (*Table, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesDeleteCall.Do)
    *   [func (c *ProjectsLocationsCatalogsDatabasesTablesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsCatalogsDatabasesTablesDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesDeleteCall.Fields)
    *   [func (c *ProjectsLocationsCatalogsDatabasesTablesDeleteCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesDeleteCall.Header)

*   [type ProjectsLocationsCatalogsDatabasesTablesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesGetCall)
*       *   [func (c *ProjectsLocationsCatalogsDatabasesTablesGetCall) Context(ctx context.Context) *ProjectsLocationsCatalogsDatabasesTablesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesGetCall.Context)
    *   [func (c *ProjectsLocationsCatalogsDatabasesTablesGetCall) Do(opts ...googleapi.CallOption) (*Table, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesGetCall.Do)
    *   [func (c *ProjectsLocationsCatalogsDatabasesTablesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsCatalogsDatabasesTablesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesGetCall.Fields)
    *   [func (c *ProjectsLocationsCatalogsDatabasesTablesGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesGetCall.Header)
    *   [func (c *ProjectsLocationsCatalogsDatabasesTablesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsCatalogsDatabasesTablesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesGetCall.IfNoneMatch)

*   [type ProjectsLocationsCatalogsDatabasesTablesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesListCall)
*       *   [func (c *ProjectsLocationsCatalogsDatabasesTablesListCall) Context(ctx context.Context) *ProjectsLocationsCatalogsDatabasesTablesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesListCall.Context)
    *   [func (c *ProjectsLocationsCatalogsDatabasesTablesListCall) Do(opts ...googleapi.CallOption) (*ListTablesResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesListCall.Do)
    *   [func (c *ProjectsLocationsCatalogsDatabasesTablesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsCatalogsDatabasesTablesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesListCall.Fields)
    *   [func (c *ProjectsLocationsCatalogsDatabasesTablesListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesListCall.Header)
    *   [func (c *ProjectsLocationsCatalogsDatabasesTablesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsCatalogsDatabasesTablesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesListCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsCatalogsDatabasesTablesListCall) PageSize(pageSize int64) *ProjectsLocationsCatalogsDatabasesTablesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesListCall.PageSize)
    *   [func (c *ProjectsLocationsCatalogsDatabasesTablesListCall) PageToken(pageToken string) *ProjectsLocationsCatalogsDatabasesTablesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesListCall.PageToken)
    *   [func (c *ProjectsLocationsCatalogsDatabasesTablesListCall) Pages(ctx context.Context, f func(*ListTablesResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesListCall.Pages)
    *   [func (c *ProjectsLocationsCatalogsDatabasesTablesListCall) View(view string) *ProjectsLocationsCatalogsDatabasesTablesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesListCall.View)

*   [type ProjectsLocationsCatalogsDatabasesTablesPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesPatchCall)
*       *   [func (c *ProjectsLocationsCatalogsDatabasesTablesPatchCall) Context(ctx context.Context) *ProjectsLocationsCatalogsDatabasesTablesPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesPatchCall.Context)
    *   [func (c *ProjectsLocationsCatalogsDatabasesTablesPatchCall) Do(opts ...googleapi.CallOption) (*Table, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesPatchCall.Do)
    *   [func (c *ProjectsLocationsCatalogsDatabasesTablesPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsCatalogsDatabasesTablesPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesPatchCall.Fields)
    *   [func (c *ProjectsLocationsCatalogsDatabasesTablesPatchCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesPatchCall.Header)
    *   [func (c *ProjectsLocationsCatalogsDatabasesTablesPatchCall) UpdateMask(updateMask string) *ProjectsLocationsCatalogsDatabasesTablesPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesPatchCall.UpdateMask)

*   [type ProjectsLocationsCatalogsDatabasesTablesRenameCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesRenameCall)
*       *   [func (c *ProjectsLocationsCatalogsDatabasesTablesRenameCall) Context(ctx context.Context) *ProjectsLocationsCatalogsDatabasesTablesRenameCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesRenameCall.Context)
    *   [func (c *ProjectsLocationsCatalogsDatabasesTablesRenameCall) Do(opts ...googleapi.CallOption) (*Table, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesRenameCall.Do)
    *   [func (c *ProjectsLocationsCatalogsDatabasesTablesRenameCall) Fields(s ...googleapi.Field) *ProjectsLocationsCatalogsDatabasesTablesRenameCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesRenameCall.Fields)
    *   [func (c *ProjectsLocationsCatalogsDatabasesTablesRenameCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesRenameCall.Header)

*   [type ProjectsLocationsCatalogsDatabasesTablesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesService)
*       *   [func NewProjectsLocationsCatalogsDatabasesTablesService(s *Service) *ProjectsLocationsCatalogsDatabasesTablesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#NewProjectsLocationsCatalogsDatabasesTablesService)

*       *   [func (r *ProjectsLocationsCatalogsDatabasesTablesService) Create(parent string, table *Table) *ProjectsLocationsCatalogsDatabasesTablesCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesService.Create)
    *   [func (r *ProjectsLocationsCatalogsDatabasesTablesService) Delete(name string) *ProjectsLocationsCatalogsDatabasesTablesDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesService.Delete)
    *   [func (r *ProjectsLocationsCatalogsDatabasesTablesService) Get(name string) *ProjectsLocationsCatalogsDatabasesTablesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesService.Get)
    *   [func (r *ProjectsLocationsCatalogsDatabasesTablesService) List(parent string) *ProjectsLocationsCatalogsDatabasesTablesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesService.List)
    *   [func (r *ProjectsLocationsCatalogsDatabasesTablesService) Patch(name string, table *Table) *ProjectsLocationsCatalogsDatabasesTablesPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesService.Patch)
    *   [func (r *ProjectsLocationsCatalogsDatabasesTablesService) Rename(name string, renametablerequest *RenameTableRequest) *ProjectsLocationsCatalogsDatabasesTablesRenameCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesService.Rename)

*   [type ProjectsLocationsCatalogsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDeleteCall)
*       *   [func (c *ProjectsLocationsCatalogsDeleteCall) Context(ctx context.Context) *ProjectsLocationsCatalogsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDeleteCall.Context)
    *   [func (c *ProjectsLocationsCatalogsDeleteCall) Do(opts ...googleapi.CallOption) (*Catalog, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDeleteCall.Do)
    *   [func (c *ProjectsLocationsCatalogsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsCatalogsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDeleteCall.Fields)
    *   [func (c *ProjectsLocationsCatalogsDeleteCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDeleteCall.Header)

*   [type ProjectsLocationsCatalogsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsGetCall)
*       *   [func (c *ProjectsLocationsCatalogsGetCall) Context(ctx context.Context) *ProjectsLocationsCatalogsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsGetCall.Context)
    *   [func (c *ProjectsLocationsCatalogsGetCall) Do(opts ...googleapi.CallOption) (*Catalog, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsGetCall.Do)
    *   [func (c *ProjectsLocationsCatalogsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsCatalogsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsGetCall.Fields)
    *   [func (c *ProjectsLocationsCatalogsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsGetCall.Header)
    *   [func (c *ProjectsLocationsCatalogsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsCatalogsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsGetCall.IfNoneMatch)

*   [type ProjectsLocationsCatalogsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsListCall)
*       *   [func (c *ProjectsLocationsCatalogsListCall) Context(ctx context.Context) *ProjectsLocationsCatalogsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsListCall.Context)
    *   [func (c *ProjectsLocationsCatalogsListCall) Do(opts ...googleapi.CallOption) (*ListCatalogsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsListCall.Do)
    *   [func (c *ProjectsLocationsCatalogsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsCatalogsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsListCall.Fields)
    *   [func (c *ProjectsLocationsCatalogsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsListCall.Header)
    *   [func (c *ProjectsLocationsCatalogsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsCatalogsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsListCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsCatalogsListCall) PageSize(pageSize int64) *ProjectsLocationsCatalogsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsListCall.PageSize)
    *   [func (c *ProjectsLocationsCatalogsListCall) PageToken(pageToken string) *ProjectsLocationsCatalogsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsListCall.PageToken)
    *   [func (c *ProjectsLocationsCatalogsListCall) Pages(ctx context.Context, f func(*ListCatalogsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsListCall.Pages)

*   [type ProjectsLocationsCatalogsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsService)
*       *   [func NewProjectsLocationsCatalogsService(s *Service) *ProjectsLocationsCatalogsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#NewProjectsLocationsCatalogsService)

*       *   [func (r *ProjectsLocationsCatalogsService) Create(parent string, catalog *Catalog) *ProjectsLocationsCatalogsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsService.Create)
    *   [func (r *ProjectsLocationsCatalogsService) Delete(name string) *ProjectsLocationsCatalogsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsService.Delete)
    *   [func (r *ProjectsLocationsCatalogsService) Get(name string) *ProjectsLocationsCatalogsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsService.Get)
    *   [func (r *ProjectsLocationsCatalogsService) List(parent string) *ProjectsLocationsCatalogsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsService.List)

*   [type ProjectsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsService)
*       *   [func NewProjectsLocationsService(s *Service) *ProjectsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#NewProjectsLocationsService)

*   [type ProjectsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsService)
*       *   [func NewProjectsService(s *Service) *ProjectsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#NewProjectsService)

*   [type RenameTableRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#RenameTableRequest)
*       *   [func (s RenameTableRequest) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#RenameTableRequest.MarshalJSON)

*   [type SerDeInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#SerDeInfo)
*       *   [func (s SerDeInfo) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#SerDeInfo.MarshalJSON)

*   [type Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#Service)
*       *   [func New(client *http.Client) (*Service, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#New)deprecated
    *   [func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#NewService)

*   [type SetIamPolicyRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#SetIamPolicyRequest)
*       *   [func (s SetIamPolicyRequest) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#SetIamPolicyRequest.MarshalJSON)

*   [type StorageDescriptor](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#StorageDescriptor)
*       *   [func (s StorageDescriptor) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#StorageDescriptor.MarshalJSON)

*   [type Table](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#Table)
*       *   [func (s Table) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#Table.MarshalJSON)

*   [type TestIamPermissionsRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#TestIamPermissionsRequest)
*       *   [func (s TestIamPermissionsRequest) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#TestIamPermissionsRequest.MarshalJSON)

*   [type TestIamPermissionsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#TestIamPermissionsResponse)
*       *   [func (s TestIamPermissionsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#TestIamPermissionsResponse.MarshalJSON)

[View Source](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/biglake/v1/biglake-gen.go#L105)

const (
	
	BigqueryScope = "https://www.googleapis.com/auth/bigquery"

	
	CloudPlatformScope = "https://www.googleapis.com/auth/cloud-platform"
)

OAuth2 scopes used by this API.

This section is empty.

This section is empty.

type AuditConfig struct {
	AuditLogConfigs []*[AuditLogConfig](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#AuditLogConfig) `json:"auditLogConfigs,omitempty"`
	
	
	Service [string](https://pkg.go.dev/builtin#string) `json:"service,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

AuditConfig: Specifies the audit configuration for a service. The configuration determines which permission types are logged, and what identities, if any, are exempted from logging. An AuditConfig must have one or more AuditLogConfigs. If there are AuditConfigs for both `allServices` and a specific service, the union of the two AuditConfigs is used for that service: the log_types specified in each AuditConfig are enabled, and the exempted_members in each AuditLogConfig are exempted. Example Policy with multiple AuditConfigs: { "audit_configs": [ { "service": "allServices", "audit_log_configs": [ { "log_type": "DATA_READ", "exempted_members": [ "user:jose@example.com" ] }, { "log_type": "DATA_WRITE" }, { "log_type": "ADMIN_READ" } ] }, { "service": "sampleservice.googleapis.com", "audit_log_configs": [ { "log_type": "DATA_READ" }, { "log_type": "DATA_WRITE", "exempted_members": [ "user:aliya@example.com" ] } ] } ] } For sampleservice, this policy enables DATA_READ, DATA_WRITE and ADMIN_READ logging. It also exempts `jose@example.com` from DATA_READ logging, and `aliya@example.com` from DATA_WRITE logging.

type AuditLogConfig struct {
	
	ExemptedMembers [][string](https://pkg.go.dev/builtin#string) `json:"exemptedMembers,omitempty"`
	
	
	
	
	
	
	LogType [string](https://pkg.go.dev/builtin#string) `json:"logType,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

AuditLogConfig: Provides the configuration for logging a type of permissions. Example: { "audit_log_configs": [ { "log_type": "DATA_READ", "exempted_members": [ "user:jose@example.com" ] }, { "log_type": "DATA_WRITE" } ] } This enables 'DATA_READ' and 'DATA_WRITE' logging, while exempting jose@example.com from DATA_READ logging.

type Binding struct {
	
	
	
	
	
	
	
	Condition *[Expr](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#Expr) `json:"condition,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	Members [][string](https://pkg.go.dev/builtin#string) `json:"members,omitempty"`
	
	
	
	
	
	Role [string](https://pkg.go.dev/builtin#string) `json:"role,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Binding: Associates `members`, or principals, with a `role`.

type Catalog struct {
	CreateTime [string](https://pkg.go.dev/builtin#string) `json:"createTime,omitempty"`
	
	DeleteTime [string](https://pkg.go.dev/builtin#string) `json:"deleteTime,omitempty"`
	
	ExpireTime [string](https://pkg.go.dev/builtin#string) `json:"expireTime,omitempty"`
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	UpdateTime [string](https://pkg.go.dev/builtin#string) `json:"updateTime,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Catalog: Catalog is the container of databases.

type Database struct {
	CreateTime [string](https://pkg.go.dev/builtin#string) `json:"createTime,omitempty"`
	
	DeleteTime [string](https://pkg.go.dev/builtin#string) `json:"deleteTime,omitempty"`
	
	ExpireTime [string](https://pkg.go.dev/builtin#string) `json:"expireTime,omitempty"`
	HiveOptions *[HiveDatabaseOptions](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#HiveDatabaseOptions) `json:"hiveOptions,omitempty"`
	
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	
	
	
	
	Type [string](https://pkg.go.dev/builtin#string) `json:"type,omitempty"`
	UpdateTime [string](https://pkg.go.dev/builtin#string) `json:"updateTime,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Database: Database is the container of tables.

type Expr struct {
	
	Description [string](https://pkg.go.dev/builtin#string) `json:"description,omitempty"`
	
	Expression [string](https://pkg.go.dev/builtin#string) `json:"expression,omitempty"`
	
	Location [string](https://pkg.go.dev/builtin#string) `json:"location,omitempty"`
	
	
	Title [string](https://pkg.go.dev/builtin#string) `json:"title,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Expr: Represents a textual expression in the Common Expression Language (CEL) syntax. CEL is a C-like expression language. The syntax and semantics of CEL are documented at [https://github.com/google/cel-spec](https://github.com/google/cel-spec). Example (Comparison): title: "Summary size limit" description: "Determines if a summary is less than 100 chars" expression: "document.summary.size() < 100" Example (Equality): title: "Requestor is owner" description: "Determines if requestor is the document owner" expression: "document.owner == request.auth.claims.email" Example (Logic): title: "Public documents" description: "Determine whether the document should be publicly visible" expression: "document.type != 'private' && document.type != 'internal'" Example (Data Manipulation): title: "Notification string" description: "Create a notification string with a timestamp." expression: "'New message received at ' + string(document.create_time)" The exact variables and functions that may be referenced within an expression are determined by the service that evaluates it. See the service documentation for additional information.

type HiveDatabaseOptions struct {
	
	LocationUri [string](https://pkg.go.dev/builtin#string) `json:"locationUri,omitempty"`
	Parameters map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `json:"parameters,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

HiveDatabaseOptions: Options of a Hive database.

type HiveTableOptions struct {
	Parameters map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `json:"parameters,omitempty"`
	StorageDescriptor *[StorageDescriptor](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#StorageDescriptor) `json:"storageDescriptor,omitempty"`
	TableType [string](https://pkg.go.dev/builtin#string) `json:"tableType,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

HiveTableOptions: Options of a Hive table.

type ListCatalogsResponse struct {
	Catalogs []*[Catalog](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#Catalog) `json:"catalogs,omitempty"`
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListCatalogsResponse: Response message for the ListCatalogs method.

type ListDatabasesResponse struct {
	Databases []*[Database](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#Database) `json:"databases,omitempty"`
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListDatabasesResponse: Response message for the ListDatabases method.

type ListTablesResponse struct {
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`
	Tables []*[Table](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#Table) `json:"tables,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListTablesResponse: Response message for the ListTables method.

type Policy struct {
	AuditConfigs []*[AuditConfig](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#AuditConfig) `json:"auditConfigs,omitempty"`
	
	
	
	
	
	
	
	
	Bindings []*[Binding](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#Binding) `json:"bindings,omitempty"`
	
	
	
	
	
	
	
	
	
	
	Etag [string](https://pkg.go.dev/builtin#string) `json:"etag,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	Version [int64](https://pkg.go.dev/builtin#int64) `json:"version,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Policy: An Identity and Access Management (IAM) policy, which specifies access controls for Google Cloud resources. A `Policy` is a collection of `bindings`. A `binding` binds one or more `members`, or principals, to a single `role`. Principals can be user accounts, service accounts, Google groups, and domains (such as G Suite). A `role` is a named list of permissions; each `role` can be an IAM predefined role or a user-created custom role. For some types of Google Cloud resources, a `binding` can also specify a `condition`, which is a logical expression that allows access to a resource only if the expression evaluates to `true`. A condition can add constraints based on attributes of the request, the resource, or both. To learn which resources support conditions in their IAM policies, see the IAM documentation ([https://cloud.google.com/iam/help/conditions/resource-policies](https://cloud.google.com/iam/help/conditions/resource-policies)). **JSON example:** ``` { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": [ "user:eve@example.com" ], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01T00:00:00.000Z')", } } ], "etag": "BwWWja0YfJA=", "version": 3 } ``` **YAML example:** ``` bindings: - members: - user:mike@example.com - group:admins@example.com - domain:google.com - serviceAccount:my-project-id@appspot.gserviceaccount.com role: roles/resourcemanager.organizationAdmin - members: - user:eve@example.com role: roles/resourcemanager.organizationViewer condition: title: expirable access description: Does not grant access after Sep 2020 expression: request.time < timestamp('2020-10-01T00:00:00.000Z') etag: BwWWja0YfJA= version: 3 ``` For a description of IAM and its features, see the IAM documentation ([https://cloud.google.com/iam/docs/](https://cloud.google.com/iam/docs/)).

type ProjectsCatalogsGetIamPolicyCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "biglake.projects.catalogs.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (c *[ProjectsCatalogsGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsGetIamPolicyCall)) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion [int64](https://pkg.go.dev/builtin#int64)) *[ProjectsCatalogsGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsGetIamPolicyCall)

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the IAM documentation ([https://cloud.google.com/iam/help/conditions/resource-policies](https://cloud.google.com/iam/help/conditions/resource-policies)).

type ProjectsCatalogsNamespacesGetIamPolicyCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "biglake.projects.catalogs.namespaces.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (c *[ProjectsCatalogsNamespacesGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesGetIamPolicyCall)) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion [int64](https://pkg.go.dev/builtin#int64)) *[ProjectsCatalogsNamespacesGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesGetIamPolicyCall)

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the IAM documentation ([https://cloud.google.com/iam/help/conditions/resource-policies](https://cloud.google.com/iam/help/conditions/resource-policies)).

type ProjectsCatalogsNamespacesService struct {
 Tables *[ProjectsCatalogsNamespacesTablesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesTablesService)	
}

func NewProjectsCatalogsNamespacesService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#Service)) *[ProjectsCatalogsNamespacesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesService)

TestIamPermissions: Tests the IAM permissions for the specified namespace.

*   resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names ([https://cloud.google.com/apis/design/resource_names](https://cloud.google.com/apis/design/resource_names)) for the appropriate value for this field.

type ProjectsCatalogsNamespacesSetIamPolicyCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "biglake.projects.catalogs.namespaces.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsCatalogsNamespacesTablesGetIamPolicyCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "biglake.projects.catalogs.namespaces.tables.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (c *[ProjectsCatalogsNamespacesTablesGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesTablesGetIamPolicyCall)) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion [int64](https://pkg.go.dev/builtin#int64)) *[ProjectsCatalogsNamespacesTablesGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesTablesGetIamPolicyCall)

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the IAM documentation ([https://cloud.google.com/iam/help/conditions/resource-policies](https://cloud.google.com/iam/help/conditions/resource-policies)).

type ProjectsCatalogsNamespacesTablesService struct {
	
}

func NewProjectsCatalogsNamespacesTablesService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#Service)) *[ProjectsCatalogsNamespacesTablesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesTablesService)

TestIamPermissions: Tests the IAM permissions for the specified table.

*   resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names ([https://cloud.google.com/apis/design/resource_names](https://cloud.google.com/apis/design/resource_names)) for the appropriate value for this field.

type ProjectsCatalogsNamespacesTablesSetIamPolicyCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "biglake.projects.catalogs.namespaces.tables.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsCatalogsNamespacesTablesTestIamPermissionsCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "biglake.projects.catalogs.namespaces.tables.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsCatalogsNamespacesTestIamPermissionsCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "biglake.projects.catalogs.namespaces.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsCatalogsService struct {
 Namespaces *[ProjectsCatalogsNamespacesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsNamespacesService)	
}

func NewProjectsCatalogsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#Service)) *[ProjectsCatalogsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsService)

func (r *[ProjectsCatalogsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsService)) TestIamPermissions(resource [string](https://pkg.go.dev/builtin#string), testiampermissionsrequest *[TestIamPermissionsRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#TestIamPermissionsRequest)) *[ProjectsCatalogsTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsTestIamPermissionsCall)

TestIamPermissions: Tests the IAM permissions for the specified catalog.

*   resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names ([https://cloud.google.com/apis/design/resource_names](https://cloud.google.com/apis/design/resource_names)) for the appropriate value for this field.

type ProjectsCatalogsSetIamPolicyCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "biglake.projects.catalogs.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsCatalogsTestIamPermissionsCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "biglake.projects.catalogs.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsCatalogsCreateCall struct {
	
}

CatalogId sets the optional parameter "catalogId": Required. The ID to use for the catalog, which will become the final component of the catalog's resource name.

Context sets the context to be used in this call's Do method.

Do executes the "biglake.projects.locations.catalogs.create" call. Any non-2xx status code is an error. Response headers are in either *Catalog.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsCatalogsDatabasesCreateCall struct {
	
}

Context sets the context to be used in this call's Do method.

DatabaseId sets the optional parameter "databaseId": Required. The ID to use for the database, which will become the final component of the database's resource name.

Do executes the "biglake.projects.locations.catalogs.databases.create" call. Any non-2xx status code is an error. Response headers are in either *Database.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsCatalogsDatabasesDeleteCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "biglake.projects.locations.catalogs.databases.delete" call. Any non-2xx status code is an error. Response headers are in either *Database.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsCatalogsDatabasesGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "biglake.projects.locations.catalogs.databases.get" call. Any non-2xx status code is an error. Response headers are in either *Database.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsCatalogsDatabasesListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "biglake.projects.locations.catalogs.databases.list" call. Any non-2xx status code is an error. Response headers are in either *ListDatabasesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": The maximum number of databases to return. The service may return fewer than this value. If unspecified, at most 50 databases will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListDatabases` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListDatabases` must match the call that provided the page token.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsCatalogsDatabasesPatchCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "biglake.projects.locations.catalogs.databases.patch" call. Any non-2xx status code is an error. Response headers are in either *Database.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsCatalogsDatabasesService struct {
 Tables *[ProjectsLocationsCatalogsDatabasesTablesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesService)	
}

func NewProjectsLocationsCatalogsDatabasesService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#Service)) *[ProjectsLocationsCatalogsDatabasesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesService)

Create: Creates a new database.

*   parent: The parent resource where this database will be created. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_i d}.

Delete: Deletes an existing database specified by the database ID.

*   name: The name of the database to delete. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_i d}/databases/{database_id}.

Get: Gets the database specified by the resource name.

*   name: The name of the database to retrieve. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_i d}/databases/{database_id}.

List: List all databases in a specified catalog.

*   parent: The parent, which owns this collection of databases. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_i d}.

Patch: Updates an existing database specified by the database ID.

*   name: Output only. The resource name. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_i d}/databases/{database_id}.

type ProjectsLocationsCatalogsDatabasesTablesCreateCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "biglake.projects.locations.catalogs.databases.tables.create" call. Any non-2xx status code is an error. Response headers are in either *Table.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

TableId sets the optional parameter "tableId": Required. The ID to use for the table, which will become the final component of the table's resource name.

type ProjectsLocationsCatalogsDatabasesTablesDeleteCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "biglake.projects.locations.catalogs.databases.tables.delete" call. Any non-2xx status code is an error. Response headers are in either *Table.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsCatalogsDatabasesTablesGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "biglake.projects.locations.catalogs.databases.tables.get" call. Any non-2xx status code is an error. Response headers are in either *Table.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsCatalogsDatabasesTablesListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "biglake.projects.locations.catalogs.databases.tables.list" call. Any non-2xx status code is an error. Response headers are in either *ListTablesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": The maximum number of tables to return. The service may return fewer than this value. If unspecified, at most 50 tables will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListTables` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListTables` must match the call that provided the page token.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

View sets the optional parameter "view": The view for the returned tables.

Possible values:

"TABLE_VIEW_UNSPECIFIED" - Default value. The API will default to the

BASIC view.

"BASIC" - Include only table names. This is the default value.
"FULL" - Include everything.

type ProjectsLocationsCatalogsDatabasesTablesPatchCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "biglake.projects.locations.catalogs.databases.tables.patch" call. Any non-2xx status code is an error. Response headers are in either *Table.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsCatalogsDatabasesTablesRenameCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "biglake.projects.locations.catalogs.databases.tables.rename" call. Any non-2xx status code is an error. Response headers are in either *Table.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsCatalogsDatabasesTablesService struct {
	
}

func NewProjectsLocationsCatalogsDatabasesTablesService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#Service)) *[ProjectsLocationsCatalogsDatabasesTablesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesTablesService)

Create: Creates a new table.

*   parent: The parent resource where this table will be created. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_i d}/databases/{database_id}.

Delete: Deletes an existing table specified by the table ID.

*   name: The name of the table to delete. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_i d}/databases/{database_id}/tables/{table_id}.

Get: Gets the table specified by the resource name.

*   name: The name of the table to retrieve. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_i d}/databases/{database_id}/tables/{table_id}.

List: List all tables in a specified database.

*   parent: The parent, which owns this collection of tables. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_i d}/databases/{database_id}.

Patch: Updates an existing table specified by the table ID.

*   name: Output only. The resource name. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_i d}/databases/{database_id}/tables/{table_id}.

Rename: Renames an existing table specified by the table ID.

*   name: The table's `name` field is used to identify the table to rename. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_i d}/databases/{database_id}/tables/{table_id}.

type ProjectsLocationsCatalogsDeleteCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "biglake.projects.locations.catalogs.delete" call. Any non-2xx status code is an error. Response headers are in either *Catalog.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsCatalogsGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "biglake.projects.locations.catalogs.get" call. Any non-2xx status code is an error. Response headers are in either *Catalog.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsCatalogsListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "biglake.projects.locations.catalogs.list" call. Any non-2xx status code is an error. Response headers are in either *ListCatalogsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": The maximum number of catalogs to return. The service may return fewer than this value. If unspecified, at most 50 catalogs will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListCatalogs` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListCatalogs` must match the call that provided the page token.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsCatalogsService struct {
 Databases *[ProjectsLocationsCatalogsDatabasesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsDatabasesService)	
}

func NewProjectsLocationsCatalogsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#Service)) *[ProjectsLocationsCatalogsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsService)

Create: Creates a new catalog.

*   parent: The parent resource where this catalog will be created. Format: projects/{project_id_or_number}/locations/{location_id}.

Delete: Deletes an existing catalog specified by the catalog ID.

*   name: The name of the catalog to delete. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_i d}.

Get: Gets the catalog specified by the resource name.

*   name: The name of the catalog to retrieve. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_i d}.

List: List all catalogs in a specified project.

*   parent: The parent, which owns this collection of catalogs. Format: projects/{project_id_or_number}/locations/{location_id}.

type ProjectsLocationsService struct {
 Catalogs *[ProjectsLocationsCatalogsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsCatalogsService)	
}

func NewProjectsLocationsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#Service)) *[ProjectsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsService)

type ProjectsService struct {
 Catalogs *[ProjectsCatalogsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsCatalogsService)
 Locations *[ProjectsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsLocationsService)	
}

func NewProjectsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#Service)) *[ProjectsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#ProjectsService)

type RenameTableRequest struct {
	
	
	
	NewName [string](https://pkg.go.dev/builtin#string) `json:"newName,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

RenameTableRequest: Request message for the RenameTable method in MetastoreService

type SerDeInfo struct {
	
	SerializationLib [string](https://pkg.go.dev/builtin#string) `json:"serializationLib,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

SerDeInfo: Serializer and deserializer information.

New creates a new Service. It uses the provided http.Client for requests.

Deprecated: please use NewService instead. To provide a custom HTTP client, use option.WithHTTPClient. If you are using google.golang.org/api/googleapis/transport.APIKey, use option.WithAPIKey with NewService instead.

NewService creates a new Service.

type SetIamPolicyRequest struct {
	
	
	
	Policy *[Policy](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#Policy) `json:"policy,omitempty"`
	
	
	UpdateMask [string](https://pkg.go.dev/builtin#string) `json:"updateMask,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

SetIamPolicyRequest: Request message for `SetIamPolicy` method.

type StorageDescriptor struct {
	InputFormat [string](https://pkg.go.dev/builtin#string) `json:"inputFormat,omitempty"`
	
	LocationUri [string](https://pkg.go.dev/builtin#string) `json:"locationUri,omitempty"`
	OutputFormat [string](https://pkg.go.dev/builtin#string) `json:"outputFormat,omitempty"`
	SerdeInfo *[SerDeInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#SerDeInfo) `json:"serdeInfo,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

StorageDescriptor: Stores physical storage information of the data.

type Table struct {
	CreateTime [string](https://pkg.go.dev/builtin#string) `json:"createTime,omitempty"`
	
	DeleteTime [string](https://pkg.go.dev/builtin#string) `json:"deleteTime,omitempty"`
	
	
	
	Etag [string](https://pkg.go.dev/builtin#string) `json:"etag,omitempty"`
	
	ExpireTime [string](https://pkg.go.dev/builtin#string) `json:"expireTime,omitempty"`
	HiveOptions *[HiveTableOptions](https://pkg.go.dev/google.golang.org/api@v0.269.0/biglake/v1#HiveTableOptions) `json:"hiveOptions,omitempty"`
	
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	
	
	
	Type [string](https://pkg.go.dev/builtin#string) `json:"type,omitempty"`
	UpdateTime [string](https://pkg.go.dev/builtin#string) `json:"updateTime,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Table: Represents a table.

type TestIamPermissionsRequest struct {
	
	
	
	Permissions [][string](https://pkg.go.dev/builtin#string) `json:"permissions,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

TestIamPermissionsRequest: Request message for `TestIamPermissions` method.

TestIamPermissionsResponse: Response message for `TestIamPermissions` method.
