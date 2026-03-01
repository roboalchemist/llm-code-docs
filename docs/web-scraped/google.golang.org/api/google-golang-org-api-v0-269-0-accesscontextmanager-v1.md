# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/accesscontextmanager/v1

Title: accesscontextmanager package - google.golang.org/api/accesscontextmanager/v1 - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/accesscontextmanager/v1

Markdown Content:
Skip to Main Content
Why Go
Learn
Docs
Packages
Community
Discover Packages
 
google.golang.org/api
 
accesscontextmanager
 
v1
accesscontextmanager
package
Version: v0.269.0 Latest 
Published: Feb 24, 2026 
License: BSD-3-Clause 
Imports: 18 
Imported by: 0
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

Package accesscontextmanager provides access to the Access Context Manager API.

For product documentation, see: https://cloud.google.com/access-context-manager/docs/reference/rest/

Library status ¶

These client libraries are officially supported by Google. However, this library is considered complete and is in maintenance mode. This means that we will address critical bugs and security issues but will not add any new features.

When possible, we recommend using our newer [Cloud Client Libraries for Go](https://pkg.go.dev/cloud.google.com/go) that are still actively being worked and iterated on.

Creating a client ¶

Usage example:

import "google.golang.org/api/accesscontextmanager/v1"
...
ctx := context.Background()
accesscontextmanagerService, err := accesscontextmanager.NewService(ctx)


In this example, Google Application Default Credentials are used for authentication. For information on how to create and obtain Application Default Credentials, see https://developers.google.com/identity/protocols/application-default-credentials.

Other authentication options ¶

To use an API key for authentication (note: some APIs do not support API keys), use google.golang.org/api/option.WithAPIKey:

accesscontextmanagerService, err := accesscontextmanager.NewService(ctx, option.WithAPIKey("AIza..."))


To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow, use google.golang.org/api/option.WithTokenSource:

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
accesscontextmanagerService, err := accesscontextmanager.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))


See google.golang.org/api/option.ClientOption for details on options.

Index ¶
Constants
type AccessContextManagerOperationMetadata
type AccessLevel
func (s AccessLevel) MarshalJSON() ([]byte, error)
type AccessPoliciesAccessLevelsCreateCall
func (c *AccessPoliciesAccessLevelsCreateCall) Context(ctx context.Context) *AccessPoliciesAccessLevelsCreateCall
func (c *AccessPoliciesAccessLevelsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *AccessPoliciesAccessLevelsCreateCall) Fields(s ...googleapi.Field) *AccessPoliciesAccessLevelsCreateCall
func (c *AccessPoliciesAccessLevelsCreateCall) Header() http.Header
type AccessPoliciesAccessLevelsDeleteCall
func (c *AccessPoliciesAccessLevelsDeleteCall) Context(ctx context.Context) *AccessPoliciesAccessLevelsDeleteCall
func (c *AccessPoliciesAccessLevelsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *AccessPoliciesAccessLevelsDeleteCall) Fields(s ...googleapi.Field) *AccessPoliciesAccessLevelsDeleteCall
func (c *AccessPoliciesAccessLevelsDeleteCall) Header() http.Header
type AccessPoliciesAccessLevelsGetCall
func (c *AccessPoliciesAccessLevelsGetCall) AccessLevelFormat(accessLevelFormat string) *AccessPoliciesAccessLevelsGetCall
func (c *AccessPoliciesAccessLevelsGetCall) Context(ctx context.Context) *AccessPoliciesAccessLevelsGetCall
func (c *AccessPoliciesAccessLevelsGetCall) Do(opts ...googleapi.CallOption) (*AccessLevel, error)
func (c *AccessPoliciesAccessLevelsGetCall) Fields(s ...googleapi.Field) *AccessPoliciesAccessLevelsGetCall
func (c *AccessPoliciesAccessLevelsGetCall) Header() http.Header
func (c *AccessPoliciesAccessLevelsGetCall) IfNoneMatch(entityTag string) *AccessPoliciesAccessLevelsGetCall
type AccessPoliciesAccessLevelsListCall
func (c *AccessPoliciesAccessLevelsListCall) AccessLevelFormat(accessLevelFormat string) *AccessPoliciesAccessLevelsListCall
func (c *AccessPoliciesAccessLevelsListCall) Context(ctx context.Context) *AccessPoliciesAccessLevelsListCall
func (c *AccessPoliciesAccessLevelsListCall) Do(opts ...googleapi.CallOption) (*ListAccessLevelsResponse, error)
func (c *AccessPoliciesAccessLevelsListCall) Fields(s ...googleapi.Field) *AccessPoliciesAccessLevelsListCall
func (c *AccessPoliciesAccessLevelsListCall) Header() http.Header
func (c *AccessPoliciesAccessLevelsListCall) IfNoneMatch(entityTag string) *AccessPoliciesAccessLevelsListCall
func (c *AccessPoliciesAccessLevelsListCall) PageSize(pageSize int64) *AccessPoliciesAccessLevelsListCall
func (c *AccessPoliciesAccessLevelsListCall) PageToken(pageToken string) *AccessPoliciesAccessLevelsListCall
func (c *AccessPoliciesAccessLevelsListCall) Pages(ctx context.Context, f func(*ListAccessLevelsResponse) error) error
type AccessPoliciesAccessLevelsPatchCall
func (c *AccessPoliciesAccessLevelsPatchCall) Context(ctx context.Context) *AccessPoliciesAccessLevelsPatchCall
func (c *AccessPoliciesAccessLevelsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *AccessPoliciesAccessLevelsPatchCall) Fields(s ...googleapi.Field) *AccessPoliciesAccessLevelsPatchCall
func (c *AccessPoliciesAccessLevelsPatchCall) Header() http.Header
func (c *AccessPoliciesAccessLevelsPatchCall) UpdateMask(updateMask string) *AccessPoliciesAccessLevelsPatchCall
type AccessPoliciesAccessLevelsReplaceAllCall
func (c *AccessPoliciesAccessLevelsReplaceAllCall) Context(ctx context.Context) *AccessPoliciesAccessLevelsReplaceAllCall
func (c *AccessPoliciesAccessLevelsReplaceAllCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *AccessPoliciesAccessLevelsReplaceAllCall) Fields(s ...googleapi.Field) *AccessPoliciesAccessLevelsReplaceAllCall
func (c *AccessPoliciesAccessLevelsReplaceAllCall) Header() http.Header
type AccessPoliciesAccessLevelsService
func NewAccessPoliciesAccessLevelsService(s *Service) *AccessPoliciesAccessLevelsService
func (r *AccessPoliciesAccessLevelsService) Create(parent string, accesslevel *AccessLevel) *AccessPoliciesAccessLevelsCreateCall
func (r *AccessPoliciesAccessLevelsService) Delete(name string) *AccessPoliciesAccessLevelsDeleteCall
func (r *AccessPoliciesAccessLevelsService) Get(name string) *AccessPoliciesAccessLevelsGetCall
func (r *AccessPoliciesAccessLevelsService) List(parent string) *AccessPoliciesAccessLevelsListCall
func (r *AccessPoliciesAccessLevelsService) Patch(name string, accesslevel *AccessLevel) *AccessPoliciesAccessLevelsPatchCall
func (r *AccessPoliciesAccessLevelsService) ReplaceAll(parent string, replaceaccesslevelsrequest *ReplaceAccessLevelsRequest) *AccessPoliciesAccessLevelsReplaceAllCall
func (r *AccessPoliciesAccessLevelsService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *AccessPoliciesAccessLevelsTestIamPermissionsCall
type AccessPoliciesAccessLevelsTestIamPermissionsCall
func (c *AccessPoliciesAccessLevelsTestIamPermissionsCall) Context(ctx context.Context) *AccessPoliciesAccessLevelsTestIamPermissionsCall
func (c *AccessPoliciesAccessLevelsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)
func (c *AccessPoliciesAccessLevelsTestIamPermissionsCall) Fields(s ...googleapi.Field) *AccessPoliciesAccessLevelsTestIamPermissionsCall
func (c *AccessPoliciesAccessLevelsTestIamPermissionsCall) Header() http.Header
type AccessPoliciesAuthorizedOrgsDescsCreateCall
func (c *AccessPoliciesAuthorizedOrgsDescsCreateCall) Context(ctx context.Context) *AccessPoliciesAuthorizedOrgsDescsCreateCall
func (c *AccessPoliciesAuthorizedOrgsDescsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *AccessPoliciesAuthorizedOrgsDescsCreateCall) Fields(s ...googleapi.Field) *AccessPoliciesAuthorizedOrgsDescsCreateCall
func (c *AccessPoliciesAuthorizedOrgsDescsCreateCall) Header() http.Header
type AccessPoliciesAuthorizedOrgsDescsDeleteCall
func (c *AccessPoliciesAuthorizedOrgsDescsDeleteCall) Context(ctx context.Context) *AccessPoliciesAuthorizedOrgsDescsDeleteCall
func (c *AccessPoliciesAuthorizedOrgsDescsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *AccessPoliciesAuthorizedOrgsDescsDeleteCall) Fields(s ...googleapi.Field) *AccessPoliciesAuthorizedOrgsDescsDeleteCall
func (c *AccessPoliciesAuthorizedOrgsDescsDeleteCall) Header() http.Header
type AccessPoliciesAuthorizedOrgsDescsGetCall
func (c *AccessPoliciesAuthorizedOrgsDescsGetCall) Context(ctx context.Context) *AccessPoliciesAuthorizedOrgsDescsGetCall
func (c *AccessPoliciesAuthorizedOrgsDescsGetCall) Do(opts ...googleapi.CallOption) (*AuthorizedOrgsDesc, error)
func (c *AccessPoliciesAuthorizedOrgsDescsGetCall) Fields(s ...googleapi.Field) *AccessPoliciesAuthorizedOrgsDescsGetCall
func (c *AccessPoliciesAuthorizedOrgsDescsGetCall) Header() http.Header
func (c *AccessPoliciesAuthorizedOrgsDescsGetCall) IfNoneMatch(entityTag string) *AccessPoliciesAuthorizedOrgsDescsGetCall
type AccessPoliciesAuthorizedOrgsDescsListCall
func (c *AccessPoliciesAuthorizedOrgsDescsListCall) Context(ctx context.Context) *AccessPoliciesAuthorizedOrgsDescsListCall
func (c *AccessPoliciesAuthorizedOrgsDescsListCall) Do(opts ...googleapi.CallOption) (*ListAuthorizedOrgsDescsResponse, error)
func (c *AccessPoliciesAuthorizedOrgsDescsListCall) Fields(s ...googleapi.Field) *AccessPoliciesAuthorizedOrgsDescsListCall
func (c *AccessPoliciesAuthorizedOrgsDescsListCall) Header() http.Header
func (c *AccessPoliciesAuthorizedOrgsDescsListCall) IfNoneMatch(entityTag string) *AccessPoliciesAuthorizedOrgsDescsListCall
func (c *AccessPoliciesAuthorizedOrgsDescsListCall) PageSize(pageSize int64) *AccessPoliciesAuthorizedOrgsDescsListCall
func (c *AccessPoliciesAuthorizedOrgsDescsListCall) PageToken(pageToken string) *AccessPoliciesAuthorizedOrgsDescsListCall
func (c *AccessPoliciesAuthorizedOrgsDescsListCall) Pages(ctx context.Context, f func(*ListAuthorizedOrgsDescsResponse) error) error
type AccessPoliciesAuthorizedOrgsDescsPatchCall
func (c *AccessPoliciesAuthorizedOrgsDescsPatchCall) Context(ctx context.Context) *AccessPoliciesAuthorizedOrgsDescsPatchCall
func (c *AccessPoliciesAuthorizedOrgsDescsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *AccessPoliciesAuthorizedOrgsDescsPatchCall) Fields(s ...googleapi.Field) *AccessPoliciesAuthorizedOrgsDescsPatchCall
func (c *AccessPoliciesAuthorizedOrgsDescsPatchCall) Header() http.Header
func (c *AccessPoliciesAuthorizedOrgsDescsPatchCall) UpdateMask(updateMask string) *AccessPoliciesAuthorizedOrgsDescsPatchCall
type AccessPoliciesAuthorizedOrgsDescsService
func NewAccessPoliciesAuthorizedOrgsDescsService(s *Service) *AccessPoliciesAuthorizedOrgsDescsService
func (r *AccessPoliciesAuthorizedOrgsDescsService) Create(parent string, authorizedorgsdesc *AuthorizedOrgsDesc) *AccessPoliciesAuthorizedOrgsDescsCreateCall
func (r *AccessPoliciesAuthorizedOrgsDescsService) Delete(name string) *AccessPoliciesAuthorizedOrgsDescsDeleteCall
func (r *AccessPoliciesAuthorizedOrgsDescsService) Get(name string) *AccessPoliciesAuthorizedOrgsDescsGetCall
func (r *AccessPoliciesAuthorizedOrgsDescsService) List(parent string) *AccessPoliciesAuthorizedOrgsDescsListCall
func (r *AccessPoliciesAuthorizedOrgsDescsService) Patch(name string, authorizedorgsdesc *AuthorizedOrgsDesc) *AccessPoliciesAuthorizedOrgsDescsPatchCall
type AccessPoliciesCreateCall
func (c *AccessPoliciesCreateCall) Context(ctx context.Context) *AccessPoliciesCreateCall
func (c *AccessPoliciesCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *AccessPoliciesCreateCall) Fields(s ...googleapi.Field) *AccessPoliciesCreateCall
func (c *AccessPoliciesCreateCall) Header() http.Header
type AccessPoliciesDeleteCall
func (c *AccessPoliciesDeleteCall) Context(ctx context.Context) *AccessPoliciesDeleteCall
func (c *AccessPoliciesDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *AccessPoliciesDeleteCall) Fields(s ...googleapi.Field) *AccessPoliciesDeleteCall
func (c *AccessPoliciesDeleteCall) Header() http.Header
type AccessPoliciesGetCall
func (c *AccessPoliciesGetCall) Context(ctx context.Context) *AccessPoliciesGetCall
func (c *AccessPoliciesGetCall) Do(opts ...googleapi.CallOption) (*AccessPolicy, error)
func (c *AccessPoliciesGetCall) Fields(s ...googleapi.Field) *AccessPoliciesGetCall
func (c *AccessPoliciesGetCall) Header() http.Header
func (c *AccessPoliciesGetCall) IfNoneMatch(entityTag string) *AccessPoliciesGetCall
type AccessPoliciesGetIamPolicyCall
func (c *AccessPoliciesGetIamPolicyCall) Context(ctx context.Context) *AccessPoliciesGetIamPolicyCall
func (c *AccessPoliciesGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *AccessPoliciesGetIamPolicyCall) Fields(s ...googleapi.Field) *AccessPoliciesGetIamPolicyCall
func (c *AccessPoliciesGetIamPolicyCall) Header() http.Header
type AccessPoliciesListCall
func (c *AccessPoliciesListCall) Context(ctx context.Context) *AccessPoliciesListCall
func (c *AccessPoliciesListCall) Do(opts ...googleapi.CallOption) (*ListAccessPoliciesResponse, error)
func (c *AccessPoliciesListCall) Fields(s ...googleapi.Field) *AccessPoliciesListCall
func (c *AccessPoliciesListCall) Header() http.Header
func (c *AccessPoliciesListCall) IfNoneMatch(entityTag string) *AccessPoliciesListCall
func (c *AccessPoliciesListCall) PageSize(pageSize int64) *AccessPoliciesListCall
func (c *AccessPoliciesListCall) PageToken(pageToken string) *AccessPoliciesListCall
func (c *AccessPoliciesListCall) Pages(ctx context.Context, f func(*ListAccessPoliciesResponse) error) error
func (c *AccessPoliciesListCall) Parent(parent string) *AccessPoliciesListCall
type AccessPoliciesPatchCall
func (c *AccessPoliciesPatchCall) Context(ctx context.Context) *AccessPoliciesPatchCall
func (c *AccessPoliciesPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *AccessPoliciesPatchCall) Fields(s ...googleapi.Field) *AccessPoliciesPatchCall
func (c *AccessPoliciesPatchCall) Header() http.Header
func (c *AccessPoliciesPatchCall) UpdateMask(updateMask string) *AccessPoliciesPatchCall
type AccessPoliciesService
func NewAccessPoliciesService(s *Service) *AccessPoliciesService
func (r *AccessPoliciesService) Create(accesspolicy *AccessPolicy) *AccessPoliciesCreateCall
func (r *AccessPoliciesService) Delete(name string) *AccessPoliciesDeleteCall
func (r *AccessPoliciesService) Get(name string) *AccessPoliciesGetCall
func (r *AccessPoliciesService) GetIamPolicy(resource string, getiampolicyrequest *GetIamPolicyRequest) *AccessPoliciesGetIamPolicyCall
func (r *AccessPoliciesService) List() *AccessPoliciesListCall
func (r *AccessPoliciesService) Patch(name string, accesspolicy *AccessPolicy) *AccessPoliciesPatchCall
func (r *AccessPoliciesService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *AccessPoliciesSetIamPolicyCall
func (r *AccessPoliciesService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *AccessPoliciesTestIamPermissionsCall
type AccessPoliciesServicePerimetersCommitCall
func (c *AccessPoliciesServicePerimetersCommitCall) Context(ctx context.Context) *AccessPoliciesServicePerimetersCommitCall
func (c *AccessPoliciesServicePerimetersCommitCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *AccessPoliciesServicePerimetersCommitCall) Fields(s ...googleapi.Field) *AccessPoliciesServicePerimetersCommitCall
func (c *AccessPoliciesServicePerimetersCommitCall) Header() http.Header
type AccessPoliciesServicePerimetersCreateCall
func (c *AccessPoliciesServicePerimetersCreateCall) Context(ctx context.Context) *AccessPoliciesServicePerimetersCreateCall
func (c *AccessPoliciesServicePerimetersCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *AccessPoliciesServicePerimetersCreateCall) Fields(s ...googleapi.Field) *AccessPoliciesServicePerimetersCreateCall
func (c *AccessPoliciesServicePerimetersCreateCall) Header() http.Header
type AccessPoliciesServicePerimetersDeleteCall
func (c *AccessPoliciesServicePerimetersDeleteCall) Context(ctx context.Context) *AccessPoliciesServicePerimetersDeleteCall
func (c *AccessPoliciesServicePerimetersDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *AccessPoliciesServicePerimetersDeleteCall) Fields(s ...googleapi.Field) *AccessPoliciesServicePerimetersDeleteCall
func (c *AccessPoliciesServicePerimetersDeleteCall) Header() http.Header
type AccessPoliciesServicePerimetersGetCall
func (c *AccessPoliciesServicePerimetersGetCall) Context(ctx context.Context) *AccessPoliciesServicePerimetersGetCall
func (c *AccessPoliciesServicePerimetersGetCall) Do(opts ...googleapi.CallOption) (*ServicePerimeter, error)
func (c *AccessPoliciesServicePerimetersGetCall) Fields(s ...googleapi.Field) *AccessPoliciesServicePerimetersGetCall
func (c *AccessPoliciesServicePerimetersGetCall) Header() http.Header
func (c *AccessPoliciesServicePerimetersGetCall) IfNoneMatch(entityTag string) *AccessPoliciesServicePerimetersGetCall
type AccessPoliciesServicePerimetersListCall
func (c *AccessPoliciesServicePerimetersListCall) Context(ctx context.Context) *AccessPoliciesServicePerimetersListCall
func (c *AccessPoliciesServicePerimetersListCall) Do(opts ...googleapi.CallOption) (*ListServicePerimetersResponse, error)
func (c *AccessPoliciesServicePerimetersListCall) Fields(s ...googleapi.Field) *AccessPoliciesServicePerimetersListCall
func (c *AccessPoliciesServicePerimetersListCall) Header() http.Header
func (c *AccessPoliciesServicePerimetersListCall) IfNoneMatch(entityTag string) *AccessPoliciesServicePerimetersListCall
func (c *AccessPoliciesServicePerimetersListCall) PageSize(pageSize int64) *AccessPoliciesServicePerimetersListCall
func (c *AccessPoliciesServicePerimetersListCall) PageToken(pageToken string) *AccessPoliciesServicePerimetersListCall
func (c *AccessPoliciesServicePerimetersListCall) Pages(ctx context.Context, f func(*ListServicePerimetersResponse) error) error
type AccessPoliciesServicePerimetersPatchCall
func (c *AccessPoliciesServicePerimetersPatchCall) Context(ctx context.Context) *AccessPoliciesServicePerimetersPatchCall
func (c *AccessPoliciesServicePerimetersPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *AccessPoliciesServicePerimetersPatchCall) Fields(s ...googleapi.Field) *AccessPoliciesServicePerimetersPatchCall
func (c *AccessPoliciesServicePerimetersPatchCall) Header() http.Header
func (c *AccessPoliciesServicePerimetersPatchCall) UpdateMask(updateMask string) *AccessPoliciesServicePerimetersPatchCall
type AccessPoliciesServicePerimetersReplaceAllCall
func (c *AccessPoliciesServicePerimetersReplaceAllCall) Context(ctx context.Context) *AccessPoliciesServicePerimetersReplaceAllCall
func (c *AccessPoliciesServicePerimetersReplaceAllCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *AccessPoliciesServicePerimetersReplaceAllCall) Fields(s ...googleapi.Field) *AccessPoliciesServicePerimetersReplaceAllCall
func (c *AccessPoliciesServicePerimetersReplaceAllCall) Header() http.Header
type AccessPoliciesServicePerimetersService
func NewAccessPoliciesServicePerimetersService(s *Service) *AccessPoliciesServicePerimetersService
func (r *AccessPoliciesServicePerimetersService) Commit(parent string, commitserviceperimetersrequest *CommitServicePerimetersRequest) *AccessPoliciesServicePerimetersCommitCall
func (r *AccessPoliciesServicePerimetersService) Create(parent string, serviceperimeter *ServicePerimeter) *AccessPoliciesServicePerimetersCreateCall
func (r *AccessPoliciesServicePerimetersService) Delete(name string) *AccessPoliciesServicePerimetersDeleteCall
func (r *AccessPoliciesServicePerimetersService) Get(name string) *AccessPoliciesServicePerimetersGetCall
func (r *AccessPoliciesServicePerimetersService) List(parent string) *AccessPoliciesServicePerimetersListCall
func (r *AccessPoliciesServicePerimetersService) Patch(name string, serviceperimeter *ServicePerimeter) *AccessPoliciesServicePerimetersPatchCall
func (r *AccessPoliciesServicePerimetersService) ReplaceAll(parent string, ...) *AccessPoliciesServicePerimetersReplaceAllCall
func (r *AccessPoliciesServicePerimetersService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *AccessPoliciesServicePerimetersTestIamPermissionsCall
type AccessPoliciesServicePerimetersTestIamPermissionsCall
func (c *AccessPoliciesServicePerimetersTestIamPermissionsCall) Context(ctx context.Context) *AccessPoliciesServicePerimetersTestIamPermissionsCall
func (c *AccessPoliciesServicePerimetersTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)
func (c *AccessPoliciesServicePerimetersTestIamPermissionsCall) Fields(s ...googleapi.Field) *AccessPoliciesServicePerimetersTestIamPermissionsCall
func (c *AccessPoliciesServicePerimetersTestIamPermissionsCall) Header() http.Header
type AccessPoliciesSetIamPolicyCall
func (c *AccessPoliciesSetIamPolicyCall) Context(ctx context.Context) *AccessPoliciesSetIamPolicyCall
func (c *AccessPoliciesSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)
func (c *AccessPoliciesSetIamPolicyCall) Fields(s ...googleapi.Field) *AccessPoliciesSetIamPolicyCall
func (c *AccessPoliciesSetIamPolicyCall) Header() http.Header
type AccessPoliciesTestIamPermissionsCall
func (c *AccessPoliciesTestIamPermissionsCall) Context(ctx context.Context) *AccessPoliciesTestIamPermissionsCall
func (c *AccessPoliciesTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)
func (c *AccessPoliciesTestIamPermissionsCall) Fields(s ...googleapi.Field) *AccessPoliciesTestIamPermissionsCall
func (c *AccessPoliciesTestIamPermissionsCall) Header() http.Header
type AccessPolicy
func (s AccessPolicy) MarshalJSON() ([]byte, error)
type AccessScope
func (s AccessScope) MarshalJSON() ([]byte, error)
type AccessSettings
func (s AccessSettings) MarshalJSON() ([]byte, error)
type ApiOperation
func (s ApiOperation) MarshalJSON() ([]byte, error)
type Application
func (s Application) MarshalJSON() ([]byte, error)
type AuditConfig
func (s AuditConfig) MarshalJSON() ([]byte, error)
type AuditLogConfig
func (s AuditLogConfig) MarshalJSON() ([]byte, error)
type AuthorizedOrgsDesc
func (s AuthorizedOrgsDesc) MarshalJSON() ([]byte, error)
type BasicLevel
func (s BasicLevel) MarshalJSON() ([]byte, error)
type Binding
func (s Binding) MarshalJSON() ([]byte, error)
type CancelOperationRequest
type ClientScope
func (s ClientScope) MarshalJSON() ([]byte, error)
type CommitServicePerimetersRequest
func (s CommitServicePerimetersRequest) MarshalJSON() ([]byte, error)
type CommitServicePerimetersResponse
func (s CommitServicePerimetersResponse) MarshalJSON() ([]byte, error)
type Condition
func (s Condition) MarshalJSON() ([]byte, error)
type CustomLevel
func (s CustomLevel) MarshalJSON() ([]byte, error)
type DevicePolicy
func (s DevicePolicy) MarshalJSON() ([]byte, error)
type EgressFrom
func (s EgressFrom) MarshalJSON() ([]byte, error)
type EgressPolicy
func (s EgressPolicy) MarshalJSON() ([]byte, error)
type EgressSource
func (s EgressSource) MarshalJSON() ([]byte, error)
type EgressTo
func (s EgressTo) MarshalJSON() ([]byte, error)
type Empty
type Expr
func (s Expr) MarshalJSON() ([]byte, error)
type GcpUserAccessBinding
func (s GcpUserAccessBinding) MarshalJSON() ([]byte, error)
type GcpUserAccessBindingOperationMetadata
type GetIamPolicyRequest
func (s GetIamPolicyRequest) MarshalJSON() ([]byte, error)
type GetPolicyOptions
func (s GetPolicyOptions) MarshalJSON() ([]byte, error)
type IngressFrom
func (s IngressFrom) MarshalJSON() ([]byte, error)
type IngressPolicy
func (s IngressPolicy) MarshalJSON() ([]byte, error)
type IngressSource
func (s IngressSource) MarshalJSON() ([]byte, error)
type IngressTo
func (s IngressTo) MarshalJSON() ([]byte, error)
type ListAccessLevelsResponse
func (s ListAccessLevelsResponse) MarshalJSON() ([]byte, error)
type ListAccessPoliciesResponse
func (s ListAccessPoliciesResponse) MarshalJSON() ([]byte, error)
type ListAuthorizedOrgsDescsResponse
func (s ListAuthorizedOrgsDescsResponse) MarshalJSON() ([]byte, error)
type ListGcpUserAccessBindingsResponse
func (s ListGcpUserAccessBindingsResponse) MarshalJSON() ([]byte, error)
type ListOperationsResponse
func (s ListOperationsResponse) MarshalJSON() ([]byte, error)
type ListServicePerimetersResponse
func (s ListServicePerimetersResponse) MarshalJSON() ([]byte, error)
type ListSupportedPermissionsResponse
func (s ListSupportedPermissionsResponse) MarshalJSON() ([]byte, error)
type ListSupportedServicesResponse
func (s ListSupportedServicesResponse) MarshalJSON() ([]byte, error)
type MethodSelector
func (s MethodSelector) MarshalJSON() ([]byte, error)
type Operation
func (s Operation) MarshalJSON() ([]byte, error)
type OperationsCancelCall
func (c *OperationsCancelCall) Context(ctx context.Context) *OperationsCancelCall
func (c *OperationsCancelCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *OperationsCancelCall) Fields(s ...googleapi.Field) *OperationsCancelCall
func (c *OperationsCancelCall) Header() http.Header
type OperationsDeleteCall
func (c *OperationsDeleteCall) Context(ctx context.Context) *OperationsDeleteCall
func (c *OperationsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *OperationsDeleteCall) Fields(s ...googleapi.Field) *OperationsDeleteCall
func (c *OperationsDeleteCall) Header() http.Header
type OperationsGetCall
func (c *OperationsGetCall) Context(ctx context.Context) *OperationsGetCall
func (c *OperationsGetCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *OperationsGetCall) Fields(s ...googleapi.Field) *OperationsGetCall
func (c *OperationsGetCall) Header() http.Header
func (c *OperationsGetCall) IfNoneMatch(entityTag string) *OperationsGetCall
type OperationsListCall
func (c *OperationsListCall) Context(ctx context.Context) *OperationsListCall
func (c *OperationsListCall) Do(opts ...googleapi.CallOption) (*ListOperationsResponse, error)
func (c *OperationsListCall) Fields(s ...googleapi.Field) *OperationsListCall
func (c *OperationsListCall) Filter(filter string) *OperationsListCall
func (c *OperationsListCall) Header() http.Header
func (c *OperationsListCall) IfNoneMatch(entityTag string) *OperationsListCall
func (c *OperationsListCall) PageSize(pageSize int64) *OperationsListCall
func (c *OperationsListCall) PageToken(pageToken string) *OperationsListCall
func (c *OperationsListCall) Pages(ctx context.Context, f func(*ListOperationsResponse) error) error
func (c *OperationsListCall) ReturnPartialSuccess(returnPartialSuccess bool) *OperationsListCall
type OperationsService
func NewOperationsService(s *Service) *OperationsService
func (r *OperationsService) Cancel(name string, canceloperationrequest *CancelOperationRequest) *OperationsCancelCall
func (r *OperationsService) Delete(name string) *OperationsDeleteCall
func (r *OperationsService) Get(name string) *OperationsGetCall
func (r *OperationsService) List(name string) *OperationsListCall
type OrganizationsGcpUserAccessBindingsCreateCall
func (c *OrganizationsGcpUserAccessBindingsCreateCall) Context(ctx context.Context) *OrganizationsGcpUserAccessBindingsCreateCall
func (c *OrganizationsGcpUserAccessBindingsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *OrganizationsGcpUserAccessBindingsCreateCall) Fields(s ...googleapi.Field) *OrganizationsGcpUserAccessBindingsCreateCall
func (c *OrganizationsGcpUserAccessBindingsCreateCall) Header() http.Header
type OrganizationsGcpUserAccessBindingsDeleteCall
func (c *OrganizationsGcpUserAccessBindingsDeleteCall) Context(ctx context.Context) *OrganizationsGcpUserAccessBindingsDeleteCall
func (c *OrganizationsGcpUserAccessBindingsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *OrganizationsGcpUserAccessBindingsDeleteCall) Fields(s ...googleapi.Field) *OrganizationsGcpUserAccessBindingsDeleteCall
func (c *OrganizationsGcpUserAccessBindingsDeleteCall) Header() http.Header
type OrganizationsGcpUserAccessBindingsGetCall
func (c *OrganizationsGcpUserAccessBindingsGetCall) Context(ctx context.Context) *OrganizationsGcpUserAccessBindingsGetCall
func (c *OrganizationsGcpUserAccessBindingsGetCall) Do(opts ...googleapi.CallOption) (*GcpUserAccessBinding, error)
func (c *OrganizationsGcpUserAccessBindingsGetCall) Fields(s ...googleapi.Field) *OrganizationsGcpUserAccessBindingsGetCall
func (c *OrganizationsGcpUserAccessBindingsGetCall) Header() http.Header
func (c *OrganizationsGcpUserAccessBindingsGetCall) IfNoneMatch(entityTag string) *OrganizationsGcpUserAccessBindingsGetCall
type OrganizationsGcpUserAccessBindingsListCall
func (c *OrganizationsGcpUserAccessBindingsListCall) Context(ctx context.Context) *OrganizationsGcpUserAccessBindingsListCall
func (c *OrganizationsGcpUserAccessBindingsListCall) Do(opts ...googleapi.CallOption) (*ListGcpUserAccessBindingsResponse, error)
func (c *OrganizationsGcpUserAccessBindingsListCall) Fields(s ...googleapi.Field) *OrganizationsGcpUserAccessBindingsListCall
func (c *OrganizationsGcpUserAccessBindingsListCall) Header() http.Header
func (c *OrganizationsGcpUserAccessBindingsListCall) IfNoneMatch(entityTag string) *OrganizationsGcpUserAccessBindingsListCall
func (c *OrganizationsGcpUserAccessBindingsListCall) PageSize(pageSize int64) *OrganizationsGcpUserAccessBindingsListCall
func (c *OrganizationsGcpUserAccessBindingsListCall) PageToken(pageToken string) *OrganizationsGcpUserAccessBindingsListCall
func (c *OrganizationsGcpUserAccessBindingsListCall) Pages(ctx context.Context, f func(*ListGcpUserAccessBindingsResponse) error) error
type OrganizationsGcpUserAccessBindingsPatchCall
func (c *OrganizationsGcpUserAccessBindingsPatchCall) Append(append bool) *OrganizationsGcpUserAccessBindingsPatchCall
func (c *OrganizationsGcpUserAccessBindingsPatchCall) Context(ctx context.Context) *OrganizationsGcpUserAccessBindingsPatchCall
func (c *OrganizationsGcpUserAccessBindingsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)
func (c *OrganizationsGcpUserAccessBindingsPatchCall) Fields(s ...googleapi.Field) *OrganizationsGcpUserAccessBindingsPatchCall
func (c *OrganizationsGcpUserAccessBindingsPatchCall) Header() http.Header
func (c *OrganizationsGcpUserAccessBindingsPatchCall) UpdateMask(updateMask string) *OrganizationsGcpUserAccessBindingsPatchCall
type OrganizationsGcpUserAccessBindingsService
func NewOrganizationsGcpUserAccessBindingsService(s *Service) *OrganizationsGcpUserAccessBindingsService
func (r *OrganizationsGcpUserAccessBindingsService) Create(parent string, gcpuseraccessbinding *GcpUserAccessBinding) *OrganizationsGcpUserAccessBindingsCreateCall
func (r *OrganizationsGcpUserAccessBindingsService) Delete(name string) *OrganizationsGcpUserAccessBindingsDeleteCall
func (r *OrganizationsGcpUserAccessBindingsService) Get(name string) *OrganizationsGcpUserAccessBindingsGetCall
func (r *OrganizationsGcpUserAccessBindingsService) List(parent string) *OrganizationsGcpUserAccessBindingsListCall
func (r *OrganizationsGcpUserAccessBindingsService) Patch(name string, gcpuseraccessbinding *GcpUserAccessBinding) *OrganizationsGcpUserAccessBindingsPatchCall
type OrganizationsService
func NewOrganizationsService(s *Service) *OrganizationsService
type OsConstraint
func (s OsConstraint) MarshalJSON() ([]byte, error)
type PermissionsListCall
func (c *PermissionsListCall) Context(ctx context.Context) *PermissionsListCall
func (c *PermissionsListCall) Do(opts ...googleapi.CallOption) (*ListSupportedPermissionsResponse, error)
func (c *PermissionsListCall) Fields(s ...googleapi.Field) *PermissionsListCall
func (c *PermissionsListCall) Header() http.Header
func (c *PermissionsListCall) IfNoneMatch(entityTag string) *PermissionsListCall
func (c *PermissionsListCall) PageSize(pageSize int64) *PermissionsListCall
func (c *PermissionsListCall) PageToken(pageToken string) *PermissionsListCall
func (c *PermissionsListCall) Pages(ctx context.Context, f func(*ListSupportedPermissionsResponse) error) error
type PermissionsService
func NewPermissionsService(s *Service) *PermissionsService
func (r *PermissionsService) List() *PermissionsListCall
type Policy
func (s Policy) MarshalJSON() ([]byte, error)
type ReplaceAccessLevelsRequest
func (s ReplaceAccessLevelsRequest) MarshalJSON() ([]byte, error)
type ReplaceAccessLevelsResponse
func (s ReplaceAccessLevelsResponse) MarshalJSON() ([]byte, error)
type ReplaceServicePerimetersRequest
func (s ReplaceServicePerimetersRequest) MarshalJSON() ([]byte, error)
type ReplaceServicePerimetersResponse
func (s ReplaceServicePerimetersResponse) MarshalJSON() ([]byte, error)
type ScopedAccessSettings
func (s ScopedAccessSettings) MarshalJSON() ([]byte, error)
type Service
func New(client *http.Client) (*Service, error)DEPRECATED
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)
type ServicePerimeter
func (s ServicePerimeter) MarshalJSON() ([]byte, error)
type ServicePerimeterConfig
func (s ServicePerimeterConfig) MarshalJSON() ([]byte, error)
type ServicesGetCall
func (c *ServicesGetCall) Context(ctx context.Context) *ServicesGetCall
func (c *ServicesGetCall) Do(opts ...googleapi.CallOption) (*SupportedService, error)
func (c *ServicesGetCall) Fields(s ...googleapi.Field) *ServicesGetCall
func (c *ServicesGetCall) Header() http.Header
func (c *ServicesGetCall) IfNoneMatch(entityTag string) *ServicesGetCall
type ServicesListCall
func (c *ServicesListCall) Context(ctx context.Context) *ServicesListCall
func (c *ServicesListCall) Do(opts ...googleapi.CallOption) (*ListSupportedServicesResponse, error)
func (c *ServicesListCall) Fields(s ...googleapi.Field) *ServicesListCall
func (c *ServicesListCall) Header() http.Header
func (c *ServicesListCall) IfNoneMatch(entityTag string) *ServicesListCall
func (c *ServicesListCall) PageSize(pageSize int64) *ServicesListCall
func (c *ServicesListCall) PageToken(pageToken string) *ServicesListCall
func (c *ServicesListCall) Pages(ctx context.Context, f func(*ListSupportedServicesResponse) error) error
type ServicesService
func NewServicesService(s *Service) *ServicesService
func (r *ServicesService) Get(name string) *ServicesGetCall
func (r *ServicesService) List() *ServicesListCall
type SessionSettings
func (s SessionSettings) MarshalJSON() ([]byte, error)
type SetIamPolicyRequest
func (s SetIamPolicyRequest) MarshalJSON() ([]byte, error)
type Status
func (s Status) MarshalJSON() ([]byte, error)
type SupportedService
func (s SupportedService) MarshalJSON() ([]byte, error)
type TestIamPermissionsRequest
func (s TestIamPermissionsRequest) MarshalJSON() ([]byte, error)
type TestIamPermissionsResponse
func (s TestIamPermissionsResponse) MarshalJSON() ([]byte, error)
type VpcAccessibleServices
func (s VpcAccessibleServices) MarshalJSON() ([]byte, error)
type VpcNetworkSource
func (s VpcNetworkSource) MarshalJSON() ([]byte, error)
type VpcSubNetwork
func (s VpcSubNetwork) MarshalJSON() ([]byte, error)
Constants ¶
View Source
const (
	// See, edit, configure, and delete your Google Cloud data and see the email
	// address for your Google Account.
	CloudPlatformScope = "https://www.googleapis.com/auth/cloud-platform"
)

OAuth2 scopes used by this API.

Variables ¶

This section is empty.

Functions ¶

This section is empty.

Types ¶
type AccessContextManagerOperationMetadata ¶
added in v0.53.0
type AccessContextManagerOperationMetadata struct {
}

AccessContextManagerOperationMetadata: Metadata of Access Context Manager's Long Running Operations.

type AccessLevel ¶
type AccessLevel struct {
	// Basic: A `BasicLevel` composed of `Conditions`.
	Basic *BasicLevel `json:"basic,omitempty"`
	// Custom: A `CustomLevel` written in the Common Expression Language.
	Custom *CustomLevel `json:"custom,omitempty"`
	// Description: Description of the `AccessLevel` and its use. Does not affect
	// behavior.
	Description string `json:"description,omitempty"`
	// Name: Identifier. Resource name for the `AccessLevel`. Format:
	// `accessPolicies/{access_policy}/accessLevels/{access_level}`. The
	// `access_level` component must begin with a letter, followed by alphanumeric
	// characters or `_`. Its maximum length is 50 characters. After you create an
	// `AccessLevel`, you cannot change its `name`.
	Name string `json:"name,omitempty"`
	// Title: Human readable title. Must be unique within the Policy.
	Title string `json:"title,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Basic") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Basic") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AccessLevel: An `AccessLevel` is a label that can be applied to requests to Google Cloud services, along with a list of requirements necessary for the label to be applied.

func (AccessLevel) MarshalJSON ¶
func (s AccessLevel) MarshalJSON() ([]byte, error)
type AccessPoliciesAccessLevelsCreateCall ¶
type AccessPoliciesAccessLevelsCreateCall struct {
	// contains filtered or unexported fields
}
func (*AccessPoliciesAccessLevelsCreateCall) Context ¶
func (c *AccessPoliciesAccessLevelsCreateCall) Context(ctx context.Context) *AccessPoliciesAccessLevelsCreateCall

Context sets the context to be used in this call's Do method.

func (*AccessPoliciesAccessLevelsCreateCall) Do ¶
func (c *AccessPoliciesAccessLevelsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "accesscontextmanager.accessPolicies.accessLevels.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccessPoliciesAccessLevelsCreateCall) Fields ¶
func (c *AccessPoliciesAccessLevelsCreateCall) Fields(s ...googleapi.Field) *AccessPoliciesAccessLevelsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccessPoliciesAccessLevelsCreateCall) Header ¶
func (c *AccessPoliciesAccessLevelsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccessPoliciesAccessLevelsDeleteCall ¶
type AccessPoliciesAccessLevelsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*AccessPoliciesAccessLevelsDeleteCall) Context ¶
func (c *AccessPoliciesAccessLevelsDeleteCall) Context(ctx context.Context) *AccessPoliciesAccessLevelsDeleteCall

Context sets the context to be used in this call's Do method.

func (*AccessPoliciesAccessLevelsDeleteCall) Do ¶
func (c *AccessPoliciesAccessLevelsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "accesscontextmanager.accessPolicies.accessLevels.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccessPoliciesAccessLevelsDeleteCall) Fields ¶
func (c *AccessPoliciesAccessLevelsDeleteCall) Fields(s ...googleapi.Field) *AccessPoliciesAccessLevelsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccessPoliciesAccessLevelsDeleteCall) Header ¶
func (c *AccessPoliciesAccessLevelsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccessPoliciesAccessLevelsGetCall ¶
type AccessPoliciesAccessLevelsGetCall struct {
	// contains filtered or unexported fields
}
func (*AccessPoliciesAccessLevelsGetCall) AccessLevelFormat ¶
func (c *AccessPoliciesAccessLevelsGetCall) AccessLevelFormat(accessLevelFormat string) *AccessPoliciesAccessLevelsGetCall

AccessLevelFormat sets the optional parameter "accessLevelFormat": Whether to return `BasicLevels` in the Cloud Common Expression Language rather than as `BasicLevels`. Defaults to AS_DEFINED, where Access Levels are returned as `BasicLevels` or `CustomLevels` based on how they were created. If set to CEL, all Access Levels are returned as `CustomLevels`. In the CEL case, `BasicLevels` are translated to equivalent `CustomLevels`.

Possible values:

"LEVEL_FORMAT_UNSPECIFIED" - The format was not specified.
"AS_DEFINED" - Uses the format the resource was defined in. BasicLevels


are returned as BasicLevels, CustomLevels are returned as CustomLevels.

"CEL" - Use Cloud Common Expression Language when returning the resource.


Both BasicLevels and CustomLevels are returned as CustomLevels.

func (*AccessPoliciesAccessLevelsGetCall) Context ¶
func (c *AccessPoliciesAccessLevelsGetCall) Context(ctx context.Context) *AccessPoliciesAccessLevelsGetCall

Context sets the context to be used in this call's Do method.

func (*AccessPoliciesAccessLevelsGetCall) Do ¶
func (c *AccessPoliciesAccessLevelsGetCall) Do(opts ...googleapi.CallOption) (*AccessLevel, error)

Do executes the "accesscontextmanager.accessPolicies.accessLevels.get" call. Any non-2xx status code is an error. Response headers are in either *AccessLevel.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccessPoliciesAccessLevelsGetCall) Fields ¶
func (c *AccessPoliciesAccessLevelsGetCall) Fields(s ...googleapi.Field) *AccessPoliciesAccessLevelsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccessPoliciesAccessLevelsGetCall) Header ¶
func (c *AccessPoliciesAccessLevelsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccessPoliciesAccessLevelsGetCall) IfNoneMatch ¶
func (c *AccessPoliciesAccessLevelsGetCall) IfNoneMatch(entityTag string) *AccessPoliciesAccessLevelsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AccessPoliciesAccessLevelsListCall ¶
type AccessPoliciesAccessLevelsListCall struct {
	// contains filtered or unexported fields
}
func (*AccessPoliciesAccessLevelsListCall) AccessLevelFormat ¶
func (c *AccessPoliciesAccessLevelsListCall) AccessLevelFormat(accessLevelFormat string) *AccessPoliciesAccessLevelsListCall

AccessLevelFormat sets the optional parameter "accessLevelFormat": Whether to return `BasicLevels` in the Cloud Common Expression language, as `CustomLevels`, rather than as `BasicLevels`. Defaults to returning `AccessLevels` in the format they were defined.

Possible values:

"LEVEL_FORMAT_UNSPECIFIED" - The format was not specified.
"AS_DEFINED" - Uses the format the resource was defined in. BasicLevels


are returned as BasicLevels, CustomLevels are returned as CustomLevels.

"CEL" - Use Cloud Common Expression Language when returning the resource.


Both BasicLevels and CustomLevels are returned as CustomLevels.

func (*AccessPoliciesAccessLevelsListCall) Context ¶
func (c *AccessPoliciesAccessLevelsListCall) Context(ctx context.Context) *AccessPoliciesAccessLevelsListCall

Context sets the context to be used in this call's Do method.

func (*AccessPoliciesAccessLevelsListCall) Do ¶
func (c *AccessPoliciesAccessLevelsListCall) Do(opts ...googleapi.CallOption) (*ListAccessLevelsResponse, error)

Do executes the "accesscontextmanager.accessPolicies.accessLevels.list" call. Any non-2xx status code is an error. Response headers are in either *ListAccessLevelsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccessPoliciesAccessLevelsListCall) Fields ¶
func (c *AccessPoliciesAccessLevelsListCall) Fields(s ...googleapi.Field) *AccessPoliciesAccessLevelsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccessPoliciesAccessLevelsListCall) Header ¶
func (c *AccessPoliciesAccessLevelsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccessPoliciesAccessLevelsListCall) IfNoneMatch ¶
func (c *AccessPoliciesAccessLevelsListCall) IfNoneMatch(entityTag string) *AccessPoliciesAccessLevelsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*AccessPoliciesAccessLevelsListCall) PageSize ¶
func (c *AccessPoliciesAccessLevelsListCall) PageSize(pageSize int64) *AccessPoliciesAccessLevelsListCall

PageSize sets the optional parameter "pageSize": Number of Access Levels to include in the list. Default 100.

func (*AccessPoliciesAccessLevelsListCall) PageToken ¶
func (c *AccessPoliciesAccessLevelsListCall) PageToken(pageToken string) *AccessPoliciesAccessLevelsListCall

PageToken sets the optional parameter "pageToken": Next page token for the next batch of Access Level instances. Defaults to the first page of results.

func (*AccessPoliciesAccessLevelsListCall) Pages ¶
func (c *AccessPoliciesAccessLevelsListCall) Pages(ctx context.Context, f func(*ListAccessLevelsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccessPoliciesAccessLevelsPatchCall ¶
type AccessPoliciesAccessLevelsPatchCall struct {
	// contains filtered or unexported fields
}
func (*AccessPoliciesAccessLevelsPatchCall) Context ¶
func (c *AccessPoliciesAccessLevelsPatchCall) Context(ctx context.Context) *AccessPoliciesAccessLevelsPatchCall

Context sets the context to be used in this call's Do method.

func (*AccessPoliciesAccessLevelsPatchCall) Do ¶
func (c *AccessPoliciesAccessLevelsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "accesscontextmanager.accessPolicies.accessLevels.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccessPoliciesAccessLevelsPatchCall) Fields ¶
func (c *AccessPoliciesAccessLevelsPatchCall) Fields(s ...googleapi.Field) *AccessPoliciesAccessLevelsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccessPoliciesAccessLevelsPatchCall) Header ¶
func (c *AccessPoliciesAccessLevelsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccessPoliciesAccessLevelsPatchCall) UpdateMask ¶
func (c *AccessPoliciesAccessLevelsPatchCall) UpdateMask(updateMask string) *AccessPoliciesAccessLevelsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. Mask to control which fields get updated. Must be non-empty.

type AccessPoliciesAccessLevelsReplaceAllCall ¶
added in v0.18.0
type AccessPoliciesAccessLevelsReplaceAllCall struct {
	// contains filtered or unexported fields
}
func (*AccessPoliciesAccessLevelsReplaceAllCall) Context ¶
added in v0.18.0
func (c *AccessPoliciesAccessLevelsReplaceAllCall) Context(ctx context.Context) *AccessPoliciesAccessLevelsReplaceAllCall

Context sets the context to be used in this call's Do method.

func (*AccessPoliciesAccessLevelsReplaceAllCall) Do ¶
added in v0.18.0
func (c *AccessPoliciesAccessLevelsReplaceAllCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "accesscontextmanager.accessPolicies.accessLevels.replaceAll" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccessPoliciesAccessLevelsReplaceAllCall) Fields ¶
added in v0.18.0
func (c *AccessPoliciesAccessLevelsReplaceAllCall) Fields(s ...googleapi.Field) *AccessPoliciesAccessLevelsReplaceAllCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccessPoliciesAccessLevelsReplaceAllCall) Header ¶
added in v0.18.0
func (c *AccessPoliciesAccessLevelsReplaceAllCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccessPoliciesAccessLevelsService ¶
type AccessPoliciesAccessLevelsService struct {
	// contains filtered or unexported fields
}
func NewAccessPoliciesAccessLevelsService ¶
func NewAccessPoliciesAccessLevelsService(s *Service) *AccessPoliciesAccessLevelsService
func (*AccessPoliciesAccessLevelsService) Create ¶
func (r *AccessPoliciesAccessLevelsService) Create(parent string, accesslevel *AccessLevel) *AccessPoliciesAccessLevelsCreateCall

Create: Creates an access level. The long-running operation from this RPC has a successful status after the access level propagates to long-lasting storage. If access levels contain errors, an error response is returned for the first error encountered.

parent: Resource name for the access policy which owns this Access Level. Format: `accessPolicies/{policy_id}`.
func (*AccessPoliciesAccessLevelsService) Delete ¶
func (r *AccessPoliciesAccessLevelsService) Delete(name string) *AccessPoliciesAccessLevelsDeleteCall

Delete: Deletes an access level based on the resource name. The long-running operation from this RPC has a successful status after the access level has been removed from long-lasting storage.

name: Resource name for the Access Level. Format: `accessPolicies/{policy_id}/accessLevels/{access_level_id}`.
func (*AccessPoliciesAccessLevelsService) Get ¶
func (r *AccessPoliciesAccessLevelsService) Get(name string) *AccessPoliciesAccessLevelsGetCall

Get: Gets an access level based on the resource name.

name: Resource name for the Access Level. Format: `accessPolicies/{policy_id}/accessLevels/{access_level_id}`.
func (*AccessPoliciesAccessLevelsService) List ¶
func (r *AccessPoliciesAccessLevelsService) List(parent string) *AccessPoliciesAccessLevelsListCall

List: Lists all access levels for an access policy.

parent: Resource name for the access policy to list Access Levels from. Format: `accessPolicies/{policy_id}`.
func (*AccessPoliciesAccessLevelsService) Patch ¶
func (r *AccessPoliciesAccessLevelsService) Patch(name string, accesslevel *AccessLevel) *AccessPoliciesAccessLevelsPatchCall

Patch: Updates an access level. The long-running operation from this RPC has a successful status after the changes to the access level propagate to long-lasting storage. If access levels contain errors, an error response is returned for the first error encountered.

name: Identifier. Resource name for the `AccessLevel`. Format: `accessPolicies/{access_policy}/accessLevels/{access_level}`. The `access_level` component must begin with a letter, followed by alphanumeric characters or `_`. Its maximum length is 50 characters. After you create an `AccessLevel`, you cannot change its `name`.
func (*AccessPoliciesAccessLevelsService) ReplaceAll ¶
added in v0.18.0
func (r *AccessPoliciesAccessLevelsService) ReplaceAll(parent string, replaceaccesslevelsrequest *ReplaceAccessLevelsRequest) *AccessPoliciesAccessLevelsReplaceAllCall

ReplaceAll: Replaces all existing access levels in an access policy with the access levels provided. This is done atomically. The long-running operation from this RPC has a successful status after all replacements propagate to long-lasting storage. If the replacement contains errors, an error response is returned for the first error encountered. Upon error, the replacement is cancelled, and existing access levels are not affected. The Operation.response field contains ReplaceAccessLevelsResponse. Removing access levels contained in existing service perimeters result in an error.

parent: Resource name for the access policy which owns these Access Levels. Format: `accessPolicies/{policy_id}`.
func (*AccessPoliciesAccessLevelsService) TestIamPermissions ¶
added in v0.63.0
func (r *AccessPoliciesAccessLevelsService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *AccessPoliciesAccessLevelsTestIamPermissionsCall

TestIamPermissions: Returns the IAM permissions that the caller has on the specified Access Context Manager resource. The resource can be an AccessPolicy, AccessLevel, or ServicePerimeter. This method does not support other resources.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type AccessPoliciesAccessLevelsTestIamPermissionsCall ¶
added in v0.63.0
type AccessPoliciesAccessLevelsTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*AccessPoliciesAccessLevelsTestIamPermissionsCall) Context ¶
added in v0.63.0
func (c *AccessPoliciesAccessLevelsTestIamPermissionsCall) Context(ctx context.Context) *AccessPoliciesAccessLevelsTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*AccessPoliciesAccessLevelsTestIamPermissionsCall) Do ¶
added in v0.63.0
func (c *AccessPoliciesAccessLevelsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)

Do executes the "accesscontextmanager.accessPolicies.accessLevels.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccessPoliciesAccessLevelsTestIamPermissionsCall) Fields ¶
added in v0.63.0
func (c *AccessPoliciesAccessLevelsTestIamPermissionsCall) Fields(s ...googleapi.Field) *AccessPoliciesAccessLevelsTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccessPoliciesAccessLevelsTestIamPermissionsCall) Header ¶
added in v0.63.0
func (c *AccessPoliciesAccessLevelsTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccessPoliciesAuthorizedOrgsDescsCreateCall ¶
added in v0.106.0
type AccessPoliciesAuthorizedOrgsDescsCreateCall struct {
	// contains filtered or unexported fields
}
func (*AccessPoliciesAuthorizedOrgsDescsCreateCall) Context ¶
added in v0.106.0
func (c *AccessPoliciesAuthorizedOrgsDescsCreateCall) Context(ctx context.Context) *AccessPoliciesAuthorizedOrgsDescsCreateCall

Context sets the context to be used in this call's Do method.

func (*AccessPoliciesAuthorizedOrgsDescsCreateCall) Do ¶
added in v0.106.0
func (c *AccessPoliciesAuthorizedOrgsDescsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "accesscontextmanager.accessPolicies.authorizedOrgsDescs.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccessPoliciesAuthorizedOrgsDescsCreateCall) Fields ¶
added in v0.106.0
func (c *AccessPoliciesAuthorizedOrgsDescsCreateCall) Fields(s ...googleapi.Field) *AccessPoliciesAuthorizedOrgsDescsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccessPoliciesAuthorizedOrgsDescsCreateCall) Header ¶
added in v0.106.0
func (c *AccessPoliciesAuthorizedOrgsDescsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccessPoliciesAuthorizedOrgsDescsDeleteCall ¶
added in v0.106.0
type AccessPoliciesAuthorizedOrgsDescsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*AccessPoliciesAuthorizedOrgsDescsDeleteCall) Context ¶
added in v0.106.0
func (c *AccessPoliciesAuthorizedOrgsDescsDeleteCall) Context(ctx context.Context) *AccessPoliciesAuthorizedOrgsDescsDeleteCall

Context sets the context to be used in this call's Do method.

func (*AccessPoliciesAuthorizedOrgsDescsDeleteCall) Do ¶
added in v0.106.0
func (c *AccessPoliciesAuthorizedOrgsDescsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "accesscontextmanager.accessPolicies.authorizedOrgsDescs.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccessPoliciesAuthorizedOrgsDescsDeleteCall) Fields ¶
added in v0.106.0
func (c *AccessPoliciesAuthorizedOrgsDescsDeleteCall) Fields(s ...googleapi.Field) *AccessPoliciesAuthorizedOrgsDescsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccessPoliciesAuthorizedOrgsDescsDeleteCall) Header ¶
added in v0.106.0
func (c *AccessPoliciesAuthorizedOrgsDescsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccessPoliciesAuthorizedOrgsDescsGetCall ¶
added in v0.106.0
type AccessPoliciesAuthorizedOrgsDescsGetCall struct {
	// contains filtered or unexported fields
}
func (*AccessPoliciesAuthorizedOrgsDescsGetCall) Context ¶
added in v0.106.0
func (c *AccessPoliciesAuthorizedOrgsDescsGetCall) Context(ctx context.Context) *AccessPoliciesAuthorizedOrgsDescsGetCall

Context sets the context to be used in this call's Do method.

func (*AccessPoliciesAuthorizedOrgsDescsGetCall) Do ¶
added in v0.106.0
func (c *AccessPoliciesAuthorizedOrgsDescsGetCall) Do(opts ...googleapi.CallOption) (*AuthorizedOrgsDesc, error)

Do executes the "accesscontextmanager.accessPolicies.authorizedOrgsDescs.get" call. Any non-2xx status code is an error. Response headers are in either *AuthorizedOrgsDesc.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccessPoliciesAuthorizedOrgsDescsGetCall) Fields ¶
added in v0.106.0
func (c *AccessPoliciesAuthorizedOrgsDescsGetCall) Fields(s ...googleapi.Field) *AccessPoliciesAuthorizedOrgsDescsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccessPoliciesAuthorizedOrgsDescsGetCall) Header ¶
added in v0.106.0
func (c *AccessPoliciesAuthorizedOrgsDescsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccessPoliciesAuthorizedOrgsDescsGetCall) IfNoneMatch ¶
added in v0.106.0
func (c *AccessPoliciesAuthorizedOrgsDescsGetCall) IfNoneMatch(entityTag string) *AccessPoliciesAuthorizedOrgsDescsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AccessPoliciesAuthorizedOrgsDescsListCall ¶
added in v0.106.0
type AccessPoliciesAuthorizedOrgsDescsListCall struct {
	// contains filtered or unexported fields
}
func (*AccessPoliciesAuthorizedOrgsDescsListCall) Context ¶
added in v0.106.0
func (c *AccessPoliciesAuthorizedOrgsDescsListCall) Context(ctx context.Context) *AccessPoliciesAuthorizedOrgsDescsListCall

Context sets the context to be used in this call's Do method.

func (*AccessPoliciesAuthorizedOrgsDescsListCall) Do ¶
added in v0.106.0
func (c *AccessPoliciesAuthorizedOrgsDescsListCall) Do(opts ...googleapi.CallOption) (*ListAuthorizedOrgsDescsResponse, error)

Do executes the "accesscontextmanager.accessPolicies.authorizedOrgsDescs.list" call. Any non-2xx status code is an error. Response headers are in either *ListAuthorizedOrgsDescsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccessPoliciesAuthorizedOrgsDescsListCall) Fields ¶
added in v0.106.0
func (c *AccessPoliciesAuthorizedOrgsDescsListCall) Fields(s ...googleapi.Field) *AccessPoliciesAuthorizedOrgsDescsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccessPoliciesAuthorizedOrgsDescsListCall) Header ¶
added in v0.106.0
func (c *AccessPoliciesAuthorizedOrgsDescsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccessPoliciesAuthorizedOrgsDescsListCall) IfNoneMatch ¶
added in v0.106.0
func (c *AccessPoliciesAuthorizedOrgsDescsListCall) IfNoneMatch(entityTag string) *AccessPoliciesAuthorizedOrgsDescsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*AccessPoliciesAuthorizedOrgsDescsListCall) PageSize ¶
added in v0.106.0
func (c *AccessPoliciesAuthorizedOrgsDescsListCall) PageSize(pageSize int64) *AccessPoliciesAuthorizedOrgsDescsListCall

PageSize sets the optional parameter "pageSize": Number of Authorized Orgs Descs to include in the list. Default 100.

func (*AccessPoliciesAuthorizedOrgsDescsListCall) PageToken ¶
added in v0.106.0
func (c *AccessPoliciesAuthorizedOrgsDescsListCall) PageToken(pageToken string) *AccessPoliciesAuthorizedOrgsDescsListCall

PageToken sets the optional parameter "pageToken": Next page token for the next batch of Authorized Orgs Desc instances. Defaults to the first page of results.

func (*AccessPoliciesAuthorizedOrgsDescsListCall) Pages ¶
added in v0.106.0
func (c *AccessPoliciesAuthorizedOrgsDescsListCall) Pages(ctx context.Context, f func(*ListAuthorizedOrgsDescsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccessPoliciesAuthorizedOrgsDescsPatchCall ¶
added in v0.106.0
type AccessPoliciesAuthorizedOrgsDescsPatchCall struct {
	// contains filtered or unexported fields
}
func (*AccessPoliciesAuthorizedOrgsDescsPatchCall) Context ¶
added in v0.106.0
func (c *AccessPoliciesAuthorizedOrgsDescsPatchCall) Context(ctx context.Context) *AccessPoliciesAuthorizedOrgsDescsPatchCall

Context sets the context to be used in this call's Do method.

func (*AccessPoliciesAuthorizedOrgsDescsPatchCall) Do ¶
added in v0.106.0
func (c *AccessPoliciesAuthorizedOrgsDescsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "accesscontextmanager.accessPolicies.authorizedOrgsDescs.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccessPoliciesAuthorizedOrgsDescsPatchCall) Fields ¶
added in v0.106.0
func (c *AccessPoliciesAuthorizedOrgsDescsPatchCall) Fields(s ...googleapi.Field) *AccessPoliciesAuthorizedOrgsDescsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccessPoliciesAuthorizedOrgsDescsPatchCall) Header ¶
added in v0.106.0
func (c *AccessPoliciesAuthorizedOrgsDescsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccessPoliciesAuthorizedOrgsDescsPatchCall) UpdateMask ¶
added in v0.106.0
func (c *AccessPoliciesAuthorizedOrgsDescsPatchCall) UpdateMask(updateMask string) *AccessPoliciesAuthorizedOrgsDescsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. Mask to control which fields get updated. Must be non-empty.

type AccessPoliciesAuthorizedOrgsDescsService ¶
added in v0.106.0
type AccessPoliciesAuthorizedOrgsDescsService struct {
	// contains filtered or unexported fields
}
func NewAccessPoliciesAuthorizedOrgsDescsService ¶
added in v0.106.0
func NewAccessPoliciesAuthorizedOrgsDescsService(s *Service) *AccessPoliciesAuthorizedOrgsDescsService
func (*AccessPoliciesAuthorizedOrgsDescsService) Create ¶
added in v0.106.0
func (r *AccessPoliciesAuthorizedOrgsDescsService) Create(parent string, authorizedorgsdesc *AuthorizedOrgsDesc) *AccessPoliciesAuthorizedOrgsDescsCreateCall

Create: Creates an authorized orgs desc. The long-running operation from this RPC has a successful status after the authorized orgs desc propagates to long-lasting storage. If a authorized orgs desc contains errors, an error response is returned for the first error encountered. The name of this `AuthorizedOrgsDesc` will be assigned during creation.

parent: Resource name for the access policy which owns this Authorized Orgs Desc. Format: `accessPolicies/{policy_id}`.
func (*AccessPoliciesAuthorizedOrgsDescsService) Delete ¶
added in v0.106.0
func (r *AccessPoliciesAuthorizedOrgsDescsService) Delete(name string) *AccessPoliciesAuthorizedOrgsDescsDeleteCall

Delete: Deletes an authorized orgs desc based on the resource name. The long-running operation from this RPC has a successful status after the authorized orgs desc is removed from long-lasting storage.

name: Resource name for the Authorized Orgs Desc. Format: `accessPolicies/{policy_id}/authorizedOrgsDesc/{authorized_orgs_desc_id}`.
func (*AccessPoliciesAuthorizedOrgsDescsService) Get ¶
added in v0.106.0
func (r *AccessPoliciesAuthorizedOrgsDescsService) Get(name string) *AccessPoliciesAuthorizedOrgsDescsGetCall

Get: Gets an authorized orgs desc based on the resource name.

name: Resource name for the Authorized Orgs Desc. Format: `accessPolicies/{policy_id}/authorizedOrgsDescs/{authorized_orgs_descs_id}`.
func (*AccessPoliciesAuthorizedOrgsDescsService) List ¶
added in v0.106.0
func (r *AccessPoliciesAuthorizedOrgsDescsService) List(parent string) *AccessPoliciesAuthorizedOrgsDescsListCall

List: Lists all authorized orgs descs for an access policy.

parent: Resource name for the access policy to list Authorized Orgs Desc from. Format: `accessPolicies/{policy_id}`.
func (*AccessPoliciesAuthorizedOrgsDescsService) Patch ¶
added in v0.106.0
func (r *AccessPoliciesAuthorizedOrgsDescsService) Patch(name string, authorizedorgsdesc *AuthorizedOrgsDesc) *AccessPoliciesAuthorizedOrgsDescsPatchCall

Patch: Updates an authorized orgs desc. The long-running operation from this RPC has a successful status after the authorized orgs desc propagates to long-lasting storage. If a authorized orgs desc contains errors, an error response is returned for the first error encountered. Only the organization list in `AuthorizedOrgsDesc` can be updated. The name, authorization_type, asset_type and authorization_direction cannot be updated.

name: Identifier. Resource name for the `AuthorizedOrgsDesc`. Format: `accessPolicies/{access_policy}/authorizedOrgsDescs/{authorized_orgs_desc}` . The `authorized_orgs_desc` component must begin with a letter, followed by alphanumeric characters or `_`. After you create an `AuthorizedOrgsDesc`, you cannot change its `name`.
type AccessPoliciesCreateCall ¶
type AccessPoliciesCreateCall struct {
	// contains filtered or unexported fields
}
func (*AccessPoliciesCreateCall) Context ¶
func (c *AccessPoliciesCreateCall) Context(ctx context.Context) *AccessPoliciesCreateCall

Context sets the context to be used in this call's Do method.

func (*AccessPoliciesCreateCall) Do ¶
func (c *AccessPoliciesCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "accesscontextmanager.accessPolicies.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccessPoliciesCreateCall) Fields ¶
func (c *AccessPoliciesCreateCall) Fields(s ...googleapi.Field) *AccessPoliciesCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccessPoliciesCreateCall) Header ¶
func (c *AccessPoliciesCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccessPoliciesDeleteCall ¶
type AccessPoliciesDeleteCall struct {
	// contains filtered or unexported fields
}
func (*AccessPoliciesDeleteCall) Context ¶
func (c *AccessPoliciesDeleteCall) Context(ctx context.Context) *AccessPoliciesDeleteCall

Context sets the context to be used in this call's Do method.

func (*AccessPoliciesDeleteCall) Do ¶
func (c *AccessPoliciesDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "accesscontextmanager.accessPolicies.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccessPoliciesDeleteCall) Fields ¶
func (c *AccessPoliciesDeleteCall) Fields(s ...googleapi.Field) *AccessPoliciesDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccessPoliciesDeleteCall) Header ¶
func (c *AccessPoliciesDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccessPoliciesGetCall ¶
type AccessPoliciesGetCall struct {
	// contains filtered or unexported fields
}
func (*AccessPoliciesGetCall) Context ¶
func (c *AccessPoliciesGetCall) Context(ctx context.Context) *AccessPoliciesGetCall

Context sets the context to be used in this call's Do method.

func (*AccessPoliciesGetCall) Do ¶
func (c *AccessPoliciesGetCall) Do(opts ...googleapi.CallOption) (*AccessPolicy, error)

Do executes the "accesscontextmanager.accessPolicies.get" call. Any non-2xx status code is an error. Response headers are in either *AccessPolicy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccessPoliciesGetCall) Fields ¶
func (c *AccessPoliciesGetCall) Fields(s ...googleapi.Field) *AccessPoliciesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccessPoliciesGetCall) Header ¶
func (c *AccessPoliciesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccessPoliciesGetCall) IfNoneMatch ¶
func (c *AccessPoliciesGetCall) IfNoneMatch(entityTag string) *AccessPoliciesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AccessPoliciesGetIamPolicyCall ¶
added in v0.63.0
type AccessPoliciesGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*AccessPoliciesGetIamPolicyCall) Context ¶
added in v0.63.0
func (c *AccessPoliciesGetIamPolicyCall) Context(ctx context.Context) *AccessPoliciesGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*AccessPoliciesGetIamPolicyCall) Do ¶
added in v0.63.0
func (c *AccessPoliciesGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "accesscontextmanager.accessPolicies.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccessPoliciesGetIamPolicyCall) Fields ¶
added in v0.63.0
func (c *AccessPoliciesGetIamPolicyCall) Fields(s ...googleapi.Field) *AccessPoliciesGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccessPoliciesGetIamPolicyCall) Header ¶
added in v0.63.0
func (c *AccessPoliciesGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccessPoliciesListCall ¶
type AccessPoliciesListCall struct {
	// contains filtered or unexported fields
}
func (*AccessPoliciesListCall) Context ¶
func (c *AccessPoliciesListCall) Context(ctx context.Context) *AccessPoliciesListCall

Context sets the context to be used in this call's Do method.

func (*AccessPoliciesListCall) Do ¶
func (c *AccessPoliciesListCall) Do(opts ...googleapi.CallOption) (*ListAccessPoliciesResponse, error)

Do executes the "accesscontextmanager.accessPolicies.list" call. Any non-2xx status code is an error. Response headers are in either *ListAccessPoliciesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccessPoliciesListCall) Fields ¶
func (c *AccessPoliciesListCall) Fields(s ...googleapi.Field) *AccessPoliciesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccessPoliciesListCall) Header ¶
func (c *AccessPoliciesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccessPoliciesListCall) IfNoneMatch ¶
func (c *AccessPoliciesListCall) IfNoneMatch(entityTag string) *AccessPoliciesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*AccessPoliciesListCall) PageSize ¶
func (c *AccessPoliciesListCall) PageSize(pageSize int64) *AccessPoliciesListCall

PageSize sets the optional parameter "pageSize": Number of AccessPolicy instances to include in the list. Default 100.

func (*AccessPoliciesListCall) PageToken ¶
func (c *AccessPoliciesListCall) PageToken(pageToken string) *AccessPoliciesListCall

PageToken sets the optional parameter "pageToken": Next page token for the next batch of AccessPolicy instances. Defaults to the first page of results.

func (*AccessPoliciesListCall) Pages ¶
func (c *AccessPoliciesListCall) Pages(ctx context.Context, f func(*ListAccessPoliciesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*AccessPoliciesListCall) Parent ¶
func (c *AccessPoliciesListCall) Parent(parent string) *AccessPoliciesListCall

Parent sets the optional parameter "parent": Required. Resource name for the container to list AccessPolicy instances from. Format: `organizations/{org_id}`

type AccessPoliciesPatchCall ¶
type AccessPoliciesPatchCall struct {
	// contains filtered or unexported fields
}
func (*AccessPoliciesPatchCall) Context ¶
func (c *AccessPoliciesPatchCall) Context(ctx context.Context) *AccessPoliciesPatchCall

Context sets the context to be used in this call's Do method.

func (*AccessPoliciesPatchCall) Do ¶
func (c *AccessPoliciesPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "accesscontextmanager.accessPolicies.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccessPoliciesPatchCall) Fields ¶
func (c *AccessPoliciesPatchCall) Fields(s ...googleapi.Field) *AccessPoliciesPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccessPoliciesPatchCall) Header ¶
func (c *AccessPoliciesPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccessPoliciesPatchCall) UpdateMask ¶
func (c *AccessPoliciesPatchCall) UpdateMask(updateMask string) *AccessPoliciesPatchCall

UpdateMask sets the optional parameter "updateMask": Required. Mask to control which fields get updated. Must be non-empty.

type AccessPoliciesService ¶
type AccessPoliciesService struct {
	AccessLevels *AccessPoliciesAccessLevelsService

	AuthorizedOrgsDescs *AccessPoliciesAuthorizedOrgsDescsService

	ServicePerimeters *AccessPoliciesServicePerimetersService
	// contains filtered or unexported fields
}
func NewAccessPoliciesService ¶
func NewAccessPoliciesService(s *Service) *AccessPoliciesService
func (*AccessPoliciesService) Create ¶
func (r *AccessPoliciesService) Create(accesspolicy *AccessPolicy) *AccessPoliciesCreateCall

Create: Creates an access policy. This method fails if the organization already has an access policy. The long-running operation has a successful status after the access policy propagates to long-lasting storage. Syntactic and basic semantic errors are returned in `metadata` as a BadRequest proto.

func (*AccessPoliciesService) Delete ¶
func (r *AccessPoliciesService) Delete(name string) *AccessPoliciesDeleteCall

Delete: Deletes an access policy based on the resource name. The long-running operation has a successful status after the access policy is removed from long-lasting storage.

name: Resource name for the access policy to delete. Format `accessPolicies/{policy_id}`.
func (*AccessPoliciesService) Get ¶
func (r *AccessPoliciesService) Get(name string) *AccessPoliciesGetCall

Get: Returns an access policy based on the name.

name: Resource name for the access policy to get. Format `accessPolicies/{policy_id}`.
func (*AccessPoliciesService) GetIamPolicy ¶
added in v0.63.0
func (r *AccessPoliciesService) GetIamPolicy(resource string, getiampolicyrequest *GetIamPolicyRequest) *AccessPoliciesGetIamPolicyCall

GetIamPolicy: Gets the IAM policy for the specified Access Context Manager access policy.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*AccessPoliciesService) List ¶
func (r *AccessPoliciesService) List() *AccessPoliciesListCall

List: Lists all access policies in an organization.

func (*AccessPoliciesService) Patch ¶
func (r *AccessPoliciesService) Patch(name string, accesspolicy *AccessPolicy) *AccessPoliciesPatchCall

Patch: Updates an access policy. The long-running operation from this RPC has a successful status after the changes to the access policy propagate to long-lasting storage.

name: Output only. Identifier. Resource name of the `AccessPolicy`. Format: `accessPolicies/{access_policy}`.
func (*AccessPoliciesService) SetIamPolicy ¶
added in v0.63.0
func (r *AccessPoliciesService) SetIamPolicy(resource string, setiampolicyrequest *SetIamPolicyRequest) *AccessPoliciesSetIamPolicyCall

SetIamPolicy: Sets the IAM policy for the specified Access Context Manager access policy. This method replaces the existing IAM policy on the access policy. The IAM policy controls the set of users who can perform specific operations on the Access Context Manager access policy.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*AccessPoliciesService) TestIamPermissions ¶
added in v0.63.0
func (r *AccessPoliciesService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *AccessPoliciesTestIamPermissionsCall

TestIamPermissions: Returns the IAM permissions that the caller has on the specified Access Context Manager resource. The resource can be an AccessPolicy, AccessLevel, or ServicePerimeter. This method does not support other resources.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type AccessPoliciesServicePerimetersCommitCall ¶
added in v0.18.0
type AccessPoliciesServicePerimetersCommitCall struct {
	// contains filtered or unexported fields
}
func (*AccessPoliciesServicePerimetersCommitCall) Context ¶
added in v0.18.0
func (c *AccessPoliciesServicePerimetersCommitCall) Context(ctx context.Context) *AccessPoliciesServicePerimetersCommitCall

Context sets the context to be used in this call's Do method.

func (*AccessPoliciesServicePerimetersCommitCall) Do ¶
added in v0.18.0
func (c *AccessPoliciesServicePerimetersCommitCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "accesscontextmanager.accessPolicies.servicePerimeters.commit" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccessPoliciesServicePerimetersCommitCall) Fields ¶
added in v0.18.0
func (c *AccessPoliciesServicePerimetersCommitCall) Fields(s ...googleapi.Field) *AccessPoliciesServicePerimetersCommitCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccessPoliciesServicePerimetersCommitCall) Header ¶
added in v0.18.0
func (c *AccessPoliciesServicePerimetersCommitCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccessPoliciesServicePerimetersCreateCall ¶
type AccessPoliciesServicePerimetersCreateCall struct {
	// contains filtered or unexported fields
}
func (*AccessPoliciesServicePerimetersCreateCall) Context ¶
func (c *AccessPoliciesServicePerimetersCreateCall) Context(ctx context.Context) *AccessPoliciesServicePerimetersCreateCall

Context sets the context to be used in this call's Do method.

func (*AccessPoliciesServicePerimetersCreateCall) Do ¶
func (c *AccessPoliciesServicePerimetersCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "accesscontextmanager.accessPolicies.servicePerimeters.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccessPoliciesServicePerimetersCreateCall) Fields ¶
func (c *AccessPoliciesServicePerimetersCreateCall) Fields(s ...googleapi.Field) *AccessPoliciesServicePerimetersCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccessPoliciesServicePerimetersCreateCall) Header ¶
func (c *AccessPoliciesServicePerimetersCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccessPoliciesServicePerimetersDeleteCall ¶
type AccessPoliciesServicePerimetersDeleteCall struct {
	// contains filtered or unexported fields
}
func (*AccessPoliciesServicePerimetersDeleteCall) Context ¶
func (c *AccessPoliciesServicePerimetersDeleteCall) Context(ctx context.Context) *AccessPoliciesServicePerimetersDeleteCall

Context sets the context to be used in this call's Do method.

func (*AccessPoliciesServicePerimetersDeleteCall) Do ¶
func (c *AccessPoliciesServicePerimetersDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "accesscontextmanager.accessPolicies.servicePerimeters.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccessPoliciesServicePerimetersDeleteCall) Fields ¶
func (c *AccessPoliciesServicePerimetersDeleteCall) Fields(s ...googleapi.Field) *AccessPoliciesServicePerimetersDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccessPoliciesServicePerimetersDeleteCall) Header ¶
func (c *AccessPoliciesServicePerimetersDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccessPoliciesServicePerimetersGetCall ¶
type AccessPoliciesServicePerimetersGetCall struct {
	// contains filtered or unexported fields
}
func (*AccessPoliciesServicePerimetersGetCall) Context ¶
func (c *AccessPoliciesServicePerimetersGetCall) Context(ctx context.Context) *AccessPoliciesServicePerimetersGetCall

Context sets the context to be used in this call's Do method.

func (*AccessPoliciesServicePerimetersGetCall) Do ¶
func (c *AccessPoliciesServicePerimetersGetCall) Do(opts ...googleapi.CallOption) (*ServicePerimeter, error)

Do executes the "accesscontextmanager.accessPolicies.servicePerimeters.get" call. Any non-2xx status code is an error. Response headers are in either *ServicePerimeter.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccessPoliciesServicePerimetersGetCall) Fields ¶
func (c *AccessPoliciesServicePerimetersGetCall) Fields(s ...googleapi.Field) *AccessPoliciesServicePerimetersGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccessPoliciesServicePerimetersGetCall) Header ¶
func (c *AccessPoliciesServicePerimetersGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccessPoliciesServicePerimetersGetCall) IfNoneMatch ¶
func (c *AccessPoliciesServicePerimetersGetCall) IfNoneMatch(entityTag string) *AccessPoliciesServicePerimetersGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type AccessPoliciesServicePerimetersListCall ¶
type AccessPoliciesServicePerimetersListCall struct {
	// contains filtered or unexported fields
}
func (*AccessPoliciesServicePerimetersListCall) Context ¶
func (c *AccessPoliciesServicePerimetersListCall) Context(ctx context.Context) *AccessPoliciesServicePerimetersListCall

Context sets the context to be used in this call's Do method.

func (*AccessPoliciesServicePerimetersListCall) Do ¶
func (c *AccessPoliciesServicePerimetersListCall) Do(opts ...googleapi.CallOption) (*ListServicePerimetersResponse, error)

Do executes the "accesscontextmanager.accessPolicies.servicePerimeters.list" call. Any non-2xx status code is an error. Response headers are in either *ListServicePerimetersResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccessPoliciesServicePerimetersListCall) Fields ¶
func (c *AccessPoliciesServicePerimetersListCall) Fields(s ...googleapi.Field) *AccessPoliciesServicePerimetersListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccessPoliciesServicePerimetersListCall) Header ¶
func (c *AccessPoliciesServicePerimetersListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccessPoliciesServicePerimetersListCall) IfNoneMatch ¶
func (c *AccessPoliciesServicePerimetersListCall) IfNoneMatch(entityTag string) *AccessPoliciesServicePerimetersListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*AccessPoliciesServicePerimetersListCall) PageSize ¶
func (c *AccessPoliciesServicePerimetersListCall) PageSize(pageSize int64) *AccessPoliciesServicePerimetersListCall

PageSize sets the optional parameter "pageSize": Number of Service Perimeters to include in the list. Default 100.

func (*AccessPoliciesServicePerimetersListCall) PageToken ¶
func (c *AccessPoliciesServicePerimetersListCall) PageToken(pageToken string) *AccessPoliciesServicePerimetersListCall

PageToken sets the optional parameter "pageToken": Next page token for the next batch of Service Perimeter instances. Defaults to the first page of results.

func (*AccessPoliciesServicePerimetersListCall) Pages ¶
func (c *AccessPoliciesServicePerimetersListCall) Pages(ctx context.Context, f func(*ListServicePerimetersResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type AccessPoliciesServicePerimetersPatchCall ¶
type AccessPoliciesServicePerimetersPatchCall struct {
	// contains filtered or unexported fields
}
func (*AccessPoliciesServicePerimetersPatchCall) Context ¶
func (c *AccessPoliciesServicePerimetersPatchCall) Context(ctx context.Context) *AccessPoliciesServicePerimetersPatchCall

Context sets the context to be used in this call's Do method.

func (*AccessPoliciesServicePerimetersPatchCall) Do ¶
func (c *AccessPoliciesServicePerimetersPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "accesscontextmanager.accessPolicies.servicePerimeters.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccessPoliciesServicePerimetersPatchCall) Fields ¶
func (c *AccessPoliciesServicePerimetersPatchCall) Fields(s ...googleapi.Field) *AccessPoliciesServicePerimetersPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccessPoliciesServicePerimetersPatchCall) Header ¶
func (c *AccessPoliciesServicePerimetersPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*AccessPoliciesServicePerimetersPatchCall) UpdateMask ¶
func (c *AccessPoliciesServicePerimetersPatchCall) UpdateMask(updateMask string) *AccessPoliciesServicePerimetersPatchCall

UpdateMask sets the optional parameter "updateMask": Required. Mask to control which fields get updated. Must be non-empty.

type AccessPoliciesServicePerimetersReplaceAllCall ¶
added in v0.18.0
type AccessPoliciesServicePerimetersReplaceAllCall struct {
	// contains filtered or unexported fields
}
func (*AccessPoliciesServicePerimetersReplaceAllCall) Context ¶
added in v0.18.0
func (c *AccessPoliciesServicePerimetersReplaceAllCall) Context(ctx context.Context) *AccessPoliciesServicePerimetersReplaceAllCall

Context sets the context to be used in this call's Do method.

func (*AccessPoliciesServicePerimetersReplaceAllCall) Do ¶
added in v0.18.0
func (c *AccessPoliciesServicePerimetersReplaceAllCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "accesscontextmanager.accessPolicies.servicePerimeters.replaceAll" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccessPoliciesServicePerimetersReplaceAllCall) Fields ¶
added in v0.18.0
func (c *AccessPoliciesServicePerimetersReplaceAllCall) Fields(s ...googleapi.Field) *AccessPoliciesServicePerimetersReplaceAllCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccessPoliciesServicePerimetersReplaceAllCall) Header ¶
added in v0.18.0
func (c *AccessPoliciesServicePerimetersReplaceAllCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccessPoliciesServicePerimetersService ¶
type AccessPoliciesServicePerimetersService struct {
	// contains filtered or unexported fields
}
func NewAccessPoliciesServicePerimetersService ¶
func NewAccessPoliciesServicePerimetersService(s *Service) *AccessPoliciesServicePerimetersService
func (*AccessPoliciesServicePerimetersService) Commit ¶
added in v0.18.0
func (r *AccessPoliciesServicePerimetersService) Commit(parent string, commitserviceperimetersrequest *CommitServicePerimetersRequest) *AccessPoliciesServicePerimetersCommitCall

Commit: Commits the dry-run specification for all the service perimeters in an access policy. A commit operation on a service perimeter involves copying its `spec` field to the `status` field of the service perimeter. Only service perimeters with `use_explicit_dry_run_spec` field set to true are affected by a commit operation. The long-running operation from this RPC has a successful status after the dry-run specifications for all the service perimeters have been committed. If a commit fails, it causes the long-running operation to return an error response and the entire commit operation is cancelled. When successful, the Operation.response field contains CommitServicePerimetersResponse. The `dry_run` and the `spec` fields are cleared after a successful commit operation.

parent: Resource name for the parent Access Policy which owns all Service Perimeters in scope for the commit operation. Format: `accessPolicies/{policy_id}`.
func (*AccessPoliciesServicePerimetersService) Create ¶
func (r *AccessPoliciesServicePerimetersService) Create(parent string, serviceperimeter *ServicePerimeter) *AccessPoliciesServicePerimetersCreateCall

Create: Creates a service perimeter. The long-running operation from this RPC has a successful status after the service perimeter propagates to long-lasting storage. If a service perimeter contains errors, an error response is returned for the first error encountered.

parent: Resource name for the access policy which owns this Service Perimeter. Format: `accessPolicies/{policy_id}`.
func (*AccessPoliciesServicePerimetersService) Delete ¶
func (r *AccessPoliciesServicePerimetersService) Delete(name string) *AccessPoliciesServicePerimetersDeleteCall

Delete: Deletes a service perimeter based on the resource name. The long-running operation from this RPC has a successful status after the service perimeter is removed from long-lasting storage.

name: Resource name for the Service Perimeter. Format: `accessPolicies/{policy_id}/servicePerimeters/{service_perimeter_id}`.
func (*AccessPoliciesServicePerimetersService) Get ¶
func (r *AccessPoliciesServicePerimetersService) Get(name string) *AccessPoliciesServicePerimetersGetCall

Get: Gets a service perimeter based on the resource name.

name: Resource name for the Service Perimeter. Format: `accessPolicies/{policy_id}/servicePerimeters/{service_perimeters_id}`.
func (*AccessPoliciesServicePerimetersService) List ¶
func (r *AccessPoliciesServicePerimetersService) List(parent string) *AccessPoliciesServicePerimetersListCall

List: Lists all service perimeters for an access policy.

parent: Resource name for the access policy to list Service Perimeters from. Format: `accessPolicies/{policy_id}`.
func (*AccessPoliciesServicePerimetersService) Patch ¶
func (r *AccessPoliciesServicePerimetersService) Patch(name string, serviceperimeter *ServicePerimeter) *AccessPoliciesServicePerimetersPatchCall

Patch: Updates a service perimeter. The long-running operation from this RPC has a successful status after the service perimeter propagates to long-lasting storage. If a service perimeter contains errors, an error response is returned for the first error encountered.

name: Identifier. Resource name for the `ServicePerimeter`. Format: `accessPolicies/{access_policy}/servicePerimeters/{service_perimeter}`. The `service_perimeter` component must begin with a letter, followed by alphanumeric characters or `_`. After you create a `ServicePerimeter`, you cannot change its `name`.
func (*AccessPoliciesServicePerimetersService) ReplaceAll ¶
added in v0.18.0
func (r *AccessPoliciesServicePerimetersService) ReplaceAll(parent string, replaceserviceperimetersrequest *ReplaceServicePerimetersRequest) *AccessPoliciesServicePerimetersReplaceAllCall

ReplaceAll: Replace all existing service perimeters in an access policy with the service perimeters provided. This is done atomically. The long-running operation from this RPC has a successful status after all replacements propagate to long-lasting storage. Replacements containing errors result in an error response for the first error encountered. Upon an error, replacement are cancelled and existing service perimeters are not affected. The Operation.response field contains ReplaceServicePerimetersResponse.

parent: Resource name for the access policy which owns these Service Perimeters. Format: `accessPolicies/{policy_id}`.
func (*AccessPoliciesServicePerimetersService) TestIamPermissions ¶
added in v0.63.0
func (r *AccessPoliciesServicePerimetersService) TestIamPermissions(resource string, testiampermissionsrequest *TestIamPermissionsRequest) *AccessPoliciesServicePerimetersTestIamPermissionsCall

TestIamPermissions: Returns the IAM permissions that the caller has on the specified Access Context Manager resource. The resource can be an AccessPolicy, AccessLevel, or ServicePerimeter. This method does not support other resources.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type AccessPoliciesServicePerimetersTestIamPermissionsCall ¶
added in v0.63.0
type AccessPoliciesServicePerimetersTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*AccessPoliciesServicePerimetersTestIamPermissionsCall) Context ¶
added in v0.63.0
func (c *AccessPoliciesServicePerimetersTestIamPermissionsCall) Context(ctx context.Context) *AccessPoliciesServicePerimetersTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*AccessPoliciesServicePerimetersTestIamPermissionsCall) Do ¶
added in v0.63.0
func (c *AccessPoliciesServicePerimetersTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)

Do executes the "accesscontextmanager.accessPolicies.servicePerimeters.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccessPoliciesServicePerimetersTestIamPermissionsCall) Fields ¶
added in v0.63.0
func (c *AccessPoliciesServicePerimetersTestIamPermissionsCall) Fields(s ...googleapi.Field) *AccessPoliciesServicePerimetersTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccessPoliciesServicePerimetersTestIamPermissionsCall) Header ¶
added in v0.63.0
func (c *AccessPoliciesServicePerimetersTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccessPoliciesSetIamPolicyCall ¶
added in v0.63.0
type AccessPoliciesSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*AccessPoliciesSetIamPolicyCall) Context ¶
added in v0.63.0
func (c *AccessPoliciesSetIamPolicyCall) Context(ctx context.Context) *AccessPoliciesSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*AccessPoliciesSetIamPolicyCall) Do ¶
added in v0.63.0
func (c *AccessPoliciesSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*Policy, error)

Do executes the "accesscontextmanager.accessPolicies.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccessPoliciesSetIamPolicyCall) Fields ¶
added in v0.63.0
func (c *AccessPoliciesSetIamPolicyCall) Fields(s ...googleapi.Field) *AccessPoliciesSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccessPoliciesSetIamPolicyCall) Header ¶
added in v0.63.0
func (c *AccessPoliciesSetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccessPoliciesTestIamPermissionsCall ¶
added in v0.63.0
type AccessPoliciesTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*AccessPoliciesTestIamPermissionsCall) Context ¶
added in v0.63.0
func (c *AccessPoliciesTestIamPermissionsCall) Context(ctx context.Context) *AccessPoliciesTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*AccessPoliciesTestIamPermissionsCall) Do ¶
added in v0.63.0
func (c *AccessPoliciesTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*TestIamPermissionsResponse, error)

Do executes the "accesscontextmanager.accessPolicies.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*AccessPoliciesTestIamPermissionsCall) Fields ¶
added in v0.63.0
func (c *AccessPoliciesTestIamPermissionsCall) Fields(s ...googleapi.Field) *AccessPoliciesTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*AccessPoliciesTestIamPermissionsCall) Header ¶
added in v0.63.0
func (c *AccessPoliciesTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type AccessPolicy ¶
type AccessPolicy struct {
	// Etag: Output only. An opaque identifier for the current version of the
	// `AccessPolicy`. This will always be a strongly validated etag, meaning that
	// two Access Policies will be identical if and only if their etags are
	// identical. Clients should not expect this to be in any specific format.
	Etag string `json:"etag,omitempty"`
	// Name: Output only. Identifier. Resource name of the `AccessPolicy`. Format:
	// `accessPolicies/{access_policy}`
	Name string `json:"name,omitempty"`
	// Parent: Required. The parent of this `AccessPolicy` in the Cloud Resource
	// Hierarchy. Currently immutable once created. Format:
	// `organizations/{organization_id}`
	Parent string `json:"parent,omitempty"`
	// Scopes: The scopes of the AccessPolicy. Scopes define which resources a
	// policy can restrict and where its resources can be referenced. For example,
	// policy A with `scopes=["folders/123"]` has the following behavior: -
	// ServicePerimeter can only restrict projects within `folders/123`. -
	// ServicePerimeter within policy A can only reference access levels defined
	// within policy A. - Only one policy can include a given scope; thus,
	// attempting to create a second policy which includes `folders/123` will
	// result in an error. If no scopes are provided, then any resource within the
	// organization can be restricted. Scopes cannot be modified after a policy is
	// created. Policies can only have a single scope. Format: list of
	// `folders/{folder_number}` or `projects/{project_number}`
	Scopes []string `json:"scopes,omitempty"`
	// Title: Required. Human readable title. Does not affect behavior.
	Title string `json:"title,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Etag") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Etag") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AccessPolicy: `AccessPolicy` is a container for `AccessLevels` (which define the necessary attributes to use Google Cloud services) and `ServicePerimeters` (which define regions of services able to freely pass data within a perimeter). An access policy is globally visible within an organization, and the restrictions it specifies apply to all projects within an organization.

func (AccessPolicy) MarshalJSON ¶
func (s AccessPolicy) MarshalJSON() ([]byte, error)
type AccessScope ¶
added in v0.198.0
type AccessScope struct {
	// ClientScope: Optional. Client scope for this access scope.
	ClientScope *ClientScope `json:"clientScope,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ClientScope") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ClientScope") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AccessScope: Access scope represents the client scope, etc. to which the settings will be applied to.

func (AccessScope) MarshalJSON ¶
added in v0.198.0
func (s AccessScope) MarshalJSON() ([]byte, error)
type AccessSettings ¶
added in v0.198.0
type AccessSettings struct {
	// AccessLevels: Optional. Access level that a user must have to be granted
	// access. Only one access level is supported, not multiple. This repeated
	// field must have exactly one element. Example:
	// "accessPolicies/9522/accessLevels/device_trusted"
	AccessLevels []string `json:"accessLevels,omitempty"`
	// SessionSettings: Optional. Session settings applied to user access on a
	// given AccessScope.
	SessionSettings *SessionSettings `json:"sessionSettings,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AccessLevels") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccessLevels") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AccessSettings: Access settings represent the set of conditions that must be met for access to be granted. At least one of the fields must be set.

func (AccessSettings) MarshalJSON ¶
added in v0.198.0
func (s AccessSettings) MarshalJSON() ([]byte, error)
type ApiOperation ¶
added in v0.37.0
type ApiOperation struct {
	// MethodSelectors: API methods or permissions to allow. Method or permission
	// must belong to the service specified by `service_name` field. A single
	// MethodSelector entry with `*` specified for the `method` field will allow
	// all methods AND permissions for the service specified in `service_name`.
	MethodSelectors []*MethodSelector `json:"methodSelectors,omitempty"`
	// ServiceName: The name of the API whose methods or permissions the
	// IngressPolicy or EgressPolicy want to allow. A single ApiOperation with
	// `service_name` field set to `*` will allow all methods AND permissions for
	// all services.
	ServiceName string `json:"serviceName,omitempty"`
	// ForceSendFields is a list of field names (e.g. "MethodSelectors") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "MethodSelectors") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ApiOperation: Identification for an API Operation.

func (ApiOperation) MarshalJSON ¶
added in v0.37.0
func (s ApiOperation) MarshalJSON() ([]byte, error)
type Application ¶
added in v0.178.0
type Application struct {
	// ClientId: The OAuth client ID of the application.
	ClientId string `json:"clientId,omitempty"`
	// Name: The name of the application. Example: "Cloud Console"
	Name string `json:"name,omitempty"`
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

Application: An application that accesses Google Cloud APIs.

func (Application) MarshalJSON ¶
added in v0.178.0
func (s Application) MarshalJSON() ([]byte, error)
type AuditConfig ¶
added in v0.63.0
type AuditConfig struct {
	// AuditLogConfigs: The configuration for logging of each type of permission.
	AuditLogConfigs []*AuditLogConfig `json:"auditLogConfigs,omitempty"`
	// Service: Specifies a service that will be enabled for audit logging. For
	// example, `storage.googleapis.com`, `cloudsql.googleapis.com`. `allServices`
	// is a special value that covers all services.
	Service string `json:"service,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AuditLogConfigs") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AuditLogConfigs") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AuditConfig: Specifies the audit configuration for a service. The configuration determines which permission types are logged, and what identities, if any, are exempted from logging. An AuditConfig must have one or more AuditLogConfigs. If there are AuditConfigs for both `allServices` and a specific service, the union of the two AuditConfigs is used for that service: the log_types specified in each AuditConfig are enabled, and the exempted_members in each AuditLogConfig are exempted. Example Policy with multiple AuditConfigs: { "audit_configs": [ { "service": "allServices", "audit_log_configs": [ { "log_type": "DATA_READ", "exempted_members": [ "user:jose@example.com" ] }, { "log_type": "DATA_WRITE" }, { "log_type": "ADMIN_READ" } ] }, { "service": "sampleservice.googleapis.com", "audit_log_configs": [ { "log_type": "DATA_READ" }, { "log_type": "DATA_WRITE", "exempted_members": [ "user:aliya@example.com" ] } ] } ] } For sampleservice, this policy enables DATA_READ, DATA_WRITE and ADMIN_READ logging. It also exempts `jose@example.com` from DATA_READ logging, and `aliya@example.com` from DATA_WRITE logging.

func (AuditConfig) MarshalJSON ¶
added in v0.63.0
func (s AuditConfig) MarshalJSON() ([]byte, error)
type AuditLogConfig ¶
added in v0.63.0
type AuditLogConfig struct {
	// ExemptedMembers: Specifies the identities that do not cause logging for this
	// type of permission. Follows the same format of Binding.members.
	ExemptedMembers []string `json:"exemptedMembers,omitempty"`
	// LogType: The log type that this config enables.
	//
	// Possible values:
	//   "LOG_TYPE_UNSPECIFIED" - Default case. Should never be this.
	//   "ADMIN_READ" - Admin reads. Example: CloudIAM getIamPolicy
	//   "DATA_WRITE" - Data writes. Example: CloudSQL Users create
	//   "DATA_READ" - Data reads. Example: CloudSQL Users list
	LogType string `json:"logType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ExemptedMembers") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExemptedMembers") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AuditLogConfig: Provides the configuration for logging a type of permissions. Example: { "audit_log_configs": [ { "log_type": "DATA_READ", "exempted_members": [ "user:jose@example.com" ] }, { "log_type": "DATA_WRITE" } ] } This enables 'DATA_READ' and 'DATA_WRITE' logging, while exempting jose@example.com from DATA_READ logging.

func (AuditLogConfig) MarshalJSON ¶
added in v0.63.0
func (s AuditLogConfig) MarshalJSON() ([]byte, error)
type AuthorizedOrgsDesc ¶
added in v0.106.0
type AuthorizedOrgsDesc struct {
	// AssetType: The asset type of this authorized orgs desc. Valid values are
	// `ASSET_TYPE_DEVICE`, and `ASSET_TYPE_CREDENTIAL_STRENGTH`.
	//
	// Possible values:
	//   "ASSET_TYPE_UNSPECIFIED" - No asset type specified.
	//   "ASSET_TYPE_DEVICE" - Device asset type.
	//   "ASSET_TYPE_CREDENTIAL_STRENGTH" - Credential strength asset type.
	AssetType string `json:"assetType,omitempty"`
	// AuthorizationDirection: The direction of the authorization relationship
	// between this organization and the organizations listed in the `orgs` field.
	// The valid values for this field include the following:
	// `AUTHORIZATION_DIRECTION_FROM`: Allows this organization to evaluate traffic
	// in the organizations listed in the `orgs` field.
	// `AUTHORIZATION_DIRECTION_TO`: Allows the organizations listed in the `orgs`
	// field to evaluate the traffic in this organization. For the authorization
	// relationship to take effect, all of the organizations must authorize and
	// specify the appropriate relationship direction. For example, if organization
	// A authorized organization B and C to evaluate its traffic, by specifying
	// `AUTHORIZATION_DIRECTION_TO` as the authorization direction, organizations B
	// and C must specify `AUTHORIZATION_DIRECTION_FROM` as the authorization
	// direction in their `AuthorizedOrgsDesc` resource.
	//
	// Possible values:
	//   "AUTHORIZATION_DIRECTION_UNSPECIFIED" - No direction specified.
	//   "AUTHORIZATION_DIRECTION_TO" - The specified organizations are authorized
	// to evaluate traffic in this organization.
	//   "AUTHORIZATION_DIRECTION_FROM" - The traffic of the specified
	// organizations can be evaluated by this organization.
	AuthorizationDirection string `json:"authorizationDirection,omitempty"`
	// AuthorizationType: A granular control type for authorization levels. Valid
	// value is `AUTHORIZATION_TYPE_TRUST`.
	//
	// Possible values:
	//   "AUTHORIZATION_TYPE_UNSPECIFIED" - No authorization type specified.
	//   "AUTHORIZATION_TYPE_TRUST" - This authorization relationship is "trust".
	AuthorizationType string `json:"authorizationType,omitempty"`
	// Name: Identifier. Resource name for the `AuthorizedOrgsDesc`. Format:
	// `accessPolicies/{access_policy}/authorizedOrgsDescs/{authorized_orgs_desc}`.
	// The `authorized_orgs_desc` component must begin with a letter, followed by
	// alphanumeric characters or `_`. After you create an `AuthorizedOrgsDesc`,
	// you cannot change its `name`.
	Name string `json:"name,omitempty"`
	// Orgs: The list of organization ids in this AuthorizedOrgsDesc. Format:
	// `organizations/` Example: `organizations/123456`
	Orgs []string `json:"orgs,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AssetType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AssetType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AuthorizedOrgsDesc: `AuthorizedOrgsDesc` contains data for an organization's authorization policy.

func (AuthorizedOrgsDesc) MarshalJSON ¶
added in v0.106.0
func (s AuthorizedOrgsDesc) MarshalJSON() ([]byte, error)
type BasicLevel ¶
type BasicLevel struct {
	// CombiningFunction: How the `conditions` list should be combined to determine
	// if a request is granted this `AccessLevel`. If AND is used, each `Condition`
	// in `conditions` must be satisfied for the `AccessLevel` to be applied. If OR
	// is used, at least one `Condition` in `conditions` must be satisfied for the
	// `AccessLevel` to be applied. Default behavior is AND.
	//
	// Possible values:
	//   "AND" - All `Conditions` must be true for the `BasicLevel` to be true.
	//   "OR" - If at least one `Condition` is true, then the `BasicLevel` is true.
	CombiningFunction string `json:"combiningFunction,omitempty"`
	// Conditions: Required. A list of requirements for the `AccessLevel` to be
	// granted.
	Conditions []*Condition `json:"conditions,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CombiningFunction") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CombiningFunction") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

BasicLevel: `BasicLevel` is an `AccessLevel` using a set of recommended features.

func (BasicLevel) MarshalJSON ¶
func (s BasicLevel) MarshalJSON() ([]byte, error)
type Binding ¶
added in v0.63.0
type Binding struct {
	// Condition: The condition that is associated with this binding. If the
	// condition evaluates to `true`, then this binding applies to the current
	// request. If the condition evaluates to `false`, then this binding does not
	// apply to the current request. However, a different role binding might grant
	// the same role to one or more of the principals in this binding. To learn
	// which resources support conditions in their IAM policies, see the IAM
	// documentation
	// (https://cloud.google.com/iam/help/conditions/resource-policies).
	Condition *Expr `json:"condition,omitempty"`
	// Members: Specifies the principals requesting access for a Google Cloud
	// resource. `members` can have the following values: * `allUsers`: A special
	// identifier that represents anyone who is on the internet; with or without a
	// Google account. * `allAuthenticatedUsers`: A special identifier that
	// represents anyone who is authenticated with a Google account or a service
	// account. Does not include identities that come from external identity
	// providers (IdPs) through identity federation. * `user:{emailid}`: An email
	// address that represents a specific Google account. For example,
	// `alice@example.com` . * `serviceAccount:{emailid}`: An email address that
	// represents a Google service account. For example,
	// `my-other-app@appspot.gserviceaccount.com`. *
	// `serviceAccount:{projectid}.svc.id.goog[{namespace}/{kubernetes-sa}]`: An
	// identifier for a Kubernetes service account
	// (https://cloud.google.com/kubernetes-engine/docs/how-to/kubernetes-service-accounts).
	// For example, `my-project.svc.id.goog[my-namespace/my-kubernetes-sa]`. *
	// `group:{emailid}`: An email address that represents a Google group. For
	// example, `admins@example.com`. * `domain:{domain}`: The G Suite domain
	// (primary) that represents all the users of that domain. For example,
	// `google.com` or `example.com`. *
	// `principal://iam.googleapis.com/locations/global/workforcePools/{pool_id}/sub
	// ject/{subject_attribute_value}`: A single identity in a workforce identity
	// pool. *
	// `principalSet://iam.googleapis.com/locations/global/workforcePools/{pool_id}/
	// group/{group_id}`: All workforce identities in a group. *
	// `principalSet://iam.googleapis.com/locations/global/workforcePools/{pool_id}/
	// attribute.{attribute_name}/{attribute_value}`: All workforce identities with
	// a specific attribute value. *
	// `principalSet://iam.googleapis.com/locations/global/workforcePools/{pool_id}/
	// *`: All identities in a workforce identity pool. *
	// `principal://iam.googleapis.com/projects/{project_number}/locations/global/wo
	// rkloadIdentityPools/{pool_id}/subject/{subject_attribute_value}`: A single
	// identity in a workload identity pool. *
	// `principalSet://iam.googleapis.com/projects/{project_number}/locations/global
	// /workloadIdentityPools/{pool_id}/group/{group_id}`: A workload identity pool
	// group. *
	// `principalSet://iam.googleapis.com/projects/{project_number}/locations/global
	// /workloadIdentityPools/{pool_id}/attribute.{attribute_name}/{attribute_value}
	// `: All identities in a workload identity pool with a certain attribute. *
	// `principalSet://iam.googleapis.com/projects/{project_number}/locations/global
	// /workloadIdentityPools/{pool_id}/*`: All identities in a workload identity
	// pool. * `deleted:user:{emailid}?uid={uniqueid}`: An email address (plus
	// unique identifier) representing a user that has been recently deleted. For
	// example, `alice@example.com?uid=123456789012345678901`. If the user is
	// recovered, this value reverts to `user:{emailid}` and the recovered user
	// retains the role in the binding. *
	// `deleted:serviceAccount:{emailid}?uid={uniqueid}`: An email address (plus
	// unique identifier) representing a service account that has been recently
	// deleted. For example,
	// `my-other-app@appspot.gserviceaccount.com?uid=123456789012345678901`. If the
	// service account is undeleted, this value reverts to
	// `serviceAccount:{emailid}` and the undeleted service account retains the
	// role in the binding. * `deleted:group:{emailid}?uid={uniqueid}`: An email
	// address (plus unique identifier) representing a Google group that has been
	// recently deleted. For example,
	// `admins@example.com?uid=123456789012345678901`. If the group is recovered,
	// this value reverts to `group:{emailid}` and the recovered group retains the
	// role in the binding. *
	// `deleted:principal://iam.googleapis.com/locations/global/workforcePools/{pool
	// _id}/subject/{subject_attribute_value}`: Deleted single identity in a
	// workforce identity pool. For example,
	// `deleted:principal://iam.googleapis.com/locations/global/workforcePools/my-po
	// ol-id/subject/my-subject-attribute-value`.
	Members []string `json:"members,omitempty"`
	// Role: Role that is assigned to the list of `members`, or principals. For
	// example, `roles/viewer`, `roles/editor`, or `roles/owner`. For an overview
	// of the IAM roles and permissions, see the IAM documentation
	// (https://cloud.google.com/iam/docs/roles-overview). For a list of the
	// available pre-defined roles, see here
	// (https://cloud.google.com/iam/docs/understanding-roles).
	Role string `json:"role,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Condition") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Condition") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Binding: Associates `members`, or principals, with a `role`.

func (Binding) MarshalJSON ¶
added in v0.63.0
func (s Binding) MarshalJSON() ([]byte, error)
type CancelOperationRequest ¶
type CancelOperationRequest struct {
}

CancelOperationRequest: The request message for Operations.CancelOperation.

type ClientScope ¶
added in v0.198.0
type ClientScope struct {
	// RestrictedClientApplication: Optional. The application that is subject to
	// this binding's scope.
	RestrictedClientApplication *Application `json:"restrictedClientApplication,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "RestrictedClientApplication") to unconditionally include in API requests.
	// By default, fields with empty or default values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields
	// for more details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "RestrictedClientApplication") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ClientScope: Client scope represents the application, etc. subject to this binding's restrictions.

func (ClientScope) MarshalJSON ¶
added in v0.198.0
func (s ClientScope) MarshalJSON() ([]byte, error)
type CommitServicePerimetersRequest ¶
added in v0.18.0
type CommitServicePerimetersRequest struct {
	// Etag: Optional. The etag for the version of the Access Policy that this
	// commit operation is to be performed on. If, at the time of commit, the etag
	// for the Access Policy stored in Access Context Manager is different from the
	// specified etag, then the commit operation will not be performed and the call
	// will fail. This field is not required. If etag is not provided, the
	// operation will be performed as if a valid etag is provided.
	Etag string `json:"etag,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Etag") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Etag") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CommitServicePerimetersRequest: A request to commit dry-run specs in all Service Perimeters belonging to an Access Policy.

func (CommitServicePerimetersRequest) MarshalJSON ¶
added in v0.18.0
func (s CommitServicePerimetersRequest) MarshalJSON() ([]byte, error)
type CommitServicePerimetersResponse ¶
added in v0.18.0
type CommitServicePerimetersResponse struct {
	// ServicePerimeters: List of all the Service Perimeter instances in the Access
	// Policy.
	ServicePerimeters []*ServicePerimeter `json:"servicePerimeters,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ServicePerimeters") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ServicePerimeters") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CommitServicePerimetersResponse: A response to CommitServicePerimetersRequest. This will be put inside of Operation.response field.

func (CommitServicePerimetersResponse) MarshalJSON ¶
added in v0.18.0
func (s CommitServicePerimetersResponse) MarshalJSON() ([]byte, error)
type Condition ¶
type Condition struct {
	// DevicePolicy: Device specific restrictions, all restrictions must hold for
	// the Condition to be true. If not specified, all devices are allowed.
	DevicePolicy *DevicePolicy `json:"devicePolicy,omitempty"`
	// IpSubnetworks: CIDR block IP subnetwork specification. May be IPv4 or IPv6.
	// Note that for a CIDR IP address block, the specified IP address portion must
	// be properly truncated (i.e. all the host bits must be zero) or the input is
	// considered malformed. For example, "192.0.2.0/24" is accepted but
	// "192.0.2.1/24" is not. Similarly, for IPv6, "2001:db8::/32" is accepted
	// whereas "2001:db8::1/32" is not. The originating IP of a request must be in
	// one of the listed subnets in order for this Condition to be true. If empty,
	// all IP addresses are allowed.
	IpSubnetworks []string `json:"ipSubnetworks,omitempty"`
	// Members: The request must be made by one of the provided user or service
	// accounts. Groups are not supported. Syntax: `user:{emailid}`
	// `serviceAccount:{emailid}` If not specified, a request may come from any
	// user.
	Members []string `json:"members,omitempty"`
	// Negate: Whether to negate the Condition. If true, the Condition becomes a
	// NAND over its non-empty fields. Any non-empty field criteria evaluating to
	// false will result in the Condition to be satisfied. Defaults to false.
	Negate bool `json:"negate,omitempty"`
	// Regions: The request must originate from one of the provided
	// countries/regions. Must be valid ISO 3166-1 alpha-2 codes.
	Regions []string `json:"regions,omitempty"`
	// RequiredAccessLevels: A list of other access levels defined in the same
	// `Policy`, referenced by resource name. Referencing an `AccessLevel` which
	// does not exist is an error. All access levels listed must be granted for the
	// Condition to be true. Example:
	// "accessPolicies/MY_POLICY/accessLevels/LEVEL_NAME"
	RequiredAccessLevels []string `json:"requiredAccessLevels,omitempty"`
	// VpcNetworkSources: The request must originate from one of the provided VPC
	// networks in Google Cloud. Cannot specify this field together with
	// `ip_subnetworks`.
	VpcNetworkSources []*VpcNetworkSource `json:"vpcNetworkSources,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DevicePolicy") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DevicePolicy") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Condition: A condition necessary for an `AccessLevel` to be granted. The Condition is an AND over its fields. So a Condition is true if: 1) the request IP is from one of the listed subnetworks AND 2) the originating device complies with the listed device policy AND 3) all listed access levels are granted AND 4) the request was sent at a time allowed by the DateTimeRestriction.

func (Condition) MarshalJSON ¶
func (s Condition) MarshalJSON() ([]byte, error)
type CustomLevel ¶
added in v0.16.0
type CustomLevel struct {
	// Expr: Required. A Cloud CEL expression evaluating to a boolean.
	Expr *Expr `json:"expr,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Expr") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Expr") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CustomLevel: `CustomLevel` is an `AccessLevel` using the Cloud Common Expression Language to represent the necessary conditions for the level to apply to a request. See CEL spec at: https://github.com/google/cel-spec

func (CustomLevel) MarshalJSON ¶
added in v0.16.0
func (s CustomLevel) MarshalJSON() ([]byte, error)
type DevicePolicy ¶
type DevicePolicy struct {
	// AllowedDeviceManagementLevels: Allowed device management levels, an empty
	// list allows all management levels.
	//
	// Possible values:
	//   "MANAGEMENT_UNSPECIFIED" - The device's management level is not specified
	// or not known.
	//   "NONE" - The device is not managed.
	//   "BASIC" - Basic management is enabled, which is generally limited to
	// monitoring and wiping the corporate account.
	//   "COMPLETE" - Complete device management. This includes more thorough
	// monitoring and the ability to directly manage the device (such as remote
	// wiping). This can be enabled through the Android Enterprise Platform.
	AllowedDeviceManagementLevels []string `json:"allowedDeviceManagementLevels,omitempty"`
	// AllowedEncryptionStatuses: Allowed encryptions statuses, an empty list
	// allows all statuses.
	//
	// Possible values:
	//   "ENCRYPTION_UNSPECIFIED" - The encryption status of the device is not
	// specified or not known.
	//   "ENCRYPTION_UNSUPPORTED" - The device does not support encryption.
	//   "UNENCRYPTED" - The device supports encryption, but is currently
	// unencrypted.
	//   "ENCRYPTED" - The device is encrypted.
	AllowedEncryptionStatuses []string `json:"allowedEncryptionStatuses,omitempty"`
	// OsConstraints: Allowed OS versions, an empty list allows all types and all
	// versions.
	OsConstraints []*OsConstraint `json:"osConstraints,omitempty"`
	// RequireAdminApproval: Whether the device needs to be approved by the
	// customer admin.
	RequireAdminApproval bool `json:"requireAdminApproval,omitempty"`
	// RequireCorpOwned: Whether the device needs to be corp owned.
	RequireCorpOwned bool `json:"requireCorpOwned,omitempty"`
	// RequireScreenlock: Whether or not screenlock is required for the
	// DevicePolicy to be true. Defaults to `false`.
	RequireScreenlock bool `json:"requireScreenlock,omitempty"`
	// ForceSendFields is a list of field names (e.g.
	// "AllowedDeviceManagementLevels") to unconditionally include in API requests.
	// By default, fields with empty or default values are omitted from API
	// requests. See https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields
	// for more details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AllowedDeviceManagementLevels")
	// to include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

DevicePolicy: `DevicePolicy` specifies device specific restrictions necessary to acquire a given access level. A `DevicePolicy` specifies requirements for requests from devices to be granted access levels, it does not do any enforcement on the device. `DevicePolicy` acts as an AND over all specified fields, and each repeated field is an OR over its elements. Any unset fields are ignored. For example, if the proto is { os_type : DESKTOP_WINDOWS, os_type : DESKTOP_LINUX, encryption_status: ENCRYPTED}, then the DevicePolicy will be true for requests originating from encrypted Linux desktops and encrypted Windows desktops.

func (DevicePolicy) MarshalJSON ¶
func (s DevicePolicy) MarshalJSON() ([]byte, error)
type EgressFrom ¶
added in v0.37.0
type EgressFrom struct {
	// Identities: A list of identities that are allowed access through
	// [EgressPolicy]. Identities can be an individual user, service account,
	// Google group, or third-party identity. For third-party identity, only single
	// identities are supported and other identity types are not supported. The
	// `v1` identities that have the prefix `user`, `group`, `serviceAccount`, and
	// `principal` in https://cloud.google.com/iam/docs/principal-identifiers#v1
	// are supported.
	Identities []string `json:"identities,omitempty"`
	// IdentityType: Specifies the type of identities that are allowed access to
	// outside the perimeter. If left unspecified, then members of `identities`
	// field will be allowed access.
	//
	// Possible values:
	//   "IDENTITY_TYPE_UNSPECIFIED" - No blanket identity group specified.
	//   "ANY_IDENTITY" - Authorize access from all identities outside the
	// perimeter.
	//   "ANY_USER_ACCOUNT" - Authorize access from all human users outside the
	// perimeter.
	//   "ANY_SERVICE_ACCOUNT" - Authorize access from all service accounts outside
	// the perimeter.
	IdentityType string `json:"identityType,omitempty"`
	// SourceRestriction: Whether to enforce traffic restrictions based on
	// `sources` field. If the `sources` fields is non-empty, then this field must
	// be set to `SOURCE_RESTRICTION_ENABLED`.
	//
	// Possible values:
	//   "SOURCE_RESTRICTION_UNSPECIFIED" - Enforcement preference unspecified,
	// will not enforce traffic restrictions based on `sources` in EgressFrom.
	//   "SOURCE_RESTRICTION_ENABLED" - Enforcement preference enabled, traffic
	// restrictions will be enforced based on `sources` in EgressFrom.
	//   "SOURCE_RESTRICTION_DISABLED" - Enforcement preference disabled, will not
	// enforce traffic restrictions based on `sources` in EgressFrom.
	SourceRestriction string `json:"sourceRestriction,omitempty"`
	// Sources: Sources that this EgressPolicy authorizes access from. If this
	// field is not empty, then `source_restriction` must be set to
	// `SOURCE_RESTRICTION_ENABLED`.
	Sources []*EgressSource `json:"sources,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Identities") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Identities") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

EgressFrom: Defines the conditions under which an EgressPolicy matches a request. Conditions based on information about the source of the request. Note that if the destination of the request is also protected by a ServicePerimeter, then that ServicePerimeter must have an IngressPolicy which allows access in order for this request to succeed.

func (EgressFrom) MarshalJSON ¶
added in v0.37.0
func (s EgressFrom) MarshalJSON() ([]byte, error)
type EgressPolicy ¶
added in v0.37.0
type EgressPolicy struct {
	// EgressFrom: Defines conditions on the source of a request causing this
	// EgressPolicy to apply.
	EgressFrom *EgressFrom `json:"egressFrom,omitempty"`
	// EgressTo: Defines the conditions on the ApiOperation and destination
	// resources that cause this EgressPolicy to apply.
	EgressTo *EgressTo `json:"egressTo,omitempty"`
	// Title: Optional. Human-readable title for the egress rule. The title must be
	// unique within the perimeter and can not exceed 100 characters. Within the
	// access policy, the combined length of all rule titles must not exceed
	// 240,000 characters.
	Title string `json:"title,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EgressFrom") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EgressFrom") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

EgressPolicy: Policy for egress from perimeter. EgressPolicies match requests based on `egress_from` and `egress_to` stanzas. For an EgressPolicy to match, both `egress_from` and `egress_to` stanzas must be matched. If an EgressPolicy matches a request, the request is allowed to span the ServicePerimeter boundary. For example, an EgressPolicy can be used to allow VMs on networks within the ServicePerimeter to access a defined set of projects outside the perimeter in certain contexts (e.g. to read data from a Cloud Storage bucket or query against a BigQuery dataset). EgressPolicies are concerned with the *resources* that a request relates as well as the API services and API actions being used. They do not related to the direction of data movement. More detailed documentation for this concept can be found in the descriptions of EgressFrom and EgressTo.

func (EgressPolicy) MarshalJSON ¶
added in v0.37.0
func (s EgressPolicy) MarshalJSON() ([]byte, error)
type EgressSource ¶
added in v0.141.0
type EgressSource struct {
	// AccessLevel: An AccessLevel resource name that allows protected resources
	// inside the ServicePerimeters to access outside the ServicePerimeter
	// boundaries. AccessLevels listed must be in the same policy as this
	// ServicePerimeter. Referencing a nonexistent AccessLevel will cause an error.
	// If an AccessLevel name is not specified, only resources within the perimeter
	// can be accessed through Google Cloud calls with request origins within the
	// perimeter. Example: `accessPolicies/MY_POLICY/accessLevels/MY_LEVEL`. If a
	// single `*` is specified for `access_level`, then all EgressSources will be
	// allowed.
	AccessLevel string `json:"accessLevel,omitempty"`
	// Resource: A Google Cloud resource from the service perimeter that you want
	// to allow to access data outside the perimeter. This field supports only
	// projects. The project format is `projects/{project_number}`. You can't use
	// `*` in this field to allow all Google Cloud resources.
	Resource string `json:"resource,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AccessLevel") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccessLevel") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

EgressSource: The source that EgressPolicy authorizes access from inside the ServicePerimeter to somewhere outside the ServicePerimeter boundaries.

func (EgressSource) MarshalJSON ¶
added in v0.141.0
func (s EgressSource) MarshalJSON() ([]byte, error)
type EgressTo ¶
added in v0.37.0
type EgressTo struct {
	// ExternalResources: A list of external resources that are allowed to be
	// accessed. Only AWS and Azure resources are supported. For Amazon S3, the
	// supported formats are s3://BUCKET_NAME, s3a://BUCKET_NAME, and
	// s3n://BUCKET_NAME. For Azure Storage, the supported format is
	// azure://myaccount.blob.core.windows.net/CONTAINER_NAME. A request matches if
	// it contains an external resource in this list (Example: s3://bucket/path).
	// Currently '*' is not allowed.
	ExternalResources []string `json:"externalResources,omitempty"`
	// Operations: A list of ApiOperations allowed to be performed by the sources
	// specified in the corresponding EgressFrom. A request matches if it uses an
	// operation/service in this list.
	Operations []*ApiOperation `json:"operations,omitempty"`
	// Resources: A list of resources, currently only projects in the form
	// `projects/`, that are allowed to be accessed by sources defined in the
	// corresponding EgressFrom. A request matches if it contains a resource in
	// this list. If `*` is specified for `resources`, then this EgressTo rule will
	// authorize access to all resources outside the perimeter.
	Resources []string `json:"resources,omitempty"`
	// Roles: IAM roles that represent the set of operations that the sources
	// specified in the corresponding EgressFrom. are allowed to perform in this
	// ServicePerimeter.
	Roles []string `json:"roles,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ExternalResources") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ExternalResources") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

EgressTo: Defines the conditions under which an EgressPolicy matches a request. Conditions are based on information about the ApiOperation intended to be performed on the `resources` specified. Note that if the destination of the request is also protected by a ServicePerimeter, then that ServicePerimeter must have an IngressPolicy which allows access in order for this request to succeed. The request must match `operations` AND `resources` fields in order to be allowed egress out of the perimeter.

func (EgressTo) MarshalJSON ¶
added in v0.37.0
func (s EgressTo) MarshalJSON() ([]byte, error)
type Empty ¶
type Empty struct {
	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
}

Empty: A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }

type Expr ¶
added in v0.16.0
type Expr struct {
	// Description: Optional. Description of the expression. This is a longer text
	// which describes the expression, e.g. when hovered over it in a UI.
	Description string `json:"description,omitempty"`
	// Expression: Textual representation of an expression in Common Expression
	// Language syntax.
	Expression string `json:"expression,omitempty"`
	// Location: Optional. String indicating the location of the expression for
	// error reporting, e.g. a file name and a position in the file.
	Location string `json:"location,omitempty"`
	// Title: Optional. Title for the expression, i.e. a short string describing
	// its purpose. This can be used e.g. in UIs which allow to enter the
	// expression.
	Title string `json:"title,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Description") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Description") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Expr: Represents a textual expression in the Common Expression Language (CEL) syntax. CEL is a C-like expression language. The syntax and semantics of CEL are documented at https://github.com/google/cel-spec. Example (Comparison): title: "Summary size limit" description: "Determines if a summary is less than 100 chars" expression: "document.summary.size() < 100" Example (Equality): title: "Requestor is owner" description: "Determines if requestor is the document owner" expression: "document.owner == request.auth.claims.email" Example (Logic): title: "Public documents" description: "Determine whether the document should be publicly visible" expression: "document.type != 'private' && document.type != 'internal'" Example (Data Manipulation): title: "Notification string" description: "Create a notification string with a timestamp." expression: "'New message received at ' + string(document.create_time)" The exact variables and functions that may be referenced within an expression are determined by the service that evaluates it. See the service documentation for additional information.

func (Expr) MarshalJSON ¶
added in v0.16.0
func (s Expr) MarshalJSON() ([]byte, error)
type GcpUserAccessBinding ¶
added in v0.33.0
type GcpUserAccessBinding struct {
	// AccessLevels: Optional. Access level that a user must have to be granted
	// access. Only one access level is supported, not multiple. This repeated
	// field must have exactly one element. Example:
	// "accessPolicies/9522/accessLevels/device_trusted"
	AccessLevels []string `json:"accessLevels,omitempty"`
	// DryRunAccessLevels: Optional. Dry run access level that will be evaluated
	// but will not be enforced. The access denial based on dry run policy will be
	// logged. Only one access level is supported, not multiple. This list must
	// have exactly one element. Example:
	// "accessPolicies/9522/accessLevels/device_trusted"
	DryRunAccessLevels []string `json:"dryRunAccessLevels,omitempty"`
	// GroupKey: Optional. Immutable. Google Group id whose users are subject to
	// this binding's restrictions. See "id" in the [Google Workspace Directory
	// API's Group Resource]
	// (https://developers.google.com/admin-sdk/directory/v1/reference/groups#resource).
	// If a group's email address/alias is changed, this resource will continue to
	// point at the changed group. This field does not accept group email addresses
	// or aliases. Example: "01d520gv4vjcrht"
	GroupKey string `json:"groupKey,omitempty"`
	// Name: Immutable. Assigned by the server during creation. The last segment
	// has an arbitrary length and has only URI unreserved characters (as defined
	// by RFC 3986 Section 2.3 (https://tools.ietf.org/html/rfc3986#section-2.3)).
	// Should not be specified by the client during creation. Example:
	// "organizations/256/gcpUserAccessBindings/b3-BhcX_Ud5N"
	Name string `json:"name,omitempty"`
	// RestrictedClientApplications: Optional. A list of applications that are
	// subject to this binding's restrictions. If the list is empty, the binding
	// restrictions will universally apply to all applications.
	RestrictedClientApplications []*Application `json:"restrictedClientApplications,omitempty"`
	// ScopedAccessSettings: Optional. A list of scoped access settings that set
	// this binding's restrictions on a subset of applications. This field cannot
	// be set if restricted_client_applications is set.
	ScopedAccessSettings []*ScopedAccessSettings `json:"scopedAccessSettings,omitempty"`
	// SessionSettings: Optional. The Google Cloud session length (GCSL) policy for
	// the group key.
	SessionSettings *SessionSettings `json:"sessionSettings,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AccessLevels") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccessLevels") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GcpUserAccessBinding: Restricts access to Cloud Console and Google Cloud APIs for a set of users using Context-Aware Access.

func (GcpUserAccessBinding) MarshalJSON ¶
added in v0.33.0
func (s GcpUserAccessBinding) MarshalJSON() ([]byte, error)
type GcpUserAccessBindingOperationMetadata ¶
added in v0.53.0
type GcpUserAccessBindingOperationMetadata struct {
}

GcpUserAccessBindingOperationMetadata: Metadata of Google Cloud Access Binding Long Running Operations.

type GetIamPolicyRequest ¶
added in v0.63.0
type GetIamPolicyRequest struct {
	// Options: OPTIONAL: A `GetPolicyOptions` object for specifying options to
	// `GetIamPolicy`.
	Options *GetPolicyOptions `json:"options,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Options") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Options") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GetIamPolicyRequest: Request message for `GetIamPolicy` method.

func (GetIamPolicyRequest) MarshalJSON ¶
added in v0.63.0
func (s GetIamPolicyRequest) MarshalJSON() ([]byte, error)
type GetPolicyOptions ¶
added in v0.63.0
type GetPolicyOptions struct {
	// RequestedPolicyVersion: Optional. The maximum policy version that will be
	// used to format the policy. Valid values are 0, 1, and 3. Requests specifying
	// an invalid value will be rejected. Requests for policies with any
	// conditional role bindings must specify version 3. Policies with no
	// conditional role bindings may specify any valid value or leave the field
	// unset. The policy in the response might use the policy version that you
	// specified, or it might use a lower policy version. For example, if you
	// specify version 3, but the policy has no conditional role bindings, the
	// response uses version 1. To learn which resources support conditions in
	// their IAM policies, see the IAM documentation
	// (https://cloud.google.com/iam/help/conditions/resource-policies).
	RequestedPolicyVersion int64 `json:"requestedPolicyVersion,omitempty"`
	// ForceSendFields is a list of field names (e.g. "RequestedPolicyVersion") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "RequestedPolicyVersion") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GetPolicyOptions: Encapsulates settings provided to GetIamPolicy.

func (GetPolicyOptions) MarshalJSON ¶
added in v0.63.0
func (s GetPolicyOptions) MarshalJSON() ([]byte, error)
type IngressFrom ¶
added in v0.37.0
type IngressFrom struct {
	// Identities: A list of identities that are allowed access through
	// [IngressPolicy]. Identities can be an individual user, service account,
	// Google group, or third-party identity. For third-party identity, only single
	// identities are supported and other identity types are not supported. The
	// `v1` identities that have the prefix `user`, `group`, `serviceAccount`, and
	// `principal` in https://cloud.google.com/iam/docs/principal-identifiers#v1
	// are supported.
	Identities []string `json:"identities,omitempty"`
	// IdentityType: Specifies the type of identities that are allowed access from
	// outside the perimeter. If left unspecified, then members of `identities`
	// field will be allowed access.
	//
	// Possible values:
	//   "IDENTITY_TYPE_UNSPECIFIED" - No blanket identity group specified.
	//   "ANY_IDENTITY" - Authorize access from all identities outside the
	// perimeter.
	//   "ANY_USER_ACCOUNT" - Authorize access from all human users outside the
	// perimeter.
	//   "ANY_SERVICE_ACCOUNT" - Authorize access from all service accounts outside
	// the perimeter.
	IdentityType string `json:"identityType,omitempty"`
	// Sources: Sources that this IngressPolicy authorizes access from.
	Sources []*IngressSource `json:"sources,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Identities") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Identities") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

IngressFrom: Defines the conditions under which an IngressPolicy matches a request. Conditions are based on information about the source of the request. The request must satisfy what is defined in `sources` AND identity related fields in order to match.

func (IngressFrom) MarshalJSON ¶
added in v0.37.0
func (s IngressFrom) MarshalJSON() ([]byte, error)
type IngressPolicy ¶
added in v0.37.0
type IngressPolicy struct {
	// IngressFrom: Defines the conditions on the source of a request causing this
	// IngressPolicy to apply.
	IngressFrom *IngressFrom `json:"ingressFrom,omitempty"`
	// IngressTo: Defines the conditions on the ApiOperation and request
	// destination that cause this IngressPolicy to apply.
	IngressTo *IngressTo `json:"ingressTo,omitempty"`
	// Title: Optional. Human-readable title for the ingress rule. The title must
	// be unique within the perimeter and can not exceed 100 characters. Within the
	// access policy, the combined length of all rule titles must not exceed
	// 240,000 characters.
	Title string `json:"title,omitempty"`
	// ForceSendFields is a list of field names (e.g. "IngressFrom") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "IngressFrom") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

IngressPolicy: Policy for ingress into ServicePerimeter. IngressPolicies match requests based on `ingress_from` and `ingress_to` stanzas. For an ingress policy to match, both the `ingress_from` and `ingress_to` stanzas must be matched. If an IngressPolicy matches a request, the request is allowed through the perimeter boundary from outside the perimeter. For example, access from the internet can be allowed either based on an AccessLevel or, for traffic hosted on Google Cloud, the project of the source network. For access from private networks, using the project of the hosting network is required. Individual ingress policies can be limited by restricting which services and/or actions they match using the `ingress_to` field.

func (IngressPolicy) MarshalJSON ¶
added in v0.37.0
func (s IngressPolicy) MarshalJSON() ([]byte, error)
type IngressSource ¶
added in v0.37.0
type IngressSource struct {
	// AccessLevel: An AccessLevel resource name that allow resources within the
	// ServicePerimeters to be accessed from the internet. AccessLevels listed must
	// be in the same policy as this ServicePerimeter. Referencing a nonexistent
	// AccessLevel will cause an error. If no AccessLevel names are listed,
	// resources within the perimeter can only be accessed via Google Cloud calls
	// with request origins within the perimeter. Example:
	// `accessPolicies/MY_POLICY/accessLevels/MY_LEVEL`. If a single `*` is
	// specified for `access_level`, then all IngressSources will be allowed.
	AccessLevel string `json:"accessLevel,omitempty"`
	// Resource: A Google Cloud resource that is allowed to ingress the perimeter.
	// Requests from these resources will be allowed to access perimeter data.
	// Currently only projects and VPCs are allowed. Project format:
	// `projects/{project_number}` VPC network format:
	// `//compute.googleapis.com/projects/{PROJECT_ID}/global/networks/{NAME}`. The
	// project may be in any Google Cloud organization, not just the organization
	// that the perimeter is defined in. `*` is not allowed, the case of allowing
	// all Google Cloud resources only is not supported.
	Resource string `json:"resource,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AccessLevel") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccessLevel") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

IngressSource: The source that IngressPolicy authorizes access from.

func (IngressSource) MarshalJSON ¶
added in v0.37.0
func (s IngressSource) MarshalJSON() ([]byte, error)
type IngressTo ¶
added in v0.37.0
type IngressTo struct {
	// Operations: A list of ApiOperations allowed to be performed by the sources
	// specified in corresponding IngressFrom in this ServicePerimeter.
	Operations []*ApiOperation `json:"operations,omitempty"`
	// Resources: A list of resources, currently only projects in the form
	// `projects/`, protected by this ServicePerimeter that are allowed to be
	// accessed by sources defined in the corresponding IngressFrom. If a single
	// `*` is specified, then access to all resources inside the perimeter are
	// allowed.
	Resources []string `json:"resources,omitempty"`
	// Roles: IAM roles that represent the set of operations that the sources
	// specified in the corresponding IngressFrom are allowed to perform in this
	// ServicePerimeter.
	Roles []string `json:"roles,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Operations") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Operations") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

IngressTo: Defines the conditions under which an IngressPolicy matches a request. Conditions are based on information about the ApiOperation intended to be performed on the target resource of the request. The request must satisfy what is defined in `operations` AND `resources` in order to match.

func (IngressTo) MarshalJSON ¶
added in v0.37.0
func (s IngressTo) MarshalJSON() ([]byte, error)
type ListAccessLevelsResponse ¶
type ListAccessLevelsResponse struct {
	// AccessLevels: List of the Access Level instances.
	AccessLevels []*AccessLevel `json:"accessLevels,omitempty"`
	// NextPageToken: The pagination token to retrieve the next page of results. If
	// the value is empty, no further results remain.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AccessLevels") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccessLevels") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListAccessLevelsResponse: A response to `ListAccessLevelsRequest`.

func (ListAccessLevelsResponse) MarshalJSON ¶
func (s ListAccessLevelsResponse) MarshalJSON() ([]byte, error)
type ListAccessPoliciesResponse ¶
type ListAccessPoliciesResponse struct {
	// AccessPolicies: List of the AccessPolicy instances.
	AccessPolicies []*AccessPolicy `json:"accessPolicies,omitempty"`
	// NextPageToken: The pagination token to retrieve the next page of results. If
	// the value is empty, no further results remain.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AccessPolicies") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccessPolicies") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListAccessPoliciesResponse: A response to `ListAccessPoliciesRequest`.

func (ListAccessPoliciesResponse) MarshalJSON ¶
func (s ListAccessPoliciesResponse) MarshalJSON() ([]byte, error)
type ListAuthorizedOrgsDescsResponse ¶
added in v0.106.0
type ListAuthorizedOrgsDescsResponse struct {
	// AuthorizedOrgsDescs: List of all the Authorized Orgs Desc instances.
	AuthorizedOrgsDescs []*AuthorizedOrgsDesc `json:"authorizedOrgsDescs,omitempty"`
	// NextPageToken: The pagination token to retrieve the next page of results. If
	// the value is empty, no further results remain.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AuthorizedOrgsDescs") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AuthorizedOrgsDescs") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListAuthorizedOrgsDescsResponse: A response to `ListAuthorizedOrgsDescsRequest`.

func (ListAuthorizedOrgsDescsResponse) MarshalJSON ¶
added in v0.106.0
func (s ListAuthorizedOrgsDescsResponse) MarshalJSON() ([]byte, error)
type ListGcpUserAccessBindingsResponse ¶
added in v0.33.0
type ListGcpUserAccessBindingsResponse struct {
	// GcpUserAccessBindings: GcpUserAccessBinding
	GcpUserAccessBindings []*GcpUserAccessBinding `json:"gcpUserAccessBindings,omitempty"`
	// NextPageToken: Token to get the next page of items. If blank, there are no
	// more items.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "GcpUserAccessBindings") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "GcpUserAccessBindings") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListGcpUserAccessBindingsResponse: Response of ListGcpUserAccessBindings.

func (ListGcpUserAccessBindingsResponse) MarshalJSON ¶
added in v0.33.0
func (s ListGcpUserAccessBindingsResponse) MarshalJSON() ([]byte, error)
type ListOperationsResponse ¶
type ListOperationsResponse struct {
	// NextPageToken: The standard List next-page token.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Operations: A list of operations that matches the specified filter in the
	// request.
	Operations []*Operation `json:"operations,omitempty"`
	// Unreachable: Unordered list. Unreachable resources. Populated when the
	// request sets `ListOperationsRequest.return_partial_success` and reads across
	// collections. For example, when attempting to list all resources across all
	// supported locations.
	Unreachable []string `json:"unreachable,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "NextPageToken") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "NextPageToken") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListOperationsResponse: The response message for Operations.ListOperations.

func (ListOperationsResponse) MarshalJSON ¶
func (s ListOperationsResponse) MarshalJSON() ([]byte, error)
type ListServicePerimetersResponse ¶
type ListServicePerimetersResponse struct {
	// NextPageToken: The pagination token to retrieve the next page of results. If
	// the value is empty, no further results remain.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// ServicePerimeters: List of the Service Perimeter instances.
	ServicePerimeters []*ServicePerimeter `json:"servicePerimeters,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "NextPageToken") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "NextPageToken") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListServicePerimetersResponse: A response to `ListServicePerimetersRequest`.

func (ListServicePerimetersResponse) MarshalJSON ¶
func (s ListServicePerimetersResponse) MarshalJSON() ([]byte, error)
type ListSupportedPermissionsResponse ¶
added in v0.269.0
type ListSupportedPermissionsResponse struct {
	// NextPageToken: The pagination token to retrieve the next page of results. If
	// the value is empty, no further results remain.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// SupportedPermissions: List of VPC-SC supported permissions.
	SupportedPermissions []string `json:"supportedPermissions,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "NextPageToken") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "NextPageToken") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListSupportedPermissionsResponse: A response to `ListSupportedPermissionsRequest`.

func (ListSupportedPermissionsResponse) MarshalJSON ¶
added in v0.269.0
func (s ListSupportedPermissionsResponse) MarshalJSON() ([]byte, error)
type ListSupportedServicesResponse ¶
added in v0.155.0
type ListSupportedServicesResponse struct {
	// NextPageToken: The pagination token to retrieve the next page of results. If
	// the value is empty, no further results remain.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// SupportedServices: List of services supported by VPC Service Controls
	// instances.
	SupportedServices []*SupportedService `json:"supportedServices,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "NextPageToken") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "NextPageToken") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListSupportedServicesResponse: A response to `ListSupportedServicesRequest`.

func (ListSupportedServicesResponse) MarshalJSON ¶
added in v0.155.0
func (s ListSupportedServicesResponse) MarshalJSON() ([]byte, error)
type MethodSelector ¶
added in v0.37.0
type MethodSelector struct {
	// Method: A valid method name for the corresponding `service_name` in
	// ApiOperation. If `*` is used as the value for the `method`, then ALL methods
	// and permissions are allowed.
	Method string `json:"method,omitempty"`
	// Permission: A valid Cloud IAM permission for the corresponding
	// `service_name` in ApiOperation.
	Permission string `json:"permission,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Method") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Method") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

MethodSelector: An allowed method or permission of a service specified in ApiOperation.

func (MethodSelector) MarshalJSON ¶
added in v0.37.0
func (s MethodSelector) MarshalJSON() ([]byte, error)
type Operation ¶
type Operation struct {
	// Done: If the value is `false`, it means the operation is still in progress.
	// If `true`, the operation is completed, and either `error` or `response` is
	// available.
	Done bool `json:"done,omitempty"`
	// Error: The error result of the operation in case of failure or cancellation.
	Error *Status `json:"error,omitempty"`
	// Metadata: Service-specific metadata associated with the operation. It
	// typically contains progress information and common metadata such as create
	// time. Some services might not provide such metadata. Any method that returns
	// a long-running operation should document the metadata type, if any.
	Metadata googleapi.RawMessage `json:"metadata,omitempty"`
	// Name: The server-assigned name, which is only unique within the same service
	// that originally returns it. If you use the default HTTP mapping, the `name`
	// should be a resource name ending with `operations/{unique_id}`.
	Name string `json:"name,omitempty"`
	// Response: The normal, successful response of the operation. If the original
	// method returns no data on success, such as `Delete`, the response is
	// `google.protobuf.Empty`. If the original method is standard
	// `Get`/`Create`/`Update`, the response should be the resource. For other
	// methods, the response should have the type `XxxResponse`, where `Xxx` is the
	// original method name. For example, if the original method name is
	// `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.
	Response googleapi.RawMessage `json:"response,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Done") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Done") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Operation: This resource represents a long-running operation that is the result of a network API call.

func (Operation) MarshalJSON ¶
func (s Operation) MarshalJSON() ([]byte, error)
type OperationsCancelCall ¶
type OperationsCancelCall struct {
	// contains filtered or unexported fields
}
func (*OperationsCancelCall) Context ¶
func (c *OperationsCancelCall) Context(ctx context.Context) *OperationsCancelCall

Context sets the context to be used in this call's Do method.

func (*OperationsCancelCall) Do ¶
func (c *OperationsCancelCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "accesscontextmanager.operations.cancel" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*OperationsCancelCall) Fields ¶
func (c *OperationsCancelCall) Fields(s ...googleapi.Field) *OperationsCancelCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OperationsCancelCall) Header ¶
func (c *OperationsCancelCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type OperationsDeleteCall ¶
type OperationsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*OperationsDeleteCall) Context ¶
func (c *OperationsDeleteCall) Context(ctx context.Context) *OperationsDeleteCall

Context sets the context to be used in this call's Do method.

func (*OperationsDeleteCall) Do ¶
func (c *OperationsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "accesscontextmanager.operations.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*OperationsDeleteCall) Fields ¶
func (c *OperationsDeleteCall) Fields(s ...googleapi.Field) *OperationsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OperationsDeleteCall) Header ¶
func (c *OperationsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type OperationsGetCall ¶
type OperationsGetCall struct {
	// contains filtered or unexported fields
}
func (*OperationsGetCall) Context ¶
func (c *OperationsGetCall) Context(ctx context.Context) *OperationsGetCall

Context sets the context to be used in this call's Do method.

func (*OperationsGetCall) Do ¶
func (c *OperationsGetCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "accesscontextmanager.operations.get" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*OperationsGetCall) Fields ¶
func (c *OperationsGetCall) Fields(s ...googleapi.Field) *OperationsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OperationsGetCall) Header ¶
func (c *OperationsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*OperationsGetCall) IfNoneMatch ¶
func (c *OperationsGetCall) IfNoneMatch(entityTag string) *OperationsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type OperationsListCall ¶
type OperationsListCall struct {
	// contains filtered or unexported fields
}
func (*OperationsListCall) Context ¶
func (c *OperationsListCall) Context(ctx context.Context) *OperationsListCall

Context sets the context to be used in this call's Do method.

func (*OperationsListCall) Do ¶
func (c *OperationsListCall) Do(opts ...googleapi.CallOption) (*ListOperationsResponse, error)

Do executes the "accesscontextmanager.operations.list" call. Any non-2xx status code is an error. Response headers are in either *ListOperationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*OperationsListCall) Fields ¶
func (c *OperationsListCall) Fields(s ...googleapi.Field) *OperationsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OperationsListCall) Filter ¶
func (c *OperationsListCall) Filter(filter string) *OperationsListCall

Filter sets the optional parameter "filter": The standard list filter.

func (*OperationsListCall) Header ¶
func (c *OperationsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*OperationsListCall) IfNoneMatch ¶
func (c *OperationsListCall) IfNoneMatch(entityTag string) *OperationsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*OperationsListCall) PageSize ¶
func (c *OperationsListCall) PageSize(pageSize int64) *OperationsListCall

PageSize sets the optional parameter "pageSize": The standard list page size.

func (*OperationsListCall) PageToken ¶
func (c *OperationsListCall) PageToken(pageToken string) *OperationsListCall

PageToken sets the optional parameter "pageToken": The standard list page token.

func (*OperationsListCall) Pages ¶
func (c *OperationsListCall) Pages(ctx context.Context, f func(*ListOperationsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*OperationsListCall) ReturnPartialSuccess ¶
added in v0.253.0
func (c *OperationsListCall) ReturnPartialSuccess(returnPartialSuccess bool) *OperationsListCall

ReturnPartialSuccess sets the optional parameter "returnPartialSuccess": When set to `true`, operations that are reachable are returned as normal, and those that are unreachable are returned in the ListOperationsResponse.unreachable field. This can only be `true` when reading across collections. For example, when `parent` is set to "projects/example/locations/-". This field is not supported by default and will result in an `UNIMPLEMENTED` error if set unless explicitly documented otherwise in service or product specific documentation.

type OperationsService ¶
type OperationsService struct {
	// contains filtered or unexported fields
}
func NewOperationsService ¶
func NewOperationsService(s *Service) *OperationsService
func (*OperationsService) Cancel ¶
func (r *OperationsService) Cancel(name string, canceloperationrequest *CancelOperationRequest) *OperationsCancelCall

Cancel: Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of `1`, corresponding to `Code.CANCELLED`.

- name: The name of the operation resource to be cancelled.

func (*OperationsService) Delete ¶
func (r *OperationsService) Delete(name string) *OperationsDeleteCall

Delete: Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

- name: The name of the operation resource to be deleted.

func (*OperationsService) Get ¶
func (r *OperationsService) Get(name string) *OperationsGetCall

Get: Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

- name: The name of the operation resource.

func (*OperationsService) List ¶
func (r *OperationsService) List(name string) *OperationsListCall

List: Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.

- name: The name of the operation's parent resource.

type OrganizationsGcpUserAccessBindingsCreateCall ¶
added in v0.33.0
type OrganizationsGcpUserAccessBindingsCreateCall struct {
	// contains filtered or unexported fields
}
func (*OrganizationsGcpUserAccessBindingsCreateCall) Context ¶
added in v0.33.0
func (c *OrganizationsGcpUserAccessBindingsCreateCall) Context(ctx context.Context) *OrganizationsGcpUserAccessBindingsCreateCall

Context sets the context to be used in this call's Do method.

func (*OrganizationsGcpUserAccessBindingsCreateCall) Do ¶
added in v0.33.0
func (c *OrganizationsGcpUserAccessBindingsCreateCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "accesscontextmanager.organizations.gcpUserAccessBindings.create" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*OrganizationsGcpUserAccessBindingsCreateCall) Fields ¶
added in v0.33.0
func (c *OrganizationsGcpUserAccessBindingsCreateCall) Fields(s ...googleapi.Field) *OrganizationsGcpUserAccessBindingsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OrganizationsGcpUserAccessBindingsCreateCall) Header ¶
added in v0.33.0
func (c *OrganizationsGcpUserAccessBindingsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type OrganizationsGcpUserAccessBindingsDeleteCall ¶
added in v0.33.0
type OrganizationsGcpUserAccessBindingsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*OrganizationsGcpUserAccessBindingsDeleteCall) Context ¶
added in v0.33.0
func (c *OrganizationsGcpUserAccessBindingsDeleteCall) Context(ctx context.Context) *OrganizationsGcpUserAccessBindingsDeleteCall

Context sets the context to be used in this call's Do method.

func (*OrganizationsGcpUserAccessBindingsDeleteCall) Do ¶
added in v0.33.0
func (c *OrganizationsGcpUserAccessBindingsDeleteCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "accesscontextmanager.organizations.gcpUserAccessBindings.delete" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*OrganizationsGcpUserAccessBindingsDeleteCall) Fields ¶
added in v0.33.0
func (c *OrganizationsGcpUserAccessBindingsDeleteCall) Fields(s ...googleapi.Field) *OrganizationsGcpUserAccessBindingsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OrganizationsGcpUserAccessBindingsDeleteCall) Header ¶
added in v0.33.0
func (c *OrganizationsGcpUserAccessBindingsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type OrganizationsGcpUserAccessBindingsGetCall ¶
added in v0.33.0
type OrganizationsGcpUserAccessBindingsGetCall struct {
	// contains filtered or unexported fields
}
func (*OrganizationsGcpUserAccessBindingsGetCall) Context ¶
added in v0.33.0
func (c *OrganizationsGcpUserAccessBindingsGetCall) Context(ctx context.Context) *OrganizationsGcpUserAccessBindingsGetCall

Context sets the context to be used in this call's Do method.

func (*OrganizationsGcpUserAccessBindingsGetCall) Do ¶
added in v0.33.0
func (c *OrganizationsGcpUserAccessBindingsGetCall) Do(opts ...googleapi.CallOption) (*GcpUserAccessBinding, error)

Do executes the "accesscontextmanager.organizations.gcpUserAccessBindings.get" call. Any non-2xx status code is an error. Response headers are in either *GcpUserAccessBinding.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*OrganizationsGcpUserAccessBindingsGetCall) Fields ¶
added in v0.33.0
func (c *OrganizationsGcpUserAccessBindingsGetCall) Fields(s ...googleapi.Field) *OrganizationsGcpUserAccessBindingsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OrganizationsGcpUserAccessBindingsGetCall) Header ¶
added in v0.33.0
func (c *OrganizationsGcpUserAccessBindingsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*OrganizationsGcpUserAccessBindingsGetCall) IfNoneMatch ¶
added in v0.33.0
func (c *OrganizationsGcpUserAccessBindingsGetCall) IfNoneMatch(entityTag string) *OrganizationsGcpUserAccessBindingsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type OrganizationsGcpUserAccessBindingsListCall ¶
added in v0.33.0
type OrganizationsGcpUserAccessBindingsListCall struct {
	// contains filtered or unexported fields
}
func (*OrganizationsGcpUserAccessBindingsListCall) Context ¶
added in v0.33.0
func (c *OrganizationsGcpUserAccessBindingsListCall) Context(ctx context.Context) *OrganizationsGcpUserAccessBindingsListCall

Context sets the context to be used in this call's Do method.

func (*OrganizationsGcpUserAccessBindingsListCall) Do ¶
added in v0.33.0
func (c *OrganizationsGcpUserAccessBindingsListCall) Do(opts ...googleapi.CallOption) (*ListGcpUserAccessBindingsResponse, error)

Do executes the "accesscontextmanager.organizations.gcpUserAccessBindings.list" call. Any non-2xx status code is an error. Response headers are in either *ListGcpUserAccessBindingsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*OrganizationsGcpUserAccessBindingsListCall) Fields ¶
added in v0.33.0
func (c *OrganizationsGcpUserAccessBindingsListCall) Fields(s ...googleapi.Field) *OrganizationsGcpUserAccessBindingsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OrganizationsGcpUserAccessBindingsListCall) Header ¶
added in v0.33.0
func (c *OrganizationsGcpUserAccessBindingsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*OrganizationsGcpUserAccessBindingsListCall) IfNoneMatch ¶
added in v0.33.0
func (c *OrganizationsGcpUserAccessBindingsListCall) IfNoneMatch(entityTag string) *OrganizationsGcpUserAccessBindingsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*OrganizationsGcpUserAccessBindingsListCall) PageSize ¶
added in v0.33.0
func (c *OrganizationsGcpUserAccessBindingsListCall) PageSize(pageSize int64) *OrganizationsGcpUserAccessBindingsListCall

PageSize sets the optional parameter "pageSize": Maximum number of items to return. The server may return fewer items. If left blank, the server may return any number of items.

func (*OrganizationsGcpUserAccessBindingsListCall) PageToken ¶
added in v0.33.0
func (c *OrganizationsGcpUserAccessBindingsListCall) PageToken(pageToken string) *OrganizationsGcpUserAccessBindingsListCall

PageToken sets the optional parameter "pageToken": If left blank, returns the first page. To enumerate all items, use the next_page_token from your previous list operation.

func (*OrganizationsGcpUserAccessBindingsListCall) Pages ¶
added in v0.33.0
func (c *OrganizationsGcpUserAccessBindingsListCall) Pages(ctx context.Context, f func(*ListGcpUserAccessBindingsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type OrganizationsGcpUserAccessBindingsPatchCall ¶
added in v0.33.0
type OrganizationsGcpUserAccessBindingsPatchCall struct {
	// contains filtered or unexported fields
}
func (*OrganizationsGcpUserAccessBindingsPatchCall) Append ¶
added in v0.202.0
func (c *OrganizationsGcpUserAccessBindingsPatchCall) Append(append bool) *OrganizationsGcpUserAccessBindingsPatchCall

Append sets the optional parameter "append": This field controls whether or not certain repeated settings in the update request overwrite or append to existing settings on the binding. If true, then append. Otherwise overwrite. So far, only scoped_access_settings with session_settings supports appending. Global access_levels, access_levels in scoped_access_settings, dry_run_access_levels, and session_settings are not compatible with append functionality, and the request will return an error if append=true when these settings are in the update_mask. The request will also return an error if append=true when "scoped_access_settings" is not set in the update_mask.

func (*OrganizationsGcpUserAccessBindingsPatchCall) Context ¶
added in v0.33.0
func (c *OrganizationsGcpUserAccessBindingsPatchCall) Context(ctx context.Context) *OrganizationsGcpUserAccessBindingsPatchCall

Context sets the context to be used in this call's Do method.

func (*OrganizationsGcpUserAccessBindingsPatchCall) Do ¶
added in v0.33.0
func (c *OrganizationsGcpUserAccessBindingsPatchCall) Do(opts ...googleapi.CallOption) (*Operation, error)

Do executes the "accesscontextmanager.organizations.gcpUserAccessBindings.patch" call. Any non-2xx status code is an error. Response headers are in either *Operation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*OrganizationsGcpUserAccessBindingsPatchCall) Fields ¶
added in v0.33.0
func (c *OrganizationsGcpUserAccessBindingsPatchCall) Fields(s ...googleapi.Field) *OrganizationsGcpUserAccessBindingsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OrganizationsGcpUserAccessBindingsPatchCall) Header ¶
added in v0.33.0
func (c *OrganizationsGcpUserAccessBindingsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*OrganizationsGcpUserAccessBindingsPatchCall) UpdateMask ¶
added in v0.33.0
func (c *OrganizationsGcpUserAccessBindingsPatchCall) UpdateMask(updateMask string) *OrganizationsGcpUserAccessBindingsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. Only the fields specified in this mask are updated. Because name and group_key cannot be changed, update_mask is required and may only contain the following fields: `access_levels`, `dry_run_access_levels`, `session_settings`, `scoped_access_settings`. update_mask { paths: "access_levels" }

type OrganizationsGcpUserAccessBindingsService ¶
added in v0.33.0
type OrganizationsGcpUserAccessBindingsService struct {
	// contains filtered or unexported fields
}
func NewOrganizationsGcpUserAccessBindingsService ¶
added in v0.33.0
func NewOrganizationsGcpUserAccessBindingsService(s *Service) *OrganizationsGcpUserAccessBindingsService
func (*OrganizationsGcpUserAccessBindingsService) Create ¶
added in v0.33.0
func (r *OrganizationsGcpUserAccessBindingsService) Create(parent string, gcpuseraccessbinding *GcpUserAccessBinding) *OrganizationsGcpUserAccessBindingsCreateCall

Create: Creates a GcpUserAccessBinding. If the client specifies a name, the server ignores it. Fails if a resource already exists with the same group_key. Completion of this long-running operation does not necessarily signify that the new binding is deployed onto all affected users, which may take more time.

- parent: Example: "organizations/256".

func (*OrganizationsGcpUserAccessBindingsService) Delete ¶
added in v0.33.0
func (r *OrganizationsGcpUserAccessBindingsService) Delete(name string) *OrganizationsGcpUserAccessBindingsDeleteCall

Delete: Deletes a GcpUserAccessBinding. Completion of this long-running operation does not necessarily signify that the binding deletion is deployed onto all affected users, which may take more time.

- name: Example: "organizations/256/gcpUserAccessBindings/b3-BhcX_Ud5N".

func (*OrganizationsGcpUserAccessBindingsService) Get ¶
added in v0.33.0
func (r *OrganizationsGcpUserAccessBindingsService) Get(name string) *OrganizationsGcpUserAccessBindingsGetCall

Get: Gets the GcpUserAccessBinding with the given name.

- name: Example: "organizations/256/gcpUserAccessBindings/b3-BhcX_Ud5N".

func (*OrganizationsGcpUserAccessBindingsService) List ¶
added in v0.33.0
func (r *OrganizationsGcpUserAccessBindingsService) List(parent string) *OrganizationsGcpUserAccessBindingsListCall

List: Lists all GcpUserAccessBindings for a Google Cloud organization.

- parent: Example: "organizations/256".

func (*OrganizationsGcpUserAccessBindingsService) Patch ¶
added in v0.33.0
func (r *OrganizationsGcpUserAccessBindingsService) Patch(name string, gcpuseraccessbinding *GcpUserAccessBinding) *OrganizationsGcpUserAccessBindingsPatchCall

Patch: Updates a GcpUserAccessBinding. Completion of this long-running operation does not necessarily signify that the changed binding is deployed onto all affected users, which may take more time.

name: Immutable. Assigned by the server during creation. The last segment has an arbitrary length and has only URI unreserved characters (as defined by RFC 3986 Section 2.3 (https://tools.ietf.org/html/rfc3986#section-2.3)). Should not be specified by the client during creation. Example: "organizations/256/gcpUserAccessBindings/b3-BhcX_Ud5N".
type OrganizationsService ¶
added in v0.33.0
type OrganizationsService struct {
	GcpUserAccessBindings *OrganizationsGcpUserAccessBindingsService
	// contains filtered or unexported fields
}
func NewOrganizationsService ¶
added in v0.33.0
func NewOrganizationsService(s *Service) *OrganizationsService
type OsConstraint ¶
type OsConstraint struct {
	// MinimumVersion: The minimum allowed OS version. If not set, any version of
	// this OS satisfies the constraint. Format: "major.minor.patch". Examples:
	// "10.5.301", "9.2.1".
	MinimumVersion string `json:"minimumVersion,omitempty"`
	// OsType: Required. The allowed OS type.
	//
	// Possible values:
	//   "OS_UNSPECIFIED" - The operating system of the device is not specified or
	// not known.
	//   "DESKTOP_MAC" - A desktop Mac operating system.
	//   "DESKTOP_WINDOWS" - A desktop Windows operating system.
	//   "DESKTOP_LINUX" - A desktop Linux operating system.
	//   "DESKTOP_CHROME_OS" - A desktop ChromeOS operating system.
	//   "ANDROID" - An Android operating system.
	//   "IOS" - An iOS operating system.
	OsType string `json:"osType,omitempty"`
	// RequireVerifiedChromeOs: Only allows requests from devices with a verified
	// Chrome OS. Verifications includes requirements that the device is
	// enterprise-managed, conformant to domain policies, and the caller has
	// permission to call the API targeted by the request.
	RequireVerifiedChromeOs bool `json:"requireVerifiedChromeOs,omitempty"`
	// ForceSendFields is a list of field names (e.g. "MinimumVersion") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "MinimumVersion") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

OsConstraint: A restriction on the OS type and version of devices making requests.

func (OsConstraint) MarshalJSON ¶
func (s OsConstraint) MarshalJSON() ([]byte, error)
type PermissionsListCall ¶
added in v0.269.0
type PermissionsListCall struct {
	// contains filtered or unexported fields
}
func (*PermissionsListCall) Context ¶
added in v0.269.0
func (c *PermissionsListCall) Context(ctx context.Context) *PermissionsListCall

Context sets the context to be used in this call's Do method.

func (*PermissionsListCall) Do ¶
added in v0.269.0
func (c *PermissionsListCall) Do(opts ...googleapi.CallOption) (*ListSupportedPermissionsResponse, error)

Do executes the "accesscontextmanager.permissions.list" call. Any non-2xx status code is an error. Response headers are in either *ListSupportedPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*PermissionsListCall) Fields ¶
added in v0.269.0
func (c *PermissionsListCall) Fields(s ...googleapi.Field) *PermissionsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*PermissionsListCall) Header ¶
added in v0.269.0
func (c *PermissionsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*PermissionsListCall) IfNoneMatch ¶
added in v0.269.0
func (c *PermissionsListCall) IfNoneMatch(entityTag string) *PermissionsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*PermissionsListCall) PageSize ¶
added in v0.269.0
func (c *PermissionsListCall) PageSize(pageSize int64) *PermissionsListCall

PageSize sets the optional parameter "pageSize": This flag specifies the maximum number of services to return per page. Default is 100.

func (*PermissionsListCall) PageToken ¶
added in v0.269.0
func (c *PermissionsListCall) PageToken(pageToken string) *PermissionsListCall

PageToken sets the optional parameter "pageToken": Token to start on a later page. Default is the first page.

func (*PermissionsListCall) Pages ¶
added in v0.269.0
func (c *PermissionsListCall) Pages(ctx context.Context, f func(*ListSupportedPermissionsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type PermissionsService ¶
added in v0.269.0
type PermissionsService struct {
	// contains filtered or unexported fields
}
func NewPermissionsService ¶
added in v0.269.0
func NewPermissionsService(s *Service) *PermissionsService
func (*PermissionsService) List ¶
added in v0.269.0
func (r *PermissionsService) List() *PermissionsListCall

List: Lists all supported permissions in VPCSC Granular Controls.

type Policy ¶
added in v0.63.0
type Policy struct {
	// AuditConfigs: Specifies cloud audit logging configuration for this policy.
	AuditConfigs []*AuditConfig `json:"auditConfigs,omitempty"`
	// Bindings: Associates a list of `members`, or principals, with a `role`.
	// Optionally, may specify a `condition` that determines how and when the
	// `bindings` are applied. Each of the `bindings` must contain at least one
	// principal. The `bindings` in a `Policy` can refer to up to 1,500 principals;
	// up to 250 of these principals can be Google groups. Each occurrence of a
	// principal counts towards these limits. For example, if the `bindings` grant
	// 50 different roles to `user:alice@example.com`, and not to any other
	// principal, then you can add another 1,450 principals to the `bindings` in
	// the `Policy`.
	Bindings []*Binding `json:"bindings,omitempty"`
	// Etag: `etag` is used for optimistic concurrency control as a way to help
	// prevent simultaneous updates of a policy from overwriting each other. It is
	// strongly suggested that systems make use of the `etag` in the
	// read-modify-write cycle to perform policy updates in order to avoid race
	// conditions: An `etag` is returned in the response to `getIamPolicy`, and
	// systems are expected to put that etag in the request to `setIamPolicy` to
	// ensure that their change will be applied to the same version of the policy.
	// **Important:** If you use IAM Conditions, you must include the `etag` field
	// whenever you call `setIamPolicy`. If you omit this field, then IAM allows
	// you to overwrite a version `3` policy with a version `1` policy, and all of
	// the conditions in the version `3` policy are lost.
	Etag string `json:"etag,omitempty"`
	// Version: Specifies the format of the policy. Valid values are `0`, `1`, and
	// `3`. Requests that specify an invalid value are rejected. Any operation that
	// affects conditional role bindings must specify version `3`. This requirement
	// applies to the following operations: * Getting a policy that includes a
	// conditional role binding * Adding a conditional role binding to a policy *
	// Changing a conditional role binding in a policy * Removing any role binding,
	// with or without a condition, from a policy that includes conditions
	// **Important:** If you use IAM Conditions, you must include the `etag` field
	// whenever you call `setIamPolicy`. If you omit this field, then IAM allows
	// you to overwrite a version `3` policy with a version `1` policy, and all of
	// the conditions in the version `3` policy are lost. If a policy does not
	// include any conditions, operations on that policy may specify any valid
	// version or leave the field unset. To learn which resources support
	// conditions in their IAM policies, see the IAM documentation
	// (https://cloud.google.com/iam/help/conditions/resource-policies).
	Version int64 `json:"version,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AuditConfigs") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AuditConfigs") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Policy: An Identity and Access Management (IAM) policy, which specifies access controls for Google Cloud resources. A `Policy` is a collection of `bindings`. A `binding` binds one or more `members`, or principals, to a single `role`. Principals can be user accounts, service accounts, Google groups, and domains (such as G Suite). A `role` is a named list of permissions; each `role` can be an IAM predefined role or a user-created custom role. For some types of Google Cloud resources, a `binding` can also specify a `condition`, which is a logical expression that allows access to a resource only if the expression evaluates to `true`. A condition can add constraints based on attributes of the request, the resource, or both. To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies). **JSON example:** ``` { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": [ "user:eve@example.com" ], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01T00:00:00.000Z')", } } ], "etag": "BwWWja0YfJA=", "version": 3 } ``` **YAML example:** ``` bindings: - members: - user:mike@example.com - group:admins@example.com - domain:google.com - serviceAccount:my-project-id@appspot.gserviceaccount.com role: roles/resourcemanager.organizationAdmin - members: - user:eve@example.com role: roles/resourcemanager.organizationViewer condition: title: expirable access description: Does not grant access after Sep 2020 expression: request.time < timestamp('2020-10-01T00:00:00.000Z') etag: BwWWja0YfJA= version: 3 ``` For a description of IAM and its features, see the IAM documentation (https://cloud.google.com/iam/docs/).

func (Policy) MarshalJSON ¶
added in v0.63.0
func (s Policy) MarshalJSON() ([]byte, error)
type ReplaceAccessLevelsRequest ¶
added in v0.18.0
type ReplaceAccessLevelsRequest struct {
	// AccessLevels: Required. The desired Access Levels that should replace all
	// existing Access Levels in the Access Policy.
	AccessLevels []*AccessLevel `json:"accessLevels,omitempty"`
	// Etag: Optional. The etag for the version of the Access Policy that this
	// replace operation is to be performed on. If, at the time of replace, the
	// etag for the Access Policy stored in Access Context Manager is different
	// from the specified etag, then the replace operation will not be performed
	// and the call will fail. This field is not required. If etag is not provided,
	// the operation will be performed as if a valid etag is provided.
	Etag string `json:"etag,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AccessLevels") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccessLevels") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ReplaceAccessLevelsRequest: A request to replace all existing Access Levels in an Access Policy with the Access Levels provided. This is done atomically.

func (ReplaceAccessLevelsRequest) MarshalJSON ¶
added in v0.18.0
func (s ReplaceAccessLevelsRequest) MarshalJSON() ([]byte, error)
type ReplaceAccessLevelsResponse ¶
added in v0.18.0
type ReplaceAccessLevelsResponse struct {
	// AccessLevels: List of the Access Level instances.
	AccessLevels []*AccessLevel `json:"accessLevels,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AccessLevels") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccessLevels") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ReplaceAccessLevelsResponse: A response to ReplaceAccessLevelsRequest. This will be put inside of Operation.response field.

func (ReplaceAccessLevelsResponse) MarshalJSON ¶
added in v0.18.0
func (s ReplaceAccessLevelsResponse) MarshalJSON() ([]byte, error)
type ReplaceServicePerimetersRequest ¶
added in v0.18.0
type ReplaceServicePerimetersRequest struct {
	// Etag: Optional. The etag for the version of the Access Policy that this
	// replace operation is to be performed on. If, at the time of replace, the
	// etag for the Access Policy stored in Access Context Manager is different
	// from the specified etag, then the replace operation will not be performed
	// and the call will fail. This field is not required. If etag is not provided,
	// the operation will be performed as if a valid etag is provided.
	Etag string `json:"etag,omitempty"`
	// ServicePerimeters: Required. The desired Service Perimeters that should
	// replace all existing Service Perimeters in the Access Policy.
	ServicePerimeters []*ServicePerimeter `json:"servicePerimeters,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Etag") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Etag") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ReplaceServicePerimetersRequest: A request to replace all existing Service Perimeters in an Access Policy with the Service Perimeters provided. This is done atomically.

func (ReplaceServicePerimetersRequest) MarshalJSON ¶
added in v0.18.0
func (s ReplaceServicePerimetersRequest) MarshalJSON() ([]byte, error)
type ReplaceServicePerimetersResponse ¶
added in v0.18.0
type ReplaceServicePerimetersResponse struct {
	// ServicePerimeters: List of the Service Perimeter instances.
	ServicePerimeters []*ServicePerimeter `json:"servicePerimeters,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ServicePerimeters") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ServicePerimeters") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ReplaceServicePerimetersResponse: A response to ReplaceServicePerimetersRequest. This will be put inside of Operation.response field.

func (ReplaceServicePerimetersResponse) MarshalJSON ¶
added in v0.18.0
func (s ReplaceServicePerimetersResponse) MarshalJSON() ([]byte, error)
type ScopedAccessSettings ¶
added in v0.198.0
type ScopedAccessSettings struct {
	// ActiveSettings: Optional. Access settings for this scoped access settings.
	// This field may be empty if dry_run_settings is set.
	ActiveSettings *AccessSettings `json:"activeSettings,omitempty"`
	// DryRunSettings: Optional. Dry-run access settings for this scoped access
	// settings. This field may be empty if active_settings is set.
	DryRunSettings *AccessSettings `json:"dryRunSettings,omitempty"`
	// Scope: Optional. Application, etc. to which the access settings will be
	// applied to. Implicitly, this is the scoped access settings key; as such, it
	// must be unique and non-empty.
	Scope *AccessScope `json:"scope,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ActiveSettings") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ActiveSettings") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ScopedAccessSettings: A relationship between access settings and its scope.

func (ScopedAccessSettings) MarshalJSON ¶
added in v0.198.0
func (s ScopedAccessSettings) MarshalJSON() ([]byte, error)
type Service ¶
type Service struct {
	BasePath  string // API endpoint base URL
	UserAgent string // optional additional User-Agent fragment

	AccessPolicies *AccessPoliciesService

	Operations *OperationsService

	Organizations *OrganizationsService

	Permissions *PermissionsService

	Services *ServicesService
	// contains filtered or unexported fields
}
func
New
DEPRECATED
func NewService ¶
added in v0.3.0
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)

NewService creates a new Service.

type ServicePerimeter ¶
type ServicePerimeter struct {
	// Description: Description of the `ServicePerimeter` and its use. Does not
	// affect behavior.
	Description string `json:"description,omitempty"`
	// Etag: Optional. An opaque identifier for the current version of the
	// `ServicePerimeter`. This identifier does not follow any specific format. If
	// an etag is not provided, the operation will be performed as if a valid etag
	// is provided.
	Etag string `json:"etag,omitempty"`
	// Name: Identifier. Resource name for the `ServicePerimeter`. Format:
	// `accessPolicies/{access_policy}/servicePerimeters/{service_perimeter}`. The
	// `service_perimeter` component must begin with a letter, followed by
	// alphanumeric characters or `_`. After you create a `ServicePerimeter`, you
	// cannot change its `name`.
	Name string `json:"name,omitempty"`
	// PerimeterType: Perimeter type indicator. A single project or VPC network is
	// allowed to be a member of single regular perimeter, but multiple service
	// perimeter bridges. A project cannot be a included in a perimeter bridge
	// without being included in regular perimeter. For perimeter bridges, the
	// restricted service list as well as access level lists must be empty.
	//
	// Possible values:
	//   "PERIMETER_TYPE_REGULAR" - Regular Perimeter. When no value is specified,
	// the perimeter uses this type.
	//   "PERIMETER_TYPE_BRIDGE" - Perimeter Bridge.
	PerimeterType string `json:"perimeterType,omitempty"`
	// Spec: Proposed (or dry run) ServicePerimeter configuration. This
	// configuration allows to specify and test ServicePerimeter configuration
	// without enforcing actual access restrictions. Only allowed to be set when
	// the "use_explicit_dry_run_spec" flag is set.
	Spec *ServicePerimeterConfig `json:"spec,omitempty"`
	// Status: Current ServicePerimeter configuration. Specifies sets of resources,
	// restricted services and access levels that determine perimeter content and
	// boundaries.
	Status *ServicePerimeterConfig `json:"status,omitempty"`
	// Title: Human readable title. Must be unique within the Policy.
	Title string `json:"title,omitempty"`
	// UseExplicitDryRunSpec: Use explicit dry run spec flag. Ordinarily, a dry-run
	// spec implicitly exists for all Service Perimeters, and that spec is
	// identical to the status for those Service Perimeters. When this flag is set,
	// it inhibits the generation of the implicit spec, thereby allowing the user
	// to explicitly provide a configuration ("spec") to use in a dry-run version
	// of the Service Perimeter. This allows the user to test changes to the
	// enforced config ("status") without actually enforcing them. This testing is
	// done through analyzing the differences between currently enforced and
	// suggested restrictions. use_explicit_dry_run_spec must bet set to True if
	// any of the fields in the spec are set to non-default values.
	UseExplicitDryRunSpec bool `json:"useExplicitDryRunSpec,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Description") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Description") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ServicePerimeter: `ServicePerimeter` describes a set of Google Cloud resources which can freely import and export data amongst themselves, but not export outside of the `ServicePerimeter`. If a request with a source within this `ServicePerimeter` has a target outside of the `ServicePerimeter`, the request will be blocked. Otherwise the request is allowed. There are two types of Service Perimeter - Regular and Bridge. Regular Service Perimeters cannot overlap, a single Google Cloud project or VPC network can only belong to a single regular Service Perimeter. Service Perimeter Bridges can contain only Google Cloud projects as members, a single Google Cloud project may belong to multiple Service Perimeter Bridges.

func (ServicePerimeter) MarshalJSON ¶
func (s ServicePerimeter) MarshalJSON() ([]byte, error)
type ServicePerimeterConfig ¶
type ServicePerimeterConfig struct {
	// AccessLevels: A list of `AccessLevel` resource names that allow resources
	// within the `ServicePerimeter` to be accessed from the internet.
	// `AccessLevels` listed must be in the same policy as this `ServicePerimeter`.
	// Referencing a nonexistent `AccessLevel` is a syntax error. If no
	// `AccessLevel` names are listed, resources within the perimeter can only be
	// accessed via Google Cloud calls with request origins within the perimeter.
	// Example: "accessPolicies/MY_POLICY/accessLevels/MY_LEVEL". For Service
	// Perimeter Bridge, must be empty.
	AccessLevels []string `json:"accessLevels,omitempty"`
	// EgressPolicies: List of EgressPolicies to apply to the perimeter. A
	// perimeter may have multiple EgressPolicies, each of which is evaluated
	// separately. Access is granted if any EgressPolicy grants it. Must be empty
	// for a perimeter bridge.
	EgressPolicies []*EgressPolicy `json:"egressPolicies,omitempty"`
	// IngressPolicies: List of IngressPolicies to apply to the perimeter. A
	// perimeter may have multiple IngressPolicies, each of which is evaluated
	// separately. Access is granted if any Ingress Policy grants it. Must be empty
	// for a perimeter bridge.
	IngressPolicies []*IngressPolicy `json:"ingressPolicies,omitempty"`
	// Resources: A list of Google Cloud resources that are inside of the service
	// perimeter. Currently only projects and VPCs are allowed. Project format:
	// `projects/{project_number}` VPC network format:
	// `//compute.googleapis.com/projects/{PROJECT_ID}/global/networks/{NAME}`.
	Resources []string `json:"resources,omitempty"`
	// RestrictedServices: Google Cloud services that are subject to the Service
	// Perimeter restrictions. For example, if `storage.googleapis.com` is
	// specified, access to the storage buckets inside the perimeter must meet the
	// perimeter's access restrictions.
	RestrictedServices []string `json:"restrictedServices,omitempty"`
	// VpcAccessibleServices: Configuration for APIs allowed within Perimeter.
	VpcAccessibleServices *VpcAccessibleServices `json:"vpcAccessibleServices,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AccessLevels") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AccessLevels") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ServicePerimeterConfig: `ServicePerimeterConfig` specifies a set of Google Cloud resources that describe specific Service Perimeter configuration.

func (ServicePerimeterConfig) MarshalJSON ¶
func (s ServicePerimeterConfig) MarshalJSON() ([]byte, error)
type ServicesGetCall ¶
added in v0.155.0
type ServicesGetCall struct {
	// contains filtered or unexported fields
}
func (*ServicesGetCall) Context ¶
added in v0.155.0
func (c *ServicesGetCall) Context(ctx context.Context) *ServicesGetCall

Context sets the context to be used in this call's Do method.

func (*ServicesGetCall) Do ¶
added in v0.155.0
func (c *ServicesGetCall) Do(opts ...googleapi.CallOption) (*SupportedService, error)

Do executes the "accesscontextmanager.services.get" call. Any non-2xx status code is an error. Response headers are in either *SupportedService.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ServicesGetCall) Fields ¶
added in v0.155.0
func (c *ServicesGetCall) Fields(s ...googleapi.Field) *ServicesGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ServicesGetCall) Header ¶
added in v0.155.0
func (c *ServicesGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ServicesGetCall) IfNoneMatch ¶
added in v0.155.0
func (c *ServicesGetCall) IfNoneMatch(entityTag string) *ServicesGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ServicesListCall ¶
added in v0.155.0
type ServicesListCall struct {
	// contains filtered or unexported fields
}
func (*ServicesListCall) Context ¶
added in v0.155.0
func (c *ServicesListCall) Context(ctx context.Context) *ServicesListCall

Context sets the context to be used in this call's Do method.

func (*ServicesListCall) Do ¶
added in v0.155.0
func (c *ServicesListCall) Do(opts ...googleapi.CallOption) (*ListSupportedServicesResponse, error)

Do executes the "accesscontextmanager.services.list" call. Any non-2xx status code is an error. Response headers are in either *ListSupportedServicesResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ServicesListCall) Fields ¶
added in v0.155.0
func (c *ServicesListCall) Fields(s ...googleapi.Field) *ServicesListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ServicesListCall) Header ¶
added in v0.155.0
func (c *ServicesListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ServicesListCall) IfNoneMatch ¶
added in v0.155.0
func (c *ServicesListCall) IfNoneMatch(entityTag string) *ServicesListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ServicesListCall) PageSize ¶
added in v0.155.0
func (c *ServicesListCall) PageSize(pageSize int64) *ServicesListCall

PageSize sets the optional parameter "pageSize": This flag specifies the maximum number of services to return per page. Default is 100.

func (*ServicesListCall) PageToken ¶
added in v0.155.0
func (c *ServicesListCall) PageToken(pageToken string) *ServicesListCall

PageToken sets the optional parameter "pageToken": Token to start on a later page. Default is the first page.

func (*ServicesListCall) Pages ¶
added in v0.155.0
func (c *ServicesListCall) Pages(ctx context.Context, f func(*ListSupportedServicesResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ServicesService ¶
added in v0.155.0
type ServicesService struct {
	// contains filtered or unexported fields
}
func NewServicesService ¶
added in v0.155.0
func NewServicesService(s *Service) *ServicesService
func (*ServicesService) Get ¶
added in v0.155.0
func (r *ServicesService) Get(name string) *ServicesGetCall

Get: Returns a VPC-SC supported service based on the service name.

name: The name of the service to get information about. The names must be in the same format as used in defining a service perimeter, for example, `storage.googleapis.com`.
func (*ServicesService) List ¶
added in v0.155.0
func (r *ServicesService) List() *ServicesListCall

List: Lists all VPC-SC supported services.

type SessionSettings ¶
added in v0.204.0
type SessionSettings struct {
	// MaxInactivity: Optional. How long a user is allowed to take between actions
	// before a new access token must be issued. Only set for Google Cloud apps.
	MaxInactivity string `json:"maxInactivity,omitempty"`
	// SessionLength: Optional. The session length. Setting this field to zero is
	// equal to disabling session. Also can set infinite session by flipping the
	// enabled bit to false below. If use_oidc_max_age is true, for OIDC apps, the
	// session length will be the minimum of this field and OIDC max_age param.
	SessionLength string `json:"sessionLength,omitempty"`
	// SessionLengthEnabled: Optional. This field enables or disables Google Cloud
	// session length. When false, all fields set above will be disregarded and the
	// session length is basically infinite.
	SessionLengthEnabled bool `json:"sessionLengthEnabled,omitempty"`
	// SessionReauthMethod: Optional. Session method when user's Google Cloud
	// session is up.
	//
	// Possible values:
	//   "SESSION_REAUTH_METHOD_UNSPECIFIED" - If method is undefined in the API,
	// LOGIN will be used by default.
	//   "LOGIN" - The user will be prompted to perform regular login. Users who
	// are enrolled for two-step verification and haven't chosen "Remember this
	// computer" will be prompted for their second factor.
	//   "SECURITY_KEY" - The user will be prompted to authenticate using their
	// security key. If no security key has been configured, then authentication
	// will fallback to LOGIN.
	//   "PASSWORD" - The user will be prompted for their password.
	SessionReauthMethod string `json:"sessionReauthMethod,omitempty"`
	// UseOidcMaxAge: Optional. Only useful for OIDC apps. When false, the OIDC
	// max_age param, if passed in the authentication request will be ignored. When
	// true, the re-auth period will be the minimum of the session_length field and
	// the max_age OIDC param.
	UseOidcMaxAge bool `json:"useOidcMaxAge,omitempty"`
	// ForceSendFields is a list of field names (e.g. "MaxInactivity") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "MaxInactivity") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SessionSettings: Stores settings related to Google Cloud Session Length including session duration, the type of challenge (i.e. method) they should face when their session expires, and other related settings.

func (SessionSettings) MarshalJSON ¶
added in v0.204.0
func (s SessionSettings) MarshalJSON() ([]byte, error)
type SetIamPolicyRequest ¶
added in v0.63.0
type SetIamPolicyRequest struct {
	// Policy: REQUIRED: The complete policy to be applied to the `resource`. The
	// size of the policy is limited to a few 10s of KB. An empty policy is a valid
	// policy but certain Google Cloud services (such as Projects) might reject
	// them.
	Policy *Policy `json:"policy,omitempty"`
	// UpdateMask: OPTIONAL: A FieldMask specifying which fields of the policy to
	// modify. Only the fields in the mask will be modified. If no mask is
	// provided, the following default mask is used: `paths: "bindings, etag"
	UpdateMask string `json:"updateMask,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Policy") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Policy") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SetIamPolicyRequest: Request message for `SetIamPolicy` method.

func (SetIamPolicyRequest) MarshalJSON ¶
added in v0.63.0
func (s SetIamPolicyRequest) MarshalJSON() ([]byte, error)
type Status ¶
type Status struct {
	// Code: The status code, which should be an enum value of google.rpc.Code.
	Code int64 `json:"code,omitempty"`
	// Details: A list of messages that carry the error details. There is a common
	// set of message types for APIs to use.
	Details []googleapi.RawMessage `json:"details,omitempty"`
	// Message: A developer-facing error message, which should be in English. Any
	// user-facing error message should be localized and sent in the
	// google.rpc.Status.details field, or localized by the client.
	Message string `json:"message,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Code") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Code") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Status: The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by gRPC (https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the API Design Guide (https://cloud.google.com/apis/design/errors).

func (Status) MarshalJSON ¶
func (s Status) MarshalJSON() ([]byte, error)
type SupportedService ¶
added in v0.155.0
type SupportedService struct {
	// AvailableOnRestrictedVip: True if the service is available on the restricted
	// VIP. Services on the restricted VIP typically either support VPC Service
	// Controls or are core infrastructure services required for the functioning of
	// Google Cloud.
	AvailableOnRestrictedVip bool `json:"availableOnRestrictedVip,omitempty"`
	// KnownLimitations: True if the service is supported with some limitations.
	// Check documentation
	// (https://cloud.google.com/vpc-service-controls/docs/supported-products) for
	// details.
	KnownLimitations bool `json:"knownLimitations,omitempty"`
	// Name: The service name or address of the supported service, such as
	// `service.googleapis.com`.
	Name string `json:"name,omitempty"`
	// ServiceSupportStage: The support stage of the service.
	//
	// Possible values:
	//   "SERVICE_SUPPORT_STAGE_UNSPECIFIED" - Do not use this default value.
	//   "GA" - GA features are open to all developers and are considered stable
	// and fully qualified for production use.
	//   "PREVIEW" - PREVIEW indicates a pre-release stage where the product is
	// functionally complete but undergoing real-world testing.
	//   "DEPRECATED" - Deprecated features are scheduled to be shut down and
	// removed.
	ServiceSupportStage string `json:"serviceSupportStage,omitempty"`
	// SupportStage: The support stage of the service.
	//
	// Possible values:
	//   "LAUNCH_STAGE_UNSPECIFIED" - Do not use this default value.
	//   "UNIMPLEMENTED" - The feature is not yet implemented. Users can not use
	// it.
	//   "PRELAUNCH" - Prelaunch features are hidden from users and are only
	// visible internally.
	//   "EARLY_ACCESS" - Early Access features are limited to a closed group of
	// testers. To use these features, you must sign up in advance and sign a
	// Trusted Tester agreement (which includes confidentiality provisions). These
	// features may be unstable, changed in backward-incompatible ways, and are not
	// guaranteed to be released.
	//   "ALPHA" - Alpha is a limited availability test for releases before they
	// are cleared for widespread use. By Alpha, all significant design issues are
	// resolved and we are in the process of verifying functionality. Alpha
	// customers need to apply for access, agree to applicable terms, and have
	// their projects allowlisted. Alpha releases don't have to be feature
	// complete, no SLAs are provided, and there are no technical support
	// obligations, but they will be far enough along that customers can actually
	// use them in test environments or for limited-use tests -- just like they
	// would in normal production cases.
	//   "BETA" - Beta is the point at which we are ready to open a release for any
	// customer to use. There are no SLA or technical support obligations in a Beta
	// release. Products will be complete from a feature perspective, but may have
	// some open outstanding issues. Beta releases are suitable for limited
	// production use cases.
	//   "GA" - GA features are open to all developers and are considered stable
	// and fully qualified for production use.
	//   "DEPRECATED" - Deprecated features are scheduled to be shut down and
	// removed. For more information, see the "Deprecation Policy" section of our
	// [Terms of Service](https://cloud.google.com/terms/) and the [Google Cloud
	// Platform Subject to the Deprecation
	// Policy](https://cloud.google.com/terms/deprecation) documentation.
	SupportStage string `json:"supportStage,omitempty"`
	// SupportedMethods: The list of the supported methods. This field exists only
	// in response to GetSupportedService
	SupportedMethods []*MethodSelector `json:"supportedMethods,omitempty"`
	// Title: The name of the supported product, such as 'Cloud Product API'.
	Title string `json:"title,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AvailableOnRestrictedVip")
	// to unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AvailableOnRestrictedVip") to
	// include in API requests with the JSON null value. By default, fields with
	// empty values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

SupportedService: `SupportedService` specifies the VPC Service Controls and its properties.

func (SupportedService) MarshalJSON ¶
added in v0.155.0
func (s SupportedService) MarshalJSON() ([]byte, error)
type TestIamPermissionsRequest ¶
added in v0.63.0
type TestIamPermissionsRequest struct {
	// Permissions: The set of permissions to check for the `resource`. Permissions
	// with wildcards (such as `*` or `storage.*`) are not allowed. For more
	// information see IAM Overview
	// (https://cloud.google.com/iam/docs/overview#permissions).
	Permissions []string `json:"permissions,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Permissions") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Permissions") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

TestIamPermissionsRequest: Request message for `TestIamPermissions` method.

func (TestIamPermissionsRequest) MarshalJSON ¶
added in v0.63.0
func (s TestIamPermissionsRequest) MarshalJSON() ([]byte, error)
type TestIamPermissionsResponse ¶
added in v0.63.0
type TestIamPermissionsResponse struct {
	// Permissions: A subset of `TestPermissionsRequest.permissions` that the
	// caller is allowed.
	Permissions []string `json:"permissions,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Permissions") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Permissions") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

TestIamPermissionsResponse: Response message for `TestIamPermissions` method.

func (TestIamPermissionsResponse) MarshalJSON ¶
added in v0.63.0
func (s TestIamPermissionsResponse) MarshalJSON() ([]byte, error)
type VpcAccessibleServices ¶
added in v0.18.0
type VpcAccessibleServices struct {
	// AllowedServices: The list of APIs usable within the Service Perimeter. Must
	// be empty unless 'enable_restriction' is True. You can specify a list of
	// individual services, as well as include the 'RESTRICTED-SERVICES' value,
	// which automatically includes all of the services protected by the perimeter.
	AllowedServices []string `json:"allowedServices,omitempty"`
	// EnableRestriction: Whether to restrict API calls within the Service
	// Perimeter to the list of APIs specified in 'allowed_services'.
	EnableRestriction bool `json:"enableRestriction,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AllowedServices") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AllowedServices") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

VpcAccessibleServices: Specifies how APIs are allowed to communicate within the Service Perimeter.

func (VpcAccessibleServices) MarshalJSON ¶
added in v0.18.0
func (s VpcAccessibleServices) MarshalJSON() ([]byte, error)
type VpcNetworkSource ¶
added in v0.141.0
type VpcNetworkSource struct {
	// VpcSubnetwork: Sub-segment ranges of a VPC network.
	VpcSubnetwork *VpcSubNetwork `json:"vpcSubnetwork,omitempty"`
	// ForceSendFields is a list of field names (e.g. "VpcSubnetwork") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "VpcSubnetwork") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

VpcNetworkSource: The originating network source in Google Cloud.

func (VpcNetworkSource) MarshalJSON ¶
added in v0.141.0
func (s VpcNetworkSource) MarshalJSON() ([]byte, error)
type VpcSubNetwork ¶
added in v0.141.0
type VpcSubNetwork struct {
	// Network: Required. Network name. If the network is not part of the
	// organization, the `compute.network.get` permission must be granted to the
	// caller. Format:
	// `//compute.googleapis.com/projects/{PROJECT_ID}/global/networks/{NETWORK_NAME
	// }` Example:
	// `//compute.googleapis.com/projects/my-project/global/networks/network-1`
	Network string `json:"network,omitempty"`
	// VpcIpSubnetworks: CIDR block IP subnetwork specification. The IP address
	// must be an IPv4 address and can be a public or private IP address. Note that
	// for a CIDR IP address block, the specified IP address portion must be
	// properly truncated (i.e. all the host bits must be zero) or the input is
	// considered malformed. For example, "192.0.2.0/24" is accepted but
	// "192.0.2.1/24" is not. If empty, all IP addresses are allowed.
	VpcIpSubnetworks []string `json:"vpcIpSubnetworks,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Network") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Network") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

VpcSubNetwork: Sub-segment ranges inside of a VPC Network.

func (VpcSubNetwork) MarshalJSON ¶
added in v0.141.0
func (s VpcSubNetwork) MarshalJSON() ([]byte, error)
 Source Files ¶
View all Source files
accesscontextmanager-gen.go
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
