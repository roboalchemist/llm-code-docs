# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha

Title: apim package - google.golang.org/api/apim/v1alpha - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha

Markdown Content:
Package apim provides access to the API Management API.

For product documentation, see: [https://cloud.google.com/apigee/](https://cloud.google.com/apigee/)

#### Library status [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#hdr-Library_status "Go to Library status")

These client libraries are officially supported by Google. However, this library is considered complete and is in maintenance mode. This means that we will address critical bugs and security issues but will not add any new features.

When possible, we recommend using our newer [Cloud Client Libraries for Go]([https://pkg.go.dev/cloud.google.com/go](https://pkg.go.dev/cloud.google.com/go)) that are still actively being worked and iterated on.

#### Creating a client [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#hdr-Creating_a_client "Go to Creating a client")

Usage example:

import "google.golang.org/api/apim/v1alpha"
...
ctx := context.Background()
apimService, err := apim.NewService(ctx)

In this example, Google Application Default Credentials are used for authentication. For information on how to create and obtain Application Default Credentials, see [https://developers.google.com/identity/protocols/application-default-credentials](https://developers.google.com/identity/protocols/application-default-credentials).

#### Other authentication options [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#hdr-Other_authentication_options "Go to Other authentication options")

To use an API key for authentication (note: some APIs do not support API keys), use [google.golang.org/api/option.WithAPIKey](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#WithAPIKey):

apimService, err := apim.NewService(ctx, option.WithAPIKey("AIza..."))

To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow, use [google.golang.org/api/option.WithTokenSource](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#WithTokenSource):

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
apimService, err := apim.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))

See [google.golang.org/api/option.ClientOption](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#ClientOption) for details on options.

*   [Constants](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#pkg-constants)
*   [type ApiObservation](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ApiObservation)
*       *   [func (s ApiObservation) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ApiObservation.MarshalJSON)

*   [type ApiOperation](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ApiOperation)
*       *   [func (s ApiOperation) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ApiOperation.MarshalJSON)

*   [type BatchEditTagsApiObservationsRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#BatchEditTagsApiObservationsRequest)
*       *   [func (s BatchEditTagsApiObservationsRequest) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#BatchEditTagsApiObservationsRequest.MarshalJSON)

*   [type BatchEditTagsApiObservationsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#BatchEditTagsApiObservationsResponse)
*       *   [func (s BatchEditTagsApiObservationsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#BatchEditTagsApiObservationsResponse.MarshalJSON)

*   [type CancelOperationRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#CancelOperationRequest)
*   [type DisableObservationJobRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#DisableObservationJobRequest)
*   [type EditTagsApiObservationsRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#EditTagsApiObservationsRequest)
*       *   [func (s EditTagsApiObservationsRequest) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#EditTagsApiObservationsRequest.MarshalJSON)

*   [type Empty](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#Empty)
*   [type EnableObservationJobRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#EnableObservationJobRequest)
*   [type Entitlement](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#Entitlement)
*       *   [func (s Entitlement) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#Entitlement.MarshalJSON)

*   [type GclbObservationSource](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#GclbObservationSource)
*       *   [func (s GclbObservationSource) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#GclbObservationSource.MarshalJSON)

*   [type GclbObservationSourcePscNetworkConfig](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#GclbObservationSourcePscNetworkConfig)
*       *   [func (s GclbObservationSourcePscNetworkConfig) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#GclbObservationSourcePscNetworkConfig.MarshalJSON)

*   [type HttpOperation](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#HttpOperation)
*       *   [func (s HttpOperation) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#HttpOperation.MarshalJSON)

*   [type HttpOperationHeader](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#HttpOperationHeader)
*       *   [func (s HttpOperationHeader) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#HttpOperationHeader.MarshalJSON)

*   [type HttpOperationHttpRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#HttpOperationHttpRequest)
*       *   [func (s HttpOperationHttpRequest) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#HttpOperationHttpRequest.MarshalJSON)

*   [type HttpOperationHttpResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#HttpOperationHttpResponse)
*       *   [func (s HttpOperationHttpResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#HttpOperationHttpResponse.MarshalJSON)

*   [type HttpOperationPathParam](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#HttpOperationPathParam)
*       *   [func (s HttpOperationPathParam) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#HttpOperationPathParam.MarshalJSON)

*   [type HttpOperationQueryParam](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#HttpOperationQueryParam)
*       *   [func (s HttpOperationQueryParam) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#HttpOperationQueryParam.MarshalJSON)

*   [type ListApiObservationTagsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ListApiObservationTagsResponse)
*       *   [func (s ListApiObservationTagsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ListApiObservationTagsResponse.MarshalJSON)

*   [type ListApiObservationsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ListApiObservationsResponse)
*       *   [func (s ListApiObservationsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ListApiObservationsResponse.MarshalJSON)

*   [type ListApiOperationsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ListApiOperationsResponse)
*       *   [func (s ListApiOperationsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ListApiOperationsResponse.MarshalJSON)

*   [type ListLocationsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ListLocationsResponse)
*       *   [func (s ListLocationsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ListLocationsResponse.MarshalJSON)

*   [type ListObservationJobsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ListObservationJobsResponse)
*       *   [func (s ListObservationJobsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ListObservationJobsResponse.MarshalJSON)

*   [type ListObservationSourcesResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ListObservationSourcesResponse)
*       *   [func (s ListObservationSourcesResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ListObservationSourcesResponse.MarshalJSON)

*   [type ListOperationsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ListOperationsResponse)
*       *   [func (s ListOperationsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ListOperationsResponse.MarshalJSON)

*   [type Location](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#Location)
*       *   [func (s Location) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#Location.MarshalJSON)

*   [type ObservationJob](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ObservationJob)
*       *   [func (s ObservationJob) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ObservationJob.MarshalJSON)

*   [type ObservationSource](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ObservationSource)
*       *   [func (s ObservationSource) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ObservationSource.MarshalJSON)

*   [type Operation](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#Operation)
*       *   [func (s Operation) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#Operation.MarshalJSON)

*   [type OperationMetadata](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#OperationMetadata)
*       *   [func (s OperationMetadata) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#OperationMetadata.MarshalJSON)

*   [type ProjectsLocationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsGetCall)
*       *   [func (c *ProjectsLocationsGetCall) Context(ctx context.Context) *ProjectsLocationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsGetCall.Context)
    *   [func (c *ProjectsLocationsGetCall) Do(opts ...googleapi.CallOption) (*Location, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsGetCall.Do)
    *   [func (c *ProjectsLocationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsGetCall.Fields)
    *   [func (c *ProjectsLocationsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsGetCall.Header)
    *   [func (c *ProjectsLocationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsGetCall.IfNoneMatch)

*   [type ProjectsLocationsGetEntitlementCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsGetEntitlementCall)
*       *   [func (c *ProjectsLocationsGetEntitlementCall) Context(ctx context.Context) *ProjectsLocationsGetEntitlementCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsGetEntitlementCall.Context)
    *   [func (c *ProjectsLocationsGetEntitlementCall) Do(opts ...googleapi.CallOption) (*Entitlement, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsGetEntitlementCall.Do)
    *   [func (c *ProjectsLocationsGetEntitlementCall) Fields(s ...googleapi.Field) *ProjectsLocationsGetEntitlementCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsGetEntitlementCall.Fields)
    *   [func (c *ProjectsLocationsGetEntitlementCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsGetEntitlementCall.Header)
    *   [func (c *ProjectsLocationsGetEntitlementCall) IfNoneMatch(entityTag string) *ProjectsLocationsGetEntitlementCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsGetEntitlementCall.IfNoneMatch)

*   [type ProjectsLocationsListApiObservationTagsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsListApiObservationTagsCall)
*       *   [func (c *ProjectsLocationsListApiObservationTagsCall) Context(ctx context.Context) *ProjectsLocationsListApiObservationTagsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsListApiObservationTagsCall.Context)
    *   [func (c *ProjectsLocationsListApiObservationTagsCall) Do(opts ...googleapi.CallOption) (*ListApiObservationTagsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsListApiObservationTagsCall.Do)
    *   [func (c *ProjectsLocationsListApiObservationTagsCall) Fields(s ...googleapi.Field) *ProjectsLocationsListApiObservationTagsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsListApiObservationTagsCall.Fields)
    *   [func (c *ProjectsLocationsListApiObservationTagsCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsListApiObservationTagsCall.Header)
    *   [func (c *ProjectsLocationsListApiObservationTagsCall) IfNoneMatch(entityTag string) *ProjectsLocationsListApiObservationTagsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsListApiObservationTagsCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsListApiObservationTagsCall) PageSize(pageSize int64) *ProjectsLocationsListApiObservationTagsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsListApiObservationTagsCall.PageSize)
    *   [func (c *ProjectsLocationsListApiObservationTagsCall) PageToken(pageToken string) *ProjectsLocationsListApiObservationTagsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsListApiObservationTagsCall.PageToken)
    *   [func (c *ProjectsLocationsListApiObservationTagsCall) Pages(ctx context.Context, f func(*ListApiObservationTagsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsListApiObservationTagsCall.Pages)

*   [type ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsListCall)
*       *   [func (c *ProjectsLocationsListCall) Context(ctx context.Context) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsListCall.Context)
    *   [func (c *ProjectsLocationsListCall) Do(opts ...googleapi.CallOption) (*ListLocationsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsListCall.Do)
    *   [func (c *ProjectsLocationsListCall) ExtraLocationTypes(extraLocationTypes ...string) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsListCall.ExtraLocationTypes)
    *   [func (c *ProjectsLocationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsListCall.Fields)
    *   [func (c *ProjectsLocationsListCall) Filter(filter string) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsListCall.Filter)
    *   [func (c *ProjectsLocationsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsListCall.Header)
    *   [func (c *ProjectsLocationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsListCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsListCall) PageSize(pageSize int64) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsListCall.PageSize)
    *   [func (c *ProjectsLocationsListCall) PageToken(pageToken string) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsListCall.PageToken)
    *   [func (c *ProjectsLocationsListCall) Pages(ctx context.Context, f func(*ListLocationsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsListCall.Pages)

*   [type ProjectsLocationsObservationJobsApiObservationsApiOperationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsApiOperationsGetCall)
*       *   [func (c *ProjectsLocationsObservationJobsApiObservationsApiOperationsGetCall) Context(ctx context.Context) *ProjectsLocationsObservationJobsApiObservationsApiOperationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsApiOperationsGetCall.Context)
    *   [func (c *ProjectsLocationsObservationJobsApiObservationsApiOperationsGetCall) Do(opts ...googleapi.CallOption) (*ApiOperation, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsApiOperationsGetCall.Do)
    *   [func (c *ProjectsLocationsObservationJobsApiObservationsApiOperationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsObservationJobsApiObservationsApiOperationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsApiOperationsGetCall.Fields)
    *   [func (c *ProjectsLocationsObservationJobsApiObservationsApiOperationsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsApiOperationsGetCall.Header)
    *   [func (c *ProjectsLocationsObservationJobsApiObservationsApiOperationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsObservationJobsApiObservationsApiOperationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsApiOperationsGetCall.IfNoneMatch)

*   [type ProjectsLocationsObservationJobsApiObservationsApiOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsApiOperationsListCall)
*       *   [func (c *ProjectsLocationsObservationJobsApiObservationsApiOperationsListCall) Context(ctx context.Context) *ProjectsLocationsObservationJobsApiObservationsApiOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsApiOperationsListCall.Context)
    *   [func (c *ProjectsLocationsObservationJobsApiObservationsApiOperationsListCall) Do(opts ...googleapi.CallOption) (*ListApiOperationsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsApiOperationsListCall.Do)
    *   [func (c *ProjectsLocationsObservationJobsApiObservationsApiOperationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsObservationJobsApiObservationsApiOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsApiOperationsListCall.Fields)
    *   [func (c *ProjectsLocationsObservationJobsApiObservationsApiOperationsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsApiOperationsListCall.Header)
    *   [func (c *ProjectsLocationsObservationJobsApiObservationsApiOperationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsObservationJobsApiObservationsApiOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsApiOperationsListCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsObservationJobsApiObservationsApiOperationsListCall) PageSize(pageSize int64) *ProjectsLocationsObservationJobsApiObservationsApiOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsApiOperationsListCall.PageSize)
    *   [func (c *ProjectsLocationsObservationJobsApiObservationsApiOperationsListCall) PageToken(pageToken string) *ProjectsLocationsObservationJobsApiObservationsApiOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsApiOperationsListCall.PageToken)
    *   [func (c *ProjectsLocationsObservationJobsApiObservationsApiOperationsListCall) Pages(ctx context.Context, f func(*ListApiOperationsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsApiOperationsListCall.Pages)

*   [type ProjectsLocationsObservationJobsApiObservationsApiOperationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsApiOperationsService)
*       *   [func NewProjectsLocationsObservationJobsApiObservationsApiOperationsService(s *Service) *ProjectsLocationsObservationJobsApiObservationsApiOperationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#NewProjectsLocationsObservationJobsApiObservationsApiOperationsService)

*       *   [func (r *ProjectsLocationsObservationJobsApiObservationsApiOperationsService) Get(name string) *ProjectsLocationsObservationJobsApiObservationsApiOperationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsApiOperationsService.Get)
    *   [func (r *ProjectsLocationsObservationJobsApiObservationsApiOperationsService) List(parent string) *ProjectsLocationsObservationJobsApiObservationsApiOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsApiOperationsService.List)

*   [type ProjectsLocationsObservationJobsApiObservationsBatchEditTagsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsBatchEditTagsCall)
*       *   [func (c *ProjectsLocationsObservationJobsApiObservationsBatchEditTagsCall) Context(ctx context.Context) *ProjectsLocationsObservationJobsApiObservationsBatchEditTagsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsBatchEditTagsCall.Context)
    *   [func (c *ProjectsLocationsObservationJobsApiObservationsBatchEditTagsCall) Do(opts ...googleapi.CallOption) (*BatchEditTagsApiObservationsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsBatchEditTagsCall.Do)
    *   [func (c *ProjectsLocationsObservationJobsApiObservationsBatchEditTagsCall) Fields(s ...googleapi.Field) *ProjectsLocationsObservationJobsApiObservationsBatchEditTagsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsBatchEditTagsCall.Fields)
    *   [func (c *ProjectsLocationsObservationJobsApiObservationsBatchEditTagsCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsBatchEditTagsCall.Header)

*   [type ProjectsLocationsObservationJobsApiObservationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsGetCall)
*       *   [func (c *ProjectsLocationsObservationJobsApiObservationsGetCall) Context(ctx context.Context) *ProjectsLocationsObservationJobsApiObservationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsGetCall.Context)
    *   [func (c *ProjectsLocationsObservationJobsApiObservationsGetCall) Do(opts ...googleapi.CallOption) (*ApiObservation, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsGetCall.Do)
    *   [func (c *ProjectsLocationsObservationJobsApiObservationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsObservationJobsApiObservationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsGetCall.Fields)
    *   [func (c *ProjectsLocationsObservationJobsApiObservationsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsGetCall.Header)
    *   [func (c *ProjectsLocationsObservationJobsApiObservationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsObservationJobsApiObservationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsGetCall.IfNoneMatch)

*   [type ProjectsLocationsObservationJobsApiObservationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsListCall)
*       *   [func (c *ProjectsLocationsObservationJobsApiObservationsListCall) Context(ctx context.Context) *ProjectsLocationsObservationJobsApiObservationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsListCall.Context)
    *   [func (c *ProjectsLocationsObservationJobsApiObservationsListCall) Do(opts ...googleapi.CallOption) (*ListApiObservationsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsListCall.Do)
    *   [func (c *ProjectsLocationsObservationJobsApiObservationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsObservationJobsApiObservationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsListCall.Fields)
    *   [func (c *ProjectsLocationsObservationJobsApiObservationsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsListCall.Header)
    *   [func (c *ProjectsLocationsObservationJobsApiObservationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsObservationJobsApiObservationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsListCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsObservationJobsApiObservationsListCall) PageSize(pageSize int64) *ProjectsLocationsObservationJobsApiObservationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsListCall.PageSize)
    *   [func (c *ProjectsLocationsObservationJobsApiObservationsListCall) PageToken(pageToken string) *ProjectsLocationsObservationJobsApiObservationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsListCall.PageToken)
    *   [func (c *ProjectsLocationsObservationJobsApiObservationsListCall) Pages(ctx context.Context, f func(*ListApiObservationsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsListCall.Pages)

*   [type ProjectsLocationsObservationJobsApiObservationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsService)
*       *   [func NewProjectsLocationsObservationJobsApiObservationsService(s *Service) *ProjectsLocationsObservationJobsApiObservationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#NewProjectsLocationsObservationJobsApiObservationsService)

*       *   [func (r *ProjectsLocationsObservationJobsApiObservationsService) BatchEditTags(parent string, ...) *ProjectsLocationsObservationJobsApiObservationsBatchEditTagsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsService.BatchEditTags)
    *   [func (r *ProjectsLocationsObservationJobsApiObservationsService) Get(name string) *ProjectsLocationsObservationJobsApiObservationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsService.Get)
    *   [func (r *ProjectsLocationsObservationJobsApiObservationsService) List(parent string) *ProjectsLocationsObservationJobsApiObservationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsService.List)

*   [type ProjectsLocationsObservationJobsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsCreateCall)
*       *   [func (c *ProjectsLocationsObservationJobsCreateCall) Context(ctx context.Context) *ProjectsLocationsObservationJobsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsCreateCall.Context)
    *   [func (c *ProjectsLocationsObservationJobsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsCreateCall.Do)
    *   [func (c *ProjectsLocationsObservationJobsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsObservationJobsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsCreateCall.Fields)
    *   [func (c *ProjectsLocationsObservationJobsCreateCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsCreateCall.Header)
    *   [func (c *ProjectsLocationsObservationJobsCreateCall) ObservationJobId(observationJobId string) *ProjectsLocationsObservationJobsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsCreateCall.ObservationJobId)
    *   [func (c *ProjectsLocationsObservationJobsCreateCall) RequestId(requestId string) *ProjectsLocationsObservationJobsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsCreateCall.RequestId)

*   [type ProjectsLocationsObservationJobsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsDeleteCall)
*       *   [func (c *ProjectsLocationsObservationJobsDeleteCall) Context(ctx context.Context) *ProjectsLocationsObservationJobsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsDeleteCall.Context)
    *   [func (c *ProjectsLocationsObservationJobsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsDeleteCall.Do)
    *   [func (c *ProjectsLocationsObservationJobsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsObservationJobsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsDeleteCall.Fields)
    *   [func (c *ProjectsLocationsObservationJobsDeleteCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsDeleteCall.Header)

*   [type ProjectsLocationsObservationJobsDisableCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsDisableCall)
*       *   [func (c *ProjectsLocationsObservationJobsDisableCall) Context(ctx context.Context) *ProjectsLocationsObservationJobsDisableCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsDisableCall.Context)
    *   [func (c *ProjectsLocationsObservationJobsDisableCall) Do(opts ...googleapi.CallOption) (*Operation, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsDisableCall.Do)
    *   [func (c *ProjectsLocationsObservationJobsDisableCall) Fields(s ...googleapi.Field) *ProjectsLocationsObservationJobsDisableCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsDisableCall.Fields)
    *   [func (c *ProjectsLocationsObservationJobsDisableCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsDisableCall.Header)

*   [type ProjectsLocationsObservationJobsEnableCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsEnableCall)
*       *   [func (c *ProjectsLocationsObservationJobsEnableCall) Context(ctx context.Context) *ProjectsLocationsObservationJobsEnableCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsEnableCall.Context)
    *   [func (c *ProjectsLocationsObservationJobsEnableCall) Do(opts ...googleapi.CallOption) (*Operation, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsEnableCall.Do)
    *   [func (c *ProjectsLocationsObservationJobsEnableCall) Fields(s ...googleapi.Field) *ProjectsLocationsObservationJobsEnableCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsEnableCall.Fields)
    *   [func (c *ProjectsLocationsObservationJobsEnableCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsEnableCall.Header)

*   [type ProjectsLocationsObservationJobsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsGetCall)
*       *   [func (c *ProjectsLocationsObservationJobsGetCall) Context(ctx context.Context) *ProjectsLocationsObservationJobsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsGetCall.Context)
    *   [func (c *ProjectsLocationsObservationJobsGetCall) Do(opts ...googleapi.CallOption) (*ObservationJob, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsGetCall.Do)
    *   [func (c *ProjectsLocationsObservationJobsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsObservationJobsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsGetCall.Fields)
    *   [func (c *ProjectsLocationsObservationJobsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsGetCall.Header)
    *   [func (c *ProjectsLocationsObservationJobsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsObservationJobsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsGetCall.IfNoneMatch)

*   [type ProjectsLocationsObservationJobsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsListCall)
*       *   [func (c *ProjectsLocationsObservationJobsListCall) Context(ctx context.Context) *ProjectsLocationsObservationJobsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsListCall.Context)
    *   [func (c *ProjectsLocationsObservationJobsListCall) Do(opts ...googleapi.CallOption) (*ListObservationJobsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsListCall.Do)
    *   [func (c *ProjectsLocationsObservationJobsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsObservationJobsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsListCall.Fields)
    *   [func (c *ProjectsLocationsObservationJobsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsListCall.Header)
    *   [func (c *ProjectsLocationsObservationJobsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsObservationJobsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsListCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsObservationJobsListCall) PageSize(pageSize int64) *ProjectsLocationsObservationJobsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsListCall.PageSize)
    *   [func (c *ProjectsLocationsObservationJobsListCall) PageToken(pageToken string) *ProjectsLocationsObservationJobsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsListCall.PageToken)
    *   [func (c *ProjectsLocationsObservationJobsListCall) Pages(ctx context.Context, f func(*ListObservationJobsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsListCall.Pages)

*   [type ProjectsLocationsObservationJobsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsService)
*       *   [func NewProjectsLocationsObservationJobsService(s *Service) *ProjectsLocationsObservationJobsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#NewProjectsLocationsObservationJobsService)

*       *   [func (r *ProjectsLocationsObservationJobsService) Create(parent string, observationjob *ObservationJob) *ProjectsLocationsObservationJobsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsService.Create)
    *   [func (r *ProjectsLocationsObservationJobsService) Delete(name string) *ProjectsLocationsObservationJobsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsService.Delete)
    *   [func (r *ProjectsLocationsObservationJobsService) Disable(name string, disableobservationjobrequest *DisableObservationJobRequest) *ProjectsLocationsObservationJobsDisableCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsService.Disable)
    *   [func (r *ProjectsLocationsObservationJobsService) Enable(name string, enableobservationjobrequest *EnableObservationJobRequest) *ProjectsLocationsObservationJobsEnableCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsService.Enable)
    *   [func (r *ProjectsLocationsObservationJobsService) Get(name string) *ProjectsLocationsObservationJobsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsService.Get)
    *   [func (r *ProjectsLocationsObservationJobsService) List(parent string) *ProjectsLocationsObservationJobsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsService.List)

*   [type ProjectsLocationsObservationSourcesCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesCreateCall)
*       *   [func (c *ProjectsLocationsObservationSourcesCreateCall) Context(ctx context.Context) *ProjectsLocationsObservationSourcesCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesCreateCall.Context)
    *   [func (c *ProjectsLocationsObservationSourcesCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesCreateCall.Do)
    *   [func (c *ProjectsLocationsObservationSourcesCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsObservationSourcesCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesCreateCall.Fields)
    *   [func (c *ProjectsLocationsObservationSourcesCreateCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesCreateCall.Header)
    *   [func (c *ProjectsLocationsObservationSourcesCreateCall) ObservationSourceId(observationSourceId string) *ProjectsLocationsObservationSourcesCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesCreateCall.ObservationSourceId)
    *   [func (c *ProjectsLocationsObservationSourcesCreateCall) RequestId(requestId string) *ProjectsLocationsObservationSourcesCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesCreateCall.RequestId)

*   [type ProjectsLocationsObservationSourcesDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesDeleteCall)
*       *   [func (c *ProjectsLocationsObservationSourcesDeleteCall) Context(ctx context.Context) *ProjectsLocationsObservationSourcesDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesDeleteCall.Context)
    *   [func (c *ProjectsLocationsObservationSourcesDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesDeleteCall.Do)
    *   [func (c *ProjectsLocationsObservationSourcesDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsObservationSourcesDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesDeleteCall.Fields)
    *   [func (c *ProjectsLocationsObservationSourcesDeleteCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesDeleteCall.Header)

*   [type ProjectsLocationsObservationSourcesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesGetCall)
*       *   [func (c *ProjectsLocationsObservationSourcesGetCall) Context(ctx context.Context) *ProjectsLocationsObservationSourcesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesGetCall.Context)
    *   [func (c *ProjectsLocationsObservationSourcesGetCall) Do(opts ...googleapi.CallOption) (*ObservationSource, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesGetCall.Do)
    *   [func (c *ProjectsLocationsObservationSourcesGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsObservationSourcesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesGetCall.Fields)
    *   [func (c *ProjectsLocationsObservationSourcesGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesGetCall.Header)
    *   [func (c *ProjectsLocationsObservationSourcesGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsObservationSourcesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesGetCall.IfNoneMatch)

*   [type ProjectsLocationsObservationSourcesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesListCall)
*       *   [func (c *ProjectsLocationsObservationSourcesListCall) Context(ctx context.Context) *ProjectsLocationsObservationSourcesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesListCall.Context)
    *   [func (c *ProjectsLocationsObservationSourcesListCall) Do(opts ...googleapi.CallOption) (*ListObservationSourcesResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesListCall.Do)
    *   [func (c *ProjectsLocationsObservationSourcesListCall) Fields(s ...googleapi.Field) *ProjectsLocationsObservationSourcesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesListCall.Fields)
    *   [func (c *ProjectsLocationsObservationSourcesListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesListCall.Header)
    *   [func (c *ProjectsLocationsObservationSourcesListCall) IfNoneMatch(entityTag string) *ProjectsLocationsObservationSourcesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesListCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsObservationSourcesListCall) PageSize(pageSize int64) *ProjectsLocationsObservationSourcesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesListCall.PageSize)
    *   [func (c *ProjectsLocationsObservationSourcesListCall) PageToken(pageToken string) *ProjectsLocationsObservationSourcesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesListCall.PageToken)
    *   [func (c *ProjectsLocationsObservationSourcesListCall) Pages(ctx context.Context, f func(*ListObservationSourcesResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesListCall.Pages)

*   [type ProjectsLocationsObservationSourcesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesService)
*       *   [func NewProjectsLocationsObservationSourcesService(s *Service) *ProjectsLocationsObservationSourcesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#NewProjectsLocationsObservationSourcesService)

*       *   [func (r *ProjectsLocationsObservationSourcesService) Create(parent string, observationsource *ObservationSource) *ProjectsLocationsObservationSourcesCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesService.Create)
    *   [func (r *ProjectsLocationsObservationSourcesService) Delete(name string) *ProjectsLocationsObservationSourcesDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesService.Delete)
    *   [func (r *ProjectsLocationsObservationSourcesService) Get(name string) *ProjectsLocationsObservationSourcesGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesService.Get)
    *   [func (r *ProjectsLocationsObservationSourcesService) List(parent string) *ProjectsLocationsObservationSourcesListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesService.List)

*   [type ProjectsLocationsOperationsCancelCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsCancelCall)
*       *   [func (c *ProjectsLocationsOperationsCancelCall) Context(ctx context.Context) *ProjectsLocationsOperationsCancelCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsCancelCall.Context)
    *   [func (c *ProjectsLocationsOperationsCancelCall) Do(opts ...googleapi.CallOption) (*Empty, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsCancelCall.Do)
    *   [func (c *ProjectsLocationsOperationsCancelCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsCancelCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsCancelCall.Fields)
    *   [func (c *ProjectsLocationsOperationsCancelCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsCancelCall.Header)

*   [type ProjectsLocationsOperationsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsDeleteCall)
*       *   [func (c *ProjectsLocationsOperationsDeleteCall) Context(ctx context.Context) *ProjectsLocationsOperationsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsDeleteCall.Context)
    *   [func (c *ProjectsLocationsOperationsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsDeleteCall.Do)
    *   [func (c *ProjectsLocationsOperationsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsDeleteCall.Fields)
    *   [func (c *ProjectsLocationsOperationsDeleteCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsDeleteCall.Header)

*   [type ProjectsLocationsOperationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsGetCall)
*       *   [func (c *ProjectsLocationsOperationsGetCall) Context(ctx context.Context) *ProjectsLocationsOperationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsGetCall.Context)
    *   [func (c *ProjectsLocationsOperationsGetCall) Do(opts ...googleapi.CallOption) (*Operation, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsGetCall.Do)
    *   [func (c *ProjectsLocationsOperationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsGetCall.Fields)
    *   [func (c *ProjectsLocationsOperationsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsGetCall.Header)
    *   [func (c *ProjectsLocationsOperationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsOperationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsGetCall.IfNoneMatch)

*   [type ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsListCall)
*       *   [func (c *ProjectsLocationsOperationsListCall) Context(ctx context.Context) *ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsListCall.Context)
    *   [func (c *ProjectsLocationsOperationsListCall) Do(opts ...googleapi.CallOption) (*ListOperationsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsListCall.Do)
    *   [func (c *ProjectsLocationsOperationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsListCall.Fields)
    *   [func (c *ProjectsLocationsOperationsListCall) Filter(filter string) *ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsListCall.Filter)
    *   [func (c *ProjectsLocationsOperationsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsListCall.Header)
    *   [func (c *ProjectsLocationsOperationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsListCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsOperationsListCall) PageSize(pageSize int64) *ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsListCall.PageSize)
    *   [func (c *ProjectsLocationsOperationsListCall) PageToken(pageToken string) *ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsListCall.PageToken)
    *   [func (c *ProjectsLocationsOperationsListCall) Pages(ctx context.Context, f func(*ListOperationsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsListCall.Pages)
    *   [func (c *ProjectsLocationsOperationsListCall) ReturnPartialSuccess(returnPartialSuccess bool) *ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsListCall.ReturnPartialSuccess)

*   [type ProjectsLocationsOperationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsService)
*       *   [func NewProjectsLocationsOperationsService(s *Service) *ProjectsLocationsOperationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#NewProjectsLocationsOperationsService)

*       *   [func (r *ProjectsLocationsOperationsService) Cancel(name string, canceloperationrequest *CancelOperationRequest) *ProjectsLocationsOperationsCancelCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsService.Cancel)
    *   [func (r *ProjectsLocationsOperationsService) Delete(name string) *ProjectsLocationsOperationsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsService.Delete)
    *   [func (r *ProjectsLocationsOperationsService) Get(name string) *ProjectsLocationsOperationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsService.Get)
    *   [func (r *ProjectsLocationsOperationsService) List(name string) *ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsService.List)

*   [type ProjectsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsService)
*       *   [func NewProjectsLocationsService(s *Service) *ProjectsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#NewProjectsLocationsService)

*       *   [func (r *ProjectsLocationsService) Get(name string) *ProjectsLocationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsService.Get)
    *   [func (r *ProjectsLocationsService) GetEntitlement(name string) *ProjectsLocationsGetEntitlementCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsService.GetEntitlement)
    *   [func (r *ProjectsLocationsService) List(name string) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsService.List)
    *   [func (r *ProjectsLocationsService) ListApiObservationTags(parent string) *ProjectsLocationsListApiObservationTagsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsService.ListApiObservationTags)

*   [type ProjectsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsService)
*       *   [func NewProjectsService(s *Service) *ProjectsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#NewProjectsService)

*   [type Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#Service)
*       *   [func New(client *http.Client) (*Service, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#New)deprecated
    *   [func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#NewService)

*   [type Status](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#Status)
*       *   [func (s Status) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#Status.MarshalJSON)

*   [type TagAction](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#TagAction)
*       *   [func (s TagAction) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#TagAction.MarshalJSON)

[View Source](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/apim/v1alpha/apim-gen.go#L100)

const (
	
	CloudPlatformScope = "https://www.googleapis.com/auth/cloud-platform"
)

OAuth2 scopes used by this API.

This section is empty.

This section is empty.

type ApiObservation struct {
	ApiOperationCount [int64](https://pkg.go.dev/builtin#int64) `json:"apiOperationCount,omitempty,string"`
	CreateTime [string](https://pkg.go.dev/builtin#string) `json:"createTime,omitempty"`
	Hostname [string](https://pkg.go.dev/builtin#string) `json:"hostname,omitempty"`
	LastEventDetectedTime [string](https://pkg.go.dev/builtin#string) `json:"lastEventDetectedTime,omitempty"`
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	
	ServerIps [][string](https://pkg.go.dev/builtin#string) `json:"serverIps,omitempty"`
	
	SourceLocations [][string](https://pkg.go.dev/builtin#string) `json:"sourceLocations,omitempty"`
	
	
	
	
	
	
	Style [string](https://pkg.go.dev/builtin#string) `json:"style,omitempty"`
	Tags [][string](https://pkg.go.dev/builtin#string) `json:"tags,omitempty"`
	UpdateTime [string](https://pkg.go.dev/builtin#string) `json:"updateTime,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ApiObservation: Message describing ApiObservation object

type ApiOperation struct {
	Count [int64](https://pkg.go.dev/builtin#int64) `json:"count,omitempty,string"`
	FirstSeenTime [string](https://pkg.go.dev/builtin#string) `json:"firstSeenTime,omitempty"`
	HttpOperation *[HttpOperation](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#HttpOperation) `json:"httpOperation,omitempty"`
	LastSeenTime [string](https://pkg.go.dev/builtin#string) `json:"lastSeenTime,omitempty"`
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ApiOperation: Message describing ApiOperation object

type BatchEditTagsApiObservationsRequest struct {
	
	Requests []*[EditTagsApiObservationsRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#EditTagsApiObservationsRequest) `json:"requests,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

BatchEditTagsApiObservationsRequest: Message for requesting batch edit tags for ApiObservations

type BatchEditTagsApiObservationsResponse struct {
	ApiObservations []*[ApiObservation](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ApiObservation) `json:"apiObservations,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

BatchEditTagsApiObservationsResponse: Message for response to edit Tags for ApiObservations

type CancelOperationRequest struct {
}

CancelOperationRequest: The request message for Operations.CancelOperation.

type DisableObservationJobRequest struct {
}

DisableObservationJobRequest: Message for disabling an ObservationJob

type EditTagsApiObservationsRequest struct {
	
	ApiObservationId [string](https://pkg.go.dev/builtin#string) `json:"apiObservationId,omitempty"`
	TagActions []*[TagAction](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#TagAction) `json:"tagActions,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

EditTagsApiObservationsRequest: Message for requesting edit tags for ApiObservation

Empty: A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }

type EnableObservationJobRequest struct {
}

EnableObservationJobRequest: Message for enabling an ObservationJob

type Entitlement struct {
	ApiObservationEntitled [bool](https://pkg.go.dev/builtin#bool) `json:"apiObservationEntitled,omitempty"`
	
	BillingProjectNumber [int64](https://pkg.go.dev/builtin#int64) `json:"billingProjectNumber,omitempty,string"`
	CreateTime [string](https://pkg.go.dev/builtin#string) `json:"createTime,omitempty"`
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	UpdateTime [string](https://pkg.go.dev/builtin#string) `json:"updateTime,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

Entitlement: Entitlement stores data related to API Observation entitlement for a given project

type GclbObservationSource struct {
	
	
	PscNetworkConfigs []*[GclbObservationSourcePscNetworkConfig](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#GclbObservationSourcePscNetworkConfig) `json:"pscNetworkConfigs,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

GclbObservationSource: The GCLB observation source.

type GclbObservationSourcePscNetworkConfig struct {
	
	Network [string](https://pkg.go.dev/builtin#string) `json:"network,omitempty"`
	
	
	
	Subnetwork [string](https://pkg.go.dev/builtin#string) `json:"subnetwork,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

GclbObservationSourcePscNetworkConfig: Network information for setting up a PSC connection.

type HttpOperation struct {
	
	
	
	
	
	
	
	
	
	
	
	
	Method [string](https://pkg.go.dev/builtin#string) `json:"method,omitempty"`
	Path [string](https://pkg.go.dev/builtin#string) `json:"path,omitempty"`
	PathParams []*[HttpOperationPathParam](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#HttpOperationPathParam) `json:"pathParams,omitempty"`
	QueryParams map[[string](https://pkg.go.dev/builtin#string)][HttpOperationQueryParam](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#HttpOperationQueryParam) `json:"queryParams,omitempty"`
	Request *[HttpOperationHttpRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#HttpOperationHttpRequest) `json:"request,omitempty"`
	Response *[HttpOperationHttpResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#HttpOperationHttpResponse) `json:"response,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

HttpOperation: An HTTP-based API Operation, sometimes called a "REST" Operation.

type HttpOperationHeader struct {
	Count [int64](https://pkg.go.dev/builtin#int64) `json:"count,omitempty,string"`
	
	
	
	
	
	
	
	
	DataType [string](https://pkg.go.dev/builtin#string) `json:"dataType,omitempty"`
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

HttpOperationHeader: An aggregation of HTTP header occurrences.

type HttpOperationHttpRequest struct {
	Headers map[[string](https://pkg.go.dev/builtin#string)][HttpOperationHeader](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#HttpOperationHeader) `json:"headers,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

HttpOperationHttpRequest: An aggregation of HTTP requests.

type HttpOperationHttpResponse struct {
	Headers map[[string](https://pkg.go.dev/builtin#string)][HttpOperationHeader](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#HttpOperationHeader) `json:"headers,omitempty"`
	ResponseCodes map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `json:"responseCodes,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

HttpOperationHttpResponse: An aggregation of HTTP responses.

type HttpOperationPathParam struct {
	
	
	
	
	
	
	
	
	DataType [string](https://pkg.go.dev/builtin#string) `json:"dataType,omitempty"`
	Position [int64](https://pkg.go.dev/builtin#int64) `json:"position,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

HttpOperationPathParam: HTTP Path parameter.

type HttpOperationQueryParam struct {
	
	Count [int64](https://pkg.go.dev/builtin#int64) `json:"count,omitempty,string"`
	
	
	
	
	
	
	
	
	DataType [string](https://pkg.go.dev/builtin#string) `json:"dataType,omitempty"`
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

HttpOperationQueryParam: An aggregation of HTTP query parameter occurrences.

type ListApiObservationTagsResponse struct {
	ApiObservationTags [][string](https://pkg.go.dev/builtin#string) `json:"apiObservationTags,omitempty"`
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListApiObservationTagsResponse: Message for response to listing tags

type ListApiObservationsResponse struct {
	
	ApiObservations []*[ApiObservation](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ApiObservation) `json:"apiObservations,omitempty"`
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListApiObservationsResponse: Message for response to listing ApiObservations

type ListApiOperationsResponse struct {
	
	ApiOperations []*[ApiOperation](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ApiOperation) `json:"apiOperations,omitempty"`
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListApiOperationsResponse: Message for response to listing ApiOperations

type ListLocationsResponse struct {
	
	Locations []*[Location](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#Location) `json:"locations,omitempty"`
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListLocationsResponse: The response message for Locations.ListLocations.

type ListObservationJobsResponse struct {
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`
	ObservationJobs []*[ObservationJob](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ObservationJob) `json:"observationJobs,omitempty"`
	Unreachable [][string](https://pkg.go.dev/builtin#string) `json:"unreachable,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListObservationJobsResponse: Message for response to listing ObservationJobs

type ListObservationSourcesResponse struct {
	
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`
	
	ObservationSources []*[ObservationSource](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ObservationSource) `json:"observationSources,omitempty"`
	Unreachable [][string](https://pkg.go.dev/builtin#string) `json:"unreachable,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListObservationSourcesResponse: Message for response to listing ObservationSources

type ListOperationsResponse struct {
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`
	
	Operations []*[Operation](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#Operation) `json:"operations,omitempty"`
	
	
	
	Unreachable [][string](https://pkg.go.dev/builtin#string) `json:"unreachable,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ListOperationsResponse: The response message for Operations.ListOperations.

Location: A resource that represents a Google Cloud location.

type ObservationJob struct {
	CreateTime [string](https://pkg.go.dev/builtin#string) `json:"createTime,omitempty"`
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	Sources [][string](https://pkg.go.dev/builtin#string) `json:"sources,omitempty"`
	
	
	
	
	
	
	
	
	
	
	State [string](https://pkg.go.dev/builtin#string) `json:"state,omitempty"`
	UpdateTime [string](https://pkg.go.dev/builtin#string) `json:"updateTime,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ObservationJob: Message describing ObservationJob object

type ObservationSource struct {
	CreateTime [string](https://pkg.go.dev/builtin#string) `json:"createTime,omitempty"`
	GclbObservationSource *[GclbObservationSource](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#GclbObservationSource) `json:"gclbObservationSource,omitempty"`
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	
	
	
	
	
	
	State [string](https://pkg.go.dev/builtin#string) `json:"state,omitempty"`
	UpdateTime [string](https://pkg.go.dev/builtin#string) `json:"updateTime,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ObservationSource: Observation source configuration types

Operation: This resource represents a long-running operation that is the result of a network API call.

type OperationMetadata struct {
	ApiVersion [string](https://pkg.go.dev/builtin#string) `json:"apiVersion,omitempty"`
	CreateTime [string](https://pkg.go.dev/builtin#string) `json:"createTime,omitempty"`
	EndTime [string](https://pkg.go.dev/builtin#string) `json:"endTime,omitempty"`
	
	
	
	RequestedCancellation [bool](https://pkg.go.dev/builtin#bool) `json:"requestedCancellation,omitempty"`
	StatusMessage [string](https://pkg.go.dev/builtin#string) `json:"statusMessage,omitempty"`
	
	Target [string](https://pkg.go.dev/builtin#string) `json:"target,omitempty"`
	Verb [string](https://pkg.go.dev/builtin#string) `json:"verb,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

OperationMetadata: Represents the metadata of the long-running operation.

type ProjectsLocationsGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apim.projects.locations.get" call. Any non-2xx status code is an error. Response headers are in either *Location.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsGetEntitlementCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apim.projects.locations.getEntitlement" call. Any non-2xx status code is an error. Response headers are in either *Entitlement.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsListApiObservationTagsCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apim.projects.locations.listApiObservationTags" call. Any non-2xx status code is an error. Response headers are in either *ListApiObservationTagsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": The maximum number of tags to return. The service may return fewer than this value. If unspecified, at most 10 tags will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListApiObservationTags` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListApiObservationTags` must match the call that provided the page token.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apim.projects.locations.list" call. Any non-2xx status code is an error. Response headers are in either *ListLocationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (c *[ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsListCall)) ExtraLocationTypes(extraLocationTypes ...[string](https://pkg.go.dev/builtin#string)) *[ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsListCall)

ExtraLocationTypes sets the optional parameter "extraLocationTypes": Do not use this field. It is unsupported and is ignored unless explicitly documented otherwise. This is primarily for internal usage.

Filter sets the optional parameter "filter": A filter to narrow down results to a preferred subset. The filtering language accepts strings like "displayName=tokyo", and is documented in more detail in AIP-160 ([https://google.aip.dev/160](https://google.aip.dev/160)).

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": The maximum number of results to return. If not set, the service selects a default.

PageToken sets the optional parameter "pageToken": A page token received from the `next_page_token` field in the response. Send that page token to receive the subsequent page.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsObservationJobsApiObservationsApiOperationsGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apim.projects.locations.observationJobs.apiObservations.apiOperations.get" call. Any non-2xx status code is an error. Response headers are in either *ApiOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsObservationJobsApiObservationsApiOperationsListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apim.projects.locations.observationJobs.apiObservations.apiOperations.list" call. Any non-2xx status code is an error. Response headers are in either *ListApiOperationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": The maximum number of ApiOperations to return. The service may return fewer than this value. If unspecified, at most 10 ApiOperations will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListApiApiOperations` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListApiApiOperations` must match the call that provided the page token.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsObservationJobsApiObservationsApiOperationsService struct {
	
}

func NewProjectsLocationsObservationJobsApiObservationsApiOperationsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#Service)) *[ProjectsLocationsObservationJobsApiObservationsApiOperationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsApiOperationsService)

Get: GetApiOperation retrieves a single ApiOperation by name.

*   name: The name of the ApiOperation to retrieve. Format: projects/{project}/locations/{location}/observationJobs/{observation_job}/a piObservations/{api_observation}/apiOperation/{api_operation}.

List: ListApiOperations gets all ApiOperations for a given project and location and ObservationJob and ApiObservation.

*   parent: The parent, which owns this collection of ApiOperations. Format: projects/{project}/locations/{location}/observationJobs/{observation_job}/a piObservations/{api_observation}.

type ProjectsLocationsObservationJobsApiObservationsBatchEditTagsCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apim.projects.locations.observationJobs.apiObservations.batchEditTags" call. Any non-2xx status code is an error. Response headers are in either *BatchEditTagsApiObservationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsObservationJobsApiObservationsGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apim.projects.locations.observationJobs.apiObservations.get" call. Any non-2xx status code is an error. Response headers are in either *ApiObservation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsObservationJobsApiObservationsListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apim.projects.locations.observationJobs.apiObservations.list" call. Any non-2xx status code is an error. Response headers are in either *ListApiObservationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": The maximum number of ApiObservations to return. The service may return fewer than this value. If unspecified, at most 10 ApiObservations will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListApiObservations` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListApiObservations` must match the call that provided the page token.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsObservationJobsApiObservationsService struct {
 ApiOperations *[ProjectsLocationsObservationJobsApiObservationsApiOperationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsApiOperationsService)	
}

func NewProjectsLocationsObservationJobsApiObservationsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#Service)) *[ProjectsLocationsObservationJobsApiObservationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsService)

BatchEditTags: BatchEditTagsApiObservations adds or removes Tags for ApiObservations.

*   parent: The parent resource shared by all ApiObservations being edited. Format: projects/{project}/locations/{location}/observationJobs/{observation_job}.

Get: GetApiObservation retrieves a single ApiObservation by name.

*   name: The name of the ApiObservation to retrieve. Format: projects/{project}/locations/{location}/observationJobs/{observation_job}/a piObservations/{api_observation}.

List: ListApiObservations gets all ApiObservations for a given project and location and ObservationJob.

*   parent: The parent, which owns this collection of ApiObservations. Format: projects/{project}/locations/{location}/observationJobs/{observation_job}.

type ProjectsLocationsObservationJobsCreateCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apim.projects.locations.observationJobs.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

ObservationJobId sets the optional parameter "observationJobId": Required. The ID to use for the Observation Job. This value should be 4-63 characters, and valid characters are /a-z-/.

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

type ProjectsLocationsObservationJobsDeleteCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apim.projects.locations.observationJobs.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsObservationJobsDisableCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apim.projects.locations.observationJobs.disable" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsObservationJobsEnableCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apim.projects.locations.observationJobs.enable" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsObservationJobsGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apim.projects.locations.observationJobs.get" call. Any non-2xx status code is an error. Response headers are in either *ObservationJob.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsObservationJobsListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apim.projects.locations.observationJobs.list" call. Any non-2xx status code is an error. Response headers are in either *ListObservationJobsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": The maximum number of ObservationJobs to return. The service may return fewer than this value. If unspecified, at most 10 ObservationJobs will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListObservationJobs` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListObservationJobs` must match the call that provided the page token.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsObservationJobsService struct {
 ApiObservations *[ProjectsLocationsObservationJobsApiObservationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsApiObservationsService)	
}

func NewProjectsLocationsObservationJobsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#Service)) *[ProjectsLocationsObservationJobsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsService)

Create: CreateObservationJob creates a new ObservationJob but does not have any effecton its own. It is a configuration that can be used in an Observation Job to collect data about existing APIs.

*   parent: The parent resource where this ObservationJob will be created. Format: projects/{project}/locations/{location}.

Delete: DeleteObservationJob deletes an ObservationJob. This method will fail if the observation job is currently being used by any ObservationSource, even if not enabled.

*   name: Name of the resource Format: projects/{project}/locations/{location}/observationJobs/{observation_job}.

Disable: Disables the given ObservationJob.

*   name: The name of the ObservationJob to disable. Format: projects/{project}/locations/{location}/observationJobs/{job}.

Enable: Enables the given ObservationJob.

*   name: The name of the ObservationJob to enable. Format: projects/{project}/locations/{location}/observationJobs/{job}.

Get: GetObservationJob retrieves a single ObservationJob by name.

*   name: The name of the ObservationJob to retrieve. Format: projects/{project}/locations/{location}/observationJobs/{job}.

List: ListObservationJobs gets all ObservationJobs for a given project and location.

*   parent: The parent, which owns this collection of ObservationJobs. Format: projects/{project}/locations/{location}.

type ProjectsLocationsObservationSourcesCreateCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apim.projects.locations.observationSources.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

ObservationSourceId sets the optional parameter "observationSourceId": Required. The ID to use for the Observation Source. This value should be 4-63 characters, and valid characters are /a-z-/.

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

type ProjectsLocationsObservationSourcesDeleteCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apim.projects.locations.observationSources.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsObservationSourcesGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apim.projects.locations.observationSources.get" call. Any non-2xx status code is an error. Response headers are in either *ObservationSource.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsObservationSourcesListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apim.projects.locations.observationSources.list" call. Any non-2xx status code is an error. Response headers are in either *ListObservationSourcesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": The maximum number of ObservationSources to return. The service may return fewer than this value. If unspecified, at most 10 ObservationSources will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

PageToken sets the optional parameter "pageToken": A page token, received from a previous `ListObservationSources` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListObservationSources` must match the call that provided the page token.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsObservationSourcesService struct {
	
}

func NewProjectsLocationsObservationSourcesService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#Service)) *[ProjectsLocationsObservationSourcesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesService)

Create: CreateObservationSource creates a new ObservationSource but does not affect any deployed infrastructure. It is a configuration that can be used in an Observation Job to collect data about APIs running in user's dataplane.

- parent: Value for parent.

Delete: DeleteObservationSource deletes an observation source. This method will fail if the observation source is currently being used by any ObservationJob, even if not enabled.

*   name: Name of the resource Format: projects/{project}/locations/{location}/observationSources/{source}.

Get: GetObservationSource retrieves a single ObservationSource by name.

*   name: The name of the ObservationSource to retrieve. Format: projects/{project}/locations/{location}/observationSources/{source}.

List: ListObservationSources gets all ObservationSources for a given project and location.

*   parent: The parent, which owns this collection of ObservationSources. Format: projects/{project}/locations/{location}.

type ProjectsLocationsOperationsCancelCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apim.projects.locations.operations.cancel" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsOperationsDeleteCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apim.projects.locations.operations.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsOperationsGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apim.projects.locations.operations.get" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsOperationsListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apim.projects.locations.operations.list" call. Any non-2xx status code is an error. Response headers are in either *ListOperationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Filter sets the optional parameter "filter": The standard list filter.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": The standard list page size.

PageToken sets the optional parameter "pageToken": The standard list page token.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (c *[ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsListCall)) ReturnPartialSuccess(returnPartialSuccess [bool](https://pkg.go.dev/builtin#bool)) *[ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsListCall)

ReturnPartialSuccess sets the optional parameter "returnPartialSuccess": When set to `true`, operations that are reachable are returned as normal, and those that are unreachable are returned in the ListOperationsResponse.unreachable field. This can only be `true` when reading across collections. For example, when `parent` is set to "projects/example/locations/-". This field is not supported by default and will result in an `UNIMPLEMENTED` error if set unless explicitly documented otherwise in service or product specific documentation.

type ProjectsLocationsOperationsService struct {
	
}

func NewProjectsLocationsOperationsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#Service)) *[ProjectsLocationsOperationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsService)

Cancel: Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of `1`, corresponding to `Code.CANCELLED`.

- name: The name of the operation resource to be cancelled.

Delete: Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

- name: The name of the operation resource to be deleted.

Get: Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

- name: The name of the operation resource.

List: Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.

- name: The name of the operation's parent resource.

type ProjectsLocationsService struct {
 ObservationJobs *[ProjectsLocationsObservationJobsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationJobsService)
 ObservationSources *[ProjectsLocationsObservationSourcesService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsObservationSourcesService)
 Operations *[ProjectsLocationsOperationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsOperationsService)	
}

func NewProjectsLocationsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#Service)) *[ProjectsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsService)

Get: Gets information about a location.

- name: Resource name for the location.

GetEntitlement: GetEntitlement returns the entitlement for the provided project.

*   name: The entitlement resource name Format: projects/{project}/locations/{location}/entitlement.

List: Lists information about the supported locations for this service. This method can be called in two ways: * **List all public locations:** Use the path `GET /v1/locations`. * **List project-visible locations:** Use the path `GET /v1/projects/{project_id}/locations`. This may include public locations as well as private or other locations specifically visible to the project.

- name: The resource that owns the locations collection, if applicable.

ListApiObservationTags: ListApiObservationTags lists all extant tags on any observation in the given project.

*   parent: The parent, which owns this collection of tags. Format: projects/{project}/locations/{location}.

type ProjectsService struct {
 Locations *[ProjectsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsLocationsService)	
}

func NewProjectsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#Service)) *[ProjectsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apim/v1alpha#ProjectsService)

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

type TagAction struct {
	
	
	
	
	
	Action [string](https://pkg.go.dev/builtin#string) `json:"action,omitempty"`
	Tag [string](https://pkg.go.dev/builtin#string) `json:"tag,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

TagAction: Message for edit tag action
