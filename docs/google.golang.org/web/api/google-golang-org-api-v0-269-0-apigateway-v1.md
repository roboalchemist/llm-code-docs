# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1

Title: apigateway package - google.golang.org/api/apigateway/v1 - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1

Markdown Content:
Package apigateway provides access to the API Gateway API.

For product documentation, see: [https://cloud.google.com/api-gateway/docs](https://cloud.google.com/api-gateway/docs)

#### Library status [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#hdr-Library_status "Go to Library status")

These client libraries are officially supported by Google. However, this library is considered complete and is in maintenance mode. This means that we will address critical bugs and security issues but will not add any new features.

When possible, we recommend using our newer [Cloud Client Libraries for Go]([https://pkg.go.dev/cloud.google.com/go](https://pkg.go.dev/cloud.google.com/go)) that are still actively being worked and iterated on.

#### Creating a client [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#hdr-Creating_a_client "Go to Creating a client")

Usage example:

import "google.golang.org/api/apigateway/v1"
...
ctx := context.Background()
apigatewayService, err := apigateway.NewService(ctx)

In this example, Google Application Default Credentials are used for authentication. For information on how to create and obtain Application Default Credentials, see [https://developers.google.com/identity/protocols/application-default-credentials](https://developers.google.com/identity/protocols/application-default-credentials).

#### Other authentication options [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#hdr-Other_authentication_options "Go to Other authentication options")

To use an API key for authentication (note: some APIs do not support API keys), use [google.golang.org/api/option.WithAPIKey](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#WithAPIKey):

apigatewayService, err := apigateway.NewService(ctx, option.WithAPIKey("AIza..."))

To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow, use [google.golang.org/api/option.WithTokenSource](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#WithTokenSource):

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
apigatewayService, err := apigateway.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))

See [google.golang.org/api/option.ClientOption](https://pkg.go.dev/google.golang.org/api@v0.269.0/option#ClientOption) for details on options.

*   [Constants](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#pkg-constants)
*   [type ApigatewayApi](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayApi)
*       *   [func (s ApigatewayApi) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayApi.MarshalJSON)

*   [type ApigatewayApiConfig](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayApiConfig)
*       *   [func (s ApigatewayApiConfig) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayApiConfig.MarshalJSON)

*   [type ApigatewayApiConfigFile](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayApiConfigFile)
*       *   [func (s ApigatewayApiConfigFile) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayApiConfigFile.MarshalJSON)

*   [type ApigatewayApiConfigGrpcServiceDefinition](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayApiConfigGrpcServiceDefinition)
*       *   [func (s ApigatewayApiConfigGrpcServiceDefinition) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayApiConfigGrpcServiceDefinition.MarshalJSON)

*   [type ApigatewayApiConfigOpenApiDocument](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayApiConfigOpenApiDocument)
*       *   [func (s ApigatewayApiConfigOpenApiDocument) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayApiConfigOpenApiDocument.MarshalJSON)

*   [type ApigatewayAuditConfig](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayAuditConfig)
*       *   [func (s ApigatewayAuditConfig) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayAuditConfig.MarshalJSON)

*   [type ApigatewayAuditLogConfig](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayAuditLogConfig)
*       *   [func (s ApigatewayAuditLogConfig) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayAuditLogConfig.MarshalJSON)

*   [type ApigatewayBinding](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayBinding)
*       *   [func (s ApigatewayBinding) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayBinding.MarshalJSON)

*   [type ApigatewayCancelOperationRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayCancelOperationRequest)
*   [type ApigatewayExpr](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayExpr)
*       *   [func (s ApigatewayExpr) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayExpr.MarshalJSON)

*   [type ApigatewayGateway](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayGateway)
*       *   [func (s ApigatewayGateway) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayGateway.MarshalJSON)

*   [type ApigatewayListApiConfigsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayListApiConfigsResponse)
*       *   [func (s ApigatewayListApiConfigsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayListApiConfigsResponse.MarshalJSON)

*   [type ApigatewayListApisResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayListApisResponse)
*       *   [func (s ApigatewayListApisResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayListApisResponse.MarshalJSON)

*   [type ApigatewayListGatewaysResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayListGatewaysResponse)
*       *   [func (s ApigatewayListGatewaysResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayListGatewaysResponse.MarshalJSON)

*   [type ApigatewayListLocationsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayListLocationsResponse)
*       *   [func (s ApigatewayListLocationsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayListLocationsResponse.MarshalJSON)

*   [type ApigatewayListOperationsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayListOperationsResponse)
*       *   [func (s ApigatewayListOperationsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayListOperationsResponse.MarshalJSON)

*   [type ApigatewayLocation](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayLocation)
*       *   [func (s ApigatewayLocation) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayLocation.MarshalJSON)

*   [type ApigatewayOperation](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayOperation)
*       *   [func (s ApigatewayOperation) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayOperation.MarshalJSON)

*   [type ApigatewayOperationMetadata](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayOperationMetadata)
*       *   [func (s ApigatewayOperationMetadata) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayOperationMetadata.MarshalJSON)

*   [type ApigatewayOperationMetadataDiagnostic](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayOperationMetadataDiagnostic)
*       *   [func (s ApigatewayOperationMetadataDiagnostic) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayOperationMetadataDiagnostic.MarshalJSON)

*   [type ApigatewayPolicy](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayPolicy)
*       *   [func (s ApigatewayPolicy) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayPolicy.MarshalJSON)

*   [type ApigatewaySetIamPolicyRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewaySetIamPolicyRequest)
*       *   [func (s ApigatewaySetIamPolicyRequest) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewaySetIamPolicyRequest.MarshalJSON)

*   [type ApigatewayStatus](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayStatus)
*       *   [func (s ApigatewayStatus) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayStatus.MarshalJSON)

*   [type ApigatewayTestIamPermissionsRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayTestIamPermissionsRequest)
*       *   [func (s ApigatewayTestIamPermissionsRequest) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayTestIamPermissionsRequest.MarshalJSON)

*   [type ApigatewayTestIamPermissionsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayTestIamPermissionsResponse)
*       *   [func (s ApigatewayTestIamPermissionsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayTestIamPermissionsResponse.MarshalJSON)

*   [type Empty](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#Empty)
*   [type ProjectsLocationsApisConfigsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsCreateCall)
*       *   [func (c *ProjectsLocationsApisConfigsCreateCall) ApiConfigId(apiConfigId string) *ProjectsLocationsApisConfigsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsCreateCall.ApiConfigId)
    *   [func (c *ProjectsLocationsApisConfigsCreateCall) Context(ctx context.Context) *ProjectsLocationsApisConfigsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsCreateCall.Context)
    *   [func (c *ProjectsLocationsApisConfigsCreateCall) Do(opts ...googleapi.CallOption) (*ApigatewayOperation, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsCreateCall.Do)
    *   [func (c *ProjectsLocationsApisConfigsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisConfigsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsCreateCall.Fields)
    *   [func (c *ProjectsLocationsApisConfigsCreateCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsCreateCall.Header)

*   [type ProjectsLocationsApisConfigsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsDeleteCall)
*       *   [func (c *ProjectsLocationsApisConfigsDeleteCall) Context(ctx context.Context) *ProjectsLocationsApisConfigsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsDeleteCall.Context)
    *   [func (c *ProjectsLocationsApisConfigsDeleteCall) Do(opts ...googleapi.CallOption) (*ApigatewayOperation, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsDeleteCall.Do)
    *   [func (c *ProjectsLocationsApisConfigsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisConfigsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsDeleteCall.Fields)
    *   [func (c *ProjectsLocationsApisConfigsDeleteCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsDeleteCall.Header)

*   [type ProjectsLocationsApisConfigsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsGetCall)
*       *   [func (c *ProjectsLocationsApisConfigsGetCall) Context(ctx context.Context) *ProjectsLocationsApisConfigsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsGetCall.Context)
    *   [func (c *ProjectsLocationsApisConfigsGetCall) Do(opts ...googleapi.CallOption) (*ApigatewayApiConfig, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsGetCall.Do)
    *   [func (c *ProjectsLocationsApisConfigsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisConfigsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsGetCall.Fields)
    *   [func (c *ProjectsLocationsApisConfigsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsGetCall.Header)
    *   [func (c *ProjectsLocationsApisConfigsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisConfigsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsGetCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsApisConfigsGetCall) View(view string) *ProjectsLocationsApisConfigsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsGetCall.View)

*   [type ProjectsLocationsApisConfigsGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsGetIamPolicyCall)
*       *   [func (c *ProjectsLocationsApisConfigsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisConfigsGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsGetIamPolicyCall.Context)
    *   [func (c *ProjectsLocationsApisConfigsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*ApigatewayPolicy, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsGetIamPolicyCall.Do)
    *   [func (c *ProjectsLocationsApisConfigsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisConfigsGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsGetIamPolicyCall.Fields)
    *   [func (c *ProjectsLocationsApisConfigsGetIamPolicyCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsGetIamPolicyCall.Header)
    *   [func (c *ProjectsLocationsApisConfigsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisConfigsGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsGetIamPolicyCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsApisConfigsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsApisConfigsGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsGetIamPolicyCall.OptionsRequestedPolicyVersion)

*   [type ProjectsLocationsApisConfigsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsListCall)
*       *   [func (c *ProjectsLocationsApisConfigsListCall) Context(ctx context.Context) *ProjectsLocationsApisConfigsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsListCall.Context)
    *   [func (c *ProjectsLocationsApisConfigsListCall) Do(opts ...googleapi.CallOption) (*ApigatewayListApiConfigsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsListCall.Do)
    *   [func (c *ProjectsLocationsApisConfigsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisConfigsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsListCall.Fields)
    *   [func (c *ProjectsLocationsApisConfigsListCall) Filter(filter string) *ProjectsLocationsApisConfigsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsListCall.Filter)
    *   [func (c *ProjectsLocationsApisConfigsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsListCall.Header)
    *   [func (c *ProjectsLocationsApisConfigsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisConfigsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsListCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsApisConfigsListCall) OrderBy(orderBy string) *ProjectsLocationsApisConfigsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsListCall.OrderBy)
    *   [func (c *ProjectsLocationsApisConfigsListCall) PageSize(pageSize int64) *ProjectsLocationsApisConfigsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsListCall.PageSize)
    *   [func (c *ProjectsLocationsApisConfigsListCall) PageToken(pageToken string) *ProjectsLocationsApisConfigsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsListCall.PageToken)
    *   [func (c *ProjectsLocationsApisConfigsListCall) Pages(ctx context.Context, f func(*ApigatewayListApiConfigsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsListCall.Pages)

*   [type ProjectsLocationsApisConfigsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsPatchCall)
*       *   [func (c *ProjectsLocationsApisConfigsPatchCall) Context(ctx context.Context) *ProjectsLocationsApisConfigsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsPatchCall.Context)
    *   [func (c *ProjectsLocationsApisConfigsPatchCall) Do(opts ...googleapi.CallOption) (*ApigatewayOperation, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsPatchCall.Do)
    *   [func (c *ProjectsLocationsApisConfigsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisConfigsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsPatchCall.Fields)
    *   [func (c *ProjectsLocationsApisConfigsPatchCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsPatchCall.Header)
    *   [func (c *ProjectsLocationsApisConfigsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApisConfigsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsPatchCall.UpdateMask)

*   [type ProjectsLocationsApisConfigsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsService)
*       *   [func NewProjectsLocationsApisConfigsService(s *Service) *ProjectsLocationsApisConfigsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#NewProjectsLocationsApisConfigsService)

*       *   [func (r *ProjectsLocationsApisConfigsService) Create(parent string, apigatewayapiconfig *ApigatewayApiConfig) *ProjectsLocationsApisConfigsCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsService.Create)
    *   [func (r *ProjectsLocationsApisConfigsService) Delete(name string) *ProjectsLocationsApisConfigsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsService.Delete)
    *   [func (r *ProjectsLocationsApisConfigsService) Get(name string) *ProjectsLocationsApisConfigsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsService.Get)
    *   [func (r *ProjectsLocationsApisConfigsService) GetIamPolicy(resource string) *ProjectsLocationsApisConfigsGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsService.GetIamPolicy)
    *   [func (r *ProjectsLocationsApisConfigsService) List(parent string) *ProjectsLocationsApisConfigsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsService.List)
    *   [func (r *ProjectsLocationsApisConfigsService) Patch(name string, apigatewayapiconfig *ApigatewayApiConfig) *ProjectsLocationsApisConfigsPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsService.Patch)
    *   [func (r *ProjectsLocationsApisConfigsService) SetIamPolicy(resource string, apigatewaysetiampolicyrequest *ApigatewaySetIamPolicyRequest) *ProjectsLocationsApisConfigsSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsService.SetIamPolicy)
    *   [func (r *ProjectsLocationsApisConfigsService) TestIamPermissions(resource string, ...) *ProjectsLocationsApisConfigsTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsService.TestIamPermissions)

*   [type ProjectsLocationsApisConfigsSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsSetIamPolicyCall)
*       *   [func (c *ProjectsLocationsApisConfigsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisConfigsSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsSetIamPolicyCall.Context)
    *   [func (c *ProjectsLocationsApisConfigsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*ApigatewayPolicy, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsSetIamPolicyCall.Do)
    *   [func (c *ProjectsLocationsApisConfigsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisConfigsSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsSetIamPolicyCall.Fields)
    *   [func (c *ProjectsLocationsApisConfigsSetIamPolicyCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsSetIamPolicyCall.Header)

*   [type ProjectsLocationsApisConfigsTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsTestIamPermissionsCall)
*       *   [func (c *ProjectsLocationsApisConfigsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsApisConfigsTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsTestIamPermissionsCall.Context)
    *   [func (c *ProjectsLocationsApisConfigsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*ApigatewayTestIamPermissionsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsTestIamPermissionsCall.Do)
    *   [func (c *ProjectsLocationsApisConfigsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisConfigsTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsTestIamPermissionsCall.Fields)
    *   [func (c *ProjectsLocationsApisConfigsTestIamPermissionsCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsTestIamPermissionsCall.Header)

*   [type ProjectsLocationsApisCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisCreateCall)
*       *   [func (c *ProjectsLocationsApisCreateCall) ApiId(apiId string) *ProjectsLocationsApisCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisCreateCall.ApiId)
    *   [func (c *ProjectsLocationsApisCreateCall) Context(ctx context.Context) *ProjectsLocationsApisCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisCreateCall.Context)
    *   [func (c *ProjectsLocationsApisCreateCall) Do(opts ...googleapi.CallOption) (*ApigatewayOperation, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisCreateCall.Do)
    *   [func (c *ProjectsLocationsApisCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisCreateCall.Fields)
    *   [func (c *ProjectsLocationsApisCreateCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisCreateCall.Header)

*   [type ProjectsLocationsApisDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisDeleteCall)
*       *   [func (c *ProjectsLocationsApisDeleteCall) Context(ctx context.Context) *ProjectsLocationsApisDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisDeleteCall.Context)
    *   [func (c *ProjectsLocationsApisDeleteCall) Do(opts ...googleapi.CallOption) (*ApigatewayOperation, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisDeleteCall.Do)
    *   [func (c *ProjectsLocationsApisDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisDeleteCall.Fields)
    *   [func (c *ProjectsLocationsApisDeleteCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisDeleteCall.Header)

*   [type ProjectsLocationsApisGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisGetCall)
*       *   [func (c *ProjectsLocationsApisGetCall) Context(ctx context.Context) *ProjectsLocationsApisGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisGetCall.Context)
    *   [func (c *ProjectsLocationsApisGetCall) Do(opts ...googleapi.CallOption) (*ApigatewayApi, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisGetCall.Do)
    *   [func (c *ProjectsLocationsApisGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisGetCall.Fields)
    *   [func (c *ProjectsLocationsApisGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisGetCall.Header)
    *   [func (c *ProjectsLocationsApisGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisGetCall.IfNoneMatch)

*   [type ProjectsLocationsApisGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisGetIamPolicyCall)
*       *   [func (c *ProjectsLocationsApisGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisGetIamPolicyCall.Context)
    *   [func (c *ProjectsLocationsApisGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*ApigatewayPolicy, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisGetIamPolicyCall.Do)
    *   [func (c *ProjectsLocationsApisGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisGetIamPolicyCall.Fields)
    *   [func (c *ProjectsLocationsApisGetIamPolicyCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisGetIamPolicyCall.Header)
    *   [func (c *ProjectsLocationsApisGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisGetIamPolicyCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsApisGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsApisGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisGetIamPolicyCall.OptionsRequestedPolicyVersion)

*   [type ProjectsLocationsApisListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisListCall)
*       *   [func (c *ProjectsLocationsApisListCall) Context(ctx context.Context) *ProjectsLocationsApisListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisListCall.Context)
    *   [func (c *ProjectsLocationsApisListCall) Do(opts ...googleapi.CallOption) (*ApigatewayListApisResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisListCall.Do)
    *   [func (c *ProjectsLocationsApisListCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisListCall.Fields)
    *   [func (c *ProjectsLocationsApisListCall) Filter(filter string) *ProjectsLocationsApisListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisListCall.Filter)
    *   [func (c *ProjectsLocationsApisListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisListCall.Header)
    *   [func (c *ProjectsLocationsApisListCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisListCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsApisListCall) OrderBy(orderBy string) *ProjectsLocationsApisListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisListCall.OrderBy)
    *   [func (c *ProjectsLocationsApisListCall) PageSize(pageSize int64) *ProjectsLocationsApisListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisListCall.PageSize)
    *   [func (c *ProjectsLocationsApisListCall) PageToken(pageToken string) *ProjectsLocationsApisListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisListCall.PageToken)
    *   [func (c *ProjectsLocationsApisListCall) Pages(ctx context.Context, f func(*ApigatewayListApisResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisListCall.Pages)

*   [type ProjectsLocationsApisPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisPatchCall)
*       *   [func (c *ProjectsLocationsApisPatchCall) Context(ctx context.Context) *ProjectsLocationsApisPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisPatchCall.Context)
    *   [func (c *ProjectsLocationsApisPatchCall) Do(opts ...googleapi.CallOption) (*ApigatewayOperation, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisPatchCall.Do)
    *   [func (c *ProjectsLocationsApisPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisPatchCall.Fields)
    *   [func (c *ProjectsLocationsApisPatchCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisPatchCall.Header)
    *   [func (c *ProjectsLocationsApisPatchCall) UpdateMask(updateMask string) *ProjectsLocationsApisPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisPatchCall.UpdateMask)

*   [type ProjectsLocationsApisService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisService)
*       *   [func NewProjectsLocationsApisService(s *Service) *ProjectsLocationsApisService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#NewProjectsLocationsApisService)

*       *   [func (r *ProjectsLocationsApisService) Create(parent string, apigatewayapi *ApigatewayApi) *ProjectsLocationsApisCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisService.Create)
    *   [func (r *ProjectsLocationsApisService) Delete(name string) *ProjectsLocationsApisDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisService.Delete)
    *   [func (r *ProjectsLocationsApisService) Get(name string) *ProjectsLocationsApisGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisService.Get)
    *   [func (r *ProjectsLocationsApisService) GetIamPolicy(resource string) *ProjectsLocationsApisGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisService.GetIamPolicy)
    *   [func (r *ProjectsLocationsApisService) List(parent string) *ProjectsLocationsApisListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisService.List)
    *   [func (r *ProjectsLocationsApisService) Patch(name string, apigatewayapi *ApigatewayApi) *ProjectsLocationsApisPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisService.Patch)
    *   [func (r *ProjectsLocationsApisService) SetIamPolicy(resource string, apigatewaysetiampolicyrequest *ApigatewaySetIamPolicyRequest) *ProjectsLocationsApisSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisService.SetIamPolicy)
    *   [func (r *ProjectsLocationsApisService) TestIamPermissions(resource string, ...) *ProjectsLocationsApisTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisService.TestIamPermissions)

*   [type ProjectsLocationsApisSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisSetIamPolicyCall)
*       *   [func (c *ProjectsLocationsApisSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisSetIamPolicyCall.Context)
    *   [func (c *ProjectsLocationsApisSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*ApigatewayPolicy, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisSetIamPolicyCall.Do)
    *   [func (c *ProjectsLocationsApisSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisSetIamPolicyCall.Fields)
    *   [func (c *ProjectsLocationsApisSetIamPolicyCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisSetIamPolicyCall.Header)

*   [type ProjectsLocationsApisTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisTestIamPermissionsCall)
*       *   [func (c *ProjectsLocationsApisTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsApisTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisTestIamPermissionsCall.Context)
    *   [func (c *ProjectsLocationsApisTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*ApigatewayTestIamPermissionsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisTestIamPermissionsCall.Do)
    *   [func (c *ProjectsLocationsApisTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisTestIamPermissionsCall.Fields)
    *   [func (c *ProjectsLocationsApisTestIamPermissionsCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisTestIamPermissionsCall.Header)

*   [type ProjectsLocationsGatewaysCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysCreateCall)
*       *   [func (c *ProjectsLocationsGatewaysCreateCall) Context(ctx context.Context) *ProjectsLocationsGatewaysCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysCreateCall.Context)
    *   [func (c *ProjectsLocationsGatewaysCreateCall) Do(opts ...googleapi.CallOption) (*ApigatewayOperation, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysCreateCall.Do)
    *   [func (c *ProjectsLocationsGatewaysCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsGatewaysCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysCreateCall.Fields)
    *   [func (c *ProjectsLocationsGatewaysCreateCall) GatewayId(gatewayId string) *ProjectsLocationsGatewaysCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysCreateCall.GatewayId)
    *   [func (c *ProjectsLocationsGatewaysCreateCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysCreateCall.Header)

*   [type ProjectsLocationsGatewaysDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysDeleteCall)
*       *   [func (c *ProjectsLocationsGatewaysDeleteCall) Context(ctx context.Context) *ProjectsLocationsGatewaysDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysDeleteCall.Context)
    *   [func (c *ProjectsLocationsGatewaysDeleteCall) Do(opts ...googleapi.CallOption) (*ApigatewayOperation, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysDeleteCall.Do)
    *   [func (c *ProjectsLocationsGatewaysDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsGatewaysDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysDeleteCall.Fields)
    *   [func (c *ProjectsLocationsGatewaysDeleteCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysDeleteCall.Header)

*   [type ProjectsLocationsGatewaysGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysGetCall)
*       *   [func (c *ProjectsLocationsGatewaysGetCall) Context(ctx context.Context) *ProjectsLocationsGatewaysGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysGetCall.Context)
    *   [func (c *ProjectsLocationsGatewaysGetCall) Do(opts ...googleapi.CallOption) (*ApigatewayGateway, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysGetCall.Do)
    *   [func (c *ProjectsLocationsGatewaysGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsGatewaysGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysGetCall.Fields)
    *   [func (c *ProjectsLocationsGatewaysGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysGetCall.Header)
    *   [func (c *ProjectsLocationsGatewaysGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsGatewaysGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysGetCall.IfNoneMatch)

*   [type ProjectsLocationsGatewaysGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysGetIamPolicyCall)
*       *   [func (c *ProjectsLocationsGatewaysGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsGatewaysGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysGetIamPolicyCall.Context)
    *   [func (c *ProjectsLocationsGatewaysGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*ApigatewayPolicy, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysGetIamPolicyCall.Do)
    *   [func (c *ProjectsLocationsGatewaysGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsGatewaysGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysGetIamPolicyCall.Fields)
    *   [func (c *ProjectsLocationsGatewaysGetIamPolicyCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysGetIamPolicyCall.Header)
    *   [func (c *ProjectsLocationsGatewaysGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsGatewaysGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysGetIamPolicyCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsGatewaysGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsGatewaysGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysGetIamPolicyCall.OptionsRequestedPolicyVersion)

*   [type ProjectsLocationsGatewaysListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysListCall)
*       *   [func (c *ProjectsLocationsGatewaysListCall) Context(ctx context.Context) *ProjectsLocationsGatewaysListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysListCall.Context)
    *   [func (c *ProjectsLocationsGatewaysListCall) Do(opts ...googleapi.CallOption) (*ApigatewayListGatewaysResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysListCall.Do)
    *   [func (c *ProjectsLocationsGatewaysListCall) Fields(s ...googleapi.Field) *ProjectsLocationsGatewaysListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysListCall.Fields)
    *   [func (c *ProjectsLocationsGatewaysListCall) Filter(filter string) *ProjectsLocationsGatewaysListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysListCall.Filter)
    *   [func (c *ProjectsLocationsGatewaysListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysListCall.Header)
    *   [func (c *ProjectsLocationsGatewaysListCall) IfNoneMatch(entityTag string) *ProjectsLocationsGatewaysListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysListCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsGatewaysListCall) OrderBy(orderBy string) *ProjectsLocationsGatewaysListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysListCall.OrderBy)
    *   [func (c *ProjectsLocationsGatewaysListCall) PageSize(pageSize int64) *ProjectsLocationsGatewaysListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysListCall.PageSize)
    *   [func (c *ProjectsLocationsGatewaysListCall) PageToken(pageToken string) *ProjectsLocationsGatewaysListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysListCall.PageToken)
    *   [func (c *ProjectsLocationsGatewaysListCall) Pages(ctx context.Context, f func(*ApigatewayListGatewaysResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysListCall.Pages)

*   [type ProjectsLocationsGatewaysPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysPatchCall)
*       *   [func (c *ProjectsLocationsGatewaysPatchCall) Context(ctx context.Context) *ProjectsLocationsGatewaysPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysPatchCall.Context)
    *   [func (c *ProjectsLocationsGatewaysPatchCall) Do(opts ...googleapi.CallOption) (*ApigatewayOperation, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysPatchCall.Do)
    *   [func (c *ProjectsLocationsGatewaysPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsGatewaysPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysPatchCall.Fields)
    *   [func (c *ProjectsLocationsGatewaysPatchCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysPatchCall.Header)
    *   [func (c *ProjectsLocationsGatewaysPatchCall) UpdateMask(updateMask string) *ProjectsLocationsGatewaysPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysPatchCall.UpdateMask)

*   [type ProjectsLocationsGatewaysService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysService)
*       *   [func NewProjectsLocationsGatewaysService(s *Service) *ProjectsLocationsGatewaysService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#NewProjectsLocationsGatewaysService)

*       *   [func (r *ProjectsLocationsGatewaysService) Create(parent string, apigatewaygateway *ApigatewayGateway) *ProjectsLocationsGatewaysCreateCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysService.Create)
    *   [func (r *ProjectsLocationsGatewaysService) Delete(name string) *ProjectsLocationsGatewaysDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysService.Delete)
    *   [func (r *ProjectsLocationsGatewaysService) Get(name string) *ProjectsLocationsGatewaysGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysService.Get)
    *   [func (r *ProjectsLocationsGatewaysService) GetIamPolicy(resource string) *ProjectsLocationsGatewaysGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysService.GetIamPolicy)
    *   [func (r *ProjectsLocationsGatewaysService) List(parent string) *ProjectsLocationsGatewaysListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysService.List)
    *   [func (r *ProjectsLocationsGatewaysService) Patch(name string, apigatewaygateway *ApigatewayGateway) *ProjectsLocationsGatewaysPatchCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysService.Patch)
    *   [func (r *ProjectsLocationsGatewaysService) SetIamPolicy(resource string, apigatewaysetiampolicyrequest *ApigatewaySetIamPolicyRequest) *ProjectsLocationsGatewaysSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysService.SetIamPolicy)
    *   [func (r *ProjectsLocationsGatewaysService) TestIamPermissions(resource string, ...) *ProjectsLocationsGatewaysTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysService.TestIamPermissions)

*   [type ProjectsLocationsGatewaysSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysSetIamPolicyCall)
*       *   [func (c *ProjectsLocationsGatewaysSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsGatewaysSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysSetIamPolicyCall.Context)
    *   [func (c *ProjectsLocationsGatewaysSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*ApigatewayPolicy, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysSetIamPolicyCall.Do)
    *   [func (c *ProjectsLocationsGatewaysSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsGatewaysSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysSetIamPolicyCall.Fields)
    *   [func (c *ProjectsLocationsGatewaysSetIamPolicyCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysSetIamPolicyCall.Header)

*   [type ProjectsLocationsGatewaysTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysTestIamPermissionsCall)
*       *   [func (c *ProjectsLocationsGatewaysTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsGatewaysTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysTestIamPermissionsCall.Context)
    *   [func (c *ProjectsLocationsGatewaysTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*ApigatewayTestIamPermissionsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysTestIamPermissionsCall.Do)
    *   [func (c *ProjectsLocationsGatewaysTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsGatewaysTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysTestIamPermissionsCall.Fields)
    *   [func (c *ProjectsLocationsGatewaysTestIamPermissionsCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysTestIamPermissionsCall.Header)

*   [type ProjectsLocationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGetCall)
*       *   [func (c *ProjectsLocationsGetCall) Context(ctx context.Context) *ProjectsLocationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGetCall.Context)
    *   [func (c *ProjectsLocationsGetCall) Do(opts ...googleapi.CallOption) (*ApigatewayLocation, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGetCall.Do)
    *   [func (c *ProjectsLocationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGetCall.Fields)
    *   [func (c *ProjectsLocationsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGetCall.Header)
    *   [func (c *ProjectsLocationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGetCall.IfNoneMatch)

*   [type ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsListCall)
*       *   [func (c *ProjectsLocationsListCall) Context(ctx context.Context) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsListCall.Context)
    *   [func (c *ProjectsLocationsListCall) Do(opts ...googleapi.CallOption) (*ApigatewayListLocationsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsListCall.Do)
    *   [func (c *ProjectsLocationsListCall) ExtraLocationTypes(extraLocationTypes ...string) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsListCall.ExtraLocationTypes)
    *   [func (c *ProjectsLocationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsListCall.Fields)
    *   [func (c *ProjectsLocationsListCall) Filter(filter string) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsListCall.Filter)
    *   [func (c *ProjectsLocationsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsListCall.Header)
    *   [func (c *ProjectsLocationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsListCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsListCall) PageSize(pageSize int64) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsListCall.PageSize)
    *   [func (c *ProjectsLocationsListCall) PageToken(pageToken string) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsListCall.PageToken)
    *   [func (c *ProjectsLocationsListCall) Pages(ctx context.Context, f func(*ApigatewayListLocationsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsListCall.Pages)

*   [type ProjectsLocationsOperationsCancelCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsCancelCall)
*       *   [func (c *ProjectsLocationsOperationsCancelCall) Context(ctx context.Context) *ProjectsLocationsOperationsCancelCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsCancelCall.Context)
    *   [func (c *ProjectsLocationsOperationsCancelCall) Do(opts ...googleapi.CallOption) (*Empty, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsCancelCall.Do)
    *   [func (c *ProjectsLocationsOperationsCancelCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsCancelCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsCancelCall.Fields)
    *   [func (c *ProjectsLocationsOperationsCancelCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsCancelCall.Header)

*   [type ProjectsLocationsOperationsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsDeleteCall)
*       *   [func (c *ProjectsLocationsOperationsDeleteCall) Context(ctx context.Context) *ProjectsLocationsOperationsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsDeleteCall.Context)
    *   [func (c *ProjectsLocationsOperationsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsDeleteCall.Do)
    *   [func (c *ProjectsLocationsOperationsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsDeleteCall.Fields)
    *   [func (c *ProjectsLocationsOperationsDeleteCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsDeleteCall.Header)

*   [type ProjectsLocationsOperationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsGetCall)
*       *   [func (c *ProjectsLocationsOperationsGetCall) Context(ctx context.Context) *ProjectsLocationsOperationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsGetCall.Context)
    *   [func (c *ProjectsLocationsOperationsGetCall) Do(opts ...googleapi.CallOption) (*ApigatewayOperation, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsGetCall.Do)
    *   [func (c *ProjectsLocationsOperationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsGetCall.Fields)
    *   [func (c *ProjectsLocationsOperationsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsGetCall.Header)
    *   [func (c *ProjectsLocationsOperationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsOperationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsGetCall.IfNoneMatch)

*   [type ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsListCall)
*       *   [func (c *ProjectsLocationsOperationsListCall) Context(ctx context.Context) *ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsListCall.Context)
    *   [func (c *ProjectsLocationsOperationsListCall) Do(opts ...googleapi.CallOption) (*ApigatewayListOperationsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsListCall.Do)
    *   [func (c *ProjectsLocationsOperationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsListCall.Fields)
    *   [func (c *ProjectsLocationsOperationsListCall) Filter(filter string) *ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsListCall.Filter)
    *   [func (c *ProjectsLocationsOperationsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsListCall.Header)
    *   [func (c *ProjectsLocationsOperationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsListCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsOperationsListCall) PageSize(pageSize int64) *ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsListCall.PageSize)
    *   [func (c *ProjectsLocationsOperationsListCall) PageToken(pageToken string) *ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsListCall.PageToken)
    *   [func (c *ProjectsLocationsOperationsListCall) Pages(ctx context.Context, f func(*ApigatewayListOperationsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsListCall.Pages)
    *   [func (c *ProjectsLocationsOperationsListCall) ReturnPartialSuccess(returnPartialSuccess bool) *ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsListCall.ReturnPartialSuccess)

*   [type ProjectsLocationsOperationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsService)
*       *   [func NewProjectsLocationsOperationsService(s *Service) *ProjectsLocationsOperationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#NewProjectsLocationsOperationsService)

*       *   [func (r *ProjectsLocationsOperationsService) Cancel(name string, ...) *ProjectsLocationsOperationsCancelCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsService.Cancel)
    *   [func (r *ProjectsLocationsOperationsService) Delete(name string) *ProjectsLocationsOperationsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsService.Delete)
    *   [func (r *ProjectsLocationsOperationsService) Get(name string) *ProjectsLocationsOperationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsService.Get)
    *   [func (r *ProjectsLocationsOperationsService) List(name string) *ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsService.List)

*   [type ProjectsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsService)
*       *   [func NewProjectsLocationsService(s *Service) *ProjectsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#NewProjectsLocationsService)

*       *   [func (r *ProjectsLocationsService) Get(name string) *ProjectsLocationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsService.Get)
    *   [func (r *ProjectsLocationsService) List(name string) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsService.List)

*   [type ProjectsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsService)
*       *   [func NewProjectsService(s *Service) *ProjectsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#NewProjectsService)

*   [type Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#Service)
*       *   [func New(client *http.Client) (*Service, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#New)deprecated
    *   [func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#NewService)

[View Source](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/apigateway/v1/apigateway-gen.go#L100)

const (
	
	CloudPlatformScope = "https://www.googleapis.com/auth/cloud-platform"
)

OAuth2 scopes used by this API.

This section is empty.

This section is empty.

type ApigatewayApi struct {
	CreateTime [string](https://pkg.go.dev/builtin#string) `json:"createTime,omitempty"`
	DisplayName [string](https://pkg.go.dev/builtin#string) `json:"displayName,omitempty"`
	
	
	Labels map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `json:"labels,omitempty"`
	
	
	
	ManagedService [string](https://pkg.go.dev/builtin#string) `json:"managedService,omitempty"`
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	
	
	
	
	
	
	
	State [string](https://pkg.go.dev/builtin#string) `json:"state,omitempty"`
	UpdateTime [string](https://pkg.go.dev/builtin#string) `json:"updateTime,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ApigatewayApi: An API that can be served by one or more Gateways.

type ApigatewayApiConfig struct {
	CreateTime [string](https://pkg.go.dev/builtin#string) `json:"createTime,omitempty"`
	DisplayName [string](https://pkg.go.dev/builtin#string) `json:"displayName,omitempty"`
	
	
	
	
	
	
	GatewayServiceAccount [string](https://pkg.go.dev/builtin#string) `json:"gatewayServiceAccount,omitempty"`
	
	GrpcServices []*[ApigatewayApiConfigGrpcServiceDefinition](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayApiConfigGrpcServiceDefinition) `json:"grpcServices,omitempty"`
	
	
	Labels map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `json:"labels,omitempty"`
	
	
	
	
	
	
	
	ManagedServiceConfigs []*[ApigatewayApiConfigFile](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayApiConfigFile) `json:"managedServiceConfigs,omitempty"`
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	OpenapiDocuments []*[ApigatewayApiConfigOpenApiDocument](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayApiConfigOpenApiDocument) `json:"openapiDocuments,omitempty"`
	
	ServiceConfigId [string](https://pkg.go.dev/builtin#string) `json:"serviceConfigId,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	State [string](https://pkg.go.dev/builtin#string) `json:"state,omitempty"`
	UpdateTime [string](https://pkg.go.dev/builtin#string) `json:"updateTime,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ApigatewayApiConfig: An API Configuration is a combination of settings for both the Managed Service and Gateways serving this API Config.

type ApigatewayApiConfigFile struct {
	Contents [string](https://pkg.go.dev/builtin#string) `json:"contents,omitempty"`
	
	Path [string](https://pkg.go.dev/builtin#string) `json:"path,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ApigatewayApiConfigFile: A lightweight description of a file.

type ApigatewayApiConfigGrpcServiceDefinition struct {
	
	
	
	
	FileDescriptorSet *[ApigatewayApiConfigFile](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayApiConfigFile) `json:"fileDescriptorSet,omitempty"`
	
	
	
	Source []*[ApigatewayApiConfigFile](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayApiConfigFile) `json:"source,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ApigatewayApiConfigGrpcServiceDefinition: A gRPC service definition.

type ApigatewayApiConfigOpenApiDocument struct {
	Document *[ApigatewayApiConfigFile](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayApiConfigFile) `json:"document,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ApigatewayApiConfigOpenApiDocument: An OpenAPI Specification Document describing an API.

type ApigatewayAuditConfig struct {
	AuditLogConfigs []*[ApigatewayAuditLogConfig](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayAuditLogConfig) `json:"auditLogConfigs,omitempty"`
	
	
	Service [string](https://pkg.go.dev/builtin#string) `json:"service,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ApigatewayAuditConfig: Specifies the audit configuration for a service. The configuration determines which permission types are logged, and what identities, if any, are exempted from logging. An AuditConfig must have one or more AuditLogConfigs. If there are AuditConfigs for both `allServices` and a specific service, the union of the two AuditConfigs is used for that service: the log_types specified in each AuditConfig are enabled, and the exempted_members in each AuditLogConfig are exempted. Example Policy with multiple AuditConfigs: { "audit_configs": [ { "service": "allServices", "audit_log_configs": [ { "log_type": "DATA_READ", "exempted_members": [ "user:jose@example.com" ] }, { "log_type": "DATA_WRITE" }, { "log_type": "ADMIN_READ" } ] }, { "service": "sampleservice.googleapis.com", "audit_log_configs": [ { "log_type": "DATA_READ" }, { "log_type": "DATA_WRITE", "exempted_members": [ "user:aliya@example.com" ] } ] } ] } For sampleservice, this policy enables DATA_READ, DATA_WRITE and ADMIN_READ logging. It also exempts `jose@example.com` from DATA_READ logging, and `aliya@example.com` from DATA_WRITE logging.

type ApigatewayAuditLogConfig struct {
	
	ExemptedMembers [][string](https://pkg.go.dev/builtin#string) `json:"exemptedMembers,omitempty"`
	
	
	
	
	
	
	LogType [string](https://pkg.go.dev/builtin#string) `json:"logType,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ApigatewayAuditLogConfig: Provides the configuration for logging a type of permissions. Example: { "audit_log_configs": [ { "log_type": "DATA_READ", "exempted_members": [ "user:jose@example.com" ] }, { "log_type": "DATA_WRITE" } ] } This enables 'DATA_READ' and 'DATA_WRITE' logging, while exempting jose@example.com from DATA_READ logging.

type ApigatewayBinding struct {
	
	
	
	
	
	
	
	Condition *[ApigatewayExpr](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayExpr) `json:"condition,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	Members [][string](https://pkg.go.dev/builtin#string) `json:"members,omitempty"`
	
	
	
	
	
	Role [string](https://pkg.go.dev/builtin#string) `json:"role,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ApigatewayBinding: Associates `members`, or principals, with a `role`.

type ApigatewayCancelOperationRequest struct {
}

ApigatewayCancelOperationRequest: The request message for Operations.CancelOperation.

type ApigatewayExpr struct {
	
	Description [string](https://pkg.go.dev/builtin#string) `json:"description,omitempty"`
	
	Expression [string](https://pkg.go.dev/builtin#string) `json:"expression,omitempty"`
	
	Location [string](https://pkg.go.dev/builtin#string) `json:"location,omitempty"`
	
	
	Title [string](https://pkg.go.dev/builtin#string) `json:"title,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ApigatewayExpr: Represents a textual expression in the Common Expression Language (CEL) syntax. CEL is a C-like expression language. The syntax and semantics of CEL are documented at [https://github.com/google/cel-spec](https://github.com/google/cel-spec). Example (Comparison): title: "Summary size limit" description: "Determines if a summary is less than 100 chars" expression: "document.summary.size() < 100" Example (Equality): title: "Requestor is owner" description: "Determines if requestor is the document owner" expression: "document.owner == request.auth.claims.email" Example (Logic): title: "Public documents" description: "Determine whether the document should be publicly visible" expression: "document.type != 'private' && document.type != 'internal'" Example (Data Manipulation): title: "Notification string" description: "Create a notification string with a timestamp." expression: "'New message received at ' + string(document.create_time)" The exact variables and functions that may be referenced within an expression are determined by the service that evaluates it. See the service documentation for additional information.

type ApigatewayGateway struct {
	
	ApiConfig [string](https://pkg.go.dev/builtin#string) `json:"apiConfig,omitempty"`
	CreateTime [string](https://pkg.go.dev/builtin#string) `json:"createTime,omitempty"`
	
	DefaultHostname [string](https://pkg.go.dev/builtin#string) `json:"defaultHostname,omitempty"`
	DisplayName [string](https://pkg.go.dev/builtin#string) `json:"displayName,omitempty"`
	
	
	Labels map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) `json:"labels,omitempty"`
	
	Name [string](https://pkg.go.dev/builtin#string) `json:"name,omitempty"`
	
	
	
	
	
	
	
	
	State [string](https://pkg.go.dev/builtin#string) `json:"state,omitempty"`
	UpdateTime [string](https://pkg.go.dev/builtin#string) `json:"updateTime,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ApigatewayGateway: A Gateway is an API-aware HTTP proxy. It performs API-Method and/or API-Consumer specific actions based on an API Config such as authentication, policy enforcement, and backend selection.

type ApigatewayListApiConfigsResponse struct {
	ApiConfigs []*[ApigatewayApiConfig](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayApiConfig) `json:"apiConfigs,omitempty"`
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`
	UnreachableLocations [][string](https://pkg.go.dev/builtin#string) `json:"unreachableLocations,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ApigatewayListApiConfigsResponse: Response message for ApiGatewayService.ListApiConfigs

type ApigatewayListApisResponse struct {
	Apis []*[ApigatewayApi](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayApi) `json:"apis,omitempty"`
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`
	UnreachableLocations [][string](https://pkg.go.dev/builtin#string) `json:"unreachableLocations,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ApigatewayListApisResponse: Response message for ApiGatewayService.ListApis

type ApigatewayListGatewaysResponse struct {
	Gateways []*[ApigatewayGateway](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayGateway) `json:"gateways,omitempty"`
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`
	UnreachableLocations [][string](https://pkg.go.dev/builtin#string) `json:"unreachableLocations,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ApigatewayListGatewaysResponse: Response message for ApiGatewayService.ListGateways

type ApigatewayListLocationsResponse struct {
	
	Locations []*[ApigatewayLocation](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayLocation) `json:"locations,omitempty"`
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ApigatewayListLocationsResponse: The response message for Locations.ListLocations.

type ApigatewayListOperationsResponse struct {
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`
	
	Operations []*[ApigatewayOperation](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayOperation) `json:"operations,omitempty"`
	
	
	
	Unreachable [][string](https://pkg.go.dev/builtin#string) `json:"unreachable,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ApigatewayListOperationsResponse: The response message for Operations.ListOperations.

ApigatewayLocation: A resource that represents a Google Cloud location.

ApigatewayOperation: This resource represents a long-running operation that is the result of a network API call.

type ApigatewayOperationMetadata struct {
	ApiVersion [string](https://pkg.go.dev/builtin#string) `json:"apiVersion,omitempty"`
	CreateTime [string](https://pkg.go.dev/builtin#string) `json:"createTime,omitempty"`
	
	Diagnostics []*[ApigatewayOperationMetadataDiagnostic](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayOperationMetadataDiagnostic) `json:"diagnostics,omitempty"`
	EndTime [string](https://pkg.go.dev/builtin#string) `json:"endTime,omitempty"`
	
	
	
	RequestedCancellation [bool](https://pkg.go.dev/builtin#bool) `json:"requestedCancellation,omitempty"`
	StatusMessage [string](https://pkg.go.dev/builtin#string) `json:"statusMessage,omitempty"`
	
	Target [string](https://pkg.go.dev/builtin#string) `json:"target,omitempty"`
	Verb [string](https://pkg.go.dev/builtin#string) `json:"verb,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ApigatewayOperationMetadata: Represents the metadata of the long-running operation.

type ApigatewayOperationMetadataDiagnostic struct {
	Location [string](https://pkg.go.dev/builtin#string) `json:"location,omitempty"`
	Message [string](https://pkg.go.dev/builtin#string) `json:"message,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ApigatewayOperationMetadataDiagnostic: Diagnostic information from configuration processing.

type ApigatewayPolicy struct {
	AuditConfigs []*[ApigatewayAuditConfig](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayAuditConfig) `json:"auditConfigs,omitempty"`
	
	
	
	
	
	
	
	
	Bindings []*[ApigatewayBinding](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayBinding) `json:"bindings,omitempty"`
	
	
	
	
	
	
	
	
	
	
	Etag [string](https://pkg.go.dev/builtin#string) `json:"etag,omitempty"`
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	Version [int64](https://pkg.go.dev/builtin#int64) `json:"version,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ApigatewayPolicy: An Identity and Access Management (IAM) policy, which specifies access controls for Google Cloud resources. A `Policy` is a collection of `bindings`. A `binding` binds one or more `members`, or principals, to a single `role`. Principals can be user accounts, service accounts, Google groups, and domains (such as G Suite). A `role` is a named list of permissions; each `role` can be an IAM predefined role or a user-created custom role. For some types of Google Cloud resources, a `binding` can also specify a `condition`, which is a logical expression that allows access to a resource only if the expression evaluates to `true`. A condition can add constraints based on attributes of the request, the resource, or both. To learn which resources support conditions in their IAM policies, see the IAM documentation ([https://cloud.google.com/iam/help/conditions/resource-policies](https://cloud.google.com/iam/help/conditions/resource-policies)). **JSON example:** ``` { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": [ "user:eve@example.com" ], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01T00:00:00.000Z')", } } ], "etag": "BwWWja0YfJA=", "version": 3 } ``` **YAML example:** ``` bindings: - members: - user:mike@example.com - group:admins@example.com - domain:google.com - serviceAccount:my-project-id@appspot.gserviceaccount.com role: roles/resourcemanager.organizationAdmin - members: - user:eve@example.com role: roles/resourcemanager.organizationViewer condition: title: expirable access description: Does not grant access after Sep 2020 expression: request.time < timestamp('2020-10-01T00:00:00.000Z') etag: BwWWja0YfJA= version: 3 ``` For a description of IAM and its features, see the IAM documentation ([https://cloud.google.com/iam/docs/](https://cloud.google.com/iam/docs/)).

type ApigatewaySetIamPolicyRequest struct {
	
	
	
	Policy *[ApigatewayPolicy](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayPolicy) `json:"policy,omitempty"`
	
	
	UpdateMask [string](https://pkg.go.dev/builtin#string) `json:"updateMask,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ApigatewaySetIamPolicyRequest: Request message for `SetIamPolicy` method.

type ApigatewayStatus struct {
	Code [int64](https://pkg.go.dev/builtin#int64) `json:"code,omitempty"`
	
	Details [][googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[RawMessage](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#RawMessage) `json:"details,omitempty"`
	
	
	Message [string](https://pkg.go.dev/builtin#string) `json:"message,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ApigatewayStatus: The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by gRPC ([https://github.com/grpc](https://github.com/grpc)). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the API Design Guide ([https://cloud.google.com/apis/design/errors](https://cloud.google.com/apis/design/errors)).

type ApigatewayTestIamPermissionsRequest struct {
	
	
	
	Permissions [][string](https://pkg.go.dev/builtin#string) `json:"permissions,omitempty"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ApigatewayTestIamPermissionsRequest: Request message for `TestIamPermissions` method.

type ApigatewayTestIamPermissionsResponse struct {
	
	Permissions [][string](https://pkg.go.dev/builtin#string) `json:"permissions,omitempty"`

	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ApigatewayTestIamPermissionsResponse: Response message for `TestIamPermissions` method.

Empty: A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }

type ProjectsLocationsApisConfigsCreateCall struct {
	
}

ApiConfigId sets the optional parameter "apiConfigId": Required. Identifier to assign to the API Config. Must be unique within scope of the parent resource.

Context sets the context to be used in this call's Do method.

Do executes the "apigateway.projects.locations.apis.configs.create" call. Any non-2xx status code is an error. Response headers are in either *ApigatewayOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisConfigsDeleteCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apigateway.projects.locations.apis.configs.delete" call. Any non-2xx status code is an error. Response headers are in either *ApigatewayOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisConfigsGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apigateway.projects.locations.apis.configs.get" call. Any non-2xx status code is an error. Response headers are in either *ApigatewayApiConfig.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

View sets the optional parameter "view": Specifies which fields of the API Config are returned in the response. Defaults to `BASIC` view.

Possible values:

"CONFIG_VIEW_UNSPECIFIED"
"BASIC" - Do not include configuration source files.
"FULL" - Include configuration source files.

type ProjectsLocationsApisConfigsGetIamPolicyCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apigateway.projects.locations.apis.configs.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *ApigatewayPolicy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (c *[ProjectsLocationsApisConfigsGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsGetIamPolicyCall)) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion [int64](https://pkg.go.dev/builtin#int64)) *[ProjectsLocationsApisConfigsGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsGetIamPolicyCall)

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the IAM documentation ([https://cloud.google.com/iam/help/conditions/resource-policies](https://cloud.google.com/iam/help/conditions/resource-policies)).

type ProjectsLocationsApisConfigsListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apigateway.projects.locations.apis.configs.list" call. Any non-2xx status code is an error. Response headers are in either *ApigatewayListApiConfigsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Filter sets the optional parameter "filter": Filter.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

OrderBy sets the optional parameter "orderBy": Order by parameters.

PageSize sets the optional parameter "pageSize": Page size.

PageToken sets the optional parameter "pageToken": Page token.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsApisConfigsPatchCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apigateway.projects.locations.apis.configs.patch" call. Any non-2xx status code is an error. Response headers are in either *ApigatewayOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

UpdateMask sets the optional parameter "updateMask": Field mask is used to specify the fields to be overwritten in the ApiConfig resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.

type ProjectsLocationsApisConfigsService struct {
	
}

func NewProjectsLocationsApisConfigsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#Service)) *[ProjectsLocationsApisConfigsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsService)

Create: Creates a new ApiConfig in a given project and location.

*   parent: Parent resource of the API Config, of the form: `projects/*/locations/global/apis/*`.

Delete: Deletes a single ApiConfig.

*   name: Resource name of the form: `projects/*/locations/global/apis/*/configs/*`.

Get: Gets details of a single ApiConfig.

*   name: Resource name of the form: `projects/*/locations/global/apis/*/configs/*`.

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

*   resource: REQUIRED: The resource for which the policy is being requested. See Resource names ([https://cloud.google.com/apis/design/resource_names](https://cloud.google.com/apis/design/resource_names)) for the appropriate value for this field.

List: Lists ApiConfigs in a given project and location.

*   parent: Parent resource of the API Config, of the form: `projects/*/locations/global/apis/*`.

Patch: Updates the parameters of a single ApiConfig.

*   name: Output only. Resource name of the API Config. Format: projects/{project}/locations/global/apis/{api}/configs/{api_config}.

SetIamPolicy: Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

*   resource: REQUIRED: The resource for which the policy is being specified. See Resource names ([https://cloud.google.com/apis/design/resource_names](https://cloud.google.com/apis/design/resource_names)) for the appropriate value for this field.

TestIamPermissions: Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

*   resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names ([https://cloud.google.com/apis/design/resource_names](https://cloud.google.com/apis/design/resource_names)) for the appropriate value for this field.

type ProjectsLocationsApisConfigsSetIamPolicyCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apigateway.projects.locations.apis.configs.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *ApigatewayPolicy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisConfigsTestIamPermissionsCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apigateway.projects.locations.apis.configs.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *ApigatewayTestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisCreateCall struct {
	
}

ApiId sets the optional parameter "apiId": Required. Identifier to assign to the API. Must be unique within scope of the parent resource.

Context sets the context to be used in this call's Do method.

Do executes the "apigateway.projects.locations.apis.create" call. Any non-2xx status code is an error. Response headers are in either *ApigatewayOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisDeleteCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apigateway.projects.locations.apis.delete" call. Any non-2xx status code is an error. Response headers are in either *ApigatewayOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apigateway.projects.locations.apis.get" call. Any non-2xx status code is an error. Response headers are in either *ApigatewayApi.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsApisGetIamPolicyCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apigateway.projects.locations.apis.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *ApigatewayPolicy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (c *[ProjectsLocationsApisGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisGetIamPolicyCall)) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion [int64](https://pkg.go.dev/builtin#int64)) *[ProjectsLocationsApisGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisGetIamPolicyCall)

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the IAM documentation ([https://cloud.google.com/iam/help/conditions/resource-policies](https://cloud.google.com/iam/help/conditions/resource-policies)).

type ProjectsLocationsApisListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apigateway.projects.locations.apis.list" call. Any non-2xx status code is an error. Response headers are in either *ApigatewayListApisResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Filter sets the optional parameter "filter": Filter.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

OrderBy sets the optional parameter "orderBy": Order by parameters.

PageSize sets the optional parameter "pageSize": Page size.

PageToken sets the optional parameter "pageToken": Page token.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsApisPatchCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apigateway.projects.locations.apis.patch" call. Any non-2xx status code is an error. Response headers are in either *ApigatewayOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

UpdateMask sets the optional parameter "updateMask": Field mask is used to specify the fields to be overwritten in the Api resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.

type ProjectsLocationsApisService struct {
 Configs *[ProjectsLocationsApisConfigsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisConfigsService)	
}

func NewProjectsLocationsApisService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#Service)) *[ProjectsLocationsApisService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisService)

Create: Creates a new Api in a given project and location.

*   parent: Parent resource of the API, of the form: `projects/*/locations/global`.

Delete: Deletes a single Api.

- name: Resource name of the form: `projects/*/locations/global/apis/*`.

Get: Gets details of a single Api.

- name: Resource name of the form: `projects/*/locations/global/apis/*`.

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

*   resource: REQUIRED: The resource for which the policy is being requested. See Resource names ([https://cloud.google.com/apis/design/resource_names](https://cloud.google.com/apis/design/resource_names)) for the appropriate value for this field.

List: Lists Apis in a given project and location.

*   parent: Parent resource of the API, of the form: `projects/*/locations/global`.

Patch: Updates the parameters of a single Api.

*   name: Output only. Resource name of the API. Format: projects/{project}/locations/global/apis/{api}.

SetIamPolicy: Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

*   resource: REQUIRED: The resource for which the policy is being specified. See Resource names ([https://cloud.google.com/apis/design/resource_names](https://cloud.google.com/apis/design/resource_names)) for the appropriate value for this field.

func (r *[ProjectsLocationsApisService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisService)) TestIamPermissions(resource [string](https://pkg.go.dev/builtin#string), apigatewaytestiampermissionsrequest *[ApigatewayTestIamPermissionsRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayTestIamPermissionsRequest)) *[ProjectsLocationsApisTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisTestIamPermissionsCall)

TestIamPermissions: Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

*   resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names ([https://cloud.google.com/apis/design/resource_names](https://cloud.google.com/apis/design/resource_names)) for the appropriate value for this field.

type ProjectsLocationsApisSetIamPolicyCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apigateway.projects.locations.apis.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *ApigatewayPolicy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsApisTestIamPermissionsCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apigateway.projects.locations.apis.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *ApigatewayTestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsGatewaysCreateCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apigateway.projects.locations.gateways.create" call. Any non-2xx status code is an error. Response headers are in either *ApigatewayOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

GatewayId sets the optional parameter "gatewayId": Required. Identifier to assign to the Gateway. Must be unique within scope of the parent resource.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsGatewaysDeleteCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apigateway.projects.locations.gateways.delete" call. Any non-2xx status code is an error. Response headers are in either *ApigatewayOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsGatewaysGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apigateway.projects.locations.gateways.get" call. Any non-2xx status code is an error. Response headers are in either *ApigatewayGateway.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsGatewaysGetIamPolicyCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apigateway.projects.locations.gateways.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *ApigatewayPolicy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (c *[ProjectsLocationsGatewaysGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysGetIamPolicyCall)) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion [int64](https://pkg.go.dev/builtin#int64)) *[ProjectsLocationsGatewaysGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysGetIamPolicyCall)

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the IAM documentation ([https://cloud.google.com/iam/help/conditions/resource-policies](https://cloud.google.com/iam/help/conditions/resource-policies)).

type ProjectsLocationsGatewaysListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apigateway.projects.locations.gateways.list" call. Any non-2xx status code is an error. Response headers are in either *ApigatewayListGatewaysResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Filter sets the optional parameter "filter": Filter.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

OrderBy sets the optional parameter "orderBy": Order by parameters.

PageSize sets the optional parameter "pageSize": Page size.

PageToken sets the optional parameter "pageToken": Page token.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsGatewaysPatchCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apigateway.projects.locations.gateways.patch" call. Any non-2xx status code is an error. Response headers are in either *ApigatewayOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

UpdateMask sets the optional parameter "updateMask": Field mask is used to specify the fields to be overwritten in the Gateway resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.

type ProjectsLocationsGatewaysService struct {
	
}

func NewProjectsLocationsGatewaysService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#Service)) *[ProjectsLocationsGatewaysService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysService)

Create: Creates a new Gateway in a given project and location.

*   parent: Parent resource of the Gateway, of the form: `projects/*/locations/*`.

Delete: Deletes a single Gateway.

- name: Resource name of the form: `projects/*/locations/*/gateways/*`.

Get: Gets details of a single Gateway.

- name: Resource name of the form: `projects/*/locations/*/gateways/*`.

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

*   resource: REQUIRED: The resource for which the policy is being requested. See Resource names ([https://cloud.google.com/apis/design/resource_names](https://cloud.google.com/apis/design/resource_names)) for the appropriate value for this field.

List: Lists Gateways in a given project and location.

*   parent: Parent resource of the Gateway, of the form: `projects/*/locations/*`.

Patch: Updates the parameters of a single Gateway.

*   name: Output only. Resource name of the Gateway. Format: projects/{project}/locations/{location}/gateways/{gateway}.

SetIamPolicy: Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

*   resource: REQUIRED: The resource for which the policy is being specified. See Resource names ([https://cloud.google.com/apis/design/resource_names](https://cloud.google.com/apis/design/resource_names)) for the appropriate value for this field.

func (r *[ProjectsLocationsGatewaysService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysService)) TestIamPermissions(resource [string](https://pkg.go.dev/builtin#string), apigatewaytestiampermissionsrequest *[ApigatewayTestIamPermissionsRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ApigatewayTestIamPermissionsRequest)) *[ProjectsLocationsGatewaysTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysTestIamPermissionsCall)

TestIamPermissions: Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

*   resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names ([https://cloud.google.com/apis/design/resource_names](https://cloud.google.com/apis/design/resource_names)) for the appropriate value for this field.

type ProjectsLocationsGatewaysSetIamPolicyCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apigateway.projects.locations.gateways.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *ApigatewayPolicy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsGatewaysTestIamPermissionsCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apigateway.projects.locations.gateways.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *ApigatewayTestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apigateway.projects.locations.get" call. Any non-2xx status code is an error. Response headers are in either *ApigatewayLocation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apigateway.projects.locations.list" call. Any non-2xx status code is an error. Response headers are in either *ApigatewayListLocationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (c *[ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsListCall)) ExtraLocationTypes(extraLocationTypes ...[string](https://pkg.go.dev/builtin#string)) *[ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsListCall)

ExtraLocationTypes sets the optional parameter "extraLocationTypes": Do not use this field. It is unsupported and is ignored unless explicitly documented otherwise. This is primarily for internal usage.

Filter sets the optional parameter "filter": A filter to narrow down results to a preferred subset. The filtering language accepts strings like "displayName=tokyo", and is documented in more detail in AIP-160 ([https://google.aip.dev/160](https://google.aip.dev/160)).

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": The maximum number of results to return. If not set, the service selects a default.

PageToken sets the optional parameter "pageToken": A page token received from the `next_page_token` field in the response. Send that page token to receive the subsequent page.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsOperationsCancelCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apigateway.projects.locations.operations.cancel" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsOperationsDeleteCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apigateway.projects.locations.operations.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsOperationsGetCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apigateway.projects.locations.operations.get" call. Any non-2xx status code is an error. Response headers are in either *ApigatewayOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsOperationsListCall struct {
	
}

Context sets the context to be used in this call's Do method.

Do executes the "apigateway.projects.locations.operations.list" call. Any non-2xx status code is an error. Response headers are in either *ApigatewayListOperationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Filter sets the optional parameter "filter": The standard list filter.

Header returns a http.Header that can be modified by the caller to add headers to the request.

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

PageSize sets the optional parameter "pageSize": The standard list page size.

PageToken sets the optional parameter "pageToken": The standard list page token.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (c *[ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsListCall)) ReturnPartialSuccess(returnPartialSuccess [bool](https://pkg.go.dev/builtin#bool)) *[ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsListCall)

ReturnPartialSuccess sets the optional parameter "returnPartialSuccess": When set to `true`, operations that are reachable are returned as normal, and those that are unreachable are returned in the ListOperationsResponse.unreachable field. This can only be `true` when reading across collections. For example, when `parent` is set to "projects/example/locations/-". This field is not supported by default and will result in an `UNIMPLEMENTED` error if set unless explicitly documented otherwise in service or product specific documentation.

type ProjectsLocationsOperationsService struct {
	
}

func NewProjectsLocationsOperationsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#Service)) *[ProjectsLocationsOperationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsService)

Cancel: Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of `1`, corresponding to `Code.CANCELLED`.

- name: The name of the operation resource to be cancelled.

Delete: Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

- name: The name of the operation resource to be deleted.

Get: Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

- name: The name of the operation resource.

List: Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.

- name: The name of the operation's parent resource.

type ProjectsLocationsService struct {
 Apis *[ProjectsLocationsApisService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsApisService)
 Gateways *[ProjectsLocationsGatewaysService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsGatewaysService)
 Operations *[ProjectsLocationsOperationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsOperationsService)	
}

func NewProjectsLocationsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#Service)) *[ProjectsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsService)

Get: Gets information about a location.

- name: Resource name for the location.

List: Lists information about the supported locations for this service. This method can be called in two ways: * **List all public locations:** Use the path `GET /v1/locations`. * **List project-visible locations:** Use the path `GET /v1/projects/{project_id}/locations`. This may include public locations as well as private or other locations specifically visible to the project.

- name: The resource that owns the locations collection, if applicable.

type ProjectsService struct {
 Locations *[ProjectsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsLocationsService)	
}

func NewProjectsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#Service)) *[ProjectsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1#ProjectsService)

New creates a new Service. It uses the provided http.Client for requests.

Deprecated: please use NewService instead. To provide a custom HTTP client, use option.WithHTTPClient. If you are using google.golang.org/api/googleapis/transport.APIKey, use option.WithAPIKey with NewService instead.

NewService creates a new Service.
