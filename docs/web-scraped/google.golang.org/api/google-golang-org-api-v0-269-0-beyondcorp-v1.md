# Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/beyondcorp/v1

Title: beyondcorp package - google.golang.org/api/beyondcorp/v1 - Go Packages

URL Source: https://pkg.go.dev/google.golang.org/api@v0.269.0/beyondcorp/v1

Markdown Content:
Skip to Main Content
Why Go
Learn
Docs
Packages
Community
Discover Packages
 
google.golang.org/api
 
beyondcorp
 
v1
beyondcorp
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

Package beyondcorp provides access to the BeyondCorp API.

For product documentation, see: https://cloud.google.com/

Library status ¶

These client libraries are officially supported by Google. However, this library is considered complete and is in maintenance mode. This means that we will address critical bugs and security issues but will not add any new features.

When possible, we recommend using our newer [Cloud Client Libraries for Go](https://pkg.go.dev/cloud.google.com/go) that are still actively being worked and iterated on.

Creating a client ¶

Usage example:

import "google.golang.org/api/beyondcorp/v1"
...
ctx := context.Background()
beyondcorpService, err := beyondcorp.NewService(ctx)


In this example, Google Application Default Credentials are used for authentication. For information on how to create and obtain Application Default Credentials, see https://developers.google.com/identity/protocols/application-default-credentials.

Other authentication options ¶

To use an API key for authentication (note: some APIs do not support API keys), use google.golang.org/api/option.WithAPIKey:

beyondcorpService, err := beyondcorp.NewService(ctx, option.WithAPIKey("AIza..."))


To use an OAuth token (e.g., a user token obtained via a three-legged OAuth flow, use google.golang.org/api/option.WithTokenSource:

config := &oauth2.Config{...}
// ...
token, err := config.Exchange(ctx, ...)
beyondcorpService, err := beyondcorp.NewService(ctx, option.WithTokenSource(config.TokenSource(ctx, token)))


See google.golang.org/api/option.ClientOption for details on options.

Index ¶
Constants
type AllocatedConnection
func (s AllocatedConnection) MarshalJSON() ([]byte, error)
type AppGateway
func (s AppGateway) MarshalJSON() ([]byte, error)
type AppGatewayOperationMetadata
func (s AppGatewayOperationMetadata) MarshalJSON() ([]byte, error)
type CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfig
func (s CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfig) MarshalJSON() ([]byte, error)
type CloudSecurityZerotrustApplinkAppConnectorProtoConnectorDetails
type CloudSecurityZerotrustApplinkAppConnectorProtoGateway
func (s CloudSecurityZerotrustApplinkAppConnectorProtoGateway) MarshalJSON() ([]byte, error)
type CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetails
type Empty
type GoogleCloudBeyondcorpAppconnectionsV1AppConnection
func (s GoogleCloudBeyondcorpAppconnectionsV1AppConnection) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpoint
func (s GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpoint) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGateway
func (s GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGateway) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadata
func (s GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponse
func (s GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponse
func (s GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetails
func (s GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetails) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadata
func (s GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1AppConnector
func (s GoogleCloudBeyondcorpAppconnectorsV1AppConnector) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfig
func (s GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfig) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadata
func (s GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfo
func (s GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfo) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccount
func (s GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccount) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetails
func (s GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetails) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1ImageConfig
func (s GoogleCloudBeyondcorpAppconnectorsV1ImageConfig) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponse
func (s GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1NotificationConfig
func (s GoogleCloudBeyondcorpAppconnectorsV1NotificationConfig) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfig
func (s GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfig) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetails
type GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequest
func (s GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequest) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponse
func (s GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1ResourceInfo
func (s GoogleCloudBeyondcorpAppconnectorsV1ResourceInfo) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadata
func (s GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetails
func (s GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetails) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetails
type GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadata
func (s GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadata
func (s GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadata
func (s GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetails
func (s GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetails) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetails
type GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadata
func (s GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadata
func (s GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1Application
func (s GoogleCloudBeyondcorpSecuritygatewaysV1Application) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationUpstream
func (s GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationUpstream) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationUpstreamExternal
func (s GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationUpstreamExternal) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationUpstreamNetwork
func (s GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationUpstreamNetwork) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeaders
func (s GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeaders) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedDeviceInfo
func (s GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedDeviceInfo) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedGroupInfo
func (s GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedGroupInfo) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedUserInfo
func (s GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedUserInfo) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1EgressPolicy
func (s GoogleCloudBeyondcorpSecuritygatewaysV1EgressPolicy) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1Endpoint
func (s GoogleCloudBeyondcorpSecuritygatewaysV1Endpoint) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1EndpointMatcher
func (s GoogleCloudBeyondcorpSecuritygatewaysV1EndpointMatcher) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1Hub
func (s GoogleCloudBeyondcorpSecuritygatewaysV1Hub) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1InternetGateway
func (s GoogleCloudBeyondcorpSecuritygatewaysV1InternetGateway) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1ListApplicationsResponse
func (s GoogleCloudBeyondcorpSecuritygatewaysV1ListApplicationsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1ListSecurityGatewaysResponse
func (s GoogleCloudBeyondcorpSecuritygatewaysV1ListSecurityGatewaysResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1ProxyProtocolConfig
func (s GoogleCloudBeyondcorpSecuritygatewaysV1ProxyProtocolConfig) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1SecurityGateway
func (s GoogleCloudBeyondcorpSecuritygatewaysV1SecurityGateway) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1SecurityGatewayOperationMetadata
func (s GoogleCloudBeyondcorpSecuritygatewaysV1SecurityGatewayOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1ServiceDiscovery
func (s GoogleCloudBeyondcorpSecuritygatewaysV1ServiceDiscovery) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1ServiceDiscoveryApiGateway
func (s GoogleCloudBeyondcorpSecuritygatewaysV1ServiceDiscoveryApiGateway) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1ServiceDiscoveryApiGatewayOperationDescriptor
func (s GoogleCloudBeyondcorpSecuritygatewaysV1ServiceDiscoveryApiGatewayOperationDescriptor) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaSecurityGatewayOperationMetadata
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaSecurityGatewayOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudLocationListLocationsResponse
func (s GoogleCloudLocationListLocationsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudLocationLocation
func (s GoogleCloudLocationLocation) MarshalJSON() ([]byte, error)
type GoogleIamV1AuditConfig
func (s GoogleIamV1AuditConfig) MarshalJSON() ([]byte, error)
type GoogleIamV1AuditLogConfig
func (s GoogleIamV1AuditLogConfig) MarshalJSON() ([]byte, error)
type GoogleIamV1Binding
func (s GoogleIamV1Binding) MarshalJSON() ([]byte, error)
type GoogleIamV1Policy
func (s GoogleIamV1Policy) MarshalJSON() ([]byte, error)
type GoogleIamV1SetIamPolicyRequest
func (s GoogleIamV1SetIamPolicyRequest) MarshalJSON() ([]byte, error)
type GoogleIamV1TestIamPermissionsRequest
func (s GoogleIamV1TestIamPermissionsRequest) MarshalJSON() ([]byte, error)
type GoogleIamV1TestIamPermissionsResponse
func (s GoogleIamV1TestIamPermissionsResponse) MarshalJSON() ([]byte, error)
type GoogleLongrunningCancelOperationRequest
type GoogleLongrunningListOperationsResponse
func (s GoogleLongrunningListOperationsResponse) MarshalJSON() ([]byte, error)
type GoogleLongrunningOperation
func (s GoogleLongrunningOperation) MarshalJSON() ([]byte, error)
type GoogleRpcStatus
func (s GoogleRpcStatus) MarshalJSON() ([]byte, error)
type GoogleTypeExpr
func (s GoogleTypeExpr) MarshalJSON() ([]byte, error)
type ListAppGatewaysResponse
func (s ListAppGatewaysResponse) MarshalJSON() ([]byte, error)
type OrganizationsLocationsOperationsCancelCall
func (c *OrganizationsLocationsOperationsCancelCall) Context(ctx context.Context) *OrganizationsLocationsOperationsCancelCall
func (c *OrganizationsLocationsOperationsCancelCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *OrganizationsLocationsOperationsCancelCall) Fields(s ...googleapi.Field) *OrganizationsLocationsOperationsCancelCall
func (c *OrganizationsLocationsOperationsCancelCall) Header() http.Header
type OrganizationsLocationsOperationsDeleteCall
func (c *OrganizationsLocationsOperationsDeleteCall) Context(ctx context.Context) *OrganizationsLocationsOperationsDeleteCall
func (c *OrganizationsLocationsOperationsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *OrganizationsLocationsOperationsDeleteCall) Fields(s ...googleapi.Field) *OrganizationsLocationsOperationsDeleteCall
func (c *OrganizationsLocationsOperationsDeleteCall) Header() http.Header
type OrganizationsLocationsOperationsGetCall
func (c *OrganizationsLocationsOperationsGetCall) Context(ctx context.Context) *OrganizationsLocationsOperationsGetCall
func (c *OrganizationsLocationsOperationsGetCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *OrganizationsLocationsOperationsGetCall) Fields(s ...googleapi.Field) *OrganizationsLocationsOperationsGetCall
func (c *OrganizationsLocationsOperationsGetCall) Header() http.Header
func (c *OrganizationsLocationsOperationsGetCall) IfNoneMatch(entityTag string) *OrganizationsLocationsOperationsGetCall
type OrganizationsLocationsOperationsListCall
func (c *OrganizationsLocationsOperationsListCall) Context(ctx context.Context) *OrganizationsLocationsOperationsListCall
func (c *OrganizationsLocationsOperationsListCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningListOperationsResponse, error)
func (c *OrganizationsLocationsOperationsListCall) Fields(s ...googleapi.Field) *OrganizationsLocationsOperationsListCall
func (c *OrganizationsLocationsOperationsListCall) Filter(filter string) *OrganizationsLocationsOperationsListCall
func (c *OrganizationsLocationsOperationsListCall) Header() http.Header
func (c *OrganizationsLocationsOperationsListCall) IfNoneMatch(entityTag string) *OrganizationsLocationsOperationsListCall
func (c *OrganizationsLocationsOperationsListCall) PageSize(pageSize int64) *OrganizationsLocationsOperationsListCall
func (c *OrganizationsLocationsOperationsListCall) PageToken(pageToken string) *OrganizationsLocationsOperationsListCall
func (c *OrganizationsLocationsOperationsListCall) Pages(ctx context.Context, f func(*GoogleLongrunningListOperationsResponse) error) error
func (c *OrganizationsLocationsOperationsListCall) ReturnPartialSuccess(returnPartialSuccess bool) *OrganizationsLocationsOperationsListCall
type OrganizationsLocationsOperationsService
func NewOrganizationsLocationsOperationsService(s *Service) *OrganizationsLocationsOperationsService
func (r *OrganizationsLocationsOperationsService) Cancel(name string, ...) *OrganizationsLocationsOperationsCancelCall
func (r *OrganizationsLocationsOperationsService) Delete(name string) *OrganizationsLocationsOperationsDeleteCall
func (r *OrganizationsLocationsOperationsService) Get(name string) *OrganizationsLocationsOperationsGetCall
func (r *OrganizationsLocationsOperationsService) List(name string) *OrganizationsLocationsOperationsListCall
type OrganizationsLocationsService
func NewOrganizationsLocationsService(s *Service) *OrganizationsLocationsService
type OrganizationsService
func NewOrganizationsService(s *Service) *OrganizationsService
type ProjectsLocationsAppConnectionsCreateCall
func (c *ProjectsLocationsAppConnectionsCreateCall) AppConnectionId(appConnectionId string) *ProjectsLocationsAppConnectionsCreateCall
func (c *ProjectsLocationsAppConnectionsCreateCall) Context(ctx context.Context) *ProjectsLocationsAppConnectionsCreateCall
func (c *ProjectsLocationsAppConnectionsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsAppConnectionsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectionsCreateCall
func (c *ProjectsLocationsAppConnectionsCreateCall) Header() http.Header
func (c *ProjectsLocationsAppConnectionsCreateCall) RequestId(requestId string) *ProjectsLocationsAppConnectionsCreateCall
func (c *ProjectsLocationsAppConnectionsCreateCall) ValidateOnly(validateOnly bool) *ProjectsLocationsAppConnectionsCreateCall
type ProjectsLocationsAppConnectionsDeleteCall
func (c *ProjectsLocationsAppConnectionsDeleteCall) Context(ctx context.Context) *ProjectsLocationsAppConnectionsDeleteCall
func (c *ProjectsLocationsAppConnectionsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsAppConnectionsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectionsDeleteCall
func (c *ProjectsLocationsAppConnectionsDeleteCall) Header() http.Header
func (c *ProjectsLocationsAppConnectionsDeleteCall) RequestId(requestId string) *ProjectsLocationsAppConnectionsDeleteCall
func (c *ProjectsLocationsAppConnectionsDeleteCall) ValidateOnly(validateOnly bool) *ProjectsLocationsAppConnectionsDeleteCall
type ProjectsLocationsAppConnectionsGetCall
func (c *ProjectsLocationsAppConnectionsGetCall) Context(ctx context.Context) *ProjectsLocationsAppConnectionsGetCall
func (c *ProjectsLocationsAppConnectionsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpAppconnectionsV1AppConnection, error)
func (c *ProjectsLocationsAppConnectionsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectionsGetCall
func (c *ProjectsLocationsAppConnectionsGetCall) Header() http.Header
func (c *ProjectsLocationsAppConnectionsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsAppConnectionsGetCall
type ProjectsLocationsAppConnectionsGetIamPolicyCall
func (c *ProjectsLocationsAppConnectionsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsAppConnectionsGetIamPolicyCall
func (c *ProjectsLocationsAppConnectionsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)
func (c *ProjectsLocationsAppConnectionsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectionsGetIamPolicyCall
func (c *ProjectsLocationsAppConnectionsGetIamPolicyCall) Header() http.Header
func (c *ProjectsLocationsAppConnectionsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsAppConnectionsGetIamPolicyCall
func (c *ProjectsLocationsAppConnectionsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsAppConnectionsGetIamPolicyCall
type ProjectsLocationsAppConnectionsListCall
func (c *ProjectsLocationsAppConnectionsListCall) Context(ctx context.Context) *ProjectsLocationsAppConnectionsListCall
func (c *ProjectsLocationsAppConnectionsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponse, error)
func (c *ProjectsLocationsAppConnectionsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectionsListCall
func (c *ProjectsLocationsAppConnectionsListCall) Filter(filter string) *ProjectsLocationsAppConnectionsListCall
func (c *ProjectsLocationsAppConnectionsListCall) Header() http.Header
func (c *ProjectsLocationsAppConnectionsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsAppConnectionsListCall
func (c *ProjectsLocationsAppConnectionsListCall) OrderBy(orderBy string) *ProjectsLocationsAppConnectionsListCall
func (c *ProjectsLocationsAppConnectionsListCall) PageSize(pageSize int64) *ProjectsLocationsAppConnectionsListCall
func (c *ProjectsLocationsAppConnectionsListCall) PageToken(pageToken string) *ProjectsLocationsAppConnectionsListCall
func (c *ProjectsLocationsAppConnectionsListCall) Pages(ctx context.Context, ...) error
type ProjectsLocationsAppConnectionsPatchCall
func (c *ProjectsLocationsAppConnectionsPatchCall) AllowMissing(allowMissing bool) *ProjectsLocationsAppConnectionsPatchCall
func (c *ProjectsLocationsAppConnectionsPatchCall) Context(ctx context.Context) *ProjectsLocationsAppConnectionsPatchCall
func (c *ProjectsLocationsAppConnectionsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsAppConnectionsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectionsPatchCall
func (c *ProjectsLocationsAppConnectionsPatchCall) Header() http.Header
func (c *ProjectsLocationsAppConnectionsPatchCall) RequestId(requestId string) *ProjectsLocationsAppConnectionsPatchCall
func (c *ProjectsLocationsAppConnectionsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsAppConnectionsPatchCall
func (c *ProjectsLocationsAppConnectionsPatchCall) ValidateOnly(validateOnly bool) *ProjectsLocationsAppConnectionsPatchCall
type ProjectsLocationsAppConnectionsResolveCall
func (c *ProjectsLocationsAppConnectionsResolveCall) AppConnectorId(appConnectorId string) *ProjectsLocationsAppConnectionsResolveCall
func (c *ProjectsLocationsAppConnectionsResolveCall) Context(ctx context.Context) *ProjectsLocationsAppConnectionsResolveCall
func (c *ProjectsLocationsAppConnectionsResolveCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponse, error)
func (c *ProjectsLocationsAppConnectionsResolveCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectionsResolveCall
func (c *ProjectsLocationsAppConnectionsResolveCall) Header() http.Header
func (c *ProjectsLocationsAppConnectionsResolveCall) IfNoneMatch(entityTag string) *ProjectsLocationsAppConnectionsResolveCall
func (c *ProjectsLocationsAppConnectionsResolveCall) PageSize(pageSize int64) *ProjectsLocationsAppConnectionsResolveCall
func (c *ProjectsLocationsAppConnectionsResolveCall) PageToken(pageToken string) *ProjectsLocationsAppConnectionsResolveCall
func (c *ProjectsLocationsAppConnectionsResolveCall) Pages(ctx context.Context, ...) error
type ProjectsLocationsAppConnectionsService
func NewProjectsLocationsAppConnectionsService(s *Service) *ProjectsLocationsAppConnectionsService
func (r *ProjectsLocationsAppConnectionsService) Create(parent string, ...) *ProjectsLocationsAppConnectionsCreateCall
func (r *ProjectsLocationsAppConnectionsService) Delete(name string) *ProjectsLocationsAppConnectionsDeleteCall
func (r *ProjectsLocationsAppConnectionsService) Get(name string) *ProjectsLocationsAppConnectionsGetCall
func (r *ProjectsLocationsAppConnectionsService) GetIamPolicy(resource string) *ProjectsLocationsAppConnectionsGetIamPolicyCall
func (r *ProjectsLocationsAppConnectionsService) List(parent string) *ProjectsLocationsAppConnectionsListCall
func (r *ProjectsLocationsAppConnectionsService) Patch(name string, ...) *ProjectsLocationsAppConnectionsPatchCall
func (r *ProjectsLocationsAppConnectionsService) Resolve(parent string) *ProjectsLocationsAppConnectionsResolveCall
func (r *ProjectsLocationsAppConnectionsService) SetIamPolicy(resource string, ...) *ProjectsLocationsAppConnectionsSetIamPolicyCall
func (r *ProjectsLocationsAppConnectionsService) TestIamPermissions(resource string, ...) *ProjectsLocationsAppConnectionsTestIamPermissionsCall
type ProjectsLocationsAppConnectionsSetIamPolicyCall
func (c *ProjectsLocationsAppConnectionsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsAppConnectionsSetIamPolicyCall
func (c *ProjectsLocationsAppConnectionsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)
func (c *ProjectsLocationsAppConnectionsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectionsSetIamPolicyCall
func (c *ProjectsLocationsAppConnectionsSetIamPolicyCall) Header() http.Header
type ProjectsLocationsAppConnectionsTestIamPermissionsCall
func (c *ProjectsLocationsAppConnectionsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsAppConnectionsTestIamPermissionsCall
func (c *ProjectsLocationsAppConnectionsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1TestIamPermissionsResponse, error)
func (c *ProjectsLocationsAppConnectionsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectionsTestIamPermissionsCall
func (c *ProjectsLocationsAppConnectionsTestIamPermissionsCall) Header() http.Header
type ProjectsLocationsAppConnectorsCreateCall
func (c *ProjectsLocationsAppConnectorsCreateCall) AppConnectorId(appConnectorId string) *ProjectsLocationsAppConnectorsCreateCall
func (c *ProjectsLocationsAppConnectorsCreateCall) Context(ctx context.Context) *ProjectsLocationsAppConnectorsCreateCall
func (c *ProjectsLocationsAppConnectorsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsAppConnectorsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectorsCreateCall
func (c *ProjectsLocationsAppConnectorsCreateCall) Header() http.Header
func (c *ProjectsLocationsAppConnectorsCreateCall) RequestId(requestId string) *ProjectsLocationsAppConnectorsCreateCall
func (c *ProjectsLocationsAppConnectorsCreateCall) ValidateOnly(validateOnly bool) *ProjectsLocationsAppConnectorsCreateCall
type ProjectsLocationsAppConnectorsDeleteCall
func (c *ProjectsLocationsAppConnectorsDeleteCall) Context(ctx context.Context) *ProjectsLocationsAppConnectorsDeleteCall
func (c *ProjectsLocationsAppConnectorsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsAppConnectorsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectorsDeleteCall
func (c *ProjectsLocationsAppConnectorsDeleteCall) Header() http.Header
func (c *ProjectsLocationsAppConnectorsDeleteCall) RequestId(requestId string) *ProjectsLocationsAppConnectorsDeleteCall
func (c *ProjectsLocationsAppConnectorsDeleteCall) ValidateOnly(validateOnly bool) *ProjectsLocationsAppConnectorsDeleteCall
type ProjectsLocationsAppConnectorsGetCall
func (c *ProjectsLocationsAppConnectorsGetCall) Context(ctx context.Context) *ProjectsLocationsAppConnectorsGetCall
func (c *ProjectsLocationsAppConnectorsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpAppconnectorsV1AppConnector, error)
func (c *ProjectsLocationsAppConnectorsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectorsGetCall
func (c *ProjectsLocationsAppConnectorsGetCall) Header() http.Header
func (c *ProjectsLocationsAppConnectorsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsAppConnectorsGetCall
type ProjectsLocationsAppConnectorsGetIamPolicyCall
func (c *ProjectsLocationsAppConnectorsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsAppConnectorsGetIamPolicyCall
func (c *ProjectsLocationsAppConnectorsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)
func (c *ProjectsLocationsAppConnectorsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectorsGetIamPolicyCall
func (c *ProjectsLocationsAppConnectorsGetIamPolicyCall) Header() http.Header
func (c *ProjectsLocationsAppConnectorsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsAppConnectorsGetIamPolicyCall
func (c *ProjectsLocationsAppConnectorsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsAppConnectorsGetIamPolicyCall
type ProjectsLocationsAppConnectorsListCall
func (c *ProjectsLocationsAppConnectorsListCall) Context(ctx context.Context) *ProjectsLocationsAppConnectorsListCall
func (c *ProjectsLocationsAppConnectorsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponse, error)
func (c *ProjectsLocationsAppConnectorsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectorsListCall
func (c *ProjectsLocationsAppConnectorsListCall) Filter(filter string) *ProjectsLocationsAppConnectorsListCall
func (c *ProjectsLocationsAppConnectorsListCall) Header() http.Header
func (c *ProjectsLocationsAppConnectorsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsAppConnectorsListCall
func (c *ProjectsLocationsAppConnectorsListCall) OrderBy(orderBy string) *ProjectsLocationsAppConnectorsListCall
func (c *ProjectsLocationsAppConnectorsListCall) PageSize(pageSize int64) *ProjectsLocationsAppConnectorsListCall
func (c *ProjectsLocationsAppConnectorsListCall) PageToken(pageToken string) *ProjectsLocationsAppConnectorsListCall
func (c *ProjectsLocationsAppConnectorsListCall) Pages(ctx context.Context, ...) error
type ProjectsLocationsAppConnectorsPatchCall
func (c *ProjectsLocationsAppConnectorsPatchCall) Context(ctx context.Context) *ProjectsLocationsAppConnectorsPatchCall
func (c *ProjectsLocationsAppConnectorsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsAppConnectorsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectorsPatchCall
func (c *ProjectsLocationsAppConnectorsPatchCall) Header() http.Header
func (c *ProjectsLocationsAppConnectorsPatchCall) RequestId(requestId string) *ProjectsLocationsAppConnectorsPatchCall
func (c *ProjectsLocationsAppConnectorsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsAppConnectorsPatchCall
func (c *ProjectsLocationsAppConnectorsPatchCall) ValidateOnly(validateOnly bool) *ProjectsLocationsAppConnectorsPatchCall
type ProjectsLocationsAppConnectorsReportStatusCall
func (c *ProjectsLocationsAppConnectorsReportStatusCall) Context(ctx context.Context) *ProjectsLocationsAppConnectorsReportStatusCall
func (c *ProjectsLocationsAppConnectorsReportStatusCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsAppConnectorsReportStatusCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectorsReportStatusCall
func (c *ProjectsLocationsAppConnectorsReportStatusCall) Header() http.Header
type ProjectsLocationsAppConnectorsResolveInstanceConfigCall
func (c *ProjectsLocationsAppConnectorsResolveInstanceConfigCall) Context(ctx context.Context) *ProjectsLocationsAppConnectorsResolveInstanceConfigCall
func (c *ProjectsLocationsAppConnectorsResolveInstanceConfigCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponse, error)
func (c *ProjectsLocationsAppConnectorsResolveInstanceConfigCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectorsResolveInstanceConfigCall
func (c *ProjectsLocationsAppConnectorsResolveInstanceConfigCall) Header() http.Header
func (c *ProjectsLocationsAppConnectorsResolveInstanceConfigCall) IfNoneMatch(entityTag string) *ProjectsLocationsAppConnectorsResolveInstanceConfigCall
type ProjectsLocationsAppConnectorsService
func NewProjectsLocationsAppConnectorsService(s *Service) *ProjectsLocationsAppConnectorsService
func (r *ProjectsLocationsAppConnectorsService) Create(parent string, ...) *ProjectsLocationsAppConnectorsCreateCall
func (r *ProjectsLocationsAppConnectorsService) Delete(name string) *ProjectsLocationsAppConnectorsDeleteCall
func (r *ProjectsLocationsAppConnectorsService) Get(name string) *ProjectsLocationsAppConnectorsGetCall
func (r *ProjectsLocationsAppConnectorsService) GetIamPolicy(resource string) *ProjectsLocationsAppConnectorsGetIamPolicyCall
func (r *ProjectsLocationsAppConnectorsService) List(parent string) *ProjectsLocationsAppConnectorsListCall
func (r *ProjectsLocationsAppConnectorsService) Patch(name string, ...) *ProjectsLocationsAppConnectorsPatchCall
func (r *ProjectsLocationsAppConnectorsService) ReportStatus(appConnector string, ...) *ProjectsLocationsAppConnectorsReportStatusCall
func (r *ProjectsLocationsAppConnectorsService) ResolveInstanceConfig(appConnector string) *ProjectsLocationsAppConnectorsResolveInstanceConfigCall
func (r *ProjectsLocationsAppConnectorsService) SetIamPolicy(resource string, ...) *ProjectsLocationsAppConnectorsSetIamPolicyCall
func (r *ProjectsLocationsAppConnectorsService) TestIamPermissions(resource string, ...) *ProjectsLocationsAppConnectorsTestIamPermissionsCall
type ProjectsLocationsAppConnectorsSetIamPolicyCall
func (c *ProjectsLocationsAppConnectorsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsAppConnectorsSetIamPolicyCall
func (c *ProjectsLocationsAppConnectorsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)
func (c *ProjectsLocationsAppConnectorsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectorsSetIamPolicyCall
func (c *ProjectsLocationsAppConnectorsSetIamPolicyCall) Header() http.Header
type ProjectsLocationsAppConnectorsTestIamPermissionsCall
func (c *ProjectsLocationsAppConnectorsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsAppConnectorsTestIamPermissionsCall
func (c *ProjectsLocationsAppConnectorsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1TestIamPermissionsResponse, error)
func (c *ProjectsLocationsAppConnectorsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectorsTestIamPermissionsCall
func (c *ProjectsLocationsAppConnectorsTestIamPermissionsCall) Header() http.Header
type ProjectsLocationsAppGatewaysCreateCall
func (c *ProjectsLocationsAppGatewaysCreateCall) AppGatewayId(appGatewayId string) *ProjectsLocationsAppGatewaysCreateCall
func (c *ProjectsLocationsAppGatewaysCreateCall) Context(ctx context.Context) *ProjectsLocationsAppGatewaysCreateCall
func (c *ProjectsLocationsAppGatewaysCreateCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsAppGatewaysCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppGatewaysCreateCall
func (c *ProjectsLocationsAppGatewaysCreateCall) Header() http.Header
func (c *ProjectsLocationsAppGatewaysCreateCall) RequestId(requestId string) *ProjectsLocationsAppGatewaysCreateCall
func (c *ProjectsLocationsAppGatewaysCreateCall) ValidateOnly(validateOnly bool) *ProjectsLocationsAppGatewaysCreateCall
type ProjectsLocationsAppGatewaysDeleteCall
func (c *ProjectsLocationsAppGatewaysDeleteCall) Context(ctx context.Context) *ProjectsLocationsAppGatewaysDeleteCall
func (c *ProjectsLocationsAppGatewaysDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsAppGatewaysDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppGatewaysDeleteCall
func (c *ProjectsLocationsAppGatewaysDeleteCall) Header() http.Header
func (c *ProjectsLocationsAppGatewaysDeleteCall) RequestId(requestId string) *ProjectsLocationsAppGatewaysDeleteCall
func (c *ProjectsLocationsAppGatewaysDeleteCall) ValidateOnly(validateOnly bool) *ProjectsLocationsAppGatewaysDeleteCall
type ProjectsLocationsAppGatewaysGetCall
func (c *ProjectsLocationsAppGatewaysGetCall) Context(ctx context.Context) *ProjectsLocationsAppGatewaysGetCall
func (c *ProjectsLocationsAppGatewaysGetCall) Do(opts ...googleapi.CallOption) (*AppGateway, error)
func (c *ProjectsLocationsAppGatewaysGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppGatewaysGetCall
func (c *ProjectsLocationsAppGatewaysGetCall) Header() http.Header
func (c *ProjectsLocationsAppGatewaysGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsAppGatewaysGetCall
type ProjectsLocationsAppGatewaysGetIamPolicyCall
func (c *ProjectsLocationsAppGatewaysGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsAppGatewaysGetIamPolicyCall
func (c *ProjectsLocationsAppGatewaysGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)
func (c *ProjectsLocationsAppGatewaysGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppGatewaysGetIamPolicyCall
func (c *ProjectsLocationsAppGatewaysGetIamPolicyCall) Header() http.Header
func (c *ProjectsLocationsAppGatewaysGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsAppGatewaysGetIamPolicyCall
func (c *ProjectsLocationsAppGatewaysGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsAppGatewaysGetIamPolicyCall
type ProjectsLocationsAppGatewaysListCall
func (c *ProjectsLocationsAppGatewaysListCall) Context(ctx context.Context) *ProjectsLocationsAppGatewaysListCall
func (c *ProjectsLocationsAppGatewaysListCall) Do(opts ...googleapi.CallOption) (*ListAppGatewaysResponse, error)
func (c *ProjectsLocationsAppGatewaysListCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppGatewaysListCall
func (c *ProjectsLocationsAppGatewaysListCall) Filter(filter string) *ProjectsLocationsAppGatewaysListCall
func (c *ProjectsLocationsAppGatewaysListCall) Header() http.Header
func (c *ProjectsLocationsAppGatewaysListCall) IfNoneMatch(entityTag string) *ProjectsLocationsAppGatewaysListCall
func (c *ProjectsLocationsAppGatewaysListCall) OrderBy(orderBy string) *ProjectsLocationsAppGatewaysListCall
func (c *ProjectsLocationsAppGatewaysListCall) PageSize(pageSize int64) *ProjectsLocationsAppGatewaysListCall
func (c *ProjectsLocationsAppGatewaysListCall) PageToken(pageToken string) *ProjectsLocationsAppGatewaysListCall
func (c *ProjectsLocationsAppGatewaysListCall) Pages(ctx context.Context, f func(*ListAppGatewaysResponse) error) error
type ProjectsLocationsAppGatewaysService
func NewProjectsLocationsAppGatewaysService(s *Service) *ProjectsLocationsAppGatewaysService
func (r *ProjectsLocationsAppGatewaysService) Create(parent string, appgateway *AppGateway) *ProjectsLocationsAppGatewaysCreateCall
func (r *ProjectsLocationsAppGatewaysService) Delete(name string) *ProjectsLocationsAppGatewaysDeleteCall
func (r *ProjectsLocationsAppGatewaysService) Get(name string) *ProjectsLocationsAppGatewaysGetCall
func (r *ProjectsLocationsAppGatewaysService) GetIamPolicy(resource string) *ProjectsLocationsAppGatewaysGetIamPolicyCall
func (r *ProjectsLocationsAppGatewaysService) List(parent string) *ProjectsLocationsAppGatewaysListCall
func (r *ProjectsLocationsAppGatewaysService) SetIamPolicy(resource string, ...) *ProjectsLocationsAppGatewaysSetIamPolicyCall
func (r *ProjectsLocationsAppGatewaysService) TestIamPermissions(resource string, ...) *ProjectsLocationsAppGatewaysTestIamPermissionsCall
type ProjectsLocationsAppGatewaysSetIamPolicyCall
func (c *ProjectsLocationsAppGatewaysSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsAppGatewaysSetIamPolicyCall
func (c *ProjectsLocationsAppGatewaysSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)
func (c *ProjectsLocationsAppGatewaysSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppGatewaysSetIamPolicyCall
func (c *ProjectsLocationsAppGatewaysSetIamPolicyCall) Header() http.Header
type ProjectsLocationsAppGatewaysTestIamPermissionsCall
func (c *ProjectsLocationsAppGatewaysTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsAppGatewaysTestIamPermissionsCall
func (c *ProjectsLocationsAppGatewaysTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1TestIamPermissionsResponse, error)
func (c *ProjectsLocationsAppGatewaysTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppGatewaysTestIamPermissionsCall
func (c *ProjectsLocationsAppGatewaysTestIamPermissionsCall) Header() http.Header
type ProjectsLocationsGetCall
func (c *ProjectsLocationsGetCall) Context(ctx context.Context) *ProjectsLocationsGetCall
func (c *ProjectsLocationsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudLocationLocation, error)
func (c *ProjectsLocationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsGetCall
func (c *ProjectsLocationsGetCall) Header() http.Header
func (c *ProjectsLocationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsGetCall
type ProjectsLocationsListCall
func (c *ProjectsLocationsListCall) Context(ctx context.Context) *ProjectsLocationsListCall
func (c *ProjectsLocationsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudLocationListLocationsResponse, error)
func (c *ProjectsLocationsListCall) ExtraLocationTypes(extraLocationTypes ...string) *ProjectsLocationsListCall
func (c *ProjectsLocationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsListCall
func (c *ProjectsLocationsListCall) Filter(filter string) *ProjectsLocationsListCall
func (c *ProjectsLocationsListCall) Header() http.Header
func (c *ProjectsLocationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsListCall
func (c *ProjectsLocationsListCall) PageSize(pageSize int64) *ProjectsLocationsListCall
func (c *ProjectsLocationsListCall) PageToken(pageToken string) *ProjectsLocationsListCall
func (c *ProjectsLocationsListCall) Pages(ctx context.Context, f func(*GoogleCloudLocationListLocationsResponse) error) error
type ProjectsLocationsOperationsCancelCall
func (c *ProjectsLocationsOperationsCancelCall) Context(ctx context.Context) *ProjectsLocationsOperationsCancelCall
func (c *ProjectsLocationsOperationsCancelCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsLocationsOperationsCancelCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsCancelCall
func (c *ProjectsLocationsOperationsCancelCall) Header() http.Header
type ProjectsLocationsOperationsDeleteCall
func (c *ProjectsLocationsOperationsDeleteCall) Context(ctx context.Context) *ProjectsLocationsOperationsDeleteCall
func (c *ProjectsLocationsOperationsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)
func (c *ProjectsLocationsOperationsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsDeleteCall
func (c *ProjectsLocationsOperationsDeleteCall) Header() http.Header
type ProjectsLocationsOperationsGetCall
func (c *ProjectsLocationsOperationsGetCall) Context(ctx context.Context) *ProjectsLocationsOperationsGetCall
func (c *ProjectsLocationsOperationsGetCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsOperationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsGetCall
func (c *ProjectsLocationsOperationsGetCall) Header() http.Header
func (c *ProjectsLocationsOperationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsOperationsGetCall
type ProjectsLocationsOperationsListCall
func (c *ProjectsLocationsOperationsListCall) Context(ctx context.Context) *ProjectsLocationsOperationsListCall
func (c *ProjectsLocationsOperationsListCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningListOperationsResponse, error)
func (c *ProjectsLocationsOperationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsListCall
func (c *ProjectsLocationsOperationsListCall) Filter(filter string) *ProjectsLocationsOperationsListCall
func (c *ProjectsLocationsOperationsListCall) Header() http.Header
func (c *ProjectsLocationsOperationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsOperationsListCall
func (c *ProjectsLocationsOperationsListCall) PageSize(pageSize int64) *ProjectsLocationsOperationsListCall
func (c *ProjectsLocationsOperationsListCall) PageToken(pageToken string) *ProjectsLocationsOperationsListCall
func (c *ProjectsLocationsOperationsListCall) Pages(ctx context.Context, f func(*GoogleLongrunningListOperationsResponse) error) error
func (c *ProjectsLocationsOperationsListCall) ReturnPartialSuccess(returnPartialSuccess bool) *ProjectsLocationsOperationsListCall
type ProjectsLocationsOperationsService
func NewProjectsLocationsOperationsService(s *Service) *ProjectsLocationsOperationsService
func (r *ProjectsLocationsOperationsService) Cancel(name string, ...) *ProjectsLocationsOperationsCancelCall
func (r *ProjectsLocationsOperationsService) Delete(name string) *ProjectsLocationsOperationsDeleteCall
func (r *ProjectsLocationsOperationsService) Get(name string) *ProjectsLocationsOperationsGetCall
func (r *ProjectsLocationsOperationsService) List(name string) *ProjectsLocationsOperationsListCall
type ProjectsLocationsSecurityGatewaysApplicationsCreateCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsCreateCall) ApplicationId(applicationId string) *ProjectsLocationsSecurityGatewaysApplicationsCreateCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsCreateCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysApplicationsCreateCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsSecurityGatewaysApplicationsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysApplicationsCreateCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsCreateCall) Header() http.Header
func (c *ProjectsLocationsSecurityGatewaysApplicationsCreateCall) RequestId(requestId string) *ProjectsLocationsSecurityGatewaysApplicationsCreateCall
type ProjectsLocationsSecurityGatewaysApplicationsDeleteCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall) Header() http.Header
func (c *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall) RequestId(requestId string) *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall) ValidateOnly(validateOnly bool) *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall
type ProjectsLocationsSecurityGatewaysApplicationsGetCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysApplicationsGetCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSecuritygatewaysV1Application, error)
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysApplicationsGetCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetCall) Header() http.Header
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsSecurityGatewaysApplicationsGetCall
type ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall) Header() http.Header
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall
type ProjectsLocationsSecurityGatewaysApplicationsListCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsListCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysApplicationsListCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSecuritygatewaysV1ListApplicationsResponse, error)
func (c *ProjectsLocationsSecurityGatewaysApplicationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysApplicationsListCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsListCall) Filter(filter string) *ProjectsLocationsSecurityGatewaysApplicationsListCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsListCall) Header() http.Header
func (c *ProjectsLocationsSecurityGatewaysApplicationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsSecurityGatewaysApplicationsListCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsListCall) OrderBy(orderBy string) *ProjectsLocationsSecurityGatewaysApplicationsListCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsListCall) PageSize(pageSize int64) *ProjectsLocationsSecurityGatewaysApplicationsListCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsListCall) PageToken(pageToken string) *ProjectsLocationsSecurityGatewaysApplicationsListCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsListCall) Pages(ctx context.Context, ...) error
type ProjectsLocationsSecurityGatewaysApplicationsPatchCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsPatchCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysApplicationsPatchCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsSecurityGatewaysApplicationsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysApplicationsPatchCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsPatchCall) Header() http.Header
func (c *ProjectsLocationsSecurityGatewaysApplicationsPatchCall) RequestId(requestId string) *ProjectsLocationsSecurityGatewaysApplicationsPatchCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsSecurityGatewaysApplicationsPatchCall
type ProjectsLocationsSecurityGatewaysApplicationsService
func NewProjectsLocationsSecurityGatewaysApplicationsService(s *Service) *ProjectsLocationsSecurityGatewaysApplicationsService
func (r *ProjectsLocationsSecurityGatewaysApplicationsService) Create(parent string, ...) *ProjectsLocationsSecurityGatewaysApplicationsCreateCall
func (r *ProjectsLocationsSecurityGatewaysApplicationsService) Delete(name string) *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall
func (r *ProjectsLocationsSecurityGatewaysApplicationsService) Get(name string) *ProjectsLocationsSecurityGatewaysApplicationsGetCall
func (r *ProjectsLocationsSecurityGatewaysApplicationsService) GetIamPolicy(resource string) *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall
func (r *ProjectsLocationsSecurityGatewaysApplicationsService) List(parent string) *ProjectsLocationsSecurityGatewaysApplicationsListCall
func (r *ProjectsLocationsSecurityGatewaysApplicationsService) Patch(name string, ...) *ProjectsLocationsSecurityGatewaysApplicationsPatchCall
func (r *ProjectsLocationsSecurityGatewaysApplicationsService) SetIamPolicy(resource string, ...) *ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall
func (r *ProjectsLocationsSecurityGatewaysApplicationsService) TestIamPermissions(resource string, ...) *ProjectsLocationsSecurityGatewaysApplicationsTestIamPermissionsCall
type ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)
func (c *ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall) Header() http.Header
type ProjectsLocationsSecurityGatewaysApplicationsTestIamPermissionsCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysApplicationsTestIamPermissionsCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1TestIamPermissionsResponse, error)
func (c *ProjectsLocationsSecurityGatewaysApplicationsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysApplicationsTestIamPermissionsCall
func (c *ProjectsLocationsSecurityGatewaysApplicationsTestIamPermissionsCall) Header() http.Header
type ProjectsLocationsSecurityGatewaysCreateCall
func (c *ProjectsLocationsSecurityGatewaysCreateCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysCreateCall
func (c *ProjectsLocationsSecurityGatewaysCreateCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsSecurityGatewaysCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysCreateCall
func (c *ProjectsLocationsSecurityGatewaysCreateCall) Header() http.Header
func (c *ProjectsLocationsSecurityGatewaysCreateCall) RequestId(requestId string) *ProjectsLocationsSecurityGatewaysCreateCall
func (c *ProjectsLocationsSecurityGatewaysCreateCall) SecurityGatewayId(securityGatewayId string) *ProjectsLocationsSecurityGatewaysCreateCall
type ProjectsLocationsSecurityGatewaysDeleteCall
func (c *ProjectsLocationsSecurityGatewaysDeleteCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysDeleteCall
func (c *ProjectsLocationsSecurityGatewaysDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsSecurityGatewaysDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysDeleteCall
func (c *ProjectsLocationsSecurityGatewaysDeleteCall) Header() http.Header
func (c *ProjectsLocationsSecurityGatewaysDeleteCall) RequestId(requestId string) *ProjectsLocationsSecurityGatewaysDeleteCall
func (c *ProjectsLocationsSecurityGatewaysDeleteCall) ValidateOnly(validateOnly bool) *ProjectsLocationsSecurityGatewaysDeleteCall
type ProjectsLocationsSecurityGatewaysGetCall
func (c *ProjectsLocationsSecurityGatewaysGetCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysGetCall
func (c *ProjectsLocationsSecurityGatewaysGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSecuritygatewaysV1SecurityGateway, error)
func (c *ProjectsLocationsSecurityGatewaysGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysGetCall
func (c *ProjectsLocationsSecurityGatewaysGetCall) Header() http.Header
func (c *ProjectsLocationsSecurityGatewaysGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsSecurityGatewaysGetCall
type ProjectsLocationsSecurityGatewaysGetIamPolicyCall
func (c *ProjectsLocationsSecurityGatewaysGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysGetIamPolicyCall
func (c *ProjectsLocationsSecurityGatewaysGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)
func (c *ProjectsLocationsSecurityGatewaysGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysGetIamPolicyCall
func (c *ProjectsLocationsSecurityGatewaysGetIamPolicyCall) Header() http.Header
func (c *ProjectsLocationsSecurityGatewaysGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsSecurityGatewaysGetIamPolicyCall
func (c *ProjectsLocationsSecurityGatewaysGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsSecurityGatewaysGetIamPolicyCall
type ProjectsLocationsSecurityGatewaysListCall
func (c *ProjectsLocationsSecurityGatewaysListCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysListCall
func (c *ProjectsLocationsSecurityGatewaysListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSecuritygatewaysV1ListSecurityGatewaysResponse, error)
func (c *ProjectsLocationsSecurityGatewaysListCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysListCall
func (c *ProjectsLocationsSecurityGatewaysListCall) Filter(filter string) *ProjectsLocationsSecurityGatewaysListCall
func (c *ProjectsLocationsSecurityGatewaysListCall) Header() http.Header
func (c *ProjectsLocationsSecurityGatewaysListCall) IfNoneMatch(entityTag string) *ProjectsLocationsSecurityGatewaysListCall
func (c *ProjectsLocationsSecurityGatewaysListCall) OrderBy(orderBy string) *ProjectsLocationsSecurityGatewaysListCall
func (c *ProjectsLocationsSecurityGatewaysListCall) PageSize(pageSize int64) *ProjectsLocationsSecurityGatewaysListCall
func (c *ProjectsLocationsSecurityGatewaysListCall) PageToken(pageToken string) *ProjectsLocationsSecurityGatewaysListCall
func (c *ProjectsLocationsSecurityGatewaysListCall) Pages(ctx context.Context, ...) error
type ProjectsLocationsSecurityGatewaysPatchCall
func (c *ProjectsLocationsSecurityGatewaysPatchCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysPatchCall
func (c *ProjectsLocationsSecurityGatewaysPatchCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)
func (c *ProjectsLocationsSecurityGatewaysPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysPatchCall
func (c *ProjectsLocationsSecurityGatewaysPatchCall) Header() http.Header
func (c *ProjectsLocationsSecurityGatewaysPatchCall) RequestId(requestId string) *ProjectsLocationsSecurityGatewaysPatchCall
func (c *ProjectsLocationsSecurityGatewaysPatchCall) UpdateMask(updateMask string) *ProjectsLocationsSecurityGatewaysPatchCall
type ProjectsLocationsSecurityGatewaysService
func NewProjectsLocationsSecurityGatewaysService(s *Service) *ProjectsLocationsSecurityGatewaysService
func (r *ProjectsLocationsSecurityGatewaysService) Create(parent string, ...) *ProjectsLocationsSecurityGatewaysCreateCall
func (r *ProjectsLocationsSecurityGatewaysService) Delete(name string) *ProjectsLocationsSecurityGatewaysDeleteCall
func (r *ProjectsLocationsSecurityGatewaysService) Get(name string) *ProjectsLocationsSecurityGatewaysGetCall
func (r *ProjectsLocationsSecurityGatewaysService) GetIamPolicy(resource string) *ProjectsLocationsSecurityGatewaysGetIamPolicyCall
func (r *ProjectsLocationsSecurityGatewaysService) List(parent string) *ProjectsLocationsSecurityGatewaysListCall
func (r *ProjectsLocationsSecurityGatewaysService) Patch(name string, ...) *ProjectsLocationsSecurityGatewaysPatchCall
func (r *ProjectsLocationsSecurityGatewaysService) SetIamPolicy(resource string, ...) *ProjectsLocationsSecurityGatewaysSetIamPolicyCall
func (r *ProjectsLocationsSecurityGatewaysService) TestIamPermissions(resource string, ...) *ProjectsLocationsSecurityGatewaysTestIamPermissionsCall
type ProjectsLocationsSecurityGatewaysSetIamPolicyCall
func (c *ProjectsLocationsSecurityGatewaysSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysSetIamPolicyCall
func (c *ProjectsLocationsSecurityGatewaysSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)
func (c *ProjectsLocationsSecurityGatewaysSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysSetIamPolicyCall
func (c *ProjectsLocationsSecurityGatewaysSetIamPolicyCall) Header() http.Header
type ProjectsLocationsSecurityGatewaysTestIamPermissionsCall
func (c *ProjectsLocationsSecurityGatewaysTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysTestIamPermissionsCall
func (c *ProjectsLocationsSecurityGatewaysTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1TestIamPermissionsResponse, error)
func (c *ProjectsLocationsSecurityGatewaysTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysTestIamPermissionsCall
func (c *ProjectsLocationsSecurityGatewaysTestIamPermissionsCall) Header() http.Header
type ProjectsLocationsService
func NewProjectsLocationsService(s *Service) *ProjectsLocationsService
func (r *ProjectsLocationsService) Get(name string) *ProjectsLocationsGetCall
func (r *ProjectsLocationsService) List(name string) *ProjectsLocationsListCall
type ProjectsService
func NewProjectsService(s *Service) *ProjectsService
type Service
func New(client *http.Client) (*Service, error)DEPRECATED
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)
type Tunnelv1ProtoTunnelerError
func (s Tunnelv1ProtoTunnelerError) MarshalJSON() ([]byte, error)
type Tunnelv1ProtoTunnelerInfo
func (s Tunnelv1ProtoTunnelerInfo) MarshalJSON() ([]byte, error)
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
type AllocatedConnection ¶
added in v0.89.0
type AllocatedConnection struct {
	// IngressPort: Required. The ingress port of an allocated connection
	IngressPort int64 `json:"ingressPort,omitempty"`
	// PscUri: Required. The PSC uri of an allocated connection
	PscUri string `json:"pscUri,omitempty"`
	// ForceSendFields is a list of field names (e.g. "IngressPort") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "IngressPort") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AllocatedConnection: Allocated connection of the AppGateway.

func (AllocatedConnection) MarshalJSON ¶
added in v0.89.0
func (s AllocatedConnection) MarshalJSON() ([]byte, error)
type AppGateway ¶
added in v0.89.0
type AppGateway struct {
	// AllocatedConnections: Output only. A list of connections allocated for the
	// Gateway
	AllocatedConnections []*AllocatedConnection `json:"allocatedConnections,omitempty"`
	// CreateTime: Output only. Timestamp when the resource was created.
	CreateTime string `json:"createTime,omitempty"`
	// DisplayName: Optional. An arbitrary user-provided name for the AppGateway.
	// Cannot exceed 64 characters.
	DisplayName string `json:"displayName,omitempty"`
	// HostType: Required. The type of hosting used by the AppGateway.
	//
	// Possible values:
	//   "HOST_TYPE_UNSPECIFIED" - Default value. This value is unused.
	//   "GCP_REGIONAL_MIG" - AppGateway hosted in a GCP regional managed instance
	// group.
	HostType string `json:"hostType,omitempty"`
	// Labels: Optional. Resource labels to represent user provided metadata.
	Labels map[string]string `json:"labels,omitempty"`
	// Name: Required. Unique resource name of the AppGateway. The name is ignored
	// when creating an AppGateway.
	Name string `json:"name,omitempty"`
	// SatisfiesPzi: Output only. Reserved for future use.
	SatisfiesPzi bool `json:"satisfiesPzi,omitempty"`
	// SatisfiesPzs: Output only. Reserved for future use.
	SatisfiesPzs bool `json:"satisfiesPzs,omitempty"`
	// State: Output only. The current state of the AppGateway.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - Default value. This value is unused.
	//   "CREATING" - AppGateway is being created.
	//   "CREATED" - AppGateway has been created.
	//   "UPDATING" - AppGateway's configuration is being updated.
	//   "DELETING" - AppGateway is being deleted.
	//   "DOWN" - AppGateway is down and may be restored in the future. This
	// happens when CCFE sends ProjectState = OFF.
	State string `json:"state,omitempty"`
	// Type: Required. The type of network connectivity used by the AppGateway.
	//
	// Possible values:
	//   "TYPE_UNSPECIFIED" - Default value. This value is unused.
	//   "TCP_PROXY" - TCP Proxy based BeyondCorp Connection. API will default to
	// this if unset.
	Type string `json:"type,omitempty"`
	// Uid: Output only. A unique identifier for the instance generated by the
	// system.
	Uid string `json:"uid,omitempty"`
	// UpdateTime: Output only. Timestamp when the resource was last modified.
	UpdateTime string `json:"updateTime,omitempty"`
	// Uri: Output only. Server-defined URI for this resource.
	Uri string `json:"uri,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AllocatedConnections") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AllocatedConnections") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AppGateway: A BeyondCorp AppGateway resource represents a BeyondCorp protected AppGateway to a remote application. It creates all the necessary GCP components needed for creating a BeyondCorp protected AppGateway. Multiple connectors can be authorised for a single AppGateway.

func (AppGateway) MarshalJSON ¶
added in v0.89.0
func (s AppGateway) MarshalJSON() ([]byte, error)
type AppGatewayOperationMetadata ¶
added in v0.89.0
type AppGatewayOperationMetadata struct {
	// ApiVersion: Output only. API version used to start the operation.
	ApiVersion string `json:"apiVersion,omitempty"`
	// CreateTime: Output only. The time the operation was created.
	CreateTime string `json:"createTime,omitempty"`
	// EndTime: Output only. The time the operation finished running.
	EndTime string `json:"endTime,omitempty"`
	// RequestedCancellation: Output only. Identifies whether the user has
	// requested cancellation of the operation. Operations that have successfully
	// been cancelled have google.longrunning.Operation.error value with a
	// google.rpc.Status.code of `1`, corresponding to `Code.CANCELLED`.
	RequestedCancellation bool `json:"requestedCancellation,omitempty"`
	// StatusMessage: Output only. Human-readable status of the operation, if any.
	StatusMessage string `json:"statusMessage,omitempty"`
	// Target: Output only. Server-defined resource path for the target of the
	// operation.
	Target string `json:"target,omitempty"`
	// Verb: Output only. Name of the verb executed by the operation.
	Verb string `json:"verb,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApiVersion") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApiVersion") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

AppGatewayOperationMetadata: Represents the metadata of the long-running operation.

func (AppGatewayOperationMetadata) MarshalJSON ¶
added in v0.89.0
func (s AppGatewayOperationMetadata) MarshalJSON() ([]byte, error)
type CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfig ¶
type CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfig struct {
	// ApplicationEndpoint: application_endpoint is the endpoint of the application
	// the form of host:port. For example, "localhost:80".
	ApplicationEndpoint string `json:"applicationEndpoint,omitempty"`
	// ApplicationName: application_name represents the given name of the
	// application the connection is connecting with.
	ApplicationName string `json:"applicationName,omitempty"`
	// Gateway: gateway lists all instances running a gateway in GCP. They all
	// connect to a connector on the host.
	Gateway []*CloudSecurityZerotrustApplinkAppConnectorProtoGateway `json:"gateway,omitempty"`
	// Name: name is the unique ID for each connection. TODO(b/190732451) returns
	// connection name from user-specified name in config. Now, name =
	// ${application_name}:${application_endpoint}
	Name string `json:"name,omitempty"`
	// Project: project represents the consumer project the connection belongs to.
	Project string `json:"project,omitempty"`
	// TunnelsPerGateway: tunnels_per_gateway reflects the number of tunnels
	// between a connector and a gateway.
	TunnelsPerGateway int64 `json:"tunnelsPerGateway,omitempty"`
	// UserPort: user_port specifies the reserved port on gateways for user
	// connections.
	UserPort int64 `json:"userPort,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApplicationEndpoint") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApplicationEndpoint") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfig: ConnectionConfig represents a Connection Configuration object.

func (CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfig) MarshalJSON ¶
func (s CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfig) MarshalJSON() ([]byte, error)
type CloudSecurityZerotrustApplinkAppConnectorProtoConnectorDetails ¶
type CloudSecurityZerotrustApplinkAppConnectorProtoConnectorDetails struct {
}

CloudSecurityZerotrustApplinkAppConnectorProtoConnectorDetails: ConnectorDetails reflects the details of a connector.

type CloudSecurityZerotrustApplinkAppConnectorProtoGateway ¶
type CloudSecurityZerotrustApplinkAppConnectorProtoGateway struct {
	// Interface: interface specifies the network interface of the gateway to
	// connect to.
	Interface string `json:"interface,omitempty"`
	// Name: name is the name of an instance running a gateway. It is the unique ID
	// for a gateway. All gateways under the same connection have the same prefix.
	// It is derived from the gateway URL. For example, name=${instance} assuming a
	// gateway URL.
	// https://www.googleapis.com/compute/${version}/projects/${project}/zones/${zone}/instances/${instance}
	Name string `json:"name,omitempty"`
	// Port: port specifies the port of the gateway for tunnel connections from the
	// connectors.
	Port int64 `json:"port,omitempty"`
	// Project: project is the tenant project the gateway belongs to. Different
	// from the project in the connection, it is a BeyondCorpAPI internally created
	// project to manage all the gateways. It is sharing the same network with the
	// consumer project user owned. It is derived from the gateway URL. For
	// example, project=${project} assuming a gateway URL.
	// https://www.googleapis.com/compute/${version}/projects/${project}/zones/${zone}/instances/${instance}
	Project string `json:"project,omitempty"`
	// SelfLink: self_link is the gateway URL in the form
	// https://www.googleapis.com/compute/${version}/projects/${project}/zones/${zone}/instances/${instance}
	SelfLink string `json:"selfLink,omitempty"`
	// Zone: zone represents the zone the instance belongs. It is derived from the
	// gateway URL. For example, zone=${zone} assuming a gateway URL.
	// https://www.googleapis.com/compute/${version}/projects/${project}/zones/${zone}/instances/${instance}
	Zone string `json:"zone,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Interface") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Interface") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

CloudSecurityZerotrustApplinkAppConnectorProtoGateway: Gateway represents a GCE VM Instance endpoint for use by IAP TCP.

func (CloudSecurityZerotrustApplinkAppConnectorProtoGateway) MarshalJSON ¶
func (s CloudSecurityZerotrustApplinkAppConnectorProtoGateway) MarshalJSON() ([]byte, error)
type CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetails ¶
type CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetails struct {
}

CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetails: LogAgentDetails reflects the details of a log agent.

type Empty ¶
type Empty struct {
	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
}

Empty: A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }

type GoogleCloudBeyondcorpAppconnectionsV1AppConnection ¶
added in v0.89.0
type GoogleCloudBeyondcorpAppconnectionsV1AppConnection struct {
	// ApplicationEndpoint: Required. Address of the remote application endpoint
	// for the BeyondCorp AppConnection.
	ApplicationEndpoint *GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpoint `json:"applicationEndpoint,omitempty"`
	// Connectors: Optional. List of
	// [google.cloud.beyondcorp.v1main.Connector.name] that are authorised to be
	// associated with this AppConnection.
	Connectors []string `json:"connectors,omitempty"`
	// CreateTime: Output only. Timestamp when the resource was created.
	CreateTime string `json:"createTime,omitempty"`
	// DisplayName: Optional. An arbitrary user-provided name for the
	// AppConnection. Cannot exceed 64 characters.
	DisplayName string `json:"displayName,omitempty"`
	// Gateway: Optional. Gateway used by the AppConnection.
	Gateway *GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGateway `json:"gateway,omitempty"`
	// Labels: Optional. Resource labels to represent user provided metadata.
	Labels map[string]string `json:"labels,omitempty"`
	// Name: Required. Unique resource name of the AppConnection. The name is
	// ignored when creating a AppConnection.
	Name string `json:"name,omitempty"`
	// SatisfiesPzi: Output only. Reserved for future use.
	SatisfiesPzi bool `json:"satisfiesPzi,omitempty"`
	// SatisfiesPzs: Output only. Reserved for future use.
	SatisfiesPzs bool `json:"satisfiesPzs,omitempty"`
	// State: Output only. The current state of the AppConnection.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - Default value. This value is unused.
	//   "CREATING" - AppConnection is being created.
	//   "CREATED" - AppConnection has been created.
	//   "UPDATING" - AppConnection's configuration is being updated.
	//   "DELETING" - AppConnection is being deleted.
	//   "DOWN" - AppConnection is down and may be restored in the future. This
	// happens when CCFE sends ProjectState = OFF.
	State string `json:"state,omitempty"`
	// Type: Required. The type of network connectivity used by the AppConnection.
	//
	// Possible values:
	//   "TYPE_UNSPECIFIED" - Default value. This value is unused.
	//   "TCP_PROXY" - TCP Proxy based BeyondCorp AppConnection. API will default
	// to this if unset.
	Type string `json:"type,omitempty"`
	// Uid: Output only. A unique identifier for the instance generated by the
	// system.
	Uid string `json:"uid,omitempty"`
	// UpdateTime: Output only. Timestamp when the resource was last modified.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "ApplicationEndpoint") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApplicationEndpoint") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpAppconnectionsV1AppConnection: A BeyondCorp AppConnection resource represents a BeyondCorp protected AppConnection to a remote application. It creates all the necessary GCP components needed for creating a BeyondCorp protected AppConnection. Multiple connectors can be authorised for a single AppConnection.

func (GoogleCloudBeyondcorpAppconnectionsV1AppConnection) MarshalJSON ¶
added in v0.89.0
func (s GoogleCloudBeyondcorpAppconnectionsV1AppConnection) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpoint ¶
added in v0.89.0
type GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpoint struct {
	// Host: Required. Hostname or IP address of the remote application endpoint.
	Host string `json:"host,omitempty"`
	// Port: Required. Port of the remote application endpoint.
	Port int64 `json:"port,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Host") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Host") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpoint: ApplicationEndpoint represents a remote application endpoint.

func (GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpoint) MarshalJSON ¶
added in v0.89.0
func (s GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpoint) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGateway ¶
added in v0.89.0
type GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGateway struct {
	// AppGateway: Required. AppGateway name in following format:
	// `projects/{project_id}/locations/{location_id}/appgateways/{gateway_id}`
	AppGateway string `json:"appGateway,omitempty"`
	// IngressPort: Output only. Ingress port reserved on the gateways for this
	// AppConnection, if not specified or zero, the default port is 19443.
	IngressPort int64 `json:"ingressPort,omitempty"`
	// L7psc: Output only. L7 private service connection for this resource.
	L7psc string `json:"l7psc,omitempty"`
	// Type: Required. The type of hosting used by the gateway.
	//
	// Possible values:
	//   "TYPE_UNSPECIFIED" - Default value. This value is unused.
	//   "GCP_REGIONAL_MIG" - Gateway hosted in a GCP regional managed instance
	// group.
	Type string `json:"type,omitempty"`
	// Uri: Output only. Server-defined URI for this resource.
	Uri string `json:"uri,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AppGateway") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AppGateway") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGateway: Gateway represents a user facing component that serves as an entrance to enable connectivity.

func (GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGateway) MarshalJSON ¶
added in v0.89.0
func (s GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGateway) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadata ¶
added in v0.89.0
type GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadata struct {
	// ApiVersion: Output only. API version used to start the operation.
	ApiVersion string `json:"apiVersion,omitempty"`
	// CreateTime: Output only. The time the operation was created.
	CreateTime string `json:"createTime,omitempty"`
	// EndTime: Output only. The time the operation finished running.
	EndTime string `json:"endTime,omitempty"`
	// RequestedCancellation: Output only. Identifies whether the user has
	// requested cancellation of the operation. Operations that have successfully
	// been cancelled have google.longrunning.Operation.error value with a
	// google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.
	RequestedCancellation bool `json:"requestedCancellation,omitempty"`
	// StatusMessage: Output only. Human-readable status of the operation, if any.
	StatusMessage string `json:"statusMessage,omitempty"`
	// Target: Output only. Server-defined resource path for the target of the
	// operation.
	Target string `json:"target,omitempty"`
	// Verb: Output only. Name of the verb executed by the operation.
	Verb string `json:"verb,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApiVersion") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApiVersion") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadata: Represents the metadata of the long-running operation.

func (GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadata) MarshalJSON ¶
added in v0.89.0
func (s GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponse ¶
added in v0.89.0
type GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponse struct {
	// AppConnections: A list of BeyondCorp AppConnections in the project.
	AppConnections []*GoogleCloudBeyondcorpAppconnectionsV1AppConnection `json:"appConnections,omitempty"`
	// NextPageToken: A token to retrieve the next page of results, or empty if
	// there are no more results in the list.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Unreachable: A list of locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AppConnections") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AppConnections") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponse: Response message for BeyondCorp.ListAppConnections.

func (GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponse) MarshalJSON ¶
added in v0.89.0
func (s GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponse ¶
added in v0.89.0
type GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponse struct {
	// AppConnectionDetails: A list of BeyondCorp AppConnections with details in
	// the project.
	AppConnectionDetails []*GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetails `json:"appConnectionDetails,omitempty"`
	// NextPageToken: A token to retrieve the next page of results, or empty if
	// there are no more results in the list.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Unreachable: A list of locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AppConnectionDetails") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AppConnectionDetails") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponse: Response message for BeyondCorp.ResolveAppConnections.

func (GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponse) MarshalJSON ¶
added in v0.89.0
func (s GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetails ¶
added in v0.89.0
type GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetails struct {
	// AppConnection: A BeyondCorp AppConnection in the project.
	AppConnection *GoogleCloudBeyondcorpAppconnectionsV1AppConnection `json:"appConnection,omitempty"`
	// RecentMigVms: If type=GCP_REGIONAL_MIG, contains most recent VM instances,
	// like
	// `https://www.googleapis.com/compute/v1/projects/{project_id}/zones/{zone_id}/
	// instances/{instance_id}`.
	RecentMigVms []string `json:"recentMigVms,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AppConnection") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AppConnection") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnecti onDetails: Details of the AppConnection.

func (GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetails) MarshalJSON ¶
added in v0.89.0
func (s GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetails) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadata ¶
type GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadata struct {
	// ApiVersion: Output only. API version used to start the operation.
	ApiVersion string `json:"apiVersion,omitempty"`
	// CreateTime: Output only. The time the operation was created.
	CreateTime string `json:"createTime,omitempty"`
	// EndTime: Output only. The time the operation finished running.
	EndTime string `json:"endTime,omitempty"`
	// RequestedCancellation: Output only. Identifies whether the user has
	// requested cancellation of the operation. Operations that have successfully
	// been cancelled have google.longrunning.Operation.error value with a
	// google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.
	RequestedCancellation bool `json:"requestedCancellation,omitempty"`
	// StatusMessage: Output only. Human-readable status of the operation, if any.
	StatusMessage string `json:"statusMessage,omitempty"`
	// Target: Output only. Server-defined resource path for the target of the
	// operation.
	Target string `json:"target,omitempty"`
	// Verb: Output only. Name of the verb executed by the operation.
	Verb string `json:"verb,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApiVersion") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApiVersion") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadata: Represents the metadata of the long-running operation.

func (GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadata) MarshalJSON ¶
func (s GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1AppConnector ¶
added in v0.89.0
type GoogleCloudBeyondcorpAppconnectorsV1AppConnector struct {
	// CreateTime: Output only. Timestamp when the resource was created.
	CreateTime string `json:"createTime,omitempty"`
	// DisplayName: Optional. An arbitrary user-provided name for the AppConnector.
	// Cannot exceed 64 characters.
	DisplayName string `json:"displayName,omitempty"`
	// Labels: Optional. Resource labels to represent user provided metadata.
	Labels map[string]string `json:"labels,omitempty"`
	// Name: Required. Unique resource name of the AppConnector. The name is
	// ignored when creating a AppConnector.
	Name string `json:"name,omitempty"`
	// PrincipalInfo: Required. Principal information about the Identity of the
	// AppConnector.
	PrincipalInfo *GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfo `json:"principalInfo,omitempty"`
	// ResourceInfo: Optional. Resource info of the connector.
	ResourceInfo *GoogleCloudBeyondcorpAppconnectorsV1ResourceInfo `json:"resourceInfo,omitempty"`
	// State: Output only. The current state of the AppConnector.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - Default value. This value is unused.
	//   "CREATING" - AppConnector is being created.
	//   "CREATED" - AppConnector has been created.
	//   "UPDATING" - AppConnector's configuration is being updated.
	//   "DELETING" - AppConnector is being deleted.
	//   "DOWN" - AppConnector is down and may be restored in the future. This
	// happens when CCFE sends ProjectState = OFF.
	State string `json:"state,omitempty"`
	// Uid: Output only. A unique identifier for the instance generated by the
	// system.
	Uid string `json:"uid,omitempty"`
	// UpdateTime: Output only. Timestamp when the resource was last modified.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "CreateTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CreateTime") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpAppconnectorsV1AppConnector: A BeyondCorp connector resource that represents an application facing component deployed proximal to and with direct access to the application instances. It is used to establish connectivity between the remote enterprise environment and GCP. It initiates connections to the applications and can proxy the data from users over the connection.

func (GoogleCloudBeyondcorpAppconnectorsV1AppConnector) MarshalJSON ¶
added in v0.89.0
func (s GoogleCloudBeyondcorpAppconnectorsV1AppConnector) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfig ¶
added in v0.89.0
type GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfig struct {
	// ImageConfig: ImageConfig defines the GCR images to run for the remote
	// agent's control plane.
	ImageConfig *GoogleCloudBeyondcorpAppconnectorsV1ImageConfig `json:"imageConfig,omitempty"`
	// InstanceConfig: The SLM instance agent configuration.
	InstanceConfig googleapi.RawMessage `json:"instanceConfig,omitempty"`
	// NotificationConfig: NotificationConfig defines the notification mechanism
	// that the remote instance should subscribe to in order to receive
	// notification.
	NotificationConfig *GoogleCloudBeyondcorpAppconnectorsV1NotificationConfig `json:"notificationConfig,omitempty"`
	// SequenceNumber: Required. A monotonically increasing number generated and
	// maintained by the API provider. Every time a config changes in the backend,
	// the sequenceNumber should be bumped up to reflect the change.
	SequenceNumber int64 `json:"sequenceNumber,omitempty,string"`
	// ForceSendFields is a list of field names (e.g. "ImageConfig") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ImageConfig") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfig: AppConnectorInstanceConfig defines the instance config of a AppConnector.

func (GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfig) MarshalJSON ¶
added in v0.89.0
func (s GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfig) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadata ¶
added in v0.89.0
type GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadata struct {
	// ApiVersion: Output only. API version used to start the operation.
	ApiVersion string `json:"apiVersion,omitempty"`
	// CreateTime: Output only. The time the operation was created.
	CreateTime string `json:"createTime,omitempty"`
	// EndTime: Output only. The time the operation finished running.
	EndTime string `json:"endTime,omitempty"`
	// RequestedCancellation: Output only. Identifies whether the user has
	// requested cancellation of the operation. Operations that have successfully
	// been cancelled have google.longrunning.Operation.error value with a
	// google.rpc.Status.code of `1`, corresponding to `Code.CANCELLED`.
	RequestedCancellation bool `json:"requestedCancellation,omitempty"`
	// StatusMessage: Output only. Human-readable status of the operation, if any.
	StatusMessage string `json:"statusMessage,omitempty"`
	// Target: Output only. Server-defined resource path for the target of the
	// operation.
	Target string `json:"target,omitempty"`
	// Verb: Output only. Name of the verb executed by the operation.
	Verb string `json:"verb,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApiVersion") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApiVersion") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadata: Represents the metadata of the long-running operation.

func (GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadata) MarshalJSON ¶
added in v0.89.0
func (s GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfo ¶
added in v0.89.0
type GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfo struct {
	// ServiceAccount: A GCP service account.
	ServiceAccount *GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccount `json:"serviceAccount,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ServiceAccount") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ServiceAccount") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfo: PrincipalInfo represents an Identity oneof.

func (GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfo) MarshalJSON ¶
added in v0.89.0
func (s GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfo) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccount ¶
added in v0.89.0
type GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccount struct {
	// Email: Email address of the service account.
	Email string `json:"email,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Email") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Email") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccount: ServiceAccount represents a GCP service account.

func (GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccount) MarshalJSON ¶
added in v0.89.0
func (s GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccount) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetails ¶
added in v0.89.0
type GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetails struct {
	// CurrentConfigVersion: The version of the current config.
	CurrentConfigVersion string `json:"currentConfigVersion,omitempty"`
	// ErrorMsg: The latest error message.
	ErrorMsg string `json:"errorMsg,omitempty"`
	// ExpectedConfigVersion: The version of the expected config.
	ExpectedConfigVersion string `json:"expectedConfigVersion,omitempty"`
	// ExtendedStatus: The extended status. Such as ExitCode, StartedAt,
	// FinishedAt, etc.
	ExtendedStatus map[string]string `json:"extendedStatus,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CurrentConfigVersion") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CurrentConfigVersion") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetails: ContainerHealthDetails reflects the health details of a container.

func (GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetails) MarshalJSON ¶
added in v0.89.0
func (s GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetails) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1ImageConfig ¶
added in v0.89.0
type GoogleCloudBeyondcorpAppconnectorsV1ImageConfig struct {
	// StableImage: The stable image that the remote agent will fallback to if the
	// target image fails. Format would be a gcr image path, e.g.:
	// gcr.io/PROJECT-ID/my-image:tag1
	StableImage string `json:"stableImage,omitempty"`
	// TargetImage: The initial image the remote agent will attempt to run for the
	// control plane. Format would be a gcr image path, e.g.:
	// gcr.io/PROJECT-ID/my-image:tag1
	TargetImage string `json:"targetImage,omitempty"`
	// ForceSendFields is a list of field names (e.g. "StableImage") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "StableImage") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpAppconnectorsV1ImageConfig: ImageConfig defines the control plane images to run.

func (GoogleCloudBeyondcorpAppconnectorsV1ImageConfig) MarshalJSON ¶
added in v0.89.0
func (s GoogleCloudBeyondcorpAppconnectorsV1ImageConfig) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponse ¶
added in v0.89.0
type GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponse struct {
	// AppConnectors: A list of BeyondCorp AppConnectors in the project.
	AppConnectors []*GoogleCloudBeyondcorpAppconnectorsV1AppConnector `json:"appConnectors,omitempty"`
	// NextPageToken: A token to retrieve the next page of results, or empty if
	// there are no more results in the list.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Unreachable: A list of locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AppConnectors") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AppConnectors") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponse: Response message for BeyondCorp.ListAppConnectors.

func (GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponse) MarshalJSON ¶
added in v0.89.0
func (s GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1NotificationConfig ¶
added in v0.89.0
type GoogleCloudBeyondcorpAppconnectorsV1NotificationConfig struct {
	// PubsubNotification: Cloud Pub/Sub Configuration to receive notifications.
	PubsubNotification *GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfig `json:"pubsubNotification,omitempty"`
	// ForceSendFields is a list of field names (e.g. "PubsubNotification") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "PubsubNotification") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpAppconnectorsV1NotificationConfig: NotificationConfig defines the mechanisms to notify instance agent.

func (GoogleCloudBeyondcorpAppconnectorsV1NotificationConfig) MarshalJSON ¶
added in v0.89.0
func (s GoogleCloudBeyondcorpAppconnectorsV1NotificationConfig) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfig ¶
added in v0.89.0
type GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfig struct {
	// PubsubSubscription: The Pub/Sub subscription the AppConnector uses to
	// receive notifications.
	PubsubSubscription string `json:"pubsubSubscription,omitempty"`
	// ForceSendFields is a list of field names (e.g. "PubsubSubscription") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "PubsubSubscription") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotification Config: The configuration for Pub/Sub messaging for the AppConnector.

func (GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfig) MarshalJSON ¶
added in v0.89.0
func (s GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfig) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetails ¶
added in v0.89.0
type GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetails struct {
}

GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetails: RemoteAgentDetails reflects the details of a remote agent.

type GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequest ¶
added in v0.89.0
type GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequest struct {
	// RequestId: Optional. An optional request ID to identify requests. Specify a
	// unique request ID so that if you must retry your request, the server will
	// know to ignore the request if it has already been completed. The server will
	// guarantee that for at least 60 minutes since the first request. For example,
	// consider a situation where you make an initial request and the request times
	// out. If you make the request again with the same request ID, the server can
	// check if original operation with the same request ID was received, and if
	// so, will ignore the second request. This prevents clients from accidentally
	// creating duplicate commitments. The request ID must be a valid UUID with the
	// exception that zero UUID is not supported
	// (00000000-0000-0000-0000-000000000000).
	RequestId string `json:"requestId,omitempty"`
	// ResourceInfo: Required. Resource info of the connector.
	ResourceInfo *GoogleCloudBeyondcorpAppconnectorsV1ResourceInfo `json:"resourceInfo,omitempty"`
	// ValidateOnly: Optional. If set, validates request by executing a dry-run
	// which would not alter the resource in any way.
	ValidateOnly bool `json:"validateOnly,omitempty"`
	// ForceSendFields is a list of field names (e.g. "RequestId") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "RequestId") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequest: Request report the connector status.

func (GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequest) MarshalJSON ¶
added in v0.89.0
func (s GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequest) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponse ¶
added in v0.89.0
type GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponse struct {
	// InstanceConfig: AppConnectorInstanceConfig.
	InstanceConfig *GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfig `json:"instanceConfig,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "InstanceConfig") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "InstanceConfig") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponse: Response message for BeyondCorp.ResolveInstanceConfig.

func (GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponse) MarshalJSON ¶
added in v0.89.0
func (s GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1ResourceInfo ¶
added in v0.89.0
type GoogleCloudBeyondcorpAppconnectorsV1ResourceInfo struct {
	// Id: Required. Unique Id for the resource.
	Id string `json:"id,omitempty"`
	// Resource: Specific details for the resource. This is for internal use only.
	Resource googleapi.RawMessage `json:"resource,omitempty"`
	// Status: Overall health status. Overall status is derived based on the status
	// of each sub level resources.
	//
	// Possible values:
	//   "HEALTH_STATUS_UNSPECIFIED" - Health status is unknown: not initialized or
	// failed to retrieve.
	//   "HEALTHY" - The resource is healthy.
	//   "UNHEALTHY" - The resource is unhealthy.
	//   "UNRESPONSIVE" - The resource is unresponsive.
	//   "DEGRADED" - Some sub-resources are UNHEALTHY.
	Status string `json:"status,omitempty"`
	// Sub: List of Info for the sub level resources.
	Sub []*GoogleCloudBeyondcorpAppconnectorsV1ResourceInfo `json:"sub,omitempty"`
	// Time: The timestamp to collect the info. It is suggested to be set by the
	// topmost level resource only.
	Time string `json:"time,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Id") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Id") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpAppconnectorsV1ResourceInfo: ResourceInfo represents the information/status of an app connector resource. Such as: - remote_agent - container - runtime - appgateway - appconnector - appconnection - tunnel - logagent

func (GoogleCloudBeyondcorpAppconnectorsV1ResourceInfo) MarshalJSON ¶
added in v0.89.0
func (s GoogleCloudBeyondcorpAppconnectorsV1ResourceInfo) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadata ¶
type GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadata struct {
	// ApiVersion: Output only. API version used to start the operation.
	ApiVersion string `json:"apiVersion,omitempty"`
	// CreateTime: Output only. The time the operation was created.
	CreateTime string `json:"createTime,omitempty"`
	// EndTime: Output only. The time the operation finished running.
	EndTime string `json:"endTime,omitempty"`
	// RequestedCancellation: Output only. Identifies whether the user has
	// requested cancellation of the operation. Operations that have successfully
	// been cancelled have google.longrunning.Operation.error value with a
	// google.rpc.Status.code of `1`, corresponding to `Code.CANCELLED`.
	RequestedCancellation bool `json:"requestedCancellation,omitempty"`
	// StatusMessage: Output only. Human-readable status of the operation, if any.
	StatusMessage string `json:"statusMessage,omitempty"`
	// Target: Output only. Server-defined resource path for the target of the
	// operation.
	Target string `json:"target,omitempty"`
	// Verb: Output only. Name of the verb executed by the operation.
	Verb string `json:"verb,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApiVersion") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApiVersion") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadata: Represents the metadata of the long-running operation.

func (GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadata) MarshalJSON ¶
func (s GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetails ¶
type GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetails struct {
	// CurrentConfigVersion: The version of the current config.
	CurrentConfigVersion string `json:"currentConfigVersion,omitempty"`
	// ErrorMsg: The latest error message.
	ErrorMsg string `json:"errorMsg,omitempty"`
	// ExpectedConfigVersion: The version of the expected config.
	ExpectedConfigVersion string `json:"expectedConfigVersion,omitempty"`
	// ExtendedStatus: The extended status. Such as ExitCode, StartedAt,
	// FinishedAt, etc.
	ExtendedStatus map[string]string `json:"extendedStatus,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CurrentConfigVersion") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CurrentConfigVersion") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetails: ContainerHealthDetails reflects the health details of a container.

func (GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetails) MarshalJSON ¶
func (s GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetails) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetails ¶
type GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetails struct {
}

GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetails: RemoteAgentDetails reflects the details of a remote agent.

type GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadata ¶
type GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadata struct {
	// ApiVersion: Output only. API version used to start the operation.
	ApiVersion string `json:"apiVersion,omitempty"`
	// CreateTime: Output only. The time the operation was created.
	CreateTime string `json:"createTime,omitempty"`
	// EndTime: Output only. The time the operation finished running.
	EndTime string `json:"endTime,omitempty"`
	// RequestedCancellation: Output only. Identifies whether the user has
	// requested cancellation of the operation. Operations that have successfully
	// been cancelled have google.longrunning.Operation.error value with a
	// google.rpc.Status.code of `1`, corresponding to `Code.CANCELLED`.
	RequestedCancellation bool `json:"requestedCancellation,omitempty"`
	// StatusMessage: Output only. Human-readable status of the operation, if any.
	StatusMessage string `json:"statusMessage,omitempty"`
	// Target: Output only. Server-defined resource path for the target of the
	// operation.
	Target string `json:"target,omitempty"`
	// Verb: Output only. Name of the verb executed by the operation.
	Verb string `json:"verb,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApiVersion") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApiVersion") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadata: Represents the metadata of the long-running operation.

func (GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadata) MarshalJSON ¶
func (s GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadata ¶
type GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadata struct {
	// ApiVersion: Output only. API version used to start the operation.
	ApiVersion string `json:"apiVersion,omitempty"`
	// CreateTime: Output only. The time the operation was created.
	CreateTime string `json:"createTime,omitempty"`
	// EndTime: Output only. The time the operation finished running.
	EndTime string `json:"endTime,omitempty"`
	// RequestedCancellation: Output only. Identifies whether the user has
	// requested cancellation of the operation. Operations that have successfully
	// been cancelled have Operation.error value with a google.rpc.Status.code of
	// 1, corresponding to `Code.CANCELLED`.
	RequestedCancellation bool `json:"requestedCancellation,omitempty"`
	// StatusMessage: Output only. Human-readable status of the operation, if any.
	StatusMessage string `json:"statusMessage,omitempty"`
	// Target: Output only. Server-defined resource path for the target of the
	// operation.
	Target string `json:"target,omitempty"`
	// Verb: Output only. Name of the verb executed by the operation.
	Verb string `json:"verb,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApiVersion") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApiVersion") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadata: Represents the metadata of the long-running operation.

func (GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadata) MarshalJSON ¶
func (s GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadata ¶
type GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadata struct {
	// ApiVersion: Output only. API version used to start the operation.
	ApiVersion string `json:"apiVersion,omitempty"`
	// CreateTime: Output only. The time the operation was created.
	CreateTime string `json:"createTime,omitempty"`
	// EndTime: Output only. The time the operation finished running.
	EndTime string `json:"endTime,omitempty"`
	// RequestedCancellation: Output only. Identifies whether the user has
	// requested cancellation of the operation. Operations that have successfully
	// been cancelled have Operation.error value with a google.rpc.Status.code of
	// 1, corresponding to `Code.CANCELLED`.
	RequestedCancellation bool `json:"requestedCancellation,omitempty"`
	// StatusMessage: Output only. Human-readable status of the operation, if any.
	StatusMessage string `json:"statusMessage,omitempty"`
	// Target: Output only. Server-defined resource path for the target of the
	// operation.
	Target string `json:"target,omitempty"`
	// Verb: Output only. Name of the verb executed by the operation.
	Verb string `json:"verb,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApiVersion") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApiVersion") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadata: Represents the metadata of the long-running operation.

func (GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadata) MarshalJSON ¶
func (s GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetails ¶
type GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetails struct {
	// CurrentConfigVersion: The version of the current config.
	CurrentConfigVersion string `json:"currentConfigVersion,omitempty"`
	// ErrorMsg: The latest error message.
	ErrorMsg string `json:"errorMsg,omitempty"`
	// ExpectedConfigVersion: The version of the expected config.
	ExpectedConfigVersion string `json:"expectedConfigVersion,omitempty"`
	// ExtendedStatus: The extended status. Such as ExitCode, StartedAt,
	// FinishedAt, etc.
	ExtendedStatus map[string]string `json:"extendedStatus,omitempty"`
	// ForceSendFields is a list of field names (e.g. "CurrentConfigVersion") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CurrentConfigVersion") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetails: ContainerHealthDetails reflects the health details of a container.

func (GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetails) MarshalJSON ¶
func (s GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetails) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetails ¶
type GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetails struct {
}

GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetails: RemoteAgentDetails reflects the details of a remote agent.

type GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadata ¶
added in v0.122.0
type GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadata struct {
	// ApiVersion: Output only. API version used to start the operation.
	ApiVersion string `json:"apiVersion,omitempty"`
	// CreateTime: Output only. The time the operation was created.
	CreateTime string `json:"createTime,omitempty"`
	// EndTime: Output only. The time the operation finished running.
	EndTime string `json:"endTime,omitempty"`
	// RequestedCancellation: Output only. Identifies whether the caller has
	// requested cancellation of the operation. Operations that have successfully
	// been cancelled have Operation.error value with a google.rpc.Status.code of
	// 1, corresponding to `Code.CANCELLED`.
	RequestedCancellation bool `json:"requestedCancellation,omitempty"`
	// StatusMessage: Output only. Human-readable status of the operation, if any.
	StatusMessage string `json:"statusMessage,omitempty"`
	// Target: Output only. Server-defined resource path for the target of the
	// operation.
	Target string `json:"target,omitempty"`
	// Verb: Output only. Name of the verb executed by the operation.
	Verb string `json:"verb,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApiVersion") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApiVersion") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadata: Represents the metadata of the long-running operation.

func (GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadata) MarshalJSON ¶
added in v0.122.0
func (s GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadata ¶
added in v0.122.0
type GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadata struct {
	// ApiVersion: Output only. API version used to start the operation.
	ApiVersion string `json:"apiVersion,omitempty"`
	// CreateTime: Output only. The time the operation was created.
	CreateTime string `json:"createTime,omitempty"`
	// EndTime: Output only. The time the operation finished running.
	EndTime string `json:"endTime,omitempty"`
	// RequestedCancellation: Output only. Identifies whether the caller has
	// requested cancellation of the operation. Operations that have successfully
	// been cancelled have Operation.error value with a google.rpc.Status.code of
	// 1, corresponding to `Code.CANCELLED`.
	RequestedCancellation bool `json:"requestedCancellation,omitempty"`
	// StatusMessage: Output only. Human-readable status of the operation, if any.
	StatusMessage string `json:"statusMessage,omitempty"`
	// Target: Output only. Server-defined resource path for the target of the
	// operation.
	Target string `json:"target,omitempty"`
	// Verb: Output only. Name of the verb executed by the operation.
	Verb string `json:"verb,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApiVersion") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApiVersion") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadata: Represents the metadata of the long-running operation.

func (GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadata) MarshalJSON ¶
added in v0.122.0
func (s GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1Application ¶
added in v0.200.0
type GoogleCloudBeyondcorpSecuritygatewaysV1Application struct {
	// CreateTime: Output only. Timestamp when the resource was created.
	CreateTime string `json:"createTime,omitempty"`
	// DisplayName: Optional. An arbitrary user-provided name for the application
	// resource. Cannot exceed 64 characters.
	DisplayName string `json:"displayName,omitempty"`
	// EndpointMatchers: Optional. An array of conditions to match the
	// application's network endpoint. Each element in the array is an
	// EndpointMatcher object, which defines a specific combination of a hostname
	// pattern and one or more ports. The application is considered matched if at
	// least one of the EndpointMatcher conditions in this array is met (the
	// conditions are combined using OR logic). Each EndpointMatcher must contain a
	// hostname pattern, such as "example.com", and one or more port numbers
	// specified as a string, such as "443". Hostname and port number examples:
	// "*.example.com", "443" "example.com" and "22" "example.com" and "22,33"
	EndpointMatchers []*GoogleCloudBeyondcorpSecuritygatewaysV1EndpointMatcher `json:"endpointMatchers,omitempty"`
	// Name: Identifier. Name of the resource.
	Name string `json:"name,omitempty"`
	// Schema: Optional. Type of the external application.
	//
	// Possible values:
	//   "SCHEMA_UNSPECIFIED" - Default value. This value is unused.
	//   "PROXY_GATEWAY" - Proxy which routes traffic to actual applications, like
	// Netscaler Gateway.
	//   "API_GATEWAY" - Service Discovery API endpoint when Service Discovery is
	// enabled in Gateway.
	Schema string `json:"schema,omitempty"`
	// UpdateTime: Output only. Timestamp when the resource was last modified.
	UpdateTime string `json:"updateTime,omitempty"`
	// Upstreams: Optional. Which upstream resources to forward traffic to.
	Upstreams []*GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationUpstream `json:"upstreams,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "CreateTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CreateTime") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpSecuritygatewaysV1Application: The information about an application resource.

func (GoogleCloudBeyondcorpSecuritygatewaysV1Application) MarshalJSON ¶
added in v0.200.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1Application) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationUpstream ¶
added in v0.243.0
type GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationUpstream struct {
	// EgressPolicy: Optional. Routing policy information.
	EgressPolicy *GoogleCloudBeyondcorpSecuritygatewaysV1EgressPolicy `json:"egressPolicy,omitempty"`
	// External: List of the external endpoints to forward traffic to.
	External *GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationUpstreamExternal `json:"external,omitempty"`
	// Network: Network to forward traffic to.
	Network *GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationUpstreamNetwork `json:"network,omitempty"`
	// ProxyProtocol: Optional. Enables proxy protocol configuration for the
	// upstream.
	ProxyProtocol *GoogleCloudBeyondcorpSecuritygatewaysV1ProxyProtocolConfig `json:"proxyProtocol,omitempty"`
	// ForceSendFields is a list of field names (e.g. "EgressPolicy") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "EgressPolicy") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationUpstream: Which upstream resource to forward traffic to.

func (GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationUpstream) MarshalJSON ¶
added in v0.243.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationUpstream) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationUpstreamExternal ¶
added in v0.251.0
type GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationUpstreamExternal struct {
	// Endpoints: Required. List of the endpoints to forward traffic to.
	Endpoints []*GoogleCloudBeyondcorpSecuritygatewaysV1Endpoint `json:"endpoints,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Endpoints") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Endpoints") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationUpstreamExternal: Endpoints to forward traffic to.

func (GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationUpstreamExternal) MarshalJSON ¶
added in v0.251.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationUpstreamExternal) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationUpstreamNetwork ¶
added in v0.243.0
type GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationUpstreamNetwork struct {
	// Name: Required. Network name is of the format:
	// `projects/{project}/global/networks/{network}
	Name string `json:"name,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Name") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Name") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationUpstreamNetwork: Network to forward traffic to.

func (GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationUpstreamNetwork) MarshalJSON ¶
added in v0.243.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationUpstreamNetwork) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeaders ¶
added in v0.251.0
type GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeaders struct {
	// DeviceInfo: Optional. The device information configuration.
	DeviceInfo *GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedDeviceInfo `json:"deviceInfo,omitempty"`
	// GroupInfo: Optional. Group details.
	GroupInfo *GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedGroupInfo `json:"groupInfo,omitempty"`
	// OutputType: Optional. Default output type for all enabled headers.
	//
	// Possible values:
	//   "OUTPUT_TYPE_UNSPECIFIED" - The unspecified output type.
	//   "PROTOBUF" - Protobuf output type.
	//   "JSON" - JSON output type.
	//   "NONE" - Explicitly disable header output.
	OutputType string `json:"outputType,omitempty"`
	// UserInfo: Optional. User details.
	UserInfo *GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedUserInfo `json:"userInfo,omitempty"`
	// ForceSendFields is a list of field names (e.g. "DeviceInfo") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DeviceInfo") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeaders: Contextual headers configuration.

func (GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeaders) MarshalJSON ¶
added in v0.251.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeaders) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedDeviceInfo ¶
added in v0.251.0
type GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedDeviceInfo struct {
	// OutputType: Optional. The output type details for the delegated device.
	//
	// Possible values:
	//   "OUTPUT_TYPE_UNSPECIFIED" - The unspecified output type.
	//   "PROTOBUF" - Protobuf output type.
	//   "JSON" - JSON output type.
	//   "NONE" - Explicitly disable header output.
	OutputType string `json:"outputType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "OutputType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "OutputType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedDeviceInfo: The delegated device information configuration.

func (GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedDeviceInfo) MarshalJSON ¶
added in v0.251.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedDeviceInfo) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedGroupInfo ¶
added in v0.251.0
type GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedGroupInfo struct {
	// OutputType: Optional. The output type of the delegated group information.
	//
	// Possible values:
	//   "OUTPUT_TYPE_UNSPECIFIED" - The unspecified output type.
	//   "PROTOBUF" - Protobuf output type.
	//   "JSON" - JSON output type.
	//   "NONE" - Explicitly disable header output.
	OutputType string `json:"outputType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "OutputType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "OutputType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedGroupInfo: The delegated group configuration details.

func (GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedGroupInfo) MarshalJSON ¶
added in v0.251.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedGroupInfo) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedUserInfo ¶
added in v0.251.0
type GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedUserInfo struct {
	// OutputType: Optional. The delegated user's information.
	//
	// Possible values:
	//   "OUTPUT_TYPE_UNSPECIFIED" - The unspecified output type.
	//   "PROTOBUF" - Protobuf output type.
	//   "JSON" - JSON output type.
	//   "NONE" - Explicitly disable header output.
	OutputType string `json:"outputType,omitempty"`
	// ForceSendFields is a list of field names (e.g. "OutputType") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "OutputType") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedUserInfo: The configuration information for the delegated user.

func (GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedUserInfo) MarshalJSON ¶
added in v0.251.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedUserInfo) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1EgressPolicy ¶
added in v0.243.0
type GoogleCloudBeyondcorpSecuritygatewaysV1EgressPolicy struct {
	// Regions: Required. List of the regions where the application sends traffic.
	Regions []string `json:"regions,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Regions") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Regions") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpSecuritygatewaysV1EgressPolicy: Routing policy information.

func (GoogleCloudBeyondcorpSecuritygatewaysV1EgressPolicy) MarshalJSON ¶
added in v0.243.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1EgressPolicy) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1Endpoint ¶
added in v0.251.0
type GoogleCloudBeyondcorpSecuritygatewaysV1Endpoint struct {
	// Hostname: Required. Hostname of the endpoint.
	Hostname string `json:"hostname,omitempty"`
	// Port: Required. Port of the endpoint.
	Port int64 `json:"port,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Hostname") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Hostname") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpSecuritygatewaysV1Endpoint: Internet Gateway endpoint to forward traffic to.

func (GoogleCloudBeyondcorpSecuritygatewaysV1Endpoint) MarshalJSON ¶
added in v0.251.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1Endpoint) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1EndpointMatcher ¶
added in v0.200.0
type GoogleCloudBeyondcorpSecuritygatewaysV1EndpointMatcher struct {
	// Hostname: Required. Hostname of the application.
	Hostname string `json:"hostname,omitempty"`
	// Ports: Required. The ports of the application.
	Ports []int64 `json:"ports,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Hostname") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Hostname") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpSecuritygatewaysV1EndpointMatcher: EndpointMatcher contains the information of the endpoint that will match the application.

func (GoogleCloudBeyondcorpSecuritygatewaysV1EndpointMatcher) MarshalJSON ¶
added in v0.200.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1EndpointMatcher) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1Hub ¶
added in v0.200.0
type GoogleCloudBeyondcorpSecuritygatewaysV1Hub struct {
	// InternetGateway: Optional. Internet Gateway configuration.
	InternetGateway *GoogleCloudBeyondcorpSecuritygatewaysV1InternetGateway `json:"internetGateway,omitempty"`
	// ForceSendFields is a list of field names (e.g. "InternetGateway") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "InternetGateway") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpSecuritygatewaysV1Hub: The Hub message contains information pertaining to the regional data path deployments.

func (GoogleCloudBeyondcorpSecuritygatewaysV1Hub) MarshalJSON ¶
added in v0.200.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1Hub) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1InternetGateway ¶
added in v0.201.0
type GoogleCloudBeyondcorpSecuritygatewaysV1InternetGateway struct {
	// AssignedIps: Output only. List of IP addresses assigned to the Cloud NAT.
	AssignedIps []string `json:"assignedIps,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AssignedIps") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AssignedIps") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpSecuritygatewaysV1InternetGateway: Represents the Internet Gateway configuration.

func (GoogleCloudBeyondcorpSecuritygatewaysV1InternetGateway) MarshalJSON ¶
added in v0.201.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1InternetGateway) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1ListApplicationsResponse ¶
added in v0.200.0
type GoogleCloudBeyondcorpSecuritygatewaysV1ListApplicationsResponse struct {
	// Applications: A list of BeyondCorp Application in the project.
	Applications []*GoogleCloudBeyondcorpSecuritygatewaysV1Application `json:"applications,omitempty"`
	// NextPageToken: A token to retrieve the next page of results, or empty if
	// there are no more results in the list.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Unreachable: A list of locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Applications") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Applications") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpSecuritygatewaysV1ListApplicationsResponse: Message for response to listing Applications.

func (GoogleCloudBeyondcorpSecuritygatewaysV1ListApplicationsResponse) MarshalJSON ¶
added in v0.200.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1ListApplicationsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1ListSecurityGatewaysResponse ¶
added in v0.200.0
type GoogleCloudBeyondcorpSecuritygatewaysV1ListSecurityGatewaysResponse struct {
	// NextPageToken: A token to retrieve the next page of results, or empty if
	// there are no more results in the list.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// SecurityGateways: A list of BeyondCorp SecurityGateway in the project.
	SecurityGateways []*GoogleCloudBeyondcorpSecuritygatewaysV1SecurityGateway `json:"securityGateways,omitempty"`
	// Unreachable: A list of locations that could not be reached.
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

GoogleCloudBeyondcorpSecuritygatewaysV1ListSecurityGatewaysResponse: Message for response to listing SecurityGateways.

func (GoogleCloudBeyondcorpSecuritygatewaysV1ListSecurityGatewaysResponse) MarshalJSON ¶
added in v0.200.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1ListSecurityGatewaysResponse) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1ProxyProtocolConfig ¶
added in v0.251.0
type GoogleCloudBeyondcorpSecuritygatewaysV1ProxyProtocolConfig struct {
	// AllowedClientHeaders: Optional. List of the allowed client header names.
	AllowedClientHeaders []string `json:"allowedClientHeaders,omitempty"`
	// ClientIp: Optional. Client IP configuration. The client IP address is
	// included if true.
	ClientIp bool `json:"clientIp,omitempty"`
	// ContextualHeaders: Optional. Configuration for the contextual headers.
	ContextualHeaders *GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeaders `json:"contextualHeaders,omitempty"`
	// GatewayIdentity: Optional. The security gateway identity configuration.
	//
	// Possible values:
	//   "GATEWAY_IDENTITY_UNSPECIFIED" - Unspecified gateway identity.
	//   "RESOURCE_NAME" - Resource name for gateway identity, in the format:
	// projects/{project_id}/locations/{location_id}/securityGateways/{security_gate
	// way_id}
	GatewayIdentity string `json:"gatewayIdentity,omitempty"`
	// MetadataHeaders: Optional. Custom resource specific headers along with the
	// values. The names should conform to RFC 9110: >Field names can contain
	// alphanumeric characters, hyphens, and periods, can contain only
	// ASCII-printable characters and tabs, and must start with a letter.
	MetadataHeaders map[string]string `json:"metadataHeaders,omitempty"`
	// ForceSendFields is a list of field names (e.g. "AllowedClientHeaders") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AllowedClientHeaders") to include
	// in API requests with the JSON null value. By default, fields with empty
	// values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpSecuritygatewaysV1ProxyProtocolConfig: The configuration for the proxy.

func (GoogleCloudBeyondcorpSecuritygatewaysV1ProxyProtocolConfig) MarshalJSON ¶
added in v0.251.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1ProxyProtocolConfig) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1SecurityGateway ¶
added in v0.200.0
type GoogleCloudBeyondcorpSecuritygatewaysV1SecurityGateway struct {
	// CreateTime: Output only. Timestamp when the resource was created.
	CreateTime string `json:"createTime,omitempty"`
	// DelegatingServiceAccount: Output only. Service account used for operations
	// that involve resources in consumer projects.
	DelegatingServiceAccount string `json:"delegatingServiceAccount,omitempty"`
	// DisplayName: Optional. An arbitrary user-provided name for the
	// SecurityGateway. Cannot exceed 64 characters.
	DisplayName string `json:"displayName,omitempty"`
	// ExternalIps: Output only. IP addresses that will be used for establishing
	// connection to the endpoints.
	ExternalIps []string `json:"externalIps,omitempty"`
	// Hubs: Optional. Map of Hubs that represents regional data path deployment
	// with GCP region as a key.
	Hubs map[string]GoogleCloudBeyondcorpSecuritygatewaysV1Hub `json:"hubs,omitempty"`
	// Name: Identifier. Name of the resource.
	Name string `json:"name,omitempty"`
	// ProxyProtocolConfig: Optional. Shared proxy configuration for all apps.
	ProxyProtocolConfig *GoogleCloudBeyondcorpSecuritygatewaysV1ProxyProtocolConfig `json:"proxyProtocolConfig,omitempty"`
	// ServiceDiscovery: Optional. Settings related to the Service Discovery.
	ServiceDiscovery *GoogleCloudBeyondcorpSecuritygatewaysV1ServiceDiscovery `json:"serviceDiscovery,omitempty"`
	// State: Output only. The operational state of the SecurityGateway.
	//
	// Possible values:
	//   "STATE_UNSPECIFIED" - Default value. This value is unused.
	//   "CREATING" - SecurityGateway is being created.
	//   "UPDATING" - SecurityGateway is being updated.
	//   "DELETING" - SecurityGateway is being deleted.
	//   "RUNNING" - SecurityGateway is running.
	//   "DOWN" - SecurityGateway is down and may be restored in the future.
	//   "ERROR" - SecurityGateway encountered an error and is in an
	// indeterministic state.
	State string `json:"state,omitempty"`
	// UpdateTime: Output only. Timestamp when the resource was last modified.
	UpdateTime string `json:"updateTime,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "CreateTime") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "CreateTime") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpSecuritygatewaysV1SecurityGateway: The information about a security gateway resource.

func (GoogleCloudBeyondcorpSecuritygatewaysV1SecurityGateway) MarshalJSON ¶
added in v0.200.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1SecurityGateway) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1SecurityGatewayOperationMetadata ¶
added in v0.200.0
type GoogleCloudBeyondcorpSecuritygatewaysV1SecurityGatewayOperationMetadata struct {
	// ApiVersion: Output only. API version used to start the operation.
	ApiVersion string `json:"apiVersion,omitempty"`
	// CreateTime: Output only. The time the operation was created.
	CreateTime string `json:"createTime,omitempty"`
	// EndTime: Output only. The time the operation finished running.
	EndTime string `json:"endTime,omitempty"`
	// RequestedCancellation: Output only. Identifies whether the user has
	// requested cancellation of the operation. Operations that have been cancelled
	// successfully have Operation.error value with a google.rpc.Status.code of 1,
	// corresponding to `Code.CANCELLED`.
	RequestedCancellation bool `json:"requestedCancellation,omitempty"`
	// StatusMessage: Output only. Human-readable status of the operation, if any.
	StatusMessage string `json:"statusMessage,omitempty"`
	// Target: Output only. Server-defined resource path for the target of the
	// operation.
	Target string `json:"target,omitempty"`
	// Verb: Output only. Name of the verb executed by the operation.
	Verb string `json:"verb,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApiVersion") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApiVersion") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpSecuritygatewaysV1SecurityGatewayOperationMetadata: Represents the metadata of the long-running operation.

func (GoogleCloudBeyondcorpSecuritygatewaysV1SecurityGatewayOperationMetadata) MarshalJSON ¶
added in v0.200.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1SecurityGatewayOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1ServiceDiscovery ¶
added in v0.251.0
type GoogleCloudBeyondcorpSecuritygatewaysV1ServiceDiscovery struct {
	// ApiGateway: Required. External API configuration.
	ApiGateway *GoogleCloudBeyondcorpSecuritygatewaysV1ServiceDiscoveryApiGateway `json:"apiGateway,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApiGateway") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApiGateway") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpSecuritygatewaysV1ServiceDiscovery: Settings related to the Service Discovery.

func (GoogleCloudBeyondcorpSecuritygatewaysV1ServiceDiscovery) MarshalJSON ¶
added in v0.251.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1ServiceDiscovery) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1ServiceDiscoveryApiGateway ¶
added in v0.251.0
type GoogleCloudBeyondcorpSecuritygatewaysV1ServiceDiscoveryApiGateway struct {
	// ResourceOverride: Required. Enables fetching resource model updates to alter
	// service behavior per Chrome profile.
	ResourceOverride *GoogleCloudBeyondcorpSecuritygatewaysV1ServiceDiscoveryApiGatewayOperationDescriptor `json:"resourceOverride,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ResourceOverride") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ResourceOverride") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpSecuritygatewaysV1ServiceDiscoveryApiGateway: If Service Discovery is done through API, defines its settings.

func (GoogleCloudBeyondcorpSecuritygatewaysV1ServiceDiscoveryApiGateway) MarshalJSON ¶
added in v0.251.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1ServiceDiscoveryApiGateway) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1ServiceDiscoveryApiGatewayOperationDescriptor ¶
added in v0.251.0
type GoogleCloudBeyondcorpSecuritygatewaysV1ServiceDiscoveryApiGatewayOperationDescriptor struct {
	// Path: Required. Contains the URI path fragment where HTTP request is sent.
	Path string `json:"path,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Path") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Path") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpSecuritygatewaysV1ServiceDiscoveryApiGatewayOperationDes criptor: API operation descriptor.

func (GoogleCloudBeyondcorpSecuritygatewaysV1ServiceDiscoveryApiGatewayOperationDescriptor) MarshalJSON ¶
added in v0.251.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1ServiceDiscoveryApiGatewayOperationDescriptor) MarshalJSON() ([]byte, error)
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaSecurityGatewayOperationMetadata ¶
added in v0.170.0
type GoogleCloudBeyondcorpSecuritygatewaysV1alphaSecurityGatewayOperationMetadata struct {
	// ApiVersion: Output only. API version used to start the operation.
	ApiVersion string `json:"apiVersion,omitempty"`
	// CreateTime: Output only. The time the operation was created.
	CreateTime string `json:"createTime,omitempty"`
	// EndTime: Output only. The time the operation finished running.
	EndTime string `json:"endTime,omitempty"`
	// RequestedCancellation: Output only. Identifies whether the user has
	// requested cancellation of the operation. Operations that have been cancelled
	// successfully have Operation.error value with a google.rpc.Status.code of 1,
	// corresponding to `Code.CANCELLED`.
	RequestedCancellation bool `json:"requestedCancellation,omitempty"`
	// StatusMessage: Output only. Human-readable status of the operation, if any.
	StatusMessage string `json:"statusMessage,omitempty"`
	// Target: Output only. Server-defined resource path for the target of the
	// operation.
	Target string `json:"target,omitempty"`
	// Verb: Output only. Name of the verb executed by the operation.
	Verb string `json:"verb,omitempty"`
	// ForceSendFields is a list of field names (e.g. "ApiVersion") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "ApiVersion") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudBeyondcorpSecuritygatewaysV1alphaSecurityGatewayOperationMetadata:

Represents the metadata of the long-running operation.

func (GoogleCloudBeyondcorpSecuritygatewaysV1alphaSecurityGatewayOperationMetadata) MarshalJSON ¶
added in v0.170.0
func (s GoogleCloudBeyondcorpSecuritygatewaysV1alphaSecurityGatewayOperationMetadata) MarshalJSON() ([]byte, error)
type GoogleCloudLocationListLocationsResponse ¶
type GoogleCloudLocationListLocationsResponse struct {
	// Locations: A list of locations that matches the specified filter in the
	// request.
	Locations []*GoogleCloudLocationLocation `json:"locations,omitempty"`
	// NextPageToken: The standard List next-page token.
	NextPageToken string `json:"nextPageToken,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "Locations") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Locations") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudLocationListLocationsResponse: The response message for Locations.ListLocations.

func (GoogleCloudLocationListLocationsResponse) MarshalJSON ¶
func (s GoogleCloudLocationListLocationsResponse) MarshalJSON() ([]byte, error)
type GoogleCloudLocationLocation ¶
type GoogleCloudLocationLocation struct {
	// DisplayName: The friendly name for this location, typically a nearby city
	// name. For example, "Tokyo".
	DisplayName string `json:"displayName,omitempty"`
	// Labels: Cross-service attributes for the location. For example
	// {"cloud.googleapis.com/region": "us-east1"}
	Labels map[string]string `json:"labels,omitempty"`
	// LocationId: The canonical id for this location. For example: "us-east1".
	LocationId string `json:"locationId,omitempty"`
	// Metadata: Service-specific metadata. For example the available capacity at
	// the given location.
	Metadata googleapi.RawMessage `json:"metadata,omitempty"`
	// Name: Resource name for the location, which may vary between
	// implementations. For example:
	// "projects/example-project/locations/us-east1"
	Name string `json:"name,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "DisplayName") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "DisplayName") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

GoogleCloudLocationLocation: A resource that represents a Google Cloud location.

func (GoogleCloudLocationLocation) MarshalJSON ¶
func (s GoogleCloudLocationLocation) MarshalJSON() ([]byte, error)
type GoogleIamV1AuditConfig ¶
type GoogleIamV1AuditConfig struct {
	// AuditLogConfigs: The configuration for logging of each type of permission.
	AuditLogConfigs []*GoogleIamV1AuditLogConfig `json:"auditLogConfigs,omitempty"`
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

GoogleIamV1AuditConfig: Specifies the audit configuration for a service. The configuration determines which permission types are logged, and what identities, if any, are exempted from logging. An AuditConfig must have one or more AuditLogConfigs. If there are AuditConfigs for both `allServices` and a specific service, the union of the two AuditConfigs is used for that service: the log_types specified in each AuditConfig are enabled, and the exempted_members in each AuditLogConfig are exempted. Example Policy with multiple AuditConfigs: { "audit_configs": [ { "service": "allServices", "audit_log_configs": [ { "log_type": "DATA_READ", "exempted_members": [ "user:jose@example.com" ] }, { "log_type": "DATA_WRITE" }, { "log_type": "ADMIN_READ" } ] }, { "service": "sampleservice.googleapis.com", "audit_log_configs": [ { "log_type": "DATA_READ" }, { "log_type": "DATA_WRITE", "exempted_members": [ "user:aliya@example.com" ] } ] } ] } For sampleservice, this policy enables DATA_READ, DATA_WRITE and ADMIN_READ logging. It also exempts `jose@example.com` from DATA_READ logging, and `aliya@example.com` from DATA_WRITE logging.

func (GoogleIamV1AuditConfig) MarshalJSON ¶
func (s GoogleIamV1AuditConfig) MarshalJSON() ([]byte, error)
type GoogleIamV1AuditLogConfig ¶
type GoogleIamV1AuditLogConfig struct {
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

GoogleIamV1AuditLogConfig: Provides the configuration for logging a type of permissions. Example: { "audit_log_configs": [ { "log_type": "DATA_READ", "exempted_members": [ "user:jose@example.com" ] }, { "log_type": "DATA_WRITE" } ] } This enables 'DATA_READ' and 'DATA_WRITE' logging, while exempting jose@example.com from DATA_READ logging.

func (GoogleIamV1AuditLogConfig) MarshalJSON ¶
func (s GoogleIamV1AuditLogConfig) MarshalJSON() ([]byte, error)
type GoogleIamV1Binding ¶
type GoogleIamV1Binding struct {
	// Condition: The condition that is associated with this binding. If the
	// condition evaluates to `true`, then this binding applies to the current
	// request. If the condition evaluates to `false`, then this binding does not
	// apply to the current request. However, a different role binding might grant
	// the same role to one or more of the principals in this binding. To learn
	// which resources support conditions in their IAM policies, see the IAM
	// documentation
	// (https://cloud.google.com/iam/help/conditions/resource-policies).
	Condition *GoogleTypeExpr `json:"condition,omitempty"`
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

GoogleIamV1Binding: Associates `members`, or principals, with a `role`.

func (GoogleIamV1Binding) MarshalJSON ¶
func (s GoogleIamV1Binding) MarshalJSON() ([]byte, error)
type GoogleIamV1Policy ¶
type GoogleIamV1Policy struct {
	// AuditConfigs: Specifies cloud audit logging configuration for this policy.
	AuditConfigs []*GoogleIamV1AuditConfig `json:"auditConfigs,omitempty"`
	// Bindings: Associates a list of `members`, or principals, with a `role`.
	// Optionally, may specify a `condition` that determines how and when the
	// `bindings` are applied. Each of the `bindings` must contain at least one
	// principal. The `bindings` in a `Policy` can refer to up to 1,500 principals;
	// up to 250 of these principals can be Google groups. Each occurrence of a
	// principal counts towards these limits. For example, if the `bindings` grant
	// 50 different roles to `user:alice@example.com`, and not to any other
	// principal, then you can add another 1,450 principals to the `bindings` in
	// the `Policy`.
	Bindings []*GoogleIamV1Binding `json:"bindings,omitempty"`
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

GoogleIamV1Policy: An Identity and Access Management (IAM) policy, which specifies access controls for Google Cloud resources. A `Policy` is a collection of `bindings`. A `binding` binds one or more `members`, or principals, to a single `role`. Principals can be user accounts, service accounts, Google groups, and domains (such as G Suite). A `role` is a named list of permissions; each `role` can be an IAM predefined role or a user-created custom role. For some types of Google Cloud resources, a `binding` can also specify a `condition`, which is a logical expression that allows access to a resource only if the expression evaluates to `true`. A condition can add constraints based on attributes of the request, the resource, or both. To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies). **JSON example:** ``` { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": [ "user:eve@example.com" ], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01T00:00:00.000Z')", } } ], "etag": "BwWWja0YfJA=", "version": 3 } ``` **YAML example:** ``` bindings: - members: - user:mike@example.com - group:admins@example.com - domain:google.com - serviceAccount:my-project-id@appspot.gserviceaccount.com role: roles/resourcemanager.organizationAdmin - members: - user:eve@example.com role: roles/resourcemanager.organizationViewer condition: title: expirable access description: Does not grant access after Sep 2020 expression: request.time < timestamp('2020-10-01T00:00:00.000Z') etag: BwWWja0YfJA= version: 3 ``` For a description of IAM and its features, see the IAM documentation (https://cloud.google.com/iam/docs/).

func (GoogleIamV1Policy) MarshalJSON ¶
func (s GoogleIamV1Policy) MarshalJSON() ([]byte, error)
type GoogleIamV1SetIamPolicyRequest ¶
type GoogleIamV1SetIamPolicyRequest struct {
	// Policy: REQUIRED: The complete policy to be applied to the `resource`. The
	// size of the policy is limited to a few 10s of KB. An empty policy is a valid
	// policy but certain Google Cloud services (such as Projects) might reject
	// them.
	Policy *GoogleIamV1Policy `json:"policy,omitempty"`
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

GoogleIamV1SetIamPolicyRequest: Request message for `SetIamPolicy` method.

func (GoogleIamV1SetIamPolicyRequest) MarshalJSON ¶
func (s GoogleIamV1SetIamPolicyRequest) MarshalJSON() ([]byte, error)
type GoogleIamV1TestIamPermissionsRequest ¶
type GoogleIamV1TestIamPermissionsRequest struct {
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

GoogleIamV1TestIamPermissionsRequest: Request message for `TestIamPermissions` method.

func (GoogleIamV1TestIamPermissionsRequest) MarshalJSON ¶
func (s GoogleIamV1TestIamPermissionsRequest) MarshalJSON() ([]byte, error)
type GoogleIamV1TestIamPermissionsResponse ¶
type GoogleIamV1TestIamPermissionsResponse struct {
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

GoogleIamV1TestIamPermissionsResponse: Response message for `TestIamPermissions` method.

func (GoogleIamV1TestIamPermissionsResponse) MarshalJSON ¶
func (s GoogleIamV1TestIamPermissionsResponse) MarshalJSON() ([]byte, error)
type GoogleLongrunningCancelOperationRequest ¶
type GoogleLongrunningCancelOperationRequest struct {
}

GoogleLongrunningCancelOperationRequest: The request message for Operations.CancelOperation.

type GoogleLongrunningListOperationsResponse ¶
type GoogleLongrunningListOperationsResponse struct {
	// NextPageToken: The standard List next-page token.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Operations: A list of operations that matches the specified filter in the
	// request.
	Operations []*GoogleLongrunningOperation `json:"operations,omitempty"`
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

GoogleLongrunningListOperationsResponse: The response message for Operations.ListOperations.

func (GoogleLongrunningListOperationsResponse) MarshalJSON ¶
func (s GoogleLongrunningListOperationsResponse) MarshalJSON() ([]byte, error)
type GoogleLongrunningOperation ¶
type GoogleLongrunningOperation struct {
	// Done: If the value is `false`, it means the operation is still in progress.
	// If `true`, the operation is completed, and either `error` or `response` is
	// available.
	Done bool `json:"done,omitempty"`
	// Error: The error result of the operation in case of failure or cancellation.
	Error *GoogleRpcStatus `json:"error,omitempty"`
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

GoogleLongrunningOperation: This resource represents a long-running operation that is the result of a network API call.

func (GoogleLongrunningOperation) MarshalJSON ¶
func (s GoogleLongrunningOperation) MarshalJSON() ([]byte, error)
type GoogleRpcStatus ¶
type GoogleRpcStatus struct {
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

GoogleRpcStatus: The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by gRPC (https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the API Design Guide (https://cloud.google.com/apis/design/errors).

func (GoogleRpcStatus) MarshalJSON ¶
func (s GoogleRpcStatus) MarshalJSON() ([]byte, error)
type GoogleTypeExpr ¶
type GoogleTypeExpr struct {
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

GoogleTypeExpr: Represents a textual expression in the Common Expression Language (CEL) syntax. CEL is a C-like expression language. The syntax and semantics of CEL are documented at https://github.com/google/cel-spec. Example (Comparison): title: "Summary size limit" description: "Determines if a summary is less than 100 chars" expression: "document.summary.size() < 100" Example (Equality): title: "Requestor is owner" description: "Determines if requestor is the document owner" expression: "document.owner == request.auth.claims.email" Example (Logic): title: "Public documents" description: "Determine whether the document should be publicly visible" expression: "document.type != 'private' && document.type != 'internal'" Example (Data Manipulation): title: "Notification string" description: "Create a notification string with a timestamp." expression: "'New message received at ' + string(document.create_time)" The exact variables and functions that may be referenced within an expression are determined by the service that evaluates it. See the service documentation for additional information.

func (GoogleTypeExpr) MarshalJSON ¶
func (s GoogleTypeExpr) MarshalJSON() ([]byte, error)
type ListAppGatewaysResponse ¶
added in v0.89.0
type ListAppGatewaysResponse struct {
	// AppGateways: A list of BeyondCorp AppGateways in the project.
	AppGateways []*AppGateway `json:"appGateways,omitempty"`
	// NextPageToken: A token to retrieve the next page of results, or empty if
	// there are no more results in the list.
	NextPageToken string `json:"nextPageToken,omitempty"`
	// Unreachable: A list of locations that could not be reached.
	Unreachable []string `json:"unreachable,omitempty"`

	// ServerResponse contains the HTTP response code and headers from the server.
	googleapi.ServerResponse `json:"-"`
	// ForceSendFields is a list of field names (e.g. "AppGateways") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "AppGateways") to include in API
	// requests with the JSON null value. By default, fields with empty values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

ListAppGatewaysResponse: Response message for BeyondCorp.ListAppGateways.

func (ListAppGatewaysResponse) MarshalJSON ¶
added in v0.89.0
func (s ListAppGatewaysResponse) MarshalJSON() ([]byte, error)
type OrganizationsLocationsOperationsCancelCall ¶
added in v0.129.0
type OrganizationsLocationsOperationsCancelCall struct {
	// contains filtered or unexported fields
}
func (*OrganizationsLocationsOperationsCancelCall) Context ¶
added in v0.129.0
func (c *OrganizationsLocationsOperationsCancelCall) Context(ctx context.Context) *OrganizationsLocationsOperationsCancelCall

Context sets the context to be used in this call's Do method.

func (*OrganizationsLocationsOperationsCancelCall) Do ¶
added in v0.129.0
func (c *OrganizationsLocationsOperationsCancelCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "beyondcorp.organizations.locations.operations.cancel" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*OrganizationsLocationsOperationsCancelCall) Fields ¶
added in v0.129.0
func (c *OrganizationsLocationsOperationsCancelCall) Fields(s ...googleapi.Field) *OrganizationsLocationsOperationsCancelCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OrganizationsLocationsOperationsCancelCall) Header ¶
added in v0.129.0
func (c *OrganizationsLocationsOperationsCancelCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type OrganizationsLocationsOperationsDeleteCall ¶
added in v0.129.0
type OrganizationsLocationsOperationsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*OrganizationsLocationsOperationsDeleteCall) Context ¶
added in v0.129.0
func (c *OrganizationsLocationsOperationsDeleteCall) Context(ctx context.Context) *OrganizationsLocationsOperationsDeleteCall

Context sets the context to be used in this call's Do method.

func (*OrganizationsLocationsOperationsDeleteCall) Do ¶
added in v0.129.0
func (c *OrganizationsLocationsOperationsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "beyondcorp.organizations.locations.operations.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*OrganizationsLocationsOperationsDeleteCall) Fields ¶
added in v0.129.0
func (c *OrganizationsLocationsOperationsDeleteCall) Fields(s ...googleapi.Field) *OrganizationsLocationsOperationsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OrganizationsLocationsOperationsDeleteCall) Header ¶
added in v0.129.0
func (c *OrganizationsLocationsOperationsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type OrganizationsLocationsOperationsGetCall ¶
added in v0.129.0
type OrganizationsLocationsOperationsGetCall struct {
	// contains filtered or unexported fields
}
func (*OrganizationsLocationsOperationsGetCall) Context ¶
added in v0.129.0
func (c *OrganizationsLocationsOperationsGetCall) Context(ctx context.Context) *OrganizationsLocationsOperationsGetCall

Context sets the context to be used in this call's Do method.

func (*OrganizationsLocationsOperationsGetCall) Do ¶
added in v0.129.0
func (c *OrganizationsLocationsOperationsGetCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.organizations.locations.operations.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*OrganizationsLocationsOperationsGetCall) Fields ¶
added in v0.129.0
func (c *OrganizationsLocationsOperationsGetCall) Fields(s ...googleapi.Field) *OrganizationsLocationsOperationsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OrganizationsLocationsOperationsGetCall) Header ¶
added in v0.129.0
func (c *OrganizationsLocationsOperationsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*OrganizationsLocationsOperationsGetCall) IfNoneMatch ¶
added in v0.129.0
func (c *OrganizationsLocationsOperationsGetCall) IfNoneMatch(entityTag string) *OrganizationsLocationsOperationsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type OrganizationsLocationsOperationsListCall ¶
added in v0.129.0
type OrganizationsLocationsOperationsListCall struct {
	// contains filtered or unexported fields
}
func (*OrganizationsLocationsOperationsListCall) Context ¶
added in v0.129.0
func (c *OrganizationsLocationsOperationsListCall) Context(ctx context.Context) *OrganizationsLocationsOperationsListCall

Context sets the context to be used in this call's Do method.

func (*OrganizationsLocationsOperationsListCall) Do ¶
added in v0.129.0
func (c *OrganizationsLocationsOperationsListCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningListOperationsResponse, error)

Do executes the "beyondcorp.organizations.locations.operations.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningListOperationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*OrganizationsLocationsOperationsListCall) Fields ¶
added in v0.129.0
func (c *OrganizationsLocationsOperationsListCall) Fields(s ...googleapi.Field) *OrganizationsLocationsOperationsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*OrganizationsLocationsOperationsListCall) Filter ¶
added in v0.129.0
func (c *OrganizationsLocationsOperationsListCall) Filter(filter string) *OrganizationsLocationsOperationsListCall

Filter sets the optional parameter "filter": The standard list filter.

func (*OrganizationsLocationsOperationsListCall) Header ¶
added in v0.129.0
func (c *OrganizationsLocationsOperationsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*OrganizationsLocationsOperationsListCall) IfNoneMatch ¶
added in v0.129.0
func (c *OrganizationsLocationsOperationsListCall) IfNoneMatch(entityTag string) *OrganizationsLocationsOperationsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*OrganizationsLocationsOperationsListCall) PageSize ¶
added in v0.129.0
func (c *OrganizationsLocationsOperationsListCall) PageSize(pageSize int64) *OrganizationsLocationsOperationsListCall

PageSize sets the optional parameter "pageSize": The standard list page size.

func (*OrganizationsLocationsOperationsListCall) PageToken ¶
added in v0.129.0
func (c *OrganizationsLocationsOperationsListCall) PageToken(pageToken string) *OrganizationsLocationsOperationsListCall

PageToken sets the optional parameter "pageToken": The standard list page token.

func (*OrganizationsLocationsOperationsListCall) Pages ¶
added in v0.129.0
func (c *OrganizationsLocationsOperationsListCall) Pages(ctx context.Context, f func(*GoogleLongrunningListOperationsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*OrganizationsLocationsOperationsListCall) ReturnPartialSuccess ¶
added in v0.253.0
func (c *OrganizationsLocationsOperationsListCall) ReturnPartialSuccess(returnPartialSuccess bool) *OrganizationsLocationsOperationsListCall

ReturnPartialSuccess sets the optional parameter "returnPartialSuccess": When set to `true`, operations that are reachable are returned as normal, and those that are unreachable are returned in the ListOperationsResponse.unreachable field. This can only be `true` when reading across collections. For example, when `parent` is set to "projects/example/locations/-". This field is not supported by default and will result in an `UNIMPLEMENTED` error if set unless explicitly documented otherwise in service or product specific documentation.

type OrganizationsLocationsOperationsService ¶
added in v0.129.0
type OrganizationsLocationsOperationsService struct {
	// contains filtered or unexported fields
}
func NewOrganizationsLocationsOperationsService ¶
added in v0.129.0
func NewOrganizationsLocationsOperationsService(s *Service) *OrganizationsLocationsOperationsService
func (*OrganizationsLocationsOperationsService) Cancel ¶
added in v0.129.0
func (r *OrganizationsLocationsOperationsService) Cancel(name string, googlelongrunningcanceloperationrequest *GoogleLongrunningCancelOperationRequest) *OrganizationsLocationsOperationsCancelCall

Cancel: Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of `1`, corresponding to `Code.CANCELLED`.

- name: The name of the operation resource to be cancelled.

func (*OrganizationsLocationsOperationsService) Delete ¶
added in v0.129.0
func (r *OrganizationsLocationsOperationsService) Delete(name string) *OrganizationsLocationsOperationsDeleteCall

Delete: Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

- name: The name of the operation resource to be deleted.

func (*OrganizationsLocationsOperationsService) Get ¶
added in v0.129.0
func (r *OrganizationsLocationsOperationsService) Get(name string) *OrganizationsLocationsOperationsGetCall

Get: Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

- name: The name of the operation resource.

func (*OrganizationsLocationsOperationsService) List ¶
added in v0.129.0
func (r *OrganizationsLocationsOperationsService) List(name string) *OrganizationsLocationsOperationsListCall

List: Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.

- name: The name of the operation's parent resource.

type OrganizationsLocationsService ¶
added in v0.122.0
type OrganizationsLocationsService struct {
	Operations *OrganizationsLocationsOperationsService
	// contains filtered or unexported fields
}
func NewOrganizationsLocationsService ¶
added in v0.122.0
func NewOrganizationsLocationsService(s *Service) *OrganizationsLocationsService
type OrganizationsService ¶
added in v0.122.0
type OrganizationsService struct {
	Locations *OrganizationsLocationsService
	// contains filtered or unexported fields
}
func NewOrganizationsService ¶
added in v0.122.0
func NewOrganizationsService(s *Service) *OrganizationsService
type ProjectsLocationsAppConnectionsCreateCall ¶
added in v0.89.0
type ProjectsLocationsAppConnectionsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectionsCreateCall) AppConnectionId ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsCreateCall) AppConnectionId(appConnectionId string) *ProjectsLocationsAppConnectionsCreateCall

AppConnectionId sets the optional parameter "appConnectionId": User-settable AppConnection resource ID. * Must start with a letter. * Must contain between 4-63 characters from `/a-z-/`. * Must end with a number or a letter.

func (*ProjectsLocationsAppConnectionsCreateCall) Context ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsCreateCall) Context(ctx context.Context) *ProjectsLocationsAppConnectionsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectionsCreateCall) Do ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.appConnections.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectionsCreateCall) Fields ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectionsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectionsCreateCall) Header ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppConnectionsCreateCall) RequestId ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsCreateCall) RequestId(requestId string) *ProjectsLocationsAppConnectionsCreateCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsAppConnectionsCreateCall) ValidateOnly ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsCreateCall) ValidateOnly(validateOnly bool) *ProjectsLocationsAppConnectionsCreateCall

ValidateOnly sets the optional parameter "validateOnly": If set, validates request by executing a dry-run which would not alter the resource in any way.

type ProjectsLocationsAppConnectionsDeleteCall ¶
added in v0.89.0
type ProjectsLocationsAppConnectionsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectionsDeleteCall) Context ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsDeleteCall) Context(ctx context.Context) *ProjectsLocationsAppConnectionsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectionsDeleteCall) Do ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.appConnections.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectionsDeleteCall) Fields ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectionsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectionsDeleteCall) Header ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppConnectionsDeleteCall) RequestId ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsDeleteCall) RequestId(requestId string) *ProjectsLocationsAppConnectionsDeleteCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsAppConnectionsDeleteCall) ValidateOnly ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsDeleteCall) ValidateOnly(validateOnly bool) *ProjectsLocationsAppConnectionsDeleteCall

ValidateOnly sets the optional parameter "validateOnly": If set, validates request by executing a dry-run which would not alter the resource in any way.

type ProjectsLocationsAppConnectionsGetCall ¶
added in v0.89.0
type ProjectsLocationsAppConnectionsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectionsGetCall) Context ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsGetCall) Context(ctx context.Context) *ProjectsLocationsAppConnectionsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectionsGetCall) Do ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpAppconnectionsV1AppConnection, error)

Do executes the "beyondcorp.projects.locations.appConnections.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpAppconnectionsV1AppConnection.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectionsGetCall) Fields ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectionsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectionsGetCall) Header ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppConnectionsGetCall) IfNoneMatch ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsAppConnectionsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsAppConnectionsGetIamPolicyCall ¶
type ProjectsLocationsAppConnectionsGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectionsGetIamPolicyCall) Context ¶
func (c *ProjectsLocationsAppConnectionsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsAppConnectionsGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectionsGetIamPolicyCall) Do ¶
func (c *ProjectsLocationsAppConnectionsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)

Do executes the "beyondcorp.projects.locations.appConnections.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *GoogleIamV1Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectionsGetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsAppConnectionsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectionsGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectionsGetIamPolicyCall) Header ¶
func (c *ProjectsLocationsAppConnectionsGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppConnectionsGetIamPolicyCall) IfNoneMatch ¶
func (c *ProjectsLocationsAppConnectionsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsAppConnectionsGetIamPolicyCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsAppConnectionsGetIamPolicyCall) OptionsRequestedPolicyVersion ¶
func (c *ProjectsLocationsAppConnectionsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsAppConnectionsGetIamPolicyCall

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies).

type ProjectsLocationsAppConnectionsListCall ¶
added in v0.89.0
type ProjectsLocationsAppConnectionsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectionsListCall) Context ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsListCall) Context(ctx context.Context) *ProjectsLocationsAppConnectionsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectionsListCall) Do ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponse, error)

Do executes the "beyondcorp.projects.locations.appConnections.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponse.ServerRespon se.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectionsListCall) Fields ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectionsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectionsListCall) Filter ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsListCall) Filter(filter string) *ProjectsLocationsAppConnectionsListCall

Filter sets the optional parameter "filter": A filter specifying constraints of a list operation.

func (*ProjectsLocationsAppConnectionsListCall) Header ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppConnectionsListCall) IfNoneMatch ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsAppConnectionsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsAppConnectionsListCall) OrderBy ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsListCall) OrderBy(orderBy string) *ProjectsLocationsAppConnectionsListCall

OrderBy sets the optional parameter "orderBy": Specifies the ordering of results. See Sorting order (https://cloud.google.com/apis/design/design_patterns#sorting_order) for more information.

func (*ProjectsLocationsAppConnectionsListCall) PageSize ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsListCall) PageSize(pageSize int64) *ProjectsLocationsAppConnectionsListCall

PageSize sets the optional parameter "pageSize": The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's next_page_token to determine if there are more instances left to be queried.

func (*ProjectsLocationsAppConnectionsListCall) PageToken ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsListCall) PageToken(pageToken string) *ProjectsLocationsAppConnectionsListCall

PageToken sets the optional parameter "pageToken": The next_page_token value returned from a previous ListAppConnectionsRequest, if any.

func (*ProjectsLocationsAppConnectionsListCall) Pages ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsListCall) Pages(ctx context.Context, f func(*GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsAppConnectionsPatchCall ¶
added in v0.89.0
type ProjectsLocationsAppConnectionsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectionsPatchCall) AllowMissing ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsPatchCall) AllowMissing(allowMissing bool) *ProjectsLocationsAppConnectionsPatchCall

AllowMissing sets the optional parameter "allowMissing": If set as true, will create the resource if it is not found.

func (*ProjectsLocationsAppConnectionsPatchCall) Context ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsPatchCall) Context(ctx context.Context) *ProjectsLocationsAppConnectionsPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectionsPatchCall) Do ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.appConnections.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectionsPatchCall) Fields ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectionsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectionsPatchCall) Header ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppConnectionsPatchCall) RequestId ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsPatchCall) RequestId(requestId string) *ProjectsLocationsAppConnectionsPatchCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsAppConnectionsPatchCall) UpdateMask ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsAppConnectionsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. Mask of fields to update. At least one path must be supplied in this field. The elements of the repeated paths field may only include these fields from [BeyondCorp.AppConnection]: * `labels` * `display_name` * `application_endpoint` * `connectors`

func (*ProjectsLocationsAppConnectionsPatchCall) ValidateOnly ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsPatchCall) ValidateOnly(validateOnly bool) *ProjectsLocationsAppConnectionsPatchCall

ValidateOnly sets the optional parameter "validateOnly": If set, validates request by executing a dry-run which would not alter the resource in any way.

type ProjectsLocationsAppConnectionsResolveCall ¶
added in v0.89.0
type ProjectsLocationsAppConnectionsResolveCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectionsResolveCall) AppConnectorId ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsResolveCall) AppConnectorId(appConnectorId string) *ProjectsLocationsAppConnectionsResolveCall

AppConnectorId sets the optional parameter "appConnectorId": Required. BeyondCorp Connector name of the connector associated with those AppConnections using the form: `projects/{project_id}/locations/{location_id}/appConnectors/{app_connector_i d}`

func (*ProjectsLocationsAppConnectionsResolveCall) Context ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsResolveCall) Context(ctx context.Context) *ProjectsLocationsAppConnectionsResolveCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectionsResolveCall) Do ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsResolveCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponse, error)

Do executes the "beyondcorp.projects.locations.appConnections.resolve" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponse.ServerRes ponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectionsResolveCall) Fields ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsResolveCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectionsResolveCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectionsResolveCall) Header ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsResolveCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppConnectionsResolveCall) IfNoneMatch ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsResolveCall) IfNoneMatch(entityTag string) *ProjectsLocationsAppConnectionsResolveCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsAppConnectionsResolveCall) PageSize ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsResolveCall) PageSize(pageSize int64) *ProjectsLocationsAppConnectionsResolveCall

PageSize sets the optional parameter "pageSize": The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's next_page_token to determine if there are more instances left to be queried.

func (*ProjectsLocationsAppConnectionsResolveCall) PageToken ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsResolveCall) PageToken(pageToken string) *ProjectsLocationsAppConnectionsResolveCall

PageToken sets the optional parameter "pageToken": The next_page_token value returned from a previous ResolveAppConnectionsResponse, if any.

func (*ProjectsLocationsAppConnectionsResolveCall) Pages ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectionsResolveCall) Pages(ctx context.Context, f func(*GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsAppConnectionsService ¶
type ProjectsLocationsAppConnectionsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsAppConnectionsService ¶
func NewProjectsLocationsAppConnectionsService(s *Service) *ProjectsLocationsAppConnectionsService
func (*ProjectsLocationsAppConnectionsService) Create ¶
added in v0.89.0
func (r *ProjectsLocationsAppConnectionsService) Create(parent string, googlecloudbeyondcorpappconnectionsv1appconnection *GoogleCloudBeyondcorpAppconnectionsV1AppConnection) *ProjectsLocationsAppConnectionsCreateCall

Create: Creates a new AppConnection in a given project and location.

parent: The resource project name of the AppConnection location using the form: `projects/{project_id}/locations/{location_id}`.
func (*ProjectsLocationsAppConnectionsService) Delete ¶
added in v0.89.0
func (r *ProjectsLocationsAppConnectionsService) Delete(name string) *ProjectsLocationsAppConnectionsDeleteCall

Delete: Deletes a single AppConnection.

name: BeyondCorp Connector name using the form: `projects/{project_id}/locations/{location_id}/appConnections/{app_connecti on_id}`.
func (*ProjectsLocationsAppConnectionsService) Get ¶
added in v0.89.0
func (r *ProjectsLocationsAppConnectionsService) Get(name string) *ProjectsLocationsAppConnectionsGetCall

Get: Gets details of a single AppConnection.

name: BeyondCorp AppConnection name using the form: `projects/{project_id}/locations/{location_id}/appConnections/{app_connecti on_id}`.
func (*ProjectsLocationsAppConnectionsService) GetIamPolicy ¶
func (r *ProjectsLocationsAppConnectionsService) GetIamPolicy(resource string) *ProjectsLocationsAppConnectionsGetIamPolicyCall

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsAppConnectionsService) List ¶
added in v0.89.0
func (r *ProjectsLocationsAppConnectionsService) List(parent string) *ProjectsLocationsAppConnectionsListCall

List: Lists AppConnections in a given project and location.

parent: The resource name of the AppConnection location using the form: `projects/{project_id}/locations/{location_id}`.
func (*ProjectsLocationsAppConnectionsService) Patch ¶
added in v0.89.0
func (r *ProjectsLocationsAppConnectionsService) Patch(name string, googlecloudbeyondcorpappconnectionsv1appconnection *GoogleCloudBeyondcorpAppconnectionsV1AppConnection) *ProjectsLocationsAppConnectionsPatchCall

Patch: Updates the parameters of a single AppConnection.

name: Unique resource name of the AppConnection. The name is ignored when creating a AppConnection.
func (*ProjectsLocationsAppConnectionsService) Resolve ¶
added in v0.89.0
func (r *ProjectsLocationsAppConnectionsService) Resolve(parent string) *ProjectsLocationsAppConnectionsResolveCall

Resolve: Resolves AppConnections details for a given AppConnector. An internal method called by a connector to find AppConnections to connect to.

parent: The resource name of the AppConnection location using the form: `projects/{project_id}/locations/{location_id}`.
func (*ProjectsLocationsAppConnectionsService) SetIamPolicy ¶
func (r *ProjectsLocationsAppConnectionsService) SetIamPolicy(resource string, googleiamv1setiampolicyrequest *GoogleIamV1SetIamPolicyRequest) *ProjectsLocationsAppConnectionsSetIamPolicyCall

SetIamPolicy: Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsAppConnectionsService) TestIamPermissions ¶
func (r *ProjectsLocationsAppConnectionsService) TestIamPermissions(resource string, googleiamv1testiampermissionsrequest *GoogleIamV1TestIamPermissionsRequest) *ProjectsLocationsAppConnectionsTestIamPermissionsCall

TestIamPermissions: Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type ProjectsLocationsAppConnectionsSetIamPolicyCall ¶
type ProjectsLocationsAppConnectionsSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectionsSetIamPolicyCall) Context ¶
func (c *ProjectsLocationsAppConnectionsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsAppConnectionsSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectionsSetIamPolicyCall) Do ¶
func (c *ProjectsLocationsAppConnectionsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)

Do executes the "beyondcorp.projects.locations.appConnections.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *GoogleIamV1Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectionsSetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsAppConnectionsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectionsSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectionsSetIamPolicyCall) Header ¶
func (c *ProjectsLocationsAppConnectionsSetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsAppConnectionsTestIamPermissionsCall ¶
type ProjectsLocationsAppConnectionsTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectionsTestIamPermissionsCall) Context ¶
func (c *ProjectsLocationsAppConnectionsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsAppConnectionsTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectionsTestIamPermissionsCall) Do ¶
func (c *ProjectsLocationsAppConnectionsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1TestIamPermissionsResponse, error)

Do executes the "beyondcorp.projects.locations.appConnections.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *GoogleIamV1TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectionsTestIamPermissionsCall) Fields ¶
func (c *ProjectsLocationsAppConnectionsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectionsTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectionsTestIamPermissionsCall) Header ¶
func (c *ProjectsLocationsAppConnectionsTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsAppConnectorsCreateCall ¶
added in v0.89.0
type ProjectsLocationsAppConnectorsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectorsCreateCall) AppConnectorId ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsCreateCall) AppConnectorId(appConnectorId string) *ProjectsLocationsAppConnectorsCreateCall

AppConnectorId sets the optional parameter "appConnectorId": User-settable AppConnector resource ID. * Must start with a letter. * Must contain between 4-63 characters from `/a-z-/`. * Must end with a number or a letter.

func (*ProjectsLocationsAppConnectorsCreateCall) Context ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsCreateCall) Context(ctx context.Context) *ProjectsLocationsAppConnectorsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectorsCreateCall) Do ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.appConnectors.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectorsCreateCall) Fields ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectorsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectorsCreateCall) Header ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppConnectorsCreateCall) RequestId ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsCreateCall) RequestId(requestId string) *ProjectsLocationsAppConnectorsCreateCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsAppConnectorsCreateCall) ValidateOnly ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsCreateCall) ValidateOnly(validateOnly bool) *ProjectsLocationsAppConnectorsCreateCall

ValidateOnly sets the optional parameter "validateOnly": If set, validates request by executing a dry-run which would not alter the resource in any way.

type ProjectsLocationsAppConnectorsDeleteCall ¶
added in v0.89.0
type ProjectsLocationsAppConnectorsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectorsDeleteCall) Context ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsDeleteCall) Context(ctx context.Context) *ProjectsLocationsAppConnectorsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectorsDeleteCall) Do ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.appConnectors.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectorsDeleteCall) Fields ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectorsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectorsDeleteCall) Header ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppConnectorsDeleteCall) RequestId ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsDeleteCall) RequestId(requestId string) *ProjectsLocationsAppConnectorsDeleteCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsAppConnectorsDeleteCall) ValidateOnly ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsDeleteCall) ValidateOnly(validateOnly bool) *ProjectsLocationsAppConnectorsDeleteCall

ValidateOnly sets the optional parameter "validateOnly": If set, validates request by executing a dry-run which would not alter the resource in any way.

type ProjectsLocationsAppConnectorsGetCall ¶
added in v0.89.0
type ProjectsLocationsAppConnectorsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectorsGetCall) Context ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsGetCall) Context(ctx context.Context) *ProjectsLocationsAppConnectorsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectorsGetCall) Do ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpAppconnectorsV1AppConnector, error)

Do executes the "beyondcorp.projects.locations.appConnectors.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpAppconnectorsV1AppConnector.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectorsGetCall) Fields ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectorsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectorsGetCall) Header ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppConnectorsGetCall) IfNoneMatch ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsAppConnectorsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsAppConnectorsGetIamPolicyCall ¶
type ProjectsLocationsAppConnectorsGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectorsGetIamPolicyCall) Context ¶
func (c *ProjectsLocationsAppConnectorsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsAppConnectorsGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectorsGetIamPolicyCall) Do ¶
func (c *ProjectsLocationsAppConnectorsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)

Do executes the "beyondcorp.projects.locations.appConnectors.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *GoogleIamV1Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectorsGetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsAppConnectorsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectorsGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectorsGetIamPolicyCall) Header ¶
func (c *ProjectsLocationsAppConnectorsGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppConnectorsGetIamPolicyCall) IfNoneMatch ¶
func (c *ProjectsLocationsAppConnectorsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsAppConnectorsGetIamPolicyCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsAppConnectorsGetIamPolicyCall) OptionsRequestedPolicyVersion ¶
func (c *ProjectsLocationsAppConnectorsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsAppConnectorsGetIamPolicyCall

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies).

type ProjectsLocationsAppConnectorsListCall ¶
added in v0.89.0
type ProjectsLocationsAppConnectorsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectorsListCall) Context ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsListCall) Context(ctx context.Context) *ProjectsLocationsAppConnectorsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectorsListCall) Do ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponse, error)

Do executes the "beyondcorp.projects.locations.appConnectors.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponse.ServerResponse .Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectorsListCall) Fields ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectorsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectorsListCall) Filter ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsListCall) Filter(filter string) *ProjectsLocationsAppConnectorsListCall

Filter sets the optional parameter "filter": A filter specifying constraints of a list operation.

func (*ProjectsLocationsAppConnectorsListCall) Header ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppConnectorsListCall) IfNoneMatch ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsAppConnectorsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsAppConnectorsListCall) OrderBy ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsListCall) OrderBy(orderBy string) *ProjectsLocationsAppConnectorsListCall

OrderBy sets the optional parameter "orderBy": Specifies the ordering of results. See Sorting order (https://cloud.google.com/apis/design/design_patterns#sorting_order) for more information.

func (*ProjectsLocationsAppConnectorsListCall) PageSize ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsListCall) PageSize(pageSize int64) *ProjectsLocationsAppConnectorsListCall

PageSize sets the optional parameter "pageSize": The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's next_page_token to determine if there are more instances left to be queried.

func (*ProjectsLocationsAppConnectorsListCall) PageToken ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsListCall) PageToken(pageToken string) *ProjectsLocationsAppConnectorsListCall

PageToken sets the optional parameter "pageToken": The next_page_token value returned from a previous ListAppConnectorsRequest, if any.

func (*ProjectsLocationsAppConnectorsListCall) Pages ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsListCall) Pages(ctx context.Context, f func(*GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsAppConnectorsPatchCall ¶
added in v0.89.0
type ProjectsLocationsAppConnectorsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectorsPatchCall) Context ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsPatchCall) Context(ctx context.Context) *ProjectsLocationsAppConnectorsPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectorsPatchCall) Do ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.appConnectors.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectorsPatchCall) Fields ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectorsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectorsPatchCall) Header ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppConnectorsPatchCall) RequestId ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsPatchCall) RequestId(requestId string) *ProjectsLocationsAppConnectorsPatchCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsAppConnectorsPatchCall) UpdateMask ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsAppConnectorsPatchCall

UpdateMask sets the optional parameter "updateMask": Required. Mask of fields to update. At least one path must be supplied in this field. The elements of the repeated paths field may only include these fields from [BeyondCorp.AppConnector]: * `labels` * `display_name`

func (*ProjectsLocationsAppConnectorsPatchCall) ValidateOnly ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsPatchCall) ValidateOnly(validateOnly bool) *ProjectsLocationsAppConnectorsPatchCall

ValidateOnly sets the optional parameter "validateOnly": If set, validates request by executing a dry-run which would not alter the resource in any way.

type ProjectsLocationsAppConnectorsReportStatusCall ¶
added in v0.89.0
type ProjectsLocationsAppConnectorsReportStatusCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectorsReportStatusCall) Context ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsReportStatusCall) Context(ctx context.Context) *ProjectsLocationsAppConnectorsReportStatusCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectorsReportStatusCall) Do ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsReportStatusCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.appConnectors.reportStatus" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectorsReportStatusCall) Fields ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsReportStatusCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectorsReportStatusCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectorsReportStatusCall) Header ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsReportStatusCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsAppConnectorsResolveInstanceConfigCall ¶
added in v0.89.0
type ProjectsLocationsAppConnectorsResolveInstanceConfigCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectorsResolveInstanceConfigCall) Context ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsResolveInstanceConfigCall) Context(ctx context.Context) *ProjectsLocationsAppConnectorsResolveInstanceConfigCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectorsResolveInstanceConfigCall) Do ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsResolveInstanceConfigCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponse, error)

Do executes the "beyondcorp.projects.locations.appConnectors.resolveInstanceConfig" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponse.ServerResp onse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectorsResolveInstanceConfigCall) Fields ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsResolveInstanceConfigCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectorsResolveInstanceConfigCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectorsResolveInstanceConfigCall) Header ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsResolveInstanceConfigCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppConnectorsResolveInstanceConfigCall) IfNoneMatch ¶
added in v0.89.0
func (c *ProjectsLocationsAppConnectorsResolveInstanceConfigCall) IfNoneMatch(entityTag string) *ProjectsLocationsAppConnectorsResolveInstanceConfigCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsAppConnectorsService ¶
type ProjectsLocationsAppConnectorsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsAppConnectorsService ¶
func NewProjectsLocationsAppConnectorsService(s *Service) *ProjectsLocationsAppConnectorsService
func (*ProjectsLocationsAppConnectorsService) Create ¶
added in v0.89.0
func (r *ProjectsLocationsAppConnectorsService) Create(parent string, googlecloudbeyondcorpappconnectorsv1appconnector *GoogleCloudBeyondcorpAppconnectorsV1AppConnector) *ProjectsLocationsAppConnectorsCreateCall

Create: Creates a new AppConnector in a given project and location.

parent: The resource project name of the AppConnector location using the form: `projects/{project_id}/locations/{location_id}`.
func (*ProjectsLocationsAppConnectorsService) Delete ¶
added in v0.89.0
func (r *ProjectsLocationsAppConnectorsService) Delete(name string) *ProjectsLocationsAppConnectorsDeleteCall

Delete: Deletes a single AppConnector.

name: BeyondCorp AppConnector name using the form: `projects/{project_id}/locations/{location_id}/appConnectors/{app_connector _id}`.
func (*ProjectsLocationsAppConnectorsService) Get ¶
added in v0.89.0
func (r *ProjectsLocationsAppConnectorsService) Get(name string) *ProjectsLocationsAppConnectorsGetCall

Get: Gets details of a single AppConnector.

name: BeyondCorp AppConnector name using the form: `projects/{project_id}/locations/{location_id}/appConnectors/{app_connector _id}`.
func (*ProjectsLocationsAppConnectorsService) GetIamPolicy ¶
func (r *ProjectsLocationsAppConnectorsService) GetIamPolicy(resource string) *ProjectsLocationsAppConnectorsGetIamPolicyCall

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsAppConnectorsService) List ¶
added in v0.89.0
func (r *ProjectsLocationsAppConnectorsService) List(parent string) *ProjectsLocationsAppConnectorsListCall

List: Lists AppConnectors in a given project and location.

parent: The resource name of the AppConnector location using the form: `projects/{project_id}/locations/{location_id}`.
func (*ProjectsLocationsAppConnectorsService) Patch ¶
added in v0.89.0
func (r *ProjectsLocationsAppConnectorsService) Patch(name string, googlecloudbeyondcorpappconnectorsv1appconnector *GoogleCloudBeyondcorpAppconnectorsV1AppConnector) *ProjectsLocationsAppConnectorsPatchCall

Patch: Updates the parameters of a single AppConnector.

name: Unique resource name of the AppConnector. The name is ignored when creating a AppConnector.
func (*ProjectsLocationsAppConnectorsService) ReportStatus ¶
added in v0.89.0
func (r *ProjectsLocationsAppConnectorsService) ReportStatus(appConnector string, googlecloudbeyondcorpappconnectorsv1reportstatusrequest *GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequest) *ProjectsLocationsAppConnectorsReportStatusCall

ReportStatus: Report status for a given connector.

appConnector: BeyondCorp Connector name using the form: `projects/{project_id}/locations/{location_id}/connectors/{connector}`.
func (*ProjectsLocationsAppConnectorsService) ResolveInstanceConfig ¶
added in v0.89.0
func (r *ProjectsLocationsAppConnectorsService) ResolveInstanceConfig(appConnector string) *ProjectsLocationsAppConnectorsResolveInstanceConfigCall

ResolveInstanceConfig: Gets instance configuration for a given AppConnector. An internal method called by a AppConnector to get its container config.

appConnector: BeyondCorp AppConnector name using the form: `projects/{project_id}/locations/{location_id}/appConnectors/{app_connector }`.
func (*ProjectsLocationsAppConnectorsService) SetIamPolicy ¶
func (r *ProjectsLocationsAppConnectorsService) SetIamPolicy(resource string, googleiamv1setiampolicyrequest *GoogleIamV1SetIamPolicyRequest) *ProjectsLocationsAppConnectorsSetIamPolicyCall

SetIamPolicy: Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsAppConnectorsService) TestIamPermissions ¶
func (r *ProjectsLocationsAppConnectorsService) TestIamPermissions(resource string, googleiamv1testiampermissionsrequest *GoogleIamV1TestIamPermissionsRequest) *ProjectsLocationsAppConnectorsTestIamPermissionsCall

TestIamPermissions: Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type ProjectsLocationsAppConnectorsSetIamPolicyCall ¶
type ProjectsLocationsAppConnectorsSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectorsSetIamPolicyCall) Context ¶
func (c *ProjectsLocationsAppConnectorsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsAppConnectorsSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectorsSetIamPolicyCall) Do ¶
func (c *ProjectsLocationsAppConnectorsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)

Do executes the "beyondcorp.projects.locations.appConnectors.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *GoogleIamV1Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectorsSetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsAppConnectorsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectorsSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectorsSetIamPolicyCall) Header ¶
func (c *ProjectsLocationsAppConnectorsSetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsAppConnectorsTestIamPermissionsCall ¶
type ProjectsLocationsAppConnectorsTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppConnectorsTestIamPermissionsCall) Context ¶
func (c *ProjectsLocationsAppConnectorsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsAppConnectorsTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppConnectorsTestIamPermissionsCall) Do ¶
func (c *ProjectsLocationsAppConnectorsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1TestIamPermissionsResponse, error)

Do executes the "beyondcorp.projects.locations.appConnectors.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *GoogleIamV1TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppConnectorsTestIamPermissionsCall) Fields ¶
func (c *ProjectsLocationsAppConnectorsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppConnectorsTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppConnectorsTestIamPermissionsCall) Header ¶
func (c *ProjectsLocationsAppConnectorsTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsAppGatewaysCreateCall ¶
added in v0.89.0
type ProjectsLocationsAppGatewaysCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppGatewaysCreateCall) AppGatewayId ¶
added in v0.89.0
func (c *ProjectsLocationsAppGatewaysCreateCall) AppGatewayId(appGatewayId string) *ProjectsLocationsAppGatewaysCreateCall

AppGatewayId sets the optional parameter "appGatewayId": User-settable AppGateway resource ID. * Must start with a letter. * Must contain between 4-63 characters from `/a-z-/`. * Must end with a number or a letter.

func (*ProjectsLocationsAppGatewaysCreateCall) Context ¶
added in v0.89.0
func (c *ProjectsLocationsAppGatewaysCreateCall) Context(ctx context.Context) *ProjectsLocationsAppGatewaysCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppGatewaysCreateCall) Do ¶
added in v0.89.0
func (c *ProjectsLocationsAppGatewaysCreateCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.appGateways.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppGatewaysCreateCall) Fields ¶
added in v0.89.0
func (c *ProjectsLocationsAppGatewaysCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppGatewaysCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppGatewaysCreateCall) Header ¶
added in v0.89.0
func (c *ProjectsLocationsAppGatewaysCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppGatewaysCreateCall) RequestId ¶
added in v0.89.0
func (c *ProjectsLocationsAppGatewaysCreateCall) RequestId(requestId string) *ProjectsLocationsAppGatewaysCreateCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsAppGatewaysCreateCall) ValidateOnly ¶
added in v0.89.0
func (c *ProjectsLocationsAppGatewaysCreateCall) ValidateOnly(validateOnly bool) *ProjectsLocationsAppGatewaysCreateCall

ValidateOnly sets the optional parameter "validateOnly": If set, validates request by executing a dry-run which would not alter the resource in any way.

type ProjectsLocationsAppGatewaysDeleteCall ¶
added in v0.89.0
type ProjectsLocationsAppGatewaysDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppGatewaysDeleteCall) Context ¶
added in v0.89.0
func (c *ProjectsLocationsAppGatewaysDeleteCall) Context(ctx context.Context) *ProjectsLocationsAppGatewaysDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppGatewaysDeleteCall) Do ¶
added in v0.89.0
func (c *ProjectsLocationsAppGatewaysDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.appGateways.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppGatewaysDeleteCall) Fields ¶
added in v0.89.0
func (c *ProjectsLocationsAppGatewaysDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppGatewaysDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppGatewaysDeleteCall) Header ¶
added in v0.89.0
func (c *ProjectsLocationsAppGatewaysDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppGatewaysDeleteCall) RequestId ¶
added in v0.89.0
func (c *ProjectsLocationsAppGatewaysDeleteCall) RequestId(requestId string) *ProjectsLocationsAppGatewaysDeleteCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsAppGatewaysDeleteCall) ValidateOnly ¶
added in v0.89.0
func (c *ProjectsLocationsAppGatewaysDeleteCall) ValidateOnly(validateOnly bool) *ProjectsLocationsAppGatewaysDeleteCall

ValidateOnly sets the optional parameter "validateOnly": If set, validates request by executing a dry-run which would not alter the resource in any way.

type ProjectsLocationsAppGatewaysGetCall ¶
added in v0.89.0
type ProjectsLocationsAppGatewaysGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppGatewaysGetCall) Context ¶
added in v0.89.0
func (c *ProjectsLocationsAppGatewaysGetCall) Context(ctx context.Context) *ProjectsLocationsAppGatewaysGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppGatewaysGetCall) Do ¶
added in v0.89.0
func (c *ProjectsLocationsAppGatewaysGetCall) Do(opts ...googleapi.CallOption) (*AppGateway, error)

Do executes the "beyondcorp.projects.locations.appGateways.get" call. Any non-2xx status code is an error. Response headers are in either *AppGateway.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppGatewaysGetCall) Fields ¶
added in v0.89.0
func (c *ProjectsLocationsAppGatewaysGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppGatewaysGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppGatewaysGetCall) Header ¶
added in v0.89.0
func (c *ProjectsLocationsAppGatewaysGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppGatewaysGetCall) IfNoneMatch ¶
added in v0.89.0
func (c *ProjectsLocationsAppGatewaysGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsAppGatewaysGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsAppGatewaysGetIamPolicyCall ¶
type ProjectsLocationsAppGatewaysGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppGatewaysGetIamPolicyCall) Context ¶
func (c *ProjectsLocationsAppGatewaysGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsAppGatewaysGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppGatewaysGetIamPolicyCall) Do ¶
func (c *ProjectsLocationsAppGatewaysGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)

Do executes the "beyondcorp.projects.locations.appGateways.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *GoogleIamV1Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppGatewaysGetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsAppGatewaysGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppGatewaysGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppGatewaysGetIamPolicyCall) Header ¶
func (c *ProjectsLocationsAppGatewaysGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppGatewaysGetIamPolicyCall) IfNoneMatch ¶
func (c *ProjectsLocationsAppGatewaysGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsAppGatewaysGetIamPolicyCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsAppGatewaysGetIamPolicyCall) OptionsRequestedPolicyVersion ¶
func (c *ProjectsLocationsAppGatewaysGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsAppGatewaysGetIamPolicyCall

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies).

type ProjectsLocationsAppGatewaysListCall ¶
added in v0.89.0
type ProjectsLocationsAppGatewaysListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppGatewaysListCall) Context ¶
added in v0.89.0
func (c *ProjectsLocationsAppGatewaysListCall) Context(ctx context.Context) *ProjectsLocationsAppGatewaysListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppGatewaysListCall) Do ¶
added in v0.89.0
func (c *ProjectsLocationsAppGatewaysListCall) Do(opts ...googleapi.CallOption) (*ListAppGatewaysResponse, error)

Do executes the "beyondcorp.projects.locations.appGateways.list" call. Any non-2xx status code is an error. Response headers are in either *ListAppGatewaysResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppGatewaysListCall) Fields ¶
added in v0.89.0
func (c *ProjectsLocationsAppGatewaysListCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppGatewaysListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppGatewaysListCall) Filter ¶
added in v0.89.0
func (c *ProjectsLocationsAppGatewaysListCall) Filter(filter string) *ProjectsLocationsAppGatewaysListCall

Filter sets the optional parameter "filter": A filter specifying constraints of a list operation.

func (*ProjectsLocationsAppGatewaysListCall) Header ¶
added in v0.89.0
func (c *ProjectsLocationsAppGatewaysListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsAppGatewaysListCall) IfNoneMatch ¶
added in v0.89.0
func (c *ProjectsLocationsAppGatewaysListCall) IfNoneMatch(entityTag string) *ProjectsLocationsAppGatewaysListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsAppGatewaysListCall) OrderBy ¶
added in v0.89.0
func (c *ProjectsLocationsAppGatewaysListCall) OrderBy(orderBy string) *ProjectsLocationsAppGatewaysListCall

OrderBy sets the optional parameter "orderBy": Specifies the ordering of results. See Sorting order (https://cloud.google.com/apis/design/design_patterns#sorting_order) for more information.

func (*ProjectsLocationsAppGatewaysListCall) PageSize ¶
added in v0.89.0
func (c *ProjectsLocationsAppGatewaysListCall) PageSize(pageSize int64) *ProjectsLocationsAppGatewaysListCall

PageSize sets the optional parameter "pageSize": The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's next_page_token to determine if there are more instances left to be queried.

func (*ProjectsLocationsAppGatewaysListCall) PageToken ¶
added in v0.89.0
func (c *ProjectsLocationsAppGatewaysListCall) PageToken(pageToken string) *ProjectsLocationsAppGatewaysListCall

PageToken sets the optional parameter "pageToken": The next_page_token value returned from a previous ListAppGatewaysRequest, if any.

func (*ProjectsLocationsAppGatewaysListCall) Pages ¶
added in v0.89.0
func (c *ProjectsLocationsAppGatewaysListCall) Pages(ctx context.Context, f func(*ListAppGatewaysResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsAppGatewaysService ¶
type ProjectsLocationsAppGatewaysService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsAppGatewaysService ¶
func NewProjectsLocationsAppGatewaysService(s *Service) *ProjectsLocationsAppGatewaysService
func (*ProjectsLocationsAppGatewaysService) Create ¶
added in v0.89.0
func (r *ProjectsLocationsAppGatewaysService) Create(parent string, appgateway *AppGateway) *ProjectsLocationsAppGatewaysCreateCall

Create: Creates a new AppGateway in a given project and location.

parent: The resource project name of the AppGateway location using the form: `projects/{project_id}/locations/{location_id}`.
func (*ProjectsLocationsAppGatewaysService) Delete ¶
added in v0.89.0
func (r *ProjectsLocationsAppGatewaysService) Delete(name string) *ProjectsLocationsAppGatewaysDeleteCall

Delete: Deletes a single AppGateway.

name: BeyondCorp AppGateway name using the form: `projects/{project_id}/locations/{location_id}/appGateways/{app_gateway_id} `.
func (*ProjectsLocationsAppGatewaysService) Get ¶
added in v0.89.0
func (r *ProjectsLocationsAppGatewaysService) Get(name string) *ProjectsLocationsAppGatewaysGetCall

Get: Gets details of a single AppGateway.

name: BeyondCorp AppGateway name using the form: `projects/{project_id}/locations/{location_id}/appGateways/{app_gateway_id} `.
func (*ProjectsLocationsAppGatewaysService) GetIamPolicy ¶
func (r *ProjectsLocationsAppGatewaysService) GetIamPolicy(resource string) *ProjectsLocationsAppGatewaysGetIamPolicyCall

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsAppGatewaysService) List ¶
added in v0.89.0
func (r *ProjectsLocationsAppGatewaysService) List(parent string) *ProjectsLocationsAppGatewaysListCall

List: Lists AppGateways in a given project and location.

parent: The resource name of the AppGateway location using the form: `projects/{project_id}/locations/{location_id}`.
func (*ProjectsLocationsAppGatewaysService) SetIamPolicy ¶
func (r *ProjectsLocationsAppGatewaysService) SetIamPolicy(resource string, googleiamv1setiampolicyrequest *GoogleIamV1SetIamPolicyRequest) *ProjectsLocationsAppGatewaysSetIamPolicyCall

SetIamPolicy: Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsAppGatewaysService) TestIamPermissions ¶
func (r *ProjectsLocationsAppGatewaysService) TestIamPermissions(resource string, googleiamv1testiampermissionsrequest *GoogleIamV1TestIamPermissionsRequest) *ProjectsLocationsAppGatewaysTestIamPermissionsCall

TestIamPermissions: Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type ProjectsLocationsAppGatewaysSetIamPolicyCall ¶
type ProjectsLocationsAppGatewaysSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppGatewaysSetIamPolicyCall) Context ¶
func (c *ProjectsLocationsAppGatewaysSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsAppGatewaysSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppGatewaysSetIamPolicyCall) Do ¶
func (c *ProjectsLocationsAppGatewaysSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)

Do executes the "beyondcorp.projects.locations.appGateways.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *GoogleIamV1Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppGatewaysSetIamPolicyCall) Fields ¶
func (c *ProjectsLocationsAppGatewaysSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppGatewaysSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppGatewaysSetIamPolicyCall) Header ¶
func (c *ProjectsLocationsAppGatewaysSetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsAppGatewaysTestIamPermissionsCall ¶
type ProjectsLocationsAppGatewaysTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsAppGatewaysTestIamPermissionsCall) Context ¶
func (c *ProjectsLocationsAppGatewaysTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsAppGatewaysTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsAppGatewaysTestIamPermissionsCall) Do ¶
func (c *ProjectsLocationsAppGatewaysTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1TestIamPermissionsResponse, error)

Do executes the "beyondcorp.projects.locations.appGateways.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *GoogleIamV1TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsAppGatewaysTestIamPermissionsCall) Fields ¶
func (c *ProjectsLocationsAppGatewaysTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsAppGatewaysTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsAppGatewaysTestIamPermissionsCall) Header ¶
func (c *ProjectsLocationsAppGatewaysTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsGetCall ¶
type ProjectsLocationsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsGetCall) Context ¶
func (c *ProjectsLocationsGetCall) Context(ctx context.Context) *ProjectsLocationsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsGetCall) Do ¶
func (c *ProjectsLocationsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudLocationLocation, error)

Do executes the "beyondcorp.projects.locations.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudLocationLocation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsGetCall) Fields ¶
func (c *ProjectsLocationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsGetCall) Header ¶
func (c *ProjectsLocationsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsListCall ¶
type ProjectsLocationsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsListCall) Context ¶
func (c *ProjectsLocationsListCall) Context(ctx context.Context) *ProjectsLocationsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsListCall) Do ¶
func (c *ProjectsLocationsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudLocationListLocationsResponse, error)

Do executes the "beyondcorp.projects.locations.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudLocationListLocationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsListCall) ExtraLocationTypes ¶
added in v0.230.0
func (c *ProjectsLocationsListCall) ExtraLocationTypes(extraLocationTypes ...string) *ProjectsLocationsListCall

ExtraLocationTypes sets the optional parameter "extraLocationTypes": Do not use this field. It is unsupported and is ignored unless explicitly documented otherwise. This is primarily for internal usage.

func (*ProjectsLocationsListCall) Fields ¶
func (c *ProjectsLocationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsListCall) Filter ¶
func (c *ProjectsLocationsListCall) Filter(filter string) *ProjectsLocationsListCall

Filter sets the optional parameter "filter": A filter to narrow down results to a preferred subset. The filtering language accepts strings like "displayName=tokyo", and is documented in more detail in AIP-160 (https://google.aip.dev/160).

func (*ProjectsLocationsListCall) Header ¶
func (c *ProjectsLocationsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsListCall) IfNoneMatch ¶
func (c *ProjectsLocationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsListCall) PageSize ¶
func (c *ProjectsLocationsListCall) PageSize(pageSize int64) *ProjectsLocationsListCall

PageSize sets the optional parameter "pageSize": The maximum number of results to return. If not set, the service selects a default.

func (*ProjectsLocationsListCall) PageToken ¶
func (c *ProjectsLocationsListCall) PageToken(pageToken string) *ProjectsLocationsListCall

PageToken sets the optional parameter "pageToken": A page token received from the `next_page_token` field in the response. Send that page token to receive the subsequent page.

func (*ProjectsLocationsListCall) Pages ¶
func (c *ProjectsLocationsListCall) Pages(ctx context.Context, f func(*GoogleCloudLocationListLocationsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsOperationsCancelCall ¶
type ProjectsLocationsOperationsCancelCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsOperationsCancelCall) Context ¶
func (c *ProjectsLocationsOperationsCancelCall) Context(ctx context.Context) *ProjectsLocationsOperationsCancelCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsOperationsCancelCall) Do ¶
func (c *ProjectsLocationsOperationsCancelCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "beyondcorp.projects.locations.operations.cancel" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsOperationsCancelCall) Fields ¶
func (c *ProjectsLocationsOperationsCancelCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsCancelCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsOperationsCancelCall) Header ¶
func (c *ProjectsLocationsOperationsCancelCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsOperationsDeleteCall ¶
type ProjectsLocationsOperationsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsOperationsDeleteCall) Context ¶
func (c *ProjectsLocationsOperationsDeleteCall) Context(ctx context.Context) *ProjectsLocationsOperationsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsOperationsDeleteCall) Do ¶
func (c *ProjectsLocationsOperationsDeleteCall) Do(opts ...googleapi.CallOption) (*Empty, error)

Do executes the "beyondcorp.projects.locations.operations.delete" call. Any non-2xx status code is an error. Response headers are in either *Empty.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsOperationsDeleteCall) Fields ¶
func (c *ProjectsLocationsOperationsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsOperationsDeleteCall) Header ¶
func (c *ProjectsLocationsOperationsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsOperationsGetCall ¶
type ProjectsLocationsOperationsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsOperationsGetCall) Context ¶
func (c *ProjectsLocationsOperationsGetCall) Context(ctx context.Context) *ProjectsLocationsOperationsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsOperationsGetCall) Do ¶
func (c *ProjectsLocationsOperationsGetCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.operations.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsOperationsGetCall) Fields ¶
func (c *ProjectsLocationsOperationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsOperationsGetCall) Header ¶
func (c *ProjectsLocationsOperationsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsOperationsGetCall) IfNoneMatch ¶
func (c *ProjectsLocationsOperationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsOperationsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsOperationsListCall ¶
type ProjectsLocationsOperationsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsOperationsListCall) Context ¶
func (c *ProjectsLocationsOperationsListCall) Context(ctx context.Context) *ProjectsLocationsOperationsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsOperationsListCall) Do ¶
func (c *ProjectsLocationsOperationsListCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningListOperationsResponse, error)

Do executes the "beyondcorp.projects.locations.operations.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningListOperationsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsOperationsListCall) Fields ¶
func (c *ProjectsLocationsOperationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsOperationsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsOperationsListCall) Filter ¶
func (c *ProjectsLocationsOperationsListCall) Filter(filter string) *ProjectsLocationsOperationsListCall

Filter sets the optional parameter "filter": The standard list filter.

func (*ProjectsLocationsOperationsListCall) Header ¶
func (c *ProjectsLocationsOperationsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsOperationsListCall) IfNoneMatch ¶
func (c *ProjectsLocationsOperationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsOperationsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsOperationsListCall) PageSize ¶
func (c *ProjectsLocationsOperationsListCall) PageSize(pageSize int64) *ProjectsLocationsOperationsListCall

PageSize sets the optional parameter "pageSize": The standard list page size.

func (*ProjectsLocationsOperationsListCall) PageToken ¶
func (c *ProjectsLocationsOperationsListCall) PageToken(pageToken string) *ProjectsLocationsOperationsListCall

PageToken sets the optional parameter "pageToken": The standard list page token.

func (*ProjectsLocationsOperationsListCall) Pages ¶
func (c *ProjectsLocationsOperationsListCall) Pages(ctx context.Context, f func(*GoogleLongrunningListOperationsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

func (*ProjectsLocationsOperationsListCall) ReturnPartialSuccess ¶
added in v0.253.0
func (c *ProjectsLocationsOperationsListCall) ReturnPartialSuccess(returnPartialSuccess bool) *ProjectsLocationsOperationsListCall

ReturnPartialSuccess sets the optional parameter "returnPartialSuccess": When set to `true`, operations that are reachable are returned as normal, and those that are unreachable are returned in the ListOperationsResponse.unreachable field. This can only be `true` when reading across collections. For example, when `parent` is set to "projects/example/locations/-". This field is not supported by default and will result in an `UNIMPLEMENTED` error if set unless explicitly documented otherwise in service or product specific documentation.

type ProjectsLocationsOperationsService ¶
type ProjectsLocationsOperationsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsOperationsService ¶
func NewProjectsLocationsOperationsService(s *Service) *ProjectsLocationsOperationsService
func (*ProjectsLocationsOperationsService) Cancel ¶
func (r *ProjectsLocationsOperationsService) Cancel(name string, googlelongrunningcanceloperationrequest *GoogleLongrunningCancelOperationRequest) *ProjectsLocationsOperationsCancelCall

Cancel: Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of `1`, corresponding to `Code.CANCELLED`.

- name: The name of the operation resource to be cancelled.

func (*ProjectsLocationsOperationsService) Delete ¶
func (r *ProjectsLocationsOperationsService) Delete(name string) *ProjectsLocationsOperationsDeleteCall

Delete: Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

- name: The name of the operation resource to be deleted.

func (*ProjectsLocationsOperationsService) Get ¶
func (r *ProjectsLocationsOperationsService) Get(name string) *ProjectsLocationsOperationsGetCall

Get: Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

- name: The name of the operation resource.

func (*ProjectsLocationsOperationsService) List ¶
func (r *ProjectsLocationsOperationsService) List(name string) *ProjectsLocationsOperationsListCall

List: Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.

- name: The name of the operation's parent resource.

type ProjectsLocationsSecurityGatewaysApplicationsCreateCall ¶
added in v0.240.0
type ProjectsLocationsSecurityGatewaysApplicationsCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSecurityGatewaysApplicationsCreateCall) ApplicationId ¶
added in v0.240.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsCreateCall) ApplicationId(applicationId string) *ProjectsLocationsSecurityGatewaysApplicationsCreateCall

ApplicationId sets the optional parameter "applicationId": User-settable Application resource ID. * Must start with a letter. * Must contain between 4-63 characters from `/a-z-/`. * Must end with a number or letter.

func (*ProjectsLocationsSecurityGatewaysApplicationsCreateCall) Context ¶
added in v0.240.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsCreateCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysApplicationsCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSecurityGatewaysApplicationsCreateCall) Do ¶
added in v0.240.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsCreateCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.securityGateways.applications.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSecurityGatewaysApplicationsCreateCall) Fields ¶
added in v0.240.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysApplicationsCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSecurityGatewaysApplicationsCreateCall) Header ¶
added in v0.240.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsSecurityGatewaysApplicationsCreateCall) RequestId ¶
added in v0.240.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsCreateCall) RequestId(requestId string) *ProjectsLocationsSecurityGatewaysApplicationsCreateCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

type ProjectsLocationsSecurityGatewaysApplicationsDeleteCall ¶
added in v0.200.0
type ProjectsLocationsSecurityGatewaysApplicationsDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSecurityGatewaysApplicationsDeleteCall) Context ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSecurityGatewaysApplicationsDeleteCall) Do ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.securityGateways.applications.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSecurityGatewaysApplicationsDeleteCall) Fields ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSecurityGatewaysApplicationsDeleteCall) Header ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsSecurityGatewaysApplicationsDeleteCall) RequestId ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall) RequestId(requestId string) *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsSecurityGatewaysApplicationsDeleteCall) ValidateOnly ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall) ValidateOnly(validateOnly bool) *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall

ValidateOnly sets the optional parameter "validateOnly": If set, validates request by executing a dry-run which would not alter the resource in any way.

type ProjectsLocationsSecurityGatewaysApplicationsGetCall ¶
added in v0.200.0
type ProjectsLocationsSecurityGatewaysApplicationsGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSecurityGatewaysApplicationsGetCall) Context ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysApplicationsGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSecurityGatewaysApplicationsGetCall) Do ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSecuritygatewaysV1Application, error)

Do executes the "beyondcorp.projects.locations.securityGateways.applications.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpSecuritygatewaysV1Application.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSecurityGatewaysApplicationsGetCall) Fields ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysApplicationsGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSecurityGatewaysApplicationsGetCall) Header ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsSecurityGatewaysApplicationsGetCall) IfNoneMatch ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsSecurityGatewaysApplicationsGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall ¶
added in v0.202.0
type ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall) Context ¶
added in v0.202.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall) Do ¶
added in v0.202.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)

Do executes the "beyondcorp.projects.locations.securityGateways.applications.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *GoogleIamV1Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall) Fields ¶
added in v0.202.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall) Header ¶
added in v0.202.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall) IfNoneMatch ¶
added in v0.202.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall) OptionsRequestedPolicyVersion ¶
added in v0.202.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies).

type ProjectsLocationsSecurityGatewaysApplicationsListCall ¶
added in v0.200.0
type ProjectsLocationsSecurityGatewaysApplicationsListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSecurityGatewaysApplicationsListCall) Context ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsListCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysApplicationsListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSecurityGatewaysApplicationsListCall) Do ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSecuritygatewaysV1ListApplicationsResponse, error)

Do executes the "beyondcorp.projects.locations.securityGateways.applications.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpSecuritygatewaysV1ListApplicationsResponse.ServerRespon se.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSecurityGatewaysApplicationsListCall) Fields ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsListCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysApplicationsListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSecurityGatewaysApplicationsListCall) Filter ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsListCall) Filter(filter string) *ProjectsLocationsSecurityGatewaysApplicationsListCall

Filter sets the optional parameter "filter": A filter specifying constraints of a list operation. All fields in the Application message are supported. For example, the following query will return the Application with displayName "test-application" For more information, please refer to https://google.aip.dev/160.

func (*ProjectsLocationsSecurityGatewaysApplicationsListCall) Header ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsSecurityGatewaysApplicationsListCall) IfNoneMatch ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsListCall) IfNoneMatch(entityTag string) *ProjectsLocationsSecurityGatewaysApplicationsListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsSecurityGatewaysApplicationsListCall) OrderBy ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsListCall) OrderBy(orderBy string) *ProjectsLocationsSecurityGatewaysApplicationsListCall

OrderBy sets the optional parameter "orderBy": Specifies the ordering of results. See Sorting order (https://cloud.google.com/apis/design/design_patterns#sorting_order) for more information.

func (*ProjectsLocationsSecurityGatewaysApplicationsListCall) PageSize ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsListCall) PageSize(pageSize int64) *ProjectsLocationsSecurityGatewaysApplicationsListCall

PageSize sets the optional parameter "pageSize": The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's next_page_token to determine if there are more instances left to be queried.

func (*ProjectsLocationsSecurityGatewaysApplicationsListCall) PageToken ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsListCall) PageToken(pageToken string) *ProjectsLocationsSecurityGatewaysApplicationsListCall

PageToken sets the optional parameter "pageToken": The next_page_token value returned from a previous ListApplicationsRequest, if any.

func (*ProjectsLocationsSecurityGatewaysApplicationsListCall) Pages ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsListCall) Pages(ctx context.Context, f func(*GoogleCloudBeyondcorpSecuritygatewaysV1ListApplicationsResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsSecurityGatewaysApplicationsPatchCall ¶
added in v0.240.0
type ProjectsLocationsSecurityGatewaysApplicationsPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSecurityGatewaysApplicationsPatchCall) Context ¶
added in v0.240.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsPatchCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysApplicationsPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSecurityGatewaysApplicationsPatchCall) Do ¶
added in v0.240.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsPatchCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.securityGateways.applications.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSecurityGatewaysApplicationsPatchCall) Fields ¶
added in v0.240.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysApplicationsPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSecurityGatewaysApplicationsPatchCall) Header ¶
added in v0.240.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsSecurityGatewaysApplicationsPatchCall) RequestId ¶
added in v0.240.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsPatchCall) RequestId(requestId string) *ProjectsLocationsSecurityGatewaysApplicationsPatchCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request timed out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsSecurityGatewaysApplicationsPatchCall) UpdateMask ¶
added in v0.240.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsPatchCall) UpdateMask(updateMask string) *ProjectsLocationsSecurityGatewaysApplicationsPatchCall

UpdateMask sets the optional parameter "updateMask": Mutable fields include: display_name.

type ProjectsLocationsSecurityGatewaysApplicationsService ¶
added in v0.200.0
type ProjectsLocationsSecurityGatewaysApplicationsService struct {
	// contains filtered or unexported fields
}
func NewProjectsLocationsSecurityGatewaysApplicationsService ¶
added in v0.200.0
func NewProjectsLocationsSecurityGatewaysApplicationsService(s *Service) *ProjectsLocationsSecurityGatewaysApplicationsService
func (*ProjectsLocationsSecurityGatewaysApplicationsService) Create ¶
added in v0.240.0
func (r *ProjectsLocationsSecurityGatewaysApplicationsService) Create(parent string, googlecloudbeyondcorpsecuritygatewaysv1application *GoogleCloudBeyondcorpSecuritygatewaysV1Application) *ProjectsLocationsSecurityGatewaysApplicationsCreateCall

Create: Creates a new Application in a given project and location.

parent: The resource name of the parent SecurityGateway using the form: `projects/{project_id}/locations/global/securityGateways/{security_gateway_ id}`.
func (*ProjectsLocationsSecurityGatewaysApplicationsService) Delete ¶
added in v0.200.0
func (r *ProjectsLocationsSecurityGatewaysApplicationsService) Delete(name string) *ProjectsLocationsSecurityGatewaysApplicationsDeleteCall

Delete: Deletes a single application.

- name: Name of the resource.

func (*ProjectsLocationsSecurityGatewaysApplicationsService) Get ¶
added in v0.200.0
func (r *ProjectsLocationsSecurityGatewaysApplicationsService) Get(name string) *ProjectsLocationsSecurityGatewaysApplicationsGetCall

Get: Gets details of a single Application.

name: The resource name of the Application using the form: `projects/{project_id}/locations/global/securityGateway/{security_gateway_i d}/applications/{application_id}`.
func (*ProjectsLocationsSecurityGatewaysApplicationsService) GetIamPolicy ¶
added in v0.202.0
func (r *ProjectsLocationsSecurityGatewaysApplicationsService) GetIamPolicy(resource string) *ProjectsLocationsSecurityGatewaysApplicationsGetIamPolicyCall

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsSecurityGatewaysApplicationsService) List ¶
added in v0.200.0
func (r *ProjectsLocationsSecurityGatewaysApplicationsService) List(parent string) *ProjectsLocationsSecurityGatewaysApplicationsListCall

List: Lists Applications in a given project and location.

parent: The parent location to which the resources belong. `projects/{project_id}/locations/global/securityGateways/{security_gateway_ id}`.
func (*ProjectsLocationsSecurityGatewaysApplicationsService) Patch ¶
added in v0.240.0
func (r *ProjectsLocationsSecurityGatewaysApplicationsService) Patch(name string, googlecloudbeyondcorpsecuritygatewaysv1application *GoogleCloudBeyondcorpSecuritygatewaysV1Application) *ProjectsLocationsSecurityGatewaysApplicationsPatchCall

Patch: Updates the parameters of a single Application.

- name: Identifier. Name of the resource.

func (*ProjectsLocationsSecurityGatewaysApplicationsService) SetIamPolicy ¶
added in v0.202.0
func (r *ProjectsLocationsSecurityGatewaysApplicationsService) SetIamPolicy(resource string, googleiamv1setiampolicyrequest *GoogleIamV1SetIamPolicyRequest) *ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall

SetIamPolicy: Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsSecurityGatewaysApplicationsService) TestIamPermissions ¶
added in v0.240.0
func (r *ProjectsLocationsSecurityGatewaysApplicationsService) TestIamPermissions(resource string, googleiamv1testiampermissionsrequest *GoogleIamV1TestIamPermissionsRequest) *ProjectsLocationsSecurityGatewaysApplicationsTestIamPermissionsCall

TestIamPermissions: Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall ¶
added in v0.202.0
type ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall) Context ¶
added in v0.202.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall) Do ¶
added in v0.202.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)

Do executes the "beyondcorp.projects.locations.securityGateways.applications.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *GoogleIamV1Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall) Fields ¶
added in v0.202.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall) Header ¶
added in v0.202.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsSetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsSecurityGatewaysApplicationsTestIamPermissionsCall ¶
added in v0.240.0
type ProjectsLocationsSecurityGatewaysApplicationsTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSecurityGatewaysApplicationsTestIamPermissionsCall) Context ¶
added in v0.240.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysApplicationsTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSecurityGatewaysApplicationsTestIamPermissionsCall) Do ¶
added in v0.240.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1TestIamPermissionsResponse, error)

Do executes the "beyondcorp.projects.locations.securityGateways.applications.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *GoogleIamV1TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSecurityGatewaysApplicationsTestIamPermissionsCall) Fields ¶
added in v0.240.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysApplicationsTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSecurityGatewaysApplicationsTestIamPermissionsCall) Header ¶
added in v0.240.0
func (c *ProjectsLocationsSecurityGatewaysApplicationsTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsSecurityGatewaysCreateCall ¶
added in v0.200.0
type ProjectsLocationsSecurityGatewaysCreateCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSecurityGatewaysCreateCall) Context ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysCreateCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysCreateCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSecurityGatewaysCreateCall) Do ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysCreateCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.securityGateways.create" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSecurityGatewaysCreateCall) Fields ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysCreateCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysCreateCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSecurityGatewaysCreateCall) Header ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysCreateCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsSecurityGatewaysCreateCall) RequestId ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysCreateCall) RequestId(requestId string) *ProjectsLocationsSecurityGatewaysCreateCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

func (*ProjectsLocationsSecurityGatewaysCreateCall) SecurityGatewayId ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysCreateCall) SecurityGatewayId(securityGatewayId string) *ProjectsLocationsSecurityGatewaysCreateCall

SecurityGatewayId sets the optional parameter "securityGatewayId": User-settable SecurityGateway resource ID. * Must start with a letter. * Must contain between 4-63 characters from `/a-z-/`. * Must end with a number or letter.

type ProjectsLocationsSecurityGatewaysDeleteCall ¶
added in v0.200.0
type ProjectsLocationsSecurityGatewaysDeleteCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSecurityGatewaysDeleteCall) Context ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysDeleteCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysDeleteCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSecurityGatewaysDeleteCall) Do ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysDeleteCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.securityGateways.delete" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSecurityGatewaysDeleteCall) Fields ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysDeleteCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysDeleteCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSecurityGatewaysDeleteCall) Header ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysDeleteCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsSecurityGatewaysDeleteCall) RequestId ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysDeleteCall) RequestId(requestId string) *ProjectsLocationsSecurityGatewaysDeleteCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsSecurityGatewaysDeleteCall) ValidateOnly ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysDeleteCall) ValidateOnly(validateOnly bool) *ProjectsLocationsSecurityGatewaysDeleteCall

ValidateOnly sets the optional parameter "validateOnly": If set, validates request by executing a dry-run which would not alter the resource in any way.

type ProjectsLocationsSecurityGatewaysGetCall ¶
added in v0.200.0
type ProjectsLocationsSecurityGatewaysGetCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSecurityGatewaysGetCall) Context ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysGetCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysGetCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSecurityGatewaysGetCall) Do ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysGetCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSecuritygatewaysV1SecurityGateway, error)

Do executes the "beyondcorp.projects.locations.securityGateways.get" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpSecuritygatewaysV1SecurityGateway.ServerResponse.Header

or (if a response was returned at all) in error.(*googleapi.Error).Header.


Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSecurityGatewaysGetCall) Fields ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysGetCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysGetCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSecurityGatewaysGetCall) Header ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysGetCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsSecurityGatewaysGetCall) IfNoneMatch ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysGetCall) IfNoneMatch(entityTag string) *ProjectsLocationsSecurityGatewaysGetCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

type ProjectsLocationsSecurityGatewaysGetIamPolicyCall ¶
added in v0.202.0
type ProjectsLocationsSecurityGatewaysGetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSecurityGatewaysGetIamPolicyCall) Context ¶
added in v0.202.0
func (c *ProjectsLocationsSecurityGatewaysGetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysGetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSecurityGatewaysGetIamPolicyCall) Do ¶
added in v0.202.0
func (c *ProjectsLocationsSecurityGatewaysGetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)

Do executes the "beyondcorp.projects.locations.securityGateways.getIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *GoogleIamV1Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSecurityGatewaysGetIamPolicyCall) Fields ¶
added in v0.202.0
func (c *ProjectsLocationsSecurityGatewaysGetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysGetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSecurityGatewaysGetIamPolicyCall) Header ¶
added in v0.202.0
func (c *ProjectsLocationsSecurityGatewaysGetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsSecurityGatewaysGetIamPolicyCall) IfNoneMatch ¶
added in v0.202.0
func (c *ProjectsLocationsSecurityGatewaysGetIamPolicyCall) IfNoneMatch(entityTag string) *ProjectsLocationsSecurityGatewaysGetIamPolicyCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsSecurityGatewaysGetIamPolicyCall) OptionsRequestedPolicyVersion ¶
added in v0.202.0
func (c *ProjectsLocationsSecurityGatewaysGetIamPolicyCall) OptionsRequestedPolicyVersion(optionsRequestedPolicyVersion int64) *ProjectsLocationsSecurityGatewaysGetIamPolicyCall

OptionsRequestedPolicyVersion sets the optional parameter "options.requestedPolicyVersion": The maximum policy version that will be used to format the policy. Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected. Requests for policies with any conditional role bindings must specify version 3. Policies with no conditional role bindings may specify any valid value or leave the field unset. The policy in the response might use the policy version that you specified, or it might use a lower policy version. For example, if you specify version 3, but the policy has no conditional role bindings, the response uses version 1. To learn which resources support conditions in their IAM policies, see the IAM documentation (https://cloud.google.com/iam/help/conditions/resource-policies).

type ProjectsLocationsSecurityGatewaysListCall ¶
added in v0.200.0
type ProjectsLocationsSecurityGatewaysListCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSecurityGatewaysListCall) Context ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysListCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysListCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSecurityGatewaysListCall) Do ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysListCall) Do(opts ...googleapi.CallOption) (*GoogleCloudBeyondcorpSecuritygatewaysV1ListSecurityGatewaysResponse, error)

Do executes the "beyondcorp.projects.locations.securityGateways.list" call. Any non-2xx status code is an error. Response headers are in either *GoogleCloudBeyondcorpSecuritygatewaysV1ListSecurityGatewaysResponse.ServerRe sponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSecurityGatewaysListCall) Fields ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysListCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysListCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSecurityGatewaysListCall) Filter ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysListCall) Filter(filter string) *ProjectsLocationsSecurityGatewaysListCall

Filter sets the optional parameter "filter": A filter specifying constraints of a list operation. All fields in the SecurityGateway message are supported. For example, the following query will return the SecurityGateway with displayName "test-security-gateway" For more information, please refer to https://google.aip.dev/160.

func (*ProjectsLocationsSecurityGatewaysListCall) Header ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysListCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsSecurityGatewaysListCall) IfNoneMatch ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysListCall) IfNoneMatch(entityTag string) *ProjectsLocationsSecurityGatewaysListCall

IfNoneMatch sets an optional parameter which makes the operation fail if the object's ETag matches the given value. This is useful for getting updates only after the object has changed since the last request.

func (*ProjectsLocationsSecurityGatewaysListCall) OrderBy ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysListCall) OrderBy(orderBy string) *ProjectsLocationsSecurityGatewaysListCall

OrderBy sets the optional parameter "orderBy": Specifies the ordering of results. See Sorting order (https://cloud.google.com/apis/design/design_patterns#sorting_order) for more information.

func (*ProjectsLocationsSecurityGatewaysListCall) PageSize ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysListCall) PageSize(pageSize int64) *ProjectsLocationsSecurityGatewaysListCall

PageSize sets the optional parameter "pageSize": The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's next_page_token to determine if there are more instances left to be queried.

func (*ProjectsLocationsSecurityGatewaysListCall) PageToken ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysListCall) PageToken(pageToken string) *ProjectsLocationsSecurityGatewaysListCall

PageToken sets the optional parameter "pageToken": The next_page_token value returned from a previous ListSecurityGatewayRequest, if any.

func (*ProjectsLocationsSecurityGatewaysListCall) Pages ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysListCall) Pages(ctx context.Context, f func(*GoogleCloudBeyondcorpSecuritygatewaysV1ListSecurityGatewaysResponse) error) error

Pages invokes f for each page of results. A non-nil error returned from f will halt the iteration. The provided context supersedes any context provided to the Context method.

type ProjectsLocationsSecurityGatewaysPatchCall ¶
added in v0.200.0
type ProjectsLocationsSecurityGatewaysPatchCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSecurityGatewaysPatchCall) Context ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysPatchCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysPatchCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSecurityGatewaysPatchCall) Do ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysPatchCall) Do(opts ...googleapi.CallOption) (*GoogleLongrunningOperation, error)

Do executes the "beyondcorp.projects.locations.securityGateways.patch" call. Any non-2xx status code is an error. Response headers are in either *GoogleLongrunningOperation.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSecurityGatewaysPatchCall) Fields ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysPatchCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysPatchCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSecurityGatewaysPatchCall) Header ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysPatchCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

func (*ProjectsLocationsSecurityGatewaysPatchCall) RequestId ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysPatchCall) RequestId(requestId string) *ProjectsLocationsSecurityGatewaysPatchCall

RequestId sets the optional parameter "requestId": An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request timed out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

func (*ProjectsLocationsSecurityGatewaysPatchCall) UpdateMask ¶
added in v0.200.0
func (c *ProjectsLocationsSecurityGatewaysPatchCall) UpdateMask(updateMask string) *ProjectsLocationsSecurityGatewaysPatchCall

UpdateMask sets the optional parameter "updateMask": Mutable fields include: display_name, hubs.

type ProjectsLocationsSecurityGatewaysService ¶
added in v0.200.0
type ProjectsLocationsSecurityGatewaysService struct {
	Applications *ProjectsLocationsSecurityGatewaysApplicationsService
	// contains filtered or unexported fields
}
func NewProjectsLocationsSecurityGatewaysService ¶
added in v0.200.0
func NewProjectsLocationsSecurityGatewaysService(s *Service) *ProjectsLocationsSecurityGatewaysService
func (*ProjectsLocationsSecurityGatewaysService) Create ¶
added in v0.200.0
func (r *ProjectsLocationsSecurityGatewaysService) Create(parent string, googlecloudbeyondcorpsecuritygatewaysv1securitygateway *GoogleCloudBeyondcorpSecuritygatewaysV1SecurityGateway) *ProjectsLocationsSecurityGatewaysCreateCall

Create: Creates a new Security Gateway in a given project and location.

parent: The resource project name of the SecurityGateway location using the form: `projects/{project_id}/locations/{location_id}`.
func (*ProjectsLocationsSecurityGatewaysService) Delete ¶
added in v0.200.0
func (r *ProjectsLocationsSecurityGatewaysService) Delete(name string) *ProjectsLocationsSecurityGatewaysDeleteCall

Delete: Deletes a single SecurityGateway.

name: BeyondCorp SecurityGateway name using the form: `projects/{project_id}/locations/{location_id}/securityGateways/{security_g ateway_id}`.
func (*ProjectsLocationsSecurityGatewaysService) Get ¶
added in v0.200.0
func (r *ProjectsLocationsSecurityGatewaysService) Get(name string) *ProjectsLocationsSecurityGatewaysGetCall

Get: Gets details of a single SecurityGateway.

name: The resource name of the PartnerTenant using the form: `projects/{project_id}/locations/{location_id}/securityGateway/{security_ga teway_id}`.
func (*ProjectsLocationsSecurityGatewaysService) GetIamPolicy ¶
added in v0.202.0
func (r *ProjectsLocationsSecurityGatewaysService) GetIamPolicy(resource string) *ProjectsLocationsSecurityGatewaysGetIamPolicyCall

GetIamPolicy: Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

resource: REQUIRED: The resource for which the policy is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsSecurityGatewaysService) List ¶
added in v0.200.0
func (r *ProjectsLocationsSecurityGatewaysService) List(parent string) *ProjectsLocationsSecurityGatewaysListCall

List: Lists SecurityGateways in a given project and location.

parent: The parent location to which the resources belong. `projects/{project_id}/locations/{location_id}/`.
func (*ProjectsLocationsSecurityGatewaysService) Patch ¶
added in v0.200.0
func (r *ProjectsLocationsSecurityGatewaysService) Patch(name string, googlecloudbeyondcorpsecuritygatewaysv1securitygateway *GoogleCloudBeyondcorpSecuritygatewaysV1SecurityGateway) *ProjectsLocationsSecurityGatewaysPatchCall

Patch: Updates the parameters of a single SecurityGateway.

- name: Identifier. Name of the resource.

func (*ProjectsLocationsSecurityGatewaysService) SetIamPolicy ¶
added in v0.205.0
func (r *ProjectsLocationsSecurityGatewaysService) SetIamPolicy(resource string, googleiamv1setiampolicyrequest *GoogleIamV1SetIamPolicyRequest) *ProjectsLocationsSecurityGatewaysSetIamPolicyCall

SetIamPolicy: Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

resource: REQUIRED: The resource for which the policy is being specified. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
func (*ProjectsLocationsSecurityGatewaysService) TestIamPermissions ¶
added in v0.202.0
func (r *ProjectsLocationsSecurityGatewaysService) TestIamPermissions(resource string, googleiamv1testiampermissionsrequest *GoogleIamV1TestIamPermissionsRequest) *ProjectsLocationsSecurityGatewaysTestIamPermissionsCall

TestIamPermissions: Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

resource: REQUIRED: The resource for which the policy detail is being requested. See Resource names (https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
type ProjectsLocationsSecurityGatewaysSetIamPolicyCall ¶
added in v0.205.0
type ProjectsLocationsSecurityGatewaysSetIamPolicyCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSecurityGatewaysSetIamPolicyCall) Context ¶
added in v0.205.0
func (c *ProjectsLocationsSecurityGatewaysSetIamPolicyCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysSetIamPolicyCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSecurityGatewaysSetIamPolicyCall) Do ¶
added in v0.205.0
func (c *ProjectsLocationsSecurityGatewaysSetIamPolicyCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1Policy, error)

Do executes the "beyondcorp.projects.locations.securityGateways.setIamPolicy" call. Any non-2xx status code is an error. Response headers are in either *GoogleIamV1Policy.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSecurityGatewaysSetIamPolicyCall) Fields ¶
added in v0.205.0
func (c *ProjectsLocationsSecurityGatewaysSetIamPolicyCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysSetIamPolicyCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSecurityGatewaysSetIamPolicyCall) Header ¶
added in v0.205.0
func (c *ProjectsLocationsSecurityGatewaysSetIamPolicyCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsSecurityGatewaysTestIamPermissionsCall ¶
added in v0.202.0
type ProjectsLocationsSecurityGatewaysTestIamPermissionsCall struct {
	// contains filtered or unexported fields
}
func (*ProjectsLocationsSecurityGatewaysTestIamPermissionsCall) Context ¶
added in v0.202.0
func (c *ProjectsLocationsSecurityGatewaysTestIamPermissionsCall) Context(ctx context.Context) *ProjectsLocationsSecurityGatewaysTestIamPermissionsCall

Context sets the context to be used in this call's Do method.

func (*ProjectsLocationsSecurityGatewaysTestIamPermissionsCall) Do ¶
added in v0.202.0
func (c *ProjectsLocationsSecurityGatewaysTestIamPermissionsCall) Do(opts ...googleapi.CallOption) (*GoogleIamV1TestIamPermissionsResponse, error)

Do executes the "beyondcorp.projects.locations.securityGateways.testIamPermissions" call. Any non-2xx status code is an error. Response headers are in either *GoogleIamV1TestIamPermissionsResponse.ServerResponse.Header or (if a response was returned at all) in error.(*googleapi.Error).Header. Use googleapi.IsNotModified to check whether the returned error was because http.StatusNotModified was returned.

func (*ProjectsLocationsSecurityGatewaysTestIamPermissionsCall) Fields ¶
added in v0.202.0
func (c *ProjectsLocationsSecurityGatewaysTestIamPermissionsCall) Fields(s ...googleapi.Field) *ProjectsLocationsSecurityGatewaysTestIamPermissionsCall

Fields allows partial responses to be retrieved. See https://developers.google.com/gdata/docs/2.0/basics#PartialResponse for more details.

func (*ProjectsLocationsSecurityGatewaysTestIamPermissionsCall) Header ¶
added in v0.202.0
func (c *ProjectsLocationsSecurityGatewaysTestIamPermissionsCall) Header() http.Header

Header returns a http.Header that can be modified by the caller to add headers to the request.

type ProjectsLocationsService ¶
type ProjectsLocationsService struct {
	AppConnections *ProjectsLocationsAppConnectionsService

	AppConnectors *ProjectsLocationsAppConnectorsService

	AppGateways *ProjectsLocationsAppGatewaysService

	Operations *ProjectsLocationsOperationsService

	SecurityGateways *ProjectsLocationsSecurityGatewaysService
	// contains filtered or unexported fields
}
func NewProjectsLocationsService ¶
func NewProjectsLocationsService(s *Service) *ProjectsLocationsService
func (*ProjectsLocationsService) Get ¶
func (r *ProjectsLocationsService) Get(name string) *ProjectsLocationsGetCall

Get: Gets information about a location.

- name: Resource name for the location.

func (*ProjectsLocationsService) List ¶
func (r *ProjectsLocationsService) List(name string) *ProjectsLocationsListCall

List: Lists information about the supported locations for this service. This method can be called in two ways: * **List all public locations:** Use the path `GET /v1/locations`. * **List project-visible locations:** Use the path `GET /v1/projects/{project_id}/locations`. This may include public locations as well as private or other locations specifically visible to the project.

- name: The resource that owns the locations collection, if applicable.

type ProjectsService ¶
type ProjectsService struct {
	Locations *ProjectsLocationsService
	// contains filtered or unexported fields
}
func NewProjectsService ¶
func NewProjectsService(s *Service) *ProjectsService
type Service ¶
type Service struct {
	BasePath  string // API endpoint base URL
	UserAgent string // optional additional User-Agent fragment

	Organizations *OrganizationsService

	Projects *ProjectsService
	// contains filtered or unexported fields
}
func
New
DEPRECATED
func NewService ¶
func NewService(ctx context.Context, opts ...option.ClientOption) (*Service, error)

NewService creates a new Service.

type Tunnelv1ProtoTunnelerError ¶
type Tunnelv1ProtoTunnelerError struct {
	// Err: Original raw error
	Err string `json:"err,omitempty"`
	// Retryable: retryable isn't used for now, but we may want to reuse it in the
	// future.
	Retryable bool `json:"retryable,omitempty"`
	// ForceSendFields is a list of field names (e.g. "Err") to unconditionally
	// include in API requests. By default, fields with empty or default values are
	// omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "Err") to include in API requests
	// with the JSON null value. By default, fields with empty values are omitted
	// from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Tunnelv1ProtoTunnelerError: TunnelerError is an error proto for errors returned by the connection manager.

func (Tunnelv1ProtoTunnelerError) MarshalJSON ¶
func (s Tunnelv1ProtoTunnelerError) MarshalJSON() ([]byte, error)
type Tunnelv1ProtoTunnelerInfo ¶
type Tunnelv1ProtoTunnelerInfo struct {
	// BackoffRetryCount: backoff_retry_count stores the number of times the
	// tunneler has been retried by tunManager for current backoff sequence. Gets
	// reset to 0 if time difference between 2 consecutive retries exceeds
	// backoffRetryResetTime.
	BackoffRetryCount int64 `json:"backoffRetryCount,omitempty"`
	// Id: id is the unique id of a tunneler.
	Id string `json:"id,omitempty"`
	// LatestErr: latest_err stores the Error for the latest tunneler failure. Gets
	// reset everytime the tunneler is retried by tunManager.
	LatestErr *Tunnelv1ProtoTunnelerError `json:"latestErr,omitempty"`
	// LatestRetryTime: latest_retry_time stores the time when the tunneler was
	// last restarted.
	LatestRetryTime string `json:"latestRetryTime,omitempty"`
	// TotalRetryCount: total_retry_count stores the total number of times the
	// tunneler has been retried by tunManager.
	TotalRetryCount int64 `json:"totalRetryCount,omitempty"`
	// ForceSendFields is a list of field names (e.g. "BackoffRetryCount") to
	// unconditionally include in API requests. By default, fields with empty or
	// default values are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-ForceSendFields for more
	// details.
	ForceSendFields []string `json:"-"`
	// NullFields is a list of field names (e.g. "BackoffRetryCount") to include in
	// API requests with the JSON null value. By default, fields with empty values
	// are omitted from API requests. See
	// https://pkg.go.dev/google.golang.org/api#hdr-NullFields for more details.
	NullFields []string `json:"-"`
}

Tunnelv1ProtoTunnelerInfo: TunnelerInfo contains metadata about tunneler launched by connection manager.

func (Tunnelv1ProtoTunnelerInfo) MarshalJSON ¶
func (s Tunnelv1ProtoTunnelerInfo) MarshalJSON() ([]byte, error)
 Source Files ¶
View all Source files
beyondcorp-gen.go
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
