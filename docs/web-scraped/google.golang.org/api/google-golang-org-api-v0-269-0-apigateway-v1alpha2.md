# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2

Title: apigateway package - google.golang.org/api/apigateway/v1alpha2 - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2

Markdown Content:
Package apigateway provides access to the API Gateway API.

For product documentation, see: [https://cloud.google.com/api-gateway/docs](https://cloud.google.com/api-gateway/docs)

#### Creating a client [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#hdr-Creating_a_client "Go to Creating a client")

Usage example:

import "google.golang.org/api/apigateway/v1alpha2"
...
ctx := context.Background()
apigatewayService, err := apigateway.NewService(ctx)

In this example, Google Application Default Credentials are used for authentication.

For information on how to create and obtain Application Default Credentials, see [https://developers.google.com/identity/protocols/application-default-credentials](https://developers.google.com/identity/protocols/application-default-credentials).

#### Other authentication options [¶](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#hdr-Other_authentication_options "Go to Other authentication options")

To use an API key for authentication (note: some APIs do not support API keys), use option.WithAPIKey:

apigatewayService, err := apigateway.NewService(ctx, option.WithAPIKey("AIza..."))

To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow), use option.WithTokenSource:

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
apigatewayService, err := apigateway.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))

See [https://godoc.org/google.golang.org/api/option/](https://godoc.org/google.golang.org/api/option/) for details on options.

*   [Constants](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#pkg-constants)
*   [type ApigatewayAuditConfig](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayAuditConfig)
*       *   [func (s *ApigatewayAuditConfig) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayAuditConfig.MarshalJSON)

*   [type ApigatewayAuditLogConfig](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayAuditLogConfig)
*       *   [func (s *ApigatewayAuditLogConfig) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayAuditLogConfig.MarshalJSON)

*   [type ApigatewayBinding](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayBinding)
*       *   [func (s *ApigatewayBinding) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayBinding.MarshalJSON)

*   [type ApigatewayCancelOperationRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayCancelOperationRequest)
*   [type ApigatewayExpr](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayExpr)
*       *   [func (s *ApigatewayExpr) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayExpr.MarshalJSON)

*   [type ApigatewayListLocationsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayListLocationsResponse)
*       *   [func (s *ApigatewayListLocationsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayListLocationsResponse.MarshalJSON)

*   [type ApigatewayListOperationsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayListOperationsResponse)
*       *   [func (s *ApigatewayListOperationsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayListOperationsResponse.MarshalJSON)

*   [type ApigatewayLocation](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayLocation)
*       *   [func (s *ApigatewayLocation) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayLocation.MarshalJSON)

*   [type ApigatewayOperation](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayOperation)
*       *   [func (s *ApigatewayOperation) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayOperation.MarshalJSON)

*   [type ApigatewayPolicy](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayPolicy)
*       *   [func (s *ApigatewayPolicy) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayPolicy.MarshalJSON)

*   [type ApigatewaySetIamPolicyRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewaySetIamPolicyRequest)
*       *   [func (s *ApigatewaySetIamPolicyRequest) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewaySetIamPolicyRequest.MarshalJSON)

*   [type ApigatewayStatus](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayStatus)
*       *   [func (s *ApigatewayStatus) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayStatus.MarshalJSON)

*   [type ApigatewayTestIamPermissionsRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayTestIamPermissionsRequest)
*       *   [func (s *ApigatewayTestIamPermissionsRequest) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayTestIamPermissionsRequest.MarshalJSON)

*   [type ApigatewayTestIamPermissionsResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayTestIamPermissionsResponse)
*       *   [func (s *ApigatewayTestIamPermissionsResponse) MarshalJSON() ([]byte, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayTestIamPermissionsResponse.MarshalJSON)

*   [type Empty](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#Empty)
*   [type ProjectsLocationsApisConfigsGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisConfigsGetIamPolicyCall)
*       *   [func (c *ProjectsLocationsApisConfigsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisConfigsGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisConfigsGetIamPolicyCall.Context)
    *   [func (c *ProjectsLocationsApisConfigsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*ApigatewayPolicy, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisConfigsGetIamPolicyCall.Do)
    *   [func (c *ProjectsLocationsApisConfigsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisConfigsGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisConfigsGetIamPolicyCall.Fields)
    *   [func (c *ProjectsLocationsApisConfigsGetIamPolicyCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisConfigsGetIamPolicyCall.Header)
    *   [func (c *ProjectsLocationsApisConfigsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisConfigsGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisConfigsGetIamPolicyCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsApisConfigsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsApisConfigsGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisConfigsGetIamPolicyCall.OptionsRequestedPolicyVersion)

*   [type ProjectsLocationsApisConfigsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisConfigsService)
*       *   [func NewProjectsLocationsApisConfigsService(s *Service) *ProjectsLocationsApisConfigsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#NewProjectsLocationsApisConfigsService)

*       *   [func (r *ProjectsLocationsApisConfigsService) GetIamPolicy(resource string) *ProjectsLocationsApisConfigsGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisConfigsService.GetIamPolicy)
    *   [func (r *ProjectsLocationsApisConfigsService) SetIamPolicy(resource string, apigatewaysetiampolicyrequest *ApigatewaySetIamPolicyRequest) *ProjectsLocationsApisConfigsSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisConfigsService.SetIamPolicy)
    *   [func (r *ProjectsLocationsApisConfigsService) TestIamPermissions(resource string, ...) *ProjectsLocationsApisConfigsTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisConfigsService.TestIamPermissions)

*   [type ProjectsLocationsApisConfigsSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisConfigsSetIamPolicyCall)
*       *   [func (c *ProjectsLocationsApisConfigsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisConfigsSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisConfigsSetIamPolicyCall.Context)
    *   [func (c *ProjectsLocationsApisConfigsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*ApigatewayPolicy, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisConfigsSetIamPolicyCall.Do)
    *   [func (c *ProjectsLocationsApisConfigsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisConfigsSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisConfigsSetIamPolicyCall.Fields)
    *   [func (c *ProjectsLocationsApisConfigsSetIamPolicyCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisConfigsSetIamPolicyCall.Header)

*   [type ProjectsLocationsApisConfigsTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisConfigsTestIamPermissionsCall)
*       *   [func (c *ProjectsLocationsApisConfigsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsApisConfigsTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisConfigsTestIamPermissionsCall.Context)
    *   [func (c *ProjectsLocationsApisConfigsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*ApigatewayTestIamPermissionsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisConfigsTestIamPermissionsCall.Do)
    *   [func (c *ProjectsLocationsApisConfigsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisConfigsTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisConfigsTestIamPermissionsCall.Fields)
    *   [func (c *ProjectsLocationsApisConfigsTestIamPermissionsCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisConfigsTestIamPermissionsCall.Header)

*   [type ProjectsLocationsApisGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisGetIamPolicyCall)
*       *   [func (c *ProjectsLocationsApisGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisGetIamPolicyCall.Context)
    *   [func (c *ProjectsLocationsApisGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*ApigatewayPolicy, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisGetIamPolicyCall.Do)
    *   [func (c *ProjectsLocationsApisGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisGetIamPolicyCall.Fields)
    *   [func (c *ProjectsLocationsApisGetIamPolicyCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisGetIamPolicyCall.Header)
    *   [func (c *ProjectsLocationsApisGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsApisGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisGetIamPolicyCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsApisGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsApisGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisGetIamPolicyCall.OptionsRequestedPolicyVersion)

*   [type ProjectsLocationsApisService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisService)
*       *   [func NewProjectsLocationsApisService(s *Service) *ProjectsLocationsApisService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#NewProjectsLocationsApisService)

*       *   [func (r *ProjectsLocationsApisService) GetIamPolicy(resource string) *ProjectsLocationsApisGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisService.GetIamPolicy)
    *   [func (r *ProjectsLocationsApisService) SetIamPolicy(resource string, apigatewaysetiampolicyrequest *ApigatewaySetIamPolicyRequest) *ProjectsLocationsApisSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisService.SetIamPolicy)
    *   [func (r *ProjectsLocationsApisService) TestIamPermissions(resource string, ...) *ProjectsLocationsApisTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisService.TestIamPermissions)

*   [type ProjectsLocationsApisSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisSetIamPolicyCall)
*       *   [func (c *ProjectsLocationsApisSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsApisSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisSetIamPolicyCall.Context)
    *   [func (c *ProjectsLocationsApisSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*ApigatewayPolicy, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisSetIamPolicyCall.Do)
    *   [func (c *ProjectsLocationsApisSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisSetIamPolicyCall.Fields)
    *   [func (c *ProjectsLocationsApisSetIamPolicyCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisSetIamPolicyCall.Header)

*   [type ProjectsLocationsApisTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisTestIamPermissionsCall)
*       *   [func (c *ProjectsLocationsApisTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsApisTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisTestIamPermissionsCall.Context)
    *   [func (c *ProjectsLocationsApisTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*ApigatewayTestIamPermissionsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisTestIamPermissionsCall.Do)
    *   [func (c *ProjectsLocationsApisTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsApisTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisTestIamPermissionsCall.Fields)
    *   [func (c *ProjectsLocationsApisTestIamPermissionsCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisTestIamPermissionsCall.Header)

*   [type ProjectsLocationsGatewaysGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGatewaysGetIamPolicyCall)
*       *   [func (c *ProjectsLocationsGatewaysGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsGatewaysGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGatewaysGetIamPolicyCall.Context)
    *   [func (c *ProjectsLocationsGatewaysGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*ApigatewayPolicy, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGatewaysGetIamPolicyCall.Do)
    *   [func (c *ProjectsLocationsGatewaysGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsGatewaysGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGatewaysGetIamPolicyCall.Fields)
    *   [func (c *ProjectsLocationsGatewaysGetIamPolicyCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGatewaysGetIamPolicyCall.Header)
    *   [func (c *ProjectsLocationsGatewaysGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsGatewaysGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGatewaysGetIamPolicyCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsGatewaysGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsGatewaysGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGatewaysGetIamPolicyCall.OptionsRequestedPolicyVersion)

*   [type ProjectsLocationsGatewaysService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGatewaysService)
*       *   [func NewProjectsLocationsGatewaysService(s *Service) *ProjectsLocationsGatewaysService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#NewProjectsLocationsGatewaysService)

*       *   [func (r *ProjectsLocationsGatewaysService) GetIamPolicy(resource string) *ProjectsLocationsGatewaysGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGatewaysService.GetIamPolicy)
    *   [func (r *ProjectsLocationsGatewaysService) SetIamPolicy(resource string, apigatewaysetiampolicyrequest *ApigatewaySetIamPolicyRequest) *ProjectsLocationsGatewaysSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGatewaysService.SetIamPolicy)
    *   [func (r *ProjectsLocationsGatewaysService) TestIamPermissions(resource string, ...) *ProjectsLocationsGatewaysTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGatewaysService.TestIamPermissions)

*   [type ProjectsLocationsGatewaysSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGatewaysSetIamPolicyCall)
*       *   [func (c *ProjectsLocationsGatewaysSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsGatewaysSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGatewaysSetIamPolicyCall.Context)
    *   [func (c *ProjectsLocationsGatewaysSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*ApigatewayPolicy, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGatewaysSetIamPolicyCall.Do)
    *   [func (c *ProjectsLocationsGatewaysSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsGatewaysSetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGatewaysSetIamPolicyCall.Fields)
    *   [func (c *ProjectsLocationsGatewaysSetIamPolicyCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGatewaysSetIamPolicyCall.Header)

*   [type ProjectsLocationsGatewaysTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGatewaysTestIamPermissionsCall)
*       *   [func (c *ProjectsLocationsGatewaysTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsGatewaysTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGatewaysTestIamPermissionsCall.Context)
    *   [func (c *ProjectsLocationsGatewaysTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*ApigatewayTestIamPermissionsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGatewaysTestIamPermissionsCall.Do)
    *   [func (c *ProjectsLocationsGatewaysTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsGatewaysTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGatewaysTestIamPermissionsCall.Fields)
    *   [func (c *ProjectsLocationsGatewaysTestIamPermissionsCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGatewaysTestIamPermissionsCall.Header)

*   [type ProjectsLocationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGetCall)
*       *   [func (c *ProjectsLocationsGetCall) Context(ctx context.Context) *ProjectsLocationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGetCall.Context)
    *   [func (c *ProjectsLocationsGetCall) Do(opts ...googleapi.CallOption) (*ApigatewayLocation, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGetCall.Do)
    *   [func (c *ProjectsLocationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGetCall.Fields)
    *   [func (c *ProjectsLocationsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGetCall.Header)
    *   [func (c *ProjectsLocationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGetCall.IfNoneMatch)

*   [type ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsListCall)
*       *   [func (c *ProjectsLocationsListCall) Context(ctx context.Context) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsListCall.Context)
    *   [func (c *ProjectsLocationsListCall) Do(opts ...googleapi.CallOption) (*ApigatewayListLocationsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsListCall.Do)
    *   [func (c *ProjectsLocationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsListCall.Fields)
    *   [func (c *ProjectsLocationsListCall) Filter(filter string) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsListCall.Filter)
    *   [func (c *ProjectsLocationsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsListCall.Header)
    *   [func (c *ProjectsLocationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsListCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsListCall) PageSize(pageSize int64) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsListCall.PageSize)
    *   [func (c *ProjectsLocationsListCall) PageToken(pageToken string) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsListCall.PageToken)
    *   [func (c *ProjectsLocationsListCall) Pages(ctx context.Context, f func(*ApigatewayListLocationsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsListCall.Pages)

*   [type ProjectsLocationsOperationsCancelCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsCancelCall)
*       *   [func (c *ProjectsLocationsOperationsCancelCall) Context(ctx context.Context) *ProjectsLocationsOperationsCancelCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsCancelCall.Context)
    *   [func (c *ProjectsLocationsOperationsCancelCall) Do(opts ...googleapi.CallOption) (*Empty, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsCancelCall.Do)
    *   [func (c *ProjectsLocationsOperationsCancelCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsCancelCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsCancelCall.Fields)
    *   [func (c *ProjectsLocationsOperationsCancelCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsCancelCall.Header)

*   [type ProjectsLocationsOperationsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsDeleteCall)
*       *   [func (c *ProjectsLocationsOperationsDeleteCall) Context(ctx context.Context) *ProjectsLocationsOperationsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsDeleteCall.Context)
    *   [func (c *ProjectsLocationsOperationsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsDeleteCall.Do)
    *   [func (c *ProjectsLocationsOperationsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsDeleteCall.Fields)
    *   [func (c *ProjectsLocationsOperationsDeleteCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsDeleteCall.Header)

*   [type ProjectsLocationsOperationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsGetCall)
*       *   [func (c *ProjectsLocationsOperationsGetCall) Context(ctx context.Context) *ProjectsLocationsOperationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsGetCall.Context)
    *   [func (c *ProjectsLocationsOperationsGetCall) Do(opts ...googleapi.CallOption) (*ApigatewayOperation, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsGetCall.Do)
    *   [func (c *ProjectsLocationsOperationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsGetCall.Fields)
    *   [func (c *ProjectsLocationsOperationsGetCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsGetCall.Header)
    *   [func (c *ProjectsLocationsOperationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsOperationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsGetCall.IfNoneMatch)

*   [type ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsListCall)
*       *   [func (c *ProjectsLocationsOperationsListCall) Context(ctx context.Context) *ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsListCall.Context)
    *   [func (c *ProjectsLocationsOperationsListCall) Do(opts ...googleapi.CallOption) (*ApigatewayListOperationsResponse, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsListCall.Do)
    *   [func (c *ProjectsLocationsOperationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsListCall.Fields)
    *   [func (c *ProjectsLocationsOperationsListCall) Filter(filter string) *ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsListCall.Filter)
    *   [func (c *ProjectsLocationsOperationsListCall) Header() http.Header](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsListCall.Header)
    *   [func (c *ProjectsLocationsOperationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsListCall.IfNoneMatch)
    *   [func (c *ProjectsLocationsOperationsListCall) PageSize(pageSize int64) *ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsListCall.PageSize)
    *   [func (c *ProjectsLocationsOperationsListCall) PageToken(pageToken string) *ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsListCall.PageToken)
    *   [func (c *ProjectsLocationsOperationsListCall) Pages(ctx context.Context, f func(*ApigatewayListOperationsResponse) error) error](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsListCall.Pages)

*   [type ProjectsLocationsOperationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsService)
*       *   [func NewProjectsLocationsOperationsService(s *Service) *ProjectsLocationsOperationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#NewProjectsLocationsOperationsService)

*       *   [func (r *ProjectsLocationsOperationsService) Cancel(name string, ...) *ProjectsLocationsOperationsCancelCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsService.Cancel)
    *   [func (r *ProjectsLocationsOperationsService) Delete(name string) *ProjectsLocationsOperationsDeleteCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsService.Delete)
    *   [func (r *ProjectsLocationsOperationsService) Get(name string) *ProjectsLocationsOperationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsService.Get)
    *   [func (r *ProjectsLocationsOperationsService) List(name string) *ProjectsLocationsOperationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsService.List)

*   [type ProjectsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsService)
*       *   [func NewProjectsLocationsService(s *Service) *ProjectsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#NewProjectsLocationsService)

*       *   [func (r *ProjectsLocationsService) Get(name string) *ProjectsLocationsGetCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsService.Get)
    *   [func (r *ProjectsLocationsService) List(name string) *ProjectsLocationsListCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsService.List)

*   [type ProjectsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsService)
*       *   [func NewProjectsService(s *Service) *ProjectsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#NewProjectsService)

*   [type Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#Service)
*       *   [func New(client *http.Client) (*Service, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#New)deprecated
    *   [func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#NewService)

[View Source](https://github.com/googleapis/google-api-go-client/blob/v0.269.0/apigateway/v1alpha2/apigateway-gen.go#L81)

const (
	CloudPlatformScope = "https://www.googleapis.com/auth/cloud-platform"
)

OAuth2 scopes used by this API.

This section is empty.

This section is empty.

type ApigatewayAuditConfig struct {
	
	AuditLogConfigs []*[ApigatewayAuditLogConfig](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayAuditLogConfig) `json:"auditLogConfigs,omitempty"`

	
	
	Service [string](https://pkg.go.dev/builtin#string) `json:"service,omitempty"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ApigatewayAuditConfig: Specifies the audit configuration for a service. The configuration determines which permission types are logged, and what identities, if any, are exempted from logging. An AuditConfig must have one or more AuditLogConfigs. If there are AuditConfigs for both `allServices` and a specific service, the union of the two AuditConfigs is used for that service: the log_types specified in each AuditConfig are enabled, and the exempted_members in each AuditLogConfig are exempted. Example Policy with multiple AuditConfigs: { "audit_configs": [ { "service": "allServices", "audit_log_configs": [ { "log_type": "DATA_READ", "exempted_members": [ "user:jose@example.com" ] }, { "log_type": "DATA_WRITE" }, { "log_type": "ADMIN_READ" } ] }, { "service": "sampleservice.googleapis.com", "audit_log_configs": [ { "log_type": "DATA_READ" }, { "log_type": "DATA_WRITE", "exempted_members": [ "user:aliya@example.com" ] } ] } ] } For sampleservice, this policy enables DATA_READ, DATA_WRITE and ADMIN_READ logging. It also exempts jose@example.com from DATA_READ logging, and aliya@example.com from DATA_WRITE logging.

type ApigatewayAuditLogConfig struct {
	
	
	ExemptedMembers [][string](https://pkg.go.dev/builtin#string) `json:"exemptedMembers,omitempty"`

	
	
	
	
	
	
	LogType [string](https://pkg.go.dev/builtin#string) `json:"logType,omitempty"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ApigatewayAuditLogConfig: Provides the configuration for logging a type of permissions. Example: { "audit_log_configs": [ { "log_type": "DATA_READ", "exempted_members": [ "user:jose@example.com" ] }, { "log_type": "DATA_WRITE" } ] } This enables 'DATA_READ' and 'DATA_WRITE' logging, while exempting jose@example.com from DATA_READ logging.

type ApigatewayBinding struct {
	
	
	
	
	
	
	
	
	Condition *[ApigatewayExpr](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayExpr) `json:"condition,omitempty"`

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	Members [][string](https://pkg.go.dev/builtin#string) `json:"members,omitempty"`

	
	Role [string](https://pkg.go.dev/builtin#string) `json:"role,omitempty"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ApigatewayBinding: Associates `members` with a `role`.

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

type ApigatewayListLocationsResponse struct {
	
	Locations []*[ApigatewayLocation](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayLocation) `json:"locations,omitempty"`

	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	
	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ApigatewayListLocationsResponse: The response message for Locations.ListLocations.

type ApigatewayListOperationsResponse struct {
	NextPageToken [string](https://pkg.go.dev/builtin#string) `json:"nextPageToken,omitempty"`

	
	Operations []*[ApigatewayOperation](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayOperation) `json:"operations,omitempty"`

	
	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ApigatewayListOperationsResponse: The response message for Operations.ListOperations.

ApigatewayLocation: A resource that represents Google Cloud Platform location.

ApigatewayOperation: This resource represents a long-running operation that is the result of a network API call.

type ApigatewayPolicy struct {
	
	AuditConfigs []*[ApigatewayAuditConfig](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayAuditConfig) `json:"auditConfigs,omitempty"`

	
	
	Bindings []*[ApigatewayBinding](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayBinding) `json:"bindings,omitempty"`

	
	
	
	
	
	
	
	
	
	
	
	Etag [string](https://pkg.go.dev/builtin#string) `json:"etag,omitempty"`

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	Version [int64](https://pkg.go.dev/builtin#int64) `json:"version,omitempty"`

	
	[googleapi](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi).[ServerResponse](https://pkg.go.dev/google.golang.org/api@v0.269.0/googleapi#ServerResponse) `json:"-"`

	
	
	
	
	
	ForceSendFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`

	
	
	
	
	
	NullFields [][string](https://pkg.go.dev/builtin#string) `json:"-"`
}

ApigatewayPolicy: An Identity and Access Management (IAM) policy, which specifies access controls for Google Cloud resources. A `Policy` is a collection of `bindings`. A `binding` binds one or more `members` to a single `role`. Members can be user accounts, service accounts, Google groups, and domains (such as G Suite). A `role` is a named list of permissions; each `role` can be an IAM predefined role or a user-created custom role. For some types of Google Cloud resources, a `binding` can also specify a `condition`, which is a logical expression that allows access to a resource only if the expression evaluates to `true`. A condition can add constraints based on attributes of the request, the resource, or both. To learn which resources support conditions in their IAM policies, see the [IAM documentation]([https://cloud.google.com/iam/help/conditions/resource-p](https://cloud.google.com/iam/help/conditions/resource-p) olicies). **JSON example:** { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": [ "user:eve@example.com" ], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01T00:00:00.000Z')", } } ], "etag": "BwWWja0YfJA=", "version": 3 } **YAML example:** bindings: - members: - user:mike@example.com - group:admins@example.com - domain:google.com - serviceAccount:my-project-id@appspot.gserviceaccount.com role: roles/resourcemanager.organizationAdmin - members: - user:eve@example.com role: roles/resourcemanager.organizationViewer condition: title: expirable access description: Does not grant access after Sep 2020 expression: request.time < timestamp('2020-10-01T00:00:00.000Z') - etag: BwWWja0YfJA= - version: 3 For a description of IAM and its features, see the [IAM documentation]([https://cloud.google.com/iam/docs/](https://cloud.google.com/iam/docs/)).

type ApigatewaySetIamPolicyRequest struct {
	
	
	
	Policy *[ApigatewayPolicy](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayPolicy) `json:"policy,omitempty"`

	
	
	
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

ApigatewayStatus: The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC]([https://github.com/grpc](https://github.com/grpc)). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide]([https://cloud.google.com/apis/design/errors](https://cloud.google.com/apis/design/errors)).

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

Empty: A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); } The JSON representation for `Empty` is empty JSON object `{}`.

type ProjectsLocationsApisConfigsGetIamPolicyCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "apigateway.projects.locations.apis.configs.getIamPolicy" call. Exactly one of *ApigatewayPolicy or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *ApigatewayPolicy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (c *[ProjectsLocationsApisConfigsGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisConfigsGetIamPolicyCall)) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion [int64](https://pkg.go.dev/builtin#int64)) *[ProjectsLocationsApisConfigsGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisConfigsGetIamPolicyCall)

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The policy format version to be returned. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional bindings must specify version 3. Policies without any conditional bindings may specify any valid value or leave the field unset. To learn which resources support conditions in their IAM policies, see the [IAM documentation]([https://cloud.google.com/iam/help/conditions/resource-p](https://cloud.google.com/iam/help/conditions/resource-p) olicies).

type ProjectsLocationsApisConfigsService struct {
	
}

func NewProjectsLocationsApisConfigsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#Service)) *[ProjectsLocationsApisConfigsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisConfigsService)

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

SetIamPolicy: Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

TestIamPermissions: Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

type ProjectsLocationsApisConfigsSetIamPolicyCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "apigateway.projects.locations.apis.configs.setIamPolicy" call. Exactly one of *ApigatewayPolicy or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *ApigatewayPolicy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type ProjectsLocationsApisConfigsTestIamPermissionsCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "apigateway.projects.locations.apis.configs.testIamPermissions" call. Exactly one of *ApigatewayTestIamPermissionsResponse or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *ApigatewayTestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type ProjectsLocationsApisGetIamPolicyCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "apigateway.projects.locations.apis.getIamPolicy" call. Exactly one of *ApigatewayPolicy or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *ApigatewayPolicy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (c *[ProjectsLocationsApisGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisGetIamPolicyCall)) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion [int64](https://pkg.go.dev/builtin#int64)) *[ProjectsLocationsApisGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisGetIamPolicyCall)

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The policy format version to be returned. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional bindings must specify version 3. Policies without any conditional bindings may specify any valid value or leave the field unset. To learn which resources support conditions in their IAM policies, see the [IAM documentation]([https://cloud.google.com/iam/help/conditions/resource-p](https://cloud.google.com/iam/help/conditions/resource-p) olicies).

type ProjectsLocationsApisService struct {
 Configs *[ProjectsLocationsApisConfigsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisConfigsService)	
}

func NewProjectsLocationsApisService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#Service)) *[ProjectsLocationsApisService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisService)

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

SetIamPolicy: Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

func (r *[ProjectsLocationsApisService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisService)) TestIamPermissions(resource [string](https://pkg.go.dev/builtin#string), apigatewaytestiampermissionsrequest *[ApigatewayTestIamPermissionsRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayTestIamPermissionsRequest)) *[ProjectsLocationsApisTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisTestIamPermissionsCall)

TestIamPermissions: Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

type ProjectsLocationsApisSetIamPolicyCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "apigateway.projects.locations.apis.setIamPolicy" call. Exactly one of *ApigatewayPolicy or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *ApigatewayPolicy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type ProjectsLocationsApisTestIamPermissionsCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "apigateway.projects.locations.apis.testIamPermissions" call. Exactly one of *ApigatewayTestIamPermissionsResponse or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *ApigatewayTestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type ProjectsLocationsGatewaysGetIamPolicyCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "apigateway.projects.locations.gateways.getIamPolicy" call. Exactly one of *ApigatewayPolicy or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *ApigatewayPolicy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

func (c *[ProjectsLocationsGatewaysGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGatewaysGetIamPolicyCall)) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion [int64](https://pkg.go.dev/builtin#int64)) *[ProjectsLocationsGatewaysGetIamPolicyCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGatewaysGetIamPolicyCall)

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The policy format version to be returned. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional bindings must specify version 3. Policies without any conditional bindings may specify any valid value or leave the field unset. To learn which resources support conditions in their IAM policies, see the [IAM documentation]([https://cloud.google.com/iam/help/conditions/resource-p](https://cloud.google.com/iam/help/conditions/resource-p) olicies).

type ProjectsLocationsGatewaysService struct {
	
}

func NewProjectsLocationsGatewaysService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#Service)) *[ProjectsLocationsGatewaysService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGatewaysService)

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

SetIamPolicy: Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

func (r *[ProjectsLocationsGatewaysService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGatewaysService)) TestIamPermissions(resource [string](https://pkg.go.dev/builtin#string), apigatewaytestiampermissionsrequest *[ApigatewayTestIamPermissionsRequest](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ApigatewayTestIamPermissionsRequest)) *[ProjectsLocationsGatewaysTestIamPermissionsCall](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGatewaysTestIamPermissionsCall)

TestIamPermissions: Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

type ProjectsLocationsGatewaysSetIamPolicyCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "apigateway.projects.locations.gateways.setIamPolicy" call. Exactly one of *ApigatewayPolicy or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *ApigatewayPolicy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type ProjectsLocationsGatewaysTestIamPermissionsCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "apigateway.projects.locations.gateways.testIamPermissions" call. Exactly one of *ApigatewayTestIamPermissionsResponse or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *ApigatewayTestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type ProjectsLocationsGetCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "apigateway.projects.locations.get" call. Exactly one of *ApigatewayLocation or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *ApigatewayLocation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type ProjectsLocationsListCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "apigateway.projects.locations.list" call. Exactly one of *ApigatewayListLocationsResponse or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *ApigatewayListLocationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Filter sets the optional parameter "filter": The standard list filter.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

PageSize sets the optional parameter "pageSize": The standard list page size.

PageToken sets the optional parameter "pageToken": The standard list page token.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsOperationsCancelCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "apigateway.projects.locations.operations.cancel" call. Exactly one of *Empty or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type ProjectsLocationsOperationsDeleteCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "apigateway.projects.locations.operations.delete" call. Exactly one of *Empty or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

type ProjectsLocationsOperationsGetCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "apigateway.projects.locations.operations.get" call. Exactly one of *ApigatewayOperation or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *ApigatewayOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

type ProjectsLocationsOperationsListCall struct {
	
}

Context sets the context to be used in this call's Do method. Any pending HTTP request will be aborted if the provided context is canceled.

Do executes the "apigateway.projects.locations.operations.list" call. Exactly one of *ApigatewayListOperationsResponse or error will be non-nil. Any non-2xx status code is an error. Response headers are in either *ApigatewayListOperationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

Filter sets the optional parameter "filter": The standard list filter.

Header returns an http.Header that can be modified by the caller to add HTTP headers to the request.

IfNoneMatch sets the optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request. Use googleapi.IsNotModified to check whether the response error from Do is the result of In-None-Match.

PageSize sets the optional parameter "pageSize": The standard list page size.

PageToken sets the optional parameter "pageToken": The standard list page token.

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsOperationsService struct {
	
}

func NewProjectsLocationsOperationsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#Service)) *[ProjectsLocationsOperationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsService)

Cancel: Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.

Delete: Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

Get: Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

List: Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. NOTE: the `name` binding allows API services to override the binding to use different resource name schemes, such as `users/*/operations`. To override the binding, API services can add a binding such as "/v1/{name=users/*}/operations" to their service configuration. For backwards compatibility, the default name includes the operations collection id, however overriding users must ensure the name binding is the parent resource, without the operations collection id.

type ProjectsLocationsService struct {
 Apis *[ProjectsLocationsApisService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsApisService)
 Gateways *[ProjectsLocationsGatewaysService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsGatewaysService)
 Operations *[ProjectsLocationsOperationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsOperationsService)	
}

func NewProjectsLocationsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#Service)) *[ProjectsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsService)

Get: Gets information about a location.

List: Lists information about the supported locations for this service.

type ProjectsService struct {
 Locations *[ProjectsLocationsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsLocationsService)	
}

func NewProjectsService(s *[Service](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#Service)) *[ProjectsService](https://pkg.go.dev/google.golang.org/api@v0.269.0/apigateway/v1alpha2#ProjectsService)

New creates a new Service. It uses the provided http.Client for requests.

Deprecated: please use NewService instead. To provide a custom HTTP client, use option.WithHTTPClient. If you are using google.golang.org/api/googleapis/transport.APIKey, use option.WithAPIKey with NewService instead.

NewService creates a new Service.
