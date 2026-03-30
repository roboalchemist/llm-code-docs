# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1

Title: bigquerydatatransfer package - google.golang.org/api/bigquerydatatransfer/v1 - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1

Markdown Content:
Package bigquerydatatransfer provides access to the BigQuery Data Transfer API.

For product documentation, see: [https://cloud.google.com/bigquery-transfer/](https://cloud.google.com/bigquery-transfer/)

#### Library status [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#hdr-Library_status "Go to Library status")

These client libraries are officially supported by Google. However, this library is considered complete and is in maintenance mode. This means that we will address critical bugs and security issues but will not add any new features.

When possible, we recommend using our newer [Cloud Client Libraries for Go]([https://pkg.go.dev/cloud.google.com/go](https://pkg.go.dev/cloud.google.com/go)) that are still actively being worked and iterated on.

#### Creating a client [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#hdr-Creating_a_client "Go to Creating a client")

Usage example:

import "google.golang.org/api/bigquerydatatransfer/v1"
...
ctx := context.Background()
bigquerydatatransferService, err := bigquerydatatransfer.NewService(ctx)

In this example, Google Application Default Credentials are used for authentication. For information on how to create and obtain Application Default Credentials, see [https://developers.google.com/identity/protocols/application-default-credentials](https://developers.google.com/identity/protocols/application-default-credentials).

#### Other authentication options [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#hdr-Other_authentication_options "Go to Other authentication options")

By default, all available scopes (see "Constants") are used to authenticate. To restrict scopes, use [google.golang.org/api/option.WithScopes](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#WithScopes):

bigquerydatatransferService, err := bigquerydatatransfer.NewService(ctx, option.WithScopes(bigquerydatatransfer.CloudPlatformReadOnlyScope))

To use an API key for authentication (note: some APIs do not support API keys), use [google.golang.org/api/option.WithAPIKey](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#WithAPIKey):

bigquerydatatransferService, err := bigquerydatatransfer.NewService(ctx, option.WithAPIKey("AIza..."))

To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow, use [google.golang.org/api/option.WithTokenSource](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#WithTokenSource):

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
bigquerydatatransferService, err := bigquerydatatransfer.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))

See [google.golang.org/api/option.ClientOption](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#ClientOption) for details on options.

*   [Constants](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#pkg-constants)
*   [type CheckValidCredsRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#CheckValidCredsRequest)
*   [type CheckValidCredsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#CheckValidCredsResponse)
*       *   [func (s CheckValidCredsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#CheckValidCredsResponse.MarshalJSON)

*   [type DataSource](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#DataSource)
*       *   [func (s DataSource) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#DataSource.MarshalJSON)

*   [type DataSourceParameter](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#DataSourceParameter)
*       *   [func (s DataSourceParameter) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#DataSourceParameter.MarshalJSON)
    *   [func (s *DataSourceParameter) UnmarshalJSON(data []byte) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#DataSourceParameter.UnmarshalJSON)

*   [type EmailPreferences](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#EmailPreferences)
*       *   [func (s EmailPreferences) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#EmailPreferences.MarshalJSON)

*   [type Empty](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#Empty)
*   [type EncryptionConfiguration](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#EncryptionConfiguration)
*       *   [func (s EncryptionConfiguration) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#EncryptionConfiguration.MarshalJSON)

*   [type EnrollDataSourcesRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#EnrollDataSourcesRequest)
*       *   [func (s EnrollDataSourcesRequest) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#EnrollDataSourcesRequest.MarshalJSON)

*   [type EventDrivenSchedule](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#EventDrivenSchedule)
*       *   [func (s EventDrivenSchedule) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#EventDrivenSchedule.MarshalJSON)

*   [type ListDataSourcesResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ListDataSourcesResponse)
*       *   [func (s ListDataSourcesResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ListDataSourcesResponse.MarshalJSON)

*   [type ListLocationsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ListLocationsResponse)
*       *   [func (s ListLocationsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ListLocationsResponse.MarshalJSON)

*   [type ListTransferConfigsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ListTransferConfigsResponse)
*       *   [func (s ListTransferConfigsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ListTransferConfigsResponse.MarshalJSON)

*   [type ListTransferLogsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ListTransferLogsResponse)
*       *   [func (s ListTransferLogsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ListTransferLogsResponse.MarshalJSON)

*   [type ListTransferRunsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ListTransferRunsResponse)
*       *   [func (s ListTransferRunsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ListTransferRunsResponse.MarshalJSON)

*   [type Location](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#Location)
*       *   [func (s Location) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#Location.MarshalJSON)

*   [type ManualSchedule](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ManualSchedule)
*   [type ProjectsDataSourcesCheckValidCredsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsDataSourcesCheckValidCredsCall)
*       *   [func (c *ProjectsDataSourcesCheckValidCredsCall) Context(ctx context.Context) *ProjectsDataSourcesCheckValidCredsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsDataSourcesCheckValidCredsCall.Context)
    *   [func (c *ProjectsDataSourcesCheckValidCredsCall) Do(opts ...googleapi.CallOption) (*CheckValidCredsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsDataSourcesCheckValidCredsCall.Do)
    *   [func (c *ProjectsDataSourcesCheckValidCredsCall) Fields(s ...googleapi.Field) *ProjectsDataSourcesCheckValidCredsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsDataSourcesCheckValidCredsCall.Fields)
    *   [func (c *ProjectsDataSourcesCheckValidCredsCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsDataSourcesCheckValidCredsCall.Header)

*   [type ProjectsDataSourcesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsDataSourcesGetCall)
*       *   [func (c *ProjectsDataSourcesGetCall) Context(ctx context.Context) *ProjectsDataSourcesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsDataSourcesGetCall.Context)
    *   [func (c *ProjectsDataSourcesGetCall) Do(opts ...googleapi.CallOption) (*DataSource, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsDataSourcesGetCall.Do)
    *   [func (c *ProjectsDataSourcesGetCall) Fields(s ...googleapi.Field) *ProjectsDataSourcesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsDataSourcesGetCall.Fields)
    *   [func (c *ProjectsDataSourcesGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsDataSourcesGetCall.Header)
    *   [func (c *ProjectsDataSourcesGetCall) IfNoneMatch(entityTag string) *ProjectsDataSourcesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsDataSourcesGetCall.IfNoneMatch)

*   [type ProjectsDataSourcesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsDataSourcesListCall)
*       *   [func (c *ProjectsDataSourcesListCall) Context(ctx context.Context) *ProjectsDataSourcesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsDataSourcesListCall.Context)
    *   [func (c *ProjectsDataSourcesListCall) Do(opts ...googleapi.CallOption) (*ListDataSourcesResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsDataSourcesListCall.Do)
    *   [func (c *ProjectsDataSourcesListCall) Fields(s ...googleapi.Field) *ProjectsDataSourcesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsDataSourcesListCall.Fields)
    *   [func (c *ProjectsDataSourcesListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsDataSourcesListCall.Header)
    *   [func (c *ProjectsDataSourcesListCall) IfNoneMatch(entityTag string) *ProjectsDataSourcesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsDataSourcesListCall.IfNoneMatch)
    *   [func (c *ProjectsDataSourcesListCall) PageSize(pageSize int64) *ProjectsDataSourcesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsDataSourcesListCall.PageSize)
    *   [func (c *ProjectsDataSourcesListCall) PageToken(pageToken string) *ProjectsDataSourcesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsDataSourcesListCall.PageToken)
    *   [func (c *ProjectsDataSourcesListCall) Pages(ctx context.Context, f func(*ListDataSourcesResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsDataSourcesListCall.Pages)

*   [type ProjectsDataSourcesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsDataSourcesService)
*       *   [func NewProjectsDataSourcesService(s *Service) *ProjectsDataSourcesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#NewProjectsDataSourcesService)

*       *   [func (r *ProjectsDataSourcesService) CheckValidCreds(name string, checkvalidcredsrequest *CheckValidCredsRequest) *ProjectsDataSourcesCheckValidCredsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsDataSourcesService.CheckValidCreds)
    *   [func (r *ProjectsDataSourcesService) Get(name string) *ProjectsDataSourcesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsDataSourcesService.Get)
    *   [func (r *ProjectsDataSourcesService) List(parent string) *ProjectsDataSourcesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsDataSourcesService.List)

*   [type ProjectsEnrollDataSourcesCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsEnrollDataSourcesCall)
*       *   [func (c *ProjectsEnrollDataSourcesCall) Context(ctx context.Context) *ProjectsEnrollDataSourcesCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsEnrollDataSourcesCall.Context)
    *   [func (c *ProjectsEnrollDataSourcesCall) Do(opts ...googleapi.CallOption) (*Empty, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsEnrollDataSourcesCall.Do)
    *   [func (c *ProjectsEnrollDataSourcesCall) Fields(s ...googleapi.Field) *ProjectsEnrollDataSourcesCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsEnrollDataSourcesCall.Fields)
    *   [func (c *ProjectsEnrollDataSourcesCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsEnrollDataSourcesCall.Header)

*   [type ProjectsLocationsDataSourcesCheckValidCredsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsDataSourcesCheckValidCredsCall)
*       *   [func (c *ProjectsLocationsDataSourcesCheckValidCredsCall) Context(ctx context.Context) *ProjectsLocationsDataSourcesCheckValidCredsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsDataSourcesCheckValidCredsCall.Context)
    *   [func (c *ProjectsLocationsDataSourcesCheckValidCredsCall) Do(opts ...googleapi.CallOption) (*CheckValidCredsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsDataSourcesCheckValidCredsCall.Do)
    *   [func (c *ProjectsLocationsDataSourcesCheckValidCredsCall) Fields(s ...googleapi.Field) *ProjectsLocationsDataSourcesCheckValidCredsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsDataSourcesCheckValidCredsCall.Fields)
    *   [func (c *ProjectsLocationsDataSourcesCheckValidCredsCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsDataSourcesCheckValidCredsCall.Header)

*   [type ProjectsLocationsDataSourcesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsDataSourcesGetCall)
*       *   [func (c *ProjectsLocationsDataSourcesGetCall) Context(ctx context.Context) *ProjectsLocationsDataSourcesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsDataSourcesGetCall.Context)
    *   [func (c *ProjectsLocationsDataSourcesGetCall) Do(opts ...googleapi.CallOption) (*DataSource, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsDataSourcesGetCall.Do)
    *   [func (c *ProjectsLocationsDataSourcesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsDataSourcesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsDataSourcesGetCall.Fields)
    *   [func (c *ProjectsLocationsDataSourcesGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsDataSourcesGetCall.Header)
    *   [func (c *ProjectsLocationsDataSourcesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsDataSourcesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsDataSourcesGetCall.IfNoneMatch)

*   [type ProjectsLocationsDataSourcesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsDataSourcesListCall)
*       *   [func (c *ProjectsLocationsDataSourcesListCall) Context(ctx context.Context) *ProjectsLocationsDataSourcesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsDataSourcesListCall.Context)
    *   [func (c *ProjectsLocationsDataSourcesListCall) Do(opts ...googleapi.CallOption) (*ListDataSourcesResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsDataSourcesListCall.Do)
    *   [func (c *ProjectsLocationsDataSourcesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsDataSourcesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsDataSourcesListCall.Fields)
    *   [func (c *ProjectsLocationsDataSourcesListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsDataSourcesListCall.Header)
    *   [func (c *ProjectsLocationsDataSourcesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsDataSourcesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsDataSourcesListCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsDataSourcesListCall) PageSize(pageSize int64) *ProjectsLocationsDataSourcesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsDataSourcesListCall.PageSize)
    *   [func (c *ProjectsLocationsDataSourcesListCall) PageToken(pageToken string) *ProjectsLocationsDataSourcesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsDataSourcesListCall.PageToken)
    *   [func (c *ProjectsLocationsDataSourcesListCall) Pages(ctx context.Context, f func(*ListDataSourcesResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsDataSourcesListCall.Pages)

*   [type ProjectsLocationsDataSourcesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsDataSourcesService)
*       *   [func NewProjectsLocationsDataSourcesService(s *Service) *ProjectsLocationsDataSourcesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#NewProjectsLocationsDataSourcesService)

*       *   [func (r *ProjectsLocationsDataSourcesService) CheckValidCreds(name string, checkvalidcredsrequest *CheckValidCredsRequest) *ProjectsLocationsDataSourcesCheckValidCredsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsDataSourcesService.CheckValidCreds)
    *   [func (r *ProjectsLocationsDataSourcesService) Get(name string) *ProjectsLocationsDataSourcesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsDataSourcesService.Get)
    *   [func (r *ProjectsLocationsDataSourcesService) List(parent string) *ProjectsLocationsDataSourcesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsDataSourcesService.List)

*   [type ProjectsLocationsEnrollDataSourcesCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsEnrollDataSourcesCall)
*       *   [func (c *ProjectsLocationsEnrollDataSourcesCall) Context(ctx context.Context) *ProjectsLocationsEnrollDataSourcesCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsEnrollDataSourcesCall.Context)
    *   [func (c *ProjectsLocationsEnrollDataSourcesCall) Do(opts ...googleapi.CallOption) (*Empty, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsEnrollDataSourcesCall.Do)
    *   [func (c *ProjectsLocationsEnrollDataSourcesCall) Fields(s ...googleapi.Field) *ProjectsLocationsEnrollDataSourcesCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsEnrollDataSourcesCall.Fields)
    *   [func (c *ProjectsLocationsEnrollDataSourcesCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsEnrollDataSourcesCall.Header)

*   [type ProjectsLocationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsGetCall)
*       *   [func (c *ProjectsLocationsGetCall) Context(ctx context.Context) *ProjectsLocationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsGetCall.Context)
    *   [func (c *ProjectsLocationsGetCall) Do(opts ...googleapi.CallOption) (*Location, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsGetCall.Do)
    *   [func (c *ProjectsLocationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsGetCall.Fields)
    *   [func (c *ProjectsLocationsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsGetCall.Header)
    *   [func (c *ProjectsLocationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsGetCall.IfNoneMatch)

*   [type ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsListCall)
*       *   [func (c *ProjectsLocationsListCall) Context(ctx context.Context) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsListCall.Context)
    *   [func (c *ProjectsLocationsListCall) Do(opts ...googleapi.CallOption) (*ListLocationsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsListCall.Do)
    *   [func (c *ProjectsLocationsListCall) ExtraLocationTypes(extraLocationTypes ...string) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsListCall.ExtraLocationTypes)
    *   [func (c *ProjectsLocationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsListCall.Fields)
    *   [func (c *ProjectsLocationsListCall) Filter(filter string) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsListCall.Filter)
    *   [func (c *ProjectsLocationsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsListCall.Header)
    *   [func (c *ProjectsLocationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsListCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsListCall) PageSize(pageSize int64) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsListCall.PageSize)
    *   [func (c *ProjectsLocationsListCall) PageToken(pageToken string) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsListCall.PageToken)
    *   [func (c *ProjectsLocationsListCall) Pages(ctx context.Context, f func(*ListLocationsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsListCall.Pages)

*   [type ProjectsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsService)
*       *   [func NewProjectsLocationsService(s *Service) *ProjectsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#NewProjectsLocationsService)

*       *   [func (r *ProjectsLocationsService) EnrollDataSources(name string, enrolldatasourcesrequest *EnrollDataSourcesRequest) *ProjectsLocationsEnrollDataSourcesCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsService.EnrollDataSources)
    *   [func (r *ProjectsLocationsService) Get(name string) *ProjectsLocationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsService.Get)
    *   [func (r *ProjectsLocationsService) List(name string) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsService.List)
    *   [func (r *ProjectsLocationsService) UnenrollDataSources(name string, unenrolldatasourcesrequest *UnenrollDataSourcesRequest) *ProjectsLocationsUnenrollDataSourcesCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsService.UnenrollDataSources)

*   [type ProjectsLocationsTransferConfigsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsCreateCall)
*       *   [func (c *ProjectsLocationsTransferConfigsCreateCall) AuthorizationCode(authorizationCode string) *ProjectsLocationsTransferConfigsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsCreateCall.AuthorizationCode)
    *   [func (c *ProjectsLocationsTransferConfigsCreateCall) Context(ctx context.Context) *ProjectsLocationsTransferConfigsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsCreateCall.Context)
    *   [func (c *ProjectsLocationsTransferConfigsCreateCall) Do(opts ...googleapi.CallOption) (*TransferConfig, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsCreateCall.Do)
    *   [func (c *ProjectsLocationsTransferConfigsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsTransferConfigsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsCreateCall.Fields)
    *   [func (c *ProjectsLocationsTransferConfigsCreateCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsCreateCall.Header)
    *   [func (c *ProjectsLocationsTransferConfigsCreateCall) ServiceAccountName(serviceAccountName string) *ProjectsLocationsTransferConfigsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsCreateCall.ServiceAccountName)
    *   [func (c *ProjectsLocationsTransferConfigsCreateCall) VersionInfo(versionInfo string) *ProjectsLocationsTransferConfigsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsCreateCall.VersionInfo)

*   [type ProjectsLocationsTransferConfigsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsDeleteCall)
*       *   [func (c *ProjectsLocationsTransferConfigsDeleteCall) Context(ctx context.Context) *ProjectsLocationsTransferConfigsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsDeleteCall.Context)
    *   [func (c *ProjectsLocationsTransferConfigsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsDeleteCall.Do)
    *   [func (c *ProjectsLocationsTransferConfigsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsTransferConfigsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsDeleteCall.Fields)
    *   [func (c *ProjectsLocationsTransferConfigsDeleteCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsDeleteCall.Header)

*   [type ProjectsLocationsTransferConfigsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsGetCall)
*       *   [func (c *ProjectsLocationsTransferConfigsGetCall) Context(ctx context.Context) *ProjectsLocationsTransferConfigsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsGetCall.Context)
    *   [func (c *ProjectsLocationsTransferConfigsGetCall) Do(opts ...googleapi.CallOption) (*TransferConfig, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsGetCall.Do)
    *   [func (c *ProjectsLocationsTransferConfigsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsTransferConfigsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsGetCall.Fields)
    *   [func (c *ProjectsLocationsTransferConfigsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsGetCall.Header)
    *   [func (c *ProjectsLocationsTransferConfigsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsTransferConfigsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsGetCall.IfNoneMatch)

*   [type ProjectsLocationsTransferConfigsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsListCall)
*       *   [func (c *ProjectsLocationsTransferConfigsListCall) Context(ctx context.Context) *ProjectsLocationsTransferConfigsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsListCall.Context)
    *   [func (c *ProjectsLocationsTransferConfigsListCall) DataSourceIds(dataSourceIds ...string) *ProjectsLocationsTransferConfigsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsListCall.DataSourceIds)
    *   [func (c *ProjectsLocationsTransferConfigsListCall) Do(opts ...googleapi.CallOption) (*ListTransferConfigsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsListCall.Do)
    *   [func (c *ProjectsLocationsTransferConfigsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsTransferConfigsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsListCall.Fields)
    *   [func (c *ProjectsLocationsTransferConfigsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsListCall.Header)
    *   [func (c *ProjectsLocationsTransferConfigsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsTransferConfigsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsListCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsTransferConfigsListCall) PageSize(pageSize int64) *ProjectsLocationsTransferConfigsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsListCall.PageSize)
    *   [func (c *ProjectsLocationsTransferConfigsListCall) PageToken(pageToken string) *ProjectsLocationsTransferConfigsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsListCall.PageToken)
    *   [func (c *ProjectsLocationsTransferConfigsListCall) Pages(ctx context.Context, f func(*ListTransferConfigsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsListCall.Pages)

*   [type ProjectsLocationsTransferConfigsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsPatchCall)
*       *   [func (c *ProjectsLocationsTransferConfigsPatchCall) AuthorizationCode(authorizationCode string) *ProjectsLocationsTransferConfigsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsPatchCall.AuthorizationCode)
    *   [func (c *ProjectsLocationsTransferConfigsPatchCall) Context(ctx context.Context) *ProjectsLocationsTransferConfigsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsPatchCall.Context)
    *   [func (c *ProjectsLocationsTransferConfigsPatchCall) Do(opts ...googleapi.CallOption) (*TransferConfig, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsPatchCall.Do)
    *   [func (c *ProjectsLocationsTransferConfigsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsTransferConfigsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsPatchCall.Fields)
    *   [func (c *ProjectsLocationsTransferConfigsPatchCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsPatchCall.Header)
    *   [func (c *ProjectsLocationsTransferConfigsPatchCall) ServiceAccountName(serviceAccountName string) *ProjectsLocationsTransferConfigsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsPatchCall.ServiceAccountName)
    *   [func (c *ProjectsLocationsTransferConfigsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsTransferConfigsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsPatchCall.UpdateMask)
    *   [func (c *ProjectsLocationsTransferConfigsPatchCall) VersionInfo(versionInfo string) *ProjectsLocationsTransferConfigsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsPatchCall.VersionInfo)

*   [type ProjectsLocationsTransferConfigsRunsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsDeleteCall)
*       *   [func (c *ProjectsLocationsTransferConfigsRunsDeleteCall) Context(ctx context.Context) *ProjectsLocationsTransferConfigsRunsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsDeleteCall.Context)
    *   [func (c *ProjectsLocationsTransferConfigsRunsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsDeleteCall.Do)
    *   [func (c *ProjectsLocationsTransferConfigsRunsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsTransferConfigsRunsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsDeleteCall.Fields)
    *   [func (c *ProjectsLocationsTransferConfigsRunsDeleteCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsDeleteCall.Header)

*   [type ProjectsLocationsTransferConfigsRunsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsGetCall)
*       *   [func (c *ProjectsLocationsTransferConfigsRunsGetCall) Context(ctx context.Context) *ProjectsLocationsTransferConfigsRunsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsGetCall.Context)
    *   [func (c *ProjectsLocationsTransferConfigsRunsGetCall) Do(opts ...googleapi.CallOption) (*TransferRun, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsGetCall.Do)
    *   [func (c *ProjectsLocationsTransferConfigsRunsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsTransferConfigsRunsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsGetCall.Fields)
    *   [func (c *ProjectsLocationsTransferConfigsRunsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsGetCall.Header)
    *   [func (c *ProjectsLocationsTransferConfigsRunsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsTransferConfigsRunsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsGetCall.IfNoneMatch)

*   [type ProjectsLocationsTransferConfigsRunsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsListCall)
*       *   [func (c *ProjectsLocationsTransferConfigsRunsListCall) Context(ctx context.Context) *ProjectsLocationsTransferConfigsRunsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsListCall.Context)
    *   [func (c *ProjectsLocationsTransferConfigsRunsListCall) Do(opts ...googleapi.CallOption) (*ListTransferRunsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsListCall.Do)
    *   [func (c *ProjectsLocationsTransferConfigsRunsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsTransferConfigsRunsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsListCall.Fields)
    *   [func (c *ProjectsLocationsTransferConfigsRunsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsListCall.Header)
    *   [func (c *ProjectsLocationsTransferConfigsRunsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsTransferConfigsRunsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsListCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsTransferConfigsRunsListCall) PageSize(pageSize int64) *ProjectsLocationsTransferConfigsRunsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsListCall.PageSize)
    *   [func (c *ProjectsLocationsTransferConfigsRunsListCall) PageToken(pageToken string) *ProjectsLocationsTransferConfigsRunsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsListCall.PageToken)
    *   [func (c *ProjectsLocationsTransferConfigsRunsListCall) Pages(ctx context.Context, f func(*ListTransferRunsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsListCall.Pages)
    *   [func (c *ProjectsLocationsTransferConfigsRunsListCall) RunAttempt(runAttempt string) *ProjectsLocationsTransferConfigsRunsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsListCall.RunAttempt)
    *   [func (c *ProjectsLocationsTransferConfigsRunsListCall) States(states ...string) *ProjectsLocationsTransferConfigsRunsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsListCall.States)

*   [type ProjectsLocationsTransferConfigsRunsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsService)
*       *   [func NewProjectsLocationsTransferConfigsRunsService(s *Service) *ProjectsLocationsTransferConfigsRunsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#NewProjectsLocationsTransferConfigsRunsService)

*       *   [func (r *ProjectsLocationsTransferConfigsRunsService) Delete(name string) *ProjectsLocationsTransferConfigsRunsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsService.Delete)
    *   [func (r *ProjectsLocationsTransferConfigsRunsService) Get(name string) *ProjectsLocationsTransferConfigsRunsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsService.Get)
    *   [func (r *ProjectsLocationsTransferConfigsRunsService) List(parent string) *ProjectsLocationsTransferConfigsRunsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsService.List)

*   [type ProjectsLocationsTransferConfigsRunsTransferLogsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsTransferLogsListCall)
*       *   [func (c *ProjectsLocationsTransferConfigsRunsTransferLogsListCall) Context(ctx context.Context) *ProjectsLocationsTransferConfigsRunsTransferLogsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsTransferLogsListCall.Context)
    *   [func (c *ProjectsLocationsTransferConfigsRunsTransferLogsListCall) Do(opts ...googleapi.CallOption) (*ListTransferLogsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsTransferLogsListCall.Do)
    *   [func (c *ProjectsLocationsTransferConfigsRunsTransferLogsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsTransferConfigsRunsTransferLogsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsTransferLogsListCall.Fields)
    *   [func (c *ProjectsLocationsTransferConfigsRunsTransferLogsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsTransferLogsListCall.Header)
    *   [func (c *ProjectsLocationsTransferConfigsRunsTransferLogsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsTransferConfigsRunsTransferLogsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsTransferLogsListCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsTransferConfigsRunsTransferLogsListCall) MessageTypes(messageTypes ...string) *ProjectsLocationsTransferConfigsRunsTransferLogsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsTransferLogsListCall.MessageTypes)
    *   [func (c *ProjectsLocationsTransferConfigsRunsTransferLogsListCall) PageSize(pageSize int64) *ProjectsLocationsTransferConfigsRunsTransferLogsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsTransferLogsListCall.PageSize)
    *   [func (c *ProjectsLocationsTransferConfigsRunsTransferLogsListCall) PageToken(pageToken string) *ProjectsLocationsTransferConfigsRunsTransferLogsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsTransferLogsListCall.PageToken)
    *   [func (c *ProjectsLocationsTransferConfigsRunsTransferLogsListCall) Pages(ctx context.Context, f func(*ListTransferLogsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsTransferLogsListCall.Pages)

*   [type ProjectsLocationsTransferConfigsRunsTransferLogsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsTransferLogsService)
*       *   [func NewProjectsLocationsTransferConfigsRunsTransferLogsService(s *Service) *ProjectsLocationsTransferConfigsRunsTransferLogsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#NewProjectsLocationsTransferConfigsRunsTransferLogsService)

*       *   [func (r *ProjectsLocationsTransferConfigsRunsTransferLogsService) List(parent string) *ProjectsLocationsTransferConfigsRunsTransferLogsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsTransferLogsService.List)

*   [type ProjectsLocationsTransferConfigsScheduleRunsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsScheduleRunsCall)
*       *   [func (c *ProjectsLocationsTransferConfigsScheduleRunsCall) Context(ctx context.Context) *ProjectsLocationsTransferConfigsScheduleRunsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsScheduleRunsCall.Context)
    *   [func (c *ProjectsLocationsTransferConfigsScheduleRunsCall) Do(opts ...googleapi.CallOption) (*ScheduleTransferRunsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsScheduleRunsCall.Do)
    *   [func (c *ProjectsLocationsTransferConfigsScheduleRunsCall) Fields(s ...googleapi.Field) *ProjectsLocationsTransferConfigsScheduleRunsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsScheduleRunsCall.Fields)
    *   [func (c *ProjectsLocationsTransferConfigsScheduleRunsCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsScheduleRunsCall.Header)

*   [type ProjectsLocationsTransferConfigsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsService)
*       *   [func NewProjectsLocationsTransferConfigsService(s *Service) *ProjectsLocationsTransferConfigsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#NewProjectsLocationsTransferConfigsService)

*       *   [func (r *ProjectsLocationsTransferConfigsService) Create(parent string, transferconfig *TransferConfig) *ProjectsLocationsTransferConfigsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsService.Create)
    *   [func (r *ProjectsLocationsTransferConfigsService) Delete(name string) *ProjectsLocationsTransferConfigsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsService.Delete)
    *   [func (r *ProjectsLocationsTransferConfigsService) Get(name string) *ProjectsLocationsTransferConfigsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsService.Get)
    *   [func (r *ProjectsLocationsTransferConfigsService) List(parent string) *ProjectsLocationsTransferConfigsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsService.List)
    *   [func (r *ProjectsLocationsTransferConfigsService) Patch(name string, transferconfig *TransferConfig) *ProjectsLocationsTransferConfigsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsService.Patch)
    *   [func (r *ProjectsLocationsTransferConfigsService) ScheduleRuns(parent string, scheduletransferrunsrequest *ScheduleTransferRunsRequest) *ProjectsLocationsTransferConfigsScheduleRunsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsService.ScheduleRuns)
    *   [func (r *ProjectsLocationsTransferConfigsService) StartManualRuns(parent string, startmanualtransferrunsrequest *StartManualTransferRunsRequest) *ProjectsLocationsTransferConfigsStartManualRunsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsService.StartManualRuns)

*   [type ProjectsLocationsTransferConfigsStartManualRunsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsStartManualRunsCall)
*       *   [func (c *ProjectsLocationsTransferConfigsStartManualRunsCall) Context(ctx context.Context) *ProjectsLocationsTransferConfigsStartManualRunsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsStartManualRunsCall.Context)
    *   [func (c *ProjectsLocationsTransferConfigsStartManualRunsCall) Do(opts ...googleapi.CallOption) (*StartManualTransferRunsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsStartManualRunsCall.Do)
    *   [func (c *ProjectsLocationsTransferConfigsStartManualRunsCall) Fields(s ...googleapi.Field) *ProjectsLocationsTransferConfigsStartManualRunsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsStartManualRunsCall.Fields)
    *   [func (c *ProjectsLocationsTransferConfigsStartManualRunsCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsStartManualRunsCall.Header)

*   [type ProjectsLocationsUnenrollDataSourcesCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsUnenrollDataSourcesCall)
*       *   [func (c *ProjectsLocationsUnenrollDataSourcesCall) Context(ctx context.Context) *ProjectsLocationsUnenrollDataSourcesCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsUnenrollDataSourcesCall.Context)
    *   [func (c *ProjectsLocationsUnenrollDataSourcesCall) Do(opts ...googleapi.CallOption) (*Empty, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsUnenrollDataSourcesCall.Do)
    *   [func (c *ProjectsLocationsUnenrollDataSourcesCall) Fields(s ...googleapi.Field) *ProjectsLocationsUnenrollDataSourcesCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsUnenrollDataSourcesCall.Fields)
    *   [func (c *ProjectsLocationsUnenrollDataSourcesCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsUnenrollDataSourcesCall.Header)

*   [type ProjectsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsService)
*       *   [func NewProjectsService(s *Service) *ProjectsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#NewProjectsService)

*       *   [func (r *ProjectsService) EnrollDataSources(name string, enrolldatasourcesrequest *EnrollDataSourcesRequest) *ProjectsEnrollDataSourcesCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsService.EnrollDataSources)

*   [type ProjectsTransferConfigsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsCreateCall)
*       *   [func (c *ProjectsTransferConfigsCreateCall) AuthorizationCode(authorizationCode string) *ProjectsTransferConfigsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsCreateCall.AuthorizationCode)
    *   [func (c *ProjectsTransferConfigsCreateCall) Context(ctx context.Context) *ProjectsTransferConfigsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsCreateCall.Context)
    *   [func (c *ProjectsTransferConfigsCreateCall) Do(opts ...googleapi.CallOption) (*TransferConfig, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsCreateCall.Do)
    *   [func (c *ProjectsTransferConfigsCreateCall) Fields(s ...googleapi.Field) *ProjectsTransferConfigsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsCreateCall.Fields)
    *   [func (c *ProjectsTransferConfigsCreateCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsCreateCall.Header)
    *   [func (c *ProjectsTransferConfigsCreateCall) ServiceAccountName(serviceAccountName string) *ProjectsTransferConfigsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsCreateCall.ServiceAccountName)
    *   [func (c *ProjectsTransferConfigsCreateCall) VersionInfo(versionInfo string) *ProjectsTransferConfigsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsCreateCall.VersionInfo)

*   [type ProjectsTransferConfigsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsDeleteCall)
*       *   [func (c *ProjectsTransferConfigsDeleteCall) Context(ctx context.Context) *ProjectsTransferConfigsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsDeleteCall.Context)
    *   [func (c *ProjectsTransferConfigsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsDeleteCall.Do)
    *   [func (c *ProjectsTransferConfigsDeleteCall) Fields(s ...googleapi.Field) *ProjectsTransferConfigsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsDeleteCall.Fields)
    *   [func (c *ProjectsTransferConfigsDeleteCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsDeleteCall.Header)

*   [type ProjectsTransferConfigsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsGetCall)
*       *   [func (c *ProjectsTransferConfigsGetCall) Context(ctx context.Context) *ProjectsTransferConfigsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsGetCall.Context)
    *   [func (c *ProjectsTransferConfigsGetCall) Do(opts ...googleapi.CallOption) (*TransferConfig, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsGetCall.Do)
    *   [func (c *ProjectsTransferConfigsGetCall) Fields(s ...googleapi.Field) *ProjectsTransferConfigsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsGetCall.Fields)
    *   [func (c *ProjectsTransferConfigsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsGetCall.Header)
    *   [func (c *ProjectsTransferConfigsGetCall) IfNoneMatch(entityTag string) *ProjectsTransferConfigsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsGetCall.IfNoneMatch)

*   [type ProjectsTransferConfigsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsListCall)
*       *   [func (c *ProjectsTransferConfigsListCall) Context(ctx context.Context) *ProjectsTransferConfigsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsListCall.Context)
    *   [func (c *ProjectsTransferConfigsListCall) DataSourceIds(dataSourceIds ...string) *ProjectsTransferConfigsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsListCall.DataSourceIds)
    *   [func (c *ProjectsTransferConfigsListCall) Do(opts ...googleapi.CallOption) (*ListTransferConfigsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsListCall.Do)
    *   [func (c *ProjectsTransferConfigsListCall) Fields(s ...googleapi.Field) *ProjectsTransferConfigsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsListCall.Fields)
    *   [func (c *ProjectsTransferConfigsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsListCall.Header)
    *   [func (c *ProjectsTransferConfigsListCall) IfNoneMatch(entityTag string) *ProjectsTransferConfigsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsListCall.IfNoneMatch)
    *   [func (c *ProjectsTransferConfigsListCall) PageSize(pageSize int64) *ProjectsTransferConfigsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsListCall.PageSize)
    *   [func (c *ProjectsTransferConfigsListCall) PageToken(pageToken string) *ProjectsTransferConfigsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsListCall.PageToken)
    *   [func (c *ProjectsTransferConfigsListCall) Pages(ctx context.Context, f func(*ListTransferConfigsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsListCall.Pages)

*   [type ProjectsTransferConfigsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsPatchCall)
*       *   [func (c *ProjectsTransferConfigsPatchCall) AuthorizationCode(authorizationCode string) *ProjectsTransferConfigsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsPatchCall.AuthorizationCode)
    *   [func (c *ProjectsTransferConfigsPatchCall) Context(ctx context.Context) *ProjectsTransferConfigsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsPatchCall.Context)
    *   [func (c *ProjectsTransferConfigsPatchCall) Do(opts ...googleapi.CallOption) (*TransferConfig, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsPatchCall.Do)
    *   [func (c *ProjectsTransferConfigsPatchCall) Fields(s ...googleapi.Field) *ProjectsTransferConfigsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsPatchCall.Fields)
    *   [func (c *ProjectsTransferConfigsPatchCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsPatchCall.Header)
    *   [func (c *ProjectsTransferConfigsPatchCall) ServiceAccountName(serviceAccountName string) *ProjectsTransferConfigsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsPatchCall.ServiceAccountName)
    *   [func (c *ProjectsTransferConfigsPatchCall) UpdateMask(updateMask string) *ProjectsTransferConfigsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsPatchCall.UpdateMask)
    *   [func (c *ProjectsTransferConfigsPatchCall) VersionInfo(versionInfo string) *ProjectsTransferConfigsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsPatchCall.VersionInfo)

*   [type ProjectsTransferConfigsRunsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsDeleteCall)
*       *   [func (c *ProjectsTransferConfigsRunsDeleteCall) Context(ctx context.Context) *ProjectsTransferConfigsRunsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsDeleteCall.Context)
    *   [func (c *ProjectsTransferConfigsRunsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsDeleteCall.Do)
    *   [func (c *ProjectsTransferConfigsRunsDeleteCall) Fields(s ...googleapi.Field) *ProjectsTransferConfigsRunsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsDeleteCall.Fields)
    *   [func (c *ProjectsTransferConfigsRunsDeleteCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsDeleteCall.Header)

*   [type ProjectsTransferConfigsRunsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsGetCall)
*       *   [func (c *ProjectsTransferConfigsRunsGetCall) Context(ctx context.Context) *ProjectsTransferConfigsRunsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsGetCall.Context)
    *   [func (c *ProjectsTransferConfigsRunsGetCall) Do(opts ...googleapi.CallOption) (*TransferRun, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsGetCall.Do)
    *   [func (c *ProjectsTransferConfigsRunsGetCall) Fields(s ...googleapi.Field) *ProjectsTransferConfigsRunsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsGetCall.Fields)
    *   [func (c *ProjectsTransferConfigsRunsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsGetCall.Header)
    *   [func (c *ProjectsTransferConfigsRunsGetCall) IfNoneMatch(entityTag string) *ProjectsTransferConfigsRunsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsGetCall.IfNoneMatch)

*   [type ProjectsTransferConfigsRunsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsListCall)
*       *   [func (c *ProjectsTransferConfigsRunsListCall) Context(ctx context.Context) *ProjectsTransferConfigsRunsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsListCall.Context)
    *   [func (c *ProjectsTransferConfigsRunsListCall) Do(opts ...googleapi.CallOption) (*ListTransferRunsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsListCall.Do)
    *   [func (c *ProjectsTransferConfigsRunsListCall) Fields(s ...googleapi.Field) *ProjectsTransferConfigsRunsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsListCall.Fields)
    *   [func (c *ProjectsTransferConfigsRunsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsListCall.Header)
    *   [func (c *ProjectsTransferConfigsRunsListCall) IfNoneMatch(entityTag string) *ProjectsTransferConfigsRunsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsListCall.IfNoneMatch)
    *   [func (c *ProjectsTransferConfigsRunsListCall) PageSize(pageSize int64) *ProjectsTransferConfigsRunsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsListCall.PageSize)
    *   [func (c *ProjectsTransferConfigsRunsListCall) PageToken(pageToken string) *ProjectsTransferConfigsRunsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsListCall.PageToken)
    *   [func (c *ProjectsTransferConfigsRunsListCall) Pages(ctx context.Context, f func(*ListTransferRunsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsListCall.Pages)
    *   [func (c *ProjectsTransferConfigsRunsListCall) RunAttempt(runAttempt string) *ProjectsTransferConfigsRunsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsListCall.RunAttempt)
    *   [func (c *ProjectsTransferConfigsRunsListCall) States(states ...string) *ProjectsTransferConfigsRunsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsListCall.States)

*   [type ProjectsTransferConfigsRunsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsService)
*       *   [func NewProjectsTransferConfigsRunsService(s *Service) *ProjectsTransferConfigsRunsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#NewProjectsTransferConfigsRunsService)

*       *   [func (r *ProjectsTransferConfigsRunsService) Delete(name string) *ProjectsTransferConfigsRunsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsService.Delete)
    *   [func (r *ProjectsTransferConfigsRunsService) Get(name string) *ProjectsTransferConfigsRunsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsService.Get)
    *   [func (r *ProjectsTransferConfigsRunsService) List(parent string) *ProjectsTransferConfigsRunsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsService.List)

*   [type ProjectsTransferConfigsRunsTransferLogsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsTransferLogsListCall)
*       *   [func (c *ProjectsTransferConfigsRunsTransferLogsListCall) Context(ctx context.Context) *ProjectsTransferConfigsRunsTransferLogsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsTransferLogsListCall.Context)
    *   [func (c *ProjectsTransferConfigsRunsTransferLogsListCall) Do(opts ...googleapi.CallOption) (*ListTransferLogsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsTransferLogsListCall.Do)
    *   [func (c *ProjectsTransferConfigsRunsTransferLogsListCall) Fields(s ...googleapi.Field) *ProjectsTransferConfigsRunsTransferLogsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsTransferLogsListCall.Fields)
    *   [func (c *ProjectsTransferConfigsRunsTransferLogsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsTransferLogsListCall.Header)
    *   [func (c *ProjectsTransferConfigsRunsTransferLogsListCall) IfNoneMatch(entityTag string) *ProjectsTransferConfigsRunsTransferLogsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsTransferLogsListCall.IfNoneMatch)
    *   [func (c *ProjectsTransferConfigsRunsTransferLogsListCall) MessageTypes(messageTypes ...string) *ProjectsTransferConfigsRunsTransferLogsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsTransferLogsListCall.MessageTypes)
    *   [func (c *ProjectsTransferConfigsRunsTransferLogsListCall) PageSize(pageSize int64) *ProjectsTransferConfigsRunsTransferLogsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsTransferLogsListCall.PageSize)
    *   [func (c *ProjectsTransferConfigsRunsTransferLogsListCall) PageToken(pageToken string) *ProjectsTransferConfigsRunsTransferLogsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsTransferLogsListCall.PageToken)
    *   [func (c *ProjectsTransferConfigsRunsTransferLogsListCall) Pages(ctx context.Context, f func(*ListTransferLogsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsTransferLogsListCall.Pages)

*   [type ProjectsTransferConfigsRunsTransferLogsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsTransferLogsService)
*       *   [func NewProjectsTransferConfigsRunsTransferLogsService(s *Service) *ProjectsTransferConfigsRunsTransferLogsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#NewProjectsTransferConfigsRunsTransferLogsService)

*       *   [func (r *ProjectsTransferConfigsRunsTransferLogsService) List(parent string) *ProjectsTransferConfigsRunsTransferLogsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsTransferLogsService.List)

*   [type ProjectsTransferConfigsScheduleRunsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsScheduleRunsCall)
*       *   [func (c *ProjectsTransferConfigsScheduleRunsCall) Context(ctx context.Context) *ProjectsTransferConfigsScheduleRunsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsScheduleRunsCall.Context)
    *   [func (c *ProjectsTransferConfigsScheduleRunsCall) Do(opts ...googleapi.CallOption) (*ScheduleTransferRunsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsScheduleRunsCall.Do)
    *   [func (c *ProjectsTransferConfigsScheduleRunsCall) Fields(s ...googleapi.Field) *ProjectsTransferConfigsScheduleRunsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsScheduleRunsCall.Fields)
    *   [func (c *ProjectsTransferConfigsScheduleRunsCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsScheduleRunsCall.Header)

*   [type ProjectsTransferConfigsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsService)
*       *   [func NewProjectsTransferConfigsService(s *Service) *ProjectsTransferConfigsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#NewProjectsTransferConfigsService)

*       *   [func (r *ProjectsTransferConfigsService) Create(parent string, transferconfig *TransferConfig) *ProjectsTransferConfigsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsService.Create)
    *   [func (r *ProjectsTransferConfigsService) Delete(name string) *ProjectsTransferConfigsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsService.Delete)
    *   [func (r *ProjectsTransferConfigsService) Get(name string) *ProjectsTransferConfigsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsService.Get)
    *   [func (r *ProjectsTransferConfigsService) List(parent string) *ProjectsTransferConfigsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsService.List)
    *   [func (r *ProjectsTransferConfigsService) Patch(name string, transferconfig *TransferConfig) *ProjectsTransferConfigsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsService.Patch)
    *   [func (r *ProjectsTransferConfigsService) ScheduleRuns(parent string, scheduletransferrunsrequest *ScheduleTransferRunsRequest) *ProjectsTransferConfigsScheduleRunsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsService.ScheduleRuns)
    *   [func (r *ProjectsTransferConfigsService) StartManualRuns(parent string, startmanualtransferrunsrequest *StartManualTransferRunsRequest) *ProjectsTransferConfigsStartManualRunsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsService.StartManualRuns)

*   [type ProjectsTransferConfigsStartManualRunsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsStartManualRunsCall)
*       *   [func (c *ProjectsTransferConfigsStartManualRunsCall) Context(ctx context.Context) *ProjectsTransferConfigsStartManualRunsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsStartManualRunsCall.Context)
    *   [func (c *ProjectsTransferConfigsStartManualRunsCall) Do(opts ...googleapi.CallOption) (*StartManualTransferRunsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsStartManualRunsCall.Do)
    *   [func (c *ProjectsTransferConfigsStartManualRunsCall) Fields(s ...googleapi.Field) *ProjectsTransferConfigsStartManualRunsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsStartManualRunsCall.Fields)
    *   [func (c *ProjectsTransferConfigsStartManualRunsCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsStartManualRunsCall.Header)

*   [type ScheduleOptions](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ScheduleOptions)
*       *   [func (s ScheduleOptions) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ScheduleOptions.MarshalJSON)

*   [type ScheduleOptionsV2](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ScheduleOptionsV2)
*       *   [func (s ScheduleOptionsV2) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ScheduleOptionsV2.MarshalJSON)

*   [type ScheduleTransferRunsRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ScheduleTransferRunsRequest)
*       *   [func (s ScheduleTransferRunsRequest) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ScheduleTransferRunsRequest.MarshalJSON)

*   [type ScheduleTransferRunsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ScheduleTransferRunsResponse)
*       *   [func (s ScheduleTransferRunsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ScheduleTransferRunsResponse.MarshalJSON)

*   [type Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#Service)
*       *   [func New(client *http.Client) (*Service, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#New)deprecated
    *   [func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#NewService)

*   [type StartManualTransferRunsRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#StartManualTransferRunsRequest)
*       *   [func (s StartManualTransferRunsRequest) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#StartManualTransferRunsRequest.MarshalJSON)

*   [type StartManualTransferRunsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#StartManualTransferRunsResponse)
*       *   [func (s StartManualTransferRunsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#StartManualTransferRunsResponse.MarshalJSON)

*   [type Status](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#Status)
*       *   [func (s Status) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#Status.MarshalJSON)

*   [type TimeBasedSchedule](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#TimeBasedSchedule)
*       *   [func (s TimeBasedSchedule) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#TimeBasedSchedule.MarshalJSON)

*   [type TimeRange](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#TimeRange)
*       *   [func (s TimeRange) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#TimeRange.MarshalJSON)

*   [type TransferConfig](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#TransferConfig)
*       *   [func (s TransferConfig) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#TransferConfig.MarshalJSON)

*   [type TransferMessage](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#TransferMessage)
*       *   [func (s TransferMessage) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#TransferMessage.MarshalJSON)

*   [type TransferRun](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#TransferRun)
*       *   [func (s TransferRun) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#TransferRun.MarshalJSON)

*   [type UnenrollDataSourcesRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#UnenrollDataSourcesRequest)
*       *   [func (s UnenrollDataSourcesRequest) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#UnenrollDataSourcesRequest.MarshalJSON)

*   [type UserInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#UserInfo)
*       *   [func (s UserInfo) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#UserInfo.MarshalJSON)

[View Source](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/bigquerydatatransfer/v1/bigquerydatatransfer-gen.go#L105)

const (
	
	BigqueryScope = "https://www.googleapis.com/auth/bigquery"

	
	CloudPlatformScope = "https://www.googleapis.com/auth/cloud-platform"

	
	CloudPlatformReadOnlyScope = "https://www.googleapis.com/auth/cloud-platform.read-only"
)

OAuth2 scopes used by this API.

This section is empty.

This section is empty.

type CheckValidCredsRequest struct {
}

CheckValidCredsRequest: A request to determine whether the user has valid credentials. This method is used to limit the number of OAuth popups in the user interface. The user id is inferred from the API call context. If the data source has the Google+ authorization type, this method returns false, as it cannot be determined whether the credentials are already valid merely based on the user id.

CheckValidCredsResponse: A response indicating whether the credentials exist and are valid.

type DataSource struct {
	
	
	
	
	
	
	
	
	
	AuthorizationType [string](https://pkg.go.dev/builtin#string) `json:"authorizationType,omitempty"`
	
	ClientId [string](https://pkg.go.dev/builtin#string) `json:"clientId,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	
	
	DataRefreshType [string](https://pkg.go.dev/builtin#string) `json:"dataRefreshType,omitempty"`
	DataSourceId [string](https://pkg.go.dev/builtin#string) `json:"dataSourceId,omitempty"`
	
	DefaultDataRefreshWindowDays [int64](https://pkg.go.dev/builtin#int64) `json:"defaultDataRefreshWindowDays,omitempty"`
	
	
	DefaultSchedule [string](https://pkg.go.dev/builtin#string) `json:"defaultSchedule,omitempty"`
	Description [string](https://pkg.go.dev/builtin#string) `json:"description,omitempty"`
	DisplayName [string](https://pkg.go.dev/builtin#string) `json:"displayName,omitempty"`
	HelpUrl [string](https://pkg.go.dev/builtin#string) `json:"helpUrl,omitempty"`
	
	ManualRunsDisabled [bool](https://pkg.go.dev/builtin#bool) `json:"manualRunsDisabled,omitempty"`
	
	MinimumScheduleInterval [string](https://pkg.go.dev/builtin#string) `json:"minimumScheduleInterval,omitempty"`
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	Parameters []*[DataSourceParameter](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#DataSourceParameter) `json:"parameters,omitempty"`
	
	
	Scopes [][string](https://pkg.go.dev/builtin#string) `json:"scopes,omitempty"`
	
	
	SupportsCustomSchedule [bool](https://pkg.go.dev/builtin#bool) `json:"supportsCustomSchedule,omitempty"`
	SupportsMultipleTransfers [bool](https://pkg.go.dev/builtin#bool) `json:"supportsMultipleTransfers,omitempty"`
	
	
	
	
	
	
	
	TransferType [string](https://pkg.go.dev/builtin#string) `json:"transferType,omitempty"`
	
	UpdateDeadlineSeconds [int64](https://pkg.go.dev/builtin#int64) `json:"updateDeadlineSeconds,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

DataSource: Defines the properties and custom parameters for a data source.

type DataSourceParameter struct {
	AllowedValues [][string](https://pkg.go.dev/builtin#string) `json:"allowedValues,omitempty"`
	
	Deprecated [bool](https://pkg.go.dev/builtin#bool) `json:"deprecated,omitempty"`
	Description [string](https://pkg.go.dev/builtin#string) `json:"description,omitempty"`
	DisplayName [string](https://pkg.go.dev/builtin#string) `json:"displayName,omitempty"`
	Fields []*[DataSourceParameter](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#DataSourceParameter) `json:"fields,omitempty"`
	Immutable [bool](https://pkg.go.dev/builtin#bool) `json:"immutable,omitempty"`
	MaxListSize [int64](https://pkg.go.dev/builtin#int64) `json:"maxListSize,omitempty,string"`
	MaxValue [float64](https://pkg.go.dev/builtin#float64) `json:"maxValue,omitempty"`
	MinValue [float64](https://pkg.go.dev/builtin#float64) `json:"minValue,omitempty"`
	ParamId [string](https://pkg.go.dev/builtin#string) `json:"paramId,omitempty"`
	Recurse [bool](https://pkg.go.dev/builtin#bool) `json:"recurse,omitempty"`
	Repeated [bool](https://pkg.go.dev/builtin#bool) `json:"repeated,omitempty"`
	Required [bool](https://pkg.go.dev/builtin#bool) `json:"required,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	Type [string](https://pkg.go.dev/builtin#string) `json:"type,omitempty"`
	
	ValidationDescription [string](https://pkg.go.dev/builtin#string) `json:"validationDescription,omitempty"`
	
	ValidationHelpUrl [string](https://pkg.go.dev/builtin#string) `json:"validationHelpUrl,omitempty"`
	
	ValidationRegex [string](https://pkg.go.dev/builtin#string) `json:"validationRegex,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

DataSourceParameter: A parameter used to define custom fields in a data source definition.

type EmailPreferences struct {
	
	EnableFailureEmail [bool](https://pkg.go.dev/builtin#bool) `json:"enableFailureEmail,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

EmailPreferences: Represents preferences for sending email notifications for transfer run events.

Empty: A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }

type EncryptionConfiguration struct {
	KmsKeyName [string](https://pkg.go.dev/builtin#string) `json:"kmsKeyName,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

EncryptionConfiguration: Represents the encryption configuration for a transfer.

type EnrollDataSourcesRequest struct {
	
	DataSourceIds [][string](https://pkg.go.dev/builtin#string) `json:"dataSourceIds,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

EnrollDataSourcesRequest: A request to enroll a set of data sources so they are visible in the BigQuery UI's `Transfer` tab.

type EventDrivenSchedule struct {
	
	
	PubsubSubscription [string](https://pkg.go.dev/builtin#string) `json:"pubsubSubscription,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

EventDrivenSchedule: Options customizing EventDriven transfers schedule.

type ListDataSourcesResponse struct {
	DataSources []*[DataSource](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#DataSource) `json:"dataSources,omitempty"`
	
	
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListDataSourcesResponse: Returns list of supported data sources and their metadata.

type ListLocationsResponse struct {
	
	Locations []*[Location](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#Location) `json:"locations,omitempty"`
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListLocationsResponse: The response message for Locations.ListLocations.

type ListTransferConfigsResponse struct {
	
	
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`
	TransferConfigs []*[TransferConfig](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#TransferConfig) `json:"transferConfigs,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListTransferConfigsResponse: The returned list of pipelines in the project.

type ListTransferLogsResponse struct {
	
	
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`
	TransferMessages []*[TransferMessage](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#TransferMessage) `json:"transferMessages,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListTransferLogsResponse: The returned list transfer run messages.

type ListTransferRunsResponse struct {
	
	
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`
	TransferRuns []*[TransferRun](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#TransferRun) `json:"transferRuns,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListTransferRunsResponse: The returned list of pipelines in the project.

Location: A resource that represents a Google Cloud location.

type ManualSchedule struct {
}

ManualSchedule: Options customizing manual transfers schedule.

type ProjectsDataSourcesCheckValidCredsCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "bigquerydatatransfer.projects.dataSources.checkValidCreds" call. Any non-2xx status code is an error. Response headers are in either *CheckValidCredsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsDataSourcesGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "bigquerydatatransfer.projects.dataSources.get" call. Any non-2xx status code is an error. Response headers are in either *DataSource.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsDataSourcesListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "bigquerydatatransfer.projects.dataSources.list" call. Any non-2xx status code is an error. Response headers are in either *ListDataSourcesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": Page size. The default page size is the maximum value of 1000 results.

PageToken sets the optional parameter "pageToken": Pagination token, which can be used to request a specific page of `ListDataSourcesRequest` list results. For multiple-page results, `ListDataSourcesResponse` outputs a `next_page` token, which can be used as the `page_token` value to request the next page of list results.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsDataSourcesService struct {
	
}

func NewProjectsDataSourcesService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#Service)) *[ProjectsDataSourcesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsDataSourcesService)

CheckValidCreds: Returns true if valid credentials exist for the given data source and requesting user.

*   name: The name of the data source. If you are using the regionless method, the location must be `US` and the name should be in the following form: * `projects/{project_id}/dataSources/{data_source_id}` If you are using the regionalized method, the name should be in the following form: * `projects/{project_id}/locations/{location_id}/dataSources/{data_source_id} `.

Get: Retrieves a supported data source and returns its settings.

*   name: The name of the resource requested. If you are using the regionless method, the location must be `US` and the name should be in the following form: * `projects/{project_id}/dataSources/{data_source_id}` If you are using the regionalized method, the name should be in the following form: * `projects/{project_id}/locations/{location_id}/dataSources/{data_source_id} `.

List: Lists supported data sources and returns their settings.

*   parent: The BigQuery project id for which data sources should be returned. Must be in the form: `projects/{project_id}` or `projects/{project_id}/locations/{location_id}`.

type ProjectsEnrollDataSourcesCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "bigquerydatatransfer.projects.enrollDataSources" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsDataSourcesCheckValidCredsCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "bigquerydatatransfer.projects.locations.dataSources.checkValidCreds" call. Any non-2xx status code is an error. Response headers are in either *CheckValidCredsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsDataSourcesGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "bigquerydatatransfer.projects.locations.dataSources.get" call. Any non-2xx status code is an error. Response headers are in either *DataSource.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsDataSourcesListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "bigquerydatatransfer.projects.locations.dataSources.list" call. Any non-2xx status code is an error. Response headers are in either *ListDataSourcesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": Page size. The default page size is the maximum value of 1000 results.

PageToken sets the optional parameter "pageToken": Pagination token, which can be used to request a specific page of `ListDataSourcesRequest` list results. For multiple-page results, `ListDataSourcesResponse` outputs a `next_page` token, which can be used as the `page_token` value to request the next page of list results.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsDataSourcesService struct {
	
}

func NewProjectsLocationsDataSourcesService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#Service)) *[ProjectsLocationsDataSourcesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsDataSourcesService)

CheckValidCreds: Returns true if valid credentials exist for the given data source and requesting user.

*   name: The name of the data source. If you are using the regionless method, the location must be `US` and the name should be in the following form: * `projects/{project_id}/dataSources/{data_source_id}` If you are using the regionalized method, the name should be in the following form: * `projects/{project_id}/locations/{location_id}/dataSources/{data_source_id} `.

Get: Retrieves a supported data source and returns its settings.

*   name: The name of the resource requested. If you are using the regionless method, the location must be `US` and the name should be in the following form: * `projects/{project_id}/dataSources/{data_source_id}` If you are using the regionalized method, the name should be in the following form: * `projects/{project_id}/locations/{location_id}/dataSources/{data_source_id} `.

List: Lists supported data sources and returns their settings.

*   parent: The BigQuery project id for which data sources should be returned. Must be in the form: `projects/{project_id}` or `projects/{project_id}/locations/{location_id}`.

type ProjectsLocationsEnrollDataSourcesCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "bigquerydatatransfer.projects.locations.enrollDataSources" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "bigquerydatatransfer.projects.locations.get" call. Any non-2xx status code is an error. Response headers are in either *Location.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "bigquerydatatransfer.projects.locations.list" call. Any non-2xx status code is an error. Response headers are in either *ListLocationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (c *[ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsListCall)) ExtraLocationTypes(extraLocationTypes ...[string](https://pkg.go.dev/builtin#string)) *[ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsListCall)

ExtraLocationTypes sets the optional parameter "extraLocationTypes": Do not use this field. It is unsupported and is ignored unless explicitly documented otherwise. This is primarily for internal usage.

Filter sets the optional parameter "filter": A filter to narrow down results to a preferred subset. The filtering language accepts strings like "displayName=tokyo", and is documented in more detail in AIP-160 ([https://google.aip.dev/160](https://google.aip.dev/160)).

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": The maximum number of results to return. If not set, the service selects a default.

PageToken sets the optional parameter "pageToken": A page token received from the `next_page_token` field in the response. Send that page token to receive the subsequent page.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsService struct {
 DataSources *[ProjectsLocationsDataSourcesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsDataSourcesService)
 TransferConfigs *[ProjectsLocationsTransferConfigsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsService)	
}

func NewProjectsLocationsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#Service)) *[ProjectsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsService)

Get: Gets information about a location.

- name: Resource name for the location.

List: Lists information about the supported locations for this service. This method can be called in two ways: * **List all public locations:** Use the path `GET /v1/locations`. * **List project-visible locations:** Use the path `GET /v1/projects/{project_id}/locations`. This may include public locations as well as private or other locations specifically visible to the project.

- name: The resource that owns the locations collection, if applicable.

func (r *[ProjectsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsService)) UnenrollDataSources(name [string](https://pkg.go.dev/builtin#string), unenrolldatasourcesrequest *[UnenrollDataSourcesRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#UnenrollDataSourcesRequest)) *[ProjectsLocationsUnenrollDataSourcesCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsUnenrollDataSourcesCall)

UnenrollDataSources: Unenroll data sources in a user project. This allows users to remove transfer configurations for these data sources. They will no longer appear in the ListDataSources RPC and will also no longer appear in the BigQuery UI ([https://console.cloud.google.com/bigquery](https://console.cloud.google.com/bigquery)). Data transfers configurations of unenrolled data sources will not be scheduled.

*   name: The name of the project resource in the form: `projects/{project_id}`.

type ProjectsLocationsTransferConfigsCreateCall struct {
	
}

AuthorizationCode sets the optional parameter "authorizationCode": Deprecated: Authorization code was required when `transferConfig.dataSourceId` is 'youtube_channel' but it is no longer used in any data sources. Use `version_info` instead. Optional OAuth2 authorization code to use with this transfer configuration. This is required only if `transferConfig.dataSourceId` is 'youtube_channel' and new credentials are needed, as indicated by `CheckValidCreds`. In order to obtain authorization_code, make a request to the following URL: [https://bigquery.cloud.google.com/datatransfer/oauthz/auth?redirect_uri=urn:ietf:wg:oauth:2.0:oob&response_type=authorization_code&client_id=client_id&scope=data_source_scopes](https://bigquery.cloud.google.com/datatransfer/oauthz/auth?redirect_uri=urn:ietf:wg:oauth:2.0:oob&response_type=authorization_code&client_id=client_id&scope=data_source_scopes) * The client_id is the OAuth client_id of the data source as returned by ListDataSources method. * data_source_scopes are the scopes returned by ListDataSources method. Note that this should not be set when `service_account_name` is used to create the transfer config.

Context sets the context to be used in this call's Do method.

Do executes the "bigquerydatatransfer.projects.locations.transferConfigs.create" call. Any non-2xx status code is an error. Response headers are in either *TransferConfig.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

ServiceAccountName sets the optional parameter "serviceAccountName": Optional service account email. If this field is set, the transfer config will be created with this service account's credentials. It requires that the requesting user calling this API has permissions to act as this service account. Note that not all data sources support service account credentials when creating a transfer config. For the latest list of data sources, read about using service accounts ([https://cloud.google.com/bigquery-transfer/docs/use-service-accounts](https://cloud.google.com/bigquery-transfer/docs/use-service-accounts)).

type ProjectsLocationsTransferConfigsDeleteCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "bigquerydatatransfer.projects.locations.transferConfigs.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsTransferConfigsGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "bigquerydatatransfer.projects.locations.transferConfigs.get" call. Any non-2xx status code is an error. Response headers are in either *TransferConfig.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsTransferConfigsListCall struct {
	
}

Context sets the context to be used in this call's Do method.

DataSourceIds sets the optional parameter "dataSourceIds": When specified, only configurations of requested data sources are returned.

Do executes the "bigquerydatatransfer.projects.locations.transferConfigs.list" call. Any non-2xx status code is an error. Response headers are in either *ListTransferConfigsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": Page size. The default page size is the maximum value of 1000 results.

PageToken sets the optional parameter "pageToken": Pagination token, which can be used to request a specific page of `ListTransfersRequest` list results. For multiple-page results, `ListTransfersResponse` outputs a `next_page` token, which can be used as the `page_token` value to request the next page of list results.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsTransferConfigsPatchCall struct {
	
}

AuthorizationCode sets the optional parameter "authorizationCode": Deprecated: Authorization code was required when `transferConfig.dataSourceId` is 'youtube_channel' but it is no longer used in any data sources. Use `version_info` instead. Optional OAuth2 authorization code to use with this transfer configuration. This is required only if `transferConfig.dataSourceId` is 'youtube_channel' and new credentials are needed, as indicated by `CheckValidCreds`. In order to obtain authorization_code, make a request to the following URL: [https://bigquery.cloud.google.com/datatransfer/oauthz/auth?redirect_uri=urn:ietf:wg:oauth:2.0:oob&response_type=authorization_code&client_id=client_id&scope=data_source_scopes](https://bigquery.cloud.google.com/datatransfer/oauthz/auth?redirect_uri=urn:ietf:wg:oauth:2.0:oob&response_type=authorization_code&client_id=client_id&scope=data_source_scopes) * The client_id is the OAuth client_id of the data source as returned by ListDataSources method. * data_source_scopes are the scopes returned by ListDataSources method. Note that this should not be set when `service_account_name` is used to update the transfer config.

Context sets the context to be used in this call's Do method.

Do executes the "bigquerydatatransfer.projects.locations.transferConfigs.patch" call. Any non-2xx status code is an error. Response headers are in either *TransferConfig.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

ServiceAccountName sets the optional parameter "serviceAccountName": Optional service account email. If this field is set, the transfer config will be created with this service account's credentials. It requires that the requesting user calling this API has permissions to act as this service account. Note that not all data sources support service account credentials when creating a transfer config. For the latest list of data sources, read about using service accounts ([https://cloud.google.com/bigquery-transfer/docs/use-service-accounts](https://cloud.google.com/bigquery-transfer/docs/use-service-accounts)).

UpdateMask sets the optional parameter "updateMask": Required. Required list of fields to be updated in this request.

type ProjectsLocationsTransferConfigsRunsDeleteCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "bigquerydatatransfer.projects.locations.transferConfigs.runs.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsTransferConfigsRunsGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "bigquerydatatransfer.projects.locations.transferConfigs.runs.get" call. Any non-2xx status code is an error. Response headers are in either *TransferRun.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsTransferConfigsRunsListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "bigquerydatatransfer.projects.locations.transferConfigs.runs.list" call. Any non-2xx status code is an error. Response headers are in either *ListTransferRunsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": Page size. The default page size is the maximum value of 1000 results.

PageToken sets the optional parameter "pageToken": Pagination token, which can be used to request a specific page of `ListTransferRunsRequest` list results. For multiple-page results, `ListTransferRunsResponse` outputs a `next_page` token, which can be used as the `page_token` value to request the next page of list results.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

RunAttempt sets the optional parameter "runAttempt": Indicates how run attempts are to be pulled.

Possible values:

"RUN_ATTEMPT_UNSPECIFIED" - All runs should be returned.
"LATEST" - Only latest run per day should be returned.

States sets the optional parameter "states": When specified, only transfer runs with requested states are returned.

Possible values:

"TRANSFER_STATE_UNSPECIFIED" - State placeholder (0).
"PENDING" - Data transfer is scheduled and is waiting to be picked up by

data transfer backend (2).

"RUNNING" - Data transfer is in progress (3).
"SUCCEEDED" - Data transfer completed successfully (4).
"FAILED" - Data transfer failed (5).
"CANCELLED" - Data transfer is cancelled (6).

type ProjectsLocationsTransferConfigsRunsService struct {
 TransferLogs *[ProjectsLocationsTransferConfigsRunsTransferLogsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsTransferLogsService)	
}

func NewProjectsLocationsTransferConfigsRunsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#Service)) *[ProjectsLocationsTransferConfigsRunsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsService)

Delete: Deletes the specified transfer run.

*   name: The name of the resource requested. If you are using the regionless method, the location must be `US` and the name should be in the following form: * `projects/{project_id}/transferConfigs/{config_id}/runs/{run_id}` If you are using the regionalized method, the name should be in the following form: * `projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}/ runs/{run_id}`.

Get: Returns information about the particular transfer run.

*   name: The name of the resource requested. If you are using the regionless method, the location must be `US` and the name should be in the following form: * `projects/{project_id}/transferConfigs/{config_id}/runs/{run_id}` If you are using the regionalized method, the name should be in the following form: * `projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}/ runs/{run_id}`.

List: Returns information about running and completed transfer runs.

*   parent: Name of transfer configuration for which transfer runs should be retrieved. If you are using the regionless method, the location must be `US` and the name should be in the following form: * `projects/{project_id}/transferConfigs/{config_id}` If you are using the regionalized method, the name should be in the following form: * `projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}`.

type ProjectsLocationsTransferConfigsRunsTransferLogsListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "bigquerydatatransfer.projects.locations.transferConfigs.runs.transferLogs.list" call. Any non-2xx status code is an error. Response headers are in either *ListTransferLogsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

MessageTypes sets the optional parameter "messageTypes": Message types to return. If not populated - INFO, WARNING and ERROR messages are returned.

Possible values:

"MESSAGE_SEVERITY_UNSPECIFIED" - No severity specified.
"INFO" - Informational message.
"WARNING" - Warning message.
"ERROR" - Error message.

PageSize sets the optional parameter "pageSize": Page size. The default page size is the maximum value of 1000 results.

PageToken sets the optional parameter "pageToken": Pagination token, which can be used to request a specific page of `ListTransferLogsRequest` list results. For multiple-page results, `ListTransferLogsResponse` outputs a `next_page` token, which can be used as the `page_token` value to request the next page of list results.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsTransferConfigsRunsTransferLogsService struct {
	
}

func NewProjectsLocationsTransferConfigsRunsTransferLogsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#Service)) *[ProjectsLocationsTransferConfigsRunsTransferLogsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsTransferLogsService)

List: Returns log messages for the transfer run.

*   parent: Transfer run name. If you are using the regionless method, the location must be `US` and the name should be in the following form: * `projects/{project_id}/transferConfigs/{config_id}/runs/{run_id}` If you are using the regionalized method, the name should be in the following form: * `projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}/ runs/{run_id}`.

type ProjectsLocationsTransferConfigsScheduleRunsCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "bigquerydatatransfer.projects.locations.transferConfigs.scheduleRuns" call. Any non-2xx status code is an error. Response headers are in either *ScheduleTransferRunsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsTransferConfigsService struct {
 Runs *[ProjectsLocationsTransferConfigsRunsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsRunsService)	
}

func NewProjectsLocationsTransferConfigsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#Service)) *[ProjectsLocationsTransferConfigsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsTransferConfigsService)

Create: Creates a new data transfer configuration.

*   parent: The BigQuery project id where the transfer configuration should be created. Must be in the format projects/{project_id}/locations/{location_id} or projects/{project_id}. If specified location and location of the destination bigquery dataset do not match - the request will fail.

Delete: Deletes a data transfer configuration, including any associated transfer runs and logs.

*   name: The name of the resource to delete. If you are using the regionless method, the location must be `US` and the name should be in the following form: * `projects/{project_id}/transferConfigs/{config_id}` If you are using the regionalized method, the name should be in the following form: * `projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}`.

Get: Returns information about a data transfer config.

*   name: The name of the resource requested. If you are using the regionless method, the location must be `US` and the name should be in the following form: * `projects/{project_id}/transferConfigs/{config_id}` If you are using the regionalized method, the name should be in the following form: * `projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}`.

List: Returns information about all transfer configs owned by a project in the specified location.

*   parent: The BigQuery project id for which transfer configs should be returned. If you are using the regionless method, the location must be `US` and `parent` should be in the following form: * `projects/{project_id} If you are using the regionalized method, `parent` should be in the following form: * `projects/{project_id}/locations/{location_id}`.

Patch: Updates a data transfer configuration. All fields must be set, even if they are not updated.

*   name: Identifier. The resource name of the transfer config. Transfer config names have the form either `projects/{project_id}/locations/{region}/transferConfigs/{config_id}` or `projects/{project_id}/transferConfigs/{config_id}`, where `config_id` is usually a UUID, even though it is not guaranteed or required. The name is ignored when creating a transfer config.

ScheduleRuns: Creates transfer runs for a time range [start_time, end_time]. For each date - or whatever granularity the data source supports - in the range, one transfer run is created. Note that runs are created per UTC time in the time range. DEPRECATED: use StartManualTransferRuns instead.

*   parent: Transfer configuration name. If you are using the regionless method, the location must be `US` and the name should be in the following form: * `projects/{project_id}/transferConfigs/{config_id}` If you are using the regionalized method, the name should be in the following form: * `projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}`.

StartManualRuns: Manually initiates transfer runs. You can schedule these runs in two ways: 1. For a specific point in time using the 'requested_run_time' parameter. 2. For a period between 'start_time' (inclusive) and 'end_time' (exclusive). If scheduling a single run, it is set to execute immediately (schedule_time equals the current time). When scheduling multiple runs within a time range, the first run starts now, and subsequent runs are delayed by 15 seconds each.

*   parent: Transfer configuration name. If you are using the regionless method, the location must be `US` and the name should be in the following form: * `projects/{project_id}/transferConfigs/{config_id}` If you are using the regionalized method, the name should be in the following form: * `projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}`.

type ProjectsLocationsTransferConfigsStartManualRunsCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "bigquerydatatransfer.projects.locations.transferConfigs.startManualRuns" call. Any non-2xx status code is an error. Response headers are in either *StartManualTransferRunsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsUnenrollDataSourcesCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "bigquerydatatransfer.projects.locations.unenrollDataSources" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsService struct {
 DataSources *[ProjectsDataSourcesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsDataSourcesService)
 Locations *[ProjectsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsLocationsService)
 TransferConfigs *[ProjectsTransferConfigsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsService)	
}

func NewProjectsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#Service)) *[ProjectsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsService)

type ProjectsTransferConfigsCreateCall struct {
	
}

AuthorizationCode sets the optional parameter "authorizationCode": Deprecated: Authorization code was required when `transferConfig.dataSourceId` is 'youtube_channel' but it is no longer used in any data sources. Use `version_info` instead. Optional OAuth2 authorization code to use with this transfer configuration. This is required only if `transferConfig.dataSourceId` is 'youtube_channel' and new credentials are needed, as indicated by `CheckValidCreds`. In order to obtain authorization_code, make a request to the following URL: [https://bigquery.cloud.google.com/datatransfer/oauthz/auth?redirect_uri=urn:ietf:wg:oauth:2.0:oob&response_type=authorization_code&client_id=client_id&scope=data_source_scopes](https://bigquery.cloud.google.com/datatransfer/oauthz/auth?redirect_uri=urn:ietf:wg:oauth:2.0:oob&response_type=authorization_code&client_id=client_id&scope=data_source_scopes) * The client_id is the OAuth client_id of the data source as returned by ListDataSources method. * data_source_scopes are the scopes returned by ListDataSources method. Note that this should not be set when `service_account_name` is used to create the transfer config.

Context sets the context to be used in this call's Do method.

Do executes the "bigquerydatatransfer.projects.transferConfigs.create" call. Any non-2xx status code is an error. Response headers are in either *TransferConfig.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

ServiceAccountName sets the optional parameter "serviceAccountName": Optional service account email. If this field is set, the transfer config will be created with this service account's credentials. It requires that the requesting user calling this API has permissions to act as this service account. Note that not all data sources support service account credentials when creating a transfer config. For the latest list of data sources, read about using service accounts ([https://cloud.google.com/bigquery-transfer/docs/use-service-accounts](https://cloud.google.com/bigquery-transfer/docs/use-service-accounts)).

type ProjectsTransferConfigsDeleteCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "bigquerydatatransfer.projects.transferConfigs.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsTransferConfigsGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "bigquerydatatransfer.projects.transferConfigs.get" call. Any non-2xx status code is an error. Response headers are in either *TransferConfig.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsTransferConfigsListCall struct {
	
}

Context sets the context to be used in this call's Do method.

DataSourceIds sets the optional parameter "dataSourceIds": When specified, only configurations of requested data sources are returned.

Do executes the "bigquerydatatransfer.projects.transferConfigs.list" call. Any non-2xx status code is an error. Response headers are in either *ListTransferConfigsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": Page size. The default page size is the maximum value of 1000 results.

PageToken sets the optional parameter "pageToken": Pagination token, which can be used to request a specific page of `ListTransfersRequest` list results. For multiple-page results, `ListTransfersResponse` outputs a `next_page` token, which can be used as the `page_token` value to request the next page of list results.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsTransferConfigsPatchCall struct {
	
}

AuthorizationCode sets the optional parameter "authorizationCode": Deprecated: Authorization code was required when `transferConfig.dataSourceId` is 'youtube_channel' but it is no longer used in any data sources. Use `version_info` instead. Optional OAuth2 authorization code to use with this transfer configuration. This is required only if `transferConfig.dataSourceId` is 'youtube_channel' and new credentials are needed, as indicated by `CheckValidCreds`. In order to obtain authorization_code, make a request to the following URL: [https://bigquery.cloud.google.com/datatransfer/oauthz/auth?redirect_uri=urn:ietf:wg:oauth:2.0:oob&response_type=authorization_code&client_id=client_id&scope=data_source_scopes](https://bigquery.cloud.google.com/datatransfer/oauthz/auth?redirect_uri=urn:ietf:wg:oauth:2.0:oob&response_type=authorization_code&client_id=client_id&scope=data_source_scopes) * The client_id is the OAuth client_id of the data source as returned by ListDataSources method. * data_source_scopes are the scopes returned by ListDataSources method. Note that this should not be set when `service_account_name` is used to update the transfer config.

Context sets the context to be used in this call's Do method.

Do executes the "bigquerydatatransfer.projects.transferConfigs.patch" call. Any non-2xx status code is an error. Response headers are in either *TransferConfig.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

ServiceAccountName sets the optional parameter "serviceAccountName": Optional service account email. If this field is set, the transfer config will be created with this service account's credentials. It requires that the requesting user calling this API has permissions to act as this service account. Note that not all data sources support service account credentials when creating a transfer config. For the latest list of data sources, read about using service accounts ([https://cloud.google.com/bigquery-transfer/docs/use-service-accounts](https://cloud.google.com/bigquery-transfer/docs/use-service-accounts)).

UpdateMask sets the optional parameter "updateMask": Required. Required list of fields to be updated in this request.

type ProjectsTransferConfigsRunsDeleteCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "bigquerydatatransfer.projects.transferConfigs.runs.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsTransferConfigsRunsGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "bigquerydatatransfer.projects.transferConfigs.runs.get" call. Any non-2xx status code is an error. Response headers are in either *TransferRun.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsTransferConfigsRunsListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "bigquerydatatransfer.projects.transferConfigs.runs.list" call. Any non-2xx status code is an error. Response headers are in either *ListTransferRunsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": Page size. The default page size is the maximum value of 1000 results.

PageToken sets the optional parameter "pageToken": Pagination token, which can be used to request a specific page of `ListTransferRunsRequest` list results. For multiple-page results, `ListTransferRunsResponse` outputs a `next_page` token, which can be used as the `page_token` value to request the next page of list results.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

RunAttempt sets the optional parameter "runAttempt": Indicates how run attempts are to be pulled.

Possible values:

"RUN_ATTEMPT_UNSPECIFIED" - All runs should be returned.
"LATEST" - Only latest run per day should be returned.

States sets the optional parameter "states": When specified, only transfer runs with requested states are returned.

Possible values:

"TRANSFER_STATE_UNSPECIFIED" - State placeholder (0).
"PENDING" - Data transfer is scheduled and is waiting to be picked up by

data transfer backend (2).

"RUNNING" - Data transfer is in progress (3).
"SUCCEEDED" - Data transfer completed successfully (4).
"FAILED" - Data transfer failed (5).
"CANCELLED" - Data transfer is cancelled (6).

type ProjectsTransferConfigsRunsService struct {
 TransferLogs *[ProjectsTransferConfigsRunsTransferLogsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsTransferLogsService)	
}

func NewProjectsTransferConfigsRunsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#Service)) *[ProjectsTransferConfigsRunsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsService)

Delete: Deletes the specified transfer run.

*   name: The name of the resource requested. If you are using the regionless method, the location must be `US` and the name should be in the following form: * `projects/{project_id}/transferConfigs/{config_id}/runs/{run_id}` If you are using the regionalized method, the name should be in the following form: * `projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}/ runs/{run_id}`.

Get: Returns information about the particular transfer run.

*   name: The name of the resource requested. If you are using the regionless method, the location must be `US` and the name should be in the following form: * `projects/{project_id}/transferConfigs/{config_id}/runs/{run_id}` If you are using the regionalized method, the name should be in the following form: * `projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}/ runs/{run_id}`.

List: Returns information about running and completed transfer runs.

*   parent: Name of transfer configuration for which transfer runs should be retrieved. If you are using the regionless method, the location must be `US` and the name should be in the following form: * `projects/{project_id}/transferConfigs/{config_id}` If you are using the regionalized method, the name should be in the following form: * `projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}`.

type ProjectsTransferConfigsRunsTransferLogsListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "bigquerydatatransfer.projects.transferConfigs.runs.transferLogs.list" call. Any non-2xx status code is an error. Response headers are in either *ListTransferLogsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

MessageTypes sets the optional parameter "messageTypes": Message types to return. If not populated - INFO, WARNING and ERROR messages are returned.

Possible values:

"MESSAGE_SEVERITY_UNSPECIFIED" - No severity specified.
"INFO" - Informational message.
"WARNING" - Warning message.
"ERROR" - Error message.

PageSize sets the optional parameter "pageSize": Page size. The default page size is the maximum value of 1000 results.

PageToken sets the optional parameter "pageToken": Pagination token, which can be used to request a specific page of `ListTransferLogsRequest` list results. For multiple-page results, `ListTransferLogsResponse` outputs a `next_page` token, which can be used as the `page_token` value to request the next page of list results.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsTransferConfigsRunsTransferLogsService struct {
	
}

func NewProjectsTransferConfigsRunsTransferLogsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#Service)) *[ProjectsTransferConfigsRunsTransferLogsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsTransferLogsService)

List: Returns log messages for the transfer run.

*   parent: Transfer run name. If you are using the regionless method, the location must be `US` and the name should be in the following form: * `projects/{project_id}/transferConfigs/{config_id}/runs/{run_id}` If you are using the regionalized method, the name should be in the following form: * `projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}/ runs/{run_id}`.

type ProjectsTransferConfigsScheduleRunsCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "bigquerydatatransfer.projects.transferConfigs.scheduleRuns" call. Any non-2xx status code is an error. Response headers are in either *ScheduleTransferRunsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsTransferConfigsService struct {
 Runs *[ProjectsTransferConfigsRunsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsRunsService)	
}

func NewProjectsTransferConfigsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#Service)) *[ProjectsTransferConfigsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ProjectsTransferConfigsService)

Create: Creates a new data transfer configuration.

*   parent: The BigQuery project id where the transfer configuration should be created. Must be in the format projects/{project_id}/locations/{location_id} or projects/{project_id}. If specified location and location of the destination bigquery dataset do not match - the request will fail.

Delete: Deletes a data transfer configuration, including any associated transfer runs and logs.

*   name: The name of the resource to delete. If you are using the regionless method, the location must be `US` and the name should be in the following form: * `projects/{project_id}/transferConfigs/{config_id}` If you are using the regionalized method, the name should be in the following form: * `projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}`.

Get: Returns information about a data transfer config.

*   name: The name of the resource requested. If you are using the regionless method, the location must be `US` and the name should be in the following form: * `projects/{project_id}/transferConfigs/{config_id}` If you are using the regionalized method, the name should be in the following form: * `projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}`.

List: Returns information about all transfer configs owned by a project in the specified location.

*   parent: The BigQuery project id for which transfer configs should be returned. If you are using the regionless method, the location must be `US` and `parent` should be in the following form: * `projects/{project_id} If you are using the regionalized method, `parent` should be in the following form: * `projects/{project_id}/locations/{location_id}`.

Patch: Updates a data transfer configuration. All fields must be set, even if they are not updated.

*   name: Identifier. The resource name of the transfer config. Transfer config names have the form either `projects/{project_id}/locations/{region}/transferConfigs/{config_id}` or `projects/{project_id}/transferConfigs/{config_id}`, where `config_id` is usually a UUID, even though it is not guaranteed or required. The name is ignored when creating a transfer config.

ScheduleRuns: Creates transfer runs for a time range [start_time, end_time]. For each date - or whatever granularity the data source supports - in the range, one transfer run is created. Note that runs are created per UTC time in the time range. DEPRECATED: use StartManualTransferRuns instead.

*   parent: Transfer configuration name. If you are using the regionless method, the location must be `US` and the name should be in the following form: * `projects/{project_id}/transferConfigs/{config_id}` If you are using the regionalized method, the name should be in the following form: * `projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}`.

StartManualRuns: Manually initiates transfer runs. You can schedule these runs in two ways: 1. For a specific point in time using the 'requested_run_time' parameter. 2. For a period between 'start_time' (inclusive) and 'end_time' (exclusive). If scheduling a single run, it is set to execute immediately (schedule_time equals the current time). When scheduling multiple runs within a time range, the first run starts now, and subsequent runs are delayed by 15 seconds each.

*   parent: Transfer configuration name. If you are using the regionless method, the location must be `US` and the name should be in the following form: * `projects/{project_id}/transferConfigs/{config_id}` If you are using the regionalized method, the name should be in the following form: * `projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}`.

type ProjectsTransferConfigsStartManualRunsCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "bigquerydatatransfer.projects.transferConfigs.startManualRuns" call. Any non-2xx status code is an error. Response headers are in either *StartManualTransferRunsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ScheduleOptions struct {
	
	
	
	DisableAutoScheduling [bool](https://pkg.go.dev/builtin#bool) `json:"disableAutoScheduling,omitempty"`
	
	
	
	EndTime [string](https://pkg.go.dev/builtin#string) `json:"endTime,omitempty"`
	
	
	
	
	StartTime [string](https://pkg.go.dev/builtin#string) `json:"startTime,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ScheduleOptions: Options customizing the data transfer schedule.

type ScheduleOptionsV2 struct {
	
	EventDrivenSchedule *[EventDrivenSchedule](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#EventDrivenSchedule) `json:"eventDrivenSchedule,omitempty"`
	
	
	
	ManualSchedule *[ManualSchedule](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ManualSchedule) `json:"manualSchedule,omitempty"`
	
	TimeBasedSchedule *[TimeBasedSchedule](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#TimeBasedSchedule) `json:"timeBasedSchedule,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ScheduleOptionsV2: V2 options customizing different types of data transfer schedule. This field supports existing time-based and manual transfer schedule. Also supports Event-Driven transfer schedule. ScheduleOptionsV2 cannot be used together with ScheduleOptions/Schedule.

type ScheduleTransferRunsRequest struct {
	
	EndTime [string](https://pkg.go.dev/builtin#string) `json:"endTime,omitempty"`
	
	StartTime [string](https://pkg.go.dev/builtin#string) `json:"startTime,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ScheduleTransferRunsRequest: A request to schedule transfer runs for a time range.

ScheduleTransferRunsResponse: A response to schedule transfer runs for a time range.

New creates a new Service. It uses the provided http.Client for requests.

Deprecated: please use NewService instead. To provide a custom HTTP client, use option.WithHTTPClient. If you are using google.golang.org/api/googleapis/transport.APIKey, use option.WithAPIKey with NewService instead.

NewService creates a new Service.

type StartManualTransferRunsRequest struct {
	
	
	
	RequestedRunTime [string](https://pkg.go.dev/builtin#string) `json:"requestedRunTime,omitempty"`
	
	
	
	RequestedTimeRange *[TimeRange](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#TimeRange) `json:"requestedTimeRange,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

StartManualTransferRunsRequest: A request to start manual transfer runs.

type StartManualTransferRunsResponse struct {
	Runs []*[TransferRun](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#TransferRun) `json:"runs,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

StartManualTransferRunsResponse: A response to start manual transfer runs.

type Status struct {
	Code [int64](https://pkg.go.dev/builtin#int64) `json:"code,omitempty"`
	
	Details [][googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[RawMessage](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#RawMessage) `json:"details,omitempty"`
	
	
	Message [string](https://pkg.go.dev/builtin#string) `json:"message,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Status: The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by gRPC ([https://github.com/grpc](https://github.com/grpc)). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the API Design Guide ([https://cloud.google.com/apis/design/errors](https://cloud.google.com/apis/design/errors)).

type TimeBasedSchedule struct {
	
	
	EndTime [string](https://pkg.go.dev/builtin#string) `json:"endTime,omitempty"`
	
	
	
	
	
	
	
	
	Schedule [string](https://pkg.go.dev/builtin#string) `json:"schedule,omitempty"`
	
	
	
	StartTime [string](https://pkg.go.dev/builtin#string) `json:"startTime,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

TimeBasedSchedule: Options customizing the time based transfer schedule. Options are migrated from the original ScheduleOptions message.

type TimeRange struct {
	
	
	
	EndTime [string](https://pkg.go.dev/builtin#string) `json:"endTime,omitempty"`
	
	
	
	StartTime [string](https://pkg.go.dev/builtin#string) `json:"startTime,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

TimeRange: A specification for a time range, this will request transfer runs with run_time between start_time (inclusive) and end_time (exclusive).

type TransferConfig struct {
	
	
	
	
	DataRefreshWindowDays [int64](https://pkg.go.dev/builtin#int64) `json:"dataRefreshWindowDays,omitempty"`
	
	
	
	DataSourceId [string](https://pkg.go.dev/builtin#string) `json:"dataSourceId,omitempty"`
	DatasetRegion [string](https://pkg.go.dev/builtin#string) `json:"datasetRegion,omitempty"`
	DestinationDatasetId [string](https://pkg.go.dev/builtin#string) `json:"destinationDatasetId,omitempty"`
	
	Disabled [bool](https://pkg.go.dev/builtin#bool) `json:"disabled,omitempty"`
	DisplayName [string](https://pkg.go.dev/builtin#string) `json:"displayName,omitempty"`
	
	EmailPreferences *[EmailPreferences](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#EmailPreferences) `json:"emailPreferences,omitempty"`
	
	
	
	
	
	EncryptionConfiguration *[EncryptionConfiguration](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#EncryptionConfiguration) `json:"encryptionConfiguration,omitempty"`
	
	Error *[Status](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#Status) `json:"error,omitempty"`
	
	
	
	
	
	
	
	
	ManagedTableType [string](https://pkg.go.dev/builtin#string) `json:"managedTableType,omitempty"`
	
	
	
	
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	NextRunTime [string](https://pkg.go.dev/builtin#string) `json:"nextRunTime,omitempty"`
	
	
	NotificationPubsubTopic [string](https://pkg.go.dev/builtin#string) `json:"notificationPubsubTopic,omitempty"`
	
	
	
	OwnerInfo *[UserInfo](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#UserInfo) `json:"ownerInfo,omitempty"`
	
	
	
	Params [googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[RawMessage](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#RawMessage) `json:"params,omitempty"`
	
	
	
	
	
	
	
	
	Schedule [string](https://pkg.go.dev/builtin#string) `json:"schedule,omitempty"`
	ScheduleOptions *[ScheduleOptions](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ScheduleOptions) `json:"scheduleOptions,omitempty"`
	
	
	ScheduleOptionsV2 *[ScheduleOptionsV2](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#ScheduleOptionsV2) `json:"scheduleOptionsV2,omitempty"`
	
	
	
	
	
	
	
	
	
	State [string](https://pkg.go.dev/builtin#string) `json:"state,omitempty"`
	
	UpdateTime [string](https://pkg.go.dev/builtin#string) `json:"updateTime,omitempty"`
	UserId [int64](https://pkg.go.dev/builtin#int64) `json:"userId,omitempty,string"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

TransferConfig: Represents a data transfer configuration. A transfer configuration contains all metadata needed to perform a data transfer. For example, `destination_dataset_id` specifies where data should be stored. When a new transfer configuration is created, the specified `destination_dataset_id` is created when needed and shared with the appropriate data source service account.

type TransferMessage struct {
	MessageText [string](https://pkg.go.dev/builtin#string) `json:"messageText,omitempty"`
	MessageTime [string](https://pkg.go.dev/builtin#string) `json:"messageTime,omitempty"`
	
	
	
	
	
	
	Severity [string](https://pkg.go.dev/builtin#string) `json:"severity,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

TransferMessage: Represents a user facing message for a particular data transfer run.

type TransferRun struct {
	DataSourceId [string](https://pkg.go.dev/builtin#string) `json:"dataSourceId,omitempty"`
	DestinationDatasetId [string](https://pkg.go.dev/builtin#string) `json:"destinationDatasetId,omitempty"`
	
	
	EmailPreferences *[EmailPreferences](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#EmailPreferences) `json:"emailPreferences,omitempty"`
	
	EndTime [string](https://pkg.go.dev/builtin#string) `json:"endTime,omitempty"`
	ErrorStatus *[Status](https://pkg.go.dev/google.golang.org/api@v0.269.0/bigquerydatatransfer/v1#Status) `json:"errorStatus,omitempty"`
	
	
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	
	NotificationPubsubTopic [string](https://pkg.go.dev/builtin#string) `json:"notificationPubsubTopic,omitempty"`
	
	
	
	
	Params [googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[RawMessage](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#RawMessage) `json:"params,omitempty"`
	
	RunTime [string](https://pkg.go.dev/builtin#string) `json:"runTime,omitempty"`
	
	
	
	
	Schedule [string](https://pkg.go.dev/builtin#string) `json:"schedule,omitempty"`
	ScheduleTime [string](https://pkg.go.dev/builtin#string) `json:"scheduleTime,omitempty"`
	
	StartTime [string](https://pkg.go.dev/builtin#string) `json:"startTime,omitempty"`
	
	
	
	
	
	
	
	
	
	State [string](https://pkg.go.dev/builtin#string) `json:"state,omitempty"`
	UpdateTime [string](https://pkg.go.dev/builtin#string) `json:"updateTime,omitempty"`
	UserId [int64](https://pkg.go.dev/builtin#int64) `json:"userId,omitempty,string"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

TransferRun: Represents a data transfer run.

type UnenrollDataSourcesRequest struct {
	
	DataSourceIds [][string](https://pkg.go.dev/builtin#string) `json:"dataSourceIds,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

UnenrollDataSourcesRequest: A request to unenroll a set of data sources so they are no longer visible in the BigQuery UI's `Transfer` tab.

type UserInfo struct {
	Email [string](https://pkg.go.dev/builtin#string) `json:"email,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

UserInfo: Information about a user.
